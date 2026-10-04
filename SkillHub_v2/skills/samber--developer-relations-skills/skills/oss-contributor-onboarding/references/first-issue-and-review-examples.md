# Worked examples: first issues and first-PR replies

Copy the shape, not the wording.

## Table of Contents

- [1. Beginner-friendly issue body](#1-beginner-friendly-issue-body)
- [2. First response on a new PR](#2-first-response-on-a-new-pr)
- [3. Review comments](#3-review-comments)
- [4. Declining a contribution](#4-declining-a-contribution)
- [5. Merge message](#5-merge-message)
- [6. Re-inviting a stalled contributor](#6-re-inviting-a-stalled-contributor)

## 1. Beginner-friendly issue body

**Weak**

```
Title: Improve error handling in the config loader
Labels: good first issue

The config loader should handle errors better.
```

Nothing here tells a stranger what "better" means, where the loader lives, how to verify a fix, or who to ask. It is small for the maintainer, who already knows all four.

**Strong**

```
Title: Config loader reports "unexpected error" when the config file is missing
Labels: good first issue, area/config, skills/file-io

**Current behaviour**
Running `app start` without `config.yaml` prints `unexpected error` and exits 1.

**Expected behaviour**
Print `config file not found: <path> - create one with 'app init'` and exit 1.

**Where**
`internal/config/loader.go`, `Load()`, around the `os.ReadFile` call.
Tests live in `internal/config/loader_test.go`.

**Suggested approach**
Check for a not-exist error from the read and return a typed error carrying the
path. The message text above is settled - no design discussion needed.

**Verify**
`make test PKG=./internal/config` - add a case covering the missing-file path.

**Mentor**
@maintainer-handle. Comment here to claim it; ask anything in the issue thread.
```

The additions that matter most: the skill label (`skills/file-io`) so a contributor can judge fit before committing, the explicit "no design discussion needed", and the named mentor.

## 2. First response on a new PR

**Weak**

Silence for eleven days, then: `Please rebase and fix the failing tests.`

**Strong**, posted the same day:

```
Thanks for this - it is in scope and the approach looks right.

I will do a full review by Thursday. Two things in the meantime:

- CI shows red on `lint` only; run `make lint` locally and it should reproduce.
- The other two red checks need repository secrets and cannot run on a fork.
  Ignore them; I will run them before merge.
```

This is the reply the 48-hour finding is about - acknowledgement, not a completed review.

## 3. Review comments

**Weak**

```
This is wrong.
Use a pointer here.
Nit: spacing.
Why did you do it this way?
```

Four unlabelled comments, one of them a formatting issue a machine should have caught, and no way for the contributor to tell which one blocks the merge.

**Strong**

```
**Blocking** - this drops the error when the file exists but is unreadable
(permissions). Wrapping it keeps the cause visible for the caller:
`return fmt.Errorf("read config %s: %w", path, err)`

**Blocking** - please add a test for the unreadable-file case next to the
missing-file one you added; it is the branch we regress most often.

**Optional** - we usually name these `errConfigMissing` rather than `ErrMissing`,
but the existing package is inconsistent, so either is fine here.

Formatting is handled by `make fmt`; ignore anything the diff shows there.
```

Each request carries its reason, and style is delegated to the formatter.

## 4. Declining a contribution

**Weak**: closing with no comment, or leaving the PR open for six months.

**Strong**

```
Thank you for writing this, and I am sorry it is a no. Plugin loading is outside
what this library covers - CONTRIBUTING lists it under "out of scope" because it
would pull in a dependency we keep the project free of.

The change itself is clean, and it would work well as a separate package; happy
to link it from the README if you publish it.

If you want another way in, #412 is open and close to what you did here.
```

One or two sentences would be enough - what matters is that it happens quickly rather than by expiry.

## 5. Merge message

**Weak**: merge, no comment.

**Strong**

```
Merged - thank you. This ships in 2.4.0 next Tuesday and you are credited in the
changelog entry.

If you want a second one, #388 is the same area and slightly deeper: it needs the
same error type applied to the loader's watch path. Happy to mentor it.
```

## 6. Re-inviting a stalled contributor

**Weak**: an automated stale bot closing the PR at 30 days with a templated message.

**Strong**

```
Checking in - no pressure, and no deadline on my side. Three options:

1. You finish it when you have time; say the word and I will hold it open.
2. I push the last two commits myself (edits are enabled) and you stay the author.
3. We close it and I open an issue with what is left.

Any of the three is a good outcome. Which do you prefer?
```

An abandoned PR is usually a life event, not a lost interest. Offering to finish it keeps both the change and the contributor.
