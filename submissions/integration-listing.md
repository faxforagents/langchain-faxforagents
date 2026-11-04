# Integration listing draft

This draft follows the [LangChain listing issue template](https://github.com/langchain-ai/docs/blob/main/.github/ISSUE_TEMPLATE/06-integration-submission.yml), fetched on 2026-11-04.
The package and repository are not published yet.
Submit only after both are public and the documented installation works.

Issue title: `[integration]: langchain-faxforagents`

## Display or class name

FaxForAgentsToolkit

## Language

Python

## Component type

tools

## PyPI package name

langchain-faxforagents

## npm package name

Leave blank.

## Docs URL

https://github.com/faxforagents/langchain-faxforagents/blob/main/README.md

## Source repository

faxforagents/langchain-faxforagents

## Short provider description

Fax for Agents provides fax preparation, quotes, human approval requests, delivery checks, inbox reading, and extraction through LangChain tools.

## Capability flags (optional)

Leave blank. The template reserves these flags for chat models and vector stores.

## Confirmations

- [ ] The package is already published on PyPI and/or npm.

This confirmation remains unchecked until publication succeeds.

## Ben's steps

- [ ] Review the package, tests, and distribution contents.
- [ ] Sign in to PyPI and verify the account email.
- [ ] Enable required two-factor authentication and store recovery codes privately.
- [ ] Configure a publishing credential through approved secret storage.
- [ ] For an initial API-token upload, use an account token if the project does not exist yet.
- [ ] After the first release, replace that token with a project-scoped token.
- [ ] Recheck package name availability immediately before publication.
- [ ] Create the public repository through the normal repository review process.
- [ ] Publish the reviewed wheel and source distribution when ready.
- [ ] Install from PyPI in a clean environment and run an authenticated sandbox check.
- [ ] Verify the README URL works publicly and describes the released version.
- [ ] Sign in to GitHub and submit the listing issue with the fields above.
- [ ] Check the publication confirmation only after the PyPI package resolves.
- [ ] Review the listing generated after a maintainer applies `integration-run`.

The PyPI JSON endpoint returned HTTP 404 for `langchain-faxforagents` on 2026-11-04.
That check found no existing project. It does not reserve the name or guarantee acceptance.
Credential instructions follow [PyPI's API-token help](https://docs.pypi.org/publishing/publishing-to-pypi/#using-an-api-token) and [two-factor help](https://docs.pypi.org/your-account/two-factor-authentication/).

Use the [listing issue form](https://github.com/langchain-ai/docs/issues/new?template=06-integration-submission.yml) after publishing.
The [publication guide](https://docs.langchain.com/oss/python/contributing/publish-langchain) directs new listings through that form.
Do not open a manual listing pull request unless a maintainer asks.
Hosted guides require 50,000 monthly downloads or maintainer-featured status.
Expect an external listing linked to this repository's documentation until eligible.

## Implementation references

- [Contributing integrations](https://docs.langchain.com/oss/python/contributing/integrations-langchain).
- [Implementing integrations](https://docs.langchain.com/oss/python/contributing/implement-langchain).
- [BaseTool reference](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool).
- [BaseToolkit reference](https://reference.langchain.com/python/langchain-core/tools/base/BaseToolkit).
- [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart).

These sources were fetched on 2026-11-04.
The publication guide and issue template provide the current listing procedure.
Their issue-based procedure supersedes older overview text suggesting a manual documentation pull request.
