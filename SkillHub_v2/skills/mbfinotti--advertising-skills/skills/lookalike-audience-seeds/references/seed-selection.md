# Seed Selection: Cohorts, Windows, Exclusions, Value, and Fallback Sources

## RFM selection - the default

RFM (Recency, Frequency, Monetary) is the dominant named framework for picking seed rows. The operationalized version (Klaviyo) splits customers into six mutually exclusive cohorts: Champions, Loyal, Recent, Needs attention, At risk, Inactive - with the Monetary score defined on historic customer lifetime value rather than AOV. The canonical seed export is **Champions + Loyal combined**.

Predictive layers on top where available: predicted CLV (needs roughly 500 orders of history to be usable), churn risk, next expected purchase date.

Top-slice heuristics when RFM tooling is absent (attributed practitioner rules). Efficiency ordering, best ratio first - `pattern filter > ticket/frequency slice > revenue slice`:

- **Pattern filter** - 2+ orders, AOV above a threshold, first order more than 90 days ago. Built specifically to strip recent one-time buyers. Best ratio on the board: one WHERE clause, no percentile computation, no coordination, and it encodes the negative-selection intent directly instead of hoping the percentile does.
- **Top 20-25% by average ticket or purchase frequency.** About an hour of SQL - a per-customer aggregate plus a percentile. Approximates worth better than spend does.
- **Top 10% by revenue over the past 12 months**, defined in the BI layer or SQL and validated with the finance/data team before export. Same query effort as the slice above, but the validation adds days of coordination, and revenue drifts toward the tenure/low-margin failure the value-based rules below warn about. Lowest ratio - use it when finance already maintains the definition, which flips its effort to near-zero.

All three assume no RFM tooling and no analyst on call. If the user has either, re-rank: with a CLV model already in place, none of these compete with predicted CLV.

Expressed as a query, a monetary seed is a per-customer aggregate with a threshold:

- Group orders by resolved customer identity.
- Sum order value.
- Keep rows above the cutoff.
- Always select against identity-resolved records, not raw source rows, so one person never appears as three.

Why quality-first: practitioner consensus, stated verbatim by Stackmatix, is that "a 150-person high-LTV customer list outperforms a 15,000-person newsletter subscriber list because it gives Meta a tighter signal cluster." Grow With Sakib reports 500 paying customers beating 5,000 newsletter subscribers "in every meaningful test". Directional practitioner claims, not audited studies - but consistent across sources, and aligned with Meta's own homogeneity-over-size guidance.

## Recency windows

- **30-90 days**: the sourced starting point for customer-list seeds.
- **180 days**: acceptable for pixel/CAPI-tracked buyers (also the platform-side maximum lookback for website custom audiences on Meta).
- **12-18 months**: the decay cliff - contact data older than this produces materially lower match rates and worse performance. Drop or archive these rows.
- Widening the window is fallback rung 2 - never part of the initial selection, and only reached once the effective seed has actually failed a floor. It may be run before rung 1 when no enrichment vendor is contracted, since it costs an afternoon. That is a cheaper order of attempts, not a licence to open with a wider window.

## The negative-selection pass

Run before every export. Strip from the seed:

- Refunders and chargeback customers
- Serial returners
- Discount-only buyers (never purchased at full price)
- Employees (by company domain or an internal list)
- Wholesale / reseller accounts
- Anyone on the do-not-contact, opt-out, or deletion list (enforced in the warehouse, before any sync)

Keep existing customers **in** the seed - they are the signal - but suppress them from the acquisition campaign at delivery level with a separate exclusion audience. Excluding past customers from the seed itself removes exactly the people the model should learn from.

## Value-based seeds

A value-based seed adds a per-row value the platform weights the model on. Rules:

- **Feed margin or predicted LTV, never cumulative lifetime revenue** - cumulative revenue tracks tenure, and high-revenue low-margin customers poison the model.
- Positive values only. Zero and negative values break or distort the build.
- Values must not be all identical - identical values carry no ranking signal.
- One currency per list. Platforms normalize scale internally but not mixed currencies.
- Cap or winsorize whales so a handful of outliers doesn't dominate the weighting.
- Exclude refunded amounts from the value computation.
- **Confirm the value column mapped at upload.** An unmapped column is a silent failure: the platform builds a standard lookalike and nothing warns you. If the value-based option is absent at audience-build time, the mapping failed (documented by MHI Growth Engine and LeadEnforce as the most common value-based mistakes, alongside confusing order count with value).
- Meta's stated requirements: minimum 100 matched, aim 1,000+. Value-based audiences need a separate terms-of-service acceptance.

## Non-purchase seed sources - ranked by efficiency

When purchase data is too thin to clear a floor at acceptable quality, pick from these eight. Rows are ordered by **efficiency** - signal quality bought per unit of setup effort - not by the sourced practitioner value ranking, which stays visible as `V1`-`V8` because it is the sourced artifact and effort runs almost exactly backwards to it.

