#!/usr/bin/env python3
"""Collect per-page search signals for a documentation site.

Reads a sitemap (index files are followed one level) or a plain URL list, fetches
each page, and extracts the signals a docs SEO pass acts on: title, meta
description, canonical, robots directives (meta tag and HTTP header), h1, rough
word count and internal link count.

Only the standard library is used, so it runs anywhere Python 3.9+ is available.

Usage:
    python3 docs-seo-crawl.py https://docs.example.com/sitemap.xml --out pages.csv --summary
    python3 docs-seo-crawl.py --urls urls.txt --out pages.csv --limit 200
    python3 docs-seo-crawl.py https://docs.example.com/sitemap.xml --format json --delay 0.5
"""

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

UA = "docs-seo-crawl/1.0 (+documentation SEO audit)"
TAG_RE = re.compile(r"<(script|style|nav|header|footer)\b.*?</\1>", re.S | re.I)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
LINK_RE = re.compile(r"""<a\s[^>]*href=["']([^"'#]+)""", re.I)
META_RE = re.compile(r"<meta\s[^>]*>", re.I)
CANON_RE = re.compile(r"""<link\s[^>]*rel=["']canonical["'][^>]*>""", re.I)
ATTR_RE = re.compile(r"""(\w[\w:-]*)\s*=\s*["']([^"']*)["']""")
STRIP_RE = re.compile(r"<[^>]+>")


def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read(3_000_000).decode(resp.headers.get_content_charset() or "utf-8", "replace")
        return resp.status, resp.geturl(), dict(resp.headers), body


def clean(text):
    return re.sub(r"\s+", " ", STRIP_RE.sub(" ", text or "")).strip()


def attrs(tag):
    return {k.lower(): v for k, v in ATTR_RE.findall(tag)}


def read_sitemap(url, timeout, depth=0):
    """Return [(loc, lastmod)]. Follows a sitemap index one level down."""
    try:
        _, _, _, body = fetch(url, timeout)
    except Exception as exc:  # network, TLS, HTTP — all equally fatal for this URL
        print(f"sitemap unreachable: {url}: {exc}", file=sys.stderr)
        return []
    entries = re.findall(r"<(sitemap|url)\b(.*?)</\1>", body, re.S | re.I)
    out = []
    for kind, chunk in entries:
        loc = re.search(r"<loc>\s*(.*?)\s*</loc>", chunk, re.S | re.I)
        if not loc:
            continue
        loc = loc.group(1).strip()
        if kind.lower() == "sitemap":
            if depth == 0:
                out.extend(read_sitemap(loc, timeout, depth + 1))
            continue
        mod = re.search(r"<lastmod>\s*(.*?)\s*</lastmod>", chunk, re.S | re.I)
        out.append((loc, mod.group(1).strip() if mod else ""))
    return out


def inspect(url, lastmod, timeout, delay):
    row = {"url": url, "sitemap_lastmod": lastmod, "status": "", "final_url": "",
           "title": "", "description": "", "canonical": "", "meta_robots": "",
           "x_robots_tag": "", "h1": "", "h1_count": 0, "words": 0, "outbound_links": 0,
           "inbound_links": 0, "error": ""}
    targets = set()
    if delay:
        time.sleep(delay)
    try:
        status, final, headers, body = fetch(url, timeout)
    except urllib.error.HTTPError as exc:
        row["status"] = exc.code
        row["error"] = "http error"
        return row, targets
    except Exception as exc:
        row["error"] = str(exc)[:120]
        return row, targets

    row["status"] = status
    row["final_url"] = final
    row["x_robots_tag"] = headers.get("X-Robots-Tag", "")

    title = TITLE_RE.search(body)
    row["title"] = clean(title.group(1)) if title else ""

    for tag in META_RE.findall(body):
        a = attrs(tag)
        name = (a.get("name") or "").lower()
        if name == "description":
            row["description"] = clean(a.get("content", ""))
        elif name in ("robots", "googlebot"):
            row["meta_robots"] = (row["meta_robots"] + " " + a.get("content", "")).strip()

    canon = CANON_RE.search(body)
    if canon:
        row["canonical"] = urllib.parse.urljoin(final, attrs(canon.group(0)).get("href", ""))

    h1s = H1_RE.findall(body)
    row["h1_count"] = len(h1s)
    row["h1"] = clean(h1s[0]) if h1s else ""

    text = clean(TAG_RE.sub(" ", body))
    row["words"] = len(text.split())

    host = urllib.parse.urlparse(final).netloc
    links = {urllib.parse.urljoin(final, h) for h in LINK_RE.findall(body)}
    targets |= {l.rstrip("/") for l in links if urllib.parse.urlparse(l).netloc == host}
    targets.discard(final.rstrip("/"))
    row["outbound_links"] = len(targets)
    return row, targets


