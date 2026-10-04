# Guide outlines

Two skeletons and one anti-pattern. Both skeletons follow the same order for the same reason: triage before work, floors before code, automation before manual labour.

## Table of Contents

- [Library / SDK / framework outline](#library-sdk-framework-outline)
- [Before you start](#before-you-start)
- [Requirements](#requirements)
- [Install](#install)
- [Automated migration](#automated-migration)
- [Breaking changes](#breaking-changes)
- [New deprecations](#new-deprecations)
- [Behavior changes](#behavior-changes)
- [Type-level changes](#type-level-changes)
- [Housekeeping](#housekeeping)
- [Troubleshooting](#troubleshooting)
- [Full changelog](#full-changelog)
- [Hosted API outline](#hosted-api-outline)
- [What changes and when](#what-changes-and-when)
- [Surfaces and versions](#surfaces-and-versions)
- [Test before you switch](#test-before-you-switch)
- [Breaking changes](#breaking-changes)
- [Webhook payload changes](#webhook-payload-changes)
- [Data-layer impact](#data-layer-impact)
- [Cutover and rollback](#cutover-and-rollback)
- [Troubleshooting](#troubleshooting)
- [Anti-pattern outline](#anti-pattern-outline)
- [What's new in v3 <- marketing section on a work document](#whats-new-in-v3---marketing-section-on-a-work-document)
- [Why we rebuilt the core <- rationale that belongs in a blog post](#why-we-rebuilt-the-core---rationale-that-belongs-in-a-blog-post)
- [Breaking changes <- alphabetical, no detection signals](#breaking-changes---alphabetical-no-detection-signals)
- [FAQ <- the real migration steps, scattered](#faq---the-real-migration-steps-scattered)
- [Requirements <- floors discovered after the code examples](#requirements---floors-discovered-after-the-code-examples)

## Library / SDK / framework outline

```markdown
# Upgrading from v2 to v3

<!-- 1. Scope: which versions, which packages, expected effort (measured, not guessed) -->

This guide covers acme-client 2.x → 3.0 for the Node and browser packages.
A cold upgrade of a typical service took 40 minutes.

## Before you start

<!-- 2. Path shape, stated first, including any known-bad intermediate version -->

Upgrade to 2.9 first and run your test suite. Every change below emits a
deprecation warning in 2.9, so the warning output becomes your work list.
Do not stop on 2.8: it ships a connection-pool regression fixed in 2.9.

## Requirements

<!-- 3. Floors -->

- Node >= 20.19
- TypeScript >= 5.4
- acme-adapter >= 1.4 (peer dependency)

## Install

<!-- 4. Copy-paste, every package manager, pinned -->

## Automated migration

<!-- 5. All-changes recipe, per-change commands, coverage boundary -->

## Breaking changes

<!-- 6. One entry per change, ordered by blast radius -->

### Changed: configuration moved to acme.config.ts

### Removed: string argument to send()

### Changed: errors are AcmeError instead of Error

## New deprecations

<!-- 7. Still works, will not in v4 - with the removal version -->

## Behavior changes

<!-- 8. Nothing breaks, but output differs: defaults, ordering, timeouts, messages -->

## Type-level changes

<!-- 9. Separate from runtime changes; different reader, different failure mode -->

## Housekeeping

<!-- 10. What is now dead: config that became a default, workaround flags,
     dependency overrides, patches, packages the framework now bundles -->

## Troubleshooting

<!-- 11. Keyed by the literal error text -->

## Full changelog

<!-- 12. Traceability only, never the migration path -->
```

## Hosted API outline

Same spine, different middle. The reader is changing behavior in production, not in a build.

```markdown
# Migrating to the 2026-07-29 API version

## What changes and when

<!-- Deadline, notice window, what happens if nothing is done -->

## Surfaces and versions

<!-- Matrix: server SDK, browser bundle, mobile SDKs, webhooks - which move together -->

## Test before you switch

<!-- The per-request pinning header, with a full example request -->

## Breaking changes

<!-- Same six-part entries, grouped by product area -->

## Webhook payload changes

<!-- Separate: consumers cannot pin an inbound request -->

## Data-layer impact

<!-- Identifier lengths, collation, enum values, stored payload shapes -->

## Cutover and rollback

<!-- Who flips the default, when, how to revert, how long the old version stays up -->

## Troubleshooting
```

## Anti-pattern outline

```markdown
# v3 Release

## What's new in v3 <- marketing section on a work document

## Why we rebuilt the core <- rationale that belongs in a blog post

## Breaking changes <- alphabetical, no detection signals

## FAQ <- the real migration steps, scattered

## Requirements <- floors discovered after the code examples
```

Four defects, in descending cost:

- Floors at the bottom.
- Migration steps hidden in an FAQ.
- Alphabetical ordering.
- A launch narrative occupying the screen the reader needed for work.

A guide is read by someone whose build is already broken; it earns nothing by opening with a celebration.
