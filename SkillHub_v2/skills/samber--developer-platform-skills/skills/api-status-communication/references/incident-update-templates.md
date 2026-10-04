# Incident update templates

Templates and examples for step 4 of the workflow. Every update below is composed as an illustration, not quoted from a published incident - copy the shape and the discipline, never the specifics. All timestamps are UTC with the zone stated; copy that habit too.

The shape is observed practice, not only prescription: major cloud providers post each update with:

- A zoned timestamp.
- An explicit workaround line (including "none at this time" when there is none).
- A named datetime for the next update.

They drop the next-update commitment only on the final mitigated/resolved post. Hold that discipline even where a large provider you admire settles for "we will post updates as we learn more" - an open-ended promise is the one this practice replaces.

## Severity to component-state mapping

Internal incident-response vocabularies commonly grade severity SEV1-4. That scale is internal - it never surfaces publicly - but responders need a pre-agreed mapping from it to the public component states, decided once in writing, not debated mid-incident. Status-page platform OpenStatus publishes a severity matrix template in this same shape: a Critical tier maps to a "Major Outage" public label with a 15-minute response target, High to "Partial Outage" at 30 minutes, Medium to "Degraded Performance" at 2 hours, and Low to a minor-issue label at one business day, with classification meant to be deterministic so every engineer reaches the same row given the same inputs. A workable default mapping in the same shape (adapt the internal column to your own scale):

| Internal severity | Typical meaning (internal)                  | Public component state | First public update                           |
| ----------------- | ------------------------------------------- | ---------------------- | --------------------------------------------- |
| SEV1              | Service down for all users                  | Major Outage           | Immediately, auto-opened from the alert       |
| SEV2              | Major feature degraded, many users affected | Partial Outage         | Immediately, auto-opened from the alert       |
| SEV3              | Minor issue, some users affected            | Degraded Performance   | Within the response window your pipeline sets |
| SEV4              | Cosmetic, no functional impact              | No public incident     | None - fix note in changelog if relevant      |

The internal meanings above come from a published internal-incident severity table. Two named platforms confirm the same severity-versus-public-state split in practice: incident.io separates "severity" (an internal, subjective triage field) from "impact" (the separate, public-facing field that actually drives the status page color), and Cloudflare's incident management policy ties its internal P0/P1 priority classes to Status Page updates without exposing the priority label itself. Remember the axis from step 1: the public state encodes breadth of impact, so a SEV2 that is "broken for everyone but only in one region" is still Partial Outage, scoped to that region.

## Update skeleton per lifecycle status

Every update carries:

- The incident title.
- The current lifecycle status.
- The affected components and their states.
- A timestamped body.
- The time of the next update.

The body follows one skeleton throughout:

1. Acknowledge the impact (what consumers are experiencing, in their terms).
2. State what is known and confirmed - never what is suspected.
3. Give a workaround if one exists.
4. Set the expectation: what happens next, and when the next update lands.

### Investigating

> **Elevated error rates on the REST API** - Investigating
> 14:02 UTC - We are seeing elevated 5xx error rates on the REST API and are investigating. Requests to the dashboard and webhooks are unaffected. Next update by 14:20 UTC.

Posted automatically from the monitoring alert (step 2); a human enriches it within minutes. It commits to a next-update time even though nothing is diagnosed yet.

### Identified

> 14:17 UTC - We have identified the cause as a failing database node affecting API requests in eu-west. Requests in other regions are succeeding normally. A workaround is to retry failed requests, which are routed to healthy nodes with increasing probability as we drain traffic. Next update by 14:45 UTC.

States the confirmed cause and the scoped breadth, gives the workaround, keeps the cadence promise.

### Monitoring

> 14:41 UTC - We have failed over to a healthy database node and error rates have returned to normal levels as of 14:38 UTC. We are monitoring before declaring the incident resolved. Next update by 15:15 UTC.

The fix is deployed but the incident stays open - closing on the first green minute and reopening is worse for trust than a visible monitoring period.

### Resolved

> 15:10 UTC - This incident is resolved. Between 13:54 and 14:38 UTC, approximately 12% of REST API requests in eu-west failed with 5xx errors. We apologize for the disruption. A summary of cause and prevention will be posted here within 3 business days.

Quantifies the impact window and scope, owns it, and - per the postmortem ladder in step 5 - commits to the follow-up in the same message.

## Good/bad update pairs

**Bad - speculation, jargon, blame, no cadence:**

> We think this might be an issue with our cloud provider's networking. The k8s ingress pods are being rescheduled. Will update when we know more.

Three violations:

- Speculation stated as information.
- Internal jargon the reader can't act on.
- Blame pre-assigned to an upstream vendor.
- An open-ended "when we know more" instead of a next-update time.

**Good - same moment, same knowledge:**

> 09:12 UTC - We are investigating connection timeouts affecting roughly a third of API requests. We have not yet confirmed the cause. Requests that succeed are processing normally, so retrying is a viable workaround. Next update by 09:40 UTC.

Says less that is unconfirmed and more that is useful. Note it admits "not yet confirmed" outright - precise includes being precise about uncertainty.

**Bad - the silent-degraded non-update:**

Latency has doubled for an hour; the page shows green and no incident exists "because nothing is down."

**Good:**

> **Increased API latency** - Investigating
> 11:05 UTC - API response times are roughly twice their normal levels for all consumers. Requests are completing successfully. We are investigating the cause. Next update by 11:35 UTC.

Degraded Performance exists as a state precisely so this gets posted; a component that is slow for everyone is an incident even though uptime arithmetic may count it as up.

## The five practices, expanded

Atlassian's five incident-communication practices, as a review checklist for every update before it posts:

1. **Early** - is this going out now, or is someone waiting for a fuller picture? An update saying "still working on it, nothing new" beats silence; silence makes readers expect the worst.
2. **Often** - does this update name the time of the next one, and was the previous promise kept?
3. **Precise** - is every claim in it confirmed? Move suspicions to internal channels.
4. **Consistent** - do the page, social posts, and emails currently say the same thing? A reader mid-incident experiences any divergence as dishonesty.
5. **Owned, with empathy** - does it acknowledge what consumers are experiencing, and does it avoid deflecting to an upstream vendor even when the root cause is genuinely upstream? The customer's contract is with you.

## Titling

Title in plain language stating the nature of the problem and its scope: "Elevated error rates on the REST API in eu-west", "Webhook deliveries delayed". Internal template names, codenames, and severity labels are team-organization artifacts and never surface publicly - the public surface is the title and the update bodies.
