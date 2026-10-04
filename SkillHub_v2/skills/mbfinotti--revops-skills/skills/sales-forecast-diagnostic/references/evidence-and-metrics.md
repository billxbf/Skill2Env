# Error metrics, calibration, and evidence discipline

Read this before quantifying a miss or quoting any number to stakeholders. The forecast-accuracy literature is dominated by vendors selling forecasting software; their mechanics are reliable, their statistics are marketing.

## Choosing the error metric

- Always compute two numbers per level per period: **signed error** (bias - are we consistently high or low?) and **absolute error** (magnitude). A symmetric average alone lets a rep who over-calls and a rep who under-calls cancel to a healthy-looking zero. These two are not competing options to be ranked and chosen between - neither is readable without the other, so both ship every time.
- Fix one denominator before reporting anything. The same quarter - forecast $10M, closed $9.5M - can be presented as "95% accuracy" (actual/forecast) or a "5.3% error rate" (miss/actual): both are defensible alone, but mixing them across periods or teams makes trends meaningless. Pick one definition, write it in the report, and keep it.
- When deal sizes vary widely, weight the error by dollars (a WMAPE-style sum of absolute errors over sum of actuals) rather than averaging per-deal percentages - small deals otherwise dominate the number while the money is elsewhere.
- Benchmark against the team's own trailing periods, not published tables. Industry MAPE bands come from supply-chain forecasting and do not transfer to sales pipelines.

## Rep and manager calibration scorecard

Per person, trailing 4+ periods, compared to their own history first and the team second. Compute every row rather than picking among them: each exposes a different bias and they are all one query against the same history, so there is nothing to rank.

| Metric                                                                   | What it exposes                                                                          |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Commit conversion rate (won-as-called / committed)                       | Inflation when chronically low; sandbagging when chronically near-perfect with big beats |
| Share of wins from outside the forecast                                  | Hidden pipeline - the sandbagging signature                                              |
| Average close-date push count on their deals                             | Date discipline                                                                          |
| Category-change latency (evidence event to category update)              | Whether the record tracks reality or the calendar                                        |
| Signed forecast error, per period                                        | Direction and consistency of personal bias                                               |
| (Managers) override delta vs. rep sum, and override accuracy vs. raw sum | Whether the override adds judgment or bias                                               |

One outlier period is noise. Industry lore - a Forrester line that circulates only as a vendor-blog quotation, with no primary attached - puts the sandbagger bar at the same person doing it more than twice. Treat that as directional support for "require a repeated pattern," not as a citable standard.

## Which circulating statistics are safe to repeat

Almost none as benchmarks. Status of the ones most likely to come up:

| Claim                                                                                                                                         | Status                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "93% of sales leaders can't forecast within 5%" / "only 18% of firms within 5%"                                                               | Vendor-repeated from an unnamed 2021 survey, with no primary attribution. Do not cite.                                                                                                                                         |
| MEDDPICC teams forecast within 10%, +18% win rates, faster cycles                                                                             | Vendor-blog cluster, no primary study anywhere in the chain. Do not cite.                                                                                                                                                      |
| "Happy ears causes 40-60% slip rates"                                                                                                         | Vendor glossary, no methodology. Do not cite.                                                                                                                                                                                  |
| 3x pipeline coverage (SMB 2.5-3x, enterprise 4-5x variants)                                                                                   | Folklore with a disputed origin story; the granular variants trace to an aggregator citing an unnamed dataset. The underlying arithmetic - coverage ≈ 1 / win rate - is sound; derive the target from the team's own win rate. |
| Default stage probabilities (80/60/40/20...)                                                                                                  | Tool conventions, not measurements. Replace with the team's own conversion by stage before trusting any weighted forecast.                                                                                                     |
| Forecast-category conversion odds (pipeline ~25%, best case ~a third to half)                                                                 | Practitioner rules of thumb repeated by consultants, not published by any platform. Directional at best.                                                                                                                       |
| Vendor slip-rate findings (most teams see >10% of committed deals slip; committed-deal conversion ranging roughly 60-80% by performance tier) | One vendor's own analysis of its customer base, methodology and sample undisclosed. Cite only with that caveat, never as an industry benchmark.                                                                                |
| "Nobody has a 100% conversion rate on committed deals"                                                                                        | Qualitative, safe, and useful: a commit list converting at 100% is itself a sandbagging signal, not excellence.                                                                                                                |

Standing rule: derive every threshold from the organization's own history; when a circulated number must be mentioned, label its provenance in the deliverable rather than dropping it into a slide as fact.

## Frameworks usable as evidence checklists

Three inspection practices, competing for the same review hours. Recommend one; the reader cannot run all three at once.

- value (most first): `qualification-framework scoring > early-quarter champion verification > buyer-side progress question`
- effort (most first): `qualification-framework scoring > early-quarter champion verification > buyer-side progress question`
- efficiency (best first): `buyer-side progress question > early-quarter champion verification > qualification-framework scoring`

Start at the buyer-side progress question: near-zero effort, one sentence added to a review that already happens, and it unwinds most stage inflation on its own. Move up to early-quarter champion verification when the miss came from deals that were never real rather than deals that slipped - it costs a leader an hour per rep at period start and buys the whole period to act.

The full framework rollout is starved by that order and stays starved: highest value, a quarter to embed, cross-team. It is the right call only when reps genuinely disagree about what qualified means, which is a methodology finding at this skill's scope boundary, not a fix it ships.

- **Buyer-side progress as the unit of evidence**: recurring practitioner principle - real progress is something the buyer did, not something the seller did. It is the single question that unwinds most stage inflation, and it costs one sentence in a review that already happens.
- **Early-quarter champion verification** (associated with John McMahon's writing on sales leadership, via published summaries): have leaders directly verify the champions of forecasted deals in the first weeks of the period, and push unqualified deals off the forecast early rather than letting them sit uninspected until they miss. A practical inspection habit; adopt the practice without attaching numbers to it. An hour per rep at period start, and it buys the rest of the period to act.
- **MEDDICC / MEDDPICC** (or whatever qualification framework the team already runs): legitimate, widely used structures for scoring deal evidence element by element. The diagnostic value is the evidence standard, not the acronym - score against buyer-confirmed facts, and remember a filled CRM field is not evidence: "unknown" counts as complete in any system that only checks non-blank. The accuracy statistics vendors attach to these frameworks are the unsourced claims flagged above, and it takes a quarter to embed across a team, which is why the order above puts it last despite ranking first on value.
