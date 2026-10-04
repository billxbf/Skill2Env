# Strategic motives for opening company code

Contents: the eight motives · evidence each demands · signal each is measured on · how much to open · combining motives · motives that are not motives.

A motive is not a slogan. Each carries an evidence test the company passes out loud and a signal deciding whether it worked. A failed evidence test makes the motive decoration; the asset needs a different reason or stays closed.

Motives 1-7 are chosen internally. Motive 8 is imposed from outside and is the more common trigger - not a lesser case.

## 1. Commoditize your complement

**Claim.** Joel Spolsky, _Strategy Letter V_ (2002): "demand for a product increases when the prices of its complements decrease". Push a complement of what you sell toward commodity pricing and demand for your product rises, letting you hold price.

**His examples**: IBM's documented PC add-in cards, non-exclusive PC-DOS licensing, Netscape's giveaway browser, Transmeta hiring Torvalds, Sun and HP funding GNOME. His counter-example from the same essay is Sun's Java, which commoditized _hardware_ - the wrong complement for a company selling hardware.

**Evidence test.** Name the product whose demand rises, and name the complement being opened. If the two are the same thing, this is not the motive.

**Signal.** Growth in the paid product, not adoption of the opened complement. Adoption is the mechanism, not the outcome.

## 2. Cost sharing

**Claim.** Several organizations jointly fund a component none of them differentiates on, usually under a foundation, instead of each maintaining a private fork (Dirk Riehle, _The Innovations of Open Source_).

**Evidence test.** Name at least one other organization with a reason to co-fund, and say what happens if none shows up. A "shared" project with one contributing vendor is single-vendor open source with extra process.

**Signal.** External contributor organizations, and engineering hours displaced from the private fork.

## 3. Block a competitor from owning a standard

**Claim.** Open a component so a rival cannot make it a proprietary chokepoint. Riehle's framing of Linux against Windows and Eclipse against Visual Studio: commoditize before you are commoditized.

**Evidence test.** Name the competitor and the chokepoint. Defensive standard-setting also demands neutral governance sooner than the company usually wants - a standard nobody else can influence is not a standard.

**Signal.** Adoption by parties who are not your customers, and the competing proprietary component's loss of default status.

## 4. Market creation

**Claim.** Non-software companies fund and open components they operationally depend on, growing a supplier and talent ecosystem that did not previously exist.

**Evidence test.** Name who is supposed to build on it and what they get. This motive has the longest payback of the eight; commit to a multi-year horizon or pick another motive.

**Signal.** Third parties shipping products or services that depend on the component.

## 5. Talent

**Claim.** TODO Group: working publicly recruits people who already know the project, and contributors are a pre-qualified hiring pool.

**Evidence test.** The asset has to be work an engineer would want to be seen doing. A build script nobody would list on a CV recruits nobody.

**Signal.** Candidates who cite the project, contributor-to-hire conversions, and retention of the engineers who maintain it. Tolerates a small, well-run project - it does not need ecosystem scale.

## 6. Trust and auditability

**Claim.** Buyers, auditors and security teams can read the code instead of trusting a claim. Strongest for security, cryptography, privacy and agent/automation surfaces where "trust us" is expensive.

**Evidence test.** Point to a deal, an audit or a compliance review where the source was actually asked for. Otherwise this is a second-order benefit of opening, not a reason to open.

**Signal.** Security reviews passed faster, procurement objections removed, third-party audits published.

## 7. Lower maintenance through upstreaming

**Claim.** TODO Group's upstream-first argument: a private patch is re-paid at every upgrade; an upstreamed patch is maintained by the project. Applied to a company's own code, opening converts private maintenance into shared maintenance.

**Evidence test.** Shared maintenance only arrives if other maintainers do. Estimate the first two years as _added_ cost - review, releases, issue response, security reports - and check the motive still holds if no external maintainer ever appears.

**Signal.** External commits landing without company review time, and the fraction of the maintenance load carried outside the company.

## 8. External demand pull

**Claim.** The decision is triggered from outside - a customer, a platform owner, a regulator or a standards body requires it - rather than chosen in a vacuum. Henkel, Schöberl and Alexy (2014) found customer demand pull to be the _initial_ trigger for selective revealing, followed by a positive feedback loop in which openness becomes a dimension of competition.

**The clearest documented case** is the Sony DRM plug-in in step 2. In CAP-model terms it is a _bottleneck_ artifact: negative business impact if absent, no positive impact if present.

**Evidence test.** Name the party imposing the requirement and what happens if the company refuses. A customer _asking_ is not demand pull; a customer conditioning a renewal on it is. If refusal costs nothing, the real motive is somewhere in motives 1-7.

**Signal.** The requirement satisfied, the deal or certification obtained, and the share of the resulting maintenance carried by the other parties subject to the same requirement.

**The trap.** A forced decision still has to pass the value-capture and ownership gates. Companies open something under customer pressure, skip the ownership question because the deal was the point, and end up with an unmaintained repository that the customer then complains about.

## How much to open

Henkel's 2006 study of embedded-Linux firms found they reveal on average about **half** the code they develop, with wide variation. A base rate from one industry at one point in time, not a target. Its real use is to reframe the question: the unit of decision is a _fraction of a codebase_, not a binary per-project verdict, and a company opening 5% or 95% should say why its situation differs from the middle.

West and Gallagher (2006) add four distinct firm strategies - pooled R&D, spinouts, selling complements, attracting donated complements - of which commoditize-your-complement is one. Check which the company is running before assuming the complement logic applies.

## Combining motives

Rank them; do not average them. One primary motive decides the line and the measurement; secondary motives are welcome side effects. A brief that lists four co-equal motives has not made a decision, and its measurement plan will contradict itself - talent and commoditization, for instance, disagree about whether small-and-well-run beats large-and-adopted.

## Motives that are not motives

- **"Our competitors did it."** Their line served their value capture, which you probably cannot see.
- **"The team wants to."** Real as retention pressure, not as strategy. Route it into the talent motive or into a sanctioned contribution policy instead.
- **"It's not core anyway."** Not-core is an argument for _not keeping it closed_, not an argument for paying the cost of running it in public.
- **"To get free contributors."** The strongest form of the maintenance motive, and the one that fails most often - most published repositories never receive an external contribution.
