# Worked allocation

A complete allocation for a fictional Series A API-observability company: 40 employees, self-serve entry with a sales-assisted enterprise tier, one advocate, one technical writer, one half-time community manager. Numbers are illustrative and internally consistent; copy the shape, never the figures.

## Contents

- The finished document
- Weak versus strong: envelope
- Weak versus strong: threshold
- Weak versus strong: review rule
- Weak versus strong: cut list
- Weak versus strong: funder narrative
- Negative example: the plan that balances on cash and fails on hours

## The finished document

### Envelope - FY, EUR

- **Total program budget: 240,000. Salaries excluded** - 2.5 devrel FTE sit on a separate headcount line owned by the VP Marketing.
- **Committed: 38,000** - community platform licence 6,000 (renews 1 Nov, 60-day notice); two-year conference contract 32,000 (final year).
- **Discretionary: 202,000** - the number allocated below.
- **Borrowed: ~25,000** - field marketing funds two regional customer dinners. Owner: Demand Gen. Not depended on by any line here.
- **In-kind** - 6 h/week of staff-engineer review time, agreed with the platform lead, capped.
- **Hours envelope: 3,680 h/year** (advocate 30 h/wk, writer 32, community manager 18, over 46 working weeks). **Planned against: 2,760 h** after the 25% deduction for support load, launches and incidents.

Primary motion this period: individual self-serve adoption, with enterprise evaluation second. Funded driver: developer adoption. Both stated by the VP Marketing, who signs.

### Allocation

| Line                          | Pillar     | Cash        | Hours     | Owner             | Buys                                                               | Threshold                                                                               | Review                   | If it misses                       |
| ----------------------------- | ---------- | ----------- | --------- | ----------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------- |
| Docs, samples and sandbox     | Enablement | 34,000      | 900       | Writer            | Quickstart rewrite, 4-language sample parity in CI, hosted sandbox | p50 time-to-first-success < 12 min (baseline 22); samples green ≥ 95% of days           | Quarterly                | Drop sandbox, keep samples         |
| Technical content pipeline    | Content    | 52,000      | 700       | Advocate          | 24 slotted pieces, agency drafts, in-house outlines and review     | ≥ 20 published and reviewed; median 450 sessions at 90 days (baseline 380)              | Quarterly                | Cut agency, 12 in-house pieces     |
| Events                        | Events     | 58,000      | 620       | Advocate          | 1 flagship booth, 3 partner workshops                              | ≤ 700 per qualified conversation fully loaded; ≥ 120 conversations (baseline 84 at 810) | 2 weeks after each event | Renegotiate booth to workshop tier |
| Community venue and champions | Community  | 18,000      | 420       | Community manager | Moderation cover, recognition, 8 champions                         | ≥ 60% of questions answered < 24 h; ≥ 25 monthly active askers by Q4 (baseline 9)       | Quarterly                | Cut champions, keep answering      |
| OSS sponsorship               | Ecosystem  | 10,000      | 60        | Advocate          | Breadth across dependency graph, depth on 3 load-bearing projects  | Experiment - named maintainer relationships on all 3 by Q3                              | Q3                       | Keep breadth, drop depth           |
| Experiments (2)               | -          | 6,000       | 60        | Advocate          | 1 sponsored newsletter run, 1 video series pilot                   | Each ships by its kill date with a written read                                         | Kill date per experiment | Close, do not extend               |
| Reserve                       | -          | 24,000      | -         | VP Marketing      | Unallocated                                                        | -                                                                                       | Quarterly                | -                                  |
| **Total**                     |            | **202,000** | **2,760** |                   |                                                                    |                                                                                         |                          |                                    |

Horizon split of the 178,000 allocated: compounding 104,000 (58%), scaling the working bet 58,000 (33%), experiments 16,000 (9%). Deliberately heavier on compounding than the familiar 70/20/10 shape, because the enterprise motion is second this period and the events line is already proven.

### Unfunded list - ranked, lost on the ranking

- Certification program - revisit when self-serve activation exceeds 500/month; no evidence of demand yet.
- Second regional community - one venue is the rule until the first clears its answer-rate threshold.

### Ruled out - never ranked

- Conference speaking tour beyond the funded events - constraint: it breaches the advocate's hours ceiling. Back on the table only if a second advocate is hired.

### Review clocks

Burn monthly (cash rate and hours actually logged) · line verdicts quarterly, events two weeks after each edition · envelope at the annual cycle, draft ask due six weeks before it locks.

### Reallocation triggers

A line misses its threshold twice · the funded driver or the VP Marketing changes · the conference contract reaches its 60-day notice date · the writer or community manager leaves · an opportunity clears a higher bar than the experiments line, which is drawn from first.

### Cut list

