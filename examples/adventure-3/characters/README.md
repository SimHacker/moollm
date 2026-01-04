# Characters

> *"You ARE your file."*

All player characters and NPCs live here. Each `.yml` file is a character.

---

## The Player

**[player.yml](./player.yml)** — The current adventurer. Visit the [coatroom](../coatroom/) to:
- Rename your file (`CHANGE-MY-FILE-NAME captain-ashford`)
- Change your name (`CHANGE-MY-NAME Captain Kira Ashford`)
- Transform your appearance and personality

---

## File = Identity

In MOOLLM, the filesystem IS the world. Your file name IS your identity.

```
characters/
  player.yml           # The default name
  captain-ashford.yml  # After renaming
  mother.yml           # NPCs live here too
  skeleton.yml         # Even dead ones
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
    neat: 5
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
    hunger: 7
    energy: 7
    fun: 7
    # ...
    
  # Goals
  goals: []
  aspirations: []
  
  # Relationships
  relationships: {}
```

---

## NPCs

NPCs can also live here! Generate them in the coatroom:

```
> GENERATE-NPC rival adventurer
> CHANGE-NPC-FILE-NAME blackcape-mcgee

Created: characters/blackcape-mcgee.yml
```

---

## Dovetails With

- [coatroom/](../coatroom/) — Where characters are created and modified
- [skills/mind-mirror/](../../../skills/mind-mirror/) — Personality system
- [start/](../start/) — Where the adventure begins
