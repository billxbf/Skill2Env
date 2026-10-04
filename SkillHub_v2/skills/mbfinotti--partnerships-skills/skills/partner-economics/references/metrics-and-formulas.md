# Metrics and Formulas

The working metric set for one partner relationship, with worked numbers. No canonical formula sheet exists in the field; these are the forms practitioners converge on. Compute every value on gross margin where the formula says so - revenue-based versions flatter the partner.

## Revenue attribution - the foundation

- Partner-sourced: closed-won revenue from opportunities the partner originated, proven by a timestamp such as deal registration. The deal would not exist without the partner.
- Partner-influenced: revenue on deals your team sourced where the partner materially advanced the deal.
- Partner-attached: any partner touch - the loosest bucket.
- Defensible defaults (practitioner consensus):
  - Track all three separately in the CRM.
  - Apply a fixed attribution window (~14 days from deal creation).
  - Credit one partner per deal.
  - Uncapped influence is how attributed revenue exceeds total revenue - the result that destroys finance's trust permanently.

## Net contribution

```
Net revenue after partner cost = list or ACV
  − partner discount − rebates/SPIFFs − MDF − marketplace fee − cost-to-serve
```

Cost-to-serve is three distinct buckets: recruit, enable, serve. It covers:

- Account-manager time.
- Training/certification delivery.
- Portal/tooling allocation.
- Support.
- Events/travel.

Worked restatement (practitioner example): a partner generating $2,000,000 in annual revenue, net of $500,000 discounts, $200,000 MDF, $150,000 dedicated account management, and $100,000 training/support, contributes **$1,050,000** - not $2M. Run this restatement on every headline number before it enters a memo.

## Partner CAC

```
Partner CAC = (partner program costs + incentives + MDF + channel overhead attributable to this partner)
              / new customers acquired via this partner
```

- Compare against direct CAC over the same window. The channel thesis exists only if partner CAC is materially below direct CAC.
- Diagnostic when partner CAC comes out HIGHER than direct: check these three causes in order. Each is cheaper to rule out than the next, and the first one invalidates the number outright.
  1. Attribution double-counting deals that would have closed anyway - a re-run of the query, near-zero effort.
  2. Commission rate too high for the deal size - an hour of arithmetic, and the fix is a term you can negotiate.
  3. Poorly qualified partner leads - weeks of cohort win-rate and retention data, and the slowest fix of the three.
- Best-documented anchor: the 2014 Pacific Crest/KeyBanc survey put channel CAC at $0.53 per $1 of new ACV (industry survey - the strongest channel-CAC evidence available; the often-quoted "$1.02 field sales" companion figure is not confirmed in the published write-up).

## ROI, LTV, payback

```
Partner ROI = ((partner-attributable revenue × gross margin) − partner-specific costs) / partner-specific costs
LTV (partner-sourced cohort) = ARPU × gross margin % / churn rate    : margin, never revenue
LTV:CAC ≥ 3:1 as the standard health line (SaaS practitioner convention)
CAC payback = partner CAC / (ARPU × gross margin %)
```

Practitioner rules of thumb, all vendor/blog evidence class - label them:

- Partner ROI above 3x with CAC payback under ~120 days reads healthy.
- Partner CAC above ~1.5x direct signals a broken structure.
- Partner-sourced retention lagging direct by more than 10-15pp signals ICP misalignment.

## Ramp and payback

- The first 6-12 months are a double cost: funding the partner's enablement and your own team simultaneously, before the partner sells or services anything alone. Analyst description of the career risk: an 18-month channel build where most people get fired at month 12.
- Model: months to first revenue → months to steady-state productivity → the month cumulative net contribution crosses zero. Present that break-even month explicitly; NPV-discount the ramp if the sign-off owner is finance.
- The upside case once ramped: a partner that can sell and service deals alone pushes incremental CAC toward zero and lifts LTV via lower churn - but only after the ramp is paid for.

## Incrementality