| Cut           | Removes                                                                          | Consequence                                                                                                                |
| ------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| −20% (40,400) | 2 of 3 workshops (18,000); agency volume halved (16,000); OSS depth (6,000)      | Enterprise evaluation coverage drops to one event; content output falls to ~14 pieces; ecosystem line becomes breadth-only |
| −40% (80,800) | The above plus the flagship booth (32,000), replaced by speaking-only attendance | No enterprise field presence; pipeline contribution becomes unmeasurable this year; compounding surfaces protected         |

This is step 4's efficiency order read from the bottom: rented reach goes first (workshops, sponsorship depth, then the booth), and the foundational override holds the rest. Docs, samples and the community answer rate are cut last: they are the surfaces whose neglect is actively harmful rather than merely invisible.

### Narrative for the funder

We fund developer adoption. Most of the money goes to the two things that compound - the path from landing page to first working call, and the technical content people find when they search for the problem. One flagship event and three workshops keep the enterprise evaluation motion alive, priced at under 700 euros per qualified conversation. Twelve percent stays unallocated so we can act on what appears mid-year. If the budget is cut by a fifth, we drop workshops and agency volume first, and we protect the docs.

## Weak versus strong: envelope

**Weak** - "Our devrel budget is 240K." Comparable to nothing, hides 38,000 of committed spend and the entire hours constraint, and invites a benchmark comparison against programs that include salaries.

**Strong** - the envelope section above: salaries named as excluded, committed spend separated with its notice date, borrowed money attributed to its real owner, hours stated and discounted.

## Weak versus strong: threshold

**Weak** - "Events should generate strong pipeline." Unmeasurable, so the line renews on vibes.

**Strong** - "≤ 700 per qualified conversation fully loaded; ≥ 120 conversations; baseline 84 at 810 last year." Derived from the program's own prior period, with the qualification bar written before the event and briefed to every staffer.

## Weak versus strong: review rule

**Weak** - "We will review the budget quarterly." One clock for three different questions, so burn-rate detail crowds out the renew-or-drop decision.

**Strong** - three clocks at different rhythms, each with its own question, plus written triggers that fire between reviews.

## Weak versus strong: cut list

**Weak** - "We could absorb a 20% cut if we had to." Hands the ordering to whoever runs the spreadsheet, and an even trim starves the compounding lines first.

**Strong** - the ordered table above: what goes, in which order, with the consequence of each removal named in one sentence.

## Weak versus strong: funder narrative

**Weak** - "DevRel drives awareness and community engagement across multiple channels, supporting the funnel end to end." No decision is visible, so the budget reads as an activity list.

**Strong** - the five sentences above: one driver, the concentration choice, the one number the events line is held to, the reserve, and the cut order. A funder can repeat it in a meeting the devrel lead is not in.

## Negative example: the plan that balances on cash and fails on hours

Same fictional company, same 202,000 discretionary. This version is the one that gets approved in the room and collapses in month four. Read it as a diagnosis exercise: five defects, all of them common, none of them visible to a reviewer who only checks that the cash column adds up.

| Line                    | Pillar     | Cash        | Hours | Owner       | Threshold                     | Review      |
| ----------------------- | ---------- | ----------- | ----- | ----------- | ----------------------------- | ----------- |
| Conferences (4)         | Events     | 72,000      | -     | DevRel      | Build awareness and pipeline  | End of year |
| Content                 | Content    | 40,000      | -     | DevRel      | 40 blog posts                 | End of year |
| Community               | Community  | 20,000      | -     | DevRel      | Grow Discord to 2,000 members | End of year |
| Docs and samples        | Enablement | 25,000      | -     | Engineering | Keep docs current             | -           |
| Certification program   | Education  | 30,000      | -     | DevRel      | Launch by Q4                  | -           |
| Newsletter sponsorships | Paid       | 15,000      | -     | DevRel      | Drive signups                 | -           |
| **Total**               |            | **202,000** |       |             |                               |             |

What is wrong with it:

1. **No hours column at all.** Priced out afterwards, the four conferences alone consume roughly 800 hours, the certification launch is over 600, and docs "owned by Engineering" is an unfunded claim on a team that never agreed to it. Total planned work exceeds the 2,760-hour envelope by more than half. The cash is real; the plan is not.
2. **Six pillars, none concentrated.** No line is large enough to clear a consistency threshold, so the year produces activity in every column and a result in none.
3. **Thresholds that cannot fail.** "Build awareness", "keep docs current" and "drive signups" have no unit and no number, so every line renews by default. "2,000 Discord members" has a number but counts joins, which a giveaway can buy without producing a single answered question.
4. **One owner for five lines, one review date for all of them.** "DevRel" is a team, not a person, and an end-of-year review arrives after every decision it was supposed to inform.
5. **No reserve, no unfunded list, no cut list.** The first mid-year opportunity has to be taken out of a funded line, and a 20% cut arrives as a flat trim that hits the compounding surfaces hardest.

The repair is not a bigger budget:

- Price the hours.
- Drop to two funded pillars plus maintenance.
- Name a person per line.
- Give each a unit and a baseline-derived number.
- Hold back a reserve.
- Write the cut order before anyone asks for it.
