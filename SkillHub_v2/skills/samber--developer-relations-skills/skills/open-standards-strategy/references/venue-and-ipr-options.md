# Venue and IPR options

Contents: [Choosing quickly](#choosing-quickly) · [Git-based community specification](#git-based-community-specification) · [Foundation-hosted consortium](#foundation-hosted-consortium) · [OASIS-style consortium](#oasis-style-consortium) · [IETF](#ietf) · [W3C](#w3c) · [ISO transposition](#iso-transposition) · [Patent regimes](#patent-regimes-in-one-page) · [Questions to ask a venue](#questions-to-ask-a-venue-before-joining)

## Choosing quickly

| Need                                                           | Venue                                                                  |
| -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Ship a spec in weeks, keep control, add legal hygiene          | Git-based community specification                                      |
| Prove neutrality fast, several companies co-founding           | Foundation-hosted consortium (e.g. Joint Development Foundation-style) |
| Enterprise data formats, members expect formal process         | OASIS-style consortium                                                 |
| Wire protocols, open participation, engineering culture        | IETF                                                                   |
| Web-platform surface, browsers must implement                  | W3C                                                                    |
| A tender, regulator or public buyer requires a standard number | ISO transposition of an existing de facto standard                     |

Speed and control decrease down the table; credible neutrality increases. This is a lookup by need, not a ranking - the efficiency, neutrality, effort and compliance-cost orderings live in the skill's Step 4, where the venue is actually chosen.

## Git-based community specification

Runs specification development in a repository with the legal layer attached:

- contributor licence
- specification licence
- scope
- governance
- contributing guide
- code of conduct
- spec template

The Community Specification 1.0 is the widely used instance of this pattern, developed through the Joint Development Foundation and drawing on the Open Web Foundation agreements and the Alliance for Open Media Patent License 1.0.

Specification licences are deliberately not open-source licences: a spec is "a blueprint developers implement in different ways in many different codebases", so the licence covers implementations of the whole specification rather than one codebase.

- **Cost**: near zero, plus your own maintainer time.
- **Buys**: velocity, a normal pull-request workflow, contributors who already know Git.
- **Does not buy**: neutrality - the repository owner still looks like the owner.

## Foundation-hosted consortium

A neutral host supplies incorporation, policies and IP options so a group of companies can start without negotiating a consortium from scratch. The Joint Development Foundation describes itself as offering "rapid-start, out-of-the box materials to create custom-branded non-profit technology consortia".

- **Offers**: an existing 501(c)(6) structure, no cost to start a project, optional services (accounting, certification, events, legal), and a route to advance the work into a larger standards organization later.
- **Buys**: neutrality with far less process weight than a formal standards body, and a defined escalation path.
- **Costs**: shared governance from day one; you can no longer change the spec unilaterally.

## OASIS-style consortium

Membership-based technical committees, with the patent regime fixed by the charter. OASIS offers four IPR modes:

- RAND
- RF on RAND Terms
- RF on Limited Terms
- Non-Assertion (a covenant not to assert)

The mode is effectively permanent - "a TC may not change its IPR Mode without closing and submitting a new charter". Patent obligations attach after presence thresholds (60 calendar days of participation, plus remaining active through approval ballots).

Practical consequence: pick the IPR mode as a strategic decision at charter time, not as a legal formality at the end.

## IETF

- **Participation**: open and individual. "IETF participation is voluntary and there is no top-down plan that requires any particular topic to be worked on or idea to be adopted." No membership fee; people participate, not companies.
- **Path**: Internet-Draft → working-group adoption call (about two weeks) → Working Group Last Call → IETF Last Call → IESG approval → RFC publication.
- **Decisions**: rough consensus, not votes. RFC 7282 records Dave Clark's formulation - "We reject: kings, presidents and voting. We believe in: rough consensus and running code" - and the working question "Can anyone not live with choice A?". A chair may declare rough consensus over a standing objection once that objection has been genuinely considered and answered.
- **IPR**: BCP 78 (RFC 5378) for contribution rights, BCP 79 (RFC 8179) for patent disclosure. Disclosure is mandatory; licensing terms are declared rather than dictated.
- **Implication**: influence comes from writing drafts and showing running code, not from company size or membership tier.

## W3C

- **Recommendation Track**: Working Draft → Candidate Recommendation ("ready for implementation experience") → Proposed Recommendation (Advisory Committee review) → Recommendation. Advancement requires evidence the specification "can be implemented interoperably".
- **Chartering**: charter refinement with wide review (minimum 28 days, up to six months), then Advisory Committee review (minimum 28 days, extendable to 60). Budget months before technical work starts.
- **Patent Policy**: royalty-free by design - specifications "can be implemented on a Royalty-Free (RF) basis", with licences "available to all, worldwide", not "conditioned on payment of royalties, fees or other consideration".
- **Essential Claims**: those that "would necessarily be infringed by implementation" where "there is no non-infringing alternative"; design patents, enabling technologies and non-normative implementation details are excluded.
- **Exclusion windows**: 150 days after the First Public Working Draft, 60 days after a Patent Review Draft for newly essential claims, 60 days after resigning from the Working Group. Miss the window and the royalty-free commitment binds.

## ISO transposition

ISO/IEC JTC 1 maintains a procedure for taking de facto standards "through the formal standardization system to be transformed into international standards". PDF is the reference run: an Adobe format, spread by free readers, then published as ISO 19005-1:2005 (PDF/A) and ISO 32000-1:2008.

Use it when a buyer, regulator or public tender needs an international standard number. It does not create adoption, and the process is the slowest of any venue here.

## Patent regimes in one page

- **Royalty-free (RF)**: participants licence Essential Claims at no cost. Required by W3C, available as several OASIS modes. Maximizes the implementer pool, including open-source projects.
- **Non-assertion covenant**: no licence granted, but a public promise not to sue implementers. Lighter to administer, weaker for implementers who need an explicit grant.
- **RAND / FRAND**: licensing on reasonable and non-discriminatory terms, potentially with royalties. Common in telecom and hardware. Most open-source projects cannot implement a royalty-bearing standard, so this caps grassroots adoption - a legitimate choice when your implementers are funded vendors, a strategic error when your plan assumed community uptake.
- **Conformance-gated licences**: some programmes grant the patent licence only to implementations that pass conformance testing, which turns the test suite into the IP gate as well as the quality gate.

Never join an RF venue expecting to keep monetizable claims out through exclusion windows: exclusions are narrow, dated and public.

## Questions to ask a venue before joining

1. What is the IPR mode, and can it change without re-chartering?
2. What did this group actually publish in the last two years, and how long did each document take?
3. Which companies do the active participants work for, and does one affiliation dominate?
4. Who owns the trademark and the conformance mark?
5. What does membership cost, in fees and in hours per month?
6. Who arbitrates when consensus fails, and what has that produced before?
