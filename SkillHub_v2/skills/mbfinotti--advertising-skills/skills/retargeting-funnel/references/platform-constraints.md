# Platform constraints for retargeting stage design

**Staleness warning - read first.** Every value in this file changes often and without notice: platforms revise minimums, retention ceilings, and cap mechanics several times a year. Treat this file as a map of _what to check_, not as current truth.

Verify each number against the platform's official documentation before building anything on it. Where a value below is dated, the date is the last point it was confirmed.

## Contents

1. Minimum audience sizes (delivery floors)
2. Retention ceilings (maximum lookback windows)
3. Impression-cap field availability
4. Practitioner frequency bands per platform and stage
5. Platform-specific gotchas
6. Privacy constraints that shrink pools

## 1. Minimum audience sizes (delivery floors)

The documented minimum is the point below which the platform refuses to serve or will not populate the audience. The practical floor is where practitioners report delivery becomes stable and CPMs normal - design stages to clear the practical floor after exclusions, not just the documented one.

| Platform                                | Documented minimum                              | Practical floor         | Notes                                                                                                                                                    |
| --------------------------------------- | ----------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Google Ads (Display / Search / YouTube) | 100 active users (standardised 2024-2025)       | ~1,000                  | Search remarketing (RLSA) historically required 1,000; dedicated search-remarketing campaigns are typically only worthwhile at 100k+ monthly site visits |
| Meta Custom Audiences                   | 100 people                                      | ~1,000                  | Below ~1,000 the delivery algorithm has too little room; learning phase may never exit                                                                   |
| LinkedIn Matched Audiences              | 300 matched members                             | 1,000-5,000 per segment | Below ~300 the campaign is flagged and will not deliver; the minimum is ANDed with a required location facet                                             |
| TikTok Custom Audiences                 | 1,000 matched users                             | 1,000                   | Highest documented floor of the majors                                                                                                                   |
| Microsoft Advertising                   | 300 (cookie pool)                               | 300                     | 1,000 for similar-audience seeds                                                                                                                         |
| Reddit                                  | 50 (pixel/engagement); 1,000 for uploaded lists | 50                      | Lowest floor - useful overflow channel for thin B2B pools                                                                                                |

When a stage cannot clear its floor after exclusions, work down this order:

widen the window > broaden the trigger (e.g. all visitors instead of product-page viewers) > merge adjacent windows into one audience > fall back to a single combined warm pool

All four are minutes of work in the audience builder, so the ordering is value, not effort: each step down spends more of the stage's message distinctness to buy the same headroom. Re-rank when the account's own constraint is elsewhere - a platform at its retention ceiling cannot widen, so broadening the trigger becomes the first move available.

## 2. Retention ceilings (maximum lookback windows)

The ceiling silently truncates any longer window you request - a "365-day" stage on a 180-day platform is a 180-day stage.

| Platform                                 | Audience type                              | Ceiling                                                                                                     |
| ---------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Meta                                     | Website custom audiences (standard events) | 180 days                                                                                                    |
| Meta                                     | Website/app purchase-event audiences       | 730 days (extended from 180, effective May 2026; existing purchase audiences auto-updated unless opted out) |
| Meta                                     | Page / Instagram engagement audiences      | 365 days                                                                                                    |
| Meta                                     | Lead-form engagement                       | 90 days                                                                                                     |
| Google Ads / Analytics remarketing lists | All                                        | 540 days                                                                                                    |
| LinkedIn                                 | Website / engagement audiences             | Commonly run at 180 or 365 days to clear the 300-member floor                                               |

The Meta 730-day purchase change is double-edged: it enables 2-year win-back stages, but any purchaser-_exclusion_ built on the same audience now suppresses two years of buyers from prospecting instead of six months. Audit converter-exclusion windows explicitly whenever a platform extends a retention default.

CRM-list (uploaded) audiences generally persist until manually removed on all platforms, which is why long-window B2B and win-back stages should be list-based rather than pixel-based.

## 3. Impression-cap field availability

| Platform                 | Cap field on conversion-type objectives?                                                                                                                      | What actually caps frequency                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Meta                     | No - cap field only on Reach / Awareness objectives                                                                                                           | Audience size and creative rotation; monitor the frequency metric and intervene manually |
| Google Display / YouTube | Partial - viewable-frequency controls on some campaign types; verify per type                                                                                 | Campaign-level settings where exposed; otherwise audience size                           |
| LinkedIn                 | No user-set cap on most objectives; platform applies internal pacing                                                                                          | Audience size, creative rotation, and engagement-based exclusion tricks (see gotchas)    |
| TikTok                   | Limited; verify per objective                                                                                                                                 | Audience size and rotation                                                               |
| DV360 / programmatic     | Yes - most granular: caps at campaign, insertion order, and line-item level, plus recency capping (e.g. max 1 impression/hour); strictest applicable cap wins | The configured caps                                                                      |

