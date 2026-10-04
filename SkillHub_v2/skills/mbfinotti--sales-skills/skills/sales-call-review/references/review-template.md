# Review template

Fill-in template for the delivered review. Sections marked (manager/peer) or (B2C) appear only in that mode. Never leave a placeholder in a delivered review - fill it or delete the line with a stated reason.

```markdown
# Call Review - <company/prospect>, <call type>, <B2B|B2C>, <date of call>

**Mode**: <self-review | manager review | peer review>
**Outcome (context only, grades nothing)**: <meeting booked / next step set / lost / unknown>
**Transcript**: <quality tier: clean / usable with damage noted / refused>, <speaker labels: native / inferred / partially unattributable>, <complete | partial - phases present: ...>
**Prior focus behaviour**: <behaviour named in the last review + whether this transcript shows it changed, quoted> | <none - first review>

## Fatal moment

<Quoted passage + location + one line on why it kills the deal or breaches a rule> | None found.

## Self-assessment (manager/peer)

<The rep's own dimension-by-dimension read, captured before any reviewer score was shown. In self-review mode: the rep's first-pass scores, kept for the divergence check.>

## Scores

| Dimension                           | Score /4             | Confidence                                             | Evidence (quote + location) | Why          |
| ----------------------------------- | -------------------- | ------------------------------------------------------ | --------------------------- | ------------ |
| Opener (<cold                       | scheduled> variant)  | <n                                                     | N/A: reason>                | High/Med/Low | "<verbatim quote>" [HH:MM:SS → HH:MM:SS] | <one line, behaviour not adjective> |
| Discovery                           |                      |                                                        |                             |              |
| Objection handling                  | <n                   | N/A: no objection - prevention or disengagement noted> |                             |              |                                          |
| Close (next-step)                   |                      |                                                        |                             |              |
| Compliance & script (B2C, optional) | <pass/fail per item> |                                                        |                             |              |

**Shape**: <one sentence on where strength and weakness cluster - this, not the total, is the headline>
**Renormalized aggregate (optional, least interesting output)**: <x / applicable max, N/A dimensions excluded>

## Strengths (max 2, each quoted)

1. "<quote>" [location] - <what the rep did and why it worked>
2. <or delete this line>

## Change items (max 3, ranked per SKILL.md Bounded feedback, SBI-shaped)

1. **<fatal slip | structural | local | fatal habit>** - Situation: "<quote>" [location]. Behaviour: <observable action>. Impact: <consequence on this call>. Effort to land: <near-zero | a week | a quarter>. <Manager/peer mode: close with a question, not a verdict.>
2. ...
3. ...

**Ranking note**: <which Interview answer or fact about this rep moved an item off the default `fatal slip > structural > local > fatal habit` order - or "default order, nothing moved it">

## The one thing

<Single focus behaviour, observable and re-executable - an action, never a trait.>

## Next-review check

<The observable, quote-level change on the next call that counts as this review landing.>

## Divergence (self-review mode)

<Where the rep's self-scores and the evidence-based scores differ, each divergence explained with the quote that decides it.>

## Notes

<Confidence flag for any statistic used - independent measurement or vendor claim; consent-disclosure observation if one was clearly expected and absent; parts of the transcript left unread and why.>
```

## B2C / contact-centre adaptations

- Add the compliance & script row; score its items pass/fail against the house list (the item set lives in the rubric anchors reference, which SKILL.md links directly).
- The call is usually the whole deal: read "Close" as the purchase/commitment ask, and expect shorter evidence passages - the one-line confidence rule still applies.
- Keep reviews shorter than the B2B format when volume is high. What survives the trim, in order: `fatal moment > the one thing > one change item > one strength > scores table`. The bounded-feedback caps are ceilings, not quotas.
- A B2C compliance failure is a rule breach, so it carries compliance cost and outranks everything else on the page - it becomes the one thing regardless of the efficiency order.
- Everything else - evidence rule, transcript gate, quality gate, one focus behaviour - is identical to B2B (stated per SKILL.md's B2B and B2C section; the B2C-specific parts are adaptations, flagged in the review's Notes).
