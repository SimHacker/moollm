#!/usr/bin/env python3
"""Which sibling checkouts are private, read from PRIVATE-REPOS.yml files kept in private repos.

No public file names a private repo. The list lives in a private checkout, at
<root>/<checkout>/PRIVATE-REPOS.yml, one level below the directory holding the sibling repos:

    naming_rule: "any repo whose name contains 'private' (any case) is private"
    repos: [owner/name, ...]
    character_layers: {owner/name: {path: characters/, layer: biography}}

Every such file under the root is merged. A checkout maps to owner/name through
`git -C <dir> remote get-url origin` (its .git/config first, cached). A repo is private when it
is listed (its .wiki too) or its name contains "private". With no file only the naming rule
applies. Nothing here raises on bad input.

    visibility.py [--root DIR]     print the private checkouts and the character layers found
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

FILENAME = "PRIVATE-REPOS.yml"
NAMING_RULE = re.compile("private", re.I)
REMOTE = re.compile(r"[:/]([^/:\s]+)/([^/\s]+?)(?:\.git)?/?$")
DEFAULT_ROOT = Path(__file__).resolve().parents[4]


def _norm_slug(s: str) -> str:
    s = s.strip().strip("/").lower()
    return s[:-5] if s.endswith(".wiki") else s


@lru_cache(None)
def remote_slug(checkout: Path | str) -> str | None:
    """owner/name of the checkout's origin; None when it has none."""
    d = Path(checkout)
    url = None
    try:
        text = (d / ".git" / "config").read_text(encoding="utf-8")
        m = re.search(r'\[remote "origin"\][^\[]*?url\s*=\s*(\S+)', text)
        url = m.group(1) if m else None
    except (OSError, UnicodeDecodeError):
        pass
    if url is None and (d / ".git").exists():
        try:
            url = subprocess.run(["git", "-C", str(d), "remote", "get-url", "origin"],
                                 capture_output=True, text=True, timeout=10).stdout.strip() or None
        except (OSError, subprocess.SubprocessError):
            url = None
    m = REMOTE.search(url) if url else None
    return f"{m.group(1)}/{m.group(2)}" if m else None


def is_checkout(d: Path) -> bool:
    try:
        return d.is_dir() and (d / ".git").exists()
    except OSError:
        return False


