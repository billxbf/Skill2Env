# Report template and worked examples

All business figures below (spend, revenue, margins, customer counts) are **invented illustrations of the method** - never quote them as benchmarks. The only external numbers are the cited published figures, which carry their provenance.

## Table of Contents

- [Report template](#report-template)
- [Headline](#headline)
- [Definitions record](#definitions-record)
- [Metric table](#metric-table)
- [Comparison ladder](#comparison-ladder)
- [Verdict and evidence gate](#verdict-and-evidence-gate)
- [Folklore appendix (only if raised)](#folklore-appendix-only-if-raised)
- [Handoffs](#handoffs)
- [Example 1 - B2C ecommerce (home-goods DTC brand, "Maple & Loam")](#example-1-b2c-ecommerce-home-goods-dtc-brand-maple-loam)
- [Example 2 - B2B SaaS (workflow vendor, "Quorline")](#example-2-b2b-saas-workflow-vendor-quorline)

## Report template

```markdown
# Spend Health Check - {business}, {window}

## Headline

- {segment/channel}: **{healthy | watch | unhealthy | insufficient evidence}** - rests on rung {1/2/3 used}. {one line why}

## Definitions record

Model: {B2B/B2C} · Window: {dates, lag maturity} · Spend lines: {…} ·
New customer = {…}, renewals {included/excluded} · Revenue basis: {source, gross/net} ·
Contribution margin: {x%} ({how derived}) · History: {n periods available}

## Metric table

| Metric | Variant | Value | Window | Source |
| ------ | ------- | ----- | ------ | ------ |

## Comparison ladder

1. Break-even: {value} - gap: {…}
2. Own history: {last 4-8 periods} - direction: {…}
3. External: {figure} ({publisher, year, sample, variant measured}) - context only

## Verdict and evidence gate

Gate: variant established {y/n} · margin known {y/n} · window ≥ lag {y/n} · channels complete {y/n}
Verdict: {state}. {conditions met / what was withheld and why}

## Folklore appendix (only if raised)

{quoted rule} - origin: {…} - this business's own break-even: {…}

## Handoffs

{finding} → {mbfinotti/advertising-skills@skill}
```

## Example 1 - B2C ecommerce (home-goods DTC brand, "Maple & Loam")

**Inputs (order system + billing, July, lag-mature).**

- Net revenue $180,000
- 1,500 orders
- AOV $120
- 900 new customers
- Paid media spend $60,000
- Total marketing spend $72,000 (adds agency $8,000, creative $4,000)
- Contribution margin after COGS, shipping, and payment fees: 45%

### Positive reading - the method applied

| Metric                    | Variant                                   | Value | Window | Source                      |
| ------------------------- | ----------------------------------------- | ----- | ------ | --------------------------- |
| Blended ROAS              | total net revenue ÷ total paid spend      | 3.0   | July   | order system + billed spend |
| MER                       | total net revenue ÷ total marketing spend | 2.5   | July   | order system + finance      |
| Blended CAC               | total marketing spend ÷ all new customers | $80   | July   | finance + order system      |
| Break-even ROAS/MER       | 1 ÷ 0.45                                  | 2.22  | -      | own margin data             |
| First-order allowable CAC | AOV × margin = $120 × 0.45                | $54   | -      | own margin data             |

Ladder:

1. **Break-even 2.22** - MER 2.5 clears it. But blended CAC ($80) exceeds first-order contribution ($54): acquisition only pays back through repeat purchases, so the verdict is contingent on the repeat rate holding. Named explicitly.
2. **Own history** - blended CAC Apr-Jul: $70 → $74 → $78 → $80. MER: 2.8 → 2.7 → 2.6 → 2.5. Four consecutive periods of deterioration. Mix-shift check: channel mix stable, so the drift is real.
3. **External** - median ecommerce ROAS 2.04 (Triple Whale 2025, 18,000+ brands, vendor-instrumented blended figure). This brand's 3.0 sits above the median - context only. It changes nothing about rungs 1-2.

**Verdict: watch.** Above break-even on matured data, but a four-period deteriorating trend and a CAC above first-order contribution.

Next-period question: does 90-day repeat contribution close the $26 gap? Handoff: none yet, unless the trend crosses 2.22, in which case `mbfinotti/advertising-skills@ad-account-diagnostic`.

### Negative reading - same business, misread

> "The ad platform dashboard shows ROAS 4.3. That beats the 4:1 target, and the industry median is only 2.04 - we're crushing it. Scale."

What went wrong, in order:

1. **Variant mismatch.** 4.3 is _platform-reported_ ROAS (attributed, view-through included, modelled credit). The money-anchored blended figure is 3.0. The two were compared as if interchangeable.
2. **Folklore as target.** "4:1" has no traceable author and is just break-even at a 25% margin - this brand's margin is 45%, so its real break-even is 2.22.
3. **Benchmark-only verdict.** The median (rung 3) was used to declare health while rung 1 was never computed and rung 2's four-period deterioration was never looked at.
4. **The contingency vanished.** Nobody noticed CAC exceeds first-order contribution, so "scale" doubles down on a bet on repeat behaviour that was never examined.

Same numbers, opposite conclusion: "crushing it, scale" vs "watch, with a named question."

## Example 2 - B2B SaaS (workflow vendor, "Quorline")

**Inputs.**

- ACV $12,000
- Gross margin 80%
- Sales cycle ~10 weeks
- March lead cohort, measured at 180-day maturity: paid spend $48,000 (media + agency, labeled)
- 400 leads
- 60 SQLs
- 8 closed-won

### Positive reading - the method applied

| Metric                     | Variant                           | Value      | Window             | Source         |
| -------------------------- | --------------------------------- | ---------- | ------------------ | -------------- |
| CPL                        | paid spend ÷ leads                | $120       | March cohort @180d | platform + CRM |
| Cost per SQL               | paid spend ÷ SQLs                 | $800       | March cohort @180d | CRM            |
| Paid new-customer CAC      | paid spend ÷ closed-won           | $6,000     | March cohort @180d | CRM + billing  |
| Allowable CAC (first-year) | ACV × gross margin                | $9,600     | -                  | own economics  |
| Break-even CPL             | ACV × lead-to-close (2%)          | $240       | -                  | own economics  |
| Payback                    | CAC ÷ (monthly gross profit $800) | 7.5 months | -                  | derived        |

Ladder:

1. **Break-even** - CAC $6,000 sits under the $9,600 first-year contribution ceiling. CPL $120 sits under the $240 break-even CPL. Above water by arithmetic.
2. **Own history** - prior cohorts at the same 180-day maturity: $6,800 → $6,400 → $6,100 → $6,000. Improving.
3. **External** - published SaaS CAC-payback medians conflict: 18 months (Benchmarkit 2025, 583 participants, self-reported), 16 months (Aleph x Benchmarkit 2026, 198 of 342 reporting), 20 months (KeyBanc 2024, private SaaS panel). Presented as a conflict, not averaged. Quorline's 7.5 months sits inside all three panels' healthy half - context only.

**Verdict: healthy** - rungs 1 and 2 both clear, cohort-mature data, every figure labeled.

### Negative reading - same business, misread

> "March: we spent $48,000 and closed 3 deals. That's a $16,000 CAC. First Page Sage says B2B SaaS CAC is $239. This is a catastrophe - kill paid."

What went wrong, in order:

1. **Window shorter than the sales cycle.** The 3 deals closed _in_ March came from January's leads. March's spend bought a cohort that closes in June. In-period division mixed two cohorts and manufactured a $16,000 figure that describes neither.
2. **Variant mismatch on the benchmark.** First Page Sage's $239 (client analytics, Jan 2022-Aug 2025) is a *combined organic + paid* figure from a sample the agency itself discloses as 75% organic-weighted - compared here against a paid-only CAC. Its own paid-channel figure ($341) is still a different sample, different cost scope, different customer definition.
3. **Benchmark-only verdict, again.** Rung 1 (allowable CAC $9,600) and rung 2 (improving cohorts) were never consulted. The entire verdict rests on a mismatched rung 3.
4. **The evidence gate was skipped.** An immature window is an explicit withhold condition - the honest March-time output was "insufficient evidence until the cohort matures; interim read: cost per SQL $800 vs break-even CPL $240 × SQL rate," not a verdict at all.

Same numbers, opposite conclusion: "catastrophe, kill paid" vs "healthy" - the difference is entirely in the comparison, not the arithmetic.
