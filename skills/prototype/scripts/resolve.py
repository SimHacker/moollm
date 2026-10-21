#!/usr/bin/env python3
"""resolve.py — the deterministic tier of MOOLLM's prototype lookup.

Implements designs/object-system/SCHEMA.md.

An object is a directory, a YAML file, or an object embedded in a YAML file
(addressed `file.yml#objects.bench`). Slots are top-level keys. A directory's
slots are the merged slots of its UPPERCASE interface files plus its children.

A directory's views (GLANCE, CARD, INDEX) summarize it and are not its slots.

Parents, in lookup order:
  1. explicit: `inherits:` (canonical) and named parents `role*: ref`
  2. implied: an UPPERCASE file implies the skill its name names (ROOM.yml ->
     room; the skill's prototype file skills/room/ROOM.yml when it has one),
     searched for in enclosing scopes first (an experiment's own
     `run` skill before skills/run), then latent (the K-line ROOM) if no
     file defines it. A directory implies the skills of its interface files.
     An embedded object implies the skill of its collection key (objects ->
     object).
  3. views (GLANCE.yml, CARD.yml, INDEX.yml) get `subject*: <their directory>`
     and then `format*: <view skill>` instead: a view that lacks a slot falls
     through to the thing it summarizes before its format.

Lookup: own slots, then declared parents in order, depth-first, first match
wins; then `defaults:` from enclosing CONTAINER.yml files, keyed by what the
object is (room, character, object...), nearest first (maps deep-merge, lists
concatenate); then implied parents. Latent parents are recorded, not followed;
the LLM tier resolves them.
`--all` shows shadowed definitions and flags Self-4 ambiguity.

Accepted legacy forms (reported by `lint --strict`, never emitted): `parents:`,
`parent:`, `extends:`, a string `prototype:`, list `prototypes:`,
`meta.inherits:`, `moollm/` path prefixes, and envelopes (`room:` wrapping a
ROOM.yml, `object:` wrapping an object file), which are read as if flat.

Usage:
    resolve.py lookup  OBJECT[#path] SLOT [--all]
    resolve.py parents OBJECT[#path]
    resolve.py lint    [PATH ...] [--verbose] [--strict]
    resolve.py stale   [PATH ...] [--verbose]     views older than their subject, per git

Standard library plus PyYAML. Read-only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

PARENT_KEYS = ("inherits", "parents", "parent", "prototype", "extends")
KLINE = re.compile(r"^[A-Z0-9][A-Z0-9_-]+$")
REF_LIKE = re.compile(r"^[\w./~#-]+$")
VIEWS = {"GLANCE": "glance", "CARD": "card", "INDEX": "index"}
SKILL_MARKER = "SKILL.md"
CONTAINER = "CONTAINER.yml"
CASCADE = "defaults: (enclosing container)"
SKIP_DIRS = {".git", "node_modules", "dist", "__pycache__", ".moollm"}
LINT_SKIP_TOP = {"temp"}  # archived imports, not live objects

Key = tuple[Path, str]  # (file or directory, fragment path inside the file)


def interface_name(path: Path) -> str | None:
    """ROOM.yml -> 'ROOM'; lowercase or non-yml -> None."""
    if path.suffix == ".yml" and path.stem.replace("-", "").isupper():
        return path.stem
    return None


@dataclass
class ParentRef:
    ref: str
    role: str | None = None
    target: Key | None = None  # None means latent
    implied: bool = False

    @property
    def latent(self) -> bool:
        return self.target is None

    @property
    def form(self) -> str:
        """file | url | broken (path-shaped, no file) | kline | prose"""
        if self.target is not None:
            return "file"
        if "://" in self.ref:
            return "url"
        if "/" in self.ref:
            return "broken"
        return "kline" if KLINE.match(self.ref) else "prose"

    def label(self) -> str:
        name = f"{self.role}*: " if self.role else ""
        tags = [t for t, on in (("implied", self.implied), ("latent", self.latent)) if on]
        return f"{name}{self.ref}" + (f"  ({', '.join(tags)})" if tags else "")


@dataclass
class Obj:
    key: Key
    slots: dict[str, Any] = field(default_factory=dict)
    parents: list[ParentRef] = field(default_factory=list)

    @property
    def path(self) -> Path:
        return self.key[0]


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / ".git").exists():
            return p
    return start


def load_yaml(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
        try:
            return yaml.safe_load(text)
        except yaml.composer.ComposerError:
            return next(iter(yaml.safe_load_all(text)), None)  # multi-document: first doc is the object
    except (yaml.YAMLError, UnicodeDecodeError, OSError):
        return None


def envelope_key(path: Path, data: dict[str, Any]) -> str | None:
    """The wrapper key a legacy file uses, if any: `room:` in ROOM.yml, `object:` anywhere."""
    iface = interface_name(path)
    if iface and (iface.endswith("S") or iface == "INDEX"):
        iface = None  # PROTOTYPES.yml's `prototypes:` is a collection, not a wrapper
    for k in ([iface.lower()] if iface else []) + ["object"]:
        if isinstance(data.get(k), dict):
            return k
    return None


def flat(path: Path, data: Any) -> dict[str, Any]:
    """A file's slots, reading a legacy envelope as if it were flat."""
    if not isinstance(data, dict):
        return {}
    env = envelope_key(path, data)
    if not env:
        return data
    out = {k: v for k, v in data.items() if k != env}
    for k, v in data[env].items():
        out.setdefault(k, v)
    return out