def summarize(rows):
    titles = Counter(r["title"] for r in rows if r["title"])
    dup_titles = {t: n for t, n in titles.items() if n > 1}
    flags = {
        "pages": len(rows),
        "unreachable": sum(1 for r in rows if r["error"] or (r["status"] and r["status"] != 200)),
        "noindex": sum(1 for r in rows if "noindex" in (r["meta_robots"] + r["x_robots_tag"]).lower()),
        "missing_title": sum(1 for r in rows if not r["title"]),
        "duplicate_title_pages": sum(dup_titles.values()),
        "distinct_duplicate_titles": len(dup_titles),
        "missing_description": sum(1 for r in rows if not r["description"]),
        "missing_canonical": sum(1 for r in rows if not r["canonical"]),
        "cross_canonical": sum(1 for r in rows if r["canonical"] and r["canonical"].rstrip("/") != r["final_url"].rstrip("/")),
        "multiple_h1": sum(1 for r in rows if r["h1_count"] > 1),
        "thin_pages_under_100_words": sum(1 for r in rows if r["words"] < 100 and not r["error"]),
        "dead_end_pages_no_outbound_links": sum(1 for r in rows if r["outbound_links"] == 0 and not r["error"]),
        "orphan_pages_no_inbound_links": sum(1 for r in rows if r["inbound_links"] == 0 and not r["error"]),
    }
    return flags, sorted(dup_titles.items(), key=lambda kv: -kv[1])[:20]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("sitemap", nargs="?", help="sitemap or sitemap-index URL")
    p.add_argument("--urls", help="file with one URL per line, instead of a sitemap")
    p.add_argument("--out", help="write results here (default: stdout)")
    p.add_argument("--format", choices=("csv", "json"), default="csv")
    p.add_argument("--limit", type=int, default=0, help="stop after N URLs (0 = all)")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--delay", type=float, default=0.2, help="seconds each worker waits before a fetch")
    p.add_argument("--timeout", type=float, default=20.0)
    p.add_argument("--summary", action="store_true", help="print issue counts to stderr")
    args = p.parse_args()

    if args.urls:
        with open(args.urls) as fh:
            targets = [(line.strip(), "") for line in fh if line.strip() and not line.startswith("#")]
    elif args.sitemap:
        targets = read_sitemap(args.sitemap, args.timeout)
    else:
        p.error("pass a sitemap URL or --urls")

    if args.limit:
        targets = targets[: args.limit]
    if not targets:
        print("no URLs to crawl", file=sys.stderr)
        return 1

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda t: inspect(t[0], t[1], args.timeout, args.delay), targets))

    # Inbound counts are only meaningful once every page has been fetched, so they
    # are filled in here rather than inside inspect().
    inbound = Counter()
    for _, links in results:
        inbound.update(links)
    rows = []
    for row, _ in results:
        key = (row["final_url"] or row["url"]).rstrip("/")
        row["inbound_links"] = inbound.get(key, 0)
        rows.append(row)

    stream = open(args.out, "w", newline="") if args.out else sys.stdout
    try:
        if args.format == "json":
            json.dump(rows, stream, indent=1)
        else:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    finally:
        if args.out:
            stream.close()

    if args.summary:
        flags, dups = summarize(rows)
        print(json.dumps(flags, indent=1), file=sys.stderr)
        if dups:
            print("most duplicated titles:", file=sys.stderr)
            for title, count in dups:
                print(f"  {count:4d}  {title[:90]}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
