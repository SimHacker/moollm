#!/usr/bin/env python3
"""Lint character layers across sibling repos: same being, several CHARACTER.yml, one set of facts.

Constitution §15 "Layers across repos": each layer carries the core it needs to run alone, and
declares how it relates to the others. designs/object-system/CHARACTER-LAYERS-ANALYSIS.md
(decisions L1-L12) names the core keys and relations. Per id with more than one layer:

  facts       name, status (memorial = deceased), born, died, real_being and
              representation.consent_level agree across layers
  relations   every layer but the canonical one declares inherits:, derived_from: or layers:
              pointing at another layer of the same being; legacy spellings are reported
  refs        declared relation refs resolve to an existing file or directory
  core keys   id, name, status, signifier; real_being and representation.consent_level for
              real beings
  signifier   real living 👤, deceased 🕯️; a topical emoji belongs in emoji:

Layers and envelopes come from layers_survey.py. Refs go through refs.py when it is importable.

Usage: layers_lint.py [ids...] [--root DIR] [--format text|yaml] [--summary] [--review [FILE]]
  --root     directory holding the sibling repos (default: moollm's parent)
  --summary  counts only
  --review   write the disagreements a person must decide (consent, life facts) as YAML;
             FILE defaults to designs/object-system/tasks/ALIGNMENT-REVIEW.yml
Exit status 1 when there are errors.
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import yaml

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import layers_survey as survey  # noqa: E402

try:
    import refs as _refs  # type: ignore  # noqa: E402
except Exception:
    _refs = None

MOOLLM = SCRIPTS.parents[2]
DEFAULT_REVIEW = MOOLLM / "designs" / "object-system" / "tasks" / "ALIGNMENT-REVIEW.yml"

RELATION_KEYS = ["inherits", "derived_from", "layers"]
# legacy spelling -> the L2 relation it most likely becomes
ALIAS_KEYS = {
    "character_ref": "inherits",
    "moollm_source": "inherits",
    "wwsff_local": "inherits",
    "canonical_soul": "inherits",
    "prototype_ref": "inherits",
    "canonical_home": "inherits",
    "moollm_home": "layers",
    "upstream": "derived_from",
    "public_portrayal": "layers",
}
# navigation keys that count as layers: only when they point at another layer of the being
SOFT_KEYS = ["see_also"]
# map keys whose strings are names or prose, never refs
NOT_REF_KEYS = {"repo", "note", "import_mode", "overlay_protocol", "moollm_skills", "lineage"}

# canonical layer, first present wins
REAL_ORDER = ["donhopkins", "wwsff-profile", "adventure", "moollm-other", "micropoliscore",
              "wwsff-cast", "show-audience"]
FICTIONAL_ORDER = ["adventure", "moollm-other", "wwsff-cast", "wwsff-profile", "donhopkins",
                   "show-audience", "micropoliscore"]

LIFE_STATUS = {"living", "deceased"}
STATUS_ALIASES = {"memorial": "deceased", "dead": "deceased", "alive": "living"}
CONSENT_NAMES = {
    "self-sovereign": 1, "self_sovereign": 1, "self": 1,
    "explicit": 2,
    "public-figure": 3, "public_figure": 3, "public": 3,
    "private": 4,
    "deceased": 5, "memorial": 5, "deceased-legacy": 5, "deceased_legacy": 5,
}
SIGNIFIERS = {"living": "👤", "deceased": "🕯️"}

SEVERITY_RANK = {"error": 0, "warning": 1, "info": 2}
REVIEW_RULES = {"consent-level", "fact-status", "fact-born", "fact-died", "fact-real-being"}


@dataclass
class Layer:
    name: str
    repo: str
    rel: str
    path: Path
    data: Any
    f: dict[str, Any] = field(default_factory=dict)

    @property
    def label(self) -> str:
        return self.name

    @property
    def repo_root(self) -> Path:
        return self.path.parents[len(Path(self.rel).parts) - 1]


@dataclass
class Finding:
    id: str
    layers: list[str]
    file: str
    rule: str
    severity: str
    message: str

    def as_dict(self) -> dict[str, Any]:
        return {"id": self.id, "severity": self.severity, "rule": self.rule,
                "layers": self.layers, "file": self.file, "message": self.message}


@dataclass
class Fact:
    layer: Layer
    value: Any
    spelled: str


def load_layers(root: Path) -> tuple[dict[str, list[Layer]], list[Layer]]:
    """Group parseable CHARACTER.yml by id; unparseable files come back separately."""
    by: dict[str, list[Layer]] = defaultdict(list)
    bad: list[Layer] = []
    for name, repo, rel, path, data in survey.load_all(root):
        lay = Layer(name or f"{repo}-other", repo, rel, path, data)
        if data == "UNPARSEABLE" or not isinstance(data, dict):
            bad.append(lay)
            continue
        lay.f, _ = survey.flat(data)
        by[survey.ident(rel, data)].append(lay)
    return by, bad


def rep(lay: Layer) -> dict[str, Any]:
    r = lay.f.get("representation")
    return r if isinstance(r, dict) else {}


def norm_status(v: Any) -> str | None:
    if not isinstance(v, str) or not v.strip():
        return None
    s = v.strip().lower()
    return STATUS_ALIASES.get(s, s)


def norm_consent(v: Any) -> int | None:
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v
    if isinstance(v, str):
        s = v.strip().lower()
        m = re.match(r"^(\d+)(?:\b|_|-|$)", s)
        if m:
            return int(m.group(1))
        return CONSENT_NAMES.get(s)
    return None


def consent_of(lay: Layer) -> Fact | None:
    r = rep(lay)
    for spelled, v in (("representation.consent_level", r.get("consent_level")),
                       ("consent_level", lay.f.get("consent_level")),
                       ("representation.consent", r.get("consent"))):
        n = norm_consent(v)
        if n is not None:
            return Fact(lay, n, spelled if isinstance(v, int) else f"{spelled}: {v}")
    return None


def real_being_of(lay: Layer) -> Fact | None:
    for spelled, v in (("real_being", lay.f.get("real_being")),
                       ("representation.real_being", rep(lay).get("real_being"))):
        if isinstance(v, bool):
            return Fact(lay, v, spelled)
    return None


def norm_date(v: Any) -> str | None:
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.isoformat()[:10]
    if isinstance(v, int):
        return str(v)
    if isinstance(v, str) and re.match(r"^\d{3,4}", v.strip()):
        return v.strip()
    return None


def date_of(lay: Layer, which: str) -> Fact | None:
    for where in ("", "dates", "memorial", "life"):
        m = lay.f if not where else lay.f.get(where)
        if isinstance(m, dict) and which in m:
            d = norm_date(m[which])
            if d is not None:
                return Fact(lay, d, f"{where}.{which}" if where else which)
    return None


def dates_agree(a: str, b: str) -> bool:
    if a == b:
        return True
    full = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if full.match(a) and full.match(b):
        return False
    return a[:4] == b[:4]


def is_real(layers: list[Layer]) -> bool:
    vals = [f.value for f in (real_being_of(l) for l in layers) if f]
    if True in vals:
        return True
    if False in vals:
        return False
    return any(consent_of(l) for l in layers)


def canonical(layers: list[Layer], real: bool) -> Layer:
    order = REAL_ORDER if real else FICTIONAL_ORDER
    rank = {n: i for i, n in enumerate(order)}
    return sorted(layers, key=lambda l: (rank.get(l.name, len(order)), l.repo, l.rel))[0]


def rel_to(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)


def _as_path(r: Any) -> Path | None:
    if isinstance(r, (str, Path)):
        p = Path(r)
    elif isinstance(r, (tuple, list)) and r:
        return _as_path(r[0])
    elif hasattr(r, "path"):
        return _as_path(getattr(r, "path"))
    else:
        return None
    try:
        return p.resolve() if p.exists() else None
    except OSError:
        return None


def refs_locate(ref: str, from_file: Path, root: Path) -> Path | None:
    """Ask refs.py; only an existing path counts (it answers a GitHub URL when nothing is local)."""
    if _refs is None:
        return None
    loc = getattr(_refs, "locate", None)
    parse = getattr(_refs, "parse_ref", None)
    if not callable(loc):
        return None
    base = from_file.parent
    calls: list[Callable[[], Any]] = [
        lambda: loc(ref, from_file=from_file, roots=[root]),
        lambda: loc(ref, base=base, root=root),
        lambda: loc(ref, base, root),
        lambda: loc(ref, root=root),
        lambda: loc(ref),
    ]
    if callable(parse):
        calls += [lambda: loc(parse(ref), base=base, root=root), lambda: loc(parse(ref), root=root),
                  lambda: loc(parse(ref))]
    for call in calls:
        try:
            p = _as_path(call())
        except Exception:
            continue
        if p is not None:
            return p
    return None


GITHUB_URL = re.compile(
    r"^https?://(?:www\.)?github\.com/[^/]+/(?P<repo>[^/]+)(?:/(?:tree|blob)/[^/]+(?P<path>/.*)?)?/?$")
RAW_URL = re.compile(r"^https?://raw\.githubusercontent\.com/[^/]+/(?P<repo>[^/]+)/[^/]+(?P<path>/.*)?$")


def resolve(ref: str, lay: Layer, root: Path) -> tuple[str, Path | None]:
    """('ok', path) | ('missing', None) | ('external', None) for URLs and repos not checked out."""
    hit = refs_locate(ref, lay.path, root)
    if hit is not None:
        return "ok", hit
    r = ref.split("#", 1)[0].split("?", 1)[0].strip()
    if not r:
        return "ok", lay.path
    target: list[Path] = []
    if r.startswith("moollm://"):
        parts = [p for p in r[len("moollm://"):].split("/") if p]
        if len(parts) >= 3 and parts[0] == "github":
            repo_dir = root / parts[2]
            if not repo_dir.is_dir():
                return "external", None
            target = [repo_dir.joinpath(*parts[3:])]
        else:
            target = [root / "moollm" / "/".join(parts), root / "/".join(parts)]
    elif re.match(r"^[a-z][a-z0-9+.-]*://", r):
        m = GITHUB_URL.match(r) or RAW_URL.match(r)
        if not m or not (root / m.group("repo")).is_dir():
            return "external", None
        target = [root / m.group("repo") / (m.group("path") or "/").lstrip("/")]
    elif r.startswith("/"):
        target = [Path(r)]
    elif "/" not in r.rstrip("/"):
        name = r.rstrip("/")
        d = lay.path.parent
        while True:
            target.append(d / name)
            if d == lay.repo_root or d == d.parent:
                break
            d = d.parent
        target.append(root / "moollm" / "skills" / name)
    else:
        rr = r[2:] if r.startswith("./") else r
        target = [lay.path.parent / rr, lay.repo_root / rr, root / rr, root / "moollm" / rr]
    for t in target:
        try:
            if t.exists():
                return "ok", t.resolve()
        except OSError:
            continue
    return "missing", None


def ref_strings(v: Any, top: bool = True) -> list[str]:
    """Strings in a relation value that look like refs: no whitespace; in maps, a slash too."""
    out: list[str] = []
    if isinstance(v, str):
        s = v.strip()
        if s and not re.search(r"\s", s) and (top or "/" in s):
            out.append(s)
    elif isinstance(v, list):
        for e in v:
            out += ref_strings(e, top)
    elif isinstance(v, dict):
        for k, e in v.items():
            if str(k) not in NOT_REF_KEYS:
                out += ref_strings(e, False)
    return out


def relations(lay: Layer) -> list[tuple[str, str, Any]]:
    """(spelling, relation, value) for every relation-like key on the layer."""
    out: list[tuple[str, str, Any]] = []
    for k in RELATION_KEYS:
        if k in lay.f and lay.f[k] is not None:
            out.append((k, k, lay.f[k]))
    for k, becomes in ALIAS_KEYS.items():
        if k in lay.f and lay.f[k] is not None:
            out.append((k, becomes, lay.f[k]))
    if rep(lay).get("layers") is not None:
        out.append(("representation.layers", "layers", rep(lay)["layers"]))
    return out


def points_at(p: Path, other: Layer) -> bool:
    o = other.path.resolve()
    return p == o or p == o.parent


def lint_id(i: str, layers: list[Layer], root: Path) -> tuple[list[Finding], list[dict[str, Any]]]:
    findings: list[Finding] = []
    review: list[dict[str, Any]] = []
    real = is_real(layers)
    canon = canonical(layers, real)
    names = sorted({l.label for l in layers})

    def add(lay: Layer, rule: str, sev: str, msg: str, involved: list[str] | None = None) -> None:
        findings.append(Finding(i, involved or [lay.label], rel_to(lay.path, root), rule, sev, msg))

    def compare(rule: str, sev: str, facts: list[Fact], same: Callable[[Any, Any], bool],
                what: str) -> None:
        facts = [f for f in facts if f is not None]
        if len(facts) < 2:
            return
        ref = next((f for f in facts if f.layer is canon), facts[0])
        bad = [f for f in facts if f is not ref and not same(f.value, ref.value)]
        for f in bad:
            add(f.layer, rule, sev,
                f"{what} {f.value!r} here ({f.spelled}) vs {ref.value!r} in {ref.layer.label} "
                f"{rel_to(ref.layer.path, root)} ({ref.spelled})",
                [ref.layer.label, f.layer.label])
        if bad and sev == "error":
            review.append({
                "id": i,
                "fact": what,
                "values": [{"layer": f.layer.label, "file": rel_to(f.layer.path, root),
                            "value": f.value, "spelled": f.spelled} for f in facts],
                "decision": None,
            })

    eq: Callable[[Any, Any], bool] = lambda a, b: a == b
    compare("fact-name", "warning",
            [Fact(l, " ".join(str(l.f["name"]).split()), "name") if l.f.get("name") else None
             for l in layers], eq, "name")
    statuses = [Fact(l, norm_status(l.f.get("status")), "status") if norm_status(l.f.get("status"))
                else None for l in layers]
    compare("fact-status", "error", [f for f in statuses if f and f.value in LIFE_STATUS],
            eq, "status")
    compare("status-vocabulary", "warning", statuses,
            lambda a, b: a == b or (a in LIFE_STATUS and b in LIFE_STATUS), "status")
    compare("fact-born", "error", [date_of(l, "born") for l in layers], dates_agree, "born")
    compare("fact-died", "error", [date_of(l, "died") for l in layers], dates_agree, "died")
    compare("fact-real-being", "error", [real_being_of(l) for l in layers], eq, "real_being")
    consents = [consent_of(l) for l in layers]
    compare("consent-level", "error", consents, eq, "consent_level")

    for c in consents:
        if c and c.spelled != "representation.consent_level":
            add(c.layer, "consent-spelling", "info",
                f"consent level spelled {c.spelled}; L7 spells it representation.consent_level: {c.value}")

    life = {f.value for f in statuses if f and f.value in LIFE_STATUS}
    being_life = life.pop() if len(life) == 1 else None

    for lay in layers:
        others = [o for o in layers if o is not lay]
        rels = relations(lay)
        linked = False
        for spelled, becomes, value in rels:
            if spelled in ALIAS_KEYS or spelled == "representation.layers":
                add(lay, "relation-alias", "info",
                    f"{spelled}: is a legacy spelling; L2 spells it {becomes}:")
            for r in ref_strings(value):
                status, p = resolve(r, lay, root)
                if status == "missing":
                    add(lay, "ref-unresolved", "warning", f"{spelled}: {r} does not resolve")
                elif status == "ok" and p is not None and any(points_at(p, o) for o in others):
                    linked = True
        for k in SOFT_KEYS:
            for r in ref_strings(lay.f.get(k)):
                status, p = resolve(r, lay, root)
                if status == "ok" and p is not None and any(points_at(p, o) for o in others):
                    linked = True
                    add(lay, "relation-alias", "info",
                        f"{k}: {r} names another layer; L2 spells that layers:")
        if lay is not canon and not linked:
            if rels:
                add(lay, "relation-missing", "warning",
                    f"declares {', '.join(s for s, _, _ in rels)} but none points at another layer "
                    f"of {i}; canonical is {canon.label} {rel_to(canon.path, root)}",
                    [lay.label, canon.label])
            else:
                add(lay, "relation-missing", "warning",
                    f"declares no inherits:, derived_from: or layers:; canonical is {canon.label} "
                    f"{rel_to(canon.path, root)}", [lay.label, canon.label])

        missing = [k for k in ("id", "name", "status", "signifier") if lay.f.get(k) in (None, "")]
        if real:
            if real_being_of(lay) is None:
                missing.append("real_being")
            if consent_of(lay) is None:
                missing.append("representation.consent_level")
        if missing:
            add(lay, "key-missing", "warning", f"core keys missing: {', '.join(missing)}")

        sig = lay.f.get("signifier")
        status = norm_status(lay.f.get("status"))
        status = status if status in LIFE_STATUS else being_life
        if real and isinstance(sig, str) and sig and status:
            want = SIGNIFIERS[status]
            if sig.replace("\ufe0f", "") != want.replace("\ufe0f", ""):
                add(lay, "signifier", "info",
                    f"signifier {sig} carries a topical emoji; move to emoji: and use {want} ({status})")

    for f in findings:
        f.layers = f.layers or names
    return findings, review


def run(root: Path, ids: list[str] | None = None) -> dict[str, Any]:
    by, bad = load_layers(root)
    if ids:
        chosen = {i: by.get(i, []) for i in ids}
    else:
        chosen = {i: ls for i, ls in by.items() if len({l.name for l in ls}) > 1}
    findings: list[Finding] = []
    review: list[dict[str, Any]] = []
    for i in sorted(chosen):
        layers = chosen[i]
        if len(layers) < 2:
            findings.append(Finding(i, [l.label for l in layers], rel_to(layers[0].path, root)
                                    if layers else "", "single-layer", "info",
                                    f"{len(layers)} layer(s); nothing to compare"))
            continue
        try:
            f, r = lint_id(i, layers, root)
        except Exception as e:
            f, r = [Finding(i, [l.label for l in layers], "", "lint-crashed", "warning",
                            f"{type(e).__name__}: {e}")], []
        findings += f
        review += r
    for lay in bad:
        if Path(lay.rel).parent.name in chosen:
            findings.append(Finding(Path(lay.rel).parent.name, [lay.label], rel_to(lay.path, root),
                                    "unparseable", "warning", "CHARACTER.yml does not parse as a map"))
    findings.sort(key=lambda f: (f.id, SEVERITY_RANK[f.severity], f.rule, f.file))
    return {"root": root, "files": sum(len(v) for v in by.values()) + len(bad), "ids": len(by),
            "checked": sorted(chosen), "findings": findings, "review": review}


def summary(res: dict[str, Any]) -> dict[str, Any]:
    fs: list[Finding] = res["findings"]
    sev = Counter(f.severity for f in fs)
    rules = Counter((f.severity, f.rule) for f in fs)
    return {
        "root": str(res["root"]),
        "files": res["files"],
        "ids": res["ids"],
        "ids_checked": len(res["checked"]),
        "findings": {s: sev.get(s, 0) for s in SEVERITY_RANK},
        "by_rule": {f"{s} {r}": n for (s, r), n in sorted(rules.items(),
                                                          key=lambda x: (SEVERITY_RANK[x[0][0]], -x[1]))},
        "error_ids": sorted({f.id for f in fs if f.severity == "error"}),
        "review_items": len(res["review"]),
    }


REVIEW_HEADER = """\
# Facts for Don to decide. Agents must not resolve them.
#
# Each entry is one being whose layers disagree about a consent level or a life fact
# (status, born, died, real_being). One of the layers is wrong about a real person, and only
# Don knows which: what the person agreed to, whether they are living, when they were born.
# Agents read this list, never edit the CHARACTER.yml files to make the values match, and
# never fill in decision:. Don writes decision: (the value, and why); a later pass applies it.
#
# Regenerate: python3 skills/prototype/scripts/layers_lint.py --review
# Rule: kernel/constitution-core.md §15 "Layers across repos";
# designs/object-system/CHARACTER-LAYERS-ANALYSIS.md decision L10.
"""


def write_review(path: Path, res: dict[str, Any]) -> None:
    body = {
        "generated_by": "skills/prototype/scripts/layers_lint.py --review",
        "generated": datetime.date.today().isoformat(),
        "root": str(res["root"]),
        "items": res["review"],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(REVIEW_HEADER + "\n" + yaml.safe_dump(body, sort_keys=False, allow_unicode=True,
                                                          width=100))


def print_text(res: dict[str, Any], only_summary: bool) -> None:
    s = summary(res)
    if not only_summary:
        for f in res["findings"]:
            print(f"{f.severity:7} {f.rule:18} {f.id:24} [{', '.join(f.layers)}] {f.file}: {f.message}")
        print()
    print(f"root {s['root']}: {s['files']} CHARACTER.yml, {s['ids']} ids, {s['ids_checked']} checked")
    print("findings: " + ", ".join(f"{k} {v}" for k, v in s["findings"].items()))
    for k, v in s["by_rule"].items():
        print(f"   {k:28} {v}")
    print(f"error ids ({len(s['error_ids'])}): {', '.join(s['error_ids'])}")
    print(f"review items: {s['review_items']}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("ids", nargs="*", help="being ids (default: every id with more than one layer)")
    ap.add_argument("--root", type=Path, default=SCRIPTS.parents[3],
                    help="directory holding the sibling repos")
    ap.add_argument("--format", choices=["text", "yaml"], default="text")
    ap.add_argument("--summary", action="store_true", help="counts only")
    ap.add_argument("--review", nargs="?", const=str(DEFAULT_REVIEW), default=None, metavar="FILE",
                    help=f"write the human-review list (default {rel_to(DEFAULT_REVIEW, MOOLLM)})")
    args = ap.parse_args(argv)
    res = run(args.root.resolve(), args.ids or None)
    if args.format == "yaml":
        out: dict[str, Any] = {"summary": summary(res)}
        if not args.summary:
            out["findings"] = [f.as_dict() for f in res["findings"]]
        print(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=120), end="")
    else:
        print_text(res, args.summary)
    if args.review:
        write_review(Path(args.review), res)
        print(f"wrote {args.review} ({len(res['review'])} items)", file=sys.stderr)
    return 1 if any(f.severity == "error" for f in res["findings"]) else 0


if __name__ == "__main__":
    sys.exit(main())
