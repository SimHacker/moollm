#!/usr/bin/env python3
"""Lint TIES.yml files against TIES-SCHEMA.yml's deterministic checks.

Every check here is build-time and needs no model. The one class of error that matters most is
synonym collision, because it fails silently: a reference resolves to a plausible wrong node, the
page looks fine, and nothing reports anything.

    ties_lint.py PATH...            # lint files or directories
    ties_lint.py --corpus DIR       # also run cross-file checks (collisions, glyph contrast)

Exit 0 clean, 1 on any error, 0 on warnings alone.
"""

import argparse
import pathlib
import re
import sys
from collections import defaultdict

import yaml

BUDGET_BYTES = 4096
RUNG_ORDER = ["glyphs", "label", "name", "definition", "description", "body"]
INLINE_RUNGS = {"glyphs", "label", "name", "definition"}
POINTER_RUNGS = {"description", "body"}

# `name` is a rung at weight 0.15 AND the identity key, so it legitimately lives in the header
# block with id/type/synonyms rather than between label and definition. Exempt from order
# enforcement; every other rung is ordered. Found by linting the first real file ever written.
ORDER_EXEMPT = {"name"}
COSTS = {"tiny", "small", "large", "huge"}

# Guests we happen to recognise. NOT a permission list — an unrecognised organelle is reported as
# INFO and preserved untouched, because needing no blessing is the point of a membrane.
KNOWN_GUESTS = {"dc", "schema_org", "prov", "skos", "cidoc"}

# Budgets are amortised: a prototype root is read once for N children, a leaf is read N times.
# BUDGET_HUB was 2048 by guess. Measured against the first three real manifests — a 415 byte
# inheriting leaf, a 1397 byte pile prototype, and a 2755 byte nine-child skill root whose every
# line survived the non-derivable test — a hub's cost is dominated by its `inside` entries at
# roughly 100 bytes each, so a flat target punishes breadth rather than chattiness.
BUDGET_LEAF = 512
BUDGET_HUB = 3072

# The 1988 canonicalizer, widened to punctuation on the archive's evidence: one article carried
# "alphabetically", "alphabetically," and "alphabetically." as three hand-registered synonyms
# because a link picked out of prose drags its trailing punctuation into the lookup key.
_COLLAPSE = re.compile(r"[ \n\t<>~]+")
_PUNCT = re.compile(r"[.,;:!?()\[\]{}\"'`]")


def canonical(name: str) -> str:
    """Fold a name to its equivalence class. The tilde is whitespace."""
    return _COLLAPSE.sub(" ", _PUNCT.sub("", str(name))).strip().casefold()


def top_level_keys_in_file_order(text: str) -> list[str]:
    """YAML mappings do not preserve order through a dict, so read the raw keys."""
    return [
        m.group(1)
        for m in re.finditer(r"^([A-Za-z_][A-Za-z0-9_]*):", text, re.MULTILINE)
    ]


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warns: list[str] = []
        self.infos: list[str] = []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warns.append(f"{where}: {msg}")

    def info(self, where, msg):
        """Unknown is not invalid. An unblessed organelle is the extension model working."""
        self.infos.append(f"{where}: {msg}")

    def emit(self) -> int:
        for e in self.errors:
            print(f"ERROR {e}")
        for w in self.warns:
            print(f"WARN  {w}")
        for i in self.infos:
            print(f"INFO  {i}")
        n_e, n_w = len(self.errors), len(self.warns)
        print(f"\n{n_e} error(s), {n_w} warning(s), {len(self.infos)} info")
        return 1 if n_e else 0


def undeclared_cache(path: pathlib.Path, doc: dict, rep: Report) -> None:
    """A cardinality in prose with nothing that regenerates it is a fork, not a cache.

    manifest_only_what_is_not_derivable licenses duplication on one condition: that it is declared
    and recomputable. So a bare count in an `inside[].what` is legal exactly when a cache sidecar says
    where it came from. Caught because the first real manifest written carried 37/36/62/9, which was
    `ls | wc -l` counting each pile's own index files as members — a wrong recipe, not a stale number,
    and therefore invisible to any amount of refreshing on schedule.
    """
    if doc.get("cache"):
        return
    for i, entry in enumerate(doc.get("inside") or []):
        what = str(entry.get("what") or "")
        counts = re.findall(r"\b\d+\b", what)
        if counts:
            rep.warn(
                path.name,
                f"inside[{i}] ({entry.get('at')}) states {', '.join(counts)} with no cache: sidecar "
                "to regenerate it — point at one, or drop the number",
            )


def path_exists(parent: pathlib.Path, ref: str) -> bool:
    """A pile's members are addressed as a glob, because naming 35 files is the thing to avoid."""
    ref = str(ref)
    if any(ch in ref for ch in "*?["):
        return any(parent.glob(ref))
    return (parent / ref).exists()


