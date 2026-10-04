# Cadence patterns

Five sustainable shapes for the practice, how to size one against real capacity, and how to pause without signalling death.

## Contents

- [The patterns](#the-patterns)
- [Capacity math](#capacity-math)
- [Repurposing loop](#repurposing-loop)
- [Pause and restart](#pause-and-restart)

## The patterns

| Pattern         | Shape                                                                    | Fits                                                       | Breaks when                                                                 |
| --------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- | --------------------------------------------------------------------------- |
| Release spine   | One post per release, no release no post                                 | Any project with a real release rhythm                     | Releases become rare; the practice disappears with them                     |
| Weekly log      | Fixed-day short update: shipped / learned / stuck / next                 | Solo maintainers building an audience habit                | The streak becomes the obligation and one miss feels terminal               |
| Batched event   | Announcements concentrated into a launch week, one headline item per day | Teams with several shippable items per quarter             | Between events, the project looks silent for months                         |
| Periodic report | Monthly or quarterly long post: metrics, decisions, misses               | Rung 4-5 disclosure; teams with reporting already in place | Written the day before with numbers nobody has verified                     |
| Daily micro-log | Short daily notes from the work itself                                   | Full-time solo builders with an existing audience          | The maintainer also reviews PRs and answers issues - which is almost always |

The release spine is the safest default for a maintainer: the material already exists, the cadence follows the work, and quiet periods degrade gracefully instead of producing filler.

Batching is a real strategic option, not a compromise. Concentrating a quarter of scattered updates into one dated event produces an attention spike that a drip never reaches - Supabase's Launch Week runs five days with one main-stage announcement per day plus additional releases, a hackathon and meetups attached. The cost is accepting long public silence between events, which only works when releases keep flowing in the repository meanwhile.

## Capacity math

Estimate honestly, in minutes:

```
per post   = drafting + screenshots/demo + review + boundary check
per cycle  = per post × posts per cycle
reply load = per post × expected threads × minutes per reply   # usually the larger number
```

Then apply two rules.

- **The tenth.** A self-set working baseline, not a measured benchmark: if the practice consumes more than roughly a tenth of the maintainer's available project time, it is competing with the work it narrates. Reduce frequency before reducing depth - one substantial monthly post beats four thin weekly ones.
- **The worst month.** Choose the cadence the worst month can sustain, then over-deliver in good months. A published cadence is a promise; repeatedly missing it reads as project decline - the exact signal the practice exists to prevent.

## Repurposing loop

One piece of real work should feed several surfaces without being rewritten:

```
release notes / ADR / postmortem   (source of truth, in the repository)
        └─> short post on the anchor surface
                └─> social amplification, per-channel format
                        └─> entry in the periodic report
                                └─> talk, stream or article material
```

Public posts link back to the repository artifact rather than duplicating it, so a change has one place to be corrected.

## Pause and restart

Announce pauses; never fade out. State the reason, the expected return, and where releases stay visible in the meantime.

An announced eight-week gap costs nothing. An unannounced one is read as abandonment and shows up in other people's adoption decisions.

Restarting after a long silence works best as a single catch-up post that covers the gap honestly - what shipped, what stalled, what changed - and then a lower cadence than the one that broke. Restarting at the old frequency usually reproduces the same collapse.
