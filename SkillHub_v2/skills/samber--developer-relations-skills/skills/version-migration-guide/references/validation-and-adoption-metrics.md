# Validating the guide, and measuring whether it worked

Two separate questions. Validation happens before publish and asks "is this document correct?". Measurement happens after and asks "did people actually move?".

## Validation layer 1 - make the guide's own commands executable in CI

The strongest check is mechanical: the snippets in the guide are compiled and run by the build. Rust is the reference implementation: `cargo test --doc` compiles every code block in doc comments into a doctest binary, and `mdbook test` extends the same treatment to book-length prose.

A broken migration snippet then fails the build the way a broken function would. Equivalents exist elsewhere: Go example tests, `pytest --doctest-modules`, and Markdown-testing crates and packages that run fenced blocks out of a README.

The rationale is anti-rot: if the code changes, the docs break; if the docs break, the build fails. A migration guide is the document that rots fastest, because it is written against a version that is still moving when it is published.

This catches a broken command. It does not catch a broken narrative - an entry that compiles fine but sends the reader down the wrong path.

## Validation layer 2 - the cold walkthrough

Have one person who did not write the guide follow it end to end, with no author hand-holding, on a real project. A support engineer, a new hire, or a design-partner customer all work. This is what surfaces the assumed step, the missing prerequisite, and the command that only works from the repository root.

Measure the elapsed time of that run and publish it as the expected effort. Never publish an effort estimate you have not measured: an underestimate is the fastest way to lose a reader mid-upgrade, because they stop trusting every other number in the document at the same moment.

Private betas and early-access cohorts are the same check run with real consumers instead of one reader: treat the mechanism as proven and the specific ritual as yours to design. Multiple API vendors document this as a named pre-GA validation stage rather than an invented step - Auth0/Okta, Klaviyo, Samsara and GitHub each publish a staged beta/early-access/GA lifecycle explicitly framed around gathering feedback and validating changes before general availability, with breaking-change protections applying only once GA is reached.

## Validation layer 3 - run the codemod against a corpus, not one repository

If the upgrade is mechanizable, the codemod is the thing under test, and one test project is not a sample. Google's large-scale change process is the industrial version: the Rosie platform shards a master change along project and ownership boundaries into pieces that are tested, reviewed and submitted independently.

At that scale, tens of thousands of commits come from the tooling rather than from people. Chromium runs a comparable documented workflow for changes touching many owner directories.

Scale it down honestly: run the codemod across every example app, internal consumer and public dependent you can clone, and record what it left behind. That residue list is the most valuable paragraph in the automation section, because it is the part readers cannot discover until their build breaks.

## Measurement - the version-adoption curve is the primary metric

Everything else is a proxy. Read the curve off package-registry downloads, runtime telemetry, or a version question in an ecosystem survey. Published reference points, useful as calibration for what a healthy curve looks like:

| Case                             | What was measured                             | Figure                                       | Source and date                                |
| -------------------------------- | --------------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| Chrome Manifest V3               | Actively maintained extensions on V3          | over 85%                                     | Google blog, May 2024                          |
| Chrome Manifest V3 (independent) | New uploads on V3 after the pause             | roughly nine in ten                          | arXiv 2404.08310, April 2024                   |
| Kubernetes in production         | Hosts on supported versions                   | 78% mainstream, 19% extended, 3% unsupported | Datadog Security Labs, data as of October 2025 |
| React                            | Daily-driver version among survey respondents | React 18.x about 78%                         | State of React 2024                            |
| React                            | Post-19 split                                 | React 19 about 48%, React 18 about 41%       | State of React 2025                            |

Two readings to take from these, not one:

1. A long tail is normal. Even a transition with vendor enforcement behind it sat at 85%, not 100%. Plan the last 15% as a named-account exercise, not as a docs problem.
2. Hard enforcement (brownouts, forced removal, closing the escape hatch) belongs after the curve visibly flattens, not on the date you first announced. Both the Chrome and Kubernetes figures above describe curves that took years to flatten.

## Secondary signals worth tagging to one upgrade

Worth tagging to one upgrade:

- Support-ticket and forum-question volume quoting an upgrade error.
- Docs-page analytics on the guide itself (pageviews, drop-off point, exit rate).
- In-page search queries, which name the entry you failed to write.
- Issue-tracker counts on a migration label, including duplicates.
- Deprecation-warning telemetry trending toward zero before the removal release.

Abandonment shows up as version pinning, rollbacks, and half-finished migrations sitting on branches.

The "was this helpful" widget is low-signal and easily gamed - do not let it stand in for the adoption curve. Page analytics connect to migration outcomes only by inference, so treat those numbers as directional.

Machine-readable support windows (a community EOL aggregator, or a project's own published schedule file) are what downstream CI and compliance checks consume to flag an unsupported version. Publishing yours in that form does more for the long tail than another announcement post.
