# release

Prepare releases for Codex with explicit boundaries: preflight gates, versioning steps, and tag-ready output.


<!-- BEGIN AGENTOPS OPERATOR CONTRACT -->
<!-- Generated from skills-codex-overrides/catalog.json for release. -->

## Codex Execution Profile

1. Keep the release boundary explicit: everything up to the tag, with validations and changelog evidence called out.
2. Prefer deterministic command sequences and clear rollback points over narrative release notes during execution.
3. Do not run `ao codex stop` after the release commit/tag boundary; finish Codex closeout before `$release` if those artifacts must be part of the release boundary.

## Guardrails

1. Do not blur preparation work with post-tag publishing tasks.

<!-- END AGENTOPS OPERATOR CONTRACT -->
