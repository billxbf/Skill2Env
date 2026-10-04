# Step-size figures - what platforms document, what practitioners claim, and where the folklore came from

Load this when the user asks where a step-size number comes from, challenges the "20% rule", or when the plan needs its evidence labels audited.

Labels:

- **documented** - platform help center.
- **research** - peer-reviewed or disclosed methodology.
- **folklore** - practitioner-repeated, no primary source.

## The "raise budget 20% every 72 hours" rule, traced

The earliest clean attribution is Charlie Lawrance in Social Media Examiner, September 2021: "In my agency's communications with Facebook, they always recommend the slow scale. This is where you increase your ad spend budget on a campaign or ad set no more than 20% in a 72-hour period." That is a second-hand relay of unverified account-rep advice - folklore. Everything downstream repeats it.

Two genuine platform artifacts likely hardened the folklore into a perceived rule:

- Meta's automated-rules interface ships a preset action literally labeled "Increase budget by 20%" (documented). A UI default, not a scaling law.
- Google documents a real 20% cadence - **for bids, on Display campaigns only**: "increase or decrease your bids by 20% and wait a week between changes" (documented). Bids, not budgets; one campaign type, not a universal rule.

## What platforms actually document

**Meta, Google, TikTok and LinkedIn publish no budget-change percentage - Pinterest is the confirmed exception.** What each one does document is below; the "20%" figure applied to the first four platforms is inferred, never stated by them.

| Platform  | Documented reset behavior                                                                                                                                                                                                     | Documented budget %                                                                                                                       | Documented hold/wait guidance                                                                      |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Meta      | Significant edits restart learning; bid/budget changes are significant "depending on the magnitude of the change". ~50 optimization events per ad set per week to exit learning                                               | None - "20%" is inferred                                                                                                                  | Judge after exiting learning, ~7 days typical                                                      |
| Google    | Budget, target, and bid-strategy changes can trigger relearning; learning can take up to 3 weeks or 1-2 conversion cycles                                                                                                     | None for budgets (20% is bids-on-Display only)                                                                                            | Performance Max: run 6 weeks, ramp 1-2 weeks, before evaluating                                    |
| TikTok    | Significant budget/bid/target changes reset; ~50 conversions per ad group is the main exit indicator                                                                                                                          | None as a %                                                                                                                               | Volatility declines past ~25 results/7 days                                                        |
| LinkedIn  | No documented discrete learning reset                                                                                                                                                                                         | None                                                                                                                                      | "~50 conversions/month for stable auto-bidding" is practitioner, not official                      |
| Pinterest | Performance+ campaigns cycle between learning and optimized states; a "Learning" indicator shows during the cycle, and Pinterest's own help documentation instructs waiting for it to disappear before changing ads or budget | **20-30%, stated directly** ("Gradually increase your budget by 20-30% based on performance," per Pinterest's own Performance+ help page) | Learning indicator clears in "on average two weeks," varying by spend, conversions, and engagement |

Reddit, Amazon, and X were also checked: none publish a learning-phase reset percentage. Amazon's system is keyword/bid-based rather than governed by a formal learning-phase reset mechanic; Reddit's newer Max campaigns lean on automated optimization without disclosing a threshold; X has no official documentation on this at all, only third-party guides describing a general first-week volatility window.

Note the distinction the folklore erases: the ~50-events threshold is a **delivery-stability** floor, not a profitability-significance test. Clearing it says delivery will be steady, not that the campaign earns money. Both are required; they answer different questions.

## Practitioner step-size positions - do not blend into one number

Deliberately unranked, and not a menu. Each entry is a different operator's stated practice under different conditions, so ordering them by efficiency would invent a comparison none of them made. The ranked menu of ways to _arrive at_ a step size lives in How to ship a step size, below.

