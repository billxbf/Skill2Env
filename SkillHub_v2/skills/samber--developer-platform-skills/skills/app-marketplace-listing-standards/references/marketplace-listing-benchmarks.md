# Eight-marketplace listing-content benchmarks

Sourced from each operator's own published listing/approval documentation unless a row says otherwise. These are reference points for calibrating your own rulebook, never numbers to copy as an industry standard - the geometries and caps below genuinely disagree with each other.

Marketplaces surveyed: Shopify App Store, Atlassian Marketplace, Slack Marketplace, Salesforce AppExchange, Google Workspace Marketplace, Zoom App Marketplace, Chrome Web Store, HubSpot App Marketplace.

## The shared skeleton

All eight converge on the same six-part listing structure despite different field names:

1. A short hook string (app introduction / tagline / short description).
2. A longer benefit-oriented body (app details / summary plus details / long description).
3. A visual gallery with a fixed count and, in six of eight, an exact geometry.
4. An optional short video with a runtime ceiling.
5. A category/keyword assignment with an explicit cap (seven of eight).
6. Off-listing trust surfaces - privacy policy, support contact, documentation/landing link - that gate approval independently of the marketing copy.

## Text-field limits

| Marketplace      | Name                                                                                    | Hook                                                                      | Body                                                                                                    |
| ---------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Shopify          | ≤30 chars, must lead with brand name                                                    | app introduction ≤100 chars                                               | app details ≤500 chars; feature list items ≤80 chars                                                    |
| Atlassian        | ≤60 chars; bans "Atlassian", "plugin", "beta", "add-on", "app" in the name              | tagline ≤130 chars                                                        | summary ≤250 chars; exactly 3 mandatory highlight blocks ("Rule of 3"): title ≤50, summary ≤220 each    |
| Slack            | unique, readable, spellable                                                             | short description ≤10 words (tightest hook cap surveyed), plain text only | long description: what the service does, the problem, and how it works inside the platform specifically |
| Salesforce       | title + tagline (no published char caps found)                                          | -                                                                         | full description + key features; completion tracked in the Listing Builder rather than gated per field  |
| Google Workspace | ≤50 chars; must match the OAuth consent screen; cannot use the operator's product names | short description ≤200 chars                                              | detailed description <16,000 chars (largest body cap surveyed)                                          |
| Zoom             | informative and unique, ≤50 chars                                                       | principles-based, no numeric caps published                               | principles-based ("Value", "Trust") - see the spec-strictness menu's deletion argument                  |
| Chrome           | -                                                                                       | -                                                                         | blank description = automatic rejection; violations enumerated, not capped (see below)                  |
| HubSpot          | brand rule: never combine the operator's name with the app's own name/logo              | -                                                                         | content must be integration-specific, not generic product marketing; all URL fields ≤250 chars          |

## Media specs and geometries

No universal screenshot ratio exists - this is the load-bearing negative finding:

| Marketplace      | Screenshot geometry                                                                 | Count                             | Icon                                              | Distinctive mechanism                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shopify          | 1600×900 (16:9)                                                                     | 3-6, ≥1 of actual app UI          | 1200×1200, no text/trademarks on it               | feature media: video or 1600×900 image, ≥4.5:1 contrast                                                                                                                       |
| Atlassian        | 1840×900 full + 580×330 cropped highlight                                           | per Rule of 3 + gallery           | -                                                 | every screenshot requires a caption ≤220 chars                                                                                                                                |
| Slack            | 1600×1000 (8:5), <2MB                                                               | -                                 | -                                                 | screenshots must show the app inside the platform's own UI, not the third-party tool's; wrong-ratio/off-topic image is a named rejection trigger                              |
| Salesforce       | 700×467 (≈3:2), ≤1MB                                                                | -                                 | 60×60 PNG; 224×164 tile for top search results    | media specs spread across Partner Community docs, not one canonical sheet - verify against the live console before citing                                                     |
| Google Workspace | 1280×800 recommended (640×400, 2560×1600 accepted), square corners, no letterboxing | 1-10                              | ≥32×32 and 128×128                                | 220×140 application-card banner required                                                                                                                                      |
| Zoom             | no published geometry                                                               | -                                 | 160×160, separate light-mode and dark-mode images | Technical Design Document required before submission is accepted at all - the only artifact-gated submission surveyed                                                         |
| Chrome           | 1280×800 (640×400 accepted)                                                         | 1-5                               | 128×128                                           | 440×280 promo tile: optional but ranking-penalized when absent - "items without it are ranked below items that have one", the only ranking-penalty enforcement lever surveyed |
| HubSpot          | no published geometry; content/URL correctness policed instead                      | screenshots + demo video required | -                                                 | every URL verified live and public by the operator's own crawler; a Shared-data table must match the app's actual OAuth scopes                                                |

## Video ceilings

The runtime ceiling tracks the buyer evaluation mode, not the market:

