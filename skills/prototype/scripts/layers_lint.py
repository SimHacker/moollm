#!/usr/bin/env python3
"""Lint character layers across sibling repos: same being, several CHARACTER.yml, one set of facts.

Constitution §15 "Layers across repos": each layer carries the core it needs to run alone, and
declares how it relates to the others. designs/object-system/CHARACTER-LAYERS-ANALYSIS.md
(decisions L1-L12) names the core keys and relations. Per id with more than one layer:

  facts       name, status (memorial, passed = deceased), born, died, real_being,
              representation.public_figure and representation.consent.state agree across the
              layers that state them; a layer that omits a fact is unknown there, not a dissent
  relations   every layer but the canonical one declares inherits:, derived_from: or layers:
              pointing at another layer of the same being, or is a public layer that a private
              layer points at; legacy spellings are reported
  refs        declared relation refs resolve to an existing file or directory
  core keys   id, name, status, signifier; real_being and representation.authored_by for
              real beings
  signifier   real living 👤, deceased 🕯️, fictional 🎭 (📖 is its alias), fictional robot or
              AI 🤖; a topical emoji belongs in emoji:

Every being, single-layer ones included, also gets the representation rules of
skills/representation-ethics/REPRESENTATION.yml: the governing rule computed from its facts
(memorial > self_authored > consented > public_figure > private, first match), granted
consent without evidence, speaks_as outside self_authored or consented, living real beings
whose public_figure no layer states, consent.state unverified, and retired consent spellings.
A being is real unless a layer states real_being: false or status: fictional. Consent is read
from whichever layer states it; it belongs in the public show layer, so a private layer that
states it is reported (consent-placement) and a private layer without it is not.

Visibility (visibility.py, PRIVATE-REPOS.yml): private layers may name and inherit public
layers, never the reverse. A layer in a public repo whose values name a private repo (an
owner/name slug, a private checkout dir followed by '/', a moollm:// ref into one) is an
error (private-ref).

Layers and envelopes come from layers_survey.py. Refs go through refs.py when it is importable.

Usage: layers_lint.py [ids...] [--root DIR] [--format text|yaml] [--summary] [--review FILE]
  --root     directory holding the sibling repos (default: moollm's parent)
  --summary  counts only
  --review   write the facts a person must decide (layer disagreements about consent,
             public_figure and life facts; unverified consent) as YAML to FILE. The list
             carries private paths, so FILE must be outside every public checkout.
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
import visibility  # noqa: E402

try:
    import refs as _refs  # type: ignore  # noqa: E402
except Exception:
    _refs = None

MOOLLM = SCRIPTS.parents[2]
REPRESENTATION = MOOLLM / "skills" / "representation-ethics" / "REPRESENTATION.yml"
CHARACTER_SCHEMA = MOOLLM / "skills" / "character" / "CHARACTER.yml"

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
REAL_ORDER = ["biography", "wwsff-profile", "adventure", "moollm-other", "micropoliscore",
              "wwsff-cast", "show-audience", "private"]
FICTIONAL_ORDER = ["adventure", "moollm-other", "wwsff-cast", "wwsff-profile", "biography",
                   "show-audience", "micropoliscore", "private"]

LIFE_STATUS = {"living", "deceased", "fictional"}
# fallback when the character schema cannot be read; a None value means unknown
STATUS_ALIASES: dict[str, str | None] = {"memorial": "deceased", "passed": "deceased", "dead": "deceased",
                                         "alive": "living", "reified": "fictional", "unknown": None}
SIGNIFIERS = {"living": "👤", "deceased": "🕯️"}
FICTIONAL_SIGNIFIERS = {"🎭", "🤖"}
# fallback when the character schema cannot be read
SIGNIFIER_ALIASES = {"📖": "🎭"}
ROBOT_TYPE = re.compile(r"robot|\bai\b|ai_|_ai|bot\b|android", re.I)

# fallbacks when REPRESENTATION.yml cannot be read; the schema file wins when it parses
CONSENT_STATES = ["not_asked", "asked", "interested", "granted", "declined", "revoked", "unverified"]
CONSENT_ALIASES = {
    "not_yet_asked": "not_asked", "not_addressed": "not_asked", "asked_no_reply_yet": "asked",
    "awaiting_reply": "asked", "pending_response": "asked", "outreach_sent_awaiting_reply": "asked",
    "collaborator_invited": "asked", "invitation_accepted": "granted",
}
# a disagreement involving one of these changes what the portrayal may do
CONSENT_DECISIVE = {"granted", "declined", "revoked"}
RULES = ["memorial", "self_authored", "consented", "public_figure", "private"]
SPEAKS_AS_OK = {"self_authored", "consented"}

SEVERITY_RANK = {"error": 0, "warning": 1, "info": 2}


def load_consent_vocabulary(path: Path = REPRESENTATION) -> tuple[list[str], dict[str, str]]:
    try:
        state = yaml.safe_load(path.read_text())["schema"]["keys"]["consent"]["keys"]["state"]
        values = [str(v) for v in state["values"]]
        aliases = {str(k): str(v) for k, v in (state.get("value_aliases") or {}).items()}
        if values:
            return values, aliases
    except Exception:
        pass
    return CONSENT_STATES, CONSENT_ALIASES


STATES, STATE_ALIASES = load_consent_vocabulary()


def load_signifier_aliases(path: Path = CHARACTER_SCHEMA) -> dict[str, str]:
    try:
        a = yaml.safe_load(path.read_text())["schema"]["keys"]["signifier"]["value_aliases"]
        if isinstance(a, dict) and a:
            return {str(k).replace("\ufe0f", ""): str(v) for k, v in a.items()}
    except Exception:
        pass
    return SIGNIFIER_ALIASES


SIGNIFIER_ALIASES = load_signifier_aliases()


def load_status_aliases(path: Path = CHARACTER_SCHEMA) -> dict[str, str | None]:
    try:
        a = yaml.safe_load(path.read_text())["schema"]["keys"]["status"]["value_aliases"]
        if isinstance(a, dict) and a:
            return {**STATUS_ALIASES, **{str(k).lower(): (str(v) if v is not None else None)
                                         for k, v in a.items()}}
    except Exception:
        pass
    return STATUS_ALIASES


STATUS_ALIASES = load_status_aliases()


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
    vis = visibility.get(root)
    for name, repo, rel, path, data in survey.load_all(root):
        lay = Layer(name or ("private-other" if vis.is_private(root / repo) else f"{repo}-other"),
                    repo, rel, path, data)
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


def consent_map(lay: Layer) -> dict[str, Any]:
    c = rep(lay).get("consent")
    return c if isinstance(c, dict) else {}


def norm_state(v: Any) -> str | None:
    if not isinstance(v, str) or not v.strip():
        return None
    s = v.strip().lower().replace("-", "_").replace(" ", "_")
    return STATE_ALIASES.get(s, s)


def state_of(lay: Layer) -> Fact | None:
    """consent.state as stated in this layer; absent is unknown here, not not_asked."""
    s = norm_state(consent_map(lay).get("state"))
    return Fact(lay, s, "representation.consent.state") if s else None


def evidence_of(lay: Layer) -> Any:
    e = consent_map(lay).get("evidence")
    return e if e not in (None, "", [], {}) else None


def public_figure_of(lay: Layer) -> Fact | None:
    v = rep(lay).get("public_figure")
    return Fact(lay, v, "representation.public_figure") if isinstance(v, bool) else None


def author_of(lay: Layer, subject: str | None = None) -> str | None:
    """authored_by as a character id; 'self' reads as the subject's id."""
    a = rep(lay).get("authored_by")
    if not isinstance(a, str) or not a.strip():
        return None
    a = a.strip().rstrip("/").split("/")[-1].split("#")[0]
    if a.lower() == "self" and subject:
        return subject
    return a or None


