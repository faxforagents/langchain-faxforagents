# Changelog

## Unreleased

The SDK dependency is `faxforagents>=0.2.3,<0.5`. The range ended below 0.3 and shut out the current SDK.
The tests pass against SDK 0.2.3, 0.3.2 and the 0.4.0 branch. No tool changed.

## 0.1.0 (2026-11-04)

Prepared the LangChain and LangGraph package with 15 canonical tools.
Added synchronous and asynchronous SDK calls with typed arguments.
Required caller-controlled idempotency keys for mutations and approval IDs for live sends.
Marked SDK response data as untrusted and returned structured failures.
Added sandbox examples, fake SDK tests, and the integration listing draft.
