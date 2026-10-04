# Launch day runbook

Times are relative to the anchor post (T+0). Adjust the absolute hour to the anchor audience's working day, mid-week.

## T-24h: Pre-flight

- Re-run the install command on a clean environment. Nothing else on this list matters if it fails.
- Verify every link in every draft: repository, docs, demo, registry page, social preview.
- Freeze the default branch. A mid-launch refactor breaks the thing strangers are cloning right now.
- Capture the measurement baseline (see the measurement reference) and store it outside the traffic panel.
- Confirm who is available for which hours, and that nobody has a meeting-heavy morning.
- Draft and review: anchor title, first comment, social thread, secondary-community posts, three answers to the hardest expected criticism.
- Prepare a decision rule for scope cuts, so an issue found at T-2h does not turn into a debate.

## T+0: Post

- Publish the anchor post yourself, from an account with genuine history in that community.
- Post the first comment within a minute or two. A thread with maintainer context attracts substantive replies; a bare link attracts drive-by dismissals.

First comment shape - adapt the wording, keep the four moves.

```
I'm <name>, I built this because <the concrete problem, in one or two sentences>.

Under the hood: <the one or two technical decisions a reader of this community would
find interesting, and why you chose them over the obvious alternative>.

What it does not do yet: <real limitations, including the ones a critic would raise>.

Happy to answer questions about <the areas you can go deep on>.
```

Do not paste a marketing paragraph, do not ask for anything, do not thank people in advance.

## T+0 to T+4h: The window that decides

- Answer every comment. Rank order: technical questions, criticism, comparisons to alternatives, praise.
- Fix and ship small breakages the same hour, then say so in the thread. Visible repair converts skeptics better than argument.
- Keep a second person triaging incoming issues so the maintainer stays in the discussion.
- Fire amplifiers on schedule even if the anchor thread is quiet - some launches are carried by the secondary wave.

Responding to criticism, by type:

| Comment type                          | Response                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------- |
| Valid technical objection             | Agree, explain the trade-off you chose, invite the better idea. Open an issue and link it.  |
| Misunderstanding                      | Clarify once, plainly, without "as stated in the README".                                   |
| "Why not just use X"                  | Answer seriously; this is the highest-value question in the thread. Name where X is better. |
| Feature request                       | Say yes/no/later with a reason. "Later" without a reason reads as a brush-off.              |
| Hostility or trolling                 | One factual reply at most, or none. Never the last word.                                    |
| Licensing or business-model suspicion | State the model, what is closed, and what will never be closed. Vagueness here is fatal.    |

## T+4h to end of day

- Keep checking back hourly; late comments still shape how the thread reads tomorrow.
- Log every question asked more than twice - those are the next README, FAQ and troubleshooting edits.
- Do not chase a dead thread with a second submission the same day.

## T+1 to T+7 days

- Ship the fixes the launch surfaced, and cut a release. Momentum is a real signal to anyone who bookmarked the project.
- Answer every issue and pull request, even with "looking at this later this week", and publish the response SLA you can actually hold.
- Fire the second wave: the long-form write-up, the communities you deliberately staggered, the newsletters that missed the cycle.
- Thank contributors by name in the release notes; the first external contributor is worth more than the first thousand stars.

## Roles when more than one person is available

| Role      | Owns                                                                               |
| --------- | ---------------------------------------------------------------------------------- |
| Voice     | The anchor thread and all replies. One person, so the tone stays consistent.       |
| Triage    | Incoming issues, pull requests, and same-hour fixes.                               |
| Amplifier | Secondary posts on schedule, monitoring for mentions elsewhere.                    |
| Watcher   | Metrics snapshots and link/uptime checks; flags a broken demo before strangers do. |

A solo maintainer merges these and drops them in reverse value order: `Voice > Triage > Watcher > Amplifier`. Silence in the anchor thread costs more than a slow issue response, a slow issue response costs more than a late metrics snapshot, and an amplifier post that never fires costs least of all - it is the row the Step 5 ranking was already prepared to delete.

Assign a named owner per _channel_ on top of these roles, not per role alone. GitLab's public handbook, the only complete launch-day playbook published openly, makes a DRI per channel its central mechanic precisely because "the team is watching" reliably means nobody is.

Give each owner an escalation route: when they cannot answer, they name the engineer who can, in the thread, rather than guessing. Agree in advance who may commit publicly to a roadmap item, a date, or a licensing statement; everyone else defers to that person.

Its tone rule is worth adopting verbatim: **conveying without convincing**. The audience is the silent majority reading the thread, not the person arguing in it.

## If a security report lands in the thread

Treat this as a separate procedure, not a hostile comment. Do it in this order:

1. Stop discussing specifics publicly. Reply once, briefly, pointing at `SECURITY.md` and the private contact.
2. Open a private advisory and add the reporter as a collaborator.
3. Develop and test the patch on a private branch.
4. Request a CVE through a numbering authority and credit the reporter when the advisory publishes.

Debating severity or validity in an open thread is the failure mode here - it invites exploit detail into a public conversation and reads as defensive whether or not the report is valid. This works only if the contact path already exists, which is why it is a readiness blocker.