REAL_GOVERNORS = ("real-being", "representation-ethics", "portrayal-standards")


def governed_as_real(lay: Layer) -> bool:
    g = rep(lay).get("governed_by", rep(lay).get("protocol"))
    gs = g if isinstance(g, list) else [g]
    return any(isinstance(x, str) and any(k in x for k in REAL_GOVERNORS) for x in gs)


def legacy_consent(lay: Layer) -> list[str]:
    """Retired consent spellings on this layer (REPRESENTATION.yml retired: consent_level)."""
    r = rep(lay)
    out = []
    if "consent_level" in r:
        out.append(f"representation.consent_level: {r['consent_level']!r}")
    if "consent_level" in lay.f:
        out.append(f"consent_level: {lay.f['consent_level']!r}")
    if isinstance(r.get("consent"), (str, int)) and not isinstance(r.get("consent"), bool):
        out.append(f"representation.consent: {r['consent']!r}")
    if "kind" in r:
        out.append(f"representation.kind: {r['kind']!r}")
    return out


def is_private(lay: Layer) -> bool:
    """Content of a private layer stays out of generated files: path and fact value only."""
    try:
        return visibility.get(lay.repo_root.parent).is_private(lay.repo_root)
    except Exception:
        return True


def strings(v: Any, path: str = "") -> list[tuple[str, str]]:
    """(dotted key path, string) for every string key and value in the data."""
    out: list[tuple[str, str]] = []
    if isinstance(v, str):
        out.append((path, v))
    elif isinstance(v, list):
        for n, e in enumerate(v):
            out += strings(e, f"{path}[{n}]")
    elif isinstance(v, dict):
        for k, e in v.items():
            p = f"{path}.{k}" if path else str(k)
            if isinstance(k, str):
                out.append((p, k))
            out += strings(e, p)
    return out


