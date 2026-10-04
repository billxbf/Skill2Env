# Changelog format specifications

Two published specifications compete. Pick one, state it at the top of the file, and stay on it. Mixing them is what produces changelogs where the category means something different every release.

## Table of Contents

- [Keep a Changelog 1.1.0](#keep-a-changelog-110)
- [Common Changelog](#common-changelog)
- [[3.1.0] - 2026-03-04](#310---2026-03-04)
- [Choosing](#choosing)
- [Mapping between them](#mapping-between-them)
- [Semantic versioning correspondence](#semantic-versioning-correspondence)

## Keep a Changelog 1.1.0

The permissive, widely adopted one. Good default for application and product changelogs.

Guiding principles, verbatim from the specification:

- "Changelogs are _for humans_, not machines."
- There should be an entry for every single version.
- The same types of changes should be grouped.
- Versions and sections should be linkable.
- The latest version comes first.
- The release date of each version is displayed.
- Adherence to Semantic Versioning should be mentioned.

Six categories:

| Category     | Use for                                       |
| ------------ | --------------------------------------------- |
| `Added`      | New features, endpoints, parameters, commands |
| `Changed`    | Changed behaviour of existing functionality   |
| `Deprecated` | Features scheduled for removal                |
| `Removed`    | Features now gone                             |
| `Fixed`      | Bug fixes                                     |
| `Security`   | Vulnerability patches                         |

Mechanics it fixes:

- Keep an `## [Unreleased]` section at the top. It lets readers see what is coming, and makes cutting a release a rename rather than a rewrite.
- Dates in ISO 8601 (`YYYY-MM-DD`). Regional formats are ambiguous across an international readership.
- Pulled releases keep their heading and gain a loud tag: `## [0.0.5] - 2014-12-13 [YANKED]`.
- Named anti-patterns: dumping commit log diffs, omitting deprecations, ambiguous dates.

File header the specification expects:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
```

## Common Changelog

The strict, reference-heavy one. Good default for libraries and SDKs whose readers diff versions.

Differences that decide the choice:

- Exactly four categories, in this fixed order: `Changed`, `Added`, `Removed`, `Fixed`. No `Deprecated`, no `Security` - both fold into `Changed`, so the entry text must carry the whole signal.
- Entries start with a present-tense imperative verb: "Add `write()` method", not "Added the write method".
- Breaking changes are prefixed `**Breaking:**`, or `**<subsystem> (breaking):**`, and listed first inside their category.
- Every change must reference a commit and should reference the pull request: `([#194](url))`, ``([`53bd922`](url))``. Authors, if listed, follow the references.
- No `Unreleased` section. The file only ever describes shipped releases.
- Contextual warnings use a free-text notice above the categories instead of a `[YANKED]` tag.

Its explicit include list is the useful half, because these are the changes teams wrongly drop:

- Refactors (they carry side effects).
- Runtime-environment changes.
- Code-style changes that adopt new language features.
- Newly documented behaviour.

Its exclude list: dotfiles, development-only dependency updates, minor style changes, documentation formatting.

```markdown
## [3.1.0] - 2026-03-04

### Changed

- **Breaking:** reject payloads over 1 MB in `send()` ([#412](https://github.com/owner/name/pull/412))
- Retry idempotent requests up to 3 times ([#418](https://github.com/owner/name/pull/418))

### Added

- Add `stream()` for token-by-token responses ([#405](https://github.com/owner/name/pull/405))
```

## Choosing

| Situation                                                         | Pick                                         |
| ----------------------------------------------------------------- | -------------------------------------------- |
| Library or SDK, readers diff versions, PRs are the unit of change | Common Changelog                             |
| Application or hosted product, mixed audience, screenshots likely | Keep a Changelog                             |
| Existing file already follows one                                 | That one - consistency beats the better spec |
| Security advisories published in the changelog itself             | Keep a Changelog (it has the category)       |
| Team wants machine-validated structure                            | Common Changelog (validators exist for it)   |

## Mapping between them

When migrating a file or deriving one from the other:

| Keep a Changelog | Common Changelog                                                    |
| ---------------- | ------------------------------------------------------------------- |
| `Added`          | `Added`                                                             |
| `Changed`        | `Changed`                                                           |
| `Fixed`          | `Fixed`                                                             |
| `Removed`        | `Removed`                                                           |
| `Deprecated`     | `Changed`, entry text must name the replacement and removal version |
| `Security`       | `Fixed`, entry text must name the advisory or CVE                   |

Never rewrite historical releases when switching specifications. Start the new format at the next release and leave the past as shipped - a rewritten history breaks every deep link into the file.

## Semantic versioning correspondence

The version number is a communication channel of its own, and the entry set must agree with it.

| Bump  | Allowed entries                                                    |
| ----- | ------------------------------------------------------------------ |
| Major | Anything, including `Removed` and breaking `Changed`               |
| Minor | `Added`, non-breaking `Changed`, `Deprecated`, `Fixed`, `Security` |
| Patch | `Fixed`, `Security`, and non-breaking internal `Changed`           |

Pre-1.0 projects have no such guarantee, and calendar-versioned projects have none either. Both must carry the compatibility statement in prose instead: state once, outside the release notes, which kinds of change count as backward-compatible.

Stripe's upgrade documentation is the reference example of that statement. It publishes the exhaustive list of changes it treats as backward-compatible, and tells integrators to code defensively against exactly those:

- New resources.
- New optional request parameters.
- New response properties.
- Reordered response properties.
- Changed opaque string formats.
- New event types.

Everything outside the list becomes a named, dated major version with its own change list. Publishing the contract once means each release note is read against it, instead of re-litigating "is this breaking?" per entry.
