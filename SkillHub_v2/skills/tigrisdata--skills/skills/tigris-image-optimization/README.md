# tigris-image-optimization

Resize, crop, and optimize images stored in Tigris. Covers all major frameworks.

## What It Covers

- **Upload-time processing** — generate thumbnails and variants on upload
- **Next.js** — `next/image` with Tigris, Sharp processing
- **Remix** — Sharp in action functions, responsive `srcset`
- **Rails** — Active Storage variants with `image_processing`
- **Django** — django-imagekit, Pillow manual processing
- **Laravel** — Intervention Image, Storage facade
- **Express** — Sharp middleware pipeline
- **CDN delivery** — Tigris public buckets serve from global edge

## Installation

**Claude Code:**

```bash
cp -r skills/tigris-image-optimization ~/.claude/skills/
```

**claude.ai:**

Add `skills/tigris-image-optimization` to project knowledge or paste `SKILL.md` contents into the conversation.

## Usage

This skill activates when you mention:

- "Image optimization", "resize images", "thumbnails"
- "Responsive images", "image CDN"
- "Image variants", "image processing Tigris"

## Example Prompts

```text
Generate thumbnails on upload and store them in Tigris
```

```text
Set up responsive image serving with Tigris CDN
```

```text
Add image resizing to my Rails app with Active Storage
```

## License

MIT
