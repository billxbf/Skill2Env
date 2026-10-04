# Where this skill's numbers come from

## Contents

- How to read this
- Sourced practices and figures
- Conventions borrowed from practitioner advice
- Baselines set by this skill
- About the worked examples

## How to read this

Every number below is one of three things, and the skill says which:

- **Sourced** - a named person or project states it, and the statement is quoted.
- **Convention** - practitioner advice that circulates widely rather than resting on a measurement.
- **Baseline** - set by this skill because the task needs a starting number. Adjust it for your slot, room and product; do not quote it to anyone as a standard.

Tell the user which kind a number is whenever they push back on one. A speaker who thinks "20 seconds" is an industry rule will defend it; a speaker who knows it is a starting point will tune it to their own talk, which is the point.

## Sourced practices and figures

| Claim in the skill                                                                                                                                                     | Source                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| "The only way to win is to not do a live demo in front of hundreds of strangers in the first place"                                                                    | Zach Holman, speaking.io, "Live Tech Demos"                                                                                        |
| A screencast in the deck removes app-switching and typing stress; copying from a script file removes typos; pre-recording the _commentary_ turns the talk into a movie | Holman, same page                                                                                                                  |
| The "golden path": a fixed order of demo actions, found by rehearsal, that has the best chance of surviving                                                            | Ben Lovejoy, 9to5Mac (9 Jan 2017), reporting the Internet History Podcast on the 2007 iPhone keynote                               |
| Six days of rehearsal still did not produce one clean end-to-end run of that demo                                                                                      | Same source - the evidence that reps do not buy reliability                                                                        |
| A portable cell tower was brought in rather than trusting the venue's signal                                                                                           | Same source                                                                                                                        |
| Rehearsing step by step is what reveals each segment's real duration; the repair is cutting low-value steps and pre-filling boilerplate                                | Arnaud Lauret (API Handyman), stepped live-coding method                                                                           |
| Restoring a step should be a copy of a stored snapshot, not a reconstruction                                                                                           | Lauret, same method (`steps/step-N/` directories plus go/next/prev/reload/reset scripts)                                           |
| Simulated typing plus pre-staged dependencies lets you show an install command without waiting for it                                                                  | `paxtonhare/demo-magic`                                                                                                            |
| Scripted editor demos (file creation, highlighting, markdown slides) driven from one keyboard shortcut                                                                 | Elio Struyf's scripted-demo talk, GitNation                                                                                        |
| The speaker buddy: a colleague not speaking in the same slot, front row, holding a clone of everything                                                                 | Marc Duiker, "Speaker Buddy System"                                                                                                |
| An abort path must be _scripted and tested before_ the event, not improvised during it                                                                                 | `jeffallan/claude-skills@chaos-engineer` safety checklist - stated there as automated rollback ≤ 30 seconds for a chaos experiment |
| A runbook needs a last-verified date and an owner, because runbooks rot; and a top-of-page checklist because the reader is under stress                                | `wshobson/agents@incident-runbook-templates`                                                                                       |

The last two come from incident-response and chaos-engineering practice. Cite them as precedent for the _rule_, never as a measured demo figure.

## Conventions borrowed from practitioner advice

These circulate as advice rather than measurement. Treat them as defaults worth keeping unless the room says otherwise.

| Figure                                                                 | Where it circulates                                                    |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Terminal 24pt or larger, editor 20pt or larger                         | `jonathimer/devmarketing-skills@developer-advocacy` pre-demo checklist |
| 10-3-1 - rehearse 10 times, hold 3 checkpoints, keep 1 recorded backup | Same skill, stated there as a rule of thumb                            |
| "At least three checkpoints"                                           | The 3 in 10-3-1                                                        |

## Baselines set by this skill

| Figure                                                                                                                                       | Why this value                                                                                                     | How to adjust                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Segments under ~90 seconds                                                                                                                   | Short enough that abandoning one costs less than a minute of the slot                                              | Scale to the slot: a 5-minute demo wants ~45s segments, a workshop tolerates longer                              |
| One repair attempt, ~20 seconds, then switch                                                                                                 | Below a conference audience's patience for silence, and long enough for the obvious fix (retry, reconnect, re-run) | Shorten for a keynote, lengthen for a workshop where the audience is debugging with you                          |
| Three consecutive clean cold runs                                                                                                            | Two can both be luck; three makes a flaky step likely to have shown itself                                         | Raise it when the demo has a genuinely non-deterministic step                                                    |
| Measured time under half the minutes allowed                                                                                                 | Leaves room for one full recovery plus questions                                                                   | Tighten to a third when the demo sits at the end of a hard-stop slot                                             |
| 80-100 columns                                                                                                                               | Wide enough for real commands, narrow enough not to wrap at projector resolution                                   | Set by the actual venue resolution during rehearsal                                                              |
| The five-tier fidelity ladder (0-4)                                                                                                          | Written for this skill as a decision aid                                                                           | It is a synthesis, not a published model - never present it as one                                               |
| The tiers' efficiency order (`3 > 2 > 1 > 4 > 0`) and the tier-3 default                                                                     | This skill's own judgment of credibility bought per rehearsal hour and per unit of stage risk                      | Re-rank per demo: an offline stack or a recording that already exists moves its tier to near-free and to the top |
| The pass threshold as a whole (three cold runs, entry from every restore point, top-three drills, one offline run, one venue-resolution run) | A designed gate: each item is the cheapest test that would catch one class of stage failure                        | Drop items the demo genuinely cannot fail, and say which you dropped                                             |

## About the worked examples

Both worked examples in the risk-register reference (the schema-migration demo done well and done badly) are illustrative. They show the structure to aim for. Do not cite their timings as typical.
