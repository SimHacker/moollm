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
(schemas, censors) merge by id, `drop: true` deletes one, lists of pairs
(contradictions) accumulate, anything else is replaced. `who:` fills `{name}` placeholders in every string. A scenario
path of `-` reads YAML from stdin.

Commands:
  resolve  FILE...        merge files and layers, print the result     (read/transform)
  lint     FILE           check a scenario; emit requests and warnings
  run      FILE           run it; print the traces                     (run)
  test     FILE           exit 2 unless every factual run fits its record and expectations
  suite    PATH...        lint and test every scenario under PATHs (and its .answers.yml)
  ablate   FILE           drop each censor in turn: which does the record need?
  sweep    FILE           perturb value weights N times: do conclusions depend on them?
  predict  FILE --offers A,B [--set-item K=on]  what each run does next, over N weightings
  induce   FILE [--run R]  learn contexts from the record: which items made each choice likelier
  argue    FILE --offers A,B --goal A --args ARGS  which arguments move each hypothesis toward A
  drift    FILE           fit over time: recency-weighted, and where each run's unbroken hits begin
  propose  FILE [--run R]  latent items: a choice that switched once, with nothing observed to explain it
  plan     FILE --goal G   Drescher's planner: the plan the agent can think of vs the one an observer sees
  duet     FILE [--n N]   two minds on one stage: each one's move is an event for the other
  learn    FILE [--run R]  Drescher's learner over the record: propose result and context spinoffs, keep what fits
  try      FILE --layer L  the gate: does the layer (from learn, a person or an LLM) make any run fit worse?

Learning is a loop across both tiers. In a run, `agent.learn_schemas: true`
makes the mind spin off schemas from what follows its own actions, starting
from bare ones. Over a record, `learn` proposes, gates on fit, and asks the
other tier what each kept schema means; the answers come back as layers,
`try` gates them, and the next `learn` starts from there.
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
import heapq
import json
import math
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
    # Lists of pairs (contradictions) accumulate: each part adds its own.
    if (isinstance(base, list) and isinstance(over, list) and base and over
            and all(isinstance(x, list) for x in base + over)):
        return base + [x for x in over if x not in base]
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
        self.score_change = a.get("score", "earned") == "change"
        self.losses_hurt = bool(a.get("losses_hurt"))
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
        # Drescher's positive learning: what follows each action, until the next choice.
        self.learn_schemas = bool(a.get("learn_schemas"))
        self.replay = False           # learn from the observed action, not the model's
        self.pending = None           # (action, items before it, items just after it, changes since)
        self.outcomes = {}            # action -> [(items before, {item: value that followed})]

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
        # A learning mind starts with bare schemas: no schema yet is how it begins.
        if not best and not self.learn_schemas and not any(s.action == action for s in self.schemas):
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
        # Default: every result is earned again each time, as if the motive
        # had decayed back between choices. `score: change` scores only what
        # the action changes, as The Sims' Find Best Action scores the delta.
        v = 0.0
        for k, val in s.result.items():
            new = parse_value(val)
            if new is None or (self.score_change and self.items.get(k) is new):
                continue
            v += self.values.get(k, 0) * (1 if new else -1)
        return v * s.reliability

    def vetoed(self, action, items=None):
        # A censor the agent can see, and no longer trusts, can be overridden.
        # A censor whose harms have all already happened has nothing to guard.
        items = items if items is not None else self.items
        hits = [c for c in self.censors
                if c.kind == "precursor" and c.action == action and c.matches(items)
                and not (c.visible and c.reliability < OVERRIDE)
                and not (c.harm and all(items.get(h) is ON for h in c.harm))]
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
            self.items[k] = parse_value(v)

    # -- planning: Drescher's composite actions ----------------------------
    def plan(self, goal, censored=True, max_steps=8):
        """Cheapest chain of schemas from the current items to every goal
        condition, by Dijkstra over states. A step costs 1 plus -log of the
        schema's reliability, so a long sure plan can beat a short gamble.
        censored=True is the plan the agent can think of: a step a precursor
        censor vetoes, in the state where it would be taken, is never
        considered. censored=False is the plan the observer can see."""
        actions = sorted({s.action for s in self.schemas})
        start = dict(self.items)
        key = lambda items: tuple(sorted((k, v) for k, v in items.items() if v is not None))
        frontier, best, n = [(0.0, 0, start, [])], {key(start): 0.0}, 0
        pruned = {}
        while frontier:
            cost, _, items, path = heapq.heappop(frontier)
            if all(holds(items, g) for g in goal):
                return {"steps": path, "cost": round(cost, 3), "pruned": sorted(pruned.items())}
            if len(path) >= max_steps or cost > best.get(key(items), math.inf):
                continue
            for act in actions:
                s = self.schema_for(act, items)
                if not s:
                    continue
                if censored:
                    hits = self.vetoed(act, items)
                    if hits:
                        pruned.setdefault(act, hits[0].id)
                        continue
                nxt = dict(items)
                for k, v in s.result.items():
                    nxt[k] = parse_value(v)
                if key(nxt) == key(items):
                    continue
                c = cost + 1 - math.log(max(s.reliability, 1e-6))
                if c < best.get(key(nxt), math.inf):
                    best[key(nxt)] = c
                    n += 1
                    heapq.heappush(frontier, (c, n, nxt, path + [act]))
        return {"steps": None, "cost": None, "pruned": sorted(pruned.items())}

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
        # With `losses_hurt`, losing something valued is pain too. Off by
        # default: most modules name a loss as its own bad item instead.
        if self.losses_hurt:
            pain += [f"lost {k}" for k, v in self.items.items()
                     if v is OFF and self.values.get(k, 0) > 0 and before.get(k) is ON]
        # Only a conflict this action created; one already standing isn't its fault.
        pain += [f"{a}+{b}" for a, b in self.conflicts()
                 if not (before.get(a) is ON and before.get(b) is ON)]
        self.trials.setdefault(action, []).append((before, bool(pain)))
        if not pain:
            return
        hurt = sum(h for _, h in self.trials[action])
        if hurt < self.learn_threshold:
            return
        ctx = self.discriminating(action)
        cid = f"learned-{action}"
        learned = next((c for c in self.censors if c.id == cid), None)
        if learned:
            if ctx != learned.context:
                learned.context = ctx
                self.log(t, f"context spin-off refines {learned.id}: {ctx}", inner=False)
            return
        c = build(Censor, {"id": cid, "kind": "precursor", "context": ctx, "action": action,
                           "harm": pain, "learned_from": f"{hurt} painful '{action}'s",
                           **self.patches.get(cid, {})})
        self.censors.append(c)
        self.log(t, f"marginal attribution mints censor {cid}: context {ctx}", inner=False)
        self.bus.emit("INFO", "minted", f"learned censor {cid}", key={"agent": self.name, "minted": cid},
                      censor=cid, context=ctx, t=t)

    # -- learning schemas: Drescher's result and context spinoffs ----------
    def watch(self, sets):
        """Items the world sets after an action, before the next choice."""
        if not self.pending:
            return
        _, before, _, changed = self.pending
        # A result is a change from before the action, not from what the mind
        # predicted; the first change is the evidence, and a later reset
        # doesn't undo that it followed.
        for k, v in sets.items():
            v = parse_value(v)
            if k not in changed and v is not before.get(k):
                changed[k] = v

    def close_window(self, t):
        if not self.pending:
            return
        act, before, _, changed = self.pending
        self.pending = None
        self.outcomes.setdefault(act, []).append((before, dict(changed)))
        self.spin_off(t, act)

    def spin_off(self, t, act):
        """Marginal attribution for results: an item that follows this action
        at least half the time, and more often by CONTRAST than it follows the
        others, is a result (Drescher's result spinoff). Then an item whose
        state before the action separates the trials where the results came
        from the ones where they didn't joins the context (context spinoff)."""
        trials = self.outcomes[act]
        if len(trials) < self.learn_threshold:
            return
        others = [tr for a, ts in self.outcomes.items() if a != act for tr in ts]

        def rate(ts, k, v):
            return sum(ch.get(k) is v for _, ch in ts) / len(ts) if ts else 0.0
        found = {}
        for k, v in sorted({(k, v) for _, ch in trials for k, v in ch.items()}, key=str):
            r = rate(trials, k, v)
            if r * len(trials) >= self.learn_threshold and r >= 0.5 and r - rate(others, k, v) >= CONTRAST:
                found[k] = v
        if not found:
            return
        ctx = []
        for i in sorted({i for b, _ in trials for i in b} - set(found)):
            on = [tr for tr in trials if tr[0].get(i) is ON]
            off = [tr for tr in trials if tr[0].get(i) is OFF]
            if not on or not off:
                continue
            d = sum(rate(on, k, v) - rate(off, k, v) for k, v in found.items()) / len(found)
            if d >= CONTRAST:
                ctx.append(i)
            elif d <= -CONTRAST:
                ctx.append("!" + i)
        sub = [tr for tr in trials if all(holds(tr[0], c) for c in ctx)]
        rel = round(sum(rate(sub, k, v) for k, v in found.items()) / len(found), 3)
        result = {k: "on" if v else "off" for k, v in found.items()}
        if ctx:
            general = next((x for x in self.schemas if x.id == f"learned-{act}"), None)
            if general:
                general.reliability = round(sum(rate(trials, k, v) for k, v in found.items()) / len(found), 3)
        s = next((x for x in self.schemas if x.action == act and sorted(x.context) == ctx), None)
        if s and not s.id.startswith("learned-"):
            new = {k: v for k, v in result.items() if k not in s.result}
            if new:
                s.result = {**s.result, **new}
                self.log(t, f"result spinoff extends {s.id}: {new}", inner=False)
            return
        if s:
            if (s.result, s.reliability) != (result, rel):
                s.result, s.reliability = result, rel
                self.log(t, f"spinoff revises {s.id}: {result} at {rel}", inner=False)
            return
        sid = f"learned-{act}" + ("-when-" + "-".join(c.replace("!", "not-") for c in ctx) if ctx else "")
        self.schemas.append(Schema(id=sid, action=act, context=ctx, result=result, reliability=rel,
                                   source=f"learned: {len(sub)} trials of '{act}'"))
        self.log(t, f"marginal attribution spins off schema {sid}: {act} → {result}"
                    + (f" when {ctx}" if ctx else "") + f", reliability {rel}", inner=False)
        self.bus.emit("INFO", "spinoff", f"learned schema {sid}", key={"agent": self.name, "spinoff": sid, "r": result},
                      schema=sid, action=act, context=ctx, result=result, reliability=rel, t=t)

    # -- humor: the training signal ---------------------------------------
    def joke(self, t, ev):
        # Humor trains censors both ways: a joke that exposes one lets the
        # agent see it; a joke with only a lesson installs one, unseen.
        if "exposes" in ev:
            target = next((c for c in self.censors if c.id == ev["exposes"]), None)
            if not target:
                # A miss exposes nothing, but its lesson (if any) still lands.
                self.bus.emit("WARNING", "joke-misses", f"joke at t={t} exposes unknown censor {ev['exposes']}",
                              key={"agent": self.name, "t": t}, t=t)
                if "lesson" not in ev:
                    return
            else:
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
        if self.learn_schemas:
            self.watch(ev.get("set", {}))
            if "offers" in ev:
                self.close_window(t)
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
            # In replay the world's answers in the record followed what the
            # person did, so that's the action they're evidence about.
            took = observed if (self.replay and observed) else act
            if self.learn_schemas and took:
                self.pending = (took, before, dict(self.items), {})


