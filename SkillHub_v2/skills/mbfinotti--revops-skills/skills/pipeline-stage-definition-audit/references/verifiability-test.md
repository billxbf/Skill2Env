# The Buyer-Verifiability Test

A stage definition passes only if its exit criterion satisfies all three conditions:

1. **Buyer-sourced** - it names something the buyer did, said, or agreed to. Not something the rep did to the buyer.
2. **Observer-independent** - a third party could confirm it without asking the rep's opinion.
3. **Recorded** - the evidence lives in a checkable place: a field, an attached document, a logged meeting with the named attendee, a signed artifact, a product event.

Operational form: **could two different managers, looking at the same deal record, independently reach the same verdict on whether the criterion is met?** If the answer depends on who is looking, the criterion fails.

## Passing vs failing wording

| Verdict | Criterion                                                                                                             | Why                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| FAIL    | "Demo scheduled"                                                                                                      | Rep activity; says nothing about buyer conviction |
| FAIL    | "Proposal sent"                                                                                                       | Rep pressed a button; buyer may never open it     |
| FAIL    | "Presentation delivered"                                                                                              | Rep task completion                               |
| FAIL    | "Strong relationship with champion"                                                                                   | Unobservable opinion                              |
| FAIL    | "Rep has confirmed budget"                                                                                            | Rep-attested; not independently checkable         |
| FAIL    | "Buyer is engaged"                                                                                                    | No observable event; two managers will disagree   |
| PASS    | "Buyer named the budget owner and made the introduction (intro email or meeting logged with that person as attendee)" | Buyer act, observable, recorded                   |
| PASS    | "Buyer's security team completed its review (assessment doc or approval email attached)"                              | Buyer organization acted; artifact exists         |
| PASS    | "Buyer agreed in writing to a mutual evaluation plan with dates (plan attached, buyer edits or reply visible)"        | Written buyer commitment                          |
| PASS    | "Buyer admin invited two teammates and connected billing details" (transaction/PLG)                                   | Product events; machine-recorded                  |
| PASS    | "Buyer proposed the contract-review call and put it on their own calendar"                                            | Buyer-initiated, calendar-verifiable              |

## Writing criteria that pass

- Start every criterion with the buyer as the actor: "buyer confirmed…", "buyer's legal returned…", "buyer scheduled…".
- Name the evidence location in the criterion itself - a criterion without a home field or artifact passes review and fails in production.
- Keep 2-4 criteria per stage (practitioner consensus). One is too easy to game; five dilute attention.
- Gate advancement the way MEDDPICC is commonly operationalized: score each criterion red/yellow/green, require all-green to advance. Yellow means "rep believes it, evidence pending" - a useful coaching state, never a passing one.
- The rep still records the entry; verifiability means the entry points at something a manager can check, not that the rep is distrusted.

## Gartner buying-job mapping

Map every stage to the buying job its exit evidence proves complete.

- A stage that maps to no job is rep activity in disguise.
- Several stages crowding one job are redundant.

| Buying job             | Buyer-verifiable evidence that it happened                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Problem Identification | Buyer articulated the problem and its cost in their own words (notes quoting the buyer, discovery recording)            |
| Solution Exploration   | Buyer requested evaluation access, attended a working session they scheduled, named the alternatives they are comparing |
| Requirements Building  | Buyer shared written requirements, an RFP, or success criteria they authored                                            |
| Supplier Selection     | Buyer confirmed shortlist status in writing; buyer's procurement engaged with the vendor                                |
| Validation             | Buyer's technical/security/legal teams completed their checks; references were taken by the buyer                       |
| Consensus Creation     | Buyer introduced the economic buyer or additional stakeholders; buying group co-signed the mutual plan                  |

Buyers loop through these jobs non-linearly, so evidence may arrive out of stage order - the map validates that each stage's exit proves _some_ job, not that jobs happen in sequence.

## The scorecard anti-pattern

Do not convert a qualification framework into the stage list. Force Management's warning: there are no "MEDDIC stages 1-6."

Each qualification dimension (pain, champion, economic buyer, decision process…) is a separate field updated continuously through the deal. The stage records where the _buyer_ is, not the scorecard.

A pipeline whose stages are scorecard letters can no longer answer "where is this buyer in their purchase?", the one question stages exist for.

## Negative example - a rewrite that still fails

A team replaces "Proposal Sent" with "Value confirmed and proposal in play." It sounds buyer-centric, but fails all three conditions:

- No buyer act is named.
- "Value confirmed" is the rep's opinion.
- Nothing is recorded.

Two managers reviewing the same deal disagree immediately.

The passing rewrite names the act and the artifact: "Buyer's evaluation lead confirmed in writing that the proposal matches the requirements they authored (email attached), and named the decision date."
