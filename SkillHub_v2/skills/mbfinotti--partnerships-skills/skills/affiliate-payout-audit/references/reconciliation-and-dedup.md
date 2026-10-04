# Reconciliation and Dedup

How to pull comparable data, match it across systems, and pay each conversion exactly once.

## Export pull and date basis

- Pull the platform/network conversion export and the source-of-truth extract for the same declared period, before touching any number.
- Exports commonly offer more than one date basis - transaction date, validation date, amendment date (Awin exposes all three). Picking the wrong one silently shifts lines between runs.
- Default to transaction date for reconciling to orders/billing; use validation date when reconciling what became payable this period. Never mix bases inside one run.
- Late-submitted conversions may be re-dated by the platform to their submission date (impact.com documents this), putting them on a new locking/payment schedule. Treat any line whose event date differs from its order date as a cutoff-risk line.
- Paginate fully on both sides. A partial page reads as "missing in the other system" and produces false exceptions.
- Exclude test-mode and sandbox transactions explicitly; verify test data cannot leak into the live export before comparing counts.

## Matching keys

- Match on stable identifiers only: order ID, transaction ID, customer ID, subscription ID. Never match on partner or customer display names.
- Apply the 0/1/many rule: zero matches → exception queue; exactly one → resolved; more than one → stop and require explicit human disambiguation, never auto-pick.
- Declare the join key between platform record and internal record before matching - and keep it for every future run, so exceptions are comparable run over run.

## The comparability gate

Before comparing or summing any two numeric sources, confirm they share every one of:

- Event definition (order placed vs order paid vs subscription invoice settled).
- Date basis and time window.
- Timezone.
- Currency.
- Counting method (per order vs per line item vs per customer).
- Deduplication identity (which key collapses duplicates, and whether blanks collapse together).

If any dimension differs: normalize first, or present the numbers side by side with their definitions and refuse to compute a total. Two sources claiming the same conversion are one conversion with two claimants - never sum across claimant sources; de-dupe against the declared source of truth.

Expect and budget for a residual gap: report claimed vs verified vs delta with an explanation, rather than forcing a false reconciliation to zero.

## The exception queue

Every one-sided record goes into a queue with a direction and a default action:

| Direction                          | Meaning                                                               | Default action                                                             |
| ---------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| In platform, not in billing/orders | Possible over-credit - a commission with no confirmed money behind it | Hold the line; investigate before approving                                |
| In billing/orders, not in platform | Untracked sale - the partner likely earned and wasn't credited        | Expect an inbound dispute; decide credit policy explicitly and document it |

- Age each open exception in days; escalate by amount and by age; a growing exception count run over run is a process defect, not noise.
- Close the run only when every exception is resolved or explicitly accepted and listed in the report.

## Period cutoff and timezone

- Use half-open windows: `period_start <= t < period_end`. Closed windows double-count the boundary instant.
- Normalize every timestamp to the single timezone declared in run scope before applying the cutoff. Platform, billing system, and program office frequently disagree on the clock.
- Diff this run's key set against the prior run's key set. Any overlap is a conversion about to be paid twice - remove it before totaling.
- Watch conversion lag: click date, conversion date, and platform post date can span a boundary; the declared date basis decides which run owns the line.

## Dedup key discipline

- One deterministic dedup key per conversion; pay each key at most once per commission event.
- Quarantine empty or malformed keys instead of letting them collide: analytics tools that dedupe on transaction ID treat all blanks as one record, collapsing many conversions into one (a documented GA4 behavior) - or one conversion into many payable lines elsewhere.
- Where the platform holds multiple records for one order ID, identify which record the platform treats as payable (impact.com applies updates to the newest action for a shared order ID, and its reattribution flow leaves only the new pending action payable). Verify exactly one payable record survives per key.

## Dual tracking collapse

- If both a platform pixel and an in-house tracker (or web analytics) record conversions, declare one canonical source per conversion type and reconcile the other against it - never union the two lists.
- The fix for persistent dual-tracking duplicates is structural: a shared idempotency key across both trackers. Flag its absence as a finding even when this run's duplicates were caught manually.