# == running =================================================================
def runs_of(spec, name=None):
    rs = spec.get("runs") or [{"name": "default"}]
    return [r for r in rs if not name or r["name"] == name]


def run_spec(spec, r):
    """The spec one run sees: its censors, schemas and agent overrides applied."""
    merged = dict(spec)
    for key in ("censors", "schemas"):
        extra = r.get("add_" + key)
        if extra:
            merged[key] = merge(spec.get(key, []), extra)
    if r.get("agent"):
        merged["agent"] = merge(spec["agent"], r["agent"])
    return merged


def run(spec, run_name=None, bus=NULL, factors=None):
    """factors: weight -> multiplier, applied after each run's own overrides,
    so a perturbation reaches the weights a run sets as well as the shared ones."""
    out = []
    for r in runs_of(spec, run_name):
        merged = run_spec(spec, r)
        if factors:
            vals = merged["agent"].get("values", {})
            merged["agent"] = {**merged["agent"],
                               "values": {k: w * factors.get(k, 1.0) for k, w in vals.items()}}
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
    rs = runs_of(spec)
    items = set(agent.get("items", {})) | {k for r in rs for k in (r.get("agent") or {}).get("items", {})}
    actions = {s["action"] for s in spec.get("schemas", [])} | {
        s["action"] for r in rs for s in r.get("add_schemas", []) if "action" in s}
    # Each run's own censors are checked like the shared ones.
    all_censors = list(spec.get("censors", [])) + [
        c for r in rs for c in r.get("add_censors", []) if not c.get("drop")]
    censors = {c["id"]: c for c in all_censors}
    if agent.get("score", "earned") not in ("earned", "change"):
        bus.emit("ERROR", "bad-score", f"agent.score is '{agent.get('score')}'; use earned or change",
                 key={"score": agent.get("score")})
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
    for c in all_censors:
        if "kind" not in c:
            if c["id"] not in learned_ok and not any("kind" in x for x in all_censors if x["id"] == c["id"]):
                bus.emit("WARNING", "orphan-patch", f"patch for censor {c['id']}, which no layer defines or the run can learn",
                         key={"orphan": c["id"]}, censor=c["id"])
            continue
        item_refs(f"censor {c['id']} context", c.get("context"))
        if c.get("kind") == "precursor" and c.get("action") not in offered:
            bus.emit("INFO", "never-offered", f"censor {c['id']} vetoes '{c.get('action')}', which no event offers",
                     key={"never": c["id"]}, censor=c["id"])
        if "self" in real and c.get("cover") and c.get("source", "") in ("", "template"):
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


