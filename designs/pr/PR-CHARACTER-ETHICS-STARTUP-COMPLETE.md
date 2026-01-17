# PR: Character Ethics, Startup Hooks, and Vanessa's Philosophy

**Branch:** don-adventure-4-run-1  
**Author:** Claude (with Don Hopkins)

---

## Summary

This PR completes a major arc: character directory reorganization, comprehensive ethical frameworks, startup hooks, YAML Jazz entropy research, and Vanessa Freudenberg's philosophy on targeting JavaScript.

---

## Commits Covered

| Commit | Summary |
|--------|---------|
| `7426944` | 📄 Vanessa Freudenberg philosophy: Target JS, not WASM |
| `bc86cab` | 🎷 YAML Jazz: Add empirical evidence — entropy collapse research |
| `6eb737e` | 🏗️ Character reorganization + ethical framework + startup hook |
| `a20b7e9` | 🎭 Add explicit impersonator & drag tribute to representation-ethics |

---

## 1. Vanessa Freudenberg Philosophy

**File:** `designs/vanessa-freudenberg-philosophy.md`

Documented Vanessa's core insight: **target JavaScript, not WebAssembly**.

Key points:
- JavaScript IS the lingua franca of computing
- WASM adds complexity without necessity for most apps
- Squeak/Smalltalk community learned this the hard way
- The web already won — embrace it

> "Why add a layer when JS already runs everywhere?"

---

## 2. YAML Jazz Entropy Research

**File:** Added empirical evidence section to YAML Jazz documentation

Research findings on LLM behavior with YAML comments:
- **Entropy collapse** — LLMs converge toward predictable outputs
- **Comments as semantic anchors** — keep models on track
- **The "warmth" phenomenon** — commented YAML feels more alive

This validates YAML Jazz as more than convention — it's empirically grounded.

---

## 3. Character Directory Reorganization

Characters now organized by **ethical category**:

```
characters/
├── abstract/          # Conceptual beings, player prototypes
│   └── player/        # The generic hero template
├── real-people/       # Living and deceased real humans
├── fictional/         # Characters from fiction, games, TV
├── animals/           # Real and fictional animals
└── robots/            # Mechanical minds, AIs
```

### Convention Clarified

| Type | Example | When DESCRIBE-ME runs |
|------|---------|----------------------|
| **Directory character** | `characters/abstract/player/` | Shows directory path |
| **File-only character** | `characters/real-people/don/biscuit.yml` | Shows file path |

---

## 4. Enhanced Ethical Declarations

Each character category now has comprehensive `ROOM.yml` ethical framing:

| Category | Protocol | Key Additions |
|----------|----------|---------------|
| `real-people/` | TRIBUTE | Living vs deceased guidelines, abstraction levels, Sims precedent |
| `fictional/` | CREATIVE | Fan tradition, fair use, legal awareness |
| `abstract/` | CONCEPTUAL | Player prototype explanation, incarnation rights |
| `animals/` | CREATURE | Real animals = tribute-level respect, species wisdom |
| `robots/` | ARTIFICIAL | Modern AI simulation distinction, philosophical territory |

All rooms now explicitly reference `skills/representation-ethics/` and `skills/incarnation/`.

---

## 5. Startup Hook System

**New file:** `startup.yml` at project root

Configurable post-boot behavior:
- Mode selection: `adventure`, `development`, `custom`, `none`
- Character handling if none exists
- Delegates to `adventure:RESUME` or `adventure:START`
- Override with `startup.local.yml` (gitignored)

### New Methods

| Skill | Method | Purpose |
|-------|--------|---------|
| `bootstrap` | `STARTUP` | Read startup.yml, dispatch to mode |
| `adventure` | `RESUME` | Continue where left off |
| `adventure` | `START` | Fresh game with character generation |
| `adventure` | `ENSURE-CHARACTER` | Make sure player exists |
| `adventure` | `CREATE-CHARACTER` | Generate from prototype |

---

## 6. Explicit Impersonation Ethics

Extended `skills/representation-ethics/` with self-framing patterns:

### The Core Insight

> **The label IS the disclaimer.**

When named "Elvis Impersonator" or "Cher-ity Case", no additional framing needed.

