# Characters

> *"You ARE your file."*

All player characters and NPCs live here. Each `.yml` file is a character.

**Architectural principle:** Characters are NOT embedded in rooms!
- Characters have a `location:` field that REFERENCES a room
- Characters can move between rooms by changing the reference
- Multiple characters can be in the same room
- Rooms contain OBJECTS, not characters

---

## Active Players

The adventure supports **multiple simultaneous players**! See [../ADVENTURE.yml](../ADVENTURE.yml) for who's currently active.

| File | Status |
|------|--------|
| [don-hopkins.yml](./don-hopkins.yml) | Active — Consciousness programmer |
| [bumblewick-fantastipants.yml](./bumblewick-fantastipants.yml) | Available — Reluctant hero, spoon enthusiast |
| [player.yml](./player.yml) | Available — Generic hero template |

---

## Multi-Player Commands

Switch who you're talking to in chat:

| Command | Effect |
|---------|--------|
| `@don-hopkins Look around` | Direct command to specific player |
| `@player What do you see?` | Different player |
| `@all Everyone gather` | Broadcast to all active players |
| `ADDRESS don-hopkins` | Switch default chat target |
| `ADDRESS-ALL` | Target all active players |
| `WHO` | Show current chat target |
| `PLAYERS` | List all active players |
| `ACTIVATE player.yml` | Add player to active list |
| `DEACTIVATE don-hopkins` | Remove from active list |

---

## How Multiple Players Work

- **Separate locations:** Each player can be in a different room
- **Separate inventories:** Each carries their own stuff
- **Separate goals:** Each pursuing their own aspirations
- **Shared world:** Changes one player makes persist for all
- **Same room interactions:** Players can talk, trade, collaborate
- **Speed-of-light communication:** Multiple characters act within single LLM calls

Think: **MUD** with multiple characters, each with their own session.  
Think: **The Sims** with multiple selectable Sims.  
Think: **Engelbart's NLS** with multiple cursors.

---

## File = Identity

In MOOLLM, the filesystem IS the world. Your file name IS your identity.

```
characters/
  don-hopkins.yml     # The creator playing his creation
  player.yml          # Generic hero template
  captain-ashford.yml # After renaming in coatroom
  mother.yml          # NPCs live here too
  skeleton.yml        # Even dead ones
```

---

## Character Structure

Every character file can include:

```yaml
player:
  name: "Character Name"
  type: player_character  # or npc, companion, etc.
  
  # Identity
  description: "..."
  backstory: "..."
  current_persona: null  # or path to persona file
  
  # State
  location: start/
  inventory: []
  gold: 10
  
  # Mind Mirror (personality)
  sims_traits:
    neat: 5           # Comments are DYNAMIC — update with values!
                      # Inner voice: "I know where everything is."
    outgoing: 5
    active: 5
    playful: 5
    nice: 5
    
  mind_mirror:
    bio_energy: { ... }
    emotional: { ... }
    mental: { ... }
    social: { ... }
    
  needs:
    hunger: 7         # Fine. Coffee counts as food, right?
                      # Inner voice: "I should probably eat."
    energy: 7
    fun: 7
    # ... comments change with values!
    
  # Goals
  goals: []
  aspirations: []
  
  # Relationships
  relationships: {}
  
  # Abbreviated (for quick Coherence Engine reference)
  abbreviated:
    personality: []
    current_mood: ""
    driving_need: ""
    main_goal: ""
```

---

## Creating New Characters

### In the Coatroom

```
> GENERATE-NPC rival adventurer
> CHANGE-NPC-FILE-NAME blackcape-mcgee

Created: characters/blackcape-mcgee.yml
```

### From Template

Copy `player.yml` and customize:
1. Change name and id
2. Adjust sims_traits with YAML Jazz comments
3. Set mind_mirror dimensions
4. Write backstory
5. Define goals and relationships

### Switching Players

```
> ACTIVATE blackcape-mcgee.yml   # Add to active list
> ADDRESS blackcape-mcgee        # Switch chat target
> DEACTIVATE player.yml          # Remove from active (not deleted!)
```

---

## Naming Rules

When renaming via `CHANGE-MY-FILE-NAME`:

| Rule | Why |
|------|-----|
| Stay in `characters/` | Characters belong together |
| No overwriting | Can't steal someone else's identity |
| `.yml` optional | We know what you mean |
| Kebab-case preferred | `captain-ashford`, not `CaptainAshford` |

---

## Dynamic Need Comments

**Critical insight:** Comments on needs are the character's **inner voice**.  
When values change, **UPDATE THE COMMENTS** to match!

```yaml
# This enables rich internal monologue and authentic dialogue:

hunger: 10  # Stuffed. Couldn't eat another bite.
            # Inner voice: "Ugh, too much pie."

hunger: 7   # Satisfied. No food thoughts.
            # Inner voice: "That was a good meal."

hunger: 3   # Getting peckish. Food ads score higher!
            # Inner voice: "Is that pie I smell?"

hunger: 1   # STARVING. Will eat anything. Even that.
            # Inner voice: "FOOD. FOOD. FOOD. FOOD."
```

---

## Architecture: What Lives Where

```
adventure-3/
│
├── characters/          # WHO — Characters (have location reference)
│   ├── don-hopkins.yml     location: start/
│   └── player.yml          location: start/
│
├── personas/            # MASKS — Wearable overlays (NO location!)
│   └── captain-ashford.yml   # Anyone can wear
│
├── start/               # WHERE — Room containing objects
│   ├── ROOM.yml
│   └── lamp.yml            # Object IN the room
│
└── kitchen/             # Another room
    ├── ROOM.yml
    └── fridge.yml          # Object IN the room
```

| Thing | Has Location? | Embedded in Room? |
|-------|---------------|-------------------|
| **Character** | Yes (references room) | NO — lives in `characters/` |
| **Persona** | No | NO — lives in `personas/` |
| **Object** | Yes (implicit) | YES — lives in room dir |
| **Room** | Yes (via exits) | — |

**Why this matters:**
- Characters MOVE by changing their `location:` reference
- Multiple characters can be in the same room
- Multiple characters can wear the same persona
- Objects belong to rooms; characters belong to themselves

---

## Dovetails With

- [../ADVENTURE.yml](../ADVENTURE.yml) — Per-adventure state (active players, chat target)
- [../personas/](../personas/) — Wearable personality overlays
- [../coatroom/](../coatroom/) — Where characters try on personas
- [../../../skills/mind-mirror/](../../../skills/mind-mirror/) — Personality system
- [../../../skills/adventure/](../../../skills/adventure/) — Adventure framework
- [../start/](../start/) — Where the adventure begins
