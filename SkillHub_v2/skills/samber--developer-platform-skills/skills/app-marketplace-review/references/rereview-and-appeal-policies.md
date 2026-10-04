# Re-review triggers and appeal tiers across platforms

## What re-triggers review after approval

Re-review-on-update is the dimension where the eight benchmarked marketplaces diverge most sharply - and the divergence maps exactly onto which platforms the 2024-2026 supply-chain incidents hit (see the update-channel incidents file).

- **Atlassian**, the most explicit objective fast-path (Atlassian approval guidelines):
  - Routine version updates skip re-approval entirely.
  - Full re-review re-triggers only on a payment-model change (free→paid, or vendor-collected→Atlassian-collected billing) or a new app type/edition, regardless of whether code changed.
  - Forge apps get automated checks on every version release anyway.
  - Connect apps are scanned daily regardless of releases.
  - Every listed app gets an annual anniversary-month review even with zero updates.
- **Salesforce** - new package versions generally require re-review, and approvals themselves **expire**, forcing periodic re-review with no code change. Salesforce documents no lightweight patch fast-path. Treat third-party claims of auto-approved updates after a first pass as unverified.
- **Slack** - re-review only for "substantial changes or updates to the features, purpose or functionality" (Slack's own wording). "Substantial" is subjective and undefined: a developer cannot self-assess it, which is why this skill deletes subjective triggers as a design option.
- **Microsoft Teams / AppSource** - unconditional: "If you make changes after your submission is certified, it must go through the certification process again" (Microsoft Learn), with no minor-update exemption. The 24-working-hour report SLA is what keeps this viable.
- **Google Workspace** - scope-based, not version-based: any change to restricted-scope usage re-triggers OAuth/CASA review, and annual CASA revalidation applies regardless of change - a restricted-scope app never reaches a steady state where re-review stops.
- **Chrome Web Store** - every update "must pass review with all code included", but with **no publish-to-install hold**: a cleared update auto-propagates immediately.
- **npm**: no review at any point. Instant self-service publish.

The pattern: platforms with an objective narrow trigger (Atlassian) or a fast unconditional re-check (Microsoft Teams) close the update-channel gap without slowing legitimate patches. The platforms with instant, ungated, auto-propagating updates (Chrome, npm) are where every documented 2024-2026 major incident actually landed.

**Objective "minor update" definition to reuse:**

- No new OAuth scopes.
- No new external endpoints.
- No change to data handling.
- No payment-model change.
- No new app type.

Anything else clears the fast path.

## Appeal tiers

Genuine appeal mechanisms - distinct from addressing reviewer feedback and resubmitting - are rare. The eight platforms split three ways:

**Real appeal:**

1. **Chrome Web Store** (strongest):
   - A dedicated Appeal button on the item detail page and in the developer dashboard, pre-populated with extension ID and violation data.
   - Rejection emails cite the violated policy.
   - Appeals are human-reviewed, with developers reporting 1-2 week turnaround.

   EU/UK business users additionally get voluntary mediation under P2B platform-to-business regulations.

2. **Shopify**: "Each appeal is reviewed by a Shopify team member, which ensures that a human reviews your case" (Shopify's own wording).
   - A defined email-based process, for account/store restrictions and terms violations.
   - A separate Partner Governance escalation path, for delistings (which developers report as opaque).

**Escalation, not an appeal** (a channel to raise concerns, not an independent re-review of the decision):

3. **Atlassian**: an escalation process for compliance concerns, and security tickets allowing direct dialogue with security engineers - framed around compliance disputes, not rejected-submission appeals.
4. **Salesforce**: a written findings report plus Partner Security Portal office hours and support cases. No independent appeal board - resolution stays iterative remediation.

**No documented formal appeal:** Slack, Microsoft Teams/AppSource (validation report + resubmission cycle only), Google Workspace Marketplace, npm (nothing to appeal - no pre-publication review exists).

**Design implication:** six of eight platforms still default to fix-and-resubmit. A marketplace that wants lower developer churn and lower regulatory exposure - the P2B angle applies to any EU-facing platform - builds a human-reviewed appeal with a stated turnaround, and graduates to the dashboard-integrated Chrome model when volume or EU exposure justifies the build.