def file_slots(path: Path) -> dict[str, Any]:
    return flat(path, load_yaml(path))


def interface_files(d: Path) -> list[Path]:
    """Interface files of a directory object, views last.

    An interface that needs files of its own lives in a subdirectory named
    after it (`troll/stomach/STOMACH.yml`). That subdirectory is the slot
    `stomach` of the troll, a child object, and is not merged into the troll.
    """
    files = sorted(p for p in d.glob("*.yml") if interface_name(p))
    return [p for p in files if interface_name(p) not in VIEWS] + [p for p in files if interface_name(p) in VIEWS]


def raw_parent_refs(m: dict[str, Any]) -> list[tuple[str, str | None]]:
    """Normalize every explicit parent declaration form to (ref, role) pairs."""
    out: list[tuple[str, str | None]] = []

    def add(value: Any, role: str | None = None) -> None:
        if isinstance(value, str) and value.strip() and "\n" not in value.strip() and len(value) <= 120:
            out.append((value.strip(), role))
        elif isinstance(value, list):
            for item in value:
                add(item)
        elif isinstance(value, dict):
            if isinstance(value.get("source"), str) and isinstance(value.get("id"), str):
                out.append((f"{value['source']}#*.{value['id']}", value.get("as", role)))  # catalog entry
                return
            for key in ("ref", "from", "path"):
                if key in value:
                    add(value[key], value.get("as", role))
                    return
            # A map of role -> ref is a set of named parents; any other map
            # (e.g. `prototype:` wrapping a whole definition) is not a parent.
            if value and all(isinstance(v, str) and REF_LIKE.match(v) for v in value.values()):
                for k, v in value.items():
                    add(v, str(k).rstrip("*"))

    for key in PARENT_KEYS:
        if key in m:
            add(m[key])
    if isinstance(m.get("prototypes"), list):  # list form = delegation; map form = a catalog of clonables
        add(m["prototypes"])
    if isinstance(m.get("meta"), dict) and "inherits" in m["meta"] and "inherits" not in m:
        add(m["meta"]["inherits"])
    for k, v in m.items():
        if isinstance(k, str) and k.endswith("*") and len(k) > 1:
            add(v, k[:-1])
    return out


def parse_address(addr: str) -> tuple[str, str]:
    path, _, frag = addr.partition("#")
    return path, frag


