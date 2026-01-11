# 🌍 World Generation

> The world grows where curiosity leads

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Generated rooms follow room patterns |
| [character/](../character/) | Generated NPCs follow character patterns |
| [incarnation/](../incarnation/) | NPCs can become full characters |
| [container/](../container/) | Containers organize generated regions |
| [adventure/](../adventure/) | World generation serves the adventure |
| [party/](../party/) | Questions about companions create them |
| [constructionism/](../constructionism/) | Exploration creates understanding |
| [empathic-templates/](../empathic-templates/) | Smart generation of content |

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

