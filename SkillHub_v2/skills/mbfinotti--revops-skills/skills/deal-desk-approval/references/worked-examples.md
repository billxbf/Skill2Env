# Worked Examples

All numbers below are illustrative constructions for a fictional company, tagged the way the real spec must tag them:

- `[derived]` - computed from that company's own deal data.
- `[illustrative]` - a stand-in to replace with a derived value.
- `[policy]` - a deliberate house decision, not a benchmark.

## Example 1 - B2B mid-market SaaS (sales-led, $30K median ACV, near-zero COGS)

```
DEAL DESK APPROVAL SPEC - Northbeam CRM (fictional), 2026-08-25
Scope        : new, renewal, and expansion deals with any non-standard element across the
               five levers. Out of scope: list pricing/packaging, expense/procurement approvals.
Levers       : all five governed; every non-price concession converted to discount-equivalent
               value at intake (net-90 on a $60K annual deal booked as ~1.5% [derived from
               internal cost of capital]; free implementation booked at its list price).
Matrix       : dimensions = discount % x ACV band x motion, fenced per segment.
               Tier 0 auto-approve: <8% new business [derived - win rate flat beyond 8% in
               6 quarters of win-rate-by-discount-band data]; <3% renewals [derived].
               Tier 1 (manager + desk analyst): 8-18% [derived, p75 of discount distribution].
               Tier 2 (VP Sales + Finance): 18-30%, or any 2+ lever change, or ACV > $150K
               [policy - leadership visibility band].
               Tier 3 (CRO + CFO jointly): >30%, below-floor economics, marquee-logo terms.
               Floor: 78% gross margin per deal [policy - set from this company's own COGS
               and target model; NOT the circulating "75%" number]. No tier waives it.
Prohibited   : MFN/best-price, price holds without scope+term+expiry, uncapped liability
               outside the carve-out list, roadmap commitments without Product+Delivery
               pre-approval. Give-get mandatory even to table one.
Intake       : full field set; impact-of-denial mandatory and weighted highest; requests
               missing fields bounce with a structured return; clock starts at completeness.
Routing      : fast lane (1 lever, in guardrails) / complex lane (2-3 levers) / exception
               lane (below floor, prohibited terms, novel security, high precedent).
SLAs         : response 4 business hours all lanes [policy]; decision same day / 2 days /
               5 days by lane [policy]; 50/80/100 elapsed escalation; every approver has a
               named delegate with dated windows; peak mode: quarter-end completeness
               cutoff at T-5 business days, exec escalation window daily 4-5pm [policy].
Precedent    : register in the system of record with expiry on every exception (default
               60 days [policy]); monthly exceptions forum with change backlog.
               Renewal treatment [policy, decided in interview]: discounts sunset at term
               end; step-up over one renewal for exceptions >20%; nothing grandfathers
               silently - carry-over requires a fresh Tier 2 approval.
Constraints  : line-item-steered discounts, future-discount promises, termination-right
               changes, >1-year payment tails -> Finance/Legal per the routing table.
Calibration  : thresholds re-derived quarterly from discount distribution + win rate by
               band; exception analytics monthly; late-discovery rate tracked per rep.
KPIs         : cycle time (median + p90, complete-submission to communicated decision),
               win rate, discount rate, per-deal margin, leakage - reported together.
```

## Example 2 - PLG / self-serve and B2C: the rules-driven equivalent

No human chain exists below the sales-assist line; the "desk" is a published rule set.

```
DISCOUNT POLICY SPEC - Flowkit (fictional PLG, $29-99/mo self-serve; sales assist > $10K/yr)
Published bands : annual prepay -17% [policy, published]; education/nonprofit -30% with
                  eligibility verification [policy, published]; no other self-serve discounts.
Promo governance: promo codes single-use, expiring, capped per campaign budget [policy];
                  stacking prohibited by the promo engine, not by support judgment;
                  win-back and save offers fixed-menu (2 months -20% max), logged per
                  account, once per 12 months [policy].
Exception rules : support may not invent discounts; every published rule states its own
                  exception path ("if X, then Y"), so the answer to an unlisted ask is no.
Human line      : > $10K/yr or 25+ seats -> sales-assist, where the B2B matrix (Example 1
                  shape) takes over [policy].
Creep monitoring: monthly - % of revenue on any discount, average realized discount,
                  save-offer redemption vs churn saved, coupon-leakage check (codes on
                  coupon aggregators), refund-policy abuse rate.
```

The transferable core is identical to B2B: bands are defined in advance, every exception is logged, and creep is monitored - only the enforcement mechanism changes (promo engine and published terms instead of a human chain). Present the equivalence as reasoning about the two motions, not as a documented finding.

## Example 3 - Negative example: the matrix that erodes itself

A spec like this fails even though it looks like governance:

- Governs discount % only. Reps stop asking for 25% off and start asking for net-120, free onboarding, an uncapped SLA credit, and a price hold "for the co-sell" - none of which route anywhere. Concession value leaves through the four ungoverned levers.
- Single top approver (the CFO) with no delegate and no elapsed-SLA escalation.
  - Requests sit for a week in a mailbox checked daily.
  - The buyer's procurement window closes.
  - Reps learn to close "verbally" first and seek approval after; the desk is now decorative.
- Approvals happen in chat threads. A year later nobody can distinguish an approved exception from an informal precedent, so every rep cites "the deal we did for Acme" and every customer cites last year's "one-time" discount - which had no expiry date and no register entry.
- The one hard rule is a "75% margin floor" imported from a blog post, unrelated to the company's actual COGS or target model - so it binds nothing real, while actual leakage happens above it.
- Cycle time is reported as a mean, which looks fine at 6 business hours while the p90 sits at 4 days - exactly the tail that drives the bypass behavior nobody can see.

Fix path:

- Govern all five levers.
- Delegate + 50/80/100 escalation.
- Move approvals into the system of record with a register and expiry dates.
- Derive the floor and tiers from own data.
- Report median + p90.
