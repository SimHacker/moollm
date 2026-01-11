# 🐕 Dog — The Canine Companion Skill

> *"Dogs are the opposite of cats. They have YOUR agenda."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [cat/](../cat/) | The feline counterpart |
| [character/](../character/) | Dogs are characters |
| [buff/](../buff/) | Dog effects as buffs |
| [mind-mirror/](../mind-mirror/) | Personality determines behavior |
| [party/](../party/) | Dogs as companions |
| [examples/adventure-4/characters/animals/](../../examples/adventure-4/characters/animals/) | Animal character directory |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | Dog adopted by cat cave |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Universal canine interactions where personality creates unique effects, but dogs fundamentally want to help, please, and be part of your pack.

**Philosophy:** Dogs are not just pets. They're partners.

## The Fundamental Difference

| Trait | Cat | Dog |
|-------|-----|-----|
| Loyalty | Earned slowly | Given freely |
| Attention | On their terms | Eager and available |
| Buff trigger | Successful interaction | Simply being present |
| Following | When they feel like it | ALWAYS |

## Quick Commands

| Command | Risk | Effect |
|---------|------|--------|
| `PAT [dog]` | None | Almost always works |
| `BELLY RUB [dog]` | **None** | Dogs LOVE this |
| `SCRITCH [dog]'S EARS` | None | Calm lean-in |
| `PLAY FETCH WITH [dog]` | Low | Mutual joy, possibly infinite |
| `TUG WITH [dog]` | Low | Playful competition |
| `GOOD BOY [dog]` | None | **MAGIC WORDS** |
| `SPEAK [dog]` | None | Bark or howl |

## Dog-Initiated Interactions

| Behavior | Meaning |
|----------|---------|
| **Play Bow** | "Let's play!" |
| **Zoomies** | Pure uncontrollable joy |
| **Head Tilt** | "What? What does that mean?" |
| **Comfort** | Dog senses your sadness |
| **Guard** | Protective positioning |

## Loyalty Levels (Not Trust!)

| Level | Points | Dog Behavior |
|-------|--------|--------------|
| New Friend | 0-25 | Excited about you |
| Good Friend | 26-50 | Seeks you out |
| Best Friend | 51-75 | Follows everywhere |
| Bonded | 76-90 | Protective, anticipates needs |
| Soulmate | 91+ | Psychic connection |

**Key:** Dogs start at 25 and forgive everything. Loyalty almost never drops.

## Special Buffs

| Buff | Effect |
|------|--------|
| **Unconditional Love** | Can't drop below 3 Cheerful |
| **Pack Strength** | +1 all social rolls |
| **Early Warning** | Never surprised |
| **Therapy Dog** | Faster mood recovery |

## Dog + Cat Cohabitation

```yaml
cat_perspective: "This large loud creature is... acceptable. It provides warmth."
dog_perspective: "CATS! MY BEST FRIENDS! I LOVE THEM! WE ARE FAMILY!"
```

## Live Examples

See the [Gezelligheid Grotto](../../examples/adventure-4/pub/README.md) for a dog adopted by the cat cave.

## Tools Required

- `file_read` — Read dog definitions
- `file_write` — Update relationships

---

*See [SKILL.md](SKILL.md) for complete specification including all interactions, loyalty mechanics, and emotional support behaviors.*
