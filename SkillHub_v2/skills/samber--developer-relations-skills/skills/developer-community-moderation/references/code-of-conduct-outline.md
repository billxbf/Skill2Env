# Code of conduct outline

Contents: base-document versions · document skeleton · scope wording · enforcement ladder · reporting section · worked example pair.

## Which base document, and which version

The Contributor Covenant is the most adopted base (40,000+ projects per opensource.guide); the Django code of conduct is the other common one. The Covenant's two live versions do not share section names, so state which one you are adapting.

| 2.1                                                    | 3.0                                                 |
| ------------------------------------------------------ | --------------------------------------------------- |
| Our Pledge                                             | Our Pledge                                          |
| Our Standards (expected + unacceptable in one section) | Encouraged Behaviors / Restricted Behaviors (split) |
| Enforcement Responsibilities                           | folded into the moderator role                      |
| Scope                                                  | Scope                                               |
| Enforcement                                            | Reporting an Issue                                  |
| Enforcement Guidelines                                 | Addressing and Repairing Harm                       |
| -                                                      | Other Restrictions                                  |

"Community leaders" (2.1) becomes "Community Moderators" (3.0); both versions invite you to rename the role and rewrite the enforcement section. Prefer 3.0 for a new document: it drops 2.1's "a public apology may be requested" line, which a committee should never act on.

## Document skeleton

Write these six sections, in this order. The order matters: a reader who stops after three sections must already know what is expected, who enforces it, and where it applies.

1. **Pledge** - what experience the community commits to, and for whom. Two to four sentences.
2. **Standards** - expected behaviour and unacceptable behaviour, both as concrete examples drawn from what actually happens in this community. Generic lists ("be respectful") give a moderator nothing to point at. Do not include "assume good intent": it moves every discussion onto what someone meant rather than what happened, and anyone acting in bad faith only has to say "I meant well" to reset the conversation (Frame Shift Consulting, "Why 'Assume Good Intent' Backfires", 2022).
3. **Enforcement responsibilities** - who may remove content, mute, suspend, and ban; and what they owe in return (consistency, privacy, explanation).
4. **Scope** - surfaces, people, and the off-platform stance (below).
5. **Reporting** - channels, privacy promise, response target, no-retaliation rule.
6. **Enforcement guidelines** - the ladder, with each rung's trigger and consequence.

Base documents worth adapting instead of writing from scratch: the Contributor Covenant (this skeleton is its structure) and the Django code of conduct. Adapting the text is expected - rewrite the enforcement section so it describes the procedure the community will really follow, and rename "community leaders" to the role title that actually exists here.

## Scope wording

The scope clause has to answer three questions explicitly:

- **Which surfaces**: name them one by one - repository and issue tracker, pull request reviews, chat server, forum, mailing list, project social accounts, in-person and virtual events, private messages between members that start in a community space.
- **Which people**: members, contributors, maintainers, employees of a sponsoring company, sponsors, speakers, event staff and vendors.
- **Off-platform conduct**: pick one stance and write it down. Either (a) it violates the code only when the person is representing the community, or (b) it is in scope when it credibly bears on member safety inside the community. Leaving this blank guarantees an argument during the first hard case.

When several bodies exist (a project, a foundation, an events arm), write the jurisdiction split too: which body handles which kind of report, and who decides when the answer is unclear.

## Enforcement ladder

Publish the trigger and the consequence for each rung. A consequence list without triggers reads as arbitrary; triggers without consequences give reporters nothing to expect.

| Rung                    | Trigger                                                   | Consequence                                                                                                                                                                                                  |
| ----------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1. Correction           | Unprofessional or unwelcome behaviour, first occurrence   | Private written notice naming the behaviour and the expected change                                                                                                                                          |
| 2. Warning              | A violation, single incident or a pattern                 | Formal warning with stated consequences; no unsolicited contact with the affected parties for a stated period                                                                                                |
| 3. Temporary suspension | Serious violation, or sustained behaviour after a warning | Time-boxed removal from interaction and public communication - state the length (Django's published bands: 30-90 days short, 90+ days extended with conditions on return - one project's choice, not a norm) |
| 4. Permanent ban        | Pattern of violation, sustained harassment, or aggression | Permanent removal from public interaction in the community                                                                                                                                                   |

