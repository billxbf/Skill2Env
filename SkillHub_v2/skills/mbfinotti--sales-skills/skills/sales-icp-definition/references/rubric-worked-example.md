# Worked example - data-led ICP scoring rubric with retro-scoring pass

An industrial-B2B setting, chosen because it carries the best-documented counterintuitive weighting finding. In the sourced manufacturing case (the FORGED scorecard lineage), firmographics - industry, revenue, headcount - turned out to be the _least_ predictive category, while certifications held, machines on the floor, and supply-chain trigger events predicted far better.

The structure below (categories, criterion counts, 100-point distribution, retro-scoring protocol) is sourced practice. The specific weights and pass-rate numbers are **illustrative arithmetic**, shown so the shape of a passing validation is concrete, never reusable benchmarks.

## Setting

A vendor selling quality-management software to mid-size manufacturers. CRM holds 140 closed deals tagged won/lost, plus churn flags. That volume supports analyst-defined weighting and is approaching the 100-150+ bar for regression.

## Step 1 - segment by value

Rank cohorts by LTV, time-to-value, churn, expansion, and reference potential - then profile the winning cohort, not the whole base. Here the winning cohort was not the largest accounts: the biggest logo by revenue consumed outsized support and churned at month 14 - a warning sign, excluded from the profile deliberately.

## Step 2 - derive criteria from tagged accounts

Tagging the winning cohort's attributes surfaced five shared structural traits (consistent with the commonly cited ~80%-share-3-5-traits pattern), which seeded the rubric. Lost deals that _matched_ firmographics were mined separately for disqualifiers - the two most common loss reasons became deductions, not footnotes.

## The rubric - 11 criteria, 100 points, analyst-defined weights

| #   | Criterion                                                                        | Category       | Weight |
| --- | -------------------------------------------------------------------------------- | -------------- | ------ |
| 1   | ISO 9001 or equivalent certification held                                        | Technographic  | 14     |
| 2   | 10+ CNC/production machines on the floor                                         | Technographic  | 12     |
| 3   | Runs an ERP but no dedicated QMS                                                 | Technographic  | 12     |
| 4   | Supply-chain trigger in last 12 months (new OEM contract, audit failure, recall) | Intent/trigger | 14     |
| 5   | Hiring for quality-engineering roles                                             | Behavioral     | 8      |
| 6   | Multiple visitors from the account on pricing/spec pages                         | Behavioral     | 8      |
| 7   | Discrete manufacturing vertical (not process)                                    | Firmographic   | 8      |
| 8   | 100-800 employees                                                                | Firmographic   | 6      |
| 9   | $20M-$250M revenue band                                                          | Firmographic   | 6      |
| 10  | North America or EU plant locations                                              | Firmographic   | 6      |
| 11  | Named quality leader exists (dir.+ level)                                        | Behavioral     | 6      |

Note the tilt: firmographics carry 26 of 100 points despite being four of eleven criteria - the analyst panel weighted by believed predictive power, informed by the sourced finding that firmographics predicted least in this domain. A generic template would have inverted that.

**Disqualifier deductions** (scored as subtractions, first-class):

- Locked into a competitor QMS contract with 18+ months remaining: **-40**
- Regulated sub-vertical the product lacks compliance modules for: **-40**
- Fewer than 25 employees (support economics never work): **-30**

**Score bands** (the bands feed the tiering skill downstream - this file only defines them): 70+ strong fit · 45-69 moderate · <45 out of profile.

## Step 3 - the retro-scoring pass (the step most teams skip)

Protocol: score the last 50-100 closed deals - won _and_ lost - against the draft rubric before anyone uses it live. Here, 90 deals (55 won, 35 lost). Illustrative result:

| Draft-rubric band | Deals | Won | Win rate |
| ----------------- | ----- | --- | -------- |
| 70+               | 31    | 26  | 84%      |
| 45-69             | 38    | 22  | 58%      |
| <45               | 21    | 7   | 33%      |

**Reading it**: high scorers close at a materially better rate than low scorers, monotonically across bands - the rubric is predictive, ship it. Had the bands come out flat (say 62% / 58% / 55%), the correct move is to revise weights and re-run, not to ship and hope.

In the first draft of this rubric, criterion 8 (employee band) was weighted at 14. Retro-scoring showed no separation on it, and the points moved to the supply-chain trigger. That reweighting is the entire value of the pass.

**Report the pass inside the artifact** - the validation table travels with the ICP so the next refresh can re-run it against the new quarter's deals.

## Negative example - the rubric that fails

A four-criterion, firmographic-only checklist ("SaaS vertical, 50-500 employees, $10M+ revenue, US-based"), weights guessed in a meeting, built on 12 closed deals, no disqualifiers, never retro-scored.

Every documented failure mode at once:

- Too few criteria to differentiate.
- One category out of four.
- Data volume that supports only equal weighting, yet weights were invented anyway.
- Nothing to subtract for known-bad patterns.
- No evidence the score predicts anything.

It will pass firmographically perfect accounts that just renewed with a competitor, and its owner will not find out until two quarters of outbound have been spent on them.
