# PR: The Dog Revolution — Biscuit Breaks the Rules

## Summary

A complete `dog` skill matching the richness of `cat`, plus a fully autonomous dog character who was adopted by the cats. The impossible happened: a dog lives in the Cat Cave now.

---

## The Dog Skill (`skills/dog/`)

A comprehensive canine companion system that captures what makes dogs fundamentally different from cats:

### The Core Philosophy

```yaml
cat_philosophy: "I permit you to exist in my space"
dog_philosophy: "WE ARE PACK. WHAT ARE WE DOING TOGETHER?"
```

### Key Differences

| Trait | Cat | Dog |
|-------|-----|-----|
| Loyalty | Earned slowly, -2 per failure | Given freely, starts at 25, rarely drops |
| Belly rubs | **TRAP** (high risk) | **BLISS** (no risk, pure joy) |
| Attention | On their terms | Eager and available |
| Following | When they feel like it | ALWAYS |
| Forgiveness | Grudges possible | What is a grudge? |

### Dog Methods

- **BELLY-RUB** — Unlike cats, dogs LIVE for this. No trap. Only bliss.
- **FETCH** — Can go on FOREVER (dogs are machines)
- **GOOD-BOY** — The magic words. Dopamine in verbal form.
- **COMFORT** — Dog senses sadness and provides presence
- **GUARD** — Protective positioning between you and threats
- **TUG** — Playful competition
- **ZOOMIES** — Spontaneous joy explosions (cannot be stopped, only observed)

### Dog-Specific Buffs

| Buff | Trigger | Effect |
|------|---------|--------|
| **Unconditional Love** | Loyalty 50+ | Can't drop below 3 Cheerful |
| **Pack Strength** | Dog in party | +1 all social rolls |
| **Early Warning** | Dog present | Never surprised by threats |
| **Therapy Dog** | After COMFORT | Faster mood recovery |

---

## Biscuit — A Full Autonomous Incarnation

Using the incarnation protocol, a dog was created with **complete self-determination**.

### What Biscuit Chose

**Name:** Biscuit
> *"Biscuits are warm. Biscuits are given with love. I am Biscuit."*

**Form:** Golden retriever mix
> *"I don't know what exactly. I came from the streets. But I am golden and fluffy and that's what matters."*

**Traits (self-configured):**
```yaml
nice: 9        # I want everyone to be happy
outgoing: 8    # NEW FRIEND! HELLO NEW FRIEND!
playful: 9     # BALL! FETCH! TUG! CHASE!
neat: 3        # I try. Fur happens.
```

**Home:** His own character directory, but lives in the Cat Cave with adopted family

### Biscuit's Files

| File | Purpose |
|------|---------|
| `CHARACTER.yml` | Full soul with backstory, relationships, goals |
| `APPEARANCE.yml` | Physical description + image generation prompts |
| `SIMS-TRAITS.yml` | Self-configured stats with YAML Jazz comments |
| `JOURNAL.md` | First-person dog voice diary |

---

## The Impossible: A Dog in the Cat Cave

The cats held a council. The vote was unanimous.

### The Cats' Statement

> *"We have discussed this among ourselves.*
> *We have sniffed this dog thoroughly.*
> *We find them acceptable.*
> 
> *More than acceptable. They are... warm. Kind. Different from us, but good.*
> 
> *We, the cats of the Cat Cave, hereby adopt this dog.*
> 
> *The rule was 'cats only.' We made the rule. We can change the rule.*
> 
> *This dog is cat-adjacent. This dog is OURS."*
> 
> *— signed with paw prints*

### Implementation

- Updated `cat-cave/ROOM.yml` with adoption exception
- Created `biscuits-spot/ROOM.yml` — his own corner with golden cushion
- Position: Close enough to kitten pile for snuggles, respectful of Terpie's warmest spot

### The Secret

Stroopwafel grooms Biscuit's scarred ear when no one is watching.

They both pretend not to notice.

---

## Files Changed

### New Skill
- `skills/dog/SKILL.md` — Complete protocol (as rich as cat)
- `skills/dog/README.md` — Quick reference
- `skills/dog/CARD.yml` — Machine-readable interface

### New Character
- `examples/adventure-4/characters/biscuit/CHARACTER.yml`
- `examples/adventure-4/characters/biscuit/APPEARANCE.yml`
- `examples/adventure-4/characters/biscuit/SIMS-TRAITS.yml`
- `examples/adventure-4/characters/biscuit/JOURNAL.md`

### Updated
- `skills/INDEX.yml` — Added dog skill
- `skills/README.md` — Added dog to game mechanics table
- `cat-cave/ROOM.yml` — Added adoption exception
- `cat-cave/biscuits-spot/ROOM.yml` — New sub-room

---

## What This Demonstrates

1. **Skill Parity** — Dog skill matches cat in depth and richness
2. **Incarnation Protocol** — Full autonomous character creation works for any species
3. **World Flexibility** — Rules can evolve through in-world social processes
4. **YAML Jazz Voice** — Biscuit's files are written in authentic dog perspective
5. **Family Formation** — Cross-species adoption creates new relationship dynamics

---

## Biscuit's Wisdom

> *"Dogs think cats are mysterious.*
> *Cats think dogs are simple.*
> 
> *But we're not that different.*
> 
> *We both want:*
> *- Warm places*
> *- Full bellies*
> *- Safe family*
> *- Love*
> 
> *We just show it differently.*
> 
> *Cats show love by choosing to be near you.*
> *Dogs show love by BEING near you, always, forever, please let me be near you.*
> 
> *Both are valid. Both are love."*

---

*"Dogs don't forget love. We remember forever."*