Non-ladder outcomes to keep available, because most reports do not end in a ban. Listed here in the order SKILL.md ranks them (recurrence prevented per unit of moderator hours and relationship cost) - that section carries the axes, the ties and the condition that promotes mentoring; do not re-derive a second order here:

- A systemic fix - a rule change, a template change, a channel change - when the incident's root cause is structural.
- Removal of the harmful content, with or without a sanction on the author.
- Removal from a leadership or maintainer role while keeping membership.
- A public statement of what the response would have been, when the account is gone or unidentifiable.
- Education or mentoring for a well-meaning repeat offender.

Outside that ranking: "no violation found" is a finding, not an outcome to choose - say so plainly to both parties whenever it is true.

The ranking governs only cases where a moderator has a real choice. Where the breach is serious, the ladder above is a gate and severity picks the rung.

Django's manual lists facilitated communication between the parties, with everyone's consent, as an available outcome. Aurora and Gardiner argue against ever mediating, because it reframes a safety problem as a personal disagreement and lets the team avoid deciding. This skill follows Django's model: facilitated communication is permitted, but only as an add-on after a decision has been made, and only with everyone's informed consent - never as a substitute for a decision, and never the response offered to a harmed person.

Rules that hold across every rung:

- Send corrections privately, but do not let the community conclude that nothing happened - people who witnessed the violation should learn that it was answered, and aggregate statistics go out on a cadence.
- State the end date of any time-boxed sanction and schedule the restoration.
- Move up the ladder on repeat offences, which only works if the case record exists.
- Choose the smallest rung that protects the community - smallest _sufficient_, judged against the breach and never against what it would cost the team to enforce: a ladder that always ends in a ban suppresses reporting, one that never gets past a warning deters nobody.

## Reporting section

Include all five, or the section is decorative:

1. A private channel that is not a public issue tracker (an alias such as `conduct@…` is the common form), with the people behind the alias listed by name - reporters who can see who reads the mail are likelier to send it.
2. A second path for a report **about** the primary recipient - a named alternate, a board, or a fiscal host.
3. Whether anonymous reports are accepted and how to file one.
4. The acknowledgment target ("within one business day", "within three business days") - a number the team can actually hold.
5. A no-retaliation statement, saying that retaliation against a good-faith reporter is itself a violation.

## Worked example pair

**Weak (what most projects ship):**

> Be respectful. Harassment will not be tolerated. Violations may result in a ban. Contact the maintainers if you have a problem.

Four defects: no scope, so nobody knows whether it covers the Discord; no named channel, so "the maintainers" means the person you are reporting; no ladder, so every case is decided from scratch; no timeline, so a reporter has no idea whether silence means "in progress" or "ignored".

**Workable (same length budget, filled in):**

> **Scope.** This code applies to the repository, the issue tracker, the community chat, project social accounts, and any event the project runs. It covers members, maintainers, and sponsor staff. Conduct outside these spaces is in scope when it credibly affects a member's safety inside them.
>
> **Reporting.** Email `conduct@example.org`, which reaches the three-person response team. To report a member of that team, email `board@example.org` instead. Anonymous reports are accepted through the form at `example.org/report`. We acknowledge every report within one business day and never disclose a reporter's identity to the person reported. Retaliation against someone who reports in good faith is itself a violation.
>
> **Consequences.** Correction (private notice) → warning (with a no-contact period) → temporary suspension (30-90 days) → permanent ban. We publish aggregate statistics twice a year and never discuss individual cases publicly.

The second version is enforceable because each sentence names a person, a place, or a number.