Where no cap field exists, write the stage's cap as a _proxy_: the frequency reading at which you act, plus the decay signals (CTR down 15-20%+, CPM up 10%+, negative feedback rising against a 7-day rolling baseline).

## 4. Practitioner frequency bands per platform and stage

These are practitioner-published operating bands calibrated on agency account data - folklore with mileage, not RCT results. Recalibrate against the account's own decay curve. One large multi-account D2C dataset shows CTR roughly halving between frequency ~2 and ~5, with cost per purchase about 2x baseline by frequency 7.

| Platform             | Prospecting (per user/week) | Retargeting (per user/week)                                   | Reported fatigue onset                                                                 |
| -------------------- | --------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Meta                 | 2-3                         | 5-7                                                           | Prospecting decline from ~2.5, cliff past ~4; retargeting decline ~7-8                 |
| YouTube              | 2-3                         | Higher tolerated                                              | -                                                                                      |
| LinkedIn (B2B)       | 3-4                         | ~3/week per person in priority accounts; rotate 3-5 creatives | Small pools build frequency fast; refresh creative every 2-3 weeks                     |
| TikTok               | 2-4                         | 5-8                                                           | Tolerates roughly 2x Meta's frequency before fatigue (~5 prospecting, ~10 retargeting) |
| Programmatic / DV360 | ~5-7                        | 5-7                                                           | Use recency caps to spread exposures                                                   |

Working bands by campaign type (watch / warning / act), from multi-account practitioner systems:

- Prospecting: 1-2.5 / 2.5-4 / >4
- Retargeting: 2-4 / 4-6 / >6
- Tiny ABM-style pools: 2-5 / 5-8 / >8

Retargeting's looser band exists because the pool is small and known-warm - expected impressions per person are structurally higher.

## 5. Platform-specific gotchas

- **LinkedIn audiences are non-retroactive.** Collection starts only when the audience is created - data before creation is gone permanently. Create every retargeting audience you might ever want (site visitors, video viewers, ad engagers, form openers, company-page visitors) before launching anything.
- **LinkedIn small-pool bidding:** small retargeting/ABM audiences deliver better on automated bidding. Manual bids underdeliver on thin pools.
- **LinkedIn lookalikes were discontinued (February 2024)**, replaced by predictive audiences - relevant if a stage plan assumed lookalike expansion from a retargeting seed.
- **Meta learning phase:** editing a live ad resets learning. Pausing does not. Launch replacement creative alongside, not as edits.
- **Sequential delivery:** true creative sequencing (ad A then ad B to the same user) is only natively enforced on DV360-style programmatic. On social platforms, sequence is approximated by the windowed mutually exclusive stages this skill designs.
- **Dynamic/catalogue ads:** suppress purchased items via the purchase event and exclude out-of-stock items at the catalogue level, or the deepest stage will advertise things the user already bought or cannot buy.

## 6. Privacy constraints that shrink pools

- **Safari/Firefox cookie limits:** first-party JavaScript cookies are capped at 7 days on Safari (24 hours when a click-tracking parameter is present), so Safari-heavy traffic largely cannot populate pixel-based windows beyond a week. Any window longer than ~7 days undercounts these users.
- **iOS App Tracking Transparency:** opt-in rates around 25-40% mean app/social pixel pools shrank roughly 10-30% versus pre-2021. Plan stage sizes with that haircut.
- **Consent Mode (EEA/UK):** denied-consent users drop out of retargetable pools. Platforms backfill measurement with modelled conversions, which affects the measurement plan more than the audience plan.
- **Mitigations**, ranked by pool recovered per unit of effort:
  1. Enhanced / first-party conversion matching - a console setting plus a tagging check, an hour. Compliance: consent-mode wiring and a privacy-notice line, reversible by switching it off.
  2. CRM-list audiences for anything beyond a 30-day window - an hour to export, then a standing weekly refresh job. Compliance: a lawful basis for pushing customer records to an ad platform, suppression of anyone who opted out, and a deletion path once uploaded.
  3. Server-side event delivery, conversions-API-style - a week of engineering, then permanent ownership of an endpoint. Compliance: the heaviest - the endpoint handles personal data directly, so data residency, processor terms and hashing rules all apply, and it is the hardest to unwind.
- effort and compliance cost both run down that list while value runs up it: server-side delivery recovers the most signal and costs the most to stand up. So the order is a default for a team without spare engineering, and flips as soon as one is available or a server-side gateway is already deployed for another site. Chrome retained third-party cookies (2024-2025 decisions), so the worst-case shock did not land - but the Safari/iOS shrinkage is permanent.
