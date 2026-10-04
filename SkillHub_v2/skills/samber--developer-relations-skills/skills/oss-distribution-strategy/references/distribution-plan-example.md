# Worked example and entry patterns

A complete plan for a fictional project, then weak/strong pairs for the entries maintainers most often get wrong. SKILL.md's failure-mode list carries the negative examples.

## 1. Worked plan

From the interview: `queuelite`, a small Python library for durable background jobs on SQLite, published to one language registry. One maintainer, 6 hours a month. Adopters so far are individual developers; the maintainer wants small-team company adoption next. A 1.0 lands the following quarter.

```markdown
# Distribution plan - queuelite

## Position today

- Registry metadata 55%: description predates the async rewrite, 2 of 5 keyword slots
  used, no documentation or funding link, classifiers missing.
- Packaged downstream nowhere; no mirrors or forks with an audience.
- 3 listings: 1 accurate, 1 pointing at the pre-rename repo, 1 on a dead directory.
- 14 dependents, all individual projects; no company-owned repository visible.
- Arrivals (last 30 days): 62% direct/registry search, 21% one third-party blog post,
  9% the accurate listing, 8% unknown.
- Baseline 2026-08-26: 3,100 monthly downloads, 240 unique cloners, 14 dependents,
  last release 71 days ago, longest gap in the last year 94 days.

## Adopter

Both, sequenced. Individual developers stay the volume path, paid for by registry
findability. Company adoption is the growth goal and needs legibility work (versioning
promise, security contact, release rhythm) before any company-facing channel is worth
entering.

## Foundation ring (this month, ~3 hours, then minutes per release)

- Rewrite the registry description in the problem's vocabulary ("background jobs",
  "task queue", "SQLite", "no broker"); fill all 5 keyword slots and the classifiers.
- Add documentation, changelog, issue-tracker and funding links.
- Fix the renamed-repository listing; request removal from the dead directory.
- Publish a one-paragraph versioning and support statement in the README, linked from
  the registry page - what a company evaluator looks for first.

## Test ring (next quarter, 2 hours a month, ends 2026-12-01)

- T1 - Ecosystem list inclusion: the two curated lists in this language's
  background-jobs category, after two unrelated contributions to each.
  Signal: referral arrivals per listing > 30/month by the end date - a self-set bar
  rather than a published benchmark; derive it from the project's own current numbers,
  not from this figure.
- T2 - Framework integration: a documented adapter for the web framework 9 of the 14
  dependents already use, offered upstream first.
  Signal: adapter installs, plus one dependent that is a company repository.

## Core channel (candidate, decided at the test-ring end date)

Integration surface, if T2 produces adoption the listings do not: this project gets
chosen while solving another problem inside a framework, so the framework's docs are
where that decision happens.

## Refused

- System packaging: a library, not a binary; users install from the language registry
  inside a virtualenv. Zero benefit, permanent packaging cost.
- Aggregator relaunch before 1.0: novelty is spent and a repost reads as noise.
- Directory sprint (20+ submissions): at 6 hours a month the sweep alone consumes the
  budget, and stale listings damage the company-adoption goal specifically.
- Paid featured placements: no evidence the audience browses those pages.

## Release rhythm

Maximum interval 6 weeks, security fixes out of band within 72 hours; batch small
changes, every release ships notes. 1.0 in Q4 is the one milestone returning to
awareness channels.

## Review

Listing and package sweep quarterly, first 2026-11-15. Metadata re-check at every
minor release. Plan re-decision 2026-12-01, with the power to kill T1, T2 or both.

## Threshold check

Metadata 100% after the foundation ring ✓ · every channel has owner/cost/signal/review
date ✓ · recurring cost 3.5h of 6h capacity (58%) ✓ · no harmful-decay channel without a
sweep date ✓ · stale listings fixed before new channels ✓
```

## 2. Weak vs strong: channel entries

**Weak** - "Submit to awesome lists and developer directories to increase visibility."

Nothing here can be executed, refused or reviewed: no list named, no cost, no signal, no end date, no acknowledgement that each listing must be swept forever.

**Strong** - "Submit to the two curated lists in this language's background-jobs category, after two unrelated contributions to each. ~90 minutes total, 15 minutes per quarterly sweep. Success: >30 referral arrivals/month per listing by 2026-12-01. Below that, remove the entries and drop the family."

Every entry in the worked plan above follows that shape: named surface, cost to enter, cost to hold, signal, and the result that retires it.

Refusals take the same shape.

**Weak** - "We're not doing social media for now": an omission, not a refusal, and it will be proposed again next month.

**Strong** - "Refused: aggregator relaunch before 1.0. Novelty is spent and a repost reads as noise. Reconsider at the 1.0 milestone, where the story genuinely changed."

A refusal earns its place when it names the channel, the reason, and the condition that would reopen it.
