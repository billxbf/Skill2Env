# Fleet View and Health Scoring

The provider-side view of which integrations are breaking, how to score partner health, and why consumer-side SLO framing does not transfer.

## Contents

- What the fleet view is for
- Layout and ranking
- Per-partner health scoring
- The consumer-side SLO adaptation gap
- What not to publish

## What the fleet view is for

Steps 2 through 5 of the skill build outward-facing surfaces. This one faces inward: your partner, support and platform teams looking across the whole integration base and asking which partner to contact first. It runs on the same aggregation as the outward surfaces, read along a different axis.

It exists because proactive outreach needs a queue. Without it, "we notice partner problems before they do" is aspirational - someone has to be looking at a ranked list on a Monday morning, and the ranking is what makes that a five-minute job rather than an afternoon.

## Layout and ranking

Rank by blast radius rather than raw error volume. A partner app failing across 200 installs outranks a single high-traffic account throwing more absolute errors, because the first is one conversation that fixes 200 problems. A flat leaderboard sorted by error count inverts exactly that priority.

Dimensions worth having on the view:

- **Installs affected** versus **installs total**, per partner app. The ratio is the diagnosis: 200/200 is a partner-side release, 3/200 is a configuration problem at three customers.
- **Error rate against that integration's own baseline**, not a global threshold.
- **First-seen timestamp**, aligned against both your release timeline and - where you know it - the partner's. Broken since your deploy is yours outright. Broken since theirs is the outreach case.
- **Dominant status-code bucket**, so the queue separates "their payloads changed" from "we broke them" from "they hit quota" before anyone opens a ticket.
- **Silent integrations** - call volume dropped to or near zero against baseline. These appear in no error ranking and are frequently the worst failures, because nobody on either side has noticed.
- **Contact ownership**, so the row is actionable. A ranked list with no named partner contact becomes a report nobody acts on.

Give the view a second tab for the platform's own view of itself: integrations whose failures correlate with your last release, aggregated. That is your regression queue, and it should never be mixed into the partner-outreach queue.

## Per-partner health scoring

A weighted health score per partner is a real shipped pattern, not an invention: third-party tooling built specifically for ISVs on Salesforce computes a per-managed-package weighted health score and a churn-risk signal from it (sourced: ISVapp product documentation). That the pattern exists as a third-party product is itself informative - it fills a gap the underlying platform did not expose to its ISVs natively.

If you build one, three rules keep it honest:

1. **Set and defend your own weights.** Borrowing another product's weighting produces a number nobody in your organisation can explain when a partner disputes it - and they will dispute it, because a low score is a commercial signal.
2. **Make the inputs inspectable.** A partner shown a score must be able to see the error counts, install coverage and windows behind it. An opaque score is a trust liability, and the first dispute converts it into a support burden larger than the one it saved.
3. **Decide internal versus external before building.** An internal prioritisation score and a partner-facing health grade are different products with different obligations. The internal one can be rough and iterated. The external one becomes a contract the moment partners optimise against it.

Score composition that holds up in practice:

- Error rate relative to baseline
- Install coverage of the failures
- Trend direction over the long window
- Time-since-last-clean-period

Volume alone is not health - a large partner with a stable 0.5% error rate is healthier than a small one at 30%.

## The consumer-side SLO adaptation gap

The published literature on error-budget and SLO framing is consistently **consumer-side**: guidance for a company that depends on third-party APIs, not for a platform providing one to external integrators (sourced: Nobl9 "A Complete Guide to Error Budgets", Stytch "Understanding SLAs, SLOs, SLIs and Error Budgets"). Borrowing the framing wholesale is a documented failure mode of this design. The consumer-side literature on reliability states these principles, some of which transfer to the provider side and others do not:

- **Give each third-party dependency its own SLO** rather than folding vendor downtime into one blended number (sourced: Nobl9, Stytch; also Google Cloud's CRE blog "Defining SLOs for services with dependencies", and formalized in Treynor, Dahlin, Rau and Beyer's "The Calculus of Service Availability", ACM Queue / SRE Workbook). _Transfers as a shape_: per-integration and per-endpoint granularity beats a blended platform number, which is the same argument step 4 of the skill makes.
- **Multi-vendor reliability compounds multiplicatively** - several 99.9% dependencies cap the consumer's achievable availability below any one of them (sourced: Nobl9, Stytch). _Does not transfer_: this is arithmetic about the consumer's position, not yours.
- **Do not trust a vendor's status page as your monitoring source.** The gap between a real outage and a status update is error budget draining unwatched (sourced: Nobl9, Stytch; also ThousandEyes, "Why You Shouldn't Trust (Only) the Status Page"). _Transfers inverted_, and this is the interesting one - you are the vendor being distrusted.
- **Endpoint-level granularity matters** because a blended uptime number hides partial outages of specific functionality (sourced: Nobl9, Stytch; the same point recurs across API-observability vendor documentation, e.g. Zuplo, Datadog, without one canonical origin). _Transfers directly._
- **Multi-window burn-rate alerting** catches both sudden spikes and slow degradation (sourced: Google SRE Workbook, "Alerting on SLOs"). _Transfers directly_: a short window for sudden breaks, a long one for creeping degradation.

The mirror-image framing - the platform working to be the trustworthy, real-time source about integration health so its partners do not have to build independent monitoring of it - is **this skill's own construction, not a sourced practice**. It is a useful design intent. It is not something to present to partners as an industry standard, and nothing in the published record establishes what a provider-side integration SLO should contain.

## What not to publish

- **A per-partner reliability number you cannot defend line by line.** Once published it is quoted back at you in commercial conversations.
- **An availability commitment derived from the fleet view.** The fleet view measures integrations, which include the partner's own code and their customers' configurations. Committing to a number you only partly control is a promise you cannot keep. Formal SLA and uptime publication belongs to `samber/developer-platform-skills@api-status-communication`.
- **Cross-partner comparisons.** A partner learning where they rank against named competitors turns an operational tool into a commercial incident.
- **A health grade with no appeal path.** If a score affects a partner's tier, placement or commercial terms, it needs a documented recomputation and dispute process before it goes live, not after the first complaint.
