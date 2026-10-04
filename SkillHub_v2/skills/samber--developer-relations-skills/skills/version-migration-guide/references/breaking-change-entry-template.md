# Breaking-change entry template

One block per breaking change. Fill every part; an empty part is a decision you have not made yet.

## Template

````markdown
### Removed: `client.send()` accepts a raw string {#removed-send-raw-string}

**Affects you if** your code calls `client.send()` with anything other than a `Payload`.
Search for `\.send\(` in your codebase. At runtime on v3 you will see:

    TypeError: send() expects a Payload, received string

`send()` took either a string or a `Payload` and guessed the encoding from the first
bytes. The guess was wrong for UTF-16 input and silently corrupted messages, so v3
requires the caller to say which one it is.

```js
// Before (v2)
await client.send("hello");

// After (v3)
await client.send(Payload.text("hello"));
```
````

**Fix:** `npx codemod@latest acme/3/send-payload` rewrites literal and template-string
arguments. Calls whose argument is a variable are left untouched and reported; fix
those by hand with `Payload.text()` or `Payload.bytes()`.

**Escape hatch:** none. `Payload` has no v2 equivalent; the v2 line receives security
fixes until 2027-03-01.

````

## Part-by-part rules

| Part | Rule |
|---|---|
| Heading | Verb first (`Removed:`, `Changed:`, `Renamed:`, `Deprecated:`), plus a stable anchor id that never changes once published |
| Affects-you-if | A search pattern *and* the literal runtime message; both, because static and runtime detection catch different call sites |
| Rationale | Three sentences maximum, and it must name the harm the old behavior caused |
| Before/after | Complete enough to paste, same variable names in both halves so the diff is visually obvious |
| Fix | One primary path. A codemod command *plus* its named residue, or numbered manual steps - never a vague "or do it manually" |
| Escape hatch | The compat flag, the config restoring old behavior, or an explicit "none" with the old version's support end date |

## Good vs bad

**Bad:**

```markdown
### send()

`send()` has been updated in v3. Update your usage accordingly. See the changelog
for details.
````

Three defects:

- The reader cannot tell whether it affects them.
- The reader cannot see what to type.
- The reader is sent to a document that will not tell them either.

This entry generates a support ticket instead of preventing one.

**Bad in a subtler way:**

```markdown
### Removed: string argument to `send()`

Use a `Payload` instead. A codemod is available on our GitHub.
```

The change is now identifiable but not actionable: no detection signal, no before/after, no exact command, and "available on our GitHub" makes the reader search. Every one of those gaps costs more reader minutes than the sentence saved.

## Grouping

When several changes share one cause (a config file moving, a module format switch) - write one entry for the cause and list the affected symbols inside it. Splitting a single mechanical change into fifteen entries pushes the genuinely different changes off the reader's first screen.

Keep grouped entries under one anchor per _fix_, not per symbol: the anchor exists so a support reply can point at the action.
