# Worked examples

Two positive plans (one B2C conversion, one B2B always-on) and one annotated negative example. Fictional brands; every number illustrative, not a benchmark.

## Table of Contents

- [Example 1 - B2C conversion campaign](#example-1---b2c-conversion-campaign)
- [Example 2 - B2B always-on ambassador program](#example-2---b2b-always-on-ambassador-program)
- [Negative example - annotated](#negative-example---annotated)

## Example 1 - B2C conversion campaign

Context: skincare DTC brand, launch flight, 8 micro-creators on short-video platforms, $40K, 6-week flight. Tracking confirmed in interview: unique codes, UTM links, post-purchase survey, platform pixel. Report read by the growth lead; decision: which creators to rebook.

```
MEASUREMENT PLAN - Lumen Skin spring launch, 2026-03-02
Header      : Lumen Skin | conversion objective (performance funnel stage) | Mar 16 - Apr 26 |
              $40K | 2 short-video platforms | 8 micro-creators
Glossary    : CPA = total flight cost / attributed conversions (dedupe: code OR link OR survey,
              priority code > link > survey), 30-day window, flight timezone UTC-5.
              CPA per creator = that creator's fee + their creator-specific amplification,
              divided by conversions attributed to them. Shared costs (platform fees, the
              $4K shared production day) are EXCLUDED from the per-creator numerator and
              reported only at flight level - so per-creator CPAs do not sum to flight CPA,
              and that is stated on every report carrying both.
              ER = engagements / reach x 100 (ERR) - reach via contracted creator analytics access.
              Conversion = first paid order. View = per-platform definition captured at flight
              start, date-stamped; views never summed cross-platform.
KPI tree    : PRIMARY  CPA per creator (target: none - first flight, baseline-setting)
              SECONDARY conversion rate per creator, AOV of attributed orders, link CTR
              GUARDRAIL code-leakage rate (<3% of redemptions), return rate, new-customer share
KPI mapping : CPA -> codes + UTMs + survey (triangulated) -> checkout system + analytics + survey tool
              ER -> creator analytics API access (contracted) -> per-creator monthly export
              Leakage -> redemptions with zero matching link click -> checkout x analytics join
Attribution : codes (leak monitor + single-use fallback) + UTMs (one per creator per placement) +
              post-purchase survey ("How did you hear about us?" with creator names listed) + pixel
              (floor only, signal loss noted). Click-based and survey-based CPA reported side by side.
Baseline    : trailing 8-week branded-search volume and direct traffic captured 2026-03-09;
              trailing ER median per creator captured from vetting data.
Test design : DIRECTIONAL ONLY. Power check: ~450 expected conversions across 8 creators cannot
              detect a 5-10% MDE at region level. No incrementality claim will be made.
Cadence     : growth lead -> weekly -> pacing, CPA by creator, leakage alerts -> pause/shift budget
              founder -> end of flight -> CPA + survey-vs-click gap + rebook shortlist -> rebook decision
Data sources: checkout (codes, orders) | analytics (UTM sessions) | survey tool | creator API access |
              pixel (flagged: floor). Zero screenshot sources.
Blind spots : dark-social shares strip UTMs; survey recency bias; pixel undercounts mobile opt-outs;
              buyers who neither click nor use codes are invisible to everything except the survey.
Open items  : confirm survey tool can list all 8 creator names; add analytics-access clause to the
              two unsigned creator contracts.
```

Why it passes:

- Every KPI is recomputable, backed by a confirmed capability.
- First-flight target honesty.
- Underpowered test declared instead of promised.
- Leakage guardrail present.
- Blind spots stated.

## Example 2 - B2B always-on ambassador program

Context: devtools SaaS, 4 newsletter/podcast creators on retainer, always-on. Tracking confirmed: UTM links, vanity URLs, HDYHAU field on signup form, CRM. No pixel, no codes (no checkout). Report read by VP Marketing; decision: continue/expand the program at annual budget review.

```
MEASUREMENT PLAN - DevFlow ambassador program, 2026-01-12
Header      : DevFlow | always-on ambassador (pipeline objective) | rolling quarters | 4 creators |
              newsletters + podcasts
Glossary    : Influenced pipeline = open opportunities whose contact cohort selected a creator/
              newsletter/podcast HDYHAU option OR entered via creator UTM/vanity URL, 90-day window.
              Signup = workspace created. HDYHAU analyzed at cohort level, never per-deal.
              Podcast downloads = publisher-reported; IAB v2.2 certification asked, answer pending.
KPI tree    : PRIMARY  influenced pipeline per quarter (target: trailing 2-quarter median once it exists)
              SECONDARY signups via vanity URLs, HDYHAU creator-channel share, branded-search trend
              GUARDRAIL creator content cadence vs retainer terms, HDYHAU "other/blank" rate (<40%)
KPI mapping : pipeline -> HDYHAU cohort + UTM/vanity -> CRM + analytics
              downloads -> publisher reports (flagged: publisher-sourced, certification unconfirmed)
Attribution : HDYHAU is PRIMARY (dark social dominates: <20% of current closed-won deals name a
              trackable channel), UTM/vanity secondary, branded-search volume as corroborating proxy.
Baseline    : 12 months of branded-search volume and signup HDYHAU distribution captured pre-program.
Test design : DIRECTIONAL ONLY - B2B conversion volume (~60 opportunities/quarter) cannot power
              geo-lift; revisit if the program quintuples. Pre/post branded-search movement reported
              against baseline with correlational framing.
Cadence     : program manager -> monthly -> cadence, vanity signups, HDYHAU share -> creator check-ins
              VP Marketing -> quarterly -> influenced pipeline vs median, branded-search trend ->
              continue/expand/cut at annual review
Data sources: CRM (HDYHAU, pipeline) | analytics (UTM/vanity) | publisher reports (flagged) |
              search console (branded queries). Zero screenshot sources; publisher numbers flagged.
Blind spots : per-deal creator credit is impossible by design (cohort-level only); podcast downloads
              prove delivery, not response; multi-stakeholder buying committees mean the form-filler
              may not be the person the creator influenced.
Open items  : IAB v2.2 certification answer from both publishers; add "creator/newsletter/podcast -
              which one?" follow-up option to the HDYHAU dropdown.
```

Why it passes:

- Revenue object is pipeline, not orders.
- HDYHAU promoted to primary with the threshold stated.
- Publisher-sourced numbers flagged.
- Incrementality honestly declined with the reason.

## Negative example - annotated

The same B2C brand as Example 1, as a plan that fails. Each `<- flaw` annotation names the defect.

```
MEASUREMENT PLAN - Lumen Skin spring launch
Goals    : go viral, build buzz                          <- no funnel stage, no decision named
KPIs     : total reach, impressions, likes, followers    <- vanity set on a conversion campaign
           EMV target: $250K earned media value          <- AVE derivative presented as financial value
           ER target: 4.5% (industry benchmark)          <- vendor benchmark as target; denominator unstated
Tracking : last-click via the affiliate network          <- single method; upper funnel structurally
                                                            under-credited; no leakage guardrail
           creators send monthly screenshots             <- falsifiable source, unflagged
ROI      : projected 5.78x based on industry data        <- the $5.78 vendor figure as a planning input
Testing  : we will run a lift test to prove incrementality  <- no power check; ~450 conversions cannot
                                                             detect the MDE; "no lift" would kill a
                                                             possibly-working channel
Baseline : (none)                                        <- launch first, measure later; every "lift"
                                                            claim will be unsupported
Reporting: dashboard for everyone, updated live          <- no stakeholder, no cadence, no decision
Views    : combined views across platforms: 2M target    <- sums incompatible view definitions;
                                                            YoY comparison crosses a definition change
```

Structural failures beyond the annotations:

- No glossary at all (nothing is recomputable).
- No blind-spot declaration.
- The primary KPI set (reach/likes) cannot inform the rebook decision the campaign exists to make.
