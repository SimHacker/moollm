---
name: knowledge-frames
description: Minsky frames, Drescher schemas, interchange registry, and MOOLLM K-lines — distinct layers.
allowed-tools: [read, grep, glob]
---

# Knowledge Frames — Layers

Several ideas get called “schema” or “frame” in the wild. This skill keeps them **separate** so MOOLLM skills can point at the right layer.

## Part of MOOLLM

See [skills/README.md](../README.md) and the repo [README](../../README.md).

## 1. Minsky frames (situation shape)

**What:** A **frame** is a structured expectation about a kind of situation: named slots, default fillers, hooks for exceptions. Restaurant, birthday party, debugging session.

**Job:** Answer “what kind of situation is this?” and “what pieces usually belong?”

**Not:** A causal learning unit (that’s Drescher). Not a protocol activation symbol (that’s K-lines).

**In MOOLLM:** Use **frame** when you mean **slot structure** or default script for a situation. YAML Jazz directory listings and CARD layouts often act as lightweight frames (“what’s here?”).

## 2. Drescher schemas (causal units)

**What:** `Context → Action → Result` — a **learned** causal unit. See `schema-mechanism`.

**Job:** Answer “what tends to happen when I do X in context Y?”

**Not:** Interchange validation (JSON Schema, XSD, RELAX NG, …). Not Minsky’s frame slots.

## 3. Interchange schema registry (wire shapes)

**What:** A **named mechanism** for valid serialized data: JSON Schema, Zod, RELAX NG, W3C XML Schema (XSD), and others registered under `schema`. Nomenclature, docs, libraries, and **gateways** between mechanisms live there.

**Job:** Answer “which validation/interchange language applies?” and “how do we translate or bridge to another stack?”

**Not:** Drescher learning. Not frame slots alone.

## 4. K-lines / protocol symbols (activation bundles)

**What:** A **symbol** that, when used in a shared culture (`PROTOCOLS.yml`, `INDEX.yml`, prior turns), **re-loads a competent stance**: which sub-skills, tone, and checks to run.

**Job:** Answer “which bundle of competence do we turn on **now**?”

**Not:** Static slot templates alone (frames). Not the Drescher learning loop.

**Henry Minsky phrasing:** Often a **whole scene or stance**, not only a pointer—closer to re-entering a closure than to naming a fact.

## Quick comparison

| Layer | Question it answers | Primary skill |
|--------|---------------------|---------------|
| Frame | What shape is this situation? | This skill + yaml-jazz |
| Drescher schema | What causal unit fired? | schema-mechanism |
| Interchange schema | What wire format is valid? Which mechanism? | schema (registry) |
| K-line | What bundle to activate? | k-lines |

## Related

- `k-lines` — protocol symbols and activation
- `schema-mechanism` — Drescher, predictive schemas
- `schema` — **schemapedia**: registry of all schema senses (interchange, Drescher, frames, K-lines, SoM, SQL/SQLite); this skill’s theory for frames is still the home for *what a frame is*
- `empathic-templates` — slots for stance and empathy

## Credits

Marvin Minsky (*Society of Mind*), Gary Drescher (*Good and Real*), MOOLLM protocol layer.

---

## Standard metadata

**License:** MIT

**Tags:** minsky, drescher, frames, schemas, k-lines, philosophy

**Related skills:** k-lines, schema-mechanism, schema, yaml-jazz, empathic-templates
