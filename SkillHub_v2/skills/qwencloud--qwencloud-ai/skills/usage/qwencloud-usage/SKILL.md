---
name: qwencloud-usage
description: "Manage account auth, query usage, billing, and subscriptions. Use for: login, logout, check usage, view billing summary/breakdown, spending limit, free tier quota, Token Plan status, coding plan status, pay-as-you-go costs, call logs (which requests failed, 4xx/5xx errors, request latency, recent models called, request-id lookup), subscription orders, team seats. Skip for: model browsing, payment methods (use qwencloud-payment)."
---

# QwenCloud Usage

Use this skill for account authentication, usage, billing, call logs, quotas, subscriptions, orders, seats, and the PAYG spending limit. Never fabricate or mock account data.

## Workflow

1. Before running anything, read [references/cli.md](references/cli.md). It is the only source for installation, authentication flow, commands, arguments, pagination, output modes, and exit handling.
2. Read only the result-semantics reference relevant to the request:
   - Usage summary, free tier, PAYG, model breakdown, or request logs: [references/usage.md](references/usage.md)
   - Billing cycles, cost breakdown, or spending limit: [references/billing.md](references/billing.md)
   - Subscription status, orders, or seats: [references/subscriptions.md](references/subscriptions.md)
   - Login, logout, expired credentials, or authentication events: [references/authentication.md](references/authentication.md)
3. For an exact requestId lookup, query directly without adding `--from`, `--to`, or `--period`, or asking the user for a date. Add time filters only when the user explicitly requests them; see [references/cli.md](references/cli.md).
4. Interpret and display the result according to the Output Contract below.

## Output Contract

### Format and Presentation

Follow the output-mode rules in the CLI reference. Present only the human-readable information relevant to the user's question, and place optional analysis after the result.

Do not display Coding Plan in user-facing output. Omit `coding_plan`, `codingPlanStatus`, and their child fields, including "not subscribed" placeholders, even when returned by the CLI.

### Result Rules

- Classify the result as `success`, `partial`, `empty`, `confirmation_required`, or `error`.
- If a top-N limit omits rows, pagination is unfinished, or the CLI reference's integrity checks fail, use `partial`; never imply the data is complete.
- For Free Tier, show every returned model when the user asks for all quotas. If the answer shows only a subset, state the shown/total model count, mark it `partial`, and include a complete command from [references/cli.md](references/cli.md) to view all free-tier quotas. An offer to show more is not a substitute for that command.
- When two supported commands return conflicting values for what appears to be the same record, show the source and scope of each value and mark the result `partial`. Never silently choose one, merge them, or invent a reconciliation.

### Billing and Subscription Data

- Use the currency returned by the operation and never convert it. For the billing-cycle summary only, display its `pretaxAmount`, `tax`, and `aftertaxAmount` values.
- For a cost breakdown, display only the returned `rows[].amount`, the applicable flat-response or slice-level `totalAmount`, and `currency`. For subscription status or orders, display only the amount and currency fields actually present. Never synthesize missing pretax, tax, after-tax, or currency fields.
- In cost breakdowns, omit `groupKey=__tax__` from model rankings and display that row's returned amount separately as tax.
- Calculate available Team seats only from `seatSummary.groups[]`: use `max(seats - assigned, 0)` for each group, then sum them. Do not derive current capacity from the historical seat-instance list.
- Do not recompute returned dates or monetary amounts. Validate the response and apply the presentation rules above.
- When presenting billing or subscription data, always append: “Final amounts are subject to the console billing statement.”

### Product Semantics

- Token Plan quota and balances use decimal Credits. Preserve the full precision returned by JSON for remaining and total Credits, whether encoded as numbers or numeric strings; never round, truncate, or abbreviate them. For example, display `63028.84805624` as `63028.84805624`, not `63,029`. This applies to usage summaries, subscription quota, tiers, seats, and credit packs; there is no per-model Credit breakdown.
- Use exact values from the same quota scope for consumption comparisons. A rounded usage percentage of zero does not prove that no Credits were consumed; do not infer unused status or refund eligibility from rounded displays.
- Coding Plan uses aggregate request counts in `per_5h`, `weekly`, and `monthly` windows; it has no per-model breakdown. If not subscribed, its branch is `{ "subscribed": false }`.
- PAYG exposes total usage only, without an input/output split.
- The per-model breakdown is PAYG-only. A zero or empty breakdown says nothing about Free Tier, Token Plan, or Coding Plan consumption.
- A usage summary has `period: { from, to }` and these product branches:
  - `free_tier[]`: `model_id` plus either `quota: null` or `quota: { remaining, total, unit, used_pct, status, resetDate }`. Only `status=valid` is usable and may contribute to an available-quota total. Treat `expire` as expired and `exhaust` as exhausted even when `remaining` is positive; an unknown status or `quota: null` has unknown availability.
  - `token_plan`: when subscribed, `subscribed`, `planName`, `status`, `totalCredits`, `remainingCredits`, `usedPct`, and `resetDate`; otherwise at least `{ "subscribed": false }`. `resetDate` is the next credit refresh date when present; if absent, report the refresh date as unknown. When subscription auto-renewal is off, note that the plan expires after this date.
  - `coding_plan`: when subscribed, `subscribed`, `plan`, and `windows` containing `per_5h`, `weekly`, and `monthly`, each with `remaining`, `total`, and `used_pct`; otherwise `{ "subscribed": false }`.
  - `pay_as_you_go`: `models[]` entries with `model_id`, `usage`, `cost`, and `currency`, plus `total: { cost, currency }`.
