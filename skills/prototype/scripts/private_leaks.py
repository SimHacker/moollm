#!/usr/bin/env python3
"""Find private repo names in public checkouts: every git-tracked text file, file:line per hit.

The private names come from visibility.py (PRIVATE-REPOS.yml in a private sibling checkout, plus
the naming rule). A hit is an owner/name slug, a private checkout dir name followed by '/', or
'../<dir>'; moollm:// refs and GitHub URLs are caught by those. A dir name after '=', '?', '@',
'.', a letter, or inside a URL on another host (news.ycombinator.com/user?id=..., x.com/...) is
a public username, not a hit.

Usage: private_leaks.py [--root DIR] [--repo NAME ...] [--summary] [--untracked]
  --root       directory holding the sibling repos (default: moollm's parent)
  --repo       scan only these public checkouts (dir names)
  --summary    counts per checkout and per name, no lines
  --untracked  also scan untracked files that are not ignored
Exit status 1 when there is any hit.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import visibility  # noqa: E402

SNIPPET = 140


def grep(checkout: Path, names: set[str], untracked: bool) -> list[tuple[str, int, str]]:
    """(file, line, text) for lines that mention any name, case-insensitive; git grep pre-filters."""
    pat = "|".join(re.escape(n) for n in sorted(names))
    cmd = ["git", "-C", str(checkout), "grep", "-n", "-z", "-I", "-i", "-E", "-e", pat]
    if untracked:
        cmd.insert(4, "--untracked")
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=600).stdout.decode("utf-8", "replace")
    except (OSError, subprocess.SubprocessError):
        return []
    rows = []
    for line in out.splitlines():
        parts = line.split("\0", 2)
        if len(parts) == 3 and parts[1].isdigit():
            rows.append((parts[0], int(parts[1]), parts[2]))
    return rows


def scan(v: visibility.Visibility, repos: list[str] | None = None, untracked: bool = False
         ) -> list[tuple[str, str, int, str, str]]:
    """(checkout, file, line, name, snippet) for every hit in the public checkouts."""
    names = v.private_names()
    if not names:
        return []
    keys = {n.split("/")[-1] for n in names} | names
    hits = []
    for d in v.public_checkouts():
        if repos and d.name not in repos:
            continue
        for f, n, text in grep(d, keys, untracked):
            for name in dict.fromkeys(v.find(text)):
                i = max(0, text.lower().find(name.lower()) - SNIPPET // 3)
                hits.append((d.name, f, n, name, text[i:i + SNIPPET].strip()))
    return hits


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=Path, default=visibility.DEFAULT_ROOT)
    ap.add_argument("--repo", nargs="+", metavar="NAME")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--untracked", action="store_true")
    args = ap.parse_args(argv)
    v = visibility.Visibility(args.root)
    if args.repo:
        bad = [r for r in args.repo if v.is_private(r)]
        if bad:
            print(f"not public, not scanned: {', '.join(bad)}", file=sys.stderr)
    hits = scan(v, args.repo, args.untracked)
    if args.summary:
        for repo, c in Counter(h[0] for h in hits).most_common():
            files = len({h[1] for h in hits if h[0] == repo})
            print(f"  {repo:28} {c:5} hits in {files} files")
        for name, c in Counter(h[3] for h in hits).most_common():
            print(f"  name {name:28} {c:5}")
    else:
        for repo, f, n, name, snip in hits:
            print(f"{repo}/{f}:{n}: {name}: {snip}")
    scanned = len([d for d in v.public_checkouts() if not args.repo or d.name in args.repo])
    print(f"public checkouts scanned: {scanned}; private names: {len(v.private_names())}; "
          f"hits: {len(hits)} in {len({(h[0], h[1]) for h in hits})} files")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
