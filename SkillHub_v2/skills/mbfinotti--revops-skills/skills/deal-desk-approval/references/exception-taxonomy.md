# Exception Taxonomy

Group exceptions by what triggers them [practitioner - Umbrex playbook synthesis]. Route each type to the function that owns its risk: the matrix decides how high, the taxonomy decides who.

1. Economic thresholds: discount beyond band, non-standard payment terms, free services above a cap, deal value above a band. Easiest to automate.
2. Structural complexity: multi-year ramps, usage commitments and true-ups, cross-product bundles, price holds, unusual termination rights.
3. Risk and precedent: contract-standard deviations, security/privacy changes, roadmap commitments.

## Type-by-type: owner and escalation trigger

**Non-standard payment terms** (net-60/90, monthly billing on annual contract, deferred start)

- Treat it as a concession even when presented as an administrative request; translate it into an equivalent price concession so approvers can compare.
- Required trade: smaller discount, longer term, partial upfront, or a security mechanism.
- Owner: Finance.
- Non-delegable escalation to Finance leadership for extremely long terms, multi-year deferrals, and "pay when paid" clauses in channel deals - these shift the vendor toward being a lender [practitioner].

**Multi-year ramps**

- Ranking: entitlement ramp > discount ramp on value and effort together, so no split axis is needed - more units over time is easier to invoice and enforce, while a price that steps up later carries the risk of the step never landing.
- Control: anchor renewal pricing to the last contract period's price so early ramp concessions cannot reset the future.
- Owner: Finance/Pricing.
- Escalate when renewal uplift falls below the corridor [practitioner].

**Custom SLAs and service credits**

- Changes both operating cost and downside exposure.
- Stays non-escalated only if credits are capped at the standard tier, the SLA matches real operational capability, and credits are the exclusive remedy.
- Owner: Security/Ops validates feasibility.
- Escalate to leadership on uncapped credits, penalties beyond credits, or an SLA beyond capability [practitioner].

**MSA/legal redlines** (liability cap, indemnity, IP, data residency, auto-renewal removal)

- Ranking: fallback library > per-deal counsel review. A one-off week of Legal's time on 15-25 pre-approved positions [illustrative] moves most redlines off counsel's desk permanently, and it is the only one of the two that gets cheaper every quarter.
- Maintain the library so an analyst, not a lawyer, handles redlines within it; only novel terms reach counsel.
- Three-track pattern [illustrative single-source; the concept is corroborated, the exact SLA hours are not]. The tracks rank A > B > C on redlines cleared per hour of legal time, a routing goal (push volume toward A) rather than a per-deal choice:
  - Track A: standard paper signed as-is, zero review.
  - Track B: redlines against the fallback library, analyst-handled on a short SLA.
  - Track C: novel/regulated terms to counsel on a longer SLA.
- Liability-cap removal or uncapped consequential damages outside pre-approved carve-outs is prohibited-class, not an exception.
- Owner: Legal for any deviation from the library.

**Security and privacy commitments** (audit rights, custom data-processing terms, residency, incident timelines, compliance attestations)

- Triage: Standard (library answer exists) / Clarify (needs input) / Exception (genuinely new commitment).
- Escalation triggers: customer-defined incident timelines, dedicated environments, unique audit support, custom logging.
- Owner: Security for feasibility.
- Owner: Privacy for residency/sub-processor/transfer asks.
- Owner: Legal only when new operational obligations are created [practitioner].

**MFN, best-price guarantees, open-ended price holds**

- Prohibited-class (see the matrix reference); listed here because reps will submit them as ordinary exceptions.
- Owner: Legal + commercial lead jointly, give-get mandatory even to discuss [practitioner].

**Roadmap/product commitments**

- Prohibited by default.
- An exception path opens only after Product and Delivery pre-approve feasibility.
- Legal caps any attached penalty structure [practitioner].

**Termination for convenience**

- Owner: Legal, with mandatory Finance input; the accounting consequence (contract term shrinking to the notice period absent a substantive penalty) is usually bigger than the legal one. See the accounting reference.
- Common negotiated fallback: allow it only with full upfront payment and no clawback right [practitioner].

**Free periods, pilots, POCs**

- Time-box; beyond roughly 90 days prefer a paid pilot [illustrative].
- Controls:
  - State "at no charge" explicitly (prevents an implied-payment claim).
  - Settle foreground-IP ownership up front.
  - Finance signs off the ARR/revenue treatment of the eventual conversion.
- Owner: Legal (terms/IP) + Finance (fee/ARR) + Product (scope), a default split to confirm with the user, not a standard RACI.

**Reseller/channel/MSP pricing**

- No published framework governs channel deal-desk approval the way discount-threshold matrices are documented for direct deals; decide the actual thresholds as house policy with the user, not adapted best practice.
- Vendor partner-program policies (AWS Partner Network, Microsoft Partner Center/CSP, Google Cloud Marketplace, Salesforce AppExchange) solve a different problem: they govern the wholesale discount or margin the vendor extends to the partner, not case-by-case approval of what the partner charges the end customer. Do not import their tier structures as a deal-desk approval matrix [practitioner].
- GitLab's public Deal Desk Handbook documents the one concretely differentiated practice available: separate quote templates per channel type (Authorized Reseller, MSP, and Distributor Order Forms versus the Standard Order Form), and an intake routing decision - "route to market: direct, channel, marketplace" - that sends channel and marketplace deals to Partner Territory Managers or Partner Account Managers instead of the standard deal-desk analyst lane [practitioner].
- Deal registration - a partner submitting a lead or opportunity for protected pricing and margin before working it - is the channel-specific intake gate with no analog in the direct motion. CompTIA's recurring State of the Channel research documents deal registration and its rules of engagement as a recurring source of partner friction [practitioner].
- The one documented escalation datum is that "pay when paid" channel clauses escalate non-delegably to Finance leadership.
- If the user has a channel motion, design the actual thresholds explicitly with them and label the result as house policy.

## Routing summary

| Exception type               | Owner                                   | Non-delegable escalation                                          |
| ---------------------------- | --------------------------------------- | ----------------------------------------------------------------- |
| Payment terms / billing      | Finance                                 | Multi-year deferrals, pay-when-paid                               |
| Ramps / renewal constructs   | Finance/Pricing                         | Renewal uplift below corridor                                     |
| Custom SLA / credits         | Security/Ops                            | Uncapped credits, penalties beyond credits                        |
| Legal redlines               | Legal (analyst inside fallback library) | Novel terms, regulated asks                                       |
| Security/privacy             | Security, Privacy                       | New operational obligations -> Legal                              |
| MFN / price holds            | Legal + commercial lead                 | Always (prohibited-class)                                         |
| Roadmap commitments          | Product + Delivery                      | Always (prohibited by default)                                    |
| Termination for convenience  | Legal + Finance                         | Penalty-free walk-away rights                                     |
| Free periods / POCs          | Legal + Finance + Product               | Unbounded duration, unowned IP                                    |
| Reseller/channel/MSP pricing | Partner management (routing) + Finance  | Pay-when-paid clauses; always routes off the standard three lanes |
