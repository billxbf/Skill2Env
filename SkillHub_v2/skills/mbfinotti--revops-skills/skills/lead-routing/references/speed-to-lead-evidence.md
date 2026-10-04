# Speed-to-lead and matching evidence

Read this before quoting any number to stakeholders. The routing literature is dominated by vendors selling routing, matching and scheduling software. Their descriptions of mechanics are reliable. Their statistics and return-on-investment claims are marketing.

## The two studies behind almost every quoted figure

**Lead Response Management Study (Oldroyd, MIT / InsideSales.com, 2007).**

- **Exact finding:** the odds of contacting a lead called in 5 minutes versus 30 minutes drop 100 times; the odds of qualifying a lead called in 5 minutes versus 30 minutes drop 21 times.
- **Sample:** 6 companies, 2004-2007, over 15,000 leads and 100,000 dials.
- **Scope:** the study explicitly did not address close ratios.
- **Credibility:** vendor-academic, robust for its scope, phone-centric and now dated.

**"The Short Life of Online Sales Leads" (Oldroyd, McElheran & Elkington, Harvard Business Review, March 2011).**

Audit of 2,241 US companies, response-time distribution:

- 37% responded within an hour
- 16% within one to 24 hours
- 24% took more than 24 hours
- 23% never responded

- **Average response time:** 42 hours, among companies responding within 30 days.
- **Qualification odds:** firms contacting within an hour were nearly seven times as likely to qualify the lead as those waiting one more hour, and more than 60 times as likely as those waiting 24+ hours.
- **Additional dataset:** a separate dataset in the same work covered 1.25M leads across 29 B2C and 13 B2B US companies.
- **Credibility:** the strongest source in the domain, and still a behavioural audit, not a controlled experiment.

- **2007 study:** the "5-minute", "21x" and "100x" figures.
- **2011 audit:** the "7x", "60x" and "42 hours" figures.

They are routinely mixed up and attributed to each other. Neither observed a routing-stage timestamp. No public study has. They are evidence that response speed matters, not evidence that a routing change produces a given revenue multiple.

## Other response-time benchmarks

| Finding                                                                                                          | Source                                                  | Year       | Sample                                        | Credibility                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Median first phone response 3h08m; mean ~61 hours; 47% (4,472 of 9,538) never responded                          | InsideSales / XANT Lead Response Report                 | 2014       | 9,538 companies, secret-shopper method        | Vendor, but a large retrievable sample; among the most robust available                                                                  |
| 7% respond within 5 minutes; 55% not within 5 business days; ~42-hour average                                    | Drift lead-response audit                               | ~2017-2019 | 433 B2B companies                             | Vendor; sound real-form audit method, but the primary URL is offline and the study is routinely confused with a separate consumer survey |
| 63.5% never responded (365 of 1,000); average response among responders ~29 hours                                | RevenueHero                                             | 2024       | 1,000 B2B SaaS companies, mystery-shopped     | Vendor; transparent methodology; convenience sample, not randomized                                                                      |
| 74% miss the 5-minute window; teams with an SLA respond within 15 minutes 54.9% of the time versus 29.5% without | Blazeo Speed-to-Lead Benchmark Report                   | 2026       | 573 service-sector companies                  | Vendor; self-reported survey, so subject to self-reporting bias; service sector, do not generalize to software                           |
| 47-hour average; 23% within 5 minutes; 8x speed via AI routing                                                   | Optifai Pipeline Study                                  | 2026       | Claimed 939 B2B SaaS companies                | Vendor marketing with no published methodology and the same sample tag reused across unrelated pages; omit or flag strongly              |
| 84% of customers say the experience a company provides matters as much as its products                           | Salesforce State of the Connected Customer, 3rd edition | 2019       | 8,022 respondents, 16 countries, double-blind | Reputable large survey; the specific per-minute restatements circulating come from aggregators, not the primary report                   |

Two figures worth naming so they are not repeated uncritically:

- "78% of customers buy from the first company that responds" circulates through aggregators with no retrievable primary methodology. Treat as directional at best.
- The "391% conversion lift from responding within one minute" comes from a Velocify white paper analysing roughly 3.5 million leads around 2013, is mortgage and insurance skewed, and the original source link has rotted.

## Matching and distribution benchmarks

- Email-domain matching alone catches roughly 70% of lead-to-account matches, with fuzzy company-name matching adding another 15-20%. Vendor-adjacent estimate; use it to size effort, not to set a target.
- Vendors claim 95%+ match rates with fuzzy matching. Treat as marketing. What matters operationally is that the gap between 80% and 95% maps directly to leads misrouted or lost, which is why a match-rate floor belongs in the pass thresholds.
- One vendor case study reports a 74% improvement in match accuracy after adopting fuzzy matching. Single-customer, vendor-published, unverifiable.
- Only around 43% of B2B teams have any formal marketing-to-sales service-level agreement, per a vendor citing unnamed research. Directional only; no primary methodology is retrievable.
- No analyst-grade, industry-wide misrouting-rate benchmark exists. This is a genuine data gap, not something to fill with a vendor estimate. Measure the organization's own rate instead.

## How to use this with stakeholders

Set the response SLA from the organization's own conversion-by-response-time history whenever enough data exists - a single quarter of leads bucketed by time-to-first-touch beats any published benchmark, because it reflects the actual product, price point and buyer. Use the published research only to justify why speed is worth instrumenting at all.

Vendor benchmark URLs rot quickly, so record, at the moment of use:

- the figure
- the source
- the year
- the sample

A statistic without a retrievable primary methodology is directional, and should be labelled that way in the deliverable rather than dropped into a slide as fact.
