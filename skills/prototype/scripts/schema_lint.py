#!/usr/bin/env python3
"""schema_lint.py — check MOOLLM objects against the schema files that exist.

Implements the linter half of designs/object-system/SCHEMA.md "Schema files" and
the projection-readiness irregularities of CARD-ANALYSIS.md section 7.

Schemas are discovered, not hard-coded: every skills/*/*.yml with a top-level
`schema:` map that has an `id` is one (ADVERTISEMENT.yml -> advertisement,
OBJECT.yml -> method, CARD.yml -> card, CHARACTER.yml -> character,
REPRESENTATION.yml -> representation). A missing schema switches off the checks
that need it (shape, range, enum, alias, default); the structural rules below
still run.

Schemas apply by context:
  CARD.yml                                  card
  each entry of any advertisements: block   advertisement
  each entry of any methods: block          method
  CHARACTER.yml                             character
  its representation:                       representation
Nothing descends into `schema:` or `*_schema:` keys; those describe objects, they
are not objects.

Rules (severity):
  unparseable                       error    YAML that does not load
  shape                             error    list where a map is expected, and so on
  shape.advertisements-list         error    advertisements: as a list
  shape.methods-list                error    methods: as a list
  shape.method-string               error    a method entry that is a bare string
  range, enum                       error    value outside range: or values:
  advertisement-no-score            warning  no numeric score (info when the schema's default applies)
  type-list                         warning  type: as a list (one id; the rest go to tags:)
  invoke-when-beside-advertisements warning  two places to look for one thing
  hyphenated-key                    warning  every hyphenated top-level CARD key; elsewhere, a
                                             hyphenated spelling of a schema key
  alias                             warning  an older spelling; names the canonical key
  default                           info     value equal to the default, removable
  internal                          error    the linter failed on a file (reported, not raised)

--cards restricts to CARD.yml files and the projection-readiness rules: unparseable,
the shape.* rules, advertisement-no-score, type-list, invoke-when-beside-advertisements,
hyphenated-key, all on the card's top level.

Usage:
    schema_lint.py [PATH ...] [--cards] [--format text|yaml] [--summary] [--root DIR]

--summary prints counts per rule instead of each finding. Exit 0 when there are
no errors; warnings and info are allowed.

Standard library plus PyYAML. Read-only.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

SKIP_DIRS = {".git", "node_modules", "dist", "__pycache__", ".moollm", "build"}
SKIP_TOP = {"temp"}  # archived imports at the repo root, as in resolve.py lint
EXPECTED = ("card", "advertisement", "method", "character", "representation")
FOREIGN_KEYS = {"allowed-tools"}  # foreign schemas keep their spelling (SCHEMA.md)
SEVERITIES = ("error", "warning", "info")
MAX_DEPTH = 40
STRING_SHAPES = {"string", "prose", "ref", "id", "path", "kline", "k_line", "url", "expression", "text"}
NUMBER_SHAPES = {"number", "int", "integer", "float"}
BOOL_SHAPES = {"bool", "boolean"}
LIST_SHAPES = {"list", "array", "seq", "sequence"}
MAP_SHAPES = {"map", "dict", "object", "mapping"}
SCALAR_SHAPES = {"enum", "scalar"}
MISSING = object()


@dataclass(frozen=True)
class Finding:
    file: str
    path: str
    rule: str
    severity: str
    message: str


@dataclass
class KeySpec:
    name: str
    shapes: list[str] = field(default_factory=list)
    range: tuple[float | None, float | None] | None = None
    values: list[Any] | None = None
    of: str | None = None
    default: Any = MISSING
    aliases: list[str] = field(default_factory=list)


@dataclass
class Schema:
    id: str
    source: str
    keys: dict[str, KeySpec] = field(default_factory=dict)
    aliases: dict[str, str] = field(default_factory=dict)  # alias -> canonical
    conventions: dict[str, Any] = field(default_factory=dict)
    extends: list[str] = field(default_factory=list)

    def has(self, convention: str) -> bool:
        return convention in self.conventions


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / ".git").exists():
            return p
    return start


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def load(path: Path) -> tuple[Any, str | None]:
    """(data, error). Multi-document files read their first document, as resolve.py does."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return None, f"cannot read: {e}"
    try:
        return yaml.safe_load(text), None
    except yaml.composer.ComposerError:
        try:
            return next(iter(yaml.safe_load_all(text)), None), None
        except yaml.YAMLError as e:
            return None, one_line(e)
    except yaml.YAMLError as e:
        return None, one_line(e)
    except Exception as e:  # recursion or constructor bugs on hostile input
        return None, f"{type(e).__name__}: {e}"


