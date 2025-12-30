# Room Skill

> **Directories as activation contexts. Entering = calling. Exiting = returning.**

---

## Purpose

Treat directories as **rooms** — cognitive spaces where work happens, cards come to life, and context is managed through spatial navigation.

---

## Core Concepts

### Room = Activation Record

| Programming | MOOLLM |
|-------------|--------|
| Function call | Enter room |
| Return | Exit room |
| Local variables | Room state files |
| Parameters | Room context |
| Stack frame | Room directory |

### Cards in Play

Rooms hold **active card instances** — tasks, familiars, helpers that are currently "in play":

```yaml
cards_in_play:
  - instance: "goblin-001"
    card: "Git Goblin"
    goal: "Bisect to find bug"
    state:
      current_commit: "abc123"
      remaining_commits: 5
```

---

## File Structure

```
room-name/
  ROOM.yml              # Room identity and state
  README.md             # Room's voice (for soul-chat)
  
  # Active card instances
  {card}-{id}.yml       # Each card in play
  
  # Room-specific state
  state/
    *.yml               # Working state files
    
  # Optional subdirectories (nested rooms)
  sub-room/
    ROOM.yml
```

---

## ROOM.yml Schema

```yaml
room:
  name: "Room Name"
  purpose: "What this room is for"
  created: "2025-12-30"
  
  # Context loaded when entering
  context:
    - "Important thing to know"
    - "Another important thing"
    
  # Active card instances
  cards_in_play:
    - instance: "instance-id"
      card: "Card Name"
      goal: "What this instance is doing"
      
  # Files to include in working_set when here
  working_set:
    - "ROOM.yml"
    - "README.md"
    - "state/*.yml"
    
  # Navigation
  exits:
    parent: "../"           # Always exists
    sibling: "../other/"    # Related rooms
    child: "./subroom/"     # Nested rooms
    
  # Room's mood/atmosphere (for soul-chat)
  atmosphere: "focused, investigative"
```

---

## Operations

### Enter Room

```yaml
operation: enter_room
path: ".agent/rooms/debug-session/"
effects:
  - "Load ROOM.yml"
  - "Add working_set to context"
  - "Activate any pending cards"
  - "Room becomes current directory"
```

### Exit Room

```yaml
operation: exit_room
effects:
  - "Save any state changes"
  - "Pop room from context"
  - "Return to parent room"
  - "Optionally return a value"
```

### Activate Card

```yaml
operation: activate_card
card: "Git Goblin"
parameters:
  repo_path: "/path/to/repo"
goal: "Find bug introduction"
effects:
  - "Clone card template"
  - "Add to cards_in_play"
  - "Card begins working toward goal"
```

### Complete Card

```yaml
operation: complete_card
instance: "goblin-001"
return_value:
  culprit_commit: "def456"
  message: "Found it!"
effects:
  - "Card writes return_value"
  - "Card can be removed or archived"
  - "Goal marked complete"
```

---

## Room Types

| Type | Purpose | Example |
|------|---------|---------|
| **Session** | Temporary work context | debug-session/, feature-work/ |
| **Project** | Persistent project home | moollm/, my-app/ |
| **Concept** | Knowledge location | yaml-jazz/, play-learn-lift/ |
| **Character** | Persona's space | gardener/, archivist/ |

---

## Memory Palace Integration

Rooms ARE the memory palace:

```
.agent/rooms/
  palace/
    entrance/           # Starting point
      README.md         # "Welcome! Choose a wing..."
      
    east-wing/          # Concepts
      yaml-jazz/
      bpip/
      
    west-wing/          # Skills
      soul-chat/
      trading-card/
      
    tower/              # Characters
      gardener/
      archivist/
```

Navigate to remember. Place things to store.

---

## Commands

| Command | Action |
|---------|--------|
| `ROOM [name]` | Create or enter room |
| `LOOK` | Describe current room |
| `ACTIVATE [card]` | Put card in play |
| `COMPLETE [instance]` | Finish card's work |
| `EXIT` | Leave room, return to parent |

---

## Integration

- **→ trading-card/**: Cards live in rooms
- **→ memory-palace/**: Rooms as memory locations
- **→ soul-chat/**: Rooms can speak (type: room)
- **→ adventure-protocol/**: Narrative room exploration
- **← working_set**: Rooms define their context

---

## See Also

- [trading-card/](../trading-card/) — What lives in rooms
- [memory-palace/](../memory-palace/) — Rooms as memory technique
- [PROTOCOLS.yml#ROOM-AS-FUNCTION](../../PROTOCOLS.yml)
