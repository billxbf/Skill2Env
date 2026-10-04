# Jurisdiction & Compliance Overlay

The core skeleton is universal: definitions, licence, commission and tracking, prohibited tactics, clawback, termination read the same everywhere. What follows is the jurisdiction-specific layer, applied per the interview's geography answers. Regulations change and penalty figures are inflation-adjusted - treat every figure as an "as-of drafting" baseline the user must re-verify, and say so in the delivered draft.

## United States

- **FTC Endorsement Guides, 16 CFR Part 255 (revised 2023).** Disclosures of material connections must be "clear and conspicuous" - difficult to miss, easily understandable, unavoidable in interactive media. Interpretive guidance, no independent civil penalty, but it defines the disclosure obligation the terms must impose on every affiliate. The advertiser is responsible for its affiliates' disclosures, so write in an audit/takedown right.
- **FTC Reviews Rule, 16 CFR Part 465 (effective October 2024).** Binding and penalty-bearing (civil penalties in the low-$50k range per violation, inflation-adjusted). Bans fake/AI-generated reviews, incentivized-sentiment reviews, undisclosed insider reviews, review suppression, fake social-influence indicators. Directly reaches affiliates who publish reviews - mirror these bans in the prohibited-tactics list.
- **Affiliate-nexus ("Amazon law") history.** State click-through-nexus statutes once forced merchants to terminate affiliates by state; _South Dakota v. Wayfair_ (2018) largely mooted the rationale, but affiliate nexus remains on the books in some states. A state-based eligibility restriction is now rarely needed - flag for counsel only if the user raises sales-tax concerns.
- **Escheatment.** Unpaid commissions can be reportable to the state as unclaimed property after a 1–5 year dormancy period - the legal limit on forfeiture clauses. `[LEGAL REVIEW]`

## European Union - Platform-to-Business Regulation (EU) 2019/1150

Applies to online intermediation services connecting business users to EU consumers, regardless of where the provider sits. Affiliate networks are the strong case; whether a merchant's in-house program qualifies is a counsel question - mark it `[LEGAL REVIEW]` rather than assuming either way.

Two Art. 2(2) limbs decide it, and Recital 11 excludes advertising tools that meet neither: the service must be **provided with the aim of facilitating direct transactions between business users and consumers**, and there must be a **contractual relationship with consumers**. A program where the affiliate merely places links and the purchase happens on the merchant's own site looks like the excluded advertising tool; a platform that hosts ranked offers and is where the consumer initiates the purchase looks covered. A B2B-only program - business users selling to businesses, not consumers - falls outside the scope threshold regardless.

When it applies, terms toward EU/UK business users must have:

- Plain and intelligible language, easily available at all stages including pre-contract.
- Amendments: at least 15 days' notice on a durable medium, never retroactive, with a right to terminate instead of accepting.
- Grounds for restriction, suspension, and termination stated in the terms themselves.
- Termination: at least 30 days' notice plus a statement of reasons.
- For non-small providers: an internal complaint-handling system and at least two designated mediators.

Terms breaching these requirements are null and void. The UK retains a mirror P2B regime post-Brexit. No US equivalent exists - this is the sharpest jurisdictional divergence in the genre.

## United Kingdom

- **ASA/CAP Code.** Marketing communications must be "obviously identifiable" as ads; affiliate marketing falls within the ASA's remit. Ambiguous labels - "affiliate", "gifted", "spon" - are insufficient; "Ad" is the preferred label. Write the labeling obligation into the disclosure clause for UK-facing affiliates.
- **CMA / DMCC Act 2024.** The competition regulator now holds direct consumer-protection enforcement powers with fines up to 10% of global turnover - undisclosed advertising and fake reviews are enforcement priorities.

## GDPR / privacy roles (genuinely contested)

- Consensus: the advertiser is always a data controller.
- Disputed: the network/affiliate role.
  - One major network publicly takes a tripartite joint-controller position.
  - Another positions itself as an independent controller.
  - SaaS tracking vendors position as processors.

  There is no settled answer - pick a position deliberately, document it in the DPA, and mark it `[LEGAL REVIEW]`.

- Independent of role allocation, ePrivacy/GDPR require cookie consent before a tracking cookie is set - the terms should oblige affiliates to honor consent requirements on their own properties.
- US state privacy laws (CCPA/CPRA and successors) add opt-out and service-provider contract requirements when California consumers are in scope.

## What is universal vs jurisdiction-specific

Nothing in this overlay is a menu. Every obligation below is a gate for the geographies the interview surfaced - drafted, or the document is not deliverable - so none of it is ranked, traded against effort, or dropped because a cheaper option exists. The table classifies obligations by where they apply, not by which to do first.

| Universal                                                                                      | Jurisdiction-specific                                                               |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Definitions, licence, commission/tracking, prohibited tactics, clawback, termination structure | Amendment and termination notice periods + statement of reasons (EU/UK P2B)         |
| Disclosure obligation existing at all                                                          | Exact disclosure standard and label (FTC "clear and conspicuous" vs ASA "Ad")       |
| Data-protection clause existing at all                                                         | Role allocation, DPA contents, consent mechanics                                    |
| Enforcement ladder                                                                             | Penalty exposure backing the review/fake-content bans (FTC Reviews Rule, CMA fines) |
