# Worked plan examples

All numbers below are illustrative planning inputs for fictional companies, not benchmarks - take real values from the interview and from the client's own account data.

## Example 1 - B2B plan (passes the gates)

**Context from interview:**

- B2B data-security vendor, $60k ACV, 5-month cycle.
- Three willing featured people (CTO, a staff engineer, one customer champion), written agreements signed.
- Retargeting audiences and conversion campaigns already live.
- $9k/month for this format (~30% of channel budget), target list of 800 accounts.
- Not regulated, no EEA audience.

**Plan produced:**

- **Roster:** CTO + staff engineer (employees, paid-promotion label + visible role) + customer champion (non-employee: partnership label, licensed usage rights, usage fee, 90-day term). Portfolio of three, so one revocation cannot end the program. Takedown-and-replace step: on any revocation or departure, pause within 24h and rotate the next scored post from another person.
- **Post selection:**
  - Each person's trailing 20 posts ranked by engagement rate against their own median.
  - Top-quartile evergreen posts about the buyer's problem shortlisted.
  - Product-pitch posts and a funding announcement excluded.
  - Format check: two shortlisted carousel posts dropped as ineligible.
  - Each selected post: author edits a tracked link in before launch, one day after its organic peak. The in-post edit is promoted over the default pinned comment here because all three authors edit their own posts unprompted, so the ask costs nothing and the higher click volume decides.
- **Sequence:** awareness-first. The brand is better known than either individual in this market, and the cold prospecting layer already exists.
  - Person-fronted ads warm the existing cold-engager pool.
  - Engagers hand off to the conversion-capable retargeting stage (designed in `mbfinotti/advertising-skills@retargeting-funnel`).
  - All engager/viewer audiences confirmed created before launch.
- **Audience:** matched account list (800 accounts, partial match expected) layered with security + IT functions, manager-and-above seniority ≈ 24,000 members.
  - Frequency math: $9k/month at the account's observed CPM supports meaningful weekly frequency at this size. List not widened.
  - Exclusions (6 entries vs. 3 inclusion layers): customers, open pipeline, employees, competitors, students, /login visitors (180-day window).
- **Budget/bidding:**
  - $100/day per campaign, two campaigns.
  - Max delivery days 1-14, then cost-cap at ~75% of suggested bid.
  - Allocation share capped at 30% of channel budget, with the rule "widen the list before adding budget" written into the plan.
- **Measurement:**
  - Week-6 gate: cost per landing-page click ≤ the account's brand-ads baseline ($6.10 from its own last quarter), engager pool ≥ the platform's serveable floor. Fail branches as in SKILL.md.
  - Two-quarter review on influenced pipeline and sales-accepted opportunities against a 3x pipeline-to-spend bar agreed with the client.
  - Reported CTR explicitly excluded from all success criteria.

## Example 2 - B2C variant (what changes)

**Context:** founder-led skincare brand, $55 average order, founder posts short-form video weekly, full-funnel objectives available on the chosen consumer platforms.

Only the deltas from Example 1:

- **Objective:** direct response (purchase) from day one - no forced trust layer, no structural handoff. Sequencing collapses to one performance campaign plus standard retargeting.
- **Permission:** per-video authorization codes, 60-day terms, tracked in a renewal calendar - expiry management replaces revocation risk.
- **Selection cadence:** promote only videos that already earn saves/shares/watch-through organically. Refresh every 3-7 days (short-video). The B2B two-week rotation is far too slow here.
- **Measurement:** split test person-fronted vs brand-account creative. Keep the person-fronted variant only while its pixel CPA is at or below the brand control. No pipeline window, no landing-page-CPC gate.
- **Governance kept identical:** written agreement, disclosure labelling, portfolio thinking (the founder plus at least one creator so the account isn't hostage to one person's feed).

## Example 3 - Broken plan (negative example, with diagnosis)

**The plan as submitted:** "Boost the CEO's latest post to our whole TAM (300,000 professionals) at $2k/month with a conversion objective. The CEO is on board - he liked the idea in the hallway. No link needed, people will find us. We'll judge it on CTR after two weeks; our agency says this format gets 3-6x the CTR of company ads."

**Diagnosis, mapped to the skill:**

1. **Consent:** a hallway remark is not consent, and nothing is per-post. No written agreement means the company has no rights to the creative and no revocation/pause terms. Fails the eligibility gate before anything else.
2. **Objective:** a conversion objective is structurally unavailable on the trust-layer network. The plan as written cannot be built. Running it "cold as direct response" is the most common documented misuse even where objectives allow it.
3. **Audience/budget:** $2k/month against 300,000 people produces near-zero frequency, the exact mismatch practitioners warn about.
   - Either cut to a list the budget can hit repeatedly, or raise budget. Neither was considered.
   - No exclusion list at all: customers and employees will absorb spend.
4. **No capture layer:** nothing says retargeting audiences exist. Engagement generated before they are created is unrecoverable.
5. **No link, no declaration:** "people will find us" is the no-destination failure mode. It must be a pinned-comment link, a tracked-link edit, or a declared retargeting-pool builder - the plan chose none.
6. **Measurement:** judging on reported CTR adopts the one metric shown (in the largest published dataset) to correlate negatively with pipeline, and the quoted "3-6x CTR" is an agency figure with an engagement-inflated denominator. Two weeks is also inside the learning window.
7. **Single person:** the whole program dies the day the CEO revokes, gets busy, or leaves.

**Smallest viable fix:**

- Written agreement with the CEO plus one more featured person.
- Engagement objective.
- Matched list sized to the budget with the standard exclusions.
- Retargeting audiences created pre-launch.
- A tracked link in the author's pinned first comment, the smallest ask that still attributes clicks.
- Week-6 gate on landing-page CPC and pool growth instead of CTR.