def resolve_ref(ref: str, base: Path, root: Path, self_path: Path | None = None) -> Key | None:
    """Relative to the object, then walking up for registries, then the repo root.

    Never resolves to the referring file itself: `prototype: wine-rack` inside
    wine-rack.yml means some other wine rack.
    """
    if "://" in ref or "\n" in ref or len(ref) > 200:
        return None
    ref, frag = parse_address(ref)
    if ref.startswith("moollm/"):
        ref = ref[len("moollm/"):]
    if not ref:  # "#objects.bench": same file
        return None
    candidates: list[Path] = []
    for anc in [base, *base.parents]:
        candidates += [anc / ref, anc / f"{ref}.yml"]
        if "/" not in ref:
            for reg in ("skills", "characters", "rooms", "objects"):
                candidates.append(anc / reg / ref)
        if anc == root:
            break
    candidates += [root / ref, root / f"{ref}.yml"]
    for c in candidates:
        try:
            if c.exists() and c.resolve() != self_path:
                return (c.resolve(), find_fragment(c.resolve(), frag))
        except OSError:
            continue
    return None


def find_fragment(path: Path, frag: str) -> str:
    """`*.id` means: the entry `id` in whichever top-level collection of the file has it."""
    if not frag.startswith("*.") or not path.is_file():
        return frag
    want = frag[2:]
    for k, v in file_slots(path).items():
        if isinstance(v, dict) and want in v:
            return f"{k}.{want}"
    return frag


def find_skill(name: str, start: Path, root: Path, exclude: Path) -> Key | None:
    """Container-scoped skill lookup: nearest enclosing scope that defines `name` wins."""
    for anc in [start, *start.parents]:
        for cand in (anc / "skills" / name, anc / name):
            c = cand.resolve()
            # A skill is a directory with a SKILL.md; the object can't be its own skill.
            if (c / SKILL_MARKER).is_file() and not exclude.is_relative_to(c):
                return (c, "")
        if anc == root:
            break
    return None


def implied_parent(name: str, scope: Path, root: Path, exclude: Path, role: str | None = None) -> ParentRef:
    """The skill a name implies. If the skill has a prototype file named for the interface
    (skills/room/ROOM.yml), that file is the parent, so instances get its slots and nothing
    else the skill directory holds. View skills have none: their CARD.yml is their own view."""
    skill = name.lower()
    target = find_skill(skill, scope, root, exclude)
    if target and name.upper() not in VIEWS:
        proto = target[0] / f"{name.upper()}.yml"
        if proto.is_file() and proto.resolve() != exclude.resolve():
            return ParentRef(ref=f"{skill}/{proto.name}", role=role, target=(proto, ""), implied=True)
    return ParentRef(ref=skill if target else name.upper(), role=role, target=target, implied=True)


def singular(key: str) -> str:
    return key[:-3] + "y" if key.endswith("ies") else key[:-1] if key.endswith("s") else key


_cache: dict[Key, Obj] = {}


