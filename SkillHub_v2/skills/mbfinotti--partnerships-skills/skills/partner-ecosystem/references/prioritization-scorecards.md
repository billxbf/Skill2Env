# Prioritization: Weighted Scorecard + 2×2

Two complementary tools. The scorecard produces defensible numbers; the 2×2 turns them into an investment conversation. This skill applies them to ecosystem _categories_ (segments of the map); ranking named candidate alliances belongs to `mbfinotti/partnerships-skills@alliance-prioritization`.

## The weighted scorecard

Score each category on a weighted combination of engagement, performance, and potential indicators. The composite drives attention and investment.

- **The load-bearing decision** is not which inputs to include but how heavily to weight leading indicators (engagement, enablement progress, joint activity) against lagging ones (revenue). The most-cited error is over-weighting lagging revenue and missing operational decay.
- **Segment weights by partner type - never one scorecard for all.** A referral band, a reseller band, an SI band, and an alliance band have different routes to revenue, cycle lengths, and influence. Define each category's _intended contribution_ before choosing its metrics: a mature reseller category carries heavier revenue/retention weighting; an emerging strategic category is judged on market development.
- **Reject the weak default** of scoring only sales volume, account size, and partner type - it says almost nothing about where to invest.
- **Validate the model**: compare its predictions against actual outcomes and adjust weights where it over- or under-predicted.

## The prioritization 2×2

Axes: **strategic fit × ease of execution** (equivalently, size of prize × ability to win). The partnerships-specific version is **Chris Lavoie's 2×2** (AfterShip, circulated through the ELG community):

|                         | High joint value                               | Weak joint value                                |
| ----------------------- | ---------------------------------------------- | ----------------------------------------------- |
| **High overlap / fit**  | **Holy grail** - priority investment           | **Uphill battle** - co-marketing only, early on |
| **Lower overlap today** | **Next best choice** - high-potential, nurture | **Low priority** - watch, wait                  |

Say the resulting order out loud instead of leaving it implied by grid position: `holy grail > next best choice > uphill battle > low priority`. That is already an efficiency ordering rather than a cost one: ease of execution _is_ the effort side of the ratio, which is why the category cheapest to run routinely is not the one to fund first.

The worked example below inverts in exactly that direction.

The ordering is a default, not a law. Re-rank it against what the map already knows about this company:

- An in-house capability the ease-of-execution axis assumed away (an integration team already shipping, a partner manager already hired) promotes a category by a full quadrant.
- A category whose fit rests on a whitespace nobody has staffing to enter belongs lower than its composite says.

Explicitly a **recurring exercise**: categories and partners move quadrants over time, so re-plot on the map's review cadence rather than treating a placement as permanent.

## Combining them

Use the scorecard to produce a composite score for _each axis_, then plot:

- **Strategic fit** = ICP overlap, joint value proposition strength, market alignment.
- **Ease of execution** = technical readiness, sales capacity, contracting friction, partner motivation - and your own capacity to support the category (staff, enablement, tooling).

Ease of execution cuts both ways: partners overwhelmingly select vendors on ease of doing business (a widely repeated ~80% figure, practitioner-circulated; treat as directional). Your own friction belongs in the assessment, not just theirs.

## Worked category example

A B2B SaaS map with four categories, composites on a 1-5 scale:

| Category                   | Strategic fit                                                         | Ease of execution                             | Quadrant         | Reading                                                          |
| -------------------------- | --------------------------------------------------------------------- | --------------------------------------------- | ---------------- | ---------------------------------------------------------------- |
| ISV / integration partners | 4.4 (heavy account overlap, integrations named in closed-won reviews) | 3.8 (API ready, no partner manager yet)       | Holy grail       | Invest first; the capacity gap (no owner) is the blocker to fix  |
| Referral / affiliate band  | 3.1 (ICP-adjacent audiences)                                          | 4.5 (cheap to run)                            | Next best choice | Run lean; do not confuse low cost with high priority             |
| Regional SIs               | 3.9 (enterprise segment uncovered - a mapped whitespace)              | 2.2 (no implementation docs, long enablement) | Uphill battle    | Quantified gap hands off to expansion planning; not this quarter |
| Marketplace listing        | 2.4 (buyers not procuring there yet)                                  | 3.5                                           | Low priority     | Watch; re-score when procurement behavior shifts                 |

Note what the example does. Each placement cites map evidence (overlap, closed-won review, whitespace), and each reading ends in a decision. The pass-threshold requirement, that the map inform at least one named decision, is satisfied inside the prioritization view itself.

Negative example to avoid: the same four categories ranked by last quarter's partner-sourced revenue alone would rank the referral band first and ISVs last, with lagging revenue inverting the strategic picture. That is the over-weighting error the scorecard exists to prevent.