def private_refs(lay: Layer) -> list[tuple[str, str]]:
    """(key path, private name) for each value of a public layer that names a private repo."""
    if is_private(lay):
        return []
    try:
        vis = visibility.get(lay.repo_root.parent)
    except Exception:
        return []
    out: list[tuple[str, str]] = []
    for where, s in strings(lay.data):
        for name in dict.fromkeys(vis.find(s)):
            out.append((where, name))
    return out


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
    """real_being as stated (true wins); else false when a layer says status: fictional; else true."""
    vals = [f.value for f in (real_being_of(l) for l in layers) if f]
    if True in vals:
        return True
    if False in vals:
        return False
    return not any(norm_status(l.f.get("status")) == "fictional" for l in layers)


def canonical(layers: list[Layer], real: bool) -> Layer:
    order = REAL_ORDER if real else FICTIONAL_ORDER
    rank = {n: i for i, n in enumerate(order)}
    return sorted(layers, key=lambda l: (rank.get(l.name, len(order)), l.repo, l.rel))[0]


def ordered(layers: list[Layer], real: bool) -> list[Layer]:
    """Canonical layer first: where layers state different values, its value is the reference."""
    order = REAL_ORDER if real else FICTIONAL_ORDER
    rank = {n: i for i, n in enumerate(order)}
    return sorted(layers, key=lambda l: (rank.get(l.name, len(order)), l.repo, l.rel))


def first(facts: list[Fact | None]) -> Fact | None:
    return next((f for f in facts if f is not None), None)


def status_fact(lay: Layer) -> Fact | None:
    s = norm_status(lay.f.get("status"))
    return Fact(lay, s, "status") if s in LIFE_STATUS else None


def rule_for(i: str, lay: Layer, layers: list[Layer]) -> str:
    """The governing rule for one layer, first match. A fact the layer omits, authorship
    included, comes from the first layer (canonical first) that states it."""
    own = [lay] + [l for l in layers if l is not lay]
    status = first([status_fact(l) for l in own])
    if status and status.value == "deceased":
        return "memorial"
    if next((a for a in (author_of(l, i) for l in own) if a), None) == i:
        return "self_authored"
    state = first([state_of(l) for l in own])
    if state and state.value == "granted" and evidence_of(state.layer) is not None:
        return "consented"
    pf = first([public_figure_of(l) for l in own])
    if pf and pf.value is True:
        return "public_figure"
    return "private"


def value_entry(f: Fact, root: Path, note: bool = False) -> dict[str, Any]:
    e: dict[str, Any] = {"layer": f.layer.label, "file": rel_to(f.layer.path, root), "value": f.value}
    if is_private(f.layer):
        return e
    e["spelled"] = f.spelled
    n = consent_map(f.layer).get("note")
    if note and isinstance(n, str) and n.strip():
        e["note"] = " ".join(n.split())
    return e


