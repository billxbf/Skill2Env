# Detection Signal Catalogue

Every number carries a provenance tag. Treat tagged values as starting points to tune against the program's own baseline - never as industry constants.

- **[VENDOR]** - vendor or agency rule of thumb, published without independent validation.
- **[ACADEMIC]** - peer-reviewed result.
- **[DERIVE]** - a threshold that only means anything against the program's own data; compute it there.

## Baseline derivation (do this before setting any threshold)

1. Pull at least 90 days of per-affiliate data: conversion rate, click-to-conversion time (CTIT), session duration, refund/chargeback rate; for B2B add lead-to-qualified and lead-to-demo-show rates.
2. Compute program-wide mean and standard deviation per metric; store per-affiliate values against them.
3. Watchlist affiliates beyond 2 standard deviations from program norms - a published agency workflow [VENDOR], not a standard, but a sane outlier definition to start from.
4. Re-derive quarterly; baselines drift as the partner mix changes.

## Which signal family to build first

The table below is a catalogue, not a build order. Four families compete for the same engineering and analyst hours:

- value (most first): `downstream outcomes > cross-account identity > timing > list filtration`
- effort (most first): `cross-account identity > timing > downstream outcomes > list filtration`
- compliance cost (most first): `cross-account identity > everything else`
- efficiency (best first): `list filtration > downstream outcomes > timing > cross-account identity`

- **List filtration** (data-center ASN, declared bots, non-browser UA). Near-zero effort, no judgment call, no personal data. Worth little on its own, but at that cost the ratio is unbeatable, and it clears the crude volume the other three would otherwise be tuned against.
- **Downstream outcomes** (lead-to-qualified, demo-show, chargeback rate, revenue per visitor). A week of CRM/ledger joins. The only family AI-generated synthetic traffic cannot fake, since it has to produce real customers to beat it.
- **Timing** (CTIT, time on site, form-fill speed). A week of instrumentation. Strongest published accuracy of any family, but only against B2C stuffing, and behavioral heuristics are the ones synthetic traffic erodes fastest.
- **Cross-account identity** (device fingerprints, duplicate contact data, shared IP or payout destination). A quarter: lawful basis, retention design, access control, counsel sign-off - see the `[LEGAL REVIEW]` gate below.

Build list filtration first, then downstream outcomes; skip nothing above them before adding anything below.

That order starves cross-account identity - top of the evidence value, bottom of the ratio. Promote it the moment a case has to survive network compliance or a wire-fraud referral: a dossier with no shared-fingerprint or shared-payout finding rarely gets acted on, and no volume of timing signal substitutes for it.

## Signal table

| Signal                                                             | Starting threshold                                                                 | B2C / B2B    | Provenance                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------- |
| Redirect to affiliate link faster than a human could read the page | under ~2 seconds                                                                   | B2C          | [ACADEMIC] Snyder & Kanich 2016                       |
| Time on merchant site after cookie set                             | under ~2 seconds                                                                   | B2C          | [ACADEMIC] Snyder & Kanich 2016                       |
| Session duration                                                   | under 5 seconds flags stuffing                                                     | Both         | [VENDOR]                                              |
| Click-to-conversion time                                           | near-zero, or set per-offer floor/ceiling                                          | Both         | [VENDOR]; one platform flags under 30s or over 15min  |
| Conversion-rate outlier                                            | 2 SD above program CR → Watch                                                      | Both         | [VENDOR] agency workflow                              |
| Conversion velocity                                                | 3+ conversions in the same minute, repeatedly; evenly spaced ~30s intervals        | B2B lead-gen | [VENDOR]                                              |
| Form-fill speed                                                    | under 3 seconds, no mouse movement, identical field-skip patterns                  | B2B lead-gen | [VENDOR]                                              |
| Chargeback rate                                                    | above 3% in rolling 30 days → suspend + net-60/90 terms                            | B2C          | [VENDOR]                                              |
| Clicks with near-zero conversions elsewhere                        | high volume, no sales - classic stuffing tell                                      | B2C          | [DERIVE] vs own click-to-sale norm                    |
| Lead-to-qualified rate                                             | materially below program norm, sustained                                           | B2B          | [DERIVE]                                              |
| Lead-to-demo-show rate                                             | materially below program norm, sustained                                           | B2B          | [DERIVE]                                              |
| Sales concentration                                                | ~80%+ of program sales from a handful of affiliates → audit, not enforcement       | Both         | [VENDOR] practitioner flag - re-verify before quoting |
| New-affiliate application                                          | free-email provider, generic phone, thin/no site → manual review or stricter terms | Both         | [VENDOR] platform practice                            |

