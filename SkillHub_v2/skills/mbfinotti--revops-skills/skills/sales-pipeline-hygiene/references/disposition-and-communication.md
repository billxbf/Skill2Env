# Dispositions and the Communication Plan

## The Evidence Test per Disposition

Decide each flagged deal by what the buyer-side evidence supports, not by what cleans the dashboard fastest. For the stale working list, only two answers are acceptable: revive it with a real next step and a validated close date, or close it out (ORM).

| Disposition                         | Evidence that supports it                                                                                                                                        | Trap to avoid                                                                                              |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Close lost, real reason code        | Stacked signals all negative: no buyer response past the silence window, champion unresponsive, no economic-buyer engagement, "what has to happen" has no answer | Closing a merely quiet deal - a legal or procurement stall is exempt, not dead                             |
| Move to nurture                     | Buyer said "not now" with a plausible future trigger (renewal date, next fiscal year)                                                                            | Nurture as a euphemism for lost - nurture needs a re-entry trigger and date, or it's a graveyard           |
| Re-stage backwards                  | Deal is alive but the stage claims buyer commitment the record can't show                                                                                        | Punitive demotion of every flagged deal - restage only where the stage genuinely overstates position       |
| Re-date with evidence               | A concrete buyer-side answer plus at least one moving stacked signal (MAP progress, legal entry, champion responsive)                                            | Accepting a seller-side answer ("I'll follow up") as evidence; updating the deal plan but not the CRM date |
| Keep, with named next step and date | Deal is healthy; the flag was a missing or stale field                                                                                                           | "Keep" without writing the next step - that re-flags the same deal next audit                              |

The manager decides, never the rep alone - do not let the seller grade their own homework (LeanLayer) - and never automation alone: flag automatically, but let managers make the final call on removal; automated deletion creates distrust (ORM). Non-standard re-stages and deal splits route through the deal desk. Every decided disposition records the decision, a named owner, and the reason.

## Reason Codes

A generic dropdown makes loss data garbage: a rep who dropped the ball still clicks "Price" to save face. Design the closed-lost list so honesty is possible:

- A clear, finite list with written definitions, plus optional sub-reasons (SalesHive):
  - No decision.
  - Lost to competitor.
  - Product fit.
  - Budget.
  - Timing.
  - Wrong persona.
- Require a one-sentence context note, ideally in the prospect's own words.
- Include no-fault codes: "we stopped pursuing / dropped follow-up", "never a real opportunity (audit cleanup)". The audit-cleanup code keeps bulk hygiene closures out of genuine competitive-loss analysis.
- Review the code distribution each audit; a code taking >40% of volume is hiding several truths.

## Reopen vs New Record

Both camps argue about where a returning buyer's record lives, so put them on one yardstick: what each buys, against what each costs in configuration, standing manager gates, and reversibility.

- **New record, linked back to the closed-lost one** (reporting-integrity camp - Varicent; HubSpot community): once closed-lost, a deal stays closed-lost; the returning buyer gets a fresh opportunity related to the old one. Costs near-zero - a written policy and a relate-records step - and stays reversible, since a policy changed next quarter rewrites nothing already recorded. Cycle-length and loss-reason series survive intact.
- **Reopen the closed-lost record** (pipeline-recovery camp - Letterdrop): reopening done correctly can recover 10-20% of lost pipeline, but only when the buying motion has genuinely resumed and with the close date reset. Costs about an hour of configuration (a gated reopen path, a "reopened" flag) plus a standing manager gate on every reopen, and it is the irreversible option: cycle length and loss reason are rewritten in place, and no later report can separate a reopened deal from an original one.

- value: reopen == new record - the 10-20% recovery is bought by working the returning buyer again, not by which record holds them, and a linked new record captures the same revenue with the same effort from the rep
- effort: reopen > new record - a gated path and a standing gate against a one-line policy, and the damage to the reporting series cannot be undone once records exist under the rule

Default to the linked new record. Two conditions genuinely flip that, and where either holds there is no honest ranking - only a choice about which failure the org would rather live with, distorted cycle and loss reporting or recovery it cannot credit:

