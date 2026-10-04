# Effort tiering and benchmarks

## Tier definitions

Rows are in efficiency order - meetings booked per hour of research, the ratio the measurement section below actually tests. Best ratio first, not cheapest first.

- **Efficiency**: 1:few > 1:many > 1:1
- **Effort**: 1:1 > 1:few == 1:many
- **Value per prospect**: 1:1 > 1:few > 1:many

1:few and 1:many tie on effort because the expensive part of both is the same one-time segment pass. The deep tier is what this order starves: highest value per prospect, highest effort, so it never wins on ratio.

Promote it deliberately for:

- Named strategic accounts.
- Multi-stakeholder deals.
- A prospect a templated tier already failed on.

| Tier            | Fits when                                                          | Research time                                                                                                           | Buys you                                                                                            | What personalization looks like                                                                                                            |
| --------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1:few (default) | A segment of similar prospects (same role, stage, or trigger type) | A one-time pass of segment research, then ~2-3 minutes per prospect (Blount's cap) - near-zero next to the segment pass | Most of the reply lift of 1:1, spread across a whole segment                                        | One shared inference for the segment plus one per-prospect variable: their specific post, event, or role detail                            |
| 1:many          | Volume outbound, or B2C lifecycle at any scale                     | The same one-time pass, plus a standing job keeping trigger data live; no per-prospect research                         | Reach - reply rates near the template baseline, at any volume                                       | A "because statement" - one researched, pattern-based reason-for-contact for the whole list - or a behavioural trigger with dynamic fields |
| 1:1 deep-dive   | Named strategic accounts, high deal value, multi-stakeholder       | An hour per account, every account, capped deliberately                                                                 | The highest per-prospect reply and meeting rate, and the only tier that reaches a guarded executive | Individual-level signals, each verified at source; all five anatomy parts bespoke per person                                               |

The ranking is a default, not a law: re-rank it against the user's position.

- An already-licensed enrichment or intent platform makes 1:few cheaper still.
- A thirty-account named list makes 1:1 affordable.
- An SDR against a daily activity quota is capped at 1:many whatever the deal size suggests.

## When templating is the correct answer

Templating at 1:many is a decision, not a failure, when any of these hold:

- Deal or customer lifetime value is too low to repay per-prospect minutes.
- The segment is large and genuinely uniform - the same inference is true of everyone in it.
- A time-capped search (2-3 minutes) finds no fresh individual signal. Stop, drop the prospect to the templated tier, and move on.
- The motion is B2C lifecycle: the trigger and its timing carry the relevance; per-person research adds nothing a behavioural event has not already said.

Guiding rule, from 30 Minutes to President's Club: "Personalize the ones that matter. Template the rest."

## Scale mechanisms

- **Because statement** (Jeb Blount, Sales Gravy; with Chris Beall): build one sentence from a pattern researched across the list - "because [pattern true of this segment], I'm reaching out" - and reuse it. Pairs with Blount's 2-3 minute per-prospect research cap.
- **First is Best** (30MPC / Jason Bay): pre-rank the segment's likeliest trigger types by conversion likelihood, then use the first trigger research actually confirms for each prospect. Bounds research time and stops cherry-picking.
- **Pre-documented trigger stacks** (30MPC): with a segment's top company and person triggers written down in advance, a personalized email takes under 3 minutes.

## Benchmark attribution table

Every figure below needs its attribution carried with it when quoted to a user. "Vendor-published" means the publisher sells outreach or sales-engagement tooling and disclosed no independent audit or full methodology - trust the direction, never the magnitude.

| Claim                                                                                                                                                                   | Attribution                                                         | Confidence                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------ |
| Average rep sends ~344 cold emails per booked meeting                                                                                                                   | Gong, from its own platform data (28M+ emails, with Outbound Squad) | Vendor-published                                 |
| Personalization lifts replies 50-250% vs a template                                                                                                                     | Lavender, citing Salesloft data                                     | Vendor-published, quoted via another vendor      |
| Personalization can boost cold email replies by 5x                                                                                                                      | Gong data, as cited by 30MPC                                        | Vendor-published, cited by a practitioner outlet |
| Personalized email in under 3 minutes once triggers are pre-documented                                                                                                  | 30MPC (Armand Farrokh / Jason Bay)                                  | Practitioner guidance                            |
| Cap first-touch research at 2-3 minutes per prospect (CRM ~30s, profile ~45s, company site ~45s)                                                                        | Jeb Blount, Sales Gravy                                             | Practitioner guidance                            |
| 5x5x5: 5 min research + 5 min writing ≈ ~30 personalized emails/day                                                                                                     | Kyle Coleman's method, as published by Lavender                     | Vendor-published                                 |
| Personalizing the message body lifts replies 32.7%, a personalized subject line lifts them 30.5%                                                                        | Backlinko                                                           | Vendor-published                                 |
| Referencing a prospect's industry correlates with an 88% reply-rate increase; referencing recent activity correlates with ~3x more replies (30,000+ prospecting emails) | Gong Labs                                                           | Vendor-published                                 |

These more granular per-tactic lift figures sit well below the "5x" headline claim above - a reminder that vendor-published multipliers vary by an order of magnitude depending on what exactly was measured and against what baseline, which is itself evidence for trusting direction over magnitude. The minutes-per-tier figures in the tier table are a practitioner synthesis, not a measured standard - planning defaults to calibrate against your own results. Say so if a user asks for "the industry number". Every figure above measures the personalization _outcome_, never its time cost: none correlates research minutes spent per prospect against the resulting reply rate.

## Measuring whether the tiering paid off

- Compare reply rate and positive-reply rate of personalized sends against a control template on the same segment. The lift claims above are only credible for a user's own list when measured there.
- Track meeting-booked rate per hour of research, by tier. If 1:1 accounts book no more meetings per hour than 1:few, the deep tier is over-scoped.
- B2C: compare triggered-flow click and conversion against the generic blast baseline; watch unsubscribe and complaint rates as guardrails.