def load_obj(key: Key, root: Path) -> Obj:
    path, frag = key[0].resolve(), key[1]
    key = (path, frag)
    if key in _cache:
        return _cache[key]
    obj = Obj(key=key)
    _cache[key] = obj  # placed before parents are computed, so cycles terminate
    base = path if path.is_dir() else path.parent
    explicit: list[ParentRef] = []
    implied: list[ParentRef] = []

    if frag:
        value: Any = file_slots(path)
        parts = frag.split(".")
        for part in parts:
            value = value.get(part) if isinstance(value, dict) else None
        obj.slots = value if isinstance(value, dict) else {}
        if len(parts) >= 2:
            implied.append(implied_parent(singular(parts[-2]), base, root, path))
    elif path.is_dir():
        for f in interface_files(path):
            if interface_name(f) in VIEWS:
                continue  # a view summarizes its directory; it is not where the directory's slots live
            for k, v in file_slots(f).items():
                obj.slots.setdefault(k, v)
        for child in path.iterdir():
            if child.name not in SKIP_DIRS and not child.name.startswith("."):
                obj.slots.setdefault(child.stem if child.is_file() else child.name, child)
        for f in interface_files(path):
            if interface_name(f) not in VIEWS:
                implied.append(implied_parent(interface_name(f), path, root, path))
    else:
        obj.slots = file_slots(path)
        iface = interface_name(path)
        if iface in VIEWS:
            implied.append(ParentRef(ref="..", role="subject", target=(base, ""), implied=True))
            implied.append(implied_parent(VIEWS[iface], base, root, path, role="format"))
        elif iface:
            implied.append(implied_parent(iface, base, root, base))

    for ref, role in raw_parent_refs(obj.slots):
        target = resolve_ref(ref, base, root, self_path=path if path.is_file() else None)
        if ref.startswith("#"):
            target = (path, ref[1:])
        explicit.append(ParentRef(ref=ref, role=role, target=target))
    seen = {p.target for p in explicit if p.target}
    obj.parents = explicit + [p for p in implied if p.target is None or p.target not in seen]
    return obj


@dataclass
class Hit:
    definer: Key
    value: Any
    via: list[str]


def get_slot(obj: Obj, dotted: str, root: Path) -> tuple[bool, Any]:
    """Own-slot lookup; dots descend into maps and into child objects (subdirectories, files)."""
    head, _, rest = dotted.partition(".")
    if head not in obj.slots:
        return False, None
    value = obj.slots[head]
    if not rest:
        return True, value
    if isinstance(value, str) and REF_LIKE.match(value):
        target = resolve_ref(value, obj.path if obj.path.is_dir() else obj.path.parent, root)
        if target:
            return get_slot(load_obj(target, root), rest, root)
    if isinstance(value, Path):
        return get_slot(load_obj((value, ""), root), rest, root)
    if isinstance(value, dict):
        return get_slot(Obj(key=obj.key, slots=value), rest, root)
    return False, None


def walk(obj: Obj, slot: str, root: Path, via: list[str], seen: set[Key], hits: list[Hit],
         latent: list[str], cycles: list[str], first_only: bool) -> bool:
    found, value = get_slot(obj, slot, root)
    if found:
        hits.append(Hit(obj.key, value, via))
        if first_only:
            return True
    for p in obj.parents:
        if p.latent:
            latent.append(p.ref)
            continue
        if p.target in seen:
            if not p.implied:
                cycles.append(" -> ".join([*via, p.label()]))
            continue
        child = load_obj(p.target, root)
        if walk(child, slot, root, [*via, p.label()], seen | {p.target}, hits, latent, cycles, first_only) and first_only:
            return True
    return False


def object_kinds(key: Key) -> list[str]:
    """The keys of a container's `defaults:` that apply to this object: its interfaces, else `object`."""
    path, frag = key
    if frag:
        parts = frag.split(".")
        return [singular(parts[-2])] if len(parts) >= 2 else ["object"]
    if path.is_dir():
        kinds = [interface_name(f).lower() for f in interface_files(path) if interface_name(f) not in VIEWS]
        return kinds or ["object"]
    iface = interface_name(path)
    if iface in VIEWS:
        return []
    return [iface.lower()] if iface else ["object"]


def enclosing_containers(key: Key, root: Path) -> list[Path]:
    """CONTAINER.yml files around an object, nearest first. A container covers what is inside
    its directory, not the directory itself."""
    path, frag = key
    if path.is_dir():
        start = path.parent
    elif interface_name(path) and not frag:
        start = path.parent.parent  # maze/room-a/ROOM.yml is the room maze/room-a
    else:
        start = path.parent
    out = []
    for d in [start, *start.parents]:
        if (d / CONTAINER).is_file():
            out.append(d / CONTAINER)
        if d == root or not d.is_relative_to(root):
            break
    return out


