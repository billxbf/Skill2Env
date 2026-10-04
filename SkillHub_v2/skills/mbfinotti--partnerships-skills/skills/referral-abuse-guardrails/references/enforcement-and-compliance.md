# Enforcement Ladder and Compliance Constraints

Enforcement principles borrowed from trust-and-safety practice: proportionality, consistency, transparency [professional-association curriculum, not a ratified standard]. The legal material below is a set of design constraints, not legal advice - route every actual legal question to counsel.

Provenance tags:

- `[published terms]` - a program's own published rules.
- `[regulator]` / `[regulator code]` / `[regulator circular]` / `[regulator rulings]` / `[statute]` - a regulator's or legislature's own text.
- `[verified incident]` - court filing or multiple independent reports.
- `[vendor claim]` - published by a party selling the remedy.

## Build order: appeal path before detector

Every reward denial needs a specific reason string and a working appeal path, built _before_ the detection rules go live. A rejected reward with a stated reason and an appeal is defensible in every regime below; a silently missing reward is not, and it also generates the support tickets and churn that make friction cost exceed leakage.

Reason strings name the published rule violated ("per our terms, referred accounts must be new customers; this account had a prior order"), never internal signals ("device match"). Log the internal evidence separately.

## The published ladder

Each rung must appear in the published terms before it is used. Language observed in published programs [published terms]:

- efficiency: `withhold > link pause > program removal > clawback > account action`
- compliance cost: `account action > clawback > program removal > link pause == withhold`

Effort tracks compliance cost rung for rung here, so it gets no separate line: the rungs that draw a regulator are the same ones that generate disputes, appeals and investigation hours. Link pause and withhold tie on compliance cost because both are reversible, pre-money, and defensible on a published rule alone. Withhold leads on efficiency because it stops leakage before money moves, while clawback tries to recover money already gone and mostly buys support load instead.

Argued opt-out on rung selection: rank the rungs to know which to build first, never to pick one for a live case. Which rung a specific account gets is a proportionality judgment - severity, evidence strength, history - and proportionality overrides efficiency every time the two disagree. An efficiency ranking applied to an individual enforcement decision is false precision, and it is exactly how a boundary-pushing customer ends up banned.

1. **Withhold pre-payout, with reason.** Most common, safest. "Delay, withhold, or deny" language tied to defined abusive behavior.
2. **Pause the referral link / cooldown.** Reversible; fits the aggressive-bargain-hunter case.
3. **Remove from the program.** For repeat confirmed violations; strike-based escalation with documented history.
4. **Claw back paid rewards.** Aggressive. One exchange's terms revoke _all_ rewards including the innocent referee's on discovered self-referral [published terms] - revoking the counterparty's reward is exactly the behavior regulators scrutinize; avoid unless the referee is a proven co-actor.
5. **Account action.** "Suspend indefinitely pending investigation" appears in published terms [published terms] - "indefinitely" is the word that will not survive regulator contact; bound every investigation in time.

Treat the abuser and the aggressive bargain-hunter differently: assess risk before the promotion is delivered and apply friction selectively; a loyal customer pushing boundaries for a better deal may be worth retaining despite low-level abuse [vendor claim, sourced to a named practitioner]. Rungs 1-2 for boundary-pushers; rungs 3-5 for confirmed patterns.

## Legal design constraints

**Publication is a precondition.** UK promotional rules require awarding advertised rewards as described, normally within 30 days, and withholding is justifiable only on criteria clearly set out in the promotional rules beforehand; rules must be amended only exceptionally [regulator code]. Practical consequence: a guardrail not published before the referral was made is not enforceable against that referral, and retroactive tightening is the named failure mode.

US doctrine converges: promising a reward on stated conditions and denying it on unstated ones is an ordinary deception case [regulator settlement]. For credit-adjacent programs, relying on fine print to cancel earned rewards may itself be an unfair or deceptive practice - a blanket "sole discretion" clause is weaker than it is drafted to look [regulator circular].

**Silent denial is a legal risk in some regimes.** EU platform rules require a clear, specific statement of reasons for suspending monetary payments or accounts, plus a free internal complaint system open at least 6 months, not resolvable by fully automated means [statute]. Scoping caveat, stated plainly: this binds "online platforms" (marketplaces, services publicly disseminating user content) - a DTC brand's own store generally is not one. Whether it applies to a specific business is a question for counsel; the design (reason string + human-reviewable appeal) is worth adopting regardless because it is also the cheapest trust protection.

**Guardrail power creates liability for referrer conduct.** UK rulings held that because a program operator could dictate how codes were shared, cap referrals, and revoke credits, it had sufficient control over customers' posts to be _responsible_ for them. Terms merely prohibiting the conduct were insufficient while the operator retained meaningful control [regulator rulings]. Consequence: publish sharing rules (where codes may be posted, required disclosures) and actually monitor them; the ability to enforce makes non-enforcement the operator's problem.

**Enforcement teeth are real.** The UK consumer regulator can now investigate and fine directly, up to 10% of global turnover; first-year totals were material but not existential [regulator]. US referrer-side note: referred-and-rewarded customers are endorsers with a material connection that must be disclosed clearly [regulator guides] - put the disclosure requirement in the sharing rules.

**The sharing mechanism itself is an exposure.** The largest documented single financial hit to a named referral program - a $9M settlement - came from the program's prefilled invite texts violating anti-spam law, not from user fraud [verified incident]. Guardrail the share flow: no prefilled mass-texting, referee consent respected.

## Appeals mechanics

- Publish the appeal channel in the denial message itself; respond within a stated SLA (14 days is a defensible default, self-set rather than standard [derive from own policy]). No referral-program-specific regulator SLA exists to calibrate against; the closest published adjacent anchor is insurance fraud-investigation practice, which tiers by complexity - a few days for triage, roughly 30 days for standard cases, 60-90 days for complex/organized ones. A different regime and a different risk profile, so treat it only as a rough shape (tier by complexity, not one flat number), never as a borrowed standard.
- A human reviews every appeal; log outcomes. Appeals-upheld rate is the program's measured false-positive rate - feed it into the leakage/friction computation.
- Uphold generously on ambiguity: the friction term carries the LTV multiplier.
