# 🎷 YAML Jazz

> YAML is sheet music. The LLM is the jazz musician. Comments are soul.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Core MOOLLM principle |
| [postel/](../postel/) | Liberal interpretation of ambiguous YAML |
| [mind-mirror/](../mind-mirror/) | Personality as YAML Jazz (numbers + comments = life) |
| [needs/](../needs/) | Dynamic comments as character inner voice |
| [sniffable-python/](../sniffable-python/) | YAML Jazz applied to Python comments |
| [empathic-templates/](../empathic-templates/) | Semantic understanding of YAML |
| [files-as-state/](../plain-text/) | YAML IS the state format |
| [k-lines/](../k-lines/) | Comments activate conceptual clusters |
| [character/](../character/) | Character state in YAML |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

**YAML Jazz** is registered in **`schema`** (schemapedia) as mechanism **`yaml-jazz`** under family **notation**—a first-class **schema plugin** alongside interchange and causal entries. Pair with JSON Schema when you need validated **tree** plus comment-rich **source**.

**YAML Jazz** is how MOOLLM treats structured data: not as rigid schemas, but as **semantic improvisation** where:

- **Structure carries meaning** — indentation, ordering, grouping
- **Comments ARE data** — they're guidance, context, soul
- **The LLM interprets** — filling gaps, resolving ambiguity
- **Schemas are suggestions** — starting points, not prisons

## Comments Matter

```yaml
# CRITICAL: Do not modify without user approval
api_key: ${SECRET}

hunger: 3  # Getting peckish. Is that pie?
           # ← This comment IS the character's inner voice
```

The LLM reads these. Acts on them. **Comments are instructions.**

## Core Principle

> No decorative `----` or `====` line comments — they waste tokens!

This is a **kernel-level directive**.

## Standards, dialects, and lenses

YAML Jazz sits on top of the **YAML spec** (1.1 / 1.2 in the wild) and whatever **domain pack** you use (Kubernetes, Actions, MOOLLM skills, …). The skill file is the **source of truth** for humans and LLMs; many parsers strip comments on load, so preserve the text or use round-trip tooling when machines rewrite files.

**Comments** use full-line `#` blocks for narrative and **end-of-line** `#` for field-local gloss. Both are semantic.

**Documentation by example:** the YAML instance teaches usage; comments add intent, guardrails, and counterexamples.

**Parallel copies:** the same key–value tree can appear in multiple files, each with a different **lens** (intent, validation, metrics, history). See [examples/lens-intent.yml](examples/lens-intent.yml) and [examples/lens-validation.yml](examples/lens-validation.yml), and [SKILL.md](SKILL.md) for the full protocol.

