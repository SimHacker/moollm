#!/usr/bin/env python3
"""refs.py — cross-repo references for MOOLLM objects.

One canonical form:

    moollm://github/<owner>/<repo>/<path>[#slot.path]

A directory ref ends in `/`. The resolver maps it to a sibling checkout when one exists
under a root (`<root>/<repo>/<path>`), else to GitHub (`blob/main` for files, `tree/main`
for directories).

Accepted spellings (read, never emitted):
  moollm://github/SimHacker/moollm/skills/real-being/
  https://github.com/SimHacker/moollm/tree/main/examples/...   (also blob/, raw.githubusercontent.com)
  moollm/examples/...           first segment is a known repo (KNOWN_REPOS)
  SimHacker/moollm/examples/... owner/repo prefix
  {repo: SimHacker/moollm, path: moollm/examples/..., absolute_url: ..., canonical_dir: ...,
   character_url: ..., card: ..., character_yml: ...}   the wwsff cast/profile map
  {ref: ...}                    a modulated parent; the ref is parsed
  ../../characters/palm/CHARACTER.yml, skills/animal, ROOM.yml#objects.bench   relative

Bare ids, K-lines and prose are not refs here (parse_ref returns None); resolve.py handles
them. Nothing raises on bad input: unparseable values give None and callers report.

Roots, searched in order: $MOOLLM_ROOTS (os.pathsep-separated), then the directory holding
the moollm checkout this file lives in.

Usage:
    refs.py parse  VALUE              print the Ref and its canonical URI
    refs.py locate VALUE [--from FILE]  print the local path or GitHub URL

Standard library plus PyYAML. Read-only.
"""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

SCHEME = "moollm://github/"
DEFAULT_OWNER = "SimHacker"
DEFAULT_BRANCH = "main"
# Owners checked against `git remote get-url origin` of each sibling checkout, 2026-10-29.
KNOWN_REPOS = {
    "moollm": "SimHacker",
    "WillWrightShowForFood": "SimHacker",
    "DonHopkins": "SimHacker",
    "MicropolisCore": "SimHacker",
    "RepoShow": "SimHacker",
    "RepoShowPrivate": "SimHacker",
    "mooco": "SimHacker",
}
_REPO_BY_LOWER = {k.lower(): k for k in KNOWN_REPOS}
_OWNERS_LOWER = {v.lower(): v for v in KNOWN_REPOS.values()}

GITHUB_URL = re.compile(r"^https?://(?:www\.)?github\.com/([^/]+)/([^/?#]+)(?:/(tree|blob)/([^/?#]+)(/[^?#]*)?)?/?(?:\?[^#]*)?$")
RAW_URL = re.compile(r"^https?://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/([^?#]*)")
PATH_LIKE = re.compile(r"^[\w.~@+,-][\w./~@+,-]*$")
LINE_ANCHOR = re.compile(r"^L\d+(-L\d+)?$")
# Keys of the map form, in the order they're trusted.
URL_KEYS = ("absolute_url", "url", "character_url", "canonical_url")
PATH_KEYS = ("canonical_dir", "path")
FILE_KEYS = ("character_yml", "card")


@dataclass(frozen=True)
class Ref:
    owner: str | None   # None, with repo None: relative to the referring file
    repo: str | None
    path: str           # posix, no leading or trailing slash; "" is the repo root (or the same file)
    fragment: str = ""  # slot path inside the file, as in SCHEMA.md `file#path`
    kind: str = "dir"   # file | dir

    @property
    def relative(self) -> bool:
        return self.repo is None


def default_roots() -> list[Path]:
    roots = [Path(p) for p in os.environ.get("MOOLLM_ROOTS", "").split(os.pathsep) if p.strip()]
    here = Path(__file__).resolve().parent
    checkout = next((p for p in [here, *here.parents] if (p / ".git").exists()), None)
    if checkout:
        roots.append(checkout.parent)
    return norm_roots(roots)


def norm_roots(roots: list[Path] | list[str] | None) -> list[Path]:
    if roots is None:
        return default_roots()
    out: list[Path] = []
    for r in roots:
        p = Path(os.path.normpath(Path(r).expanduser().absolute()))
        if p not in out:
            out.append(p)
    return out


def canonical_repo(owner: str | None, repo: str) -> tuple[str, str]:
    """Known repos get their canonical spelling and owner; GitHub names are case-insensitive."""
    repo = repo[:-4] if repo.endswith(".git") else repo
    known = _REPO_BY_LOWER.get(repo.lower())
    if known and (owner is None or owner.lower() == KNOWN_REPOS[known].lower()):
        return KNOWN_REPOS[known], known
    return owner or DEFAULT_OWNER, repo


def guess_kind(path: str, trailing_slash: bool) -> str:
    if trailing_slash or not path:
        return "dir"
    last = path.rsplit("/", 1)[-1]
    return "file" if "." in last.strip(".") else "dir"


