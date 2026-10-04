# Verification protocol

The author's machine always lies: it has the credentials, the runtime, the cached package and the tribal knowledge the page forgot to state. Verification exists to remove that advantage.

## Cold-run protocol

1. **Build a clean environment**: fresh container or VM, no global toolchains beyond the OS default, no cached package registries, no dotfiles.
2. **Create a fresh account** for the product (or a fresh tenant/project), with no prior configuration.
3. **Start a timer** at the moment the page loads, not at the first command.
4. **Execute every block verbatim.** Paste, run, record. Never fix a command silently - a command you had to adjust is a defect.
5. **Compare every output** to the documented output. Different is a defect, even when the run still succeeds.
6. **Log each defect** with its step number, what the page says, what actually happened, and the elapsed time at that point.
7. **Stop the timer** at the documented success moment.
8. **Repeat with a second reader profile**: someone fluent in the ecosystem and someone new to it. Their blockers differ, and only the second one finds the assumed knowledge.

An author's own cold run still under-catches: Tom Johnson's API documentation course reports a SendGrid getting-started tutorial that only 1 of 20 workshop participants completed successfully once tested against real readers live. A page that reads as finished to its author can still fail almost everyone who did not write it, which is the exact gap the second reader profile exists to close.

Record the run as a table so the same page can be re-measured after a fix:

| Step    | Elapsed | Command ran verbatim | Output matched | Defect                  |
| ------- | ------- | -------------------- | -------------- | ----------------------- |
| Prereqs | 0:40    | yes                  | n/a            | Node version not stated |
| 1       | 1:25    | no                   | no             | package name missing    |

## Pass threshold

The five ship criteria live in `SKILL.md` § Pass threshold - they are stated once so the two files cannot drift. Apply them here on the clean environment, for both reader profiles.

Failing the time budget means cutting the success moment, not raising the budget. Failing any other criterion means fixing the page and rerunning from step 1 of this protocol - a partial rerun misses defects the fix introduced.

## Friction log

While cold-running, keep a friction log alongside the defect table. This is the practice Aja Hammerly documented from Google's DevRel team, where new hires write one in their first weeks precisely because they lack the inside knowledge that lets veterans route around rough spots.

Frame it around the single scenario the quickstart serves. Log one line per moment of hesitation, confusion or surprise:

- The search term used.
- The link clicked.
- The command pasted.
- The reaction.

Tag each entry with Hammerly's stoplight convention:

- Green for delight.
- Yellow for friction.
- Red for blocking.

Hesitations are not defects yet. As this skill's own rule of thumb (not Hammerly's) - treat three hesitations in the same step as a sign the step is doing two things and should be split. The log's value is only realised when it reaches the people who can act on it: it covers docs and discoverability gaps, not just bugs.

## CI regression job

A page verified once decays as the product ships. Automate the run so drift fails loudly:

- Extract the quickstart's command blocks (annotate them in source so the extractor knows which blocks are executable).
- Run them in a clean container against the **published** artefact (the released package, the public endpoint) - not the repository working copy, since readers never have the working copy.
- Assert the documented outputs, normalizing volatile fragments (ids, timestamps, durations) with patterns rather than deleting the assertion.
- Provision a throwaway account/tenant per run so credential state never leaks between runs.
- Run on a schedule as well as on release: upstream dependencies and hosted-API changes break the page without any commit in your repository.
- On failure, fail the release rather than filing a ticket - an outdated quickstart is worse than a missing one, because it consumes the reader's trust before it consumes their time.

## Measurement instrumentation

Instrument the page so the funnel is observable without another manual run:

- Fire a distinct event at page load, at each step's copy-button click, and at the documented success action.
- Compute the median page-load-to-success time per week; it is the honest version of the number in the title.
- Break down drop-off per step, and treat the largest single drop as the next work item.
- Track issues and support tickets quoting a step number; each one names an ambiguous instruction.
- Compare completers' day-7 return against non-completers to confirm first success actually mattered.

When analytics are unavailable, run the cold-run protocol quarterly and after every major release; it produces the timing number, just less often.
