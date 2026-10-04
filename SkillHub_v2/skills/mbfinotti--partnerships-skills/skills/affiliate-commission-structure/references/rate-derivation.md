# Rate Derivation - Ceiling Calculations and Pass-Threshold Math

The rate is derived from unit economics, never copied from a benchmark. Two derivation paths - one per business model - plus the duration-cost comparison and the pass-threshold check.

## Ecommerce ceiling: the contribution-margin walk

Sequence (per Track360 and Shopify guides, 2026 - vendor content, practitioner consensus):

1. Gross margin = selling price minus COGS for a representative order.
2. Subtract variable costs (fulfilment, shipping, payment processing, platform fees) → contribution margin.
3. Net out the expected return rate → post-return contribution margin.
4. Pay one-third to one-half of post-return contribution margin.
5. Sanity band: total commission should land at 20-30% of gross margin.

Worked example - $80 AOV physical product:

```
Selling price                     $80.00
COGS                             -$32.00   → gross margin $48.00 (60%)
Shipping                          -$8.00
Fulfilment                        -$4.00
Payment processing (2.9% + $0.30) -$2.62   → contribution margin $33.38
Expected returns (8%)             ×0.92    → post-return contribution $30.71
Pay 1/3 to 1/2                             → $10.24 to $15.35 per order
As commission rate                         → 12.8% to 19.2% of AOV
Sanity check: 20-30% of gross margin ($48) → $9.60 to $14.40 ✓ (overlaps)
Publishable rate                           → 13-17%
```

A companion formula from Shopify's May 2026 guide (vendor content - practitioner consensus, not peer-reviewed): maximum sustainable affiliate acquisition cost = gross profit per conversion − non-affiliate variable costs − required contribution margin. Its worked example yields a $15 maximum on a representative order.

## SaaS ceiling: the LTV:CAC walk

Commission is part of CAC. Two constraints (practitioner consensus per multiple platform guides):

- Keep LTV:CAC ≥ ~3:1 and blended CAC payback ≤ ~12 months.
- Keep total lifetime commission per customer at 5-15% of LTV, never above 30-40% of gross margin.

Why 3:1 caps the budget: at 80% gross margin and LTV:CAC of 3:1, the total CAC budget is ~27% of revenue LTV (0.80 ÷ 3) - and affiliate commission shares that budget with every other acquisition cost. A 30% lifetime commission alone blows it. A bounded 12-month or tapering model fits.

Worked example (Tapfiliate, vendor blog - practitioner consensus), and a demonstration of why vendor guidance gets checked against your own ceiling rather than copied:

- 85% gross margin
- 18-month average tenure
- $50/mo plan
- $900 LTV
- $765 gross profit

A 30% recurring rate ($15/mo) pays $270 total. That is **30% of LTV - twice the 15% ceiling** - and 35% of gross profit. It fails the LTV leg of the gate below and only scrapes inside the gross-margin leg, and the gate needs both.

Their proposed fix does not rescue it: 20% ($10/mo) pays $180 = 20% of LTV, and the $50-per-10-sales bonus takes it to $185 = 20.6%. Still over.

What fits the ceiling on these numbers is a duration rule, not a lower headline: 30% for months 1-6 then 15% for months 7-12 pays $90 + $45 = $135, exactly 15% of LTV and 17.6% of gross profit, both legs clear. This keeps the 30% headline the recruiting pitch is built on. The next section is that lever.

## The duration rule beats the headline percentage

The single most consequential recurring-commission decision. Worked comparison (Track360, vendor blog - practitioner consensus): $100/mo plan, 30% rate, 20-month average customer tenure ($2,000 revenue):

| Duration rule                          | Total paid | Effective rate on customer revenue |
| -------------------------------------- | ---------- | ---------------------------------- |
| Lifetime (uncapped)                    | $600       | 30.0%                              |
| Capped at 12 months                    | $360       | 18.0%                              |
| Taper: 30% months 1-6, 15% months 7-12 | $270       | 13.5%                              |

Same 30% headline, same recruiting pitch - less than half the cost under the taper. Negotiate duration before percentage: a generous headline with a 12-month cap usually beats a thin lifetime rate on both recruiting and economics.

A 25% rev-share capped at 12 months on a $99/mo product pays a hard maximum of $297 per customer, a number finance can model. Uncapped lifetime has no such number.

## Pass-threshold math

The structure passes only when both conditions hold:

1. **Below CAC**: projected blended cost per incremental affiliate-acquired customer < current blended CAC.
2. **Inside the ceiling**: total commission per customer sits inside the derived margin ceiling.
   - Ecommerce: ≤ one-half of post-return contribution margin.
   - SaaS: ≤ 15% of LTV and ≤ 30-40% of gross margin.

Compute the projected cost:

```
cost per incremental customer =
  (total commissions incl. recurring within the cap + bonuses + network/platform fees)
  ÷ (affiliate-acquired customers × expected incrementality share)
```

Discount the denominator by incrementality: if coupon partners drive 40% of volume at ~30% incrementality, only that fraction counts as acquired. Ignoring this is how a program "beats CAC" on paper while buying its own existing demand.

## Levers when the check fails, ranked

Rank by cost removed per unit of effort and recruiting damage - not by which is cheapest to type.

- efficiency: shorten duration or add a taper > rebalance the partner-type split > flatten or delay tiers > cut the headline rate
- value (cost removed): shorten duration > rebalance the split > cut the headline > flatten or delay tiers - duration and the split both remove cost without removing acquired customers, because they cut where incrementality is lowest
- effort: rebalance the split > flatten or delay tiers > cut the headline == shorten duration - the last two tie on a pre-launch card, where each is one field, but on a live card both become a migration
- compliance cost (live cards only): cut the headline > flatten or delay tiers > shorten duration > rebalance the split - a rate decrease runs into the network's contractual decrease caps and notice periods (one major network publishes a hard rule: at most a 20% reduction each time, no more than once every 30 days, with at least 7 days' partner notice), while a partner-type split rebalance usually does not, because it adds a rate row rather than cutting an existing one

1. **Shorten recurring duration or add a taper.** Removes the largest share of effective cost, keeps the headline the recruiting pitch is built on, and on most platforms is a single field.
2. **Rebalance the partner-type split** (cap or gate bottom-funnel rates) removes cost concentrated where incrementality is lowest. Needs a new-customer flag in tracking. Without one this drops behind tiers until the flag ships.
3. **Flatten or delay tiers.** Near-zero before launch - just do not ship them - so on a pre-launch card this moves to first. On a live card it is a migration with notice and grandfathering, and stays here.
4. **Cut the headline rate.** Last: it hits recruiting hardest, and it is the least reversible lever on a live card.

What this order starves: rebalancing the partner-type split. It removes cost exactly where incrementality is lowest, so it sits near the top of the value line. But it tops the effort line because it needs a new-customer flag in tracking plus a per-partner-type migration.

That is why it loses to a single duration field every time. Promote it above duration when the program's overpayment is concentrated in coupon/cashback partners and the flag already exists, and when the mandate is a rate card meant to survive several years rather than one quarter's payouts.

Constraints delete a lever rather than demote it: a one-shot ecommerce program has no duration lever at all, and a program with no tiers has no tier lever - do not pad the list with either.

If no combination passes, narrow the program to high-margin SKUs (ecommerce) or high-margin plans (SaaS) where a ceiling exists that partners will still work for. Recommend not launching only when no narrowing leaves one.

Identical math for B2B and B2C - only the inputs differ (churn and trial conversion vs return rate, and LTV vs per-order contribution).
