# Demo risk register

## Contents

- How to use it
- Risk taxonomy
- Worked example: done well
- Worked example: done badly
- Negative example: hardened versus faked

## How to use it

Walk the taxonomy against the specific demo, keep only the risks that can actually fire, and rank the survivors by likelihood × how visibly they break. Drill the top three. A register that lists every risk equally is a document nobody acts on.

Each row's mitigation is a design change, not a reminder to be careful. "Practise typing it twenty times" is a discipline answer to a design problem; scripting the input is the design answer.

## Risk taxonomy

### Network and dependencies

| Risk                                                                                 | Mitigation                                                                      |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Venue Wi-Fi unusable, saturated, or behind a captive portal that expires mid-session | Run the stack locally; hotspot as backup, tested in the room                    |
| Third-party API down, rate-limited, or slow                                          | Replay recorded responses or run a local mock; never depend on a free tier live |
| Package registry, image registry or model download needed on stage                   | Pre-provision everything; warm every cache before the session                   |
| Audience floods your demo endpoint the second the URL is on screen                   | Keep the endpoint local, or don't show a reachable URL                          |
| Corporate VPN reconnects, IPv6-only or NAT64 venue network, non-443 ports blocked    | Local stack; if impossible, test on the venue network the day before            |

### Execution

| Risk                                                          | Mitigation                                                                 |
| ------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Typo or forgotten flag freezes the speaker                    | Script the input: paste from a file or drive it with a demo runner         |
| Error the speaker cannot fix live                             | Named checkpoints; skip to the next segment rather than debug              |
| Slow step eats the budget (install, build, cold start, index) | Pre-provision; show the command, not the wait                              |
| State left over from the previous run changes behaviour       | One-command idempotent reset, rehearsed from a cold machine                |
| A segment cannot start because the previous one failed        | Architectural fix only: every segment enterable from its own restore point |
| Demo runs long                                                | Segments under 90s, marked droppable; budget at twice the rehearsed length |

### Screen and machine

| Risk                                                                   | Mitigation                                                              |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Text unreadable from the back                                          | 24pt+ terminal, 20pt+ editor, high contrast, verified from the back row |
| Dark theme washed out by the projector                                 | Light or high-contrast theme for the session                            |
| Notification, calendar popup or personal message on screen             | Do Not Disturb; quit chat, mail and calendar entirely                   |
| Token, client name or embarrassing command in an autocomplete dropdown | Fresh browser profile, cleared shell history and editor recents         |
| Display refuses to mirror, or resolution changes the layout            | Test mirroring at the venue's resolution; rehearse at that resolution   |
| Laptop dies                                                            | Deck PDF plus a buddy in the front row holding a clone                  |

### Content and data

| Risk                                                                                  | Mitigation                                                                   |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Real customer data or identifiers visible                                             | Seeded fixtures in a sandbox tenant; never demo against production           |
| Embargoed or unreleased feature appears in a menu                                     | Feature-flag it off in the demo build; check every screen that will be shown |
| Placeholder data undermines credibility with a buyer                                  | Domain-realistic seed data at realistic volume                               |
| Demo shows six features and proves none                                               | Re-anchor every segment to the single claim                                  |
| An on-screen number is hard-coded, stubbed or edited to look better than the real run | Only harden the setup, never the output - see the negative example below     |

## Worked example: done well

Constructed for illustration - copy the shape, not the specifics; no real conference runbook is quoted here.

Demo: a CLI that migrates a schema without downtime. Slot allows 5 minutes.

```
Claim:  "One command migrates a live table with zero failed writes."
Tier:   2 (live execution, fully local); the claim is about behaviour under
        concurrent writes, so a recording would not settle the room's doubt.
        Fallback tier 3: a screencast of the same run, on slide 22.

Segments
 1  Concurrent writers are running        enter: image tag demo/step-1   45s  not droppable
 2  Migration starts, writes keep landing enter: image tag demo/step-2   60s  not droppable
 3  Verification query shows zero loss    enter: dump demo-verify.sql    40s  droppable

Top risks, drilled
 1  Container fails to start        → goto step-2 image; drill: switched in 11s
 2  Writer process dies mid-run     → recording clip 02; drill: switched in 9s
 3  Verification query returns odd  → screenshot of the verified run, slide 23

Reset: ./demo reset   (recreates volumes, reseeds 50k rows, ~4s, verified cold)
Network: none required; Wi-Fi disabled during all three cold runs.
Measured: 2:25, 2:20, 2:22 across three cold runs. Budget 5:00.
```

Why it works: the claim is narrow, every segment proves part of it, each segment starts from its own artifact, the whole thing runs offline, and the recovery times are measured rather than assumed.

## Worked example: done badly

Same product, same slot.

```
Plan: "I'll open the terminal and show the migration on our staging cluster,
       then jump into the dashboard to show the metrics, then show the new
       UI we shipped last week, then take questions."

No claim written down.
No segments; one continuous 5-minute flow.
Staging cluster over conference Wi-Fi; VPN required.
Dashboard depends on the migration having just run.
Backup plan: "I've done this loads of times."
Rehearsed twice, at a desk, on the office network, on a dark theme.
```

Everything that is wrong here is structural, not sloppy:

- No claim, so nothing tells the speaker which parts to cut when the clock slips.
- The dashboard segment consumes the migration segment's output, so one failure takes down two thirds of the demo.
- The remote dependency chain (VPN → cluster → dashboard) has three independent ways to fail and no local equivalent.
- "The new UI we shipped last week" is a fourth topic with no relationship to the claim.
- Rehearsing on the office network measures nothing about the venue, and rehearsing at a desk measures nothing about legibility.
- With no fallback asset, the only recovery available on stage is debugging in front of the audience.

The repair is not more practice. It is:

- Write the claim.
- Split into three restorable segments.
- Move the cluster to a local stack.
- Delete the UI tour.
- Record a fallback clip.
- Re-time it cold.

## Negative example: hardened versus faked

Every technique in this skill removes variance from the demo's _setup_. The moment a technique starts producing an _output_ the real system would not produce, it has crossed from engineering into faking, and a developer audience treats the two very differently.

The 2007 iPhone keynote sits on both sides of that line, which is why it is the clearest teaching case. Per 9to5Mac's report of the Internet History Podcast, the team fixed the order of operations (the golden path) and had AT&T bring in a portable cell tower - both are hardening. They also "hard-coded all the demo units to display five bars of cell strength, whether that happened to be true or not" - that is faking, and it was only survivable because nobody could inspect the device.

Apply it to the schema-migration demo:

```
Hardened; keep                       Faked; never ship
------------------------------------  ------------------------------------
Seeded 50k-row fixture, fixed seed    A "rows migrated" counter that
                                      increments on a timer

Pinned versions, pre-pulled images    A verification query with the failure
                                      case filtered out of the WHERE clause

Recorded third-party responses,       A recorded clip played while claiming
captured from a real run              it is executing live

Hiding a flaky status badge that is   Hiding an error banner that is about
not part of the claim                 the claim

A screencast, announced as a          Latency numbers from a laptop run,
recording                             labelled as production
```

The test: if an audience member asked "is that real?", could you answer yes and then prove it on the spot? Hardening survives that question. Faking depends on nobody asking, and the cost of being caught is the credibility the live demo existed to buy in the first place.

When a demo can only clear its claim by faking, the claim is wrong. Narrow it to something the system actually does today, or drop to tier 4 and show the architecture instead.
