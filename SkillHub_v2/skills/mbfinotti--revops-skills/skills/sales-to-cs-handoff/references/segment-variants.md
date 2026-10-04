# Segment Variants

The governing principle is Lincoln Murphy's Appropriate Experience (AX)-based segmentation: set the touch level by the experience a segment needs to feel successful, never by what it pays. Segment the handoff by needed experience and operational capability, with price as a constraint, not the driver.

Two consequences invert naive defaults:

- Over-serving self-serve customers with human touch is itself a bad experience ("smaller customers may need a lot, but self-service and 1:many is what they expect").
- A large, mature customer may need less hand-holding than assumed ("bigger more mature customers may not need much from us at all").

## Summary table

Columns run from most ceremony to least; that is a segment ordering, not a build order. The build order inside any one column is the efficiency ranking in the skill's Ceremony, Ranked section - build wiring first everywhere, then add rungs until the segment's hour ceiling runs out. The last two rows are that ceiling and what it buys.

| Design decision      | Enterprise / high-touch                                           | Mid-market                                            | High-volume SMB                                     | PLG / self-serve                                    | B2C subscription                                               |
| -------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------- |
| Trigger              | Closed-won, gated on full packet + SOW                            | Closed-won, gated on must-block fields                | Closed-won, gated on structured fields only         | Conversion/plan-change event in billing             | Subscription-start event in billing                            |
| Artifact             | Packet document + CRM fields + recordings                         | CRM fields + short packet                             | CRM fields only                                     | Event payload on account record                     | Event payload on customer record                               |
| Receiver             | Named CSM + implementation team                                   | Named CSM (or onboarding pool → CSM)                  | Pooled CS, assignment rule                          | No human; lifecycle system owns it                  | No human; lifecycle system owns it                             |
| Meetings             | Internal sync + live customer kickoff                             | Internal sync (async brief acceptable) + kickoff call | No internal meeting; welcome call optional          | None; activation flow instead                       | None; lifecycle messaging instead                              |
| Internal clock       | 1 business day                                                    | 1 business day                                        | Same day (automated assignment)                     | Instant (event-driven)                              | Instant (event-driven)                                         |
| External clock       | Kickoff held ≤ 10 business days                                   | Kickoff held ≤ 5 business days                        | First touch ≤ 2 business days                       | First automated touch ≤ 1 hour                      | First automated touch ≤ 1 hour                                 |
| Acceptance           | CSM accepts/rejects explicitly                                    | CSM accepts/rejects explicitly                        | Sampling audit instead of per-deal acceptance       | Automated validation of record completeness         | Automated validation of record completeness                    |
| CS hours per handoff | Several hours, across two meetings and a document                 | About an hour, one meeting plus a short packet        | Minutes, and none on most deals                     | Near-zero; hours spent once on the motion map       | Near-zero; hours spent once on the motion map                  |
| Retention bought     | Ghosting prevented on accounts whose loss is individually visible | Momentum held between signature and first value       | Repeat-yourself and archaeology removed at scale    | A reliable path to the activation event             | A reliable path to the activation event, within consent limits |
| Rungs deleted        | None                                                              | Packet document, unless services ship with the deal   | Per-deal acceptance, internal sync, packet document | Both meetings, packet document, per-deal acceptance | Both meetings, packet document, per-deal acceptance            |

Clock values are starting defaults to calibrate against the org's baseline, not published standards. Hour figures are orders of magnitude for sizing the ceremony, not measured averages - measure the org's own before treating them as a budget.

The rungs in the deleted row are deleted, not deprioritized: a segment that keeps them on a backlog re-acquires them the first time a deal goes badly, and the volume that made them unaffordable has not changed.

## Enterprise / high-touch

Multi-person transfer at the internal sync:

- Rep briefs CSM and implementation/services together.
- Commitments and SOW reviewed line by line before any customer contact.

The customer kickoff is a formal, visible transfer - sales introduces the post-sale owner live and stays engaged until CS accepts, because the customer must never wonder who owns them now. A phased 30/60/90 outline is _presented_ at kickoff, but building and running it belongs to onboarding, not to this process.

## Mid-market

Same shape, lighter weight: the internal sync can be an async written brief with a confirmation step when calendars don't allow a meeting, but the acceptance step stays explicit - this is the segment where "we skipped the sync just this once" quietly becomes the norm.

- One named receiver per deal.
- Kickoff within a week keeps momentum from the buying decision.

## High-volume SMB

Volume kills per-deal ceremony:

- Structured CRM fields are the whole artifact.
- Assignment is rule-driven into a pool with a fallback owner.
- The welcome touch is a templated call or email sequence.

Per-deal acceptance is replaced by a weekly sampling audit of packet quality plus automated completeness checks - the gate still blocks, but a human no longer inspects every deal.

## PLG / self-serve

There is no human handoff, by design - do not invent one. The handoff is a system-to-system event: a billing or CRM state change (trial converts, plan upgrades, team crosses a seat threshold) that must fire reliably and carry a complete account record. The design questions become:

- **Which signals trigger which automated motion**:
  - Conversion → lifecycle onboarding sequence and in-app guidance toward the activation event (the behavioral moment that predicts retention - identify it and design the shortest path to it).
  - Usage threshold → expansion motion.
  - Silence past a defined window → re-engagement motion.
- **Who owns exceptions**: pooled, reactive CS (or support) receives the cases automation escalates - failed activation after N days, high-value account inactive, billing failure. Ownership of the motion map itself typically sits with growth or lifecycle marketing, not CS - name the owner explicitly either way.
- **What the gate checks**: record completeness (plan, billing state, consent, attribution), because a malformed record silently breaks every downstream motion.

The substitutes for the human motion:

- The activation event stands in for the kickoff.
- Time-to-activation stands in for time-to-kickoff.

## B2C subscription

Mechanically the PLG pattern - system-triggered lifecycle onboarding, no human owner, pooled exception handling - with three differences worth designing for:

- Consent and privacy constraints gate which lifecycle messages may fire at all.
- Involuntary-churn handling (failed payments, dunning) enters the exception map immediately because the payment relationship starts at day zero.
- The "stakeholder" model collapses to one person, so all context is behavioral, not relational.

Everything else transfers unchanged.

## Mixed-motion orgs

Most orgs run two or three of these at once. Write one spec with per-segment rows for trigger, artifact, clocks, meetings, and acceptance - not separate specs - so the segments share the gate logic, the reason codes, and the KPI definitions, and deals that cross segments (a self-serve account converting to sales-led) inherit a defined path.
