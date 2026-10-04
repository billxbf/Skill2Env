# Contributor path scorecard

Score before changing anything, and again at the end.

## 1. Blocking checks

Four checks, pass or fail. A fail here outranks every scored check, because each one ends the first contribution outright.

| #   | Check                     | Passes when                                                                                                                      |
| --- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| B1  | Contribution is invited   | A CONTRIBUTING file exists in a location the forge surfaces, and states which kinds of contribution are accepted                 |
| B2  | The documented setup runs | A cold run reaches passing tests using only the written steps, with no undocumented step                                         |
| B3  | There is work available   | At least three unclaimed, currently-valid beginner-friendly issues exist, each with a body a stranger could act on               |
| B4  | Submissions get answered  | The median time to first human response on externally-opened issues and PRs over the last 90 days is inside the published target |

B4 cannot be faked by publishing a slower target and then meeting it - if the honest target is two weeks, say so, and note it as a finding rather than a pass in disguise.

## 2. Scored checks

Eight checks, 0-2 points each, 16 total:

- 2: evidence you can point at
- 1: partial
- 0: absent

| #   | Check                       | 2 points                                                                                                      |
| --- | --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| S1  | Out-of-scope is stated      | A reader can predict which PRs get declined without asking                                                    |
| S2  | Prerequisites are pinned    | Runtime and tool versions are pinned in a version file or container definition, not prose                     |
| S3  | Local gates match CI        | Every check CI enforces is runnable locally with a documented command                                         |
| S4  | Fork CI is useful           | A credential-free lane runs on fork PRs and goes green; nothing red is unfixable by the contributor           |
| S5  | First issues are complete   | Beginner issues carry expected behaviour, location, required skills, verification command, and a named mentor |
| S6  | Claiming is defined         | The claim convention and the stale-claim expiry are written down and applied                                  |
| S7  | Legal gate is pre-announced | DCO or CLA appears in CONTRIBUTING before the reader writes code                                              |
| S8  | Credit and next step        | Merged contributions are credited, and the contributor is pointed at a concrete next issue                    |

## 3. Cold-run protocol

The only way to score B2 honestly. Reasoning about the instructions does not count.

1. Start clean: a fresh container, a new user account, or a machine that has never built this project. No warm caches, no global config, no credentials you forgot you have.
2. Read only what a stranger reads - the README and the CONTRIBUTING file. Do not use repository knowledge you already hold.
3. Execute the written steps literally, in order. When a step fails, record the failure and the fix, then continue.
4. Record wall-clock time to the first passing test run.
5. Log every undocumented requirement: system package, environment variable, running service, credential, minimum resource, platform assumption.
6. Fix the documentation, then run the whole sequence again from clean. Repeat until nothing is discovered.

If you cannot execute commands in your environment, say so plainly and ask the maintainer to run the sequence and paste the full output - including the failures. Do not mark B2 passed by inspection.

Second cold run, same discipline, for the task path: from the beginner-issue list, can a stranger pick an issue, understand what is being asked, and locate the file to change in under 15 minutes without asking a question?

## 4. Pass threshold

The path passes when all four blocking checks pass and the scored checks total at least 12 of 16.

No published rubric scores a first-contribution path, so that mark is this skill's own baseline, not a finding - say so when a maintainer asks where the number comes from, and let a project set a different bar with a stated reason. The two numbers inside the rubric that are sourced are B4's 48-hour reference point (GitHub Open Source Guides) and the CHAOSS definitions behind the funnel baseline; `published-findings.md` carries the full published-versus-self-set split.

Below the threshold, iterate rather than shipping with a caveat. Re-score after each round of fixes, and keep the first score - the delta is the only evidence the work changed anything.

## 5. Report format

Produce this shape verbatim, with evidence attached to every line.

```markdown
# Contributor path audit - <project> - <date>

## Verdict

<PASS | FAIL> - blocking: <n>/4 passed, scored: <n>/16

## Blocking checks

| Check                   | Result | Evidence                                                 |
| ----------------------- | ------ | -------------------------------------------------------- |
| B1 Contribution invited | PASS   | `.github/CONTRIBUTING.md`, lines 1-12                    |
| B2 Setup runs cold      | FAIL   | Cold run stopped at `make setup`: `libpq-fe.h not found` |
| ...                     |

## Scored checks

| Check                  | Score | Evidence                                                      | Fix                                         |
| ---------------------- | ----- | ------------------------------------------------------------- | ------------------------------------------- |
| S1 Out of scope stated | 0     | No scope section; 3 of the last 10 PRs closed as out of scope | Add scope section naming those 3 categories |
| ...                    |

## Funnel baseline

- New external contributors, last 4 quarters: <n, n, n, n>
- Second-contribution rate within 90 days: <n%>
- Median time to first response, external issues/PRs: <n days>
- External first-PR merge rate: <n%>
- Contributor absence factor: <n>

## Fix order

1. <highest-damage fix, with the check it unblocks>
2. ...

## Confounders

<launches, conference talks, mentions that moved these numbers independently>
```

Rank fixes by damage removed per hour spent, and let effort break ties only among fixes of similar damage. A failed blocking check outranks every scored one. A setup that fails on a common platform outranks every wording improvement in the file, however fast the wording is to rewrite: cheap and efficient are different orderings, and only the second one answers what to do first.
