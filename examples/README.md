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
├── adventure-4/           # Don Hopkins' run — ACTIVE! The main example.
│   ├── README.md          # Incarnation protocol, Palm, Speed of Light
│   ├── characters/        # Animals, fictional, real-people
│   │   └── animals/monkey-palm/   # Palm the capuchin philosopher
│   ├── pub/               # The Pub — games, stage, karaoke
│   ├── street/            # Lane Neverending — buildings, slideshows
│   └── sessions/          # Session logs and transcripts
└── old/                   # Earlier adventures (archived)
    ├── adventure-1/       # The seed adventure (minimal template)
    ├── adventure-2/       # Captain Ashford's epic — grue slain, PhD written
    └── adventure-3/       # Rich template
```

---

## The Examples

| Example | Description | Status |
|---------|-------------|--------|
| [adventure-4/](./adventure-4/) | Don Hopkins' run — incarnation, Palm, Lane Neverending, Fluxx, Speed of Light | 🔥 **ACTIVE** |

### Archived (in `old/`)

| Example | Description | Status |
|---------|-------------|--------|
| [old/adventure-1/](./old/adventure-1/) | The seed world — minimal starting template | 🌱 Archived |
| [old/adventure-2/](./old/adventure-2/) | Captain Ashford's epic — grue slain, PhD written, 69 moves | 🏆 Archived |
| [old/adventure-3/](./old/adventure-3/) | Rich template — advanced mechanics, pub, NPCs, crafting | 📦 Archived |

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
