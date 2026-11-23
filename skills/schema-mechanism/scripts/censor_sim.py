#!/usr/bin/env python3
"""censor_sim: Minsky's AI Memo 603 censors, run on Drescher's schema mechanism.

A schema is context -> action -> result with a reliability. A censor is a
schema with the sign bit flipped: same triple, result marked harmful, stored
response "suppress". Precursor censors veto an action before it runs, so the
agent never sees the thought, only the cover story it tells itself.
Suppressors fire after a forbidden state forms and re-file it under another
frame. Marginal attribution over painful results mints new censors. A joke
makes a firing visible to the agent, which is how censors get retrained.

Two traces: INNER is what the agent experiences; OBSERVER also records
every censor that fired. The gap between them is the cognitive unconscious.

THE CLI NEVER CALLS AN LLM. It is the deterministic tier, cheap enough to
run thousands of times a second. What it can't compute, it asks for:

  stdout  the data you asked for (--format text|md|yaml|json)
  stderr  one JSON event per line: REQUEST, ERROR, WARNING, INFO, RESULT,
          TELEMETRY. Request ids are hashes of what's being asked, so the
          same open question has the same id in every invocation, and any
          number of threads can be tracked from outside with jq or grep.

A request carries a `patch`: the YAML layer that would answer it. Whoever
answers (an LLM in a chat, a person, another program) writes that layer to
a file and passes it back with --layer FILE, or merges it into a file with
`apply`. The loop lives outside the tool, so it composes: files in, files
out, filters in between.

Scenarios inherit personality modules (`inherits: [file, ...]`, relative,
recursive, multiple: a part two parents share is merged once, where it
first appears). `imports: [{from: FILE, take: [id, values.KEY]}]` takes
single traits from an archetype without the rest of it. Layers merge in
order: dicts merge, lists of `id`ed entries
(schemas, censors) merge by id, `drop: true` deletes one, anything else is
replaced. `who:` fills `{name}` placeholders in every string. A scenario
path of `-` reads YAML from stdin.

Commands:
  resolve  FILE...        merge files and layers, print the result     (read/transform)
  lint     FILE           check a scenario; emit requests and warnings
  run      FILE           run it; print the traces                     (run)
  test     FILE           exit 2 unless every factual run fits its record and expectations
  ablate   FILE           drop each censor in turn: which does the record need?
  sweep    FILE           perturb value weights N times: do conclusions depend on them?
  predict  FILE --offers A,B [--set-item K=on]  what each run does next, over N weightings
  induce   FILE [--run R]  learn contexts from the record: which items made each choice likelier
  bench    FILE           time N unperturbed runs                      (benchmark)
  diff     A B            compare two resolved minds: shared logic, different priorities
  where    FILE PATTERN   which layer defines what matches PATTERN     (search)
  lineage  FILE           the parts a mind is built from, in merge order
  export   FILE           resolved model as json, or a censor graph as dot
  import   TEXT           split a message thread into skeleton events + requests
  apply    PATCH --into F merge a patch layer into a file               (write)

Common options: --layer FILE (repeatable), --who k=v, --set a.b.c=value
(lists of id'd entries are addressed by id: censors.too-long.cover=...),
--format, -o FILE, --events FILE (default stderr), --quiet (no INFO).

Exit codes: 0 ok, 1 errors, 2 test failure, 3 unanswered requests (--strict).
"""

import argparse
import hashlib
import json
import os
import random
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass, field, fields

import yaml

ON, OFF = True, False
OVERRIDE = 0.6      # a visible censor below this reliability can be overridden
CONTRAST = 0.5      # P(pain | item ON) - P(pain | item OFF) to join a context


# == events: the engine's only voice to the outside =========================
class Bus:
    LEVELS = ("REQUEST", "ERROR", "WARNING", "INFO", "RESULT", "TELEMETRY")

    def __init__(self, stream=None, quiet=False, thread=""):
        self.stream, self.quiet, self.thread = stream, quiet, thread
        self.counts = Counter()
        self.seen = set()
        self.open_requests = {}
        self.seq = 0

    def emit(self, type_, kind, msg, key=None, **params):
        """key: what makes this event the same event next time (gives a stable id)."""
        if key is not None:
            eid = f"{type_[:3].lower()}-{kind}-" + hashlib.sha1(
                json.dumps(key, sort_keys=True, default=str).encode()).hexdigest()[:10]
            if eid in self.seen:
                return eid
            self.seen.add(eid)
        else:
            self.seq += 1
            eid = f"{type_[:3].lower()}-{kind}-{self.seq}"
        self.counts[type_] += 1
        if type_ == "REQUEST":
            self.open_requests[eid] = msg
        if self.stream and not (self.quiet and type_ == "INFO"):
            ev = {"id": eid, "type": type_, "kind": kind, "thread": self.thread, "msg": msg}
            ev.update({k: v for k, v in params.items() if v is not None})
            self.stream.write(json.dumps(ev, default=str) + "\n")
            self.stream.flush()
        return eid


NULL = Bus()


# == the model ===============================================================
@dataclass
class Schema:
    id: str
    action: str
    context: list
    result: dict
    reliability: float = 1.0
    note: str = ""
    source: str = ""


@dataclass
class Censor:
    id: str
    kind: str                     # precursor | suppressor
    context: list
    action: str = ""              # precursor: the action it vetoes
    state: list = field(default_factory=list)   # suppressor: the forbidden state
    refile: dict = field(default_factory=dict)  # suppressor: frame substitution
    harm: list = field(default_factory=list)
    cover: str = ""               # what the agent tells itself instead
    source: str = ""              # whose words the cover is
    reliability: float = 1.0
    learned_from: str = ""
    anecdotal: bool = False
    visible: bool = False         # a joke has exposed it to the agent
    note: str = ""

    def matches(self, items):
        return all(holds(items, c) for c in self.context)

    @property
    def generated(self):
        return self.source.startswith("tier0")


def build(cls, d):
    names = {f.name for f in fields(cls)}
    return cls(**{k: v for k, v in d.items() if k in names})


def holds(items, cond):
    """'x' means x is ON; '!x' means x is OFF."""
    if cond.startswith("!"):
        return items.get(cond[1:]) is OFF
    return items.get(cond) is ON


