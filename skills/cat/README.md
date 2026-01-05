# 🐱 Cat — The Feline Interaction Skill

> *"Cats are the original NPCs. They have their own agenda."*

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Universal feline interactions that cat instances overlay with their personalities. Creates personalized charm/buff/curse effects.

**Philosophy:** Cats are not decoration. They're gameplay.

## Quick Commands

| Command | Risk | Effect |
|---------|------|--------|
| `PAT [cat]` | Low | Minor charm |
| `PET [cat]` | Medium | Mood boost |
| `SCRITCH [cat]` | Medium | Requires knowing preferences |
| `BELLY [cat]` | **HIGH** | The forbidden zone (trust test) |
| `PLAY WITH [cat]` | Low | Mutual joy |
| `SLOW BLINK [cat]` | None | Feline I-love-you |
| `PSPSPS` | None | Summon nearby cats |
| `SNIFF [cat]` | Low | Bidirectional info exchange |
| `LICK [cat]` | Medium | Usually cat-initiated |
| `BOOP [cat]` | Low | Nose boop greeting |

## Bidirectional Interactions

SNIFF, LICK, and BOOP go both ways — you can do them to cats, cats can do them to you, and cats do them to each other. See [SKILL.md](SKILL.md) for full cat-to-cat and cat-to-human interactions.

## Relationship Levels

| Level | Points | Effect Mod | Cat Behavior |
|-------|--------|------------|--------------|
| Stranger | 0-10 | 50% | Cautious |
| Familiar | 26-50 | 100% | Comfortable |
| Friend | 51-75 | 125% | Seeks attention |
| Bonded | 76-90 | 150% | Follows you |
| Soulmate | 91-100 | 200% | Psychic connection |

## Terpene Effects (Kittens)

| Kitten | Effect | Duration |
|--------|--------|----------|
| Myr | DEEP RELAXATION | 30 min |
| Lemon | JOY INFUSION | 45 min |
| Lily | PEACEFUL PRESENCE | 1 hour |
| Pine | SHARP CLARITY | 2 hours |
| Carrie | GUARDIAN'S RESOLVE | 1 hour |
| Hops | REFINED STANDARDS | 45 min |
| Terpy Jr. | CHAOS MUSE | ??? |
| Ocie | FRESH START | 30 min |
| **All 8** | **ENTOURAGE EFFECT** | Legendary |

## Live Examples

See the [Gezelligheid Grotto](../../examples/adventure-3/pub/README.md) for 10 cats using this skill.

## Related Skills

- [character/](../character/) — Cats are characters
- [buff/](../buff/) — Cat effects as buffs
- [mind-mirror/](../mind-mirror/) — Personality determines charms
- [room/](../room/) — Cats belong to locations

## Tools Required

- `file_read` — Read cat definitions
- `file_write` — Update relationships

---

*See [SKILL.md](SKILL.md) for the complete specification including all interactions, relationship mechanics, terpene details, and cat-to-cat behaviors.*
