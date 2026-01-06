# PR: Pub Evolution — Stage, Menus, Personas & Performance Framing

## Summary

This PR transforms the Gezelligheid Grotto from a simple pub into a fully-realized social space with layered personas, specialized menus, a theatrical stage, and explicit performance framing that enables ethical impersonation and roleplay.

## Key Changes

### 🎭 The Stage (`pub/stage/ROOM.yml`)

A new sub-room featuring:

- **Physical Space**: 2-foot elevated platform, worn oak planks, faded velvet curtains
- **Theatrical Equipment**: 
  - Old Faithful (haunted spotlight with pac-man filter)
  - The Truth Teller (mic that squeals when you lie)
  - The Mercy Gong (Marieke's judgment made manifest)
  - Box of Wonders (props including Gerald the rubber duck)
  - Hall of Fame signature wall

- **Weekly Schedule with Playable Games**:
  | Day | Event | Games |
  |-----|-------|-------|
  | Moonday | Open Stage | PERFORM, POETRY-SLAM, INTERPRETIVE-DANCE |
  | Treesday | Storytelling Circle | TELL-TALE, CONTINUE-STORY, CHALLENGE-TRUTH |
  | Woodsday | Quiz Night | FORM-TEAM, ANSWER, WAGER |
  | Thundersday | 🎤 Karaoke | SING, DUET, GROUP-NUMBER, KARAOKE-ROULETTE |
  | Freeday | 🎭 Comedy Night | SIGN-UP, PERFORM-SET, CALLBACK, ROAST |
  | Starday | 👑 Drag Night | WERK, LIP-SYNC, DEATH-DROP, WIG-TOSS, CROWD-SURF |
  | Sunday | Jam Session | JAM, START-GROOVE, SOLO, TRADE-FOURS |

- **Performance Framing**: Explicit declaration that the stage is a space where impersonation, acting, and fiction are understood as performance — enabling ethical portrayal of characters while maintaining clear boundaries.

### 👑 Drag Night — "Grotto Glamour"

The crown jewel of entertainment featuring:

- **Regular Performers**:
  - Mevrouw Mysterie (Marieke) — "Gezellig, but make it GORGEOUS"
  - Grim Reapurr (the bartender) — "Death becomes me"
  - Madame Maurice (from the Coatroom) — "The REAL you was in the closet all along"
  - The Terpene Queens (all 8 kittens represented)

- **Performance Moves**: WERK, LIP-SYNC, DEATH-DROP, WIG-TOSS, CROWD-SURF, REVEAL, SPLIT, READ, KIKI

- **Philosophy**: "Drag taught me that we ALL wear masks. Every day. Drag just makes the masks beautiful on purpose."

### 🍽️ Separated Menus (`pub/menus/`)

| Menu | Served By | Themed? |
|------|-----------|---------|
| `drinks.yml` | Bartender | ✅ Changes with pub theme |
| `buds.yml` | Budtender only | ❌ Always Amsterdam authentic |
| `snacks.yml` | Kitchen + bartender | ✅ |
| `games.yml` | Various | ✅ |

### 🌿 Expanded Buds Menu

800+ lines of cannabis culture including:

- **Lucky Strains**: Monkey's Blessing, Postel's Law, YAML Jazz
- **Terpene Family**: 8 strains named for the kittens
- **Diesel Family**: Sour Diesel, NYC Diesel, Chemdawg, etc.
- **Adventure Strains**: Grue Bane, Mind Mirror, Simulation Haze
- **House Blends**: Gezelligheid, Terpie's Choice, Mammie's Pride

Plus character recommendations from every kitten and regular!

### 🎮 Games with Fluxx Variants

Theme-appropriate Fluxx decks:
- Stoner Fluxx (always available)
- Pirate/Fantasy Fluxx (classic adventure)
- Star/Firefly Fluxx (space cantina)
- Zombie/Cthulhu Fluxx (horror night)

### 👤 Layered Persona Stack Model

Characters now support CSS-like persona layering:

```yaml
persona_stack:
  - marieke-core      # Layer 0: Permanent identity
  - budtender         # Layer 1: Job role
  - best-friend       # Layer 2: Situational (switchable)
  - tired             # Layer 3: Temporary (auto-expires)
```

Properties resolve top-to-bottom, enabling dynamic code-switching.

### 🍸 Bartender & Budtender Skills

New prototype skills in `skills/bartender/` and `skills/budtender/`:

- Generic bartending capabilities (POUR, TAKE-ORDER, LISTEN, etc.)
- Budtender inherits bartender + adds cannabis expertise
- **Jimmy Carter Protocol**: TALK-DOWN and HANDLE-WHITEOUT for harm reduction

### 🔧 Technical Cleanup

- Completed `FOO_BAR` → `FOO-BAR` (kebab-case) conversion
- Merged `menu-strains.yml` into `buds.yml`
- Updated bartender.yml to reference skills
- Added VM metadata to `working_set.yml`

## Design Principles Demonstrated

1. **Room-Based Framing**: The stage declares performance context; all contents inherit it
2. **Duplication as Curation**: Games listed in both stage ROOM.yml and games menu — multiple surfaces to discover affordances
3. **Persona vs Character vs Skill**: Clear separation of identity, body, and capability
4. **Ethical AI Representation**: Explicit framing enables impersonation within understood bounds

## Files Changed

```
examples/adventure-4/pub/
├── stage/ROOM.yml (NEW - 720 lines)
├── menus/
│   ├── buds.yml (expanded - 878 lines)
│   ├── drinks.yml
│   ├── snacks.yml
│   ├── games.yml (expanded with stage reference)
│   └── README.md
├── bar/
│   ├── bartender.yml (updated with skill reference)
│   ├── budtender-marieke.yml (persona stack added)
│   ├── ROOM.yml (social boundary clarification)
│   └── cat-cave/
├── pie-table.yml (kebab-case)
└── gong.yml (kebab-case)

skills/
├── bartender/ (NEW)
│   ├── SKILL.md
│   ├── CARD.yml
│   └── README.md
├── budtender/ (NEW - with Jimmy Carter protocol)
│   ├── SKILL.md
│   ├── CARD.yml
│   └── README.md
├── persona/SKILL.md (persona stack model)
└── INDEX.yml (updated)
```

## Testing Notes

- Stage schedule includes strain/drink/snack pairings for each event
- Character recommendations cross-reference menu items
- Drag performers are linked to their "real" character files
- All methods now use kebab-case

## Credits

- Drag night inspiration: Heklina, Trannyshack, Leigh Bowery, Klaus Nomi, Lady Bunny, RuPaul, Sisters of Perpetual Indulgence
- Jimmy Carter Protocol: SNL "Ask President Carter" (1977) — Dan Aykroyd
- Amsterdam coffeeshop culture for authentic cannabis representation
