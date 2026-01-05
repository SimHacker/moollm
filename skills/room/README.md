# 🚪 Room

> Directories as activation contexts where objects come alive

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

## Related Skills

- [card](../card/) — cards live in rooms
- [memory-palace](../memory-palace/) — room + mnemonic intent
- [adventure](../adventure/) — room + narrative quest framing
