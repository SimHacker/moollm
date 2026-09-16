#!/usr/bin/env python3
"""Compile Margolus block rules from Korz YAML slots into specialized JavaScript.

Input:  ../../examples/margolus-rules.yml  (unmodified — the spec is the source)
Output: generated/margolus.js

This is the first Futamura projection done by hand for one rule family: the slot set is
partially evaluated over every reachable block state, producing a 16-entry table, and the
table is emitted inside a scan loop specialized for the declared group and schedule.
"""

import sys, json, pathlib, yaml

HERE = pathlib.Path(__file__).parent
SPEC = HERE / ".." / ".." / "examples" / "margolus-rules.yml"
OUT = HERE / "generated" / "margolus.js"

# Block site indexing, clockwise from north-west. 2D only; the YAML is written for
# arbitrary d, and see FINDINGS.md for what that costs.
NW, NE, SE, SW = 0, 1, 2, 3
SITE_NAMES = ["NW", "NE", "SE", "SW"]

# A permutation is "content at site i moves to site perm[i]".
PERMUTATIONS = {
    "rotate+1": [1, 2, 3, 0],
    "rotate-1": [3, 0, 1, 2],
    "rotate+2": [2, 3, 0, 1],
    "swap-diagonals": [2, 3, 0, 1],
}

COMPILABLE = ["rotate", "tron", "billiard_ball", "critters", "hpp_gas", "swap_on_diagonal"]

# TODO (unfinished): diffusion. Its random dimension is FINITE, so taking
# margolus-rules.yml's "random as a context coordinate, not a side effect" literally means the
# index widens from 16 to 16k and the rule still tabulates — no code back end needed. build_table
# already widens; emit_kernel does not yet index the wider table. Do not add it to this list
# until the kernel reads the random coordinate.

# margolus-rules.yml: "random as a context coordinate, not a side effect". Taken literally, a
# random dimension of arity k just widens the table index from 16 to 16k. It does not force the
# code back end. This list is the declared value set for each symbolic random dimension.
RANDOM_VALUES = ["cw", "ccw"]


def popcount(state):
    return bin(state).count("1")


def orbit_labels(state):
    """The label vocabulary the YAML's `arrangement` guard refers to but never enumerates."""
    labels = set()
    pop = popcount(state)
    if pop in (0, 4):
        labels.add("uniform")
    if pop == 2:
        diagonal = state in (0b0101, 0b1010)  # {NW,SE} or {NE,SW}
        labels.add("diagonal" if diagonal else "adjacent")
    return labels


def apply_permutation(state, perm):
    out = 0
    for i in range(4):
        if state & (1 << i):
            out |= 1 << perm[i]
    return out


def apply_emission(state, emit):
    """Apply one slot's emission. Order within a slot is source order; see FINDINGS.md."""
    out = state
    for key, value in emit.items():
        if key == "identity":
            pass
        elif key == "complement":
            out = (~out) & 0xF
        elif key == "rotate":
            sign = "+" if value >= 0 else "-"
            out = apply_permutation(out, PERMUTATIONS[f"rotate{sign}{abs(value)}"])
        elif key == "permute":
            if value not in PERMUTATIONS:
                raise Unsupported(f"emission bank has no permutation {value!r}")
            out = apply_permutation(out, PERMUTATIONS[value])
        else:
            raise Unsupported(f"unknown emission {key!r}")
    return out


class Unsupported(Exception):
    pass


def guard_matches(state, guard, ctx):
    for key, want in guard.items():
        if key == "population":
            pop = popcount(state)
            if isinstance(want, list):
                if pop not in want:
                    return False
            elif pop != want:
                return False
        elif key == "arrangement":
            if want not in orbit_labels(state):
                return False
        elif key == "random":
            if not isinstance(want, str):
                raise Unsupported("random guard is real-valued, not a finite dimension")
            if ctx.get("random") != want:
                return False
        else:
            raise Unsupported(f"guard dimension {key!r}")
    return True


def build_table(rule_name, rule):
    """Partial evaluation: run the dispatch contract over every reachable context."""
    slots = rule["slots"]
    specific = [s for s in slots if s.get("guard")]
    fallbacks = [s for s in slots if not s.get("guard")]
    if len(fallbacks) > 1:
        raise Unsupported("more than one empty-guard slot")

    # A finite context dimension widens the index instead of forcing the code back end.
    stochastic = any("random" in s.get("guard", {}) for s in slots)
    contexts = [{"random": v} for v in RANDOM_VALUES] if stochastic else [{}]

    table, diagnostics = [], []
    for ctx in contexts:
        for state in range(16):
            hits = [s for s in specific if guard_matches(state, s["guard"], ctx)]
            if len(hits) > 1:
                # dispatch_contract.tie == error
                raise Unsupported(
                    f"tie on state {state:04b}: {len(hits)} slots match "
                    f"({[h['guard'] for h in hits]})"
                )
            if hits:
                chosen = hits[0]
            elif fallbacks:
                chosen = fallbacks[0]
            else:
                raise Unsupported(f"totality violated: state {state:04b} matches no slot")
            table.append(apply_emission(state, chosen["emit"]))

    # dispatch_contract.reversibility_test — read the slot set as a function, check bijection.
    is_bijection = sorted(table) == list(range(16))
    declared = rule.get("reversible")
    if isinstance(declared, bool) and declared != is_bijection:
        diagnostics.append(
            f"DECLARED reversible={declared} but table {'IS' if is_bijection else 'IS NOT'} a bijection"
        )

    # Conservation laws, verified over the whole table rather than asserted.
    for law in rule.get("conserves", []):
        if law == "population":
            bad = [s for s in range(16) if popcount(table[s]) != popcount(s)]
            if bad:
                diagnostics.append(f"declared conserves population, violated on {len(bad)} states")
        elif law == "arrangement":
            bad = [s for s in range(16) if orbit_labels(table[s]) != orbit_labels(s)]
            if bad:
                diagnostics.append(f"declared conserves arrangement, violated on {len(bad)} states")
        else:
            # A checker that silently accepts what it cannot check is worse than no checker.
            diagnostics.append(f"UNVERIFIED: declared conserves {law!r}, no checker for it")

    inverse = None
    if is_bijection:
        inverse = [0] * 16
        for s, d in enumerate(table):
            inverse[d] = s

    return {
        "name": rule_name,
        "what": rule.get("what", ""),
        "group": str(rule.get("group", "")),
        "table": table,
        "inverse": inverse,
        "bijection": is_bijection,
        "declared_reversible": declared,
        "conserves": rule.get("conserves", []),
        "diagnostics": diagnostics,
        "identity": table == list(range(16)),
    }


