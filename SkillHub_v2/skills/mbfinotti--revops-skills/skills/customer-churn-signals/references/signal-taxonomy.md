# Signal Taxonomy

Category-by-category candidate signals, the operational-definition template every candidate must satisfy, lead-time expectations, and the frameworks worth crediting. All tool-agnostic: "product event stream" means whatever telemetry the user has, "support ticket system" whatever they file tickets in.

## Table of Contents

- [The five-part operational definition](#the-five-part-operational-definition)
- [Categories, ranked by value per unit of instrumentation effort](#categories-ranked-by-value-per-unit-of-instrumentation-effort)
- [Lead-time expectations](#lead-time-expectations)
- [Framework credits](#framework-credits)
- [Confirmation tripwires](#confirmation-tripwires)

## The five-part operational definition

A signal is testable only when all five parts are written down:

| Part               | Question it answers     | Example sketch                                                                       |
| ------------------ | ----------------------- | ------------------------------------------------------------------------------------ |
| Event              | What is observed?       | Weekly active users in the account                                                   |
| Threshold          | How much change counts? | Down 40% or more                                                                     |
| Observation window | Over what period?       | Sustained 3 consecutive weeks                                                        |
| Baseline           | Compared to what?       | The account's own trailing-90-day median                                             |
| Normalization      | Adjusted for what?      | Per licensed seat; seasonality-adjusted for known cycles (holidays, fiscal-year-end) |

Baselines come in two flavors:

- The account's own history: catches decline in a healthy account. Prefer this for decline signals.
- Segment peers: catches an account that never activated. Prefer this for adoption-depth signals.

Without seat normalization, every growing account looks healthier and every downsizing account looks sicker than it is.

## Categories, ranked by value per unit of instrumentation effort

Work the categories in the efficiency order below and stop when the register clears its register-level floor.

Effort here is never money. It is:

- Engineering work to emit the signal at all.
- The analyst hours to define and backtest it.
- The latency before it can fire.
- Whatever standing job keeps it alive afterwards.

The axes disagree sharply, so each gets its own line:

- **value** (churn caught early enough that someone can still act): `product usage > feature-adoption breadth > champion departure (B2B) > login recency > seat utilisation > support-ticket pattern == customer business context > CRM engagement > billing behaviour > survey movement`
- **effort**, cheapest first: `login recency == billing behaviour == survey movement > seat utilisation == CRM engagement > support-ticket pattern > champion tracking > customer business context > product usage == feature-adoption breadth`
- **efficiency**, the default build order: `login recency > seat utilisation > support-ticket pattern > CRM engagement > champion departure (B2B) > product usage > feature-adoption breadth > billing behaviour > customer business context > survey movement`
- **compliance cost**: product usage, feature-adoption breadth, champion tracking, and customer business context only - each collects behavioural or personal data on named individuals, so each triggers a privacy review before the first event is stored, and the exposure is one-way: events collected without a lawful basis have to be deleted, not relabelled. Every other category reads a record the business already keeps for billing or support, and carries none.

Ties, justified:

- **login == billing == survey** on effort: each is a query against a system of record that already stores the field, with nothing new to emit.
- **seats == CRM**: both cost an hour of definition work rather than plumbing, reconciling provisioned against active seats and filtering CRM activity down to customer-initiated.
- **product usage == feature-adoption breadth** on both effort and compliance: they are blocked on the same missing artifact, a per-account product event stream. Once it exists both collapse to near-zero together, so they never separate.
- **support-ticket pattern == customer business context** on value: each catches a churn population the usage signals structurally miss, the frustrated heavy user and the healthy-usage account killed by a budget freeze, and neither covers much of the book alone.

### 1. Login recency and frequency - effort: near-zero

The RFM lens (Recency/Frequency/Monetary), remapped from retail to subscription:

- Recency: days since last login.
- Frequency: usage or touchpoint count over the window.
- Monetary: tier and expansion history.

Across sources applying RFM to churn, recency carries the strongest predictive influence of the three. Login logs exist wherever authentication does, which is what makes this the first candidate on every book.

### 2. Seat / licence utilisation - effort: near-zero to an hour

Gap between provisioned and active seats. A wide gap means low switching cost at renewal even if the active users are happy.

Define as active seats / provisioned seats, trended. The hour goes to reconciling what "active" means against the provisioning record, not to new data collection.

### 3. Support tickets and escalations - effort: an hour

Volume, severity mix, unresolved-ticket age, and sentiment trend - plus formal escalations as a discrete event. Genuinely ambiguous: an engaged customer files more tickets because they care; a silently disengaging one files none.

Never ship raw volume alone - pair it with sentiment/severity, and define "silence after a spike" (tickets surge then stop) as its own candidate. Sentiment scoring is what lifts this above near-zero.

### 4. CRM meeting/email engagement - effort: an hour

Customer-initiated meetings booked, email response rate and latency, QBR attendance. Artefact warning: a CSM emailing an at-risk account makes measured "engagement" rise - count customer-initiated activity only, or the vendor's own save motion pollutes the signal. That filter is the whole hour, and skipping it is what turns this category into noise.

### 5. Champion and executive-sponsor engagement/departure - effort: a week to stand up, then a standing job

B2B-only. Repeatedly cited as among the strongest single B2B signals; Lemkin puts non-renewal odds above 50% when the sponsoring executive departs.

Two distinct signals:

- Departure: a job-change event on the recorded champion.
- Disengagement: champion response rate/meeting attendance declining.

Champion departure is commonly cited as preceding churn by 30-60 days - and typically discovered at the renewal call, not when it happens, so instrument the detection, not just the field. The standing job is keeping the recorded-champion field true; a stale field silently produces a signal that never fires.

### 6. Product usage / telemetry - effort: near-zero if the product already emits per-account events, otherwise a quarter

The most commonly cited earliest-detectable family, and the highest-value category on the list. Decline is usually gradual - daily use becomes weekly becomes biweekly - not a cliff, so define trends against the account's own baseline rather than absolute floors.

Usage/engagement decline is commonly cited by practitioners as appearing 60-90 days before churn. It ranks sixth on efficiency only because of that instrumentation gate; see the starvation note below before accepting the position.

### 7. Feature-adoption breadth - effort: same gate as §6, plus an hour

Narrowing to fewer features, or plateauing instead of expanding into new teams and use cases, is flagged as a risk even when raw engagement looks fine (Jason Lemkin, SaaStr: usage that is not growing or spreading signals the customer is not seeing incremental value). Define as count of distinct core features used per window vs the account's prior window and vs segment peers. Needs the event stream of §6 plus a maintained definition of which features count as core.

### 8. Billing and payment behaviour - effort: near-zero

Failed payments, invoice disputes, late renewals, downgrade requests.

- **B2B**: late-stage/confirmatory - by the time payment friction surfaces, the account is usually already evaluating alternatives, which is what drops a near-zero-effort category this far down.
- **B2C**: payment failure is a proportionally larger churn driver and worth catching pre-emptively, so it climbs several rungs on a consumer book; it is still confirmatory of intent only when the customer lets it fail.

### 9. Customer business context - effort: a week to stand up, then a standing job

Layoffs, budget freeze, leadership change, M&A at the customer. Externally sourced (news, job-change alerts, the champion saying so); low frequency but high severity, and often the only warning for accounts whose product usage looks fine. Promote it on an enterprise book where losing one account is material - low coverage stops mattering when each covered account is worth a quarter of the number.

### 10. Survey movement (NPS/CSAT) - effort: near-zero

Weaker than assumed: point-in-time, and response-biased - the happiest and angriest over-respond while the quietly disengaging do not respond at all, making it a weaker churn predictor than product engagement in most subscription businesses. Counterpoint worth knowing: Dave Kellogg argues a direct "intent to renew" survey question captures churn-predictive signal that NPS misses.

Candidate definitions: score trend across waves (not one reading), and non-response itself after prior participation. It lands last despite costing nothing because the accounts it misses are exactly the quietly-disengaging ones the register exists to catch.

### What this order starves

Product usage and feature-adoption breadth carry the highest lift and the longest lead times on the list, and cost the most to instrument. So a register built strictly by ratio is all CRM-derived, all lagging relative to what the customer is actually doing in the product.

Promote both to the front of the build order when any of these holds:

- The product already emits per-account events. Effort collapses to near-zero and the ratio inverts outright - this is the common case in product-led books, so check it before accepting the default order.
- The Interview answer was "compounding asset" and the renewal cycle is long enough that the instrumentation lands before the next renewal window opens.
- A register assembled from the cheap categories fails the 70% register-level floor, which is what happens on a book whose churn is usage-driven: no volume of CRM-derived signals substitutes for never having watched the product.

Delete a category outright rather than parking it at the bottom when the Interview ruled it out:

- An unreachable data source.
- The B2B-only relationship categories on a B2C book, where there is no buying committee to lose a member from.

A ruled-out category left in the list reappears as scope two sessions later.

Treat this order as a default, not a law - it shifts with the book, with the product, and with who executes it.

Re-rank it against what you already know about the user:

- A data engineer on the team collapses the telemetry effort.
- An unmaintained CRM inflates the cheap categories' real cost.
- A book where every account is already wired for events makes the entire ordering above moot.

## Lead-time expectations

Commonly cited practitioner figures, not laws - measure the user's own median lead times in the backtest and prefer those:

- Usage/engagement decline: 60-90 days before churn.
- Enterprise intervention windows: extended to 120-180 days, to leave room for procurement cycles and multi-stakeholder re-alignment.
- Champion departure: 30-60 days before churn.

## Framework credits

Credit these where they genuinely fit; never force one onto a book of business it does not match:

- **Leading vs lagging indicators** - the foundational distinction this whole skill runs on.
- **Lincoln Murphy's Success Milestones** - usage is not success; track progress toward the customer's own defined outcome, and run structured churn-reason analysis on every loss.
- **Gainsight's guidance** - a deliberately small weighted signal set (4-6 signals) beats tracking everything, segmented by account tier because health looks different for SMB vs enterprise; Nick Mehta's DEAR frame (Deployment, Engagement, Adoption, ROI) names the leading-indicator stack he recommends over NPS alone.
- **RFM (Recency/Frequency/Monetary)** - remapped for subscription as above; recency strongest.
- **Survival/cohort analysis and WoE/IV** - ranking machinery, covered in the ranking reference.

## Confirmation tripwires

Class these as confirmatory - they formalize a decision usually made weeks earlier. They still belong in the register (flagged) because they escalate triage urgency, but they never satisfy the lead-time bar.

Deliberately unranked, unlike the categories above: every tripwire costs near-zero to instrument and buys zero lead time, so any ordering between them would be false precision. Instrument whichever ones the billing and product systems already expose, and treat the set as one triage input rather than a menu to choose from.

- Failed payment / lapsed card (B2B)
- Downgrade or seat-reduction request
- Procurement delay or renewal-date slippage
- Data export initiated
- Cancellation- or billing-page visits (B2C: often only days of warning)
- Auto-renewal switched off
