# tigris-security-access-control

Configure access keys, CORS rules, bucket policies, and presigned URL security for Tigris.

## What It Covers

- **Access key lifecycle** — create, assign, rotate, revoke
- **Roles** — Editor vs ReadOnly, scoping keys to buckets
- **CORS configuration** — development, production, and permissive examples
- **Public vs private** — bucket visibility and access patterns
- **Presigned URL security** — expiration, scoping, best practices
- **Audit checklist** — security review for Tigris storage
- **Key compromise** — incident response steps

## Installation

**Claude Code:**

```bash
cp -r skills/tigris-security-access-control ~/.claude/skills/
```

**claude.ai:**

Add `skills/tigris-security-access-control` to project knowledge or paste `SKILL.md` contents into the conversation.

## Usage

This skill activates when you mention:

- "CORS", "CORS error", "CORS configuration"
- "Access key", "key rotation", "security"
- "Bucket policy", "permissions", "access denied"

## Example Prompts

```text
Set up CORS for browser uploads to my Tigris bucket
```

```text
Rotate my Tigris access keys with zero downtime
```

```text
Audit my Tigris storage security configuration
```

## License

MIT
