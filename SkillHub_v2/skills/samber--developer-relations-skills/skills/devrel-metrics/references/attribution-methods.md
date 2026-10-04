# Attribution methods

How to decide what a DevRel program is allowed to claim, and how to write the rule down before the period starts.

The method numbering below is exposition order, not a ranking. Stand them up in the efficiency order decided in SKILL.md § Attribution realism: `self-reported > pre/post lift > tagged links > influenced pipeline`.

## Contents

- [Why DevRel attribution breaks](#why-devrel-attribution-breaks)
- [Method 1 - self-reported attribution](#method-1--self-reported-attribution)
- [Method 2 - tagged links and last-touch analytics](#method-2--tagged-links-and-last-touch-analytics)
- [Method 3 - influenced pipeline](#method-3--influenced-pipeline)
- [Method 4 - pre/post lift and holdouts](#method-4--prepost-lift-and-holdouts)
- [Writing the attribution rule](#writing-the-attribution-rule)
- [The revenue-metric decision](#the-revenue-metric-decision)

## Why DevRel attribution breaks

Three structural reasons, none of them fixable with better tracking:

1. **Touches happen off-web.** A hallway conversation, a podcast listened to while driving, a colleague's recommendation. No pixel exists for any of them.
2. **Referrers disappear.** Aggregators, chat clients, privacy browsers and PDF or slide links strip the referrer. Roughly 70% of AI-assistant-driven traffic arrives with no referrer header and is classified as "direct". A large direct bucket during a launch week is the normal case.
3. **Every source is biased toward itself.**
   - Ad platforms count their own conversions inside their own windows.
   - Web analytics anchors on last non-direct click and dumps the unknown into direct.
   - CRM reflects whatever a rep typed.

   Reconcile with a stated method; never average them.

The consequence is not "measurement is impossible". It is that the method must be chosen, stated and held constant, so a change in the number means a change in the world rather than a change in the counting.

## Method 1 - self-reported attribution

Ask the human. A short question at signup, at first sales conversation, or in an onboarding email.

**Bias:** over-counts memorable touches (a talk, a podcast, a specific person), under-counts boring-but-real ones (search, docs, retargeting). Accept it: DevRel's touches are disproportionately the memorable kind, so this is the one method that sees the program at all.

**Question set that works.** One required question, free text optional:

```
How did you first hear about <product>?
( ) Search engine or AI assistant
( ) A colleague or friend
( ) A conference talk, meetup or workshop
( ) A podcast, video or livestream
( ) A blog post or newsletter - ours or someone else's
( ) An open-source project or repository
( ) Social media
( ) Other: ______
```

Rules that keep it usable:

- Keep the option list stable across quarters - a changed list breaks the trend.
- Always keep the free-text box - it surfaces channels you did not list.
- Never make it more than one question.
- Read the free text quarterly rather than only the counts.

**Reading it honestly:** report it as "self-reported first touch", not as attribution. Response rates and recall both bias it. Its value is direction and discovery, not precision.

## Method 2 - tagged links and last-touch analytics

Tag the links you control, one campaign or event per tag, never reused.

**Bias:** sees only clicks from taggable surfaces. Everything printed, spoken, screenshotted or shared in a chat client vanishes.

**Use for:** comparing two artifacts of the same type (which post, which event landing page, which docs entry point). Never for program totals - the untaggable share is too large and varies by channel, so totals compare tracking coverage rather than performance.

Pair every event, talk or campaign with a dedicated short URL or code, and record the pre-period baseline for the destination, or the lift cannot be claimed at all.

## Method 3 - influenced pipeline

The B2B answer, and the one most likely to be demanded. It requires a written rule, because "influenced" without a rule means whatever the presenter needs it to mean.

**Worked rule (adapt the specifics, keep the shape):**

> An opportunity is **DevRel-influenced** when, in the 180 days before it reached stage 2, at least one contact on the account recorded one of: attendance at a program-run event or workshop; a question answered by the team in a public community venue; a self-reported first touch naming a program surface; or a documented conversation logged by a program team member.
>
> Influence is claimed as _influenced pipeline value_, never as sourced revenue. Marketing and Sales may claim the same opportunities. The rule is fixed for the fiscal year; a mid-year change invalidates the trend and must be reported as a restatement.

Things the rule must always name:

- Which touch types count.
- The lookback window.
- Whether the touch must precede a specific stage.

Things it must never do:

- Change mid-period.
- Claim sourcing.
- Count a touch that was recorded after the opportunity was created.

**Bias:** over-counts by construction. Accounts that engage are already more likely to buy; the metric cannot separate influence from selection. State this once in the framework and stop re-litigating it.

**Latency:** enterprise cycles push the answer two to four quarters out. Name the leading indicator carrying the interim - typically qualified conversations or evaluations that survived review.

## Method 4 - pre/post lift and holdouts

The only family with a causal claim. In advertising, randomised tests routinely show observational attribution overstating true lift by a large multiple, which is the argument for doing this at all. The same literature also shows how much volume a properly powered test needs, which is why DevRel rarely gets a clean one.

**What is affordable at DevRel volume:**

- **Pre/post against a recorded baseline** for one bounded push (a docs rewrite, a launch, a regional event series). Record the pre-period before the push, not after.
- **A regional or segment holdout**: run the push in some regions or ecosystems and not others, compare the difference in differences. Works for event series and localized content.
- **A staggered rollout**: ship the change to one docs section or one SDK first.

**What to claim:** direction and rough magnitude. Never a point estimate with a decimal place. A "+12% lift" whose interval spans zero is not a finding, and DevRel-sized samples produce wide intervals by default.

## Writing the attribution rule

The rule is one short section of the framework document. It names:

1. Which methods are in use, and for what.
2. What each method may and may not claim, in one sentence each.
3. The lookback window and any stage condition.
4. What happens to the trend if the rule changes (a restatement, announced).
5. The known blind spots - the touches no method sees.

Point five is what makes the rest credible. An exec who discovers an unstated gap discounts the whole sheet; one who was told about it up front reads the remaining numbers as honest.

## The revenue-metric decision

Two defensible positions. Pick one deliberately; the deciding input is who owns the budget.

**No sales metrics on DevRel.** Mary Thengvall's position (14 December 2019): a quota "muddies our work too much and changes what should be a genuine relationship into one that revolves around money". The proposed currency instead is the **DevRel Qualified Lead** - a connection passed to whichever team can act on it, logged and reviewed monthly or quarterly for patterns:

- Marketing for a case study
- Product for feedback or a beta
- Engineering for a bug
- BizDev for a partnership
- Recruiting for a candidate
- Sales for a customer

It borrows the qualified-lead vocabulary the business already speaks without pretending every relationship ends in a sale.

**Influenced pipeline, explicitly shared.** A program funded from a sales or marketing line will be measured on a revenue-adjacent number whether it proposes one or not. Proposing the honest version - influenced, rule-bound, shared credit, with the leading indicator named - beats having a dishonest one assigned by someone with no view of the work.

Write the choice into the framework with its reason. A team that never made the choice ends up doing both badly: chasing pipeline informally while reporting reach formally.
