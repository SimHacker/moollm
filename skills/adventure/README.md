# ⚔️ Adventure

> *"Every directory is a room. Every file is a clue. Navigation is investigation."*

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Transform exploration into narrative investigation. Directories become rooms, files become clues, and the LLM dungeon-masters you through the quest.

**Lineage:** Colossal Cave, Zork, LambdaMOO, The Sims.

## Quick Commands

| Command | Effect |
|---------|--------|
| `QUEST objective` | Start adventure |
| `ENTER room` | Go to directory |
| `LOOK` | Describe room |
| `EXAMINE object` | Study file |
| `COLLECT clue` | Add evidence |
| `SELECT character` | Control who |
| `CYCLE` | Next character |

## When to Use

- **Codebase archaeology** — "Find where the auth bug was introduced"
- **Onboarding** — "Understand this project's structure"
- **Bug hunting** — "Follow the evidence trail"
- **Documentation diving** — "What does this system actually do?"

## Templates

| File | Purpose |
|------|---------|
| [ADVENTURE.yml.tmpl](ADVENTURE.yml.tmpl) | Quest state & evidence |
| [LOG.md.tmpl](LOG.md.tmpl) | Narrative journal |

## Related Skills

- [room/](../room/) — Adventure IS room + narrative framing
- [memory-palace/](../memory-palace/) — Spatial knowledge organization
- [card/](../card/) — Companions on the quest
- [debugging/](../debugging/) — Investigation as adventure
- [character/](../character/) — Player and NPC management

## Tools Required

- `file_read` — Read rooms and clues
- `file_write` — Update adventure state
- `list_directory` — Survey rooms

---

*See [SKILL.md](SKILL.md) for complete specification.*