def one_line(e: Exception) -> str:
    mark = getattr(e, "problem_mark", None)
    where = f"line {mark.line + 1}: " if mark is not None else ""
    problem = getattr(e, "problem", None) or str(e).splitlines()[0]
    return f"{where}{problem}"


def as_list(v: Any) -> list[Any]:
    if v is None:
        return []
    if isinstance(v, list):
        return v
    if isinstance(v, str):
        return [s.strip() for s in v.split("|") if s.strip()]
    return [v]


def parse_range(v: Any) -> tuple[float | None, float | None] | None:
    """[lo, hi], 'lo..hi', or {min, max}; either end may be null."""
    def num(x: Any) -> float | None:
        if isinstance(x, bool) or x is None:
            return None
        try:
            return float(x)
        except (TypeError, ValueError):
            return None

    if isinstance(v, (list, tuple)) and len(v) == 2:
        return num(v[0]), num(v[1])
    if isinstance(v, str) and ".." in v:
        lo, hi = v.split("..", 1)
        return num(lo.strip() or None), num(hi.strip() or None)
    if isinstance(v, dict):
        return num(v.get("min")), num(v.get("max"))
    return None


def key_spec(name: str, raw: Any) -> KeySpec:
    """Postel: a key spec may be a map, a bare shape name, or nothing."""
    if isinstance(raw, str):
        return KeySpec(name, shapes=[s.lower() for s in as_list(raw)])
    if not isinstance(raw, dict):
        return KeySpec(name)
    values = raw.get("values")
    of = raw.get("of")
    return KeySpec(
        name=name,
        shapes=[str(s).strip().lower() for s in as_list(raw.get("shape"))],
        range=parse_range(raw.get("range")),
        values=values if isinstance(values, list) else None,
        of=str(of) if isinstance(of, str) and of.strip() else None,
        default=raw["default"] if raw.get("default") is not None else MISSING,
        aliases=[str(a) for a in as_list(raw.get("aliases")) if a is not None],
    )


def schema_from(block: dict[str, Any], source: str) -> Schema:
    s = Schema(id=str(block["id"]), source=source)
    keys = block.get("keys")
    if isinstance(keys, dict):
        for k, raw in keys.items():
            s.keys[str(k)] = key_spec(str(k), raw)
    conv = block.get("conventions")
    if isinstance(conv, dict):
        s.conventions = {str(k): v for k, v in conv.items()}
    elif isinstance(conv, list):
        s.conventions = {str(k): True for k in conv}
    s.extends = [str(x) for x in as_list(block.get("extends")) if x]
    return s


def merge_extends(schemas: dict[str, Schema]) -> None:
    """Fold extended schemas' keys in; own keys win. Cycle-safe."""
    def collect(sid: str, seen: set[str]) -> dict[str, KeySpec]:
        s = schemas.get(sid)
        if s is None or sid in seen:
            return {}
        seen.add(sid)
        out: dict[str, KeySpec] = {}
        for parent in s.extends:
            out.update(collect(parent, seen))
        out.update(s.keys)
        return out

    merged = {sid: collect(sid, set()) for sid in schemas}
    for sid, s in schemas.items():
        s.keys = merged[sid]
        s.aliases = {a: k for k, spec in s.keys.items() for a in spec.aliases if a not in s.keys}


