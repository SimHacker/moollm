---
name: card
description: Portable tokens of capability, identity, and access
allowed-tools:
  - read_file
  - write_file
  - list_dir
tier: 1
protocol: TRADING-CARD
related: [skill, prototype, room, character, party, soul-chat, adventure, multi-presence, advertisement, return-stack]
tags: [moollm, gamification, capabilities, portable, actor]
templates:
  - file: CARD.yml.tmpl
    purpose: Individual card template
  - file: COLLECTION.yml.tmpl
    purpose: Card collection template
---

# Card

> **Portable tokens of capability, identity, and access.**

Cards are templates. Put them "in play" in a [room](../room/) to activate them.

> [!TIP]
> **Hero-stories.** Actors. Safe pointers to wisdom. No risks of impersonation, just tribute, storytelling, skill sharing and composing.

---

## The Card Pun Stack — What A CARD Is

"Card" elegantly puns across a stack of well-proven computing concepts. MOOLLM's CARD sits at the intersection of all of them, and borrows from each. Take the richness as intentional:

| Lineage | What it contributes | How it shows up in `CARD.yml` |
|---|---|---|
| 🎴 **HyperCard** (Bill Atkinson, 1987) | A card as a **self-contained navigable unit** with fields, buttons, scripts — a little interactive object you can page through, link to, and stack. "Everything is a card." | `card:` identity, `navigation:`, `advertisements:` that surface actions the way HyperCard buttons did |
| 💾 **Type Library / IDL / ActiveX / OLE Control** (Microsoft, 1990s) | **Dispatch metadata** describing an object's interface: its methods, properties, events, IDs. Binary in COM; human-readable YAML for us. | `methods:`, `state:`, `k_lines:` (our stand-in for UUIDs), `inherits:` (analog to COM aggregation) |
| 🎭 **Actor** (Hewitt 1973; Agha 1986) | A **message-receiving autonomous entity** with its own state, responding to messages by sending messages or changing state. Concurrency is inherent. | The whole card is an actor signature; advertisements describe the messages this actor handles |
| 🧵 **Thread / Process** | A **unit of control** with its own identity, lifecycle, and dispatchable surface. | Cards are dispatchable in parallel; `state:` is the actor-thread's local memory |
| 📬 **Message Dispatching Surface** (Smalltalk/Self/Objective-C) | The OO insight: methods aren't called, **messages are sent**, and the receiver decides what to do. Late binding, polymorphism, duck typing. | `methods:` ≠ functions; they're the messages this card responds to. DOP delegation composes dispatch across parent cards. |
| 🃏 **Trading / Playing Card** | **Portable token of identity and capability** — you collect them, play them, trade them. Front = identity/rarity; back = mechanical rules. | `rarity:`, `tier:`, `emoji:`, `tagline:`, the whole collectible ethos (hero-stories, soul-chat) |
| 🎯 **Business Card / Index Card** | **Sniffable surface.** Hand it to someone, they know who you are, how to reach you, what you do. | `tagline:`, `description:`, the entire "sniffable interface" framing |

A CARD is **all of these at once** — that's the design, not accident. When you encounter a `CARD.yml`, you're looking at:

- an **interface definition** (like IDL) describing a dispatchable surface,
- a **HyperCard** you can navigate to, activate, and page through,
- an **actor signature** describing a message-receiving entity with local state,
- a **type library entry** in a distributed, human-readable, zero-ceremony registry (the filesystem itself),
- a **collectible token** with rarity, identity, and portability, and
- a **business card** you can hand to a reader (human or LLM) to say "this is what I am and what I do."

The richness is load-bearing. Every time you write `methods:`, `advertisements:`, `k_lines:`, or `inherits:`, you're simultaneously:

- declaring an interface (IDL-style),
- describing an actor's message-handling surface (Hewitt-style),
- exposing navigation/activation triggers (HyperCard-style),
- publishing metadata that tooling and LLMs can sniff without execution (TypeLib-style),
- presenting a portable token of identity (trading-card-style).

This is why a CARD-only directory (no `SKILL.md`) is already a first-class dispatchable object. The CARD isn't documentation for the skill — it **is** the skill's interface, actor, card, type library, and business card rolled into one YAML file.

> 💡 *The other meta-skills (`skill`, `prototype`, `schema`, `file-system-object`) each name one aspect of the MOOLLM object system. `card` names the interface-and-actor surface itself — the CARD is the handle by which everything else is invoked.*

