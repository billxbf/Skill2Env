# Partner Types, ACV Bands, and Process Tracks

Citations name the publishing vendor or consultancy. Treat single-source specifics as one practitioner's convention.

## Registration and credit mechanics by partner type

The best-corroborated pattern in the co-sell literature: mechanics map to how each partner type earns money, and do not generalize across types (PartnerStandard, Suger).

| Partner type              | Primary economics                                                               | Mechanic the charter needs                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Referral                  | Flat fee or % of first-year revenue (typically 5-20%) for an introduction       | Lightest touch - clean attribution tracking and payment reliability, not margin protection or formal registration            |
| Reseller / VAR            | Margin between wholesale and resale; owns contract, billing, first-line support | Formal deal registration is essential - pricing/margin rules, enablement, registration to prevent direct-vs-channel conflict |
| Distributor               | Two-tier economics, sell-through volume commissions                             | Same formal tier as resellers, plus reseller-network development tooling                                                     |
| SI / consultancy          | Services revenue, not resale margin                                             | Resale-style registration doesn't map - motivate with services pipeline, certification, co-sell support, qualified leads     |
| ISV / tech partner        | Builds on the platform, sells its own product                                   | Resale registration is commercially irrelevant - needs integration certification, marketplace listing, developer access      |
| Marketplace / hyperscaler | Revenue share tied to a specific transaction                                    | Registration exists but is transaction-linked; rate, caps, payment trigger, and clawback terms travel with the record        |

Edge case: **OEM/white-label** partners own the entire customer-facing relationship, so traditional registration conflict doesn't arise at all.

Hyperscaler programs converge on one generic architecture (Tackle, Clazar, Labra - vendor summaries; Microsoft Learn is the one primary source):

1. Partner-network tier membership.
2. Marketplace as the transaction rail.
3. An opportunity-sharing system that assigns an ID and routes the deal into the platform's own pipeline.
4. Escalating co-sell status tiers unlocking deeper field-seller engagement.

Published gating exists - for example, Microsoft requires a $25,000 minimum deal value for registration, and its top co-sell tier requires ~$100K revenue and a transactable marketplace offer. Treat these as one platform's published mechanics, not portable defaults.

## ACV bands and segment differences

- One consultant's bands (PartnerStandard - illustrative, single-sourced, not authoritative):
  - Below €3-5k ACV: channel is difficult and referral is the only realistic motion.
  - €5-50k: referral plus light co-sell becomes viable.
  - Above €50k: resellers/SIs/service partners become viable.
- The general floor for _any_ sales-assisted motion: practitioner consensus around $3k ACV for a hyper-efficient team, $5k once overhead is counted (SaaStr) - below that, stay self-serve and skip co-sell overhead entirely.
- **Segment differences (SMB / mid-market / enterprise) have no settled co-sell design.** The intuitive mapping - lightweight self-serve registration for SMB, formal with legal/security gates for enterprise - is an inference from general sales-segment practice, not an established convention. Present it as a hypothesis for the user to confirm against their own motion, never as established practice.

## Readiness diagnostics for the disqualifier gate

Questions worth asking verbatim during the gate, beyond the five disqualifiers in SKILL.md:

- One investor framework's readiness screen (Insight Partners):
  - Have you established a predictable ARR engine through direct sales already?
  - Is there real market pull, or would a channel be "pushing the ball uphill"?
  - Do you have referenceable customers partners can point to?
  - Is the product documented and understood well enough for a third party to implement or sell it?
- Operational threshold (PartnerStandard - single consultant source): early-stage companies should start with **two or three deeply engaged referral partners, not a formal program**. A formal program with a dedicated full-time operator only pays off around €1M-5M ARR. Below that, a shared/part-time owner is inadequate.
- Foundational overhead that must exist before registration can credibly run: basic partnership agreements, a program outline, partner pricing, rules of engagement, registration procedures, and sales-ops readiness. Skipping straight to a formal program without this scaffolding is itself disqualifying (Avoid The Drift).
- Second-order disqualifier: passing the readiness gate and then jumping straight to drafting a partner agreement instead of running discovery first. "Not ready" is also about skipping the design process, not only company stage.
- Fit-based disqualifier: a trivially cheap, auto-installing product may structurally have no partner play at all, regardless of ACV or stage.
- Commercial diagnostics in this space run 130+ checkpoints across four dimensions - business fundamentals, growth stage, general partner readiness, operational readiness for the specific partner type - but only the dimension names are public. Use the dimensions as an outline, not a checklist to fabricate.

## The two process tracks

