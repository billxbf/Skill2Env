# Worked Examples

Real published agreements decomposed by section, one worked output outline, and one negative example. Vendor names appear here only as sourced structural examples - never as required tools.

## Real published agreements, decomposed

- **Shopify Partner Program Agreement** (B2B SaaS - shopify.com/partners/terms)
  - Part A applies to all partners: Definitions, Partner Responsibilities (including a duty to disclose), Fees and Payments, Termination, IP Rights, Confidentiality, Warranty Disclaimer, Liability/Indemnification, General.
  - Part B is referral/affiliate-specific: FTC Guidelines, Revenue Sharing, Responsibilities, Prohibited Activities.
  - Lesson: layer a universal part plus a role-specific part when one program covers several partner types.
- **HubSpot Affiliate Program Agreement** (B2B SaaS - legal.hubspot.com/affiliate-program-agreement)
  - Clause order: Definitions, Non-Exclusivity, Affiliate Acceptance, Customer Transactions, Trademarks, Proprietary Rights, Confidentiality, Term and Termination, Reps and Warranties, Indemnification, Disclaimers/Limitations, General.
  - Its amendment clause notifies by electronic means and offers termination to affiliates who reject an update.
  - Lesson: notice + exit is the model amendment mechanism.
- **Amazon Associates Operating Agreement** (B2C ecommerce - affiliate-program.amazon.com)
  - A master agreement plus incorporated Program Policies, Participation Requirements, and IP License, with per-jurisdiction schedules.
  - It mandates an exact disclosure phrase and deems any policy violation a material breach.
  - Lesson: incorporation by reference lets operational policies update without amending the master; jurisdiction schedules localize governing law and tax.
- **Awin Publisher Terms** (network - awin.com/us/publisher-terms)
  - The network's master publisher terms govern; each advertiser's Program Terms sit on top and may change on short notice.
  - Data-protection annexes per regime; a separate publisher Code of Conduct adds a governance layer.
  - Lesson: in a network-hosted program, draft only the program layer - the master terms are not yours to write.

## Worked output outline

B2B SaaS, in-house program, US + EU affiliates, recurring commission decided elsewhere:

```
AFFILIATE PROGRAM TERMS - <Company> (DRAFT FOR LEGAL REVIEW - NOT LEGAL ADVICE)
1.  Definitions (Affiliate, Customer Transaction, Net Collected Revenue, Commission, Link)
2.  Eligibility & Approval - manual review; tax forms; one account; content standards
3.  Brand Licence - approved creatives only; auto-revoked on termination; 5-day destruction
4.  Commission & Payment - cites the decided structure: rate, 12-month recurring window,
    $X threshold; paid on net collected revenue
5.  Tracking & Attribution - last-click; 30-day cookie; company data authoritative
6.  Prohibited Tactics - enumerated list per program decisions; enforcement ladder
    [LEGAL REVIEW: trademark-bidding ban - contractual enforceability]
7.  Disclosure - clear and conspicuous per FTC; "Ad" label for UK-facing content
8.  IP & Confidentiality - survives 3 years
9.  Data Protection - DPA incorporated [LEGAL REVIEW: controller/processor allocation]
10. Reps & Warranties  11. Indemnity  12. Limitation of Liability [LEGAL REVIEW: cap]
13. Term & Termination - 30-day convenience; immediate for cause;
    EU affiliates: statement of reasons [LEGAL REVIEW: P2B applicability to in-house program]
14. Pending Commissions at Termination - non-fraud: paid as accrued; fraud: forfeited
    [LEGAL REVIEW: forfeiture scope vs escheatment]
15. Clawback & Reversal - 60-day validation; reversal grounds: fraud, refund, chargeback, churn <30 days
16. Amendment - email notice; 15 days for EU affiliates; continued participation = acceptance
17. Assignment  18. Governing Law & Disputes [LEGAL REVIEW: arbitration]  19. Tax & Contractor Status
DELIVERY NOTE: draft for qualified counsel - retain every [LEGAL REVIEW] marker until cleared.
```

## Negative example - do not draft this

> "Company may terminate any Affiliate at any time for any reason. Upon termination, all commissions, whether pending or earned, are forfeited. Company may modify these Terms at any time without notice. Affiliates shall not engage in any unethical or inappropriate marketing practices."

Why every sentence fails:

- Blanket forfeiture of earned commissions is legally contested, collides with escheatment law, and invites disputes on every termination - no fraud/non-fraud split.
- No-notice unilateral amendment is null and void toward EU/UK business users under P2B, and destroys trust everywhere else.
- "Unethical or inappropriate" prohibits nothing under the enumerate-or-permit principle - no listed tactics, no enforcement ladder, no material-breach hook for for-cause termination.
- Termination "for any reason" with no notice period fails the P2B 30-day/statement-of-reasons requirement for EU/UK business users.
- Nothing revokes the brand licence or addresses assets, so an ex-affiliate can keep running ads with the company's marks.
