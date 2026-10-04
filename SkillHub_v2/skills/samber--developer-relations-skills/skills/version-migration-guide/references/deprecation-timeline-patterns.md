# Deprecation timelines

## Warning-level ladder

Grade a deprecation by how loudly it fails, and escalate it across releases rather than jumping straight from silence to removal. Node.js's four levels are the most complete published example:

| Level                 | Behavior                                                      | Use when                                                               |
| --------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Documentation-only    | No runtime effect; opt-in warning behind a flag               | The replacement exists but adoption has not started                    |
| Application-code only | Warning on first use, suppressed for code inside dependencies | Most deprecations - the application author is the only one who can act |
| Runtime, all code     | Warning on first use, dependencies included                   | Close to removal, or the dependency ecosystem must be pushed           |
| End-of-life           | Removed                                                       | The removal release                                                    |

Warning only application code first is the detail that makes the ladder tolerable. A warning raised inside a dependency the reader cannot patch teaches them to ignore warnings, which is exactly the habit the removal release depends on them not having.

## Window length

Express the window in **releases**, not months, for open-source and library audiences: readers upgrade on their own cadence, and a release count survives a slipped schedule. Django's rule is the well-worn reference - deprecated in N, still warning in N+1, removed in N+2, which lands around 12-18 months.

Use **dates** for contractual and hosted-API audiences, because those readers schedule against calendars and contracts, not your tags. Publish both when both apply.

State exceptions explicitly. A security-driven accelerated removal is legitimate; an unannounced one is what makes readers stop believing the policy.

## Stable identifiers

Give every deprecation an identifier that never changes: `DEP0042`, `acme-deprecate-send-string`, or a permanent anchor. Node.js pairs each `DEP0XXX` with a version-by-version history table; Ember pairs each deprecation with an `until` version plus a stable ID.

Identifiers let lint rules, codemods, and support replies point at one deprecation instead of a page. They also make a _revocation_ survivable: a revoked deprecation keeps its identifier and gets a status change rather than disappearing, so anyone who linked to it still lands somewhere truthful.

## Timeline table

Publish one table per major, organized by removal version so a reader jumping several versions reads one section per hop:

```markdown
| Deprecated API        | Replacement                    | Warning level in 3.x     | Removed in |
| --------------------- | ------------------------------ | ------------------------ | ---------- |
| `client.send(string)` | `client.send(Payload)`         | Runtime (3.0)            | 4.0        |
| `AcmeError.code`      | `AcmeError.reason`             | Documentation-only (3.2) | 5.0        |
| `--legacy-parser`     | none (parser is always strict) | Runtime (3.0)            | 4.0        |
```

Each row needs the replacement or an explicit "none". A row without one is an unfinished deprecation: nobody can act on it, so it will still be in use on removal day.

## Reverse view

Keep a second, cumulative page organized by _removal_ version ("what disappears in 4.0") separate from the per-release notes. Readers arrive with two different questions ("what do I have to fix before 4.0" and "what did 3.2 deprecate") and one ordering cannot serve both.
