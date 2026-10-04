# Distribution, Backtesting, and Cadence

How many tiers, how partners spread across them, and how movement between them is governed.

## Choosing the tier count

No efficiency ranking here, deliberately: tier count is set by the size and heterogeneity of the base, not by what each count returns per unit of effort. Ordering 2, 3 and 4 against each other would be false precision, because the right count moves entirely with the base and a wrong count is not an inefficient choice but an unfillable one.

- Default to 3 - the "good, better, best" norm across 98% of top IT partner programs (Forrester analyst assertion, not raw survey data).
- Collapse to 2 below roughly 50 partners; a small base cannot fill three meaningful cohorts.
- Add a 4th only when the base is large and genuinely heterogeneous. Five or more tiers "with overlapping criteria... that no one inside or outside the company can explain quickly" is the documented bloat failure.
- Consider an unranked "registered" entry rung below the first earned tier - it absorbs new signups without diluting the earned ladder.

## Backtesting against the current base

1. Pull 4-8 quarters of real partner data: revenue by motion, certifications, retention, registered deals.
2. Apply the proposed criteria; count who lands in each tier.
3. Compare the resulting shape to the targets below; escalate or relax thresholds; rerun until it fits.
4. Check key partners by name: where do the advisory-council members land? A design that demotes half the council needs either rework or heavy socialization before announcement.

## Target distribution shape

- Aim for a pyramid: a broad base, a substantial middle, a selective top.
- Keep the top tier reachable by roughly >=10% of partners (a PRM-vendor rule of thumb, not an empirical dataset) - but not crowded. Compression at the top is the most common sign criteria haven't kept pace with ecosystem growth.
- Avoid the documented most-common mistake: tiers "too easy to achieve at the bottom and too hard at the top".
- Avoid cliff effects: a partner narrowly missing a threshold should not face a dramatic benefit drop - smooth the step or add an intermediate criterion.
- Expect revenue concentration of 10-20% of partners producing 70-80% of channel revenue (consultancy rule of thumb); a backtest wildly off that pattern deserves a data check before a design change.

## Review cadence and measurement windows

Three cadences compete for one job: keeping status current without making it feel unstable.

- efficiency (best ratio first): `quarterly > annual > monthly`
- value (status that reads as current and earned): `monthly > quarterly > annual`
- effort (heaviest first): `monthly > quarterly > annual`
- **Quarterly** (default rung): four scheduled runs a year track a base that moves, and each is a run rather than a standing job.
- **Annual**: near-zero effort, and lets partners coast for eleven months.
- **Monthly**: a standing job - a recalculation, a comms wave and an appeals queue every month - and it spends goodwill besides, since status that can move monthly feels unstable and feeds anxiety and churn (practitioner convention, not a study). At least one major program runs it anyway, on a fixed day.
- Move up to monthly when the mechanic's inputs already compute themselves and the base transacts continuously. Drop to annual only when partner agreements or the fiscal calendar force it, and expect coasting.
- This order starves monthly, the most responsive cadence and the most expensive to run. Promote it anyway for a high-volume transactional base, where a quarter of stale status is a quarter of misapplied discounts.
- Use a rolling trailing-4-quarter window to prevent tier tourism (one spike quarter buying lasting status).
- Publish decision dates in advance - partners should never discover a review happened by losing a badge.

## Promotion, demotion, and grace

- Promote at recalculation, effective immediately; delaying a promotion only punishes momentum.
- Enforce demotion. Never demoting anyone makes status meaningless and quietly inflates every tier.
- Treat demotion as the highest-risk moment in the program. Peer-reviewed loyalty research finds status demotion heightens negative emotions, threatens identity, and raises switching intent - worst for top-to-bottom drops. The findings generalize to any hierarchical status system.

Three documented postures exist for the same goal:

- one vendor's public terms demote automatically one tier at the annual audit
- another removes the badge at the next quarterly update with no stated grace
- the practitioner convention grants a cycle of grace

- efficiency (best ratio first): `one review cycle of grace > automatic single-tier demotion at the audit > badge removed at the next update, no grace`
- value (discipline restored): `automatic single-tier demotion == badge removed with no grace > one cycle of grace`
- effort (heaviest first): `one cycle of grace > automatic single-tier demotion == badge removed with no grace`
- Both ties are one fact seen twice: the two harsh postures are a single automated status change at the review with a single notification, so they restore the same discipline at the same cost and differ only in how far a partner falls. Grace splits from them on both axes - it buys nearly all the discipline while spending far less goodwill at the program's highest-risk moment, and it costs a warned state to track, a second comms wave, and the appeals traffic in between.
- Default to one review cycle (~90 days) of grace. Move to the harsher end when the top tier is already compressed and grace would postpone the reset another full year; the trade is goodwill for discipline, and reversing it later means telling partners something other than what their agreement says.
- Pre-communicated, criteria-backed demotion can open a constructive conversation. Cody Jones of Zapier: "Nothing grabs their attention quite like a tier change." A surprise demotion just churns.

## Grandfathering, migration, and appeals

- On migration, choose between the two documented vendor practices: set each partner to the best status they earned during the review period, or publish an explicit no-loss date. Efficiency: `best status earned > published no-loss date`, with effort `==` - both fall out of the backtest already run, so neither adds work. They split on value: best-status-earned lets demotions land one partner at a time as each window expires, while a single no-loss date concentrates every demotion in the program's history onto one day.
- Run structural overhauls as phased multi-quarter transitions with published milestones; the largest 2026 redesigns all did.
- Give written notice before any status change and an appeals path with a named decision owner and published decision dates.

## Preventing tier inflation

- Revisit thresholds at least annually; a growing base under static thresholds compresses the top by default.
- Expire stale inputs: one vendor stops counting expired certifications toward tier points immediately.
- Keep windows rolling so old achievements age out instead of accumulating forever.
