# Program charter, edition log and scorecard

Contents: charter template · filled example · edition log · healthy scorecard · failing scorecard read line by line.

## Charter template

```markdown
# <Group name>

**Room:** who attends - technology, seniority, work-time or own-time
**Host model:** independent vendor-neutral | vendor-backed volunteer chapter | company-staffed series (name the company)
**Purpose:** the one outcome that justifies the effort in a year - exactly one, named in SPACES terms if a company hosts
**Format:** default format, plus the no-speaker fallback format
**Rhythm:** fixed slot (e.g. second Tuesday, 19:00), cadence, months off
**Program decisions:** who selects talks, and on what test
**Organizers:** names, employers, area owned by each
**Venue:** current host, booked through <date>
**Money:** what is spent per edition, who pays, who signs
**We don't:** the explicit refusals (bought slots, attendee lists, recruiter pitches from stage…)
**Accounts:** listing, mailing list, socials - who has access (at least two people each)
```

## Filled example

```markdown
# Nantes Go Meetup

**Room:** backend engineers using Go in production, mid to senior, attending after work
**Host model:** independent vendor-neutral; venue rotates between three local companies
**Purpose:** a local Go hiring and hallway network - people who can call each other about production problems
**Format:** anchor talk (25 min) plus two lightning slots; fallback is a demo night
**Rhythm:** second Tuesday, 19:00. Ten editions a year, off in August and December
**Program decisions:** two organizers review title, takeaway and slides; the test is "could a non-vendor give this talk?"
**Organizers:** Camille (program, employer A), Théo (venue and sponsors, employer B), Sofia (comms and door, employer C)
**Venue:** employer B through November
**Money:** ~€250 per edition, food only, paid by the venue host of the month
**We don't:** sell speaking slots, share the attendee list, allow recruiting from the stage
**Accounts:** listing and socials shared between Camille and Sofia; mailing list on a group address
```

## Edition log

One row per edition, filled the evening it happens. The trend is the product; a single row is noise.

| #   | Date   | Format             | Speakers           | RSVP | Door | Repeat % | New faces | Notes                                                               |
| --- | ------ | ------------------ | ------------------ | ---- | ---- | -------- | --------- | ------------------------------------------------------------------- |
| 14  | 11 Mar | Anchor + lightning | Rossi, 2 lightning | 62   | 41   | 46%      | 9         | Both lightning speakers were first-timers from the room             |
| 15  | 8 Apr  | Two-talk           | Chen, Diallo       | 58   | 38   | 51%      | 6         | Projector adapter missing; buy a kit                                |
| 16  | 13 May | Demo night         | 6 attendees        | 44   | 35   | 63%      | 3         | Fewest new faces in six months - promote outside the usual channels |

## Healthy scorecard

| Line                               | Value        | Verdict                                        |
| ---------------------------------- | ------------ | ---------------------------------------------- |
| Gap since last edition             | 33 days      | Pass                                           |
| Editions with confirmed speakers   | 2            | Pass                                           |
| Door attendance trend (3 editions) | 41 → 38 → 35 | Watch - flat-to-down, act before it is a trend |
| Repeat attendance                  | 63%          | Pass                                           |
| New faces                          | 3            | Watch - reach is narrowing                     |
| Organizers / employers             | 3 / 3        | Pass                                           |
| Sponsor stage time                 | 0-10 min     | Pass                                           |

Read: the group is healthy internally and closing in on itself. The fix is outward promotion - neighboring groups, universities, a topic outside the core clique - not another format change.

## Failing scorecard

| Line                             | Value               | Verdict                                              |
| -------------------------------- | ------------------- | ---------------------------------------------------- |
| Gap since last edition           | 118 days            | Fail - past the 90-day line; the program has stopped |
| Editions with confirmed speakers | 0                   | Fail - every edition starts from zero                |
| Door attendance trend            | 45 → 26 → 12        | Fail                                                 |
| Repeat attendance                | 18%                 | Fail - a churn funnel, not a community               |
| Organizers / employers           | 1 / 1               | Fail - one job change from dead                      |
| Sponsor stage time               | 30 min product demo | Fail - explains the repeat rate                      |

Read: do not schedule a bigger event to fix this. In order:

1. Recruit a second organizer from the remaining regulars.
2. Fix a date and book the room before finding a speaker.
3. Pick a fallback format that needs no external speaker.
4. Cap sponsor time at 15 minutes and say so publicly.
5. Restart at a cadence the pair can actually hold.
