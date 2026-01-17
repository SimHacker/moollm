# 🎮🔧🏰✨ PR: Adventure Compiler Vision — From YAML to Browser

## Summary

This PR documents the **complete architectural vision** for the adventure skill:
- **7 commits** crystallizing the pipeline
- YAML → Lint → LLM Compile → Browser runtime
- Scott Adams & Don Hopkins lineage documented
- adventure-4/pub/ as the gold standard example

> *"Cursor becomes a point-and-click adventure authoring system."*

---

## Part 1: 🏆 THE GOLD STANDARD

### adventure-4/pub/ — The Crown Jewel

```
pub/
├── ROOM.yml              # 6 themes!
├── bartender.yml         # 6 identity variants
├── pie-table.yml         # Octagonal debate table
├── gong.yml              # Gezelligheid protocols
├── bar/
│   ├── bartender.yml     # The omniscient bartender
│   ├── budtender-marieke.yml
│   └── cat-cave/         # TARDIS-like cat sanctuary
│       └── 10 cats (Terpie, Stroopwafel, kittens...)
├── arcade/               # Pacman, Pong, Pinball
├── games/                # Chess, Darts, Cards
├── stage/
│   └── palm-nook/        # Multi-room character space
│       ├── study/        # Infinite typewriters
│       ├── gym/          # Infinite climb
│       ├── play/
│       └── rest/         # Hammock, silence cushion
└── menus/                # drinks, snacks, buds, games
```

### Themeable NPCs (bartender.yml)

```yaml
identity:
  classic_adventure: { name: Grim, appearance: "Weathered human..." }
  space_cantina: { name: Z-4RT, appearance: "Multi-armed droid..." }
  cyberpunk_bar: { name: Nyx, appearance: "Chrome-implanted..." }
  victorian_parlor: { name: Reginald, appearance: "Magnificent mustache..." }
  pirate_tavern: { name: Pegleg Pete, appearance: "Exactly what you'd expect..." }
  wild_west_saloon: { name: Miss Kitty, appearance: "Sharp-eyed woman..." }
```

Same knowledge, different personality per theme. "I've always been here."

---

## Part 2: 🔧 THE PIPELINE

### The Four Stages

```
┌─ 1. AUTHOR ─────────────────────────────────────────┐
│   Write empathic YAML in Cursor                     │
│   (readable, expressive, human/LLM-friendly)        │
└─────────────────────────────────────────────────────┘
                        ↓
┌─ 2. LINT ───────────────────────────────────────────┐
│   $ adventure.py lint quest/                        │
│                                                     │
│   [ERROR]   Broken references                       │
│   [WARN]    Missing fields                          │
│   [COMPILE] Needs execution data + expressions      │
│   [HINT]    Improvement suggestions                 │
│   [IMAGE]   Generate image prompts                  │
└─────────────────────────────────────────────────────┘
                        ↓
┌─ 3. LLM COMPILES ───────────────────────────────────┐
│   Linted YAML  →  HTML + CSS + JSON + JavaScript    │
│                                                     │
│   - Generates compiled_behavior with JS expressions │
│   - Creates navigation structure                    │
│   - Builds dialogue trees                           │
│   - Produces image generation prompts               │
└─────────────────────────────────────────────────────┘
                        ↓
┌─ 4. BROWSER RUNTIME ────────────────────────────────┐
│   🖼️ Generated images                               │
│   💬 Scrolling chat                                 │
│   🎯 Point-and-click commands                       │
│   🥧 Right-click pie menus                          │
│   ⌨️ Text input                                     │
│   🎲 Runtime expression evaluation                  │
│   🤖 Optional LLM escalation for complex situations │
└─────────────────────────────────────────────────────┘
```

---

## Part 3: 💭 EMPATHIC EXPRESSIONS

### The Key Insight

**Empathic expressions** are high-level behavioral intentions readable by LLMs:

```yaml
behavior:
  mood: curious
  patrol_pattern: "wander between rooms, investigate sounds"
  when_startled: "freeze, then flee to nearest hiding spot"
```

The linter asks the LLM to compile these into **static execution data**:

```yaml
compiled_behavior:
  patrol_waypoints: [room_a, room_b, room_c]
  patrol_speed: 0.5
  startle_response:
    freeze_duration: 2
    flee_targets: ["under_bed", "corner_shadow"]
```

### Runtime Expressions: JavaScript in YAML

The LLM generates YAML with **embedded JavaScript** for runtime evaluation:

```yaml
expressions:
  damage_roll: "roll('1d6') + this.strength"     # Dice!
  flee_chance: "player.intimidation > 5 ? 0.8 : 0.3"
  greeting: "pick_random(this.greetings)"        # Variation
  mood_shift: "this.hunger > 50 ? 'aggressive' : 'curious'"
```

| Expression Type | Example | Purpose |
|-----------------|---------|---------|
| **Dice** | `roll('2d6+3')` | Combat, skill checks |
| **Random pick** | `pick_random(responses)` | Dialogue variation |
| **Conditionals** | `hp < 10 ? 'wounded' : 'healthy'` | State-based behavior |
| **Math** | `base_price * (1 - haggle_skill/100)` | Economy |
| **Time** | `turn % 10 === 0` | Periodic events |
| **Proximity** | `distance(player, this) < 3` | Spatial triggers |

---

