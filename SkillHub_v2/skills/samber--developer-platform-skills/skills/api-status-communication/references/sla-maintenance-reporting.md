# SLA/SLO public reporting and maintenance notices

Detail for steps 6 and 7 of the workflow.

## SLI / SLO / SLA in public material

| Term | What it is                                                             | Public role                                                                   |
| ---- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| SLI  | The measured metric (e.g. response time, error rate)                   | The raw material - measured by your observability stack, not by this practice |
| SLO  | The internal target (e.g. 99.9% of requests under a latency bound)     | Publish only if you will report against it honestly                           |
| SLA  | The contractual, customer-facing commitment with consequences attached | The number the public page reports on                                         |

Keep the vocabulary straight in everything published: presenting an internal aspiration as if it carried contractual weight - or a contractual number you don't actually measure - is how disputes start.

## SLA page vs status page

A public SLA/uptime page and a status page are distinct artifacts answering distinct questions:

- **SLA page**: historical uptime percentages per component against commitments - "are you meeting your number". Directly checkable by a prospect or a procurement reviewer.
- **Status page**: discrete current incidents and manually-or-automatically set component states - "what is happening right now". It can cover components with no formal SLA at all (third-party dependencies, databases).

A mature reporting practice offers both, cross-linked.

## Edge cases to define before publishing any number

Each of these is a documented dispute source; define them in writing first:

- **Slow-but-responding requests**: set an explicit maximum acceptable response-time threshold above which a response counts as downtime - otherwise "downtime" silently excludes real user-facing pain.
- **Partial outages**: state whether the SLA is evaluated service-wide or per affected component. This is the same breadth axis the status page models; the two must agree.
- **Planned maintenance**: excluded from downtime arithmetic only when adequate notice was given (see notice scaling below) - write the notice condition into the SLA text itself.
- **Monitoring calibration**: probing too sensitively overcounts downtime (every 500ms blip flagged); probing too coarsely (long intervals, multi-failure thresholds) undercounts it. Either miscalibration corrupts the public number regardless of the reporting around it.

## Percentage to minutes

Translate targets into stakes a non-engineer feels - publish the minutes alongside the percentage (values are arithmetic on a 30-day month / 365-day year):

| Target | Allowed downtime / month | Allowed downtime / year |
| ------ | ------------------------ | ----------------------- |
| 99%    | ~7.2 hours               | ~3.7 days               |
| 99.9%  | ~43 minutes              | ~8.8 hours              |
| 99.95% | ~22 minutes              | ~4.4 hours              |
| 99.99% | ~4.3 minutes             | ~53 minutes             |

Where an error-budget model is in use internally, a visible burn-down communicates urgency for deployment and prioritization decisions in a way the percentage alone doesn't.

Publish incident history beside the headline figure. Degraded Performance conventionally counts as 0% downtime and partial outages may be weighted at a fraction of their duration - so an excellent-looking percentage can mask real incidents, and the honest page lets the reader check the number against the incident list behind it.

## Maintenance-notice scaling

Notice scales with impact and audience - there is no single correct number:

| Change                                  | Notice                                                                                   | Reminders                   |
| --------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------- |
| Minor, low-impact work                  | ~24 hours minimum                                                                        | none needed                 |
| Major changes                           | weeks                                                                                    | yes, as the date approaches |
| Anything affecting enterprise customers | a week or more, even when self-serve users would get same-day                            | yes                         |
| Contractual floor                       | whatever the contract says - a 5-business-day minimum is a documented real-world example | per contract                |

This horizon (24 hours to ~2 weeks) is this skill's; the 6-12-month deprecation/breaking-change runway belongs to `samber/developer-platform-skills@api-versioning-policy`. They are different communications - never fold a breaking change into a maintenance notice.

## Maintenance notice content checklist

- Exact start and end times with an explicit time zone - ambiguous timing is the single most common cause of maintenance confusion.
- Scheduled against the affected user base's actual low-traffic hours, not the provider's office hours.
- Precise scope: which endpoints/features are affected, and which remain available.
- What consumers should expect and do (errors vs read-only vs full outage; whether to pause jobs or retry).
- Delivered via status page plus at least one push channel - never the page alone.
- Start and completion confirmations posted, even for short windows.

Good communication does not make maintenance disappear from customers' trust ledger just because the SLA arithmetic excludes it - a poorly communicated but SLA-compliant window still costs trust.

## Worked examples

Both notices are composed as illustrations, not quoted from a real vendor announcement. Their shape matches Atlassian's own guide to scheduled-maintenance messaging, which documents real vendor examples (DigitalOcean, Heroku, ToutApp) using the same elements: exact times in a neutral time zone, explicit affected-versus-unaffected scope, and a stated consumer action. The start/completion confirmation step in the good example below goes beyond Atlassian's documented pattern.

**Bad notice:**

> The API will be down for maintenance this Saturday night.

No date, no times, no time zone, no scope ("the API" - all of it?), no expected behavior, no channel redundancy, "night" in whose timezone?

**Good notice (sent 10 days ahead, re-sent 24 hours ahead):**

> **Scheduled maintenance: database migration affecting write endpoints**
> On Saturday 2026-09-12, from 02:00 to 04:00 UTC, POST/PUT/DELETE requests to the REST API will return 503 with a Retry-After header while we migrate our primary database. GET requests, the dashboard, and webhook deliveries are unaffected. We chose this window as the lowest-traffic period across our user base. We will post a confirmation here when the window starts and when it completes. Follow this page or subscribe to updates to be notified.

Scoped, timed, zoned, behavior-specified, redundantly delivered, with progress confirmations promised.
