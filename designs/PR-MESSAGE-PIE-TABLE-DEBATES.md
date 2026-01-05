# 🥧 Pie Menus, Gong Shows, and Factorio Debates

> *"All voices equal. All directions valid. Ring to speak. Pass to yield."*
> — The plaque on the Pie Menu Round Table

## The Numbers

```
40 commits (this session)
294 files changed
+34,222 lines / -17,691 lines
1 new skill (debate)
2 new pub objects (pie-table, gong)
∞ musical chairs games possible
```

⚠️ **DO NOT SQUASH** — the commit history tells a story of iterative design.

---

## 🎯 The Big Ideas

### 1. Cards as Activation Records

**Playing a card = creating a stack frame.**

Cards aren't just tokens — they're methods with persistent state:

```yaml
# design-room/architect-task-001.activation
card: architect.card
method: generate_proposal
state:
  iteration: 3
  current_draft: proposal-v3.yml
  feedback_received: [critic-001, economist-001]
  status: awaiting_vote
```

Like Self, cards have **multiple methods**. The LLM supplies implicit parameters from context (POSTEL).

**Activation advertisements:** Buttons that others can press:

```yaml
advertisements:
  APPROVE:   # Committee members can vote
  CRITIQUE:  # Experts provide feedback
  REVISE:    # Request iteration
  FINALIZE:  # Lock when quorum reached
```

**Rooms press buttons too.** The room isn't passive — it's a participant:

```yaml
on_tick:
  - scan: activations
    condition: "status == 'stalled'"
    action: "NUDGE activation"  # Room prods for attention
```

### 2. Data Flow Ensembles (Factorio for LLMs)

Cards can contain **coordinated pipelines** of generators, transformers, and consumers:

```
┌─────────────────────────────────────────────────────┐
│ debate.card                                         │
│                                                     │
│  GENERATORS        TRANSFORMERS      CONSUMERS      │
│  ┌─────────┐       ┌───────────┐    ┌──────────┐   │
│  │CREATE   │──────▶│CREATE     │───▶│CREATE    │   │
│  │SIDE     │       │MODERATOR  │    │AUDIENCE  │   │
│  └─────────┘       └───────────┘    └──────────┘   │
│  ┌─────────┐            │           ┌──────────┐   │
│  │CREATE   │            │           │CREATE    │   │
│  │TOPIC    │────────────┘           │TRANSCRIPT│   │
│  └─────────┘                        └──────────┘   │
│                                                     │
│  QUEUES: buffering, backpressure, overflow         │
└─────────────────────────────────────────────────────┘
```

**Natural language assembly:**

```
> "Set up a debate about AI safety with three sides:
>  optimists, pessimists, and pragmatists.
>  Add a moderator who enforces Robert's Rules.
>  Audience of 7 with different expertise levels."

# LLM interprets, creates components, wires data flow
# POSTEL handles the ambiguity gracefully
```

### 3. Flux Cards: Rules That Change Rules

