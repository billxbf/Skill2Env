#!/usr/bin/env python3
"""Cluster raw support/issue text into candidate troubleshooting pages.

Reads exported tickets, issues, log lines or search queries, extracts the
error-like strings from each record, normalizes the parts that vary between
occurrences (paths, IDs, numbers, quoted values), and ranks the resulting
clusters by how many records they appear in.

One cluster is one candidate page. The raw examples are kept so the verbatim
error text can be copied into the entry.

Usage:
    python3 scripts/error-cluster.py tickets.csv issues.jsonl notes.txt
    python3 scripts/error-cluster.py export.csv --min-count 3 --top 40
    python3 scripts/error-cluster.py export.jsonl --format json > clusters.json
    cat log.txt | python3 scripts/error-cluster.py -

Input formats are detected per file: .csv/.tsv (all cells of a row form one
record), .json/.jsonl (all string values of an object form one record),
anything else (one line = one record).
"""

import argparse
import csv
import json
import re
import sys
from collections import defaultdict

# Patterns that identify an error-like fragment inside free text. Ordered from
# most specific to most generic; every match is kept, so one record can produce
# several candidate strings.
ERROR_PATTERNS = [
    (r"\bERR_[A-Z0-9_]+\b", 0),                             # Node-style codes
    (r"\b[A-Z]{2,}\d{3,5}\b", 0),                           # SQLSTATE / E0382 / ORA-style
    (r"\bE[A-Z]{3,}\b", 0),                                 # ECONNREFUSED, EACCES
    (r"\b[A-Za-z_][A-Za-z0-9_.]*(?:Error|Exception)\b[^\n]{0,120}", 0),
    (r"(?:^|[\s\"'])(?:error|fatal|panic|warning)\s*:\s*[^\n]{0,120}", re.IGNORECASE),
    (r"\bHTTP\s*(?:status\s*)?[45]\d{2}\b[^\n]{0,80}", re.IGNORECASE),
    (r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)*_(?:error|failed|failure|invalid|denied|declined"
     r"|required|unsupported|expired|missing|exceeded|timeout)\b", 0),
    (r"\b(?:invalid|missing|unknown|unsupported|expired|denied)_[a-z0-9_]+\b", 0),
]

# Variable parts replaced before counting, so two occurrences of the same
# failure with different IDs land in one cluster.
NORMALIZERS = [
    (r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "<UUID>"),
    (r"https?://[^\s'\"]+", "<URL>"),
    (r"[\w.+-]+@[\w-]+\.[\w.]+", "<EMAIL>"),
    (r"(?:/[\w.\-@]+){2,}/?", "<PATH>"),
    (r"[A-Za-z]:\\[^\s'\"]+", "<PATH>"),
    (r"\b[0-9a-fA-F]{7,}\b", "<HEX>"),
    (r"\b\d+(?:\.\d+){2,}\b", "<VERSION>"),
    (r"'[^']*'", "'<VALUE>'"),
    (r'"[^"]*"', '"<VALUE>"'),
    (r"`[^`]*`", "`<VALUE>`"),
    (r"\b\d+\b", "<N>"),
]

DATE_KEYS = ("created_at", "createdat", "date", "created", "opened_at", "timestamp")

# How many characters of the normalized error identify the cluster.
KEY_LENGTH = 60


def records_from_file(path):
    """Yield (text, date_or_None) per record."""
    if path == "-":
        for line in sys.stdin:
            if line.strip():
                yield line.strip(), None
        return

    lower = path.lower()
    if lower.endswith((".csv", ".tsv")):
        delimiter = "\t" if lower.endswith(".tsv") else ","
        with open(path, newline="", encoding="utf-8", errors="replace") as handle:
            for row in csv.DictReader(handle, delimiter=delimiter):
                cells = [str(v) for v in row.values() if v]
                date = next((str(row[k]) for k in row if k and k.lower() in DATE_KEYS and row[k]), None)
                if cells:
                    yield " ".join(cells), date
        return

    if lower.endswith((".json", ".jsonl", ".ndjson")):
        with open(path, encoding="utf-8", errors="replace") as handle:
            content = handle.read().strip()
        objects = []
        if content.startswith("["):
            objects = json.loads(content)
        else:
            objects = [json.loads(line) for line in content.splitlines() if line.strip()]
        for obj in objects:
            if isinstance(obj, dict):
                strings = [str(v) for v in obj.values() if isinstance(v, (str, int, float)) and str(v)]
                date = next((str(obj[k]) for k in obj if k.lower() in DATE_KEYS and obj[k]), None)
                yield " ".join(strings), date
            else:
                yield str(obj), None
        return

    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if line.strip():
                yield line.strip(), None


