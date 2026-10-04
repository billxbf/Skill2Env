# Rate and Tier Verification

Recompute every line's expected commission independently from raw inputs, then diff against the proposed value. Never trust the platform's own stated total as evidence of its own correctness.

## Marginal vs retroactive tiers - worked math

Example structure: 20% up to $10,000 referred volume, 25% from $10,000 to $25,000, 30% above $25,000. Partner's period volume: $26,000.

- **Marginal (incremental)** - each band pays its own rate:
  `20% x 10,000 + 25% x 15,000 + 30% x 1,000 = 2,000 + 3,750 + 300 = $6,050`
- **Retroactive ("back to dollar one")** - crossing a threshold re-rates the entire volume:
  `30% x 26,000 = $7,800`

Same partner, same sales, $1,750 apart. The audit must know which method the written structure specifies and recompute with exactly that method - most programs use marginal to preserve margin.

Retroactive tiers create cliffs: at $24,999 the retroactive payout is `25% x 24,999 = $6,249.75`; at $25,001 it is `30% x 25,001 = $7,500.30`. Two dollars of revenue moved $1,250.55 of commission. Treat every line near a retroactive breakpoint as high-risk and review it 100%.

## The boundary-operator bug

- Decide whether the threshold dollar itself earns the old rate or the new one: `>=` vs `>` at each breakpoint.
- Recompute boundary lines under both operators; if the results differ and the written structure is silent, raise a finding - the structure is ambiguous, not the math.
- Walk marginal tiers in ascending order, consuming each band's capacity (`up_to - from`) before spilling into the next; a common implementation bug applies the top rate flat instead of graduating.

## Overrides checklist - verify per line

- **Partner-type override**: agency, creator, reseller, coupon/cashback rates differ; confirm each line used its partner's assigned rate card, not the program default.
- **Promo/bonus windows**: evaluate against start AND end datetimes in the run's timezone; a promo rate applied outside its window is a finding either way.
- **New-customer gating**: confirm how "new" is determined - email, customer ID, first-order flag - and that the gate was actually evaluated, not assumed.
- **Sub-affiliate / second-tier overrides**: a parent's override commission needs its own line, its own rate, and its own dedup key - and must never double-pay the child's base commission.
- **Grandfathered legacy rates**: partners kept on an old rate card after a migration; verify against the partner's contract, not the current published card.
- **Buyout clauses**: a recurring-commission partner may have been bought out (lump sum ends the stream); any recurring line for a bought-out account is an overpay.

## Terms in force at the transaction

Recompute against the contract terms active on the original transaction date - never today's terms. At least one major platform re-evaluates a _modified_ action against currently-active contract terms, so an expired promo can silently change a historical line's payout when the line is edited. Any line whose applied rate matches today's card but not the transaction-date card is a finding.

## Recurring revenue-share specifics (B2B SaaS)

- **Commission base**: MRR vs ARR - confirm which, and confirm the base is the _settled_ billing amount, not the plan list price.
- **Discounts and coupons** reduce the commissionable base; a line commissioned on list price while the customer paid a discounted invoice is an overpay.
- **Proration**: mid-cycle upgrades/downgrades produce prorated invoices; the commission must follow the prorated amount, both directions.
- **Seat expansion**: added seats mid-cycle are commissionable on the prorated add; verify removed seats follow the program's stated policy (many programs give no mid-cycle credit for removals - check the policy, then check the data matches it).
- **Duration cap**: a 12-month cap means month 13's billing event earns zero; lifetime means it keeps paying. Verify each recurring line's month index against the cap - month-13 payments under a 12-month cap are a systematic, compounding overpay.
- **Churn**: a churned subscription must stop generating lines the cycle it lapses; pay in arrears on confirmed billing events so this happens automatically, and flag any commission line without a matching settled invoice.
