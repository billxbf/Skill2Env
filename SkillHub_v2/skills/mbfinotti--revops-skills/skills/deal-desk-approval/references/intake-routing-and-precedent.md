# Intake, Routing, SLAs, and Precedent Control

Sourced primarily from the Umbrex deal-desk operator series [practitioner] unless tagged otherwise.

## Intake fields

Require these field groups on every request:

- Identity and routing: account (and parent account), opportunity ID, seller, seller's manager, segment, region, channel.
- Commercial basics: list price, proposed price, requested discount or target price, currency, expected close date.
- Offer essentials: products/SKUs, quantities, term length, start-date assumption, deal type (new/renewal/expansion).
- Context: use case in one or two sentences, customer decision date, primary competitor or alternative.
- Non-standard flags: structured tags per lever - pricing, payment terms, services scope, contract terms, security/privacy, delivery commitments.
- Justification, split into separate fields:
  - Economic upside: revenue, term, margin, cash.
  - Strategic upside: reference value, target-vertical entry, named-competitor displacement, credible expansion path.

  Each field ties to the specific exception requested - a strategic logo does not justify every concession. State what the company gets in exchange for this ask.

- Impact of denial - the highest-weight field: what changes if the exception is refused. "The customer asked for it" is not sufficient justification.
- Prior exceptions granted to the same account.

## Completeness gate and bounce protocol

Work starts only when required fields are present; incomplete submissions bounce, they never queue.

The bounce is structured:

- List the missing items.
- Explain the business impact.
- Name the responsible party.
- Give resubmit instructions.

Quality dimensions to enforce:

- Completeness
- Validity (numeric/logical checks)
- Consistency (deal record, quote, and contract systems must agree)
- Timeliness
- Auditability (rationale recorded against each decision)

## Routing lanes

Structural risk, not deal size, forces the lane: a large deal at list price with standard terms needs no review, while a small deal with a custom indemnity clause does [illustrative example].

The design goal is to move volume down this list, not to staff it evenly - the fast lane clears deals per analyst hour by an order of magnitude over the other two.

- deals cleared per analyst hour: fast > complex > exception
- concession value and risk governed per case: exception > complex > fast
- analyst load per case: exception > complex > fast
- compliance cost: exception > complex == fast

**Fast lane** - one lever changed, within guardrails, standard terms, no novel risk. Near-zero analyst load (a completeness check and a rule match), same-business-day decision, and it should carry the bulk of volume.

**Complex lane** - two or three lever changes, or delivery dependencies needing confirmation, within risk appetite. About an hour of analyst work plus one cross-function confirmation; one to two business days.

**Exception lane** - below-floor economics, prohibited terms, novel security obligations, or high-precedent structures. Several hours of package assembly against several approvers' calendars, and a week of elapsed time.

Complex == fast on compliance cost by construction, not coincidence: anything on the accounting/legal routing table, in the prohibited class, or setting precedent is exception-lane by definition, so neither of the other lanes may ever carry that exposure.

What this order starves: the exception lane. It is high value and high effort, so a desk measured on cycle time quietly widens the fast lane's guardrails until below-floor and precedent-setting structures slip through - the failure the lanes exist to prevent. Promote a request to the exception lane on structure alone, however simple it looks and however close the quarter-end is.

## Two SLA clocks

- Response SLA: within a few business hours for every lane.
  - Acknowledge.
  - Validate completeness.
  - Assign the lane.
  - Communicate next steps.
- Decision SLA, per lane:
  - Fast lane: same business day.
  - Complex lane: one to two business days.
  - Exception lane: several business days, with an interim milestone of a complete decision package within one day.
- Both clocks run in business hours. The clock starts when required fields are complete in the system of record and stops when the decision is recorded and communicated - not when a reviewer replies with a clarifying question.
- A circulating claim that win rate degrades materially past a 48-business-hour ceiling (sometimes attributed to revenue-intelligence data) is [unverified] - the named revenue-intelligence vendors' own published research contains no such finding, and no named study backs the number anywhere it circulates. Use the mechanism (slow approvals lose deals and breed bypass), not the number.

## Elapsed-SLA auto-escalation: 50 / 80 / 100

- 50% of SLA elapsed: case owner confirms next steps and checks blockers.
- 80% elapsed: escalate to the approver's delegate or manager with a decision window; at quarter-end peaks, apply this trigger to top-tier approvals with a complete decision memo attached.
- 100% elapsed: formal escalation path, decision package attached.

## Approver absence and delegation

