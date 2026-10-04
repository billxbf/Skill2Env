# Worked example: the score-to-tier bridge

A mid-market B2B SaaS company, ~$60K ACV, with a qualified list of 600 accounts. The upstream segmentation skill maintains a 0-100 composite fit score per account; an intent provider feeds a 0-100 signal score. Six reps carry named books.

## Step 1-3 - the composite

The fit score arrives as given. The signal score decays on a 90-day timer; fit points persist. Two composition options:

- **Additive composite**: e.g. 70% fit + 30% signal, one 0-100 number. Simple, readable, the common default.
- **Multiplicative (fit × intent)**: rewards accounts strong on _both_. Worked contrast from practice: fit 6 × intent 80 = 480 beats fit 2 × intent 100 = 200 - a pure-intent account with weak fit still loses to a strong-fit account with moderate intent. Choose this when intent data is noisy and weak-fit accounts keep spiking to the top.

## Step 4 - cutoffs, then calibration

Start from the published convention - 80+ → Tier 1, 50-79 → Tier 2, below 50 → Tier 3 - then calibrate against capacity, because the convention knows nothing about this company's score distribution.

Calibration on the 600-account list: 6 reps × a 15-account Tier-1 cap = 90 Tier-1 slots. If 140 accounts score 80+, the cutoff moves up (here, to ~86) until the count fits under 90 - the cap wins over the round number, always. A related practitioner convention sets the qualifying threshold to capture roughly the top 20% of accounts by score (e.g. a threshold of 70 when the average account scores ~35); use whichever calibration the score distribution supports, but let capacity have the final word.

Letter-grade variants (A ≥80, B ≥65, C ≥50, D ≥35, F <35) and dimension sub-caps (e.g. a 100-point score split into fixed per-dimension maxima) are equivalent mechanics - keep whichever the upstream score already uses rather than converting.

## Step 5 - gates

Firmographic must-haves per tier, tighter as tiers rise:

| Account                                            | Composite | Gate check                                 | Tier                  |
| -------------------------------------------------- | --------- | ------------------------------------------ | --------------------- |
| A - 1,200-employee logistics firm, target vertical | 88        | passes all Tier-1 gates                    | Tier 1                |
| B - 40-employee startup, intent spike              | 84        | fails Tier-1 size gate (min 200 employees) | Tier 2, watch-flagged |
| C - 800-employee firm, adjacent vertical           | 74        | passes Tier-2 gates                        | Tier 2                |
| D - 500-employee firm, no signal history           | 47        | -                                          | Tier 3 nurture        |

Account B is the reason gates exist: intent alone must not buy a Tier-1 slot the capacity model can't afford to waste.

## Step 6 - the override budget

Sales leadership may override the mechanical assignment for strategic value the score doesn't carry (reference logo, expansion whitespace, partnership leverage). Bound it: e.g. at most 10% of Tier-1 slots, each override logged with its reason and reviewed at the quarterly tier review. An unlogged override channel is how tier collapse starts.

Example: a 78-scoring account is promoted to Tier 1 because it is the flagship logo of the target vertical and two open deals reference it. Logged, one slot spent.

## Step 7-8 - publication and routing

Publish per-dimension sub-scores next to each assignment so a rep can see that account C sits in Tier 2 on vertical fit, not on a data error. Route mechanically: Tier 1 → immediate named assignment; Tier 2 → sequence plus SDR follow-up within an agreed SLA; Tier 3 → marketing nurture until a signal promotes it. Recalculate on the governance schedule, with signal points decaying and fit points persisting.

## Negative example - what not to ship

The same 600-account list, cutoffs left at 80/50 without calibration, no gates, no cap: 270 accounts land in "Tier 1" because the fit model was generous, six reps nominally own 45 top-tier accounts each at an ACV whose capacity math supports 20-50 _total_ accounts per rep, and within a quarter reps privately re-triage their books while the official tiers go stale. The system reports tiering; the floor runs on judgment. This is tier collapse plus labeling-without-differentiation in one artifact - the two checks that would have caught it are the capacity calibration in step 4 and the SLA encoding in step 8.
