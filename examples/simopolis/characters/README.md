# Simopolis Citizens

**Every Sim a citizen. Every citizen a person.**

This directory contains all imported and created Sims living in Simopolis. Each character has the full MOOLLM character structure: CHARACTER.yml (the soul), CARD.yml (the interface), GLANCE.yml (the quick scan), and README.md (the deep story).

## Citizen Registry

### The Newbie Family
*Source: Export/Newbie_1.FAM — Tutorial family, Lot 1*

| Citizen | Traits (N/O/A/P/Ni) | Career | Status |
|---------|---------------------|--------|--------|
| [Bob Newbie](./bob-newbie/) | 4/8/4/3/6 | Unemployed | Tutorial survivor |
| [Betty Newbie](./betty-newbie/) | 8/3/6/3/5 | Unemployed | The capable one |

### The Goth Family
*Source: Export/Goth_5.FAM — Lot 5, the mansion on the hill*

| Citizen | Traits (N/O/A/P/Ni) | Career | Status |
|---------|---------------------|--------|--------|
| [Mortimer Goth](./mortimer-goth/) | 7/3/2/3/5 | Science | Grieving patriarch |
| [Bella Goth](./bella-goth/) | 5/8/7/3/2 | — | Missing |
| [Cassandra Goth](./cassandra-goth/) | 5/5/5/5/5 | — | Child, observer |

### Singles
*Various sources — the unattached citizens of Simopolis*

| Citizen | Traits (N/O/A/P/Ni) | Career | Status |
|---------|---------------------|--------|--------|
| [Don Lothario](./don-lothario/) | 3/9/6/5/2 | — | Charming someone |

## Character File Structure

Every citizen's directory contains:

```
character-name/
├── CHARACTER.yml    # Full character definition (the soul)
│                    #   inherits, ontology, character, sims, mind_mirror,
│                    #   relationships, incarnation
├── CARD.yml         # Interface card (the handshake)
│                    #   name, id, tagline, type, files
├── GLANCE.yml       # Quick scan (5 seconds)
│                    #   name, traits, location, vibe
└── README.md        # Deep story (the biography)
```

## Personality Systems

### Sims Traits (0-10 scale, total 25 points)
- **N**eat: sloppy ↔ neat
- **O**utgoing: shy ↔ outgoing
- **A**ctive: lazy ↔ active
- **P**layful: serious ↔ playful
- **Ni**ce: grouchy ↔ nice

### Mind Mirror (0-7 scale, Leary's Four Thought Planes)
Synthesized from Sims traits during Uplift. The mapping is documented in each CHARACTER.yml with YAML Jazz comments explaining the reasoning.

### Needs (dynamic, decay over time)
hunger, comfort, hygiene, bladder, energy, fun, social, room — just like The Sims, but with inner voice commentary.

## Creating New Citizens

Use the [blank Sim template](../exchange/templates/blank-sim.yml) or let the LLM generate a character from a description.

## Importing From Save Files

Use the [Exchange](../exchange/) to uplift `.FAM` or `.iff` files into full citizens.

## See Also

- [Sims Stats reference](../../../skills/mind-mirror/SIMS-STATS.yml) — Complete trait/skill/need data model
- [Mind Mirror](../../../skills/mind-mirror/CARD.yml) — Leary personality system
- [Zodiac](../../../skills/mind-mirror/ZODIAC.yml) — Zodiac computation from traits
- [Templates](../exchange/templates/) — Blank Sim and family templates