- Atlassian: 30 seconds (strictest - live functionality only, explicitly anti-marketing).
- Slack: 30-90 seconds (public video link, captions on, ads off, realistic environment).
- Shopify: 2-3 minutes (loosest - promotional tone allowed, screencast content capped at 25% of runtime).
- Zoom: permits local-language or English demo video.

Pick a ceiling from your own question-4 answer. Do not average these.

## Description philosophy - the convergent rule with the worked pair

Shopify and Atlassian arrived independently at the same instruction: lead with the customer outcome, connect features to measurable results. Shopify's worked pair (Partner Dashboard requirements) is the cleanest accept/reject example surveyed:

- Accepted: "Reports that show you sales data in real time."
- Rejected: "Reports that use the latest push technology to offer you sales data with only 250ms of latency." - technical mechanics the buyer doesn't evaluate on.

Chrome's Listing Requirements policy (last updated 2024-07-10) enumerates the violation side most explicitly:

- Misleading, inaccurate, incomplete, or non-descriptive text.
- Out-of-date metadata.
- Keyword spam, defined concretely as unnatural repetition of a keyword more than five times, or lists of sites/brands/regions with no added value.
- Unattributed or anonymous user testimonials - the only surveyed marketplace naming testimonial attribution as its own trigger.

## Naming-order rule - three independent enforcements

- Atlassian: "Time Tracker for Jira" accepted; "Jira Time Tracker" treated as a trademark issue.
- Slack: "Task notifications for Slack" accepted; "Slack task notifications" not.
- Zoom: "for Zoom" explicitly permitted to describe compatibility; the operator's name or trademarks in the app name itself are not.

Three operators converging on the identical shape makes this a default rule for any marketplace whose name carries trademark weight.

## Taxonomy caps - the full spectrum

| Marketplace      | Shape                                                            | Cap                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Salesforce       | fixed list                                                       | 1 category + 2 industries (tightest surveyed)                                                                                                                          |
| Chrome           | single fixed-list pick                                           | 1 category; soft cross-locale consistency warning only                                                                                                                 |
| Atlassian        | fixed flat list of 10                                            | 2 categories + 4 keywords; stale categorization → marked "uncategorized" and removed from every browse/filter surface (soft, self-correcting)                          |
| Shopify          | categories + structured tags                                     | up to 25 structured features per category; 5 search terms, one idea per term ("email marketing" accepted, "email marketing for leads" rejected for stacking two ideas) |
| Google Workspace | 1 self-selected category + operator-curated layers               | Editor's Choice, "Works with…" labels, "Recommended" status - all operator-assigned, none purchasable                                                                  |
| HubSpot          | 1 category + feature tags + operator-curated persona collections | collections curated for marketer/sales/designer personas                                                                                                               |
| Slack            | browse categories                                                | no explicit cap documented in the fetched guidelines                                                                                                                   |
| Zoom             | overlapping product-based and function-based categories          | no published per-listing cap; the widely cited "15+ categories" figure is third-party analysis (UC Today), not an operator spec - treat as unverified                  |

## Localization - the three shapes plus one asymmetry

- **Auto-translate with override** (Shopify):
  - An English listing auto-translates into eight languages across every text field.
  - A vendor can override any one language.
  - Deleting the override silently reverts to machine translation.
- **Region-locked** (Google Workspace): for each distribution region selected, that region's language must be present in the listing details, or users in that region cannot find or open the listing at all.
- **All-or-nothing declaration** (Slack): declaring a language commits the vendor to every message, interactive component, and related interface being available in that language - a runtime-capability claim, with no machine-translation fallback.
- **Opt-in per market** (Salesforce): market-specific listings (e.g. a per-country storefront listing) via a documented setup, fully optional.
- **The asymmetry** (Chrome): text, screenshots, and video localize per locale, but the two promo tiles cannot be localized at all - the one ranking-relevant visual asset stays locked to a single design across every locale. Worth checking your own asset pipeline for the same accidental gap.

## Off-listing trust surfaces

Slack documents the strictest requirements beyond the marketplace page itself:

- A landing page publicly accessible without login, covering the integration and install path (a PDF, document, or code repository explicitly disqualified as a substitute).
- A support page offering contact without a new account signup, committing to a response within 2 business days.
- A privacy policy with a minimum-coverage checklist: data collected, usage, retention duration, access/transfer/deletion request process, and a real contact channel (a physical address alone explicitly insufficient).

HubSpot adds the enforcement mechanism: every URL verified live by crawler, setup guide not behind a login, listed pricing required to match the vendor's own website. Atlassian adds the commercial-hygiene variant: paid apps must use a company email domain, not a personal one.

## Merchant/customer eligibility gating

One upstream mechanism worth copying from Shopify: the vendor sets machine-checkable install eligibility (sales channel, country, currency) so poor-fit customers are excluded _before_ the install-then-uninstall-then-negative-review cycle - listing-quality enforcement acting upstream of the review score rather than policing content after the fact.
