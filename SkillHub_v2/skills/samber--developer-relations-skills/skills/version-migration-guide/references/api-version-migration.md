# Hosted API migrations

A library upgrade is local and opt-in. An API version change alters behavior on someone else's running production system, on a date they did not pick. Everything below is what a hosted-API guide needs _in addition_ to the standard breaking-change entries.

## Pinning and pre-cutover testing

The single most valuable instruction such a guide gives is how to try the new version **without changing anything permanent**: a per-request version header, a per-client version parameter, or a sandbox pinned to the new version. Give a complete example request with the header in place, and state clearly which mechanism wins when both an account default and a per-request pin exist.

Tell the reader to pin explicitly in code rather than inheriting the account default. Inherited defaults mean the next cutover changes behavior in an application nobody touched, which is how a scheduled migration becomes an incident.

## Surface matrix

List every surface and how it versions, because they rarely move together:

| Surface              | Versioning                  | Moves with the API version?                 |
| -------------------- | --------------------------- | ------------------------------------------- |
| Server SDK           | Semver, per language        | Configurable, per request or per client     |
| Browser bundle       | Named evergreen releases    | Pinned to a specific API version            |
| Mobile SDK           | Semver                      | Independent; compatible across API versions |
| Webhooks / callbacks | Follows the account default | Not pinnable per request                    |
| CLI / dashboard      | Product release train       | Independent                                 |

Strongly-typed language SDKs often pin the API version at compile time, while dynamic-language SDKs allow per-request overrides. Say which applies to each SDK you ship - a reader who assumes the wrong model plans the wrong migration.

## Webhooks get their own section

Inbound events cannot be version-pinned the way outbound calls can: the consumer does not make the request. Cover which event types change shape, whether a parallel endpoint on the new version can be registered for testing, and how to handle a window where both payload shapes arrive.

## Publish the compatibility contract once

State the exhaustive list of changes you consider backward-compatible (new resources, new optional request parameters, new response properties, reordered properties, new enum members, new event types) and tell integrators to code defensively against exactly those. Anything outside the list becomes a named version with its own guide.

Publishing the contract once ends the per-release argument about whether a change is breaking, and it tells integrators which defensive code is actually required rather than leaving them to over-engineer.

## Data-layer consequences

Wire changes leak into consumers' databases. Cover:

- Identifier length and case sensitivity.
- Changed enum values persisted in columns.
- Timestamp precision or timezone representation.
- Decimal versus integer money fields.
- Any stored raw payloads that must be re-parsed.

These are the changes that break consumers weeks after a successful cutover, which is why they need their own section rather than a line in a code entry.

## Cutover and rollback

State, in this order:

1. Who flips the account default, and on what date.
2. What the customer must complete beforehand.
3. How to roll back, and for how long that remains possible.
4. How long the old version stays available after the deadline.

Give the rollback procedure even when you are confident. Readers schedule an irreversible change differently from a reversible one, and the difference decides whether they migrate early or wait for the deadline.

## Notice and escalation

For contractual audiences, put the notice window, the support path and the escalation contact inside the guide. The announcement email reaches one address that may no longer be monitored; the guide is what the engineer actually opens.
