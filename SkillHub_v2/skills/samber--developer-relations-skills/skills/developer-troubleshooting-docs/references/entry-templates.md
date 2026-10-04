# Entry templates and worked examples

Contents: standards the block comes from · page shapes · error-reference template · troubleshooting how-to template · known-issues template · worked example (weak vs. strong) · quoting rules · microcopy style guides.

## Table of Contents

- [Where the block comes from](#where-the-block-comes-from)
- [Page shapes](#page-shapes)
- [Error reference entry](#error-reference-entry)
- [Message](#message)
- [Applies to](#applies-to)
- [Cause](#cause)
- [Fix](#fix)
- [Confirm it worked](#confirm-it-worked)
- [Still stuck](#still-stuck)
- [Troubleshooting how-to](#troubleshooting-how-to)
- [Symptoms](#symptoms)
- [Before you start](#before-you-start)
- [Check 1 - <cheapest, most common cause>](#check-1-cheapest-most-common-cause)
- [Check 2 - <next cause>](#check-2-next-cause)
- [Confirm it worked](#confirm-it-worked)
- [Still stuck](#still-stuck)
- [Known-issues entry](#known-issues-entry)
- [Worked example](#worked-example)
- [Authentication problems](#authentication-problems)
- [Message](#message)
- [Applies to](#applies-to)
- [Cause](#cause)
- [Fix](#fix)
- [Confirm it worked](#confirm-it-worked)
- [Still stuck](#still-stuck)
- [Microcopy: the string versus the page](#microcopy-the-string-versus-the-page)
- [Quoting the error text](#quoting-the-error-text)

## Where the block comes from

The six-part entry is not invented here. It is the intersection of three published models, which is why it is worth defending when a team wants to shorten it.

- **OASIS DITA 1.3** (Part 2, Technical Content) defines a `<troubleshooting>` topic type whose `<troublebody>` runs condition/symptom → cause → remedy, with several cause-remedy pairs supported explicitly as "successive fall-backs for resolving a condition". That is the multi-cause fix section, standardized.
- **KCS** article fields are issue, environment, cause, resolution - the environment field is the "Applies to" block, and it is the part teams drop first and regret first.
- **Rust RFC 1567** mandates, per error code: description, erroneous code example, explanation, how to fix. It is the strictest published per-entry template and a good bar for a reference catalog.

Two quality standards apply to the prose inside the block. **ISO 24495-1:2023**, the first international plain-language standard, defines success as readers being able to "find what they need, understand what they find, and use that information". **Nielsen heuristic 9** requires error content to use plain language, precisely identify the problem, offer a constructive solution, and never blame the user.

## Page shapes

| Shape                  | Choose when                                                                                             | Reader arrives with                    | Lives in the docs as                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------- |
| Error reference entry  | The product emits a stable identifier (`ERR_INVALID_ARG_TYPE`, `E0382`, `invalid_grant`, exit code 137) | An exact string                        | One page per code, or one anchored row per code on a codes page |
| Troubleshooting how-to | The failure has symptoms but no code ("webhooks never arrive", "build hangs at 90%")                    | A description of misbehaviour          | One page per symptom, under the feature it belongs to           |
| Known-issues entry     | Cause confirmed, fix not shipped                                                                        | A suspicion that it is not their fault | A dated list per product area, pruned on release                |

A coded error written as a how-to loses the match; an uncoded symptom forced into a code table loses the diagnosis. When a symptom has several possible codes, write the how-to as the triage page and link out to each code entry.

## Error reference entry

````markdown
# `ERROR_IDENTIFIER`

<one line: what the product was trying to do when it emitted this>

## Message

```text
<the error text, byte-for-byte as emitted, variable parts in <ANGLE_BRACKETS>>
```
````

## Applies to

<versions / platforms / plans / configurations where this occurs>

## Cause

<one or two sentences, in the product's own model of the world>

## Fix

1. <check or command>
2. <check or command>

<repeat as "### If <condition>" blocks when there are several distinct causes,
most-often-the-cause per minute of reader time first, not cheapest first>

## Confirm it worked

<the output, log line, or state the reader should now see>

## Still stuck

<where to report it, and what to attach: version, config excerpt, full trace>

---

Last verified: <YYYY-MM-DD> on <version> · Owner: <team or handle>

````

The last-verified stamp and owner are what make staleness visible without reading the page. A troubleshooting entry with no date is indistinguishable from a correct one until a reader runs a dead command.

## Troubleshooting how-to

```markdown
# <Symptom, in the reader's words>

## Symptoms

- Does <observable A> happen?
- Do you see <observable B> in the logs?

## Before you start

<what to have open: log access, a reproducible request, admin rights>

## Check 1  -  <cheapest, most common cause>

<how to check, what a healthy result looks like, what to do if it is not healthy>

## Check 2  -  <next cause>

…

## Confirm it worked

## Still stuck
````

Order checks by `probability ÷ cost`, not by architectural layer. A reader in an incident abandons the page at the first step that takes ten minutes.

Give each command its own prerequisite and failure branch. The reader is on a broken machine, not the healthy one the steps were written on:

```markdown
3. Check the service is reachable: `curl -sf https://<HOST>/healthz`
   - Requires: network access to <HOST>, no proxy interception.
   - If this fails with a TLS error: your proxy is terminating TLS - see <entry>.
   - Expected: HTTP 200 with body `ok`.
```

## Known-issues entry

```markdown
### <Short title> - affects <versions>, reported <YYYY-MM-DD>

**Symptom**: <what the reader sees, error text included>
**Cause**: <confirmed cause, or "under investigation">
**Workaround**: <steps, or "none - avoid <operation> until fixed">
**Tracking**: <issue link> **Fixed in**: <version, or "unreleased">
```

Delete the entry when the fix ships, or move it into the error entry with a version note. A known-issues list that only grows becomes a graveyard nobody reads.

## Worked example

The same failure, written twice.

### Weak

```markdown
## Authentication problems

If you have trouble authenticating, make sure your credentials are correct and
that your token has not expired. Check the auth documentation for more details.
If the problem persists, contact support.
```

Nothing here is searchable (the error string is absent), nothing is checkable (no command, no expected output), and the only action is "contact support" - which is the outcome the page exists to prevent.

### Strong

````markdown
# `invalid_grant`

The token endpoint rejected the refresh token you presented.

## Message

```text
{"error":"invalid_grant","error_description":"Token is expired or revoked"}
```
````

## Applies to

All API versions. Refresh tokens issued before <VERSION> expire after 30 days;
tokens issued after it expire after 90 days.

## Cause

The refresh token has expired, was already exchanged (refresh tokens are
single-use), or was revoked when the user changed their password.

## Fix

### If the token is older than its lifetime

1. Read the issue date: `curl -s https://api.example.com/v1/token/info -H "Authorization: Bearer <TOKEN>"`.
2. Re-run the authorization flow to obtain a new refresh token.
3. Store the new refresh token returned in the same response - the old one is now dead.

### If two processes refresh concurrently

Both receive the same token, one exchange wins, the loser gets `invalid_grant`.
Serialize refreshes behind a single owner, or retry once after re-reading the
stored token.

## Confirm it worked

`token/info` returns `"status": "active"` and a new `expires_at` in the future.

## Still stuck

Open an issue with the token's `jti`, the timestamp of the failed request, and
your client ID. Never paste the token itself.

````

Every claim is checkable, the fix branches on cause instead of listing everything, and the escape hatch says what to attach  -  and what not to.

### Also weak, and more tempting

The trap is not only the empty page above. It is the entry that looks complete and still fails the reader:

```markdown
# Token error

Simply refresh your token  -  this is an easy fix. If you forgot to store the new
refresh token, you'll get this error again. Error 401.
````

Four defects, each common:

- The title is not the emitted string, so nobody finds it.
- "simply" and "easy" read as blame to someone the fix is not working for.
- "you forgot" blames the reader outright (Nielsen heuristic 9).
- There is no verification step, so the reader cannot tell a real fix from a second failure masking the first.

Being wrong in a confident, tidy voice is worse than being visibly incomplete.

## Microcopy: the string versus the page

These are two surfaces with different budgets, and conflating them is the most common structural mistake. Microsoft's style guide draws the line explicitly: "avoid long how-to or instructional guidance in errors - that content lives in your documentation." The emitted string stays short and points at the entry; the entry carries the diagnostic depth.

| Guide                                    | Blame                                                                          | Codes and jargon                                              | Notable rule                                                                                                 |
| ---------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Microsoft Writing Style Guide            | "Avoid phrasing that blames the user"; passive voice acceptable to avoid blame | Avoid the word "error"; hide codes under a details affordance | Reserve "please" for when the software is at fault; "sorry" only for serious problems                        |
| Microsoft Win32 error message guidelines | -                                                                              | No technical jargon; no "error" in the title bar              | "Write a separate error message for each known cause" - one generic message serves nobody                    |
| Nielsen Norman Group (heuristic 9)       | Never blame the user                                                           | Plain language, no bare "Error 502"                           | Make errors visible, reduce the work to fix them, educate along the way                                      |
| Go Code Review Comments                  | -                                                                              | -                                                             | Error strings are not capitalized and do not end with punctuation, because they compose into larger messages |
| PostgreSQL error message style guide     | Readers "aren't expected to know the details"                                  | Avoid implementation details                                  | Separate primary message, detail and hint                                                                    |
| Rust RFC 1567                            | -                                                                              | Code plus `--explain` entry                                   | Explanations help users "understand why their code cannot be accepted", not just paste a fix                 |

Elm is the origin of the non-adversarial tone this table keeps circling. Evan Czaplicki's stated goal was to "get the compiler to a point where people feel like it is actually helping them learn Elm syntax", and Elm maintains a public error-message catalog repository for confusing messages. Its influence on Rust's diagnostics is widely noted.

Rewriting the emitted string itself is a product change, not a docs task. Hand it to the owning engineer and record it in the queue.

## Quoting the error text

- Copy the string from a real run, not from the source code: the emitted text often differs from the format template.
- Keep casing, punctuation and line breaks. Readers scan-match against their terminal.
- Replace only what genuinely varies, with a placeholder that cannot be mistaken for content: `<PATH>`, `<REQUEST_ID>`, `<VERSION>`.
- Put it in a fenced block so copy-paste is clean and search engines index it as text.
- When the product emits several variants of one failure, list them all in the same block; readers search on whichever they got.
- Redact secrets in every example, and say so - a page that shows a full token teaches readers to paste theirs into an issue.