def clean_path(path: str) -> str:
    """Repo path without `.`, doubled slashes, or leading and trailing slashes."""
    return posixpath.normpath("/" + path.strip()).lstrip("/") if path.strip() else ""


def _absolute(owner: str | None, repo: str, path: str, fragment: str, kind: str | None = None) -> Ref | None:
    if not repo or "/" in repo or not PATH_LIKE.match(repo) or (owner is not None and not PATH_LIKE.match(owner)):
        return None
    if ".." in path.split("/"):
        return None  # a repo path never escapes its repo
    trailing = path.endswith("/")
    cleaned = clean_path(path)
    owner, repo = canonical_repo(owner, repo)
    return Ref(owner, repo, cleaned, fragment, kind or guess_kind(cleaned, trailing))


def _parse_string(value: str) -> Ref | None:
    s = value.strip()
    if not s or "\n" in s or len(s) > 500:
        return None
    if s.startswith(SCHEME):
        body, _, frag = s[len(SCHEME):].partition("#")
        parts = body.split("/", 2)
        if len(parts) < 2 or not parts[0] or not parts[1]:
            return None
        return _absolute(parts[0], parts[1], parts[2] if len(parts) > 2 else "", frag)
    m = GITHUB_URL.match(s.split("#", 1)[0]) if "github.com" in s else None
    if m:
        owner, repo, mode, _branch, path = m.groups()
        frag = s.partition("#")[2]
        frag = "" if LINE_ANCHOR.match(frag) else frag
        kind = {"tree": "dir", "blob": "file"}.get(mode or "", "dir")
        return _absolute(owner, repo, (path or "").lstrip("/"), frag, kind)
    m = RAW_URL.match(s)
    if m:
        owner, repo, _branch, path = m.groups()
        return _absolute(owner, repo, path, "", "file")
    if "://" in s:
        return None
    path, _, frag = s.partition("#")
    if path and not PATH_LIKE.match(path):
        return None  # prose
    segs = [p for p in path.split("/") if p]
    if len(segs) >= 2 and segs[0].lower() in _OWNERS_LOWER and segs[1].lower() in _REPO_BY_LOWER:
        return _absolute(segs[0], segs[1], "/".join(segs[2:]) + ("/" if path.endswith("/") else ""), frag)
    if segs and segs[0].lower() in _REPO_BY_LOWER and "/" in path:
        return _absolute(None, segs[0], "/".join(segs[1:]) + ("/" if path.endswith("/") else ""), frag)
    if not path and frag:
        return Ref(None, None, "", frag, "file")  # "#objects.bench": the same file
    if "/" in path or path in (".", "..") or guess_kind(path, False) == "file":
        trailing = path.endswith("/")
        rel = posixpath.normpath(path) if path else ""
        return Ref(None, None, "" if rel == "." else rel, frag, guess_kind(rel, trailing or rel.endswith("..")))
    return None  # bare id, K-line


def _repo_field(value: Any) -> tuple[str | None, str] | None:
    if not isinstance(value, str) or not value.strip():
        return None
    v = value.strip().rstrip("/")
    m = GITHUB_URL.match(v)
    if m:
        return m.group(1), m.group(2)
    parts = v.split("/")
    if len(parts) == 2:
        return parts[0], parts[1]
    if len(parts) == 1:
        return None, parts[0]
    return None


def _parse_map(value: dict[Any, Any]) -> Ref | None:
    if "ref" in value:
        return parse_ref(value["ref"])
    for key in URL_KEYS:
        r = parse_ref(value.get(key)) if isinstance(value.get(key), str) else None
        if r and not r.relative:
            return r
    repo = _repo_field(value.get("repo"))
    if repo:
        owner, name = repo
        for key in PATH_KEYS:
            p = value.get(key)
            if isinstance(p, str):
                segs = p.strip().lstrip("/").split("/")
                if len(segs) > 1 and segs[0].lower() == name.lower():
                    p = "/".join(segs[1:])  # legacy `path: moollm/examples/...` repeats the repo
                return _absolute(owner, name, p, "")
        return _absolute(owner, name, "", "")
    for key in FILE_KEYS:
        r = parse_ref(value.get(key)) if isinstance(value.get(key), str) else None
        if r and not r.relative:
            return r
    if isinstance(value.get("path"), str):
        return parse_ref(value["path"])
    return None


def parse_ref(value: Any, base: Path | str | None = None, roots: list[Path] | None = None) -> Ref | None:
    """Any accepted spelling to a Ref, or None. With `base` (the referring file), a relative
    path that lands inside a checkout under `roots` becomes an absolute Ref."""
    try:
        if isinstance(value, str):
            ref = _parse_string(value)
        elif isinstance(value, dict):
            ref = _parse_map(value)
        elif isinstance(value, Ref):
            ref = value
        else:
            return None
        if ref is not None and ref.relative and base is not None:
            return absolutize(ref, base, roots) or ref
        return ref
    except (TypeError, ValueError, RecursionError):
        return None


