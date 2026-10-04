# Layout, Cadence, and Alerts

View design per audience, slicing dimensions, refresh/review rhythm, and alert mechanics.

## Two audiences, two views

Executive and operator views differ in metrics, not just zoom level [VENDOR consensus]. Both follow the same layout convention: headline KPI tiles (value + delta vs a stated prior period, color-coded) -> trend/composition charts -> leaderboard/detail table -> alert strip. Keep fraud/compliance signals on the operator view itself, never in a separate tool.

Executive view - profitability and risk at a glance:

```
+--------------------------------------------------------------------+
| NET CONTRIBUTION      | COST OF SALE   | NEW-TO-FILE  | TOP-5      |
| $412K  (+6% vs P-1)   | 14.2% (-0.4pt) | 38% (+2pt)   | SHARE 44%  |
+-----------------------+----------------+--------------+------------+
|  Validated net revenue trend (13 mo)   |  Revenue by partner type  |
+----------------------------------------+---------------------------+
|  Sourced $X | Influenced $Y (separate, capped - never summed)      |
+--------------------------------------------------------------------+
|  ALERTS: concentration breach? reversal trend? window changes?     |
+--------------------------------------------------------------------+
```

Operator view - daily movement and anomalies:

```
+--------------------------------------------------------------------+
| EPC        | CONV RATE   | REVERSAL %  | PENDING vs   | 1-PARTNER  |
| (vs 30d)   | (vs 30d)    | (vs band)   | APPROVED $   | SHARE      |
+------------+-------------+-------------+--------------+------------+
|  Daily validated conversions (6 wk)    |  Reversals by reason      |
+----------------------------------------+---------------------------+
|  Partner leaderboard: validated comm | conv | EPC | reversal% |    |
|  new-to-file% | delta vs prior period  (sortable, full tail)       |
+--------------------------------------------------------------------+
|  ALERT STRIP: EPC drop | reversal spike | share spike | compliance |
+--------------------------------------------------------------------+
```

Tile rule: every tile shows value plus delta against a _stated_ prior period - never a bare absolute number. The operator tiles above are the B2C set; in B2B swap EPC for the stage conversion rate, since EPC is deleted from the B2B metric menu.

## Slicing dimensions, ranked by efficiency

Choose only dimensions the data actually carries; the Interview answers decide, and a dimension the data cannot carry is deleted from the spec with a line in Open items, never listed as an aspiration. Effort below is tagging discipline and standing classification maintenance, not query time.

- efficiency: `partner > partner type > product/plan > geography > device > landing page > creative`
- value: `partner type > partner > product/plan > landing page > geography > device > creative`
- effort (most first): `creative > landing page > partner type > product/plan > geography == device == partner`

Partner type - content, coupon, cashback/loyalty, sub-network, influencer, email, PPC - is the highest-value slice, because it is what separates demand creation from demand capture and therefore what drives every repricing decision. It is not the highest-efficiency one: the classification has to be maintained as partners change methods and sub-networks blend several, which is a standing job the partner slice does not carry.

Build the partner slice because it is free, and build partner type because it is the one that pays. Geography, device and partner tie on effort because all three arrive as attributes of the click or order record already being stored - no tagging convention, no maintenance.

**What the efficiency order starves: landing page and creative.** Both need tagging discipline at link-creation time, so they lose every ratio round - and they are the only slices that tell a content partner _why_ their traffic converts. Promote them when the program funds placements or creative feeds, or when partner optimization support is itself part of the offer.

## Cadence

Match refresh and review to each tier's own volatility; one refresh rate for the whole dashboard is a defect. Four-band structure [VENDOR, converging with generic dashboard practice]:

| Cadence          | Reviewed                                                                                             | Drives                                       |
| ---------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Continuous/daily | Operational: EPC, reversal %, pending vs approved, single-partner share, compliance flags            | Spike response, holds                        |
| Weekly           | Acquisition: new partners onboarded, conversion-to-active rate, tail activation                      | Recruiting and activation pushes             |
| Monthly          | Performance: attributed net revenue, cost of sale, active-partner count, new-to-file, tier movements | Tier and budget decisions                    |
| Quarterly        | Portfolio: top-1/5/10% concentration, cohort curves, incrementality findings, partner mix            | Commission architecture, partner development |

Review means a named ritual - who looks, in which meeting, deciding what - not just a data refresh. Route deep quarterly per-partner reviews to the partner-performance scorecard skill; this dashboard feeds them.

The four bands carry no efficiency ordering, deliberately. They are not competing options for one job - each band exists because a different tier of metric moves at a different speed, and dropping one loses that tier's decision rather than saving effort. Build all four; rank the metrics inside them instead.

## Alert design

- Every alert carries four fields:
  - Threshold
  - Owner
  - Delivery channel
  - Expected response time

  A threshold with no owner is decoration.

- Prefer rolling-baseline dynamic thresholds over static ones - static thresholds cause alert fatigue and get ignored. Example anomaly rule: flag when a value deviates more than 2 standard deviations from its 30-day rolling mean.

Alerts compete for one scarce resource - the team's willingness to keep reading the strip - so ship them in this order and stop when attention runs out. Effort is build time plus the standing job of keeping the rule from crying wolf.

- efficiency: `reversal-rate spike > single-partner share spike > click-to-conversion anomaly > EPC drop > brand-bidding flag`
- value: `reversal-rate spike > brand-bidding flag > single-partner share spike > click-to-conversion anomaly > EPC drop`
- effort (most first): `brand-bidding flag > click-to-conversion anomaly == EPC drop > single-partner share spike > reversal-rate spike`

The anomaly and EPC-drop alerts tie on effort because they are one rolling-baseline rule over two numerators - build either and the second is a copy. Reversal-rate spike leads outright: it fires on money already at risk and reads off a state the platform maintains anyway.

**What the efficiency order starves: the brand-bidding/trademark flag.** It needs standing SERP monitoring or a licensed tool, so it loses every round despite guarding real margin and a trademark position. Promote it the moment the program pays PPC partners at all, or after the first trademark complaint - by then the alert is retroactive.

The last two are fraud-adjacent: the dashboard surfaces them; rule definitions and enforcement belong to the fraud-detection skill. Alert catalogue [SYNTH].

- Annotate every chart with validation-window changes and program-term changes - an unexplained step in a trend line wastes an investigation.
- Keep an alert log (fired, acknowledged by, resolved in) - alert response time is itself a health metric for the operating rhythm.
