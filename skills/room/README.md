# 🚪 Room

> Directories as activation contexts where objects come alive

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [card/](../card/) | Cards live in rooms |
| [container/](../container/) | Non-navigable inheritance scopes |
| [exit/](../exit/) | Room connections |
| [object/](../object/) | Things in rooms |
| [memory-palace/](../memory-palace/) | Room + mnemonic intent |
| [adventure/](../adventure/) | Room + narrative quest framing |
| [character/](../character/) | Characters inhabit rooms |
| [data-flow/](../data-flow/) | Rooms as pipeline nodes |
| [multi-presence/](../multi-presence/) | Same card in multiple rooms |
| [files-as-state/](../plain-text/) | Rooms ARE directories |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | Live pub with stage, menus, arcade |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: ROOM.yml](ROOM.yml.tmpl) — room template

## Overview

Rooms are **intertwingled navigable activation context maps**. Entering = calling. Exiting = returning.

In MOOLLM:
- **Room** = Directory = Activation record = Stack frame
- **Enter** = cd = Push context = Call function
- **Exit** = cd .. = Pop context = Return
- **Cards in room** = Active task instances

## Room Anatomy

```
room-name/
  ROOM.yml          # Room definition (optional if inheriting!)
  README.md         # Room's voice
  CARD.yml          # Optional: makes room card-playable
  state/            # Room state
  char-name.yml     # Embedded NPCs
```

## Room Inheritance

**Subdirectories inherit room-ness from parent ROOM.yml files.**

This means you don't need to clutter every directory with its own ROOM.yml. If a parent directory has a ROOM.yml, all children are automatically rooms.

### Example: The Skills Directory

```
skills/
  ROOM.yml          # Defines the Skill Nexus
  adventure/        # IS a room (inherits from parent)
    README.md       # The room's description
    SKILL.md        # Full documentation
  character/        # IS a room (inherits from parent)
  yaml-jazz/        # IS a room (inherits from parent)
```

Each skill subdirectory IS a room without needing its own ROOM.yml.

### When to Create a Custom ROOM.yml

Only create a ROOM.yml in a subdirectory if you need to **customize**:

| Customization | Example |
|---------------|---------|
| Override atmosphere | Different lighting, sounds |
| Add custom exits | Beyond K-line navigation |
| Zone-specific ads | Local commands |
| Change narration style | Different personality |

### K-Line Navigation

For skill directories, exits are derived from the **MOOLLM K-Lines** table in README.md:

| K-Line Table Row | Becomes |
|------------------|---------|
| K-line name | Exit direction |
| "Why Related" | Connection narration |

When you traverse a K-line, the "Why Related" text tells the CONNECTION STORY — like James Burke explaining how carrier pigeons connect to instant messaging.

## Virtual Zones

Rooms can contain virtual sub-zones without physical subdirectories:

```yaml
zones:
  nap-zone:
    path: ./nap-zone
    description: "Warm sleeping area"
```

## Etymology & Historical Trivia

The "room" metaphor has deep roots in both cognitive science and HCI:

### Xerox PARC Rooms (1986)

Henderson & Card's influential paper ["Rooms: The Use of Multiple Virtual Workspaces to Reduce Space Contention in a Window-based Graphical User Interface"](https://dl.acm.org/doi/10.1145/24054.24056) introduced virtual desktop rooms as navigable workspaces. MOOLLM's room concept extends this to semantic activation contexts.

### Why "Room" Instead of "Frame"

Marvin Minsky's AI "frames" are foundational, but the term is overloaded (stack frames, video frames, picture frames, framing effects). "Room" is more concrete and fits MOOLLM's adventure game aesthetic:

| Concept | Frame Term | Room Term |
|---------|------------|-----------|
| Navigate | "Switch frames" | "Enter/exit rooms" |
| Contains | "Frame slots" | "Things in the room" |
| Connections | "Frame relations" | "Exits and doors" |
| Context | "Active frame" | "The room you're in" |

Kids get rooms. Developers get rooms. Everyone's been in a room.

### The MOO Connection 🐄

**Fun fact:** ROOMS contains MOO spelled backwards (OOM).

This is fitting because [LambdaMOO](https://en.wikipedia.org/wiki/LambdaMOO) and text-based MUDs pioneered room-based virtual world navigation in the 1990s. MOOLLM's filesystem-as-dungeon approach is a direct descendant of this tradition.

And if you spell ROOMS backwards? **SMOOR** — which could stand for *Society of Mind, Object-Oriented Rooms*. Coincidence? Almost certainly. But it's a good mnemonic anyway.

