# Published findings on open source strategy

Contents: strategy sources · empirical studies · company-published mechanics · reversal record · operating guidance.

What each source establishes and - the part that matters more - what it does _not_ prove. Cite the source when you use its claim, and drop the claim rather than upgrading it when the user needs something the source cannot carry.

Three labels appear below:

- **Sourced**: traceable to a named author, company page or peer-reviewed paper
- **Via trade press**: a publication reporting what a company or founder said, directionally reliable, not quotable as that company's own words
- **Self-set**: a baseline, never an industry standard

## Strategy sources

- **Joel Spolsky, _Strategy Letter V_ (2002)** - "demand for a product increases when the prices of its complements decrease", with IBM's PC add-in cards, Microsoft's non-exclusive PC-DOS licensing, Netscape's browser, Transmeta hiring Torvalds and Sun/HP funding GNOME as examples, and Sun's Java as the counter-example. _Sourced._ Does not prove commoditization works reliably; it is a strategic argument with selected illustrations, not a study.
- **Dirk Riehle, _The Innovations of Open Source_** - the cost-sharing motive, the block-a-competitor motive (Linux against Windows, Eclipse against Visual Studio) and the differentiating-versus-context split, illustrated by a distributor keeping test suites, configuration databases and compatibility matrices closed while the code is open. _Sourced._ An analytical framework, not measured outcomes.
- **Geoffrey Moore, core versus context** - the same cut in general-management vocabulary. _Sourced as terminology._ Adds a vocabulary, not evidence.
- **Adam Jacob, "The war for the soul of open source", OSCON Portland 2019** - the strongest available argument _against_ boundary-drawing: the value sits in the totality of the product, not in a proprietary sliver. _Sourced._ Use it as the steelman when a user is set on open core, not as a prediction that open core fails.
- **David Cramer (Sentry), "Open Source is not a Business Model"** - founders face a practical binary: AGPL deters competitors but scares some customers, MIT protects nothing, so many choose closed source and the technology is never adopted. _Sourced._
- **Chad Whitacre (Sentry), the Fair Source essays** - open source as a distribution and development model rather than a business model; licensing terms limit which business models are available at all. _Sourced._
- **Stephen Walli (Microsoft), "There is NO Open Source Business Model"** - open source as engineering economics, argued in a slide deck. Delivered at LinuxCon + ContainerCon + CloudOpen China, Beijing, 19 June 2017 (session schedule listing; SlideShare listing, 65 slides, matches).

## Empirical studies

- **Henkel (2006), Research Policy 35(7)** - firms in embedded Linux reveal on average about **half** the code they develop, with strong heterogeneity across firms. _Sourced._ Use it as a base rate that makes "how much" a legitimate question; it does not prescribe a target, and it is one industry at one point in time.
- **Henkel, Schöberl & Alexy (2014), Research Policy 43(5)** - customer demand pull is the _initial trigger_ for selective revealing, followed by a positive feedback loop, with openness becoming a dimension of competition. _Sourced._ Supports treating demand pull as a first-class motive; does not say externally triggered decisions turn out better.
- **West & Gallagher (2006), R&D Management 36(3)** - four firm strategies for engaging open source: pooled R&D, spinouts, selling complements, attracting donated complements. _Sourced._ Commoditize-your-complement is one of four, not the general case.
- **West & O'Mahony (2008), Industry & Innovation 15(2)** - across twelve corporate-initiated projects, sponsors offered _transparency_ far more readily than _accessibility_. _Sourced._ The sharpest available diagnostic for "we open sourced it and nobody came"; it explains a gap, it does not quantify how much accessibility is enough.
- **O'Mahony (2007), Journal of Management & Governance 11(2)** - five principles of community-managed governance and how hybrid corporate/community models differ. _Sourced._ Useful for stating what a company gives up under community governance.
- **O'Mahony & Karp (2022), Strategic Management Journal 43(3), "From proprietary to collective governance: How do platform participation strategies evolve?"** - across four governance phases of one platform, participation rose as access widened and fell again once governance turned ambiguous; leadership passed to outsiders only under structured, collective governance. _Sourced (published abstract; full text paywalled)._ Extends gate 4 into a standing check, not a one-time pass. One platform, one trajectory - no general timeline or maturity bar.
- **Linåker, Munir, Wnuk & Mols, the CAP model (arXiv 2208.00308)** - the one industrial, artifact-level decision model with a documented instantiation (Sony Mobile): two axes, four quadrants, a dominant objective per quadrant, a cross-functional governance board, and the enabler-versus-differentiator split inside one asset. _Sourced._ The same paper validates the quadrant classification at three further, anonymized firms (agriculture-tech, mobile games, telecommunications), so the classification itself rests on four organizations across four industries, though only Sony Mobile is named; the model's own authors note it does not capture how fast an artifact drifts from differentiating to commodity, which is why they recommend re-running the evaluation each planning cycle.
- **Henry Chesbrough (2003), _Open Innovation_ (Harvard Business School Press), excerpted as "The Logic of Open Innovation," _California Management Review_ 45(3), Spring 2003** - Open Innovation firms profit from others' use of their IP and buy others' IP, rather than relying on controlling it. _Sourced (read directly)._ The base model West & Gallagher and the CAP model build on, and gate 3's grounding for treating the business model, not the license, as the value-capture mechanism. General R&D and IP management, not open source licensing, and predates open-core SaaS.

