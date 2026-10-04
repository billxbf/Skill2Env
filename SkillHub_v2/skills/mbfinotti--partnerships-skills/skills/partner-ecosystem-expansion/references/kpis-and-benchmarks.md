# KPIs and Benchmarks

## The vendor-bias warning - read first

Nearly every published number in this field comes from a party that profits when it looks good:

- PRM and ecosystem-platform vendors.
- Analyst studies commissioned by an interested party.
- Consultancies quoting their own engagement models.

The only independent evidence base is academic alliance-portfolio research, which measures firm performance rather than program vanity metrics. Therefore, **every benchmark quoted in a roadmap carries a provenance flag**, and vendor figures are directional context, never proof.

Flag taxonomy:

- **ACADEMIC**: peer-reviewed, independent.
- **ANALYST**: research firm, often paywalled.
- **VENDOR**: published by a tool/platform vendor.
- **VENDOR-COMMISSIONED**: analyst research paid for by an interested party.
- **CONSULTANT**: a consultancy's own models.
- **MIXED**: aggregated across the above.

## Leading indicators per added category

Judge a new category by cohort, early. Instrument these in efficiency order - gate decisions settled per unit of measurement effort and waiting time, highest ratio first - and stop when the gate can be read:

1. **Partner activation rate** - signed partners closing at least one deal in year one. One query against data you already hold, and it settles the recruit-ahead-of-enablement question by itself.
2. **Time-to-first-deal per partner**, against the expected window for that category. Same data, and it separates a slow category from a failing one.
3. **Partner-sourced and partner-influenced pipeline** (B2B); incremental attributed revenue (B2C). Needs attribution built and a quarter of accumulation, and it is what the funding conversation runs on.
4. **Enablement/certification completion** inside the onboarding window - whether the cohort did the motion.
5. **Deal-registration volume** - whether deals are surfacing before they collide.
6. **Category share of new revenue**, once the category matures.
7. **Partner NPS** for the pilot cohort - opinion, useful for diagnosing a failing cohort, never sufficient to open a gate.

- cost (heaviest first): `category share of new revenue > partner-sourced pipeline > partner NPS > activation rate > time-to-first-deal > enablement completion == deal-registration volume`
- value (biggest payoff first): `category share of new revenue > partner-sourced pipeline > activation rate > time-to-first-deal > enablement completion > deal-registration volume > partner NPS`
- efficiency (instrument first): `activation rate > time-to-first-deal > partner-sourced pipeline > enablement completion == deal-registration volume > category share of new revenue > partner NPS`

`enablement completion == deal-registration volume` on both lines: each falls out of a system the category's prerequisites forced you to build anyway (the certification track, deal registration), and each is read as a report rather than measured. Neither proves revenue - both only report whether the cohort is running the motion.

**What this order starves: category share of new revenue.** The number leadership actually judges the program by, ranked second-to-last because it needs a year of cohorts before it says anything. Promote it whenever the review is a funding or board decision rather than a stage gate - there, no cheaper indicator is accepted as the answer.

This order is a default; it shifts with the motion and with who reads it. A category with no deal registration has no line 5, a B2C affiliate cohort reads incremental attributed revenue where a B2B one reads sourced pipeline, and a user whose CRM already reports partner attribution should promote line 3 to the top because its cost is already paid.

## Published numbers, with flags

| Metric                                  | Figure                                                                                        | Source + flag                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Healthy partner activation              | 30-50%; below 20% when unmanaged                                                              | Introw - VENDOR                                              |
| Onboarding window before likely failure | 90-120 days                                                                                   | Forrester Partner Onboarding Framework - ANALYST (paywalled) |
| Ramp analog for a partner seller        | SMB ~3 mo; mid-market 5-7 mo; enterprise 9-12 mo                                              | RevOps sources incl. The Bridge Group - MIXED                |
| Orchestration-investment threshold      | Partner-sourced 5-10% of new ARR                                                              | Forecastable - CONSULTANT                                    |
| Ecosystem revenue multiplier            | 5x-10x on annual partner spend over 3-4 yrs; GSI 6x-12x                                       | Alexander Group's own models - CONSULTANT                    |
| Partner-services multiplier             | $7.13 services per $1 platform sold (services-heavy partners) vs $1.26 (resell-focused)       | Canalys for AWS - VENDOR-COMMISSIONED                        |
| Co-sell effects                         | +51% average revenue growth, 65% higher close rates, 54% larger deals for frequent co-sellers | Canalys for AWS, 2024 - VENDOR-COMMISSIONED                  |
| Mature programs' revenue share          | 28% of overall company revenue through partnerships                                           | Forrester - ANALYST                                          |
| MDF sizing                              | 2-6% of channel revenue; 25-50% cost-share per activity; 40-60% utilization                   | MIXED                                                        |

## Known-unstable statistics - never quote as settled fact

- **"Buyers spend 68% of their journey digitally / 71% reach vendor selection digital-only."** Derives from a 2013 SiriusDecisions statistic that Forrester itself later publicly flagged as a myth and revised to "70-80% self-directed". Vendor-analyst assertion; often used to justify adding influence-category partners early - the direction may hold, the precision does not.
- **"95% of Microsoft revenue flows through partners."** Traceable to a real primary source: Microsoft's own corporate blog (February 2019) quotes this figure directly from Satya Nadella and Amy Hood's Q2 FY2019 earnings-call commentary ("95 percent of Microsoft's commercial revenue flows directly through our partner ecosystem"), and then-CVP Gavriella Schuster repeated it in her own remarks. Genuinely sourced to Microsoft rather than an untraceable round number - but still one company's self-reported commercial-revenue framing from 2019, not an audited or updated figure, so present it as Microsoft's own claim rather than a current industry constant.
- **Reseller-profitability figures drift.** The older "~25% of the channel struggles to break even" has been superseded by Omdia's 378-partner survey: 58% expecting profit decline, 51% forecasting double-digit drops. Use the current figures and note the drift.

## Using the numbers

- Set gate thresholds from the user's own base rates wherever any exist (current categories' activation, time-to-first-deal); use published figures only to sanity-check, never to substitute.
- When a plan's viability depends on a flagged number, list it in the roadmap's Open Questions with what would verify it.
- Refuse the comparison when a vendor benchmark and the user's cohort measure different things - signed partners vs active partners is the classic mismatch.
- Any number appearing in the roadmap without a flag fails the Pass Threshold; fix it before shipping.
