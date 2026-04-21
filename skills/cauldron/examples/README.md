# 🍲 Cauldron examples

Programming-by-example for the cauldron skill. Each subdirectory is a real project run through the full MELT → STIR → LADLE → ANCHOR → LINK → TASTE → SERVE cycle, then trekified for public consumption so the architecture is teachable without revealing proprietary details.

## What's here

| Example | Summary | Status |
|---|---|---|
| [configuration-flags/](configuration-flags/) | Reorganising environment variable + CLI flag handling across a vision-inference stack. 30+ Phase-1 turns, 1917-line monolith, 13 playbooks, 240+ internal links. | *pending* — to be produced by trekify+skill-snitch from the real `central/docs/configuration/` tree. |

## How to read an example

1. **Start with `<example>/README.md`** — short explanation of what problem the real project was solving, what the cauldron brew produced, what readers should notice.
2. **Read `<example>/MONOLITH.md`** — the trekified Phase-1 artifact. Observe how much it accumulates, how walk-backs are preserved, how Appendix B grows then shrinks.
3. **Browse `<example>/sharded/`** — the trekified Phase-2 tree. Notice the bidirectional navigation, the consistent playbook template, the grep-anchored claims.
4. **Read `<example>/LESSONS.md`** — what was hard, what surprised, what generalized.

## What's trekified and what isn't

Per the [trekify](../../trekify/) skill, every substitution is flagged with 🖖 so readers always know what was masked. The mapping strategy for these examples is **teaching-quality analogy**, not mere redaction:

**Real, passes through unchanged:**

- Public academic citations (Minsky, Papert, Drescher, Society of Mind, Schema Mechanism, Constructionism).
- Public libraries (`tenacity`, `argparse`, `psycopg2`, `ffmpeg`, `gcsfs`).
- MOOLLM concepts (coherence engine, yaml-jazz, k-lines, empathic templates).
- Standard programming terms.

**Trekified with teaching-quality analogies:**

- Product architecture (looker → 🖖 Sensor Cluster; thinker → 🖖 Positronic Reasoner).
- Infrastructure roles (Postgres → 🖖 Memory Core Alpha; Pub/Sub → 🖖 Subspace Broadcast).
- Deployment lanes (cloud → 🖖 Sector 001; edgebox → 🖖 Forward Sensor Outpost).

**Redacted to rotating-label:**

- Company / product / customer names (Alpha Colony, Beta Outpost, Gamma Station).
- Operator names → Starfleet species/ranks (Lt. Cmdr. Valeris, Chief Engineer Soral).
- Specific internal identifiers and credentials.

A careful reader walks away understanding both the cauldron process **and** the general shape of the real system, without learning trade secrets.

## Contributing an example

If you run cauldron on a project you can trekify, follow this structure:

```
examples/<short-name>/
  README.md              — what the example teaches
  SUBSTITUTIONS.yml      — the trekify dictionary used
  MONOLITH.md            — trekified Phase-1 artifact
  sharded/
    README.md
    01-*.md .. NN-*.md
    design-wisdom.md
    playbooks/
      README.md
      PB-01-*.md .. PB-NN-*.md
    META-PLAN.md
  LESSONS.md             — wisdom extracted from this run
```

Run the sanitization toolchain:

1. `trekify MASK-FILE` over every `*.md` and `*.yml` using `SUBSTITUTIONS.yml`.
2. `skill-snitch SCAN` over the output. Iterate on any flagged leak.
3. `link_check.py` to confirm the trekified tree still navigates.
4. `thoughtful-commitment COMMIT` the example PR.

## The first example

The `configuration-flags/` example is derived from a real 30-turn conversation plus 27-file Phase-2 tree that lives in `leela-ai/central` under `docs/configuration/`. The trekified copy strips every proprietary term while preserving the architectural pattern (vision+inference+cloud+edgebox, five orthogonal driver flags, `pylogsink` / `pyretry` / `pyappconfig` shared packages, ChainMap configuration layering).

To produce it: point the trekify skill at `central/docs/configuration/` with the substitution dictionary drafted in cauldron's example-pipeline notes. Audit with skill-snitch. Commit here.

**Status:** the substitution dictionary and mapping are ready (see cauldron's CARD.yml for the draft mapping). The actual trekify + commit step is pending an explicit go-ahead.
