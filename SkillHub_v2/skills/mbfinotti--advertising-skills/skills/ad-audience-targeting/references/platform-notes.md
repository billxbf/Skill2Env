# Platform notes - vendor-specific floors, thresholds, and mechanics

Optional integration notes. Load only when the user names their platform. **Every number here has moved at least once in 2024-2026 - verify against current platform documentation before locking a plan.** Where platform docs and practitioner practice disagree, the platform states a general-case optimum; practitioners optimize for specific constraints.

## Table of Contents

- [Meta (Facebook/Instagram)](#meta-facebookinstagram)
- [Google Ads](#google-ads)
- [LinkedIn](#linkedin)
- [TikTok and other short-video platforms](#tiktok-and-other-short-video-platforms)
- [EU / regulatory quick reference (all platforms)](#eu--regulatory-quick-reference-all-platforms)
- [Sources](#sources)

## Meta (Facebook/Instagram)

- Learning threshold: ~50 optimization events per ad set per week; below it, ad sets stay "learning limited". Budget floor per ad set ≈ (target CPA × 50) ÷ 7 per day.
- Lookalike seed:
  - Platform floor: 100 people from a single country ("Facebook requires a minimum of 100 people from a single country for a seed audience, we recommend using a list with at least 1,000 contacts" - Demand Curve).
  - Practitioner recommendation: 1,000+ contacts.
  - Lookalike % = similarity band: 1% = closest match to seed, larger % = broader.
- Custom audience delivery:
  - Pools under ~1,000 people struggle to deliver.
  - Use engagement audiences when pixel traffic is thin, in the fill-speed order the skill body sets: `video viewers > page/profile engagers > lead-form openers`.
- Audience size guidance:
  - Meta currently recommends 2M+ ("Meta wants you to set your audience size to 2 million or more" - Ben Heath).
  - Heath earlier used a 500,000 floor as his own rule of thumb.
  - Heath's survey: open/broad 45%, detailed 34%, lookalike 21%.
- Retargeting windows:
  - Website visitors: max 180 days.
  - Video viewers and social engagers: up to 365 days.
  - Ben Heath's practice: include the maximum inclusive pool, let algorithmic expansion work on top.
- Detailed targeting:
  - Treated as suggestions, not constraints, for most performance goals.
  - Detailed-targeting _exclusions_ were removed; campaigns using them stopped delivering from January 31, 2025.
  - First-party suppression lists still work and remain best practice.
- Sensitive interest categories (health, race/ethnicity, political affiliation, religion, sexual orientation) removed in waves (January 2022, early 2024).
- Special Ad Categories (Housing, Employment, Credit, Financial Products, Social Issues/Elections/Politics) trigger:
  - Age fixed 18-65+.
  - Gender fixed all.
  - No ZIP targeting.
  - Minimum 15-mile radius.
  - No lookalikes.
  - No detailed-targeting exclusions.
  - All US financial-product advertisers included since January 21, 2025.
- Audience Overlap tool:
  - Suppresses results under 1,000 overlapping users.
  - Least reliable when comparing two uploaded custom audiences.
- CBO/ABO:
  - Meta self-reports CBO cutting CPA ~4.6% on average (self-reported, treat as marketing).
  - One third-party test found fixed per-ad-set budgets perform better for prospecting tests.
  - Practitioner default: test with fixed budgets, scale with pooled.
- Signal loss:
  - Pixel-only accounts are estimated to miss 30-40% of iOS purchase signal.
  - Run Conversions API alongside the pixel, deduplicated by event_id.

## Google Ads

- Customer Match: minimum cut from 1,000 to 100 active users across Search, Display, YouTube (rolled out from May 2024, standardized by late 2025) - a 90% cut that made older published advice stale.
- Lookalike segments:
  - Similar Audiences were sunset.
  - The successor lives in Demand Gen only.
  - It requires a 1,000-user seed.
  - It needs 2-3 days of processing before launch.
- Performance Max:
  - Google claims "over 18% more conversions at a similar cost per action" (vendor self-reported).
  - Audience signals are advisory inputs, not hard constraints.
  - Practitioner floor: ~$50/day per PMax campaign, plus complete conversion tracking before launch.
- In-market/behavioral segments are the platform's native mid-funnel tier; keyword intent remains the dominant signal on Search, so the targeting-plan leverage there is lower than on social.
- Third-party cookies: Chrome deprecation was cancelled (July 2024, confirmed 2025), but ~17-20% of traffic (Safari, Firefox, Brave) blocks them regardless - plan EU/Apple-heavy audiences with that discount.

## LinkedIn

- Hard floor:
  - 300 members per matched audience ("LinkedIn requires an audience size of at least 300 people (that the platform recognizes in its user base) in order to run a campaign" - B2Linked).
  - Company lists need 300 rows and 300 matched accounts.
  - Location is a mandatory facet.
- Recommended vs. practiced:
  - LinkedIn suggests 50,000+ (300,000 for Sponsored Content).
  - B2B SaaS practitioners commonly run 5,000-30,000 for conversion campaigns, because the recommended sizes dilute a narrow ICP.
- Targeting taxonomy and exclusions:
  - Targeting taxonomy (B2Linked's framing): "Audiences" (matched: ABM lists, retargeting, lookalike-style) vs. "Audience Attributes" (profile-derived: title, function, seniority, company).
  - Exclusions run first: "LinkedIn will prioritize exclusion before inclusion criteria."
  - Standard exclusion set: current customers, employees, competitors.
- Job titles and function targeting:
  - Job titles are freeform text, and LinkedIn recognizes only ~30% of them, so title-only targeting misses most of the real audience.
  - Function + seniority typically triples the addressable audience at similar engagement.
  - Title and seniority facets cannot be stacked together.
- Audience Expansion:
  - Leave off for defined-ICP B2B ("It's a complete waste of ad budget to advertise to anybody and everybody, which is exactly what happens when Audience Expansion is enabled" - B2Linked).
  - Lookalike Audiences were replaced by Predictive Audiences in February 2024.
- Retargeting pool build order:
  - By efficiency: `video viewers > site visitors > lead-form openers`.
  - By fill time: a video-view pool (targeting ≥50% viewers) fills in about a week.
  - A lead-form-opener pool takes one to three months of continuous spend.
  - B2Linked's benchmarks put the same gap at roughly $1,000 versus $6,000-9,000; use the ratio, not the figures, since both move with market and geography.
  - Recency windows: 30/60/90/180/365 days.
- Small-audience cost: "SUPER small audiences will make you pay out the nose" (AJ Wilcox). Fix: run last-90-days with the last-30-days slice excluded rather than a bare 30-day pool.

## TikTok and other short-video platforms

- Broad targeting plus native-feeling creative is the norm.
- Interest layers behave as loose suggestions.
- Practitioner comfortable minimums run to the hundreds of thousands or millions.
- Verify current floors in platform docs; published third-party numbers for these platforms go stale fastest.

## EU / regulatory quick reference (all platforms)

- DSA:
  - No profiling-based ads to known minors.
  - No targeting on special-category data (ethnicity, religion, political views, sexual orientation).
  - User consent cannot override either ban.
- Political/electoral/social-issue ads: non-deliverable in the EU since October 6, 2025 (TTPA).
- GDPR/Consent Mode: marketing-consent rates average 40-60%, so expect EU audience pools and tracked conversions to undercount accordingly.

## Sources

- Ben Heath (Heath Media): heathmedia.co.uk/best-audience-size-for-facebook-ads/ · heathmedia.co.uk/open-targeting-the-big-facebook-ads-debate/ · heathmedia.co.uk/facebook-ads-retargeting-strategy/
- AJ Wilcox / Eric Jones (B2Linked): b2linked.com/blog-page/linkedin-ads-how-to-effectively-target-your-audience · b2linked.com/blog-page/how-to-effectively-use-linkedin-ads-lookalike-audiences · b2linked.com/blog-page/the-fastest-ways-to-build-retargeting-audiences-on-linkedin-ads · b2linked.com/blog-page/linkedin-ads-exclusions-how-to-refine-your-targeting-to-reach-the-right-audience · b2linked.com/blog-page/start-retargeting-small-audiences-linkedin-ads · b2linked.com/blog-page/linkedin-audience-expansion-why-its-not-good-for-brand-awareness
- Demand Curve: demandcurve.com/blog/facebook-ads-targeting
- Google PMax claim: blog.google (official); Customer Match minimum change: searchengineland.com, ppc.land
- LinkedIn floors: LinkedIn Help articles a420864, a423690
- Meta policy changes (exclusion removal, sensitive categories, Special Ad Categories): searchengineland.com, socialmediatoday.com, adweek.com, jonloomer.com (Meta's primary newsroom pages were corroborated via these outlets)