def emit_kernel(c):
    """Emit a scan loop specialized to this rule. An identity table emits no loop at all."""
    if c["identity"]:
        return (
            f"// {c['name']}: table is the identity permutation — kernel elided by the specializer.\n"
            f"export function step_{c['name']}(g, w, h, phase) {{ /* nothing to do */ }}\n"
        )
    return f"""export const TABLE_{c['name']} = Uint8Array.from({json.dumps(c['table'])});
export function step_{c['name']}(g, w, h, phase) {{
  const o = phase & 1;
  for (let by = 0; by < h; by += 2) {{
    for (let bx = 0; bx < w; bx += 2) {{
      const x0 = (bx + o) % w, y0 = (by + o) % h;
      const x1 = (x0 + 1) % w, y1 = (y0 + 1) % h;
      const iNW = y0 * w + x0, iNE = y0 * w + x1, iSE = y1 * w + x1, iSW = y1 * w + x0;
      const s = g[iNW] | (g[iNE] << 1) | (g[iSE] << 2) | (g[iSW] << 3);
      const d = TABLE_{c['name']}[s];
      g[iNW] = d & 1; g[iNE] = (d >> 1) & 1; g[iSE] = (d >> 2) & 1; g[iSW] = (d >> 3) & 1;
    }}
  }}
}}
"""


def main():
    spec = yaml.safe_load(SPEC.read_text())
    rules = spec["rules"]

    compiled, skipped = [], []
    for name in COMPILABLE:
        try:
            compiled.append(build_table(name, rules[name]))
        except Unsupported as e:
            skipped.append((name, str(e)))
    for name, rule in rules.items():
        if name not in COMPILABLE:
            skipped.append((name, "not attempted — see FINDINGS.md"))

    parts = [
        "// GENERATED by compile.py from ../../examples/margolus-rules.yml — do not edit.\n",
        f"// {len(compiled)} rules compiled, {len(skipped)} skipped.\n\n",
    ]
    for c in compiled:
        parts.append(f"// {c['name']}: {c['what']}  [group {c['group']}]\n")
        parts.append(emit_kernel(c))
        if c["inverse"]:
            parts.append(
                f"export const INVERSE_{c['name']} = Uint8Array.from({json.dumps(c['inverse'])});\n"
            )
            parts.append(
                f"""export function unstep_{c['name']}(g, w, h, phase) {{
  const o = phase & 1;
  for (let by = 0; by < h; by += 2) {{
    for (let bx = 0; bx < w; bx += 2) {{
      const x0 = (bx + o) % w, y0 = (by + o) % h;
      const x1 = (x0 + 1) % w, y1 = (y0 + 1) % h;
      const iNW = y0 * w + x0, iNE = y0 * w + x1, iSE = y1 * w + x1, iSW = y1 * w + x0;
      const s = g[iNW] | (g[iNE] << 1) | (g[iSE] << 2) | (g[iSW] << 3);
      const d = INVERSE_{c['name']}[s];
      g[iNW] = d & 1; g[iNE] = (d >> 1) & 1; g[iSE] = (d >> 2) & 1; g[iSW] = (d >> 3) & 1;
    }}
  }}
}}
"""
            )
        parts.append("\n")

    meta = {
        c["name"]: {
            k: c[k]
            for k in ("bijection", "declared_reversible", "conserves", "diagnostics", "identity")
        }
        for c in compiled
    }
    parts.append(f"export const META = {json.dumps(meta, indent=2)};\n")
    parts.append(
        "export const RULES = {\n"
        + "".join(
            f"  {c['name']}: {{ step: step_{c['name']}, "
            f"unstep: {'unstep_' + c['name'] if c['inverse'] else 'null'} }},\n"
            for c in compiled
        )
        + "};\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(parts))

    print(f"compiled {len(compiled)} rules -> {OUT.relative_to(HERE)}")
    for c in compiled:
        flags = []
        flags.append("bijection" if c["bijection"] else "NOT-bijection")
        if c["conserves"]:
            flags.append("conserves " + "+".join(c["conserves"]))
        print(f"  {c['name']:20s} {', '.join(flags)}")
        for d in c["diagnostics"]:
            print(f"      !! {d}")
    print("\nskipped:")
    for name, why in skipped:
        print(f"  {name:20s} {why}")

    # Fusion check: composing a rule with its own inverse must yield the identity table,
    # which the specializer then elides. This is the monoid claim, mechanically checked.
    print("\nfusion (rule then inverse):")
    for c in compiled:
        if not c["inverse"]:
            continue
        fused = [c["inverse"][c["table"][s]] for s in range(16)]
        print(f"  {c['name']:20s} {'identity -> kernel elided' if fused == list(range(16)) else 'NOT identity'}")


if __name__ == "__main__":
    sys.exit(main())
