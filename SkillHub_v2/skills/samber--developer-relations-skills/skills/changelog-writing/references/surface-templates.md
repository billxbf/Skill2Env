# Surface templates

One release, several artefacts. Writing one text and pasting it everywhere is why changelogs read as too terse in one place and too promotional in another.

| Surface                          | Reader                                              | Budget              | Emphasis                                            |
| -------------------------------- | --------------------------------------------------- | ------------------- | --------------------------------------------------- |
| `CHANGELOG.md`                   | integrator diffing versions                         | one line per change | specification conformance, reference links          |
| Release body on the git host     | upgrader arriving from a tag or a dependency-bot PR | one screenful       | summary, grouped list, contributors, full-diff link |
| Hosted changelog page            | evaluator and existing customer                     | a scroll            | dated entries, media, breaking changes pinned       |
| In-product or email "what's new" | user who follows nothing                            | 3-5 items           | benefit-led, links back to the entry                |

The budgets are this skill's working defaults, not published standards.

## Table of Contents

- [`CHANGELOG.md`](#changelogmd)
- [[2.4.0] - 2026-03-04](#240---2026-03-04)
- [Release body on the git host](#release-body-on-the-git-host)
- [Hosted changelog page](#hosted-changelog-page)
- [March 4, 2026 - Streaming responses](#march-4-2026-streaming-responses)
- [In-product or email "what's new"](#in-product-or-email-whats-new)
- [Deriving one from another](#deriving-one-from-another)
- [Full delivery example](#full-delivery-example)
- [Release notes - v2.4.0 (CHANGELOG.md)](#release-notes-v240-changelogmd)
- [Traceability](#traceability)
- [Excluded (7 changes)](#excluded-7-changes)
- [Needs a human](#needs-a-human)

## `CHANGELOG.md`

Follow the chosen specification exactly. Nothing here is decorative - this file is read by people comparing two versions and by tooling that renders it.

```markdown
## [2.4.0] - 2026-03-04

### Added

- Add `stream()` to the client for token-by-token responses ([#405](url))
- Support Python 3.13 ([#409](url))

### Changed

- **Breaking:** reject payloads over 1 MB in `send()` instead of truncating ([#412](url))
- Raise the default request timeout from 10s to 30s ([#418](url))

### Fixed

- Fix sign-ins failing when several tabs refresh a token at once ([#421](url))
```

## Release body on the git host

Opens with a summary paragraph - the only place in the whole set where prose earns its space. It is what an advocate or newsletter writer quotes, and what a reader sees inside a dependency-update pull request.

```markdown
This release adds streaming responses and raises the default timeout. One breaking
change affects callers that relied on oversized payloads being truncated.

### Breaking

- `send()` now rejects payloads over 1 MB. Chunk the payload or catch
  `PayloadTooLarge`. See the [migration notes](url).

### Added

- Streaming responses via `stream()` (#405)
- Python 3.13 support (#409)

### Fixed

- Concurrent token refresh no longer fails sign-in (#421)

**Full changelog**: v2.3.0...v2.4.0
```

Git hosts can generate a first draft of this from merged pull requests - on GitHub, `.github/release.yml` maps pull-request labels to categories and supports `exclude.labels`, `exclude.authors` and a `*` catch-all. Treat that output as raw material for the editorial pass, never as the finished artefact:

- It is ordered by merge time.
- It is titled by whoever opened the pull request.
- It is blind to what any of it means.

## Hosted changelog page

Reverse-chronological entries, each dated and independently linkable. Breaking changes pinned above the fold. This is the surface where a screenshot or a short code block pays for itself, because the reader is often evaluating rather than upgrading.

````markdown
## March 4, 2026 - Streaming responses

Long completions can now be consumed token by token instead of waiting for the
full response.

```python
for chunk in client.stream(prompt):
    print(chunk.text, end="")
```

**Breaking:** `send()` rejects payloads over 1 MB. [Migration notes](url)

Also in this release: Python 3.13 support, a 30s default timeout, and a fix for
concurrent token refresh. [Full changelog](url)
````

## In-product or email "what's new"

Three to five items, benefit first, no version numbers in the copy. Anyone who wants precision clicks through.

```markdown
**What's new this month**

- Long answers now stream in as they are generated, so you see the first words immediately.
- Slow connections get more time before a request gives up.
- Fixed a sign-in failure that hit people with several tabs open.

[Read the full release notes](url)
```

## Deriving one from another

1. Write the `CHANGELOG.md` entries first; they are the most constrained and force the facts to be right.
2. Derive the release body by adding the summary paragraph and grouping.
3. Derive the hosted page by adding media and context.
4. Derive the in-product note last, from the hosted page, by dropping everything an ordinary user cannot act on.

Going the other direction - starting from the marketing-facing note - loses the detail that cannot be reconstructed later, and tends to leak adjectives into the specification-conformant file.

This derivation order is the same as the production order in SKILL.md § Which surface to produce first, for the same underlying reason: each surface downstream costs more and reaches a reader the one above it missed. Stopping partway leaves the cheap surfaces finished rather than every surface half-written.

## Full delivery example

The notes never travel alone. Hand them over with the traceability table, the exclusion list and the open items, in this shape:

```markdown
## Release notes - v2.4.0 (CHANGELOG.md)

### Added

- Add `stream()` to the client for token-by-token responses ([#405](url))
  ...

## Traceability

| Entry                        | Source              |
| ---------------------------- | ------------------- |
| Add `stream()`               | #405                |
| Fix concurrent token refresh | #421, #422 (merged) |

## Excluded (7 changes)

| Change                       | Reason                                   |
| ---------------------------- | ---------------------------------------- |
| Bump pytest 8.1 → 8.2 (#406) | dev-only dependency, no consumer surface |

## Needs a human

- #425 claims a performance win; no benchmark in the PR. Number omitted.
```
