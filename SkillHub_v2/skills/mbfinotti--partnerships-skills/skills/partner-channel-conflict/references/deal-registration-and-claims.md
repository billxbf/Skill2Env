# Deal Registration as a Claim Instrument

This file treats registration only as the conflict-prevention and claim-adjudication instrument: who may claim a deal, for how long, on what evidence, and what happens when two parties claim the same one. The co-sell mechanics of working a registered deal together belong to the co-sell sibling skill.

## Eligibility and required data

Codify eligibility (minimum deal size, new-logo vs upsell, opportunity type) and required data: customer name and domain, deal size, expected close date, products, and evidence of a real partner relationship with the account. Collect only fields actually used in the approval decision - every unnecessary field is a reason not to submit.

## Protection window

- Observed range **30-180 days, 90 is the most common**. Enterprise cycles run 90-180.
- Sizing rule: **at least ~75% of average sales-cycle length** (a 60-day average cycle makes a 30-day window useless).
- Common shape: 90-day validity from approval, one optional 30-day extension gated on demonstrated activity. Expiry reminders run at 30/14/7 days with one-click renewal.
- Higher partner tiers commonly earn longer windows and priority routing - the criteria belong to the tiering skill.
- Rule on expiry explicitly: an expired registration re-opens the deal. Resubmission is allowed but does not outrank a rival claim filed in the gap.

## Approval SLA

Approve or reject within 1 business day (24h benchmark). The convention ceiling is ~48 hours.

The recurring practitioner finding: partners tolerate a 48-hour process, they do not tolerate an _unpredictable_ one. An "In Review" status that acknowledges receipt without committing to a decision preserves trust while the check runs. (Benchmarks vendor-published, directionally solid.)

## Standard rejection grounds

Codify these so rejection is a rule, not a judgment call:

- Duplicate registration.
- Account already in active direct pipeline or an existing customer.
- Account on the house/named list.
- Not qualified (no budget, timeline, or decision-maker access).
- No verifiable partner relationship with the account (speculative land-grab).
- Thin submission with no evidence of value-add activity.

Every rejection carries its reason: the rejection-reason mix is itself a governance metric.

## Tie-break: two claims on the same deal

The published convention:

- **First-to-register wins.**
- **The tie-breaker is a "substantial work" test**: evidence of active pursuit (meetings held, stakeholders engaged, activity logged), not merely the earlier timestamp.
- **Vendor discretion is the explicit fallback**, exercised by the named adjudicator and documented.

Once one registration is approved, later registrations on the same opportunity are rejected as duplicates with a reason. When the rival claimant is the direct team, the same evidence standard applies - the registration timestamp and first-engagement timeline decide, not seniority - the same evidence standard the tiered escalation ladder applies at every rung.

## Margin and price protection

Registered deals commonly carry **5-15 points of extra margin** over standard partner discount (vendor-published range, one vendor illustration: 18% protected vs 8% standard). Anti-pattern: a flat uniform bump for every deal regardless of size or complexity - it fails to motivate registration of exactly the large strategic deals you most need visibility into.

## Marketplace-transacted deals

Where deals transact through a cloud marketplace, the claim and the transaction can diverge: the customer buys on the marketplace and bypasses the registered partner's margin entirely. Rule on how a registration is honored when the transaction routes through a marketplace - margin routed via the marketplace's partner-offer mechanism, or influence credit for the registered partner.

Named examples, as examples only: AWS Channel Partner Private Offers, Microsoft Multiparty Private Offers, Microsoft's CPOR partner-of-record construct (one partner of record per workload, customer notified and able to opt out). The common failure is registration, co-sell, and marketplace records living in disconnected systems reconciled manually.

## Documented failure modes

| Failure                       | Mechanism                                                                             | Fix                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Squatting / hoarding          | Partner registers deals it isn't working, blocking others for months                  | Default expiry plus an activity-based extension test                                                                          |
| Portal-CRM disconnect         | Registration approved for an account already a customer or in active direct pipeline  | Auto-check the domain against the CRM at submission; auto-reject with the reason                                              |
| Direct-team overrides         | Direct routinely overrides approved registrations                                     | Registration rates collapse and word spreads; executive commitment to honoring registrations is the fix and is non-negotiable |
| Onboarding gap                | New partners submit ineligible deals, get rejected, disengage                         | Teach eligibility at onboarding; show rejection-reason stats back to partners                                                 |
| Form friction                 | Long forms suppress submission                                                        | Only decision-relevant fields                                                                                                 |
| Bespoke process per edge case | Multi-partner deals, regional handoffs, services-only plays each get special handling | One process; multiple roles allowed on one opportunity; credit split by documented contribution                               |

## Honest caveat

There is no rigorous public evidence that deal registration reduces _total_ conflict. It is simultaneously the most-recommended and most-criticized instrument in the field.

The criticism (squatting, margin-erosion edge cases, administrative burden) is as well documented as the advocacy, and both rest on practitioner consensus and vendor content rather than independent measurement. Treat it as the standard claim-adjudication instrument, not a proven conflict-reduction device.
