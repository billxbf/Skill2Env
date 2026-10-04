# Reward Sizing, Economics, and Tier Design

How much to pay, how to frame the number, how to know the spend is incremental, and how to build a ladder that does not blow up.

## The ceiling: compute it first

No consensus formula recommends an amount, but a family of anchors converges on one discipline: **total reward cost per successful referral must stay under the gross profit the referred customer creates, and referral CAC must undercut the next-best channel.**

```
Reward ceiling = referred LTV x gross margin x allowed acquisition %
```

Example: LTV $1,200, margin 70%, willing to spend 20% of gross profit on acquisition → ceiling = $168. That is an upper boundary, not a recommendation - set the actual reward well below it.

Count the _total_ cost against the ceiling: referrer reward + friend reward + fulfillment + the margin impact of any discount. And remember credit costs margin only when redeemed, not face value.

## The anchors: pick a target inside the ceiling

Three anchors, ranked by efficiency - confidence in the number per unit of analysis work it takes to compute:

- **efficiency**: % of CAC > % of LTV > payback discipline
- **value** (tightness of the bound it puts on the P&L, strongest first): payback discipline > % of LTV > % of CAC
- **effort** (lightest first): % of CAC > % of LTV > payback discipline

| Anchor                          | Published range                                             | Effort to compute                             | Notes                                                                       |
| ------------------------------- | ----------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------- |
| % of CAC                        | 40-60% of blended/paid CAC                                  | Near-zero - finance already reports it        | Guarantees referral CAC beats the paid channel it displaces                 |
| % of LTV (combined, both sides) | 10-30% of first-year LTV consumer; 10-15% B2B               | An hour, or a week when churn data is thin    | The most common practitioner band                                           |
| Payback discipline              | Reward paid back by referred gross profit within ~12 months | A week - requires a cohort gross-profit curve | Compute against first 3/6/12 months of gross profit depending on churn risk |

**Default rung**: % of CAC. Move up to payback discipline when churn is front-loaded or the LTV figure is a guess dressed as a number - that is exactly the case the least-effort anchor cannot catch.

**What this order starves**: payback discipline, the strongest bound and the slowest to compute. It also swings hardest with who runs it: a team with a working cohort model reaches it in an afternoon, which re-ranks it first.

The commission-style anchor (a share of first-year contract value) is deleted rather than listed last - it prices a partner motion, which sits outside this skill. Route that case to `mbfinotti/partnerships-skills@affiliate-commission-structure`.

These bands are practitioner-published, not peer-reviewed - use them as starting points for a test, not as answers.

## The floor: the response curve is non-monotonic

The foundational result (Gneezy & Rustichini, "Pay Enough or Don't Pay at All", _Quarterly Journal of Economics_ 2000): introducing a _small_ payment produces worse performance than no payment at all, because it converts an intrinsically motivated favor into a poorly paid job. Applied here: a token reward against a meaningful purchase reads as insulting and can suppress referrals below the unpaid baseline.

Above the floor, returns diminish: past a moderate amount, social friction - not reward size - becomes the binding constraint, and doubling the reward moves the referral rate only marginally. So the shape is: **pay nothing (and lean on recognition), or pay meaningfully; never pay a little.** Fix friction and ask-timing before raising the number - placement of the ask moves participation more than size does.

Also justified by evidence when paying near the top of the range: referred customers are worth more. The strongest study in the field (Schmitt, Skiera & Van den Bulte, _Journal of Marketing_ 2011 - ~10,000 bank customers over 33 months) found referred customers churn ~18% less (persistently) and carry a 16-25% LTV premium. A €25 reward against a ~€40 value difference returned ~60% over six years.

Referred customers also go on to make 31-57% more referrals themselves (Gershon & Jiang, _Journal of Marketing Research_ 2024). Both effects vary by segment - the authors explicitly recommend selective rather than blanket rewards.

## Framing: the Rule of 100

Present whichever number _looks_ bigger:

- Price under $100 → frame as a **percentage** ("50% off" beats "$15 off" on a $30 plan).
- Price over $100 → frame as an **absolute amount** ("$200 off" beats "10% off" on a $2,000 contract).

At exactly $100 they are equal. Grounded in reference-dependence (people evaluate the number itself, not just what it denotes).

## Incrementality: the honest measure of the program