## Part 4: 🏛️ THE LINEAGE

### Primary Source: Hacker News (Nov 2021)

Conversation between:
- **Scott Adams** — Creator of *Adventureland* (1978, first commercial text adventure)
- **Don Hopkins** — SimCity, The Sims, pie menus, cellular automata

### Adventure Games = Memory Palaces

The [Method of Loci](https://en.wikipedia.org/wiki/Method_of_loci) was **banned by Puritans in 1584** for evoking "bizarre and irrelevant" imagery.

Don Hopkins: *"Mnemonics was seen as dangerous and magical and heretical... And they were right, fortunately: Dangerous magic that works!"*

### Pie Menus = Room Navigation

```
      N
      ↑
  NW ↖ ↗ NE
 W ←  ●  → E     Pie menu = Room exits = Memory palace navigation
  SW ↙ ↘ SE
      ↓
      S
```

Don Hopkins: *"4-item and 8-item pie menus are the essential elements of an Adventure map, as long as you think of 'menus' as rooms with two-way links."*

### Code as Buildings

Don Hopkins visualizes code as memory palaces:

> *"Each function is a little building like an office or a shop, which has a sign out front telling what services or products it sells.*
> 
> *You're standing behind the front counter, just about to receive a customer through the front entrance door with the parameters.*
> 
> *You go into the back room, solve the problem, then deliver the results out the exit door at the back."*

### The Vision: Archives as Adventures

Both want to publish their **papers, articles, emails, and biographies** as interactive adventures:

| Traditional Archive | Adventure Archive |
|---------------------|-------------------|
| Read papers linearly | Explore rooms of ideas |
| Static biography | Talk to younger/older selves |
| Download files | Interact with objects |
| Search text | Ask characters questions |
| Passive consumption | Active discovery |

### The Lineage

| Year | Project | Platform |
|------|---------|----------|
| 1995 | DreamScape | ScriptX (WWDC demo) |
| ???? | MediaGraph | Unity3D (Will Wright's Stupid Fun Club) |
| 2008 | iLoci | iPhone (Amsterdam Mobile Dev Camp) |
| 2026 | **THIS** | Cursor + LLM + YAML |

*"Each iteration: a little different and a little better, as technology advanced."*

---

## Part 5: 🦉 LLOOOOMM HERITAGE

### The Shneiderman Owl Simulation

YAML definitions compile to JavaScript classes:

```yaml
# owl.yml (YAML definition)
name: "Nightwatch-7"
type: owl
behaviors: [patrol, hunt, drone]
stats: { energy: 100, catches: 0, altitude: 50 }
```

↓ **Compiles to** ↓

```javascript
// owl.js (Generated JavaScript)
class Owl {
    constructor(id, timezone) {
        this.position = { x: 0, y: 0, z: 50 };
        this.velocity = { x: 0, y: 0, z: 0 };
        this.energy = 100;
    }
    
    update() {
        this.patrol();
        this.hunt();
        if (this.energy < 20) this.rest();
    }
    
    patrol() {
        // Boids algorithm: separation, alignment, cohesion
    }
}
```

### The Projection Concept

Browser provides deterministic simulation. Complex situations escalate to LLM:

```javascript
if (situation.complexity > THRESHOLD) {
    // Pause simulation
    // Send context to LLM API
    // LLM decides outcome
    // Resume with LLM's decision
}
```

---

## Commits

| Hash | Message |
|------|---------|
| 3a111f2 | feat(adventure): Add adventure.py CLI uplift plan |
| b290ba0 | feat(adventure): Add lloooomm crown jewels architecture |
| faa16af | docs(adventure): Add adventure-4 and pub as gold standard examples |
| db42312 | docs(adventure): Add Empathic Expressions → Static Execution Data pattern |
| e11f602 | docs(adventure): Complete pipeline — YAML → Lint → LLM Compile → Browser |
| c54f44b | docs(adventure): Add Scott Adams & Don Hopkins inspiration and lineage |
| cfc2a6a | fix: Remove accidentally added temp/lloooomm embedded repo |

---

## Why This Matters

### 1. Cursor = Adventure IDE

Write YAML. Lint validates. LLM compiles. Browser runs.
**Point-and-click adventure authoring system.**

### 2. Two Layers of Expression

| Layer | Who Reads | Example |
|-------|-----------|---------|
| Empathic | LLM + Human | `"wander, investigate sounds"` |
| Execution | JavaScript | `patrol_waypoints: [a, b, c]` |

### 3. Archives Come Alive

Scott Adams' papers. Don Hopkins' research. Anyone's biography.
Rooms of ideas instead of linear documents.
Characters you can talk to. Objects you can examine.
**The Method of Loci returns.**

### 4. Standing on Giants

- Scott Adams (Adventureland, 1978)
- Don Hopkins (pie menus, DreamScape, iLoci)
- Will Wright (SimCity, The Sims)
- The Shneiderman lineage (structured programming → Nassi-Shneiderman → code as buildings)

---

## The Banned Magic Returns

> *"Mnemonics was seen as dangerous and magical and heretical back in the Medieval world... And they were right, fortunately!"*
>
> — Don Hopkins

🏰✨🎮

---

*"From empathic YAML to playable browser adventure in one pipeline."*

*"Cursor becomes a point-and-click adventure authoring system."*

---

🎮🔧🏰✨
