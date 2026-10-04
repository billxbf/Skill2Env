# Hypothesis conversion - worked examples

The hypothesis step is what separates a pipeline from an archive. Every research session ends with 5-8 written hypotheses in this exact format:

> We believe **[change]** will produce **[outcome]** because **[insight]**.

The insight must cite the file: which competitor, which signal, what corroboration, and what is missing from the user's own account. An insight without a receipt does not enter the list.

## Ranking method

Rank by value returned per unit of production effort. Two axes carry value - how strong the signal is, and how absent the angle is from the user's own account - and one carries effort. Weight them:

`signal strength == gap in own account > ease of production`

The two value axes tie because neither is usable alone: a well-corroborated angle the user already runs teaches nothing, and an untested gap with no signal behind it is a guess. A hypothesis has to score on both before ease of production is even consulted.

Score each hypothesis 1-3 on all three:

| Axis                        | 1                                 | 2                                       | 3                                                      |
| --------------------------- | --------------------------------- | --------------------------------------- | ------------------------------------------------------ |
| Signal strength (value)     | longevity only, uncorroborated    | longevity + one corroborating signal    | longevity + 2+ signals, or cross-competitor repetition |
| Gap in own account (value)  | angle already tested recently     | angle tested long ago or half-heartedly | angle never tested                                     |
| Ease of production (effort) | needs a shoot, creator, or rights | needs design or editing time            | can ship this week from existing assets                |

Band on the two value axes summed, then order within each band by ease of production, cheapest first. Ease never promotes a hypothesis into a higher value band. The one exception is a hard delivery date from the interview - that answer legitimately puts a shippable-this-week hypothesis ahead of a better-evidenced one that needs a shoot.

Take the **top three** into briefs. Keep the rest in the file with `test_status: hypothesized`: they are next session's starting bench.

Strike, rather than bench, any hypothesis the user's constraints make permanently unproducible:

- No route to creator rights.
- A claim their category forbids.
- A channel they will not enter.

Record it as deleted with the constraint that killed it, so it does not inflate the pipeline gate or reappear as scope next session.

What this ranking starves is the well-evidenced hypothesis that needs a shoot: it tops both value axes, scores 1 on ease, and the near-date exception keeps pushing it out of the top three. Promote it once it has survived two consecutive sessions in the top band, or when the interview answer was a compounding asset - the shoot also produces the footage the rest of that family reuses.

The ordering is a default, not a law, and it moves with who executes it.

- An in-house editor or a retained creator flattens the ease axis until signal strength decides alone.
- A team with no production capacity has to lead with what it can actually ship.

Re-rank against everything the file already knows about the user before presenting the list.

## Worked session - B2C example (fictional skincare brand, 3 direct competitors, 71 ads pulled)

Observations synthesized:

- Two competitors have run question-hook UGC videos 35+ days with multiple concept variants.
- All three lead with before/after statics at BOFU.
- Nobody in the category addresses the "sensitive skin" objection.
- The user's account has only tested statement hooks and product-shot statics.

| #   | Hypothesis                                                                                                                                                                                                                                                 | Signal | Gap | Ease | Value | Rank |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --- | ---- | ----- | ---- |
| H1  | We believe a UGC video opening with a question hook will beat our current product-shot statics on cold traffic, because both closest competitors have run question-hook UGC for 35+ days with 3+ variants each, while we have only tested statement hooks. | 3      | 3   | 2    | 6     | 1    |
| H3  | We believe adding a before/after static to our BOFU retargeting will lift conversion, because all three competitors run the format there continuously and we never have.                                                                                   | 3      | 3   | 2    | 6     | 1    |
| H2  | We believe an ad addressing the sensitive-skin objection head-on will open an underserved segment, because no competitor in the pulled set addresses it despite it dominating category reviews.                                                            | 2      | 3   | 3    | 5     | 3    |
| H6  | We believe a countdown/urgency hook will underperform in this category, because two competitors launched and dropped urgency concepts within two weeks - worth one cheap disconfirming test.                                                               | 2      | 3   | 3    | 5     | 4    |
| H4  | We believe a proof-first hook citing our review count will beat our curiosity hooks at MOFU, because the largest competitor duplicated its proof-first concept into 5 variants last month.                                                                 | 2      | 2   | 3    | 4     | 5    |
| H5  | We believe a "morning routine" day-in-the-life concept will hold attention longer than our current demo video, because an adjacent-vertical import shows the concept running 60+ days in a neighboring category.                                           | 1      | 3   | 2    | 4     | 6    |

The axes disagree, so read all three:

- value: `H1 == H3 > H2 == H6 > H4 == H5`
- effort (highest first): `H1 == H3 == H5 > H2 == H4 == H6`
- efficiency: `H1 == H3 > H2 > H6 > H4 > H5`

Every tie here is a scoring tie, identical cells in the table above, not a refusal to choose - each one gets broken by what the score could not see:

- **H1/H3** breaks toward H1: both are untested formats with strong signal, but H1's insight names two competitors and H3's names a format all three run, which is weaker evidence of a _winner_.
- **H4/H5** breaks toward H4 on signal quality, since H5's only evidence comes from an adjacent vertical.
- **H2/H6** breaks toward H2 because its payoff is a new segment while H6's is only learning. H6 stays as a cheap disconfirming test if capacity allows.

Top three forward: H1, H3, H2. Note that neither ranked first on effort: the two value axes put H1 and H3 in the higher band despite each needing editing time.

Hand the top three to `mbfinotti/advertising-skills@ad-creative-brief`, then `mbfinotti/advertising-skills@ad-creative-test-plan`.

Had this team answered the interview with a delivery date two weeks out, H2 and H6 would lead instead: both ship from existing assets, and a date that near is the one condition under which effort promotes a hypothesis across a value band.

Note H3's compliance flag when briefing: before/after claims are regulated in health, finance, and beauty - the brief must carry substantiation.

## B2B variant of the same move

B2B hypotheses lean on angle and audience rather than volume, and can use EU-exposed targeting as the insight:

> We believe a comparison-angle ad aimed at IT decision-makers will out-produce our generic demo ad, because our main competitor has targeted "IT decision-makers, 200+ employees" in three EU markets for 6+ weeks with a comparison angle, and our account has never run one - while our own targeting reaches the same committee role.

The format, ranking, and top-three rule are identical to B2C.

## Negative example - what a hypothesis must not look like

> ~~We believe copying CompetitorX's video will work because their ads are great.~~

Three failures:

- The change is reproduction rather than adaptation, which is an IP problem before it is a creative one.
- "Their ads are great" is opinion, not a signal with a threshold.
- No outcome is stated, so the test can never be judged.

Rewrite it as an adaptation of the _angle_ with a cited signal and a measurable outcome, or drop it.