- **Demand Curve case study** ($62k → $493k/month over 90 days): "Budgets increased in 15-20% increments, avoiding the CPA spikes that come with aggressive budget jumps." One account's stated practice rather than a controlled study - folklore. Each spend tier was paired with a structural change (bidding pivot, new campaign types, geo segmentation, allocation automation), not the same lever pulled repeatedly.
- **An open-source B2B playbook:** +20% every 5 days, "never +30%+ in one move - resets learning" - folklore, internally consistent. Its scaling protocol requires:
  - Proven-ad count.
  - Frequency < 3.0.
  - Cost per qualified lead at or under target for 2+ consecutive weeks.
  - 3+ replacement creatives staged.
- **Tier 11 (Ralph Burns, Kobi Topaz):** no fixed percentage. Each push is gated on re-checking that contribution margin held - validate-then-push, not a cadence. Their nCAC (12-month LTV → gross margin → minus refunds → minus fulfilment/OpEx → target profit margin) is the ceiling that authorizes spend; the stated risk of skipping it is insolvency.
- **Common Thread Collective (Taylor Holiday, Andrew Faris):** front-load measurement rigor - server-side tracking, an incrementality-derived defensible ROAS target - then "push it there" aggressively. Explicitly against slow percentage laddering once the target is trusted.
- **The no-universal-number school (open-source):** "No universal percentage is safe"; "Change the target by N% every N days" as a universal rule is listed by name as an unsafe recommendation. Step size and timing come from platform simulations, account history, conversion cycles, and blast-radius limits.
- **Ben Heath (Heath Media):** an automated rule scaling in small increments (his own example: 3%) against a maximum daily cap, but the percentage itself should shrink as absolute spend grows - comfortable taking a campaign from £10 to £30/day (a 200% jump) but never £1,000 to £2,000/day (the same 200%) in one move, because a bigger audience reached at higher spend contains weaker prospects, so the same percentage risks a worse marginal cohort. Explicitly against tripling or quadrupling budget just to exit Learning Limited, which spikes cost per conversion instead of fixing it.
- **AJ Wilcox (B2Linked, LinkedIn Ads specifically):** no fixed step size; "nail it, then scale it" - feed a campaign that is already proven rather than laddering a fixed percentage on a schedule. A diagnostic for whether a bid increase is still buying proportional volume: raise bids 20% and check the resulting click increase - anything under 20% back means diminishing returns have set in and the increase should be pulled back, not pushed further.

## Rollback recipes

All practitioner conventions, none platform law:

- Cost per qualified lead exceeds 1.5x target after a scale step → cut budget 20-30% immediately, stabilize two weeks, resume at +10%/week.
- A ROAS drop persisting beyond 5-7 days → revert to the prior budget.
- Never act on a fixed multiple alone: check sample size, conversion lag, tracking outages, downstream lead quality, seasonality, and active experiments first - "a doubled CPA on 6 conversions with a 14-day conversion lag is noise."

## How to ship a step size

Teach the derivation and the constraint, not the number. Two constraints bind every rung:

1. The step must be small enough that the platform does not classify it as a significant edit (magnitude-dependent, undocumented - err small).
2. The hold must cover the learning window plus this account's conversion lag.

Inside those constraints, three ways to arrive at the number, ranked by value returned per unit of effort - the axes disagree, so read all three:

- efficiency: `account history > concrete default > validate-then-push`
- effort: `validate-then-push > account history > concrete default`
- value: `validate-then-push > account history > concrete default`

1. **Account history - the default.** How did efficiency respond to the last three budget changes of known size? About an hour in the change log, and the only rung whose number cannot be folklore.
2. **The 15-20% concrete default.** Near-zero effort, and a defensible opening guess only. Ship it exclusively alongside the explicit instruction to recalibrate. Use when the account has no change history to read yet.
3. **Validate-then-push.** No percentage at all: serious practitioners refuse any universal number, and the strongest scaling operators replace the ladder entirely with validate-then-push against a causally measured target. A week to instrument plus a hold spent waiting, and it presupposes causal measurement the account already trusts - which is exactly when it should lead instead of trail.

The order is a default, not a law. Re-rank it against what the account already owns: a live incrementality program makes rung 3 nearly free, and an empty change log leaves only rung 2 until the account has stepped a few times.
