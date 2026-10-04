# Verification playbook

The plan is unproven until one real event has been traced end to end on each surface. A green debugger, a live tag, or a configured API connection proves that something is configured - not that anything is measured correctly.

## Contents

- [The trace](#the-trace)
- [Per-surface trace recipes](#per-surface-trace-recipes)
- [Exclude your own traffic](#exclude-your-own-traffic)
- [Comparability gate](#comparability-gate)
- [Re-verification triggers](#re-verification-triggers)
- [Finding schema](#finding-schema)

## The trace

For each primary conversion event, walk the real user path and confirm every hop, in this order:

1. **Act as a real user.** Fresh browser profile, no cached session, arriving through a tagged external link. Accept or deny consent deliberately - run the trace twice if both states matter.
2. **Confirm the landing URL keeps its query string.** Redirects, shorteners, OAuth hops and locale rewrites are where tags die.
3. **Inspect the outgoing request payload.** It must carry the event name, a unique event ID, the identity fields the spine defines, and the properties in the registry - with the registry's types, not stringified numbers.
4. **Confirm receipt in the collector**, not just in the browser's network tab.
5. **Find the stored record** and confirm the identity fields resolved: `anonymous_id` present, `user_id` attached on the signup event, `account_id` populated if the motion needs it.
6. **Find the row in the report** the funnel view will actually read. This is the step teams skip, and it is where a correct event silently lands in the wrong bucket.
7. **Verify no duplicate.** Refresh the confirmation page and re-enter through the back button; the deduplication key must hold.
8. **Record the evidence** - surface, event, timestamp, consent state, payload excerpt, report row - in the plan document. An untraced event ships as "unverified", never as done.

## Per-surface trace recipes

| Surface    | The one trace that matters                                                                                                    |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Docs       | tagged inbound link → quickstart page → `quickstart_step_completed` → success event → the funnel view's step-2 count          |
| Blog       | tagged inbound link → outbound click to signup → signup event carrying the original source                                    |
| Repository | export the traffic endpoints twice 24 hours apart and confirm the append landed without gaps or duplicate days                |
| Registry   | pull the same day's download figure twice a week apart; if it moved, you are reading a revised or differently-filtered series |
| Community  | post as a test member, confirm the export sees the message, the bot filter excludes bots, and the staff flag marks staff      |
| Off-web    | load the vanity URL from a phone on mobile data and confirm it resolves, tags, and lands in the source report                 |
| Product    | fire the activation event from a test account and confirm the devrel-side identity resolves to it                             |

## Exclude your own traffic

Do this before the plan goes live; exclusion filters are not retroactive.

- Office and VPN ranges, the team's own accounts, CI, preview/staging deployments, and docs-preview URLs.
- Confirm the filter is _active_, not merely defined - collection tools commonly ship a new filter in a testing state that tags internal traffic without excluding it.
- Retract test conversions and delete test records once the trace is recorded.
- Internal and test traffic is a large fraction of sessions on a small docs site; unfiltered, it makes the team's own reading habits look like adoption.

## Comparability gate

Refuse to sum or average numbers from two sources until they share:

- The event definition.
- The attribution window.
- The counting rule (once per session versus every occurrence).
- The deduplication identity.
- The timezone.
- The bot/mirror filter.

Two download series with different mirror policies, or two conversion counts with different windows, are not addable - publish both with their definitions and explain the delta.

## Re-verification triggers

Re-run the full trace after any of these, because each one silently strips instrumentation:

- A site redesign or a docs-generator major upgrade.
- A consent-banner or consent-mode change.
- A new domain, subdomain or CDN in front of an existing surface.
- A new surface, a new registry, or a migrated community venue.
- Any change to the identity spine.

Schedule a standing re-trace at least quarterly even when nothing above happened. Silent breakage is the default failure mode; nobody files a bug for a missing event.

## Finding schema

Report each verification result in one shape so a reviewer can act without re-reading the plan:

| Field              | Values                                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------- |
| Result             | pass / fail / unknown / not applicable                                                   |
| Severity           | critical (a primary event is missing, double-counted, or wrongly valued) / major / minor |
| Confidence         | high / medium / low, with the reason                                                     |
| Observation        | what was seen                                                                            |
| Evidence           | payload excerpt, report row, timestamps                                                  |
| Owner and due date | a named person                                                                           |

Reserve _critical_ for a confirmed defect with observed impact. A surface that is simply not instrumented yet is a coverage gap, not a critical finding - labelling everything critical is how a verification report gets ignored.

A verification pass never mutates production tracking. It returns findings; someone else applies them, and the trace is re-run afterwards.
