# Sample audit checklist

Run the mechanical checks with `scripts/sample-audit.py` first, then apply judgement to what the script cannot see. The script finds pattern defects; only a reader who understands the product finds a sample that runs fine and teaches the wrong thing.

## Severity anchors

| Severity | Test                           | Examples                                                                                                                                |
| -------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| P0       | Harms the reader who copies it | Real-format credential, destructive command without a guard, disabled TLS verification, wildcard IAM policy, data-loss default          |
| P1       | Does not work as written       | Missing import, removed or renamed symbol, wrong argument order, documented output that no longer matches, unpinned version that broke  |
| P2       | Works but violates policy      | No execution tier, prompt characters, no expected output, ellipsis omission, missing language identifier, parity gap, stale-but-passing |

Report P0 findings the moment you see them rather than at the end of the audit - a leaked credential does not wait for the report.

## Per-sample checks

Mechanical (script covers these):

- [ ] Fence carries a language identifier.
- [ ] No prompt character starting a command line.
- [ ] Command output not interleaved in the command block.
- [ ] No `...`, `…` or HTML ellipsis entity inside the block.
- [ ] Placeholders use the policy's format; no bare `YOUR_KEY_HERE` variants mixed in.
- [ ] No credential-shaped literal (long base64/hex string, `sk_live`-style prefix, `-----BEGIN * PRIVATE KEY-----`).
- [ ] No insecure switch (`--insecure`, `verify=False`, `rejectUnauthorized: false`, `InsecureSkipVerify`).
- [ ] No unguarded destructive command.
- [ ] Block length within the policy cap.
- [ ] No trailing whitespace (screen readers announce it).

Judgement (human or agent, per sample):

- [ ] Every symbol used exists in the current public API surface.
- [ ] All imports present; the sample would run in a fresh file.
- [ ] Client setup shown, with reuse and cleanup addressed.
- [ ] One code path; nothing extraneous to the point being made.
- [ ] Error handling specific, and present only where it is intrinsic to the example.
- [ ] Expected output present and currently accurate.
- [ ] Comments add non-obvious context.
- [ ] Execution tier assigned, and honest - a "Run" sample that CI does not run is a P1, not a P2.
- [ ] Version pinned in install commands where a floating version can break the path.
- [ ] The scenario matches the sibling-language samples of the same identifier.

## Finding format

One finding per line, evidence first, fix in one sentence. Prose paragraphs get triaged by nobody.

```
docs/guides/webhooks.md:142 - sample calls client.verify(payload, sig); the method was renamed
  to verifySignature in v4 (breaking change, 2026-03). Fix: update the call and re-pin the
  install block to ^4.
```

## Worked pair

Negative - five defects in six lines:

````markdown
```
$ curl -X POST https://api.example.com/v1/charges \
  -H "Authorization: Bearer sk_live_4eC39HqLyjWDarjtT1zdp7dc" \
  -d amount=2000 ...
{"id":"ch_1","status":"succeeded"}
```
````

Five defects:

- No language identifier.
- A prompt character that breaks copy-paste.
- A live-format secret key.
- An ellipsis inside a copyable block.
- Response body glued to the request so both get copied together.

Positive - same scenario, policy-compliant:

````markdown
Create a charge. Replace `<YOUR_API_KEY>` with the test key from your dashboard.

```bash
curl -X POST https://api.example.com/v1/charges \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -d amount=2000 \
  -d currency=eur
```

Expected response:

```json
{ "id": "ch_1", "status": "succeeded", "amount": 2000 }
```
````

The fix costs four lines and removes every P0 and P2 in the original. Most of a first audit looks exactly like this: cheap, mechanical, and never done because nobody owned it.

## Corpus-level checks

- [ ] Parity matrix filled; coverage computed, not estimated.
- [ ] Every tier-1 scenario has a sample; every sample maps to a named scenario.
- [ ] Duplicate samples for the same scenario reconciled to one source.
- [ ] Orphan samples (no page links to them) either linked or deleted.
- [ ] Samples in archived posts carry a version banner or are removed.
- [ ] Freshness: samples whose last successful run exceeds the window, counted and listed.
