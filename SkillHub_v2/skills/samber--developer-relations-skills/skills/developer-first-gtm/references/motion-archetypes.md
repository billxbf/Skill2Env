# Motion archetypes and the friction gates

Contents: where this taxonomy comes from; the three friction gates in detail; the four motions (money path, prerequisite, what it forces you to build, leading indicator, failure mode, fit signals); combining motions; sequencing by stage.

## Table of Contents

- [Where this taxonomy comes from](#where-this-taxonomy-comes-from)
- [The three friction gates](#the-three-friction-gates)
- [Motion 1 - Bottom-up self-serve](#motion-1-bottom-up-self-serve)
- [Motion 2 - Developer-influenced sales (product-led sales)](#motion-2-developer-influenced-sales-product-led-sales)
- [Motion 3 - Top-down with developer proof](#motion-3-top-down-with-developer-proof)
- [Motion 4 - Ecosystem-mediated](#motion-4-ecosystem-mediated)
- [Combining motions](#combining-motions)
- [Sequencing by stage](#sequencing-by-stage)

## Where this taxonomy comes from

The four motions below are **this skill's synthesis**, not a published framework. Present them that way. They are built on top of a vocabulary that _is_ published, in the Lenny's Newsletter study _GTM motions of 30 B2B SaaS companies_, which separates two independent axes:

- **Product-led** (the product is self-serve; users convert on their own) versus **sales-led** (someone must onboard you before you try it).
- **Top-down** (target leaders who push the tool down) versus **bottom-up** (target individual contributors who spread it).

Plus two useful compound terms from the same source:

- **sales assist** - a sales team closing and expanding the larger accounts that arrived product-led
- **bottom-up lead gen** - a sales-led company whose self-serve product exists to feed leads rather than revenue; worth naming out loud, because teams run it while believing they run product-led growth

The mapping:

- bottom-up self-serve = product-led × bottom-up
- developer-influenced sales = product-led × bottom-up plus sales assist, which the industry calls product-led sales
- top-down with developer proof = sales-led × top-down, with the developer holding a veto rather than the pen
- ecosystem-mediated has no counterpart in the published axes: it is this skill's own addition and the least evidenced of the four

A second published check, from _The Transition: Layering sales onto a bottom-up self-serve product_: self-serve is plausible as a starting motion if at least one of these is true.

- The product is simple enough for **its own audience** to self-activate; complexity is relative, a technical product can be self-serve when the audience is technical.
- The category is new enough that there is nothing to compare against.
- The product can coexist with an incumbent in the same stack rather than requiring a rip-and-replace.
- You can focus on small organisations that have no incumbent yet.

## The three friction gates

Run these before choosing anything. Each gate is answered with evidence - a cold run of your own onboarding on a clean machine, a read of the actual signup flow, or account data - not with an opinion.

### Gate 1 - Entry

Can a developer reach first real value with no account, no approval, no credit card and no conversation?

List every mandatory step between "arrived" and "value", and mark each one _required_, _deferrable_ or _removable_.

Steps that reliably cost you people:

- mandatory signup before any output
- credit card before trial
- waiting for a quota or key to be approved
- installing infrastructure
- needing a second person's permission
- needing a colleague to accept an invite

A failing entry gate does not mean the product is bad. It means the motion cannot be pure bottom-up, and the plan must say so instead of pretending.

### Gate 2 - Value

Is the value visible to one developer working alone, or does it only appear once a team or organization uses the product?

Single-developer value supports a pure self-serve motion. Team-scale value (shared dashboards, policy enforcement, cross-service correlation, collaboration) means the developer can _enter_ alone but the purchase is an organizational decision - a hybrid motion, with a champion pack and a human step.

### Gate 3 - Spread

Does ordinary use create a reason for a second developer to see the product? Examples:

- a shared artifact
- a config committed to the repo
- a link someone must open
- a status check on a pull request
- an invite that is the natural next action

Without a spread mechanism, self-serve produces a long tail of single-seat accounts that never expand, and land-and-expand is not available as a strategy - growth has to come from new logos, which is a far more expensive plan and should be priced as one.

## Motion 1 - Bottom-up self-serve

**Money path.** An individual developer adopts, usage grows, they or their team pay by card. No human on the vendor side is ever required.

**Prerequisite.** All three gates pass, and the paid boundary triggers at something an individual or small team hits on their own (volume, projects, environments, retention of data) rather than at governance features only an enterprise wants.

**What it forces you to build.**

- A product that onboards itself.
- Documentation that answers every pre-purchase question.
- Transparent pricing and limits.
- In-product upgrade paths.
- Billing and dunning.
- Per-account usage analytics.
- Self-serve support scaled by docs and community rather than headcount.

**Effort to stand up.** A quarter of product and docs work, no new headcount, largely reversible - the lowest of the four. The ranked comparison across all four motions lives in the skill's step 3; the lines here only feed it.

**Leading indicator.** Share of new accounts reaching first value in the first session, and cohort free-to-paid conversion at account level.

**Failure mode.** Volume without depth: thousands of accounts that never reach production, never add a second developer and never hit a limit. The free surface becomes a cost centre with a good-looking chart.

**Fit signals.**

- Small initial contracts.
- An individual who can spend without approval.
- A product with an observable spread mechanic.
- A category developers already search for by name.

## Motion 2 - Developer-influenced sales (product-led sales)

**Money path.** Developers adopt the free surface; account-level usage crosses a written threshold; a human runs the organization-level deal from a position of evidence.

_The Transition_ splits this motion into two jobs that need different people and different rules; pick one to start rather than blending them.

- **Penetration/expansion** - unifies scattered pods of users inside one organisation into a single contract and adds more pods. Fits multi-player products; Slack's and Zoom's "account managers" are the cited pattern.
- **Conversion assist** - raises conversion of high-value accounts that signed up and never activated. Fits when deal value justifies a human touching an individual sign-up.

**Prerequisite.** Usage can be attributed to an account, _and_ someone exists who can act on the signal within days. Both halves are required; the signal without the responder is telemetry.

**What it forces you to build.**

- Account rollup and identity resolution.
- A qualification rule with owner and response time.
- A champion enablement pack.
- Procurement-ready paperwork (security questionnaire answers, DPA, SLA, invoicing).
- A compensation and territory model that does not reward contacting every signup.

**Effort to stand up.** A quarter to build the rollup and write the rule, then a standing job to answer the signal within the promised window. Reversible on the human side, less so once compensation is tied to it.

**Leading indicator.** Number of accounts crossing the threshold per month, and the share of them contacted inside the promised window.

**Failure mode.** Either extreme: nobody is ever contacted because the rule was never written, or everybody is, which teaches a developer audience that signing up costs them their inbox.

**Fit signals.**

- Value gate is team-scale.
- The paid boundary is made of organization features.
- Deals are mid-sized.
- There is already a base of free accounts with more than one active developer.

## Motion 3 - Top-down with developer proof

**Money path.** An executive, platform team or architecture group buys; developers are then convinced not to route around it.

**Prerequisite.** A budget line that already exists - the buyer funds this category today. Creating a new budget category top-down is a multi-year effort, not a motion.

**What it forces you to build.**

- Business-case material in the buyer's vocabulary.
- Compliance and security evidence up front.
- A rollout and migration plan.
- A genuine developer experience, the part teams skip, because mandated tools that developers hate get quietly bypassed and churn at renewal.

**Effort to stand up.** A standing sales job, plus coordination across product, security and legal before the first contract, and a compliance evidence base that has to be maintained. The highest of the four, and the slowest to unwind once a team is hired against it.

**Leading indicator.** Post-purchase developer activation inside bought accounts: share of licensed developers actually using the product within 90 days.

**Failure mode.** Shelfware. The contract is signed, adoption never happens, and the renewal conversation has no usage to point at.

**Fit signals.**

- Large contracts.
- Mandatory compliance or governance drivers.
- A concentrated market of known accounts.
- A product that replaces an incumbent the buyer already pays for.

## Motion 4 - Ecosystem-mediated

**Money path.** A platform, cloud marketplace, systems integrator, agency or complementary vendor puts the product in front of developers it already reaches.

**Prerequisite.** A partner whose developers already have the problem, and a revenue share or strategic reason the partner accepts. Cloud marketplaces additionally offer buyers a procurement shortcut (committed spend drawdown), which is often the real value.

**What it forces you to build.**

- Partner enablement material.
- A listing that meets the platform's technical bar.
- Support and escalation across the boundary.
- Margin room for the share.

**Effort to stand up.** A quarter of partner and listing work, coordination across an external boundary you do not control, and permanent margin. Slow to reverse: a listing withdrawn or an exclusivity unwound is visible to the partner's customers.

**Leading indicator.** Qualified accounts sourced per partner per quarter, and the share of partners that are active rather than merely signed.

**Failure mode.** Dependency on a partner whose roadmap eventually includes your product, or a signed-partner list where nobody sells anything.

**Fit signals.**

- The product is a component inside a larger workflow the partner owns.
- Buyers already have committed spend on that platform.
- The direct motion cannot reach the accounts economically.

## Combining motions

Run one primary and at most one secondary. The combinations that work in practice:

- Bottom-up self-serve **plus** developer-influenced sales - the standard developer-tool pattern; self-serve creates the base, assisted sales monetizes the accounts that outgrow it. The interface between them is the qualification rule.
- Developer-influenced sales **plus** ecosystem-mediated - partners source accounts, the same qualification and champion machinery closes them.
- Top-down **plus** bottom-up entry - the buyer signs, but a self-serve entry exists so developers adopt willingly rather than under protest.
- **Refuse:** top-down enterprise pricing with no self-serve floor and no free surface. It leaves the entire long tail unservable and hands the developer mindshare to whoever does offer an entry.

## Sequencing by stage

- **Pre-revenue.** One motion. A second before the first is repeatable produces two half-built funnels and no learning.
- **First revenue.** Instrument before adding. The usual second motion is developer-influenced sales layered on an existing self-serve base, because the accounts already exist and only need rollup and a rule.
- **Scaling.** Motions specialize into different owners (product/growth versus sales), and the handoff rule between them becomes the most valuable artifact the company has. Re-read it every quarter; it decays as the paid boundary moves.
