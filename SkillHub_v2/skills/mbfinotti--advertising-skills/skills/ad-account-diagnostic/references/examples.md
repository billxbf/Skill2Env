# Worked Examples

Three diagnoses in the verdict-block shape, each with the tempting wrong read it replaces. Numbers are illustrative account data, not benchmarks. Findings are listed in the efficiency order of SKILL.md's Prioritisation section, each tagged `[severity, confidence, outcome bought, effort, owner]`.

## Table of Contents

- [Example 1 - B2C ecommerce: looks like creative fatigue, is a tracking break](#example-1---b2c-ecommerce-looks-like-creative-fatigue-is-a-tracking-break)
- [Example 2 - B2B SaaS: cheap leads, empty pipeline - the wrong conversion event](#example-2---b2b-saas-cheap-leads-empty-pipeline---the-wrong-conversion-event)
- [Example 3 - the false positive: a "collapse" that is attribution lag plus a learning reset](#example-3---the-false-positive-a-collapse-that-is-attribution-lag-plus-a-learning-reset)

## Example 1 - B2C ecommerce: looks like creative fatigue, is a tracking break

Situation: DTC store, paid social, ~$60K/month. Reported ROAS fell from 3.1 to 1.8 in ten days. The team's instinct: "the creatives are burnt out, we need new ads" - the ads _are_ eight weeks old, which makes the story feel right.

Decomposition says otherwise: CPM flat vs the 60-day baseline, CTR flat, AOV flat - the entire drop is in reported CVR, and it fell across every campaign, every audience, cold and retargeting alike, starting the same Tuesday. Fatigue does not synchronise across unrelated audiences on one date. The site changelog shows a checkout-platform migration deployed that Tuesday; the order table shows revenue down only ~4%.

```
ROOT-CAUSE VERDICT - dtc-apparel, 2026-08-12
platform(s)    : paid social | model: B2C
window         : Aug 1-10 vs baseline Jun 28-Jul 27 (lag maturity matched: yes)
volume         : $19.4K, 214 reported conversions | reconciliation gap: 41% vs order table (baseline norm: 9%)

decomposition  : CVR -42% reported; CPM +2%, CTR -1%, AOV +1% - single failing link
localisation   : uniform across all campaigns and audiences, common start date Aug 5

layer screen
  measurement/tracking : FAIL - purchase event missing on new checkout domain; gap jumped 9%→41% on deploy date  [critical, high]
  structure            : pass - no changes, volumes above learning gates                                          [-, high]
  targeting            : pass - frequency and reach trends unchanged                                              [-, high]
  creative             : pass - CTR flat vs each creative's own baseline                                          [-, high]
  bidding/budget       : unknown - delivery now optimising on starved signal; re-screen after fix                 [medium, low]
  offer & downstream   : pass - backend CVR ~flat; revenue -4% vs -42% reported                                   [-, high]
  external             : pass - CPM flat; category calm                                                           [-, medium]

confidence     : high - backend reconciliation is direct evidence; single break date; uniform pattern
verdict        : measurement/tracking - conversion event lost in checkout migration
evidence       : reconciliation ratio broke on deploy date; drop uniform across unrelated audiences; upstream metrics flat
findings       : 1) restore + dedupe purchase event
                    [critical, high, restores every downstream number and the delivery signal, ~a day of dev, web dev]
                 2) re-screen bidding after 7 lag-mature days
                    [medium, low, unquantified, an hour once the window matures, media buyer]
prediction     : reported CVR recovers to ~baseline within one lag-mature week of the event firing; ROAS follows
handoff        : mbfinotti/advertising-skills@ad-conversion-tracking (fix), then re-run this diagnostic
re-check       : 2026-08-26
```

**The wrong move**: shipping new creative. It would have cost two weeks of production, reset delivery on fresh ads mid-breakage, and "failed" - because the measured CVR was broken, the new ads would report just as badly, burning the creative budget _and_ the team's trust in creative testing. Never diagnose downstream layers through a failed reconciliation gate.

## Example 2 - B2B SaaS: cheap leads, empty pipeline - the wrong conversion event

Situation: B2B SaaS, search + paid social, ~$40K/month. Dashboard looks great: CPL down 35% quarter over quarter.

Sales says the leads are junk; pipeline is flat. The tempting read: "targeting got worse, tighten the audiences."

The account optimises to raw form fills. Decomposition shows CTR and CVR-to-form _improved_ - the platform is doing exactly what it was asked: finding people who fill forms cheaply.

CRM join shows lead→SQL rate fell from 14% to 5% in the same quarter, concentrated in the campaigns that shifted spend toward the cheapest-CPL audiences. This is the Happy Cog failure mode - "leads look great in dashboard, sales say trash" - and per Swydo, cost per closed-won, not CPL, is the KPI that tells the truth in B2B.

```
ROOT-CAUSE VERDICT - b2b-saas, 2026-08-12
platform(s)    : search + paid social | model: B2B
window         : May-Jul vs baseline Feb-Apr (lag maturity matched: yes - 90-day windows per long cycle)
volume         : $118K, 1,240 leads, 74 SQLs | reconciliation gap: 6% on form fills (backend = CRM)

decomposition  : CPL -35%, but cost per SQL +61%; failing link is post-conversion quality, not the funnel to form
localisation   : concentrated in campaigns optimising to form-fill with broadest audiences

layer screen
  measurement/tracking : pass - form event reconciles at 6%; but no offline/CRM outcome feeds back to platforms   [-, high]
  structure            : FAIL - optimization event is raw form fill; platform rewarded for junk volume            [high, high]
  targeting            : pass-with-note - drift is the *symptom* of the event choice, not an independent cause    [medium, medium]
  creative             : pass - stable engagement, no decay pattern                                               [-, medium]
  bidding/budget       : pass - targets met; the targets measure the wrong thing                                  [-, high]
  offer & downstream   : pass - demo-page CVR stable for the SQLs that do arrive                                  [-, medium]
  external             : n/a - no cost-side anomaly to explain                                                    [-, -]

confidence     : high - CRM join is direct evidence; pattern tracks spend shift; volume clears the gate on 90-day windows
verdict        : structure - optimising to a conversion event the business does not value
evidence       : cost per SQL up while CPL down; SQL-rate collapse concentrated where the cheap-lead spend went
findings       : 1) feed CRM outcomes (SQL/closed-won) back to platforms; optimise to a qualified event
                    [high, high, recovers most of the SQL-cost delta and keeps paying, ~a week of CRM wiring,
                     marketing ops]  - Koda: the offline feedback loop "consistently improves lead quality
                     more than any targeting adjustment"
                 2) judge campaigns on cost per SQL at 4-6 week maturity, not CPL
                    [medium, high, judgement that tracks revenue instead of form volume, near-zero, media buyer]
prediction     : CPL rises, lead→SQL rate recovers toward ~14%, cost per SQL falls within 2 windows of the event switch
handoff        : mbfinotti/advertising-skills@ad-conversion-tracking (offline import wiring); targeting redesign only
                 if drift persists after the event fix - mbfinotti/advertising-skills@ad-audience-targeting
re-check       : 2026-10-15 (one 4-6 week B2B window, lag-mature)
```

**The wrong move**: tightening targeting first. The platform would keep hunting cheap form fills inside the narrower audience, CPL would rise, quality would stay junk - and the "fix" would look like it made things worse, inviting the next reflex: more budget.

## Example 3 - the false positive: a "collapse" that is attribution lag plus a learning reset

Situation: lead-gen account, ~$9K/month, low volume (~55 conversions/month). Monday panic: "conversions fell off a cliff last week - the account is broken, should we double the budget to compensate?"

The screen: the trailing 7 days always under-report (conversions attribute over a multi-week window - recent days are immature by construction); the account's own history shows every trailing week "down" ~30% before maturing flat. And the budget was raised 40% eight days ago - a significant edit widely treated as resetting learning, inside which 20-50% day-to-day swings are normal (Niblin). Conversion volume in the panic window: 9 - far below any read that survives the noise band, and below Google's ≥30-conversions evaluation reference for Target CPA.

```
ROOT-CAUSE VERDICT - leadgen-local, 2026-08-12
platform(s)    : search | model: B2B
window         : Aug 4-10 vs baseline Jul 1-28 (lag maturity matched: NO - comparison window immature)
volume         : $2.1K, 9 conversions in window | reconciliation gap: unverified (no CRM access this run)

decomposition  : reported CVR -33% - but inside the account's own historical immature-week band
localisation   : not meaningful at this volume

layer screen
  measurement/tracking : unknown - no backend access; ratio history unavailable          [medium, low]
  structure            : pass - unchanged                                                [-, medium]
  targeting            : pass - unchanged                                                [-, medium]
  creative             : unknown - 9 conversions cannot power a creative read            [-, low]
  bidding/budget       : unknown - +40% budget edit 8 days ago; learning likely reset    [medium, medium]
  offer & downstream   : pass - no site changes logged                                   [-, medium]
  external             : pass - CPM flat                                                 [-, medium]

confidence     : low - immature window, sub-noise volume, unverified reconciliation
verdict        : insufficient evidence - observed "collapse" fully explainable by attribution lag + learning reset
evidence       : every historical trailing week shows the same immature dip; edit date precedes the volatility
findings       : 1) wait: judge only a lag-mature window ≥14 days post-edit
                    [high, high, avoids paying for variance, near-zero - freeze and wait, media buyer]
                 2) get CRM read access before the next diagnostic run
                    [medium, -, unblocks reconciliation on every later run, an hour of access admin, ops]
gate math      : at ~2 conversions/day, ≈3 more weeks are needed for the noise band to shrink below a 30% delta
prediction     : none issued - a prediction on this data would be noise laundered as analysis
handoff        : none - no fix is recommended, because no defect is established
re-check       : 2026-08-31, mature window, edits frozen until then
```

**The wrong move**: doubling the budget "to compensate". Another significant edit would reset learning again, extend the volatile window, run CPAs 20-50% hotter through it (Grow With Sakib), and - because the trailing week always looks bad - the dashboard would "confirm" the account is broken, justifying the next panic edit. The right move costs nothing: freeze, wait for maturity, then diagnose. The most expensive failure mode in low-volume accounts is not a defect - it is treating variance as a defect and paying for the fix.
