# Worked Specs and a Negative Example

Two fully worked commission structure specs - one B2B SaaS, one B2C ecommerce - and one negative example that fails the pass threshold. Numbers are illustrative but internally consistent. Recompute with the user's real inputs.

## Worked spec - B2B SaaS

Inputs from the interview:

- Project-management SaaS
- $49/mo entry plan
- 80% gross margin
- 3.5% monthly churn (~28-month average tenure)
- Revenue LTV ~$1,400
- Blended CAC $310
- 14-day free trial
- 30-day refund policy
- Wants content partners and review sites
- A few coupon sites already apply

```
COMMISSION STRUCTURE - <SaaS example>, <date>
Rate model        : recurring revenue share - subscription product, retention-aligned partners
Headline rates    : content/review/agency 25% recurring; coupon/deal sites 15% recurring
                    - coupon capped below content per incrementality data
Tiers             : flat - revisit after 2 quarters of partner performance history
Recurring duration: capped at 12 months; optional 5% renewal bonus in year 2
                    - margin (80%) qualifies for longer, but churn data is young; cap first
Attribution       : 90-day cookie (content); 7-day (coupon); coupon gated to new customers
Validation        : 45-day lock = 14-day trial-to-paid + 30-day refund window
Payment           : net-30, $50 minimum threshold; clawback on refund/chargeback,
                    negative balance carried forward
Economics         : max commission/customer = 25% x $49 x 12 = $147
                    = 10.5% of LTV (inside 5-15%) and 13% of gross-margin LTV (inside 30-40% cap)
                    projected cost per incremental customer = ($147 + ~15% platform fee) / 0.80
                    incrementality ≈ $211 < $310 blended CAC → PASS
Validation plan   : 30-day holdout on top 3 coupon partners in month 4; track new-customer share
KPIs              : cost per incremental affiliate customer vs $310 CAC; effective commission rate;
                    new-customer share of affiliate sales; reversal rate (expect ~2-3%);
                    revenue share of top 10% partners
```

Every line traces to an interview answer or a derivation - that is what makes the spec reviewable.

## Worked spec - B2C ecommerce

Inputs:

- DTC skincare brand
- $60 AOV
- COGS $21 (65% gross margin = $39)
- Variable costs $11.04/order (shipping $6, fulfilment $3, processing $2.04)
- 5% return rate
- Blended CAC $22
- Wants creators and content sites
- Two large cashback sites are asking to join

```
COMMISSION STRUCTURE - <ecommerce example>, <date>
Rate model        : percentage of order value - narrow AOV spread, incentive-aligned
Headline rates    : content/creator 18%; coupon/cashback 8%, new customers only
Tiers             : flat - revisit when >20 partners exceed 10 orders/month
Recurring duration: not applicable - one-shot per order
Attribution       : 30-day cookie (content/creator); 7-day (coupon/cashback)
Validation        : 35-day lock - covers the 30-day return window
Payment           : net-30, $50 minimum threshold; clawback on return/chargeback,
                    negative balance carried forward
Economics         : contribution margin = $39 - $11.04 = $27.96; post-return (x0.95) = $26.56
                    1/3 to 1/2 band = $8.85-$13.28 → 18% ($10.80) sits inside it
                    and at 27.7% of gross margin (inside the 20-30% sanity band)
                    projected blended cost per incremental customer ≈ $14-16 < $22 CAC → PASS
Validation plan   : 30-day holdout on both cashback sites before granting standard rates;
                    exclusive codes per creator to measure lift
KPIs              : cost per incremental affiliate customer vs $22 CAC; new-customer share;
                    return-driven reversal rate; revenue share of top 10% partners
```

What differs from the SaaS spec:

- One-shot vs recurring
- 30-day vs 90-day window
- Validation tied to the return window vs trial-to-paid

What is identical:

- Net-30
- $50 threshold
- Clawback carry-forward
- Coupon gating
- The holdout plan

## Negative example - what NOT to do

Inputs:

- Consumer-electronics accessories store
- $200 AOV
- 22% gross margin ($44)
- $18 variable costs/order
- 6% returns

The founder saw beauty programs paying 20% and wants to "match the market to attract affiliates."

```
Proposed (copied) rate : 20% of order value = $40 per order
Contribution margin    : $44 - $18 = $26; post-return (x0.94) = $24.44
Result                 : -$15.56 PER ORDER before any other marketing cost
Ceiling check          : max payable = 1/2 x $24.44 = $12.22 → ~6% of AOV, not 20%
Pass threshold         : FAILS both conditions - above the ceiling, and effective
                         cost per customer exceeds any sane CAC
```

Three compounding mistakes:

1. **Copied a benchmark across verticals** - beauty sustains 20% because its margin is 65-80%, while electronics margin is 22%. The rate must come from this catalog's contribution margin.
2. **Flat percentage over a wide AOV spread** - the store sells $15 cables and $400 monitors. 20% of a $400 order is $80 against maybe $50 of margin. One large order wipes out the economics.
3. **The loss is invisible at launch** - it surfaces only after returns net out, weeks into the program, when partners are already recruited at the unsustainable rate and cutting it triggers churn and network notice rules.

The honest recommendation:

1. A derived 4-6% rate, or a flat $10 CPA (consistent with the published 1-10% electronics range).
2. Narrow the program to high-margin accessory SKUs if partners will not work for that.
3. If neither recruits, the affiliate channel does not fit this margin structure: say so rather than launching a program that loses money per sale.
