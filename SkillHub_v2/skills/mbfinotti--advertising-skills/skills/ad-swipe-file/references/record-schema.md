# Swipe-file record schema and classification taxonomies

Every entry carries the same fields, or entries cannot be compared, filtered, or counted. Consistency beats completeness on any single entry. Store the file in whatever the user already uses - a spreadsheet, a database, a notes tool - as long as every field below is filterable.

## Per-ad fields

**Provenance (observations - record exactly what was seen):**

| Field                      | Content                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| `capture_date`             | Date this entry was recorded                                                                    |
| `advertiser`               | Competitor name                                                                                 |
| `competitor_tier`          | direct / adjacent / aspirational                                                                |
| `channel`                  | The paid channel the ad runs on                                                                 |
| `placement`                | Feed, story/reel, search, in-stream, sponsored message - if visible                             |
| `source`                   | URL or description of where the ad was observed (transparency surface, user screenshot, export) |
| `first_seen` / `last_seen` | Run dates if the surface exposes them; otherwise `unknown`                                      |
| `geography`                | Country/region the ad was observed in or targeted at                                            |
| `message`                  | Paraphrase or one short attributed quote - never a full transcription                           |
| `landing_destination`      | Where the CTA goes; reveals the funnel behind the ad                                            |

**Classification (analyst judgment, applied consistently):**

| Axis              | Vocabulary                                                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `format`          | static, carousel, video, UGC-style, before/after, testimonial, catalog/product feed, motion graphic                                    |
| `hook_type`       | curiosity gap, bold claim, first-person confession, contrast/before-after, relatability/POV, question, countdown/gamified, proof-first |
| `offer_angle`     | The value prop or promotional mechanic being pushed, in a short phrase                                                                 |
| `concept`         | The overall creative idea, independent of format - the same before/after format can carry many concepts                                |
| `awareness_stage` | Eugene Schwartz's five levels: unaware, problem aware, solution aware, product aware, most aware                                       |
| `funnel_stage`    | TOFU / MOFU / BOFU                                                                                                                     |
| `persona`         | Who the ad appears to address (labelled inference)                                                                                     |

Optional further axes when the category rewards them, ordered by analytic payoff per tagging minute: `objection addressed > proof type > product feature`. Objection addressed feeds the gap analysis directly - it is the axis that surfaces what nobody in the category is saying. Product feature is last because it usually re-describes what `offer_angle` already carries.

**Judgment fields (always labelled as inference, never as fact):**

| Field               | Content                                                                          |
| ------------------- | -------------------------------------------------------------------------------- |
| `longevity_signal`  | e.g. "active 40+ days" plus the corroboration seen (variants, breadth, relaunch) |
| `variant_count`     | Distinct concepts vs cosmetic variations observed                                |
| `confidence`        | high / medium / low - how strongly the signals corroborate                       |
| `why_it_might_work` | One sentence, phrased as hypothesis, not verdict                                 |

**Pipeline field (mandatory - the column that makes the file a pipeline, not an archive):**

| Field         | Values                                                                        |
| ------------- | ----------------------------------------------------------------------------- |
| `test_status` | saved → hypothesized → briefed → testing → tested-won / tested-lost / dropped |

## Hard rules

- Never save an entry missing: advertiser + tier, format, offer/angle, a longevity estimate or `unknown`, a one-sentence note, and a test status.
- Mark unverifiable fields **unknown**: an unknown reduces evidence coverage. A guess poisons the file.
- **Cosmetic resizes and recrops are not distinct entries.** Deduplicate on concept, not on asset. Record the variation count on the concept's entry instead.
- Identical fields across every advertiser, so entries stay comparable side by side.
- Dated raw pulls live separately from this synthesized file and are never overwritten. The file cites which pull each entry came from.

## Worked example - one filled record

```
capture_date:        2026-08-24
advertiser:          FlowMetric (fictional)
competitor_tier:     direct
channel:             social feed video
placement:           feed + reels
source:              public ad transparency surface, EU view (link saved in raw pull 2026-08-24)
first_seen:          2026-07-02
last_seen:           still active
geography:           DE, FR, NL (EU view exposed 6 more markets)
message:             Paraphrase - "asks whether you still build reports by hand,
                     then shows a 15-second dashboard build". Quoted hook line:
                     "Still exporting to spreadsheets every Monday?"
landing_destination: /demo - a demo-request page, not the homepage
format:              video (UGC-style, talking head + screen capture)
hook_type:           question
offer_angle:         time saved on weekly reporting; free trial, no card
concept:             "Monday morning reporting pain" - day-in-the-life problem dramatization
awareness_stage:     problem aware
funnel_stage:        TOFU
persona:             inference - ops/analytics lead at a mid-size company
                     (EU targeting data showed job-function targeting, 200+ employees)
longevity_signal:    inference - active 53 days, 3 distinct hook variants of the same
                     concept, running in 9 markets; corroborated, likely performing
variant_count:       3 concept-level variants (question / bold-claim / proof-first hooks)
confidence:          high
why_it_might_work:   Hypothesis - question hook + problem dramatization meets a
                     problem-aware audience where our category ads all lead product-first
test_status:         hypothesized (feeds hypothesis H2, session 2026-08-24)
```

Note what the example does:

- Run dates and targeting fields are recorded as observations because an EU surface actually exposed them.
- Persona and "likely performing" are marked as inference with their reasoning shown.
- The message is a paraphrase plus one short quoted line, not a transcript.

## Organizing the file

Two-level structure, chosen before saving: split first by intent collection (pattern library / competitor pulse / vertical imports), then filter by any schema axis. Within the competitor pulse, keep one view per competitor and one cross-competitor view per classification axis - "all question hooks", "all BOFU offers" - so gaps become visible.