def extract(text):
    found = []
    for pattern, flags in ERROR_PATTERNS:
        for match in re.finditer(pattern, text, flags):
            fragment = match.group(0).strip().lstrip("\"'")
            if len(fragment) >= 4:
                found.append(re.sub(r"\s+", " ", fragment))
    # A bare code (ENOENT) found inside a fuller message ("Error: ENOENT: no such
    # file…") is the same failure: keep the richest fragment so the cluster label
    # carries the text a reader would actually paste into a search box.
    return [f for f in found if not any(f != other and f in other for other in found)]


def normalize(fragment):
    normalized = fragment
    for pattern, replacement in NORMALIZERS:
        normalized = re.sub(pattern, replacement, normalized)
    return normalized.strip().rstrip(".,;:")


def cluster_key(normalized, key_length=KEY_LENGTH):
    """Group on the head of the message.

    Tickets append prose to the error ("… every time", "… when refreshing the
    token"), which would otherwise split one failure across several clusters.
    The first characters carry the identity; the tail carries the reporter's
    mood.
    """
    return normalized[:key_length]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="+", help="input files, or - for stdin")
    parser.add_argument("--min-count", type=int, default=2, help="drop clusters seen fewer times (default 2)")
    parser.add_argument("--top", type=int, default=50, help="how many clusters to print (default 50)")
    parser.add_argument("--format", choices=["tsv", "json"], default="tsv")
    parser.add_argument(
        "--key-length",
        type=int,
        default=KEY_LENGTH,
        help=f"characters of the normalized error used to group (default {KEY_LENGTH}; "
        "lower it when one failure still splits across clusters)",
    )
    args = parser.parse_args()

    counts = defaultdict(int)
    labels = {}
    examples = defaultdict(list)
    dates = defaultdict(list)
    total_records = 0
    records_with_error = 0

    for path in args.files:
        try:
            records = list(records_from_file(path))
        except (OSError, json.JSONDecodeError) as error:
            sys.exit(f"cannot read {path}: {error}")
        for text, date in records:
            total_records += 1
            fragments = extract(text)
            if fragments:
                records_with_error += 1
            # Count each cluster at most once per record: ten mentions inside one
            # ticket are one occurrence of the problem, not ten.
            for normalized, raw in {normalize(f): f for f in fragments}.items():
                key = cluster_key(normalized, args.key_length)
                counts[key] += 1
                if len(normalized) > len(labels.get(key, "")):
                    labels[key] = normalized
                if len(examples[key]) < 3 and raw not in examples[key]:
                    examples[key].append(raw)
                if date:
                    dates[key].append(date)

    ranked = [(k, v) for k, v in counts.items() if v >= args.min_count]
    ranked.sort(key=lambda item: (-item[1], item[0]))
    ranked = ranked[: args.top]

    if args.format == "json":
        payload = {
            "records_scanned": total_records,
            "records_with_error_text": records_with_error,
            "clusters": [
                {
                    "count": count,
                    "normalized": labels[key],
                    "examples": examples[key],
                    "first_seen": min(dates[key]) if dates[key] else None,
                    "last_seen": max(dates[key]) if dates[key] else None,
                }
                for key, count in ranked
            ],
        }
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return

    print(f"# records scanned: {total_records}\trecords with error text: {records_with_error}")
    print("count\tfirst_seen\tlast_seen\tnormalized\texample")
    for key, count in ranked:
        seen = dates[key]
        first = min(seen) if seen else ""
        last = max(seen) if seen else ""
        print(f"{count}\t{first}\t{last}\t{labels[key]}\t{examples[key][0] if examples[key] else ''}")


if __name__ == "__main__":
    main()