def cascade_hits(key: Key, slot: str, root: Path) -> list[Hit]:
    hits = []
    for c in enclosing_containers(key, root):
        defaults = file_slots(c).get("defaults")
        if not isinstance(defaults, dict):
            continue
        for kind in object_kinds(key):
            if isinstance(defaults.get(kind), dict):
                found, value = get_slot(Obj(key=(c, ""), slots=defaults[kind]), slot, root)
                if found:
                    hits.append(Hit((c, f"defaults.{kind}"), value, [CASCADE]))
    return hits


def cascade_merge(near: Any, far: Any) -> Any:
    """Maps deep-merge, lists concatenate (nearest first), scalars: nearest wins."""
    if isinstance(near, dict) and isinstance(far, dict):
        return {**far, **{k: cascade_merge(v, far[k]) if k in far else v for k, v in near.items()}}
    if isinstance(near, list) and isinstance(far, list):
        return near + far
    return near


def lookup(obj: Obj, slot: str, root: Path, first_only: bool) -> tuple[list[Hit], list[str], list[str]]:
    """Own slots, declared parents, enclosing containers' defaults, then implied skill parents.

    Defaults come before implied parents so a container's `lighting: 0` beats anything the
    generic room skill might say, as an author's stylesheet beats the browser's.
    """
    hits: list[Hit] = []
    latent: list[str] = []
    cycles: list[str] = []
    declared = Obj(key=obj.key, slots=obj.slots, parents=[p for p in obj.parents if not p.implied])
    if walk(declared, slot, root, [], {obj.key}, hits, latent, cycles, first_only) and first_only:
        return hits, latent, cycles
    defaults = cascade_hits(obj.key, slot, root)
    if defaults:
        merged = defaults[0].value
        for h in defaults[1:]:
            merged = cascade_merge(merged, h.value)
        hits.append(Hit(defaults[0].definer, merged, [CASCADE]))
        if first_only:
            return hits, latent, cycles
        hits += defaults[1:]
    implied = Obj(key=obj.key, parents=[p for p in obj.parents if p.implied])
    walk(implied, slot, root, [], {obj.key}, hits, latent, cycles, first_only)
    return hits, latent, cycles


def is_ancestor(a: Key, b: Key, root: Path, seen: set[Key] | None = None) -> bool:
    """True if a is reachable from b through explicit file parents."""
    seen = seen or set()
    for p in load_obj(b, root).parents:
        if p.target and not p.implied and p.target not in seen:
            if p.target == a or is_ancestor(a, p.target, root, seen | {p.target}):
                return True
    return False


def show(value: Any) -> str:
    if isinstance(value, Path):
        return f"<file {value.name}>"
    if isinstance(value, (str, int, float, bool)) or value is None:
        return repr(value) if isinstance(value, str) else str(value)
    text = yaml.safe_dump(value, default_flow_style=True, width=1000).strip()
    return text[:200] + ("…" if len(text) > 200 else "")


def rel(p: Path | Key, root: Path) -> str:
    path, frag = (p, "") if isinstance(p, Path) else p
    try:
        s = str(path.relative_to(root))
    except ValueError:
        s = str(path)
    return s + (f"#{frag}" if frag else "")


def key_of(addr: str) -> Key:
    path, frag = parse_address(addr)
    if not Path(path).exists():
        raise SystemExit(f"no such file or directory: {path}")
    return (Path(path).resolve(), frag)


