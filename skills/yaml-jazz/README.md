# YAML Jazz

> *"YAML is sheet music. The LLM is the jazz musician. Comments are soul."*

---

## What Is It?

**YAML Jazz** is how MOOLLM treats structured data: not as rigid schemas, but as **semantic improvisation** where:

- **Structure carries meaning** — indentation, ordering, grouping
- **Comments ARE data** — they're guidance, context, soul
- **The LLM interprets** — filling gaps, resolving ambiguity, inferring intent
- **Schemas are suggestions** — starting points, not prisons

```yaml
# This comment is NOT ignored!
# It tells the LLM: "be gentle with this section"
user_preferences:
  theme: dark    # they mentioned eye strain
  font_size: 16  # ← bump this if they complain again
```

---

## Core Principles

### Comments Matter

```yaml
# CRITICAL: Do not modify without user approval
api_key: ${SECRET}

# TODO: migrate to new format after v2 launch
legacy_format: true  # keeping for backwards compat
```

The LLM reads these. Acts on them. **Comments are instructions.**

### Structure Is Semantic

```yaml
# Priority by position (first = most important)
tasks:
  - Fix authentication bug     # P0
  - Update documentation       # P1  
  - Refactor old module        # P2
```

Order matters. Grouping matters. Proximity implies relationship.

### Improvise Within Constraints

Given incomplete data:

```yaml
user:
  name: Alice
  # preferences unknown
```

The LLM can improvise reasonable defaults while noting uncertainty:

```yaml
user:
  name: Alice
  preferences:        # inferred from context
    theme: light      # default, unconfirmed
    notifications: on # assumed
```

---

## The Jazz Metaphor

| Jazz | YAML Jazz |
|------|-----------|
| Sheet music | Schema / template |
| Chord changes | Required fields |
| Improvisation | LLM interpretation |
| Soul | Comments |
| Ensemble | Multiple agents |
| Standards | Protocol conventions |

Like John Coltrane playing "My Favorite Things" — the structure is there, but every performance is unique, responsive, alive.

---

## When to Use

- **Configuration files** — comments explain why, not just what
- **State files** — annotations track history and intent  
- **Data exchange** — structured enough to parse, loose enough to extend
- **Human-LLM collaboration** — both can read and write it

---

## Anti-Patterns

❌ **Rigid schema enforcement** — "field X is required" without context  
❌ **Stripping comments** — losing the soul  
❌ **Machine-only YAML** — if humans can't read it, use JSON  
❌ **Over-specification** — killing the jazz

---

## Dovetails With

- [BPIP](../bpip/) — Best Possible Interpretation of ambiguous YAML
- [Coherence Engine](../coherence-engine/) — LLM as interpreter
- [Soul Chat](../soul-chat/) — Markdown with embedded YAML Jazz
- [Room](../room/) — ROOM.yml files are YAML Jazz

---

## Protocol Symbol

```
YAML-JAZZ
```

Invoke when: Interpreting YAML semantically, not just syntactically.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#YAML-JAZZ)