def organelles(path: pathlib.Path, doc: dict, rep: Report, inherited: dict | None = None) -> None:
    """Validate the membrane, never the contents. The guest keeps its own genome."""
    guests = doc.get("x")
    if guests is None:
        return
    # A leaf's organelle may take its schema from the prototype; only the pair must be complete.
    from_proto = (inherited or {}).get("x") or {}
    if not isinstance(guests, dict):
        rep.error(path.name, "x: must be a map of named organelles, one sub-object per guest schema")
        return
    for name, body in guests.items():
        if not isinstance(body, dict):
            rep.error(path.name, f"x.{name} must be a sub-object — a membrane, not a bare value")
            continue
        schema = body.get("schema") or (from_proto.get(name) or {}).get("schema")
        if not schema:
            rep.error(path.name, f"x.{name} has no schema: pointer here or in its prototype — an organelle without its own genome is just clutter in the host")
        elif name not in KNOWN_GUESTS:
            rep.info(path.name, f"x.{name} is an unrecognised guest schema, preserved as-is ({schema})")


def inheritance(path: pathlib.Path, doc: dict, text: str, rep: Report) -> dict:
    """Resolve proto: far enough to check it exists and that the diff is actually a diff.

    Returns the effective inherited mapping so later checks can see what the leaf did not restate.
    """
    proto = doc.get("proto")
    if proto is None:
        return {}
    if str(proto).startswith("~"):
        return {}  # named prototype, resolved by scope walk at read time, not on disk
    target = path.parent.parent / "TIES.yml" if proto == ".." else path.parent / str(proto)
    if not target.exists():
        rep.error(path.name, f"proto: {proto!r} resolves to {target}, which does not exist")
        return {}
    try:
        parent = yaml.safe_load(target.read_text()) or {}
    except yaml.YAMLError as exc:
        rep.error(path.name, f"proto: {proto!r} does not parse: {exc}")
        return {}

    # A prototype states shared values under `inherited:` so its own screen fields stay its own.
    # Without that, every child would inherit the parent's name, label and definition.
    parent = {**parent, **(parent.get("inherited") or {})}

    for key, value in doc.items():
        if key in ("proto", "name", "ties_schema"):
            continue
        if key in parent and parent[key] == value:
            rep.warn(path.name, f"{key} repeats the prototype verbatim — delete it and inherit, or the diff is not a diff")
    for key in doc.get("unset") or []:
        root = str(key).split(".")[0]
        if root not in parent:
            rep.warn(path.name, f"unset: {key!r} tombstones something the prototype does not have")
    return parent


def lint_one(path: pathlib.Path, doc: dict, text: str, rep: Report) -> None:
    where = path.name
    parent = path.parent

    if doc.get("ties_schema") != 1:
        rep.error(where, "ties_schema must be 1")

    if not doc.get("name"):
        rep.error(where, "name is required")

    # The rung the web dropped, kept mandatory.
    definition = doc.get("definition")
    if not definition:
        rep.error(where, "definition is required — it is the rung that answers 'should I go there'")
    elif len(str(definition).split()) > 90:
        rep.warn(where, "definition is long; 1 to 3 sentences is the rung")

    # order_implies_cost is a guarantee or it is nothing — but ORDER_EXEMPT keys are dropped from
    # both sides of the comparison rather than required in place.
    present = [k for k in top_level_keys_in_file_order(text) if k in RUNG_ORDER and k not in ORDER_EXEMPT]
    expected = [k for k in RUNG_ORDER if k in present]
    if present != expected:
        rep.error(
            where,
            f"rung keys out of ladder order: {present} should be {expected} "
            "(RUNGS.yml order, so top-to-bottom is cheap-to-dear)",
        )

    if isinstance(doc.get("body"), str) and "\n" in doc["body"].strip():
        rep.error(where, "body must be a path, never inline prose — read_in_bulk")

    size = len(text.encode())
    if size > BUDGET_BYTES:
        rep.error(where, f"{size} bytes exceeds the {BUDGET_BYTES} byte hard limit; a hundred of these get read at once")
    elif doc.get("proto") and size > BUDGET_LEAF:
        rep.warn(where, f"{size} bytes for an inheriting leaf ({BUDGET_LEAF} target) — check whether the diff is carrying shared lines")
    elif not doc.get("proto") and size > BUDGET_HUB:
        rep.warn(where, f"{size} bytes with no proto: ({BUDGET_HUB} hub target) — if siblings share lines, hoist them to a prototype")

    for rung in POINTER_RUNGS:
        target = doc.get(rung)
        if isinstance(target, str) and "\n" not in target and not path_exists(parent, target):
            rep.error(where, f"{rung} points at {target!r}, which does not exist")

    for i, entry in enumerate(doc.get("inside") or []):
        tag = f"inside[{i}]"
        at = entry.get("at")
        if not at:
            rep.error(where, f"{tag} has no 'at'")
            continue
        if not entry.get("what"):
            rep.error(where, f"{tag} ({at}) has no 'what'")
        cost = entry.get("cost")
        if cost is None:
            rep.error(where, f"{tag} ({at}) has no 'cost' — position cannot imply a directory's size, and absence means unknown")
        elif cost not in COSTS:
            rep.error(where, f"{tag} ({at}) cost {cost!r} not in {sorted(COSTS)}")
        if not path_exists(parent, at):
            rep.error(where, f"{tag} points at {at!r}, which matches nothing")

    undeclared_cache(path, doc, rep)
    inherited = inheritance(path, doc, text, rep)
    organelles(path, doc, rep, inherited)

    if isinstance(doc.get("cache"), str) and not (parent / doc["cache"]).exists():
        rep.error(where, f"cache: points at {doc['cache']!r}, which does not exist")
    if isinstance(doc.get("provenance"), dict) and "cached" in doc["provenance"]:
        rep.error(where, "derived values belong in the cache: sidecar, not inline in provenance — read_in_bulk")

    for i, tie in enumerate(doc.get("ties") or []):
        if not tie.get("to"):
            rep.error(where, f"ties[{i}] has no 'to'")
        if not tie.get("rel"):
            rep.error(where, f"ties[{i}] ({tie.get('to')}) has no 'rel'")

    declared = doc.get("type")
    if declared:
        container = parent.parent.name
        if container and container.endswith("s") and container[:-1] != declared:
            rep.warn(
                where,
                f"type {declared!r} disagrees with container {container!r}; "
                "the path is the guard expression, so one of them is wrong",
            )

    # Generic aliases collide with everything. Mean-regression, same failure as the glyph benchmark.
    for syn in doc.get("synonyms") or []:
        if len(str(syn).split()) > 6:
            rep.warn(where, f"synonym {syn!r} is long enough to be generic; distinctness filter")


