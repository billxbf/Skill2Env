# Worked examples

Two filled-in passes in the skill's output shape - one B2B lead gen, one e-commerce - followed by a negative example. Figures are illustrative. Always substitute the account's own numbers.

## Example 1 - B2B lead gen (project management software, $18k/month, target CPA $220, avg CPC $6)

High CPC → click gate tightened to 10-12. Lookback: 14 days, $8,400 analyzed.

### Summary

- Spend analyzed: $8,400 (14 days, non-brand campaigns)
- Wasted spend found: $1,270 on zero-conversion candidates (15.1% of analyzed spend)

### Additions

| Term                       | Match type | Level                       | Evidence                | Category           | Variants added                                                        |
| -------------------------- | ---------- | --------------------------- | ----------------------- | ------------------ | --------------------------------------------------------------------- |
| project manager jobs       | phrase     | account                     | 41 clicks, $246, 0 conv | job seeker         | project manager job, project management jobs, project manager careers |
| project manager salary     | phrase     | account                     | 28 clicks, $168, 0 conv | job seeker         | project manager salaries, project management salary                   |
| free project plan template | phrase     | shared list "DIY-free"      | 34 clicks, $204, 0 conv | DIY/free           | free project plan templates, free project planning template           |
| what is a gantt chart      | phrase     | shared list "informational" | 22 clicks, $132, 0 conv | informational      | what are gantt charts, gantt chart meaning                            |
| project management course  | phrase     | shared list "informational" | 19 clicks, $114, 0 conv | informational      | project management courses, project management training               |
| construction daily log app | exact      | campaign "Non-brand core"   | 11 clicks, $72, 0 conv  | wrong product tier | (none - surgical exact block)                                         |

Level choice follows the ranking: shared lists carry the two recurring themes (DIY/free, informational) because every future campaign inherits them by attachment. Job-seeker terms went to account level as universal disqualifiers - no campaign in this account ever wants them - and the single stray construction query stayed at campaign level, where a wrong call costs one container.

### Do-not-negate

- "project management software pricing" - 12 clicks, 0 conversions this window, but 3 conversions in the prior 90 days. Fails the overblocking review.
- Queries naming a rival product plus "alternative" - competitor-adjacent, and the account deliberately bids competitor comparisons. Strategy call: keep.

### Watchlist

- "project tracker excel" - 7 clicks, $44, 0 conv. Trips the 10-click gate at ~3 more clicks; likely DIY intent but too little data.
- "best project management tool" - 9 clicks, $61, 0 conv. Comparison intent; early-funnel, may assist later conversions. Re-check next pass.

### Next review

Weekly cadence - next pass in 7 days, 14-day lookback.

## Example 2 - e-commerce (running-gear store, $45k/month, target ROAS 400%, avg CPC $0.90)

Low CPC → standard 15-20 click gate. Conversion volume is high enough to gate on conversions directly. Lookback: 7 days, $10,900 analyzed.

### Summary

- Spend analyzed: $10,900 (7 days)
- Wasted spend found: $760 on zero-conversion candidates (7.0% of analyzed spend - near the 4-8% practical floor; be conservative)

### Additions

| Term                       | Match type | Level                       | Evidence               | Category                                          | Variants added                                    |
| -------------------------- | ---------- | --------------------------- | ---------------------- | ------------------------------------------------- | ------------------------------------------------- |
| used running shoes         | phrase     | account                     | 62 clicks, $56, 0 conv | wrong product tier                                | used running shoe, second hand running shoes      |
| running shoe repair        | phrase     | shared list "services"      | 38 clicks, $34, 0 conv | wrong product tier                                | running shoes repair, shoe repair running         |
| how to clean running shoes | phrase     | shared list "informational" | 44 clicks, $40, 0 conv | informational                                     | how to wash running shoes, cleaning running shoes |
| running shoes for toddlers | phrase     | campaign "Adult footwear"   | 29 clicks, $26, 0 conv | wrong product tier (catalog has no toddler sizes) | toddler running shoes, kids running shoes         |

### Do-not-negate

- "cheap running shoes" - 51 clicks and 4 conversions at target ROAS. "Cheap" is junk in many accounts but converts here (the store carries a budget line). Taxonomy signals are priors, not verdicts.

### Watchlist

- "trail running shoes review" - 12 clicks, $11, 0 conv. Comparison intent; below the click gate. Re-check next pass.

### Next review

Weekly cadence - next pass in 7 days.

## Negative example - what not to do

The request: "cut wasted spend, here's the report" on the B2B account above.

The bad pass:

- Added broad negative `free` account-wide → also blocks "risk-free project management software trial" and every query containing "free trial", which converted 9 times last quarter. No overblocking review was run. (Violates: the overblocking review, workflow step 5.)
- Added broad negative `free template` expecting it to also block "free" alone - it doesn't. A broad negative only blocks searches containing ALL its words, so single-word "free …" queries kept spending. The mechanics were assumed, not checked. (Violates: the match-type mechanics, Core mechanics.)
- Added `project management` as a phrase negative to kill informational queries → conflicts with the account's own core keywords. Negatives beat positives, so the main ad group silently stopped serving while showing "active". (Violates: the conflict check, workflow step 5.)
- Accepted the platform's default match type (exact) on 30 report additions → each blocked only its one literal query. Plural and reworded variants kept matching, and the next report looked identical. (Violates: the default-match-type check, Core mechanics.)
- Negated every term with a single click and no conversion → hundreds of exclusions on no statistical basis, reach collapse on an account whose true waste was ~7% of spend. (Violates: the negation gates, workflow step 3.)
