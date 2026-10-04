#!/usr/bin/env python3
"""Extract every fenced code sample in a docs tree and lint it mechanically.

Walks a documentation directory, emits one row per fenced block with the facts a
sample audit needs, and flags the pattern defects a policy check can decide
without understanding the product: missing language identifier, shell prompt
characters, ellipsis omissions, credential-shaped literals, insecure switches,
unguarded destructive commands, placeholder style and block length.

Usage:
    sample-audit.py <docs-dir> [--format tsv|json|summary] [--ext .md,.mdx]
                    [--max-lines N] [--placeholder-style angle|brace|upper]

Columns: path, line, lang, lines, chars, tier, flags.

`tier` is read from the fence info string when the corpus already carries one
(```python tier=run), otherwise reported as `unset` — the audit treats unset as
tier Run, so silence is never an excuse for an untested sample.

Judgement checks (does the symbol still exist, is the documented output current,
does the sibling-language sample do the same thing) are deliberately out of
scope: they need the product, not a regex. Treat every flag as a candidate to
confirm, not a verdict — a docs page about credential rotation legitimately
contains a key-shaped string.
"""

import argparse
import json
import os
import re
import sys

FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([^\s`]*)\s*(.*)$")
TIER_INFO = re.compile(r"\btier\s*=\s*(compile-only|compile|run|illustrative)\b", re.I)

SHELL_LANGS = {"bash", "sh", "shell", "zsh", "console", "terminal", "powershell", "ps", "cmd"}
PROMPT = re.compile(r"^\s*(\$|#|>|PS[^>]*>)\s+\S")
ELLIPSIS = re.compile(r"(^|\s)(\.\.\.|…)(\s|$)|&hellip;|&#8230;")
SECRET = re.compile(
    r"(sk_live_|pk_live_|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,})"
)
LONG_LITERAL = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|passwd|client[_-]?secret)\b\s*[:=]\s*"
    r"[\"']([A-Za-z0-9/+_-]{16,})[\"']"
)
INSECURE = re.compile(
    r"(--insecure\b|--no-check-certificate\b|verify\s*=\s*False|rejectUnauthorized\s*:\s*false|"
    r"InsecureSkipVerify\s*:\s*true|curl\s+(-k|\S*\s-k)\b|NODE_TLS_REJECT_UNAUTHORIZED)"
)
DESTRUCTIVE = re.compile(
    r"(rm\s+-[a-z]*[rf][a-z]*\s+/|\bDROP\s+(TABLE|DATABASE|SCHEMA)\b|\bTRUNCATE\s+TABLE\b|"
    r"\bDELETE\s+FROM\s+\w+\s*;|git\s+push\s+--force\b|kubectl\s+delete\s+(ns|namespace)\b|"
    r"\bmkfs\b|\bdd\s+if=.*of=/dev/)",
    re.I,
)
PLACEHOLDER_STYLES = {
    "angle": re.compile(r"<[A-Za-z0-9_ -]{2,40}>"),
    "brace": re.compile(r"\{\{?[A-Za-z0-9_ -]{2,40}\}?\}"),
    "upper": re.compile(r"\b(YOUR|MY|EXAMPLE)_[A-Z0-9_]{2,40}\b"),
}
TRAILING_WS = re.compile(r"[ \t]+$")
OUTPUT_HINT = re.compile(r"^\s*[\[{]|^\s*(HTTP/|\w+:\s|\|)|^\s*(Error|Traceback|Exception)\b")


def blocks(path, text):
    """Yield (start_line, lang, info, body_lines) for each fenced block."""
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        opened = FENCE_OPEN.match(lines[index])
        # A fence only opens when the marker is at the start of the trimmed line.
        if not opened or not lines[index].lstrip().startswith(("```", "~~~")):
            index += 1
            continue
        indent, marker, lang, info = opened.groups()
        closer = re.compile(r"^\s*" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*$")
        body = []
        cursor = index + 1
        while cursor < len(lines) and not closer.match(lines[cursor]):
            body.append(lines[cursor])
            cursor += 1
        yield index + 1, lang, info, body
        index = cursor + 1


def lint(lang, info, body, args):
    flags = []
    text = "\n".join(body)
    lowered = (lang or "").lower()

    if not lang:
        flags.append("no-language-id")
    if lowered in SHELL_LANGS or not lang:
        prompted = [line for line in body if PROMPT.match(line)]
        if prompted:
            flags.append("prompt-char")
        # Output glued under a command in the same block defeats copy-paste.
        if prompted and any(OUTPUT_HINT.match(line) for line in body):
            flags.append("output-in-command-block")
    if ELLIPSIS.search(text):
        flags.append("ellipsis-omission")
    if SECRET.search(text) or LONG_LITERAL.search(text):
        flags.append("credential-shaped-literal")
    if INSECURE.search(text):
        flags.append("insecure-switch")
    if DESTRUCTIVE.search(text):
        flags.append("destructive-command")
    if any(TRAILING_WS.search(line) for line in body):
        flags.append("trailing-whitespace")
    if len(body) > args.max_lines:
        flags.append("over-length")

    expected = PLACEHOLDER_STYLES[args.placeholder_style]
    others = [name for name, rx in PLACEHOLDER_STYLES.items()
              if name != args.placeholder_style and rx.search(text)]
    if others and not expected.search(text):
        flags.append("placeholder-style:" + ",".join(others))

    tier = TIER_INFO.search(info or "")
    return (tier.group(1).lower() if tier else "unset"), flags


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("docs_dir")
    parser.add_argument("--format", choices=["tsv", "json", "summary"], default="tsv")
    parser.add_argument("--ext", default=".md,.mdx,.markdown")
    parser.add_argument("--max-lines", type=int, default=40)
    parser.add_argument("--placeholder-style", choices=sorted(PLACEHOLDER_STYLES),
                        default="angle")
    args = parser.parse_args()

    if not os.path.isdir(args.docs_dir):
        sys.exit(f"not a directory: {args.docs_dir}")

    extensions = tuple(e if e.startswith(".") else "." + e for e in args.ext.split(","))
    rows = []
    for root, dirs, files in os.walk(args.docs_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules"]
        for name in sorted(files):
            if not name.endswith(extensions):
                continue
            path = os.path.join(root, name)
            with open(path, "r", encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            for line, lang, info, body in blocks(path, text):
                if not body:
                    continue
                tier, flags = lint(lang, info, body, args)
                rows.append({
                    "path": os.path.relpath(path, args.docs_dir),
                    "line": line,
                    "lang": lang or "",
                    "lines": len(body),
                    "chars": sum(len(l) for l in body),
                    "tier": tier,
                    "flags": flags,
                })

    if args.format == "json":
        json.dump(rows, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return

    if args.format == "tsv":
        print("path\tline\tlang\tlines\tchars\ttier\tflags")
        for row in rows:
            print("\t".join([row["path"], str(row["line"]), row["lang"], str(row["lines"]),
                             str(row["chars"]), row["tier"], ",".join(row["flags"]) or "-"]))
        return

    counts = {}
    for row in rows:
        for flag in row["flags"] or ["clean"]:
            counts[flag.split(":")[0]] = counts.get(flag.split(":")[0], 0) + 1
    languages = {}
    for row in rows:
        languages[row["lang"] or "(none)"] = languages.get(row["lang"] or "(none)", 0) + 1
    print(f"samples: {len(rows)}  files: {len({r['path'] for r in rows})}")
    print("languages: " + ", ".join(f"{k}={v}" for k, v in sorted(
        languages.items(), key=lambda kv: -kv[1])))
    print("tiers: " + ", ".join(f"{k}={v}" for k, v in sorted(
        {r["tier"]: sum(1 for x in rows if x["tier"] == r["tier"]) for r in rows}.items())))
    print("flags:")
    for flag, count in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {flag}: {count}")


if __name__ == "__main__":
    main()