def lint_corpus(docs: list[tuple[pathlib.Path, dict]], rep: Report) -> None:
    """Cross-file checks. Scope is the containing directory; namespace is the declared type."""
    claims: dict[tuple, list[tuple[pathlib.Path, str]]] = defaultdict(list)
    for path, doc in docs:
        scope = str(path.parent.parent)
        ns = doc.get("type") or "untyped"
        names = [doc.get("name")] + list(doc.get("synonyms") or [])
        for raw in filter(None, names):
            claims[(scope, ns, canonical(raw))].append((path, raw))

    for (scope, ns, key), claimants in sorted(claims.items()):
        if len(claimants) > 1:
            paths = ", ".join(f"{p.parent.name}/{p.name} as {raw!r}" for p, raw in claimants)
            rep.error(
                f"{ns} namespace in {scope}",
                f"name {key!r} claimed {len(claimants)} times: {paths} — "
                "unresolvable in principle; this is the failure that leaves no artifact",
            )

    # Set-contrastive glyphs apply WITHIN A PILE, not across a type globally.
    #
    # The scope was type-wide and that was wrong, caught by the first two hubs that had glyphs: ties
    # and design-sense are both skills, so the check demanded they share a leading emoji. But a skill
    # is addressed by name and rendered on its own; its first glyph is its single most valuable
    # identifying byte, and 150 skills cannot be distinguished after a shared prefix anyway. A pile is
    # the opposite: 35 lenses ARE read as a set, in one menu, where a shared lead reads as "these are
    # the same kind of thing" and the tail does the distinguishing. Same directory is the test for
    # being read as a set, which is also dry-piles' definition of a pile.
    by_pile: dict[tuple[str, str], list[tuple[pathlib.Path, str]]] = defaultdict(list)
    for path, doc in docs:
        glyphs = doc.get("glyphs")
        if glyphs:
            key = (str(path.parent), doc.get("type") or "untyped")
            by_pile[key].append((path, str(glyphs)))
    for (pile, ns), members in by_pile.items():
        firsts = {g[0] for _, g in members if g}
        if len(firsts) > 1 and len(members) > 1:
            rep.warn(
                f"{pathlib.Path(pile).name}/ {ns} glyphs",
                f"pile members lead with different type glyphs {sorted(firsts)}; "
                "within one pile the first glyph should be shared and the rest should distinguish",
            )


def collect(paths: list[str]) -> list[pathlib.Path]:
    out: list[pathlib.Path] = []
    for raw in paths:
        p = pathlib.Path(raw)
        if p.is_dir():
            out += sorted(p.rglob("*TIES.yml"))
        elif p.exists():
            out.append(p)
        else:
            print(f"WARN  {p}: no such path")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--corpus", action="store_true", help="also run cross-file collision checks")
    args = ap.parse_args()

    files = collect(args.paths)
    if not files:
        print("no TIES.yml files found")
        return 0

    rep = Report()
    docs: list[tuple[pathlib.Path, dict]] = []
    for path in files:
        text = path.read_text()
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError as exc:
            rep.error(path.name, f"unparseable: {exc}")
            continue
        if not isinstance(doc, dict):
            rep.error(path.name, "top level must be a mapping")
            continue
        docs.append((path, doc))
        lint_one(path, doc, text, rep)

    if args.corpus:
        lint_corpus(docs, rep)

    print(f"linted {len(docs)} file(s)")
    return rep.emit()


if __name__ == "__main__":
    sys.exit(main())
