# KPI definitions, KPI sets per objective, and target-setting rules

Provenance labels used throughout:

- **[standard]**: standards body (ANA/MRC/AMEC/IAB).
- **[platform]**: platform-published.
- **[vendor]**: commercially interested source.
- **[practice]**: practitioner consensus without a governing standard.
- **[internal]**: the brand's own history.

## Exposure metrics [standard - ANA definitions]

- Impressions: total times content was displayed, counting repeat displays to the same person.
- Reach: unique individuals who saw the content at least once. One person seeing a post twice = 2 impressions, 1 reach. Impressions >= reach, always.
- Viewability caveat [standard - MRC]: the MRC bar is 50% of pixels on screen for 1 continuous second (display) or 2 continuous seconds (video). Most organic platform metrics do not meet it - per the ANA guidelines' own footnote. Never equate a platform "view" with an MRC-viewable impression.

## Engagement rate - the denominator problem [practice]

Four formulas circulate; the same post can read 9% on one and 1.2% on another. The plan picks exactly one, states it in the glossary, and holds it constant.

| Formula           | Definition                      | Use when                                       | Distortion                                                    |
| ----------------- | ------------------------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| ER by reach (ERR) | engagements / reach x 100       | Judging individual organic posts (most common) | Reach only visible with creator data access                   |
| ER by impressions | engagements / impressions x 100 | Paid or high-frequency bursts                  | Dilutes with repeat exposure                                  |
| ER by followers   | engagements / followers x 100   | Almost never - legacy habit                    | Flatters small accounts; meaningless on algorithm-first feeds |
| ER by views       | engagements / video views x 100 | Video-first platforms                          | Inherits each platform's view definition                      |

## Cost and efficiency metrics [practice; formulas uncontested]

- CPM = (cost / impressions) x 1000 - awareness efficiency.
- CPV = cost / video views - no reliable cross-campaign benchmark, since organic performance drives the denominator.
- CPE = cost / total engagements - consideration efficiency.
- CPA = total campaign cost / attributed conversions. ANA's variant [standard]: program cost / total conversions.
- **CPA per creator** = that creator's allocated cost / conversions attributed to that creator. Recomputable only with a written cost-allocation rule, since the flight-level numerator does not divide by itself:
  - Assign creator-specific costs (fee, usage rights, gifted product, creator-specific paid amplification) directly.
  - Then either exclude shared costs (platform fees, agency retainer, shared production) or allocate them pro-rata by fee share. State which in the glossary before the first report.
  - Without that line, the metric is not recomputable and must not drive a pause, budget-shift, or rebook decision.
- ROAS = attributed revenue / campaign spend.
- ROI = (attributed revenue - cost) / cost x 100. Only defensible when "attributed" is defined in the glossary.

## KPI sets by objective [practice - synthesized consensus, no governing standard]

| Objective                  | Primary KPIs                                                                | Secondary / guardrail                       | Notes                                                        |
| -------------------------- | --------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| Awareness / reach          | Reach, impressions, CPM, video views; brand lift if powered                 | Frequency, view-completion rate, sentiment  | Baseline mandatory: trailing branded search + direct traffic |
| Consideration / engagement | ER (chosen denominator), CPE, saves, shares, comments, link CTR             | Watch time, completion rate, profile visits | Saves/shares signal intent better than likes                 |
| Conversion / performance   | CPA, ROAS, conversion rate, AOV                                             | CTR, new-customer rate                      | Requires a working attribution stack, not one method         |
| Affiliate-linked           | Attributed revenue, EPC, conversion rate                                    | Code-leakage rate, return rate              | Leakage rate is a mandatory guardrail, not optional          |
| Always-on ambassador       | Incremental revenue (if powered), LTV of referred customers, content volume | Post cadence, retention of creators         | Only objective where incrementality is usually feasible      |

B2B substitution: for the conversion and always-on rows, replace orders/revenue with influenced pipeline, opportunities created, and cohort-level self-reported ("how did you hear about us") channel share - purchase rarely falls inside the flight window, and dark social strips the tracking that would otherwise credit the creator.

## EMV, MIV, AVE - why they never appear as financial value

- EMV (Tribe Dynamics/CreatorIQ) and MIV (Launchmetrics) are proprietary black boxes [vendor]; MIV's own description bases it on "advertising value equivalent" - confirming both are AVE derivatives.
- Barcelona Principle 5 [standard - AMEC]: "AVEs are not the value of communication" (3.0, July 2020; reaffirmed 4.0, June 2025: invalid measures such as AVEs should not be used). The IPR rejected AVE unanimously in 2010. AMEC's "22 reasons to say no to AVEs" (2017) notes there is no agreed methodology and no peer-reviewed multiplier.
- Legitimate use: relative, directional comparison inside one vendor's consistent methodology (creator A vs creator B, this quarter vs last). Never converted to dollars for finance, never called ROI.

## Benchmarks and target setting

- The "$5.78 per $1" influencer ROI figure [vendor - Influencer Marketing Hub] has inconsistent provenance (variously cited as $5.20, misattributed to other sources) and mixes industries, platforms, and self-reported methodologies. Never use it, or any variant, as a planning input.
- Vendor benchmark reports carry survivorship bias (their own customers' successful campaigns) and silently pick flattering ER denominators. Treat all of them as calibration context, provenance-tagged, never as targets.
- Defensible targets are internal [internal]: the brand's own trailing median by platform, objective, and creator tier. First campaign on a platform = baseline-setting flight; the plan says "no target - establishes the baseline" instead of inventing one.
- "Good engagement is 1-5%" and similar ranges are heuristics [practice], not standards; no credible universal benchmark exists for ER, ROI, or CPA in influencer marketing.
