---
# STONE.md — the SEED-BY-EXAMPLE of the STONE skill.
#
# ⬑ CAPTURED CANONICAL EXAMPLE.
#   This is the quintessential INSTANCE the `stone` skill was generalized from.
#   The skill (../SKILL.md) was "read off" THIS file — instance precedes class.
#   Canonical authoring home (private): DonHopkins/characters/stone-librande/STONE.md
#   captured_from: DonHopkins/characters/stone-librande/STONE.md
#
# This file is two things at once:
#   1. A STONE — a quintessential one-page design (its subject: Stone Librande).
#   2. The PROTOTYPE every other STONE clones. The skill is defined BY this
#      concrete instance, not by an abstract class. (See skills/prototype.)
#
# Proposed the prototype way: reify ONE quintessential instance first, then read
# the rules off it. The instance precedes the skill. To make a STONE, clone this.

name: stone
protocol: STONE
kind: skill-seed                 # a skill reified as its own first instance
named_for: stone-librande        # honors Stone Librande's one-page designs (the pun is the point)
tier: stone                      # ladder rung: GLANCE → CARD → DESCRIPTION → STONE → README → full
one_page_rule: "If you only read one page, read this one."

is_a: [stone, skill, prototype]
parents:                         # clone-from-example, not instance-from-class
  - moollm://github/SimHacker/moollm/skills/prototype/
  - moollm://github/SimHacker/moollm/skills/card/
prototype_of: "every other STONE.md — set parents: [ moollm://…/skills/stone/examples/STONE.md ]"

subject: Stone Librande
representation: { protocol: HERO-STORY, consent_level: 3, ethics: "moollm://github/SimHacker/moollm/skills/representation-ethics/" }
quotes_are: "💬 confirmed + sourced only — tribute / K-line, never impersonation"
---

> **This page is a STONE** — and the seed of the STONE skill. It is named after
> **Stone Librande**, whose one-page designs it imitates by *being* one. Clone it to
> make the next STONE; the rules at the bottom are *read off* this example, not
> imposed on it. (Instance first; skill second. That is the prototype way.)

# 🪨 Stone Librande — one page

**Class:** Systemic Game Designer  ·  **Set:** Micropolis Founders  ·  👤 Living
**Known for:** "**One-Page Designs**" (GDC) — distilling a whole system (Diablo III,
Spore, even The Simpsons) onto a single dense, legible page that makes the
relationships visible.

**The discipline (his, in four moves):**

- **Consolidate** — one page, because the first page is the only page most people read.
- **Draw the arrows** — put the relationships *on the page*; the connections become the star.
- **Earn it** — you cannot make the diagram until you actually understand the system.
- **Resist fragmentation** — wikis and design bibles chop a living system into dead pieces.

**Connections (the arrows — a STONE always shows them):**

```
Will Wright ──"make the complex graspable, don't oversimplify"──▶┐
Chaim Gingold ──reverse-diagram lineage─────────────────────────▶┤
                                              🪨 Stone Librande ──┤── one-page designs
                                                                  ├──▶ Don Hopkins — one-page UIs & control panels for Micropolis
                                                                  └──▶ STONE — this very skill / resolution tier (named for him)
```

> 💬 "Diagrams make relationships visible. Words make them invisible." — Stone Librande
>
> 💬 "Why create a document with more than one page if most people only read the first page anyway?" — Stone Librande

**Where a STONE sits in the ladder:**
`GLANCE` (one line) → `CARD` (collectible) → `DESCRIPTION` (a paragraph) →
**`STONE` (one page — you are here)** → `README` (full) → directory / implementation.
Lower tiers tease; the README sprawls; the **STONE is the one page you'd keep.**

---

## The skill, read off the example

A file is a **STONE** when it has the four properties this page just demonstrated:

| Property | …demonstrated here by |
|---|---|
| **One page** | stopping *here* — denser than a `DESCRIPTION`, shorter than a `README` |
| **Relationships are the star** | the arrows block, not just prose |
| **Made from understanding** | you can't draw those arrows without knowing the system |
| **The "read-one-page" view** | it's the tier you'd keep if you could keep only one |

**To make a STONE:** copy this file beside your subject, set
`parents: [ moollm://…/skills/stone/examples/STONE.md ]`, keep the four
properties, and swap in the new subject. The prototype **governs by example, not by
decree** — improve the seed and every clone inherits the improvement.

*Representational portrayal authored by Don Hopkins (tribute / K-line, not impersonation).*
