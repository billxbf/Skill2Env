# Subscription lifecycle and debugging surface: vendor comparison

Detail behind SKILL.md steps 5-6. The clearest pattern in this data: the three infrastructure-only vendors (Svix, Hookdeck, Convoy) converge on richer states, deeper filtering, true replay, and a full portal, while the platforms where webhooks are one feature among many (Stripe partially, Shopify, GitHub) ship the thinner model. Treat the infrastructure-vendor shape as the target state; the thinner shape is what most teams launch with and outgrow.

## Endpoint states

| Vendor                 | States                     | Notes                                                                                                  |
| ---------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------ |
| Stripe                 | enabled / disabled         | Auto-disabled after the ~3-day retry window                                                            |
| GitHub                 | active / inactive          | Binary                                                                                                 |
| Shopify                | active until auto-deleted  | 8 consecutive failures deletes an Admin-API-created subscription; TOML-declared ones restore on deploy |
| Svix, Hookdeck, Convoy | active / paused / disabled | Plus auto-disable-with-notification on sustained failure - the model to default to                     |

Case-study lesson on state design (Salesforce's managed event subscriptions): valid states are run and stop; an internal pause state exists but user-created subscriptions are rejected from setting it. The transferable rule: choose the states a customer-created subscription may legally reach, and reject internal-only states at the API boundary rather than exposing them.

## Replay positions (same case study)

Two independently configured positions, each taking "latest" (new events only) or "earliest" (full retained backlog):

- **Default replay** - where a newly created subscription starts reading.
- **Error-recovery replay** - where a subscription resumes after a platform-side incident, as distinct from a normal restart.

These can legitimately differ; specify both.

- Deleting a subscription permanently destroys its replay-tracking state - recreating under the same name restarts from the default position, so a subscriber deleting-to-reset silently loses or double-replays a backlog.
- Activating a full-backlog replay on a high-volume channel can mean days of replay traffic - gate it behind an explicit confirmation.
- Config changes can take a minute or two to propagate to the delivery path; document that as expected, not a bug.

## Replay and backfill capability

The sharpest capability split in the domain:

- **Stripe**: Events API lists/retrieves 30 days, supports resend; documents polling the resource API to backfill missed objects.
- **Svix**: portal replay of individual messages or ranges; polling endpoints iterate the entire event history.
- **Hookdeck**: permanent event log, bulk pause/cancel/replay via API. Source of the terminology worth adopting verbatim: **retry** = a new delivery attempt of the same event; **replay** = re-ingesting the original request as a brand-new entity that produces new events.
- **Convoy**: persists all events; UI + API manual and batch retry.
- **Shopify**: no native replay or backfill - the documented mitigation is a consumer-side reconciliation job.
- **GitHub**: UI redeliver (3-day window) or Deliveries API (30-day listing); no true backfill.

## Filtering and fan-out

Two independent filtering axes - keep them separate in the design:

1. **Event type** - selection against the catalog (Stripe's `enabled_events`, Shopify's one-subscription-per-topic).
2. **Recipient/channel scoping** - an orthogonal dimension for sub-grouping deliveries (per-tenant, per-repo, per-project). Svix models this as "channels", off by default, filtered independently of event types; Hookdeck and Convoy route on richer rule/payload-structure criteria.

Filtering is producer-side: an endpoint with no filter configured receives everything - state that explicitly. Multi-endpoint fan-out is universal (Standard Webhooks recommends multiple endpoints per consumer as a resilience pattern); one event fans out to every matching endpoint, each delivered and retried independently, so one slow or broken endpoint never blocks the others.

## Portal and testing tooling benchmark

What the A-grade debugging surface actually ships, per vendor:

- **Stripe CLI** - the reference for code-first consumers: `stripe listen --forward-to localhost:PORT` (stable CLI-issued signing secret) plus `stripe trigger <event>` firing a realistic example event on demand.
- **Svix App Portal** - the most complete consumer portal, embeddable and brandable: event catalog with schemas and example events, a schema-driven "send example webhook" button, filterable logs, per-attempt inspection, message replay.
- **Hookdeck** - real-time visual delivery traces; exports latency/error-rate metrics to an external observability stack; config-as-code via API/Terraform.
- **Convoy** - embeddable customer-facing dashboard (iframe or white-label) with email and chat failure notifications built in.
- **GitHub** - no first-party trigger command; sends an automatic "ping" event on webhook creation (a pattern worth copying: the subscriber verifies wiring without waiting for a real event).

Local tunneling and inspection (ngrok-class tunnels, request-inspection sites) are a shared consumer-side ecosystem - your docs should point at the category rather than build it, unless you ship a first-party CLI tunnel.

No-code consumers arrive with the catch-URL mental model from workflow-automation tools: a temporary URL captures one real payload so they can map fields before building logic, and a frequent production bug is a sender left pointed at the test URL after setup. Your test-event feature is the provider side of that same job - design and document it assuming this mental model, and make test deliveries clearly distinguishable from live ones.
