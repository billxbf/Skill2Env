# Quickstart page skeleton

Fill this in and delete every section the product genuinely does not need. Nothing optional survives by default - each surviving line spends part of the time budget.

## Skeleton

```markdown
# <Verb the reader's outcome> in <N> minutes

<One sentence naming what will be working at the end. No product history, no architecture.>

## Before you start

- <Requirement 1>: check with `<command>` (<install pointer>)
- <Requirement 2>: check with `<command>`
- <Credential>: <how to get it in one click/step, with link>

## 1. <Install / connect>

`<single copy-pasteable block>`

You should see:

`<real output, trimmed but not edited>`

Not what you got? <one-line fail branch with link>

## 2. <Configure>

`<block using <YOUR_API_KEY> style placeholders>`

## 3. <Do the thing>

`<complete, runnable file or command; never a fragment>`

## 4. <See it work>

`<verification command>`

You should see:

`<the success moment, verbatim>`

## What just happened

<Two sentences at most, connecting the output to the product concept it proves.>

## Next steps

- <Most common second task>
- <Reference documentation>
- <Where to get help>
```

## Section rules

- **Title.** Name the reader's outcome and the time, not the product ("Send your first SMS in 5 minutes", not "Getting started with Messaging"). The time claim is a promise the cold run must honour.
- **Before you start.** Requirements only - things that must exist before step 1. Each gets a check command so the reader detects a mismatch here rather than at step 3. Credentials get a direct path, not "see the account settings documentation".
- **Steps.** Three to six. More than six means the success moment is too big; re-cut it. Number them so a support reply can say "step 3 failed". Each step covers:
  - A verb heading.
  - One block.
  - Expected output.
  - A fail branch.
- **Expected output.** Paste what the product really prints, trimmed of noise but never invented. A reader comparing their terminal to a fabricated output loses trust permanently.
- **What just happened.** The only place explanation is allowed, and only to bind the output to one concept the reader now needs. Skip it entirely if the output speaks for itself.
- **Next steps.** Three links maximum. More links means the reader chooses instead of continuing.

## Variants of the same page

When several ecosystems must be supported, keep one canonical path in this page and publish siblings with identical structure (`quickstart-python`, `quickstart-go`), each verified independently. Tabs inside one page work only when every tab is cold-run verified - an unverified tab is worse than a missing one, because the reader trusts it equally.

## What never belongs here

- Authentication theory, architecture diagrams, comparison tables.
- Configuration matrices and every flag a command accepts.
- Error catalogues beyond the one-line fail branches.
- Production hardening, scaling, or security guidance.
- Feature tours of anything the success moment does not need.

Each of these has its own home (explanation docs, reference, troubleshooting pages, how-to guides). Linking to them costs one line; inlining them costs the reader's remaining attention.
