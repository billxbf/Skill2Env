# The per-tier coverage matrix

The concrete SLA set to encode in the CRM and marketing-automation platform per tier. Adapt the rows to the user's motion; the discipline is that every row differs visibly across the columns - a matrix whose columns read the same is labeling, not tiering.

| Dimension         | Tier 1 / Strategic (1:1)                                                   | Tier 2 / Targeted (1:few)                                    | Tier 3 / Programmatic (1:many)                                  |
| ----------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| Personalization   | Bespoke: custom value proposition, account-specific content and benchmarks | Segment/persona-led, semi-custom by industry or cluster      | Automated, role/segment-level, intent-triggered                 |
| Human involvement | Dedicated AE + SDR + SE, executive sponsor                                 | Shared AE coverage, SDR-supported                            | SDR-led or fully automated; pooled CS                           |
| Channel mix       | Executive roundtables, direct mail, custom demos, in-person reviews        | Vertical campaigns, targeted outbound, digital-first reviews | Email nurture, retargeting, content syndication, in-app         |
| Review cadence    | Quarterly QBRs with the customer's executive sponsor present               | Semi-annual reviews or detailed digital recaps               | Automated quarterly value summaries; live touch on trigger only |
| Executive sponsor | Formal program                                                             | By exception                                                 | None                                                            |
| Marketing motion  | Multi-quarter account plans (3-9 month horizons)                           | Grouped campaigns by trigger or industry                     | Always-on programmatic, intent-prioritized                      |

Role-allocation note (practitioner guidance):

- AEs belong in Tier 1 and Tier 2 coverage alongside ABM/SDR functions.
- Tier 3 runs on ABM and SDR alone, without AE hours.

## QBR economics

A Tier-1 QBR costs roughly 3-6 hours of preparation, which is why cadence must be tier-differentiated: running true QBRs for every account "produces shallow QBRs for everyone" (the consistent CS-practitioner position). Quarterly for strategic accounts, semi-annual or automated below.

## Executive sponsorship, concretely

The public reference implementation is GitLab's program: each executive sponsor caps at 4 accounts, selected annually, with a one-year commitment, governed at CRO/CEO level. The load-bearing parts are the cap, the fixed term, and the named governance - an uncapped, open-ended "execs will help on big deals" arrangement is not a program and decays within two quarters.

## When citing figures from this matrix

Present every number in the charter with its confidence grade; never let a directional figure or a vendor claim wear the weight of verified fact.

**Mark as sourced** figures that originate in research studies or practitioner frameworks: the 1,500 selling-hours-per-year anchor, the ACV-to-capacity tiers, the 6-10-person buying-committee size, the "20-50 named accounts" rule of thumb from the field.

**Mark as rule-of-thumb** per-rep tier caps (~5-25 for Tier 1, ~25-60 for Tier 2), CS ratios (1:5-15 / 1:20-75 / 1:100+), and the ~20%/quarter list-churn guidance; these are practitioner consensus but not measured benchmarks audited across a cohort.

**Mark as vendor claims** figures like "tiered accounts are 2.3x more likely to hit targets" or "ABM delivers 208% higher ROI" - if the user wants them in a business case, write "vendor X claims…" and keep the charter's own weight on the capacity math instead. Vendor numbers originate in marketing, not in measured results.

**Flag emerging practices** not yet assumed as baseline by this matrix: dynamic, signal-triggered tier moves in near-real-time rather than quarterly recalibration - worth mentioning to a tooling-rich user as a direction to explore, not a standard starting point.
