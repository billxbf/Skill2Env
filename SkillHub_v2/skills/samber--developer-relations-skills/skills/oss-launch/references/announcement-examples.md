# Announcement examples

Weak and strong versions of the artifacts a launch needs. The pattern behind all of them: a developer audience reads adversarially, and one inflated claim discredits everything around it.

## One-liners

| Weak                                              | Strong                                                                                                       | Why                                                                       |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| "A revolutionary new approach to data pipelines." | "A Python library for running SQL transformations on Parquet files without a warehouse."                     | Names the category, the runtime and the constraint it removes.            |
| "The fastest HTTP router for Go."                 | "An HTTP router for Go with zero allocations on the hot path - benchmarks and method in `bench/`."           | Replaces a superlative with a measurable property and where to verify it. |
| "Modern observability, reimagined."               | "A drop-in OpenTelemetry collector for teams that cannot ship data to a third party."                        | States who it is for and what makes them choose it.                       |
| "Like Kubernetes but simple."                     | "A single-binary container scheduler for one to ten machines, for teams that do not need Kubernetes' scale." | Draws the boundary honestly instead of picking a fight it will lose.      |

## Aggregator titles

| Weak                                                     | Strong                                                                           |
| -------------------------------------------------------- | -------------------------------------------------------------------------------- |
| "Show HN: We're excited to launch our amazing new tool!" | "Show HN: Litequeue – a job queue that runs entirely inside SQLite"              |
| "Show HN: Our startup raised $4M to fix logging"         | "Show HN: A log collector that costs $0 at 10 GB/day (open source)"              |
| "Show HN: v2.1.3 released"                               | "Show HN: I rewrote our tracing library and cut p99 overhead from 12ms to 400µs" |

A funding announcement is not a Show HN; a patch release is not either. Both belong in a normal submission, if anywhere.

## Comparison tables

Weak - every row favors you, so a reader stops believing the whole page.

|        | Ours | Theirs |
| ------ | ---- | ------ |
| Fast   | ✅   | ❌     |
| Easy   | ✅   | ❌     |
| Modern | ✅   | ❌     |

Strong - comparable dimensions, real numbers, and at least one row you lose.

|                         | Ours                             | Established alternative               |
| ----------------------- | -------------------------------- | ------------------------------------- |
| Install size            | 8 MB single binary               | 140 MB + runtime                      |
| Cold start              | 40 ms                            | 900 ms                                |
| Ecosystem / plugins     | 6                                | 400+                                  |
| Production track record | 8 months, 3 companies we know of | 9 years, widely deployed              |
| Best when               | Small deployments, edge, CI      | Large clusters, existing integrations |

Losing a row costs one reader and buys the trust that makes the other rows credible.

## First comment on the anchor thread

Weak:

> Hey everyone! We're thrilled to share our project with the community. It's a game-changing solution that makes development 10x faster. Would love your feedback and support! 🚀

Strong:

> I'm the author. I built this after our team spent a quarter debugging cross-service traces that dropped spans under load - the existing collectors we tried buffered in memory and lost data on restart, so this one writes to a local WAL first and replays.
>
> The interesting part is the WAL format: it trades ~8% throughput for restart durability, and I wrote up the benchmark method in `bench/README.md` so it can be argued with.
>
> It does not do sampling yet, the Windows build is untested, and the API will break at least once before 1.0.
>
> Happy to go deep on the WAL design or the OpenTelemetry compatibility surface.

The strong version does four things the weak one cannot:

- Establishes who is speaking.
- Gives a technical hook worth replying to.
- Discloses limits before a critic finds them.
- Invites a specific conversation.

## Disclosure when a company is behind the project

Weak: no mention of the company, an "Enterprise" link in the nav, and a licensing surprise after adoption.

Strong, in the announcement itself:

> This is built and maintained by <company>. The core is Apache-2.0 and stays that way; we sell a hosted version and an SSO/audit add-on. Nothing in this repository is time-limited or crippled - if it stops being useful without the paid product, that is a bug, tell us.

Readers accept a business model stated up front. They rarely forgive discovering one later.

## Rallying the team: The tempting mistake

This is the one every team reaches for, because it feels like ordinary enthusiasm rather than manipulation. It is the most damaging single launch mistake available; the damage is invisible: aggregators detect voting rings and penalize the submission, the account and sometimes the whole domain, silently. The team never learns why the post died and concludes the launch just did not land.

Wrong - an internal message that solicits votes.

> @channel we're live on HN! 🚀 Link below. Please upvote and drop a comment so we can hit the front page - every vote in the first hour counts. Also star the repo if you haven't!

Every clause is a violation: soliciting upvotes, soliciting comments, coordinating timing, soliciting stars. Rewriting it as "if you feel like it" does not help; coordination is the thing being detected.

Right - the same message, made legitimate.

> We're live on HN, link below. Don't vote or comment as a favour - that gets the post penalized and it's not worth it. What genuinely helps: if you know the problem space, reply where you have something real to add, and flag anything factually wrong in the thread to me directly so I can correct it. If you know someone who'd actually use this, send it to them.

The line is intent, not wording: pointing people at something is fine, asking them to act on the platform's ranking signals is not. Say this to the team before launch day, because someone will otherwise do it in good faith.

Product Hunt's terms prohibit the same thing, so the rule travels across channels unchanged.

## Register and rewriting

Announcements written by marketing read as press releases and get filed as ads. Restore the maintainer's voice: first person, the concrete problem, what was hard, what got cut, what is still broken. Run the final draft through your preferred humanizer skill, then read it aloud - anything you would not say to another engineer at a bar does not belong in it.