## Company-published mechanics

- **GitLab stewardship page** - eleven promises, the buyer-persona test, reverse-direction acceptance criteria, and the 2020 audit moving eighteen features across seven DevOps stages into open source. **GitLab pricing handbook** - the decision matrix in which the CEO decides. _Sourced from the company's own handbook._ One company's model; the promises are unusually strong and are not an industry norm.
- **Google open source release approval documentation** - the manager-owned strategy call, escalation to director or VP, parallel licensing/patent/privacy review, published rejection criteria, approve-by-default posture. _Sourced._
- **HashiCorp (2023-08-10), Elastic (Banon, 2024-08), Confluent (2018-12), Red Hat (McGrath, 2023-06-26)** - each company's own stated reason for its boundary. _Sourced from company or founder blogs._ These are positioning statements; treat the reasoning as sincere but self-serving.
- **Chef (Adam Jacob) and Mercedes-Benz (FOSS Manifesto)** - Sourced via trade press coverage of founder statements.
- **caniszczyk/rugpulls.dev** - a maintained dataset of relicensing events with dates and announcement URLs, including MongoDB's 2018 AGPL-to-SSPL move and Grafana's 2021 Apache-to-AGPL move. _Sourced dataset._ Use it instead of re-deriving a timeline.

## Reversal record

The six reversal cases this skill cites are each sourced to a company blog, LWN or trade press. What they collectively support: the reputational cost concentrates at the reversal, forks appear in days, and governance surprise costs even when no code is withdrawn.

What they do **not** support: that any particular initial scope prevents a reversal. The steelman for the opposite reading is that initial scope determines whether a community forms at all, and a project nobody adopts never generates a reversal event - so scoping is still causally prior. Both readings are defensible; say so rather than picking one silently.

## Operating guidance

- **TODO Group** - the open source program office definition and function set, the staffing picture, inbound and outbound policy structure, the upstream-first rule ("submit patches upstream first, and consume in your own products downstream"), engagement triage, and the foundation-membership band of **$5,000–$250,000+ per year**. _Sourced, but the membership band carries no publication date in the guide and membership pricing moves_ - treat it as an order of magnitude, and check the target foundation's current schedule before putting a number in a budget.
- **TODO Group, measuring open source program success** - the caution from a named Oath/Yahoo open source director that data gets collected because it is available, not because it answers the question. _Sourced._
- **Linux Foundation / TODO, "Business Value of the OSPO"** - Spotify spinning successful open source projects into separate business units with commercial products, the closest thing to a per-project success criterion from a named company. _Sourced._
- **CHAOSS** - adopted by Red Hat's open source office as its definition of community health. _Sourced._ Measures health, not strategic return.
