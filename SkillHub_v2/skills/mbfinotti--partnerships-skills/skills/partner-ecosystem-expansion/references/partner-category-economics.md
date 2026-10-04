# Partner Category Economics

The per-category facts sequencing runs on, ordered by efficiency: value returned per unit of effort, highest ratio first. All ranges are directional - the underlying figures mix vendor and consultant sources and are not independently benchmarked; carry that flag when quoting them.

Effort is what the team spends - build time, standing coordination, headcount held, reversibility - never a currency amount. Readiness prerequisites per category are scored at a separate workflow step and are not repeated here.

## B2B categories

Efficiency order (open first): **tech/ISV > referral/affiliate > agency > marketplace > MSP == SI/GSI > reseller/VAR**

| Category                              | Commercial model                                                                    | What it buys                                                                                                                 | Time to first revenue | Effort to stand up                                                                                        | Standing load                                        | Compliance exposure                                                                                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Technology / ISV                      | Rev-share on integrations, marketplace referral fees, co-sell credits               | Closes whole-product gaps named in lost deals, and compounds - the integration surface makes a later marketplace stage cheap | Medium                | A quarter - integration surface, docs, sandbox, built once and reused by every partner                    | An hour per partner once the docs hold               | Low - standard agreement; a security review only if a marketplace stage follows                                           |
| Referral / affiliate                  | Fixed fee or referral commission; simple contract                                   | Top-of-funnel pipeline from people already advising your buyer; no delivery capacity, no coverage                            | Fastest               | A week - tracking, payout, simple terms                                                                   | Near-zero per partner                                | Low - disclosure plus a standard agreement; ends when the agreement ends                                                  |
| Agency                                | Referral fee or margin, plus their own services around your product                 | Coverage of buyers who arrive with an advisor, and delivery capacity you never staff                                         | Medium                | A quarter - certification content, co-marketing assets, lead sharing                                      | A week per cohort                                    | Low - disclosure plus a standard agreement                                                                                |
| Marketplace (hyperscaler / app store) | Platform take rate on transactions, or listing plus co-sell                         | The procurement path itself: committed spend, an existing vendor relationship, a buying process you skip                     | Medium                | A quarter - listing readiness, billing integration, security review                                       | A week per quarter of listing ops and policy changes | High - platform policy, security review, price parity; delisting and take-rate changes are the platform's call, not yours |
| MSP                                   | Recurring, bundled managed-service revenue                                          | Retained revenue plus an operating layer you never staff - the bucket the surviving channel margin moved into                | Slow                  | A standing job - multi-tenant administration, monitoring/billing hooks, tiered support                    | A standing job                                       | Medium - contracting, support SLAs, data handling inside a partner-operated tenant                                        |
| SI / GSI, consultancy                 | Services-first; co-sell credits, SOWs - partner services revenue often 2-5x license | The enterprise route to market itself, in segments that buy only through implementers                                        | Slowest               | A standing job - implementation methodology, certified-practitioner program, executive sponsorship        | A standing job, named-account by named-account       | Medium - MSAs, sub-contracting terms, named-account alignment                                                             |
| Reseller / VAR                        | Margin/discount on booked revenue                                                   | Booked revenue through a procurement relationship you already lost - at a margin that has structurally collapsed             | Medium-slow           | A quarter or more - deal registration, margin structure, sales and technical certification, support model | A standing job                                       | Medium-high - channel pricing discipline and margin committed contractually before you learn the volume                   |

The axes disagree, so read them separately:

- cost (heaviest first): `SI/GSI > MSP > reseller/VAR > tech/ISV == marketplace == agency > referral/affiliate`
- value (biggest payoff first): `SI/GSI > MSP > tech/ISV > marketplace > reseller/VAR > agency > referral/affiliate`
- compliance cost (most exposure first): `marketplace > reseller/VAR > MSP > SI/GSI > tech/ISV > agency == referral/affiliate`
- efficiency (open first): `tech/ISV > referral/affiliate > agency > marketplace > MSP == SI/GSI > reseller/VAR`

