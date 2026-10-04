# Accounting and Legal Constraints

These are design constraints for the approval spec - reasons certain structures must route to Finance or Legal before any tier can approve. They are not legal or accounting advice; the spec's job is to route the question to the right function, never to answer it.

## Revenue recognition (ASC 606 / IFRS 15)

**Discount allocation across performance obligations**

- A discount on a bundle (subscription + implementation + services) is allocated proportionately across all performance obligations by relative standalone selling price, not to whichever line item the negotiation focused on.
- Sales' internal logic ("we discounted the services, not the license") is accounting-irrelevant unless the specific-allocation criteria are met with observable evidence: observable standalone prices, an observable bundle price, and a discount matching what the allocation would produce (ASC 606-10-32-37).
- Design consequence: any deal that steers a discount onto one line item routes to Finance. The quote's line-item story does not control the books. [Big-Four-documented standard mechanics]

**Material right**

- A customer-specific future discount promised today, e.g. a steep renewal discount not offered to others granted to win the initial deal, can be a material right: a separate performance obligation forcing part of today's revenue to be deferred until the option is exercised or expires.
- Design consequence: future-discount promises and customer-specific renewal locks route to Finance at any size. [standard mechanics, vendor-explainer sourced]

**Termination for convenience and contract term**

- If a customer can terminate at will with no substantive penalty, the enforceable contract term for revenue purposes is the notice period, not the stated multi-year term, even though the paper says "3 years". A substantive termination charge preserves the full term.
- Confirmed by the standard-setters' transition group for government contracts; the mechanic generalizes.
- Design consequence: any change to termination rights routes to Legal and Finance together. A "harmless" legal concession can silently change how much revenue exists. [practitioner-accounting sourced]

**Significant financing component**

- When payment timing diverges materially from delivery (multi-year prepay, long deferrals), a financing component may need to be recognized.
- Practical expedient: gaps under one year are exempt, which is why standard annual billing is fine and multi-year prepaid or deferred-payment structures need Finance scrutiny.
- Design consequence: payment-timing exceptions beyond one year route to Finance leadership. [practitioner-accounting sourced]

**Variable consideration boundary**

- A discount fixed at contract inception is not variable consideration; only amounts contingent on future events (rebates, refunds, performance credits, penalties) are.
- Useful for keeping ordinary negotiated discounts out of a more complex accounting path, but the classification call belongs to Finance. [practitioner-accounting sourced]

### Routing table

| Structure                                         | Routes to          | Why                                              |
| ------------------------------------------------- | ------------------ | ------------------------------------------------ |
| Discount steered to one line item of a bundle     | Finance            | Relative-SSP allocation controls, not the quote  |
| Customer-specific future/renewal discount promise | Finance            | Possible material right; revenue deferral        |
| Termination-for-convenience change                | Legal + Finance    | Contract term may shrink to notice period        |
| Multi-year prepay or extended payment tail        | Finance leadership | Significant financing component; credit risk     |
| Acceptance-based or deferred invoicing            | Finance            | Only sound with objective, time-bounded criteria |
| Rebates, credits, performance penalties           | Finance            | Variable consideration estimation                |

## Pricing-discrimination law: the load-bearing negative finding

- US - Robinson-Patman Act: on the enforcement agency's own framing, the Act applies to commodities, not services, and to purchases, not leases. SaaS is a service/intangible, so Robinson-Patman does not reach ordinary SaaS differential pricing at all. Even where it applies (tangible goods), it demands competitive injury among actual competitors and is notoriously hard to enforce. [agency guidance, corroborated by legal commentary]
- EU/UK - Article 102 TFEU and Chapter II of the UK Competition Act 1998: discriminatory-pricing prohibitions exist but are dominance-gated - they only bind firms already found dominant in a relevant market. A non-dominant vendor's differential discounting falls outside their scope by definition. [legal-commentary synthesis]
- Plain statement for the spec: for a typical, non-dominant B2B SaaS vendor, neither the US nor the EU/UK regime meaningfully constrains charging different customers different prices through a deal desk. Do not manufacture this compliance risk or build approval friction around it.
- Residual caveats, stated once:
  - General antitrust theories (e.g. US Sherman Act / FTC Act, or abuse rules if the vendor is dominant) can still reach genuinely anticompetitive pricing conduct.
  - Sector rules and public-sector procurement have their own regimes.
  - Contractual MFN clauses the vendor itself signed are a self-inflicted constraint (which is one reason they sit in the prohibited class).

  Route any actual legal question to counsel.
