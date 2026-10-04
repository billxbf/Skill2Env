# Published findings

Every figure and mechanism this skill relies on, split by evidentiary strength, plus the figures it refuses. Quote the tier along with the number: a plan that presents a soft figure as validated loses the exec who checks it, and several execs do check.

## Tier 1: figures published by the organization that produced them, cite freely with attribution

**Stack Overflow Developer Survey 2025** (~49,000 respondents, 177 countries, survey.stackoverflow.co/2025/work):

- Autonomy and trust rank first among job-satisfaction drivers, ahead of competitive pay and "solving real-world problems". Technology and tooling are not the top driver.
- 24.5% of developers describe themselves as happy at work (up from ~20% the prior year); a combined ~75% describe themselves as "complacent" or "not happy".
- Caveat that travels with every use: this is stated preference at large sample, not observed hiring behavior. Do not conflate "engineers say they value X" with "publishing X produces applications".

**Stack Overflow Developer Survey 2022** (83,000+ developers, reported via Forbes):

- Why candidates abandon an interview process:
  - Disliking the tech stack: 32%
  - Disorganized interview process: 24%
  - Odd interview questions: 24%
  - Poor employer reviews: 24%
- Use: the posting and the loop are brand artifacts candidates screen on, so process fixes belong in the channel menu.

**Glassdoor** (two distinct sources, keep them apart):

- 86% of candidates research a company's reviews before applying, forming an opinion after about six reviews: Glassdoor's own US site survey (self-report, published by Glassdoor itself).
- A 0.5-star increase in overall rating is associated with 20% more job clicks and 16% more apply-starts on average: Glassdoor Economic Research (Dr. Andrew Chamberlain), based on platform data, not self-report. The best-grounded elasticity figure in this domain.
- Responding to reviews has a documented positive perception effect.

**LinkedIn Talent Solutions / Talent Brand Index:**

- Job seekers trust current employees' word about a company roughly 3x more than the company's own messaging.
- Companies with a strong talent brand on LinkedIn see on average 2.5x more applicants per posting; a strong talent brand increases InMail response ~25% and rate of hire ~20% ("11 Facts You Should Know About Talent Brand", 2015). Platform correlation: real and named, but not a controlled experiment.

**Realistic job preview (RJP) meta-analyses: the only peer-reviewed causal evidence in this domain:**

- Phillips 1998 (_Academy of Management Journal_); Premack & Wanous 1985 (_Journal of Applied Psychology_); Earnest, Allen & Landis 2011 (_Personnel Psychology_): accurate, specific job previews modestly reduce voluntary turnover and improve met-expectations and perceived organizational honesty.
- Saks, Wiesner & Summers 1996 (_Journal of Vocational Behavior_): specific compensation/reward information (versus "competitive pay" language) improves candidates' person-reward fit assessment: the direct backing for salary bands and leveling docs as a channel.
- The inverse mechanism, psychological contract breach: expectations formed from published material that reality then violates drive dissatisfaction and turnover. This is _why_ honesty outperforms polish, not just an assertion.
- Scope limits to state whenever cited: general hiring research, not engineering-specific; effect sizes modest, not large.

**EVP framework origins:**

- Ambler & Barrow 1996 coined "employer brand"; Backhaus & Tikoo 2004 formalized the EVP → brand-image causal chain (the Design-before-Activation sequencing).
- The **EmpAt scale** (Berthon, Ewing & Hah 2005, _International Journal of Advertising_) is a 25-item instrument with five values (interest, social, economic, development, application), α ≈ 0.93–0.96, independently replicated (Sivertzen et al. 2013; Eger et al. 2019). Validated but **generic to all employers**: state it precisely, a validated generic instrument, never an engineer-specific one. Gartner's EVP model and Universum's rankings are commercial instruments, not peer-reviewed ones.

## Tier 2: named practitioner and company accounts (coherent, but self-reported)