Attributed revenue is not incremental revenue. The canonical demonstration: Blake, Nosko & Tadelis (2015, _Econometrica_) - eBay halted brand-keyword paid search and 99.5% of clicks were retained organically. A channel can carry a real, positive, statistically significant revenue number while contributing almost zero incremental business.

Ranked by evidence bought per unit of effort, strongest ratio first - the axes disagree, so read all four:

- efficiency: assumed-rate band > matched holdout > geo split > channel pause
- value, meaning evidence strength: channel pause > matched holdout == geo split > assumed-rate band
- effort: channel pause > geo split > matched holdout > assumed-rate band
- compliance cost: channel pause > geo split > matched holdout == assumed-rate band

Matched holdout and geo split tie on evidence strength because they are the same quasi-experiment read two ways - a treated group against an untreated one - and each is confounded in its own direction, matching quality against territory heterogeneity, with neither dominating the other. They do not tie on effort, so the holdout wins on efficiency. Matched holdout and assumed-rate band tie on compliance cost at genuine zero: both run inside the vendor's own systems, touch no clause of the partner agreement, and can be abandoned mid-way with nobody outside the company aware they ran.

| Method                      | What it buys                                                                                                                                                                                                                                          | Effort                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Assumed-rate band - default | Bounds the verdict without measuring anything: state the assumed incrementality rate as a named assumption and show the verdict at 100%, 70% and 40% incremental. A verdict that holds across the band settles the question with no experiment at all | An hour, alone, on the model already built. Fully reversible                                                               |
| Matched holdout             | Withhold partner-sourced leads from a comparable segment and read the conversion difference. Real measurement, confounded only by matching quality                                                                                                    | A week to set up in the CRM, then weeks to a quarter of read-out. Needs the partner manager's agreement and sales-ops help |
| Geo split                   | Same measurement on a territory carve-out; cleaner separation, coarser matching                                                                                                                                                                       | A quarter. Needs a rules-of-engagement change and territory sign-off, and it is visible to the partner                     |
| Channel pause               | The eBay design and the strongest evidence available outside a lab - but it spends real pipeline to get it                                                                                                                                            | A quarter of foregone revenue plus sales-leadership sign-off, and the lost pipeline never comes back                       |

Compliance cost by method, heaviest first:

- Channel pause: suspending a partner motion can breach exclusivity, minimums or rules of engagement written into the agreement, so it needs a contract read and legal sign-off before it starts, and it cannot be unwound afterwards.
- Geo split: a smaller version of the same exposure - a territory carve-out amends the rules of engagement and is visible to the partner, so it needs sign-off and is awkward to reverse.
- Matched holdout and assumed-rate band: neither carries any compliance cost.

Default to the assumed-rate band; buy an experiment only when the verdict flips inside the plausible range.

What that default starves is the channel pause: strongest evidence on the page, heaviest effort on the page, last on efficiency every time, so a program ranking on the ratio never once measures incrementality properly. Promote it when a nine-figure renewal, an exit decision, or a finance owner who rejects assumed rates makes the incrementality number the whole verdict rather than one input to it.

Where the agreement carries exclusivity or minimums the pause would breach, delete it from the menu and record it as deleted with the clause that killed it - a method left at the bottom of the list gets proposed again by whoever reads the memo next.

Re-rank against the situation too: an existing holdout, or a channel already paused for unrelated reasons, makes the measured options nearly free. This ordering is a default, not a law.

Academic literature is genuinely unsettled - documented synergy and documented substitution both exist depending on channel and product.

## Incentive ceiling

```
Max affordable partner payout per customer = (lifetime REVENUE per customer × gross margin %)
                                             − target CAC
```

Worked example: lifetime revenue $1,200, gross margin 70%, target CAC $200 → ceiling = $640. Any referral fee, commission, or discount value above the ceiling buys revenue at a loss.

Note the input here is lifetime _revenue_, not the margin-adjusted LTV defined above - applying gross margin twice halves the ceiling and rejects payouts the business can afford.

## Revenue per partner

```
RPP = partner-sourced revenue / active partners
```

For a single-partner model, use RPP of comparable active partners as the volume sanity check - and count only active partners, or the denominator flatters the program.
