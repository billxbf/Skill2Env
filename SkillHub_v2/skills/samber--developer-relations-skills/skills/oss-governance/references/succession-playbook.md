# Succession playbook

Measuring concentration, granting trust safely, and writing the exits before they are needed.

## Measure concentration

**Contributor absence factor** (the CHAOSS metric formerly called bus factor): the smallest number of contributors responsible for 50% of contributions.

Sum contributions over a window (12 months is a reasonable default):

1. Take 50% of the total.
2. Sort contributors descending.
3. Accumulate until the threshold is crossed.
4. Count the contributors used.

Worked example: `1000, 433, 343, 332, 202, 90, 42, 33` totals 2,475, threshold 1,237.5. The top two (1,433) cross it, giving a factor of **2**.

Compute it on more than commits: reviews, issue responses and documentation reveal a different and usually smaller set of load-bearing people. Derive it from repository history where you can run commands; otherwise ask maintainers to rank themselves and treat it as an estimate.

Take two companions with it:

- **Employer spread**: how many distinct employers the top contributors have, since the graduation-grade test is survival of any single organization withdrawing.
- **Trend**: a factor of 2 that used to be 5 is a different story from a 2 that used to be 1.

Publish aggregates, not per-person league tables; contribution metrics attached to names create privacy and performance-review problems the project did not sign up for.

**Measurement hygiene.** A concentration number is only as credible as its filters, and every one of these changes the answer:

- Exclude merge commits, or the person who integrates looks like the person who writes.
- Exclude bot and automated-dependency authors, or the top contributor is a robot.
- Choose author or committer identity deliberately; they diverge wherever patches are relayed or rebased.
- Bound the window, or weight by recency, so people who left three years ago stop propping the number up.
- Drop contributors below a small share of the total rather than reporting a long tail.
- Compute it **per governed area as well as project-wide**. A project-level factor of 3 routinely hides a subsystem owned by exactly one person, and that subsystem is what actually breaks on a departure.

One incidental signal: if the top contributors' commit timestamps cluster in a single timezone, the project is more concentrated than the employer count suggests, and a 72-hour vote window is probably not buying the participation it was meant to buy. Where history is machine-readable this whole measurement is scriptable, and the same pass can diff the result against the code-owner file to surface ownership drift.

## Inventory the credentials

Code access is rarely the binding constraint - the credentials are. List each, with who holds it and who could recover it:

- Repository and organization ownership (who can add and remove people).
- Protected-branch and merge-policy administration.
- Release signing keys and any code-signing certificates.
- Package-registry publishing rights, per registry.
- Domain registration, DNS and site hosting.
- Continuous-integration secrets and deployment tokens.
- The security-report inbox and any embargo channels.
- Social, forum and chat administration.
- Funding and donation accounts.

A row with exactly one holder is a single point of failure; a row held by someone no longer active is a security incident waiting to be discovered. Aim for two current holders per row with recovery documented, and re-verify on a fixed cadence - this list rots silently.

## The staged trust ladder

Separate what someone can review from what they can ship, and grant in stages against evidence measured in months:

1. **Contributor** - merged changes.
2. **Triager** - labels, closes, reopens; no merge rights. Cheap to grant, immediately useful, and a real signal of judgement.
3. **Reviewer** - approvals count toward merge requirements in a named area.
4. **Maintainer** - merge rights across the project, a vote in governance decisions.
5. **Key holder** - release signing and registry publishing, granted after at least one supervised release cycle, never in the same act as merge rights.

The 2024 xz-utils takeover (step 7, evidence base) justifies the split. Nothing in that story is detectable by reviewing a single pull request, and everything in it is slowed by staged grants, a second key holder, and treating pressure to hand over control as a signal to pause. Practical rules that follow:

- Require reviews _given_, not only pull requests merged - reviewing is where judgement shows.
- For key-holder roles, prefer a verifiable identity or an established public track record, and say so in the document rather than applying it silently.
- Treat urgency as suspicious: a legitimate co-maintainer can wait a release cycle.
- When a maintainer is struggling, relieve load first (triage help, scope cuts, funding, a release pause). Promotion is not a burnout treatment.

## Exit paths

Write all four before any of them is needed:

- **Vacation / reduced availability** - publish it. Silence reads as abandonment and invites the pressure described above; a stated weekly budget ("2-5 hours") is a legitimate governance clause.
- **Emeritus** - credit retained, rights removed, listed separately, reinstatement by simple majority. Triggered by resignation or by the written inactivity definition, so it is procedural rather than personal.
- **Handover** - recruit from reviewers, run a joint period where both merge and release, transfer credentials one at a time with the old holder revoking only after the new one has used theirs successfully, then update the people file and announce. Document the project's direction first so a successor can honour it.
- **Archive** - a legitimate, honourable end state. Announce it, mark the repository read-only, state the last supported version and any security policy, point at a successor fork if one exists. An unmaintained project that never says so is the worst outcome for its users.

## Handover checklist

- [ ] Successor named and publicly announced, or archive announced.
- [ ] Every credential row has a new holder who has used it once; registry and domain ownership transferred with two holders each.
- [ ] Old holder's access revoked, keys rotated, recovery contacts and security inbox updated.
- [ ] Governance file, people file and funding accounts updated.
- [ ] Direction and known-hazards notes written down for the successor.
- [ ] Users told, in the release notes and on the project's main surface.
