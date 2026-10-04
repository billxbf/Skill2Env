# Report shape and worked examples

## Report shape

Present in this order, section by section, each gated on user approval:

1. **The miss, quantified** - forecast vs. actual per level and category, signed bias and absolute error, the error definition used.
2. **Attribution table** - every gap dollar to a named deal (or model assumption), one primary cause, one class; residual labeled unexplained.
3. **Verdicts** - causes in impact order (attributed dollars), each with its two supporting signals and its class. This section is the arithmetic of the miss and stays in dollar order.
4. **Demand isolation** - the hindsight-corrected forecast and the residual genuine shortfall, if any.
5. **Fixes** - in leverage order (dollars divided by fix effort), one per cause, each with class, owner, effort tier, and the metric that proves it worked within one period. Print the impact order beside it and name every cause that moved between the two, with the effort that moved it.
6. **Threshold check** - attribution coverage, evidence rule, backtest result.

## Worked example (positive)

B2B SaaS, 40 reps, quarterly forecast. Quarter-start commit $4.0M; actual $3.15M; gap $850K (21% signed miss at company level). Snapshots and field history available for 6 quarters.

Attribution table (all figures from the period-start snapshot reconstruction):

| Gap component                        | Deals | $               | Primary cause                   | Class    | Signals                                                                                                                        |
| ------------------------------------ | ----- | --------------- | ------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Commit deals slipped to next quarter | 5     | $370K           | Stale / mass-pushed close dates | Data     | 3+ pushes each, no reasons; all 5 edited the same evening before the month-end forecast call                                   |
| Commit deals lost                    | 2     | $260K           | Stage inflation                 | Behavior | Both single-threaded with no economic-buyer contact ever logged; both skipped from discovery to negotiation in field history   |
| Commit deals dead at quarter start   | 3     | $140K           | Zombie opportunities            | Data     | No activity for 70+ days at snapshot date; reps confirmed in interview they knew the deals were dead                           |
| Wins from outside the forecast       | 4     | +$120K (offset) | Rep sandbagging                 | Behavior | One rep, third consecutive quarter beating commit by >30%; all 4 deals showed late-stage activity weeks before entering commit |
| Unexplained residual                 | -     | $80K            | -                               | -        | 9.4% of gap, within the 10% cap, labeled as such                                                                               |

Note the offset is reported, not netted: the true over-forecast was $970K, partially masked by $120K of hidden upside. Netting the two would have understated both problems.

Demand isolation: rebuilding the quarter-start forecast with zombies removed, the two unevidenced deals downgraded, and evidence-backed dates gives a corrected commit of $3.28M vs. $3.15M actual - a $130K residual attributable to genuinely thin coverage in one segment. That part goes to pipeline generation, not to forecast-process fixes.

Backtest: the same fingerprints run on the prior quarter flagged 9 of the 11 deals that actually slipped or lost from commit (82% - passes).

### The ranking adjustment, shown

Impact order, straight from the table: stale dates $370K > stage inflation $260K > zombies $140K > sandbagging $120K.

Leverage order, the same causes divided by their fix effort tier: stale dates ($370K, an hour) > zombies ($140K, an hour) > stage inflation ($260K, a week plus a cycle) > sandbagging ($120K, a week plus two periods of history).

What moved and why:

- **Zombies up, #3 to #2.** Same admin hour as the leader for a third of the dollars, and the purge makes coverage honest in the current cycle rather than the next one.
- **Stage inflation down, #2 to #3.** The largest behavioral number in the diagnosis, but the evidence gate takes a week to define, needs sales leadership to enforce it, and does not move commit conversion until the following period.
- **Nothing moved into first place.** The leader is the largest attributed cause that also happens to be an hour of admin - leverage promotes cheap fixes, it does not promote cheapness. A $20K zombie purge would still rank below a $370K one at identical effort.
- **Comp-driven bias is absent, and that is a finding.** Nothing in this period's fingerprints pointed at a quota cliff, so it was never confirmed. Had it been, it would have ranked last on leverage and first in the narrative, with the behavior fixes flagged as temporary until the plan changed.

Fixes shipped, in leverage order:

| Fix                                       | Class    | Owner            | Effort                              | Metric                      |
| ----------------------------------------- | -------- | ---------------- | ----------------------------------- | --------------------------- |
| Reason-required close-date pushes         | Data     | RevOps           | An hour                             | Silent-push count           |
| Zombie purge plus recurring hygiene audit | Data     | RevOps           | An hour, then a standing job        | Stale-deal count            |
| Buyer-evidence gate on commit entry       | Behavior | Sales leadership | A week, then a standing inspection  | Commit conversion rate      |
| Open rep-calibration scorecard            | Behavior | Sales leadership | A week, plus two periods of history | Rep commit beat/miss spread |

## Negative example (a wrong diagnosis, and why)

Same company, first pass - before this method was applied. Leadership concluded: "reps have happy ears - mandate qualification retraining."

Evidence offered: (a) the team's win rate on forecast-weighted deals was 19%, far below the ~60% the late stages implied; (b) the VP recalled one vivid deal a rep had sworn was closing that never did.

Why the diagnosis was wrong:

- **Single-signal reasoning.** The win-rate gap was one signal, and the anecdote was not a signal at all. No field history was pulled; the two-signal rule would have blocked the verdict.
- **Hindsight data.** The 19% was computed on the end-of-quarter deal list, whose denominator was padded with zombie deals nobody had closed out - a data problem inflating the apparent optimism. On the period-start snapshot with zombies excluded, evidenced late-stage deals actually converted at 54%.
- **Wrong class, wrong fix.** Retraining (a behavior fix) was applied to what was mostly a data problem. Stale dates and zombies were untouched, so the next quarter missed again.
- **Second-order damage.** Because the retraining arrived framed as blame, reps protected themselves the following quarter by under-calling - the error flipped from over-forecast to under-forecast, and leadership concluded the training "worked" until the annual plan, built on sandbagged numbers, came in short.

The corrected diagnosis (the positive example above) attributed only $260K of a $970K gross miss to actual inflation - the retraining had targeted roughly a quarter of the problem with a fix that made the rest worse.
