# Skill Snitch Report: NAMING-RELATIONSHIPS

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** TWO-WAY COMMUNICATION CHANNELS

---

## Executive Summary

**K-lines connect ideas. Two-way references are communication channels.**

But relationships have DIRECTION and CONSTRAINTS. Comment each side.

---

## The Core Insight

When A references B and B references A, that's not just links — it's a **bidirectional relationship** with semantics.

```
skills/no-ai-slop ←————————→ skills/yaml-jazz
                   tube
```

The "tube" has rules. Document them.

---

## Relationship Types

| Type | Direction | Example |
|------|-----------|---------|
| **uses** | A → B | "no-ai-slop uses yaml-jazz format" |
| **example** | B ← A | "yaml-jazz references no-ai-slop as example" |
| **exit** | A ↔ B | "pub ↔ coatroom" (symmetric) |
| **carries** | A → B | "postal carries beads" (one-way) |
| **dependency** | A → B | "Core dependency — required" |
| **soft reference** | A ··· B | "Reference only — not required" |

---

## Annotated Relationships

```yaml
see-also:
  - skills/bead        # Reference only — yaml-jazz does not require beads
  - skills/postel      # Core dependency — robustness principle
  - kernel/postal      # One-way — yaml-jazz can be sent via postal
```

The comment documents the relationship type:
- "Reference only" = soft link
- "Core dependency" = hard link
- "One-way" = directional constraint

---

## Rich Annotation Example

```yaml
see-also:
  - skills/bead        
    # Beads are a prominent YAML Jazz example
    # but this skill does NOT depend on beads
    # yaml-jazz is the paradigm, beads are one instantiation
    # 
    # WHY THIS MATTERS:
    # Without this annotation, an LLM might think:
    #   "yaml-jazz requires beads" (WRONG)
    #   "I must load bead skill to use yaml-jazz" (WRONG)
    #   "yaml-jazz is about beads" (WRONG — beads are ONE example)
    #
    # With this annotation, the LLM understands:
    #   "beads demonstrate yaml-jazz, but don't define it"
```

---

## Common Relationship Patterns

### Parent-Child
```
skills/skill → skills/prototype
  # skill inherits from prototype philosophy
```

### Consumer-Producer
```
skills/needs ← skills/advertisement
  # needs drives advertisement scoring
  # advertisement satisfies needs
```

### Mentor-Mentee
```
skills/play-learn-lift → skills/constructionism
  # play-learn-lift is the methodology
  # constructionism is the philosophy behind it
```

### Sibling
```
skills/cat ↔ skills/dog
  # Both are companions
  # Contrasting philosophies
  # Neither depends on other
```

### Implementation-Specification
```
skills/cursor-mirror → skills/skill-snitch
  # cursor-mirror provides runtime surveillance
  # skill-snitch uses it for auditing
```

---

## Pneumatic Tube Metaphor

Two-way K-lines are like pneumatic tubes:

```
skills/A ←————tube————→ skills/B
```

But tubes can have RULES:
- "No food in this tube"
- "One-way — sender cannot receive reply"
- "Priority — urgent messages first"
- "Filtered — only beads, not raw messages"

---

## Tiered Resolution

| Tier | Location | Detail Level |
|------|----------|--------------|
| 1 | CARD.yml advertisements | Brief, activation-focused |
| 2 | SKILL.md see-also | Important relationships with comments |
| 3 | README.md K-Lines table | Full explanation with why column |

Match detail to tier. Don't bloat the CARD.

---

## All Relationship Types Found in MOOLLM

### Structural
| Relationship | Example | Semantics |
|--------------|---------|-----------|
| **inherits** | character → prototype | Delegation chain |
| **contains** | room → object | Spatial containment |
| **points-to** | exit → room | Navigation edge |
| **member-of** | character → party | Group membership |

### Behavioral
| Relationship | Example | Semantics |
|--------------|---------|-----------|
| **advertises-to** | object → character | Action offering |
| **satisfies** | action → need | Motive fulfillment |
| **suppresses** | agent → agent | Competition inhibition |
| **amplifies** | agent → agent | Competition boost |

### Data Flow
| Relationship | Example | Semantics |
|--------------|---------|-----------|
| **sends-to** | room → room | THROW objects |
| **receives-from** | inbox ← room | RECEIVE objects |
| **transforms** | room → object | Processing |
| **routes** | postal → address | Delivery |

### Identity
| Relationship | Example | Semantics |
|--------------|---------|-----------|
| **wears** | character → persona | Costume on body |
| **tagged-with** | character → ontology | Being-type |
| **observes** | b-brain → a-brain | Self-awareness |

### Epistemological
| Relationship | Example | Semantics |
|--------------|---------|-----------|
| **activates** | k-line → agents | Memory recall |
| **demonstrates** | example → pattern | Learning |
| **instantiates** | instance → template | Creation |

---

## Security Assessment

### Concerns

1. **Relationship ambiguity** — unclear direction
2. **Hidden dependencies** — undocumented hard links
3. **Circular references** — infinite loops

### Mitigations

- Comment every see-also
- Explicit direction in comments
- Tiered resolution

**Risk Level:** LOW — the whole point is to make relationships explicit

---

## Verdict

**RELATIONSHIPS ARE SEMANTIC. APPROVE.**

Links without comments are just pointers. Links WITH comments are **communication channels**.

Document the direction. Document the constraints. Document the why.

The LLM reads the comments. Make them count.
