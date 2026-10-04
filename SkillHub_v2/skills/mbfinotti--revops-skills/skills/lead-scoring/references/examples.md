# Worked Examples

Two passing specs and one broken model. The point values are illustrative shapes, not universal constants - every real spec re-derives them from the user's own won/lost data.

## Example 1 - Mid-market B2B, sales-led

```
SCORING MODEL SPEC - B2B SaaS, ACV ~$15K, 2026-03, v1
Motion       : sales-led mid-market - 50/50 fit/engagement, 100-pt scale (50+50)
Fit (50)     : primary industry +15 (2.1x won-vs-lost) | 51-1,000 employees +15 (1.8x)
               | manager-to-VP title in buying dept +12 | complementary tool +8 (coverage 71%)
Engagement   : demo/trial request +30, no decay until worked | pricing 2+ visits +20, -5/wk
(50, capped) : integration-docs view +15, -5/2wk (3.1x baseline - the surprise winner)
               | webinar attended +5, -5/mo (~1x baseline; kept low deliberately)
               | all email engagement capped at 10 total
Exclusions   : competitor domains, .edu, existing customers, unsubscribed, hard bounces
Negative pts : personal email -10 | careers-page-only -30 | consultant title -10
Threshold    : 65 -> projects ~35 MQL/wk against 8 reps x 5/wk = 40 capacity
Tiers        : T1 hand-raiser or 85+ -> fast human follow-up | T2 65-84 -> queue
               | T3 fit >=30, eng <15 -> nurture | T4 rest -> lifecycle only
Backtest     : 12-mo retro-score: top band 21% -> opportunity vs 6% baseline = 3.5x lift;
               9% of wins scored <65 (all event-sourced -> event-attendance signal added)
Guardrails   : acceptance floor 60% | alarm if >12% of active database sits above 65
Governance   : owner MOps lead | sign-off VP Sales, 2026-03-10 | v2 review 2026-05-10
```

Why it passes:

- Every weight cites a won/lost delta.
- A folklore signal (webinars) was measured, found to be noise, and demoted instead of deleted silently.
- The threshold comes from capacity math, then survives the conversion-band check.
- The false-negative finding produced a signal fix, not a lower bar.
- Lift 3.5x clears the 2x floor.

## Example 2 - PLG collaboration tool (mechanics identical, inputs and speed differ)

```
SCORING MODEL SPEC - PLG collaboration SaaS, $12/seat/mo, 2026-03, v1
Motion       : PLG - 30/70 fit/engagement; engagement fed by product events;
               rescored daily, threshold trigger fires instantly
Fit (30)     : work-email domain +10 | company 10-500 +10 (enrichment coverage 64%;
               unknown scores 0, never negative) | manager+ title +10
Engagement   : activation milestone +20 | core feature 3+ uses +20 | teammate invited
(70)         : +20, no decay | usage-limit hit +15 | pricing view +10, -5/wk
               | inactivity decay: engagement -25% per 14 idle days
Exclusions   : existing paid workspaces, .edu domains, competitor domains
Threshold    : PQL = 60 - one user's behavior qualifies; no committee to wait for
Tiers        : PQL -> sales-assist outreach | 40-59 -> in-product upgrade nudges
               | <40 -> lifecycle email only
Backtest     : 6-mo cohort: PQL band converted free->paid at 4.6x the all-signup
               baseline; false negatives 6%
Guardrails   : acceptance floor 60% for sales-assist queue | fit gate retained so
               high-usage consumer/edu users never reach sales
Governance   : owner growth ops | sign-off sales-assist lead | recalibration monthly
               (volume supports it) | v2 review +60 days
```

Why it passes:

- The fit layer is thin but present - the classic PQL failure (routing high-usage, low-fit users) is blocked by design.
- Decay and rescoring run at product speed.
- Monthly recalibration matches the data volume.

## Example 3 - Negative: a plausible-looking broken model

```
"MARKETING ENGAGEMENT SCORE" - v3 (inherited, undocumented)
Single blended score, no ceiling: email open +2 | email click +5 | any page view +3
| whitepaper +10 | webinar registration +10 | blog visit +3 | demo request +10
Fit          : title contains "manager" +10
Exclusions   : none    Decay: none    Caps: none
Threshold    : 100 ("felt right when we launched")
Validation   : never backtested    Owner: unclear    Change log: none
Status       : sales quietly stopped opening MQL tasks in Q2
```

Every flaw, decomposed:

- **Unbounded accumulation, no decay, no caps.** Six months of newsletter opens (+2 each) outscores a demo request (+10). The hottest signal in the model is worth three email clicks.
- **Vanity signals carry the model.** Opens and generic page views - the two least reliable signals, opens being auto-fired by mail-privacy proxies - contribute most crossings of the threshold.
- **Fit and engagement blended into one number**, and fit is one title keyword. The model cannot distinguish a cold-but-perfect prospect from an enthusiastic student - and has no exclusions, so competitors and students routinely cross 100.
- **Threshold chosen by feel**, never checked against sales capacity or a conversion band, never backtested. Volume swamped the reps; acceptance collapsed; the bar was then quietly lowered to keep the MQL chart up - the textbook Goodhart spiral.
- **No owner, no version log, no review date.** Three undocumented revisions in, nobody can say why any weight is what it is, so nobody can fix it - only distrust it.

The rebuild path is the main workflow, not patching:

- Split the axes.
- Re-derive weights from 12-24 months of won/lost outcomes.
- Move disqualifiers to exclusions.
- Add decay and category caps.
- Set the threshold from capacity.
- Backtest to a >= 2x lift.
- Put a name, a version, and a v2 date on the result.
