# Worked accelerator curve

A complete curve for a new-logo AE plan, expressed entirely in ratios so it transfers across markets and price levels. Substitute the org's own quota and OTE to price it.

## Assumptions

- Pay mix 50/50 (variable share of OTE = 0.5).
- Quota:OTE ratio 5x (from the quota plan - see mbfinotti/sales-skills@sales-quota-setting).
- The identity: 50/50 mix at 5x quota:OTE implies roughly a 10% blended commission rate on new business, and compensation cost of sales lands near 20% of new ARR.
- Fix any two of {mix, quota:OTE, rate} and the third is determined.
- Accelerator bound: accelerated rate ≤ 1 ÷ 0.5 = 2.0x the base rate. Anything above 2x on a 50/50 plan pays out faster than the revenue it rewards.

## The rate table (marginal)

| Attainment band                       | Rate multiplier    | Rationale                                                                   |
| ------------------------------------- | ------------------ | --------------------------------------------------------------------------- |
| 0-40%                                 | 0.5x (decelerated) | Below the floor the plan stops pro-rating; pairs with the accelerator below |
| 40-100%                               | 1.0x               | The base commission rate                                                    |
| 100-130%                              | 1.5x               | First accelerator band                                                      |
| above 130%                            | 2.0x               | Second band, at the bound exactly                                           |
| any single deal > 25% of annual quota | windfall review    | Manual review clause instead of a cap                                       |

Each band's rate applies **only to attainment inside that band** (marginal application).

The decelerator here is a deliberate choice, not a default: it funds the 1.5x/2.0x bands. Running the same accelerators with no decelerator is also legitimate:

- **Majority modern-SaaS position:** dropping decelerators as demoralizing.
- **Minority position:** keeping them for behavior control.

Choose explicitly and record why.

## Worked payout at 120% attainment

Payout as a share of target variable pay:

- 0-40% band: 40 × 0.5x = 20 points
- 40-100% band: 60 × 1.0x = 60 points
- 100-120% band: 20 × 1.5x = 30 points
- **Total: 110% of target variable** for 120% attainment.

The rep can reconstruct this on a napkin - that reconstructability is the design goal, not a side effect. Line of sight survives because each band is independent.

## Cost model before publishing

Model at least these scenarios against last cycle's actual attainment distribution before the rate table ships:

1. **Expected case:** last cycle's distribution replayed under the new table - total payout vs the current plan's actual payout.
2. **High-attainment case:** 20% of the team lands above 150%. On the table above, a rep at 150% earns 20 + 60 + 45 + 40 = 165% of target variable. If that outcome across a fifth of the team breaks the budget, fix the accelerator _rate_ now - never bolt on a cap after publication.
3. **Windfall case:** one outsized deal per quarter routed through the review clause - confirm the clause's trigger threshold catches it.

Survey grounding:

- Uncapped accelerators are the overwhelming B2B SaaS norm (82% of companies in ICONIQ Growth's May 2023 survey of 236 GTM executives), typically boosting a top performer's payout 20-30% above quota - the modeling above is what makes uncapped affordable.
- WorldatWork's separate "3x rule" sizes total upside: a 90th-percentile performer should earn roughly 3x target incentive, anchored to the labor market's own 90th-percentile pay (some industries 2x, some 4x).

## Negative example 1 - the cumulative table

Same bands, but crossing 100% reprices **all prior attainment** at 1.5x. At 99% the rep holds 79 points; at 101% they hold ~121 - a 2-point attainment move triples the marginal payout.

Reps hold deals at quarter-end to time the cliff, and mid-period the rep cannot compute what a deal is worth. This is the named source of the cliff effects and line-of-sight erosion the marginal table avoids.

## Negative example 2 - the cap

Replacing the windfall clause with a hard payout cap (e.g. nothing above 130%) tells the best rep on the team to stop selling in the strongest month of their year, and deals slip to next period at the rep's convenience, not the company's. Retroactively capping payouts that the plan document called "uncapped" has produced actual litigation and settlements - _Comin and Briggs v. IBM_ (N.D. Cal.) settled for $4.75M in 2023 on exactly this fact pattern - treat cap language as a counsel-gate item at step 9, not a budgeting lever.

## Adapting the shape

- **Higher variable share** tightens the bound: at 60% variable, the ceiling is 1 ÷ 0.6 ≈ 1.67x - the accelerator must be flatter.
- **Enterprise plans** (fewer, larger deals) lower the windfall threshold and lean harder on the review clause, since one deal can be half a year's quota.
- **Gates and kickers** (e.g. a strategic-product attach goal) can frame the same incentive as a carrot (richer acceleration if hit) or a stick (no acceleration if missed). Loss-framing typically produces the stronger behavioral response (WorldatWork), but every gate spends the clarity budget of the rule of three.
