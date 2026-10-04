# Alerting and Notification

Per-integration error aggregation, detection windows, and how to notify a partner without training them to ignore you.

## Contents

- Aggregation schema
- Status-code buckets
- Detection windows
- Threshold and cooldown mechanics
- Notification templates
- Anti-fatigue rules

## Aggregation schema

The minimum a per-integration aggregate has to carry, one row per identity per window:

| Field                        | Why it exists                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| Integration identity         | API key or app/client ID, tagged at ingestion - the aggregation is only as granular as this tag |
| Account                      | Which of your customers the integration was acting on; a fleet app needs both dimensions        |
| Window start and end         | Explicit, so a rate is interpretable rather than a floating number                              |
| Success count                | The denominator; an error count without it cannot produce a rate                                |
| Count per status-code bucket | 4xx, 5xx, 429 separately - never one blended error total                                        |
| Top error codes              | The machine-readable codes, ranked; this is what makes a notification actionable                |
| Deploy markers               | Your release timeline, overlaid, so a platform-caused spike is distinguishable                  |

Tag at ingestion rather than reconstructing later. A tag added after the fact leaves the preceding history unqueryable by integration, which is exactly the period any investigation wants.

## Status-code buckets

Three buckets, kept apart because each has a different owner and a different remediation:

- **4xx - the integrator's side.** Malformed payloads, missing fields, invalid auth, calls against deleted objects. Actionable by them, and the bucket where naming the top error codes does most of the work.
- **5xx - your side.** Never notify a partner about a 5xx spike without first checking it against your deploy timeline, and never phrase it as though it were theirs to fix.
- **429 - neither party's bug.** Rate-limit rejection is a capacity and quota conversation, not a defect. Isolating it prevents the most common misread of a blended rate: a partner scaling successfully looks identical to a partner whose code is broken. Quota design itself belongs to `samber/developer-platform-skills@api-rate-limit-policy`.

A fourth signal sits outside the buckets entirely: **volume drop to zero**. An integration that stopped calling produces no errors and appears nowhere in an error-rate view, so detect it separately by comparing call volume against the integration's own recent baseline.

## Detection windows

Two speeds catch two different failures, and a design with only one will miss half of them:

- **A short window** (minutes) catches a sudden break - a deploy on either side, a revoked credential, an endpoint gone.
- **A long window** (hours to a day) catches slow degradation - an error rate creeping from 1% to 6% over a week, which never trips a short-window threshold but is the more expensive failure because it runs unnoticed for longer.

This is the multiwindow, multi-burn-rate pattern from SRE alerting practice: pair a long window that confirms a problem is sustained with a shorter window that confirms budget is still actively being consumed before firing (sourced: Google SRE Workbook, "Alerting on SLOs"). The two-speed detection instinct transfers cleanly to per-integration alerting. The surrounding error-budget framing does not, because it was written for a team measuring its own dependence on somebody else's API.

Compare each integration against its own baseline rather than a platform-wide threshold. Traffic shapes differ by orders of magnitude between integrations, so any single global percentage is either noise for the small ones or blindness for the large ones.

## Threshold and cooldown mechanics

The concrete pattern worth copying comes from Salesforce's Agentforce health monitoring (sourced: Salesforce): notify immediately when an error-rate or latency threshold is crossed, then enforce a **cooldown period - 30 minutes by default there - before the same subject can alert again.**

Why the cooldown is the load-bearing part: without it, a single ongoing incident generates a continuous alert stream, and the recipient's only defence is to mute the channel - permanently, and for every future incident too. The cooldown converts "we alert on incidents" from a claim into something that survives contact with a real incident.

Design decisions to make explicitly:

- **Cooldown length.** Long enough that one incident produces one alert. Short enough that a second, distinct incident is not swallowed. Start from your typical incident duration, not from a borrowed number.
- **Recovery notification.** Send one when the rate returns to baseline. Without it, the partner has no signal to stop investigating, and the missing all-clear is itself a source of tickets.
- **Threshold ownership.** Decide whether partners can tune their own thresholds. Self-service tuning is the honest answer for a diverse partner base, since no single threshold fits every traffic shape - but it is a build, not a config flag.
- **Escalation path.** Where a repeated alert goes if nobody acts: your partner team, and after what interval. An alert with no escalation is a notification, not a control.

## Notification templates

**Digest (default rung).** A scheduled summary as the deliberate alternative to an instant per-failure alert is a real, named pattern in adjacent observability tooling - Elementary Data ships an "Incidents Digest" explicitly as a scheduled complement to real-time alerts (sourced: Elementary Data docs) - though no platform surveyed documents it scoped specifically to a per-integration or per-partner audience the way this rung is; that scoping is this skill's own application of the pattern. One scheduled message per integration:

```
Integration health - acme-connector - 30 Aug

  Calls          12,480   (-3% vs prior day)
  Failed           1,204   (9.6%)

  Integrator-side (4xx)  1,190
    invalid_shipping_address   842
    missing_customer_email     201
    object_not_found           147
  Platform-side (5xx)        14
  Rate-limited (429)           0

  Full request log: <link>
```

**Threshold alert (promoted rung).** One message, sent on crossing, then held for the cooldown:

```
Alert: acme-connector error rate at 41% (baseline 2%)
Started 14:05 UTC, ongoing. 3,912 failed calls across 84 installs.
Top error: invalid_shipping_address (94% of failures).
No platform release in this window - this pattern indicates a change on your side.
Request log filtered to these failures: <link>
Next alert for this integration no earlier than 14:35 UTC.
```

Two things make the second template work: it states what the platform already ruled out (its own deploys), and it names when the next alert can arrive, which is what stops the recipient from bracing for a flood.

**State-change alert (narrow rung).** Credentials revoked, integration disabled, subscription lapsed - one discrete event, sent immediately, no threshold and no cooldown, because there is nothing to repeat.

## Anti-fatigue rules

- One alert per incident, not per failure. If the design cannot express that, it is not ready to send.
- Never alert on a 5xx spike before checking your own deploy timeline.
- Every alert names the top error codes and links directly into the filtered log. An alert that only says "errors are up" costs the recipient a search and buys them nothing.
- Send a recovery message. Silence is not an all-clear.
- Track the share of alerts partners act on and treat a sustained decline as the design failing, not the partners. Widen the threshold or lengthen the cooldown before adding another channel.
- Never route the digest and the threshold alert to the same place at the same cadence. The point of two rungs is that they interrupt differently.
