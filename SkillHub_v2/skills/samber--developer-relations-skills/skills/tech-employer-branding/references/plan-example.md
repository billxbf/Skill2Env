# Worked plan example

A full plan for a fictional company, then a negative example showing the most tempting failure. The company, its numbers and its findings are **illustrative inventions** - use them to calibrate section depth and tone, never as benchmarks to quote.

## The setup (from the Interview)

- **Company:** Nordwind Analytics, a 60-engineer scale-up, self-hosted data-pipeline product with an open-source ingestion library that has outside contributors.
- **Accountable owner:** VP Engineering.
- **Hardest tier to land (question 3):** senior and staff.
- **Instrumentation (question 5):** offer-acceptance 64%, source-of-hire dominated by two agencies.
- **Verification surfaces (question 6):** 3.4 employer-review rating across 41 reviews, recent ones alleging chaotic on-call; present in compensation databases with ranges below what the company actually pays; two forum threads on the on-call theme.
- **Honest weaknesses (question 7):** real on-call load on two legacy services, no promotion committee yet.
- **Deadline (question 11):** six senior hires within three quarters.
- **Mandate (question 12):** compounding - the founders want a durable funnel, not a push.
- **Ceiling (question 13):** four protected engineer-hours a week, one talent-lead owner, no new headcount.

Offer-acceptance at 64% is below the 70% floor, so the plan leads with the trust gap, not with content - that single baseline reorders everything below.

## The plan

```markdown
# Engineering employer-brand plan: Nordwind Analytics, Q3 2026 – Q1 2027

## Position

Scale-up, senior/staff target, OSS core with existing contributors. Offer-acceptance
64% (below the 70% re-plan floor). Agency-dominated sourcing = headroom. Review
surfaces contradict the current careers page on on-call; comp databases understate
real bands.

## EVP

- Interest: own the multi-region rewrite of an ingestion pipeline moving 40M rows/day;
  Kafka-to-object-store migration decided in public RFCs.
- Development: staff track exists in writing; promotion committee does NOT exist yet; said plainly, with the date one is planned.
- Economic: publish the real bands (currently understated on comp databases by ~15%).
- Social/application: contributors ship to the same repo candidates can read today.
- What we don't offer: no promotion committee yet; genuine on-call on two legacy
  services until the Q4 decommission; hybrid, not remote-first.
- Mismatch check: the old careers page claimed "no meetings culture": deleted; forum
  threads contradict it.

## Channel bets

1. Posting + process fix (owner: talent lead, tier: all): rewrite the three senior
   postings with real stack, interview stages, on-call terms; cut loop from 6 stages
   to 4. Signal: interview-abandon rate. Review: 6 weeks.
2. Referral program (owner: VP Eng, tier: senior/staff): structured quarterly ask +
   bonus, targets the team's ex-colleague graph. Signal: referral share of qualified
   pipeline. Review: 8 weeks.
3. Salary-band publication (owner: talent lead, tier: junior→senior): real bands on
   postings and corrected on comp databases. Signal: apply-starts per posting.
   Review: 8 weeks.
4. OSS contributor path (owner: staff engineer, 4h/week, tier: senior/staff): label good-first-issues, pay top-3 contributors, document a contributor-to-hire path. Signal: repeat outside contributors. Review: end of horizon.

## Starved

The engineering blog. High value for the senior tier, but it needs writing hours the
ceiling doesn't cover this horizon. Promotion condition: the Q4 decommission frees
the two engineers who volunteered to write; revisit then.

## Fix-first

On-call reality precedes any claim touching it: no "sustainable on-call" language
anywhere until the Q4 decommission lands. Respond to the 5 most recent reviews now
(owner: VP Eng, this week).

## Measurement

Baselines: offer-acceptance 64%, referral share 18%, senior time-to-fill 71 days.
Re-plan triggers: acceptance still <70% at horizon end; rating drops below 3.2.

## Refused

No seeded reviews. No "72%/69%/50%" statistics in any internal deck. No culture
claims the forum threads currently contradict. No job-board spend for the senior
tier.

## Review

Early re-plan on: a leadership change, the decommission slipping past Q4, or the
rating dropping two consecutive months.
```

Why this plan holds together: bet 4 (OSS-as-funnel) survives despite losing every efficiency round because the Interview answered both promotion conditions (a real OSS core and a compounding mandate), and it is funded properly (a named owner with protected hours, paid contributors), not as a token effort. The blog is starved _with a named promotion condition_, so it can return without re-litigating the plan. And the fix-first section keeps the RJP logic honest: no claim ships before the reality it describes does.

## Negative example - the funnel-shaped plan

The same company, planned the tempting way:

```markdown
## Channel bets (rejected draft)

1. Publish 2 engineering blog posts/month showcasing our world-class culture.
2. Employer-brand video campaign: "engineers love it here".
3. Boost job-board spend for senior roles.
4. Ask the team to leave positive reviews to lift the rating past 4.0.
```

Four failures, each mapped to the skill's rules:

1. It ships culture-marketing content on top of a 64% acceptance rate and live forum threads - content amplifying a trust problem.
2. It spends on job boards for a tier that specialist recruiters consistently report is not reached through postings - an option the skill deletes, not demotes.
3. It solicits reviews, which engineers read as a stronger negative signal than the 3.4 rating itself - a refused tactic.
4. The phrase "world-class culture" is exactly the aspirational claim the psychological-contract-breach mechanism punishes: every hire it lands arrives with expectations reality then violates, converting a branding spend into future turnover.

The tell is structural: the rejected draft has no Fix-first section, no Starved section, and no baseline it could fail against. A plan that cannot fail is a wishlist.
