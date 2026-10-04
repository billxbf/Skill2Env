# Report Template and Worked Example

## Table of Contents

- [Template](#template)
- [Worked example (condensed - B2C, paid social)](#worked-example-condensed---b2c-paid-social)
- [Negative example - what a finding must never look like](#negative-example---what-a-finding-must-never-look-like)

## Template

```
LANDING PAGE AUDIT - <page>, <date>
traffic        : <platform(s), campaign type> | model: B2B | B2C
goal           : <the one action> | downstream truth: <pipeline | revenue>
window         : <dates> | volume: <sessions>, <conversions> | volume floor: cleared | NOT cleared
economics      : <current CPA/ROAS> vs target <target> - gap: <x>
inputs         : <ad creative: yes/no | analytics: yes/no | recordings: yes/no | page: fetched/pasted/screenshots>

VERDICT
<One paragraph: is the page the problem, or does the evidence point upstream?
If upstream: name the signal, hand off, stop here.>

FIX NOW (max 7, ranked by efficiency: funnel step unblocked per unit of effort,
best ratio first - not cheapest first; compliance removals lead regardless)
1. <element> - <failure> → <specific change>
   funnel step: <which leak this unblocks> | evidence: opinion|observation | source: research|consensus
   severity: critical|major|minor | effort: hours|days|weeks
2. ...

RULED OUT (deleted from the ranked list, not deferred to the bottom of it)
- <fix or family> - removed by <effort ceiling | no dev access | page not owned by this team>

TEST, DON'T GUESS
- <change> - judged on <metric>. <Why it is plausible but not evidenced enough to just ship.>
(Framing: a portfolio of bets; most tests lose.)

NOT A PROBLEM
- <what was checked and is fine, and against which criterion>

COULD NOT CHECK
- <missing input or skipped capability-gated check> - <what that means for the findings above>

RE-CHECK
- <per shipped fix: the funnel step expected to move, direction, judged on <date> at matched lag maturity>
```

## Worked example (condensed - B2C, paid social)

```
LANDING PAGE AUDIT - /spring-bundle, 2026-08-26
traffic        : paid social, cold prospecting | model: B2C
goal           : purchase | downstream truth: revenue
window         : last 28 days | volume: 41,200 sessions, 310 conversions | volume floor: cleared
economics      : CPA $61 vs target $38 - gap: 1.6x
inputs         : ad creative: yes | analytics: yes | recordings: no | page: fetched, mobile + desktop

VERDICT
The page is the problem. Upstream checks pass: CTR is stable, frequency flat, the purchase
event fires once and reconciles with the order table within 6%. The funnel leaks hardest
between landing and add-to-cart on mobile (82% of spend), and the first screen breaks the
ad's promise - the evidence below is consistent with a message-match and mobile-friction
failure, not an ad or offer failure.

FIX NOW
1. Hero headline - ad promises "the spring bundle, 30% off"; page opens "Welcome to
   <brand>" with no bundle or price in the first screen → open with the bundle offer,
   in the ad's wording, price visible
   funnel step: land → engage | evidence: opinion | source: consensus (message match)
   severity: critical | effort: hours
2. Hero visual - ad creative shows the product in use; page hero is an abstract brand
   pattern → reuse the ad's key frame so the clicker recognises the page on sight
   funnel step: land → engage | evidence: opinion | source: consensus
   severity: major | effort: hours
3. Mobile hero video (4.1s LCP on 4G field data vs ≤2.5s good) → replace autoplay video
   with a static bundle image; move the video below the fold
   funnel step: land → engage | evidence: observation | source: research (Core Web Vitals)
   severity: critical | effort: days
4. Shipping cost first shown at payment step → show delivery cost and time on the product
   section; late-revealed costs are the top stated abandonment reason (Baymard, B2C)
   funnel step: add-to-cart → purchase | evidence: observation | source: research
   severity: major | effort: days

TEST, DON'T GUESS
- Guest checkout as default (account creation currently pre-selected) - judged on
  checkout completion rate. Plausible per Baymard's forced-account findings, but this
  checkout's own field data doesn't isolate the step, so test rather than assume.

NOT A PROBLEM
- CTA count: one primary action per screen, secondary "see contents" link correctly
  subordinated.
- Contrast: CTA passes 4.5:1; form labels visible; keyboard focus visible.
- Policy: destination loads, no redirect chain, offer terms match the ad.

COULD NOT CHECK
- Session recordings unavailable - form-hesitation and rage-click reads are absent, so
  fixes 1-3 rest on heuristics plus funnel position, not observed behaviour.
- INP field data insufficient sample on desktop - mobile only.

RE-CHECK
- Fixes 1-3: land → engage rate on mobile paid social, expected up, judged 2026-09-23.
- Fix 4: add-to-cart → purchase rate, expected up, same date.
```

Note the order: fix 2 is only "major" and fix 3 is "critical", yet 2 ships first - an hour
of asset swap against days of video work on the same funnel step. Efficiency ordering, not
severity ordering. Severity is one input to it, never the sort key.

## Negative example - what a finding must never look like

> "Shortening the form from 6 fields to 3 will increase conversions by 30-50% based on
> industry data. Also consider adding a countdown timer to create urgency."

Three violations in two sentences:

- A promised percentage lift (forbidden: the cited "industry data" is the contested per-field folklore).
- No evidence class or severity.
- A recommended manufactured-urgency widget, which this skill flags against pages, never prescribes.

The same finding, written correctly, is fix-list material:

- Name the fields that are removable (or, B2B, worth keeping for lead quality).
- State "every field costs conversion, non-linearly - no trustworthy percentage exists".
- Class it as opinion unless field-level abandonment data exists.
- Skip the timer entirely.
