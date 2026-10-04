# Retry policy: vendor comparison

Documented schedules behind SKILL.md step 4's ranked menu. Retry policy is the single sharpest divergence axis between real webhook platforms - the delivery guarantee, signing algorithm, and ordering stance all converge; this doesn't.

## Documented schedules, six vendors

| Vendor   | Automatic retries                                                                    | Span                                               | Timeout                  | After exhaustion                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------ | -------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stripe   | Exponential backoff (live mode)                                                      | Up to 3 days (test mode: 3 tries over a few hours) | -                        | Endpoint auto-disabled after ~3 days of failure, with notification                                                                                                                               |
| GitHub   | **None**                                                                             | -                                                  | 2xx expected within 10s  | Manual: UI redeliver (3-day window) or REST Deliveries API (30-day listing)                                                                                                                      |
| Shopify  | 8 retries, exponential backoff                                                       | 4 hours (policy current since Sept 2024)           | 5s response + 1s connect | Subscription auto-**deleted** after 8 consecutive failures; warning email to the app's emergency address. Declarative (TOML) subscriptions restore on next deploy; Admin-API-created ones do not |
| Svix     | 8 attempts, exact schedule: immediately, +5s, +5m, +30m, +2h, +5h, +10h, +10h        | ~27.5 hours                                        | ~15s                     | DLQ; consistently failing endpoints disabled with notification                                                                                                                                   |
| Hookdeck | Configurable: linear or exponential, up to 50 automatic retries                      | Configurable                                       | -                        | Exhausted deliveries surface as "Issues" (grouped incidents), unlimited manual retries                                                                                                           |
| Convoy   | Two algorithms: constant-time or exponential-with-jitter; per-endpoint rate limiting | Configurable                                       | Configurable             | Batch retry for consecutively failing endpoints; true circuit breaker (below)                                                                                                                    |

Staleness warnings baked into the table: Shopify's widely-cited "19 times over 48 hours" is the pre-Sept-2024 policy - any source repeating it is stale. Stripe's manual Dashboard resend does not cancel the still-running automatic schedule; the two run independently.

## Policy mechanics

- **Backoff formula**: `delay = base_delay * (2 ^ attempt_number)`, with jitter. Linear intervals are actively harmful - they hammer a down endpoint continuously and worsen an active rate-limit response.
- **Failure classes differ in duration**, so size the total span against them: a network blip resolves in milliseconds, a deployment in minutes, an infrastructure outage in hours. A schedule ending before a realistic outage ends dead-letters events the subscriber would have recovered.
- **Not everything retries**: non-retriable 4xx (anything except 408/429) skips the budget and dead-letters immediately - retrying a permanent failure wastes resources and can look like an attack to the receiving endpoint. A 429 with `Retry-After` is retried at the receiver's stated delay, overriding your own curve.
- **Queue-first is the prerequisite**: POSTing webhooks from the main application thread collapses under load; delivery decouples from the event-producing request path via a durable queue before any retry policy matters.

## Dead-letter policy

- Exactly two triggers: retry budget exhausted, or a non-retriable error class.
- Retention: 7-30 days, preserving full event context (headers included) for investigation and replay.
- **Dead-letter rate is the headline operational metric** - a spike signals an endpoint in sustained failure, distinct from background transient retries.
- The "Issues" framing (Hookdeck): treat an exhausted delivery as an operational incident to investigate - grouped by endpoint and status code, surfaced to a human with notification - rather than a message sitting in a queue behind a bare replay button.
- Test the recovery path on a schedule: inject failures, verify events land in the DLQ, practice the replay - the path decays if untested.

## Circuit breaker (the promoted rung's reference design)

Convoy ships the only true half-open circuit breaker among the six: a volume threshold and error-ratio threshold trip it, a timeout parameter holds it open, and an automatic probe delivery tests recovery before resuming full traffic. Contrast with the common simpler mechanisms - Stripe's auto-disable and Shopify's auto-delete are one-way doors requiring subscriber action to reopen. The circuit breaker matters at scale: without it, every sustained-failing endpoint consumes its full retry budget on every event, and a platform with thousands of endpoints pays that continuously.

## Why "no retries" is a named anti-pattern, precisely

GitHub ships zero automatic retries and survives it only because two compensations ship alongside: a deliveries-list API with a redeliver endpoint (so consumers can build a scheduled poll-and-redeliver script), and documentation that explicitly assigns reconciliation to the consumer. That pushes 100% of reliability engineering onto every integrator - defensible for GitHub's developer-heavy audience, and still the sharpest outlier surveyed. A platform copying the "no retries" half without the API-and-docs half is not shipping a minimalist design; it is shipping unreliable delivery.

## Reconciliation as an endorsed practice

For high-stakes event types (payments is the canonical example), recommend consumers periodically diff processed events against your API's own records - if the API shows state changes the consumer never processed, events were lost in a way retries and the DLQ didn't catch. Shopify's docs recommend exactly this as the primary defense rather than treating gaps as a bug to fix - set the same honest expectation.
