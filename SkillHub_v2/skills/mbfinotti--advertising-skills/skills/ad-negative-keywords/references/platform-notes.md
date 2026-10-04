# Platform notes (optional)

Vendor-specific mechanics for the main workflow. Load this file only when the user names their platform; the SKILL.md workflow stands on its own without it. Limits and defaults drift - verify in-account before building at scale.

## Google Ads

- Negatives never match close variants: excluding broad `flowers` blocks "red flowers" but NOT "red flower". Add plurals, synonyms, and stems manually.
- Casing and misspellings are covered automatically.
- When adding a negative from the search terms report UI, the pre-selected match type is exact - the trap flagged in the skill's failure modes. Switch to phrase before saving.
- Levels and limits:
  - Up to 10,000 negatives per Search or Performance Max campaign (PMax raised from 100 in March 2025).
  - 20 shared lists per account, 5,000 keywords per list.
  - Account-level list applies to all eligible Search and Shopping inventory including PMax.
  - Display/Video considers at most 1,000 account-level negatives and treats them as thematic exclusions, not literal blocks.
- Performance Max and standard Shopping have no positive keywords - negatives (plus brand exclusions in PMax) are the primary query control. PMax negatives became self-serve in December 2024. Shared-list support arrived August 2025.
- Search term visibility is partial since September 2020. Practitioner measurements put hidden terms around 40% of spend (ranging 20-80%). This is what makes the n-gram pass necessary rather than optional.
- Formatting rules:
  - Max 80 characters and 10 words per negative.
  - A query longer than 16 words can bypass a negative whose match falls after the 16th word.
  - Usable symbols are `&`, accents, and `*` - accented and unaccented count as different negatives.
  - Most other punctuation errors out.
- Conflict tooling: the platform's "conflicting negative keywords" recommendation misses shared-list conflicts - pair it with a script or third-party conflict check rather than trusting it alone. Never auto-apply it.
- Data pull via API (GAQL): `keyword_view` segmented by date returns one row per keyword per day per match type - deduplicate on (ad group, keyword text, match type) and aggregate metrics, or drop the date segment, before computing thresholds.

## Microsoft Advertising

- Default negative match type is phrase (opposite of Google's exact default when adding from a report).
- No negative broad match at all - phrase and exact only.
- Negative keyword lists attach to campaigns only, never ad groups: one list per campaign, 20 lists per account, 5,000 keywords per list.
- Close variants are not filtered by negatives here either: plurals, synonyms, and misspellings of a negative still match - add variants manually, same as Google.
- A dedicated negative keyword conflict report exists - use it for the quarterly conflict sweep.

## Amazon Ads

- Only negative phrase and negative exact exist - no negative broad.
- Opposite of Google on variants: Amazon negatives DO block close variations of the phrase. Fewer manual variants needed.
- Negative product/ASIN targeting blocks specific product detail pages - a lever Google has no equivalent for. Use it against poorly converting placements and competitor pages.
- Three distinct reports:
  - The advertising Search Term Report - actual shopper queries, the input for this skill's workflow.
  - Search Query Performance in Brand Analytics - organic search behavior, brand-registered sellers only.
  - Search Term Impression Share - your share per query, 30-day lookback.
- Common use of negative exact: stop auto and manual campaigns from cannibalizing each other on the same query.
- Cadence practitioners use: weekly above ~$10k/month ad spend, bi-weekly below.
- The 15-20-click zero-order gate (10-12 for CPCs above ~$3) originated in this ecosystem and transfers directly.

## Cross-platform reminders

- Never assume one platform's match-type defaults or variant behavior on another - the three above disagree on both.
- The skill's match-type ranking (`phrase > exact > broad`) survives a platform with no negative broad match: broad already sits last, so Microsoft and Amazon simply lose the bottom rung. The level ranking does move - where shared lists attach to campaigns only, the shared-list rung loses the ad-group reach the default order assumes, and a recurring theme inside one campaign drops to the campaign rung.
- Keep one master exclusion taxonomy per business, but maintain per-platform lists: syntax, limits, and levels don't port automatically.
