#!/usr/bin/env python3
"""Censor simulator: Minsky's AI Memo 603 run on Drescher's schema mechanism.

A schema is context -> action -> result with a reliability. A censor is a
schema with the sign bit flipped: same triple, result marked harmful, stored
response "suppress". Precursor censors veto an action before it runs, so the
agent never sees the thought; it only sees the cover story it tells itself.
Suppressors fire after a forbidden state forms and re-file it under another
frame. Marginal attribution over painful results mints new censors. A joke
makes a firing visible to the agent, which is how censors get retrained.

Two traces are kept. INNER is what the agent experiences: chosen actions and
the reasons it gives. OBSERVER also records every censor that fired. The gap
between them is the cognitive unconscious.

Events may record what a real agent actually did (`observed:`); the report
then scores the model's fit, and --ablate drops each censor in turn to show
which ones the data actually requires. Real quotes (`response:`) print only
when the model's action matches the observed one.

Usage: censor_sim.py SCENARIO.yml [--run NAME] [--markdown] [--ablate]
"""

import argparse
import sys
from dataclasses import dataclass, field

import yaml

ON, OFF = True, False
OVERRIDE = 0.6


@dataclass
class Schema:
    id: str
    action: str
    context: list
    result: dict
    reliability: float = 1.0
    note: str = ""


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
    reliability: float = 1.0
    learned_from: str = ""
    anecdotal: bool = False
    visible: bool = False         # a joke has exposed it to the agent

    def matches(self, items):
        return all(holds(items, c) for c in self.context)


def holds(items, cond):
    """'x' means x is ON; '!x' means x is OFF."""
    if cond.startswith("!"):
        return items.get(cond[1:]) is OFF
    return items.get(cond) is ON


class Mind:
    def __init__(self, spec, learn_threshold=2):
        a = spec["agent"]
        self.name = a["name"]
        self.items = {k: parse_value(v) for k, v in a.get("items", {}).items()}
        self.values = a.get("values", {})
        self.contradictions = [tuple(p) for p in a.get("contradictions", [])]
        self.schemas = [Schema(**s) for s in spec.get("schemas", [])]
        self.censors = [Censor(**c) for c in spec.get("censors", [])]
        self.learn_threshold = learn_threshold
        self.pain_counts = {}         # (action, item) -> times ON when it hurt
        self.pain_events = {}         # action -> times it hurt
        self.inner, self.observer = [], []
        self.fit = []                 # (t, observed action, model's action)

    # -- the two traces ---------------------------------------------------
    def log(self, t, text, inner=True, quote=None):
        entry = {"t": t, "text": text, "inner": inner}
        if quote:
            entry["quote"] = quote
        self.observer.append(entry)
        if inner:
            self.inner.append(entry)

    # -- schema machinery -------------------------------------------------
    def schema_for(self, action):
        fits = [s for s in self.schemas
                if s.action == action and all(holds(self.items, c) for c in s.context)]
        return max(fits, key=lambda s: (len(s.context), s.reliability), default=None)

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

    def decide(self, t, offers):
        open_, covers = [], []
        for act in offers:
            hits = self.vetoed(act)
            if hits:
                c = hits[0]
                self.log(t, f"censor {c.id} vetoes '{act}' (predicts {', '.join(c.harm)})",
                         inner=c.visible)
                if c.cover:
                    covers.append(c.cover)
            else:
                open_.append(act)
        if not open_:
            self.log(t, "every option vetoed; does nothing")
            return None, covers
        best = max(open_, key=self.predicted_value)
        return best, covers

    def apply(self, t, action):
        s = self.schema_for(action)
        if not s:
            return []
        changed = []
        for k, v in s.result.items():
            if self.items.get(k) is not v:
                self.items[k] = v
                changed.append(k)
        return changed

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
                    self.log(t, f"thinks: \"{c.cover}\"")

    # -- learning: marginal attribution over pain --------------------------
    def attribute(self, t, action, before):
        pain = [k for k, v in self.items.items()
                if v is ON and self.values.get(k, 0) < 0 and before.get(k) is not ON]
        pain += [f"{a}+{b}" for a, b in self.conflicts()]
        if not pain:
            return
        self.pain_events[action] = self.pain_events.get(action, 0) + 1
        for k, v in before.items():
            if v is ON:
                self.pain_counts[(action, k)] = self.pain_counts.get((action, k), 0) + 1
        n = self.pain_events[action]
        if n < self.learn_threshold or any(c.action == action and c.learned_from for c in self.censors):
            return
        ctx = sorted(k for (a, k), cnt in self.pain_counts.items() if a == action and cnt == n)
        cid = f"learned-{action}"
        self.censors.append(Censor(id=cid, kind="precursor", context=ctx, action=action,
                                   harm=pain, cover="", learned_from=f"{n} painful '{action}'s"))
        self.log(t, f"marginal attribution mints censor {cid}: context {ctx}", inner=False)

    # -- humor: the training signal ---------------------------------------
    def joke(self, t, ev):
        target = next((c for c in self.censors if c.id == ev["exposes"]), None)
        if not target:
            return
        target.visible = True
        target.reliability *= ev.get("discount", 0.5)
        self.log(t, f"laughs: notices censor {target.id} ({ev.get('text', '')})")
        if "lesson" in ev:
            L = ev["lesson"]
            self.censors.append(Censor(anecdotal=True, visible=True, kind="precursor",
                                       learned_from=f"joke at t={t}", **L))
            self.log(t, f"installs anecdotal censor {L['id']}: vetoes '{L['action']}' when {L['context']}")

    # -- the run loop ------------------------------------------------------
    def step(self, ev):
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
            if act:
                why = f' — "{covers[0]}"' if covers else ""
                # A real quote belongs only to the action the real person took.
                quote = ev.get("response") if act == observed or not observed else None
                self.log(t, f"does '{act}'{why}", quote=quote)
                self.apply(t, act)
                self.suppress(t)
                self.attribute(t, act, before)