def parse_value(v):
    if v in (True, "on", "ON"):
        return ON
    if v in (False, "off", "OFF"):
        return OFF
    return None


# == layers: inheritance, casting, transforms ================================
def merge(base, over):
    if isinstance(base, dict) and isinstance(over, dict):
        out = dict(base)
        for k, v in over.items():
            out[k] = merge(base[k], v) if k in base else v
        return out
    key = keyed(base, over)
    if key:
        out = {x[key]: x for x in base}
        order = [x[key] for x in base]
        for x in over:
            if x.get("drop"):
                out.pop(x[key], None)
            elif x[key] in out:
                out[x[key]] = merge(out[x[key]], {k: v for k, v in x.items()})
            else:
                out[x[key]] = x
                order.append(x[key])
        return [out[i] for i in order if i in out]
    return over


def keyed(base, over):
    """Schemas and censors merge by id, events by t; other lists replace."""
    if not (isinstance(base, list) and isinstance(over, list) and base and over):
        return None
    both = base + over
    for key in ("id", "t"):
        if all(isinstance(x, dict) and key in x for x in both):
            return key
    return None


def read_yaml(path):
    if path == "-":
        return yaml.safe_load(sys.stdin) or {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def chain(path, _seen=()):
    """Every file in the inheritance chain, base first, with its raw YAML."""
    real = "-" if path == "-" else os.path.abspath(path)
    if real in _seen:
        raise ValueError(f"inheritance loop at {path}")
    raw = read_yaml(path)
    here = os.getcwd() if path == "-" else os.path.dirname(real)
    parents = raw.get("inherits", []) or []
    out = []
    for p in [parents] if isinstance(parents, str) else parents:
        out += chain(os.path.join(here, p), _seen + (real,))
    return out + [(real, raw)]


def linearize(paths, layers=()):
    """Base first, each file once. A part two parents share is merged where
    it first appears, so it can't come back later and undo an override."""
    seen, out = set(), []
    for p in list(paths) + list(layers):
        for real, raw in chain(p):
            if real != "-" and real in seen:
                continue
            seen.add(real)
            out.append((real, raw))
    return out


def merged(paths, layers=()):
    spec = {}
    for real, raw in linearize(paths, layers):
        spec = merge(spec, imported(real, raw))
        spec = merge(spec, {k: v for k, v in raw.items() if k not in ("inherits", "imports", "part")})
    return spec


def imported(real, raw):
    """`imports: [{from: FILE, take: [id, values.KEY, ...]}]`: one trait out
    of an archetype, without the rest of it. No `take` means all of FILE."""
    out = {}
    here = os.getcwd() if real == "-" else os.path.dirname(real)
    for imp in raw.get("imports") or []:
        src = merged([os.path.join(here, imp["from"])])
        if imp.get("take") is None:
            out = merge(out, src)
            continue
        pick = {}
        for name in imp["take"]:
            if name.startswith("values."):
                key = name[len("values."):]
                if key not in src.get("agent", {}).get("values", {}):
                    raise ValueError(f"import: {imp['from']} has no value {key}")
                pick = merge(pick, {"agent": {"values": {key: src["agent"]["values"][key]}}})
                continue
            hits = {sec: [x for x in src.get(sec, []) if x.get("id") == name] for sec in ("censors", "schemas")}
            if not any(hits.values()):
                raise ValueError(f"import: {imp['from']} has no censor or schema {name}")
            pick = merge(pick, {sec: xs for sec, xs in hits.items() if xs})
        out = merge(out, pick)
    return out


def load(paths, layers=(), who=(), sets=()):
    spec = merged(paths, layers)
    for kv in who:
        k, _, v = kv.partition("=")
        spec.setdefault("who", {})[k] = v
    for kv in sets:
        path, _, v = kv.partition("=")
        set_path(spec, path, yaml.safe_load(v))
    return cast(spec)


def set_path(spec, dotted, value):
    node, parts = spec, dotted.split(".")
    for i, part in enumerate(parts):
        last = i == len(parts) - 1
        if isinstance(node, list):
            hit = next((x for x in node if isinstance(x, dict) and x.get("id") == part), None)
            if hit is None:
                hit = {"id": part}
                node.append(hit)
            node = hit
            if last:
                raise ValueError(f"--set {dotted}: name a field of '{part}'")
            continue
        if last:
            node[part] = value
        else:
            node = node.setdefault(part, {})


def cast(spec):
    """Fill {name} placeholders from `who:`; unknown names stay as written."""
    who = spec.get("who", {}) or {}

    def fill(x):
        if isinstance(x, str):
            return re.sub(r"\{([\w-]+)\}", lambda m: str(who.get(m.group(1), m.group(0))), x)
        if isinstance(x, list):
            return [fill(v) for v in x]
        if isinstance(x, dict):
            return {k: fill(v) for k, v in x.items()}
        return x
    return fill(spec)


# == the mind ================================================================
class Mind:
    def __init__(self, spec, bus=NULL, learn_threshold=2):
        a = spec["agent"]
        self.name = a["name"]
        self.items = {k: parse_value(v) for k, v in a.get("items", {}).items()}
        self.values = a.get("values", {})
        self.contradictions = [tuple(p) for p in a.get("contradictions", [])]
        self.schemas = [build(Schema, s) for s in spec.get("schemas", [])]
        # A censor entry with no `kind` is a patch waiting for a learned censor.
        self.censors = [build(Censor, c) for c in spec.get("censors", []) if "kind" in c]
        self.patches = {c["id"]: c for c in spec.get("censors", []) if "kind" not in c}
        self.bus = bus
        self.learn_threshold = learn_threshold
        self.trials = {}              # action -> [(items before, hurt?)]
        self.inner, self.observer = [], []
        self.fit = []                 # (t, observed action, model's action)
        self.choices = []             # (t, model's action)
        self.situations = []          # (t, offers, observed, items before)

    def log(self, t, text, inner=True, quote=None):
        entry = {"t": t, "text": text, "inner": inner}
        if quote:
            entry["quote"] = quote
        self.observer.append(entry)
        if inner:
            self.inner.append(entry)

    def on_items(self, items=None):
        return sorted(k for k, v in (items or self.items).items() if v is ON)

    # -- schema machinery -------------------------------------------------
    def schema_for(self, action, items=None):
        items = items if items is not None else self.items
        fits = [s for s in self.schemas
                if s.action == action and all(holds(items, c) for c in s.context)]
        best = max(fits, key=lambda s: (len(s.context), s.reliability), default=None)
        if not best and not any(s.action == action for s in self.schemas):
            self.request_schema(action, items)
        return best

    def request_schema(self, action, items):
        self.bus.emit(
            "REQUEST", "schema", f"no schema says what '{action}' does",
            key={"agent": self.name, "action": action},
            action=action, items_on=self.on_items(items), values=self.values,
            patch={"schemas": [{"id": action, "action": action, "context": [],
                                "result": {"<item>": "on|off"}, "reliability": "<0..1>",
                                "source": "tier0: <who answered>"}]})

    def predicted_value(self, action):
        s = self.schema_for(action)
        if not s:
            return 0.0
        v = sum(self.values.get(k, 0) * (1 if val else -1) for k, val in s.result.items())
        return v * s.reliability

    def vetoed(self, action):
        # A censor the agent can see, and no longer trusts, can be overridden.
        # A censor whose harms have all already happened has nothing to guard.
        hits = [c for c in self.censors
                if c.kind == "precursor" and c.action == action and c.matches(self.items)
                and not (c.visible and c.reliability < OVERRIDE)
                and not (c.harm and all(self.items.get(h) is ON for h in c.harm))]
        # Anecdotal censors outrank the general ones they patch.
        hits.sort(key=lambda c: (not c.anecdotal, -c.reliability))
        return hits

    def cover_for(self, c):
        if not c.cover:
            self.bus.emit(
                "REQUEST", "cover", f"censor {c.id} fired with no cover story",
                key={"agent": self.name, "censor": c.id},
                censor=c.id, vetoes=c.action, guards=c.harm, context=c.context,
                items_on=self.on_items(),
                ask=f"one sentence {self.name} tells itself instead of '{c.action}', "
                    "unaware of the censor; for a real person, their own words or nothing",
                patch={"censors": [{"id": c.id, "cover": "<sentence>",
                                    "source": "tier0: <who answered>"}]})
        return c.cover

    def decide(self, t, offers):
        open_, covers = [], []
        for act in offers:
            hits = self.vetoed(act)
            if hits:
                c = hits[0]
                self.log(t, f"censor {c.id} vetoes '{act}' (predicts {', '.join(c.harm)})",
                         inner=c.visible)
                if self.cover_for(c):
                    covers.append(c)
            else:
                open_.append(act)
        if not open_:
            self.log(t, "every option vetoed; does nothing")
            return None, covers
        return max(open_, key=self.predicted_value), covers

    def apply(self, action):
        s = self.schema_for(action)
        for k, v in (s.result.items() if s else []):
            self.items[k] = parse_value(v) if not isinstance(v, bool) else v

    # -- suppressors: after the fact ---------------------------------------
    def conflicts(self):
        return [(a, b) for a, b in self.contradictions
                if self.items.get(a) is ON and self.items.get(b) is ON]

    def suppress(self, t):
        for c in self.censors:
            if c.kind != "suppressor" or not c.matches(self.items):
                continue
            if all(self.items.get(s) is ON for s in c.state):
                for k, v in c.refile.items():
                    self.items[k] = parse_value(v)
                self.log(t, f"suppressor {c.id} re-files {c.state} as {c.refile}",
                         inner=c.visible)
                if c.cover:
                    self.log(t, f"thinks: \"{c.cover}\"" + (" [PI]" if c.generated else ""))

    # -- learning: marginal attribution over pain --------------------------
    def discriminating(self, action):
        """Drescher's extended context, for pain: start from the positive
        schema's own context (a censor is that schema, sign flipped), then add
        each item whose state separates painful trials from painless ones.
        An item that never varied across trials carries no evidence."""
        trials = self.trials[action]
        s = self.schema_for(action, trials[-1][0])
        ctx = set(s.context) if s else set()
        for k in sorted({k for before, _ in trials for k in before}):
            on = [hurt for before, hurt in trials if before.get(k) is ON]
            off = [hurt for before, hurt in trials if before.get(k) is OFF]
            if not on or not off:
                continue
            d = sum(on) / len(on) - sum(off) / len(off)
            if d >= CONTRAST:
                ctx.add(k)
            elif d <= -CONTRAST:
                ctx.add("!" + k)
        return sorted(ctx)

    def attribute(self, t, action, before):
        pain = [k for k, v in self.items.items()
                if v is ON and self.values.get(k, 0) < 0 and before.get(k) is not ON]
        pain += [f"{a}+{b}" for a, b in self.conflicts()]
        self.trials.setdefault(action, []).append((before, bool(pain)))
        if not pain:
            return
        hurt = sum(h for _, h in self.trials[action])
        if hurt < self.learn_threshold:
            return
        ctx = self.discriminating(action)
        learned = next((c for c in self.censors if c.action == action and c.learned_from), None)
        if learned:
            if ctx != learned.context:
                learned.context = ctx
                self.log(t, f"context spin-off refines {learned.id}: {ctx}", inner=False)
            return
        cid = f"learned-{action}"
        c = build(Censor, {"id": cid, "kind": "precursor", "context": ctx, "action": action,
                           "harm": pain, "learned_from": f"{hurt} painful '{action}'s",
                           **self.patches.get(cid, {})})
        self.censors.append(c)
        self.log(t, f"marginal attribution mints censor {cid}: context {ctx}", inner=False)
        self.bus.emit("INFO", "minted", f"learned censor {cid}", key={"agent": self.name, "minted": cid},
                      censor=cid, context=ctx, t=t)

    # -- humor: the training signal ---------------------------------------
    def joke(self, t, ev):
        # Humor trains censors both ways: a joke that exposes one lets the
        # agent see it; a joke with only a lesson installs one, unseen.
        if "exposes" in ev:
            target = next((c for c in self.censors if c.id == ev["exposes"]), None)
            if not target:
                self.bus.emit("WARNING", "joke-misses", f"joke at t={t} exposes unknown censor {ev['exposes']}",
                              key={"agent": self.name, "t": t}, t=t)
                return
            target.visible = True
            target.reliability *= ev.get("discount", 0.5)
            self.log(t, f"laughs: notices censor {target.id} ({ev.get('text', '')})")
        elif "lesson" in ev:
            L = ev["lesson"]
            self.censors.append(build(Censor, {"anecdotal": True, "kind": "precursor",
                                               "learned_from": f"joke at t={t}", **L}))
            self.log(t, f"laughs along ({ev.get('text', '')})")
            self.log(t, f"the joke installs censor {L['id']}: vetoes '{L['action']}' when {L['context']}",
                     inner=False)
            return
        if "lesson" in ev:
            L = ev["lesson"]
            self.censors.append(build(Censor, {"anecdotal": True, "visible": True,
                                               "kind": "precursor",
                                               "learned_from": f"joke at t={t}", **L}))
            self.log(t, f"installs anecdotal censor {L['id']}: vetoes '{L['action']}' when {L['context']}")

    # -- the run loop ------------------------------------------------------
    def step(self, ev, quotes=True):
        t = ev["t"]
        for k, v in ev.get("set", {}).items():
            self.items[k] = parse_value(v)
        if ev.get("say"):
            self.log(t, f"hears: {ev['say']}", quote=ev.get("quote"))
        if "joke" in ev:
            self.joke(t, ev["joke"])
        if "offers" in ev:
            before = dict(self.items)
            act, covers = self.decide(t, ev["offers"])
            observed = ev.get("observed")
            if observed:
                self.fit.append((t, observed, act))
                self.situations.append((t, list(ev["offers"]), observed, dict(before)))
            self.choices.append((t, act))
            if act:
                why = ""
                if covers:
                    c = covers[0]
                    why = f' — "{c.cover}"' + (" [PI]" if c.generated else "")
                # A real quote belongs only to the action the real person took.
                quote = ev.get("response") if quotes and (act == observed or not observed) else None
                self.log(t, f"does '{act}'{why}", quote=quote)
                self.apply(act)
                self.suppress(t)
                self.attribute(t, act, before)


# == running =================================================================
def runs_of(spec, name=None):
    rs = spec.get("runs") or [{"name": "default"}]
    return [r for r in rs if not name or r["name"] == name]


def run(spec, run_name=None, bus=NULL):
    out = []
    for r in runs_of(spec, run_name):
        merged = dict(spec)
        for key in ("censors", "schemas"):
            extra = r.get("add_" + key)
            if extra:
                merged[key] = merge(spec.get(key, []), extra)
        if r.get("agent"):
            merged["agent"] = merge(spec["agent"], r["agent"])
        m = Mind(merged, bus)
        for ev in sorted(spec.get("events", []) + r.get("events", []), key=lambda e: e["t"]):
            m.step(ev, quotes=r.get("quotes", True))
        out.append((r, m))
    return out


def score(m):
    return sum(1 for _, o, a in m.fit if o == a), len(m.fit)


def result_of(r, m):
    hits, total = score(m)
    return {
        "run": r["name"], "agent": m.name, "about": (r.get("about") or "").strip() or None,
        "counterfactual": bool(r.get("counterfactual")),
        "inner": m.inner, "observer": m.observer,
        "final": {k: ("ON" if v else "OFF" if v is OFF else "?") for k, v in m.items.items()},
        "choices": [{"t": t, "action": a} for t, a in m.choices],
        "fit": None if r.get("counterfactual") or not m.fit else {
            "hits": hits, "total": total,
            "mismatches": [{"t": t, "observed": o, "model": a} for t, o, a in m.fit if o != a]},
        "conflicts": [list(c) for c in m.conflicts()],
    }


def render_text(results, markdown):
    lines = []
    for res in results:
        lines.append(f"## {res['agent']} — run: {res['run']}" if markdown else f"=== {res['agent']} / {res['run']}")
        if res["about"]:
            lines.append(res["about"])
        lines.append("")
        bullet = "- " if markdown else "  "
        lines.append("**Inner trace** (what it experiences)" if markdown else "INNER (what it experiences):")
        lines.append("")
        lines += [f"{bullet}t={e['t']}: {e['text']}" for e in res["inner"]]
        lines.append("")
        lines.append("**Observer trace** (everything that fired)" if markdown else "OBSERVER (everything that fired):")
        lines.append("")
        for e in res["observer"]:
            mark = " *[unconscious]*" if markdown else "  [unconscious]"
            lines.append(f"{bullet}t={e['t']}: {e['text']}{'' if e['inner'] else mark}")
            if e.get("quote"):
                lines.append(f"  > {e['quote']}" if markdown else f"      \"{e['quote']}\"")
        lines.append("")
        lines.append("final items: " + ", ".join(f"{k}={v}" for k, v in res["final"].items()))
        if res["fit"]:
            f = res["fit"]
            lines.append("")
            lines.append(f"fit to observed actions: {f['hits']}/{f['total']}" + "".join(
                f"\n  MISMATCH t={m['t']}: observed '{m['observed']}', model did '{m['model']}'"
                for m in f["mismatches"]))
        if res["conflicts"]:
            lines.append("")
            lines.append("unresolved conflict, now conscious: " + "; ".join(f"{a} vs {b}" for a, b in res["conflicts"]))
        lines.append("")
    return "\n".join(lines)


def emit_out(data, fmt, text=None):
    if fmt == "json":
        return json.dumps(data, indent=2, default=str)
    if fmt == "yaml":
        return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    return text if text is not None else yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


# == commands ================================================================
def cmd_resolve(a, bus):
    spec = load(a.files, a.layer, a.who, a.set)
    return emit_out(spec, a.format if a.format in ("json",) else "yaml")


def lint_spec(spec, bus):
    agent = spec.get("agent", {})
    items = set(agent.get("items", {}))
    actions = {s["action"] for s in spec.get("schemas", [])}
    censors = {c["id"]: c for c in spec.get("censors", [])}
    events = spec.get("events", []) + [e for r in runs_of(spec) for e in r.get("events", [])]
    offered = {a for e in events for a in e.get("offers", [])}
    learned_ok = {f"learned-{a}" for a in offered}
    # Who in the cast is a real person: `real: [self, ally, ...]`.
    real = set(spec.get("real") or []) | ({"self"} if spec.get("real_person") else set())

    def item_refs(where, conds):
        for c in conds or []:
            name = c.lstrip("!")
            if name not in items:
                bus.emit("WARNING", "unknown-item", f"{where} uses item '{name}', not declared in agent.items",
                         key={"where": where, "item": name}, where=where, item=name)

    for s in spec.get("schemas", []):
        item_refs(f"schema {s['id']} context", s.get("context"))
        item_refs(f"schema {s['id']} result", list(s.get("result", {})))
    for c in spec.get("censors", []):
        if "kind" not in c:
            if c["id"] not in learned_ok:
                bus.emit("WARNING", "orphan-patch", f"patch for censor {c['id']}, which no layer defines or the run can learn",
                         key={"orphan": c["id"]}, censor=c["id"])
            continue
        item_refs(f"censor {c['id']} context", c.get("context"))
        if c.get("kind") == "precursor" and c.get("action") not in offered:
            bus.emit("INFO", "never-offered", f"censor {c['id']} vetoes '{c.get('action')}', which no event offers",
                     key={"never": c["id"]}, censor=c["id"])
        if "self" in real and c.get("source", "") in ("", "template"):
            bus.emit("ERROR", "template-words", f"censor {c['id']} would put template words in a real person's mouth",
                     key={"template": c["id"]}, censor=c["id"],
                     fix="replace the cover with their own words and a source, or drop the censor",
                     patch={"censors": [{"id": c["id"], "cover": "<their words>", "source": "<where they said it>"}]})
    for e in events:
        item_refs(f"event t={e['t']} set", list(e.get("set", {})))
        for act in e.get("offers", []):
            if act not in actions:
                bus.emit("REQUEST", "schema", f"no schema says what '{act}' does",
                         key={"agent": agent.get("name"), "action": act}, action=act,
                         patch={"schemas": [{"id": act, "action": act, "context": [],
                                             "result": {"<item>": "on|off"}, "source": "tier0: <who answered>"}]})
        if e.get("observed") and e["observed"] not in e.get("offers", []):
            bus.emit("ERROR", "observed-not-offered", f"t={e['t']}: observed '{e['observed']}' isn't among the offers",
                     key={"t": e["t"]}, t=e["t"])
        if real - {"self"} and (e.get("say") or e.get("response")) and not e.get("source"):
            bus.emit("ERROR", "unsourced-event", f"t={e['t']}: a real person ({', '.join(sorted(real - {'self'}))}) "
                     "is in the cast and this event has no source",
                     key={"unsourced": e["t"]}, t=e["t"],
                     fix="add source: where it was said or done, or mark the line as paraphrase in a fictional case",
                     patch={"events": [{"t": e["t"], "source": "<url or citation>"}]})
        if "joke" in e and "exposes" in e["joke"] and e["joke"]["exposes"] not in censors \
                and e["joke"]["exposes"] not in learned_ok:
            bus.emit("WARNING", "joke-misses", f"t={e['t']}: joke exposes unknown censor {e['joke'].get('exposes')}",
                     key={"joke": e["t"]}, t=e["t"])
    return {"errors": bus.counts["ERROR"], "warnings": bus.counts["WARNING"], "requests": bus.counts["REQUEST"]}


def cmd_lint(a, bus):
    return emit_out(lint_spec(load([a.file], a.layer, a.who, a.set), bus), a.format or "yaml")


def cmd_run(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    t0 = time.perf_counter()
    results = [result_of(r, m) for r, m in run(spec, a.run, bus)]
    bus.emit("TELEMETRY", "run", "done", runs=len(results), seconds=round(time.perf_counter() - t0, 4))
    for res in results:
        if res["fit"]:
            bus.emit("RESULT", "fit", f"{res['run']}: {res['fit']['hits']}/{res['fit']['total']}",
                     run=res["run"], **{k: res["fit"][k] for k in ("hits", "total")})
    fmt = a.format or "text"
    return emit_out(results, fmt, render_text(results, fmt == "md") if fmt in ("text", "md") else None)


def cmd_test(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    failed, report = 0, []
    for r, m in run(spec, None, bus):
        res = result_of(r, m)
        problems = []
        exp = r.get("expect", {})
        if res["fit"] and res["fit"]["hits"] < res["fit"]["total"] and not exp.get("fit"):
            problems.append(f"fit {res['fit']['hits']}/{res['fit']['total']}")
        if exp.get("fit") and res["fit"] and f"{res['fit']['hits']}/{res['fit']['total']}" != exp["fit"]:
            problems.append(f"fit {res['fit']['hits']}/{res['fit']['total']}, expected {exp['fit']}")
        for k, v in (exp.get("final") or {}).items():
            if res["final"].get(k) != ("ON" if parse_value(v) else "OFF"):
                problems.append(f"final {k}={res['final'].get(k)}, expected {v}")
        if "conflict" in exp and bool(res["conflicts"]) != bool(exp["conflict"]):
            problems.append(f"conflict {bool(res['conflicts'])}, expected {exp['conflict']}")
        if "choices" in exp and [c["action"] for c in res["choices"]] != exp["choices"]:
            problems.append(f"choices {[c['action'] for c in res['choices']]}")
        failed += bool(problems)
        bus.emit("RESULT", "test", f"{r['name']}: " + ("; ".join(problems) or "ok"), run=r["name"], ok=not problems)
        report.append({"run": r["name"], "ok": not problems, "problems": problems})
    a._exit = 2 if failed else 0
    return emit_out(report, a.format or "yaml")


def ablate(spec, bus=NULL):
    rows = []
    for r in [r for r in runs_of(spec) if not r.get("counterfactual")]:
        full, total = score(run({**spec, "runs": [r]})[0][1])
        for c in [c for c in spec.get("censors", []) if "kind" in c]:
            trimmed = {**spec, "runs": [r], "censors": [x for x in spec["censors"] if x["id"] != c["id"]]}
            hits, _ = score(run(trimmed)[0][1])
            rows.append({"run": r["name"], "censor": c["id"], "fit_without": f"{hits}/{total}",
                         "fit_with": f"{full}/{total}", "needed": hits < full})
            if hits >= full:
                bus.emit("WARNING", "unneeded-censor", f"{r['name']}: the record doesn't need censor {c['id']}",
                         key={"run": r["name"], "unneeded": c["id"]}, run=r["name"], censor=c["id"])
        # A joke that installs a censor is a censor too, put there by someone else.
        for e in [e for e in spec.get("events", []) if "lesson" in e.get("joke", {}) and "exposes" not in e["joke"]]:
            events = [{k: v for k, v in x.items() if k != "joke"} if x is e else x for x in spec["events"]]
            hits, _ = score(run({**spec, "runs": [r], "events": events})[0][1])
            rows.append({"run": r["name"], "censor": f"{e['joke']['lesson']['id']} (joke t={e['t']})",
                         "fit_without": f"{hits}/{total}", "fit_with": f"{full}/{total}", "needed": hits < full})
    return rows


def cmd_ablate(a, bus):
    rows = ablate(load([a.file], a.layer, a.who, a.set), bus)
    text = "\n".join(f"{x['run']}: without {x['censor']:<26} {x['fit_without']} (all: {x['fit_with']})  "
                     f"{'needed' if x['needed'] else 'NOT NEEDED'}" for x in rows)
    return emit_out(rows, a.format or "text", text)


def sweep(spec, n, seed=0, spread=0.5):
    rng = random.Random(seed)
    values = spec["agent"].get("values", {})
    names = [r["name"] for r in runs_of(spec)]
    tallies = {k: Counter() for k in names}
    fits = {k: Counter() for k in names}
    start = time.perf_counter()
    for _ in range(n):
        v = {k: w * rng.uniform(1 - spread, 1 + spread) for k, w in values.items()}
        for r, m in run({**spec, "agent": {**spec["agent"], "values": v}}):
            tallies[r["name"]][tuple(a for _, a in m.choices)] += 1
            if m.fit and not r.get("counterfactual"):
                fits[r["name"]]["%d/%d" % score(m)] += 1
    secs = time.perf_counter() - start
    return {"n": n, "seed": seed, "spread": spread, "simulations": n * len(names),
            "seconds": round(secs, 3), "per_second": round(n * len(names) / secs),
            "runs": {k: {"fit": {f: round(c / n, 4) for f, c in fits[k].most_common()},
                         "outcomes": [{"share": round(c / n, 4), "choices": list(ch)}
                                      for ch, c in tallies[k].most_common(5)]} for k in names}}


def cmd_sweep(a, bus):
    s = sweep(load([a.file], a.layer, a.who, a.set), a.n, a.seed, a.spread)
    bus.emit("TELEMETRY", "sweep", "done", **{k: s[k] for k in ("simulations", "seconds", "per_second")})
    lines = [f"{s['n']} perturbations (±{s['spread']:.0%}), seed {s['seed']}: "
             f"{s['simulations']} simulations in {s['seconds']}s ({s['per_second']:,}/s)"]
    for k, v in s["runs"].items():
        lines.append(f"run {k}:")
        lines += [f"  fit {f}: {share:.1%}" for f, share in v["fit"].items()]
        lines += [f"  {o['share']:6.1%}  " + " → ".join(map(str, o["choices"])) for o in v["outcomes"]]
    return emit_out(s, a.format or "text", "\n".join(lines))


def cmd_predict(a, bus):
    """A forecast for an event that hasn't happened: commit the output
    before it does, and the commit date makes it a preregistration."""
    spec = load([a.file], a.layer, a.who, a.set)
    t_next = max([e["t"] for e in spec.get("events", [])] + [0]) + 1
    ev = {"t": t_next, "offers": [x.strip() for x in a.offers.split(",")],
          "set": {k: v for k, _, v in (kv.partition("=") for kv in a.set_item)}}
    if a.say:
        ev["say"] = a.say
    trial = {**spec, "events": spec.get("events", []) + [ev]}
    rng = random.Random(a.seed)
    values = spec["agent"].get("values", {})
    tallies = {r["name"]: Counter() for r in runs_of(spec)}
    for _ in range(a.n):
        v = {k: w * rng.uniform(1 - a.spread, 1 + a.spread) for k, w in values.items()}
        for r, m in run({**trial, "agent": {**trial["agent"], "values": v}}):
            tallies[r["name"]][m.choices[-1][1] if m.choices and m.choices[-1][0] == t_next else None] += 1
    out = {"event": ev, "n": a.n, "spread": a.spread,
           "runs": {k: {str(act): round(c / a.n, 4) for act, c in t.most_common()} for k, t in tallies.items()}}
    bus.emit("RESULT", "predict", f"t={t_next}: " + "; ".join(
        f"{k}: {max(v, key=v.get) if v else '-'}" for k, v in out["runs"].items()), **out)
    lines = [f"prediction for t={t_next}: offers {ev['offers']}, set {ev['set'] or '{}'}  ({a.n} weightings, ±{a.spread:.0%})"]
    for name, dist in out["runs"].items():
        lines.append(f"  {name}: " + ", ".join(f"{act} {share:.0%}" for act, share in dist.items()))
    return emit_out(out, a.format or "text", "\n".join(lines))


def induce(m, min_trials=3, thresh=0.5):
    """Drescher's extended context, run over the record: for each action
    the person was offered, how much likelier he was to take it with an item
    on than off. A large gap proposes a context spinoff, a schema for that
    action with the item in its context. Learned from what he did, not from
    what we wrote, so it can find a condition nobody put in."""
    out = []
    for act in sorted({x for _, offers, _, _ in m.situations for x in offers}):
        rows = [(obs == act, items) for _, offers, obs, items in m.situations if act in offers]
        if len(rows) < min_trials:
            continue
        for item in sorted({k for _, items in rows for k in items}):
            on = [took for took, items in rows if items.get(item) is ON]
            off = [took for took, items in rows if items.get(item) is not ON]
            if len(on) < min_trials or len(off) < min_trials:
                continue
            p_on, p_off = sum(on) / len(on), sum(off) / len(off)
            if abs(p_on - p_off) >= thresh:
                out.append({"action": act, "item": item, "gap": round(p_on - p_off, 3),
                            "on": f"{sum(on)}/{len(on)}", "off": f"{sum(off)}/{len(off)}"})
    return sorted(out, key=lambda r: (-abs(r["gap"]), r["action"], r["item"]))


def cmd_induce(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    (r, m), = run(spec, a.run or runs_of(spec)[0]["name"])
    rows = induce(m, a.min_trials, a.thresh)
    have = {(x.action, c) for x in m.schemas for c in x.context}
    for row in rows:
        row["in_model"] = (row["action"], row["item"]) in have
    bus.emit("RESULT", "induce", f"{len(rows)} proposed contexts", rows=rows)
    lines = [f"induced from {len(m.situations)} observed choices (run {r['name']}; gap = P(take | on) - P(take | off)):"]
    for row in rows:
        mark = "" if row["in_model"] else "   <- not in the model"
        lines.append(f"  {row['action']:<12} {row['item']:<32} {row['gap']:+.2f}  on {row['on']:>5}  off {row['off']:>5}{mark}")
    return emit_out(rows, a.format or "text", "\n".join(lines))


def cmd_bench(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    t0 = time.perf_counter()
    for _ in range(a.n):
        run(spec)
    secs = time.perf_counter() - t0
    out = {"runs_per_pass": len(runs_of(spec)), "passes": a.n, "seconds": round(secs, 3),
           "simulations_per_second": round(a.n * len(runs_of(spec)) / secs)}
    bus.emit("TELEMETRY", "bench", "done", **out)
    return emit_out(out, a.format or "yaml")


def cmd_diff(a, bus):
    A, B = load([a.a], a.layer, a.who, a.set), load([a.b], a.layer, a.who, a.set)
    sa = {s["id"]: {k: s.get(k) for k in ("action", "context", "result")} for s in A.get("schemas", [])}
    sb = {s["id"]: {k: s.get(k) for k in ("action", "context", "result")} for s in B.get("schemas", [])}
    va, vb = A["agent"].get("values", {}), B["agent"].get("values", {})
    ca = {c["id"]: c for c in A.get("censors", []) if "kind" in c}
    cb = {c["id"]: c for c in B.get("censors", []) if "kind" in c}
    out = {
        "a": A["agent"]["name"], "b": B["agent"]["name"],
        "shared_logic": sorted(k for k in sa if sb.get(k) == sa[k]),
        "different_logic": sorted(k for k in set(sa) | set(sb) if sa.get(k) != sb.get(k)),
        "priorities": {k: {"a": va.get(k), "b": vb.get(k)} for k in sorted(set(va) | set(vb))
                       if va.get(k) != vb.get(k)},
        "censors_only_a": sorted(set(ca) - set(cb)),
        "censors_only_b": sorted(set(cb) - set(ca)),
        "censors_both": sorted(set(ca) & set(cb)),
    }
    lines = [f"{out['a']}  vs  {out['b']}",
             f"shared logic: {len(out['shared_logic'])} schemas identical; differ: {out['different_logic'] or 'none'}",
             "priorities (value weights):"]
    lines += [f"  {k:<32} {v['a']!s:>6} {v['b']!s:>6}" for k, v in out["priorities"].items()]
    lines += [f"censors only in {out['a']}: {out['censors_only_a'] or 'none'}",
              f"censors only in {out['b']}: {out['censors_only_b'] or 'none'}"]
    return emit_out(out, a.format or "text", "\n".join(lines))


def cmd_lineage(a, bus):
    rows = []
    for path, raw in linearize([a.file], a.layer):
        agent = raw.get("agent") or {}
        part = raw.get("part") or {}
        rows.append({
            "file": os.path.relpath(path) if path != "-" else "-",
            "part": part.get("id") if isinstance(part, dict) else part,
            "about": (part.get("about") or "").strip() or None if isinstance(part, dict) else None,
            "censors": [c["id"] for c in raw.get("censors", []) if "kind" in c],
            "patches": [c["id"] for c in raw.get("censors", []) if "kind" not in c],
            "schemas": [s["id"] for s in raw.get("schemas", [])],
            "values": agent.get("values") or {},
            "items": sorted(agent.get("items") or {}),
            "events": len(raw.get("events", [])),
            "imports": [f"{', '.join(i['take']) if i.get('take') else '*'} from {i['from']}"
                        for i in raw.get("imports") or []],
        })
    lines = []
    for n, r in enumerate(rows, 1):
        bits = [f"import {i}" for i in r["imports"]] + [
                f"{len(r['schemas'])} schemas" if r["schemas"] else "",
                "censors " + ", ".join(r["censors"]) if r["censors"] else "",
                "covers " + ", ".join(r["patches"]) if r["patches"] else "",
                "values " + ", ".join(f"{k}={v}" for k, v in r["values"].items()) if r["values"] else "",
                f"{r['events']} events" if r["events"] else ""]
        lines.append(f"{n:2}. {r['file']}" + (f"  [{r['part']}]" if r["part"] else ""))
        lines += [f"      {b}" for b in bits if b]
    return emit_out(rows, a.format or "text", "\n".join(lines))


def cmd_where(a, bus):
    rx = re.compile(a.pattern, re.I)
    hits = []
    for path, raw in linearize([a.file], a.layer):
        for section in ("agent", "schemas", "censors", "events", "runs", "who"):
            node = raw.get(section)
            entries = node if isinstance(node, list) else [node] if node else []
            for e in entries:
                text = json.dumps(e, default=str)
                if rx.search(text):
                    hits.append({"file": os.path.relpath(path) if path != "-" else "-", "section": section,
                                 "id": e.get("id") or e.get("t") or e.get("name") if isinstance(e, dict) else None,
                                 "match": rx.search(text).group(0)})
    text = "\n".join(f"{h['file']}: {h['section']} {h['id'] if h['id'] is not None else ''}: …{h['match']}…" for h in hits)
    return emit_out(hits, a.format or "text", text)


def cmd_export(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    if a.format != "dot":
        return emit_out(spec, a.format or "json")
    q = lambda s: '"' + str(s).replace('"', '\\"') + '"'
    lines = ["digraph censors {", "  rankdir=LR; node [fontname=Helvetica];"]
    for c in [c for c in spec.get("censors", []) if "kind" in c]:
        lines.append(f"  {q(c['id'])} [shape=octagon, color=red];")
        for x in c.get("context", []):
            lines.append(f"  {q(x)} -> {q(c['id'])} [style=dashed];")
        if c["kind"] == "precursor":
            lines.append(f"  {q(c['id'])} -> {q('do: ' + c['action'])} [label=veto, color=red];")
        for k in c.get("refile", {}):
            lines.append(f"  {q(c['id'])} -> {q(k)} [label=refile, color=orange];")
    for s in spec.get("schemas", []):
        for k in s.get("result", {}):
            lines.append(f"  {q('do: ' + s['action'])} -> {q(k)};")
    lines.append("}")
    return "\n".join(lines)


def cmd_import(a, bus):
    """Deterministic part only: split the thread. Meaning is a request."""
    text = sys.stdin.read() if a.text == "-" else open(a.text).read()
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines) if re.match(r"^(From:|On .+ wrote:|-{3,}\s*$|Date:)", l)] or [0]
    starts = sorted(set([0] + starts))
    events = []
    for n, (s, e) in enumerate(zip(starts, starts[1:] + [len(lines)]), 1):
        chunk = "\n".join(lines[s:e]).strip()
        if not chunk:
            continue
        ev = {"t": n, "say": chunk[:160].replace("\n", " "), "source": f"{a.text}:{s + 1}-{e}",
              "offers": [], "observed": None}
        events.append(ev)
        bus.emit("REQUEST", "event", f"t={n}: turn lines {s + 1}-{e} into an event",
                 key={"import": a.text, "lines": [s + 1, e]}, t=n, source=ev["source"], excerpt=chunk[:600],
                 ask="set: items this message turns on/off; offers: the choices the agent had; "
                     "observed: what they did; response: their words, verbatim",
                 patch={"events": [{"t": n, "set": {}, "offers": [], "observed": None, "response": None}]})
    return emit_out({"events": events}, "yaml")


def cmd_apply(a, bus):
    patch = read_yaml(a.patch)
    target = read_yaml(a.into) if os.path.exists(a.into) else {}
    merged = merge(target, patch)
    with open(a.into, "w") as f:
        yaml.safe_dump(merged, f, sort_keys=False, allow_unicode=True, width=100)
    bus.emit("INFO", "applied", f"merged {a.patch} into {a.into}", patch=a.patch, into=a.into)
    return None


# == main ====================================================================
def main(argv=None):
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--layer", action="append", default=[], help="extra layer on top (repeatable)")
    common.add_argument("--who", action="append", default=[], metavar="K=V")
    common.add_argument("--set", action="append", default=[], metavar="PATH=VALUE")
    common.add_argument("--format", choices=["text", "md", "yaml", "json", "dot"])
    common.add_argument("-o", "--output", help="write stdout data to a file")
    common.add_argument("--events", default="-", help="event stream file (default: stderr)")
    common.add_argument("--quiet", action="store_true", help="no INFO events")
    common.add_argument("--strict", action="store_true", help="exit 3 if requests are left open")

    p = argparse.ArgumentParser(prog="censor_sim", description=__doc__.splitlines()[0],
                                epilog="\n".join(__doc__.splitlines()[1:]),
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("resolve", parents=[common]); s.add_argument("files", nargs="+")
    for name in ("lint", "test", "ablate", "export", "lineage"):
        sub.add_parser(name, parents=[common]).add_argument("file")
    s = sub.add_parser("run", parents=[common]); s.add_argument("file"); s.add_argument("--run")
    s = sub.add_parser("sweep", parents=[common]); s.add_argument("file")
    s.add_argument("--n", type=int, default=1000); s.add_argument("--seed", type=int, default=0)
    s.add_argument("--spread", type=float, default=0.5)
    s = sub.add_parser("predict", parents=[common]); s.add_argument("file")
    s.add_argument("--offers", required=True); s.add_argument("--set-item", action="append", default=[], metavar="ITEM=on|off")
    s.add_argument("--say"); s.add_argument("--n", type=int, default=1000); s.add_argument("--seed", type=int, default=0)
    s.add_argument("--spread", type=float, default=0.5)
    s = sub.add_parser("induce", parents=[common]); s.add_argument("file"); s.add_argument("--run")
    s.add_argument("--min-trials", type=int, default=3); s.add_argument("--thresh", type=float, default=0.5)
    s = sub.add_parser("bench", parents=[common]); s.add_argument("file"); s.add_argument("--n", type=int, default=1000)
    s = sub.add_parser("diff", parents=[common]); s.add_argument("a"); s.add_argument("b")
    s = sub.add_parser("where", parents=[common]); s.add_argument("file"); s.add_argument("pattern")
    s = sub.add_parser("import", parents=[common]); s.add_argument("text")
    s = sub.add_parser("apply", parents=[common]); s.add_argument("patch"); s.add_argument("--into", required=True)
    a = p.parse_args(argv)

    stream = sys.stderr if a.events == "-" else open(a.events, "a")
    thread = f"{os.path.basename(getattr(a, 'file', '') or getattr(a, 'a', '') or '')}:{a.command}"
    bus = Bus(stream, a.quiet, thread)
    a._exit = 0
    try:
        out = globals()["cmd_" + a.command](a, bus)
    except (OSError, ValueError, KeyError, yaml.YAMLError) as e:
        bus.emit("ERROR", "fatal", f"{type(e).__name__}: {e}")
        return 1
    if out is not None:
        if a.output:
            with open(a.output, "w") as f:
                f.write(out + "\n")
        else:
            print(out)
    if bus.open_requests:
        bus.emit("TELEMETRY", "open-requests", f"{len(bus.open_requests)} requests open",
                 ids=sorted(bus.open_requests))
    if a._exit:
        return a._exit
    if bus.counts["ERROR"]:
        return 1
    if a.strict and bus.open_requests:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
