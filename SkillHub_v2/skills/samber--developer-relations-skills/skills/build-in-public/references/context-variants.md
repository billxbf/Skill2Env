# Context variants, stop conditions and objections

The same disclosure decision has different answers depending on who else has a claim on the numbers. This file covers that fork, the documented procedure for deciding when to stop, and the objections a user will raise.

## Contents

- [Who else has a claim](#who-else-has-a-claim)
- [The stop test](#the-stop-test)
- [The reversal wave](#the-reversal-wave)
- [The clone-theft objection](#the-clone-theft-objection)
- [Verifiability and transparency theater](#verifiability-and-transparency-theater)
- [Survivorship bias](#survivorship-bias)

## Who else has a claim

| Dimension                | Funded startup                                                                     | Bootstrapped company                            | Solo maintainer                                                                                         |
| ------------------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Who owns the practice    | Founder plus marketing or DevRel; often a community manager                        | Founder, sometimes with one marketing hire      | The maintainer, personally                                                                              |
| Review before publishing | Legal and comms review; board and investor sensitivity                             | Founder's discretion                            | None                                                                                                    |
| Revenue disclosure       | Generally not available                                                            | Common, and treated as a channel                | Rare; sponsorship totals more often than income                                                         |
| What gets shared instead | Culture, hiring, engineering process, fundraise news                               | Revenue, churn, roadmap, mistakes               | Changelogs, roadmaps, RFCs, release notes                                                               |
| Primary goal             | Recruiting, employer brand, category credibility                                   | User acquisition, credibility, audience as moat | Contributors, sponsorship, adoption                                                                     |
| Characteristic failure   | Competitive leak; narrative anchored to a founder who may leave; investor friction | Copycats; the stress of live numbers; burnout   | Entitlement from unpaid users; burnout; conflating code transparency with personal-finance transparency |

**Why funded companies usually cannot publish revenue.** Standard investor rights agreements grant information rights and impose confidentiality on company financials, which makes revenue disclosure a legal question before it is a marketing one. Gumroad's Sahil Lavingia is the documented exception - a venture-backed founder who published detailed financials and recorded public board meetings - and it followed an explicit strategic pivot away from growth-at-all-costs. Treat it as an exception that required renegotiating expectations, not a template.

**Why bootstrapped companies can treat revenue as a channel.** Plausible Analytics published "How we built a $1M ARR open source SaaS", with a timeline of milestones after launching paid subscriptions in May 2019:

- 324 days to reach the first $400 MRR
- nine months to go from $400 to $10,000 MRR
- $1M ARR reached on 2 June 2022

Arvid Kahl credits transparent revenue sharing with helping sell FeedbackPanda.

**Why the solo-maintainer case is a different axis entirely.** Transparency about code is already the OSS norm and contributors expect it. Transparency about the maintainer's own time and money is not, and it changes the relationship: published income invites entitlement ("you make this much, fix my issue").

GitHub reports more than $100 million routed to maintainers through Sponsors since 2019, across over 70,000 maintainers, while still describing the funding gap as enormous and maintainer burnout as one of the biggest supply-chain risks. Artem Sapegin's "Why I quit open source" is the counter-narrative worth reading before assuming visibility converts to funding.

## The stop test

There is no rigorous, widely adopted framework for choosing a disclosure level - this is a genuine gap in the practitioner literature, not something to paper over with a confident-sounding checklist. The closest thing to a documented procedure is Damon Chen's essay "The golden era of being an open startup is gone", which gives four stop conditions:

1. Larger companies belittle you once they know your numbers are small.
2. It raises copy and clone risk.
3. Above some threshold it stops inspiring anyone and starts reading as bragging.
4. It stops being a personal milestone once other people are on the team.

Chen's own case demonstrates the fourth directly: he stopped because "with someone else on my team, it's no longer my personal milestone anymore." Jon Yongfook articulated the underlying curve in 2022: the higher your open revenue, the fewer people it benefits and the more risk you take on.

Use the test the way it was written - as a stop condition set before starting, recorded in the charter, so the decision to stop is a pre-commitment rather than a reaction to a bad month.

## The reversal wave

Between 2022 and 2024 a large share of the practice's most visible practitioners withdrew revenue disclosure. This is the strongest evidence available on how the decision actually plays out.

- **Jon Yongfook (Bannerbear)** removed public revenue and his live MRR Twitter-bio bot on 5 February 2024: "when your numbers are live for the world to see, the level of stress and dread is amplified 10x. You feel like you're a failure and everyone can see it." The page now says the company shares only selected metrics.
- **Danny Postma** (January 2024) listed his reasons: bragging, competitive disadvantage, personal safety, damaged relationships, and numbers that don't tell the full story.
- **Pieter Levels** removed his open pages in late 2022, citing security.
- **Tony Dinh** removed his public revenue bar in October 2022 on personal-safety grounds. He has also defended revenue sharing at other times - a nuanced case, not an opponent.
- **Damon Chen** removed his revenue bar in October 2022 and wrote the essay above.
- **Francesco Di Lorenzo (Typefully)** stopped and then resumed in January 2024, once the product was solid and pricing had raised the barrier for copycats. The only documented reversal of a reversal.
- **Buffer did not reverse.** The pioneer that started the pattern in 2013 with open salaries still publishes revenue, salaries and support metrics. Cite it whenever someone concludes the practice is discredited.

Yongfook also reported that going dark was itself stressful. Reversal is a second public event, not a neutral reset - which is the practical argument for starting narrower than feels natural instead of planning to widen later.

## The clone-theft objection

The dominant practitioner rebuttal is that execution beats ideas - the Rework line "competitors can never copy the you in your product" is the usual citation, and KP reframes the fear as a readiness test rather than a risk assessment.

The objection is not imaginary, though. Baremetrics reported roughly a dozen copycat businesses. Sebastian Röhl (HabitKit) posted on 3 February 2024: "Every time I post a MRR chart, a whole bunch of new habit trackers with a very similar concept to @HabitKit pop up. At what point would you stop sharing your numbers?"

On the other side, Wise published a full public roadmap in May 2021 and succeeded anyway, at real scale.

**The 2026 reassessment is the part that changes the advice.** Arvid Kahl, writing in 2026: "Building in public once helped me sell my company. Today, that same transparency could destroy yours." His argument is that agentic coding tools turn a publicly described architecture and feature set into a working competitor in days, and that "the old safety threshold of $20-30K MRR has collapsed to zero." A counter-analysis argues the real barrier was always getting strangers to trust the clone, so distribution and trust remain the moat regardless of build speed.

Both positions point at the same working rule: assume the visible surface can be cloned quickly, and compete on distribution, trust and switching costs.

- Share the journey and the reasoning behind decisions.
- Keep the operational playbook, the exact architecture and the specific growth levers out of public writing.

Describing what you built is safe. Describing precisely how it wins is not.

## Verifiability and transparency theater

Fear of disclosure plus appetite for social proof produces a predictable distortion: fabricated numbers. Screenshot-faking services exist, and a verified-revenue product (TrustMRR, launched 31 October 2025 after a viral post about fake MRR screenshots) exists as the market's countermeasure. The consequence for anyone publishing real numbers is that proof now beats polish - a bare screenshot reads as more likely fake than impressive, so publish from a source the reader can verify or don't publish the number.

## Survivorship bias

The visible winners of this practice obscure a much larger mass of quiet failures. Named skeptics:

- Jason Leow - "Building in public is overrated... It's just ONE tool amongst many"
- Krzysztof Kowalczyk - on the survivorship framing of the movement's most-cited success stories
- Arvid Kahl - on himself, that building in public "is a performance... artificial and strategic."

Leow's specific warning is the useful one to pass on: newcomers "build in public, tweet daily, and burn out because of low returns on that investment in time and energy, when the channel-offer fit isn't there." Channel-offer fit, not effort, decides whether it pays.
