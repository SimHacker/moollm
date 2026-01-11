# 🚪 Room

> Directories as activation contexts where objects come alive

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [card/](../card/) | Cards live in rooms |
| [memory-palace/](../memory-palace/) | Room + mnemonic intent |
| [adventure/](../adventure/) | Room + narrative quest framing |
| [character/](../character/) | Characters inhabit rooms |
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
  ROOM.yml          # Room definition
  README.md         # Room's voice
  CARD.yml          # Optional: makes room card-playable
  state/            # Room state
  char-name.yml     # Embedded NPCs
```

## Virtual Zones

Rooms can contain virtual sub-zones without physical subdirectories:

```yaml
zones:
  nap-zone:
    path: ./nap-zone
    description: "Warm sleeping area"
```