def lint_being(i: str, layers: list[Layer], root: Path
               ) -> tuple[list[Finding], list[dict[str, Any]], dict[str, Any]]:
    """Representation rules for one being, any number of layers."""
    findings: list[Finding] = []
    review: list[dict[str, Any]] = []
    real = is_real(layers)
    lays = ordered(layers, real)

    def add(lay: Layer, rule: str, sev: str, msg: str) -> None:
        findings.append(Finding(i, [lay.label], rel_to(lay.path, root), rule, sev, msg))

    unverified: list[Fact] = []
    for lay in lays:
        for where, name in private_refs(lay):
            add(lay, "private-ref", "error",
                f"{where} names private repo {name}; a public layer never names a private one "
                "(private layers name and inherit public layers)")
        if is_private(lay) and rep(lay).get("consent") is not None:
            add(lay, "consent-placement", "info",
                "representation.consent stated in a private layer; consent belongs in the public "
                "show layer")
        for old in legacy_consent(lay):
            add(lay, "consent-legacy", "info",
                f"{old} is a retired consent spelling; REPRESENTATION.yml states authored_by, "
                "consent: {state, evidence}, public_figure and status instead")
        if str(rep(lay).get("authored_by") or "").strip().lower() == "self":
            add(lay, "authored-by-spelling", "info",
                f"authored_by: self; REPRESENTATION.yml spells the subject's id ({i})")
        c = rep(lay).get("consent")
        if c is not None and not isinstance(c, (dict, str, int)):
            add(lay, "consent-state-unknown", "warning",
                f"representation.consent is a {type(c).__name__}; expected a map with state:")
        st = state_of(lay)
        if st is None and isinstance(c, dict) and c.get("state") is not None:
            add(lay, "consent-state-unknown", "warning",
                f"consent.state {c.get('state')!r} is not one of {', '.join(STATES)}")
        if st is None:
            continue
        if st.value not in STATES:
            add(lay, "consent-state-unknown", "warning",
                f"consent.state {st.value!r} is not one of {', '.join(STATES)}")
        if st.value == "granted" and evidence_of(lay) is None:
            add(lay, "consent-no-evidence", "error",
                "consent.state granted without consent.evidence; it governs nothing until the "
                "evidence is on file")
        if st.value == "unverified":
            unverified.append(st)
            add(lay, "consent-unverified", "warning",
                "consent.state unverified: an earlier record claimed consent with no evidence on "
                "file; Don confirms or corrects")

    rule = rule_for(i, lays[0], lays) if real else None
    pf_unknown = False
    if real:
        for lay in lays:
            if rep(lay).get("speaks_as") is True:
                r = rule_for(i, lay, lays)
                if r not in SPEAKS_AS_OK:
                    add(lay, "speaks-as", "error",
                        f"speaks_as: true under the {r} rule; only self_authored or consented "
                        "(with a scope that says so) may speak as the subject")
        status = first([status_fact(l) for l in lays])
        if (status is None or status.value == "living") and not any(public_figure_of(l) for l in lays):
            pf_unknown = True
            lay = lays[0]
            add(lay, "public-figure-unknown", "warning",
                f"no layer of {i} states representation.public_figure"
                f"{'' if status else ' (status unknown)'}; the private rule applies until one does")
    if unverified:
        review.append({
            "id": i,
            "fact": "consent.state",
            "reason": "unverified: an earlier record claimed consent and no evidence is on file",
            "values": [value_entry(f, root, note=True) for f in unverified],
            "decision": None,
        })
    info = {"id": i, "rule": rule, "real_being": real, "public_figure_unknown": pf_unknown,
            "layers": [l.label for l in lays]}
    return findings, review, info


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
                "reason": "layers disagree",
                "values": [value_entry(f, root) for f in facts],
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
    compare("fact-public-figure", "error", [public_figure_of(l) for l in layers], eq, "public_figure")

    states = [f for f in (state_of(l) for l in ordered(layers, real)) if f is not None]
    if states:
        ref = states[0]
        decisive = False
        for f in states[1:]:
            if f.value == ref.value:
                continue
            pair = {f.value, ref.value}
            where = (f"{f.value!r} here vs {ref.value!r} in {ref.layer.label} "
                     f"{rel_to(ref.layer.path, root)}")
            if pair & CONSENT_DECISIVE:
                decisive = True
                add(f.layer, "consent-state", "error", f"consent.state {where}",
                    [ref.layer.label, f.layer.label])
            elif pair == {"asked", "not_asked"}:
                behind = f if f.value == "not_asked" else ref
                ahead = ref if behind is f else f
                add(behind.layer, "consent-stale", "warning",
                    f"consent.state {where}; {behind.layer.label} is behind "
                    f"({ahead.layer.label} records asked)", [ref.layer.label, f.layer.label])
            else:
                add(f.layer, "consent-state", "warning", f"consent.state {where}",
                    [ref.layer.label, f.layer.label])
        if decisive:
            review.append({
                "id": i,
                "fact": "consent.state",
                "reason": "layers disagree",
                "values": [value_entry(f, root, note=True) for f in states],
                "decision": None,
            })

    life = {f.value for f in statuses if f and f.value in LIFE_STATUS}
    being_life = life.pop() if len(life) == 1 else None

    targets: dict[int, set[int]] = {}
    for lay in layers:
        others = [o for o in layers if o is not lay]
        hit: set[int] = set()
        for value in [v for _, _, v in relations(lay)] + [lay.f.get(k) for k in SOFT_KEYS]:
            for r in ref_strings(value):
                status, p = resolve(r, lay, root)
                if status == "ok" and p is not None:
                    hit |= {id(o) for o in others if points_at(p, o)}
        targets[id(lay)] = hit
    pointed_by_private = {t for l in layers if is_private(l) for t in targets[id(l)]}

    for lay in layers:
        others = [o for o in layers if o is not lay]
        rels = relations(lay)
        linked = id(lay) in pointed_by_private and not is_private(lay)
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
            if author_of(lay) is None:
                missing.append("representation.authored_by")
        if missing:
            add(lay, "key-missing", "warning", f"core keys missing: {', '.join(missing)}")

        sig = lay.f.get("signifier")
        status = norm_status(lay.f.get("status"))
        status = status if status in LIFE_STATUS else being_life
        want = SIGNIFIERS.get(status or "")
        if real and isinstance(sig, str) and sig and want:
            if sig.replace("\ufe0f", "") != want.replace("\ufe0f", ""):
                add(lay, "signifier", "info",
                    f"signifier {sig} carries a topical emoji; move to emoji: and use {want} ({status})")
        if not real and isinstance(sig, str) and sig:
            s = sig.replace("\ufe0f", "").strip()
            fic = "🤖" if ROBOT_TYPE.search(str(lay.f.get("type") or "")) else "🎭"
            if s in SIGNIFIER_ALIASES:
                add(lay, "signifier", "info", f"signifier {s} is an alias of {SIGNIFIER_ALIASES[s]}; "
                    f"spell it {fic}")
            elif s not in FICTIONAL_SIGNIFIERS:
                add(lay, "signifier", "info",
                    f"signifier {sig} carries a topical emoji; move to emoji: and use {fic} (fictional)")

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
    beings: list[dict[str, Any]] = []
    for i in sorted(set(ids) if ids else by):
        layers = by.get(i, [])
        if not layers:
            continue
        try:
            f, r, info = lint_being(i, layers, root)
        except Exception as e:
            f, r, info = [Finding(i, [l.label for l in layers], "", "lint-crashed", "warning",
                                  f"{type(e).__name__}: {e}")], [], {"id": i, "rule": None}
        findings += f
        review += r
        beings.append(info)
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
    findings.sort(key=lambda f: (f.id, SEVERITY_RANK.get(f.severity, 9), f.rule, f.file))
    review.sort(key=lambda r: (r["id"], r["fact"], r.get("reason", "")))
    return {"root": root, "files": sum(len(v) for v in by.values()) + len(bad), "ids": len(by),
            "checked": sorted(chosen), "findings": findings, "review": review, "beings": beings}


