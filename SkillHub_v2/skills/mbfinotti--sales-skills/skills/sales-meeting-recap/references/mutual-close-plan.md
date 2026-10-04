# Mutual close plan reference

A mutual close plan - also called a mutual action plan (MAP), mutual success plan, or joint execution plan - is a shared document between seller and buyer that maps the path from today through signature to go-live and first measured value. It is co-owned by the rep and a buyer project lead; a plan only the seller maintains is an internal close plan wearing a costume.

## When to introduce

Whether to build a plan at all is the rung ladder in SKILL.md; this file is the rung-3 detail. Once at rung 3, only the timing question is left.

- Introduce early - around the time the opportunity is created, not at negotiation. A late plan reads as a closing device.
- Evidence honesty: the widely circulated win-rate uplifts attributed to MAPs ("26%", "57-200%") are vendor self-reports with no disclosed sample, methodology, or control, and obvious selection bias - buyers willing to co-build a plan were already more engaged. Quote them, if at all, as directional vendor claims.
- The defensible value of the plan is coordination:
  - Dated, owned milestones.
  - A surfaced paper process.
  - Multithreaded visibility.

## Columns

| Column                  | Rule                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------- |
| Milestone / deliverable | Concrete and verifiable ("security questionnaire returned"), never "make progress" |
| Buyer owner             | One named person, never a team                                                     |
| Seller owner            | One named person; seller rows are what keep the plan mutual                        |
| Due date                | A calendar date, worked backwards from the buyer's target                          |
| Status                  | On track / at risk / blocked / done                                                |
| Notes / dependencies    | What this milestone waits on                                                       |

Ranked by value per unit of upkeep:

- efficiency: milestone == buyer owner == seller owner == due date > status > notes/dependencies. The first four tie because they are not separable - a row missing any one of them is not a lighter row, it is not a row at all ("What needs to happen / When it needs to happen / Who is responsible", Salesforce Salesblazer).
- effort: notes/dependencies (thinking per row, rewritten whenever the sequencing shifts) > status (one update per call, for the life of the deal - a standing job) > the irreducible four (written once, with the row).

Status and dependencies are practitioner extensions, not requirements. Cut both on a plan under roughly six rows, where the sequencing is visible at a glance and a status column is only a second place to go stale. Keep status once the plan spans more than a couple of calls: an out-of-date plan is worse than no plan.

## Milestone taxonomy

Work backwards from the buyer's compelling event or go-live date - never the seller's quarter-end - and group by phase:

- **Evaluation**: goals and requirements documented; demo to the full committee; technical validation or sandbox; success criteria agreed in writing.
- **Decision Process** (MEDDICC, Andy Whyte - the buyer's own steps to a decision, spanning technical validation and business approval): economic-buyer review; internal debrief; vendor selection.
- **Paper Process** (MEDDICC - "the series of steps that follow the Decision Process, detailing how you will go from decision to signature"): security review and questionnaires, DPA, MSA redlines and legal, procurement onboarding, signature. Surfacing these early is what stops a won evaluation from stalling for weeks in a contracts queue.
- **Post-signature**: implementation kickoff, onboarding, go-live, first measured value or ROI review. Extending past signature is what keeps the plan from reading as a device to extract a contract.

Fill order when the plan is half-built - efficiency: Paper Process > Decision Process > Evaluation > Post-signature.

- Paper Process: costs one question to the champion, prevents the multi-week contracts stall.
- Decision Process: costs a conversation, buys the buyer's real path.
- Evaluation: rows mostly write themselves from the call notes, so they add little the recap did not already carry.

The order starves the post-signature rows: they are cheap but buy trust rather than pace, so they lose every ratio round - promote them the moment the buyer reads the plan as a closing device.

## The Salesforce 5-part structure

Attributed to Salesforce's Salesblazer mutual action plan template:

1. **Objective or value statement** at the top: a two-way document helping the buyer reach their stated goal by their target date - the buyer's goal, not the seller's.
2. **Buying committee and responsibilities**: list known and unknown roles up front, so every gap becomes an explicit question for the champion instead of a silent hole.
3. **Key dates from both sides**, anchored to a buyer compelling event - an audit deadline, a contract expiry, a launch - never the seller's fiscal calendar.
4. **Deliverables and action items**, including the seller's own, to reinforce that the document is mutual.
5. **Projected outcomes and ROI past signature**: onboarding timeline and expected value at 6 and 12 months.

## Buyer co-ownership

- Never send a fully built plan cold. Propose 2-3 milestones drawn from what was actually agreed on the call, then ask for a working session to build the rest together.
- Get explicit sign-off once the plan is complete - a plan the buyer never approved is a seller wishlist.
- Open and close every subsequent call on the plan: what happens next, how the deal is pacing to the target date, what must be done before the next call.
- Keep seller-owned rows visible so the plan never reads as buyer homework.
- Expect resistance - buyers see "more work". Keep it to one page, not a monster spreadsheet, so the champion can forward it internally without apology.
- Agree where the plan lives (a shared document, a workspace the buyer can edit, mirrored into the CRM) and how often it is updated.

## Worked micro-example

- Vendor: a data-quality company selling to a logistics company.
- Buyer's compelling event: a Q2 audit deadline.
- Committee: VP Ops (champion), IT lead, procurement, COO (economic buyer).

| Milestone                                    | Buyer owner         | Seller owner | Due    | Status      |
| -------------------------------------------- | ------------------- | ------------ | ------ | ----------- |
| Security questionnaire + SOC 2 returned      | Marcus (IT)         | Nora         | Mar 12 | on track    |
| Technical review with IT team                | Marcus (IT)         | Nora         | Mar 17 | on track    |
| Procurement onboarding started               | Priya (Procurement) | Nora         | Mar 24 | not started |
| Economic-buyer review with COO               | Dana (VP Ops)       | Nora         | Mar 31 | not started |
| Signature                                    | Dana (VP Ops)       | Nora         | Apr 15 | not started |
| Go-live: re-keying removed from billing flow | Marcus (IT)         | Nora         | May 15 | not started |

How it is introduced inside the recap email, in one sentence: "Based on today, I've drafted the first three milestones toward your Q2 audit deadline - can we take 20 minutes Tuesday to build out the rest together?"
