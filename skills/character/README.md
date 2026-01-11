# 👤 Character

> *"File is identity. Location is presence. Relationships are memory."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [cat/](../cat/) | Feline character patterns |
| [dog/](../dog/) | Canine character patterns |
| [persona/](../persona/) | Identity layers on top of character |
| [room/](../room/) | Where characters live |
| [buff/](../buff/) | Temporary effects on characters |
| [needs/](../needs/) | Sims-style dynamic motivation |
| [mind-mirror/](../mind-mirror/) | Personality system |
| [incarnation/](../incarnation/) | Characters write their own souls |
| [party/](../party/) | Characters in groups |
| [examples/adventure-4/characters/](../../examples/adventure-4/characters/) | Live character catalog |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Core patterns for all characters in MOOLLM. Players, NPCs, companions, cats — all are characters.

## Invocation vs Incarnation

**You can invoke a character without incarnating them.**

| Mode | Where They Exist | Persistence |
|------|------------------|-------------|
| **Invoke** | Chat + session log | Narrative memories |
| **Incarnate** | Own directory | `CHARACTER.yml` soul file |

**Invoke for:**
- A quick conversation ("Ask Minsky about K-lines")
- Adventure companions who accompany the party
- Debate participants around the pie menu table
- The [Annie Hall Protocol](../hero-story/) — experts appear to correct mistakes!

**Incarnate when:**
- Character has become important to the story
- They should persist across sessions/adventures
- They want to author their own soul file
- They need their own home directory

**You can escalate at any time.** Palm started as a ACME catalog entry of a Monkey's Paw, became an order, materialized a full monkey, and finally incarnated with full autonomy.

See: [incarnation/](../incarnation/) for the full ceremony

## Key Concept: Home vs Location

```yaml
player:
  home: characters/don-hopkins/   # FILE never moves
  location: pub/                  # CHARACTER moves
```

## File Belonging

| Type | Home | Example |
|------|------|---------|
| **Belongs** | Room directory | `pub/bartender.yml` |
| **Visits** | Own directory | `characters/don/CHARACTER.yml` |

## Relationships

Key = other entity ID. From is implicit.

```yaml
relationships:
  don-hopkins:
    feeling: "A regular now."
  self:  # Private storage!
    fears: "That I'm not enough."
```

## Quick Commands

| Command | Effect |
|---------|--------|
| `HELLO [char]` | Greet |
| `GOODBYE [char]` | Dismiss |
| `TALK TO [char]` | Converse |


## Tools Required

- `file_read` — Read character state
- `file_write` — Update location, relationships

---

*See [SKILL.md](SKILL.md) for complete specification.*