| Source                                                                                                                                | Value                                     | Effort                                                                                                                                                          | Consent exposure                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Purchasers                                                                                                                            | V1 - best per-row signal by a wide margin | An hour **when the customer export already exists**, the usual case; a data project when it doesn't - warehouse export, identity-resolution join, normalization | Full: lawful basis, suppression, platform list terms                                                        |
| High-intent page viewers (pricing, demo)                                                                                              | V3                                        | Near-zero if the pixel already fires; about an hour with one judgment call to agree which pages count as intent                                                 | None new when built platform-native; full gate if exported to a list                                        |
| Lead-form submitters - submitters, never openers                                                                                      | V4                                        | Near-zero on a platform-native form; about an hour on an owned form the pixel tracks                                                                            | None new when platform-native                                                                               |
| Checkout / add-to-cart initiators                                                                                                     | V2                                        | An hour if commerce events are instrumented and trusted; a tracking project rather than a seed choice if they aren't                                            | None new when platform-native                                                                               |
| Email clickers - never openers; Apple Mail Privacy Protection (2021) inflated opens into an unusable signal                           | V5                                        | About an hour: ESP export, click segment, dedupe against the warehouse                                                                                          | Re-enters the full gate, and ESP consent scope rarely covers ad-platform upload - check it, never assume it |
| Video viewers, by completion: 95% > 75% > 50% > 25% > 3-second. 75% is the named inflection point - below it intent drops off sharply | V6                                        | Minutes, inside the ad account, off signal the platform already holds                                                                                           | None - nothing leaves the platform                                                                          |
| Page/profile engagers                                                                                                                 | V7                                        | Minutes, same                                                                                                                                                   | None                                                                                                        |
| All site visitors                                                                                                                     | V8                                        | Minutes                                                                                                                                                         | None                                                                                                        |

Purchasers keep the top slot in the common case: a large value gap for one query against a table someone maintains anyway. Where the export genuinely doesn't exist, high-intent page viewers and lead-form submitters are the best ratio on the board - near-zero setup, no upload, no new consent exposure, and still in the top half on value. Below lead-form submitters, per-row quality falls off faster than effort does, so stop letting effort pull the choice down: a cheap seed that teaches the model the wrong customer costs more than the hour it saved.

Platform-native engagement audiences are also durable against mobile-OS tracking loss, because the signal originates inside the platform, with retention windows up to 365 days. In B2B, an SQL-only seed beats an all-MQL seed at every rung.

Re-rank before recommending:

- A warehouse with identity resolution already built, or a data team that owns the customer export on a schedule, drops the purchaser row's effort to near-zero and widens its lead.
- No pixel and no commerce events removes the middle rows from the board.
- An unresolved consent basis leaves only the zero-exposure rows available at any effort.
- A hard launch date promotes every minutes-not-weeks row.
- A compounding-asset mandate promotes the purchaser row even when its export has to be built.

## B2B specifics

- **Seed from closed-won CRM opportunities**, not MQL exports. Practitioner note: most B2B teams find 300-1,000 closed-won records sufficient for initial testing.
- **The identity problem**: work emails match under ~5% natively on consumer platforms, and personal emails match poorly on LinkedIn. Identity enrichment (resolving work identities to personal identifiers, or the reverse) is the documented workaround - it turns rung 1 of the fallback ladder into the standard B2B move.
- **Documented case**: a tight 200-account, ~600-contact ABM list matched ~180 people natively on LinkedIn and never activated below the 300 floor. Enrichment to 70-90% match made a 400-500 contact list viable.
- **Account-level vs contact-level**: expand a company list into contacts using job title + seniority + function filters before upload. LinkedIn: company list 1,000+ companies recommended, contact list roughly 10,000+ emails uploaded to reliably clear 300 matched.
- **Segment mixed account lists** into homogeneous bands (enterprise / mid-market / SMB) - left as one audience, delivery over-serves the largest companies in the list.
- Firmographic/technographic sources (industry, headcount, revenue, installed technology) can define the account list that becomes the seed, but the seed itself should still be selected on won revenue, not on fitting the ICP on paper.

## Splitting the seed

Each split becomes its own seed and its own lookalike. Split in this order - `country > product line > high-AOV vs. all > language/region`:

- **Country** - not really a choice: lookalikes are country-scoped, so a single global seed doesn't produce a worse lookalike so much as an averaged one that serves no market. Do it before considering any other split.
- **Product line or SKU category with different buyers** - the split that changes what the model learns most, so the highest-value optional one.
- **High-AOV vs. all customers** - a test rather than a decision. Its value is one comparison, so run it only once the two above are settled, then keep the winner.
- **Language/region** - usually correlates with country and adds the least new information.

Effort doesn't rank this list: every split is one more WHERE clause. What ranks it is the standing cost, which is identical per split and permanent - one more audience to refresh on cadence, monitor for overlap, and hold above its floor forever, plus one more chance of silently falling under it.

Two splits is fine. Six is a part-time job nobody was assigned. Cap the count at what the named refresh owner can maintain, and check each split's own effective seed against the floor **before** committing, not after.

The test for splitting: would a single model trained on the combined list be learning two different customers? If yes, split. Homogeneity matters more than size, so splitting trades size for homogeneity, usually the right trade above the floor.

Re-rank against the user: an automated warehouse sync collapses every split's standing cost to near-zero and makes more splits affordable, while a manual CSV process makes the third split cost as much attention as the first two combined.
