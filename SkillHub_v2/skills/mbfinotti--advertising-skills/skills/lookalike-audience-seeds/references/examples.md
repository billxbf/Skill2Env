# Worked Seed Specifications

Two worked examples: a B2C value-based seed that clears its floor directly, and a B2B closed-won seed that fails the floor and takes the fallback ladder. Numbers are illustrative of the method. The platform floors and match ranges they use are the documented ones.

## Example 1 - B2C ecommerce, value-based seed (clears the floor)

Context from the interview:

- Skincare brand, ~48,000 lifetime customers in the warehouse.
- Identifiers: email, phone, name, postal on ~70% of rows.
- Value column: margin, computed by finance.
- EEA customers present. Consent for ad-platform matching is captured at checkout, and opt-outs sync nightly to the warehouse.

Destination: a value-based audience on a large social platform. Goal: new-customer CPA under $34, with acquired-customer 90-day LTV at or above the account average of $61.

Selection:

- RFM Champions + Loyal, 180-day window (buyers are pixel-tracked), margin as the value column.
- Negative-selection pass applied: 2,100 rows removed (refunders, chargebacks, discount-code-only buyers, staff domains, two wholesale accounts). Result: 7,400 rows.
- Expected match: 60% - platform's good-list band is 50-80%, list is fresh and multi-identifier, so mid-band.
- Effective seed: 7,400 x 0.60 = ~4,440 matched, clears the 100 floor and sits inside the 1,000-5,000 recommended band.
- US-only campaign, so no country split needed.

```
SEED SPECIFICATION - champions-loyal-margin v1, 2026-08-20
platform        : social (value-based customer list) | audience type: value-based
definition      : identity-resolved customers, RFM Champions+Loyal, last purchase <= 180 days
value column    : contribution margin (USD, finance-owned, refunds excluded) | mapping confirmed: at upload
row count       : 7,400 | identifiers/row: email, phone (E.164 digits), first/last name, zip
expected match  : 60% (platform good-list band 50-80%; fresh multi-identifier list)
effective seed  : 7,400 x 0.60 = ~4,440 matched vs floor 100 -> clears (within 1,000-5,000 recommended)
fallback used   : none
exclusions      : refunders, chargebacks, discount-only, employees, wholesale stripped from seed;
                  all-customers suppression audience excluded at delivery level
consent basis   : checkout consent for ad matching; opt-outs/deletions enforced in warehouse nightly (2026-08-19)
refresh         : bi-weekly via warehouse sync | owner: lifecycle marketing lead
measurement     : new-customer CPA <= $34; cohort LTV at 90/180/365d by seed version vs $61 account avg
re-check        : 2026-11-20 (90-day cohort checkpoint; learning phase respected before any early read)
```

## Example 2 - B2B closed-won seed (fails the floor, takes the fallback ladder)

Context: infrastructure-software vendor, 410 closed-won customers, average contract $38K, CRM has work emails only for most contacts. Destination: predictive audience on the professional network (300 matched floor). An earlier attempt uploaded the raw list and the audience never served - the team read 410 rows as a 410 seed.

First computation: 410 contacts, work emails on the professional network match at ~30-40%, so take 35%. Effective seed: 410 x 0.35 = ~144 matched. **Fails the 300 floor.**

The spec does not get loosened to "all opportunities including lost" - that is trading selection quality, which the ladder forbids as a first move.

Fallback ladder. Rung 1 leads here despite being the most expensive rung in effort: a vendor, a DPA, and counsel sign-off, so a week or more of coordination.

This is the case where the cheap rungs are structurally empty, which the ladder's efficiency default calls out. The list is already all-time closed-won, so there is no recency left to widen - rung 2 costs an afternoon and returns nothing. The only adjacent segments are lost deals or MQLs, which the selection-quality rule forbids as a first move.

On a B2C list with 48,000 candidates the order would have been the opposite: rung 2 first, and procurement probably never started.

1. **Enrich identifiers** (rung 1): identity enrichment appends personal emails and phones, and fills missing contacts on won accounts via title/seniority/function expansion - 410 accounts become 1,240 contacts at a projected 70% match. Effective seed: ~868 matched. Clears 300. **Stop here** - rung 1 resolved it. Rungs 2-4 stay unused.
2. (Not needed, and empty here) Widen recency one notch - the seed is already all-time, so there are no older closed-won deals to add.
3. (Not needed) Stack an adjacent segment - late-stage open opportunities of the same segment.
4. (Not needed) Switch to a non-purchase source - SQL-only demo requesters, never all-MQL.

```
SEED SPECIFICATION - closed-won-enriched v2, 2026-08-22
platform        : professional network (contact list -> predictive audience) | audience type: predictive
definition      : contacts on closed-won accounts (all-time), expanded by title/seniority/function,
                  enriched with personal identifiers
value column    : none (flat seed; ACV band is homogeneous by selection)
row count       : 1,240 | identifiers/row: work email, personal email (enriched), phone
expected match  : 70% (enrichment vendor's projected band; native work-email match was ~35%)
effective seed  : 1,240 x 0.70 = ~868 matched vs floor 300 -> clears
fallback used   : ladder rung 1 (identifier enrichment + account-to-contact expansion);
                  selection quality unchanged - still closed-won only
exclusions      : churned-with-refund accounts, partner/reseller accounts, employees;
                  current-customer domains excluded at delivery level
consent basis   : legitimate-interest assessment on file per counsel; enrichment vendor DPA signed;
                  opt-outs enforced in CRM export job - counsel sign-off dated 2026-08-15
refresh         : monthly manual export until warehouse sync ships | owner: revops manager
measurement     : cost per SQL from the audience; pipeline created; cohort read only at sales-cycle
                  maturity (~2 quarters) - early reads limited to match quality and engagement
re-check        : 2026-09-22 (30-day match/engagement check; cohort verdict deferred to maturity)
```

The contrast to carry over: Example 1's constraint was selection discipline (48,000 candidates, pick ~7,400). Example 2's constraint was the floor (410 candidates, reach 300 matched without diluting to lost deals or MQLs). Same arithmetic, opposite binding constraint - which is the B2C/B2B split in practice.
