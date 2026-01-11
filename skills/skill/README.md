# 🛠️ Skill — The Meta-Skill

> **A skill is documentation that learned to do things.**

## MOOLLM K-Lines

| K-Line | Meaning |
|--------|---------|
| [skills-as-prototypes](../prototype/) | Skills are factories that create instances (Self language) |
| [play-learn-lift](../play-learn-lift/) | Explore → Notice patterns → Share as skills |
| [sister-scripts](../sister-script/) | Document → Procedure → Automation |
| [sniffable-code](../sniffable-python/) | LLMs understand from first 50 lines |
| [files-as-state](../plain-text/) | Everything persists in files |
| [speed-of-light](../speed-of-light/) | Many agents, many turns, one LLM call |
| [constructionism](../constructionism/) | Build to learn (Papert) |
| [empathic-templates](../empathic-templates/) | Smart generation, not string substitution |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Interface Card](CARD.yml) — machine-readable methods
- [Delegation Protocol](delegation-object-protocol.md) — Self-like inheritance
- [Instantiation Protocol](skill-instantiation-protocol.md) — how skills become instances

---

## Overview

The meta-protocol: how skills work, evolve, compose, and how **MOOLLM advances the state of the art**.

A skill is a **documented capability** that can be:
- **Instantiated** — Create running instances with state
- **Composed** — Build complex from simple
- **Inherited** — Clone and override (Self-style)
- **Lifted** — Extract patterns into reusable skills

---

## MOOLLM's Unique Contributions

| Innovation | What It Means | Proof |
|------------|---------------|-------|
| **Instantiation** | Skills as prototypes that create instances | adventure-4 from adventure/ |
| **K-lines** | Names activate entire knowledge contexts | "Palm" → all of Palm's soul |
| **Empathic Templates** | Smart generation, not string substitution | Character descriptions |
| **Speed of Light** | Many agents, many turns, one call | **33-turn Fluxx**, **21-turn cat prowl** |
| **Three-Tier Persistence** | Platform → Narrative → State | Session logs + world state |

---

## Skill Anatomy (Required Structure)

```
skills/
  my-skill/
    README.md         # Human entry point (GitHub renders)
    SKILL.md          # Full spec with YAML frontmatter
    CARD.yml          # Machine-readable interface
    *.tmpl            # Templates (optional)
```

Every skill has:
- **README.md** — Human discovery (you're reading one!)
- **SKILL.md** — Full protocol with YAML frontmatter
- **CARD.yml** — Interface: methods, tools, state, advertisements

---

## The Evolution Path

```
Documentation → Procedure → Script → Tool
     ↑              ↑         ↑        ↑
   PLAY           LEARN     LIFT  SISTER-SCRIPT
```

**Play-Learn-Lift**: Do it manually → Notice patterns → Extract skill

---

## Three-Tier Persistence

| Tier | Where | Lifespan |
|------|-------|----------|
| **Platform** | Cursor session | Ephemeral |
| **Narrative** | `LOG.md` data islands | Read-mostly |
| **State** | `*.yml` files | Read-write |

**Key patterns:**
- **Data islands**: Embed YAML in logs with `#object-id` addressing
- **Promotion**: Pop to `.yml` file when editing needed
- **Log inheritance**: `inherits: LOG.md#birth-state`

---

## Front-Matter Sniffing

LLMs can understand skills by reading first ~50 lines:

1. **Lines 1-15**: YAML frontmatter (name, tier, tools)
2. **Lines 16-25**: Purpose and philosophy
3. **Lines 26-40**: File map (what's in the skill)

Efficient discovery without reading everything.

---

## Proven Results

| Demonstration | Turns | Agents | What It Proves |
|---------------|-------|--------|----------------|
| **Stoner Fluxx** | 33 | 8+ | Complex game state, rules, consistency |
| **Cat Prowl** | 21 | 10 | Parallel agents, coordinated behavior |
| **Palm Incarnation** | 1 | 6+ | Committee debate, autonomous creation |

**The architecture works.** Speed-of-light simulation is real.

---

## Related Skills

- [prototype/](../prototype/) — Self-like inheritance
- [play-learn-lift/](../play-learn-lift/) — how skills evolve
- [empathic-templates/](../empathic-templates/) — smart instantiation
- [speed-of-light/](../speed-of-light/) — multi-agent simulation
- [card/](../card/) — skills as playable cards

---

*"Start with jazz, end with standards. But never stop playing."*