Inspired by [Fluxx](https://en.wikipedia.org/wiki/Fluxx) — some cards modify the game itself:

```yaml
# flux/chaos-mode.card
on_play:
  modify: room.rules
  changes:
    action_order: random
    advertisement_scoring: inverted  # Worst wins!

# flux/immutable.card (meta-flux)
on_play:
  modify: room.meta_rules
  changes:
    flux_cards_allowed: false  # Lock down further changes!
```

**MOOLLM becomes a self-modifying game** — rules are game state.

### 4. The Debate Skill

A full skill for structured multi-perspective deliberation:

```
skills/debate/
├── README.md          # Overview
├── SKILL.md           # Full spec + debate.card
├── DEBATE.yml.tmpl    # Session state
├── SIDE.yml.tmpl      # Position/advocates
└── TRANSCRIPT.md.tmpl # Structured record
```

**Commands include Robert's Rules:**

| Command | Effect |
|---------|--------|
| `MOTION [text]` | Propose for vote |
| `SECOND` | Support a motion |
| `ARGUMENT` | Make your case |
| `REBUTTAL` | Counter an argument |
| `GONG` | Mercy ending (see below) |

### 5. The Pie Menu Round Table

Don Hopkins' pie menu insight applied to furniture:

```
       [N]
    NW     NE
  [W]  🔔  [E]
    SW     SE
       [S]

All seats equidistant from center.
Selection is spatial, not linear.
No head of table. Arthurian equality.
```

**Features:**

- **8 compass-stable slices** (configurable 3-12)
- **Each slice has contents**: chair, serving tray, drink holder
- **Addressable seats**: `pub/pie-table.yml#SW`
- **Bidirectional occupancy**: table knows who's sitting, character knows where
- **SUMMON_PANEL**: Instant diverse voices for any topic
- **MUSICAL_CHAIRS**: Chairs disappear, compass stays stable

**Built-in panels:**

```yaml
technology_ethics:
  - optimist, pessimist, pragmatist, historian
  - futurist, ethicist, skeptic, visionary

political_spectrum:
  - progressive, conservative, libertarian
  - communitarian, technocrat, populist

creative_process:
  - dreamer, critic, builder, editor
  - researcher, storyteller, contrarian, synthesizer
```

### 6. The Gong of Gezelligheid

A magnificent bronze gong for attention and mercy:

| Strike | Effect |
|--------|--------|
| `RING` (once) | All conversation pauses |
| `RING_TWICE` | Emergency interrupt |
| `RING_THRICE` | **The Gong Show termination** |
| `CELEBRATION_RING` | Victory fanfare |

**Chuck Barris understood:** The gong isn't cruel — it's merciful. It makes failure acceptable.

**AUTOGONG:** During musical chairs, the gong rings automatically:
- *GONG* once for each eliminated player
- *GONG* *GONG* *GONG* for the winner

### 7. Addressable Locations with Fragments

Characters can parent to specific positions:

```yaml
# In maya.yml
location: pub/pie-table.yml#SW

# Bidirectional:
# pie-table.yml#SW.occupant.id = "maya"
# maya.yml.location = "pub/pie-table.yml#SW"
```

**Stable geography:** Removing a chair empties the slice, doesn't change compass directions. `#NE` always means northeast.

---

## 📊 Stats

| Metric | This Session |
|--------|--------------|
| Commits | 40 |
| Files changed | 294 |
| Lines added | +34,222 |
| Lines removed | -17,691 |
| New skills | 1 (debate) |
| New pub objects | 2 (pie-table, gong) |

---

## 📁 Key New Files

### New Skill

```
skills/debate/
├── SKILL.md           # 511 lines
├── DEBATE.yml.tmpl
├── SIDE.yml.tmpl
├── TRANSCRIPT.md.tmpl
└── README.md
```

### New Pub Objects

```
examples/adventure-4/pub/
├── pie-table.yml      # 388 lines — the round table
└── gong.yml           # 231 lines — attention and mercy
```

### Enhanced Skills

```
skills/card/SKILL.md   # +500 lines
├── Activation Records
├── Multiple Methods
├── Activation Advertisements
├── Room-Driven Activation
├── Flux Cards
└── Data Flow Ensembles
```

---

## 🔗 Commit Highlights

```
1092458 AUTOGONG: Gong rings automatically during musical chairs
b4ab303 Rich table_layout with customizable slices, contents, and occupants
2fe7f01 Stable compass directions — remove chairs, not slices
f182922 Add addressable seats — characters parent to chairs via location
880b64d Add MUSICAL_CHAIRS to the round table
8200bc4 Add The Gong of Gezelligheid to the pub
173e671 Add Pie Menu Round Table to the pub
3bff191 Add debate skill with card, templates, and data flow ensemble
b904de4 Add Data Flow Ensembles: Factorio meets Natural Language
8f6a705 Add Flux cards: rules that change rules
571c2b0 Activation records advertise buttons that others can press
98caecc Document card activation records and methods
```

---

## 🎮 Try It

```yaml
# Enter the pub
> GO pub

# Examine the new furniture
> EXAMINE pie-table
> EXAMINE gong

# Sit at the table
> SIT position=N

# Summon a panel for instant debate
> SUMMON_PANEL topic="tabs vs spaces" style=adversarial

# Start the debate
> START_DISCUSSION format=roundtable

# Or just play musical chairs
> MUSICAL_CHAIRS elimination_style=gong_show

# *GONG* *GONG* *GONG* — WINNER!
```

---

## 🧠 Design Principles Demonstrated

1. **Cards as Objects** — Not just tokens, but rich entities with methods and state
2. **Spatial Metaphors** — Pie menus, compass directions, rooms as activation contexts
3. **Bidirectional References** — Table knows who's sitting, character knows where
4. **Self-Modifying Systems** — Flux cards change the rules of the game
5. **Mercy Endings** — The gong as compassionate termination
6. **Natural Language Wiring** — POSTEL for data flow assembly

---

*"Ring for attention. Ring twice for emergency. Ring thrice to end what should not continue. Ring with kindness. The sound carries far."*

*"All choices equidistant from center. All voices equal. All directions valid."*
