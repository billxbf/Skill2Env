# Media Map

Contents: outlet classes · dated examples · per-reporter verification · scoring rubric · a worked entry and its bad twin · the map artefact · the pitch tracker · maintenance.

## Table of Contents

- [Outlet classes](#outlet-classes)
- [Dated examples, not a send list](#dated-examples-not-a-send-list)
- [Per-reporter verification](#per-reporter-verification)
- [Scoring rubric](#scoring-rubric)
- [A worked entry and its bad twin](#a-worked-entry-and-its-bad-twin)
- [The map artefact](#the-map-artefact)
- [Tier 1](#tier-1)
- [Tier 2](#tier-2)
- [Do not pitch](#do-not-pitch)
- [The pitch tracker](#the-pitch-tracker)
- [Maintenance](#maintenance)

## Outlet classes

Build by class, then verify the humans inside it. Named lists rot within months; classes do not.

| Class                            | Trades in                                               | Wants from you                                                              | Realistic outcome                             |
| -------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------- |
| Developer-native trade press     | Architecture, languages, infrastructure, tooling shifts | A checkable technical claim, an engineer to interview, a working repository | A technical piece read by practitioners       |
| Enterprise-IT trade press        | Budgets, procurement, vendor moves, compliance          | Customer names, deployment scale, the buyer's problem                       | Credibility inside accounts                   |
| Business and startup press       | Funding, valuations, founders, market conflict          | A round, an unusual number, an exclusive                                    | Investor and candidate perception             |
| Practitioner newsletters         | One curator's judgement                                 | Something their readers can use this week                                   | High-intent clicks, small volume              |
| Community aggregators and forums | Peer verdict, not editorial                             | The artefact itself, posted by a participant                                | Adoption, and unfiltered criticism            |
| Analyst firms                    | Category framing and vendor comparison                  | A briefing, not a pitch                                                     | A correct mental model in buyer conversations |
| Podcasts, video, broadcast       | A person with a position                                | A guest who argues something, not a product tour                            | Durable, transcribed, citable material        |

Newsletters and community forums are routinely underrated for developer products: smaller audiences, but the readers are the adopters.

## Dated examples, not a send list

The publications that actually cover open-source launches, over and over: TechCrunch, The New Stack, The Register, TechTarget and SDxCentral, plus the Linux Foundation and CNCF newsrooms for foundation-backed announcements.

Use those as a calibration of what the classes above look like in practice - nothing more. They are a starting point for finding bylines, never a list to send to. Every name still has to pass the per-reporter verification below, and outlets fold, merge and reassign beats, so re-check the list itself before relying on it.

## Per-reporter verification

Every candidate needs all five before they enter the map:

- Last five bylines read, dated, and on this beat.
- Current employer confirmed on the outlet's own site.
- Stated pitch preferences noted, including any refusal of embargoes or pitches.
- Angle history noted - what they have already argued about this category, especially scepticism.
- A contact route that is real. Never guess an address into a send list; an unconfirmed contact is a blank field, not a hypothesis.

## Scoring rubric

Score each dimension 1-5, multiply, rank.

| Dimension      | Question                                                        | Weight |
| -------------- | --------------------------------------------------------------- | ------ |
| Beat match     | Do their recent bylines cover exactly this?                     | 3x     |
| Audience fit   | Does their readership contain the people who must believe this? | 2x     |
| Responsiveness | Do they engage publicly, answer sources, run reader tips?       | 2x     |
| Recency        | Have they touched this topic in the last quarter?               | 1x     |

Tiers:

- 30+ is tier 1 (bespoke pitch, eligible for exclusive or embargo).
- 18-29 is tier 2 (adapted pitch, after tier 1 answers).
- Below 18 is tier 3 (no pitch - they pick up from tier 1 or from your own post).

Audience fit outranks raw reach. A newsletter with four thousand platform engineers beats a general tech site with two million readers when the goal is adoption by platform engineers.

## A worked entry and its bad twin

The tempting shortcut is to rank by audience size and fill the contact column with whatever an address-guessing pattern produces. Both are illustrative entries; the reporter, outlet and dates are invented.

**Bad.**

| Reporter  | Outlet       | Beat evidence                         | Score | Contact                                     |
| --------- | ------------ | ------------------------------------- | ----- | ------------------------------------------- |
| A. Rivera | BigTechDaily | writes about tech, 4M monthly readers | 40    | a.rivera@bigtechdaily.com (guessed pattern) |

Everything wrong with it: "writes about tech" is not beat evidence, the score is reverse-engineered from reach, no byline was read, no employment check was done, and the address is a hypothesis dressed as a fact. A send to this row bounces or annoys, and either way it burns the outlet.

**Good.**

| Reporter  | Outlet       | Beat evidence (last 5 bylines)                                      | Score | Contact                  |
| --------- | ------------ | ------------------------------------------------------------------- | ----- | ------------------------ |
| A. Rivera | BigTechDaily | 1 of 5 on developer tooling (2026-03-02), rest on consumer hardware | 14    | verified via author page |

Same reporter, honest evidence, and the score drops them to tier 3 - no pitch. That is the map doing its job: it is as valuable for the sends it prevents as for the ones it produces.

## The map artefact

```markdown
# Media map - <product>, updated <date>

## Tier 1

| Reporter | Outlet   | Beat evidence (last 5 bylines)        | Score | Contact    | Last contact | Outcome                   | Notes                    |
| -------- | -------- | ------------------------------------- | ----- | ---------- | ------------ | ------------------------- | ------------------------ |
| <name>   | <outlet> | 3 of 5 on <topic>, most recent <date> | 34    | <verified> | 2026-08-14   | passed, asked for numbers | takes embargoes, no PDFs |

## Tier 2

…

## Do not pitch

| Reporter | Reason                 |
| -------- | ---------------------- |
| <name>   | bio states no pitches  |
| <name>   | left the outlet <date> |
```

Keep the "do not pitch" section. It stops the same wasted send being repeated by the next person or the next campaign.

## The pitch tracker

One row per send, kept next to the map:

| Date | Reporter | Angle | Subject line | Ask | Reply | Outcome |
| ---- | -------- | ----- | ------------ | --- | ----- | ------- |

After roughly thirty sends, read the tracker rather than general advice: which angle, which subject-line shape and which ask actually work for this company will be visible in it, and they differ by category.

## Maintenance

- Re-verify employers quarterly; reporters change outlets constantly and a dead contact silently reduces the map.
- Add every reporter who covers the category, even hostile ones - knowing who is sceptical is planning information.
- Record who honoured an embargo and who did not. That record is the only basis for offering the next one.
- Never merge this map with the practitioner reading list from a radar skill. One is who you pitch, the other is who you learn from, and conflating them produces pitches to people who never write about products.
