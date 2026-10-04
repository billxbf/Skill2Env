# Program archetypes and published benchmarks

Contents: archetype comparison table · what six published programs actually do · outcome benchmarks · how to choose · points-ledger mechanics · two-tier pattern.

Every fact in the "published programs" and "outcome benchmarks" sections is sourced to the linked page or case study. Everything in "how to choose" is a judgement call this skill makes, not a published rule - the two are separated deliberately so a reader can tell which is which.

## The four shapes

Every named vendor or foundation champions program collapses into one of four shapes. The shape decides intake, cohort size, and how much staff time the program burns.

| Archetype                    | Intake                                   | Cohort shape              | Staff cost                             | Fails when                                                                    |
| ---------------------------- | ---------------------------------------- | ------------------------- | -------------------------------------- | ----------------------------------------------------------------------------- |
| Invite-only circle           | private tap on the shoulder              | 5-20, no public roster    | very low                               | the community grows past the point where a private tap looks fair             |
| Award / recognition          | nomination-only, closed committee review | small, fixed, dated term  | low per member, spiky per review cycle | nominators all sit inside one team, so the roster mirrors that team's network |
| Application cohort           | open window, published criteria          | medium, annual intake     | medium; review load spikes once a year | criteria stay unpublished, making every rejection indefensible                |
| Points / contribution ledger | automatic on tracked activity            | unbounded, self-selecting | high tooling cost, low review cost     | tracking is built on a spreadsheet the program outgrows                       |

## What published programs actually do

Verified against each program's own public page (re-fetched 2026-08-28). Cohort dates and application windows roll every year - re-check the linked page before quoting a date to a user.

