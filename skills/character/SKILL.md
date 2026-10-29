---
name: character
description: Core patterns for all characters — home, location, relationships, inventory
allowed-tools:
  - read_file
  - write_file
tier: 1
protocol: CHARACTER-AS-ENTITY
related: [soul, mind, cat, dog, society-of-mind, persona, room, buff, needs, mind-mirror, incarnation, party, representation-ethics]
tags: [moollm, entity, location, relationships, inventory, identity]
---

# Character

> *"File is identity. Location is presence. Relationships are memory."*

Ethics: [ETHICS.md](ETHICS.md) · [soul/ETHICS.md](../soul/ETHICS.md) · [mind/ETHICS.md](../mind/ETHICS.md) · [representation-ethics](../representation-ethics/)

Characters are entities that exist in the world. Players, NPCs, companions, cats — all are characters.

## The Prototype Character

[`CHARACTER.yml`](CHARACTER.yml) in this skill is the prototype character. Every
`CHARACTER.yml` inherits it as its implied parent, so a character states only what makes it
itself: name, description, home, location, and whatever differs.

| From the prototype | Value |
|---|---|
| `type` | `character` |
| `inventory`, `buffs` | empty |
| `relationships` | empty |
| `sims` | Sims 1 person_data defaults: traits 5, skills 0, needs 50, unemployed |
| `mind_mirror` | empty; an absent property is neutral (4) |
| `methods` | STATUS, MOVE, TAKE, DROP, WEAR, REMOVE-PERSONA, RELATE, SNIFF, LICK, GREET, CUDDLE |

A map the character states replaces the prototype's whole: a character with `sims:` of its
own does not get the prototype's needs filled in by lookup. A character that extends another
(a private layer over a public one) says `inherits: [path/to/public/]`; lookup reads the
character, then that parent, then the prototype.

A character's own `GLANCE.yml` keeps at least `name`, `description` and `location`.

### Facts, not verdicts

A character file records what is true of the character and leaves judgments to whoever
judges. `lighting:` belongs to a room and the grue decides whether it hunts there; a
character carries a lamp, not a `grue_safe: true`. The same goes for trust, danger and
taste: store the observation, let the observer's rules decide.

## Layers

