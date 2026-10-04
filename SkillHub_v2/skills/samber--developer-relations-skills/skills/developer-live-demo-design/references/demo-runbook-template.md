# Demo runbook template

The artifact this skill produces. One page per demo, readable while stressed. Fill every field; an empty field is an untested assumption.

## Contents

- Header
- Segments
- Fallback assets
- Reset and pre-provisioning
- Recovery lines
- Pre-flight checklist
- Rehearsal log

## Header

```
Demo:          <short name>
Claim:         <the one sentence the demo must make the audience believe>
Venue/format:  <stage | workshop | webinar | recorded | customer call>
Budget:        <minutes allowed>  /  Measured: <minutes in the last cold run>
Tier:          <0-4>  Fallback tier: <n+1>
Network:       <offline | hotspot primary | venue Wi-Fi + recorded fallback>
Data:          <fixture set, tenant, account; and what must not appear on screen>
Buddy:         <name, what they hold, where they sit>
Owner:         <who maintains this runbook>
Last verified: <date of the last clean cold run>  on <product version>
Re-verify:     <before each event, and whenever the demo path ships a change>
```

The last three lines exist because a runbook rots silently: the commands stop matching the product months before anyone notices, usually at the next event. A stale verification date is the signal to re-run the rehearsal protocol rather than trust the document.

## Segments

One row per segment. "Droppable" is what you cut first when the clock slips.

| #   | Proves                     | Enter from                | Runs                  | Budget | Droppable | Fallback                        |
| --- | -------------------------- | ------------------------- | --------------------- | ------ | --------- | ------------------------------- |
| 1   | The old way is slow        | tag `demo/step-1`         | scripted commands 1-3 | 60s    | no        | recorded clip `01-baseline.mp4` |
| 2   | The new way is one command | tag `demo/step-2`         | scripted command 4    | 45s    | no        | recorded clip `02-oneshot.mp4`  |
| 3   | It holds under load        | seeded tenant `demo-load` | load script           | 75s    | yes       | screenshot of the dashboard     |

Every "Enter from" must be reachable without running any earlier segment. If a cell reads "after segment 2", the architecture is wrong - fix it before rehearsing.

For each segment, also write down what must already be true before it starts and what the screen should look like when it works - one line each, in the speaker notes:

```
Segment 2  precondition: containers up, step-2 image tag checked out, tenant seeded
           expected:     three green lines, last one "0 failed writes"
           if not:       one retry, then clip 02-oneshot.mp4 (slide 16)
```

Written down, that turns "something looks wrong" into a decision the speaker can make in a second. Held in memory, it becomes the pause where the demo dies.

## Fallback assets

```
01-baseline.mp4      recorded 2026-08-20, 58s, embedded on slide 14
02-oneshot.mp4       recorded 2026-08-20, 41s, embedded on slide 16
03-dashboard.png     annotated, slide 18
deck.pdf             includes all three key frames, on USB key and buddy's laptop
```

Assets live inside the deck wherever the deck format allows it. An asset that requires alt-tabbing to a file browser is not a 20-second fallback.

## Reset and pre-provisioning

```
Reset (one command):   ./demo reset
Verified cold:         yes; 2026-08-21, fresh boot
Pre-provisioned:       deps installed, images pulled, model cached, tenant seeded, DNS warm
Never on stage:        install, build, first-run migration, account verification
```

## Recovery lines

Write them out; do not improvise them.

- Network failure: "The Wi-Fi here has opinions - I recorded this exact run yesterday, so let's watch that instead. What you're about to see is the same four commands."
- Unfixable error: "That's a new one, and I'm not going to debug it at you. Here's what it does when it behaves - " then switch and continue.
- Overrun: "I'll skip the load test, the numbers are on the next slide anyway."

## Pre-flight checklist

Run in the room, before the session starts.

```
[ ] Machine plugged in, sleep and screensaver off
[ ] Do Not Disturb on; chat, mail, calendar quit
[ ] Fresh browser profile, demo tabs only, extensions off
[ ] Shell history and editor recents cleared; custom prompt set; clear run
[ ] Terminal 24pt+, editor 20pt+, high-contrast theme, block cursor
[ ] Display set to venue resolution and aspect ratio; mirroring tested
[ ] Adapters tested (yours and the venue's)
[ ] Reset command run once; demo left at segment 1
[ ] Hotspot on and paired; venue network is the backup, not the plan
[ ] Fallback assets open or one keystroke away
[ ] Deck PDF on a USB key and with the buddy
[ ] Nothing embargoed, no customer data, no production credentials on this machine
[ ] Demo profile only - daily-driver profile, mail, chat, calendar and personal browser all closed
[ ] Share mode set to application or window, not entire screen, and rehearsed
[ ] .env holds placeholders only; demo repo URL on a slide, not the internal one
[ ] Safe screen ready on a known hotkey; stop-sharing key known; recovery line rehearsed out loud
```

For the items a one-line checklist cannot fully check (the dedicated profile, the synthetic data, the share-mode rehearsal), see [./surface-exposure.md](./surface-exposure.md) and run it as a separate pass the day before, not at the venue.

## Rehearsal log

| Date       | Run type                          | Time | Failures           | Change made                  |
| ---------- | --------------------------------- | ---- | ------------------ | ---------------------------- |
| 2026-08-18 | segment-by-segment                | -    | segment 3 ran 2:10 | pre-filled fixture, now 1:05 |
| 2026-08-20 | cold, offline                     | 3:40 | none               | -                            |
| 2026-08-21 | cold, offline                     | 3:35 | none               | -                            |
| 2026-08-21 | drill: kill network mid-segment 2 | -    | switched in 14s    | -                            |

The log is the evidence for the pass threshold: three clean consecutive cold runs, plus a drill per top risk. That bar is this skill's own baseline, not a published standard - the rehearsal log is what makes it arguable, because a reviewer can see which runs were clean and which were not.
