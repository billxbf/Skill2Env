# Environment hardening for a demo

## Contents

- Offline mode
- Venue network failure modes
- Legibility
- Machine hygiene
- Sharing mode
- Display and hardware
- Integration note: scripted-demo tooling

For the surfaces the demo chooses to expose on the projection screen - the dedicated profile, the browser and notification surfaces, the terminal prompt, the repository and data hygiene, the panic button - see [./surface-exposure.md](./surface-exposure.md). This file covers the room, the network and the display; that one covers what can leak.

## Offline mode

The target is a demo that completes with the network cable pulled. Anything short of that is a demo whose success depends on a room full of strangers' devices sharing an access point with it.

- Run the whole stack locally: local server, local database with seeded fixtures, local queue, local object storage.
- Replace third-party calls with recorded responses or a local mock. Record them from a real run so the payloads are honest.
- Warm every cache before the session: package cache, container images, model weights, build artifacts, search indexes.
- Map a real-looking hostname to `127.0.0.1` in the hosts file when the URL bar is part of the story.
- Disable auto-update, telemetry and file-sync clients. They saturate a shared uplink and raise modal dialogs at the worst moment.
- If one segment genuinely must reach the internet, isolate it: make it the droppable segment, give it a recorded fallback, and put a hotspot behind it.

## Venue network failure modes

Worth planning for explicitly, because each one has bitten speakers who "tested the Wi-Fi":

- Captive portals that expire mid-session, or that re-authenticate per device per day.
- Bandwidth collapse when the room fills - a network that was fine at 8am is unusable at 2pm.
- IPv6-only or NAT64 conference networks that break tooling assuming IPv4 literals.
- Blocked outbound ports: SSH, custom development ports, anything that is not 80/443.
- Corporate VPN auto-reconnect kicking in and rerouting the demo traffic.
- Hotspot signal that works in the lobby and fails in a concrete basement hall - test in the actual room.
- The audience hitting your demo endpoint simultaneously the moment its URL appears on screen.

## Legibility

- Terminal 24pt or larger; editor 20pt or larger. Verify from the back row of the actual room, not from the stage.
- Light or high-contrast theme. Projectors crush dark themes; a theme that looks great on a laptop can be unreadable four rows back.
- Block cursor rather than a thin line - the audience has to be able to find it.
- Keep lines to roughly 80-100 columns; a wrapped command is an unreadable command.
- Increase line height and disable ligatures if they blur at distance.
- Zoom the browser, do not rely on the projector's scaling.

## Machine hygiene

- Do Not Disturb on, and quit chat, mail and calendar entirely rather than trusting focus mode to catch every surface.
- Disable hover panels, inline hints, autocomplete popups and editor notification toasts. They cover the exact line you are talking about.
- Fresh browser profile: demo tabs only, extensions off, history and autofill empty.
- Clear shell history and editor recent-files lists. Tokens, client names and embarrassing commands surface in dropdowns and stay in the recording forever.
- Log out of personal accounts on that profile.
- Sleep, screensaver and automatic display dimming off; machine plugged in.
- Custom shell prompt with no username, hostname, client name or personal path - a short string the speaker can read at a glance. A default prompt is a small biography on every command.
- `clear` before the session. The previous demo's tokens, paths and typos sit in the scrollback until explicitly cleared, and a `clear` on stage is a tell.
- No real secrets in `.env`, even for a local stack. Placeholders (`API_KEY=demo_key_123`) keep the demo runnable and the leak inert; the audience can read every value on screen.

## Sharing mode

The mode the speaker chooses to share is the cheapest single decision in this file. Wrong mode, hours of work undone in one click.

- Share the application or window, not the entire screen, wherever the platform offers it. A window share is bounded by the window; a desktop share is bounded by everything the laptop is willing to display.
- For a multi-window demo, share the app that drives the demo and switch windows only inside that app.
- An extended display to the venue's projector is a desktop share in practice. The other desktop carries the daily-driver notifications, the personal mail, the personal browser.
- Rehearse the actual share mode on the actual platform the day before. "I clicked Share and it worked" hides the difference between application, window and entire screen on every platform the speaker has not used that week.
- Treat the platform's optional sensitive-content detection as a backstop, not a strategy. It catches some leaks after they have already been put on screen.

## Display and hardware

- Set the display to the venue's resolution and aspect ratio, then rehearse at that setting. Layouts shift, and a font size that worked at one resolution does not at another.
- Bring your own adapters - the common connectors plus whatever the venue lists - and test mirroring, not just that the cable fits.
- Check what the stage gives you: confidence monitor, countdown clock, power, and microphone type. A handheld mic plus a presenter remote plus a keyboard is three objects and two hands.
- Keep the deck exported as PDF, including the key demo frames, on a USB key and on a second machine. A talk can be delivered from someone else's laptop; a demo cannot.
- Arrange a buddy: a colleague not speaking in the same slot, sitting in the front row, holding a clone of the repository, the deck and the fallback recordings on a working machine.

## Integration note: scripted-demo tooling

Tier 1 needs a way to run pre-written input without typing it. The mechanism matters more than the tool, and every ecosystem has one:

- **Shell demo runners** - libraries that simulate typing a pre-written command and then execute it, with pauses under the presenter's control. They also let you stage a slow dependency in advance and "type" its install command without waiting for it.
- **Editor demo extensions** - scripted step lists that create files, highlight regions, run editor commands and show markdown slides, all advanced by one keyboard shortcut, so the speaker never alt-tabs.
- **Terminal session recorders** - text-based recordings that replay at a chosen speed and stay copy-pasteable, small enough to embed and to publish alongside the talk.
- **The zero-dependency version** - a plain text file of the commands, in order, with a large font, that you copy from. It has no install step and it fails at nothing.

Pick whichever exists in the environment the demo already runs in. Do not add a tool to the demo whose own failure becomes a new risk row.
