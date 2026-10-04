# Worked Examples

Three illustrative cases with filled Fatigue Verdict blocks. All figures are invented for illustration - internally consistent, but not benchmarks; every real verdict derives its numbers from the account's own data.

## Table of Contents

- [Example A - B2C ecommerce, Meta: this one IS fatigue](#example-a---b2c-ecommerce-meta-this-one-is-fatigue)
- [Example B - B2B, LinkedIn: the audience is saturating, not the creative fatiguing](#example-b---b2b-linkedin-the-audience-is-saturating-not-the-creative-fatiguing)
- [Example C - NEGATIVE example: a convincing fatigue call that is actually a budget scale-up](#example-c---negative-example-a-convincing-fatigue-call-that-is-actually-a-budget-scale-up)

## Example A - B2C ecommerce, Meta: this one IS fatigue

Skincare brand, cold prospecting, broad audience (~2.1M), UGC video "morning routine" running 6 weeks in a 4-creative ad set. No edits, no budget changes, stable $900/day at ad-set level. Data: per-creative per-day export; 3-day moving average vs the creative's own trailing 14-day baseline.

Noise check on the lead signal: baseline link CTR 1.32% on ~210,000 comparison-window impressions gives a noise band of 1.32% ± 2×sqrt(0.0132×0.9868/210000) ≈ 1.27%-1.37%. Observed 0.98% sits far outside it. Two leading signals plus one confirming signal moved together across four consecutive 3-day periods; CVR held - the classic fatigue signature (costs rise, people who still click still buy).

```
FATIGUE VERDICT - "UGC-morning-routine-v3", 2026-08-20
platform      : Meta | funnel stage: cold prospecting
window        : Aug 08-20 (3-day MA) vs baseline Jul 25-Aug 07 (trailing 14-day)
volume        : $4,120 spent, 209,700 impressions, 118 conversions in window

signals
  link CTR             : 0.98% vs 1.32% (-26%)    [leading]
  hook rate (3s)       : 17.9% vs 24.1% (-26%)    [leading]
  hold rate (15s)      : 8.7% vs 9.0% (-3%, flat) [leading]
  spend share (ad set) : 22% vs 34% (no manual change) [leading]
  frequency            : 2.3 vs 1.9               [lagging]
  CVR                  : 3.4% vs 3.5% (stable)    [lagging]
  CPA                  : $34.90 vs $26.10 (+34%)  [lagging]

confounder screen
  budget/bid change        : pass - no changes in 6 weeks
  learning-phase reset     : pass - last significant edit Jul 02
  audience saturation      : pass - first-time impression ratio 68%, reach still growing
  auction CPM inflation    : pass - CPM +4%, in line with account's other ad sets
  seasonality/window mix   : pass - day-of-week-matched windows, no promo days
  tracking breakage        : pass - platform-to-orders ratio stable at ~0.83
  attribution-window skew  : pass - both windows lag-mature, same 7-day-click setting
  placement/device mix     : pass - placement shares within 2pts of baseline
  statistical noise        : pass - delta far outside the 2-SE band (see above)
  landing page/offer change: pass - no deploys; other traffic to page converting normally
  sibling-mix shift        : pass - same 4 creatives all window

confidence    : high - 2 leading + 2 confirming signals, 4 consecutive periods, gate cleared with margin
verdict       : fatigued
action        : rung 1 - hook/thumbnail swap on the same body (hook rate fell, hold rate held:
                the opening is tired, not the ad). Negative feedback normal, so same body is fine,
                but launch as a NEW ad alongside - never edit the live one. Asset via
                mbfinotti/advertising-skills@ugc-ad-scripts; keep v3 running while the swap ramps.
ruled out     : new concept - stated 6-week production lead time runs past the account's Q4
                asset freeze, so it is off this account's ladder, not merely last on it.
                Iterate survives (in-house editor, days) and is the fallback if the swap fails.
expected      : hook rate and link CTR back toward baseline on the same audience within one
                window; CPA follows. Recovery on same audience also confirms fatigue over saturation.
re-check      : 2026-09-03 (one full 14-day window after launch)
```

## Example B - B2B, LinkedIn: the audience is saturating, not the creative fatiguing

Cybersecurity vendor, cold ABM motion, matched company list rendering ~46,000 members, 5 sponsored-content ads per LinkedIn's guidance, 11 weeks in. Conversion volume (demo requests) is single-digit weekly, so the conversion floor cannot clear - the call gates on leading engagement signals, and the confidence line says so.

The tell: all five creatives - including one launched fresh 3 weeks ago - decay together, reach has been flat for a month while impressions climb, and CVR degrades alongside CTR. Fatigue is creative-specific and leaves CVR stable; this is pool depletion. The fresh creative's failure to recover performance on the same audience is the discriminating test failing in the saturation direction.

```
FATIGUE VERDICT - "ROI-report-static-A" (pattern shared by all 5 ads), 2026-08-20
platform      : LinkedIn | funnel stage: cold prospecting (ABM list)
window        : Jul 21-Aug 17 (rolling 7-day) vs baseline May 26-Jun 22 (30-day)
volume        : $18,400 spent, 342,000 impressions, 14 demo requests in window

signals
  link CTR             : 0.31% vs 0.44% (-30%, all 5 ads within 4pts of each other) [leading]
  reach (rolling)      : flat 4 weeks; impressions +38%                             [leading]
  new-member reach     : falling steadily since early July                          [leading]
  frequency            : 8.1 vs 4.9                                                 [lagging]
  CVR (click->demo)    : 1.1% vs 1.6% (degrading WITH engagement)                   [lagging]
  CPL                  : $1,310 vs $780 (+68%) - low volume, directional only       [lagging]

confounder screen
  budget/bid change        : pass - stable budget, manual bid unchanged
  learning-phase reset     : pass - no edits inside window (1 sibling added Jul 28, see mix)
  audience saturation      : FAIL - list rendered ~46k; reach plateaued at ~41k; fresh
                             creative (Jul 28) decayed to the pack within 2 weeks on the
                             same audience - the discriminating test points to the pool
  auction CPM inflation    : pass - CPM +6%, normal for the category
  seasonality/window mix   : pass - matched windows; B2B summer dip checked vs last year, smaller
  tracking breakage        : pass - form fills reconcile with CRM
  attribution-window skew  : pass - lag-mature windows
  placement/device mix     : pass - feed-only placement
  statistical noise        : pass - CTR delta outside 2-SE band on 342k impressions
  landing page/offer change: pass - no changes; other channels' CVR to page stable
  sibling-mix shift        : noted, not causal - Jul 28 add redistributed spend but decay predates it

confidence    : medium - engagement-gated (14 conversions cannot clear the conversion floor);
                signals many and consistent, but CVR/CPL read is directional
verdict       : saturating (audience), not fatigued (creative)
action        : rung 6, promoted to first under a `saturating` verdict - expand the pool:
                refresh/extend the account list, add lookalike-style expansion off
                closed-won, and add a frequency cap via the engagement-exclusion
                mechanic; audience work via mbfinotti/advertising-skills@ad-audience-targeting.
                Do NOT commission new creative - the Jul 28 test already showed it changes nothing.
ruled out     : none - no stated constraint deletes a rung here. The creative rungs are ruled
                out by the verdict, not by capacity; that is an evidence call, and it reverses
                the moment the pool grows again.
expected      : new-member reach resumes growth; frequency falls below its Jun level;
                CTR recovers only as fresh members enter - not before
re-check      : 2026-09-17 (one full 30-day window after list expansion)
```

## Example C - NEGATIVE example: a convincing fatigue call that is actually a budget scale-up

Home-fitness brand, Meta, cold prospecting. The account's best static has run 5 weeks; 12 days ago the team scaled the ad set budget +80% in one step. Now: CTR -14%, CPA +32%, frequency up.

Pattern-matched against a fatigue checklist this "confirms": two signals down, multiple periods, frequency rising. The screen catches it in two lines: the decline starts exactly at the budget step, the whole ad set (all 3 creatives) moved together, and the comparison is being made against the _pre-scale_ peak, which the platform can no longer buy at 1.8x the spend.

```
FATIGUE VERDICT - "before-after-static-hero", 2026-08-20
platform      : Meta | funnel stage: cold prospecting
window        : Aug 08-20 (3-day MA) vs baseline Jul 25-Aug 07 (trailing 14-day)
volume        : $9,700 spent, 407,000 impressions, 221 conversions in window

signals
  link CTR             : 1.19% vs 1.38% (-14%)   [leading]
  hook rate            : n/a (static)
  frequency            : 2.6 vs 1.8              [lagging]
  CVR                  : 3.1% vs 3.2% (stable)   [lagging]
  CPA                  : $43.90 vs $33.30 (+32%) [lagging]

confounder screen
  budget/bid change        : FAIL - ad-set budget +80% on Aug 08; decline onset same day;
                             all 3 sibling creatives degraded in lockstep (fatigue is
                             creative-specific; scale effects hit the whole ad set)
  learning-phase reset     : FAIL - the +80% step is a significant edit; delivery volatile
                             through ~Aug 15; window overlaps the reset
  audience saturation      : pass - first-time impression ratio 74%, reach growing fast
  auction CPM inflation    : pass - CPM +5% only; the cost move is CTR-and-mix-driven
  seasonality/window mix   : pass - matched windows
  tracking breakage        : pass - platform-to-orders ratio stable
  attribution-window skew  : partial - last 3 days not lag-mature; CPA overstated at the margin
  placement/device mix     : FAIL (secondary) - Audience Network share 9% -> 17% post-scale;
                             within-placement CTR nearly flat
  statistical noise        : pass - deltas outside noise band (but explained above)
  landing page/offer change: pass
  sibling-mix shift        : pass - same 3 creatives

confidence    : high - in the confounder, not in fatigue: three screen lines explain the decline
verdict       : confounded (budget scale-up + learning reset + placement mix), NOT fatigued
action        : no refresh. Re-baseline the creative at the new spend level from Aug 16 (post-
                stabilisation); judge future decay against that baseline, not the pre-scale peak.
                Accept that marginal efficiency at 1.8x spend sits below the old average, and
                hand the "how fast to scale" question to mbfinotti/advertising-skills@paid-media-scaling.
ruled out     : n/a - no rung was selected. A `confounded` verdict acts on the cause and never
                enters the Action Ladder, so nothing was deleted from it.
expected      : metrics stabilise at a new, slightly worse-than-peak level; if decay then
                resumes against the NEW baseline with confounders clean, re-open the fatigue case
re-check      : 2026-09-01 (first full clean window on the new baseline)
```

The lesson: commissioning a refresh here would have burned production capacity, reset learning again with the new upload, and "validated" the fatigue call when metrics stabilised for reasons that had nothing to do with the new creative.
