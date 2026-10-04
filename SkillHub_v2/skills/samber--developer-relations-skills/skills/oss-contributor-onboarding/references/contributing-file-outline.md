# CONTRIBUTING file outline

## 1. Placement and precedence

- Valid locations: repository root, `docs/`, `.github/`.
- When several copies exist, GitHub displays `.github/` first, then the root, then `docs/`. Keep exactly one file; duplicates diverge silently.
- The file is surfaced automatically when someone opens an issue or a pull request, in the repository sidebar, and on the repository's contribute page. Assume the reader arrives mid-task, already typing - write for skimming, put the entry points near the top.
- An organization-level `.github` repository supplies defaults to every repository that has no file of its own. Useful for policy boilerplate; never a substitute for the per-project setup and first-issue sections.

## 2. Section-by-section outline

Order matters: each section answers the question the reader has at that moment, and a reader who cannot answer question N never reaches section N+1.

1. **Welcome and scope of contribution (3-5 lines).** Which kinds are wanted: code, documentation, tests, triage, translation, design, examples. Naming non-code work here is what recruits the majority of first-time contributors.
2. **Out of scope (3-6 lines).** Features outside the project's purpose, new dependencies, style rewrites, vendored platform support. Every line here prevents a PR that would have cost both sides a week and ended in a rejection.
3. **Ways to help without code (short list).** Reproducing bug reports, answering questions, improving error messages, adding a missing test. Link the label or query that surfaces each.
4. **Get the project running (the longest technical section).** One command from a fresh clone to passing tests, plus the expected output and the version file or container definition that pins the prerequisites. Anything the contributor must install by hand is a documented prerequisite, not an assumption.
5. **Find something to work on.** The beginner-issue query, the claiming convention, the expiry rule for stale claims, and what to do when nothing fits.
6. **Before you open a pull request.** The gating commands, the branch to target, the commit-message convention with one example, and the legal step (DCO sign-off or CLA) stated here rather than discovered at the gate.
7. **What happens after you submit.** Who reviews, the response target, what each label means, the merge style, which release the change ships in, and what happens when a PR goes quiet, from both sides.
8. **Getting unstuck.** The synchronous channel, the asynchronous channel, and the expected latency of each. A contributor stuck for two days who never asked is a contributor you lost to a missing link.
9. **Recognition and growing into the project.** How contributions are credited, and what the next rungs are. Keep it to a pointer if a governance document owns the full ladder.

## 3. Sizing by project shape

The advice diverges most between a volunteer project and a corporate-backed one, so state which you are - contributors calibrate their expectations from it.

|                            | Volunteer / solo maintainer                                                        | Corporate-backed or foundation project                                                 |
| -------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Response target to publish | Honest and generous ("usually within a week"), plus the real hours-per-week budget | A staffed target, with the on-call or triage rota named                                |
| Legal gate                 | Usually DCO sign-off, one line                                                     | Often a CLA; link it and say when it triggers                                          |
| Scope negotiation          | Ask before large work, always                                                      | Often a design-doc or RFC process to link                                              |
| Ladder                     | Repeat contributor → co-maintainer, informal                                       | Published ladder with sponsors, areas, and emeritus rules                              |
| Risk to name               | Maintainer burnout; say no early                                                   | Contributor suspecting the roadmap is decided internally; publish the decision process |

Everything else - setup, first issues, pre-PR checks, review tone, recognition - is identical in both shapes. Say so rather than writing two documents.

Length: a small library is complete at roughly 150-300 words plus the setup block. A multi-repository project needs a short root file that routes to per-area guides, not one long file.

## 4. What belongs in a neighbouring file

Link each of these instead of duplicating its content:

- `README`: what the project is
- `CODE_OF_CONDUCT`: behaviour and enforcement
- `SECURITY`: private vulnerability reporting
- `SUPPORT`: where _users_ ask usage questions
- `GOVERNANCE`: decision rights and maintainer selection
- issue and PR templates: per-submission prompts
- `CODEOWNERS`: reviewer routing

A CONTRIBUTING file that absorbs its neighbours becomes the document nobody finishes.

## 5. Compact skeleton

```markdown
# Contributing to <project>

Thanks for being here. We take code, documentation, tests, triage and translations.
We do not take <the two or three things that get declined>.

## Set up

    git clone <fork> && cd <project>
    make setup      # installs everything and runs the test suite

Expect: `<N> tests passed` in under <M> minutes.
Prerequisites: <runtime> <version> (pinned in `<version file>`), <system package>.

## Find something to work on

- Beginner-friendly: <link to the label query>. Comment on the issue to claim it;
  claims expire after <N> days.
- Nothing fits? Open an issue describing what you want to change before writing code.

## Before opening a pull request

    make test lint

Target the `<branch>` branch. Sign your commits with `git commit -s` (DCO).

## After you submit

A maintainer responds within <target>. We squash-merge. Changes ship in the next
<cadence> release, and you are credited in the changelog.

## Stuck?

Ask in <channel> (usually answered within <latency>) or comment on your pull request.
```

## 6. Legibility to an agent-assisted contributor

Some first pull requests now arrive prepared by a coding agent reading this file on the contributor's behalf. GitHub's own `make-repo-contribution`, a widely installed skill on skills.sh, searches the README, the CONTRIBUTING file, project documentation, and the issue and PR templates _before_ the first branch. It applies exactly six things:

- branch naming
- commit message format
- which template to use
- required reviewers
- whether an issue must precede the pull request
- the prerequisite build/lint/test commands

Anything the project leaves unstated is replaced by that skill's own generic templates: an unstated convention is not merely undiscovered, it is overwritten.

Three consequences for how the file is written:

- **State conventions literally, near the top.** A branch prefix or commit format published only inside a PR template is found after the commits already exist.
- **Write the commands out, not just the wrapper.** The same skill refuses to execute anything it finds in repository documentation and asks the human to run and confirm builds and tests instead. `make setup` alone is not enough; give the literal commands and the output that proves they worked.
- **Never put a required step behind an off-repo link.** The agent is instructed not to fetch URLs mentioned in repository docs. Anything mandatory belongs in the file itself.

The same posture the skill sets for itself - "you are a guest in someone else's repository" - is a usable line for a project's own guidance.
