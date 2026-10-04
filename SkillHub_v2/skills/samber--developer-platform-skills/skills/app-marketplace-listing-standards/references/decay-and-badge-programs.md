# Decay enforcement and badge programs across the benchmarks

Same sourcing rule as the field benchmarks: operator-published documentation unless labeled otherwise. Two source conflicts are carried below as-is, per the label on each - do not silently resolve either.

## Decay-enforcement inventory

No shared industry term or standard for listing decay exists; each operator handles staleness through a different mechanism:

- **Policy-as-violation** - Chrome and Google Workspace both classify "out of date" metadata (description, category, developer name, title, icon, screenshots, promo images) as a rejectable/removable policy violation outright. Google additionally re-reviews its most popular apps on a recurring basis.
- **Staleness downgrade** - Atlassian marks an app whose categorization goes stale post-launch as "uncategorized", removing it from every category browse/filter surface: soft, self-correcting (fixable any time by updating the listing), no delisting fight.
- **Substantial-change trigger** - Slack names "a listing not updated to reflect substantial changes" to the app as a rejection/removal risk. Note the trigger is subjective ("substantial"), which is exactly the trap the skill's field-spec menu warns about - if you adopt this shape, define "substantial" objectively.
- **Version-currency enforcement** - HubSpot is the most systematic mechanism surveyed:
  - The platform ships a new developer-platform/API version every six months (March/September).
  - New apps built on unsupported versions are rejected outright.
  - Existing apps must be on a supported version at certification or recertification time, with roughly 60 days to migrate.
  - Deprecated components (classic CRM cards, deprecated 2025-06-16) make an app unlistable.

  The platform's own release cadence does the freshness-detection work.

- **Fee-as-renewal** - Salesforce charges paid apps a $150 annual listing fee (Partner Community FAQ): an ongoing-cost nudge, not a content-freshness gate; no published content-update cadence is tied to delisting. This is why the skill deletes fees from the decay menu - nothing about a fee checks content.
- **Discretionary monitoring** - Zoom monitors published apps for continued compliance and may remove or require revisions, with no published calendar trigger; developers must maintain ongoing support surfaces (terms, privacy policy, self-serve docs, support URL).

**Adjacent-ecosystem hard cadences** - the only explicit numeric auto-removal rules found live outside the eight-marketplace benchmark set, in the neighboring e-commerce/enterprise marketplace ecosystem; label them as adjacent when citing:

- Adobe Commerce Marketplace ("Abandoned listings" policy, verbatim):
  - The app or extension must be updated at least once every year.
  - A monthly automated checker collects everything not updated for 11 months or more.
  - At 12 months without an update, after automated notification, the listing is removed.
- Microsoft's commercial marketplace (AppSource documentation): publishers must keep listings updated across the lifecycle, with a staged deprecation/removal timeline running from T+1 to T+150 after a listing is flagged.

Use Adobe's 12-month rule as an internal worst-case freshness SLA even where nothing external forces one.