def summary(res: dict[str, Any]) -> dict[str, Any]:
    fs: list[Finding] = res["findings"]
    sev = Counter(f.severity for f in fs)
    rules = Counter((f.severity, f.rule) for f in fs)
    beings = res.get("beings", [])
    gov = Counter(b.get("rule") for b in beings if b.get("rule"))
    pf_unknown = sorted(b["id"] for b in beings if b.get("public_figure_unknown"))
    return {
        "root": str(res["root"]),
        "files": res["files"],
        "ids": res["ids"],
        "ids_checked": len(res["checked"]),
        "findings": {s: sev.get(s, 0) for s in SEVERITY_RANK},
        "by_rule": {f"{s} {r}": n for (s, r), n in sorted(
            rules.items(), key=lambda x: (SEVERITY_RANK.get(x[0][0], 9), -x[1]))},
        "error_ids": sorted({f.id for f in fs if f.severity == "error"}),
        "real_beings": sum(gov.values()),
        "governing_rules": {r: gov.get(r, 0) for r in RULES},
        "public_figure_unknown": {"count": len(pf_unknown), "ids": pf_unknown},
        "review_items": len(res["review"]),
    }


REVIEW_HEADER = """\
# Facts for Don to decide. Agents must not resolve them.
#
# Each entry is one being and one representation or life fact that only Don can settle:
#   reason "layers disagree"  two layers state different values for public_figure,
#                             consent.state, status, born, died or real_being; one of them is
#                             wrong about a real person
#   reason "unverified"       consent.state unverified: an earlier record claimed consent and
#                             no evidence is on file; Don confirms (granted, with evidence) or
#                             corrects it
# Only Don knows what the person agreed to, whether they are a public figure, whether they are
# living, when they were born. Agents read this list, never edit the CHARACTER.yml files to make
# the values match, and never fill in decision:. Don writes decision: (the value, and why); a
# later pass applies it. Entries from private repos carry only the file path and the value.
#
# Regenerate: python3 skills/prototype/scripts/layers_lint.py --review FILE (outside public repos)
# Rule: kernel/constitution-core.md §15 "Layers across repos";
# designs/object-system/CHARACTER-LAYERS-ANALYSIS.md decision L10;
# skills/representation-ethics/REPRESENTATION.yml (facts and computed rules).
"""