- Every approver names a delegate with an explicit delegation window (start and end dates).
- An expiring delegation with a pending item escalates rather than deadlocks.
- Define a break-glass role for the case where the delegate is also absent.
- Design the absence protocol explicitly with the user and record it as house policy.

## Quarter-end peak mode

Peak mode adds capacity and clarity, never relaxed rules; the completeness gate and the approval matrix stay intact:

- Extended coverage where available
- Published completeness cutoffs for same-day handling
- Dedicated executive escalation windows

Period-end discount spikes are the signature of undisciplined (not strategic) discounting. The durable fix is earlier deal shaping upstream, not crunch-time exceptions.

## Precedent control

- "This is a one-time exception" is not self-enforcing - customers cite it as precedent the following year. Precedent is a first-class risk dimension alongside margin, revenue-recognition, legal, and deliverability; the register is the desk's institutional memory.
- Time-box every granted exception (30-60 days is the typical published window [practitioner]); a quote without an expiration date is itself a precedent risk.
- Exception register - treat this field list as a suggestion to adapt to the user's systems: request ID and deal ID, requestor, exception type (by lever), justification and impact-of-denial as submitted, approver and tier, decision and reason string, expiry/sunset date, renewal-exposure flag, later-cited-as-precedent tracking.
  - Umbrex's own toolkit publishes a second, per-lever variant instead of one universal register - separate field sets per exception type:
    - Discount: ask, baseline, category, evidence, give-get, economics delta, precedent control, fallback.
    - Payment terms: ask, invoice trigger, cash impact, give-get, credit trigger, expiration.
    - Free/discounted services: ask, assumptions, timeline, feasibility, give-get, change control.
    - Competitive match: competitor and evidence, comparability, requested response, trade required, validity, escalation.
    - Approval record (standalone, closes every type): decision, approved package, conditions, expiration and triggers, links - makes conditions enforceable in CPQ/CLM.
  - Either shape works: a per-lever register fits a desk where each lever routes to a different owner; one universal register fits a single desk owning all five.
- Pattern-to-policy loop: a monthly exceptions forum reviews recurring exceptions and produces a change backlog with owners and dates. Trigger question: "we approve this same exception routinely - should it become standard for this segment?" Promote or explicitly reject; never let a de facto precedent persist undocumented.

## Renewal treatment of a granted exception

Decide this at grant time, per exception class, never at the renewal itself. The treatment chosen becomes the template every future renewal argues from, which makes it the least reversible decision on this page.

The ordering below reasons from margin, renewal risk, and standing effort rather than from renewal data; the treatment is house policy either way. One adjacent published datum: ramp-deal renewals anchor to the last period's price.

Lead with sunset - it recovers the most margin for the least standing effort.

- margin recovered at renewal: sunset > step-up > grandfather-on-re-approval
- renewal risk carried (churn or escalation at the snap-back): sunset > step-up > grandfather-on-re-approval
- analyst effort: step-up > sunset == grandfather-on-re-approval
- compliance cost: grandfather-on-re-approval > sunset == step-up

**Sunset** - the exception expires at term end and price returns to standard. One dated clause written into the original approval, near-zero standing effort, recovers the whole concession, and stays reversible: nothing was promised, so grandfathering stays available later. Default treatment.

**Step-up** - staged return to standard over one or two renewals. Recovers the concession a year or two late and costs per-account tracking across two renewal cycles - a standing job for whoever owns the register - in exchange for removing the snap-back cliff.

**Grandfather on re-approval** - the concession carries into renewal, but only after a fresh approval at the tier that granted it. Near-zero effort at renewal and it buys the least: the account keeps the discount and cites it again the following year.

- Sunset == grandfather on effort: both are minutes of register work at renewal, what separates them is the price on the quote, not the hours.
- Sunset == step-up on compliance cost: both write a dated end state into the original approval, so neither creates an open-ended commitment, only the schedule differs.
- Grandfather ranks worst there because a renewal that re-grants the same term is exactly the evidence a customer cites at the next one.

Deleted, not demoted: **silent grandfather** - carry-over with no re-approval. An exception with no expiry is the defect the register exists to prevent, so it is not a treatment to weigh against the others; parked at the bottom of a menu it returns as the path of least resistance.

What this order starves: step-up. It is the only treatment that recovers margin without a cliff, and it loses every round because its tracking never ends. Promote it above sunset when a full snap-back has already driven churn or an escalation in that segment, or when the account is the reference or expansion base later deals depend on.