def cmd_lookup(args: argparse.Namespace, root: Path) -> int:
    obj = load_obj(key_of(args.object), root)
    hits, latent, cycles = lookup(obj, args.slot, root, first_only=not args.all)
    for c in cycles:
        print(f"cycle skipped: {c}")
    if not hits:
        print(f"{args.slot}: not found in files")
        if latent:
            print("  latent parents the LLM tier would consult: " + "; ".join(dict.fromkeys(latent)))
        return 1
    seen_definers: set[Key] = set()
    for i, h in enumerate(hits):
        tag = ("found" if i == 0 else "cascade, merged under nearer containers" if h.via == [CASCADE] and i > 0 and hits[i - 1].via == [CASCADE]
               else "shadowed (diamond: reached again)" if h.definer in seen_definers else "shadowed")
        seen_definers.add(h.definer)
        path = " > ".join(h.via) or "(own slot)"
        print(f"{tag}: {rel(h.definer, root)}  via {path}\n  {args.slot} = {show(h.value)}")
    if args.all:
        branch_firsts: dict[str, Key] = {}
        for h in hits:
            if h.via and h.via[0] != CASCADE:
                branch_firsts.setdefault(h.via[0], h.definer)
        firsts = list(dict.fromkeys(branch_firsts.values()))
        if len(firsts) > 1 and hits[0].via:
            winner = firsts[0]
            rivals = [d for d in firsts[1:] if not is_ancestor(d, winner, root) and not is_ancestor(winner, d, root)]
            if rivals:
                print("self-4: ambiguous — parents define it in unrelated objects: "
                      + ", ".join(rel(d, root) for d in [winner, *rivals]) + "; MOOLLM order picks the first")
    return 0


def cmd_parents(args: argparse.Namespace, root: Path) -> int:
    def show_tree(obj: Obj, depth: int, seen: set[Key]) -> None:
        for p in obj.parents:
            target = f" -> {rel(p.target, root)}" if p.target else ""
            print("  " * depth + f"- {p.label()}{target}")
            if p.target and p.target not in seen:
                show_tree(load_obj(p.target, root), depth + 1, seen | {p.target})
            elif p.target:
                print("  " * (depth + 1) + "(already shown)")
    obj = load_obj(key_of(args.object), root)
    print(rel(obj.key, root))
    show_tree(obj, 1, {obj.key})
    return 0


def iter_yaml(paths: list[Path], root: Path) -> list[Path]:
    files: list[Path] = []
    for base in paths:
        if base.is_file():
            files.append(base)
            continue
        for p in base.rglob("*.yml"):
            parts = p.resolve().relative_to(root).parts if p.resolve().is_relative_to(root) else p.parts
            if not SKIP_DIRS.intersection(parts) and not (parts and parts[0] in LINT_SKIP_TOP):
                files.append(p)
    return files


def legacy_spellings(d: dict[str, Any], path: Path | None = None) -> list[str]:
    """Spellings that resolve accepts but would not emit."""
    env = envelope_key(path, d) if path else None
    d = flat(path, d) if path else d
    out = [f"envelope {env}:"] if env else []
    out += [f"{k}:" for k in ("parents", "parent", "extends") if k in d]
    if isinstance(d.get("prototype"), str):
        out.append("prototype: <ref>")
    if isinstance(d.get("prototypes"), list):
        out.append("prototypes: [list]")
    if isinstance(d.get("meta"), dict) and "inherits" in d["meta"]:
        out.append("meta.inherits:")
    if isinstance(d.get("container"), dict) and "inherits" in d["container"]:
        out.append("container.inherits: (use defaults:)")
    if isinstance(d.get("inherits"), dict) and not raw_parent_refs({"inherits": d["inherits"]}):
        out.append("inherits: {values} (slots, or defaults: on a container)")
    if isinstance(d.get("prototype"), dict) and "source" in d["prototype"]:
        out.append("prototype: {source, id} (use inherits: [file#collection.id])")
    if any(r.startswith("moollm/") for r, _ in raw_parent_refs(d)):
        out.append("moollm/ path prefix")
    keys = nested_keys(d)
    out += [f"{k}: (use done_when:)" for k in sorted(keys & DONE_WHEN_SPELLINGS)]
    out += [f"{k}: (use {SCHEMA_KEY_RENAMES[k]}:)" for k in sorted(keys & set(SCHEMA_KEY_RENAMES))]
    return out


