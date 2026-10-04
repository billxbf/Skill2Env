# Sample policy template

Fill every field. A blank field is a decision the first reviewer will make for you, differently each time. Keep the finished policy in the docs repository next to the contributing guide, not in a wiki nobody opens.

## 1. Scope

- Surfaces covered: docs site / API reference / README / examples directory / blog / in-product help.
- Surfaces explicitly out of scope, and why.
- Effective date and the review cadence (per release, per quarter).

## 2. Coverage - which scenarios get a sample

- Every tier-1 scenario listed by name (one row per scenario, matching the identifier used in the parity matrix).
- Selection rule: frequently used elements and elements that are tricky or easy to misuse come first.
- Exclusion rule: no sample for an obvious point or a contrived scenario. A sample that teaches nothing costs maintenance forever.
- Complexity rule: simple first, complexity only after the common scenarios are covered. Long multi-feature samples belong in tutorials where prose can carry them.

## 3. Anatomy - what every sample must contain

- [ ] All imports and dependencies, explicitly. No elided setup in the published artefact.
- [ ] One sample per file in the source project, so its imports can be validated.
- [ ] Top-level comment: what it does, what it assumes exists, link to the concept page.
- [ ] Explicit client/connection initialization, with a note on reuse, thread-safety and cleanup.
- [ ] Arrange / act / assert shape; nesting no deeper than three levels.
- [ ] One code path. Conditionals, loops and switches only when they _are_ the subject.
- [ ] Minimal parameters: only project-specific values, external paths, and what the test needs. Hard-code the rest.
- [ ] Expected output, in its own block or as a trailing comment.
- [ ] Comments that add context the code lacks - never a restatement of the line above.
- [ ] Language identifier on every fence; `plaintext` when nothing fits.
- [ ] Line length capped (80-100 characters) so samples survive narrow panes.

## 4. Safety - copy-paste and security rules

- [ ] No shell prompt characters (`$`, `#`, `PS>`) in command blocks.
- [ ] Commands and their output in separate blocks, so output cannot be copied with the command.
- [ ] Placeholders in angle brackets (`<YOUR_API_KEY>`), each explained in the surrounding prose.
- [ ] No plausible-looking fake values a reader could paste verbatim; no real-format credentials, account IDs or endpoints.
- [ ] Omissions marked with a comment in the language's own syntax - never `...` or `…`, and never inside a click-to-copy block.
- [ ] No disabled TLS verification, wildcard permissions, or credentials read from source.
- [ ] Input validation shown wherever the sample accepts user input.
- [ ] Destructive commands (delete, drop, force-push, recursive remove) carry an inline guard and a warning above the block.
- [ ] Errors caught specifically and logged; no blanket catch, no silent swallow, no process-killing helper.
- [ ] Sample code license stated when readers are expected to ship the code.

## 5. Parity

- Tier-1 languages (every scenario, tested) - list them and the evidence used to choose them.
- Tier-2 languages (entry path plus top scenarios) - list them.
- Community languages (present, unowned, labelled) - list them.
- What stays identical across languages: sample identifier, scenario, step order, testing approach.
- What may differ: everything else. Idiomatic beats uniform.

## 6. Verification

- Tier assignment rule and where each tier runs.
- Source of truth: samples live in `<path>` and are published into docs by `<mechanism>`.
- CI job: installs `<published artefact>`, runs on `<events>` plus a `<schedule>`, and fails `<the docs build / a required check>`.
- Fixture policy: which accounts/projects tests use, and who cleans up created resources.
- Freshness window: maximum age of a sample's last **successful run** before it is marked stale on the page.

## 7. Ownership

| Surface                 | Owner | Fix SLA for a red sample |
| ----------------------- | ----- | ------------------------ |
| Quickstart / auth path  |       |                          |
| API reference snippets  |       |                          |
| Examples repository     |       |                          |
| Blog and archived posts |       |                          |

Archived content deserves an explicit rule: freeze it with a version banner or delete it. A five-year-old post whose sample still ranks in search does more damage than a missing page.

## 8. Exceptions

One row per accepted violation: sample, rule waived, reason, expiry date. An exception without an expiry is a policy edit made quietly.