def review_refusal(path: Path, root: Path) -> str | None:
    """The public checkout that would hold the review file, or None when it may be written."""
    p = path.expanduser().resolve()
    for d in [p, *p.parents]:
        if (d / ".git").exists():
            return None if visibility.get(root).is_private(d) else str(d)
    return None


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
        for b in res.get("beings", []):
            if b.get("rule"):
                print(f"rule:   {b['rule']:14} {b['id']:24} [{', '.join(b.get('layers', []))}]")
        print()
        for f in res["findings"]:
            print(f"{f.severity:7} {f.rule:21} {f.id:24} [{', '.join(f.layers)}] {f.file}: {f.message}")
        print()
    print(f"root {s['root']}: {s['files']} CHARACTER.yml, {s['ids']} ids, {s['ids_checked']} "
          "with several layers compared")
    print("findings: " + ", ".join(f"{k} {v}" for k, v in s["findings"].items()))
    for k, v in s["by_rule"].items():
        print(f"   {k:31} {v}")
    print(f"error ids ({len(s['error_ids'])}): {', '.join(s['error_ids'])}")
    print(f"governing rule ({s['real_beings']} real beings): "
          + ", ".join(f"{k} {v}" for k, v in s["governing_rules"].items()))
    pf = s["public_figure_unknown"]
    print(f"public_figure unknown ({pf['count']}): {', '.join(pf['ids'])}")
    print(f"review items: {s['review_items']}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("ids", nargs="*", help="being ids (default: every id with more than one layer)")
    ap.add_argument("--root", type=Path, default=SCRIPTS.parents[3],
                    help="directory holding the sibling repos")
    ap.add_argument("--format", choices=["text", "yaml"], default="text")
    ap.add_argument("--summary", action="store_true", help="counts only")
    ap.add_argument("--review", default=None, metavar="FILE",
                    help="write the human-review list to FILE, outside every public checkout")
    args = ap.parse_args(argv)
    if args.review:
        where = review_refusal(Path(args.review), args.root.resolve())
        if where:
            print(f"--review {args.review}: inside the public checkout {where}; the review list "
                  "carries private paths. Write it inside a private checkout or outside the "
                  "sibling repos.", file=sys.stderr)
            return 2
    res = run(args.root.resolve(), args.ids or None)
    if args.format == "yaml":
        out: dict[str, Any] = {"summary": summary(res)}
        if not args.summary:
            out["beings"] = [{"id": b["id"], "rule": b.get("rule"), "layers": b.get("layers", [])}
                             for b in res["beings"] if b.get("rule")]
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
