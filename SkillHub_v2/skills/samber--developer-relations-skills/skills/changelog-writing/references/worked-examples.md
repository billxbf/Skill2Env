# Worked examples

Three cases: a clean conventional history, a messy one, and a breaking release. Each shows the raw material, the reduction, and the finished entries.

## Contents

- [Case 1 - Clean history](#case-1--clean-history)
- [Case 2 - Messy history](#case-2--messy-history)
- [Case 3 - Breaking release](#case-3--breaking-release)
- [Entry rewrite pairs](#entry-rewrite-pairs)

## Case 1 - Clean history

Raw material, `v2.3.0..HEAD`:

```
feat(client): add stream() for incremental responses (#405)
chore(deps): bump pytest 8.1.0 -> 8.2.0 (#406)
ci: cache uv downloads (#407)
feat(build): support python 3.13 (#409)
fix(auth): serialize concurrent token refresh (#421)
fix(auth): add missing lock release (#422)
style: reformat with ruff 0.5 (#423)
perf(http): reuse connection pool across clients (#425)
```

Reduction:

- `#421` and `#422` are one outcome - the second fixes the first before release. One entry.
- `#406`, `#407`, `#423` have no consumer surface. Excluded, and the exclusion is stated to the user.
- `#425` is internal _and_ observable: connection reuse changes behaviour under concurrency. Keep it, but only claim what is measured.
- `#409` looks like build tooling and is not: a new supported runtime is what half the readers came for.

Finished:

```markdown
### Added

- Add `stream()` to the client for token-by-token responses ([#405](url))
- Support Python 3.13 ([#409](url))

### Changed

- Reuse one connection pool across client instances, reducing socket churn in
  multi-client processes ([#425](url))

### Fixed

- Fix sign-in failures when several tabs refreshed a token at once ([#421](url))
```

Note what did _not_ happen: `#425` did not become "40% faster connection handling". No benchmark accompanied the pull request, so no number is claimed.

## Case 2 - Messy history

Raw material, squash merges with no convention:

```
Merge pull request #88 from acme/fix-stuff
wip
address review
fix tests
Update index.ts
Merge pull request #91 from acme/dark-mode
final fix
```

Commit subjects carry no information. Work from the pull requests and the diff instead.

1. Read the pull-request titles and bodies: `#88` "Handle expired sessions on reconnect", `#91` "Dark mode".
2. Read the diffstat per merge to see what each actually touched.
3. Confirm with the user before writing: "Is `#88` user-visible - did users see an error, or was it only logged?"

Finished, after confirmation:

```markdown
### Added

- Add a dark theme, selectable in Settings and remembered per device ([#91](url))

### Fixed

- Reconnect cleanly after a session expires instead of showing a blank screen ([#88](url))
```

The confirmation step is not optional here. Without it, "handle expired sessions" could equally be a silent internal retry, and an entry claiming a visible fix would be wrong.

## Case 3 - Breaking release

Raw material:

```
feat(api)!: reject payloads over 1MB in send() (#412)
feat(api): deprecate legacy() in favour of send() (#414)
fix(api): remove truncation warning log (#415)
```

The breaking entry gets all three parts - what breaks, who it hits, what to do:

```markdown
## [3.0.0] - 2026-03-04

### Changed

- **Breaking:** `send()` now rejects payloads over 1 MB instead of silently
  truncating them. Affects callers that relied on truncation - chunk the payload
  or catch `PayloadTooLarge`. See the [v3 migration guide](url) ([#412](url))
- Deprecate `legacy()` in favour of `send()`. `legacy()` keeps working through
  the 3.x line and is removed in 4.0.0 ([#414](url))
```

`#415` produces no entry: removing a log line that only fired on the now-impossible truncation path has no consumer surface once `#412` shipped.

The deprecation names both the replacement and the removal version. The removal, when it comes in 4.0.0, gets its own `Removed` entry that points back here.

Counter-example - the same release written badly:

```markdown
### Changed

- Improved payload handling for better reliability
- Various API improvements and cleanups
```

Both lines are technically true and operationally useless. The first hides a breaking change behind a benefit word; the second hides a deprecation. A reader upgrading on these notes discovers the change in production.

## Entry rewrite pairs

| Raw                                                                       | Entry                                                                                      |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `Implemented Redis caching layer for dashboard API endpoints (PROJ-4471)` | Dashboards load noticeably faster on accounts with large workspaces.                       |
| `Refactored auth middleware to fix race condition`                        | Fixed sign-ins that could fail when several tabs refreshed a token at once.                |
| `Bump minimum Node to 20`                                                 | **Breaking:** require Node.js 20 or later. Node 18 reached end of life.                    |
| `Update error copy`                                                       | Error messages now name the failing field; scripts matching on the old text need updating. |
| `Add feature flag for new editor`                                         | _(no entry - flag defaults off, nothing observable yet)_                                   |
| `Revolutionary new streaming experience, rebuilt from the ground up!`     | Add `stream()` to the client for token-by-token responses.                                 |
