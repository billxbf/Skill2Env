# Attribution methods, data sources, and their failure modes

Every method below fails somewhere. The plan's attribution section lists which methods are in use and, next to each, its known failure - so the readout's gaps are declared before launch, not discovered after.

## Method-by-method

| Method                                | How it works                                                  | Where it breaks                                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unique promo codes                    | Creator-specific code at checkout                             | Leaks to coupon/cashback extensions; over-credits the creator; misses buyers who skip codes                                                                   |
| UTM-tagged links                      | Query params read in web analytics                            | Stripped by shorteners and in-app link handling; lost in dark-social sharing; last-click only                                                                 |
| Affiliate network links               | Cookie or server-to-server tracking, commission on conversion | Cookie windows vary wildly between networks (24 hours to 30+ days), so the same sale is credited differently per network; extensions overwrite the last click |
| Platform pixel / shopping             | On-platform conversion events                                 | Mobile privacy opt-outs cause heavy signal loss; walled-garden numbers; the platform grades its own homework                                                  |
| Post-purchase / post-signup survey    | One "how did you hear about us?" question at conversion       | Self-report and recency bias; buyers credit the last-remembered touch                                                                                         |
| Vanity URLs / dedicated landing pages | Per-creator page or redirect                                  | Only captures typed/clicked entries; still last-touch                                                                                                         |
| Geo holdout / matched market          | Channel on/off by region, compare                             | Needs scale; contaminated by overlapping campaigns                                                                                                            |

**The triangulation rule [practice - near-universal]:** last-click structurally under-credits upper-funnel creator content. Deploy standardized UTMs + unique per-creator codes + a one-question survey together, and cross-check transactions with high code usage but zero link clicks. Report click-based and survey-based attribution side by side; the gap between them is information, not an error to hide.

## Code leakage [verified events]

- Coupon/cashback browser extensions insert themselves as the last click and harvest creator codes. A December 2024 exposé of this practice (13M+ views within days) triggered class-action litigation over "stolen influencer commissions" against several major extensions.
- Plan-level controls:
  - Creator onboarding policy ("personal channels only, no coupon sites").
  - A leakage monitor (redemption with no matching link click).
  - Immediate deactivation of leaked codes.
  - Single-use codes once leakage passes a few percent of redemptions.

## Signal loss context

- Mobile app-tracking opt-out rates remain high enough that pixel-based numbers materially undercount; third-party cookies are already blocked by default in several major browsers. Treat pixel/cookie counts as a floor, not a total.
- Cookie-window asymmetry: some affiliate programs credit within 24 hours, others 30 days last-click. When a campaign spans networks, the glossary states each window and the plan never sums across them as if comparable.

## Platform data access - what the brand can actually get

| Platform class           | Brand-side access                                                                                                                              | Screenshot risk                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Image/short-video social | Partnership/branded-content tooling gives ad-manager metrics when the creator opts in; organic story metrics expire fast and live creator-side | High without contracted access |
| Long-form video          | Public view counts; watch time and retention only via the creator's analytics                                                                  | Medium                         |
| Professional network     | Impression definitions include non-follower feed displays; weak marketplace tooling                                                            | Medium                         |
| Live streaming           | Platform APIs exist; attribution to commerce is weakest here                                                                                   | High                           |
| Podcasts / newsletters   | No native brand access at all - measure via codes, vanity URLs, and publisher-reported numbers                                                 | Highest                        |

- **Contract the access, don't hope for it:** API or account-level analytics connection belongs in the creator agreement. Screenshots are trivially falsified and a documented fraud vector; any screenshot-sourced figure gets flagged as such in every report.
- **Podcast/newsletter sponsorships [standard - IAB]:** the IAB Tech Lab Podcast Measurement Technical Guidelines v2.2 (May 2, 2024) define server-side, filtered download counting - the only certified standard in this space. Ask publishers whether their numbers are IAB v2.2-certified; pair downloads with unique codes and vanity URLs since downloads prove delivery, not response.

## The view-definition problem [platform - verified changes]

- Major platforms redefined or relabeled "views" during 2025-2026, moving toward counting from the first frame. Any comparison crossing a definition-change date is invalid; split the reporting series at the date and annotate it.
- Consequence for the plan: the glossary records each platform's view definition _as of the plan date_, and cross-platform view totals are never summed into one "views" number.

## B2B: dark social and self-reported attribution

- B2B creator influence travels through DMs, private communities, podcasts, and screenshots - channels that strip every tracking parameter. Click-based attribution then shows "direct" and "branded search" doing the work that creators actually did.
- Primary workaround [practice]: a "How did you hear about us?" (HDYHAU) field on demo/signup forms - dropdown of known channels plus free text - analyzed at cohort level, never per-deal. Corroborate with trailing branded-search volume.
- Provenance caution: the widely quoted dark-social revenue percentages come from individual practitioners' own CRMs and vendor reports [vendor/practice], not audited studies. Use the mechanism (HDYHAU + branded-search proxy), not the quoted percentages, in the plan.
- Decision threshold [practice]: if fewer than ~20% of closed-won deals name a trackable channel, dark social dominates - promote HDYHAU to the primary conversion source and say so in the plan.