DONE_WHEN_SPELLINGS = {"complete_when", "research_complete_when"}
# Schema keys are identifiers: the key in the file is the name in code. Names of things
# (skills, rooms, ids) keep their hyphens, so only known schema words are listed here.
SCHEMA_KEY_RENAMES = {"k-lines": "k_lines", "klines": "k_lines", "see-also": "see_also",
                      "invoked-by": "invoked_by"}


def nested_keys(v: Any) -> set[str]:
    if isinstance(v, dict):
        return set(map(str, v)).union(*(nested_keys(x) for x in v.values()))
    if isinstance(v, list):
        return set().union(*(nested_keys(x) for x in v))
    return set()


def cmd_lint(args: argparse.Namespace, root: Path) -> int:
    files = iter_yaml([Path(p) for p in (args.paths or [root])], root)
    declaring = file_refs = named = cycles = 0
    latent: dict[str, list[str]] = {}
    broken: dict[str, list[str]] = {}
    implied_latent: dict[str, list[str]] = {}
    implied_files: dict[str, list[str]] = {}
    unparsed: list[str] = []
    legacy: dict[str, list[str]] = {}
    shadows: list[str] = []  # a data slot with the same name as a child directory
    for f in files:
        data = load_yaml(f)
        if data is None and f.stat().st_size > 0:
            unparsed.append(rel(f, root))
            continue
        if not isinstance(data, dict):
            continue
        for variant in legacy_spellings(data, f):
            legacy.setdefault(variant, []).append(rel(f, root))
        if interface_name(f) and interface_name(f) not in VIEWS:
            for k, v in flat(f, data).items():
                child = f.parent / str(k)
                if child.is_dir() and not (isinstance(v, str) and v.rstrip("/") == str(k)):
                    shadows.append(f"{rel(f, root)}: {k}")
        obj = load_obj((f, ""), root)
        for p in obj.parents:
            if p.implied:
                if p.role == "subject":
                    continue
                bucket = implied_latent if p.latent else implied_files
                bucket.setdefault(p.ref, []).append(rel(f, root))
                continue
            named += p.role is not None
            if p.latent:
                # A path-shaped ref that names no file is a broken link, not a latent parent.
                (broken if "/" in p.ref else latent).setdefault(p.ref, []).append(rel(f, root))
            else:
                file_refs += 1
                if p.target == obj.key or is_ancestor(obj.key, p.target, root):
                    cycles += 1
                    print(f"cycle: {rel(f, root)} -> {p.ref}")
        declaring += any(not p.implied for p in obj.parents)

    def total(b: dict[str, list[str]]) -> str:
        return f"{sum(map(len, b.values()))} ({len(b)} distinct)"

    print(f"yaml files scanned:        {len(files)}")
    print(f"unparseable yaml:          {len(unparsed)}")
    print(f"objects declaring parents: {declaring}")
    print(f"parent refs to files:      {file_refs}")
    print(f"named parent slots (x*:):  {named}")
    print(f"latent parent refs:        {total(latent)}")
    print(f"broken path refs:          {total(broken)}")
    print(f"implied skills found:      {total(implied_files)}")
    print(f"implied skills latent:     {total(implied_latent)}")
    print(f"cycles:                    {cycles}")
    print(f"slots shadowing children:  {len(shadows)}")
    print(f"legacy spellings:          {sum(map(len, legacy.values()))}"
          + "".join(f"\n  {len(v):4d}  {k}" for k, v in sorted(legacy.items(), key=lambda kv: -len(kv[1]))))
    if args.verbose:
        if legacy:
            print("legacy:")
            for k, where in sorted(legacy.items()):
                for w in where:
                    print(f"  {k:28} {w}")
        for title, bucket in (("latent", latent), ("broken", broken), ("implied latent", implied_latent)):
            print(f"{title}:")
            for ref, where in sorted(bucket.items(), key=lambda kv: (-len(kv[1]), kv[0])):
                print(f"  {len(where):3d}  {ref[:50]!r:54}  {where[0]}")
        if shadows:
            print("slots shadowing children:")
            for s in shadows:
                print(f"  {s}")
        if unparsed:
            print("unparseable:")
            for u in unparsed:
                print(f"  {u}")
    if args.strict and (legacy or broken or cycles):
        return 1
    return 0