- Attribution or comp credits the original opportunity's owner, so splitting one buyer across two records mis-pays someone.
- Reporting cannot join a new record to its predecessor, which quietly costs the linked-record option the recovery history it exists to preserve.

Either way, restrict casual stage movement out of Closed-Lost so reps cannot reset stale counters by reopening.

## The Pipeline Amnesty - Run Before Enforcement

Named practice (ORM): give reps one day per month to clean their pipeline with **no penalties** for removing deals. Frame it as a fresh start, not an audit, and exclude amnesty-removed deals from win-rate calculations. This is the antidote to the honesty problem - reps hide dead deals because closing them hurts coverage and win-rate math; the amnesty removes the punishment for telling the truth.

Run an amnesty _before_ the first enforcement pass whenever the sizing step finds more than 20-30% of pipeline value stale: enforcing rules against a book that is one-third dead punishes the honest and rewards whoever games first.

## The Communication Plan - Before Enforcement, Not After

The posture throughout is coaching, not compliance - governance should feel like guardrails, not a cage, and a stale flag is the start of a coaching conversation, not a write-off. Communicate whatever gets automated; otherwise, to the sales team, it didn't happen (RevOps Co-op). Sequence:

1. **Announce the rules before the first flag**:
   - The meaningful-activity definition.
   - The per-segment thresholds, and what they're derived from.
   - What a flag means (a review conversation, never automatic closure).

   A rep who first meets a rule by being flagged experiences an ambush.

2. **Publish the exception list at least 12 hours before the meeting that works it** (ORM: any meeting that starts by pulling a report has already failed). Managers arrive with records that failed rules, not opinions about effort.
3. **Run the review inside existing rituals as coaching.** Per deal, walk: here is the flag, here is the evidence, what do you know that the record doesn't?
   - Keep executives out of the rep-level session.
   - Keep hygiene-score comparisons inside 1:1s and pipeline reviews - a company-wide leaderboard invites gaming.
4. **Publish the outcome**:
   - Deals reviewed.
   - Dispositions by type.
   - Pipeline-value delta.
   - KPI movement.

   Showing that most flags ended in "keep, with next step" or "re-date with evidence" - not mass closure - is what buys trust for the next cycle.

5. **Announce the cadence and the escalation path.** A one-off purge trains reps to wait it out. Exceptions that clear within a week are a functioning process; exceptions that age past thirty days signal a rule that needs to exist in the system rather than in a conversation (ORM).

**Compensation warning**: never tie comp to field completion - it produces fast, complete, low-quality data (ORM). If any variable comp touches hygiene, tie it to forecast accuracy (an outcome), not field completion (an input that invites junk entry).

## Mass-Cleanup Change Management

Manager attention is the scarce input in a mass cleanup, so spend it by pipeline value recovered per minute of review: **bulk proposal with an override window > per-deal conversation**.

- value: per-deal conversation > bulk proposal - a conversation recovers the deals a rule would have wrongly closed, which is only worth doing on deals carrying real pipeline value
- effort: per-deal conversation > bulk proposal - minutes of manager review per record against one pass over a list

Split the two at a value threshold derived from the pipeline's own value distribution, never at a fixed amount: below it bulk-apply, above it converse. The split moves with who executes it - a manager already running a weekly pipeline review absorbs more conversations than one who reviews monthly, so lower the threshold for them.

- Never let RevOps close deals unilaterally, and never auto-close on a rule.
- On SLA breach, auto-tag for manager review.
- Batch proposals, give managers a stated override window, then apply. Silence after the window is consent to the _proposed_ disposition the rep already saw, not to a surprise.
- The override window applies on both sides of the threshold.
- Use the "never a real opportunity (audit cleanup)" code for bulk closures so rep win-rate and loss analysis stay clean; amnesty removals are likewise excluded from win-rate math.
- Scheduled auto-close is acceptable only when all of the following hold:
  - High-velocity pipelines.
  - Pre-qualified early stages.
  - Referencing last-activity date.
  - Sales-leadership buy-in.
- Handle dibs deals as an ownership decision: settle who holds the account (territory rules, a named-account list, or release to marketing), then close the placeholder record. Closing without settling ownership regenerates the problem within a quarter.
