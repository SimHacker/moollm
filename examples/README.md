# Examples

> *"Show, don't tell. Then tell what you showed."*

Each example directory captures:
1. **The chat dialog** that created it (this README)
2. **The artifacts** produced (YAML files, rooms, characters)
3. **How to explore** the example yourself

---

## How Examples Work

Examples are **live adventures** you can explore and modify. Each one was created through conversation — the README documents what we said to create it.

```
examples/
├── README.md              # This file
├── adventure-1/           # The seed adventure (minimal template)
│   ├── README.md          # Chat log that created it
│   ├── player.yml         # Bumblewick Fantastipants
│   ├── start/             # Chamber of Commencement
│   ├── end/               # The Treasury
│   ├── kitchen/           # Food for maze mapping
│   ├── coatroom/          # Maurice & identity transformation
│   └── maze/              # 10-room grue-infested labyrinth
├── adventure-2/           # Captain Ashford's epic — COMPLETE!
│   ├── README.md          # 69 moves, grue slain, PhD paper written
│   └── ...                # The legendary run
├── adventure-3/           # Rich template — YOUR turn!
│   ├── README.md          # Fresh start, enriched world
│   └── ...                # Same structure, new hero
├── adventure-4/           # Don Hopkins' run — ACTIVE!
│   ├── README.md          # Incarnation protocol, Palm, Speed of Light
│   ├── characters/palm/   # Palm the monkey (fully incarnated)
│   ├── pub/stage/         # Drag shows, karaoke, open mic
│   └── sessions/          # Session logs
└── [more examples...]
```

---

## The Examples

| Example | Description | Status |
|---------|-------------|--------|
| [adventure-1/](./adventure-1/) | The seed world — minimal starting template | 🌱 Seed |
| [adventure-2/](./adventure-2/) | Captain Ashford's epic — grue slain, PhD written, 69 moves | 🏆 **LEGENDARY** |
| [adventure-3/](./adventure-3/) | Rich template — advanced mechanics, pub, NPCs, crafting | 🎮 **PLAY ME** |
| [adventure-4/](./adventure-4/) | Don Hopkins' run — incarnation, Palm, 33-turn Fluxx, Speed of Light | 🔥 **ACTIVE** |

---

## Creating New Examples

Every example starts with a conversation:

```
User: "Create an adventure with X, Y, Z..."
DM: [creates files, explains structure]
User: "Now add W..."
DM: [extends, documents]
```

The README in each example IS that conversation — a tutorial and history in one.

---

## Dovetails With

| Resource | Relationship |
|----------|--------------|
| [skills/adventure/](../skills/adventure/) | The adventure protocol these examples implement |
| [skills/room/](../skills/room/) | Room structure and navigation |
| [skills/card/](../skills/card/) | Characters and objects as cards |
| [PROTOCOLS.yml](../PROTOCOLS.yml) | Symbol definitions |

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [Project Root](../) |
| 📖 Skills | [skills/](../skills/) |
| 🎯 Adventure Protocol | [skills/adventure/](../skills/adventure/) |
