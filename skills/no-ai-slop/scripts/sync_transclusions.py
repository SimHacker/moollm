#!/usr/bin/env python3
"""Keep transcluded skills byte-identical to their upstream repos.

Reads ../TRANSCLUSIONS.yml. For each entry it shallow-clones `upstream.repo` at
`upstream.ref` and compares that tree with the local copy at `path`.

    --check   report: up to date, upstream moved, or local copy edited
    --update  replace the local copy with upstream and record the new commit

--update refuses when the local copy differs from the recorded commit, because
that means someone edited a transcluded file. Fixes belong upstream; behavior
changes belong in the host's CARD.yml.

Projections are the host's summaries of the organelle (GLANCE, CARD, SKILL).
They are written by hand or by an LLM, never by this script. It only reports
them stale when `projections.built_from` lags the copy, and names the source
files that changed and the targets to rebuild.

Needs git and PyYAML (already used by scripts/pre-commit).
"""

from __future__ import annotations

import argparse
import filecmp
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

SKILL_DIR = Path(__file__).resolve().parent.parent
MANIFEST = SKILL_DIR / "TRANSCLUSIONS.yml"


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


def clone(repo: str, ref: str, commit: str | None, into: Path) -> str:
    """Shallow-clone `ref`, or fetch exactly `commit` if given. Returns the HEAD sha."""
    if commit:
        git("init", "-q", str(into))
        git("remote", "add", "origin", repo, cwd=into)
        git("fetch", "-q", "--depth", "1", "origin", commit, cwd=into)
        git("checkout", "-q", "FETCH_HEAD", cwd=into)
    else:
        git("clone", "-q", "--depth", "1", "--branch", ref, repo, str(into))
    return git("rev-parse", "HEAD", cwd=into)


def tree(root: Path, exclude: list[str]) -> set[str]:
    return {
        str(p.relative_to(root))
        for p in root.rglob("*")
        if p.is_file() and not any(part in exclude for part in p.relative_to(root).parts)
    }


def differences(a: Path, b: Path, exclude: list[str]) -> list[str]:
    ta, tb = tree(a, exclude), tree(b, exclude)
    out = [f"only local:    {f}" for f in sorted(ta - tb)]
    out += [f"only upstream: {f}" for f in sorted(tb - ta)]
    out += [
        f"changed:       {f}"
        for f in sorted(ta & tb)
        if not filecmp.cmp(a / f, b / f, shallow=False)
    ]
    return out


def skill_version(root: Path) -> str | None:
    skill = root / "SKILL.md"
    if not skill.exists():
        return None
    m = re.search(r'^\s*version:\s*"?([^"\n]+)"?', skill.read_text(), re.M)
    return m.group(1).strip() if m else None


def record(name: str, sha: str, committed: str, version: str | None) -> None:
    """Rewrite commit/committed/version lines inside one entry, keeping every comment."""
    lines = MANIFEST.read_text().splitlines(keepends=True)
    inside = False
    for i, line in enumerate(lines):
        if re.match(rf"^  {re.escape(name)}:\s*$", line):
            inside = True
            continue
        if inside and re.match(r"^  \S", line):
            break
        if not inside:
            continue
        for key, value in (("commit", sha), ("committed", committed), ("version", version)):
            if value is None:
                continue
            m = re.match(rf"^(\s+{key}:\s*)(\S+)(.*)$", line.rstrip("\n"))
            if m:
                lines[i] = f"{m.group(1)}{value}{m.group(3)}\n"
    MANIFEST.write_text("".join(lines))


def projection_sources(entry: dict) -> set[str]:
    targets = (entry.get("projections") or {}).get("targets") or {}
    return {src.split("#", 1)[0] for t in targets.values() for src in t.get("from", [])}


def check_projections(name: str, entry: dict, local: Path, tmp: Path) -> int:
    """Stale when built_from differs from the pinned commit. Lists which source files changed."""
    proj = entry.get("projections")
    if not proj:
        return 0
    built, pinned = proj.get("built_from"), entry["upstream"]["commit"]
    if built == pinned:
        print(f"{name}: projections current (built from {built[:7]})")
        return 0
    old = tmp / "built"
    clone(entry["upstream"]["repo"], entry["upstream"]["ref"], built, old)
    changed = sorted(
        f for f in projection_sources(entry)
        if not (old / f).exists() or not (local / f).exists()
        or not filecmp.cmp(old / f, local / f, shallow=False)
    )
    print(f"{name}: PROJECTIONS STALE, built from {str(built)[:7]}, copy is at {pinned[:7]}")
    for f in changed:
        print(f"  source changed: {f}")
    for target in proj.get("targets", {}):
        print(f"  rebuild: {target}")
    print("  then set projections.built_from to the copy's commit")
    return 1


def sync(name: str, entry: dict, update: bool) -> int:
    up = entry["upstream"]
    local = SKILL_DIR / entry["path"]
    exclude = entry.get("exclude", [".git"])
    with tempfile.TemporaryDirectory() as tmp:
        head_dir, pinned_dir = Path(tmp) / "head", Path(tmp) / "pinned"
        head = clone(up["repo"], up["ref"], None, head_dir)
        pinned = clone(up["repo"], up["ref"], up["commit"], pinned_dir)

        edits = differences(local, pinned_dir, exclude)
        if edits:
            print(f"{name}: LOCAL EDITS against recorded {pinned[:7]} (not allowed):")
            print("\n".join(f"  {d}" for d in edits))
            return 2

        if head == pinned:
            print(f"{name}: up to date at {head[:7]}")
            return check_projections(name, entry, local, Path(tmp))

        moved = differences(local, head_dir, exclude)
        print(f"{name}: upstream moved {pinned[:7]} -> {head[:7]}, {len(moved)} file(s):")
        print("\n".join(f"  {d}" for d in moved))
        if not update:
            return 1

        shutil.rmtree(local)
        shutil.copytree(head_dir, local, ignore=shutil.ignore_patterns(*exclude))
        committed = git("log", "-1", "--format=%cI", cwd=head_dir)
        record(name, head, committed, skill_version(head_dir))
        print(f"{name}: updated to {head[:7]}.")
        entry["upstream"]["commit"] = head
        return max(1, check_projections(name, entry, local, Path(tmp)))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="report only (default)")
    mode.add_argument("--update", action="store_true", help="copy upstream over the local copy")
    ap.add_argument("names", nargs="*", help="entries to sync (default: all)")
    args = ap.parse_args(argv)

    entries = yaml.safe_load(MANIFEST.read_text())["transclusions"]
    names = args.names or list(entries)
    status = 0
    for name in names:
        if name not in entries:
            print(f"{name}: not in {MANIFEST.name}")
            status = max(status, 2)
            continue
        try:
            status = max(status, sync(name, entries[name], args.update))
        except subprocess.CalledProcessError as e:
            print(f"{name}: git failed: {e.stderr.strip() or e}")
            status = max(status, 2)
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
