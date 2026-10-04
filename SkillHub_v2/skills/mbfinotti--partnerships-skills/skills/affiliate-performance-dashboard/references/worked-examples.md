# Worked Examples

Two full specs and one negative example. Every target and threshold below tagged [DERIVE] is illustrative - recompute from the program's own history before adopting.

## Table of Contents

- [B2B SaaS spec - project-management tool, 350 partners, 20% recurring for 12 months, 90-day cookie, 60-day validation](#b2b-saas-spec---project-management-tool-350-partners-20-recurring-for-12-months-90-day-cookie-60-day-validation)
- [B2C ecommerce spec - apparel store, 900 affiliates, 10% CPA on order value, 30-day cookie, 45-day validation](#b2c-ecommerce-spec---apparel-store-900-affiliates-10-cpa-on-order-value-30-day-cookie-45-day-validation)
- [Negative example - do not deliver this spec](#negative-example---do-not-deliver-this-spec)

## B2B SaaS spec - project-management tool, 350 partners, 20% recurring for 12 months, 90-day cookie, 60-day validation

```
DASHBOARD SPEC - Acme PM affiliate program
Header    : audiences: exec (monthly) + program ops (daily); source of truth: billing
            system (platform numbers reconciled to it); UTC, validation-date basis,
            USD, 60-day validation window
Metrics   :
 Net program contribution | attributed net MRR-derived revenue - (validated commission
   + platform fee + agency fee), calendar month, validated only | Business | Billing
   | tile + 13-mo line | > $0 and growing | 2 consecutive down months | [DERIVE]
 Cost of sale | (validated commission + all fees) / attributed net revenue, monthly
   | Business | Billing | tile | <= 25% [DERIVE] | > 30% | [DERIVE]
 Partner-sourced MRR | MRR from partner-sourced accounts, billing-interval normalized,
   monthly | Business | Billing+CRM | line | growth trend | -10% MoM | [DERIVE]
 Partner-sourced vs influenced ARR | two capped numbers, sourced precedence, quarterly
   | Business | CRM | paired tiles | n/a | never summed | rule, [VENDOR consensus]
 Trial-to-paid rate | referred paid conversions / referred trials, per monthly cohort,
   unique accounts | Input | Product analytics | cohort bars | own baseline | -2 SD
   vs 6-mo mean | [DERIVE]
 New-to-file share | net-new accounts / partner-sourced accounts, monthly | Input
   | CRM join | line | >= 60% [DERIVE] | < 45% | [DERIVE]
 Active-partner rate | partners with >= 1 validated conversion in 90 days / enrolled,
   monthly | Health | Platform | tile | own band | < 15% | [DERIVE]
 Churn-adjusted partner LTV ratio | 24-mo referred revenue net of churn / first-year
   payout, quarterly | Health | Billing | table by partner type | >= 4x | < 3x |
   [SYNTH calibration 4.2-9.5x; band is ours]
 Reversal rate | reversed / total conversions, validation basis, monthly | Health
   | Platform | line vs band | < 3% | > 5% | [DERIVE]
 Top-5-partner share | top-5 validated revenue / program revenue, quarterly | Health
   | Billing | tile on exec view | < 50% | >= 50% | threshold [VENDOR], band [DERIVE]
Views     : exec: contribution, cost of sale, sourced MRR, top-5 share -> revenue trend
            + partner-type mix -> sourced/influenced pair -> alert strip
            ops: trial-to-paid, signup conv rate, reversal, pending vs approved,
            1-partner share
            -> daily conversions -> partner leaderboard -> alert strip
Dimensions: partner, partner type, plan, geography
Cadence   : daily ops / weekly acquisition / monthly business review (program owner
            + finance) / quarterly portfolio review (adds VP)
Alerts    : reversal spike > 2 SD vs 30-day mean -> program owner, chat channel, 24h;
            single-partner share +10pt in 7 days -> program owner, chat, 24h;
            trial-to-paid cohort -2 SD -> partner manager, weekly review, 1 wk
Open items: influenced-ARR definition awaiting CRM field; agency fee allocation
            awaiting finance confirmation
```

Why it passes:

- Contribution, cost of sale, and top-5 share sit on one exec view.
- Every row states formula, window, counting method.
- Every alert has owner/channel/response time.
- Vendor numbers appear only as calibration tags.

Two ranking calls are visible in it. EPC is absent because recurring commission makes it uninterpretable in B2B. Churn-adjusted LTV is present despite being the starved rung, because the 12-month recurring cap is up for renegotiation: the promoting condition, stated rather than assumed.

## B2C ecommerce spec - apparel store, 900 affiliates, 10% CPA on order value, 30-day cookie, 45-day validation

```
DASHBOARD SPEC - Riverline Apparel affiliate program
Header    : audiences: marketing director (monthly) + affiliate manager (daily);
            source of truth: order database (network export reconciled to it);
            America/New_York, transaction-date basis for orders and validation-date
            for payables, USD, 45-day validation window
Metrics   :
 Net program contribution | attributed net revenue (net of returns, excl. tax/shipping)
   - (validated commission + network fee + placement fees), monthly | Business |
   Orders DB | tile + line | positive, seasonal-adjusted | 2 down months | [DERIVE]
 Attributed ROAS vs ROI | ROAS = attributed rev / program spend; ROI adds COGS;
   both monthly, labeled "last-click, 30-day cookie" | Business | Orders DB + finance
   | paired tiles | own baseline | -20% vs 3-mo mean | formulas [VENDOR glossary]
 New-to-file rate | first-ever customers / affiliate orders, order-level, monthly
   | Input | Orders DB | line by partner type | >= 35% [DERIVE] | < 25% | [DERIVE]
 AOV net of returns | net order revenue / orders, excl. tax+shipping, monthly, by
   partner type | Input | Orders DB | bars | own baseline | n/a | [DERIVE]
 Click-to-conversion | orders / unique clicks x 100, 30-day window | Input | Network
   + orders | line | own baseline | -2 SD vs 30-day mean | [DERIVE]
 EPC | validated commission / unique clicks (per-click, bot-filtered), weekly | Input
   | Network | line | own baseline | -2 SD | convention declared, [DERIVE]
 Active-affiliate rate | affiliates with >= 1 validated order in 60 days / enrolled,
   monthly | Health | Network | tile | own band | < 12% | [DERIVE]
 Reversal rate | reversed / total orders, validation basis, monthly | Health | Orders
   DB | line vs band | < 8% | > 10% | red line [VENDOR], band [DERIVE]
 Top-10% share | top-decile validated revenue / program revenue, quarterly | Health
   | Orders DB | exec tile | own band | top 5 partners >= 50% | [VENDOR threshold]
 Checkout-adjacent share | coupon+cashback+extension validated revenue / program
   revenue, monthly | Health | Network | stacked area | own band | +10pt in a quarter
   -> incrementality review | [DERIVE]
Views     : exec: contribution, ROAS/ROI, new-to-file, top-10% share -> revenue trend
            + partner-type mix -> alert strip
            ops: EPC, conv rate, reversal, pending vs approved, 1-partner share ->
            daily orders -> affiliate leaderboard w/ new-to-file column -> alert strip
Dimensions: partner, partner type, product category, device, landing page, creative
Cadence   : daily ops / weekly acquisition + creative review / monthly performance
            (director) / quarterly concentration + commission-reduction test readout
Alerts    : reversal spike > 2 SD vs 30-day mean -> affiliate manager, chat, same day;
            single-partner share spike -> manager, chat, 24h; brand-bidding flag ->
            manager, email, 48h (rule owned by fraud rule set)
Open items: cross-device loss unquantified; return-reason codes not yet in export
```

Why it passes:

- The return-window reversal driver, order-level counting, and checkout-adjacent share are all explicit.
- The ROI tile carries its attribution basis.
- The incrementality review is scheduled, not implied.
- Landing page and creative appear among the dimensions, the starved pair, because this program funds creative feeds and offers partners optimization help.
- Geography is absent rather than parked, since the store ships one market.

## Negative example - do not deliver this spec

> "Headline KPIs: total clicks (target 1M/month), affiliate signups (target 200/month), and gross commissions earned. Program ROI = revenue tracked by the network / commissions, currently 14:1 - well above the industry's 12:1, so the program is healthy. All partners in one leaderboard, refreshed live. Alert: email the team if daily revenue falls below $10,000."

Line by line:

- Clicks and signups as headline KPIs are vanity metrics informing no decision; 90 of 200 signups never activating would be invisible. Demote to diagnostics; headline contribution and cost of sale.
- Gross commissions overstate cost and revenue at once; reversals and the validation window vanish. Validated only, pending shown separately.
- Network-tracked revenue over commissions is last-click-only, fee-free, COGS-blind, and computed on the claimant's own numbers - it inflates checkout-adjacent partners and ignores the source of truth. Reconcile to orders/billing; include all fees; label attribution basis.
- Beating "the industry's 12:1" adopts a trade-body average - drawn from member networks - as the program's own target. Calibration only; derive baselines from history.
- No concentration view: one super-affiliate could be 40% of revenue and its loss invisible until it happens. Top-N share on the exec view, quarterly.
- One live leaderboard for everyone is a single view with a single refresh rate: executives get noise, operators get no alert design. Two views, tiered cadence.
- A static $10K floor fires all winter and never in summer - alert fatigue, then a real drop gets ignored. Rolling-baseline threshold with owner, channel, response time.
