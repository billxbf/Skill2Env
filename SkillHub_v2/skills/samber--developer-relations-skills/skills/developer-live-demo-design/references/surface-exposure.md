# Public-safe surface for a demo

What appears on the projection screen during a session is public the moment it goes up, and the published recording a week later makes it permanent. This file is the companion to `environment-hardening.md`: that file is about the room, the network and the display; this one is about the surfaces you choose to expose on that display, and the artefacts that have to live behind them.

## Contents

- The exposure model
- Dedicated demo profile
- Browser surface
- Notification surface
- Sharing surface
- Terminal surface
- Repository surface
- Data surface
- Panic button
- Pre-flight additions for public-safe surface
- Worked example: a single demo repo from clean

## The exposure model

Treat every pixel on the projector as if the room, the recording, and a screenshot posted to social media will all see it. The model the rest of this file follows is one assumption and one consequence:

- Assumption: anything that can be on screen _will_ be on screen at least once during the slot.
- Consequence: a public-safe demo runs from surfaces that have nothing private to leak. The work is choosing those surfaces, not auditing the laptop on the morning of the talk.

The cheapest way to keep that promise is to make the demo profile a different profile from the daily driver - a separate browser profile, a separate user account, ideally a separate OS account or VM. Anything on the daily driver stays out of reach of the demo, and the demo has nothing on it that the daily driver needs.

## Dedicated demo profile

A separate profile is the load-bearing decision; everything else in this file is cheaper once it is in place.

- A separate OS user account, or a separate browser profile, for demos. The daily-driver account never opens during the session.
- No personal accounts signed in on the demo profile: no personal mail, no personal chat, no personal cloud drive, no password manager, no personal VPN, no personal calendar.
- A demo-only cloud project, tenant or org where the live calls land. Production is never opened on this profile, and the production credentials never sit on this machine.
- A separate Git identity (name and email) for the demo repo if the talk is on someone else's product. The identity attached to a commit is on screen whenever the demo runs `git log`.
- A throwaway hotspot or a second mobile line for the demo, separate from the personal phone. A notification from the personal phone on the same account leaks regardless of focus mode.
- A VM or a second laptop is the only way to enforce "daily driver is closed" when the speaker's discipline is the only check. The VM is worth its cost for any talk that gets re-given.

## Browser surface

The browser carries the most surface area and the least control. One profile, one window, and a fixed list of tabs.

- Fresh browser profile, with sync off, history and autofill empty, password manager disconnected, payment methods removed.
- A fixed list of tabs, opened before the session, on the speaker's notes. Three to five is the target; ten is the upper bound before accidental context switches become likely.
- Bookmarks only the demo needs. Personal bookmarks and reading-list folders stay in the other profile.
- Extensions off, or reduced to the one the demo path needs. Extensions inject UI and fetch content, both of which are out of the speaker's control on stage.
- Webmail, chat, calendar and the production console are closed. "Closed" means the tab is gone, not "minimised" and not "in another desktop".
- Before the session: open the tab, navigate the path the demo follows, verify nothing the speaker does not want appears, and leave that window alone. Closing and reopening the window mid-session is when the wrong profile opens.

## Notification surface

Every notification channel is a leak. The fix is to close the source, not to mute the surface, because a notification that has already been delivered to the laptop waits for the screen to come back.

- Do Not Disturb on, at the OS level, with a schedule that covers the slot and any buffer.
- Quit chat, mail, calendar and any IM client. Focus modes are not enough: a message that arrives while chat is open and is read on the lock screen is still a leak.
- Browser notifications off for every site. The OS-level toggle is not enough; sites can still surface badges and toasts in some browsers.
- Phone on silent, and the watch, and the tablet, and anything else that mirrors notifications from the demo account. A mirrored notification on the wrist still ends up photographed.
- Calendar and reminder apps quit, not silenced. A reminder due during the slot will fire regardless of focus.
- Auto-update, telemetry and file-sync clients disabled. They surface modal dialogs at the worst possible moment and saturate the shared uplink.

## Sharing surface

The mode the speaker chooses to share is the cheapest single decision in this file. Wrong mode, hours of work undone in one click.

- Share the application window, not the desktop, wherever the platform offers it. A window share is bounded by the window; a desktop share is bounded by everything the laptop is willing to display.
- For a multi-window demo (terminal plus editor plus browser), share the app that drives the demo, not the OS desktop, and switch windows only inside that app.
- A second display extended from the laptop to the venue's projector is a desktop share in practice. Treat it the same way: the laptop's other desktop has notifications, mail and personal tabs.
- Rehearse the actual share mode. "I clicked Share and it worked" hides the difference between application, window and entire screen on every platform the speaker has not used that week.
- Treat the platform's optional "sensitive content detection" as a backstop, not a strategy. It catches some leaks after they have already been put on screen.

## Terminal surface

The terminal leaks by what it shows, not by what runs. Two surfaces matter: the prompt and the scrollback.

- A custom prompt with no username, no hostname, no path that names a client, a project or a person. A short string the speaker types is a short string the audience reads; the default prompt is a small biography on every command.
- No `env`, no `printenv`, no `set | grep -i token` in the script. If a value must be visible to the audience, name the variable, not its value, and `print` the safe placeholder.
- No `cat ~/.bash_history` or `history`. If the demo needs to show a previous command, the script is the previous command.
- No `git remote -v` against a URL that contains credentials. SSH config aliases are a working substitute; the demo URL is otherwise a credential.
- `clear` before the session. The previous demo's tokens, paths and typos sit in the scrollback until explicitly cleared, and a `clear` on stage is a tell.
- Editor recent-files and project switchers cleared. The path dropdown is a list of every project the laptop has opened, in the order it opened them.
- No real secrets in `.env`, even for a local stack. Placeholders (`API_KEY=demo_key_123`, `DATABASE_URL=postgres://demo:demo@localhost/demo`) keep the demo runnable and the leak inert.
- A short script that the speaker can paste from a file, not retype. Re-typed commands grow typos; pasted ones stay accurate.

