# tigris-s3-migration

Migrate from AWS S3, Google Cloud Storage, or Azure Blob Storage to Tigris with zero downtime.

## What It Covers

- **Shadow buckets** — zero-downtime migration with automatic backfill from S3
- **Bulk copy** — `tigris cp` and `aws s3 sync` for clean cutover
- **SDK swaps** — endpoint changes for Node.js, Python, Ruby, PHP
- **Environment variables** — what to change in your `.env`
- **Verification** — checklist for confirming migration success
- **Rollback** — strategy for safe migration with fallback

## Installation

**Claude Code:**

```bash
cp -r skills/tigris-s3-migration ~/.claude/skills/
```

**claude.ai:**

Add `skills/tigris-s3-migration` to project knowledge or paste `SKILL.md` contents into the conversation.

## Usage

This skill activates when you mention:

- "Migrate from S3", "switch from AWS S3"
- "Shadow bucket", "move to Tigris"
- "Migrate storage", "S3 to Tigris"

## Example Prompts

```text
Migrate my app from S3 to Tigris with zero downtime
```

```text
Set up a shadow bucket to gradually move data from S3
```

```text
What do I need to change in my code to switch from S3 to Tigris?
```

## License

MIT
