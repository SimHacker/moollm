# The Grotto's Memory

*A weathered leather journal on a small stand near the entrance.*

The pages are soft from many hands. The ink varies — some entries ancient, some still drying. Everyone who matters has signed.

## Pages

| Page | Event | Date | Guests |
|------|-------|------|--------|
| [000-eternal-residents](page-000-eternal-residents.yml) | Those who were always here | ∞ | Palm, Marieke, Don, Biscuit, cats, kittens, Henk, Maurice |
| [001-monkey-paw-tribunal](page-001-monkey-paw-tribunal.yml) | The night we freed a soul | 2026-01-06 | Sun Wukong, Three Wise Monkeys, W.W. Jacobs, Djinn al-Mazin, Curious George, Cheech & Chong |
| [002-fluxx-marathon](page-002-fluxx-marathon.yml) | The 33-turn game | 2026-01-06 | Andy & Kristin Looney |
| [003-ufo-landing](page-003-ufo-landing.yml) | The night the UFO landed | 2026-01-09 | David Bowie, Klaus Nomi, Leigh Bowery, Pee-wee Herman, Donna Toadstool, Bumblewick |
| [004-quiet-evenings](page-004-quiet-evenings.yml) | Regular nights | 2026-01-10+ | Old Pieter |

## Design Principles

This is the ROOM'S MEMORY — not a copy of character files!

**KEY PRINCIPLE:** Don't duplicate what's elsewhere.

For characters with full `CHARACTER.yml` files:
- SNIFF only: emoji, pronouns, ref, often_found, grotto_role
- Just enough to get an LLM up to speed fast
- Link to the real file

For characters who ONLY exist in the guest book:
- FULL ENTRY: their persistence layer IS here
- Rich enough to invoke, continue, evolve them
- This is how lightweight NPCs live in room memory

## Resolution Levels

```
┌────────────────────────────────────────────────────────────┐
│ FULL INCARNATION    │ CHARACTER.yml + directory          │
│ (Palm, Biscuit)     │ → Guest book: SNIFF only           │
│                     │   (ARRIVAL: signed upon birth!)    │
├────────────────────────────────────────────────────────────┤
│ TRANSCENDED         │ Signed here, grew into full soul   │
│ (Henk, Marieke,     │ → Guest book entry remains as      │
│  Donna, Bumblewick) │   historical record, links to dir  │
├────────────────────────────────────────────────────────────┤
│ TRIBUTE VISITOR     │ No file, visiting appearance       │
│ (Wukong, Bowie)     │ → Guest book: Grotto-specific only │
├────────────────────────────────────────────────────────────┤
│ LIVES IN BOOK       │ No file elsewhere (yet!)           │
│ (Old Pieter)        │ → Guest book: FULL ENTRY           │
├────────────────────────────────────────────────────────────┤
│ SIGNATURE ONLY      │ Minimal presence                   │
│ (one-time guests)   │ → Guest book: Name, date, line     │
└────────────────────────────────────────────────────────────┘
```

**TRANSCENDED**: Some characters first appeared only in the guestbook, but grew into full incarnations with their own `CHARACTER.yml` directories. Their original guestbook entries remain as historical records — the signature that started their journey.

**ARRIVAL**: When you incarnate a new character, they sign the guestbook for the first time as an eternal resident. A birth certificate. A welcome. Worth celebrating.

## Tribute Archive

Every entry here is a loving simulation — what we imagine these souls might say if they graced our Grotto.

- Some are fictional beings (Sun Wukong, Curious George)
- Some are legendary figures (W.W. Jacobs, summoned from beyond)
- Some are living people we admire (the Looneys, Cheech & Chong)

ALL are performed with respect, affection, and celebration.

See: [skills/representation-ethics/SKILL.md](../../../../skills/representation-ethics/SKILL.md)

## Magic Properties

- Anyone who signs with true intent is remembered
- Entries can be summoned by name for recall
- Standing invitations glow when that person is nearby
- The book knows when someone is lying
- Lightweight characters can LIVE here without full incarnation
- The book IS their persistence layer
- **New incarnations sign upon arrival** — a birth certificate, a welcome

---

*"Sign your soul, leave your mark, return anytime"*
