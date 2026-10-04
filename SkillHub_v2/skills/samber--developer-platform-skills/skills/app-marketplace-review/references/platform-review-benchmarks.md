# Platform review benchmarks

Eight marketplace operators' documented review processes from their published docs and security guides. Every figure carries its source. Where a platform discloses nothing, that non-disclosure is stated rather than filled in.

## Per-platform pipelines

**Salesforce AppExchange / AgentExchange**, the single-hard-gate archetype (Salesforce developer docs, review policy effective 2023-08-09):

- **Stages** (five sequential, published duration bands):
  1. Submission.
  2. Verification (1-2 weeks) - the Security Review Operations team checks materials.
  3. Initial testing (3-4 weeks) - the Product Security team's full manual pass.
  4. Results notification.
  5. Resubmission testing on denial (2-3 weeks).
- **Fee:** $999 per review (Salesforce partner docs).
- **SAST:** mandatory and named - Checkmarx (branded "Source Code Scanner"), 3 free scans per review, alongside Salesforce's own in-house Code Analyzer the developer must run pre-submission. Its report is "useful but not sufficient" per the docs.
- **DAST:** Salesforce retired its own Chimera scanner on June 16, 2025. Partners now bring OWASP ZAP, Burp Suite, or Qualys for external endpoints.
- **Test surface:** the OWASP Top 10 plus Salesforce-specific surfaces (CRUD/FLS enforcement, SOQL injection, sharing violations).
- **Status tracking:** a color-coded Security Review Wizard in the Partner Console.
- **Re-review:** approvals expire, forcing periodic re-review with zero code change.
- **First-pass failure rate:** "Salesforce estimates 50 percent of applications fail the first time" (ISV consultancy Aquiva Labs, relaying Salesforce's own estimate) - re-verified as still current and now converged on independently by multiple other ISV/consulting sources (Magicfuse, Digital Flask, Concret.io, Appnigma), though none point to an official Salesforce-published statistic either.

**Atlassian Marketplace**, the staged-gate-with-fast-path archetype (Atlassian app-approval guidelines and security-workflow docs):

- **Four mandatory security parts:** a security questionnaire (manually reviewed - specific answers can fail the app), one-time partner KYC/KYB via a third-party vendor (2-3 business days, informational only), automated vulnerability scanning that hard-blocks on any critical or high finding, and Privacy & Security tab disclosures.
- **Timelines by submission type:**
  - New app: 5-10 business days.
  - Major version: 5-10 days.
  - Minor Cloud update: instant, security checks skipped.
  - Minor Data Center update: minutes-to-hours (automated scan only).
- **Base functional/quality review:** 10-15 business days, run separately.
- **Annual review:** every listed app, in the anniversary month of first approval, regardless of updates.
- **Ecoscanner** (run by the named Ecosystem Security Team, the most transparent operator scanner documented anywhere):
  - Named per-framework scanners: CSRT for Connect, FSRT for Forge, CVS.
  - TruffleHog-based secret scanning, Endor Labs dependency scanning.
  - Cadence tiered by cost: Connect checks daily, Forge checks per version release, the long-running XSS check monthly.
  - Critical/high findings auto-raise a ticket; fixes auto-close within 24 hours.
  - Only secret-scan hits route to human validation, to control false positives (Atlassian Ecoscanner docs).

**Shopify App Store**, mandatory human review with non-gating automation (shopify.dev app-store-review requirements):

- **Automated pre-submission checks** (expanded April 30, 2025: auth-after-install, redirect, uninstall/reinstall), plus a developer-run AI self-review tool (launched April 20, 2026) that Shopify states "doesn't replace human review". A human reviewer installs and tests every app regardless.
- **SLA:** none fixed. Multi-week, multi-round reviews are common per 2025-2026 developer-forum reports.
- **Scope minimization:** numbered requirements operationalize it per named scope (e.g. `read_all_orders` must justify needing order history beyond the default 60-day window).
- **Billing:** off-platform billing is an outright disqualifier.
- **Five reviewer verification techniques:** codebase scanning for prohibited patterns, configuration/manifest inspection, UI/UX verification, OAuth-billing-install flow tracing, and scope-necessity assessment against declared functionality.
- **Partner-level suspension** (distinct from app rejection): triggers on 2+ unaddressed review exchanges, repeat submissions with growing issue counts, or non-response.

**Slack App Directory**, the functional-only archetype (Slack's review guide):

- **Two phases:** automated feedback cleared during submission, then manual review where the App Directory team installs and tests the app. The checklist has historically run ~36 items.
- **Security-adjacent check:** OAuth scope review - "your app only uses scopes that it needs to work" - with legacy umbrella scopes ineligible for listing at all.
- **SLA:** none fixed ("we will not be able to skip or accelerate the review"). No mandated SAST/DAST/pen test.

**Microsoft Teams / AppSource**, unconditional re-certification made viable by speed (Microsoft Learn):

- **Testing:** "More than 400 tests" run against every app by a named App Validation team ("concierge validators") across desktop, web, and mobile. A self-service validation tool replays the same test cases pre-submission.
- **Timeline:** detailed test report within 24 working hours; clean apps publish in 1-2 business days.
- **Gating:** Publisher Verification plus Publisher Attestation (a self-assessment, not an audit).
- **Optional tier:** Microsoft 365 Certification adds an elevated compliance tier.

**Google Workspace Marketplace**, dual independent gates (Google Workspace developer docs):

- **Base gate:** a manual Marketplace listing review sits on top of Google's OAuth app verification.
- **Restricted scopes** (Gmail, Drive): additionally pass a CASA security audit built on OWASP ASVS and run by App Defense Alliance labs (named: TAC Security, Leviathan, DEKRA), not by Google.
- **CASA tiers:**
  - Tier 1: self-assessment.
  - Tier 2: independent lab DAST plus questionnaire (required for restricted scopes - Google removed the self-scan option at this tier).
  - Tier 3: full manual pen test (required only for the "independent security verification" badge).
- **Cost:** roughly $500-$6,000 per assessment depending on lab and turnaround speed, with annual revalidation regardless of change (App Defense Alliance / Google docs). Re-verified: TAC Security (Google's named preferred partner) prices Tier 2 at $540-$1,800 and Tier 3 at $4,500; Leviathan Security (an ADA founding member) prices Tier 2 at $3,000-$6,000 depending on how fast the assessment must start, with Tier 3 quoted case-by-case. The App Defense Alliance is transitioning its Tier 1-3 naming to Assurance Levels (AL1/AL2) under Linux Foundation governance; Google may still map apps to the legacy tier names.

**Chrome Web Store**, per-update review, ungated propagation:

- Every update must pass review with all code included, but there is no publish-to-install hold - a cleared update auto-propagates immediately (see the incidents file).
- Chrome is also the strongest benchmarked appeal path (see the re-review and appeals file).

**npm**: no pre-publication review of any kind - a registry, not a curated store. Included as the boundary case: its 2025 hardening was authentication-layer, because there was no review gate to strengthen (see the incidents file).

## Reviewer team design, cross-cutting

Every operator that discloses structure names at least two functions - intake/triage and technical testing (Salesforce: Security Review Operations + Product Security; Atlassian: Ecosystem Security Team; Microsoft: App Validation team). No marketplace operator discloses review-team headcount, and none states whether its reviewers are in-house or outsourced - treat headcount or outsourcing claims found elsewhere as unverified. One rare disclosed operational metric: Microsoft's VS Marketplace reported 136 extensions reviewed, 110 removed in one reporting period (Microsoft marketplace security blog).

The automation-pre-screen → human-triage pattern is confirmed at three operators: Atlassian (Ecoscanner → tickets), Microsoft VS Marketplace (multi-engine AV + sandbox → security engineers), and Microsoft Teams (validation tool → concierge validators).

- Shopify keeps automation and AI self-review explicitly non-gating, with mandatory human review.
- Salesforce is the outlier, pairing automated scanning with full manual re-testing of every submission.

## Named scanning vendors documentably inside review pipelines

Confirmed vendor-to-marketplace mapping:

- Checkmarx → Salesforce (mandatory SAST).
- TruffleHog + Endor Labs → Atlassian Ecoscanner.
- Bugcrowd → Atlassian's marketplace bug bounty.
- CASA labs (TAC Security, Leviathan, DEKRA) → Google Workspace.
- OWASP ZAP / Burp Suite / Qualys → accepted DAST for Salesforce.
- Multi-engine AV → Microsoft VS Marketplace.

Slack and Shopify disclose no third-party scanning vendor.

Boundary to keep: SSPM/OAuth-governance vendors (AppOmni, Obsidian Security, Nightfall AI) score and police apps on the customer-tenant side - an org's own security team watching what is connected to its instance. They are not operator-side admission gates. Do not conflate the two when designing who scans what.