- **Stripe (Greg Brockman, First Round Review):** every recruiting channel measured, optimized for hire quality; referrals consistently outperformed careers-page inbound, which "hasn't delivered a proportionately effective return". The most credible practitioner account of channel effectiveness on record, and the standing counterweight to "publish more".
- **Supabase (Contrary Research's Business Breakdown):**
  - No outbound recruitment until after 32 developer hires over two-plus years.
  - Open source its "primary source of finding new talent".
  - Many of the first ~50 employees came from the OSS community, including a PostgREST maintainer.
  - Runs a formal contributor-to-employee path ("SupaSquad").
- **HashiCorp:** community built before the company existed (Mitchell Hashimoto's Vagrant evangelism, ~2010-2011); sponsored contributors, hired maintainers full-time.
- **Netflix's 2009 "Freedom & Responsibility" culture deck:** the archetypal culture-document-as-recruiting-artifact, and the origin of the practice.
- **Gergely Orosz (The Pragmatic Engineer):** documents wide published total-comp ranges under pay-transparency law (e.g. Netflix advertising $300,000–$900,000 total comp), aggregated by compensation-database sites; documents anonymous forums as where engineers find the comp and culture data recruiters won't volunteer.
- **Senior-tier sourcing consensus:** multiple specialist technical recruiters independently converge on "distinguished/principal engineers are not found through postings or profile searches, but through community reputation and referrals". Practitioner consensus, not a measured study: label it as such.
- All company accounts are self-reported by the company or its founders, with an incentive toward a coherent narrative. Treat as strong illustrations, not audited results.

## Tier 3: practitioner folklore (use as color, never as a figure)

- Negative word-of-mouth from a bad interview or workplace "reaches a large peer audience within days" on developer forums; a referral from a respected engineer "carries more weight than a job ad". Plausible and widely repeated, but unquantified: never attach a reach or conversion number to it.
- The "roughly three open roles per qualified candidate" market-pressure framing circulating in 2026 vendor commentary: narrative context, vendor-blog quality, not a labor-market dataset.
- The "convert developers into customers" hiring-manager anecdote, used as this skill's negative example, is a widely-recirculated anonymous practitioner account: representative, not verifiable.

## Refused figures

The "72% check blog/GitHub" claim, Gartner's 69%, and LinkedIn's "50% more qualified applicants": where each figure actually comes from, and the refusal wording, are in the stat-debunking reference, linked from SKILL.md. Also refuse un-anchored case-study percentages ("17% increase in offer acceptance", "55% decrease in cost per hire") circulating without disclosed methodology.

## Self-set baselines (this skill's own defaults: movable, and say so)

- **Offer-acceptance floor of ~70%** as the trigger to audit trust before funding top-of-funnel: this skill's threshold, derived from practitioner discussion of acceptance-rate norms, not a published standard. Ashby's 2025 Talent Trends platform data (aggregated ATS acceptance data, not self-report) puts technical-role offer-acceptance at ~73% against ~84% for business roles - close enough to corroborate the 70% floor as a reasonable technical-role-specific line, though Ashby's own figure is a market average, not a "problem below this line" threshold.
- **50% of quality hires from referrals + organic/branded inbound** as the "brand is working" benchmark at Stage-0 instrumentation: a widely used practitioner heuristic rather than a measured result.
- **2-4 channel bets per horizon**, one signal each: this skill's own cap, set so the plan stays falsifiable.
- Time-to-fill context: SHRM's 2025 median of 44 days for nonexecutive roles is sourced; "senior engineering typically runs longer" is directional practitioner consensus, so state it without attaching a number.

## Caveats to state out loud

- The employer-branding statistics ecosystem is epistemically poor: most circulating percentages are self-reported survey outputs re-cited across vendor blogs without methodology, control groups, or a traceable primary source. Treat any un-anchored percentage as marketing.
- Engineering specificity and causality rarely arrive together: RJP research is causal but general, Stack Overflow data is engineering-specific but stated-preference. Treat one channel's causal effect (e.g. an engineering blog's) on engineer application or acceptance behavior as unmeasured: never promise channel-level ROI.
- LinkedIn's core survey figures derive from 2010, predating normalized remote work, AI-assisted coding, and the 2023-2025 tech contraction.
