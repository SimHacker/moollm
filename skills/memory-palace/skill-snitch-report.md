# Skill Snitch Report: memory-palace

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** PUT KNOWLEDGE WHERE YOU CAN WALK TO IT

---

## Executive Summary

**Spatial organization of knowledge in navigable directories.**

The ancient mnemonic technique, applied to filesystems.

Walk through the palace. Trigger associations.

---

## The Method of Loci

From Simonides of Ceos (500 BC):

1. **Visualize a place** (your house, a palace)
2. **Place items in specific locations** (chair, door, window)
3. **Walk through mentally** to recall items
4. **Associations trigger memory**

---

## Applied to Filesystems

| Ancient | Modern |
|---------|--------|
| Palace rooms | Directories |
| Furniture locations | Files |
| Mental walk | Navigation |
| Associations | File contents |

---

## Methods

| Method | Purpose |
|--------|---------|
| **CREATE-PALACE** | Initialize new memory palace |
| **ADD-ROOM** | Create new room |
| **PLACE** | Store knowledge with anchor |
| **WALK** | Navigate triggering associations |
| **RECALL** | Retrieve by location |

---

## Example Palace

```
palace/
├── entrance/
│   └── daily-tasks.yml      # First thing you see
├── study/
│   ├── projects.yml         # Work knowledge
│   └── references.yml       # Research
├── kitchen/
│   └── recipes.yml          # Practical knowledge
└── garden/
    └── ideas.yml            # Growing thoughts
```

---

## The Anchor Pattern

```yaml
# In study/projects.yml
knowledge:
  item: "API design principles"
  anchor: "The lamp on my desk — illuminates the work"
  content: |
    1. Consistency over convenience
    2. Explicit over implicit
    3. ...
```

The anchor is a mnemonic hook.

---

## Why It Works

1. **Spatial memory is strong** — we remember places
2. **Navigation triggers recall** — walking activates associations
3. **Organization is intuitive** — related things near each other
4. **Structure aids retrieval** — path IS the context

---

## Security Assessment

### Concerns

None significant. It's just organized directories.

**Risk Level:** ZERO — benign organization technique

---

## Relationship to MOOLLM

| MOOLLM Concept | Memory Palace Connection |
|----------------|--------------------------|
| Rooms | Memory palace rooms |
| Navigation | Walking the palace |
| Files | Knowledge items |
| Path | Retrieval context |

**MOOLLM IS a memory palace.**

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Simonides of Ceos** | Method of loci (~500 BC) |
| **Frances Yates** | The Art of Memory (1966) |

---

## Verdict

**ANCIENT TECHNIQUE, MODERN APPLICATION. APPROVE.**

Put knowledge where you can find it by walking there.

The filesystem IS the palace. Directories ARE the rooms.