def test_spec(spec, bus=NULL):
    report = []
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
        bus.emit("RESULT", "test", f"{r['name']}: " + ("; ".join(problems) or "ok"), run=r["name"], ok=not problems)
        report.append({"run": r["name"], "ok": not problems, "problems": problems,
                       "fit": f"{res['fit']['hits']}/{res['fit']['total']}" if res["fit"] else None})
    return report


def cmd_test(a, bus):
    report = test_spec(load([a.file], a.layer, a.who, a.set), bus)
    a._exit = 2 if any(not x["ok"] for x in report) else 0
    return emit_out([{k: v for k, v in x.items() if k != "fit"} for x in report], a.format or "yaml")


def scenarios(dirs):
    """Every YAML file with `runs:` under the given paths, each with the
    answer layer beside it (X.answers.yml), if there is one."""
    out = []
    for d in dirs:
        paths = [d] if os.path.isfile(d) else sorted(
            os.path.join(root, f) for root, subs, files in os.walk(d)
            if not any(part.startswith(".") or part == "node_modules" for part in root.split(os.sep))
            for f in files if f.endswith((".yml", ".yaml")))
        for p in paths:
            if p.endswith(".answers.yml"):
                continue
            try:
                raw = read_yaml(p)
            except (OSError, yaml.YAMLError):
                continue
            if isinstance(raw, dict) and raw.get("seats") and raw.get("turns"):
                out.append((p, None))
                continue
            if not isinstance(raw, dict) or not (raw.get("runs") or raw.get("inherits")):
                continue
            inh = raw.get("inherits") or []
            if not all(isinstance(x, str) for x in ([inh] if isinstance(inh, str) else inh)):
                continue
            try:
                spec = raw if raw.get("runs") and raw.get("events") else merged([p])
            except (OSError, ValueError, TypeError, AttributeError, yaml.YAMLError):
                spec = raw
            if not isinstance(spec, dict):
                continue
            if spec.get("runs") and spec.get("events"):
                out.append((p, []))
                ans = p[:-4] + ".answers.yml"
                if os.path.exists(ans):
                    out.append((p, [ans]))
    return out


def cmd_suite(a, bus):
    """Lint and test every scenario under the given paths. One line each;
    exit 2 if any run fails its record or expectations, 1 on lint errors."""
    rows, t0 = [], time.perf_counter()
    for path, layers in scenarios(a.paths):
        if layers is None:
            row = {"file": os.path.relpath(path) + " (duet)", "errors": 0, "warnings": 0, "requests": 0, "runs": 1, "fits": []}
            try:
                spec = load([path])
                row["failed"] = test_duet(spec, duet_seats(spec, os.path.dirname(os.path.abspath(path))))
            except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as e:
                row.update({"errors": 1, "failed": [f"{type(e).__name__}: {e}"]})
            rows.append(row)
            continue
        row = {"file": os.path.relpath(path) + "".join(f" + {os.path.basename(x)}" for x in layers)}
        try:
            spec = load([path], layers)
            row.update(lint_spec(spec, Bus()))
            report = test_spec(spec)
            if a.ablate:
                row["unneeded"] = [f"{x['run']}:{x['censor']}" for x in ablate(spec) if not x["needed"]]
            row["runs"] = len(report)
            row["failed"] = [f"{x['run']}: {'; '.join(x['problems'])}" for x in report if not x["ok"]]
            row["fits"] = [x["fit"] for x in report if x["fit"]]
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as e:
            row.update({"errors": 1, "warnings": 0, "requests": 0, "runs": 0, "fits": [],
                        "failed": [f"{type(e).__name__}: {e}"]})
        rows.append(row)
    bad = [r for r in rows if r["failed"]]
    errs = [r for r in rows if r["errors"]]
    bus.emit("RESULT", "suite", f"{len(rows)} scenarios, {len(bad)} failing, {len(errs)} with lint errors",
             scenarios=len(rows), failing=len(bad), lint_errors=len(errs), seconds=round(time.perf_counter() - t0, 3))
    a._exit = 2 if bad else 1 if errs else 0
    w = max([len(r["file"]) for r in rows] + [8])
    fw = max([len(" ".join(r["fits"])) for r in rows] + [4])
    lines = [f"{'scenario':<{w}}  runs  {'fits':<{fw}}  lint (E/W/R)  result"]
    for r in rows:
        lines.append(f"{r['file']:<{w}}  {r['runs']:>4}  {' '.join(r['fits']):<{fw}}  "
                     f"{r['errors']}/{r['warnings']}/{r['requests']:<9}  " + ("FAIL " + " | ".join(r["failed"]) if r["failed"] else "ok")
                     + (f"   unneeded: {len(r['unneeded'])}" + (f" ({', '.join(r['unneeded'])})" if len(r["unneeded"]) <= 3 else "")
                        if r.get("unneeded") else ""))
    lines.append(f"{len(rows)} scenarios, {len(bad)} failing, {len(errs)} with lint errors, "
                 f"{time.perf_counter() - t0:.1f}s")
    return emit_out(rows, a.format or "text", "\n".join(lines))


def ablate(spec, bus=NULL):
    rows = []
    for r in [r for r in runs_of(spec) if not r.get("counterfactual")]:
        full, total = score(run({**spec, "runs": [r]})[0][1])
        # The censors this run actually has: shared ones it keeps, plus its own.
        for c in [c for c in run_spec(spec, r).get("censors", []) if "kind" in c]:
            without = {**r, "add_censors": list(r.get("add_censors", [])) + [{"id": c["id"], "drop": True}]}
            hits, _ = score(run({**spec, "runs": [without]})[0][1])
            rows.append({"run": r["name"], "censor": c["id"], "fit_without": f"{hits}/{total}",
                         "fit_with": f"{full}/{total}", "needed": hits < full})
            if hits >= full:
                bus.emit("WARNING", "unneeded-censor", f"{r['name']}: the record doesn't need censor {c['id']}",
                         key={"run": r["name"], "unneeded": c["id"]}, run=r["name"], censor=c["id"])
        # A joke that installs a censor is a censor too, put there by someone else.
        lessons = lambda evs: [e for e in evs if "lesson" in e.get("joke", {}) and "exposes" not in e["joke"]]
        unjoke = lambda evs, e: [{k: v for k, v in x.items() if k != "joke"} if x is e else x for x in evs]
        for e in lessons(spec.get("events", [])) + lessons(r.get("events", [])):
            if e in spec.get("events", []):
                trial = {**spec, "runs": [r], "events": unjoke(spec["events"], e)}
            else:
                trial = {**spec, "runs": [{**r, "events": unjoke(r["events"], e)}]}
            hits, _ = score(run(trial)[0][1])
            rows.append({"run": r["name"], "censor": f"{e['joke']['lesson']['id']} (joke t={e['t']})",
                         "fit_without": f"{hits}/{total}", "fit_with": f"{full}/{total}", "needed": hits < full})
    return rows


