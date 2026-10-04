# Visibility Surfaces

The three developer-facing log surfaces, what each row must carry, replay semantics, and the access and redaction rules that gate all of it.

## Contents

- The three surfaces
- Required fields per surface
- Good and bad log rows
- Replay semantics
- Retention, access scoping, redaction

## The three surfaces

They answer three different questions and are not substitutes. Stripe's developer dashboard keeps them separate and is the clearest public reference for the split (sourced: Stripe docs).

| Surface              | Question it answers         | Granularity                               | Primary reader                                              |
| -------------------- | --------------------------- | ----------------------------------------- | ----------------------------------------------------------- |
| Request log          | "Did my call work?"         | One HTTP request/response pair            | Any integrator debugging a synchronous failure              |
| Event log            | "What did it change?"       | One business-level event, with payload    | An integrator reconciling state, or auditing after the fact |
| Delivery-attempt log | "Did you tell me about it?" | One delivery attempt against one endpoint | A webhook consumer whose handler went quiet                 |

A platform that ships only the request log leaves every "the webhook never arrived" ticket unanswerable, and one that ships only the delivery log cannot explain a synchronous 400. Build the one matching your ticket pile first. Plan for all three.

## Required fields per surface

**Request log row** carries:

- Timestamp with timezone
- HTTP method and endpoint path
- Status code
- Machine-readable error code
- Request ID
- Integration identity (API key or app ID, and the account it acted on)
- Latency
- Request and response bodies, subject to redaction

Omitting the error code and keeping only the status code is the common shortfall: `400` alone tells an integrator nothing their own client did not already know.

**Event log row** carries:

- Event ID
- Event type
- Creation timestamp
- The object it concerns
- The full payload as delivered
- A pointer to the request that caused it

The link back to the causing request is what turns two logs into one investigation.

**Delivery-attempt log row** carries:

- Event ID
- Destination endpoint
- Attempt number
- Attempt timestamp
- Response status or transport-level failure reason (timeout, connection refused, TLS failure, non-2xx)
- The response body your server received back, if any
- The next scheduled retry time

The failure reason must be the actual one, not a generic "delivery failed" - the whole value of the surface is giving the integrator the detail their own logs would have shown if their handler had ever run. This is a real, shipped external surface rather than an internal-only convenience: Twilio's Debugger, HubSpot's webhook monitoring log, Zapier's Zap history, and Workato's job history each expose attempt-level status and the actual failure reason (including a distinction between a timeout and other causes) to their own external developers (sourced: Twilio, HubSpot, Zapier, Workato docs).

Across all three: make every identifier copy-pasteable and searchable, and show the same identifiers the integrator sees in their own responses. A dashboard that displays an internal primary key instead of the request ID you returned in the header breaks the lookup path entirely.

## Good and bad log rows

Bad - a row that produces a support ticket:

```
2026-08-31 14:22  POST /v1/orders   400   Error
```

Nothing here is actionable. No error code, no request ID, no indication of which field failed, no identity, no link to detail.

Good - a row the integrator resolves alone:

```
2026-08-31 14:22:07 UTC  POST /v1/orders  400  invalid_shipping_address
  request_id  req_8f2c1ab9d3e04c7f
  app         acme-connector v2.3   account acct_19KdQ2
  detail      shipping.postal_code: "SW1A" is not a valid postal code for country "US"
  latency     84 ms
```

The difference is not volume of text - it is that each field answers a question the integrator would otherwise have asked you.

## Replay semantics

Replay is the highest-effort rung of the visibility ladder. Design it around four decisions:

1. **Window.** Bound how far back a replay can reach. Stripe allows manual resend of a failed event for up to 15 days after creation (sourced: Stripe docs). Pick your own bound from your retention and state model, and publish it.
2. **Independence from automatic retry.** A manual replay must not cancel, reset or interfere with the platform's own retry schedule, and the two must not double-deliver in a way the integrator cannot detect. Stripe's resend explicitly does not cancel its automatic schedule (sourced: Stripe docs) - the two mechanisms run independently. PayPal ships the same pattern: a "Resend" action on its Webhooks Events dashboard, separate from its automatic retry schedule (sourced: PayPal docs). Checkout.com documents the same feature and is explicit about the risk this decision creates: manual resend can produce a duplicate delivery "if any automatic retries are scheduled" (sourced: Checkout.com docs) - exactly the failure this rule exists to prevent.
3. **Idempotency.** Every replayed delivery carries the same event ID as the original so the consumer can deduplicate. Without a stable ID, replay converts a missed event into a duplicated side effect, which is a worse failure than the one it fixed.
4. **Scope.** Decide whether replay is per-event, per-endpoint (everything that failed in a window), or per-time-range. Bulk replay needs rate control, or an integrator recovering from an outage becomes your next incident.

Do not offer replay of synchronous API requests the way you offer replay of events. Re-issuing a POST on the integrator's behalf creates side effects nobody authorised. Give them the full request detail and let their own client re-issue it.

## Retention, access scoping, redaction

**Retention.** The window has to exceed the time it realistically takes a partner to notice a failure. A 24-hour window on a failure class noticed at weekly reconciliation guarantees the evidence expires before the investigation starts. Publish the window, since an undocumented one gets discovered during an incident.

**Access scoping.** Decide explicitly who can read each surface: the account owner, any user of the account, and - separately - the partner engineer who maintains the integration but is not a user of the customer's account. That third case is the one platforms usually miss, and it is the reason a partner with a fleet of installs cannot debug through a per-account dashboard even when one exists.

**Redaction.** Before any payload becomes visible to an external party, run a data-classification pass:

- Strip credentials, tokens and signing secrets unconditionally - never partially masked, since a prefix plus a length is often enough to attack.
- Mask PII to the level your legal answer (question 7 of the interview) permits, and make the masking visible so the integrator knows a field was withheld rather than absent.
- Guarantee tenant isolation structurally, not by query convention. A log surface that filters by account ID in application code is one missing clause away from showing one customer another's data.
- Treat the redaction rule set as a published contract once integrators build against it - loosening it later is a privacy incident, tightening it later breaks their tooling.
