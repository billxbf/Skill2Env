# Weighting and Thresholds

## Derive weights from outcomes, not opinions

The intuited signal list and the list that actually correlates with revenue are usually different. Calibrate against the company's own history, never against industry averages.

1. Pull closed-won and closed-lost records from the last 12-24 months (12 months of history is the practical minimum for evidence-based weights).
2. For each candidate signal, compute its frequency in the won group vs the lost group; rank signals by the delta. Where volume allows, compute per-signal conversion vs baseline - one documented recalibration found an integrations-doc download converting at 3.2x baseline while webinar attendance sat at ~1x, i.e. pure noise that had been carrying points for years.
3. Scale points proportionally to the observed delta, then round to values sales can reason about.
4. Trap - fields populated at close: won records often carry complete firmographic data only because sales filled it in right before closing. A signal is only usable if it existed on the record at scoring time; check field history, not field completeness.
5. Below ~12 months of usable history, start from the template split below, label every weight "assumed", and pull the first recalibration forward to 60 days.

## Fit/engagement split by motion

| Motion                          | Split (fit/engagement) | Why                                                                                |
| ------------------------------- | ---------------------- | ---------------------------------------------------------------------------------- |
| Enterprise sales-led (high ACV) | 60/40                  | Fit is the gate; a wrong-market lead engaging heavily is still a wrong-market lead |
| Mid-market hybrid               | 50/50                  | Balanced motion, balanced evidence                                                 |
| PLG / self-serve                | 30-40 / 60-70          | Product usage is the evidence of value; fit is a thin filter                       |
| B2C transactional               | Behavior-dominated     | Fit reduces to a demographic gate; propensity signals expire in hours              |

The split mechanics are identical for B2B and B2C - only the ratio and the signal sources change.

## Keep the two axes visible - the grid

Report fit and engagement as separate scores and route on the combination (Marketo-style: letter grade A-D for fit x number 1-4 for engagement, quartile cutoffs; MadKudu-style: Fit band x Likelihood-to-Buy band combined via a matrix into a grade). A 75 from an A-fit account at demo stage is not the same lead as a 75 from a D-fit account browsing the careers page.

Check win rate per grid cell empirically once volume accrues - B cells sometimes outperform A cells, and that finding is the point of the grid. It exists for calibration, not decoration.

## Category caps

Cap each signal category's total contribution so no single channel can cross the threshold alone - e.g. all email engagement capped at 10-15 points of a 100-point scale. Two silent inflation bugs to check for:

- Repeatable low-value events (opens, blog visits) with no cap compounding past the threshold.
- Multi-value properties scored once per matching value instead of once per record (a contact with three matching job functions triple-counts the points).

## Setting the threshold

Three methods, ranked by value per unit of effort - effort being analyst hours plus the scored history each method needs before it can run at all. They cross-check each other, so run them in this order; the order is the ranking.

- efficiency: sales capacity > conversion band > percentile sanity check
- value (a threshold that still holds three months after launch): conversion band > sales capacity > percentile sanity check
- effort: conversion band > sales capacity > percentile sanity check

Effort in magnitudes: the percentile check is minutes against the current database; the capacity math is an hour of arithmetic available before a single lead is scored; the conversion band needs ~60 days of live scored history or a full backtest first, then a week of analysis.

1. **Sales capacity first.** Threshold where projected weekly MQL/PQL volume roughly matches what reps can actually work (reps x leads-per-rep-per-week). This is the honest constraint most guides underweight - a statistically perfect threshold that produces 3x workable volume just recreates the triage problem downstream. It leads on efficiency because it needs no scored history at all and still buys the outcome that matters most on day one: a queue reps finish.
2. **Conversion band.** After ~60 days of scored history (or on backtest data), chart sales acceptance and opportunity conversion per score band; set the threshold where the curve breaks upward. Highest value of the three - it is the only method that reads actual conversion instead of proxying it - and highest effort, since it cannot run until the data exists.
3. **Percentile sanity check.** The threshold should land near the top 15-20% of the active database; on a 100-point scale most working models sit at 60-80. Far outside that range usually signals a weighting problem, not an unusual business. Cheapest and last on purpose: it catches a gross weighting error but can never set a threshold, because a database's top 20% is a statement about the database, not evidence those leads convert.

What this order starves: the conversion band, first on value and first on effort, so a day-one build never reaches it. Promote it the moment 60 days of scored history or a clean backtest exists, and treat the v2 review as its standing invitation. Where the Interview gave no analyst and no backtest, delete it from the plan rather than carrying it - set from capacity, sanity-check the percentile, and book the band check for when someone can run it.

**Initial calibration before any live data:** retro-score the last 6-12 months of closed-won deals; find the natural breakpoint separating wins from losses; set the threshold just below where ~80% of wins would have scored; validate against closed-lost - if many losses land above it, tighten the criteria rather than lowering the bar.

High-intent hand-raisers (demo request, contact-sales) bypass the threshold entirely - they qualify on the action, whatever the score.

## Tiers

Each tier maps to a distinct play or it is not a tier:

| Tier | Definition                          | Play                                |
| ---- | ----------------------------------- | ----------------------------------- |
| T1   | Hand-raiser, or top band (e.g. 85+) | Immediate human follow-up under SLA |
| T2   | Above threshold                     | Standard sales queue                |
| T3   | Good fit, low engagement            | Orchestrated nurture + ads          |
| T4   | Below both bars                     | Hold; lifecycle marketing only      |

Tier-to-rep assignment, SLAs, and escalation are routing concerns - hand the tiers to `mbfinotti/revops-skills@lead-routing`.

## Rules-based vs predictive

Ranked by value per unit of effort, effort being the data volume required up front, analyst and vendor onboarding time, and what it costs to keep the thing running:

- efficiency: rules-based > hybrid (rules disqualify, a predictive layer ranks the remainder) > pure predictive
- value (ranking accuracy on the leads sales actually works): pure predictive > hybrid > rules-based - but only above the data floor below; under it, predictive's value is unmeasurable and frequently negative
- effort: pure predictive > hybrid > rules-based

Effort in magnitudes: a rules model is a week of design plus an hour per tuning pass; the hybrid adds the vendor layer on top of rules that already work; a pure predictive build is a quarter before it scores anything - data floor, onboarding, validation - and then a standing job of retraining, drift monitoring, and explaining scores to reps.

Default to rules-based, and promote the hybrid once the data floor is genuinely cleared. Delete the predictive rungs entirely below that floor rather than ranking them last. A model trained on 80 outcomes is not a slower option, it is a wrong one, and a rung left at the bottom of the list comes back as a vendor evaluation.

What this order starves: pure predictive, first on value and first on effort. Promote it where lead volume is high enough that a few points of ranking accuracy outweigh the transparency reps lose - and even there, keep the hard disqualifiers in rules.

- **Rules-based** works from day one, is transparent, and sales can audit it - which is most of why they trust it. It degrades without tuning.
- **Predictive/ML needs volume.** Vendor minimums range from 40 qualified + 40 disqualified leads at the permissive end to 1,000+ leads with 120+ conversions at the strict end; the vendor-neutral floor is roughly 500-1,000 clean closed outcomes. Below that, a governed two-axis rules model delivers most of the benefit at a fraction of the data requirement.
- **The black-box trust problem is real:** when the model cannot explain a score, reps stop acting on it regardless of accuracy. Prefer the hybrid pattern - rules handle hard disqualification, a predictive layer ranks the remainder - and resist stacking manual overrides on a predictive base until nobody can audit the result.