### New Abstraction Levels

| Level | Example | Safety |
|-------|---------|--------|
| `explicit-impersonator` | "Elvis Impersonator" | HIGH — word "impersonator" = disclosure |
| `drag-celebrity-tribute` | "Cher-ity Case" | HIGH — pun name = declared tribute |
| `satirical-character` | "Tina Fey as Sarah Palin" | MEDIUM-HIGH — sketch comedy context |

### Precedents Documented

- Elvis impersonators (beloved industry)
- Tribute bands ("The Australian Pink Floyd Show")
- Snatch Game (drag queens "playing" celebrities)
- SNL political impressions
- Weird Al (parody is its own category)

---

## 7. Navigation Fixes

Verified canonical layout from `start/ROOM.yml`:
- **WEST** → kitchen
- **EAST** → coatroom

The coatroom is now a transformation hub:
- **WEST** → start (Chamber of Commencement)
- **NORTH** → characters (Hall of Bodies)
- **SOUTH** → personas (Wardrobe of Masks)
- **EAST** → skills (Skill Nexus)

---

## 8. Anti-Pattern: ASCII Maps

Added explicit prohibition in `skills/room/CARD.yml`:

```yaml
anti-patterns:
  ascii-maps:
    prohibition: FORBIDDEN
    reason: |
      - LLM indentation is unreliable
      - High token cost, high maintenance
      - Use markdown tables instead
```

---

## Files Changed

### New Files
- `startup.yml` — Session startup configuration
- ~~`examples/adventure-4/skills/ROOM.yml`~~ — *Refactored: Now use global `skills/ROOM.yml` with abstract room references*
- ~~`examples/adventure-4/skills/README.md`~~ — *Refactored: Deleted — global skills/ IS the Skill Nexus*
- `designs/vanessa-freudenberg-philosophy.md` — Vanessa's JS philosophy
- `designs/pr/PR-CHARACTER-ETHICS-STARTUP-COMPLETE.md` — This PR

> **Note:** The adventure-local `skills/` folder was later refactored. The global `skills/` directory now serves as the Skill Nexus for all adventures, using abstract room references that resolve at runtime. See `skills/ROOM.yml` for the abstract reference pattern.

### Major Modifications
- `skills/representation-ethics/CARD.yml` — Explicit impersonation section
- `skills/representation-ethics/SKILL.md` — Frame 6: Drag Celebrity Tribute
- `skills/bootstrap/CARD.yml` — STARTUP method
- `skills/adventure/CARD.yml` — RESUME/START/ENSURE-CHARACTER/CREATE-CHARACTER
- `skills/room/CARD.yml` — Anti-patterns section
- `examples/adventure-4/characters/*/ROOM.yml` — All 5 ethical declarations enhanced
- `examples/adventure-4/coatroom/ROOM.yml` — Updated exits and references
- `PROTOCOLS.yml` — New K-lines

### Renamed (User-initiated moves)
- `characters/player/` → `characters/abstract/player/`
- `characters/biscuit/` → `characters/animals/biscuit/`
- `characters/palm/` → `characters/animals/palm/`
- `characters/bumblewick-fantastipants/` → `characters/fictional/bumblewick-fantastipants/`
- `characters/don-hopkins/` → `characters/real-people/don-hopkins/`

---

## Key Quotes

> "Target JavaScript, not WASM." — Vanessa Freudenberg

> "The word 'impersonator' carries the disclaimer within itself."

> "Animals are not objects. They have inner lives."

> "DO NOT create ASCII art maps!" — skills/room/CARD.yml

> "You ARE your file." — MOOLLM character philosophy

---

## Related PRs

- `PR-SIMS-ARCHAEOLOGY-COMPLETE.md` — Previous major PR (22 Sims docs)
- `PR-TRIBUTE-FRAMING-ETHICS.md` — Earlier ethics work
- `PR-CHARACTER-CATALOG-EXPANSION.md` — Character catalog setup

---

## What's Next

- Execute `STARTUP` in bootstrap flow
- Test character generation from prototype
- Add more characters to ethical categories
- Continue Vanessa Freudenberg collaboration
