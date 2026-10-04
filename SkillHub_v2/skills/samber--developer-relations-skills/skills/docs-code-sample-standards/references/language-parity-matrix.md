# Language parity matrix

## What parity means

Parity is a claim about coverage and behaviour, never about line-by-line translation. Across every language version of a sample, three things stay identical:

- the sample identifier,
- the scenario it demonstrates and the order of its steps,
- the testing approach applied to it.

Everything else may differ, because idiomatic style outranks cross-language uniformity. A Python sample that reads like transliterated Java satisfies a diff and fails the reader.

## Tiering the languages

Uniform coverage across every SDK is a promise no team keeps. Tier instead, and publish the tiers.

| Tier      | Commitment                                                                             | Chosen from                                               |
| --------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Tier 1    | Every documented scenario, tested                                                      | Actual download/telemetry share and support-ticket volume |
| Tier 2    | Entry path (install, auth, first call) plus top scenarios; deeper pages link to tier 1 | Meaningful but secondary usage                            |
| Community | Present, unowned, labelled untested, with the maintenance expectation stated           | Contributed, not staffed                                  |

Choosing tiers from real usage rather than team preference is the whole point - most corpora over-serve the language the API was first written in, usually the maintainer's own, and under-serve the one most readers arrive with.

## The matrix

Rows are scenarios (one per sample identifier), columns are the languages. Cell values:

- `T` tested - exists and CI runs it
- `P` present - exists, untested
- `M` missing
- `S` stale - pinned to an unsupported version, or last successful run older than the freshness window

```
Scenario                      | py | ts | go | java | rb
------------------------------|----|----|----|------|----
auth_api_key                  | T  | T  | T  | T    | P
storage_upload_file           | T  | T  | P  | M    | M
storage_signed_url            | T  | M  | M  | M    | M
webhooks_verify_signature     | T  | T  | T  | S    | M
```

Parity coverage = `T` cells ÷ (scenarios × tier-1 languages). One number, recomputable each release, and it separates the two failure shapes a raw sample count hides: samples that do not exist, and samples that exist but nothing runs.

Read the matrix by row and by column. A sparse **row** means a scenario the docs only support in one language - usually a feature shipped with a single SDK. A sparse **column** means a language tiered above what the team actually staffs; either fund it or demote it.

## Drift patterns to check

- **Different outcome**: one language's sample creates a resource the others only read.
- **Auth divergence**: one uses an environment variable, another a key file path, a third an inline literal.
- **Error handling in one language only**, usually the one whose sample was written last.
- **Version skew**: samples pinned to different major versions of the same SDK across languages.
- **Orphan scenario**: a sample exists in one language with no matching identifier anywhere else - either the scenario matters (add it) or it does not (delete it).
- **Structural drift**: the same identifier demonstrating a different step order, so a reader switching languages cannot follow the same prose.

## Generated versus hand-written

Generated snippets guarantee parity and freshness for single calls on reference pages, at near-zero cost per added language. Hand-written samples carry multi-step idiomatic usage and drift per language. Most corpora need both - so state in the policy which surface uses which, or the team hand-maintains what a generator already covers, and the two sets disagree in public.
