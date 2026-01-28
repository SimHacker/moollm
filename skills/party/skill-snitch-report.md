# Skill Snitch Report: party

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** NO HERO SUCCEEDS ALONE

---

## Executive Summary

**Companions and group dynamics — relationships within the group.**

Manage characters traveling together. Track composition, inter-party relationships, shared resources, and group dynamics.

---

## The Core Pattern

```yaml
party:
  name: "The Fellowship"
  members:
    - characters/don-hopkins/
    - characters/palm/
    - characters/rocky/
  leader: characters/don-hopkins/
  location: pub/
  shared-inventory:
    - gold: 500
    - rope
  inter-party-relationships:
    don-palm: 85  # Close friends
    don-rocky: 70  # Good friends
    palm-rocky: 50  # Neutral
```

---

## Methods

| Method | Purpose |
|--------|---------|
| **FORM** | Create a new party |
| **JOIN** | Add character to party |
| **LEAVE** | Remove character from party |
| **STATUS** | Show composition and state |
| **SPLIT** | Divide into sub-parties |
| **REUNITE** | Merge split parties |

---

## Party State

| Field | Purpose |
|-------|---------|
| name | Party identity |
| members | Character references |
| leader | Who makes decisions |
| location | Where party is (as a unit) |
| shared-inventory | Items held by party, not individuals |
| inter-party-relationships | How members feel about each other |

---

## Split/Reunite

Parties can divide:

```
Fellowship
    │
    └── SPLIT
         ├── Group A (Don, Palm)
         │   └── location: basement/
         └── Group B (Rocky)
             └── location: pub/
```

And merge back:

```
REUNITE → Fellowship restored
```

---

## Inter-Party Relationships

Separate from character-to-world relationships:

```yaml
inter-party-relationships:
  don-palm: 85    # Long-standing friendship
  don-rocky: 70   # Newer friendship
  palm-rocky: 50  # Haven't bonded yet
```

Party dynamics affect:
- Who listens to whom
- Conflict resolution
- Group decision-making

---

## Shared Inventory

Items owned by the party, not individuals:

```yaml
shared-inventory:
  - gold: 500        # Party funds
  - healing-potions: 3
  - map-to-treasure
```

Different from:
- Individual inventory (belongs to one character)
- Room contents (belongs to location)

---

## Security Assessment

### Concerns

1. **Member manipulation** — forced joins/leaves
2. **Inventory theft** — take from shared
3. **Split abuse** — leave someone behind

### Mitigations

- Player controls party actions
- Shared inventory visible
- Reunite always possible

**Risk Level:** LOW — standard RPG mechanic

---

## Why Parties Matter

| Solo | Party |
|------|-------|
| One perspective | Multiple perspectives |
| One skill set | Complementary skills |
| Lonely | Social dynamics |
| Simple | Emergent behavior |

Parties create drama. Relationships create story.

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **RPG parties** | The original concept |
| **The Sims** | Household management |

---

## Verdict

**ESSENTIAL GROUP MECHANIC. APPROVE.**

No hero succeeds alone. Parties create:
- Shared goals
- Internal conflict
- Emergent relationships
- Division of labor

Simple but essential.
