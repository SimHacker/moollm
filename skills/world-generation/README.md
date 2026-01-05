# 🌍 World Generation

> The world grows where curiosity leads

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Dynamic world creation — the world grows as you explore. Nothing exists until needed. Questions create places.

## Triggers

| Trigger | Example |
|---------|---------|
| Questions | "Where did grue come from?" → creates homeland |
| Statements | "There must be a library!" → maybe creates it |
| Actions | DIG → tunnel, CLIMB → passage |
| Quests | Objective generates location |

## Directory Patterns

| Directory | Character |
|-----------|-----------|
| maze/ | Dark, grue, twisty |
| tower/ | Height, wind, views |
| garden/ | Outdoor, weather, bugs |
| library/ | Books, knowledge, quiet |

## NPC Containers

Sub-directories can hide NPCs that emerge by changing their `location`:
- `cat-cave/` — cats come out when wanted
- `guard-house/` — guards patrol when needed

## Related Skills

- [room](../room/) — generated rooms follow room patterns
- [character](../character/) — generated NPCs follow character patterns
- [adventure](../adventure/) — world generation serves the adventure
