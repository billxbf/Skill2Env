# Billing Response Semantics

All invocation syntax, validation, supported combinations, and bounds live in [cli.md](cli.md). This document only defines how to interpret billing responses.

## Billing-Cycle Summary

The response contains `period`, `chargeType`, `currency`, `cycles[]`, and `totals`. This is the only amount contract that requires `pretaxAmount`, `tax`, and `aftertaxAmount`; display those returned fields for each requested cycle or total. Never derive a missing value.

The returned period must match the requested billing range. A mismatch is a query-contract error, and those cycles must not be presented as the requested period.

## Cost Breakdown

The response shape depends on whether the requested range spans multiple granularity buckets:

- A flat response contains `currency`, `period`, `rows[]`, `totalAmount`, and `totalRows`.
- A sliced response contains `currency`, `dateRange`, `granularity`, and `slices[]`; each slice has `period`, `rows[]`, and `totalAmount`.

In both shapes each row has `groupKey`, `groupLabel`, and `amount`. Display only the monetary fields actually returned. Exclude `groupKey=__tax__` from model rankings and show that row's `amount` separately as tax.

At either the flat or slice level, `totalAmount` is the subtotal of the returned, already top-truncated rows, including the returned tax row when present. It is not the untruncated full total. In a flat response, compare `totalRows` with the count of returned non-tax rows. If `totalRows` is larger, classify the result as `partial` and state that `totalAmount` covers only the returned subset. Any requested top limit also makes the completeness claim `partial` unless the response proves that no rows were omitted.

## Spending Limit

Treat the spending-limit response as read-only configuration. Present only fields actually returned; do not claim it contains current spend unless such a field is present.