No single dominant design methodology exists. Published guidance splits into a lightweight and a heavyweight track, ranked by value per unit of effort and presented in that order: `lightweight playbook > heavyweight JBP`.

The axes disagree: on raw value `heavyweight JBP > lightweight playbook`, and on effort `heavyweight JBP > lightweight playbook` too, which is exactly why the higher-value track loses on ratio. Choose per partner. A portfolio usually needs both, and the ordering shifts with partner type, ACV, and who on the user's side runs the session.

### Lightweight: single-session playbook fill (transactional / high-volume partners)

Best ratio, and the default for every partner until something moves it. Buys a named owner per cell and a shared deal-stage map - the two things most co-sell disputes actually turn on. Costs one 90-minute session per partner plus a one-time template build.

Build one fixed 5-section template, then fill it per partner in a single 90-minute working session with the partner-program owners of both companies present. Only the content changes per partner; the structure stays fixed (Forecastable - vendor content):

1. ICP and target-account criteria - where both companies have credible reason to engage.
2. Roles and ownership matrix - **a named individual, not a team, in every cell**: "shared ownership is no ownership."
3. Joint deal-stage map with an exit criterion per stage, giving deal reviews a shared language.
4. Messaging and assets per stage.
5. Metrics and review cadence.

### Heavyweight: joint business planning (strategic / enterprise alliances)

Highest value, worst ratio. Buys two-sided executive sponsorship and a budgeted plan - the only lever that moves a partner whose own field sellers carry quota. Costs weeks of drafting, a two-sided sign-off chain, and a standing quarterly review job.

Move up to it only when the partner's sellers are the ones you need to influence and both sides will fund the reviews. If the partner side will not name an executive sponsor, drop this track from the menu entirely rather than recommending against it: an unsponsored joint plan produces a document nobody executes.

Rooted in retailer-supplier planning, adapted to tech alliances (The Gap Partnership, ZINFI, NACDS):

1. Senior-leadership kickoff establishing ground rules and visible sponsorship on both sides.
2. Alignment on shared, measurable objectives.
3. Each side shares its own business plan and the mutual growth opportunity is discussed.
4. Plan drafted across functional sections: GTM, marketing, sales KPIs by quarter, training/certification, communication SLAs.
5. Formal approval and sign-off, then execution with quarterly reviews.

Readiness gate before starting: "is there enough business happening, is the incremental opportunity big enough, and is there adequate will-and-skill on both sides to invest the time."

Three published ways to actually run it, ranked by value per unit of effort: `the 5-step sequence above > AWS objective vocabulary > CHAMP workshop`. Only the efficiency axis is stated, because CHAMP's value is a single consultant's uncorroborated claim and ranking it on value would be false precision.

- The 5-step sequence above costs nothing beyond the meetings it schedules and already delivers sponsorship, objectives, and a review cadence.
- AWS's own program guidance is the most authoritative published design sequence for platform/hyperscaler co-sell, framed around launched opportunities, influenced revenue, marketplace gross software sales, and co-sell opportunity counts:
  1. Define SMART objectives.
  2. Align initiatives to each objective.
  3. Adopt the marketplace as a strategic channel.
  4. Build enablement.
  5. Secure cross-functional sponsorship (internal leadership plus the partner's own sales managers).
  6. Allocate people/budget/time per initiative.
  7. Monitor through regular reviews.

  An hour to borrow the objective vocabulary, which is useful even outside that platform. Narrower than a full method.

- CHAMP is a certifiable methodology delivered as a 2-day cross-functional workshop producing a Partner Plan and a Joint Plan - two days of senior calendar plus a consultant, and not independently corroborated. Mention it as an option, never as a standard.

## Partner discovery-session mechanics

Single vendor source (Forecastable), specific enough to reuse with that flag:

- Pre-read one-pager sent 24 hours ahead: overlap-account list, draft joint value frame, the proposed motion, three open questions for the partner side.
- Right attendee: the partner-side partnerships leader or regional sales leader - defer the session if that person can't attend.
- Length: 60 minutes as a working session. 15 minutes is a vendor pitch. 90 is a relationship meeting the partner side won't make time for.
- Directional conversion benchmark: mature programs convert 3-4 of 8 discovery sessions into a scoped co-sell pilot. Weak programs convert ≤1 of 8.

Account-overlap mapping through a neutral third party (rather than emailing spreadsheets between partners) is now standard practice for building the overlap list. The associated partner-lift statistics (bigger ACV, higher win rate, faster cycles) are that category's own vendor marketing - directional only.
