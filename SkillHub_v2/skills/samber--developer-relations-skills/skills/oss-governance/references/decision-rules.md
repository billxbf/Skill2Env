# Decision rules

Turning a governance model into rules with numbers: decision classes, mechanisms, thresholds, timers, and clauses to paste and edit.

## Decision classes

Define rules per class, not per situation. The minimum set:

| Class                          | Typical decider           | Typical mechanism                        |
| ------------------------------ | ------------------------- | ---------------------------------------- |
| Routine change                 | any maintainer            | lazy consensus + review requirement      |
| Breaking change / scope change | maintainers               | consensus-seeking, written proposal      |
| New maintainer                 | maintainers               | nomination + vote or no-objection window |
| Maintainer removal             | maintainers               | supermajority vote                       |
| Release                        | release owner             | majority approval, no veto               |
| Security response              | security responders       | private, delegated authority             |
| Money and brand                | council / committee       | vote, minutes published                  |
| Governance amendment           | maintainers or electorate | supermajority + long window              |

A class the project cannot assign a decider to is the finding - write that rule before anything else.

## Mechanisms

**Lazy consensus** - announce the intent, state the window, proceed if nobody objects. The cheapest mechanism that still leaves a record, and the right default for most decisions. Not for decisions where review is mandatory before merging, and never for irreversible actions (a release, a key rotation, a removal).

**Consensus-seeking** - pursue agreement, accept that unanimity is not required, let a reasoned objection block until it is addressed or overridden. Its failure mode is the unbounded thread, so every consensus-seeking rule needs a timer and a named body that can end the discussion.

**Voting** - rarer than most drafts assume (Fogel's last-resort position is in the evidence base). Write the thresholds anyway, since they make the last resort usable, but specify them precisely:

- Who is binding.
- The threshold (simple majority, two-thirds of _all_ existing maintainers, or consensus approval).
- Quorum.
- Minimum open period.
- Whether abstentions count in the denominator - that last ambiguity is where governance arguments actually happen.

**Justified veto** - a blocking objection must carry a technical justification. An unjustified veto carries no weight. The single most useful clause to import: it converts "I don't like it" into an argument that can be answered.

**Delegation** - an area owner, working group or security team decides inside a named scope without returning to the full body. Write the scope and the report-back expectation, or delegation is indistinguishable from drift.

## Reference numbers

Published windows, thresholds and terms are listed with their owners in the evidence base. Quote them from there rather than restating them as a standard, and adjust every one for community size and timezone spread. The aging rule on approvals - two approvals to merge, dropping to one once a change has sat a week - is the single most useful import for a small project, because it stops a two-maintainer repository stalling when one is away.

## Example clauses

**Good - bounded, testable, escalatable**

> Changes to public API behaviour require a design proposal, a 10-day comment period, and approval by two maintainers with no unresolved objection. An objection must state a technical reason. If an objection remains unresolved after 30 days, any maintainer may refer the proposal to the maintainer council, which decides by simple majority.

**Bad - unbounded and unenforceable**

> Significant changes are discussed by the community until consensus is reached. The maintainers will consider all feedback and make the best decision for the project.

"Significant" is undefined, "consensus" has no test, there is no clock, nobody is named. It cannot be violated, so it cannot be relied on.

**Good - promotion criteria a candidate can self-assess**

> A contributor may be nominated as maintainer after six months of sustained participation, including at least ten merged non-trivial pull requests and at least twenty substantive reviews. Any maintainer may nominate; the nomination passes if no maintainer objects within seven days, otherwise it goes to a simple-majority vote.

**Bad** - "Maintainers are added when the existing maintainers feel someone is ready." A contributor cannot act on this, so nobody applies and the pool never grows.

## Written proposal processes

Adopt one when decisions get re-litigated or knowledge lives in calls and chat. Keep it cheap:

- A template with motivation, goals and non-goals, design, alternatives and open questions.
- A status vocabulary (`proposed`, `accepted`, `deferred`, `rejected`, `withdrawn`, `replaced`).
- A comment period.
- A stated disposition from the deciding body.

Two properties matter more than the format: the artefact is public and durable, and acceptance is explicit rather than inferred from silence.

Set the trigger narrowly: proposals for substantial changes only (semantics, removals, new public surface) keeps the process alive; requiring them for everything kills it in a month. An accepted proposal is a decision, not a commitment that anyone will implement it.

## Escalation and deadlock

Beyond step 3's rule that escalation costs a label rather than a confrontation, name the escalation body: a council, a committee, or a named tiebreaker on a two-person project. Bound it, so it decides within a stated period; a decision not taken by then defaults to the status quo. Record the outcome where the discussion happened.

Handle conflicts of interest up front: anyone employed by a party to the dispute recuses, with a named fallback for when that leaves no quorum. Conduct cases never travel this path: they belong to the code-of-conduct process, in private, with the accused excluded.

Six projects publish ladders that get used. Each names who holds the final call and what it excludes. Pick the one whose shape matches the project rather than assembling a hybrid.

| Project | Final authority                                         | Threshold or mechanism                                                                                                                        | Explicitly out of scope                                        |
| ------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Apache  | the project management committee                        | a justified -1 vetoes a code change and cannot be overridden; the committee judges whether the justification is technical                     | releases and procedural votes cannot be vetoed                 |
| Node.js | the technical steering committee                        | consensus-seeking; a member may call a closing vote, which itself needs majority approval to happen; a label puts a stuck issue on the agenda | anything already settled by consensus                          |
| Rust    | per-team decision, council above it                     | a registered concern during the final comment period blocks the merge until resolved                                                          | most technical calls stay with teams                           |
| Python  | the steering council                                    | court of final appeal once every other route has failed                                                                                       | anything a delegate can still decide                           |
| Debian  | the technical committee, then a project-wide resolution | the committee may direct a developer against their wishes on a 3:1 majority                                                                   | disputes the parties have not first tried to settle themselves |
| Go      | a named individual arbiter                              | proposals with no consensus are declined; unresolved ones sit in a hold state rather than being force-closed                                  | nothing - the arbiter is the ceiling                           |

One rule underlies all six: a proposal that cannot reach agreement gets _declined_ or _held_ explicitly, because an issue left open forever is a decision nobody can appeal.

The prompt to formalize is behavioural: when the same dispute recurs and nobody can point to a written appeal path, write one. Every ecosystem that built its ladder only after the crisis reports the same thing afterwards - the structure that stuck was the simplest workable one, not the most sophisticated.