## Repository surface

The repo shipped to the audience, or visible on screen during the demo, is a public artefact. The rule is the same as the data one: the demo repo contains only what the speaker is happy to publish.

- A dedicated repository, cloned fresh for the talk, not the working repo the team ships from. The team repo carries real names, real secrets in the history, and real issues a search engine will find.
- A clean git history, or no history at all (`git init` in an empty directory). Deleting a secret from the current file does not delete it from earlier commits; the audience can `git log -p` a slide.
- No branches carrying abandoned experiments, no tags with internal codenames, no `.git/config` left over from a personal fork.
- Synthetic data: fake names, fake addresses, fake API keys, fake org names, fake support tickets. The realism that helps a B2B demo is the realism of shape and volume, not the realism of the actual customer.
- The dependency manifest pinned to exact versions. A `^1.2` range is an install-on-stage decision, and a fresh install on stage is a failure mode.
- The demo's repo URL on a slide, not the team's internal URL. The internal URL has internal-only documentation, internal tickets and internal naming conventions in adjacent paths.

## Data surface

The data is the leak channel most likely to slip past a careful setup, because it looks anonymous until someone reads it.

- Synthetic data, not anonymised data. Anonymising a real customer by replacing the name leaves the email, the URL, the bucket name, the IP range, the project codename, the support ticket, the colleague's name in a comment, and the avatar; "anonymous" data with any of those intact is a one-step re-identification.
- Read-only credentials against a sandbox tenant, with the role limited to what the claim needs. The credential on screen is a credential an audience member can photograph and try.
- Production read-offs, screenshots from real accounts, and recordings of real customer sessions are out of scope for the demo repo, the demo data, the demo slides and the speaker notes.
- Embargoed or unreleased features flagged off in the build, in the docs, and in the marketing site, before the session. An audience that spots a feature the company has not announced ends the talk on a question the speaker cannot answer.
- A pre-flight pass on every screen the demo will show, including error states, empty states, dropdowns, autocomplete, and the next slide. Hidden screens leak the same as visible ones when a click goes wrong.

## Panic button

Rehearsed recovery is the difference between a forty-second reset and a five-minute embarrassment. The panic button is the recovery line, the artefact, and the muscle memory in that order.

- A rehearsed recovery line, written down and read aloud at least once: "I'm going to switch to the recorded run for this segment - it's the same four commands, recorded yesterday, and we'll be back live in ninety seconds."
- A safe screen ready to display on a single keystroke. A full-screen note that says "Demo paused - one moment" in a font the back row can read is enough; a blank screen is not.
- A rehearsed muscle memory for "stop sharing" in the platform the speaker is using. The button location is checked once, before the slot, not discovered during the failure.
- A rehearsed second profile or VM to switch to if the daily-driver account opened by accident. A second context that has nothing private to leak is the fastest way to recover.
- A buddy in the room, briefed, holding a clone of the repo, the deck PDF and the fallback recordings on a working machine. The buddy's job is the human-redundancy case the recovery plan does not cover: a dead laptop, a lost account, a venue-side failure.

## Pre-flight additions for public-safe surface

Run these alongside the checklist in the runbook template:

- Demo profile only - daily-driver profile, mail, chat, calendar and personal browser all closed.
- Hotspot paired; personal phone on silent, watch and tablet too.
- Custom prompt set; shell history and editor recents cleared; `clear` run.
- `.env` contains placeholders only; no real secret in the working tree or the history.
- Demo repo URL on a slide, not the internal one.
- Synthetic data verified - one full pass through the demo path against the fixture set, not just the first screen.
- Safe screen ready; stop-sharing key known; recovery line rehearsed out loud.
- Buddy briefed and holding the clone.

## Worked example: a single demo repo from clean

A speaker is preparing a CLI demo for a 25-minute slot at a vendor-neutral conference. The talk has been re-given three times in the last year and will be re-given again.

The demo repo is a fresh directory, `git init` from empty, with a `README.md`, an `app/`, a `data/` folder holding a 50-row synthetic fixture, a `.env.example` with placeholders, and a `Makefile` that exposes `make reset`. The repo has no history of the team's real product, no inherited secrets, no real customer names. The repo URL is on a slide near the demo segment.

The browser is a separate Firefox profile, signed out of everything, with two tabs open: the repo on the speaker's own site, and the CLI's hosted sandbox. No mail, no chat, no docs, no production console, no password manager.

The terminal runs a custom prompt (`demo % `), shell history cleared, and a single pane set to 24pt on a high-contrast theme. The script is a five-line file the speaker pastes from; there is no `env`, no `printenv`, no `cat`, no `git remote -v` in the script.

The panic button is a `Stop sharing` shortcut the speaker has used once today, a full-screen "Demo paused" image on a known hotkey, and a buddy two rows back holding the deck PDF and a clone of the repo on a working laptop.

The cost of the setup is one afternoon. The cost of skipping it is a notification on a projector at minute nine, a token in the conference recording, or a customer name in a screenshot the speaker posts to social media a week later.