Roughly half of referral rewards in academic data go to customers who would have joined anyway (Kumar, Petersen & Leone's type-one vs type-two referral distinction, _Journal of Marketing_ 2010). The canonical freemium success story confirms the pattern: about a third of its signups already came from word-of-mouth _before_ its referral program launched - the program captured existing word-of-mouth rather than creating it.

Two diagnostics to build into the spec - **efficiency: holdout > on/off check**. Pausing the program costs no engineering but buys a read that seasonality and word-of-mouth spillover both confound; the holdout costs a week to design and actually answers the question. Fall back to the on/off check only when the base cannot be segmented cleanly.

1. **Holdout test**: withhold the program from a slice of customers or a geography. If total acquisition stays flat while CAC rises, rewards are cannibalizing organic referrals. Design the holdout strictly - referral is the channel most prone to word-of-mouth leaking into the control group.
2. **The crude on/off check**: pause the program briefly; if new-customer volume barely moves, most rewarded referrals were type-two.

Judge the program on **incremental CAC and referred-cohort retention**, never on the attributed-revenue dashboard.

## Tier design

Tier only when the fit conditions hold: high referral volume, plausible repeat referrers, and advocacy concentrated in a small group. A flat reward is simpler to explain, support, and account for - complexity kills participation.

Three shapes, ranked by efficiency - referrals unlocked per unit of build and upkeep:

- **efficiency**: flat > threshold ladder > stepwise
- **value** (extra referrals unlocked, strongest first): threshold ladder > stepwise > flat
- **effort** (lightest first): flat > stepwise > threshold ladder

The ladder outranks stepwise on efficiency despite costing more to build, because it is the only shape that raises output from a referrer you already have; stepwise merely re-times a payout the flat design would have made anyway.

| Shape            | Effort to run                                                                                                                           | Mechanism                                                               | Fits                                      |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------- |
| Flat             | Near-zero - one reward, one rule to explain                                                                                             | Same reward per referral for everyone                                   | Default; low volume; B2B                  |
| Threshold ladder | A quarter to build (milestone accounting, progress display, cap enforcement), plus a standing fulfillment job if the rungs are physical | Escalating rewards at cumulative milestones (3 → 5 → 10 → 25...)        | Newsletters, communities, high-volume B2C |
| Stepwise         | A week - one instrumented event per step, plus partial-payout accounting                                                                | Different rewards for different actions (share, signup, first purchase) | Multi-step funnels with long conversion   |

**Default rung**: flat. The ladder loses every round on ratio and is still the right answer for a high-volume, low-value-per-referral program - the condition that promotes it is the three-part fit test above, never the ratio. Re-rank against what the user already owns: a rewards platform that ships milestone tracking and progress bars out of the box erases most of the ladder's effort, and with it the gap to flat.

The cascading shape - commission on the referred network's own activity - is deleted from this menu rather than ranked last: it is an affiliate/network structure, and a user who needs it is designing a partner program. Route them to `mbfinotti/partnerships-skills@affiliate-commission-structure`.

Ladder rules, each traceable to a documented program outcome:

1. **Make the first tier trivially achievable** - low enough that a motivated customer can clear it from the people immediately around them. The hardest conversion is from zero referrals to one; an entry micro-milestone ("share once, get a small unlock") converts intention into action.
2. **Escalate perceived value faster than real cost.** Physical or in-product rewards with high perceived value and low unit cost (swag, exclusive access, product capacity) make ladders affordable; pure-cash ladders scale cost linearly with success.
3. **Show a progress bar.** The goal-gradient effect - people accelerate as they approach a goal - is the main behavioral lever of a ladder, and it only works if progress is visible.
4. **Cap the top tier, always.** The best-documented failure in this discipline is an automaker's uncapped referral ladder whose "secret levels" escalated to free cars, was killed for "adding too much cost", relaunched cheaper, and eventually shut down for good. An uncapped ladder is an open-ended liability that grows with your most successful advocates.
5. **Raise the friend's incentive modestly at higher tiers too**, not only the advocate's - top referrers reach progressively colder audiences who need more reason to act.

## Budget and P&L notes

State in the spec who owns the cost line and how it is booked:

- Practice at scale treats referrer rewards as customer-acquisition cost, a sales & marketing expense.
- Any payment beyond the fair value of the referral service counts as a reduction of revenue.
- Friend-side discounts are margin give-up.
- Unredeemed credit is a liability until it expires.

Getting finance sign-off on this before launch is cheaper than re-architecting the program after the first audit question.