def cmd_ablate(a, bus):
    rows = ablate(load([a.file], a.layer, a.who, a.set), bus)
    text = "\n".join(f"{x['run']}: without {x['censor']:<26} {x['fit_without']} (all: {x['fit_with']})  "
                     f"{'needed' if x['needed'] else 'NOT NEEDED'}" for x in rows)
    return emit_out(rows, a.format or "text", text)


def weight_names(spec):
    """Every value weight any run can see: the shared ones first, in file
    order, then the ones only a run sets, sorted. The order fixes which
    random draw each weight gets, so a seed means the same thing everywhere."""
    shared = list(spec["agent"].get("values", {}))
    extra = sorted({k for r in runs_of(spec) for k in (r.get("agent") or {}).get("values", {})} - set(shared))
    return shared + extra


def draws(spec, n, seed, spread):
    rng, names = random.Random(seed), weight_names(spec)
    for _ in range(n):
        yield {k: rng.uniform(1 - spread, 1 + spread) for k in names}


def sweep(spec, n, seed=0, spread=0.5):
    names = [r["name"] for r in runs_of(spec)]
    tallies = {k: Counter() for k in names}
    fits = {k: Counter() for k in names}
    start = time.perf_counter()
    for f in draws(spec, n, seed, spread):
        for r, m in run(spec, factors=f):
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


def forecast(spec, new_events, n, seed=0, spread=0.5):
    """Each run's choice at the last new event, as shares over n weightings.
    The same seed gives every caller the same weightings, so two forecasts
    differ only in their events."""
    t_next = max(e["t"] for e in new_events)
    trial = {**spec, "events": spec.get("events", []) + list(new_events)}
    tallies = {r["name"]: Counter() for r in runs_of(spec)}
    for f in draws(spec, n, seed, spread):
        for r, m in run(trial, factors=f):
            tallies[r["name"]][m.choices[-1][1] if m.choices and m.choices[-1][0] == t_next else None] += 1
    return {k: {str(act): round(c / n, 4) for act, c in t.most_common()} for k, t in tallies.items()}


def cmd_argue(a, bus):
    """Plan validation by simulation: before suggesting an argument, run it.
    Each argument is an event (say, set, joke) just before the next choice.
    Where the hypotheses disagree about an argument, trying it tests them."""
    spec = load([a.file], a.layer, a.who, a.set)
    t_next = max([e["t"] for e in spec.get("events", [])] + [0]) + 1
    ev = {"t": t_next, "offers": [x.strip() for x in a.offers.split(",")]}
    if a.goal not in ev["offers"]:
        raise ValueError(f"goal '{a.goal}' is not one of the offers {ev['offers']}")
    args = read_yaml(a.args)
    args = args.get("arguments", args) if isinstance(args, dict) else args
    # The situation the argument lands in, before the argument.
    start = [{"t": t_next - 0.75, "set": {k: v for k, _, v in (kv.partition("=") for kv in a.set_item)}}]
    base = forecast(spec, start + [ev], a.n, a.seed, a.spread)
    rows = [{"id": "(none)", "about": "no argument", "p": {k: v.get(a.goal, 0.0) for k, v in base.items()}}]
    for x in args:
        pre = {**{k: v for k, v in x.items() if k in ("say", "set", "joke", "quote")}, "t": t_next - 0.5}
        p = forecast(spec, start + [pre, ev], a.n, a.seed, a.spread)
        rows.append({"id": x["id"], "about": x.get("about", ""), "source": x.get("source"),
                     "p": {k: v.get(a.goal, 0.0) for k, v in p.items()}})
    for row in rows:
        row["lift"] = {k: round(v - rows[0]["p"][k], 4) for k, v in row["p"].items()}
        row["split"] = round(max(row["p"].values()) - min(row["p"].values()), 4)
    bus.emit("RESULT", "argue", f"t={t_next}, goal {a.goal}: " + "; ".join(
        f"{r['id']} " + "/".join(f"{v:.0%}" for v in r["p"].values()) for r in rows),
        goal=a.goal, offers=ev["offers"], n=a.n, spread=a.spread, rows=rows)
    names = list(base)
    w = max(len(r["id"]) for r in rows)
    cw = max([len(k) for k in names] + [6])
    lines = [f"P({a.goal}) at t={t_next}, offers {ev['offers']}, under each hypothesis ({a.n} weightings, ±{a.spread:.0%}):",
             f"  {'argument':<{w}}  " + "  ".join(f"{k:>{cw}}" for k in names) + "   split"]
    for r in rows:
        lines.append(f"  {r['id']:<{w}}  " + "  ".join(f"{r['p'][k]:>{cw}.0%}" for k in names)
                     + f"   {r['split']:.0%}" + ("   <- tests the hypotheses" if r["split"] >= 0.5 else ""))
    return emit_out(rows, a.format or "text", "\n".join(lines))


def cmd_predict(a, bus):
    """A forecast for an event that hasn't happened: commit the output
    before it does, and the commit date makes it a preregistration."""
    spec = load([a.file], a.layer, a.who, a.set)
    t_next = max([e["t"] for e in spec.get("events", [])] + [0]) + 1
    ev = {"t": t_next, "offers": [x.strip() for x in a.offers.split(",")],
          "set": {k: v for k, _, v in (kv.partition("=") for kv in a.set_item)}}
    if a.say:
        ev["say"] = a.say
    out = {"event": ev, "n": a.n, "spread": a.spread,
           "runs": forecast(spec, [ev], a.n, a.seed, a.spread)}
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
                # Positive: a context spinoff. Negative: Drescher's overriding
                # condition, an item that stops an action he otherwise takes,
                # which is what a Minsky censor looks like from outside.
                out.append({"action": act, "item": item, "gap": round(p_on - p_off, 3),
                            "kind": "context" if p_on > p_off else "overriding",
                            "on": f"{sum(on)}/{len(on)}", "off": f"{sum(off)}/{len(off)}"})
    return sorted(out, key=lambda r: (-abs(r["gap"]), r["action"], r["item"]))


