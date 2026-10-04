# Platform controls and volume defenses

Contents: venue classes · earned trust · rate limits · content actions · volume attacks · moderator roster.

## Match the control to the venue class

Write the playbook against the class, then note the current feature names for the venue actually in use - vendors rename these controls often, so verify on the platform's own moderation documentation before publishing a runbook that depends on them.

| Venue class                                                    | Controls it gives a moderator                                                                                                                                    | What it does not give                                                                              |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Async forum (self-hosted or hosted)                            | Earned trust levels, member flagging with auto-hide thresholds, post edit/hide history, category permissions                                                     | Instant reach - a bad post can sit for hours                                                       |
| Forge-native (issues, pull requests, discussions)              | Temporary interaction limits, per-user open-PR caps, comment hiding with a stated reason, comment editing for redaction, conversation locking, blocking          | Chat-speed presence, and any control over off-forge spillover                                      |
| Real-time chat                                                 | Keyword and spam filters with automatic actions (block message, alert a private channel, time out the member), entry gates, role-based channel access, slow mode | A durable public record - deleted messages are gone unless archived                                |
| Rented public space (subreddit, Q&A site, ecosystem-wide chat) | Reporting to the host, muting a thread, moving the conversation to an owned surface                                                                              | Any authority of your own: the host's rules outrank your code of conduct and you cannot ban anyone |

## Earned trust beats appointed authority

Mature forum software promotes members automatically as they read, post, and receive likes, and hands each level more moderation weight. A flag from a high-trust member can hide a new member's post immediately, while flags from the top level take effect at once. The generalizable pattern: let the membership carry the first moderation layer and have humans review after the fact, instead of gating every post through a small team that cannot scale.

Mirror it manually where the platform has no trust system: a "regular" role granted after a visible track record, with the power to flag and to move threads but not to ban.

## Rate limits are the answer to floods

Individual bans answer individual behaviour. A raid, a brigading wave, or a spam campaign is a volume problem, and banning accounts one at a time just burns the team's hours.

Forge-native limits worth pre-configuring so they can be switched on in seconds:

- Interaction limits in three tiers - new accounts (under 24 hours old with no prior contribution), non-contributors, or non-collaborators - applied for a fixed window (24 hours, 3 days, 1 week, 1 month, 6 months) at repository, account, or organization level. They block commenting, opening issues and pull requests, reactions, and edits.
- A cap on concurrent open pull requests from users without write access, with a bypass list for trusted contributors.

Chat equivalents: slow mode, entry gates (rules acceptance, account-age or email verification, onboarding questions), and automatic filters. Entry gates cost real join conversion - decide that trade deliberately rather than discovering it after a raid.

## Content actions, in order of reversibility

Deliberately not ranked by efficiency: these four are not four ways to reach one outcome, they are four different situations. A leaked API key needs a redaction and a thread nobody can stop needs a lock, and no ratio converts one into the other. Reversibility is the axis that actually decides between them, so it is the only order given here.

1. **Hide/minimize with a stated reason** - the audit trail stays, the reader sees that a moderator acted and why.
2. **Edit to redact** - for leaked secrets or personal data; replace the content with a redaction marker and add a note saying a moderator edited it.
3. **Lock the conversation** - when the thread, not a person, is the problem.
4. **Delete** - last resort. It erases the evidence and the community's ability to check the moderator, so record the content in the case file first.

## Volume attacks of low-quality submissions

Automated and AI-assisted submissions have made "sincere but worthless" a category of its own. The behaviour ladder handles it badly: there is usually no malice to escalate against, and banning individuals does nothing to the inflow rate.

What is measured, with sources:

