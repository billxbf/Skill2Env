# Sourced benchmarks, and what this skill sets itself

Contents: how to read this file; published free-to-paid conversion bands; the developer-specific conversion finding; measurement definitions; published net-revenue-retention bands; the sales-economics test; numbers this skill sets itself; numbers nobody publishes.

## How to read this file

Two kinds of number appear in a GTM memo and they must never be mixed:

- a **sourced** number comes from a published study or benchmark post; quote it with its source and its measurement definition
- a **self-set baseline** is a defensible starting point with no study behind it; present it as adjustable and say so out loud

Everything in the first four sections is sourced. Everything after "Numbers this skill sets itself" is not.

The published figures below come from Lenny's Newsletter benchmark posts, treated as well-attributed; re-check the live post before publishing as fact:

- _What is good free-to-paid conversion_
- _What is good retention?_
- _The Transition: Layering sales onto a bottom-up self-serve product_

## Free-to-paid conversion, by free-surface model

From _What is good free-to-paid conversion_, described as based on a survey of 1,000+ products.

| Free surface               | GOOD  | GREAT  |
| -------------------------- | ----- | ------ |
| Freemium, pure self-serve  | 3-5%  | 6-8%   |
| Freemium with sales-assist | 5-7%  | 10-15% |
| Free trial, time-limited   | 8-12% | 15-25% |

Related findings from the same source:

- sign-up rate is lower for free-trial products than for freemium (5% vs. 9%)
- reverse trials convert at roughly twice classic freemium at similar sign-up rates
- larger target customers correlate with lower conversion
- 40-60% of new users never return after day one
- 44% of free-trial companies have sales contact more than half of sign-ups, against 24% of freemium companies

## The developer-specific finding

**Developer-focused companies show a median free-to-paid conversion of 5% - half the median of non-developer-focused companies** (same source).

This is the single most useful published number for this skill. A developer tool converting at 2% is not obviously broken and a blended B2B benchmark will tell it that it is. Use the figure to reset expectations, not as a target: a median is the middle of a distribution that includes products with a very different paid boundary from yours.

## Measurement definitions the bands assume

Quoting a band while measuring differently is how these get misused.

- Free-to-paid = accounts that begin paying within their first six months ÷ accounts created in the measurement window.
- Measure by cohort. A lifetime ratio flatters any product whose sign-ups grew.
- Define at account level - one user or a group of them - not per user.
- Report per audience as well as blended.
- Net revenue retention = a cohort's MRR today ÷ that same cohort's MRR twelve months ago.

## Net revenue retention, 12-month

From _What is good retention?_ - a survey of roughly twenty named growth practitioners, not a single published headline figure. Each expert gave their own GOOD/GREAT number per business model; the row below is this skill's compression of that spread into one representative point per cell, generally set at or near the low end of the reported range.

| Business model                       | GOOD  | GREAT |
| ------------------------------------ | ----- | ----- |
| Bottom-up SaaS                       | ~100% | ~120% |
| Land-and-expand, very small business | ~80%  | ~100% |
| Land-and-expand, SMB and mid-market  | ~90%  | ~110% |
| Enterprise SaaS                      | ~110% | ~130% |

Read the row that matches the motion actually chosen, not the aspirational one. A bottom-up product measuring itself against the enterprise row will conclude that expansion has failed when it is performing normally.

## The sales-economics test

From _The Transition_: a salesperson added to a self-serve motion should return roughly **4x their fully loaded cost** in incremental revenue.

Apply this before arguing about which motion to run. It converts "should we hire a rep?" into arithmetic: incremental revenue per rep must clear four times salary plus overhead, which for most single-developer-account products means the answer is no until account rollup exists and multi-developer accounts are common.

The same source names the opposite risk: waiting too long to add sales lets sales-assisted competitors firewall a self-serve-only product out of enterprise segments - Dropbox is the cited casualty. Both failure directions are real; the 4x test is what tells you which one you are in.

## Numbers this skill sets itself

These are this skill's own baselines. They are internally consistent and reasoned, and **no published study supports them**. Move them when your data says otherwise.

- One primary motion, at most one secondary.
- Two or three candidate motions presented before a recommendation, never one.
- A qualification threshold expressed as one sentence.
- A response window measured in hours, not days, for accounts above the threshold.
- Multi-threading defined as two engaged contacts, one of them manager-level.
- A leading-indicator set of five or fewer numbers.
- Quarterly review of the threshold sentence.
- The step 3 motion ordering - effort, value and efficiency across the four motions, and the effort magnitudes behind it. Reasoned from what each motion forces a company to build, hire and coordinate; nothing published ranks GTM motions this way, and the order is meant to be re-ranked against what a given team already has.

## Numbers nobody publishes

Searched for and not found, so derive them from your own cohorts and label them accordingly:

- deal-size cut-offs separating self-serve, inside and field sales
- time-to-first-value targets for developer products
- PQL-to-opportunity conversion for developer tools
- the share of accounts that should reach a depth signal
- how many active developers an account needs before it converts

That last one is the number a threshold rule depends on most, and it is company-specific by construction - a product whose paid boundary is volume and one whose boundary is seats will disagree by an order of magnitude.