def git_times(root: Path) -> dict[Path, float]:
    """Last commit time per file, from one `git log` pass; uncommitted changes count as now."""
    import subprocess
    import time
    times: dict[Path, float] = {}
    log = subprocess.run(["git", "-C", str(root), "log", "--format=%x00%ct", "--name-only"],
                         capture_output=True, text=True, check=False).stdout
    t = 0.0
    for line in log.splitlines():
        if line.startswith("\x00"):
            t = float(line[1:])
        elif line:
            times.setdefault((root / line).resolve(), t)
    status = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "-uall"],
                            capture_output=True, text=True, check=False).stdout
    now = time.time()
    for line in status.splitlines():
        times[(root / line[3:].split(" -> ")[-1]).resolve()] = now
    return times


def view_subject_files(view: Path) -> list[Path]:
    """What a view summarizes: its directory's other files; for INDEX, everything below it."""
    d = view.parent
    files = d.rglob("*") if interface_name(view) == "INDEX" else d.iterdir()
    return [f for f in files if f.is_file() and interface_name(f) not in VIEWS
            and not SKIP_DIRS.intersection(f.parts) and not f.name.startswith(".")]


def cmd_stale(args: argparse.Namespace, root: Path) -> int:
    """Views whose subject changed after the view did. Git is the record; files carry no timestamps."""
    times = git_times(root)
    stale: list[tuple[float, str, str]] = []
    views = [f for f in iter_yaml([Path(p) for p in (args.paths or [root])], root) if interface_name(f) in VIEWS]
    for v in views:
        vt = times.get(v.resolve())
        if vt is None:
            continue
        newer = [(times[f.resolve()], f) for f in view_subject_files(v) if times.get(f.resolve(), 0) > vt]
        if newer:
            t, f = max(newer)
            stale.append((t - vt, rel(v, root), rel(f, root)))
    print(f"views checked: {len(views)}")
    print(f"stale views:   {len(stale)}")
    for lag, v, f in sorted(stale, reverse=True)[: None if args.verbose else 20]:
        print(f"  {lag / 86400:6.1f} days  {v}  (newer: {f})")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", help="repo root (default: nearest .git)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    lk = sub.add_parser("lookup", help="find a slot through the parent chain")
    lk.add_argument("object", help="directory, file, or file.yml#path.to.embedded")
    lk.add_argument("slot", help="slot name; dotted for nested keys")
    lk.add_argument("--all", action="store_true", help="show shadowed definitions and Self-4 ambiguity")
    pa = sub.add_parser("parents", help="print the parent tree")
    pa.add_argument("object")
    li = sub.add_parser("lint", help="tally parent declarations across YAML files")
    li.add_argument("paths", nargs="*")
    li.add_argument("--verbose", "-v", action="store_true")
    li.add_argument("--strict", action="store_true", help="exit 1 on legacy spellings, broken refs or cycles")
    st = sub.add_parser("stale", help="views (GLANCE, CARD, INDEX) older than what they summarize, per git")
    st.add_argument("paths", nargs="*")
    st.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args(argv)
    first = getattr(args, "object", None) or (args.paths[0] if getattr(args, "paths", None) else ".")
    start = Path(parse_address(first)[0]).resolve()
    root = Path(args.root).resolve() if args.root else find_root(start if start.is_dir() else start.parent)
    return {"lookup": cmd_lookup, "parents": cmd_parents, "lint": cmd_lint, "stale": cmd_stale}[args.cmd](args, root)


if __name__ == "__main__":
    sys.exit(main())
