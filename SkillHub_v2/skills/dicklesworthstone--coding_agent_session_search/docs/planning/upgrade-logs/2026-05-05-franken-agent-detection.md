# Dependency Upgrade Log

**Date:** 2026-05-05 | **Project:** coding_agent_session_search | **Language:** Rust

## Summary

- **Updated:** 1
- **Skipped:** 0
- **Failed:** 0
- **Needs attention:** 1

## Updates

### franken-agent-detection: f7eddabae5026d5bdc88f0d295a9f2870c24e090 -> 029253c450702a1714fca4fb34ba290f2cc71d87

- **Reason:** Pull in the OpenCode v1.2 SQLite connector performance fix for GitHub issue #210.
- **Research:** Reviewed sibling commits:
  - `2b39527` batches OpenCode SQLite messages and parts instead of using the previous per-session/per-message N+1 query shape.
  - `029253c` adds regression coverage for bulk SQLite message grouping.
- **Breaking changes:** None identified for cass; the public crate version remains `0.1.3` and the enabled feature set is unchanged.
- **Update command:** `cargo update -p franken-agent-detection --precise 029253c450702a1714fca4fb34ba290f2cc71d87`
- **Resolver changes:** Cargo advanced several `windows-sys` lockfile edges to `0.61.2`.
- **Tests:** `cargo check --locked --all-targets` passed.

## Needs Attention

### itertools direct wildcard edge

- **Observation:** After the FAD update, Cargo selected `itertools 0.13.0` for cass's direct wildcard dependency because `criterion v0.8.2` requires `itertools ^0.13`.
- **Attempted update:** `cargo update -p itertools@0.13.0 --precise 0.14.0`.
- **Result:** Cargo refused the update because `criterion v0.8.2` requires `itertools = "^0.13"`.
- **Action:** Left the resolver-selected lockfile intact rather than adding a manifest exception against this repo's wildcard dependency policy.