def declares_schema(p: Path) -> bool:
    try:
        return re.search(r"^schema:\s*$", p.read_text(encoding="utf-8", errors="replace"), re.M) is not None
    except OSError:
        return False


def owns(s: Schema, p: Path) -> bool:
    """The file named for the schema is its home (ADVERTISEMENT.yml for advertisement); a CARD copy is a view."""
    return p.stem.lower() == s.id.lower() or (p.name not in ("CARD.yml", "GLANCE.yml", "INDEX.yml"))


def load_schemas(root: Path) -> tuple[dict[str, Schema], list[str]]:
    """Every skills/*/*.yml with a top-level schema: {id: ...}. Problems are returned, not raised."""
    schemas: dict[str, Schema] = {}
    problems: list[str] = []
    skills = root / "skills"
    files = sorted([*skills.glob("*/*.yml"), *skills.glob("*/*.yaml")]) if skills.is_dir() else []
    for p in files:
        data, err = load(p)
        if err:
            if declares_schema(p):
                problems.append(f"{rel(p, root)}: unparseable ({err}); its schema is skipped")
            continue
        block = data.get("schema") if isinstance(data, dict) else None
        if not isinstance(block, dict) or not isinstance(block.get("id"), (str, int)):
            continue
        try:
            s = schema_from(block, rel(p, root))
        except Exception as e:
            problems.append(f"{rel(p, root)}: bad schema block ({type(e).__name__}: {e})")
            continue
        old = schemas.get(s.id)
        if old is not None:
            keep, drop = (s, old) if owns(s, p) and not owns(old, root / old.source) else (old, s)
            problems.append(f"{drop.source}: schema id {s.id!r} also in {keep.source}; using {keep.source}")
            s = keep
        schemas[s.id] = s
    merge_extends(schemas)
    return schemas, problems


def shape_of(v: Any) -> str:
    if isinstance(v, dict):
        return "map"
    if isinstance(v, list):
        return "list"
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, (int, float)):
        return "number"
    if isinstance(v, str):
        return "string"
    if v is None:
        return "null"
    return type(v).__name__


