# Worked Example: TIME Scoring Pass with Renewal Overlay

TIME (Gartner) scores each tool on two axes: technical fit and functional fit. Each combination assigns one of four verdicts:

- High technical / high functional: **Invest**
- High technical / low functional: **Tolerate**
- Low technical / high functional: **Migrate**
- Low technical / low functional: **Eliminate**

Gartner's own authors stress the goal is maximizing value, not reducing spend. Tolerate verdicts decay: they need re-scoring each cycle, never a permanent pass.

The High/Low binary below is the fastest usable version. Ardoq's public TIME implementation operationalizes it with more granularity for a reader who wants it: score business value as the sum of strategic fit, features and usability, functional fit and criticality (each 0-3), and technical fit the same way; a tool scoring 0-3 on both axes gets an automatic Eliminate. Use the finer scale only when the binary produces ties that block a real decision - it adds arithmetic, not new judgment.

The example below is illustrative - generic tool categories, invented but realistic scores. The scoring logic and overlay mechanics are the transferable part; the verdicts are not benchmarks.

## The stack slice (B2B sales-led, mid-market)

A 10-tool slice of a larger inventory, after the overlap map flagged two duplicate functions (enrichment, scheduling).

| Tool                           | Function                 | Technical fit | Functional fit | TIME verdict | Value evidence (one line)                                                                             |
| ------------------------------ | ------------------------ | ------------- | -------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| CRM platform                   | System of record         | High          | High           | Invest       | Every revenue workflow terminates here; 100% of forecast built on it                                  |
| Marketing-automation platform  | Nurture, scoring, email  | High          | High           | Invest       | Sources the majority of qualified pipeline                                                            |
| Sales-engagement platform      | Sequencing, outreach     | High          | Low            | Tolerate     | Adopted by one team of three; overlaps the marketing platform's email module for the rest             |
| Data-enrichment service A      | Firmographic enrichment  | High          | High           | Invest       | Feeds routing and scoring; match rate verified quarterly                                              |
| Data-enrichment service B      | Firmographic enrichment  | Low           | Low            | Eliminate    | Duplicate function; lower match rate on the same test set; nothing writes to the CRM from it          |
| Conversation-intelligence tool | Call recording, coaching | High          | Low            | Tolerate     | Managers stopped reviewing calls two quarters ago - flag for enablement before any cut decision       |
| Scheduling tool A              | Meeting booking          | High          | High           | Invest       | Embedded in every routing flow                                                                        |
| Scheduling tool B              | Meeting booking          | High          | Low            | Eliminate    | Duplicate function, bought by one team on expense; migrate its three users to tool A                  |
| E-signature service            | Quote/sign               | Low           | High           | Migrate      | Business-critical but fails on the CRM integration weekly; replace, don't cut                         |
| Data-hygiene/dedupe service    | Dedupe, record merge     | High          | High           | Invest       | 3 seats, 9% of licensed features used - and it protects forecast integrity (see the negative example) |

## The renewal overlay

A verdict without an action window is a wasted verdict. Overlay the calendar before ranking actions:

| Tool                      | Verdict   | Renewal       | Notice window | Action                                                                                         |
| ------------------------- | --------- | ------------- | ------------- | ---------------------------------------------------------------------------------------------- |
| Data-enrichment service B | Eliminate | 4 months out  | 60 days       | Act this cycle: give notice inside the window; migrate any residual lookups to service A first |
| Scheduling tool B         | Eliminate | 11 months out | 30 days       | Queue: set a calendar action for month 9; migrate users now (cheap), cancel at the window      |
| Sales-engagement platform | Tolerate  | 2 months out  | 90 days       | Window already closed - auto-renew will fire. Renew at the smallest tier, re-score next cycle  |
| E-signature service       | Migrate   | 7 months out  | 60 days       | Start replacement evaluation now; the migration must complete before month 5 to use the window |

The sales-engagement row is the point of the overlay: a correct Tolerate-toward-Eliminate trajectory is worth nothing this cycle because the notice window closed before the review ran - which is the argument for renewal-triggered cadence over calendar-triggered.

## Negative example - the utilization-only cut, done wrong

A reviewer sorting the inventory by seat-activity percentage flags the dedupe service first: 3 seats, 9% feature utilization, lowest usage in the stack. Verdict proposed: Eliminate.

Wrong, and the error is the method: usage was used as the cutoff instead of a diagnostic. The tool's function is invisible in login data - it deduplicates records in nightly jobs, and duplicate account records corrupt routing, attribution, and forecast rollups within a quarter of its removal.

The business-value check (what breaks if this disappears?) reverses the verdict to Invest. The 40-seat sequencer with no adoption and a duplicate function is the cut; the 3-seat service protecting the system of record is not comparable - this is the Brinker caveat operationalized.

Two remedies beat the cut for tools flagged on low utilization:

- **Enablement**: the conversation-intelligence row - managers stopped using it; teach before cutting.
- **Do nothing**: secondary users meant to touch a tool rarely are not waste.
