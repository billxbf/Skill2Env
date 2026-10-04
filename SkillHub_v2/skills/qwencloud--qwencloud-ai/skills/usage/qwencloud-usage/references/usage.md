# Usage Response Semantics

All invocation syntax, validation, windowing, and pagination rules live in [cli.md](cli.md). This document only defines how to interpret usage responses.

## Aggregate Usage

An aggregate response has `period: { from, to }` and these product branches:

- `free_tier[]`: each entry has `model_id` and either `quota: null` or a quota object with `remaining`, `total`, `unit`, `used_pct`, `status`, and `resetDate`.
- `token_plan`: when subscribed, includes `subscribed`, `planName`, `status`, `totalCredits`, `remainingCredits`, `usedPct`, and `resetDate`; when explicitly unsubscribed, it contains at least `{ "subscribed": false }` and no other field should be assumed.
- `coding_plan`: when subscribed, includes `subscribed`, `plan`, and request-count windows named `per_5h`, `weekly`, and `monthly`; otherwise it is `{ "subscribed": false }`.
- `pay_as_you_go`: contains model entries with `model_id`, `usage`, `cost`, and `currency`, plus a total cost and currency.

For Free Tier, inspect status before using `remaining`:

- Only `valid` is available and may contribute to an available-quota total.
- `expire` is expired, even if `remaining` is positive.
- `exhaust` is exhausted.
- A null quota or unknown status has unknown availability and must be excluded from available-quota totals.

Token Plan base quota uses decimal Credits. Display `remainingCredits` and `totalCredits` at their full returned precision, following the [Output Contract](../SKILL.md#product-semantics); there is no per-model Credit breakdown. Keep these Credits separate from Coding Plan request counts and PAYG usage.

`token_plan.resetDate` is the next credit refresh date when present; if absent, the refresh date is unknown.

PAYG exposes total usage only, without an input/output split.

## Per-Model Breakdown

The per-model breakdown is PAYG-only history. An empty or zero result says nothing about Free Tier, Token Plan, or Coding Plan consumption.

For TTS, request-log `characters` totals and breakdown aggregates are known to disagree, and breakdown rows can vary in shape. Present the fields actually returned by each source, label their scopes, and mark a cross-source comparison `partial`; do not reconcile the values or derive one from the other.

## Request Logs

The response top level contains `totalCount`, `page`, `pageSize`, `period`, and `items`. Each item contains:

| Field | Meaning |
|---|---|
| `requestId` | Correlation with server-side traces |
| `model` | Called model |
| `createdAt` | ISO 8601 call timestamp |
| `statusCode` | Numeric HTTP-style outcome; `0` means cancellation |
| `durationMs` | Total latency |
| `firstOutputDurationMs` | Time to first token; `0` when not applicable |
| `errorCode` | Optional failure detail; it may be null on failed as well as successful calls |
| `usages` | Per-request `key`/`value` consumption pairs; empty for failed or cancelled calls |

Use `statusCode` as the authoritative outcome: `2xx` is successful, `4xx` and `5xx` are failed, and `0` is cancelled. Use a non-null `errorCode` only as supplementary detail. When it is null on a failed request, report that the detailed reason is unavailable; never treat the request as successful.

Observed usage keys include:

- Text/LLM: `total`, `input`, and `output` token counts.
- Image generation: `output_image` count.
- TTS: `characters` count.
- ASR: `duration` in seconds.

A request-ID lookup needs no user-supplied time range; follow the direct lookup rules in [cli.md](cli.md). Use the returned period, when present, as the authoritative coverage label. An empty request-ID result means only that this query returned no matching log; never invent a searched range or turn it into a global nonexistence claim.

Logs do not currently cover Token Plan API-key traffic. Therefore an empty item list may be classified as `empty` only after the CLI reference's safe pagination and coverage checks have completed, and only for traffic the endpoint covers. For a Token Plan request, say that the log result is inconclusive and do not claim that no call occurred. If the traffic source is mixed or unknown, describe the result as partial coverage even when items are present; never present it as the account's complete request history. If before-and-after Credit snapshots or another server-side trace are available, use them only as supporting evidence and keep request-level attribution `partial`.