class Visibility:
    def __init__(self, root: Path | str = DEFAULT_ROOT) -> None:
        self.root = Path(root).expanduser().resolve()
        self.listed: dict[str, str] = {}
        self.layers: dict[str, tuple[str, str]] = {}
        self.sources: list[Path] = []
        try:
            files = sorted(self.root.glob(f"*/{FILENAME}"))
        except OSError:
            files = []
        for f in files:
            self._read(f)
        self._matcher: re.Pattern[str] | None = None

    def _read(self, f: Path) -> None:
        try:
            doc = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception:
            return
        if not isinstance(doc, dict):
            return
        self.sources.append(f)
        for s in doc.get("repos") or []:
            if isinstance(s, str) and "/" in s.strip("/"):
                self.listed.setdefault(_norm_slug(s), s.strip().strip("/"))
        cl = doc.get("character_layers")
        for s, v in (cl.items() if isinstance(cl, dict) else []):
            if isinstance(s, str) and isinstance(v, dict) and isinstance(v.get("layer"), str):
                path = v.get("path") if isinstance(v.get("path"), str) else ""
                self.layers[_norm_slug(s)] = (path.strip("/") + "/" if path.strip("/") else "",
                                              v["layer"])

    def checkouts(self) -> list[Path]:
        try:
            return sorted(d for d in self.root.iterdir() if is_checkout(d))
        except OSError:
            return []

    def _dir(self, x: Path | str) -> Path | None:
        p = Path(x)
        for cand in ([p] if p.is_absolute() else [self.root / p, p]):
            try:
                if cand.is_dir():
                    return cand.resolve()
            except OSError:
                continue
        return None

    def slug_of(self, x: Path | str) -> str | None:
        d = self._dir(x)
        return remote_slug(d) if d is not None else None

    def _listed_name(self, name: str) -> bool:
        n = name.lower()
        return any(s.split("/", 1)[1] == n for s in self.listed)

    def is_private(self, x: Path | str) -> bool:
        """A checkout dir, an owner/name slug, or a bare repo name."""
        try:
            s = str(x).strip()
            if not s:
                return False
            d = self._dir(x)
            if d is not None:
                slug = remote_slug(d)
                if NAMING_RULE.search(d.name) or (slug and NAMING_RULE.search(slug)):
                    return True
                if slug:
                    return _norm_slug(slug) in self.listed
                return self._listed_name(d.name)
            if NAMING_RULE.search(s):
                return True
            if "/" in s.strip("/"):
                return _norm_slug(s) in self.listed
            return self._listed_name(s)
        except Exception:
            return False

    def public_checkouts(self) -> list[Path]:
        return [d for d in self.checkouts() if not self.is_private(d)]

    def private_checkouts(self) -> list[Path]:
        return [d for d in self.checkouts() if self.is_private(d)]

    def private_names(self) -> set[str]:
        """Listed slugs and the dir names of private checkouts: what a public file must not say."""
        return set(self.listed.values()) | {d.name for d in self.private_checkouts()}

    def character_layer(self, x: Path | str) -> tuple[str, str] | None:
        """(path prefix inside the checkout, layer kind) for a private checkout's characters."""
        try:
            d = self._dir(x)
            if d is None:
                return None
            slug = remote_slug(d)
            if slug and _norm_slug(slug) in self.layers:
                return self.layers[_norm_slug(slug)]
            if not slug:
                n = d.name.lower()
                hit = next((v for s, v in self.layers.items() if s.split("/", 1)[1] == n), None)
                return hit
        except Exception:
            return None
        return None

    def matcher(self) -> re.Pattern[str] | None:
        """One regex for every way a text can name a private repo; None when nothing is private."""
        if self._matcher is not None or not (self.listed or self.private_checkouts()):
            return self._matcher
        owners = {s.split("/", 1)[0] for s in self.listed} | {
            (remote_slug(d) or "/").split("/", 1)[0].lower() for d in self.checkouts()}
        slugs = sorted(self.listed.values(), key=len, reverse=True)
        dirs = sorted({d.name for d in self.private_checkouts()} - {""}, key=len, reverse=True)
        dirs = [n for n in dirs if n.lower() not in owners]
        alts = []
        if slugs:
            alts.append(r"(?i:(?<![\w.-])(?P<slug>" + "|".join(map(re.escape, slugs)) + r")(?:\.wiki)?(?![\w-]))")
        if dirs:
            names = "|".join(map(re.escape, dirs))
            alts.append(r"(?<![\w.=?@-])(?P<dir>" + names + r")/")
            alts.append(r"\.\./(?P<up>" + names + r")(?![\w.-])")
        self._matcher = re.compile("|".join(alts))
        self._canon = {n.lower(): n for n in self.private_names()}
        self._sibling = re.compile(r"^(?:(?:\.\.?/)+|.*/" + re.escape(self.root.name) + r"/|"
                                   r"moollm://github/[^/]+/|(?:https?://)?(?:www\.)?github\.com/[^/]+/|"
                                   r"(?:https?://)?raw\.githubusercontent\.com/[^/]+/)?$", re.I)
        return self._matcher

    def find(self, text: str) -> list[str]:
        """The private names a text contains, in order. A dir name counts only where a path starts
        at the sibling checkout: alone, after ../, <root>/, moollm://github/<owner>/ or a GitHub
        URL; skills/<name>/ in a public repo, or a username on another site, is not one."""
        m = self.matcher()
        if m is None or not isinstance(text, str):
            return []
        out = []
        for hit in m.finditer(text):
            if "dir" in m.groupindex and hit.group("dir"):
                prefix = re.split(r"[\s\"'`(<\[|,;]", text[:hit.start()])[-1]
                if not self._sibling.match(prefix):
                    continue
            name = next(g for g in hit.groups() if g)
            out.append(self._canon.get(name.lower(), name))
        return out


@lru_cache(None)
def get(root: Path | str = DEFAULT_ROOT) -> Visibility:
    return Visibility(Path(root).expanduser().resolve())


def is_private(x: Path | str, root: Path | str = DEFAULT_ROOT) -> bool:
    return get(root).is_private(x)


def private_names(root: Path | str = DEFAULT_ROOT) -> set[str]:
    return get(root).private_names()


def character_layer(x: Path | str, root: Path | str = DEFAULT_ROOT) -> tuple[str, str] | None:
    return get(root).character_layer(x)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="directory holding the sibling repos")
    args = ap.parse_args(argv)
    v = Visibility(args.root)
    print(f"root {v.root}: {len(v.sources)} {FILENAME}, {len(v.listed)} listed repos")
    for d in v.private_checkouts():
        layer = v.character_layer(d)
        print(f"  private {d.name}" + (f"  {layer[0] or '.'} -> {layer[1]}" if layer else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
