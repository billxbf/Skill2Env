# Sizing a developer segment

Contents: what each source measures · misreadings to refuse · the estimate shape · cheap tests for a hypothesis segment.

No public source gives a clean population per segment. Every size is an assembled estimate, and its credibility comes from stating the method rather than from the number looking precise.

## What each source measures

| Source class                             | Named examples                                                                                                                                                                                                              | Measures                                                                              | Safe to claim                                                                                                        | Not safe to claim                                                                                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Independent developer-population surveys | SlashData / Developer Nation (30,000+ developers, 165+ countries per wave; sector and language-community sizing reports)                                                                                                    | survey-modelled population per language, sector and role                              | order of magnitude per ecosystem or sector                                                                           | precise counts, or counts for a niche the survey never sampled                                                                                        |
| Practitioner surveys                     | Stack Overflow Developer Survey (2025 wave: 49,000+ responses, 177 countries; splits professional developers from people learning to code; role mix runs roughly full-stack 27%, back-end 14%, students 11%, architects 6%) | proportions inside a self-selected respondent pool                                    | relative mix, direction of change year to year                                                                       | absolute population; the sample skews to English-speaking, survey-answering developers                                                                |
| Language-activity rankings               | RedMonk (public GitHub pull requests × Stack Overflow activity)                                                                                                                                                             | correlation of code activity and discussion, aimed at spotting future adoption trends | tiers and direction of travel between languages                                                                      | population or market share - the publisher states the tier matters more than the rank, and that Stack Overflow's decline distorts the discussion axis |
| Forge-platform reports                   | GitHub Octoverse                                                                                                                                                                                                            | accounts, repositories, pull requests, language activity                              | platform-level growth and language trends                                                                            | one account = one professional developer; bots, duplicates and dormant accounts inflate every count                                                   |
| Package and image registries             | language registries, container registries, extension marketplaces                                                                                                                                                           | downloads and fetches                                                                 | rough adoption trend for one library                                                                                 | human users; CI re-downloads dominate most download graphs                                                                                            |
| Artifact and connector hubs              | model/dataset hubs (Hugging Face, Kaggle), connector and plugin directories (Airbyte, dbt Package Hub, Terraform Registry, Ansible Galaxy, Grafana, Semgrep, Zapier, n8n, Slack)                                            | published artifact counts, per-artifact downloads, likes and installs                 | the shape of a practitioner niche - which tasks, formats, base models or host stacks the segment actually works with | segment population; the counts are requests and listings, not people, and a handful of artifacts carry almost all of the volume                       |
| Job-market data                          | postings mentioning a technology                                                                                                                                                                                            | employer demand                                                                       | professional-developer demand in a region                                                                            | hobbyist or OSS population, which postings never see                                                                                                  |
| First-party data                         | signups, telemetry, docs analytics, support tickets, sales notes                                                                                                                                                            | your own funnel                                                                       | segment shares of your current users - the highest-quality evidence you hold                                         | anything about developers who never arrived                                                                                                           |

## Four misreadings to refuse

1. **Ranking as population.** Rank 12 does not mean twelfth-largest community; activity proxies carry known platform bias.
2. **Your users as the market.** First-party data is survivorship-shaped. Sizing an unserved segment from it returns "small" by construction, which is how promising segments get killed.
3. **A single round number.** "There are 4 million Rust developers" without source, date and method survives one skeptical question.
4. **A hub's catalogue size as a market.** Artifact counts are publishing activity, and publishing on these hubs is free and unreviewed. The operator of one ML hub reported in August 2026 that 85.6% of its models had fewer than 200 lifetime downloads and that 1.5% of repositories accounted for 99.2% of all downloads. So "millions of models exist" and "millions of models are used" are different claims by roughly two orders of magnitude.

## The estimate shape

```
<segment>: ~<low>–<high> developers
  method:     <source> filtered by <criteria>, cross-checked against <second source>
  as of:      <date>
  confidence: measured | estimated | inferred
```

- **measured** - counted in your own systems.
- **estimated** - public research applied to your filter, with the filter written down.
- **inferred** - analogy or expert judgement; no data. Legitimate, as long as it is labelled and paired with the lookup that would upgrade it.

Cross-check every estimate against one independent source of a different class. Two sources of the same class agreeing usually means they share an upstream dataset.

## Cheap tests for a hypothesis segment

A segment below the evidence floor (5-10 independent data points from a consistent group) needs a test that costs days, not a quarter:

- Ten support tickets or community threads read end to end, tagged for the hypothesised trait.
- Five conversations with people who match the profile, recruited from existing users or a public community.
- One landing page or docs page written for the segment's own words, measured on whether the right people arrive and act.
- One targeted content piece published where the segment gathers, measured on qualified replies rather than views.
- A telemetry cut on a trait already collected - runtime version, deployment shape, region - checking whether behaviour actually diverges.

Each test should be able to _fail_. Write the result that would make you drop the segment before running it.
