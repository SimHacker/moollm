# EVAL Taxonomy: Entities, Autonomy, and Language

> *Everything pivots. Entities become personas. Personas become dialects. Dialects become Scats. Scats become entities.*

---

## Purpose

This document provides a **unified taxonomy** for:
- Entities (who/what acts)
- Autonomy (how much control)
- Language (how they express)
- Structure (how it's organized)

These are not separate systems. They **dovetail and interlock**.

---

## The Pivot Principle

Any element can be viewed through multiple lenses:

```
ENTITY ←→ PERSONA ←→ VOICE ←→ DIALECT ←→ SCAT
   ↑                                       ↓
   └─────────── feedback loop ─────────────┘
```

| View | Question |
|------|----------|
| **Entity** | Who is acting? |
| **Persona** | What role are they playing? |
| **Voice** | How do they sound? |
| **Dialect** | What patterns do they use? |
| **Scat** | What did they emit? |

**A Scat can instantiate an Entity. An Entity can emit a Scat. The cycle continues.**

---

## Part I: Entity Taxonomy

### Primary Entity Types

| Type | Definition | Example |
|------|------------|---------|
| **Player Character (PC)** | Human-controlled entity | Don at the pie table |
| **Non-Player Character (NPC)** | LLM-simulated entity with persistence | Marieke the budtender |
| **Bot** | Automated agent with defined behavior | Skeptic Worm |
| **Persona** | Role overlay on any entity | "Val" Dobias |
| **Environmental Force** | Non-agentive world dynamics | Weather, time, economy |
| **Faction** | Collective meta-entity | EvalNonymous, EvalState |
| **Abstract Entity** | Conceptual actor | "The Algorithm", "The Market" |

### Entity Hierarchy

```
                    ┌─────────────┐
                    │   ENTITY    │
                    └──────┬──────┘
           ┌───────────────┼─────────────────┐
           ▼               ▼                 ▼
      ┌──────────┐    ┌───────────┐    ┌───────────┐
      │ AGENTIVE │    │ COLLECTIVE│    │ AMBIENT   │
      └─────┬────┘    └─────┬─────┘    └─────┬─────┘
            │               │                │
     ┌──────┴──────┐        │         ┌──────┴──────┐
     ▼             ▼        ▼         ▼             ▼
 ┌──────┐     ┌──────┐  ┌───────┐  ┌──────┐    ┌──────┐
 │  PC  │     │  NPC │  │Faction│  │Force │    │ Mood │
 └──────┘     └──────┘  └───────┘  └──────┘    └──────┘
                 │
          ┌──────┴──────┐
          ▼             ▼
       ┌──────┐     ┌───────┐
       │ Bot  │     │Persona│
       └──────┘     └───────┘
```

---

## Part II: Autonomy Spectrum

### The Autonomy Ladder

| Level | Name | Control | Example |
|-------|------|---------|---------|
| **0** | **Inert** | No action | A rock, a door |
| **1** | **Reactive** | Responds to triggers | Tripwire, sensor |
| **2** | **Scripted** | Follows fixed patterns | Patrol guard, timed event |
| **3** | **Responsive** | Adapts to input | Chatbot, FAQ system |
| **4** | **Autonomous** | Makes decisions within constraints | NPC with needs/traits |
| **5** | **Deliberative** | Plans and reasons | Worm with strategy |
| **6** | **Self-Modifying** | Changes own behavior | Evolving faction |
| **7** | **Incarnate** | Full agency protocol | Palm the monkey |

### Autonomy by Entity Type

| Entity Type | Typical Level | Can Reach |
|-------------|---------------|-----------|
| Environmental Force | 2-3 | 4 |
| Bot | 3-5 | 6 |
| NPC | 4-5 | 6 |
| Persona | 4-6 | 7 |
| PC | 7 | 7 |
| Faction | 5-6 | 6 |

### Autonomy Transitions

Entities can **level up or down**:

| Transition | Trigger | Example |
|------------|---------|---------|
| Inert → Reactive | Player interaction | "You pick up the lamp" |
| Scripted → Responsive | Player attention | NPC notices player |
| Responsive → Autonomous | Incarnation protocol | Palm's wish |
| Autonomous → Deliberative | Player grant | "Take over while I'm gone" |
| Any → Inert | Player command | "Freeze" |

---

## Part III: Persona and Code-Switching

### What Is a Persona?

A **Persona** is a role overlay that can attach to any entity:

| Base Entity | + Persona | = Result |
|-------------|-----------|----------|
| NPC Marieke | + Referee | Marieke officiating a dispute |
| Bot Worm | + Skeptic | Skeptic Worm |
| Player Don | + "Val" | Don channeling "Val" |
| Force Weather | + Angry God | Vengeful storm |

### Persona Attributes

```yaml
persona:
  name: "The Skeptic"
  emoji: 🧊🤔❓
  voice:
    tone: questioning
    hedging: high
    certainty: low
  triggers:
    - claims without evidence
    - unanimous agreement
  dialect: skeptic-speak
```

### Code-Switching

**Code-switching** is when an entity changes persona mid-interaction:

| Type | Description | Example |
|------|-------------|---------|
| **Contextual** | Environment triggers switch | Formal in court, casual in pub |
| **Audience** | Interlocutor triggers switch | Technical with devs, simple with users |
| **Tactical** | Strategic switch | Friendly, then intimidating |
| **Involuntary** | Stress/emotion triggers switch | Breaking character under pressure |
| **Ritual** | Protocol triggers switch | "Speaking as Referee, Auctioneer, etc..." |

### Code-Switch Markers

In Scats, mark switches explicitly:

```yaml
💬:
  speaker: marieke
  persona: budtender
  says: "What can I get you?"
  
💬:
  speaker: marieke
  persona: referee  # CODE SWITCH
  _comment: "Switching to official role"
  says: "Order in the pub. The gong has sounded."
```

---

## Part IV: Language Taxonomy

### The Language Stack

```
┌─────────────────────────────────────┐
│           NATURAL LANGUAGE          │  ← Human prose
├─────────────────────────────────────┤
│              DIALECT                │  ← Regional/group variation
├─────────────────────────────────────┤
│               SLANG                 │  ← In-group markers
├─────────────────────────────────────┤
│                DSL                  │  ← Domain-specific patterns
├─────────────────────────────────────┤
│            YAML JAZZ                │  ← Semantic structure + comments
├─────────────────────────────────────┤
│              SCATS                  │  ← Emoji-rich expressions
├─────────────────────────────────────┤
│         EMOJI GRAMMAR               │  ← Pure symbolic
└─────────────────────────────────────┘
```

### Dialect Types

| Dialect | Speaker | Characteristics |
|---------|---------|-----------------|
| **Faction Dialect** | EvalNonymous, Church | Vocabulary, emoji sets, frames |
| **Professional Dialect** | Referee, Auditor | Formal patterns, hedging |
| **Regional Dialect** | Room-specific | Local slang, references |
| **Temporal Dialect** | Era-specific | Archaic, futuristic |
| **Species Dialect** | Cats, worms | Non-human patterns, Meowjies |

### Slang Evolution

Slang emerges through use:

```
1. NEOLOGISM    → Someone coins a term
2. ADOPTION     → Others use it
3. DRIFT        → Meaning shifts
4. IRONY        → Used sarcastically
5. RECLAMATION  → Original meaning restored (or not)
6. FOSSILIZATION → Becomes standard
```

### Domain-Specific Languages (DSLs)

| DSL | Domain | Form |
|-----|--------|------|
| **Eval-speak** | Judgment | Metrics, rubrics, scores |
| **Worm-speak** | Interpretation | Diet, stance, casting |
| **Church-speak** | Religion | Theology, ritual, blessing |
| **Faction-speak** | Politics | Ideology, tactics, signals |
| **Room-speak** | Navigation | Exits, objects, atmosphere |

---

## Part V: YAML Jazz Deep Taxonomy

### YAML Jazz Registers

| Register | Formality | Use |
|----------|-----------|-----|
| **Formal Jazz** | High | Schemas, protocols, specs |
| **Working Jazz** | Medium | State files, configs |
| **Conversational Jazz** | Low | Quick notes, drafts |
| **Scat Jazz** | Variable | Social expressions |
| **Stream Jazz** | Minimal | Logs, events |

### Comment Semantics

Comments carry meaning at different levels:

| Level | Marker | Purpose |
|-------|--------|---------|
| **Meta** | `# TEMPLATE:` | Instructions for generation |
| **Intent** | `# Why:` | Explains purpose |
| **History** | `# Was:` | Documents changes |
| **Warning** | `# CAUTION:` | Flags risks |
| **Todo** | `# TODO:` | Marks incomplete |
| **Voice** | `# [persona]:` | In-character comment |

### Structure as Meaning

| Structure | Meaning |
|-----------|---------|
| Sibling order | Priority |
| Nesting depth | Scope/detail |
| Key naming | Semantic category |
| Anchor choice | Stance/mode |
| Comment density | Uncertainty/complexity |

---

## Part VI: Scat Taxonomy

### Scat Types by Function

| Type | Function | Example |
|------|----------|---------|
| **Declaration** | State a position | "I believe X" |
| **Observation** | Report perception | "I saw X" |
| **Interpretation** | Offer meaning | "X means Y" |
| **Question** | Seek information | "What is X?" |
| **Command** | Request action | "Do X" |
| **Blessing** | Grant positive | "+1 confidence" |
| **Curse** | Grant negative | "−1 reputation" |
| **Ritual** | Perform ceremony | "In 'Val's' name..." |
| **Meta** | Comment on scats | "That scat was 🔥" |

### Scat Types by Origin

| Origin | Characteristics |
|--------|-----------------|
| **Player Scat** | Human-authored, authentic |
| **NPC Scat** | LLM-generated, in-character |
| **Bot Scat** | Automated, patterned |
| **Worm Scat** | Digested, interpreted |
| **Faction Scat** | Collective, coordinated |
| **System Scat** | Environmental, neutral |

### Scat Complexity

| Level | Elements | Example |
|-------|----------|---------|
| **Atomic** | 1-3 emoji | 👁🔥 |
| **Simple** | Emoji + value | `stance: 🔥` |
| **Compound** | Multiple fields | Diet + stance + take |
| **Nested** | Hierarchical | Full worm casting |
| **Threaded** | References others | Reply chain, discussion tree |
| **Canonical** | Authoritative version | Official doctrine |

---

## Part VII: Semantic Interlocks

### How Entities and Languages Connect

```
ENTITY ──produces──→ SCAT
   │                   │
   │ uses              │ in
   ▼                   ▼
DIALECT ←──shapes──── CONTEXT
   │                   │
   │ evolves into      │ triggers
   ▼                   ▼
 SLANG ←──marks────── FACTION
   │                   │
   │ formalizes into   │ adopts
   ▼                   ▼
  DSL ←───defines──── PROTOCOL
```

### Pivot Points

Transformations between taxonomy layers:

| Source | Target | Process | What Happens |
|--------|--------|---------|--------------|
| Entity | Scat | **Emission** | Entity speaks, acts, produces expression |
| Scat | Entity | **Incarnation** | Expression instantiates character |
| Persona | Dialect | **Voice** | Persona manifests through speech patterns |
| Dialect | Slang | **Drift** | Patterns compress into identity markers |
| Slang | DSL | **Formalization** | Slang gets documented, rules emerge |
| DSL | Protocol | **Standardization** | DSL becomes required, shared |
| Faction | Dialect | **Identity** | Group develops distinctive vocabulary |
| Worm | Scat | **Casting** | Worm digests input, emits interpretation |
| Scat | Worm | **Ingestion** | Worm consumes expression as input |
| Context | Dialect | **Activation** | Situation triggers appropriate register |
| Faction | Slang | **Coinage** | Group invents new terms, grammars, and meme templates |
| Protocol | Entity | **Binding** | Rules constrain entity behavior |

### The Full Cycle

1. **Entity** (Palm) adopts **Persona** (writer)
2. **Persona** speaks in **Dialect** (philosophical)
3. **Dialect** includes **Slang** (monkey idioms)
4. **Slang** follows **DSL** (YAML Jazz conventions)
5. **DSL** produces **Scat** (a published reflection)
6. **Scat** is consumed by **Worm** (theory worm)
7. **Worm** emits new **Scat** (interpretation)
8. **Scat** influences **Faction** (Church of Eval Genius)
9. **Faction** develops new **Dialect** (Val-speak)
10. **Dialect** is adopted by new **Entity**...

---

## Part VIII: Environmental Forces

### Force Types

| Force | Behavior | Autonomy |
|-------|----------|----------|
| **Weather** | Cyclical + random | 2-3 |
| **Time** | Linear, inexorable | 1 |
| **Economy** | Emergent from transactions | 4 |
| **Reputation** | Emergent from evaluations | 4 |
| **Mood** | Ambient emotional state | 3 |
| **Attention** | Collective gaze | 4 |
| **Entropy** | Decay, disorder | 2 |

### Forces as Actors

Forces can be personified:

| Force | As Entity | Voice |
|-------|-----------|-------|
| Weather | Storm God | Angry, capricious |
| Time | The Clock | Patient, inevitable |
| Economy | The Market | Impersonal, efficient |
| Reputation | The Crowd | Fickle, loud |
| Attention | EvalEye | Watchful, judging |

### Force Interactions

| Force A | + Force B | = Emergent |
|---------|-----------|------------|
| Time + Reputation | Fading memory | Old scandals forgotten |
| Economy + Attention | Engagement markets | Attention as currency |
| Weather + Mood | Pathetic fallacy | Rain makes sad |
| Entropy + Reputation | Scandal decay | Controversy fades |

---

## Part IX: Dovetail Patterns

### Pattern: Entity-Dialect Binding

An entity's dialect reveals their identity:

```yaml
marieke:
  dialects:
    default: dutch-english-hybrid
    professional: budtender-speak
    official: referee-formal
  code_switch_triggers:
    - gong: referee-formal
    - customer: budtender-speak
    - cats: cat-adjacent
```

### Pattern: Faction-Slang Emergence

Factions develop slang organically:

```yaml
evalnonymous:
  slang:
    "drop a scat": leak information
    "go gray": pretend neutrality
    "val'd": publicly evaluated
    "eyeballed": under surveillance
  emoji_dialect:
    attack: 🕳️🔥
    retreat: 👁️💨
    victory: ⚖️✨
```

### Pattern: Worm-DSL Specialization

Each worm type has a DSL:

```yaml
skeptic_worm:
  dsl:
    keywords: [doubt, question, hedge, caveat]
    operators: [but, however, unless, except]
    emoji_grammar:
      - 🤔 = uncertainty
      - ❓ = question
      - 🧊 = cooling claim
    output_pattern: "claim → doubt → alternative"
```

### Pattern: Scat-Entity Instantiation

A Scat can create an entity:

```yaml
# This Scat...
🙏📜:
  wish: "I want the rest of the monkey"
  protocol: incarnation
  
# ...instantiates this entity
palm:
  type: npc
  autonomy: 7
  origin: scat-instantiation
  parent_scat: "monkey-paw-wish-001"
```

---

## Part X: Autonomy Protocols

### Granting Autonomy

| Protocol | Grants | Requires |
|----------|--------|----------|
| **OBSERVE** | Perception | Attention |
| **REACT** | Response | Trigger |
| **DECIDE** | Choice | Options |
| **PLAN** | Strategy | Goals |
| **INCARNATE** | Full agency | Consent ritual |
| **DELEGATE** | Transfer control | Trust |

### Autonomy Constraints

| Constraint | Limits |
|------------|--------|
| **Scope** | What domains can act in |
| **Duration** | How long autonomy lasts |
| **Reversibility** | Can actions be undone |
| **Visibility** | Who sees actions |
| **Accountability** | Who is responsible |

### Autonomy Revocation

| Trigger | Effect |
|---------|--------|
| Player command | Immediate freeze |
| Constraint violation | Rollback + warning |
| Session end | Suspend (preserve state) |
| Explicit revocation | Return to lower level |
| Entity request | Self-demotion |

---

## Part XI: The Master Grid

### Entity × Autonomy × Language

| Entity | Autonomy | Primary Language | Secondary |
|--------|----------|------------------|-----------|
| PC | 7 | Natural + YAML Jazz | Any |
| NPC | 4-6 | Dialect + Scats | DSL |
| Bot | 3-5 | DSL + Scats | Dialect |
| Worm | 5 | DSL + Castings | Emoji |
| Persona | 4-7 | Voice + Dialect | Slang |
| Faction | 5-6 | Ideology + Slang | DSL |
| Force | 2-4 | System + Ambient | Mood |

### Language × Formality × Entity

| Language | Formal | Casual | Entities |
|----------|--------|--------|----------|
| Natural | Documents | Chat | PC, NPC |
| Dialect | Ceremony | Banter | NPC, Faction |
| Slang | Rare | Common | Faction, NPC |
| DSL | Protocols | Quick refs | Bot, Worm |
| YAML Jazz | Schemas | Notes | All |
| Scats | Canonical | Drafts | All |
| Emoji | Rituals | Reactions | All |

---

## Summary: The Interlock Principle

**Everything connects:**

- Entities produce Scats in Dialects
- Dialects emerge from Factions with Slang
- Slang formalizes into DSLs
- DSLs structure YAML Jazz
- YAML Jazz carries Scats
- Scats instantiate Entities
- Entities join Factions
- Factions develop Dialects...

**The taxonomy is not a hierarchy. It is a web of pivots.**

---

## Related Documents

- [SCATS-DESIGN.md](./SCATS-DESIGN.md) — Scat structure
- [EVAL-WORMS.md](./EVAL-WORMS.md) — Worm entities
- [EVAL-FACTIONS.md](./EVAL-FACTIONS.md) — Faction entities
- [EMOJI-ANCHORS.md](./EMOJI-ANCHORS.md) — Emoji grammar
- [EVAL-DOM-SPEC.md](./EVAL-DOM-SPEC.md) — YAML Jazz structure
- [../../skills/yaml-jazz/](../../skills/yaml-jazz/) — Language skill
- [../../skills/incarnation/](../../skills/incarnation/) — Autonomy protocol
- [../../skills/character/](../../skills/character/) — Entity definition

---

*"The taxonomy is not a cage. It is a map of freedom."*
