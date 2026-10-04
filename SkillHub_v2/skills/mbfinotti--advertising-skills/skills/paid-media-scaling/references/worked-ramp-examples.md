# Worked ramp examples

Load this when drafting a Ramp Plan and the user would benefit from seeing a complete one first, or to check a draft against the negative example. Amounts and dates are illustrative; every folklore default shown must be recalibrated to the actual account.

## Worked example - B2C e-commerce, vertical ladder

Context from the interview:

- Paid-social prospecting campaign at $30K/month, 9 weeks of history, blended MER 3.2, marginal aMER on the last spend band 2.1 vs a 1.8 break-even (owner-approved).
- Evidence: triangulated (platform + blended revenue), no causal test yet.
- 30-day penetration ~14%.
- Creative: 7 proven ads, 4 tests/month capacity.
- Cash: net-30 card float, revenue lag ~5 days.
- Target: $90K/month "as fast as safe."
- Last scale attempt: none.

```
MEDIA SCALING RAMP  -  prospecting campaign, $30K → $90K/month over ~14 weeks
Gates        : affordability PASS (payback 0.9 months, per-cohort) | data maturity PASS
               (9 weeks > learning + 5-day lag) | marginal PASS (2.1 vs 1.8, triangulated)
               | measurement 11/15 PASS | creative supply MARGINAL  -  7 proven vs
               ~6 needed at $30K, but 18 needed at $90K (folklore ratio, calibrate)
               | absorption PASS | rollback defined below
Evidence bar : triangulated. Upgrade planned: geo holdout at the $60K tier  -  beyond
               2x start, attributed-plus-blended is no longer enough
Approach     : vertical ladder  -  default rung held (penetration 14% → headroom, target
               under 2x at the start), switching horizontal if penetration crosses
               ~30% mid-ramp; measure-first folded in at the 2x line instead of leading
Steps        : W1  $36K (+20%) | hold 2 wks | marginal aMER ≥1.8, reach up, freq <3
              W3  $43K (+20%) | hold 2 wks | same set
              W5  $52K (+20%) | hold 2 wks | same set + creative count ≥11
              W7  $62K (+20%) | hold 2 wks | launch geo holdout here
              W9  $75K (+20%) | hold 2 wks | holdout readout gates next step
              W11 $90K (+20%) | hold 2 wks | confirm at target
Rollback     : marginal aMER <1.8 across a full hold (not one day) → revert one step,
               stabilize 2 wks, resume +10% per step. Emergency cut only for runaway
               spend, broken destination, or tracking corruption
Ceilings     : creative supply binds first (18 proven ads needed at target; pipeline
               produces ~4 tests/month at ~1-in-6 win rate  -  folklore  -  so creative,
               not the auction, sets the ramp speed) | cash clears | penetration ~42%
               at target is past the hold band → expect horizontal switch near $70K
Exit         : target reached, OR marginal contribution margin ≤ $0 on a band, OR
               penetration >35% with declining unique reach → remaining budget goes
               horizontal
Open items   : geo-holdout design; the ÷$5,000-per-proven-ad ratio is folklore  -
               recalibrate from this account's fatigue history by W5
```

Why this passes the threshold:

- Every step pre-commits its hold, monitor set, and rollback.
- The causal upgrade arrives before the 2x line.
- The binding ceiling (creative) is named and slows the ramp rather than being discovered mid-collapse.

## Worked example - B2B long sales cycle, measure-first flavored ladder

Context:

- Professional-network lead-gen at $15K/month, cost per SQL $310 vs $400 break-even (ACV $12K × 25% SQL-to-close ÷ margin - per-cohort).
- Conversion lag click-to-closed-won ~5 months.
- Offline conversion loop: live (CRM stages flow back to the platform).
- Target: $40K/month within two quarters, CFO approves steps above 25%.

```
MEDIA SCALING RAMP  -  lead-gen line, $15K → $40K/month over 2 quarters
Gates        : affordability PASS | data maturity PASS on leading indicators only  -
               closed-won verdict arrives ~5 months late, so steps are judged on
               cost per SQL and lead-quality score, never last month's revenue
               | measurement 12/15 PASS (offline loop live  -  precondition, or stop)
               | creative supply PASS | absorption: cash float covers 60-281-day
               pipeline lag at target  -  CFO sign-off attached | rollback below
Evidence bar : triangulated via CRM. Causal upgrade: audience-split holdout in Q2  -
               TAM too small for a clean geo test (state this, don't fake one)
Approach     : vertical ladder with monthly steps  -  default rung held; measure-first
               not promoted despite the 2.6x target, since no clean geo test exists
               at this TAM; horizontal (new segment) parked until penetration
               signals fire  -  small TAM saturates fast
Steps        : M1 $18K (+20%) | hold 4 wks | cost/SQL ≤ $340, quality score ≥6/9
              M2 $21.5K (+20%) | hold 4 wks | same + penetration check
              M3 $26K (+21%, CFO) | hold 4 wks | CRM-platform reconciliation  -
                 when they disagree, the CRM wins
              M4-M6 continue +15-20%/month to $40K, each gated on the prior hold
Rollback     : cost/SQL >1.5x target across a full hold → cut 20-30%, stabilize
               2 wks, resume +10%/month. Falling CPL with flat SQL volume = broken
               proxy → freeze the ramp and fix the proxy, don't celebrate
Ceilings     : TAM binds first  -  30-day penetration 22% now; at ~35% the remaining
               increase opens a second segment instead | sales capacity: SDR team
               absorbs ~1.6x current lead volume before speed-to-lead degrades  -
               staffing gate at M4
Exit         : target reached, OR penetration >35%, OR cohort ROAS at 180 days
               (first readable cohort, M6) fails the boundary → hold at last
               good tier until the cohort verdict
Open items   : quality-score sample (~20 scored calls/month) to keep the leading
               indicator honest; audience-split holdout design for Q2
```

Why this differs from B2C, and only where it should: same conjunction, same loop, same ceilings. What changes:

- Monthly holds.
- Leading indicators instead of revenue.
- The CRM as arbiter.
- Sales capacity as a gate.

## Negative example - annotated

A widely installed open-source ads skill reduces scaling to a single line - "budget reallocation: move budget to top performers" - and its sample output recommends increasing budget on the campaign with the best CPA in a summary table. What's wrong, line by line:

- **"Best CPA" is a blended, attributed average** - no marginal read, no evidence label, and the best-looking CPA line (usually brand or retargeting) is exactly where attribution overstates most.
- **No readiness gates.** Nothing checks affordability, data maturity, creative supply, cash, or measurement health before recommending the raise.
- **No step size, no derivation.** "Increase budget" with no magnitude, so the user defaults to a big jump - the documented learning-reset trap.
- **No hold period.** Nothing says when to judge the change or on what window; a bad first week triggers panic, a lucky one triggers another raise.
- **No rollback.** The recommendation has no down-rule, no trigger, no verification date - the single most reliable marker of an unsafe scaling instruction.
- **No ceiling or exit.** The logic recommends the same raise forever; nothing detects saturation or a binding non-media constraint.

The one-sentence test for any scaling recommendation: does it name the evidence, the step, the hold, the rollback, and the exit? Missing any one of the five, it is a budget edit wearing a plan's clothes.