The ties, and why they are genuine:

- `MSP == SI/GSI` on efficiency: both buy the durable retain-and-deliver economics, both cost a standing job to run, and neither converts ahead of the other unless the buyer route already goes through an implementer - the same condition promotes both.
- `tech/ISV == marketplace == agency` on cost: each is roughly a quarter of build reused across the whole category (integration surface, listing plus security review, certification track), and none of them adds a per-partner headcount.
- `agency == referral/affiliate` on compliance cost: both carry only disclosure and a standard agreement, and both unwind by ending that agreement - no platform policy, no committed margin, nothing to claw back.

**Why tech/ISV leads and referral does not.** Referral is the cheapest category, not the most efficient one: it buys pipeline only, and nothing it builds makes the next category cheaper. The integration surface an ISV motion forces you to build is reused by the marketplace stage, by agency implementers, and by every MSP that operates the product later. Cheapest-first is the practitioner-asserted prior - it is the cost line above, not the recommendation.

**What this order starves: SI/GSI and MSP.** Highest value in the table, highest effort, so a ratio ranking pushes both to the back every single round - the documented pattern where programs over-serve cheap influence categories and starve technical and services enablement.

Promote them anyway when any of these holds:

- The buyer purchases only through implementers (enterprise, regulated, public sector).
- Implementation capacity is named in three or more lost deals.
- The roadmap needs retained rather than new revenue.

The services multiple is the argument to eventually get there - Canalys' AWS-commissioned studies report $7.13 of partner-services revenue per $1 of platform sold for services-heavy "Expert" partners vs $1.26 for resell-focused partners (VENDOR-COMMISSIONED) - sourced from a party with an interest in that conclusion.

**Reseller/VAR sits last for a structural reason.** McBain/Omdia document point-of-sale reseller margins falling from ~20% to ~3% as vendors shifted to subscription; in a 378-partner survey, 58% expected profit decline, 51% forecasting double-digit drops (ANALYST). The category still buys real booked revenue, but at an effort and margin commitment the current economics no longer repay for most vendors.

## B2C categories

Efficiency order (open first): **creator/influencer > affiliate > marketplace > retail/wholesale > licensing == co-branding > distributor**

| Category             | Commercial model                                        | What it buys                                                                                     | Time to first revenue | Effort to stand up                                                                   | Standing load                                     | Compliance exposure                                                                                 |
| -------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Creator / influencer | Flat fee, commission, or hybrid; gifting at the low end | Demand created before intent exists, plus content assets reusable in paid and owned channels     | Fast                  | A week - brief and asset kit, usage-rights terms                                     | A week per campaign cohort                        | Medium - disclosure rules are enforcement-backed, and the liability is yours as well as theirs      |
| Affiliate            | Commission on tracked sales (often 10-15% for creators) | Conversion of demand that mostly already existed - cheap, and rarely incremental                 | Fastest               | A week - link/code attribution, payout process                                       | Near-zero per partner                             | Low - disclosure plus a standard agreement                                                          |
| Marketplace          | Platform take rate                                      | Shelf reach with no trade negotiation, and a buying flow customers already trust                 | Medium                | A quarter - listing operations, fulfillment integration, price-parity policy         | A week per quarter of listing ops                 | High - platform policy and price parity; the platform can change the take rate or delist you        |
| Retail / wholesale   | Wholesale margin                                        | Physical shelf reach and the volume that comes with it - the biggest distribution step available | Medium-slow           | A standing job - trade pricing, fulfillment at retail cadence, merchandising support | A standing job                                    | High - trade terms, promotional commitments, and margin fixed before the sell-through is known      |
| Licensing            | Royalty                                                 | Royalty revenue with no COGS and no fulfillment, on a brand you already own                      | Slow                  | A quarter of legal and brand work, then near-zero ongoing                            | An hour per quarter, plus quality-control reviews | High - brand guidelines, quality control, and long terms that are the hardest thing here to reverse |
| Co-branding          | Shared campaign economics                               | Borrowed brand equity and a reach spike for one campaign; nothing compounds after it ends        | Medium                | A quarter - brand-fit vetting, joint approval process                                | A week per campaign                               | Medium - trademark and joint-approval terms, ending with the campaign                               |
| Distributor          | Distributor margin layered above retail                 | Reach into retail you cannot serve directly, at a second margin layer stacked on the first       | Slow                  | A standing job - volume production, channel pricing discipline                       | A standing job                                    | High - channel pricing discipline and terms that bind what you can do direct                        |