The two ~2-second timing features are the strongest single published result: a two-feature decision tree hit 93.3% accuracy, 1.5% false positive, 5.2% false negative against human labeling (Snyder & Kanich, _Journal of Cybersecurity_ 2016). They are the empirical basis for every "near-zero CTIT" vendor heuristic.

## Data-protection caveat on every cross-account identity signal - `[LEGAL REVIEW]`

Device fingerprinting, matching emails/phones/addresses across accounts, and comparing click IP to billing address are all processing of personal data, and several sit outside anything a cookie banner covers. The UK regulator's published position is that deploying fingerprinting requires fair choices and possibly consent even outside advertising.

Before shipping a rule built on these signals, state each of the following, then route the design to counsel:

- The lawful basis.
- The retention period.
- Who can see the matched records.

Fraud prevention is a commonly cited basis, not an automatic one, and "we needed it to catch fraud" is not a basis at all.

This applies to every signal below that identifies a person or a device across accounts, and to the cross-reference step in the investigation reference.

## Signals without defensible published numbers - all [DERIVE]

- Blank or suspicious HTTP referrer headers; declared traffic source vs observed referrers.
- Data-center ASN, VPN/proxy, TOR exit nodes (GIVT-class; list-filter these outright).
- Geo mismatch between click IP and billing address.
- Duplicate emails, phones, addresses, or device fingerprints across leads or accounts.
- Disposable-email and role-account domains on B2B leads.
- High traffic with low customer lifetime value; high lead volume with zero customers.
- New-affiliate first week: approved affiliates who never send traffic, then spike; apply stricter filters and longer payout terms (net-60/90) to new partners.
- Shared registration IP/billing between affiliate and customer accounts (self-referral).

## Structural cross-check principle

Never trust client-reported data standalone. Cross-check what a click claims about itself (declared UA, source, geo) against an independently observed layer: server-side postbacks vs client pixels, your CRM/order ledger vs the platform's reported conversions, edge-observed IP/ASN vs claimed location. A mismatch between the client's story and the network's story is itself a signal.

## Statistics to distrust

- "17% of affiliate traffic is fake / $3.4B lost": single anti-fraud vendor's marketing study, circularly cited across the industry. Never use as a baseline.
- "30% of losses tied to fraud", "8-15% of commissions lost", "IVT is ~40% of web traffic": all vendor estimates with commercial incentive.
- The only adjudicated dollar figures are the eBay wire-fraud court records; the strongest prevalence studies are a decade old and disagree by methodology.

## Manual review or automated scoring

- efficiency (best first): `manual review + IP/email validation > automated per-event scoring` - and the order flips above roughly 50 affiliates or $50K/month commission spend [VENDOR].
- effort (most first): `automated per-event scoring > manual review` - scoring costs a quarter to procure, integrate and tune before it flags anything; manual review costs analyst hours from day one and never stops.

Below the trigger, an analyst reading the partner list beats a scoring model that has too few events to calibrate against. Above it, the analyst hours grow with the roster while the model's do not, which is the whole reason the order flips. Behavioral heuristics (session duration, scroll depth) are being eroded by AI-generated synthetic traffic - anchor automation on server-side postbacks and downstream outcomes, and treat recent detection-efficacy claims as unverified.
