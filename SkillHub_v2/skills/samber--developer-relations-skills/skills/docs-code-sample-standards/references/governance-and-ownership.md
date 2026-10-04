# Governance and ownership

Ownership stated in a wiki decays. Ownership encoded in the repository holds, because the build enforces it. This file covers the three ownership models in production, the metadata layer that makes a corpus governable, and the gates that turn a policy into a merge requirement.

## Contents

- Choosing an ownership model
- Intake and prioritisation
- Metadata-driven governance
- The enforcement layer
- Migration order

## Choosing an ownership model

| Model                                | Who authors                                                                 | Strengths                                                                        | Costs                                                           | Fits                                                   |
| ------------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------ |
| Dedicated examples team              | A standing team separate from product engineering and from the docs writers | Highest and most consistent quality; per-language standards actually get applied | Slow intake; new examples queue behind maintenance              | Large multi-language SDK surfaces                      |
| DevRel/community with expert vetting | Contributors and advocates, reviewed by named experts                       | Breadth and scenario variety; catches use cases the vendor would not think of    | Needs paid capacity behind it or the backlog rots               | Catalogue-style example galleries                      |
| Product engineers co-own             | The team that shipped the feature                                           | Samples stay current by construction; no handoff lag                             | Depends entirely on the engineering org counting docs as "done" | Single-product APIs with a strong docs-as-code culture |

Real practice, for calibration:

- AWS runs the dedicated-team model with a separate documentation team alongside it, taking all example requests through a public issue tracker and moving accepted work across a public roadmap (Wish List → Backlog → In Progress → Recently Completed).
- Twilio's community catalogue is vetted by named experts, and its growth was backstopped by _contracted_ senior engineers - one engagement covered authoring 10 new apps and maintaining 45 existing ones. Treat "community-maintained" as a funding model, not a free one.
- Stripe has product engineers co-own the docs for what they ship, with docs part of the definition of done and reflected in performance reviews.

Pick one per surface rather than one for the whole corpus. An examples repository and an API reference rarely deserve the same model.

## Intake and prioritisation

Publish the queue rules, whatever the model. AWS states two that generalise well:

- Large examples need requesting well ahead of the date they are needed - its stated guidance is at least two months.
- "Bug fixes and security issues take priority over new code examples."

That second rule is the one teams skip, and skipping it is how a corpus accumulates hundreds of samples nobody can fix. Write it into the policy's ownership section with a fix SLA per surface.

## Metadata-driven governance

A governed corpus keeps samples in compilable source and describes each one in structured metadata, so the docs build can pull the right snippet for the right page in the right language.

Two mechanisms, always both:

**Snippet tagging.** Paired markers delimit the publishable region inside a real source file. Give each tag a globally unique, hierarchical, dotted or snake_case identifier carrying language, product area and example name, and keep it identical across languages so the parity matrix can key on it.

**Example metadata.** One record per example, holding at minimum: title, short title, synopsis, category, the languages it exists in, the SDK version it targets, the source location, and the snippet tags it composes. The tag alone cannot tell a renderer which page a snippet belongs on or which language variant to select - that is what the metadata record is for.

Transclusion is the unifying pattern underneath: keep canonical code in real, compilable source, mark a region, inject it at build time. Every major docs toolchain has a form of it - paired start/end markers, line-range includes, or an include directive naming a file plus a marker.

The published sample is never hand-typed prose; it is a _view_ into a file CI already validates. That is what turns "keep samples accurate" from an editorial promise into a build step.

## The enforcement layer

Once samples are source code, ordinary code governance applies to them. Build these as blocking gates, not advisory checks:

- **Code owners on sample paths.** Map per-language or per-product directories to required reviewers, so a pull request touching Go examples cannot merge without a Go-example owner's approval.
- **Metadata schema validation.** Reject a record with missing or malformed fields before it reaches the renderer.
- **Referenced-file existence checks.** Assert that every snippet file named in metadata still exists - this is what catches a moved or deleted source file before the docs ship a blank.
- **Secret scanning over the whole corpus.** Scan for a disallowed word list and for credential-shaped literals (long fixed-length base64/hex strings, known token prefixes, private-key headers). Run it in the same tool that validates structure, so there is one exit code to gate on.
- **Non-zero exit fails the check.** Post the failure on the pull request. A validator whose output nobody sees is documentation of a problem, not a gate against it.
- **Snippet-sync assertions.** Where Markdown embeds extracted code, re-run the extractor in CI and fail on drift, so an edit to the source file cannot silently desynchronise the published copy.
- **Per-language standards.** Encode the conventions each language's samples must follow - required first parameters, return shapes, mandatory doc comments, module layout, even formatting rules justified by how the snippet will render rather than by language convention alone. Put them where contributors will find them, next to the code.

External contributions deserve the same gate as internal ones. AWS describes outside snippet sources as "tributaries, flowing into the 'river' of AWS Documentation" - the validator is the checkpoint every tributary passes through.

## Migration order

When a corpus has no governance at all, sequence it this way - each step makes the next cheaper:

1. **Census and secret scan.** Find the credential leaks first; they are the only findings that cannot wait.
2. **Automated compile/run gates** on whatever is already testable, at 100% coverage.
3. **Move samples into compilable source** and publish by transclusion. This is the single highest-leverage investment for a corpus with no region-tag or metadata coverage, because every later guarantee depends on it.
4. **Add metadata records and schema validation.**
5. **Assign code owners and fix SLAs**, once the paths are stable enough to own.

Reversing steps 3 and 5 is the common mistake: assigning owners to hand-pasted Markdown gives them responsibility without any mechanism to discharge it.
