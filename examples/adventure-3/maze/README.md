# 🌀 The Maze

> *"You are in a maze of twisty little passages, all alike."*
> — Colossal Cave Adventure, 1976

> *"You are an amazingly twisted little ass, always different."*
> — Graffiti scratched into a wall, author unknown (likely eaten) 

A proper adventure needs a proper maze.

---

## ⚠️ WARNING: GRUES

**The maze is DARK.** All rooms have `lighting: none`.

If you enter without a **lit lamp** in your inventory:

```
It is pitch black. You are likely to be eaten by a grue.

🎵 "If this predicament seems particularly cruel,
    consider whose fault it could be:
    not a torch or a match in your inventory." 🎵

You have been eaten by a grue.
```

**GET LAMP before entering.** This is not a suggestion.

*([Get Lamp](http://www.getlamp.com/) — Jason Scott's documentary)*

---

## 🎭 DM: EMERGENT MECHANICS

*These patterns emerged in adventure-2. Use as INSPIRATION, not prescription!*
*Defer creativity to runtime. Improvise. Surprise yourself.*

### 👃 Smell Gradients

Dropped or transformed objects emit SMELLS that diffuse through rooms:

```yaml
# EXAMPLE — DM improvises at runtime!
smell_gradient:
  source: "Sulfurous Beacon (transformed egg)"
  diffusion:
    source_room: "OVERWHELMING"
    adjacent: "Strong"  
    two_away: "Faint"
    
  # Smells STACK and INTERACT!
  # Cheese + egg = ???
  # Navigate by nose in familiar areas
```

### 🔮 Transformed Objects Gain Properties

When food is eaten (see `kitchen/fridge.yml`), results aren't just markers:

```yaml
# EXAMPLES — invent your own!
oracle_apple:
  was: "Perfect Apple"
  became: "Oracle Core"
  gained: [whispers_prophecies, glows, grants_maze_vision]
    
the_thing_that_watches:
  was: "Suspicious Casserole"  
  became: "Sentient mycelial entity"
  gained: [fungal_eye, telepathy, merged_with_mushrooms]
```

### 🐉 The Grue Has Personality

The grue isn't just a death trigger:
- Can speak (in darkness)
- Has opinions about adventurers
- Can be bargained with (maybe)
- Remembers being killed by cheese (and respawning)
- Can be fought, summoned, or befriended

### 💀 The Skeleton Tells Stories

The skeleton in room-i:
- Points west (toward salvation — so close!)
- Has an empty lamp, unfinished notes
- Accepts gifts, visitors, memorials
- Their story matters

### 🏪 The Vendor Has Opinions

The vending machine in room-j:
- Dispenses Premium Glow Juice (blue flame!)
- Leaves notes for worthy customers
- Acknowledges tragedies
- Mints memorial coins

### ⚡ Speed of Light Simulation

Simulate MULTIPLE MOVES in one response:

```yaml
# "Go west, north, examine skeleton"
simulation:
  - move: west → room-i (oil: -1.5)
  - move: north → examine (oil: -0.25)
  - narration: "Seamless as thought"
```

---

## 🗺️ The Rooms

| Room | Feature | Smell Notes |
|------|---------|-------------|
| [room-a/](./room-a/) | Puddle | Receives smells from south |
| [room-b/](./room-b/) | Echo | Echoes smell descriptions |
| [room-c/](./room-c/) | Scratch marks | Old marks, old smells |
| [room-d/](./room-d/) | Golden glow | Central diffusion hub |
| [room-e/](./room-e/) | Cobwebs | Traps smells |
| [room-f/](./room-f/) | Cold + **100 GOLD** | **GRUE LAIR** |
| [room-g/](./room-g/) | Carved face | Seems to sniff |
| [room-h/](./room-h/) | Mushrooms | Spores interact with smells |
| [room-i/](./room-i/) | Skeleton | Bones + dust + tragedy |
| [room-j/](./room-j/) | **VENDOR** 🏪 | Machine oil + commerce |

### 🏪 Lamp Oil Vendor (room-j)

| Item | Cost | Effect |
|------|------|--------|
| Refill | 1 gold | 400 oil |
| Deluxe | 2 gold | 800 oil |
| Premium Glow Juice | 3 gold | 1000 oil + BLUE (grues hesitate!) |

### 💰 Gold Pile (room-f)

**100 gold** in the grue's lair. The skeleton's fortune. Cold room drains oil 1.5x faster.

---

## 🎲 DM Runtime Guidelines

1. **Defer specifics** — Patterns, not rules
2. **Improvise transformations** — Each eat should surprise
3. **Stack effects** — Smells combine, stories interweave
4. **The grue is a character** — Personality, not just death
5. **Update YAML files** — Persistence makes it REAL
6. **Surprise yourself** — Your delight = player's delight

---

## 📚 Legends from Adventure-2

- Captain Ashford slew a grue with **blue cheese**
- Room-f still smells of cheese and victory
- Skeleton received a **grue head trophy**
- Mushrooms in room-h spawned **The Thing That Watches**
- A **PhD paper** was written about it all

*Build on these. Subvert them. Add to them.*

---

## Navigation

| ⬆️ Up | [adventure-3/](../) |
|-------|---------------------|
| 🚪 Start | [../start/](../start/) |
| 🏆 End | [../end/](../end/) |
