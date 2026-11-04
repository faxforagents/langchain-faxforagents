"""Run both agent loops with a scripted model and fake SDK tools."""

import importlib.util
from pathlib import Path

import pytest
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from pydantic import PrivateAttr

pytest.importorskip("langchain")
pytest.importorskip("langgraph")

from test_tools import DOC, KEY, QUOTE, TEST_KEY, FakeSDK

from langchain_faxforagents import tools as module


class ScriptedModel(BaseChatModel):
    _step: int = PrivateAttr(default=0)

    @property
    def _llm_type(self):
        return "scripted-fax-test"

    def bind_tools(self, tools, **kwargs):
        assert {tool.name for tool in tools} == {"prepare_fax", "quote_fax"}
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        calls = [
            {
                "name": "prepare_fax",
                "args": {"text": "Example", "idempotency_key": KEY + "-prepare"},
                "id": "prepare",
            },
            {
                "name": "quote_fax",
                "args": {
                    "document_id": DOC,
                    "to": "+15550000001",
                    "idempotency_key": KEY + "-quote",
                },
                "id": "quote",
            },
        ]
        if self._step < 2:
            message = AIMessage(content="", tool_calls=[calls[self._step]])
        else:
            assert len([m for m in messages if isinstance(m, ToolMessage)]) == 2
            message = AIMessage(content="Quoted. Nothing sent.")
        self._step += 1
        return ChatResult(generations=[ChatGeneration(message=message)])


@pytest.mark.parametrize("example", ["langchain_agent", "langgraph_agent"])
def test_agent_loop(example, monkeypatch):
    fake = FakeSDK()
    fake.responses["documents.create"] = {"id": DOC}
    fake.responses["quotes.create"] = {"id": QUOTE, "amount_micro": 0}
    monkeypatch.setattr(module, "Client", fake.factory())
    monkeypatch.setenv("FAXFORAGENTS_API_KEY", TEST_KEY)
    path = Path(__file__).parents[1] / "examples" / f"{example}.py"
    spec = importlib.util.spec_from_file_location(example, path)
    imported = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(imported)
    graph = imported.build_agent(ScriptedModel())
    result = graph.invoke({"messages": [("user", "Prepare and quote a sandbox fax.")]})
    assert result["messages"][-1].content == "Quoted. Nothing sent."
    assert [call[1] for call in fake.calls] == ["documents.create", "quotes.create"]
    assert fake.calls[1][2]["to"] == "+15550000001"
