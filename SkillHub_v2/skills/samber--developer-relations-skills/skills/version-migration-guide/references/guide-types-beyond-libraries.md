# Guide types beyond a library upgrade

The library/SDK case is the baseline the rest of this skill describes. Four other artefact types diverge enough that copying the library shape produces a wrong document. Pick the row that matches before drafting.

| Type                      | Core artefact                         | Distinctive mechanics                                                | Reversibility                                   |
| ------------------------- | ------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------- |
| Application library / SDK | Prose guide plus codemods             | Semver, deprecation warnings, N-1 bridging                           | High - pin the old version, roll back           |
| Database / schema         | **Runbook**, not prose                | Expand/contract, dual writes, batched backfill, online schema change | Low - data loss risk, rollback must be designed |
| Cloud / platform          | Vendor playbook plus state migration  | Provider major upgrades, state refresh, remote backend               | Medium - the state file is authoritative        |
| Mobile app                | Store listing plus in-app update flow | Forced or staged rollout, on-device data migration on first launch   | Very low - a shipped binary cannot be recalled  |
| Browser / platform API    | Official docs plus deprecation trials | Public intent-to-deprecate, origin trials, enterprise policy escape  | Low - breaks live sites globally                |

## Database and schema: write a runbook

Each step is an operational action with an explicit rollback and a backfill plan, not a snippet the reader pastes. That is the deepest divergence from the library shape.

Use **expand/contract** (also called parallel change): add the new schema elements without touching the old ones, dual-write and backfill, then remove the obsolete parts in a separate, later deploy. The reason is deployment overlap - during any rollout, old and new code run at the same time, so an in-place rename leaves one of them querying a column that no longer exists.

Runbook rules worth stating in the document itself:

1. Additive steps ship in any deploy; destructive steps (drop, rename) ship alone, after nothing references the old shape.
2. Every step names its rollback, and the rollback has been executed at least once against a copy of production.
3. Backfills run in throttled batches off the hot path - a single statement over millions of rows locks the table.
4. Build large indexes without blocking writes where the engine supports it.
5. Database-level tooling can carry the dual-write for you (versioned schema views and trigger-backed dual writes, or an online schema-change tool) - name whichever exists for the reader's engine.

## Cloud and platform: state is the source of truth, not code

Infrastructure-as-code provider major upgrades need a per-version upgrade guide, and the guide must say what to run immediately after the upgrade to reconcile stored state with the new internal schemas (a refresh-only apply, in Terraform's case). Say that a versioned remote backend is what makes rollback possible; without one there is no rollback story to write.

## Mobile: you cannot un-ship a binary

Cover the staged-rollout percentage plan, the forced-update path for versions that must not keep running, and the on-device data migration that executes once on first launch of the new binary - including what happens when it fails halfway.

## Browser and platform APIs: the timeline is public and contested

These deprecations run through a formal public process, and the timeline moves in response to developer backlash. Chrome's Manifest V2 to V3 transition is the flagship case: announced in 2021, then paused in December 2022, then republished, then resumed in the May 2024 "Resuming the transition" post, with an enterprise policy giving managed deployments the longest escape hatch. The DevRel deliverables that eventually moved adoption past 85% of actively maintained extensions were a migration guide, per-capability checklists, and a public progress page tracking the top blocking issues.

Two transferable lessons:

- Ship a **public progress page** for the gaps you have not closed yet. A deprecation with known missing capabilities and no visible tracker reads as indifference, and the backlash costs more than the honesty would have.
- Give managed or contractual deployments a **named escape hatch with its own end date**, separate from the general timeline. They plan on a different cycle and will otherwise escalate.

## Language runtime and OS: the hardest case

Python 2 to 3 is the reference: a semantic break across an entire ecosystem, an announcement-to-sunset window of over a decade (2008 announcement, 2015 target, sunset January 1 2020), dedicated tooling, and a hard publicly committed date that is what finally forced completion. If your break is of this class, the guide is one input among many - the date and the ecosystem tooling do most of the work.

Attribution for the figures above:

- The 85% Manifest V3 number and the transition dates come from Google's own Chromium and Chrome-for-Developers posts (May 2024).
- The Python sunset date comes from the Python Software Foundation.
- Expand/contract and online schema-change tooling are documented by the Postgres and MySQL tool projects that implement them.
