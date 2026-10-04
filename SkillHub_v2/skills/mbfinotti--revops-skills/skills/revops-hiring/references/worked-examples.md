# Worked Examples

## Positive: first RevOps hire at a Series A B2B SaaS

Interview answers:

- Company: 45 people, Series A.
- GTM team: seven sales reps, four marketers, three CS.
- First dedicated ops hire.
- Pain: (b) + (c) - nobody trusts the forecast and lead handoffs leak.
- Stack: CRM plus marketing automation, messy.
- Budget: req funded at manager level.
- Reporting: reports to the CRO, who sponsors it.
- Panel: the CRO, the VP Marketing, a senior AE, and the CEO for the final round.
- Headcount: approved.
- Mandate: a compounding capability, not a one-off.
- Forcing date: the next fiscal year's planning cycle, not this quarter.

**Profile choice**: headcount is approved and the mandate is compounding, so no row was deleted and the default order held - `fractional > agency > in-house specialist > in-house strategist` on value per hour spent.

Re-ranked on this company's context: seven reps puts it past the roughly-five-rep threshold in the first-hire guidance, and the pain recurs weekly rather than resolving into one bounded project, which demotes both contract rows. Recommendation: in-house specialist. The strategist row was not deleted but stayed last - the cross-boundary pain is real, but a quarter to fill plus a quarter to ramp lands after the planning cycle the sponsor is hiring for.

**Archetype and level**: analyst-leaning generalist at manager level - the profile-choice test points to analytics-trust pain first, cross-boundary second, and first-hire guidance calls for a strategic generalist willing to do tactical CRM work. Budget checked against published bands: Revenue Operations Manager positions average $128.2K ($102-163K); the funded number sat below the range floor, so the sponsor raised it before posting rather than making an aspirational-junior compromise.

**Scorecard**:

- Mission: "make our pipeline data trustworthy enough to forecast from."
- Ranked outcomes: by day 60, a weekly pipeline report leadership trusts; by day 90, the sales process documented and reflected in the CRM; by month 6, forecast accuracy measured and improving against a written baseline. (This outcome shape follows the principle: define specific outcomes before they start.)
- Competencies (five, covering typical RevOps domains): technical and analytical; systems thinking; cross-functional communication; change management; forecast and pipeline judgment.

**Requirements matrix** (excerpt):

Must-haves weighted to 100%:

| Must-have                                         | Weight |
| ------------------------------------------------- | ------ |
| Intermediate SQL                                  | 25%    |
| One end-to-end CRM implementation owned           | 25%    |
| Forecast/pipeline reporting experience            | 20%    |
| Stakeholder-facing process work                   | 20%    |
| 4+ years in a GTM ops role, scored level-relative | 10%    |

- Nice-to-haves as bonus: marketing automation admin experience, BI tool depth, CRM admin certification (not a must-have - this is not a pure systems req).
- Disqualifiers, separate checklist: no work authorization, tool-first answers to every process question.

**Stage map**:

| Stage                        | Interviewer        | Competencies owned                                             |
| ---------------------------- | ------------------ | -------------------------------------------------------------- |
| Screen (30 min)              | CRO                | Trajectory, comp fit - no scored competency                    |
| Deep-dive (60 min)           | CRO + VP Marketing | Forecast and pipeline judgment; cross-functional communication |
| Work-sample debrief (45 min) | Senior AE + CRO    | Technical and analytical; systems thinking                     |
| Final (30 min)               | CEO                | Change management                                              |

Three rounds plus one take-home per best practice guidance. Every score submitted with a quote before debrief.

Sample anchor, "forecast and pipeline judgment":

| Anchor | Behavior                                                                                                                                     |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 5      | Diagnoses the forecast question by comparing commit categories against actuals over time and names the data-quality prerequisite unprompted. |
| 3      | Structured diagnosis after prompting, credible fix sequence.                                                                                 |
| 1      | Answers "I'd clean up the data" or names a tool as the fix.                                                                                  |

**Work sample**: the messy-CRM-export prompt - 40 synthetic opportunity rows with duplicate accounts, blank close dates, and inconsistent stage names; "diagnose, prioritize your fixes, and list what you would ask stakeholders before touching anything." Two-hour cap, tested on the senior AE first. Rubric written before sending, on the loop's 1/3/5 anchors across diagnosis, prioritization, stakeholder step, communication - all four required at 3+, no summed total (point values are this skill's convention).

**Ramp** (excerpt):

- Week one: CRM admin + sandbox, BI access, seat in the weekly pipeline and forecast calls, 1:1s with every rep and marketer; buddy is the senior AE, not the CRO.
- Day-60 goal maps to scorecard outcome one.
- Watch areas: dashboards nobody asked for; ticket-queue capture above the agreed one-day-per-week cap; no documented definition of pipeline stages by day 45.

## Negative: the aspirational strategist hire

A 30-person seed-stage company with a barely configured CRM hires a "Head of RevOps" - a strategist profile with a director title - because the founder wants "someone strategic".

- No executive sponsor is named.
- The role reports vaguely to "the founders".
- The req skips the archetype diagnosis that would have pointed at capacity-plus-systems pain.

What follows tracks the documented failure patterns: the hire is at the wrong altitude - "too senior to do the work, too junior to own the strategy. Sprints don't ship."

- Every improvement becomes a negotiation because no sponsor clears the way.
- The operating strategy decks pile up while reps still work from spreadsheets.
- The hire leaves inside a year.

This is the compound risk RevOps Co-op names: "An aspirational hire is a risk to you as a hiring manager on multiple levels."

The cost: a senior req takes 12-16 weeks to fill and the replacement ramps in 1-3 months (startup-planning timelines), so the redo costs roughly four to seven months of calendar on top of the failed hire's tenure and salary. A director-level year runs $171-279K, plus the un-fixed CRM the whole time. The fix was available before posting:

- Run the profile-choice test (capacity/systems pain wants a hands-on generalist or fractional help, not a Head-of title).
- Name a sponsor.
- Fund the level the diagnosis calls for - or per the fractional guidance, do not open the full-time req below roughly $3M ARR at all.
