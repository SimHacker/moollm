# Skill Snitch Report: advertisement

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE SIMS SECRET SAUCE

---

## Executive Summary

**Objects announce what they can do — The Sims style.**

> "Objects don't wait to be used — they announce what's possible."

This is how The Sims enabled infinite expansion without code changes.

---

## The Core Insight

Traditional interaction: **Player → Object → Action**
Advertisement pattern: **Object → Broadcast → Player selects**

Objects self-describe. Players choose from what's offered.

---

## Advertisement Schema

```yaml
advertisements:
  PROVIDE-LIGHT:
    action: "LIGHT"
    description: "Illuminate the room"
    score: 90
    score-if: "room.dark"
    preconditions: ["has_oil"]
    satisfies: ["light", "safety"]
```

---

## Methods

| Method | Purpose |
|--------|---------|
| **SCAN** | Collect all ads from current room |
| **SHOW** | Display what an object advertises |
| **SELECT** | Choose an advertised action |
| **EVALUATE** | Score ads against character needs |

---

## AMBIENT Advertisement

Special type for skills that should be "in the air":

```yaml
AMBIENT:
  score: 100
  condition: always
  scope: session
  resolution: card-only
```

Like air filters — always cleaning, no explicit invocation.

---

## Scope Options

| Scope | Duration |
|-------|----------|
| session | Entire session |
| conversation | Current conversation |
| room | While in this room |
| card-only | Just the CARD |

---

## Resolution Options

| Resolution | What Loads |
|------------|------------|
| full | Everything |
| summary | SKILL.md only |
| sniff | First 50 lines |
| card-only | Just CARD.yml |

---

## Why The Sims Pattern Worked

| Feature | Benefit |
|---------|---------|
| **User-created objects** | Anyone makes new items |
| **Expansion packs** | Drop in, no code changes |
| **Self-describing** | Objects define their own behaviors |
| **Infinite variety** | Community millions of objects |

---

## MOOLLM Parallel

| Sims | MOOLLM |
|------|--------|
| Object definitions | YAML files |
| Expansion packs | New skills/objects |
| No code changes | LLM reads descriptions |
| Community content | Shared object definitions |

---

## Pie Menu Integration

> "Advertisements naturally map to pie menus."

Click object → ads become slices → sorted by score → highest at top.

Don Hopkins' pie menus meet Will Wright's advertisements.

---

## Score Dynamics

| Factor | Effect |
|--------|--------|
| Base score | Starting priority |
| score-if | Conditional modifier |
| Needs | Low hunger → food ads score higher |
| Context | Room state affects scores |

---

## Security Assessment

### Concerns

1. **Score manipulation** — artificially high scores
2. **Precondition bypass** — skip guards
3. **Effect injection** — malicious ad effects

### Mitigations

- Scores are visible
- Preconditions evaluated
- Effects sandboxed

**Risk Level:** LOW — transparent, auditable

---

## Design Decision: AMBIENT in CARD

**Considered:** Separate AMBIENT.yml file with smart orchestrator.

**Rejected because:**
- Requires orchestrator we don't control (Cursor, Claude Code)
- CARD.yml already serves as sniffable interface
- Adds complexity without runtime support

**Pragmatic solution:**
1. Declare AMBIENT in CARD.yml
2. Manual hot list in `.moollm/hot.yml`
3. Resolution field declares how much to page in
4. Trust the LLM

---

## Verdict

**THE SECRET SAUCE. APPROVE.**

This is why The Sims could have infinite expansion:

1. Objects self-describe
2. No code changes needed
3. Community creates content
4. System just works

Will Wright's greatest insight: **let the objects advertise**.