- **curl** (Daniel Stenberg, "Death by a thousand slops", 2025-07): about 20% of the year's bug-bounty submissions were AI-generated junk, roughly two per week; each report cost the seven-person security team 30 minutes to 3 hours and pulled in three to four people. In one early-July sample only 5% of submissions were genuine. On 2026-01-31 curl ended the bounty entirely - the confirmed-vulnerability rate had fallen from historically above 15% to below 5%, and Stenberg described the inflow as "effectively being DDoSed".
- **Node.js** now requires a HackerOne Signal score of 1.0 to submit, after one month brought "over 30 reports" against a usual 6-7.
- **OpenSSF**'s working-group issue on the problem records that there is "no reliable technical indicator for AI-generated content" - detection runs on maintainer intuition. So gate volume; do not try to detect authorship.

Countermeasures that fit the shape, ranked by inflow removed per hour of maintainer time:

- efficiency: reputation or contribution gate > review-effort cap > raising the submission cost > disclosure rule
- effort: review-effort cap == disclosure rule (one paragraph each, in the template and the policy) > reputation gate (pick a floor, change one setting) > raising the submission cost (redesigning what a submission must contain, and removing a reward is a decision with its own politics)
- value: reputation gate (cuts inflow itself - Node.js's Signal-score floor pulled "over 30 reports" back toward the usual 6-7) > raising the submission cost (removes the incentive being farmed, which is what curl finally did) > review-effort cap (protects reviewers without lowering the rate) > disclosure rule (changes nothing alone; it gives the other three a line to point at)
- compliance cost: review-effort cap == reputation gate (platform-native, and neither makes a claim about any person) > disclosure rule (once published it must be enforced evenly, including against people you like) > raising the submission cost (a refundable fee touches payments, and withdrawing a bounty breaks a promise made to existing participants)

The effort tie is real: both the cap and the disclosure rule are single paragraphs written once. The compliance tie holds because neither the cap nor the gate stores anything new or accuses anyone of anything.

1. **Gate on reputation or contribution history** rather than on suspected authorship - a platform reputation score, an account-age floor, prior-contributor requirements.
2. **Cap review effort per submission** and close on a standard template when the cap is hit.
3. **Raise the submission cost** where an incentive is being farmed: required reproduction steps, proof-of-concept artifacts, a refundable fee - or removing the monetary reward, which is what curl ultimately did.
4. **Publish a disclosure rule for AI-assisted submissions** and enforce it on the submission's content, not on suspicion - accusing a member of using a language model without proof creates its own incident.

Efficiency starves option 3: it is the highest-value entry and the one that costs the most political capital, because withdrawing a reward means telling a real audience their reward is gone. Promote it once the gate is in place and the valid share is still falling - curl's own sequence. Re-rank all four against the community's own shape: a project with no bounty has nothing to withdraw and should delete option 3 rather than carry it, and a forge with no reputation signal has no option 1.

Measurement is not a countermeasure and does not compete with them: track submissions per week and valid share regardless of which you pick, because the rate is the only thing that says whether any of it worked.

## Moderator roster

- Recruit from observed behaviour in the room - the people already answering newcomers and de-escalating - not from seniority or job title.
- Cover the hours and the languages the community actually posts in; a single-timezone roster means unmoderated hours.
- Grant powers in tiers: remove a post → time out → temporary ban → permanent ban, with the top rung reserved for the response team.
- Give each moderator a written agreement: powers, confidentiality, recusal duty, what to escalate instead of deciding alone, and how to step down without drama.
- Run a private moderator channel for calibration - decisions made alone drift apart quickly - and rotate duty with a per-person weekly cap. Burnout, taking abuse personally, and isolation are the standard failure modes, and rotation plus visible team support is the standard mitigation.
- For a body that decides sanctions, borrow the structure large foundations use: a few elected members plus alternates, fixed terms, a cap on how many seats one employer may hold, and eligibility rules (no recent violation of their own). Practitioner sizing guidance is 3-6 members, chosen so the body still functions with about a third of it unavailable - a two-person team is one holiday away from having no quorum.
- List the deciding members by name wherever reports are solicited. Many people doubt a report will be taken seriously, and knowing who will read it is what changes their mind.
- Rehearse. Run the team through practice cases on a cadence - yearly, when someone joins, or before a large event - and use real published incident write-ups rather than invented ones where you can. Deciding fast under pressure is a trained reflex.