- cost (heaviest first): `distributor > retail/wholesale > licensing > marketplace == co-branding > creator/influencer > affiliate`
- value (biggest payoff first): `retail/wholesale > distributor > licensing > marketplace > creator/influencer > co-branding > affiliate`
- compliance cost (most exposure first): `licensing > retail/wholesale > distributor > marketplace > creator/influencer > co-branding == affiliate`
- efficiency (open first): `creator/influencer > affiliate > marketplace > retail/wholesale > licensing == co-branding > distributor`

The ties:

- `licensing == co-branding` on efficiency: both buy borrowed brand equity rather than distribution, both need an approval and quality-control machine you do not have unless legal is already in-house, and neither makes the next category cheaper.
- `marketplace == co-branding` on cost: both are a quarter of setup work (listing and fulfillment integration; brand-fit vetting and a joint approval process) with no standing headcount attached.
- `co-branding == affiliate` on compliance cost: both carry a disclosure obligation and a trademark clause, and both end when the campaign or the agreement does.

**What this order starves: retail/wholesale and distributor.** The largest distribution steps a consumer brand can take, ranked last because both are a standing job with margin committed up front. Promote them when the category the buyer shops in is physical-first, when a retail buyer has already asked, or when DTC growth has flattened and the roadmap needs reach rather than efficiency.

## Trifurcation buckets (candidate-pool axis)

Every category above sits in one of McBain/Canalys' three journey buckets - use them to spot the empty bucket, never as a sequence:

- **Influence**: referral, affiliate, creators/influencers, agencies (advisory side), analysts.
- **Transact**: resellers/VARs, distributors, marketplaces, retail/wholesale.
- **Retain-and-deliver**: MSPs, SIs/GSIs, agencies (delivery side), licensing operations.

## Re-ranking against this user

Both orders above are defaults, not laws. They shift with context and with who executes them, so re-rank before presenting anything:

- **Delete, never demote.** A category the user's constraints rule out leaves the candidate pool entirely, with the reason recorded in the roadmap's `Not now` line and a re-entry trigger. Examples: no channel margin room deletes reseller/VAR, no multi-tenant administration on the roadmap deletes MSP, no in-house legal capacity deletes licensing. A ruled-out category parked at the bottom of a ranked list reappears later as scope.
- **An existing services arm promotes SI/GSI to the top**: the standing job that makes it expensive is already staffed and already carries the methodology.
- **A product that needs no implementation demotes SI/GSI and agency below marketplace**: there is no services gap for either to fill.
- **A partner team of one deletes every standing-job category** - MSP, SI/GSI, reseller, retail, distributor - until headcount changes; a single manager cannot carry one of them and the proven motion at the same time.
- **The buyer's route outranks the effort ranking.** If the buyer only purchases through implementers, an SI category comes early despite its load - the sequence serves the route to market.
- **The current base changes the adjacency.** The cheapest next category depends on what is already proven: an ISV motion reaches a marketplace stage cheaply, while the same stage is premature for a referral-only base.
- **A whole-product gap named in lost deals** pulls its filling category forward regardless of where the efficiency line puts it.
- **A category's structural economics can shift.** The reseller margin collapse is the live example: an order that made sense a decade ago can point at a bucket whose economics have moved.
