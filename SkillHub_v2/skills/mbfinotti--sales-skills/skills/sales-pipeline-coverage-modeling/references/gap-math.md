# Pipeline gap math

Turns a coverage ratio into the number a team can act on: how many dollars (or units) of new pipeline must be created, by whom, by when.

## The deficit formula

1. **Remaining quota** = full-period quota − closed-won to date.
2. **Expected close from existing pipeline** = Σ(deal value × the org's own historical close rate for that stage) - never rep-supplied confidence. Compute it on the _adjusted_ pipeline (stale, out-of-period, repeatedly slipped, and single-threaded late-stage deals stripped out); a deficit computed on inflated pipeline is false comfort.
3. **Pipeline deficit** = remaining quota − expected close.

Worked example (illustrative arithmetic, not sourced data): $500K remaining quota, $320K expected close from weighted pipeline → **$180K deficit**.

## Per-rep new-pipeline-required

Divide each rep's own remaining-quota gap by **that rep's historical win rate** - never a team blanket average; a new rep at 15% and a tenured rep at 40% need materially different pipeline to close the same gap. Then window it against cycle length: only new pipeline created before the point of no return (period length − median cycle) counts toward _this_ period; the rest is next period's opening coverage.

## Stage-level coverage: locating the gap

`Stage coverage = (pipeline at stage × stage close rate) ÷ (quota × that stage's required contribution)`, computed per stage. Strong late-stage with weak early-stage coverage predicts a gap _next_ period even when this one looks fine - a generation problem and a conversion problem need different fixes.

## The direction diagnostic

Read how raw and weighted coverage move relative to each other before prescribing anything:

- **Raw falling, weighted rising** → deals are dropping out without replacement → a **generation** problem. Run a dedicated generation sprint - but only while it can still land before the point of no return.
- **Raw stable, weighted flat** → deals enter but don't progress → a **qualification/execution** problem. Tighten stage-gate qualification, coach stuck deals, purge zombies. Do not respond by adding more low-quality volume - that grows the fiction.
- **Past the point of no return** → re-forecast the period down honestly, accelerate existing late-stage deals, and redirect generation at _next_ period's opening pipeline.

## The four levers, ranked

- efficiency: `raise win rate / stage progression > accelerate late-stage deals > generate more pipeline > increase deal size`
- value: `raise win rate (compounds - permanently lowers the coverage the segment needs) > increase deal size (compounds, but structural) > generate more pipeline (a one-off refill) > accelerate (borrows from next period, roughly net-zero across the pair)`
- effort: `increase deal size (quarters of packaging, pricing and ICP work - a standing job) > generate more pipeline (a quarter of sustained pipegen, and only the share landing before the point of no return counts) > raise win rate (a quarter of coaching and stage-gate discipline) > accelerate (days, on deals that already exist)`

1. **Raise win rate / stage progression.** Tighten stage-gate qualification, coach stuck deals, thread late-stage deals running thin on engaged contacts. Better conversion lowers required coverage permanently, so it pays this period and every one after.
2. **Accelerate existing deals.** The only lever still live once the point of no return has passed. Cap how much of the gap may be filled this way: each pull-forward costs a concession now and a hole in next period's opening pipeline.
3. **Generate more pipeline.** Slow and effort-heavy, and under loose qualification it inflates the deficit instead of closing it. Only pipeline created before the point of no return counts toward this period.
4. **Increase deal size.** Structural - repackaging, repricing, moving up-market. Slowest of the four to move.

Default lever: **raise win rate / stage progression.** Promote acceleration the moment the segment passes its point of no return, and generation when the direction diagnostic reads "raw falling, weighted rising" - a genuine volume shortfall that no amount of conversion work fixes.

The efficiency order starves **increase deal size**: it carries real compounding value, but a payback measured in quarters loses every ratio round to levers that land inside this period. Promote it anyway when the segment's misses trace to deals landing below the size the model assumed rather than to too few of them - no conversion or generation work repairs a wrong price point. Treat this ordering as a default, not a law: re-rank it against the team's own position, since an org already running tight qualification has little conversion headroom left and should generate instead.

## Threshold playbook

Pre-agreed, threshold-triggered responses remove emotion and inconsistency from the mid-period call. One template - recalibrate the breakpoints to the segment's own target band before using it; 2x is an emergency for a mid-market team needing 3-4x and normal mid-period for a high-velocity team needing 2x:

| Coverage vs segment target | Response                                                  |
| -------------------------- | --------------------------------------------------------- |
| Above target               | Maintain; shift attention from volume to quality          |
| At target                  | Healthy; balance across the four levers                   |
| Moderately below           | Increase generation investment (~25% more pipegen effort) |
| Far below                  | Emergency protocols; executive intervention               |

## Cadence and ownership

- **Measure weekly, never monthly.** Only ~20% of day-1 in-period pipeline typically closes in-period; a 4x day-one ratio can be 2x by week 6, and monthly measurement surfaces the decay after it stops being actionable.
- **Owner split:** RevOps owns reporting truth - the dashboards and gap-to-plan views - so leadership isn't debating metric definitions inside the decision meeting. Sales leadership owns the corrective decisions on top.
- Keep deal-level coaching (weekly manager reviews) separate from the aggregate coverage review; blending them turns both into a close-date interrogation.
- **Re-baselining the quota is the last resort**, handled at the monthly/quarterly strategic level - reserved for a segment persistently under-covered _despite_ strong close rates (a structural creation problem) or for territory/quota assumptions that were wrong. That decision belongs to a quota-derivation exercise, not to this model.
