# Vendor limit models - what real platforms key their limits on

Evidence base for the tier-design step: which named platforms key limits on what, how they split burst from sustained, and which of their figures to trust.

## The tier-keying finding

The naive mental model - a billing-plan column maps to a limit column - is the special case among large platforms, not the default:

| Platform  | Primary limit keyed on                                                                                                                    | Evidence                                                                                                        |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Stripe    | Flat account default + per-API limits + support-granted overrides - **not plan**                                                          | Docs state "API endpoints have a default limit of 25 requests per second"; live mode 100 operations, sandbox 25 |
| GitHub    | **Auth method**: 60 req/hr unauthenticated (per IP), 5,000 req/hr per user/PAT/OAuth token, 15,000 req/hr for Enterprise Cloud org tokens | GraphQL metered separately in points                                                                            |
| Shopify   | Plan: REST standard = 40-request bucket leaking 2/s, Plus = 400 leaking 20/s                                                              | Leaky bucket, vendor's own marble metaphor                                                                      |
| Zoom      | Plan × request-type: endpoints grouped Light/Medium/Heavy/Resource-intensive, quotas per Free/Pro/Business+                               |                                                                                                                 |
| Auth0     | Tenant type (production vs dev) × subscription (Free/Essential/Professional/Enterprise)                                                   |                                                                                                                 |
| Anthropic | Cumulative spend: auto-promotion through Tiers 1→4, Custom via account team                                                               |                                                                                                                 |

Design consequence: model limits as a function of **identity/auth-scope × endpoint-class × account-override**, and make plan-tiering a deliberate choice on top, not the starting assumption.

## Per-endpoint-class granularity (Stripe)

Rather than one account-wide number, Stripe publishes separate limits per API surface:

- Files API: 20 read + 20 write/s.
- Search API: 20 read/s.
- Payment Intents: 1,000 updates per intent per hour.
- Payouts: 15 req/s + 30 concurrent per merchant.
- Meter events: 1,000 calls/s per account.
- Connect account creation: 30/s live.

This is the pattern for carving expensive operations out of the general-purpose budget.

## Primary/secondary split (GitHub)

A two-layer policy distinct from a flat single limit:

- **Primary**: the headline quota by auth tier (60 / 5,000 / 15,000 req/hr).
- **Secondary**: an abuse guard triggered by request _shape_, not raw count - no more than 100 concurrent requests (shared across REST and GraphQL). GitHub's own docs now officially state the ceiling: no more than 900 points per minute for REST endpoints, no more than 2,000 points per minute for the GraphQL endpoint. **Cite the 900/2,000 ceilings as official** - what stays undisclosed is the per-endpoint point cost, which GitHub's docs say some endpoints deliberately do "not share publicly".

The communication lesson: a caller can be under its published quota and still get throttled by an opaque layer it discovers only by tripping it. Have a secondary guard - but document that it exists, what shape triggers it, and how it signals.

## Burst vs sustained as two explicit numbers

- **Shopify** communicates both live in every GraphQL response: `throttleStatus.maximumAvailable` (burst depth), `currentlyAvailable` (remaining), `restoreRate` (sustained points/s).
- **Stripe** engineered burst headroom deliberately - its engineering blog (Paul Tarjan, "Scaling your API with rate limiters"): Stripe "added the ability to briefly burst above the cap for sudden spikes in usage during real-time events". Sustained = token refill rate, burst = bucket depth, both intentional.
- **GitHub** splits them into two _different mechanisms_ (hourly primary quota + secondary burst guard) - workable, but only if both are documented; see above.
- The widely-cited failure mode is **burst = sustained**, which breaks legitimate spikes (webhook fan-out, scheduled reports) that need headroom above steady state. Setting burst far above sustained, conversely, defeats the protection the sustained rate exists to provide.

## A minimal published tier table

The shape integrators expect on a limits page - adapt the numbers, keep the columns:

| Tier          | Limit      | Window / keyed on | Use case            |
| ------------- | ---------- | ----------------- | ------------------- |
| Anonymous     | 30/min     | Per IP            | Public endpoints    |
| Authenticated | 100/min    | Per user          | Standard API access |
| Paid          | 1,000/min  | Per API key       | Paid plans          |
| Internal      | 10,000/min | Per service       | Service-to-service  |

Two choices this table makes implicitly that a policy must make explicitly: the identifier a tier keys on changes with the tier (IP → user → API key → service), and the magnitude step between tiers (~30× here) is a decision, not a constant. State both on purpose.

## Standing caveats

- Published limits are hints, not SLAs: every major platform in the evidence base reserves the right to lower limits for platform stability, sometimes without notice.
- Stripe's exact per-account behavior must be confirmed empirically - its docs describe defaults, and increases are per-account via Support.
- Twilio is the reminder that the metering unit itself varies: its throttling is concurrency-based (`Twilio-Concurrent-Requests`, error 20429) - in-flight requests, not requests-per-window.
