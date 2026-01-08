---
name: character
description: Core patterns for all characters — home, location, relationships, inventory
allowed-tools:
  - read_file
  - write_file
tier: 1
protocol: CHARACTER-AS-ENTITY
tags: [entity, location, relationships, inventory]
related: [persona, room, cat, buff, needs, mind-mirror]
---

# Character

> *"File is identity. Location is presence. Relationships are memory."*

Characters are entities that exist in the world. Players, NPCs, companions, cats — all are characters.

## Home vs Location

**The critical distinction:**

```yaml
player:
  home: characters/don-hopkins/   # Where FILE lives (never moves)
  location: pub/                  # Where CHARACTER is (changes)
```

| Concept | Purpose | Changes? |
|---------|---------|----------|
| **home** | Physical file path | NEVER |
| **location** | Current position in world | Runtime |

**Why:** Stability, safety, git-friendly diffs.

## Directory Structure

### Players (Need Junk Storage)

```
characters/
  don-hopkins/           # Directory name = character ID
    CHARACTER.yml        # The character file
    CARD.yml             # Optional: makes character a playable card
    cookie-1.yml         # Dispensed items
    notes.yml            # Personal stuff
```

### Sidecar Cards

Any character directory can have a `CARD.yml` sidecar to make the character card-playable:

```yaml
# characters/don-hopkins/CARD.yml
card:
  for: ./CHARACTER.yml
  type: hero-story
  tradition: "Pie menus, SimCity, constructionism"
  
  advertisements:
    SUMMON:
      description: "Activate Don's design traditions"
```

See [card skill](../card/SKILL.md#sidecar-cardyml-pattern) for full pattern.

### Embedded NPCs (Room is Home)

```
pub/
  bartender.yml          # Lightweight NPC
  cat-cave/
    terpie.yml           # Full family as single files
    stroopwafel.yml
    kitten-myrcene.yml
```

**Rule:** Need junk storage? → `directory/CHARACTER.yml`. Just a character in a room? → `character-name.yml`.

## File Belonging

> "Does this character BELONG to a place, or VISIT places?"

| Type | Home | Examples |
|------|------|----------|
| **Belongs** | Room directory | `pub/bartender.yml`, `maze/skeleton.yml` |
| **Visits** | Own directory/repo | `characters/don.yml`, `github:user/char.yml` |

## Relationships

Key = other entity ID. From is implicit (file owner).

```yaml
# In marieke.yml
relationships:
  don-hopkins:
    feeling: "A regular now. One of the good ones."
    memories:
      - "The day he sat with Myr for three hours"
    hopes: "I hope he keeps coming back."
    
  self:  # Private inner data!
    identity: "Third generation. This is who I am."
    fears: "That I'm not enough."
    mantra: "The cats need me. I need them."
```

### Targets

Relationships can point to anything:
- Characters (`don-hopkins`)
- Objects (`brass-lamp`)
- Locations (`pub/`, `maze/`)
- Concepts (`acme-corporation`)
- **Yourself** (`self`) — private storage!

### Levels

| Level | Score | Effect |
|-------|-------|--------|
| Stranger | 0-15 | -10% success, 50% effects |
| Familiar | 41-60 | +10% success, 100% effects |
| Friend | 61-80 | +20% success, greetings |
| Soulmate | 91-100 | +50% success, psychic link |

## Inventory (Bidirectional)

Objects stay in their home. Picking up = references, not file moves.

```yaml
# Don picks up kitten:

# In don-hopkins.yml
inventory:
  - pub/cat-cave/kitten-myrcene.yml
  
# In kitten-myrcene.yml
location: characters/don-hopkins/inventory

# File didn't move. Location changed.
```

**Reset:** Snap objects back home: `location = home`.

## Dispensers

Some objects clone on pickup. Original stays, you get instance.

```yaml
# pub/cookie-jar.yml
object:
  id: cookie-jar
  dispenser: true
  instance_template: cookie
```

When picked up:
1. Original stays
2. Instance created: `characters/don-hopkins/cookie-1.yml`
3. Instance inherits from prototype

## Ephemeral vs Persistent

| Type | File? | Use For |
|------|-------|---------|
| **Ephemeral** | No | Quick transaction, one-line dialog |
| **Persistent** | Yes | Ongoing negotiation, relationship state |

**Rule:** Will this matter in 5 minutes? No → ephemeral. Yes → persistent.

## Stats

Two systems:

| System | Scale | Origin |
|--------|-------|--------|
| **Sims Traits** | 0-10 | The Sims 1 |
| **Mind Mirror** | 0-7 | Timothy Leary |

### Sims Traits

- **Neat** — Sloppy ↔ Organized
- **Outgoing** — Shy ↔ Social
- **Active** — Lazy ↔ Energetic
- **Playful** — Serious ↔ Fun-loving
- **Nice** — Grouchy ↔ Kind

**Distribution:** Original Sims used 25 points across 5 traits. Good guideline.

## Commands

| Command | Effect |
|---------|--------|
| `LOOK AT [char]` | Description, visible state |
| `TALK TO [char]` | Conversation based on relationship |
| `HELLO [char]` | Initiate social interaction |
| `GOODBYE [char]` | End interaction, dismiss ephemeral |
| `EXAMINE [char]` | Deeper observation |

## External Homes

Characters can live in other repositories:

```yaml
player:
  home: github:donhopkins/characters/don.yml
  location: pub/
```

## Code Locations

Characters can be "at" a specific line in a file:

```yaml
character:
  name: schema-expert
  home: characters/experts/schema-expert/
  location: "@central/apps/insights/pyleela/brain/Schema.py:142"
  # Currently examining line 142 of Schema.py
```

**Location path syntax for code:**
- `@repo/path/to/file.py` — at a file
- `@repo/path/to/file.py:42` — at specific line
- `@repo/path/to/file.py:42-67` — examining line range
- `@repo/path/dir/` — in a directory (room)

```
> where is schema-expert?
schema-expert is at @central/apps/insights/pyleela/brain/Schema.py:142
examining the createSyntheticItemIfNeeded method
```

See [room/](../room/) for directories as rooms and files as objects.

## Party-Based Code Review

Form parties of expert characters to explore code together:

```
> summon drescher-expert, devops-expert, security-auditor
Party formed: [drescher-expert, devops-expert, security-auditor]

> party: review @central/tools/edgebox/scripts/ingest.py
drescher-expert: "The claim_task function is a schema pattern..."
devops-expert: "The PostgreSQL SKIP LOCKED is elegant..."
security-auditor: "I see proper parameter binding, good..."

> party: focus on lines 280-350
[Multi-perspective analysis of the code section]
```

**Party Navigation:**
```
> go to @central/apps/insights/pyleela/brain/
> enter Schema.py
> look at lines 140-180
> search for "synthetic"
> follow import ExtendedContext
> back
> party: gather here
```

Each party member brings their expertise. The LLM simulates all perspectives in a single call (see [speed-of-light/](../speed-of-light/)).

## Inner Voice (YAML Jazz)

Comments ARE the character's thoughts:

```yaml
needs:
  hunger: 3
  # I could eat. But I'm comfortable here.
  # The kittens are asleep on my lap.
```