def cmd_induce(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    (r, m), = run(spec, a.run or runs_of(spec)[0]["name"])
    rows = induce(m, a.min_trials, a.thresh)
    have = {"context": {(x.action, c) for x in m.schemas for c in x.context},
            "overriding": {(c.action, x) for c in m.censors if c.kind == "precursor" for x in c.context}}
    for row in rows:
        row["in_model"] = (row["action"], row["item"]) in have[row["kind"]]
    bus.emit("RESULT", "induce", f"{len(rows)} proposed contexts", rows=rows)
    if a.patch:
        patch = {"censors": [{
            "id": f"learned-no-{row['action']}-when-{row['item']}", "kind": "precursor",
            "context": [row["item"]], "action": row["action"], "harm": [],
            "learned_from": f"induce over {a.file}, run {r['name']}: took it {row['on']} with "
                            f"{row['item']} on, {row['off']} off",
            "cover": "", "source": ""} for row in rows if row["kind"] == "overriding" and not row["in_model"]]}
        return emit_out(patch, a.format or "yaml")
    lines = [f"induced from {len(m.situations)} observed choices (run {r['name']}; gap = P(take | on) - P(take | off)):"]
    for row in rows:
        mark = "" if row["in_model"] else "   <- not in the model"
        lines.append(f"  {row['action']:<12} {row['item']:<28} {row['kind']:<10} {row['gap']:+.2f}  on {row['on']:>5}  off {row['off']:>5}{mark}")
    return emit_out(rows, a.format or "text", "\n".join(lines))


def drift(m, half_life=4.0):
    """How a hypothesis fits over time, not just in total. People change:
    one that fit his first ten choices and missed his last three is worse
    than its total says. Recent choices weigh more, halving every
    `half_life` choices back; `holds_since` is where the unbroken run of
    hits at the end starts."""
    hits = [o == a for _, o, a in m.fit]
    n = len(hits)
    w = [0.5 ** ((n - 1 - i) / half_life) for i in range(n)]
    tail = next((i for i in range(n, 0, -1) if not hits[i - 1]), 0)
    return {"hits": sum(hits), "total": n,
            "recent": round(sum(x * h for x, h in zip(w, hits)) / sum(w), 3) if n else None,
            "holds_since": m.fit[tail][0] if tail < n else None,
            "strip": "".join("#" if h else "." for h in hits),
            "misses": [t for (t, _, _), h in zip(m.fit, hits) if not h]}


def cmd_drift(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    rows = []
    for r, m in run(spec):
        if r.get("counterfactual") or not m.fit:
            continue
        rows.append({"run": r["name"], **drift(m, a.half_life)})
    rows.sort(key=lambda x: (-x["recent"], -x["hits"]))
    bus.emit("RESULT", "drift", "; ".join(f"{x['run']}: recent {x['recent']:.2f}" for x in rows), rows=rows)
    w = max([len(x["run"]) for x in rows] + [3])
    lines = [f"fit over time (recent: hits weighted by recency, half-life {a.half_life:g} choices; # hit, . miss, oldest first):",
             f"  {'run':<{w}}  {'fit':>6}  recent  holds since  record"]
    lines += [f"  {x['run']:<{w}}  {str(x['hits']) + '/' + str(x['total']):>6}  {x['recent']:.2f}    "
              f"{('t=' + str(x['holds_since'])) if x['holds_since'] is not None else '-':<11}  {x['strip']}"
              for x in rows]
    return emit_out(rows, a.format or "text", "\n".join(lines))


def propose(m, min_run=2):
    """Drescher's synthetic items, over the record. When no item we observe
    explains an action, but his choices about it are locally consistent
    (taken, taken, taken, then refused from some point on), something we
    don't see changed state there. Propose it as a latent item, oriented so
    that ON stops the action, and ask what it was."""
    out = []
    for act in sorted({x for _, offers, _, _ in m.situations for x in offers}):
        rows = sorted((t, obs == act, items) for t, offers, obs, items in m.situations if act in offers)
        took = [x for _, x, _ in rows]
        n = len(took)
        if n < 2 * min_run or all(took) or not any(took):
            continue
        best_seen = max(took.count(True), took.count(False))
        seen_by = None
        # An item the choice itself sets is its result, not its cause.
        offered = {x for _, offers, _, _ in m.situations if act in offers for x in offers}
        results = {k for s in m.schemas if s.action in offered for k in s.result}
        for item in sorted({k for _, _, items in rows for k in items} - results):
            hits = sum(x == (items.get(item) is ON) for _, x, items in rows)
            hits = max(hits, n - hits)
            if hits > best_seen:
                best_seen, seen_by = hits, item
        best = None
        for k in range(min_run, n - min_run + 1):
            a, b = took[:k], took[k:]
            fa, fb = a.count(True) >= len(a) / 2, b.count(True) >= len(b) / 2
            if fa == fb:
                continue
            hits = (a.count(fa)) + (b.count(fb))
            if not best or hits > best[0]:
                best = (hits, k, fa)
        if not best or best[0] <= best_seen:
            continue
        hits, k, before_takes = best
        t_last, t_first = rows[k - 1][0], rows[k][0]
        out.append({"action": act, "latent": f"latent-{act}-{'from' if before_takes else 'until'}-t{t_first if before_takes else t_last}",
                    "on_from": t_first if before_takes else None, "off_from": None if before_takes else t_first,
                    "between": [t_last, t_first], "fits": f"{hits}/{n}",
                    "best_observed": f"{best_seen}/{n}" + (f" ({seen_by})" if seen_by else " (no item)"),
                    "flips": sum(x != y for x, y in zip(took, took[1:]))})
    # In a two-way choice, one action stopping is the other starting: one
    # latent item per window, put on the action that stopped.
    stops = {tuple(r["between"]) for r in out if r["on_from"] is not None}
    return [r for r in out if r["on_from"] is not None or tuple(r["between"]) not in stops]


def cmd_propose(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    (r, m), = run(spec, a.run or runs_of(spec)[0]["name"])
    rows = propose(m, a.min_run)
    patch = {"agent": {"items": {}}, "events": [], "censors": []}
    for row in rows:
        lo, hi = row["between"]
        t_switch = round(lo + (hi - lo) / 2, 3)
        first_on = row["on_from"] is not None
        patch["agent"]["items"][row["latent"]] = "off" if first_on else "on"
        patch["events"].append({"t": t_switch, "set": {row["latent"]: "on" if first_on else "off"},
                                "say": f"<what changed between t={lo} and t={hi}>", "source": ""})
        patch["censors"].append({
            "id": f"learned-no-{row['action']}-when-{row['latent']}", "kind": "precursor",
            "context": [row["latent"]], "action": row["action"], "harm": [],
            "learned_from": f"propose over {a.file}, run {r['name']}: a switch between t={lo} and "
                            f"t={hi} fits {row['fits']}; the best observed item, {row['best_observed']}",
            "cover": "", "source": ""})
        bus.emit("REQUEST", "latent", f"'{row['action']}' changed between t={lo} and t={hi}, and nothing observed explains it",
                 key={"agent": m.name, "latent": row["latent"]}, **row,
                 ask="what happened in that window that would make the change; name it, cite it, or say nothing is known",
                 patch={"agent": {"items": {row["latent"]: patch["agent"]["items"][row["latent"]]}},
                        "events": [patch["events"][-1]], "censors": [patch["censors"][-1]]})
    bus.emit("RESULT", "propose", f"{len(rows)} latent items proposed", rows=rows)
    if a.patch:
        return emit_out(patch, a.format or "yaml")
    lines = [f"proposed from {len(m.situations)} observed choices (run {r['name']}):"]
    lines += [f"  {row['action']:<16} {'stops' if row['on_from'] is not None else 'starts'} between t={row['between'][0]} and "
              f"t={row['between'][1]}: fits {row['fits']}, best observed {row['best_observed']}, {row['flips']} flip(s)"
              for row in rows] or ["  nothing: every action is constant, or explained by an item we observe"]
    return emit_out(rows, a.format or "text", "\n".join(lines))


def walk(m, steps):
    """Replay a plan from the current items: which censor, if any, vetoes
    each step in the state where it would be taken."""
    items, out = dict(m.items), []
    for act in steps:
        hits = m.vetoed(act, items)
        out.append({"action": act, "vetoed_by": hits[0].id if hits else None})
        s = m.schema_for(act, items)
        for k, v in (s.result.items() if s else []):
            items[k] = parse_value(v)
    return out


def cmd_plan(a, bus):
    """Drescher's planner with Minsky's censors in the search. Two plans:
    the one the agent can think of, and the one an observer can see. Where
    they differ, the censor that pruned the path is named."""
    spec = load([a.file], a.layer, a.who, a.set)
    goal = [g.strip() for g in a.goal.split(",") if g.strip()]
    r = runs_of(spec, a.run)[0] if a.run else runs_of(spec)[0]
    if a.at == "start":
        m = Mind(run_spec(spec, r), bus)
    else:
        (_, m), = run(spec, r["name"], bus)
    for k, _, v in (kv.partition("=") for kv in a.set_item):
        m.items[k] = parse_value(v)
    inner = m.plan(goal, censored=True, max_steps=a.max_steps)
    outer = m.plan(goal, censored=False, max_steps=a.max_steps)
    hidden = [x for x in walk(m, outer["steps"] or []) if x["vetoed_by"]]
    out = {"run": r["name"], "at": a.at, "goal": goal, "items_on": m.on_items(),
           "agent_plan": inner["steps"], "agent_cost": inner["cost"],
           "observer_plan": outer["steps"], "observer_cost": outer["cost"],
           "hidden_by": hidden, "pruned": [{"action": x, "censor": c} for x, c in inner["pruned"]]}
    if outer["steps"] is None:
        bus.emit("REQUEST", "schema", f"no chain of schemas reaches {goal}",
                 key={"agent": m.name, "plan": goal}, goal=goal, items_on=m.on_items(),
                 ask="which action would bring this about, from what context?",
                 patch={"schemas": [{"id": "<action>", "action": "<action>", "context": [],
                                     "result": {g.lstrip("!"): "off" if g.startswith("!") else "on" for g in goal},
                                     "source": "tier0: <who answered>"}]})
    bus.emit("RESULT", "plan", f"{goal}: agent {inner['steps']}, observer {outer['steps']}", **out)
    show = lambda steps: " → ".join(steps) if steps else ("(already true)" if steps == [] else "none found")
    lines = [f"plan for {', '.join(goal)} (run {r['name']}, at {a.at}; on: {', '.join(m.on_items()) or 'nothing'}):",
             f"  agent sees:    {show(inner['steps'])}" + (f"   cost {inner['cost']}" if inner["steps"] else ""),
             f"  observer sees: {show(outer['steps'])}" + (f"   cost {outer['cost']}" if outer["steps"] else "")]
    lines += [f"  hidden: '{x['action']}' is vetoed by censor {x['vetoed_by']}" for x in hidden]
    if inner["steps"] != outer["steps"] and not hidden and outer["steps"]:
        lines.append("  the plans differ in cost only")
    return emit_out(out, a.format or "text", "\n".join(lines))


# == learning from a record: propose, gate, ask ===============================
def run_fit(spec, r):
    return score(run({**spec, "runs": [r]})[0][1])[0]


def replayed(spec, r):
    """Run r with schema learning on, learning from what the person did."""
    merged = run_spec(spec, r)
    merged = {**merged, "agent": {**merged["agent"], "learn_schemas": True}}
    m = Mind(merged)
    m.replay = True
    for ev in sorted(spec.get("events", []) + r.get("events", []), key=lambda e: e["t"]):
        m.step(ev, quotes=False)
    return m


def learn(spec, run_name=None, rounds=4):
    """Drescher's learner over a record, as a loop with a gate. Each round
    replays the record with result and context spinoffs on, proposes every
    schema it learned, and keeps a proposal only if the model with it fits
    the record better. Kept ones feed the next round. Stops when a round
    keeps nothing. The words for what a kept schema means are asked for."""
    r = runs_of(spec, run_name)[0]
    cur, rows, kept = spec, [], []
    for rnd in range(1, rounds + 1):
        have = {s["id"]: s for s in cur.get("schemas", [])}
        m = replayed(cur, r)
        props = []
        for s in m.schemas:
            if s.id.startswith("learned-"):
                p = {"id": s.id, "action": s.action, "context": s.context, "result": s.result,
                     "reliability": s.reliability, "source": s.source}
                if have.get(s.id) and {k: have[s.id].get(k) for k in ("context", "result")} == \
                        {"context": s.context, "result": s.result}:
                    continue
            elif s.id in have and s.result != have[s.id].get("result"):
                p = {"id": s.id, "result": {k: v for k, v in s.result.items() if k not in have[s.id].get("result", {})}}
            else:
                continue
            props.append(p)
        base = run_fit(cur, r)
        scored = sorted(((run_fit(merge(cur, {"schemas": [p]}), r) - base, p) for p in props),
                        key=lambda x: (-x[0], x[1]["id"]))
        took = 0
        for d, p in scored:
            now = run_fit(cur, r)
            after = run_fit(merge(cur, {"schemas": [p]}), r)
            verdict = "kept" if after > now else "worse" if after < now else "no gain"
            rows.append({"round": rnd, "id": p["id"], "action": p.get("action"), "context": p.get("context"),
                         "result": p["result"], "reliability": p.get("reliability"),
                         "fit": f"{now} → {after}", "verdict": verdict})
            if verdict == "kept":
                cur = merge(cur, {"schemas": [p]})
                kept.append(p)
                took += 1
        if not took:
            break
    return r, rows, kept, cur


def cmd_learn(a, bus):
    spec = load([a.file], a.layer, a.who, a.set)
    r, rows, kept, cur = learn(spec, a.run, a.rounds)
    total = len([e for e in spec.get("events", []) + r.get("events", []) if e.get("observed")])
    start, end = run_fit(spec, r), run_fit(cur, r)
    for p in kept:
        bus.emit("REQUEST", "schema-meaning", f"learned schema {p['id']} fits the record; say what it means",
                 key={"learned": p["id"], "result": p["result"]}, schema=p["id"],
                 ask="one line saying in words what this schema claims, and a source if one supports it; "
                     "or drop it if it's an artifact of how the record was written",
                 patch={"schemas": [{"id": p["id"], "note": "<what it claims>", "source": "tier0: <who answered>"}]})
    bus.emit("RESULT", "learn", f"{r['name']}: fit {start}/{total} → {end}/{total}, {len(kept)} schemas kept",
             run=r["name"], before=start, after=end, total=total, kept=[p["id"] for p in kept])
    if a.patch:
        return emit_out({"schemas": [{**p, "learned_from": f"learn over {os.path.basename(a.file)}, run {r['name']}"}
                                     for p in kept]}, a.format or "yaml")
    lines = [f"learned from the record (run {r['name']}): fit {start}/{total} → {end}/{total}"]
    for x in rows:
        what = f"{x['action'] or ''} → {x['result']}" + (f" when {x['context']}" if x.get("context") else "")
        lines.append(f"  round {x['round']}  {x['verdict']:<8} {x['id']:<36} {what}  (fit {x['fit']})")
    if not rows:
        lines.append("  nothing to propose: no item follows any action more than it follows the others")
    return emit_out(rows, a.format or "text", "\n".join(lines))


def cmd_try(a, bus):
    """The gate for a proposal from outside: the same scenario with and
    without the --layer files. Keep the layer only if no run fits worse."""
    base, cand = load([a.file], [], a.who, a.set), load([a.file], a.layer, a.who, a.set)
    rows = []
    for r in runs_of(cand, a.run):
        if r.get("counterfactual"):
            continue
        rb = next((x for x in runs_of(base) if x["name"] == r["name"]), None)
        before = run_fit(base, rb) if rb else None
        after, total = score(run({**cand, "runs": [r]})[0][1])
        rows.append({"run": r["name"], "before": before, "after": after, "total": total})
    lint = {"before": lint_spec(base, Bus())["errors"], "after": lint_spec(cand, Bus())["errors"]}
    worse = [x for x in rows if x["before"] is not None and x["after"] < x["before"]]
    better = [x for x in rows if x["before"] is not None and x["after"] > x["before"]]
    verdict = "reject" if worse or lint["after"] > lint["before"] else "keep" if better else "no gain"
    a._exit = 2 if verdict == "reject" else 0
    bus.emit("RESULT", "try", verdict, verdict=verdict, runs=rows, lint=lint)
    lines = [f"{x['run']}: {x['before']}/{x['total']} → {x['after']}/{x['total']}" for x in rows]
    lines.append(f"lint errors: {lint['before']} → {lint['after']}")
    lines.append(f"verdict: {verdict}")
    return emit_out({"verdict": verdict, "runs": rows, "lint": lint}, a.format or "text", "\n".join(lines))


# == duets: two minds, one world ==============================================
def duet_seats(spec, here):
    """Each seat's mind, resolved once: its file, one of its runs, and any
    overrides the duet gives it. The mind's own record is not used."""
    seats = {}
    for seat, d in spec["seats"].items():
        mspec = load([os.path.join(here, d["mind"])], [os.path.join(here, x) for x in d.get("layers", [])])
        r = runs_of(mspec, d.get("run"))[0] if d.get("run") else runs_of(mspec)[0]
        if d.get("agent"):
            r = {**r, "agent": merge(r.get("agent") or {}, d["agent"])}
        seats[seat] = run_spec(mspec, r)
    return seats


def duet(spec, seats, factors=None, bus=NULL):
    """Play the turns. A turn with a `seat` is that mind's choice; one without
    is the world changing. An action listed in `effects` sets items for every
    seat, so one mind's move is the other's news. A turn with `when` happens
    only if those conditions hold in the world so far."""
    minds = {}
    for seat, merged in seats.items():
        f = (factors or {}).get(seat)
        if f:
            vals = merged["agent"].get("values", {})
            merged = {**merged, "agent": {**merged["agent"], "values": {k: w * f.get(k, 1.0) for k, w in vals.items()}}}
        minds[seat] = Mind(merged, bus)
    world, log, effects = {}, [], spec.get("effects") or {}
    for k, v in (spec.get("world") or {}).items():
        world[k] = parse_value(v)
        for m in minds.values():
            m.items[k] = world[k]
    for turn in sorted(spec.get("turns", []), key=lambda e: e["t"]):
        if not all(holds(world, c) for c in turn.get("when", [])):
            log.append({"t": turn["t"], "seat": turn.get("seat"), "skipped": turn.get("when")})
            continue
        sets = turn.get("set") or {}
        for k, v in sets.items():
            world[k] = parse_value(v)
        seat = turn.get("seat")
        if seat and seat not in minds:
            raise ValueError(f"turn t={turn['t']}: no seat '{seat}'")
        for name, m in minds.items():
            ev = {"t": turn["t"], "set": sets}
            if name == seat:
                ev.update({k: turn[k] for k in ("say", "offers", "observed", "response", "joke") if k in turn})
            elif turn.get("say") and not seat:
                ev["say"] = turn["say"]
            m.step(ev)
        if not seat:
            log.append({"t": turn["t"], "seat": None, "set": sets, "say": turn.get("say")})
            continue
        m = minds[seat]
        act = m.choices[-1][1] if m.choices and m.choices[-1][0] == turn["t"] else None
        fired = [e["text"] for e in m.observer if e["t"] == turn["t"] and "vetoes" in e["text"]]
        log.append({"t": turn["t"], "seat": seat, "action": act, "observed": turn.get("observed"),
                    "censors": fired, "effect": effects.get(act) or {}})
        for k, v in (effects.get(act) or {}).items():
            world[k] = parse_value(v)
            for other in minds.values():
                other.items[k] = world[k]
    return log, world, minds


def duet_spread(spec, seats, n, seed=0, spread=0.5):
    """The duet over n weightings, each seat's weights drawn independently."""
    rng = random.Random(seed)
    names = {s: list(m["agent"].get("values", {})) for s, m in seats.items()}
    seqs, finals = Counter(), Counter()
    watch = spec.get("watch") or []
    for _ in range(n):
        f = {s: {k: rng.uniform(1 - spread, 1 + spread) for k in ks} for s, ks in names.items()}
        log, world, _ = duet(spec, seats, f)
        seqs[tuple(f"{x['seat']}:{x['action']}" for x in log if x.get("seat") and "action" in x)] += 1
        for k in watch:
            finals[k] += world.get(k) is ON
    return {"n": n, "spread": spread,
            "watch": {k: round(finals[k] / n, 4) for k in watch},
            "outcomes": [{"share": round(c / n, 4), "moves": list(s)} for s, c in seqs.most_common(5)]}


def test_duet(spec, seats):
    log, world, _ = duet(spec, seats)
    exp, problems = spec.get("expect") or {}, []
    moves = [f"{x['seat']}:{x['action']}" for x in log if x.get("seat") and "action" in x]
    if "moves" in exp and moves != exp["moves"]:
        problems.append(f"moves {moves}")
    for k, v in (exp.get("world") or {}).items():
        if (world.get(k) is ON) != bool(parse_value(v)):
            problems.append(f"world {k}={'on' if world.get(k) is ON else 'off'}, expected {v}")
    misses = [x for x in log if x.get("observed") and x["observed"] != x.get("action")]
    if misses and not exp.get("misses_ok"):
        problems += [f"t={x['t']} {x['seat']}: observed {x['observed']}, model {x['action']}" for x in misses]
    return problems


def cmd_duet(a, bus):
    """Two minds on one stage: each one's move is an event for the other."""
    spec = load([a.file], a.layer, a.who, a.set)
    seats = duet_seats(spec, os.path.dirname(os.path.abspath(a.file)))
    if a.n > 1:
        out = duet_spread(spec, seats, a.n, a.seed, a.spread)
        bus.emit("RESULT", "duet", "; ".join(f"{k} {v:.0%}" for k, v in out["watch"].items()) or "done", **out)
        lines = [f"{a.n} weightings (±{a.spread:.0%}), each seat drawn independently:"]
        lines += [f"  {k} ends on: {v:.0%}" for k, v in out["watch"].items()]
        lines += [f"  {o['share']:6.1%}  " + " → ".join(o["moves"]) for o in out["outcomes"]]
        return emit_out(out, a.format or "text", "\n".join(lines))
    log, world, minds = duet(spec, seats, bus=bus)
    problems = test_duet(spec, seats)
    a._exit = 2 if (a.test and problems) else 0
    bus.emit("RESULT", "duet", "; ".join(problems) or "ok", ok=not problems, problems=problems)
    lines = []
    for x in log:
        if x.get("skipped") is not None:
            lines.append(f"  t={x['t']}: ({x['seat'] or 'world'} skipped: needs {', '.join(x['skipped'])})")
        elif not x.get("seat"):
            lines.append(f"  t={x['t']}: world: " + (x.get("say") or ", ".join(
                f"{k}={'on' if parse_value(v) else 'off'}" for k, v in x["set"].items())))
        else:
            name = minds[x["seat"]].name
            mark = "" if not x.get("observed") else ("  (as observed)" if x["observed"] == x["action"] else f"  (observed: {x['observed']})")
            lines.append(f"  t={x['t']}: {name}: {x['action'] or 'nothing'}{mark}")
            lines += [f"         {c}  [unconscious]" for c in x["censors"]]
            if x["effect"]:
                lines.append("         → " + ", ".join(f"{k}={'on' if parse_value(v) else 'off'}" for k, v in x["effect"].items()))
    lines.append("world at the end: " + (", ".join(k for k, v in world.items() if v is ON) or "nothing on"))
    if problems:
        lines.append("PROBLEMS: " + "; ".join(problems))
    return emit_out({"log": log, "world": {k: v for k, v in world.items()}, "problems": problems},
                    a.format or "text", "\n".join(lines))


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
            "patches": [c["id"] for c in raw.get("censors", []) if "kind" not in c and not c.get("drop")],
            "drops": [c["id"] for c in raw.get("censors", []) + raw.get("schemas", []) if c.get("drop")],
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
                "drops " + ", ".join(r["drops"]) if r["drops"] else "",
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
    s = sub.add_parser("suite", parents=[common]); s.add_argument("paths", nargs="+")
    s.add_argument("--ablate", action="store_true", help="also list censors each factual run doesn't need")
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
    s.add_argument("--patch", action="store_true", help="emit learned censors for the overriding conditions the model lacks")
    s = sub.add_parser("argue", parents=[common]); s.add_argument("file")
    s.add_argument("--offers", required=True); s.add_argument("--goal", required=True)
    s.add_argument("--args", required=True, help="YAML list of arguments: {id, about, say, set, joke, source}")
    s.add_argument("--set-item", action="append", default=[], metavar="ITEM=on|off", help="the situation before any argument")
    s.add_argument("--n", type=int, default=300); s.add_argument("--seed", type=int, default=0)
    s.add_argument("--spread", type=float, default=0.5)
    s = sub.add_parser("drift", parents=[common]); s.add_argument("file")
    s.add_argument("--half-life", type=float, default=4.0, help="choices back at which a hit counts half")
    s = sub.add_parser("propose", parents=[common]); s.add_argument("file"); s.add_argument("--run")
    s.add_argument("--min-run", type=int, default=2, help="fewest choices on each side of a switch")
    s.add_argument("--patch", action="store_true", help="emit the latent items, their switch events and censors as one layer")
    s = sub.add_parser("plan", parents=[common]); s.add_argument("file")
    s.add_argument("--goal", required=True, help="items to make true, comma-separated; !x for x off")
    s.add_argument("--run"); s.add_argument("--at", choices=["start", "end"], default="end",
                                           help="plan from the run's starting items, or where the record leaves it")
    s.add_argument("--set-item", action="append", default=[], metavar="ITEM=on|off")
    s.add_argument("--max-steps", type=int, default=8)
    s = sub.add_parser("learn", parents=[common]); s.add_argument("file"); s.add_argument("--run")
    s.add_argument("--rounds", type=int, default=4)
    s.add_argument("--patch", action="store_true", help="emit the kept schemas as one layer")
    s = sub.add_parser("try", parents=[common]); s.add_argument("file"); s.add_argument("--run")
    s = sub.add_parser("duet", parents=[common]); s.add_argument("file")
    s.add_argument("--n", type=int, default=1, help="more than 1: draw each seat's weights n times and tally outcomes")
    s.add_argument("--seed", type=int, default=0); s.add_argument("--spread", type=float, default=0.5)
    s.add_argument("--test", action="store_true", help="exit 2 unless the duet meets its expect:")
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