def to_uri(ref: Ref | None) -> str | None:
    """The canonical moollm:// form. Relative refs have none until absolutized."""
    if ref is None or ref.relative or ref.owner is None:
        return None
    path = ref.path + ("/" if ref.kind == "dir" and ref.path else "")
    return f"{SCHEME}{ref.owner}/{ref.repo}/{path}" + (f"#{ref.fragment}" if ref.fragment else "")


def github_url(ref: Ref | None, branch: str = DEFAULT_BRANCH) -> str | None:
    if ref is None or ref.relative or ref.owner is None:
        return None
    base = f"https://github.com/{ref.owner}/{ref.repo}"
    if not ref.path:
        return base
    return f"{base}/{'tree' if ref.kind == 'dir' else 'blob'}/{branch}/{ref.path}"


def _base_dir(base: Path | str) -> Path:
    b = Path(os.path.normpath(Path(base).expanduser().absolute()))
    if b.is_dir() or (not b.exists() and not b.suffix):
        return b
    return b.parent


def checkout_of(path: Path, roots: list[Path]) -> tuple[Path, str, str] | None:
    """(checkout dir, owner, repo) for the sibling checkout containing `path`."""
    for root in roots:
        try:
            rel = path.relative_to(root)
        except ValueError:
            continue
        if not rel.parts:
            continue
        checkout = root / rel.parts[0]
        owner, repo = remote_of(checkout) or canonical_repo(None, rel.parts[0])
        return checkout, owner, repo
    return None


def remote_of(checkout: Path) -> tuple[str, str] | None:
    """owner/repo from the checkout's .git/config origin url; None for a known repo or no config."""
    if checkout.name.lower() in _REPO_BY_LOWER:
        return None
    try:
        text = (checkout / ".git" / "config").read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    m = re.search(r'\[remote "origin"\][^\[]*?url\s*=\s*\S*github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?\s', text + "\n")
    return (m.group(1), m.group(2)) if m else None


def absolutize(ref: Ref, base: Path | str, roots: list[Path] | None = None) -> Ref | None:
    """A relative Ref, read from the file `base`, as an absolute Ref; None outside every checkout."""
    if not ref.relative:
        return ref
    try:
        target = Path(os.path.normpath(_base_dir(base) / ref.path)) if ref.path else Path(os.path.normpath(Path(base).absolute()))
        found = checkout_of(target, norm_roots(roots))
    except (OSError, ValueError):
        return None
    if not found:
        return None
    checkout, owner, repo = found
    path = target.relative_to(checkout).as_posix()
    return Ref(owner, repo, "" if path == "." else path, ref.fragment, ref.kind)


def locate(ref: Ref | str | dict[Any, Any] | None, from_file: Path | str | None = None,
           roots: list[Path] | None = None) -> Path | str | None:
    """A local Path when the target exists in a sibling checkout, else its GitHub URL.

    Relative refs are tried against the referring file's directory and then each enclosing
    directory up to its checkout (the walk resolve.py does for repo paths). None when nothing
    can be determined: unparseable, or relative with no `from_file`.
    """
    try:
        r = ref if isinstance(ref, Ref) else parse_ref(ref)
        if r is None:
            return None
        roots = norm_roots(roots)
        if r.relative:
            if from_file is None:
                return None
            if not r.path:
                return Path(os.path.normpath(Path(from_file).absolute()))
            start = _base_dir(from_file)
            found = checkout_of(start, roots)
            for anc in [start, *start.parents]:
                cand = Path(os.path.normpath(anc / r.path))
                if cand.exists():
                    return cand
                if found is None or anc == found[0]:
                    break
            return github_url(absolutize(r, from_file, roots))
        for root in roots:
            cand = root / r.repo / r.path if r.path else root / r.repo
            if cand.exists():
                return cand
        return github_url(r)
    except (OSError, ValueError, TypeError):
        return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    pa = sub.add_parser("parse", help="print the normalized Ref and canonical URI")
    pa.add_argument("value", help="a ref string, or a YAML/JSON map")
    lo = sub.add_parser("locate", help="print the local path or GitHub URL")
    lo.add_argument("value")
    lo.add_argument("--from", dest="from_file", help="the referring file, for relative refs")
    args = ap.parse_args(argv)
    try:
        value = yaml.safe_load(args.value) if args.value.lstrip().startswith("{") else args.value
    except yaml.YAMLError:
        value = args.value
    ref = parse_ref(value, base=getattr(args, "from_file", None))
    if args.cmd == "parse":
        print(ref if ref else "not a ref")
        if ref and to_uri(ref):
            print(to_uri(ref))
        return 0 if ref else 1
    where = locate(ref, args.from_file)
    print(where if where is not None else "not found")
    return 0 if where is not None else 1


if __name__ == "__main__":
    sys.exit(main())