---

## 📑 Index

**Architecture**
- [The Card Pun Stack — What A CARD Is](#the-card-pun-stack--what-a-card-is)
- [What a CARD carries](#what-a-card-carries) — the standard keys, defaults, copy-down, projection
- [Card Architecture](#card-architecture) — The most important section!
- [Recommended Section Order](#recommended-section-order)
- [What Goes Where](#what-goes-where)
- [Advertisements Before Methods](#advertisements-before-methods)
- [Method Placement Rules](#method-placement-rules)

**Card Types**
- [What's a Card?](#whats-a-card)
- [Sidecar Pattern](#sidecar-cardyml-pattern)
- [Card Types](#card-types)

**Mechanics**
- [Activation Records](#activation-records)
- [Card State](#card-state)
- [Collections](#collections)

---

## What a CARD carries

`CARD.yml` is the one file a model reads to learn what an object does
([constitution §15](../../kernel/constitution-core.md#15-the-semantic-image-pyramid-concentrated-not-dry-universal)).
The standard is the `schema:` section of [CARD.yml](CARD.yml): every key's shape, default,
meaning and aliases, in the format of
[SCHEMA.md § Schema files](../../designs/object-system/SCHEMA.md#schema-files).

### One file, concentrated, not DRY

A card holds the object's advertisements, methods, k-lines, state, Dublin Core, card face,
relations and its own YAML Jazz, all in one file. There is no `ADVERTISEMENTS.yml`,
`METHODS.yml` or `K-LINES.yml` beside it. A directory with several interfaces (`ROOM.yml` and
`CHARACTER.yml`) still has one CARD, and every interface feeds it.

Repeating a key that `SKILL.md`, an interface file or the prototype file already has is the
point, not a defect. Never remove something from a card because a larger file says it; ask
whether it is among the most important things at card size. Lint keeps the copies in
agreement; the fix for a disagreement is updating the copy.

### The keys

| Group | Keys | Defaults when omitted |
|---|---|---|
| Identity, Dublin Core | `id`, `name`, `type`, `tags`, `description`, `credits`, `license` | `id` the directory name; `name` the id in title case; `type` `skill` in `skills/`, else the implied skill of the first interface file; `license` the repo's |
| Card face | `emoji`, `tier`, `rarity`, `tagline`, `t_shirt`, `tools {required, optional}`, `files` | `tier: 2`; `rarity: common`; `tagline` the first sentence of description; `files` the directory listing |
| Behavior | `advertisements` (map of [advertisement](../advertisement/)), `methods` (map of method, [OBJECT.yml](../object/OBJECT.yml)) | empty |
| Activation | `k_lines` | the id in UPPER-DASHES |
| State | `state` | empty |
| Copy-down | `interfaces` | the directory's interface files and the skill's prototype file, nothing copied |
| Relations | `inherits`, `inherited_by`, `related` (`{id, role, when, why}`), `see_also`, `lineage` | `see_also` is SKILL.md and README.md when present |
| Common jazz | `schema`, `examples`, `principles`, `anti_patterns` | `examples` the `examples/` directory |

`type:` is one id; other kinds go in `tags:`. `k_lines:` is a flat list of K-LINE words, run by
the same matcher as an advertisement's `trigger:` words. Situations that call for the card
are advertisement `score_if:` lines, not a separate `invoke_when:` list. `status:` and
`version:` are retired (git knows), and so are `card:` and `skill:` envelopes: cards are
flat.

Readers accept the older spellings listed as `aliases:` in the schema (`one_liner`,
`documentation`, `related_skills`, `activates`, `invoke_when`, `allowed_tools`, ...); writers
emit only the canonical key. Lint reports an alias as a finding.

### Copy-down from interfaces

Interface files stay canonical for instances: `skills/room/ROOM.yml` is what every room
inherits. The card copies down their most important slots and methods so the card level of
the pyramid represents them. A model reading the room card learns that every room answers
LOOK.

```yaml
interfaces:
  ROOM.yml:                        # path relative to the card
    role: prototype                # prototype: what every instance inherits; interface: one of this directory's
    slots: { exits: "map DIRECTION → path", lighting: "0 pitch black .. 10 full sun; default 6" }
    methods: [LOOK, ENTER, EXIT, CONTENTS, ADVERTISE]

methods:
  LOOK: { signature: "LOOK (AT [thing])", from: ROOM.yml }   # the copy, in the one methods map
```

Copied methods go into `methods:` with `from:`, so everything callable is in one map.
Which UPPERCASE files count as interfaces is decided per file; data files such as
`LAYOUTS.yml` belong in `files:`.

### Defaults keep cards short

Every key documents its default, and the default is the sensible case
([constitution §16](../../kernel/constitution-core.md#16-advertisements-push-into-the-auction-compile-graduate-universal)).
An omitted key means its default, so a card states only what is unusual about its object:
no `tier:` means standard, no `score_if:` means always, no `method:` on an advertisement
means the method of the same name, or "load this object and act". A value equal to its
default is removable.

### Projection

Orchestrators filter cards they can't read whole: the advertisements whose triggers match,
the methods a role may invoke, the cards a k-line activation or heat map has warmed. They
rely on these keys and nothing else:

`id`, `name`, `type`, `tags`, `tier`, `k_lines`, `advertisements[*].score`,
`advertisements[*].trigger`, `advertisements[*].score_if`, `methods[*].invoked_by`

That works only on standard shapes: maps keyed by name, numeric scores, lists where lists are
expected, one type id. A card with irregular shapes gets read whole or skipped.

### YAML Jazz rides on structure

Comments carry meaning, and object-specific keys (`types:`, `world_generation:`,
`self_correction:`) stay. Jazz goes on top of the standard keys and never stands in for one.
Where a jazz key means the same as a standard key, rename it to the standard one; a jazz key
that collides with an alias gets renamed too.

---

## Card Architecture

> **KEY INSIGHT: Cards are ACTIVATION TRIGGERS, not activation handlers.**

This is the most important concept in MOOLLM card design.

### The Fundamental Distinction

| | CARD.yml | SKILL.md |
|--|----------|----------|
| **Purpose** | Decide IF this skill applies | Explain HOW to execute |
| **Role** | Activation trigger | Activation handler |
| **Content** | Sniffable interface | Full documentation |
| **Size** | ~150-200 lines | As needed |
| **LLM reads** | First, to decide | Second, if activated |

The CARD asks: "Does this situation call for me?"
The SKILL.md answers: "Here's how to actually do it."

### Recommended Section Order

Order sections for optimal LLM scanning. Flat keys, no `card:` envelope; the full template is
[CARD.yml.tmpl](CARD.yml.tmpl).

```yaml
# 1. Identity and card face (who am I?)
id: my-skill
name: "My Skill"
type: skill
emoji: 🎯
tagline: "One-line pitch"
description: "Brief paragraph"

# 2. Files index (what else should LLM read?)
files:
  docs: [SKILL.md]
  examples: [examples/]

# 3. K-lines (what words and concepts wake this card?)
k_lines: [MY-SKILL, RELATED-CONCEPT]

# 4. ADVERTISEMENTS — PRIMARY! Put BEFORE methods!
advertisements:
  DO-THE-THING:
    score: 90
    score_if: "situation that calls for this skill"

# 5. Methods (signatures only, implementations in SKILL.md)
methods:
  DO-THING: { signature: "DO-THING [arg]" }

# 6. Copy-down from interface files, then state
interfaces:
  MY-SKILL.yml: { role: prototype, methods: [DO-THING] }
state:
  field1: 0

# 7. Relations: inherits, related, see_also, lineage
see_also:
  - SKILL.md: ["§ Detailed section"]
```

### Why Advertisements Before Methods?

Advertisements are the **PRIMARY activation signal**:

1. LLM scans top-down looking for "does this apply?"
2. Ads answer that question directly
3. Methods are secondary — only relevant AFTER activation
4. Front-loading ads speeds up skill selection

```yaml
# GOOD — Ads first
advertisements:
  PET-THE-CAT:
    score: 80
    score_if: "cat is present"
    
methods:
  PAT: { signature: "PAT [cat]" }

# BAD — Methods first (LLM has to read past them)
methods:
  PAT: { ... long list ... }
  SCRITCH: { ... }
  # ... many more ...
  
advertisements:  # Too late! LLM already moved on
```

### What Goes Where

#### In CARD.yml (sniffable interface)

```yaml
# YES — Include these
- Brief description + tagline
- Files index (for one-shot activation)
- K-lines (activation vectors)
- Advertisements (PRIMARY!)
- Method SIGNATURES (one-liners)
- The most important slots and methods of the interface files (copy-down)
- Brief state (field names and defaults)
- see_also pointers

# NO — Move these to SKILL.md
- Implementation details
- Detailed protocols with sequences
- Dispatch tables
- Dialogue examples
- Full state schemas with types
- Worked examples
```

#### In SKILL.md (full documentation)

```markdown
- ## 📑 Index (link to each section)
- Detailed method implementations
- Protocols with step sequences
- Dispatch tables (actor_verb_target)
- State schemas with types and defaults
- Integration points with other skills
- Mechanics explanations
```

#### In examples/ (worked examples)

```yaml
# Separate files with descriptive names
examples/
  ceremony-invocation.yml    # Good!
  buff-chain-trigger.yml     # Good!
  example1.yml               # Bad — not descriptive
```

### Method Placement Rules

| Situation | Place In | Example |
|-----------|----------|---------|
| Short signature | CARD methods | `PAT: { signature: "PAT [cat]" }` |
| Trivial inline | Advertisement | `method: "PAT [nearest-pet]"` |
| Detailed protocol | SKILL.md | Dispatch tables, sequences |
| Multiple variants | SKILL.md | Species-specific versions |
| Dispatch table | SKILL.md | `cat_sniffs_dog`, etc. |

#### Embed in CARD when:
- Method is SHORT (one-liner signature)
- Method is UNIQUE to this skill
- Just showing signature, not implementation

#### Embed in advertisement when:
- Method is TRIVIAL (buff, reply, simple prompt)
- Method is AD-SPECIFIC (only makes sense in this trigger)

#### Delegate to SKILL.md when:
- Method has DETAILED protocol (sequences, tables)
- Method is SHARED with other skills
- Method has multiple VARIANTS
- Method needs EXAMPLES to understand

### Target Card Size

```yaml
card_yml: ~150-200 lines
skill_md: As long as needed, but indexed
examples:  Separate files, descriptively named

smell: "If CARD > 300 lines, refactor"
```

---

## What's a Card?

Cards are **portable tokens** you can carry, give, play, and activate.

### The Card Intersection

CARD.yml sits at the intersection of *many* card traditions, each contributing essential meaning:

| Tradition | What It Contributes | In CARD.yml |
|-----------|---------------------|-------------|
| **PC Board Card** | Slot/interface — plugs into a system | Cards plug into rooms, skills, activations |
| **HyperCard** | Navigable unit of content | Each card is a stack, browsable, clickable |
| **Playing Cards** | Combinable, playable, deckable | Cards compose into decks, hands, plays |
| **Magic: The Gathering** | Abilities, costs, types, combos | Methods, state, synergies, triggered effects |
| **Pokémon** | Creatures with stats, evolution | Characters with sims_traits, mind_mirror, growth |
| **Fluxx** | Cards that change the rules | Meta-cards that modify the game itself |
| **Tarot** | Archetypal symbols, prompts | K-lines as archetypal activation |
| **Business Cards** | Contact, credentials, intro | Hero-Story cards introduce traditions |
| **Key Cards** | Access tokens | Room access, capability gates |
| **Hollerith Cards** | Data as physical artifact | YAML as punchable, portable data |

**The genius is the layering.** When you create a CARD.yml, you're creating:

- An **interface slot** (PC board) that plugs into the MOOLLM system
- A **navigable document** (HyperCard) that LLMs can browse and activate
- A **playable piece** (playing card) that can be dealt, held, played
- A **creature with abilities** (MTG/Pokémon) that has stats and moves
- A **rule modifier** (Fluxx) that can change the game
- An **archetypal pointer** (Tarot/K-line) that invokes patterns
- An **access token** (key card) that grants capabilities

All at once. Different contexts activate different metaphors.

### Card Examples by Tradition

| Type | Examples |
|------|----------|
| **Trading cards** | Hero-Story cards for real people's traditions |
| **Playing cards** | Actions, abilities, spells to play |
| **Magic: The Gathering** | Complex cards with costs, effects, combos |
| **Pokémon cards** | Characters with stats, moves, evolution |
| **Fluxx cards** | Rule-changing cards — play to modify the game itself |
| **Tarot cards** | Archetypal symbols, prompts for reflection |
| **Business cards** | Contact info, credentials, introductions |
| **Pleasure cards** | Memberships, VIP access, perks |
| **Key cards** | Access tokens for rooms and resources |
| **Receipts** | Proof of transaction, claim tickets |
| **Tickets** | Entry passes, reservations, permissions |
| **Coupons** | Redeemable capabilities, discounts |
| **Hollerith cards** | Punch cards — data as physical holes! |
| **QR codes** | Scannable data, links, actions |
| **Wallet cards** | Apple/Google Pay — phone as card carrier |

A card is anything you can **carry in your inventory** and **play when needed**.

---

## Sidecar CARD.yml Pattern

Any entity that lives in a directory can have a **sidecar `CARD.yml`** file that makes it card-playable:

```
pub/
├── ROOM.yml           # The room definition
├── CARD.yml           # Makes the pub a playable card!
└── ...

characters/don-hopkins/
├── CHARACTER.yml      # Character definition
├── CARD.yml           # Don's trading card representation
└── ...

objects/magic-lamp/
├── OBJECT.yml         # Lamp definition
├── CARD.yml           # Card for summoning/playing the lamp
└── ...
```

### Why Sidecars?

- **Separation of concerns** — Entity definition vs. card representation
- **Optional** — Not everything needs to be a card
- **Composable** — Same entity, multiple views
- **Portable** — Card data can reference the entity by path

### Sidecar Card Schema

```yaml
# pub/CARD.yml — makes the pub a playable card
type: room
tags: [location-card]

# Card-specific presentation (YAML Jazz)
name: "Gezelligheid Grotto"
art: "cozy-coffeeshop.png"
flavor: "Where good vibes flow like espresso"

interfaces:
  ROOM.yml: {}              # the room this card represents

# What playing this card does
advertisements:
  VISIT:
    description: "Teleport party to this location"
    effect: "Set party.location = pub/"

  SUMMON:
    description: "Bring the pub's vibe to current room"
    effect: "Apply pub buffs to current location"
```

### Character Cards

Characters automatically become tradeable/playable:

```yaml
# characters/don-hopkins/CARD.yml
type: character
tags: [hero-story]        # Real person tradition

# K-line activation
k_lines: [PIE-MENUS, CONSTRUCTIONIST-GAMES, MICROPOLIS]
tradition: "HyperCard, SimCity, OLPC, procedural rhetoric, Maxis"

interfaces:
  CHARACTER.yml: {}       # the character this card represents

# Playing the card
summon: |
  Activate Don's documented ideas:
  - Pie menu interaction patterns
  - Constructionist game design
  - Urban simulation philosophy
```

---

## The Big Idea

```mermaid
graph TD
    C[📇 Card Template] -->|clone + parameterize| I[🎴 Instance in Room]
    I -->|has| S[State: goals, vars, stack]
    I -->|lives in| R[🚪 Room]
    R -->|can hold| M[Multiple instances]
```

A **card** is a capability template — a tool, character, function, familiar, key, receipt.

A **card in play** is an instance with:
- Local variables
- Parameters
- Goal stack (what it's trying to do)
- Return value (when done)
- Room it lives in

You can have **multiple activations** of the same card, in the same or different rooms. They're independent task instances.

---

## Activation Records

> **Full specification:** [ACTIVATION.md](./ACTIVATION.md)

**Playing a card = creating an activation record** — an instantiated method with persistent state.

| Concept | Description |
|---------|-------------|
| **Multiple methods** | Cards have any number of methods (like Self objects) |
| **Implicit params** | LLM infers parameters from context (POSTEL) |
| **Pure state cards** | Cards can be just state, no methods |
| **Activation lifecycle** | pending → in_progress → completed |
| **Advertisements** | Activations expose buttons others can press |
| **Room participation** | Rooms can press buttons on cards in play |
| **Cross-card interaction** | Cards trigger each other's methods |

**The Sims meets Magic: The Gathering** — autonomous agents with triggered abilities.

---

## Fluxx Cards: Rules That Change Rules

> **Full specification:** [FLUXX.md](./FLUXX.md)

Inspired by [Fluxx](https://en.wikipedia.org/wiki/Fluxx), some cards **modify the game itself**.

| Feature | Description |
|---------|-------------|
| **Rule modification** | Cards can change room.rules on play |
| **Stacking** | Multiple Fluxx cards stack effects |
| **Meta-Fluxx** | Rules about rules (prevent further changes) |
| **Dispel** | Cards can advertise removal actions |

Fluxx cards make MOOLLM a **self-modifying game**.

---

## Data Flow Ensembles

> **Full specification:** [ENSEMBLES.md](./ENSEMBLES.md)

Cards can contain **coordinated ensembles** of generators, transformers, and consumers.

| Feature | Description |
|---------|-------------|
| **POSTEL binding** | Components self-wire by compatible inputs/outputs |
| **Factorio-style** | Queues with capacity, overflow, backpressure |
| **Natural language** | Describe wiring in plain English |
| **Orchestration** | Card tracks ensemble health and bottlenecks |

**Factorio meets Dataflow meets Natural Language** — pipelines assembled by intent.

---

## Cards Advertise

Just like [objects in rooms](../advertisement/), cards **advertise what they can do**:

```yaml
# Git Goblin card
advertisements:
  BISECT:
    description: "Binary search for bug introduction"
    score_if: "debugging AND has_git_repo"
    score: 90

  BLAME:
    description: "Find who changed this line"
    score_if: "examining_code"
    score: 70

  LOG:
    description: "Show commit history"   # score 50 is the default
```

**In inventory:** Advertisements visible but lower priority.

**Played in room:** Card's advertisements merge with room objects. Best action wins regardless of source.

**Multiple cards:** All advertisements compete. The right tool for the moment rises to top.

---

## Why K-Lines Are Safe

> [!IMPORTANT]
> **Cards for real people don't need proxy abstractions.**

A "Dave Ungar" card doesn't impersonate Dave Ungar. It **activates the tradition**:
- Self language, prototype-based inheritance
- "It's About Time" compilation philosophy
- Message-not-class thinking

This is like citing someone's work, not pretending to be them.

```yaml
name: "Dave Ungar"
type: person
# NOT impersonation — K-line activation

invokes:
  - "Self language"
  - "Prototype-based inheritance"
  - "ITS-ABOUT-TIME compilation"
  - "Message-passing purity"

wisdom: |
  "Programming should be about the experience
  of programming, not fighting the language."
```

When you "play" this card, you invoke the tradition — not simulate the person.

---

## Card Types

| Type | What It Is | Examples |
|------|------------|----------|
| `person` | Real human's wisdom | Dave Ungar, Seymour Papert |
| `character` | Fictional persona | The Gardener, The Archivist |
| `tool` | A capability | fs.read, search.vector |
| `function` | A procedure | summarize, repair |
| `familiar` | Helper spirit | Git Goblin 🧌, Index Owl 🦉 |
| `concept` | An idea | POSTEL, YAML-JAZZ |
| `place` | A location link | kernel/, skills/ |

---

## Card Anatomy

### Hero-Story (Real Person)

```yaml
name: "Dave Ungar"
type: person

# K-line activation — what tradition this invokes
invokes:
  - "Self language"
  - "Prototype-based inheritance"
  - "ITS-ABOUT-TIME compilation"
  - "Message-not-class thinking"

wisdom: |
  "Programming should be about the experience
  of programming, not fighting the language."

contributions:
  - "Self programming language"
  - "Morphic UI framework"
  - "Optimistic compilation"

stats:
  wisdom: 10
  influence: 9
  domain_expertise: ["languages", "VMs", "UI"]
```

### Familiar (Tool Spirit Animal)

```yaml
name: "Git Goblin"
type: familiar
emoji: "🧌"
enthralled_by: "Linus Torvalds" # My master (I mean main)!

abilities:
  - "Track changes"
  - "Commit with message"
  - "Navigate history"

parameters:
  repo_path: { type: string, required: true }

stats:
  power: 7
  reliability: 9
  learning_curve: 4

related:
  - { id: session-log, role: composes }
  - { id: plan-then-execute, role: composes }
```

---

## Putting Cards in Play

When you **activate** a card in a room:

```yaml
# Instance in room: .agent/rooms/debug-session/

activation:
  card: "Git Goblin"
  instance_id: "goblin-001"
  room: ".agent/rooms/debug-session/"
  
  # Instance-specific state
  parameters:
    repo_path: "/path/to/repo"
    
  state:
    current_branch: "main"
    uncommitted_changes: 3
    
  goals:
    - "Find when bug was introduced"
    - "Bisect to culprit commit"
    
  subgoals: []
  
  return_value: null  # Filled when done
```

---

## Multiple Instances

Same card, different activations:

```
.agent/rooms/
  debug-session/
    goblin-001.yml      # Git Goblin hunting a bug
    goblin-002.yml      # Git Goblin checking history
  feature-work/
    goblin-003.yml      # Git Goblin managing commits
```

Each instance has its own state, goals, and lifecycle.

---

## Contents

| File | Purpose |
|------|---------|
| [SKILL.md](./SKILL.md) | Full protocol documentation |
| [CARD.yml.tmpl](./CARD.yml.tmpl) | Template for new cards |
| [COLLECTION.yml.tmpl](./COLLECTION.yml.tmpl) | Template for card collections |

---

## Familiars (Special Cards)

Cards that embody tool capabilities as helpful spirits:

| Familiar | Emoji | Domain |
|----------|-------|--------|
| Git Goblin | 🧌 | Version control |
| Index Owl | 🦉 | Search and lookup |
| Memory Moth | 🦋 | Context management |
| Repair Imp | 🔧 | Self-healing |
| Session Scribe | 📜 | Logging |

See [P-HANDLE-K](../../PROTOCOLS.yml) — familiars are safe K-line wrappers.

---

## Actor Lineage

Cards-in-play ARE actors in the classic sense:

| Tradition | Contribution | In MOOLLM |
|-----------|--------------|-----------|
| **Hewitt (1973)** | Independent concurrent agents | Cards have independent state |
| **Simula (1967)** | Coroutines with state | Cards persist between messages |
| **Smalltalk (1972)** | Everything is message passing | Goals and returns are messages |
| **Self (1987)** | Prototypes, no classes | Cards are cloned, not instantiated |

> **Cards are prototypes. Activation clones them into actors.**

The microworld (filesystem) is the stage. Rooms are the scenes. Cards are the performers.

---

## The Intertwingularity

```mermaid
graph LR
    TC[🎴 card] -->|activates in| R[🚪 room]
    TC -->|can speak via| SC[💬 soul-chat]
    TC -->|logged by| SL[📜 session-log]
    TC -->|composes via| DOP[delegation-object-protocol]
    
    R -->|holds instances of| TC
    SC -->|voices for| TC
```

---

## Dovetails With

### Sister Skills
| Skill | Relationship |
|-------|--------------|
| [room/](../room/) | Cards **activate** in rooms. Rooms hold card instances. |
| [soul-chat/](../soul-chat/) | Cards can **speak** — hero-stories, familiars, all have voice |
| [adventure/](../adventure/) | Cards are your **companions** on quests |
| [play-learn-lift/](../play-learn-lift/) | Card creation follows PLL — play with ideas, learn patterns, lift into cards |

### Protocol Symbols
| Symbol | Meaning | Link |
|--------|---------|------|
| `TRADING-CARD` | Capabilities as cards | [PROTOCOLS.yml](../../PROTOCOLS.yml#TRADING-CARD) |
| `HERO-STORY` | Real person cards (safe) | [PROTOCOLS.yml](../../PROTOCOLS.yml#HERO-STORY) |
| `FAMILIAR` | Tool spirit animals | [PROTOCOLS.yml](../../PROTOCOLS.yml#FAMILIAR) |
| `P-HANDLE-K` | Why K-lines are safe | [PROTOCOLS.yml](../../PROTOCOLS.yml#P-HANDLE-K) |
| `ACTOR` | Cards-in-play are actors | [PROTOCOLS.yml](../../PROTOCOLS.yml#ACTOR) |
| `CARD-IN-PLAY` | Activated instance | [PROTOCOLS.yml](../../PROTOCOLS.yml#CARD-IN-PLAY) |
| `INVENTORY` | Things characters carry | [PROTOCOLS.yml](../../PROTOCOLS.yml#INVENTORY) |

### Meta
- [delegation-object-protocol.md](../delegation-object-protocol.md) — How cards inherit from prototypes
- [skill-instantiation-protocol.md](../skill-instantiation-protocol.md) — Card activation is skill instantiation

### Navigation
| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| ⬆️⬆️ Root | [Project Root](../../) |
| 🚪 Sister | [room/](../room/) |
| 💬 Sister | [soul-chat/](../soul-chat/) |
