# The conversion-inversion method (week-3 pipeline conversion rate)

The rigorous alternative to `target = 1 ÷ win rate`, from Dave Kellogg's "Target Pipeline Coverage is Not the Inverse of Win Rate" (Kellblog; also discussed on his "SaaS Talk with the Metrics Brothers" podcast with Ray Rike).

## Why inverting win rate is structurally flawed

1. **Win rate is ambiguous.** A narrow win rate (wins ÷ wins + losses) and a broad one (wins ÷ wins + losses + no-decisions) produce very different numbers from the same pipeline, and most targets never state which was inverted.
2. **Win rate excludes slips.** A deal whose close date moves out of the period is neither a win nor a loss in most CRM reporting - but it consumes coverage exactly like a loss. Kellogg's rule of thumb across the deals he has studied: you win a third, you lose a third, and you slip a third.
3. **The timing is mismatched.** Coverage must be assessed at period start, from pipeline that exists then; win rate is only knowable once deals reach a terminal state, later. Inverting a lagging metric to set a leading target measures the wrong moment.

## The method

1. Snapshot total pipeline value at the **start of week 3** of the quarter - early enough to act on, late enough that sales can no longer argue the pipeline still needs scrubbing before being judged.
2. Compute **week-3 conversion rate** = new revenue closed in the period ÷ the week-3 snapshot value.
3. Take a **trailing 7-9-quarter average** - a single quarter is too noisy given normal deal-timing variance.
4. **Invert the trailing average** to get the target coverage ratio.

## Worked examples

- Trailing nine-quarter average week-3 conversion of **34%** inverts to a target of **1 ÷ 0.34 ≈ 2.86x**.
- A **25%** conversion rate implies roughly **4x** target coverage.
- Run it backwards as an audit: a handed-down "3x" target implies the org is assuming a 33% conversion rate. If nobody can defend that 33%, the target was never derived - it was inherited.

## Scope limit: long cycles only

The method assumes the sales cycle is significantly longer than the measurement period - in a 9-12-month-cycle business, everything that can close this quarter already exists at quarter start, which is what makes the snapshot meaningful. Under a ~30-day cycle, quarterly week-3 coverage is close to meaningless: two-thirds of the pipeline needed to close during the quarter hasn't been created yet at snapshot time. For short-cycle businesses, substitute **day-3 monthly snapshots** - the same "early enough to act, late enough to be real" logic at a cadence matching the cycle.

## When to adopt

Stay on simple 1÷win-rate inversion until the org holds **7+ quarters of clean pipeline-snapshot history** to average over - the simple version is easier to compute and communicate, and directionally correct. Treat conversion-inversion as the upgrade path for a mature RevOps function, not the day-one requirement.

Source caveat: Kellogg's worked examples come from his own enterprise-software operating experience. The method transfers across motions; the specific numbers may not.
