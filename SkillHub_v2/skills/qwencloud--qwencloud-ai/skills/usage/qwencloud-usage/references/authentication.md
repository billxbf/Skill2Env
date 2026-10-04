# Authentication Response Semantics

All authentication invocation syntax and sequencing live in [cli.md](cli.md). This document only defines how to interpret authentication state and events.

## Status

When `authenticated` is true and the token is unexpired, continue to the requested account operation without starting another login.

## Device-Flow Events

Interpret the structured `events` array as follows:

- `already_authenticated`: authentication is already usable; continue the original task.
- `device_code`: extract and present the returned `verification_url` and its expiry.
- `success`: authentication completed; continue the original task.
- `expired`: the current device code is no longer usable; restart the flow once.
- `error`: report the failure without fabricating a result.
- `pending`: continue the active completion flow.

Do not initialize a second device code while one is pending because doing so invalidates the page already opened for the user.

## Logout

Logout revokes the server-side session and clears local keychain or file credentials. Server-side revocation is best-effort, but local logout still clears the current session. Treat logout as destructive: return `confirmation_required` and obtain explicit confirmation before executing it.

## Credential Storage

Credentials use the OS keychain when available and an encrypted-file fallback otherwise. Never expose, copy, or persist token contents in an answer or test artifact.