- **CNCF Ambassadors** (<https://www.cncf.io/people/ambassadors/application-process/>) - application cohort. Applicants must be 18+ and must annually review and sign the "Ambassador Standards of Excellence".
  - Meet **two or more** of five criteria:
    - Project contribution (minimum DevStats score 20, voter status, or SIG/TAG membership).
    - Community leadership (1 year minimum, ideally 2 - Kubernetes Community Days or Cloud Native Community Group organizer, program committee member, event co-chair).
    - Public speaking at industry or CNCF events.
    - Mentorship via LFX/GSoC/Outreachy on a CNCF project.
    - Non-paywalled content creation.
  - Dated cohorts with one window a year: the 2024 cohort ends 1 October 2026, the 2025 cohort ends 1 October 2027.
  - The 2026 cycle shows the full rhythm: window open late May, closed 12 July 2026, notifications in August, cohort starting September - roughly three months from close to start, worth copying as the planning envelope for an annual intake.
  - Benefits: recognition, networking, funding support for events, speaking and content, discount codes for CNCF-sponsored events, exclusive swag, input on community initiatives.
- **HashiCorp Ambassadors** (<https://www.hashicorp.com/en/ambassador>) - application cohort. Single annual window (1 December - 5 January), accepting both self-applications and nominations from community members or employees, judged on activity "during the preceding twelve months", cohort announced at the start of the calendar year.
  - Perks are access-shaped: care package, product release briefings, roadmap reviews, feedback sessions, collaboration on blogs, video, certification development and conference talks.
- **MongoDB Champions** (<https://www.mongodb.com/community/champions>) - award/recognition. Nomination-only, with nominations from employees, current Champions and program **alumni**.
  - Criteria: advanced or expert product knowledge, leadership through community education, and visibility through talks, blogs, videos, user groups and forum answers.
  - Perks: executive access, roadmap and preview programs, an annual Champions Summit, reserved content features and speaking slots, and training in public speaking, writing and social.
  - A separate application-based **Creators Program** with a much larger intake acts as the feeder tier - the two-tier pattern below.
- **Twilio Champions** (<https://www.twilio.com/en-us/champions>) - application cohort. Applications run in windows and close between cohorts.
  - Eligibility: 18+, English fluency, demonstrated expertise, contribution through speaking, content or forums, and a commitment to represent the brand in line with company values.
- **GitHub Stars** (<https://stars.github.com/nominate/>) - award/recognition by peer nomination, capped at three nominations per nominator, with a public **alumni roster** published alongside the active one.
- **Elastic Contributor Program** (case study with Ully Sampaio, <https://developerrelations.com/case-studies/globalising-a-champions-program>) - points ledger. See the mechanics section below.

## Outcome benchmarks

Two public numbers describe what a champions program produces. Both are weak evidence; quote them as the shape of a plausible outcome, never as a target.

- **Elastic Contributor Program, 2019 pilot → 2022** (case study, first-party): first-party reporting with no baseline comparison, from the team that ran the program.
  - +13% participants, +38% contributions, +11% participating countries, +25% supported languages.
  - The contribution mix rebalanced away from the flagship product (Elasticsearch fell from 92% to 78% of contributions).
  - Four community members were hired by the company.
- **Notion ambassadors**: 300+ ambassadors, 1M+ template downloads, and roughly 25% of new users arriving via community referrals. Reported second-hand (Corey Haines, _Founding Marketing_, ch. 12), not confirmed by Notion itself, and describing a consumer-adjacent product at extreme scale.

This is why the Step 8 scorecard in `SKILL.md` is explicitly self-set rather than benchmarked against other programs.

## Choosing between them

The ranking lives in `SKILL.md` Step 2 - efficiency: `invite-only circle > award > application cohort > points ledger`. These bullets follow that order and give the condition that moves a user off it.

- Below roughly 500 active community members, pick **invite-only**. A public program with three members reads as a failed program, and that failure stays visible. The 500 figure is self-set: the nearest published anchor puts ambassador programs in the 1,000+ member "enable others" phase of community growth, and a private circle needs less community than a public roster does.
- Pick **award/recognition** when the goal is status transfer to the member - their career benefits from the title - rather than throughput of activity.
- Pick an **application cohort** once the community is large enough that a private tap looks arbitrary. Published criteria are the thing that makes a "no" survivable, and they are what buys the strongest cohort of the four shapes.
- Pick a **points ledger** only with engineering capacity to build tracking, and only when inclusion matters more than scarcity.
- Programs graduate upward: invite-only → application cohort as the community grows. Design the first one so it can be retired without embarrassment.

## Points-ledger mechanics

Drawn from the Elastic case study, which is the most detailed public account of running one.

- The program existed because Elastic recognised code contributions and nothing else, leaving community organizers, translators and content creators invisible - "we had no formal way to either recognise them or even to thank them."
- Every contribution type earns points weighted by **effort and current strategic need**. The weighting is a steering wheel, not a fairness calculation: under-served areas get more points until the imbalance closes. Revisit the weights every cycle and announce the change.
- Counted contributions span talks, event organizing, blog posts, Stack Overflow answers and social content - deliberately wider than code.
- Points redeem for training, certification and conference trips, never cash.
- Point values were **calibrated per region**: Brazil's community contributed mostly through events, other markets through content, so one global table would have systematically under-recognised one of them.
- **Publish the ledger.** A private point total only staff can see recreates the gatekeeper the ledger was meant to remove. Elastic's stated reason for transparency was governance, not gamification: "We wanted to encourage conversations between community members rather than for the Community team to act as a gatekeeper."
- **Budget the tooling.** GitHub-based tracking did not survive the program going global; Elastic built an internal portal with leaderboards and browsable contribution feeds. Treat that as a cost of the archetype, not a surprise.
- Reported results, 2019 pilot → 2022:
  - +13% participants, +38% contributions, +11% participating countries, +25% supported languages.
  - The contribution mix rebalanced away from the flagship product (Elasticsearch fell from 92% to 78% of contributions).
  - Four community members were hired by the company.
- Measure the ledger to award recognition, never as a quota whose miss triggers punishment.

## The two-tier pattern

When demand exceeds the cohort you can support, run two tiers rather than picking a side in the scarcity-versus-inclusion argument:

- **Feeder tier** - open, low-friction, self-serve enrolment, light perks (a badge, a channel, early-read access). It absorbs everyone the inner cohort has to reject.
- **Inner cohort** - selective, dated term, high-touch access perks, recruited primarily out of the feeder tier.

MongoDB's Creators → Champions funnel is the clearest published example. The benefit beyond capacity: the feeder tier generates the observable activity record the inner cohort's selection needs, so selection stops depending on who the program owner happens to have noticed.