**Resolved, not a live conflict**: the $2,550 one-time Security Review fee is the pre-March-2023 model (paired with a $150 annual fee); Salesforce replaced it in March 2023 with the current $999-per-attempt fee, charged on the initial submission and on every resubmission after a failed review. Cite $999 as current; treat $2,550 as historical only. (The fee itself belongs to the review/monetization siblings' scope - it is recorded here only because the listing-fee source carried the now-resolved conflict.)

## Badge programs and their display rules

Badge eligibility mechanics belong to the review process; what follows is the display-relevant detail per operator:

- **Atlassian - the dedicated trust surface**: the Trust & Security tab is physically separate from the marketing description; it must state data-storage location, display relevant earned badges (Cloud Fortified, Bug Bounty participation), and list compliance certifications. The clearest surveyed example of splitting persuasive content from trust content.
- **Google Workspace - two badges, and the brand rulebook**:
  - An independent security-verification badge earned via CASA assessment, displayed on the marketplace homepage, in search results, and to admins in the admin console; mandatory for "Recommended" status. **Resolved**: "Tier 3" and "Assurance Level 2 (AL2)" name the same CASA requirement - Google's own get-featured page uses AL2 in its current English version and "Tier 3" in other cached/localized versions of the identical page (French, German). Cite AL2 as the current name; "Tier 3" is the same tier under its older name, not a different requirement.
  - A developer-embeddable promotional badge governed by the most detailed brand-usage spec surveyed (create-badge page, last updated 2026-07-22):
    - Use as provided and never alter.
    - Clear space equal to one-quarter of badge height.
    - Equal to or larger than any other app-store badge alongside it.
    - Any online use links back to the listing.
    - Caption must read "from" the marketplace, never "on" it.
- **HubSpot - renewal-linked certification**: App Certification is reviewed against seven quality categories (security, privacy, reliability, performance, usability, accessibility, value).
  - Requires ≥6 months listed and ≥60 active unique installs over a trailing six-month window (floor raised from 6 to 60 effective 2024-05-15).
  - Falling below removes certified status (app stays listed, uncertified) with a six-month wait before re-applying.
  - Certification renews on a rolling two-year cycle.

  The most systematic recertification mechanism surveyed, and the model for wiring badge display to lapsable eligibility data.

- **Salesforce - self-service badges**:
  - Lightning Ready, via a self-attested checkbox in the publishing console.
  - 100% Native, via a support case.

  Lightweight to run, and the trust they carry is correspondingly self-attested.

- **Zoom - no badge program, by architecture**: no software-app trust/certified badge exists on the marketplace at all; "Zoom Certified" applies only to hardware, run as a separate program. A genuine design choice, not a documentation gap - present "no badge program" as a legitimate option.
- **Chrome - identity, not quality**: a linked "Official URL" renders under the listing title only for publishers who verify site ownership - an identity-verification display distinct from any quality/security badge; worth offering because it costs the operator almost nothing.

## The external-certification gap

No ISO standard, IAB standard, or independent certification body exists for B2B SaaS marketplace listing quality. Only two substitute classes exist:

- Operator-proprietary programs (the badges above, none portable across marketplaces).
- General security/quality-management standards (SOC 2, ISO/IEC 27001, ISO 9001, CASA/ASVS, FedRAMP) that certify an organization's posture, never a listing page's content.

Practical consequence: an operator claiming its listings are "certified to an industry listing standard" is making an unverifiable claim. The honest positioning is compositional, named as its own:

- WCAG for accessibility.
- Recognized security attestations for security posture.
- The operator's own published rubric.

## The accessibility gap

- Atlassian is the only operator across all eight that names listing-content accessibility as an approval requirement: descriptive alt text on every informative image, no color-only meaning, enforced contrast/legibility on visual assets.
- HubSpot scores "accessibility" as a certification category, but for the app's own UI, not the listing page.
- Nobody else requires submitter-supplied alt text for uploaded screenshots at all.

WCAG 2.2 AA (text alternatives per SC 1.1.1, captions, contrast) is the de facto external reference an operator would adopt voluntarily - a low-cost differentiator today and future-proofing against tightening accessibility law (EU accessibility legislation, ADA exposure).

## Conversion figures - vendor-reported, unaudited

Marketplace-tooling vendor Partner Fleet (a party selling marketplace software, so a motivated source) publishes:

- "84% of businesses say integrations are 'very important' or a 'key requirement'" (attributed to a 2024 State of SaaS Integrations report).
- "One Partner Fleet customer sees a 30% click-through rate" from marketplace to free trial.
- "An average 2-3% CTR on most SaaS pages", as its comparison baseline.

Treat all three as vendor marketing, never as a target to promise. Its recurring UX recommendations are more transferable than its numbers:

- Lead with a media section.
- Rank calls-to-action: embedded scheduler above lead-capture form above generic link.
- Require attributed social proof.
- Run operator-side "listing scorecards" - a configurable rubric (e.g. minimum screenshot count, at least one attributed testimonial) enforcing consistency across partner-maintained listings, which is a vendor-tool implementation of exactly the rulebook this skill writes.

Notably, the listing UX this vendor cites as best-in-class belongs to the one operator with no badge program at all - listing quality and certification are independent axes.