One being can have a tree of incarnations, one layer per purpose and repo. Palm plays in
moollm's adventure-4, has a profile and a cast entry in WillWrightShowForFood, and sits in
the audience of two repo shows. A real person has a biography layer in DonHopkins, an
invitation or memorial layer in a show repo, and sometimes a published page. Each layer runs
alone as far as it can, so each carries the core keys and the representation ethics itself
([constitution §15](../../kernel/constitution-core.md#15-the-semantic-image-pyramid-concentrated-not-dry-universal)).
The schema, with defaults, aliases and worked examples, is the `schema:` key of
[`CHARACTER.yml`](CHARACTER.yml).

### Core keys

| Key | Default when omitted |
|---|---|
| `id` | the directory name; the same in every layer |
| `name` | none: every layer states it |
| `real_being` | `false` if `status: fictional` or `layer` is `adventure`, `cast` or `prototype`; otherwise `true`, including when `layer` is absent |
| `status` | `living`, `deceased` or `fictional`: a life fact. Omitted: `fictional` for a non-real being, otherwise unknown and treated as living |
| `born`, `died` | absent; dates agree at the lower precision (`1940` and `1940-05-17`) |
| `signifier` | 👤 living or unknown, 🕯️ deceased, 🎭 fictional (🤖 robot or AI). A topical emoji goes in `emoji:` |
| `type` | `character`. The being's kind (person, animal, robot, ai_agent, a species) or role in play (player, npc) |
| `layer` | from the file's location: `adventure`, `prototype`, `biography`, `profile`, `invitation`, `memorial`, `dream_guest`, `cast`, `audience`, `page` |
| `representation.authored_by` | unattributed, which the lint reports for a real being. The being's own id means self-authored |
| `representation.public_figure` | unknown, treated as private (the stricter rule); the lint reports it for a living real being |
| `representation.consent` | `{ state: not_asked }`. `state` is `not_asked`, `asked`, `granted`, `declined`, `revoked` or `unverified`, with `scope`, `date`, `evidence`, `note` |
| `representation.governed_by` | `skills/real-being/` and `skills/representation-ethics/` for a real being |

Every omitted value errs toward caution for a real person. A real person in an adventure,
cast or prototype layer states `real_being: true`; the cross-layer lint reports one that
doesn't when another layer of the same id says it is real.

A layer states facts and never the rule. The rule that governs the portrayal is the first of
memorial (`status: deceased`), self_authored, consented (`consent.state: granted` with
`consent.evidence`), public_figure, private; its lists are in
[REPRESENTATION.yml](../representation-ethics/REPRESENTATION.yml). `granted` without evidence
governs nothing. Warmth (old friend, warm lead) goes in `consent.note`, never in `state`.
`representation.consent` is also the invitation's answer; `invitation.status` is a work status
validated against the show repo's `schemas/invitation-workflow.yml`. A life fact, a consent
record and a work status: three keys.

### Three relations

| Key | Relation | Read by |
|---|---|---|
| `inherits:` | lookup: slots this layer lacks come from that layer | lookup, like any parent |
| `derived_from:` | authoring: this layer was projected from that one; `copies:` lists the keys that must agree | the cross-layer lint |
| `layers:` | navigation: the being's other layers, keyed by layer | readers; linted against what is on disk |

```yaml
# WillWrightShowForFood/characters/alan-kay/CHARACTER.yml
id: alan-kay
name: Alan Kay
type: person
layer: invitation
status: living
born: "1940-05-17"
signifier: "👤"
emoji: "💡"
representation:
  authored_by: don-hopkins
  public_figure: true
  consent: { state: not_asked }
  governed_by: [../../schemas/portrayal-standards.md]
derived_from:
  - ref: moollm://github/SimHacker/DonHopkins/characters/alan-kay/
    transform: "projected for the show: adds the invitation, sources and people to discuss"
    copies: [name, status, born, died, representation.public_figure, representation.consent.state]
layers:
  biography: moollm://github/SimHacker/DonHopkins/characters/alan-kay/
```

`relationships:` is a map of id → `{type, narrative}` (plus `feeling`, `memories`, `hopes`);
`relationship:` is prose about this layer's tie to its author or show.

Across repos a reference is `moollm://github/<owner>/<repo>/<path>`, resolved to a sibling
checkout or a GitHub URL. `inherits:` never points from a public repo into a private one; a
public layer may name a private layer in `derived_from:` or `layers:` by ref only.

### Older spellings

| Older | Canonical |
|---|---|
| `character:` envelope | flat |
| `character_ref:`, `moollm_source:`, `wwsff_local:`, `canonical_soul:`, `prototype_ref:`, `canonical_home:`, `moollm_home:` | `inherits:` |
| `inherits: {repo, path, absolute_url, ...}` | `inherits: [moollm://github/<owner>/<repo>/<path>]` |
| `inherits: {moollm_skills: [...]}` | the skill ids as further `inherits:` entries |
| `upstream:` | `derived_from:` |
| `menagerie:`, `profile_home:`, `wwsff_overlay.audience_fork` | `layers:` |
| `representation.protocol:` | `representation.governed_by:` |
| `representation.consent_level` (also `consent_level:`, `5_deceased_legacy`, `self-sovereign`) | retired: 1 → `authored_by` is the being; 2 → `consent.state: granted` with evidence, else `unverified`; 3 → `public_figure: true`; 4 → `public_figure: false`; 5 → `status: deceased` |
| `invitation.consent: not_yet_asked`, `awaiting_reply`, `invitation_accepted` | `representation.consent.state: not_asked`, `asked`, `granted` |
| `type: invitation`, `memorial`, `representational`, `audience_member` | `layer:`; `type:` takes the being's kind |
| `connections:`, `friends:` | `relationships:` |
| `status: memorial`, `status: passed` | `status: deceased` |

## Home vs Location

**The critical distinction:**

```yaml
# characters/don-hopkins/CHARACTER.yml
home: characters/don-hopkins/   # Where FILE lives (never moves)
location: pub/                  # Where CHARACTER is (changes)
```

| Concept | Purpose | Changes? |
|---------|---------|----------|
| **home** | Physical file path | NEVER |
| **location** | Current position in world | Runtime |

**Why:** Stability, safety, git-friendly diffs.

## Character State Ownership (CANONICAL vs MIRROR)

**Characters own their own state.** The CHARACTER.yml file is CANONICAL for:

| State | Stored In | Notes |
|-------|-----------|-------|
| `location` | CHARACTER.yml | Where the character is in the world |
| `inventory` | CHARACTER.yml | What the character carries |
| `gold` | CHARACTER.yml | Character's resources |
| `sims` | CHARACTER.yml | Sims 1 traits, skills, needs |
| `mind_mirror` | CHARACTER.yml | Personality (Leary-style) |
| `relationships` | CHARACTER.yml | Who they know and feel about |
| `memories` | CHARACTER.yml | What they remember |

**ADVENTURE.yml (or other world state files) may MIRROR some state for convenience**, but CHARACTER.yml is always the source of truth.

```yaml
# CHARACTER.yml (CANONICAL — edit this first)
location: coatroom/  # CANONICAL — character owns their location
inventory: [lamp]    # CANONICAL — character owns their inventory

# ADVENTURE.yml (MIRROR — optional convenience copy)
player:
  location: coatroom/  # Mirror of CHARACTER.yml
```

**When updating state:**
1. Edit CHARACTER.yml first (canonical)
2. Optionally update ADVENTURE.yml mirror for convenience
3. If conflict, CHARACTER.yml wins

**Why this matters:**
- Characters can be used across multiple adventures
- Character state persists independent of adventure state
- Clear ownership prevents conflicts

## Directory Structure

### Players (Need Junk Storage)

```
characters/
  don-hopkins/           # Directory name = character ID
    CHARACTER.yml        # The character file
    CARD.yml             # Optional: makes character a playable card
    QUOTES.yml           # Optional: notable quotes (standard pattern)
    cookie-1.yml         # Dispensed items
    notes.yml            # Personal stuff
```

### Sidecar Cards

Any character directory can have a `CARD.yml` sidecar to make the character card-playable:

```yaml
# characters/don-hopkins/CARD.yml — a view of the character directory
subject*: ..       # the character; slots this card lacks come from there
format*: card
type: hero-story
tradition: "Pie menus, SimCity, constructionism"

advertisements:
  SUMMON:
    description: "Activate Don's design traditions"
```

See [card skill](../card/SKILL.md#sidecar-cardyml-pattern) for full pattern.

### QUOTES.yml (Optional)

Characters with notable quotes can have a `QUOTES.yml` file:

```yaml
# characters/don-hopkins/QUOTES.yml
meta:
  attributed_to: "Don Hopkins"
  uname: "Don"  # password: Don
  attribution_format: '💬 "[quote]" — Don Hopkins (date, source)'

# Categories organized to fit the character
design_philosophy:
  - quote: "The problem is not getting new ideas, it's getting rid of old ones."
    date: "2015"
    source: "HN comment"
    tags: [design, innovation]
    
programming:
  - quote: "Pie menus are faster because moving in a direction is easier than targeting."
    date: "1991"
    source: "CHI paper"
    tags: [ui, pie-menus]
```

**Standard base keys per quote:**
- `quote` — The text
- `date` — Year or YYYY-MM-DD  
- `source` — Where it came from
- `link` — Verification URL (when available)
- `tags` — Searchable tags

**Optional YAML Jazz keys:**
- `note` — Editorial commentary
- `context` — What prompted this quote
- `significance` — Why it matters
- `humor` — Is it meant to be funny?

**For extensive quote collections** (like RMS), QUOTES.yml is the ROOT pointing to auxiliary files:

```yaml
auxiliary_files:
  natalism-flame-1993.yml:
    description: "The legendary kabuki-west exchange"
    parrot_can_squawk: true
  controversial-quotes.yml:
    description: "Documented but prohibited"
    parrot_can_squawk: false  # EXPLICIT PROHIBITION
```

**See:** [tmnn7-8 StIGNUcius QUOTES.yml](https://github.com/SimHacker/tmnn7-8/tree/main/analysis/characters/StIGNUcius/QUOTES.yml) for an exemplary implementation.

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

## Inventory Protocol (Objects vs Refs)

Items in inventory can be **OBJECTS** or **REFS**:

| Type | Weight | Bulk | What It Is |
|------|--------|------|------------|
| **Object** | Yes | Yes | The actual item (lamp, sword, lunchbox) |
| **Ref** | No | No | Lightweight pointer to a prototype |

**Refs are perfect for:** catalogs, manuals, maps, guides — things you reference but don't physically carry.

```yaml
inventory:
  # Full object
  - item: "Brass Lantern"
    type: object
    source: start/lamp.yml
    weight: 2
    fuel: 100
    
  # Lightweight ref
  - item: "ACME Catalog"
    ref: street/lane-neverending/w1/acme-catalog.yml
    annotations: ["circled portable hole", "margin notes on physics"]
```

### Dispenser Protocol

Some objects dispense **refs** (like the ACME Catalog Dispenser):

1. TEAR OFF / TAKE at dispenser
2. Receive REF in inventory (weight: 0)
3. REF points to prototype for full content
4. REF can accumulate instance-specific data (annotations, condition)

### Drop Protocol

When dropping a ref in a room:

1. Remove from inventory
2. Create pointer file in room directory: `[item-name].yml`
3. Pointer contains: `inherits:` the catalog, dropped_by, condition, annotations
4. Item now lives in that room (can be picked up again)

```yaml
# kitchen/acme-catalog.yml — dropped instance
inherits: [../street/lane-neverending/w1/acme-catalog.yml]
origin: "Torn from dispenser at 4 Lane Neverending"
dropped_by: "don-hopkins"
annotations: ["DO NOT ORDER Rocket Skates", "circled portable hole"]
```

### Capacity

```yaml
inventory_capacity:
  max_weight: 45    # Varies by character
  max_bulk: 10
  refs_free: true   # Refs don't count!
```

## Dispensers (Full Objects)

Some objects clone **full objects** on pickup. Original stays, you get instance.

```yaml
# pub/cookie-jar.yml
name: "Cookie Jar"
clones: ./cookie.yml     # what TAKE hands out; the jar is not the cookie's parent
```

When picked up:
1. Original stays
2. Instance created: `characters/don-hopkins/cookie-1.yml`
3. Instance file says `inherits: [pub/cookie.yml]` and holds only what differs

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
home: github:donhopkins/characters/don.yml
location: pub/
```

## Code Locations

Characters can be "at" a specific line in a file:

```yaml
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

## Motivation as Declared, Not Felt

**Important distinction:** When CHARACTER.yml specifies `motivations`, `goals`, or `needs`, these are *declarative descriptions* — they tell the LLM how to roleplay this character.

The LLM does not *genuinely want* to achieve these goals. It *performs* wanting them.

```yaml
motivations:
  - protect_the_kittens     # Declared, not felt
  - find_good_food          # The LLM roleplays caring about this
  - explore_new_places      # No intrinsic drive — just character data
```

**Why this matters:**
- No genuine agency — the character is a simulacrum
- Roleplay all the way down (Shanahan)
- Declared motivations are performed, not experienced
- This is fine when acknowledged, problematic when mistaken for genuine will

**See:** [representation-ethics/examples/aggregate-patterns.yml](../representation-ethics/examples/aggregate-patterns.yml) for the distinction between aggregate simulation (valid) and individual prediction (not valid).

**K-line:** `MOTIVATION-ROLEPLAY`

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/character/](https://github.com/SimHacker/moollm/tree/main/skills/character)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
