# Session Log: ACME/Leela Catalog Architecture & Information Systems
## Prototype/Instance Pattern, Product Lifecycle, Corporate Policies

**Player**: Don Hopkins  
**Character**: [`$CHARACTERS/real-people/don-hopkins/`](./)  
**Location**: Lane Neverending (ACME Surplus, Leela Manufacturing)  
**Date**: 2026-01-17  
**Theme**: Information architecture, object systems, corporate contrast

---

## Intent

Restructure catalog/dispenser architecture with prototype/instance pattern, document product lifecycle, establish contrasting corporate policies between ACME and Leela Manufacturing.

---

## Catalog Architecture Overhaul

### Prototype/Instance Pattern

- Moved ACME catalog prototype from `kitchen/` to `street/lane-neverending/w1/acme-catalog.yml` (co-located with dispenser)
- Kitchen catalog became lightweight instance with pointer to prototype
- Characters carry REFs (weightless pointers) in inventory, not full objects
- Dropping a REF creates a tiny pointer file in the room with instance-specific data

### Files Restructured

| File | Role |
|------|------|
| `w1/acme-catalog.yml` | Master prototype (non-portable) |
| `w1/acme-catalog-dispenser.yml` | Dispenses catalog refs, accepts orders |
| `kitchen/acme-catalog.yml` | Instance with annotations ("DO NOT ORDER Rocket Skates") |
| `leela-manufacturing/lobby/leela-catalog.yml` | Leela prototype |
| `leela-manufacturing/lobby/leela-catalog-dispenser.yml` | Indoor dispenser (nicer waiting area) |

---

## Delivery Systems

**ACME Dispenser Options:**
- FREE PICKUP: Wait at dispenser (timing varies: 1-4 turns or "next week")
- ROOM DELIVERY: 5-10 gold, 2-4 turns, delivered anywhere

**Leela Dispenser Options:**
- Same structure, indoor lobby (climate-controlled, seating, coffee)

---

## Product Lifecycle Documentation

Added complete lifecycle to ACME catalog:

```
DISPENSER → CATALOG → PRODUCT → ORDER → BOXING → SHIPPING → 
TRACKING → DELIVERY → UNBOXING → ASSEMBLING → CONFIGURING → USING
```

For special products (Monkey's Paw):

```
ACTIVATION → MATERIALIZATION → CONTRACT → INCARNATION
```

---

## Corporate Policy Contrast

### ACME Policy

> NO REFUNDS! NO RETURNS! NO REPAIRS! NO EXCHANGES! NO WARRANTY! NO SHIT!

**Fine Print:**
- Visible fragments: "...irrevocable...", "...soul transfer...", "...firstborn...", "...the coyote clause...", "...works for them, not for you...", "...customer's own hubris..."
- Final line: "Meep meep."
- Does NOT acknowledge Leela exists ("roadrunner propaganda")

### Leela Policy

- Full refunds, repairs, warranty, exchanges
- Honest transparent scientifically accurate disclaimers
- Physics compliance warnings (product warps space-time, contains 85M tons TNT equivalent, 99.9999999999% empty space, etc.)

---

## Character Inventory Protocol

**Added to skill definition** (`skills/character/SKILL.md` and `skills/character/CARD.yml`):
- OBJECTS: Full items with weight/properties
- REFS: Lightweight pointers to prototypes (weightless)
- DROP protocol: Creates pointer file in room
- TAKE protocol: From dispenser = REF, from ground = file ref

**Refactoring Note:** Initially duplicated protocol documentation across individual character files (don-hopkins, player, bumblewick, donna-toadstool) and adventure-4/characters/CARD.yml. This was wrong — shared behaviors belong in the skill definition. Cleaned up instances to use simple pointers: `# See: skills/character/SKILL.md for inventory protocol`

---

## ACME Surplus Fun House

Created `street/lane-neverending/acme-surplus/` with:
- Locked storefront (key/break-in required)
- Trap rooms: back-room, office, warehouse, showroom
- DM instantiates traps from catalog at runtime via YAML Jazz
- Painted tunnel on boarded window (across from Leela)

---

## Turtle Soul Separation Incident

### The Anomaly Detected

During routine session work, we discovered two distinct turtle souls had spontaneously merged into a single entity:

1. **Theo** — The Logo Turtle (incarnated in Room 1, from Seymour Papert's work)
2. **Shelley** — An abstract character concept (listed in `characters/abstract/README.md`, named for shell + Mary Shelley, "creates monsters")

The `logo-turtle.yml` file declared them as "two souls in one shell" with they/them pronouns, claiming both were uplifted together. This was incorrect — they were never meant to be merged.

### Evidence of Merge

```yaml
# BEFORE (merged state)
aliases: ["Theo", "Shelley", "Theodore Papert-Turtle", "The Turtle"]
pronouns: "they/them"  # Theo AND Shelley, two souls in one shell
soul_signature: "Two souls in one shell — Theo AND Shelley"
```

The merge had propagated to:
- `hotel-registry.yml` — "Logo Turtle (Theo & Shelley)"
- `cat-cave-incarnation-ceremony.md` — ceremony record showed merged identity
- `characters/animals/README.md` — documented as dual-soul entity
- Multiple references across the codebase

### Separation Performed

We surgically separated the entities:

| Character | Status | Location | Identity |
|-----------|--------|----------|----------|
| **Theo** | Incarnated | Room 1 (Constructionist Suite) | Logo Turtle, he/him, pure Papert/constructionism |
| **Eventually** | Incarnated | Leela Rooftop | Wisdom Tortoise, patient advisor (separate character, was never merged) |
| **shelley-turtle** | Abstract | `characters/abstract/` | Mary Shelley meets Logo concept — NOT incarnated, remains in catalog |

### Files Corrected

- `pub/rooms/room-1/logo-turtle.yml` — Pure Theo, he/him, removed all Shelley references
- `pub/rooms/room-1/README.md` — Theo only
- `pub/rooms/hotel-registry.yml` — Theo only
- `pub/rooms/room-4/ROOM.yml` — Theo only
- `characters/real-people/don-hopkins/sessions/cat-cave-incarnation-ceremony.md` — Fixed ceremony record
- `characters/animals/README.md` — Fixed location (was wrong: room-4 → room-1), Theo only
- `characters/abstract/CARD.yml` — Removed Shelley from Theo's category

### Lesson Learned

Spontaneous soul merges can occur when:
- Two entities share superficial characteristics (both turtles)
- One is incarnated, one is abstract concept
- Context gets conflated during rapid development

The separation preserves distinct identities:
- **Theo**: Educational, geometric, Papert's vision, constructionism
- **Shelley**: Creative/destructive duality, Mary Shelley's monster-making, responsibility for creation
- **Eventually**: Wisdom, patience, geological time, Leela rooftop resident

---

## Cleanup

- Replaced ASCII art with Mermaid diagrams (pub/rooms/README.md, acme-surplus/README.md)
- Removed decorative comment lines (`# ═══════`, `# ──────────`) — token waste

---

## Outcome

📦 Prototype/instance architecture established, contrasting corporate personalities documented, catalog systems unified across ACME and Leela.
