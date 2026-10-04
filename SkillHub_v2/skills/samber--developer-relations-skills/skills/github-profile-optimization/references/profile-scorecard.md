# Profile scorecard

Score the profile before touching it, and again after. Attach evidence to every line - a quoted sentence, a field value, or a line of `scripts/profile-audit.py` output. A judgement with no evidence is an opinion the owner can dismiss.

## Blocking checks (pass/fail - any failure blocks shipping)

| #   | Check                                                     | Fails when                                                                                                  |
| --- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| B1  | The README renders at all                                 | Repository name, visibility, path or emptiness breaks one of the four prerequisites                         |
| B2  | A visitor can name what this account or organization does | The first screen is decoration, greetings, or a widget row with no sentence                                 |
| B3  | Every claim is true today                                 | A shipped-project link 404s, a role or employer changed, a "currently building" line predates the last year |
| B4  | A next step exists                                        | No link to docs, a repository, a contact route, or a community                                              |

## Scored checks (2 points each, 16 total)

| #   | Check                         | 2 points                                                                                                  | 1 point                    | 0 points                                              |
| --- | ----------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------- |
| S1  | Positioning sentence          | One sentence naming audience and value, checkable                                                         | Vague but present          | Absent or pure adjectives                             |
| S2  | Pins used as editorial        | 6 pins chosen for a reader's path, each with a description                                                | Pins set but arbitrary     | Unset, or padded with archived or forked repositories |
| S3  | Pin descriptions and topics   | Every pinned repository has a description and topics                                                      | Most do                    | Half or more are bare                                 |
| S4  | Reading order                 | Positioning → proof → next step within the first screen                                                   | Right content, wrong order | Buried under badges, banners or a table of contents   |
| S5  | Decoration budget             | ≤3 images/widgets, each earning its place                                                                 | 4-6                        | 7+, or any widget whose data is visibly stale         |
| S6  | Accessibility and portability | Alt text everywhere, no meaning encoded in colour alone, readable in a plain markdown viewer              | One violation              | Multiple, or the page collapses without rendered HTML |
| S7  | Freshness signals             | Owner named and review triggers listed (launch, talk, release, role change), no stale time-bound phrasing | Fresh but unowned          | Stale statements a visitor can disprove               |
| S8  | Route to the real destination | Clear path to docs, product, community or contact, with tracked links where the harness allows            | Link present, untracked    | Dead end                                              |

## Thresholds

Every number below is this skill's own baseline, not a published standard - no rubric or pass mark exists for profile work. Offer them as defaults and let a reasoned owner move them.

Ship when all four blocking checks pass and the scored total reaches **13/16**. Below that, iterate - do not ship with a note explaining the gap.

For an organization profile, add one more blocking condition: the page must answer "which repository do I open first" without the visitor scrolling into the repository list.

## Cold-reader test

Give a reader who has never seen the account **45 seconds** on the profile page, then close it and ask:

1. What does this person or organization do?
2. Which project should I look at first, and why that one?
3. Is this active?
4. What am I meant to do next?
5. (Organization only) What is open source here, and what is commercial?

Four of four (five of five for an organization) is the pass. Each wrong answer maps to a section: 1 → positioning, 2 → pins, 3 → freshness, 4 → call to action, 5 → the open-source stance paragraph.

Use a person if one is available. A fresh agent session with no prior context on the account is an acceptable substitute; your own reading is not, because you already know the answers.

## Report format

```
PROFILE AUDIT - <account> (<personal | organization>)
Goal on record: <the one outcome this page serves>

Blocking
  B1 renders            PASS
  B2 identifiable       FAIL - first screen is a trophy row, no sentence
  B3 claims true        FAIL - "currently building X" - X archived 14 months ago
  B4 next step          PASS

Scored  9/16
  S1 positioning        1  "full-stack developer passionate about code"
  S2 pins               0  pins unset; fallback surfaces an archived fork first
  ...

Cold reader   2/4 - reader could not answer 2 or 3

Fix order (return per hour spent)
  1. B3 - remove or update the two false claims
  2. S2 - set six pins, flagship first
  3. B2 - one positioning sentence above everything else
  moved by owner's answers: hard date on 12 Nov dropped the page rebuild from this pass
```

Order the fix list using SKILL.md § Order the fixes, and re-rank it against the owner's deadline, durability and effort ceiling. Name in the report which answer moved which fix.
