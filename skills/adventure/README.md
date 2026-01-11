# ⚔️ Adventure

> *"Every directory is a room. Every file is a clue. Navigation is investigation."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Adventure IS room + narrative framing |
| [character/](../character/) | Player and NPC management |
| [card/](../card/) | Companions on the quest |
| [memory-palace/](../memory-palace/) | Spatial knowledge organization |
| [debugging/](../debugging/) | Investigation as adventure |
| [sniffable-python/](../sniffable-python/) | Linter feedback loop drives generation |
| [examples/adventure-4/](../../examples/adventure-4/) | Live world with 36 rooms |
| [examples/adventure-4/LINTER.yml](../../examples/adventure-4/LINTER.yml) | Validation output for LLM consumption |

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


## Tools Required

- `file_read` — Read rooms and clues
- `file_write` — Update adventure state
- `list_directory` — Survey rooms

---

*See [SKILL.md](SKILL.md) for complete specification.*
