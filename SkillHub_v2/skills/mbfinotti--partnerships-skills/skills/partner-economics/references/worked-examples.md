# Worked Examples

Both examples model the same fictional case: a B2B SaaS vendor ($40K average ACV, 78% gross margin, direct CAC $11,000) evaluating a proposed reseller. Numbers are illustrative, built to be internally consistent - not benchmarks.

## Positive example - a memo that earns a verdict

```
PARTNER ECONOMICS: Meridian Systems (reseller/VAR), 2026-03-10
Decision        : sign / don't sign. Threshold agreed with CFO: partner acquisition cost
                  per $1 of net revenue below the direct motion's $0.275 ($11,000 CAC on
                  $40K ACV), and cumulative contribution positive by month 20.
Partner type    : Reseller. 25% discount off list; +5pp deal-registration uplift;
                  $30K/yr MDF commitment; no marketplace flow.
Revenue model   : Sourced only: Meridian originates; no influenced credit claimed.
                  Y1: 6 deals × $40K ACV = $240K. Y2: 14 deals = $560K. Y3: 20 = $800K.
                  Volume source: Meridian's own plan, haircut 30% (unverified, partner-supplied).
Cost stack (Y2) : discount $168K (30% effective incl. registration) | MDF $30K |
                  0.4 FTE partner manager $52K | enablement/certification $18K |
                  support uplift $12K | portal allocation $3K  → total $283K
Net contribution: Y1 −$74K (ramp) | Y2 +$154K margin-adjusted | Y3 +$248K
Partner CAC     : Y2 acquisition cost excluding discount $115K → $8,214/customer; fully
                  loaded including the $168K discount $283K → $20,214/customer. Neither
                  figure compares to direct CAC ($11,000) per customer: the partner nets
                  us $28K per deal against direct's $40K, so per-customer numbers price
                  different goods. Like-for-like, per $1 of net revenue: partner $0.293
                  vs direct $0.275. Fails the threshold by 6.7%. (Against the Pacific
                  Crest $0.53-per-$1-of-new-ACV channel benchmark the partner is normal
                  at $0.505: normal for the channel, still worse than our own direct.)
Ramp & payback  : first revenue month 5; double-cost months 1-8;
                  cumulative contribution crosses zero month 17. Inside threshold.
Incrementality  : Meridian's install base overlaps our outbound territory ~20%.
                  Assumed 75% incremental; verdict still holds at 50%, flips at 35%.
Partner's P&L   : Meridian earns $168K margin + est. 2x in implementation services (their
                  model, unverified). Passes the Third-Law check: the split funds their climb.
Sensitivity     : two levers, both tight. Hold effective discount at or under 25.3% at the
                  planned 14 Y2 deals, or land 15 Y2 deals at the proposed 30%. Either one
                  clears $0.275; neither has slack. Incrementality < 35% flips it whatever
                  the discount. Ramp length ±3 months does not flip it.
Verdict         : RENEGOTIATE: do not sign at 30% effective. Ask: 25% all-in, funding the
                  deal-registration uplift from MDF instead of stacking it on the discount.
                  Re-run at signature; sign if the term lands at or under 25%, with a
                  month-12 gate of ≥5 closed deals.
Open questions  : Meridian's services attach rate unverified; churn of their sourced
                  customers unknown: a 10pp retention gap vs direct would flip Y3.
```

Why it works:

- Sourced-only revenue with a haircut and a named source.
- The cost stack is fully loaded, including people time.
- CAC is stated on both conventions and then compared on the only basis that is like-for-like.
- Incrementality carries a number and a flip point.
- The partner's own P&L is checked.
- The verdict names the exact term that would reverse it.

The CAC line is the part worth copying. Divide each side's acquisition cost by the net revenue it actually bought: neither convention produces a per-customer number comparable to direct when the partner nets $28K per deal against direct's $40K.

Two conventions are internally consistent; only one can be used at a time:

- Book revenue gross and charge the discount to acquisition cost.
- Book revenue net of discount and leave it out of cost.

Reporting the $8,214 non-discount figure against the $11,000 direct CAC as a 25% win is the trap: it charges the $168K discount to nobody while still counting the revenue it bought at list, and it makes every reseller look cheap.

A memo that lands on "renegotiate" rather than "sign" is the skill working, not failing.

## Negative example - a memo that flatters the partner

Each line annotated with what is wrong.

```
PARTNER ECONOMICS: Meridian Systems, 2026-03-10
Revenue         : $1.2M partner-attributed pipeline over 3 years.
```

- Blends sourced and influenced into one "attributed" number, and quotes pipeline, not closed-won. The single most common inflation move.

```
Costs           : 25% reseller discount.
```

- Cost stack missing everything but the discount: no MDF, no partner-manager time, no enablement, no support uplift. This is the $2M-partner-that-is-really-$1.05M failure in miniature.

```
Partner LTV     : $40K ACV × 5-year lifetime = $200K per customer.
```

- LTV computed on revenue, not gross margin, and lifetime asserted with no churn basis. At 78% margin the honest figure is ~$156K before churn adjustment.

```
Partner CAC     : $0: Meridian brings the customers.
```

- Ignores every acquisition-side cost: MDF, enablement, partner-manager time, the discount itself. Partner CAC is never zero; a zero here means the model never looked.

```
Incrementality  : all partner revenue is net-new by definition (they source the deals).
```

- Assumes 100% incrementality. Sourcing proves origination, not incrementality - the deal may have arrived through direct or another partner anyway.

```
Benchmark       : industry data shows partners deliver 80% of channel revenue
                  through top performers like Meridian.
```

- Launders the untraceable 80/20 statistic as fact, and misapplies a concentration claim as if it predicted this partner's performance.

```
Verdict         : strong strategic fit: recommend signing.
```

- No threshold, no sensitivity, no ramp, no payback month, no open questions. "Strategic fit" is doing the work the numbers were supposed to do.

The tell across all seven lines: every omission moves the answer in the partner's favor. A model whose every simplification points the same direction was built to justify, not to decide.
