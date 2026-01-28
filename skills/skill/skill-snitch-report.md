# Skill Snitch Report: skill

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** DOCUMENTATION THAT LEARNED TO DO THINGS

---

## Executive Summary

**The meta-skill for creating, understanding, and debugging skills.**

> "A skill is documentation that learned to do things."

Every skill you encounter was forged here.

---

## MOOLLM's Eight Extensions

| # | Extension | Description |
|---|-----------|-------------|
| 1 | **Instantiation** | Skills as prototypes that create instances |
| 2 | **Three-Tier Persistence** | Platform → Narrative → State |
| 3 | **K-lines** | Names as semantic activation vectors |
| 4 | **Empathic Templates** | Smart generation, not string substitution |
| 5 | **Speed of Light** | Many turns in one call |
| 6 | **CARD.yml** | Machine-readable interface with advertisements |
| 7 | **Ethical Framing** | Room-based inheritance of performance context |
| 8 | **Ambient Skills** | Always-on behavioral shaping |

---

## Methods

| Method | Signature |
|--------|-----------|
| **CREATE** | `CREATE [name] (tier) (prototypes)` |
| **INSTANTIATE** | `INSTANTIATE [skill] AT [location]` |
| **DEBUG** | `DEBUG [skill-path]` |
| **UPGRADE** | `UPGRADE [skill] TO [tier]` |
| **LIFT** | `LIFT [pattern] AS [name]` |
| **COMPOSE** | `COMPOSE [skills] AS [name]` |

---

## Directories as Interests

| Principle | Description |
|-----------|-------------|
| **ls IS the index** | Directory listings are semantic indices |
| **Big-endian naming** | Most significant component FIRST |
| **Filenames as K-lines** | Well-written names are LLM-recognizable |

```
✓ 2026-01-24-description.yml   (date groups by time)
✓ RUN-001-name.yml             (number groups by sequence)
✗ example1.yml                  (not semantic)
```

---

## Hierarchical Skills

```
skills/experiment/              # The skill (prototype)
├── CARD.yml
├── SKILL.md
└── experiments/
    └── fluxx-chaos/           # An experiment INSTANCE
        ├── EXPERIMENT.yml
        └── runs/
            └── amsterdam-flux/ # A run INSTANCE
                ├── RUN.yml
                ├── RUN-000.yml
                └── RUN-001.yml
```

The path IS the activation context.

---

## Ambient Skills

Skills that should be "in the air":

```yaml
advertisements:
  AMBIENT:
    score: 100
    condition: always
    scope: session
    resolution: card-only
```

Like air filters — always cleaning.

---

## Files in a Skill

| File | Purpose |
|------|---------|
| CARD.yml | Sniffable interface |
| SKILL.md | Full protocol |
| README.md | Human landing page |
| *.yml.tmpl | Templates |

---

## Security Assessment

### Concerns

1. **Skill creation** — can create any capability
2. **Instantiation** — creates files
3. **Tier escalation** — upgrade to higher capabilities

### Mitigations

- All skills visible
- Tiers explicit
- Templates reviewed

**Risk Level:** MEDIUM — powerful but transparent

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Self language** | Prototype inheritance |
| **Marvin Minsky** | Society of Mind, K-lines |
| **Seymour Papert** | Constructionism |

---

## Verdict

**THE META-SKILL. APPROVE.**

Every skill is forged here. The skill skill is how skills work.

Documentation that learned to do things.
