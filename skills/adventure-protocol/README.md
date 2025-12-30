# Adventure Protocol

> *"Every directory is a room. Every file is a clue. Navigation is investigation."*

Turn exploration into a quest.

> [!TIP]
> **Perfect for codebase archaeology.** "Find where the auth bug was introduced" — that's a quest!

---

## The Premise

You're an **adventurer** exploring unknown territory:

- **Directories** = Rooms to enter
- **Files** = Clues, artifacts, characters
- **Navigation** = Quest progress
- **Log** = Your adventure journal

This is [Memory Palace](../memory-palace/) with **narrative framing**.

---

## Quest Structure

```mermaid
graph TD
    START[🎯 Quest Objective] --> R1[Enter Room]
    R1 --> LOOK[👀 Look Around]
    LOOK --> EXAMINE[🔍 Examine Objects]
    EXAMINE --> COLLECT[📝 Collect Evidence]
    COLLECT --> DECIDE{What next?}
    DECIDE -->|New room| R1
    DECIDE -->|Solved| END[🏆 Quest Complete]
```

---

## When to Use

Perfect for:
- **Codebase archaeology** — "Find where the auth bug was introduced"
- **Onboarding** — "Understand this project's structure"
- **Documentation diving** — "What does this system actually do?"
- **Bug hunting** — "Follow the evidence trail"

---

## The Files

```
quest/
├── ADVENTURE.yml     # Quest state
├── LOG.md            # Narrative journal
├── EVIDENCE/         # Collected clues
└── MAP.yml           # Explored territory
```

### ADVENTURE.yml

```yaml
adventure:
  quest: "Find the authentication bug"
  status: in_progress
  
  current_room: "src/auth/"
  rooms_explored: 5
  clues_found: 3
  
  hypothesis: "Session cookie not being set"
  confidence: 0.7
```

### LOG.md

```markdown
# Adventure Log

## Day 1: Entering the Auth Dungeon

I stepped into `src/auth/` — a maze of middleware.

**Clues found:**
- `session.ts` — handles cookie creation
- `middleware.ts` — checks auth state

**Suspicion:** The cookie is created but never sent...

## Day 2: The Cookie Mystery Deepens
...
```

---

## Commands

| Command | Action |
|---------|--------|
| `QUEST [objective]` | Start new adventure |
| `ENTER [room]` | Go to directory |
| `LOOK` | Describe current room |
| `EXAMINE [object]` | Study a file |
| `COLLECT [clue]` | Add to evidence |
| `DEDUCE` | Form/update hypothesis |

---

## Integration with Cards

[Trading cards](../trading-card/) can be your adventure companions:

```yaml
# Activate helpers for this quest
cards_in_play:
  - card: "Index Owl 🦉"
    goal: "Search for cookie-related code"
    
  - card: "Git Goblin 🧌"
    goal: "Find when session handling changed"
```

---

## Contents

| File | Purpose |
|------|---------|
| [SKILL.md](./SKILL.md) | Full protocol documentation |
| [PROTOTYPE.yml](./PROTOTYPE.yml) | Machine-readable definition |
| [template/](./template/) | Adventure templates |

---

## The Intertwingularity

Adventure is Room with **narrative quest framing**.

```mermaid
graph LR
    AP[⚔️ adventure] -->|IS-A| R[🚪 room]
    AP -->|companions| TC[🎴 trading-card]
    AP -->|logs to| SL[📜 session-log]
    AP -->|similar to| DB[🔧 debugging]
    
    MP[🏛️ memory-palace] -->|sibling of| AP
    R -->|+ quest framing| AP
```

---

## See Also

### Sister Skills
| Skill | Relationship |
|-------|--------------|
| [room/](../room/) | Adventure IS Room + narrative quest framing |
| [memory-palace/](../memory-palace/) | Memory Palace IS Room + mnemonic framing |
| [trading-card/](../trading-card/) | Cards are your **companions** on the quest |
| [debugging/](../debugging/) | Debugging IS investigation quest |
| [research-notebook/](../research-notebook/) | Evidence collection |
| [session-log/](../session-log/) | Adventure LOG.md is session-log variant |

### Protocol Symbols
| Symbol | Link |
|--------|------|
| `ROOM-AS-FUNCTION` | [PROTOCOLS.yml](../../PROTOCOLS.yml#ROOM-AS-FUNCTION) |
| `PLAY-LEARN-LIFT` | [PROTOCOLS.yml](../../PROTOCOLS.yml#PLAY-LEARN-LIFT) — Questing IS playing |

### Narrative Mapping
| Adventure | Investigation | MOOLLM |
|-----------|--------------|--------|
| Quest | Bug hunt | Objective |
| Room | Directory | Context |
| Clue | Evidence | File content |
| Companion | Tool | Card in play |
| Journal | Log | session-log.md |

### Navigation
| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| ⬆️⬆️ Root | [Project Root](../../) |
| 🚪 Sister | [room/](../room/) |
| 🏛️ Sister | [memory-palace/](../memory-palace/) |
| 🔧 Sister | [debugging/](../debugging/) |
