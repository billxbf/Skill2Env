# Audit rubric, templates, and benchmark checklist

## Severity tiers

- **Blocker** - an integrator cannot complete a correct call without guessing or reading source: undocumented endpoint, undocumented required parameter, undocumented error code with no cause/fix, documented endpoint that no longer exists, no spec at all.
- **Major** - the call succeeds but reliability or self-service suffers: missing response example, missing 4xx documentation, missing parameter constraints or example, snippet absent for a shipped language, no version statement, retry/idempotency safety unstated.
- **Minor** - polish gaps: stale prose, quadrant drift (tutorial/explanation content on a reference page), inconsistent terminology between endpoints, broken anchors.

## Census template (step 1)

| Operation                      | In spec? | In published reference? | In SDKs? | Discrepancy                                |
| ------------------------------ | -------- | ----------------------- | -------- | ------------------------------------------ |
| `POST /v1/payments`            | yes      | yes                     | yes      | -                                          |
| `GET /v1/payments/{id}/events` | yes      | **no**                  | yes      | live + SDK-exposed, undocumented - blocker |
| `DELETE /v1/drafts/{id}`       | no       | yes                     | no       | documented but removed - blocker           |

Both directions matter:

- Live-but-undocumented surface forces guessing.
- Documented-but-removed endpoints destroy trust in every page around them.

Probe beyond the spec where feasible (gateway logs, SDK internals, support tickets naming unknown endpoints) - production APIs have been shown to carry undocumented-but-valid routes even when a spec exists.

## Per-endpoint rubric (step 2)

Grade every operation on each row; every "no" becomes a finding at the listed severity.

| #   | Row                    | Pass condition                                                                                                    | Severity if failed                                               |
| --- | ---------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1   | Description            | Operation has a purpose statement in the reference (what it does, not how the product works)                      | Blocker                                                          |
| 2   | Parameters - presence  | Every spec parameter appears: name, location (path/query/header/body), type                                       | Blocker                                                          |
| 3   | Parameters - depth     | Each carries required/optional, constraints (min/max, format, enum values, disallowed values), and a sample value | Major                                                            |
| 4   | Request example        | At least one complete, valid request body/call shown                                                              | Major                                                            |
| 5   | Response example       | At least one realistic success response body shown                                                                | Major                                                            |
| 6   | Response codes         | Every status the endpoint can return is listed, including at least one 4xx                                        | Blocker                                                          |
| 7   | Error codes            | Every error code documented with its cause AND its fix, not just its value                                        | Blocker                                                          |
| 8   | Per-language snippets  | One sample per shipped SDK language, exercising the SDK - not relabeled curl                                      | Major                                                            |
| 9   | Try-it affordance      | The endpoint is executable from the page (console, runnable collection), ideally with pre-filled test credentials | Minor (Major if the platform already offers one and it's broken) |
| 10  | Version statement      | The page states which API version it documents and links the migration guide                                      | Major                                                            |
| 11  | Idempotency/retry note | States whether the operation is idempotency-safe and how retries behave                                           | Major                                                            |
| 12  | Ordering constraints   | Any invocation-ordering requirement ("create X before Y") is stated                                               | Major                                                            |
| 13  | Auth requirements      | Required scopes/permissions for this operation are stated                                                         | Major                                                            |
| 14  | Quadrant shape         | Page is lookup-shaped; worked examples fine, explanatory digressions flagged                                      | Minor                                                            |
| 15  | Currency               | No references to removed fields, old versions, renamed products                                                   | Minor                                                            |

Rows 7, 11, and 12 are the ones auditors habitually skip - error surface, retry safety, and ordering constraints are exactly the omissions research finds most neglected.

## Report template (step 3)

```markdown
# API Reference Audit - {API name} - {date}

## Verdict

{One paragraph: coverage headline numbers, the drift diagnosis
(spec-generated vs hand-maintained - if hand-maintained, state that every
finding below will recur until stage 1 of the rollout is done), and the
recommended remediation tier.}

## Coverage scores

| Dimension                                               | Score       | Gate |
| ------------------------------------------------------- | ----------- | ---- |
| Operations documented                                   | 41/44 (93%) | 100% |
| Parameters fully documented                             | 78%         | 100% |
| Operations with all responses documented (incl. ≥1 4xx) | 61%         | 100% |
| Error codes with cause+fix                              | 34%         | 100% |
| Snippet parity (operations x languages)                 | 55%         | 100% |

## Findings by severity

### Blockers

- {endpoint} - {rubric row} - {what's missing, and what an integrator does instead}

### Major

...

### Minor

...

## Benchmark comparison

{Where the reference stands against the Stripe/Twilio checkable mechanisms

- see checklist below. Name what they do that this reference doesn't.}

## Remediation

{The chosen tier, the rollout stages it implies, in order, each with its
pass threshold.}
```

## Stripe/Twilio checkable-mechanism checklist

Cite Stripe and Twilio by name as the paired benchmark - but compare against their checkable mechanisms, not their reputation. Attribution is well-corroborated practitioner consensus, not a controlled study.

Stripe:

- Reference content generated from the spec, so it cannot drift from the contract.
- Working, personalized test API keys embedded directly in code samples for logged-in users.
- Persistent language switcher; prose paired with a runnable sample in a multi-pane layout.
- Typed, self-describing resource-ID prefixes (`ch_`, `cus_`, `pi_`, `sub_`) so every example teaches the ID scheme.
- Documentation quality written into engineering career ladders and enforced in review.

Twilio:

- Unusually complete per-endpoint error tables.
- A public, CI-tested snippet repository (`TwilioDevEd/api-snippets`): one repo, snippets versioned per helper-library release, a testing harness with a fake API server validating every snippet before merge. This mechanism - not editorial diligence - is what produces per-language parity that never ships broken samples.
- Task-oriented guides layered over (not replacing) the complete endpoint list.

A reference that scores 100% on the rubric but has none of these mechanisms will not stay at 100%; the mechanisms are what the rollout stages install.
