# Governance and quality-bar case studies

## The Platform Revolution framework

_Platform Revolution_ (Parker, Van Alstyne, Choudary, 2016) defines platform governance as "the set of rules concerning who gets to participate in an ecosystem, how to divide the value, and how to resolve conflicts." An operating model that leaves any of the three unanswered is incomplete by definition - admission criteria, value split, and dispute/removal process each need a written answer with an owner.

Their curation argument: trust is central to any marketplace with interaction risk, and it is built by curating participants until both sides are comfortable with the residual risk of engaging. Curation is not a one-time gate - the book notes platforms tend to grow more open over time, which requires continually re-adjusting curation criteria rather than setting them once at launch.

Their four named causes of platform market failure (good interactions failing to occur, or bad ones occurring) are the diagnostic checklist for why governance rules exist at all:

1. **Information asymmetry** - one side knows something material the other cannot see (their example: a seller who knows goods are fake and doesn't disclose it).
2. **Externalities** - an interaction imposes costs on parties outside it.
3. **Monopoly power** - one participant, or the platform itself, extracts beyond its contribution.
4. **Risk** - the residual chance of a bad outcome that deters good interactions.

Walk each of the four against your marketplace design; every governance rule you write should trace back to at least one of them.

## Two quality-bar architectures

**Ladder - HubSpot's listed/certified two-tier model.**

- Any app meeting minimal requirements gets "listed."
- A separate, harder "Certified" tier layers on quantitative gates (2026: a security questionnaire, 95% API success rate, sustained maintenance evidence, a minimum review-quality threshold), reviewed by a dedicated Ecosystem Quality team on a 2-4 week cycle.

Losing certified status keeps the app listed, just without the badge - decoupling "allowed to exist" from "endorsed by the marketplace." The ladder lets a marketplace stay open to low-risk apps while still signaling trust for the subset that clears a higher bar.

**Single gate - Zoom's four-stage review pipeline.**

1. Submission-completeness check.
2. Compliance review (data handling against Zoom's own privacy/security requirements).
3. Security review (OWASP Top 10 testing, OAuth-scope minimization - unused or excessive scopes get flagged for removal).
4. Post-approval ongoing monitoring with removal authority.

Review duration scales with app quality and scope clarity, which itself incentivizes developers to submit minimal, well-documented scope requests.

Choose the gate when every listing carries real data-access risk. Choose the ladder when most listings are low-risk and the trust signal only needs to cover a subset.

## Enforcement precedents

- **Delisting as the compliance lever (Salesforce, 2026):** mandatory new security controls for Connected Apps from May 2026, with non-compliant apps delisted. A mature marketplace enforces retroactive requirements through removal, not persuasion.
- **Delisting as the anti-circumvention lever (Shopify):** apps that routed billing through Stripe directly to dodge revenue share violated the terms. Several high-revenue apps reversed course under delisting threat. "Pay through us" is a governance rule enforced by removal, not a pricing preference.
- **Post-approval monitoring (Zoom):** approval is not permanent. Ongoing monitoring with removal authority is the mechanism that keeps the admission gate meaningful after day one.

## The openness counter-argument

A U.S. NTIA analysis of the mobile app ecosystem argued heavy gatekeeping produces "prices inflated due to fees collected by gatekeepers, innovation hampered by policy decisions to limit access... and loss of choice" - the standard antitrust argument against curation-as-control. Treat it as the live counterweight when setting the curation position: every notch toward the curated end buys trust and costs supply, fee tolerance, and (at platform scale) regulatory attention.

## Discoverability is a separate governance surface

Admission (who gets listed) and discoverability (who gets seen first) are independent axes - a marketplace can be open on the first and still gate or monetize the second.

- **Paid/featured placement** (homepage, search results, email campaigns) is a second revenue line distinct from take-rate - and it needs its own disclosure rule. Featured placement that reads as an editorial pick erodes exactly the trust curation was meant to build.
- **Review-driven organic ranking** is the counterweight: HubSpot explicitly cites its user review system as the mechanism that "helps ensure listed apps are of high quality and meet user needs."
- **Heavier structures exist above the review gate:** some enterprise marketplaces gate listing itself behind a formal partnership agreement layered on top of technical/security review. Cloud marketplaces add multi-tier reseller/distributor structures with downstream storefronts. Relevant only if the marketplace expects resellers, not just direct app builders.

## Partner concentration and pooled scale

Once complementors scale, a few can gain outsized bargaining power over the platform. The documented countermeasure is the platform actively "pooling scale" for complementors - shared analytics, shared advertising infrastructure - so smaller partners get scale benefits without individually reaching that scale, keeping the complementor base level rather than letting a few dominate. Write this into the governance section as a standing mechanism, not a crisis response.
