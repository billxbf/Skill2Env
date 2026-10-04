# Consumer Referral Abuse Patterns

Defensive taxonomy: each pattern is described only to the depth needed to recognize and block it. The useful split is not by technique but by two axes - is one person or several behind it, and is the referred party real? That distinction determines which controls can possibly work.

Provenance tags:

- `[published terms]` - the program's own published rules.
- `[academic]` - peer-reviewed or peer-reviewed-track work.
- `[vendor claim]` - published by a party selling the remedy.
- `[verified incident]` - regulator/court filing or multiple independent press reports.
- `[unverified]` - widely circulated but unconfirmed; do not cite as fact.

## One person, both sides

**Self-referral.** The referrer controls the referee account: the only category where deterministic linkage checks work well (shared payment instrument, shared device, matching cookie identifier, near-identical email). Major referral platforms ship dedicated self-referral checks (cookie, IP+user-agent, similar-email) as a default product surface [vendor docs, published]. Observable tell: referrer and referee share a scarce identifier.

**Duplicate and synthetic account farming.** One main account plus several fabricated referee accounts, often deleted and recreated with modified credentials to repeat the cycle ("account cycling") [vendor claim]. Observable tells: referred accounts with no digital footprint, claim-then-dormant behavior, deletion/recreation cycles, disposable or sequential email patterns. This is the slice OWASP OAT-019 (Account Creation) actually covers.

## Several real people

**Referral rings and collusion.** The most underrated category, because every account is a real human on a real device - no device, IP, or identity check catches it. Best-documented case: drivers and riders in Uber's China operation matched on public forums, ran fake rides, and split the incentive [verified incident, contemporaneous press and book reporting].

Observable tells are cluster-level only: dense referral graphs among accounts with no organic relationship, synchronized claim timing, and downstream cohort collapse (referred accounts that never retain or transact). Warning: a genuinely enthusiastic advocate looks structurally identical to a small ring in graph data [academic - see detection signals]; require corroboration before enforcement.

**Repeatable incentive farming and return abuse.** Referee purchases to trigger the reward, then refunds; or an uncapped program invites the same pair to repeat [vendor claim]. Observable tell: refund rate on referred first orders far above organic. This pattern is the clearest argument for a hold window tied to the refund window rather than a round number.

## Leakage and stacking

**Code and link leakage.** A referral code escapes its intended audience onto coupon sites, deal forums, and code-swap communities; strangers - not friends - apply it [vendor claim]. Observable tells: referral volume spiking without matching referrer share activity, one code converting across unrelated geographies, the code indexed on public coupon pages. Mitigation is contractual (published sharing restrictions) plus code rotation; some programs ban coupon-site posting explicitly in terms [published terms].

**Cashback and coupon browser extensions.** A distinct problem: the attribution is rewritten by an intermediary, not gamed by your customer. Litigation over extension-based attribution rewriting exists [verified as to the litigation existing; allegations unproven]. Treat as an attribution-integrity issue, not a customer-enforcement issue.

**Reward stacking.** Referral credit combined with other promotions past the intended discount. Standard mitigation is a published exclusivity clause - "may not be used in conjunction with any other promotional offer" [published terms].

## Gaming the qualifying event

The single most important structural insight: promotion abuse at scale is a group activity in which ordinary customers conduct legitimate transactions with fraudulent behavior intertwined [academic, production-deployed system at a major delivery platform]. If the qualifying event is cheap and reversible, everything downstream - caps, detection, review - is a losing game. Fix the event first (see guardrail mechanics).

## B2B-specific patterns

- **Shell-entity self-referral.** A customer refers a "new company" they control. The shell has a real domain and a real work email, which is why a work-email check alone is weak. Observable tells: referrer-referee domain overlap in billing/admin contacts, freshly registered referee domain, shared billing entity or payment instrument.
- **Routing a deal that would have closed anyway.** An employee or agency inserts a referral link into an inbound deal. Observable tell: referee was already in the pipeline or trialing before the referral timestamp.
- **Referrer-buyer collusion.** An individual at the referring or referred company splits the reward with the counterpart [vendor claim as pattern; consistent with the loss shape]. This is a procurement/gift-policy and, in regulated sectors, anti-kickback problem before it is a fraud problem - company-account credit by default is the structural fix.

## Documented incidents (calibration, not fear)

| Incident                                     | Reported figure                                                  | Lesson                                                                                                                                          | Status                                                                                            |
| -------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Organized ring vs US delivery/ride platforms | $194,800 in referral payouts across 487 accounts (~$400/account) | The only clean per-account referral-loss figure on record; identity re-verification was the response                                            | [verified incident, DOJ-linked reporting]                                                         |
| Uber China incentive collusion               | "Millions" lost; a widely repeated 30,000-fake-rides/day figure  | Rings of real people defeat device checks; device-persistence countermeasures failed                                                            | Losses [verified incident]; the 30,000/day figure [unverified - traced to an investor in a rival] |
| Robinhood refer-a-friend settlement          | $9M settlement, ~827,000 consumers                               | The largest documented referral-program loss came from the sharing mechanism (unsolicited texts), not from fraud - guardrail the share flow too | [verified incident]                                                                               |

Do not use the "referral fraud = 21% of ecommerce fraud" statistic anywhere: it is circular vendor citation [unverified].
