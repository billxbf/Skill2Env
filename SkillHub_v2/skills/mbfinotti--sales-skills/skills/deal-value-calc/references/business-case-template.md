# Fill-in templates

Fill every bracketed slot with a real value or a labelled placeholder the user must replace. Never fill a slot with an invented number.

## Table of Contents

- [1. Input ledger](#1-input-ledger)
- [2. Arithmetic block](#2-arithmetic-block)
- [3. Scenario table (conservative first)](#3-scenario-table-conservative-first)
- [4. Disclosure line (when required)](#4-disclosure-line-when-required)
- [5. One-page business case (five parts)](#5-one-page-business-case-five-parts)
- [6. Finance-reviewer appendix (enterprise, or whenever finance reviews)](#6-finance-reviewer-appendix-enterprise-or-whenever-finance-reviews)

## 1. Input ledger

| #   | Input                            | Value       | Unit        | Source (document, person, or named benchmark) | Provenance     |
| --- | -------------------------------- | ----------- | ----------- | --------------------------------------------- | -------------- |
| 1   | [e.g. invoices processed]        | [4,200]     | [per month] | [buyer's ops report, June]                    | buyer-supplied |
| 2   | [fully loaded cost multiplier]   | [1.3x base] | [ratio]     | [named benchmark source]                      | benchmark      |
| 3   | [post-implementation touch time] | [1]         | [min/unit]  | [rep estimate, unconfirmed]                   | rep-assumed    |

Rules:

- One row per raw input
- No derived figure appears here
- Every value-side row carries exactly one of the three provenance labels
- Cost-side rows (the rep's own pricing and fees) cite the written quote instead

If any rep-assumed row materially moves the headline, add the disclosure line (section 4).

## 2. Arithmetic block

Per driver, show the full chain:

```
Driver: [name]                                   [hard | soft]
  Formula : [as stated in the skill's driver table]
  Inputs  : [ledger row numbers used]
  Math    : [every step written out, e.g.
            5 min x 4,200/mo x 12 = 4,200 h/yr
            4,200 h x $32.50/h = $136,500 gross
            x 0.65 realization = $88,725]
  Annual value: [$]
```

Then the totals:

```
Total annual HARD value : [$]   (headline basis)
Total annual SOFT value : [$]   (separate section, never in headline)
Total Year-1 investment : [$]   = licence [$] + implementation [$]
                                + integration [$] + internal effort
                                ([h] x [$/h]) + training [$] + admin [$]
Annual recurring cost   : [$]
Annual net value        : [$]   = hard value - recurring cost
ROI ([horizon], net-benefit convention)
                        : [(total benefits - total costs) / total costs]%
Payback                 : [12 x Year-1 investment / annual hard value]
                          months - or "does not pay back within the
                          horizon" if net value <= 0
Multi-year ([N]y)       : per-year value/cost table + cumulative net
                          [+ NPV at buyer's own rate r = [%], if finance
                          reviews]
```

## 3. Scenario table (conservative first)

| Case         | Changed inputs (and why the range is defensible)   | Annual hard value | ROI | Payback |
| ------------ | -------------------------------------------------- | ----------------- | --- | ------- |
| Conservative | [haircut rep-assumed and benchmark inputs hardest] | [$]               | [%] | [mo]    |
| Expected     | [inputs at face value, haircuts applied]           | [$]               | [%] | [mo]    |
| Optimistic   | [upper bounds, stated]                             | [$]               | [%] | [mo]    |

Sensitivity note (mid-market and up): "The result is most sensitive to [input 1] and [input 2]; swinging [input 1] between [low] and [high] moves annual value between [$] and [$]."

## 4. Disclosure line (when required)

> Headline figures rest in part on rep-assumed inputs ([list rows]); they have not been confirmed by [buyer]. Replacing them with confirmed values is the next step of this analysis.

## 5. One-page business case (five parts)

```
[No vendor logo. Plain formatting or the buyer's own template.]

1. HEADLINE - tied to [buyer's named priority/initiative]:
   "[Outcome] in support of [initiative]"

2. PROBLEM - [affected team/parties] currently [problem], costing
   [buyer's own quantified figure] per [period]. [Urgency driver:
   what makes this a now-problem]. Cost of doing nothing over
   [horizon]: [$, in the buyer's own units].

3. RECOMMENDED APPROACH - the shift: from [current practice] to
   [new practice]. (Not a feature list.)

4. TARGET OUTCOMES - before/after on executive KPIs:
   [KPI 1]: [current] -> [target]     [KPI 2]: [current] -> [target]
   Conservative-case annual value: [$] (full math attached).

5. REQUIRED INVESTMENT - from us: [$, resources, timeline].
   From [buyer]: [people, hours, decisions, dates].
   Payback: [conservative-case months]. Time to value: [date].
```

Aim the whole page at the economic buyer's three concerns: costs, time to value, and confidence in the initiative - and the cost of inaction.

## 6. Finance-reviewer appendix (enterprise, or whenever finance reviews)

- [ ] Assumption appendix: every ledger row with source and provenance label.
- [ ] ROI convention and time horizon stated.
- [ ] Full TCO shown, including internal effort.
- [ ] No double counting (attest which resources back which driver).
- [ ] Soft value in its own labelled section, excluded from headline.
- [ ] Three scenarios plus sensitivity on the top inputs.
- [ ] NPV/discount rate: the buyer's own hurdle rate, asked for - not assumed.
- [ ] Written assumption sign-off requested from champion/finance, with date.
