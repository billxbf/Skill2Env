# GOVERNANCE.md template

Section order, fill-in guidance, and two worked examples showing right-sized versus over-engineered.

- [Section order](#section-order)
- [Transparency of meetings and minutes](#transparency-of-meetings-and-minutes)
- [Right-sized example: two-maintainer project](#right-sized-example-two-maintainer-project)
- [Over-engineered example and what it costs](#over-engineered-example-and-what-it-costs)
- [Neighbouring files](#neighbouring-files)

## Section order

Converged from GitHub's Minimum Viable Governance and the Cloud Native Computing Foundation templates, in the order listed in the table below. Skip any section the project does not need, but keep the order for the ones it does. Code-of-conduct enforcement and security response are pointers to their own files plus a statement of who acts.

| Section                       | What has to be in it                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Values and scope              | three to six lines, only values the project would enforce, plus what it refuses to become - the sentence that lets maintainers decline features impersonally                                                                                                                                                                                                                    |
| Roles                         | per role: what it may do, what it is expected to do, how it is granted. List merge rights separately from privileged credentials (signing, publishing, org ownership) - different grants                                                                                                                                                                                        |
| Becoming a maintainer         | self-assessable criteria (a time period, a count of non-trivial contributions, a count of reviews), who nominates, what approves it, what rights follow. With more than one employer represented, add that nominations are judged without prejudice to employer - and near a neutrality claim, a cap on nominations from an organization already employing half the maintainers |
| Removing a maintainer         | resignation, inactivity defined in months, conduct violations, and the threshold - commonly two-thirds of remaining maintainers. Writing it before it is needed makes it survivable                                                                                                                                                                                             |
| Emeritus                      | recognition kept, rights removed, listed separately, reinstatement by simple majority. The humane alternative to a stale maintainer list or an ugly removal                                                                                                                                                                                                                     |
| Meetings and communication    | cadence, public by default, explicit exceptions (security reports, conduct cases, personnel matters), where notes are published. With no meetings, say so rather than inventing them                                                                                                                                                                                            |
| Decision-making and voting    | one line per decision class - who decides, threshold, timer, escalation - plus who may demand a vote, quorum, minimum open period, whether abstentions count in the denominator                                                                                                                                                                                                 |
| Code-of-conduct enforcement   | who acts, and what happens when the subject is a maintainer: excluded from deliberation, two others handle it, escalate outside the project if the whole group is implicated. The standard lives in its own file                                                                                                                                                                |
| Security response             | a named group of at least two, a pointer to the reporting process, a review cadence for who is on it                                                                                                                                                                                                                                                                            |
| Appeals and escalation        | how a decision gets reconsidered - open an issue, get a written answer within a stated period, escalate if denied. No appeal path pushes disagreement into public conflict or forks                                                                                                                                                                                             |
| Trademarks and project assets | who controls the name, logo, domains and registry accounts, and what happens to a departing maintainer's rights. This clause decides whether "vendor-neutral" is true; keep it factual, route the contract to counsel                                                                                                                                                           |
| Amendments                    | threshold, window, who may propose - plus a line saying the document is expected to change as the project grows, so amending it is normal rather than a crisis                                                                                                                                                                                                                  |

## Transparency of meetings and minutes

The pattern separating real transparency from the performative kind is **public by default, privacy by enumerated exception, with a visible marker where something was withheld**.

The strongest published versions list exhaustively which categories may be decided in private, and instruct the body to avoid private decisions otherwise:

- Contract negotiations.
- Interpersonal disputes.
- Personal-safety matters.
- Commitments made under confidentiality.

```
✓ Good - a project strikes private sections from its minutes and leaves a marker; a reader can tell something is missing
✗ Bad - an executive session with no marker and no policy for when the content becomes public; omission then looks identical to there being nothing to omit
```

Minutes committed to the repository, or tracked as labelled issues, also make the record versioned and searchable.

## Right-sized example: two-maintainer project

```markdown
# Governance

## Scope

Alice Ng and Ben Torres maintain <project>. It stays a single-purpose library;
storage backends and a plugin system are out of scope.

## Roles

- Maintainers: Alice, Ben. Merge, release, and decide direction.
- Release keys: Alice and Ben both hold signing keys and registry publish rights.
- Contributors: anyone with a merged change.

## Decisions

Routine changes: one maintainer approves; either may merge.
Anything that changes public API behaviour, scope, or the license: both maintainers
must agree, in a public issue, with a 7-day comment window first.
Disagreement that survives one week: the change is not made, and the issue records why.

## Adding a maintainer

Three months of sustained review activity, then both current maintainers agree.
New maintainers get merge rights immediately and release keys after one release cycle.

## Stepping back

A maintainer inactive for six months with no return date moves to emeritus and keeps
credit in MAINTAINERS.md; credentials are rotated within 30 days.
If both maintainers step back, we will name a successor or archive the repository
publicly rather than leave it unmaintained.

## Changing this document

Both maintainers agree, in a pull request open for at least 7 days.
```

Roughly a page. Every clause describes something the project has done or will plausibly do this year; the last two sections carry most of the value.

## Over-engineered example and what it costs

The failure: a five-seat steering committee with staggered two-year terms, appointed election officers, a contribution-based electorate, three working groups and a two-thirds amendment rule - on a project with four maintainers, all at one employer, that has never held an election. Costs:

- Elections that never happen (expired terms, a visibly false governance file).
- Working groups with one member.
- A review that distrusts the whole document because one part is false.

The fix is to write the smaller model honestly and record the revisit trigger - "revisit when maintainers exceed eight or a second organization holds two seats".

## Neighbouring files

Link, do not absorb:

- Contribution mechanics (`CONTRIBUTING.md`).
- Behaviour standard (`CODE_OF_CONDUCT.md`).
- People and affiliations plus emeritus (`MAINTAINERS.md`).
- Vulnerability reporting (`SECURITY.md`).
- Role progression (`CONTRIBUTOR_LADDER.md`).
- Release process, review guidelines, code-owner routing.

Governance defines authority, those files define practice; mixing them makes every process tweak a governance amendment.
