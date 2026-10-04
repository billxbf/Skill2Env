# GraphQL cost-point metering - formulas, accounting, and client traps

The cost-based metering model in concrete, citable detail: the two dominant formulas (GitHub, Shopify), the smaller named variants, and the traps a policy must design around. Structural query guards (depth ceilings, persisted queries, complexity rejection as schema design) belong to `samber/developer-platform-skills@public-graphql-api-design`; this file covers the pricing and budget policy.

## Why per-request counting fails GraphQL

A REST-style "N requests per minute" treats a query fetching one scalar the same as one fetching hundreds of nested objects, despite wildly different server cost. The cost model prices the _query_, not the _request_: every query gets a computed cost, and the limit is a budget of points per window.

## GitHub GraphQL (v4)

- A connection field's cost is its `first`/`last` argument value ÷ 100, rounded to the nearest whole number, minimum 1 per connection field.
- Schema guards make it ungameable: every connection must supply `first`/`last` in 1–100, and a single call cannot request more than 500,000 total nodes.
- The budget is introspectable mid-session: `rateLimit { limit cost remaining resetAt }` - and querying it costs nothing. A transparency mechanism distinct from a response header, worth copying.
- Budgets: 5,000 points/hr for users, 10,000/hr for Enterprise-owned apps; GitHub App installations scale (50 points/hr per repo and per user above 20, capped at 12,500).
- **Client trap**: exceeding the primary GraphQL limit returns **HTTP 200 with an error in the body** and `x-ratelimit-remaining: 0` - not a 429. A status-code-only client silently treats it as success.

## Shopify Admin API (GraphQL)

Official source: `shopify.dev/docs/api/usage/limits`. Calculated query cost spent against a leaky bucket (50 points/s restore, 1,000-point bucket on Standard; 100/s and 2,000 on Plus - but see the caveat below).

- **Field cost rules**: Scalar = 0, Enum = 0, Object = 1, Connection = sized by its `first`/`last` arguments, Interface/Union = max of its possible selections, **Mutation = 10**. Shopify reserves the right to set manual per-field costs beyond the general rule.
- **Pre-charge then refund**: the bucket must hold the full `requestedQueryCost` (static worst-case estimate) _before_ execution or the query is rejected outright; after execution the difference vs `actualQueryCost` is refunded. Per-response accounting under `extensions.cost`:

```json
{
  "requestedQueryCost": 101,
  "actualQueryCost": 46,
  "throttleStatus": {
    "maximumAvailable": 1000,
    "currentlyAvailable": 954,
    "restoreRate": 50
  }
}
```

- **Portability trap**: a single query may never exceed **1,000 points regardless of plan**, enforced pre-execution on the _requested_ cost. Higher plans get a deeper bucket, not bigger single queries - Shopify's own error: "Query cost is 1040, which exceeds the single query max cost limit (1000)." A query written against a Plus store's bucket can instantly fail on a Standard store.
- **Debug affordance**: `Shopify-GraphQL-Cost-Debug: 1` returns a per-field cost breakdown - the mechanism that lets an integrator understand _why_ a query costs what it costs.
- **Client trap**: a cost-throttled request returns **HTTP 200 with a `THROTTLED` error code** ("Similar to 429 Too Many Requests") - not a 429. Meanwhile Shopify's _resource-based_ limits (e.g. product-creation ceilings) do return a real 429, so one API mixes both conventions by limit type.
- **Conflicting-figures caveat, to state rather than fix silently**: Shopify's official plan-comparison table lists restore rates of 100/200/1,000/2,000 points/s (Standard/Advanced/Plus/Enterprise), while Shopify's own response examples and most 2026 developer write-ups show 1,000-point bucket / 50 points/s (Standard) and 2,000/100 (Plus). The 1,000-point single-query cap is unambiguous across every source; the restore rates are not - verify against the docs for the specific plan rather than trusting either source alone.

## Other named implementations

- **Zonos**: pool refilling at 3,000 points/s; every response includes a `zonos-query-complexity` header stating what the just-executed query cost.
- **Thinkific**: per-minute window; caps a single request at 1,000 points; divides raw cost by 100 purely to keep numbers human-readable.
- **Buildkite**: computes cost both before execution (static estimate, for admission control) and after (based on what was actually returned) - a connection can legitimately return fewer nodes than requested, and the post-execution number is what should count against the budget.

## Policy takeaways

- Publish the cost formula and per-field weights, not just the budget - an integrator who cannot price a query before sending it can only discover the ceiling by tripping it.
- Expose the computed cost back on every response (header or `extensions` object), plus the restore rate and remaining budget, so a client can model the bucket locally.
- Pin the per-query hard cap independently of plan and say so explicitly, or integrators will ship queries that break on smaller-plan customers.
- Weight mutations well above reads of equivalent shape (general guidance 2–5×; Shopify uses 10×).
- REST surfaces on the same platforms stay simple request counters (GitHub 5,000 req/hr; Shopify's 40-request bucket) - the two models coexist per paradigm, they never merge. Shopify is actively deprecating REST in favor of GraphQL, a forward-looking signal for where new metering design effort goes.
