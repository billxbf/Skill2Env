#!/usr/bin/env python3
"""Emit mechanical facts about a public GitHub personal or organization profile.

Usage: profile-audit.py <username-or-org>

Reads the public REST API; no authentication required. Set GITHUB_TOKEN to raise
the hourly rate limit and to include pinned items, which are only exposed through
the authenticated GraphQL API. Judgement stays with the caller: this script
reports numbers and never says whether they are good.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
WIDGET_HOSTS = [
    "github-readme-stats",
    "github-readme-streak-stats",
    "github-profile-trophy",
    "readme-typing-svg",
    "github-readme-activity-graph",
    "visitor-badge",
    "komarev.com/ghpvc",
    "hits.seeyoufarm.com",
    "wakatime",
    "spotify-github-profile",
    "leetcode",
]
BIO_LIMIT = 160
SOCIAL_LIMIT = 4
PIN_LIMIT = 6


def get(path, accept="application/vnd.github+json"):
    req = urllib.request.Request(API + path, headers={"Accept": accept, "User-Agent": "profile-audit"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8", "replace")
            return json.loads(body) if accept.endswith("json") else body
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        if err.code in (403, 429):
            sys.exit("RATE LIMITED or FORBIDDEN on %s — set GITHUB_TOKEN and retry" % path)
        raise


def graphql_pins(login):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return None
    query = (
        '{"query":"{ repositoryOwner(login: \\"%s\\") { pinnedItems(first: 6, types: [REPOSITORY, GIST]) '
        '{ totalCount nodes { ... on Repository { nameWithOwner stargazerCount pushedAt } '
        '... on Gist { name } } } } }"}' % login
    )
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=query.encode(),
        headers={"Authorization": "Bearer " + token, "User-Agent": "profile-audit"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode())["data"]["repositoryOwner"]["pinnedItems"]


def readme_facts(text):
    images = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text)
    html_images = re.findall(r"<img\s[^>]*>", text, re.I)
    no_alt = [src for alt, src in images if not alt.strip()]
    no_alt += [tag for tag in html_images if not re.search(r"alt\s*=", tag, re.I)]
    widgets = sorted({w for w in WIDGET_HOSTS if w in text})
    links = re.findall(r"\]\((https?://[^)]+)\)", text)
    stale_phrases = [
        p
        for p in ["currently working on", "🔭", "right now I", "this year", "2019", "2020", "2021", "2022", "2023"]
        if p.lower() in text.lower()
    ]
    return {
        "words": len(text.split()),
        "images": len(images) + len(html_images),
        "images_without_alt": len(no_alt),
        "widgets": widgets,
        "links": len(links),
        "headings": re.findall(r"^#{1,6} .*", text, re.M),
        "time_bound_phrases": stale_phrases,
    }


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    login = sys.argv[1].strip().strip("/").split("/")[-1]

    owner = get("/users/" + login)
    if owner is None:
        sys.exit("NOT FOUND: no user or organization named %s" % login)
    is_org = owner.get("type") == "Organization"
    if is_org:
        # /users/<org> omits is_verified and twitter_username; /orgs/<org> carries them.
        owner.update(get("/orgs/" + login) or {})

    print("TARGET: %s (%s)" % (login, "organization" if is_org else "user"))
    print("FOLLOWERS: %s   PUBLIC REPOS: %s   CREATED: %s" % (owner.get("followers"), owner.get("public_repos"), owner.get("created_at")))

    bio = owner.get("bio") or owner.get("description") or ""
    print("\nPROFILE FIELDS")
    print("  name: %r" % (owner.get("name") or ""))
    print("  bio/description: %d/%d chars %s" % (len(bio), BIO_LIMIT, "EMPTY" if not bio else ""))
    print("  website: %r" % (owner.get("blog") or ""))
    print("  company: %r   location: %r" % (owner.get("company") or "", owner.get("location") or ""))
    if owner.get("is_verified") is not None:
        print("  verified domain badge: %s" % owner.get("is_verified"))
    if not is_org:
        socials = get("/users/%s/social_accounts" % login) or []
        print("  social links: %d/%d %s" % (len(socials), SOCIAL_LIMIT, [s.get("url") for s in socials]))

    print("\nPROFILE README")
    if is_org:
        meta = get("/repos/%s/.github/contents/profile/README.md" % login)
        location = "%s/.github → profile/README.md" % login
        commits = get("/repos/%s/.github/commits?path=profile/README.md&per_page=1" % login)
    else:
        meta = get("/repos/%s/%s/readme" % (login, login))
        location = "%s/%s → README.md" % (login, login)
        commits = get("/repos/%s/%s/commits?path=README.md&per_page=1" % (login, login))
    if not meta:
        print("  MISSING at %s — the profile page shows no README" % location)
    else:
        print("  found at %s (%s bytes)" % (location, meta.get("size")))
        if commits:
            print("  last edited: %s" % commits[0]["commit"]["committer"]["date"])
        else:
            repo = get("/repos/%s/.github" % login) if is_org else get("/repos/%s/%s" % (login, login))
            if repo:
                print("  last push to the hosting repository: %s" % repo.get("pushed_at"))
        with urllib.request.urlopen(urllib.request.Request(meta["download_url"], headers={"User-Agent": "profile-audit"}), timeout=20) as resp:
            raw = resp.read().decode("utf-8", "replace")
        facts = readme_facts(raw)
        print("  words: %d   links: %d   images: %d (%d without alt text)" % (facts["words"], facts["links"], facts["images"], facts["images_without_alt"]))
        print("  headings: %s" % (facts["headings"] or "(none)"))
        if facts["widgets"]:
            print("  third-party widgets: %s  [each is an external dependency the image proxy can cache stale]" % ", ".join(facts["widgets"]))
        if facts["time_bound_phrases"]:
            print("  time-bound phrasing found: %s  [check it is still true]" % ", ".join(facts["time_bound_phrases"]))

    print("\nPINNED ITEMS")
    pins = graphql_pins(login)
    if pins is None:
        print("  UNAVAILABLE without GITHUB_TOKEN — read them off the profile page instead (limit %d)" % PIN_LIMIT)
    else:
        print("  %d/%d used" % (pins["totalCount"], PIN_LIMIT))
        for node in pins["nodes"]:
            print("    %s" % json.dumps(node))

    print("\nMOST-STARRED PUBLIC REPOSITORIES (what a visitor finds when pins are unset)")
    repos = get("/users/%s/repos?per_page=100&type=owner&sort=updated" % login) or []
    top = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:8]
    for repo in top:
        flags = []
        if not repo.get("description"):
            flags.append("no description")
        if not repo.get("topics"):
            flags.append("no topics")
        if repo.get("archived"):
            flags.append("archived")
        if repo.get("fork"):
            flags.append("fork")
        print("  %-40s %6d★  pushed %s  %s" % (repo["name"], repo.get("stargazers_count", 0), (repo.get("pushed_at") or "")[:10], ", ".join(flags)))
    if len(repos) == 100:
        print("  (first 100 repositories only — re-run against the full list if the account has more)")


if __name__ == "__main__":
    main()