def parse_value(v):
    if v in (True, "on", "ON"):
        return ON
    if v in (False, "off", "OFF"):
        return OFF
    return None


def run(spec, run_name=None):
    runs = spec.get("runs") or [{"name": "default"}]
    out = []
    for r in runs:
        if run_name and r["name"] != run_name:
            continue
        merged = {**spec,
                  "censors": spec.get("censors", []) + r.get("add_censors", []),
                  "schemas": spec.get("schemas", []) + r.get("add_schemas", [])}
        m = Mind(merged)
        events = sorted(spec.get("events", []) + r.get("events", []), key=lambda e: e["t"])
        for ev in events:
            m.step(ev)
        out.append((r, m))
    return out


def render(results, markdown):
    lines = []
    for r, m in results:
        lines.append(f"## {m.name} — run: {r['name']}" if markdown else f"=== {m.name} / {r['name']}")
        if r.get("about"):
            lines.append(r["about"].strip())
        lines.append("")
        bullet = "- " if markdown else "  "
        lines.append("**Inner trace** (what it experiences)" if markdown else "INNER (what it experiences):")
        lines.append("")
        for e in m.inner:
            lines.append(f"{bullet}t={e['t']}: {e['text']}")
        lines.append("")
        lines.append("**Observer trace** (everything that fired)" if markdown else "OBSERVER (everything that fired):")
        lines.append("")
        for e in m.observer:
            mark = " *[unconscious]*" if markdown else "  [unconscious]"
            lines.append(f"{bullet}t={e['t']}: {e['text']}{'' if e['inner'] else mark}")
            if e.get("quote"):
                lines.append(f"  > {e['quote']}" if markdown else f"      \"{e['quote']}\"")
        lines.append("")
        lines.append(f"final items: " + ", ".join(
            f"{k}={'ON' if v else 'OFF' if v is OFF else '?'}" for k, v in m.items.items()))
        if m.fit and not r.get("counterfactual"):
            hits = sum(1 for _, o, a in m.fit if o == a)
            lines.append("")
            lines.append(f"fit to observed actions: {hits}/{len(m.fit)}" + "".join(
                f"\n  MISMATCH t={t}: observed '{o}', model did '{a}'" for t, o, a in m.fit if o != a))
        open_conflicts = m.conflicts()
        if open_conflicts:
            lines.append("")
            lines.append("unresolved conflict, now conscious: " + "; ".join(f"{a} vs {b}" for a, b in open_conflicts))
        lines.append("")
    return "\n".join(lines)


def ablate(spec):
    """Drop each hypothesized censor in turn. A censor the fit doesn't need
    is an invention the data doesn't support."""
    lines = ["Ablation: fit to observed actions with each censor removed", ""]
    factual = [r for r in (spec.get("runs") or [{"name": "default"}]) if not r.get("counterfactual")]
    for r in factual:
        base = run({**spec, "runs": [r]})[0][1]
        total = len(base.fit)
        lines.append(f"run {r['name']}: all censors -> {sum(o == a for _, o, a in base.fit)}/{total}")
        for c in spec.get("censors", []):
            trimmed = {**spec, "runs": [r], "censors": [x for x in spec["censors"] if x["id"] != c["id"]]}
            m = run(trimmed)[0][1]
            hits = sum(o == a for _, o, a in m.fit)
            verdict = "needed" if hits < total else "NOT NEEDED"
            lines.append(f"  without {c['id']:<16} -> {hits}/{total}  {verdict}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("scenario")
    p.add_argument("--run")
    p.add_argument("--markdown", action="store_true")
    p.add_argument("--ablate", action="store_true", help="test whether each censor is needed")
    a = p.parse_args()
    with open(a.scenario) as f:
        spec = yaml.safe_load(f)
    print(ablate(spec) if a.ablate else render(run(spec, a.run), a.markdown))


if __name__ == "__main__":
    sys.exit(main())
