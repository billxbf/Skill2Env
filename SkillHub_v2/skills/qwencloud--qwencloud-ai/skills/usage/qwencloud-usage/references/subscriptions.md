# Subscription Response Semantics

All invocation syntax, validation, and pagination rules live in [cli.md](cli.md). This document only defines how to interpret subscription responses.

## Aggregate Status

The aggregate response does not provide stable `subscribed` or `edition` fields. Do not infer “not subscribed,” Personal, Team, or renewability from an all-null combination, `renewable: null`, or `remainingDays: null`; report only the observable fields and say the unavailable state is unknown. A numeric `remainingDays`, including zero, may be displayed as returned, while a null value is unknown. For an explicit Coding Plan subscription decision, prefer the aggregate usage response's `coding_plan.subscribed` when that branch is available.

The Token Plan branch can include:

- `plan`, `period: { start, end }`, `quota: { remaining, total, usedPct }`, `autoRenew`, `renewable`, and `remainingDays`;
- `seatTiers[]` with `specType`, `seats`, `totalCredits`, `remainingCredits`, `usedPct`, and `nextCycleFlushTime`;
- `creditPacks[]` with `instanceId`, total and remaining Credits, and `expiresAt`;
- `codingPlanStatus`, `recentOrders[]`, and `diagnostics[]`.

Base quota, tier, seat-summary, and credit-pack balances are decimal Credits. Preserve their full returned precision, including numeric strings, following the [Output Contract](../SKILL.md#product-semantics). Credit packs are add-ons consumed independently of the base-plan quota, so show them as supplementary balances. A null `codingPlanStatus` means this response supplied no Coding Plan detail; do not turn that alone into a subscription conclusion. An empty `creditPacks` array means no add-on balance was returned.

Do not use `plan` as an edition identifier. For `renewable`, report an explicit boolean or object when present; null means unknown. Do not promise that the user can renew based only on `remainingDays` or `autoRenew`.

In the aggregate response, `autoRenew` is a top-level boolean:

- When true, the subscription renews automatically.
- When false, describe `period.end` as the expiry date and state that the plan lapses unless renewed.
- When null, the state is unknown; do not promise renewal or a guaranteed reset.

Coding Plan uses request-count windows named `per_5h`, `weekly`, and `monthly`, each with remaining, total, and used percentage. Keep these request counts separate from Token Plan Credits.

## Orders

Each full order row provides `orderId`, `orderType`, `orderTime`, `amount`, `currency`, and `status`. Display only the monetary fields actually present and do not invent tax components.

The dedicated order history is filtered to Token Plan products, while `recentOrders` in aggregate status currently has a broader or different filter and does not carry the same currency detail. They are not interchangeable complete histories. Label the source and scope when showing either list. If the same `orderId` has different amounts, show both returned values and currency when present, mark the result `partial`, and report the inconsistency without choosing or combining them.

## Token Plan Team Status

On success, the Team status response contains `product`, `period`, an `autoRenew` object or null, a `renewable` object or null, and `seatSummary`. The summary groups contain `specType`, `seats`, `assigned`, Credit values, `unit`, and `nextCycleFlushTime`; the total contains aggregate seats and Credit values.

Use non-empty `seatSummary.groups[]` with real, non-empty `specType` values as the source of truth for current Team capacity. Calculate available seats per group as `max(seats - assigned, 0)` and then sum the group results. The `product` label is fixed by affected clients and is not edition evidence.

In this response, `autoRenew` is an object such as `{ "enabled": true, "period": 1, "periodUnit": "M" }`:

- When `enabled` is true, the subscription renews automatically.
- When it is false, the group time may be null; describe `period.end` as the expiry date after which the plan lapses unless renewed.
- When the object is null, do not describe any present date as a guaranteed reset.

The Team endpoints do not make the aggregate response a reliable edition detector. Do not guess Personal or Team from null fields or the fixed product label. An unsupported-edition error establishes only that the Team endpoint is unavailable; it does not prove Personal unless the response explicitly says so. Provide a management URL only when returned by the service.

## Team Seat Instances

The seat-instance response contains `page`, `filter`, `items`, and `diagnostics`. Treat it as a historical instance list, not as the source for available capacity.

Only `NORMAL` is established as a current instance state. `REFUNDED` and `RELEASE` are historical and must not be counted as current. Treat every other status, including `CREATING`, `LIMIT`, and `STOP`, as unknown unless an authoritative contract establishes its meaning; report the raw status and exclude it from current-seat counts. Only describe the result as complete after the pagination checks in the CLI reference succeed.
