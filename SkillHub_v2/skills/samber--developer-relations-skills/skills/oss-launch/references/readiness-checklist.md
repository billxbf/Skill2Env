# Launch readiness checklist

Score the repository before a date exists. Blockers postpone the launch; boosters change conversion, never the date.

The blocker list below is Karl Fogel's pre-announcement inventory from _Producing Open Source Software_ (producingoss.com), reordered by what a launch actually breaks on. Fogel's own framing of why presentation counts: "the very first thing a visitor learns about a project is what its home page looks like." A visitor reads polish as a proxy for whether the project will still exist next year; abandonment risk is what they are really screening for.

## Blockers

| #   | Check                | Passes when                                                                                                                                                                                                                                                                           |
| --- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | Name                 | Trademark clearance done (phonetic, visual, conceptual, all target jurisdictions), and the domain, code-host org and handles are secured. This one carries an 8-week lead time, so it gates the date rather than the gate.                                                            |
| 1   | License              | An OSI-recognized license file is present, matches what the README claims, and dependencies allow it. Company projects also state the ownership/CLA position.                                                                                                                         |
| 2   | Install              | The documented install command works on a clean machine for every OS and runtime version the README claims.                                                                                                                                                                           |
| 3   | First success        | One runnable example produces visible output within the claimed time budget, using only what the README provides.                                                                                                                                                                     |
| 4   | Ten-second read      | The top of the README answers what it is, who it is for, and what it replaces.                                                                                                                                                                                                        |
| 5   | Reachability         | Repository is public, issues enabled, and a maintainer is available on launch day and the day after.                                                                                                                                                                                  |
| 6   | Distribution         | Published to the ecosystem registry, or the install path genuinely does not need one. Tag and release notes exist.                                                                                                                                                                    |
| 7   | Hygiene              | No keys, tokens, internal hostnames, customer data or proprietary code anywhere in the history - not only in the current tree.                                                                                                                                                        |
| 8   | Claims               | Every claim in the announcement draft is defensible: benchmarks reproducible, "used in production" true, adoption numbers real.                                                                                                                                                       |
| 9   | Security contact     | `SECURITY.md` exists, names a private reporting channel, and someone is watching it. A vulnerability posted in the launch thread has to move private within minutes, and it cannot if there is nowhere to move it.                                                                    |
| 10  | Contribution channel | Issue tracker open, communication channel named, and basic contributor guidance present. Fogel's inventory treats these as pre-announcement items, not post-launch cleanup: without a public place to talk, people contact the maintainer directly and the load never becomes shared. |

## Boosters

Boosters raise conversion; none is worth delaying the date for. Listed by lift per pre-launch hour, best ratio first - not cheapest first.

| #   | Booster                                                                | Effort         | Lift                                                                                                        |
| --- | ---------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | Social preview image, repository description, 5-10 topics              | near-zero      | Whether the link previews at all and whether the repository is findable by topic                            |
| 2   | Demo GIF, short video, or hosted playground                            | an hour or two | Highest lift per hour for individual adoption - shows output instead of claiming it                         |
| 3   | Comparison section naming real alternatives with honest trade-offs     | an hour        | Highest lift for company adoption; pre-answers the thread's highest-value question                          |
| 4   | Security policy, release cadence statement, maintainer/funding model   | an hour        | The pages an internal approver blocks on; without them a team-shaped launch stalls                          |
| 5   | CONTRIBUTING.md, issue templates, a few small `good first issue` items | an hour        | Opens the contributor funnel and doubles as the triage guard if the launch over-performs                    |
| 6   | Benchmarks with hardware, versions, method and a reproduction command  | a day or more  | Strong credibility and the one booster that can backfire - an unreproducible number becomes the top comment |
| 7   | Long-form "why this exists" write-up                                   | a week         | Durable: carries week two and still delivers readers a year out                                             |
| 8   | Documentation site                                                     | a week or more | Only once the surface outgrows one README; below that, a second place to go stale                           |

The axes disagree:

- efficiency: `1 > 2 > 3 > 4 > 5 > 6 > 7 > 8`
- effort, heaviest first: `8 > 7 > 6 > 2 > 3 == 4 == 5 > 1`

Rows 3, 4 and 5 tie on effort because each is one sitting spent writing a page from facts the maintainer already holds, and none of them scales with the size of the project.

**Default: take rows 1-3.** Add row 4 when the target adopter is a company, row 5 when contributors are the launch goal.

Rows 6-8 are what the ratio starves: durable, beaten every round. Promote them on a named condition:

- Benchmarks only when a performance claim is already in the announcement draft (blocker 8 then makes them mandatory, not optional).
- The write-up only when differentiation is an argument rather than a demo.
- The docs site only when the README has outgrown itself.

Delete the rest rather than parking them at the bottom - a booster listed and unbuilt reappears as work on launch morning.

## Cold-run protocol

The gate is empirical. Opinions about README quality do not settle it; a stranger's session does.

1. Pick a reader who has never used the project and is representative of the target adopter.
2. Give them a clean environment and the repository URL. Nothing else.
3. Forbid maintainer help. The maintainer watches silently and takes notes.
4. Record every hesitation: a command retyped, a version guessed, a missing prerequisite, a page they had to search for.
5. Stop at first success or at the time budget, whichever comes first.
6. Fix every hesitation, then re-run with a different reader.

Pass condition: an unaided cold reader reaches first success inside the claimed budget, with zero blocking hesitations.

When no human reader is available and you can execute commands, run the protocol yourself in a fresh directory:

- Follow the README literally.
- Never use knowledge of the codebase.
- Treat any moment you had to inspect source as a hesitation.

Say clearly in the plan that this substitute was used - an agent reads more charitably than a tired developer at 9 p.m.

## Verdict shapes

- **Go** - all blockers pass, boosters chosen, date set.
- **Go with reduced scope** - a blocker touches only part of the claim surface. Cut that claim (drop the benchmark, drop the Windows support statement) and launch the rest.
- **Not ready** - list the open blockers, the estimated work, and the earliest honest date. Say it plainly; a postponed launch costs a week, a broken one costs the novelty budget permanently.
