# Risk and Dependency Screens

Risk feeds the ranking as scores and gates - never a downstream compliance annex read after the decision.

## Must-pass gates (pass/fail, outside the score)

A gate failure removes the candidate regardless of composite score. Each gate decision cites its evidence in the memo.

Gates are never ranked against each other on value - every one of them is pass/fail, and a gate that can be skipped for being low-value is a scorecard criterion in disguise. Only their run order is ranked, by what each costs to check:

- check effort: `legal/antitrust == security attestation == creator fraud > exit path == three-laws > financial viability` - the top three tie because each is a week on somebody else's calendar: counsel review, a TPRM questionnaire, a paid audience audit. Exit path and three-laws tie one rung below because each needs a short artifact drafted before it can be judged at all - a contract sketch, a JVP sketch - an hour or two of your own time. Financial viability sits lowest on its own: funding history, layoffs and filings read off public sources in minutes.
- Run them in the reverse of that order: desk gates across the whole longlist first, the week-long reviews only on survivors. The staged default and its compliance trade-off are in SKILL.md § Method choices.

| Gate                        | Fails when                                                                                                                                              | Evidence to check                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Financial viability         | Credible risk the candidate folds or is fire-sold inside the alliance horizon                                                                           | Funding history, layoffs, filings, churn signals           |
| Security/compliance posture | Candidate cannot meet the data-sharing bar the alliance needs (SOC 2 / ISO 27001-class attestations, TPRM questionnaire)                                | Attestation status, breach history                         |
| Legal/antitrust exposure    | Exclusivity or data terms create regulatory or IP exposure                                                                                              | Counsel review of proposed terms                           |
| Brand safety (B2C)          | Unresolved brand-safety flag, active controversy, values conflict                                                                                       | Vetting report, press scan                                 |
| Creator fraud (B2C)         | Fake-follower or engagement-fraud share above the stated tolerance                                                                                      | Audience audit from a fraud-screening tool                 |
| Three-laws screen           | The combination fails any of Gomes-Casseres's laws: creates no value beyond standalone, cannot operationally act as one, or has no workable value split | JVP draft, integration feasibility, commercial term sketch |
| Exit path                   | No plausible wind-down without stranding customers                                                                                                      | Contract sketch, data-portability check                    |

## Relational vs performance risk (Das & Teng)

Score both, separately, per candidate - they are different failure modes with different mitigations:

- **Relational risk** - the partner behaves opportunistically or stops cooperating. Raised by: competing roadmaps, asymmetric dependence, no prior ties, misaligned incentives. Mitigated by governance and staged commitment, not by enthusiasm.
- **Performance risk** - everyone cooperates and the alliance still misses its objectives. Raised by: unproven market, hard integration, weak joint value proposition. Mitigated by pilots and milestone gates.

A candidate high on both is a kill or a small staged pilot - never a flagship bet.

## Ecosystem dependency risk (Adner's Wide Lens)

Two risks standard scorecards miss entirely; ask both questions per candidate:

- **Co-innovation risk** - does joint success require the candidate (or a third party) to build something that does not exist yet? Score how much of the value depends on someone else's unshipped roadmap.
- **Adoption-chain risk** - must intermediaries (the candidate's sales force, resellers, retailers, platform reviewers) adopt before the end customer ever sees the value? Every unwilling link discounts the expected value.

Sketch the value blueprint for top candidates: every actor whose action is necessary for the customer to get the value. A blueprint with three dependent actors you cannot influence is a materially riskier alliance than its scorecard suggests.

## Platform-envelopment risk (Eisenmann, Parker & Van Alstyne)

For any candidate whose platform you would build on, score the risk of being commoditized by the partner you are joining: the platform owner can absorb your functionality by bundling it, or quietly re-rank and substitute you even while technical access stays open.

Warning signs:

- The platform ships adjacent first-party features.
- Its marketplace terms allow self-preferencing.
- Your value sits in a thin layer it could replicate.

High envelopment risk does not forbid the alliance. It demands staged commitment, contractual safeguards, and a stated dependency ceiling in the memo.

## B2C-specific screens

- **Reputational contagion** - consumer attitudes toward a brand pairing spill over onto each partner, and not symmetrically (Simonin & Ruth, 1998); a co-branding meta-analysis found high-esteem brands are the most exposed to dilution. Model at least one negative-spillover scenario per shortlisted candidate: partner scandal, product failure, values controversy - and what it costs you.
- **Creator fraud vetting** - run as pass/fail before any scoring. Screen for fake followers, engagement pods, bot activity, undisclosed past controversies. One investigative firm reports roughly one in four vetted influencers carried significant risk flags (vendor-reported figure - treat as directional). Demand incrementality-tested metrics, not vanity reach.

## Feeding risk back into the rank

Fold the scored (non-gate) risks into a risk composite per candidate and show it beside the value and effort columns. Two candidates with equal expected value and different risk composites are not tied - say which risk drives the gap and what mitigation would close it.
