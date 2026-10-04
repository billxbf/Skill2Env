# Verification patterns

The purpose of verification is to move a sample's failure from the reader's machine into CI. Everything below serves that one move.

## Why it works

Ecosystems that made examples executable did it for the same reason: an example that is not run drifts silently. Rust's documentation tests compile and run every fenced block in a doc comment, so an outdated example fails the build. Go's testable examples compile with the package and assert stdout against an `// Output:` comment; the language team's stated payoff is that executable documentation "guarantees that the information will not go out of date as the API changes".

Manny Silva's **Docs as Tests** generalizes it beyond code: documentation should not just inform, it should also verify - every documented step becomes a test case against the real product surface.

## Choosing a source of truth

Three patterns, in decreasing reliability. Pick one per surface and write it into the policy.

**1. Extract from tested source.** Samples live in a real project that compiles, lints and tests; the docs pull a named region at build time.

- Give each region a globally unique, snake_case identifier prefixed by the product area, identical across languages.
- Wrap the maximum useful code - a region that starts after the imports publishes a sample the reader cannot run.
- Strongest guarantee, highest setup cost. Choose it for anything on the adoption path.

**2. Test what is embedded.** Samples stay in the Markdown; a CI step extracts every fenced block, reassembles it into a runnable file with the declared setup, and executes it.

- Cheapest to adopt on an existing corpus and the only option when docs are contributed by non-engineers.
- Needs a per-block metadata convention (tier, setup fixture, expected output) carried in the fence info string or an adjacent comment.
- Weak at multi-block sequences; be explicit about which blocks share state.

**3. Generate from a spec.** Per-language request/response snippets generated from the API description.

- Guarantees parity and freshness for reference pages at near-zero marginal cost per language.
- Expresses single calls only. Multi-step, idiomatic usage still needs hand-written, tested samples.

A sample pasted into prose by hand belongs to none of these. That is the default state of most corpora and the thing the policy exists to eliminate.

## Hiding setup without breaking runnability

Readers want the three interesting lines; the test needs the whole file. Every workable scheme separates the two: the tested artefact is the complete file, the published artefact is a region or a filtered view of it.

Rustdoc does this with `#`-prefixed lines that compile but do not render. Reproduce the property, whatever the mechanism - never publish a fragment that was made runnable by deleting nothing and hoping.

## CI shape

- **Install the published artefact.** Registry package, released container, deployed endpoint - whatever the reader will have. A suite that builds from the working tree passes on code no reader can install yet.
- **Split hermetic from integration.** Hermetic (mocked or local) runs on every pull request for speed. Integration runs against the real service, because that is where the breakage actually originates.
- **Run on a schedule, not only on commit.** Samples break when the _service_ changes, not when the docs repo changes. A nightly or weekly run is what catches server-side drift.
- **Fail something that blocks.** The docs build or a required check. An advisory job goes red and stays red.
- **Report per sample, not per suite.** The output the maintainer needs is "which sample, which page, which line", so the finding can be routed to its owner.

## Fixtures

Untended fixtures are the usual reason a sample suite gets disabled six months in.

- Dedicated test accounts/projects per language, never a shared human account.
- Teardown in the test, plus a scheduled sweeper for what teardown missed - a suite that leaks resources eventually costs money and gets switched off.
- Deterministic naming for created resources (prefix + run id) so the sweeper can identify them safely.
- Secrets from the CI secret store, never from the sample. The sample shows a placeholder; the harness injects the value.

## Freshness signals

Track these per sample and expose the worst of them on the page:

- Age of the last **successful run**, not the last edit - an edited sample nobody ran is not fresher.
- Version pinned in the sample versus the current released version.
- Symbols referenced that no longer exist in the public API surface.
- Issues or tickets quoting the sample verbatim.

## Degrading gracefully

When you cannot execute anything in the current environment - no CI access, no runtime for that language - do not silently downgrade the audit. Produce the tier assignments, the mechanical lint results, and a written verification plan the team can implement, and label every unexecuted sample's status as _unverified_ rather than _passing_.
