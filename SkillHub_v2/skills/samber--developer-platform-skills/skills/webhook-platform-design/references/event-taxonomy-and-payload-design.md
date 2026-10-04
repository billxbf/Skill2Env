# Event taxonomy and payload design

Vendor comparisons and worked detail behind SKILL.md steps 1-2.

## Naming conventions in production

| Platform          | Convention                                               | Example                                             | Note                                                               |
| ----------------- | -------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------ |
| Stripe            | `resource.action`, dot-delimited                         | `charge.succeeded`, `customer.subscription.updated` | No domain prefix; subresource events never bubble to parent events |
| Shopify           | `resource/action`, slash-delimited                       | `orders/create`, `app/uninstalled`                  |                                                                    |
| GitHub            | Split: header + body field                               | `X-GitHub-Event: issues` + `"action": "opened"`     | No single string names the full event - the shape to avoid         |
| Standard Webhooks | `resource.action`, identifiers `[a-zA-Z0-9_]`            | `invoice.paid`                                      | Closest to Stripe's convention; the recommended default            |
| Svix              | First-class event-type objects with attached JSON Schema | -                                                   | Auto-generates the Event Catalog from them                         |

Recommended: Object-Action, past tense (`invoice.paid`, not `invoice.pay`), dot notation for hierarchy, optional domain prefix for grouping. Reject underscore-joined or verb-first names (`user_update`, `invoiceWasPaid`) - inconsistent and harder to filter and route on.

## Event design principles (checklist per event type)

1. **Self-contained** - include what a consumer needs; don't force a callback to the API just for context (thin payloads are a deliberate exception, chosen platform-wide, not per event).
2. **Immutable** - never modify a schema after events of that type have shipped; add fields, never repurpose them. Stripe goes further: an Event object, once created, never changes - a later update to the resource produces a new Event.
3. **Traceable** - correlation IDs, audit-trail fields.
4. **Actionable** - enough context for the consumer's business logic, not just an ID.
5. **Debuggable** - source, environment, originating trigger in metadata.

## Minimal envelope

Required: `type` (the catalog name) and `data` (the payload). Valuable: a unique event `id` (the dedup key), a timestamp, and a schema-version marker. Where each of these lives is the envelope-placement fork below.

## Envelope placement: body-only vs header-split

- **Body-only (Stripe)**: everything - `id`, `type`, `api_version`, `created`, `data` - lives in one top-level JSON object. The full event is self-contained in a single payload dump for logging.
- **Header-split (GitHub, Shopify, Standard Webhooks/Svix)**: metadata rides HTTP headers (`webhook-id`, `webhook-timestamp`, or vendor equivalents); the body carries `{type, timestamp, data}` or just the resource. CloudEvents' "binary" content mode standardizes the same split via `ce-*` headers; its "structured" mode is the all-in-body alternative.

The consequential difference: a header-split design means your delivery log and replay feature must capture headers _and_ body to reproduce an event faithfully. Decide the fork before building the log, not after.

## Thin vs full payloads

- **Full (snapshot)**: embed the resource state as of the event. Self-contained, but the payload shape is coupled to your API version.
- **Thin**: identifiers only; the consumer fetches the resource. Smaller (Standard Webhooks recommends staying under ~20kb), and the notification never changes shape when the API version bumps - the version question moves to the API call the consumer makes.

Migration pattern (Stripe's snapshot-to-thin transition): emit both event flavors together during the transition and stamp a discriminator field on the payload so consumers can dual-run idempotently. Reusable for any full-to-thin move made after launch.

## Schema versioning: the two camps

1. **Pin the consumer to an API version** (Stripe): each webhook endpoint is pinned to an account API version and payloads render per that version. Upgrading the account version changes what existing webhooks receive - which is exactly the hazard to manage. Retrieving an old event under a newer version does not retroactively reshape it.
2. **Version the event type** (Svix / Standard Webhooks): a new event-type name per breaking change (`v1.customer.created` → `v2.customer.created`), additive-only evolution otherwise. The type name is the version marker; no out-of-band version applies.

Both solve the same problem. Pick one deliberately - drifting into both by accident, or letting an API version bump silently reshape stored payloads, is the failure mode. GitHub and Shopify version payload shape implicitly with the overall (date-versioned) API - the ambient default a deliberate choice replaces.

## Standards map (layers, not competitors)

| Standard                     | Layer                      | What it gives you                                                                                                                                     |
| ---------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard Webhooks            | Signing + delivery headers | Interoperable signature scheme; near-zero adoption cost                                                                                               |
| CloudEvents (CNCF-graduated) | Envelope                   | `id`/`source`/`type`/`specversion` attributes; HTTP/Kafka/AMQP/MQTT bindings; low real-world adoption for consumer-facing webhooks despite graduation |
| AsyncAPI                     | Description language       | Documents channels and message schemas; never on the wire; can describe WebSocket channels too                                                        |
| OpenAPI 3.1 `webhooks`       | Description language       | Outbound events documented in the _same_ spec as the inbound API - the recommended documentation home                                                 |
| WebSub (W3C)                 | Pub/sub protocol           | Content-syndication oriented; rarely relevant to transactional B2B webhooks                                                                           |

No ratified W3C/IETF transactional-webhook standard exists. Practical layering for a new platform: Standard Webhooks for signing/delivery, whichever envelope placement fits your API conventions, OpenAPI 3.1 for description - and full CloudEvents only to interoperate with an event mesh that already speaks it.
