# Community launch brief

Contents: template → worked example (launch verdict) → worked example (do-not-launch verdict) → weak example to avoid.

Present the brief one section at a time and get the user's agreement before writing the next. A brief delivered whole invites a single "looks good" that hides disagreement on the parts that matter.

## Template

```markdown
# Community Launch Brief - <project or product>

## 1. Verdict

Launch / Launch on <condition> / Do not launch - <one sentence of reasoning>.
Gates: demand <pass|weak|fail>, owner <…>, purpose <…>, venue vacuum <…>, seed supply <…>.
Evidence behind each gate: <one line each>.

## 2. Audience and outcome

Primary audience: <role, seniority, ecosystem>. B2B or B2C: <which, and what it changes>.
Primary outcome (SPACES letter): <support | product | acquisition and advocacy | content and contribution | engagement | success> - <measurable claim>. Secondary: <list, explicitly unranked below the primary>.
Community model: support-driven / product-development / education / founder-led.

## 3. Venue

Chosen: <class, then vendor> - highest surviving rung, at <standing presence per week> against <outcome bought>.
Deleted by constraint: <class> - reopens when <trigger>. <class> - reopens when <trigger>.
Rejected on the ratio: <class> because <reason>.
Mechanics verified on <date>: <pricing, history retention, permission model, export>.

## 4. Target member mix at 90 days

Founding cohort: <n> named people, <topic areas>, <time zones>.
Target: <n> contributors/advocates actively answering, <n> participants posting monthly.

## 5. Seeding plan

Founding invitations: <who, the ask, the time-box>.
Seeded content: <the 5-10 posts and who answers them>.
Opened surface: <the small set of rooms/categories and why each exists>.
Ritual: <what, when, who runs it>.
Published response-time commitment: <target>.

## 6. First 90 days

Weeks 1-2 (private cohort): <activities>.
Weeks 3-6 (invited beta): <activities, and the activity gate to pass before opening>.
Weeks 7-12 (public): <announcement channels, and what gets measured weekly>.

## 7. Thresholds and measurement

Day-30 leading indicators: <list>.
Day-90 pass thresholds: <table or list, with any B2B/B2C adjustment and its justification>.
Threshold basis: <which thresholds are published and which are baselines set for this plan, and what will recalibrate them>.
Who measures, how often, from which source.

## 8. Fold-back criteria

If <failing condition> at <date>, we <archive read-only | merge into <space> | convert to support channel>.
Decision owner: <name>.

## 9. Open risks

<risk> - <mitigation or accepted>.
```

## Worked example - launch verdict

> **Verdict:** Launch on 15 October, gated on the second answerer being confirmed.
> Gates: demand pass (31 setup questions arrived by email in 60 days, 9 of them duplicates; three users already answer each other in the repository's issues), owner pass (Priya, 6h/week committed through Q1, confirmed by her manager), purpose pass (SPACES: Support - "cut duplicate setup questions reaching the inbox by half within two quarters"), venue vacuum pass (the ecosystem's Discord has no channel for this problem domain and its moderators declined a dedicated one), seed supply weak (22 named invitees, but only one reliable answerer outside Priya - mitigation: recruit a second before opening).
>
> **Venue:** Owned async forum (self-hosted Discourse) - the highest rung left standing, at roughly an hour a day of batched moderation against durable indexed answers. Answers about setup and configuration stay valid for months, search traffic on error strings is a wanted acquisition channel, and per-instance pricing suits a growing free-tier audience. Deleted by constraint: real-time chat, because Priya cannot be present most days at 6h/week - reopens only if a second staffed owner joins and the primary outcome moves off Support. Forge-native discussions, because half the audience are operators without accounts on the forge - reopens if the operator segment stops being the majority.
>
> **Fold-back:** if fewer than 50% of posts come from non-staff at day 90, archive the forum read-only, redirect to the repository's discussions, and publish the top 20 answers as troubleshooting pages. Decision owner: Priya.

Why it works:

- Every gate cites evidence rather than intuition.
- The weak gate has a named mitigation and gates the launch date.
- The venue choice names the rejected options and the reasons.
- The exit is decided while it is still cheap to accept.

## Worked example - do-not-launch verdict

> **Verdict:** Do not launch. Gates: demand fail (support volume is 4 tickets/month, none repeating; no evidence users want to talk to each other), owner fail (no named owner; the plan assumed a DevRel hire in Q2), purpose weak ("build community" restated, no measurable claim), venue vacuum fail (the language's official Discord already hosts an active channel where two of our users post), seed supply pass (35 named customers).
>
> **Recommendation instead:** answer publicly in the ecosystem Discord under the company name for one quarter, convert the six most-asked questions into troubleshooting pages, and run monthly office hours. Re-decide when either repeat questions exceed 10/month or users start answering each other in the repository.

Why it works:

- The "no" is as specific as a "yes".
- The alternative serves the same outcome at a fraction of the cost.
- The re-decision trigger is an observable number rather than a date.

## Weak example - what to avoid

> We'll launch a Discord because that's where developers are. Channels: #general, #announcements, #help, #showcase, #jobs, #random, #frontend, #backend, #devops. We'll announce on launch day to the newsletter (8,000 subscribers) and aim for 1,000 members in the first quarter. Marketing will keep an eye on it.

Four defects:

1. The venue is picked by habit rather than by the standing presence it demands forever: a Discord is free to open and a standing job to keep alive, and nobody here has that job.
2. Nine empty rooms broadcast that nobody is there.
3. The whole audience is spent on a single announcement into an unseeded room.
4. "marketing will keep an eye on it" is the ownership gap that produces a ghost town.

The target is also a joins counter, not a health signal - 1,000 members with 20 weekly posters is a failure.
