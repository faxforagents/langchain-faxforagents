# Changelog

## 0.2.0 (2026-11-14)

The package has the 17 tools of the hosted MCP server at API 1.20.3. It had 15.

New tool `request_card_payment`: a person pays for one quoted fax by card, with no wallet balance.
It returns a payment link in `status_url`. It takes no card details and cannot pay.
New tool `get_card_payment_status`: the order, its next step, and the fax once it was released.
Both results leave out the order's status token, the payer's email address and the card's brand and last four digits.
A live card order requires `approval_id`, the same rule this package applies to live sends.

`quote_fax` takes `quality`, `sender_name`, `from_number` and `delete_after_send`.
`list_faxes` takes `idempotency_key` as a filter.
The local guide has the sections `one_time` and `going_live`.
Tool descriptions and annotations follow the hosted server. `cancel_fax` is now marked idempotent.

The SDK dependency is `faxforagents>=0.11.2,<0.12`, so this release needs SDK 0.11.2 or a later 0.11 release.
0.1.0 accepted only SDK versions below 0.3, which shut out the current SDK.
SDK 0.11.2 has every call and argument the tools use.
If an older SDK is installed anyway, those calls answer `sdk_upgrade_required` and send no request.
The tests pass against SDK 0.11.2, and the lock file uses it.

## 0.1.0 (2026-11-04)

Prepared the LangChain and LangGraph package with 15 canonical tools.
Added synchronous and asynchronous SDK calls with typed arguments.
Required caller-controlled idempotency keys for mutations and approval IDs for live sends.
Marked SDK response data as untrusted and returned structured failures.
Added sandbox examples, fake SDK tests, and the integration listing draft.
