# Worked Examples

Both examples are fictional companies; the mechanics are the point.

## Positive example - mid-market B2B SaaS, six named candidates

Scenario: a workflow-automation vendor (sales-led, ~$40k ACV) must decide where two alliance managers' capacity goes next year. Goal: partner-sourced pipeline in the enterprise segment. Capacity: roughly eight alliance-manager-months a year, which the team also describes as "two managed alliances".

**Gates.** Six candidates enter. One - a fast-growing point solution - fails the viability gate (two down-rounds, key-team departures, evidence cited). Five proceed.

**Scorecard.** Criteria and justified weights:

- Complementarity 25% - "value only exists combined - their data layer, our workflow engine".
- Compatibility 20% - "enterprise deals die on mismatched deal cadence".
- Goal fit 15%.
- Verified overlap 10% - "capped - overlap sample is 60 accounts".
- JVP strength 15%.
- Alliance readiness 15%.

| Candidate                            | Value composite | Effort (mgr-months/yr) | Value ÷ effort | Risk composite                                        | Rank |
| ------------------------------------ | --------------- | ---------------------- | -------------- | ----------------------------------------------------- | ---- |
| DataFabric (data platform)           | 4.3             | 4                      | 1.08           | Medium                                                | 1    |
| SecureID (identity vendor)           | 3.1             | 3                      | 1.03           | Low                                                   | 2    |
| FormaCRM (CRM vendor)                | 3.6             | 5                      | 0.72           | Medium                                                | 3    |
| CloudSuite (hyperscaler marketplace) | 4.1             | 7                      | 0.59           | Medium-high (envelopment)                             | 4    |
| BrightBI (analytics)                 | 2.9             | 6                      | 0.48           | High (co-innovation: value needs their unshipped API) | 5    |

Read the CloudSuite row before anything else. It is second of five on value and fourth after dividing, because 7 manager-months buys 4.1 where SecureID's 3 buys 3.1. Ranking this table by the value column alone - the intuitive move, and the one the negative example below is built on - puts CloudSuite in a two-slot shortlist and leaves SecureID out.

**Capacity line.** Drawn on summed effort, not headcount: DataFabric (4) plus SecureID (3) is 7 of the 8 available manager-months; adding FormaCRM (5) would need 12. The headcount phrasing and the effort sum happen to agree here - they stop agreeing the moment one candidate costs double another.

**Sensitivity.** ±20% shifts on every weight leave the top two intact. DataFabric and SecureID sit 4% apart, inside the 5% tie-band, but both fit inside capacity, so this tie needs no breaking - say so rather than manufacturing a tiebreaker.

The live question is CloudSuite: it enters the shortlist only if a scoped first phase cuts its effort below ~4 manager-months. Positions 4-5 are 21% apart and are not a tie.

BrightBI is the co-innovation candidate the ratio structurally starves, and here the last place is the right answer twice over: the goal is pipeline rather than a product gap, and the API the joint value depends on carries no ship date. An undated dependency earns a recycle, never a reserved capacity slot.

**Verdicts.**

- DataFabric: go - first-value milestone: integration live plus three joint opportunities in two quarters.
- SecureID: go - first-value milestone: identity integration live plus two joint enterprise opportunities in two quarters.
- FormaCRM: hold - re-entry trigger: an alliance-manager hire.
- CloudSuite: hold - re-entry trigger: a scoped phase-one under 4 manager-months, with envelopment safeguards written into the marketplace agreement.
- BrightBI: recycle - re-score when the dependent API ships.

One kill, two holds, one recycle: the ranking made a real decision.

Why this works:

- The capacity line forced a choice.
- Every weight has a reason.
- Effort divided value instead of sitting in a column nobody used.
- The gate failure was not traded away.
- The instability that existed was disclosed.
- Every non-go candidate left with a trigger, not a shrug.

## Negative example - the logo-collecting scorecard

Same vendor, same six candidates, the way this goes wrong in practice:

| Candidate         | Brand (20%) | Market size (20%) | Overlap (20%) | Exec relationship (20%) | Revenue potential (20%) | Total |
| ----------------- | ----------- | ----------------- | ------------- | ----------------------- | ----------------------- | ----- |
| CloudSuite        | 5           | 5                 | 4             | 5                       | 5                       | 4.8   |
| MegaCorp Platform | 5           | 5                 | 3             | 4                       | 5                       | 4.4   |
| DataFabric        | 3           | 3                 | 4             | 2                       | 4                       | 3.2   |

What is wrong, line by line:

- **Equal weights, no justifications** - nobody decided anything; the format decided. This is the arbitrary-weights defect in its purest form.
- **Brand and executive relationship as 40% of the score** - logo halo and prior personal ties are the documented revealed criteria that crowd out fit; the evidence says complementarity and compatibility should dominate, and neither appears at all.
- **No effort column** - CloudSuite at 7 manager-months and DataFabric at 4 are scored as if capacity were free.
- **No gates** - MegaCorp Platform's pending security review would have been a conditional-go at best; here it ranks second on charm.
- **No risk scoring** - CloudSuite's envelopment exposure is invisible; the scorecard is recommending building on a platform that ships competing features.
- **No sensitivity check, no tie-band** - the 4.8 vs 4.4 gap reads as decisive and would not survive a modest re-weighting.
- **No capacity line, no verdicts** - all six candidates stay "in play", which means the loudest sponsor wins later, off the record.
- **The revenue-potential column is unevidenced** - TAM-flavored guesses scored as data.

The output looks rigorous - a table, percentages, a winner. It is a ratified gut feeling, and the two candidates it crowns are the famous one and the sponsored one. When a user brings a scorecard shaped like this, rebuild from the gates up rather than tuning its numbers.