def is_number(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def shape_ok(v: Any, shape: str, schema: Schema | None, known: dict[str, Schema]) -> bool:
    """Containers are strict; scalars are Postel (a number where prose is expected passes)."""
    scalar = not isinstance(v, (dict, list))
    if shape in STRING_SHAPES or shape in SCALAR_SHAPES:
        return scalar
    if shape in NUMBER_SHAPES:
        return is_number(v)
    if shape in BOOL_SHAPES:
        return isinstance(v, bool)
    if shape in LIST_SHAPES:
        if isinstance(v, list):
            return True
        if schema and schema.has("list_of_one") and scalar:
            return True
        if schema and schema.has("any_all_not") and isinstance(v, dict) and set(map(str, v)) <= {"all", "any", "not"}:
            return True
        return False
    if shape in MAP_SHAPES or shape in known:
        return isinstance(v, dict)
    if shape in ("null", "none"):
        return v is None
    return True  # "any" and shape names this linter doesn't know


def same(a: Any, b: Any) -> bool:
    if isinstance(a, bool) or isinstance(b, bool):
        return isinstance(a, bool) and isinstance(b, bool) and a == b
    if is_number(a) and is_number(b):
        return a == b
    return type(a) is type(b) and a == b


def join(path: str, key: Any) -> str:
    if isinstance(key, int) and not isinstance(key, bool):
        return f"{path}[{key}]"
    k = str(key)
    if "." in k or " " in k or "[" in k:
        k = f'["{k}"]'
        return f"{path}{k}"
    return f"{path}.{k}" if path else k


class Linter:
    def __init__(self, root: Path, schemas: dict[str, Schema], cards_only: bool = False) -> None:
        self.root = root
        self.schemas = schemas
        self.cards_only = cards_only
        self.findings: list[Finding] = []
        self.files = 0
        self._seen: set[tuple[str, str, str, str]] = set()
        self._claimed: set[tuple[str, str]] = set()
        self._file = ""

    def add(self, path: str, rule: str, severity: str, message: str, claim: bool = False) -> None:
        """claim=True: this finding owns the path, and later generic shape findings there are dropped."""
        if rule == "shape" and not claim and (self._file, path) in self._claimed:
            return
        key = (self._file, path, rule, message)
        if key not in self._seen:
            self._seen.add(key)
            self.findings.append(Finding(self._file, path, rule, severity, message))
        if claim:
            self._claimed.add((self._file, path))

    def lint_file(self, path: Path) -> None:
        self._file = rel(path, self.root)
        self.files += 1
        try:
            self._lint_file(path)
        except RecursionError:
            self.add("", "internal", "error", "structure too deep to lint")
        except Exception as e:
            self.add("", "internal", "error", f"linter failed: {type(e).__name__}: {e}")

    def _lint_file(self, path: Path) -> None:
        data, err = load(path)
        if err:
            self.add("", "unparseable", "error", err)
            return
        if data is None:
            return
        if not self.cards_only:
            self.walk(data, "", 0, set())  # structural findings first: they claim paths
        name = path.name
        if name in ("CARD.yml", "CARD.yaml"):
            self.lint_card(data)
        elif name in ("CHARACTER.yml", "CHARACTER.yaml") and not self.cards_only:
            self.lint_character(data)

    def envelope(self, data: dict[str, Any], key: str) -> tuple[dict[str, Any], str]:
        """A legacy `card:` / `character:` wrapper is read as if flat; paths keep the wrapper."""
        inner = data.get(key)
        if isinstance(inner, dict) and len(data) <= 3:
            return inner, key
        return data, ""

    def lint_card(self, data: Any) -> None:
        if not isinstance(data, dict):
            self.add("", "shape", "error", f"a CARD is a map, got {shape_of(data)}")
            return
        d, prefix = self.envelope(data, "card")
        self.top_level_rules(d, prefix, hyphen_all=True)
        if self.cards_only:
            if "advertisements" in d:
                self.check_adverts(d["advertisements"], join(prefix, "advertisements"))
            if "methods" in d:
                self.check_methods(d["methods"], join(prefix, "methods"))
            return
        self.apply(self.schemas.get("card"), d, prefix)

    def lint_character(self, data: Any) -> None:
        if not isinstance(data, dict):
            self.add("", "shape", "error", f"a CHARACTER is a map, got {shape_of(data)}")
            return
        d, prefix = self.envelope(data, "character")
        self.top_level_rules(d, prefix, hyphen_all=False)
        rep = d.get("representation")
        rpath = join(prefix, "representation")
        if rep is not None and not isinstance(rep, dict):
            self.add(rpath, "shape", "error", f"representation: is a map, got {shape_of(rep)}", claim=True)
        self.apply(self.schemas.get("character"), d, prefix)
        if isinstance(rep, dict):
            self.apply(self.schemas.get("representation"), rep, rpath)

    def top_level_rules(self, d: dict[str, Any], prefix: str, hyphen_all: bool) -> None:
        t = d.get("type")
        if isinstance(t, list):
            p = join(prefix, "type")
            self.add(p, "type-list", "warning", f"type: is a list of {len(t)}; one id, the rest go to tags:", claim=True)
        if "invoke_when" in d and "advertisements" in d:
            self.add(join(prefix, "invoke_when"), "invoke-when-beside-advertisements", "warning",
                     "invoke_when: beside advertisements:; each line is a score_if: for an advertisement")
        if hyphen_all:
            for k in d:
                k = str(k)
                if "-" in k and k not in FOREIGN_KEYS:
                    self.add(join(prefix, k), "hyphenated-key", "warning", self.hyphen_message(k, self.schemas.get("card")))

    def hyphen_message(self, k: str, schema: Schema | None) -> str:
        u = k.replace("-", "_")
        if schema and u in schema.keys:
            return f"{k}: is the schema key {u}: spelled with hyphens"
        if schema and u in schema.aliases:
            return f"{k}: is the alias {u}: of {schema.aliases[u]}: spelled with hyphens"
        return f"{k}: schema keys use underscores ({u}:)"

    def apply(self, schema: Schema | None, obj: dict[str, Any], path: str, depth: int = 0) -> None:
        """Check each key of obj that the schema names; unknown keys are YAML Jazz."""
        if schema is None or depth > MAX_DEPTH:
            return
        for raw_k, v in obj.items():
            k = str(raw_k)
            p = join(path, k)
            if k in schema.keys:
                self.check_value(schema, schema.keys[k], v, p, depth)
            elif k in schema.aliases:
                canon = schema.aliases[k]
                self.add(p, "alias", "warning", f"{k}: is an alias; the canonical key is {canon}:")
            elif "-" in k and k not in FOREIGN_KEYS and k not in schema.keys:
                u = k.replace("-", "_")
                if u in schema.keys or u in schema.aliases:
                    self.add(p, "hyphenated-key", "warning", self.hyphen_message(k, schema))

    def check_value(self, schema: Schema, spec: KeySpec, v: Any, path: str, depth: int) -> None:
        if v is None:
            return
        if spec.shapes and not any(shape_ok(v, s, schema, self.schemas) for s in spec.shapes):
            self.add(path, "shape", "error", f"{spec.name}: expected {' | '.join(spec.shapes)}, got {shape_of(v)}")
            return
        if spec.range and is_number(v):
            lo, hi = spec.range
            if (lo is not None and v < lo) or (hi is not None and v > hi):
                shown = f"[{'' if lo is None else fmt(lo)}, {'' if hi is None else fmt(hi)}]"
                self.add(path, "range", "error", f"{spec.name}: {v} is outside {shown}")
        if spec.values is not None:
            items = v if isinstance(v, list) else [v]
            for x in items:
                if not isinstance(x, (dict, list)) and not any(same(x, y) for y in spec.values):
                    self.add(path, "enum", "error", f"{spec.name}: {x!r} is not one of {spec.values}")
        if spec.default is not MISSING and same(v, spec.default):
            self.add(path, "default", "info", f"{spec.name}: {v!r} is the default; removable")
        if spec.of:
            self.check_elements(schema, spec, v, path, depth)

    def check_elements(self, schema: Schema, spec: KeySpec, v: Any, path: str, depth: int) -> None:
        elems: Iterable[tuple[Any, Any]]
        if isinstance(v, dict):
            elems = v.items()
        elif isinstance(v, list):
            elems = enumerate(v)
        else:
            return
        sub = self.schemas.get(spec.of or "")
        for k, x in elems:
            p = join(path, k)
            if sub is not None:
                if isinstance(x, dict):
                    self.apply(sub, x, p, depth + 1)
                elif x is not None:
                    self.add(p, "shape", "error", f"{spec.name} entry: expected map ({sub.id}), got {shape_of(x)}")
            else:
                inner = KeySpec(f"{spec.name} entry", shapes=[s.strip().lower() for s in as_list(spec.of)])
                self.check_value(schema, inner, x, p, depth + 1)

    def walk(self, node: Any, path: str, depth: int, stack: set[int]) -> None:
        """Find advertisements: and methods: blocks at any depth, outside schema descriptions."""
        if depth > MAX_DEPTH or id(node) in stack:
            return
        if isinstance(node, dict):
            stack.add(id(node))
            if "invoke_when" in node and "advertisements" in node:
                self.add(join(path, "invoke_when"), "invoke-when-beside-advertisements", "warning",
                         "invoke_when: beside advertisements:; each line is a score_if: for an advertisement")
            for raw_k, v in node.items():
                k = str(raw_k)
                if k == "schema" or k.endswith("_schema"):
                    continue
                p = join(path, k)
                if k == "advertisements":
                    self.check_adverts(v, p)
                elif k == "methods":
                    self.check_methods(v, p)
                self.walk(v, p, depth + 1, stack)
            stack.discard(id(node))
        elif isinstance(node, list):
            stack.add(id(node))
            for i, x in enumerate(node):
                self.walk(x, join(path, i), depth + 1, stack)
            stack.discard(id(node))

    def check_adverts(self, block: Any, path: str) -> None:
        schema = self.schemas.get("advertisement")
        if block is None:
            return
        if isinstance(block, list):
            self.add(path, "shape.advertisements-list", "error",
                     f"advertisements: is a list of {len(block)}; a map keyed by name (action:) is expected", claim=True)
            entries: Iterable[tuple[Any, Any]] = enumerate(block)
        elif isinstance(block, dict):
            entries = block.items()
        else:
            self.add(path, "shape", "error", f"advertisements: expected map, got {shape_of(block)}", claim=True)
            return
        for k, e in entries:
            p = join(path, k)
            if not isinstance(e, dict):
                if e is not None:
                    self.add(p, "shape", "error", f"advertisement: expected map, got {shape_of(e)}")
                continue
            self.check_score(e, p, schema)
            if not self.cards_only:
                self.apply(schema, e, p)

    def check_score(self, e: dict[str, Any], path: str, schema: Schema | None) -> None:
        names = ["score"] + ([a for a, c in schema.aliases.items() if c == "score"] if schema else [])
        present = [n for n in names if n in e and e[n] is not None]
        if not present:
            spec = schema.keys.get("score") if schema else None
            if spec is not None and spec.default is not MISSING:
                self.add(path, "advertisement-no-score", "info", f"no score; the default {spec.default!r} applies")
            else:
                self.add(path, "advertisement-no-score", "warning", "no score")
            return
        n = present[0]
        v = e[n]
        if not is_number(v):
            p = join(path, n)
            self.add(p, "advertisement-no-score", "warning", f"{n}: is {shape_of(v)} {short(v)}, not a number", claim=True)

    def check_methods(self, block: Any, path: str) -> None:
        schema = self.schemas.get("method")
        if block is None:
            return
        if isinstance(block, list):
            self.add(path, "shape.methods-list", "error",
                     f"methods: is a list of {len(block)}; a map keyed by method name is expected", claim=True)
            for i, e in enumerate(block):
                p = join(path, i)
                if isinstance(e, dict) and len(e) == 1 and isinstance(next(iter(e.values())), dict):
                    name, body = next(iter(e.items()))
                    self.method_entry(name, body, join(p, name), schema)
                elif isinstance(e, dict):
                    self.method_entry(e.get("name", i), e, p, schema)
            return
        if not isinstance(block, dict):
            self.add(path, "shape", "error", f"methods: expected map, got {shape_of(block)}", claim=True)
            return
        for name, e in block.items():
            self.method_entry(name, e, join(path, name), schema)

    def method_entry(self, name: Any, e: Any, path: str, schema: Schema | None) -> None:
        if e is None:
            return
        if isinstance(e, str):
            self.add(path, "shape.method-string", "error",
                     f"method {name} is a bare string; a map ({{description: ...}}) is expected", claim=True)
            return
        if not isinstance(e, dict):
            self.add(path, "shape", "error", f"method {name}: expected map, got {shape_of(e)}")
            return
        if not self.cards_only:
            self.apply(schema, e, path)


def fmt(x: float) -> str:
    return str(int(x)) if float(x).is_integer() else str(x)


def short(v: Any) -> str:
    s = repr(v)
    return s if len(s) <= 40 else s[:37] + "..."


def iter_files(paths: list[Path], root: Path, cards_only: bool) -> list[Path]:
    def wanted(p: Path) -> bool:
        if cards_only:
            return p.name in ("CARD.yml", "CARD.yaml")
        return p.suffix in (".yml", ".yaml")

    out: list[Path] = []
    for base in paths:
        if base.is_file():
            if wanted(base):
                out.append(base)
            continue
        if not base.is_dir():
            continue
        for p in sorted([*base.rglob("*.yml"), *base.rglob("*.yaml")]):
            r = rel(p, root)
            parts = Path(r).parts
            if SKIP_DIRS.intersection(parts) or (parts and parts[0] in SKIP_TOP and not r.startswith("..")):
                continue
            if p.is_file() and wanted(p):
                out.append(p)
    seen: set[Path] = set()
    unique = []
    for p in out:
        k = p.resolve()
        if k not in seen:
            seen.add(k)
            unique.append(p)
    return unique


def summarize(lint: Linter, schemas: dict[str, Schema], problems: list[str]) -> dict[str, Any]:
    counts: dict[tuple[str, str], int] = collections.Counter((f.rule, f.severity) for f in lint.findings)
    files: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    for f in lint.findings:
        files[(f.rule, f.severity)].add(f.file)
    sev = collections.Counter(f.severity for f in lint.findings)
    order = sorted(counts, key=lambda rs: (SEVERITIES.index(rs[1]), -counts[rs], rs[0]))
    return {
        "schemas_found": {sid: schemas[sid].source for sid in sorted(schemas)},
        "schemas_missing": [s for s in EXPECTED if s not in schemas],
        "schema_problems": problems,
        "files_scanned": lint.files,
        "totals": {s: sev.get(s, 0) for s in SEVERITIES},
        "rules": [{"rule": r, "severity": s, "count": counts[(r, s)], "files": len(files[(r, s)])} for r, s in order],
    }


def print_summary(s: dict[str, Any]) -> None:
    found = ", ".join(f"{k} ({v})" for k, v in s["schemas_found"].items()) or "none"
    print(f"schemas found:   {found}")
    print(f"schemas missing: {', '.join(s['schemas_missing']) or 'none'}")
    for p in s["schema_problems"]:
        print(f"  schema problem: {p}")
    print(f"files scanned:   {s['files_scanned']}")
    t = s["totals"]
    print(f"findings:        {t['error']} errors, {t['warning']} warnings, {t['info']} info")
    for r in s["rules"]:
        print(f"  {r['count']:6d}  {r['severity']:7s}  {r['rule']:34s} in {r['files']} files")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*", help="files or directories (default: repo root)")
    ap.add_argument("--cards", action="store_true", help="CARD.yml projection-readiness rules only")
    ap.add_argument("--format", choices=("text", "yaml"), default="text")
    ap.add_argument("--summary", action="store_true", help="counts per rule instead of each finding")
    ap.add_argument("--root", help="repo root, where skills/ schemas are read (default: nearest .git)")
    args = ap.parse_args(argv)

    targets = [Path(p) for p in args.paths] or [Path.cwd()]
    start = targets[0].resolve()
    root = Path(args.root).resolve() if args.root else find_root(start if start.is_dir() else start.parent)
    if not args.paths:
        targets = [root]
    for t in targets:
        if not t.exists():
            print(f"schema_lint: no such path: {t}", file=sys.stderr)
    schemas, problems = load_schemas(root)
    lint = Linter(root, schemas, cards_only=args.cards)
    for f in iter_files(targets, root, args.cards):
        lint.lint_file(f)

    if args.summary:
        s = summarize(lint, schemas, problems)
        if args.format == "yaml":
            print(yaml.safe_dump(s, sort_keys=False, allow_unicode=True), end="")
        else:
            print_summary(s)
    elif args.format == "yaml":
        print(yaml.safe_dump([asdict(f) for f in lint.findings], sort_keys=False, allow_unicode=True), end="")
    else:
        for f in lint.findings:
            where = f"{f.file}:{f.path}" if f.path else f.file
            print(f"{where}: {f.severity}: [{f.rule}] {f.message}")
        t = collections.Counter(f.severity for f in lint.findings)
        print(f"{lint.files} files, {t['error']} errors, {t['warning']} warnings, {t['info']} info")
    return 1 if any(f.severity == "error" for f in lint.findings) else 0


if __name__ == "__main__":
    sys.exit(main())
