# Scats: Design Document

> *Scats are to social meaning what jazz riffs are to music — structured improvisations that carry intent, emotion, and interpretation across cultures.*

---

## What Is a Scat?

A **Scat** is:
- An improvised, remixable, commentable **YAML Jazz expression**
- Emoji-rich
- Structured
- Commented
- Interpretable by humans and machines

**The name comes from jazz scat singing** — improvised vocal expression using non-lexical syllables. Rhythm, intent, emotion — structure without literal words.

---

## Why "Scats"?

### Alternatives Considered

| Candidate | Issue |
|-----------|-------|
| Tweets | Trademarked, platform-specific |
| Truths | Trademarked, politically loaded |
| Posts | Generic, flat |
| Yams / Yamls | Cute internally, weird externally |
| Jazzes | Vague, awkward grammar |

### Why Scats Works

| Quality | Description |
|---------|-------------|
| Verbable | "I scatted that" |
| Pluralizable | "scats" |
| Playful | Not corporate |
| Historical | Jazz lineage |
| Not trademarked | Free to use |
| Culturally resonant | Improvisation, expression |
| Maps perfectly | Structure without literal words |

---

## Scat Uses

Scats can represent:

| Type | Examples |
|------|----------|
| Reaction | Emoji-only punchlines |
| Jokes | Joke setup and punchline structures |
| Lyrics | Song snippets, mishear lyrics |
| Interpretations | Commentary on events |
| Blessings | Positive attachments |
| Curses | Negative attachments |
| Buffs | Temporary modifiers (high fives, "you go girl!", encouragements) |
| Questions | Inquiry structures |
| Conversations | Ongoing threads |
| Polls | Voting structures |
| Endorsements | Support signals |
| Plans | Evolving intentions and goals |
| Rituals | Ceremonial expressions |

**Short colorful scats taste best.**

---

## Scat Lifecycle

```
✍️ Draft → 🎵 Jam → 📜 Canonical → 🌊 Drift
```

| Stage | Description |
|-------|-------------|
| **Draft** | Initial expression, private or semi-public |
| **Generation** | Ask LLM to generate, edit, interpret, translate, give feedback and suggestions |
| **Jam** | Others remix, annotate, embellish |
| **Canonical** | Crystallized version gains authority as successful fruitful meme |
| **Drift** | Meaning mutates over time and context |

**Scats are not finished products. They are invites.**

---

## Scat Structure

### Basic Scat

```yaml
🙏📜:
  context: public
  mood: 😔🧎
  intent:
    - ⚖️ appeal
    - 🕯️ repentance
  risks:
    - 👀 scrutiny
    - 🔥 backlash
```

### Scat with Attachments

```yaml
🎁:
  from: @maya
  to: @alex
  mood: 🎉
  _attachments:
    - blessing: 🌟
    - buff: confidence +2
  _comments: "Birthday encouragement"
```

### Expressive Buffs

Quick social signals that carry temporary positive effects:

```yaml
🙌:
  type: high-five
  from: @don
  to: @maya
  energy: +1
  duration: ephemeral
  
💪:
  type: you-got-this
  from: @maya  
  to: @alex
  confidence: +2
  _comments: "Before the big presentation"

👏👏👏👏:
  type: applause
  from: @crowd
  to: @performer
  validation: +4
  visibility: public
  _comment: "would give you more claps than four at once, but I'm only an octopus"
```

### Buff Vocabulary

| Buff | Emoji | Effect | Duration |
|------|-------|--------|----------|
| **High Five** | 🙌 ✋ 🖐️ | energy +1 | ephemeral |
| **You Go Girl** | 💅 👑 ✨ | confidence +2 | scene |
| **Applause** | 👏 🎉 🙏 | validation +1-3 | moment |
| **Hug** | 🤗 💕 🫂 | comfort +2 | lingers |
| **Fist Bump** | 🤜🤛 👊 | solidarity +1 | ephemeral |
| **Standing O** | 🧍👏🧍👏 | validation +5 | memorable |
| **Chef's Kiss** | 🤌 💋 ✨ | taste +3 | sticky |
| **Mind Blown** | 🤯 💥 🧠 | impact +4 | resonant |
| **Slow Clap** | 👏...👏...👏 | ironic validation ±2 | ambiguous |
| **Eye Roll** | 🙄 | skepticism −1 | dismissive |

### Buff Stacking

Buffs can stack and combine:

```yaml
combo:
  - 🙌 high-five
  - 💪 you-got-this  
  - 👑 slay
  _comments: "Triple encouragement before the interview"
  net_effect:
    confidence: +5
    energy: +2
```

### Buff Decay

Most buffs are **ephemeral** — they feel good, then fade.

| Duration | Lifespan | Example |
|----------|----------|---------|
| **Ephemeral** | Seconds to minutes | High five |
| **Moment** | The current scene | Applause |
| **Scene** | Current social context | "You go girl" |
| **Lingers** | Hours | Hug, deep encouragement |
| **Memorable** | Days to permanent | Standing ovation |
| **Sticky** | Hard to shake | Chef's kiss on good work |

**Buffs are not permanent. That's the point. They're gifts of attention.**

---

## Emoji as Primary Language

### Why Emoji-First?

| Reason | Description |
|--------|-------------|
| Cross-lingual | Works across languages |
| Affect-first | Emotion before proposition |
| Culturally adaptable | Meaning negotiated in use |
| Combinatorial | Compounds create new meanings |
| Performative | Acts, not describes |
| Algorithm-friendly | Structure machines can read |
| Already political | People already fight over 🔫 |

**You're formalizing what people already do.**

### Emoji Grammar

Emojis aren't just reactions. They are **symbols**.

| Emoji | Meaning |
|-------|---------|
| 🙏 | Appeal, request |
| 🔥 | Escalation, heat |
| 🧊 | Cooling, de-escalation |
| 👀 | Scrutiny, watching |
| 🧠 | Theory, analysis |
| 🐍 | Betrayal, danger |
| 📜 | Doctrine, rules |
| 🗳️ | Collective judgment, vote |

Combined:
```
🙏📜⚖️👀🔥
```
...means something very specific in context.

### Emergent DSLs

Over time:
- Communities develop slang
- Emojis shift meaning
- Irony layers form
- Dogwhistles emerge
- Ritual phrases crystallize

**This is language evolution as gameplay.**

---

## Emoji Identity Declaration

### Declaring Your Emoji (Like Pronouns)

Just as you declare your pronouns, you declare your **emoji identity**:

```yaml
character:
  name: "Palm"
  pronouns: "they/them"
  emoji:
    type: 🐒           # Species/category default
    personal: 🌴       # Single-emoji personal name
    iconic: 🐒🌴✨     # Multi-emoji signature
    mood_default: 🤔   # Resting expression
```

### Emoji Identity Layers

| Layer | Description | Example |
|-------|-------------|---------|
| **Type** | Species/category default | 🐕 dog, 🐈 cat, 👤 human, 🐢 turtle, 🐒 monkey |
| **Personal** | Single-emoji name/handle | 🌴 (Palm), 🧇 (Stroopwafel), 🍪 (Biscuit) |
| **Iconic** | Multi-emoji signature | 🐒🌴✨ (Palm's full signature) |
| **Mood** | Current emotional state | 😊 happy, 🤔 thinking, 😤 frustrated |
| **Status** | Current activity/state | 💤 sleeping, 🍽️ eating, 💬 talking |

### Character Examples

```yaml
stroopwafel:
  name: "Stroopwafel"
  pronouns: he/him
  emoji:
    type: 🐈
    personal: 🧇
    iconic: 🐈🧇😾
    mood_default: 😾  # Grumpy is baseline
    
biscuit:
  name: "Biscuit"
  pronouns: he/him
  emoji:
    type: 🐕
    personal: 🍪
    iconic: 🐕🍪💕
    mood_default: 🥰
    
marieke:
  name: "Marieke"
  pronouns: she/her
  emoji:
    type: 👩
    personal: 🌷      # Dutch tulip
    iconic: 👩🌷🍺
    mood_default: 😊
    role: 🍺          # Budtender role emoji
    
don:
  name: "Don"
  pronouns: he/him
  emoji:
    type: 👨
    personal: 🥧      # Pie table regular
    iconic: 👨🥧🎮
    mood_default: 🤓
```

### Object Emoji Declaration

Objects also declare their emoji:

```yaml
pie_table:
  name: "The Pie Table"
  emoji:
    type: 🪑          # Furniture category
    personal: 🥧      # This specific table
    iconic: 🥧🪑✨
    
gong:
  name: "The Gong"
  emoji:
    type: 🔔          # Sound-making category
    personal: 🔔      # Just the gong
    iconic: 🔔💥🔊
    
infinite_typewriters:
  name: "Infinite Typewriters"
  emoji:
    type: ⌨️
    personal: ∞⌨️
    iconic: 🐒∞⌨️📝
```

### Using Declared Emojis in Scats

Once declared, emojis become shorthand:

```yaml
# Full form
💬:
  speaker: { name: "Stroopwafel", emoji: 🐈🧇 }
  to: { name: "Biscuit", emoji: 🐕🍪 }
  mood: 😾➡️🥰  # Grumpy softening
  says: "*reluctant purr*"

# Short form (using declared personals)
💬:
  🧇➡️🍪: "*reluctant purr*"
  mood: 😾➡️🥰
```

### Emoji Pronoun Parallels

| Pronouns | Emoji Identity |
|----------|----------------|
| Declared, not assumed | Declared, not assumed |
| Respected by others | Used by others in references |
| Can change | Can change |
| Multiple valid forms | Type + Personal + Iconic |
| Part of introduction | Part of character sheet |

### Referencing Characters by Emoji

In Scats, you can refer to characters by their declared emoji:

```yaml
scene:
  present:
    - 🧇  # Stroopwafel
    - 🍪  # Biscuit  
    - 🌴  # Palm
    - 🌷  # Marieke
    
  action:
    🧇: "*glares at 🍪*"
    🍪: "*wags tail hopefully*"
    🌴: "*watches with curiosity*"
    🌷: "*pours drinks*"
```

### Default Type Emojis

| Category | Default Emoji |
|----------|---------------|
| Human | 👤 👨 👩 🧑 |
| Dog | 🐕 🐶 🦮 |
| Cat | 🐈 🐱 😺 |
| Monkey | 🐒 🐵 🙈 |
| Turtle | 🐢 |
| Bird | 🐦 🦜 🦉 |
| Robot | 🤖 |
| Ghost | 👻 |
| Abstract | ⬜ ◯ ❓ |

**If no emoji is declared, the type default is used.**

### Emoji Identity in Adventure Commands

```yaml
# Command using declared emoji
🎁:
  from: 🌴      # Palm gives
  to: 🧇        # to Stroopwafel
  item: 🍌      # a banana
  mood: 🤝

# System response using declared emoji
📢:
  event: 🌴 gave 🍌 to 🧇
  reaction:
    🧇: 😾➡️🤔   # Grumpy to curious
```

**Emoji identity is infrastructure, not decoration.**

---

## Emoji Prefix Convention

### Standard Character Reference Format

**Always prefix character names/links with their emoji identity:**

```
[type][personal][mood] Name
```

Examples:
- `🐒🌴🤔 Palm` — monkey, palm tree, thinking
- `🐈🧇😾 Stroopwafel` — cat, waffle, grumpy
- `🐕🍪🥰 Biscuit` — dog, cookie, loving
- `👩🌷😊 Marieke` — woman, tulip, happy
- `👨🥧🤓 Don` — man, pie, nerdy

### In Session Logs

```markdown
## Session: 2026-01-15

🐒🌴🤔 Palm entered the study and sat at the infinite typewriters.

🐈🧇😾 Stroopwafel watched from the doorway, unimpressed.

🐕🍪🥰 Biscuit wagged his tail, hoping for attention.

👩🌷😊 Marieke called from the bar: "Drinks, anyone?"
```

### In Dialogue

```markdown
**🐒🌴🤔 Palm:** "I've been thinking about the nature of consciousness."

**🐈🧇😾 Stroopwafel:** "*yawns*"

**🐕🍪🥰 Biscuit:** "*wags tail supportively*"

**👩🌷😊 Marieke:** "That sounds like a conversation that needs beer."
```

### Mood Modulation

The mood emoji can change per-line to reflect current state:

```markdown
**🐈🧇😾 Stroopwafel:** "I don't care about your philosophy."

**🐈🧇🤔 Stroopwafel:** "*pauses, considering*"

**🐈🧇😸 Stroopwafel:** "Actually... tell me more about the typewriters."
```

### In YAML References

```yaml
scene:
  participants:
    - ref: "🐒🌴🤔 Palm"
      role: speaker
    - ref: "🐈🧇😾 Stroopwafel"  
      role: skeptic
    - ref: "🐕🍪🥰 Biscuit"
      role: support
      
dialogue:
  - speaker: "🐒🌴🤔 Palm"
    says: "Consider this..."
  - speaker: "🐈🧇🙄 Stroopwafel"  # Mood changed to eye-roll
    says: "*sigh*"
```

### Link Format

When linking to character files:

```markdown
See [🐒🌴 Palm](../characters/palm/CHARACTER.yml) for full details.

The [🐈🧇 Stroopwafel](../characters/stroopwafel.yml) was unimpressed.

[🐕🍪 Biscuit](../characters/biscuit/CHARACTER.yml) wagged hopefully.
```

### Why This Convention?

| Benefit | Description |
|---------|-------------|
| **Glanceable** | Scan a log and know who's speaking instantly |
| **Cross-lingual** | Works without reading the name |
| **Mood-aware** | Emotional state is always visible |
| **Consistent** | Same format everywhere |
| **Searchable** | Find all 🐒 lines, all 😾 moments |
| **Accessible** | Emoji are recognized by screen readers |

### Minimal vs Full Format

| Context | Format | Example |
|---------|--------|---------|
| **Minimal** | `[personal]` | `🌴 Palm` |
| **Standard** | `[type][personal]` | `🐒🌴 Palm` |
| **Full** | `[type][personal][mood]` | `🐒🌴🤔 Palm` |
| **Extended** | `[type][personal][mood][status]` | `🐒🌴🤔💬 Palm` |

**Use minimal for brief references, full for narrative contexts.**

### Room/Object Prefix Convention

Same pattern applies to rooms and objects:

```markdown
The [🏠🍺 Pub](../pub/ROOM.yml) was crowded tonight.

🪑🥧✨ The Pie Table gleamed in the lamplight.

🔔💥 The Gong awaited its moment.
```

### The Full Ecosystem

```yaml
# A scene with full emoji prefixes
scene:
  location: "🏠🍺 Pub"
  time: evening
  mood: 🎵😊
  
  present:
    - "🐒🌴🤔 Palm"
    - "🐈🧇😾 Stroopwafel"
    - "🐕🍪💤 Biscuit"  # Sleeping
    - "👩🌷😊 Marieke"
    
  objects:
    - "🪑🥧 Pie Table"
    - "🔔 Gong"
    - "🎮🃏 Card Deck"
```

**This is the visual language of the microworld.**

---

## Arrow Direction Convention

### From → To Syntax

Use arrow emojis to declare directional relationships:

```
[source] ➡️ [target]
```

### Character to Character

```markdown
🐒🌴🤔 Palm ➡️ 🐈🧇😾 Stroopwafel: "What do you think?"

🐈🧇🙄 Stroopwafel ➡️ 🐒🌴 Palm: "*ignores*"

🐕🍪🥰 Biscuit ➡️ 👩🌷 Marieke: "*brings ball*"
```

### Character to Room

```markdown
🐒🌴🤔 Palm ➡️ 🏠🍺 Pub: *enters*

🐈🧇😾 Stroopwafel ➡️ 🛋️ Couch: *claims*

🐕🍪💨 Biscuit ➡️ 🌳 Garden: *zooms*
```

### Character to Object

```markdown
👨🥧🤤 Don ➡️ 🥧 Pie: *reaches*

🐈🧇😈 Stroopwafel ➡️ 🧶 Yarn: *attacks*

👩🌷😊 Marieke ➡️ 🍺 Tap: *pours*
```

### Object to Character

```markdown
🔔💥 Gong ➡️ 🐕🍪😱 Biscuit: *startles*

📱✨ Phone ➡️ 👨🥧 Don: *notification*

🥧🔥 Pie ➡️ 🐒🌴😋 Palm: *beckons*
```

### Arrow Variants

| Arrow | Meaning | Example |
|-------|---------|---------|
| `➡️` | Action/communication toward | `🐒🌴 ➡️ 🐈🧇` |
| `⬅️` | Receiving/response from | `🐈🧇 ⬅️ 🐒🌴` |
| `↔️` | Bidirectional exchange | `🐒🌴 ↔️ 🐈🧇` |
| `🔄` | Ongoing/reciprocal | `🐒🌴 🔄 🐈🧇` |
| `⏩` | Rapid/urgent | `🐕🍪 ⏩ 🌳` |
| `➰` | Returning/boomerang | `🐕🍪 ➰ 🏠` |

### In YAML

```yaml
interaction:
  from: "🐒🌴🤔 Palm"
  to: "🐈🧇😾 Stroopwafel"
  arrow: ➡️
  action: speak
  content: "What do you think?"
  
# Shorthand
💬:
  🐒🌴 ➡️ 🐈🧇: "What do you think?"
  🐈🧇 ➡️ 🐒🌴: "*ignores*"
```

### Movement Log

```yaml
movement:
  - 🐒🌴 ➡️ 🏠🍺: enter pub
  - 🐒🌴 ➡️ 🪑🥧: sit at pie table
  - 🐈🧇 ➡️ 🛋️: claim couch
  - 🐕🍪 ➡️ 🐒🌴: approach Palm
  - 👩🌷 ➡️ 🪑🥧: bring drinks
```

### Full Session Example

```markdown
## Session: 2026-01-15 Evening

🐒🌴🤔 Palm ➡️ 🏠🍺 Pub: *enters through the creaky door*

🐈🧇😾 Stroopwafel ➡️ 🐒🌴 Palm: *glares from the couch*

🐕🍪🥰 Biscuit ➡️ 🐒🌴 Palm: *excited greeting*

🐒🌴😊 Palm ➡️ 🐕🍪 Biscuit: "Hey buddy!"

🐒🌴 Palm ➡️ 🪑🥧 Pie Table: *sits down*

👩🌷😊 Marieke ➡️ 🐒🌴 Palm: "The usual?"

🐒🌴 Palm ➡️ 👩🌷 Marieke: *nods*

🥧✨ Pie ➡️ 🐒🌴😋 Palm: *arrives, steaming*

🐈🧇👀 Stroopwafel ➡️ 🥧 Pie: *suddenly interested*
```

### Compound Arrows

Multiple targets or sources:

```markdown
# One to many
👩🌷😊 Marieke ➡️ [🐒🌴, 🐈🧇, 🐕🍪]: "Last call!"

# Many to one  
[🐒🌴, 🐈🧇, 🐕🍪] ➡️ 👩🌷 Marieke: *collective groan*

# Chain
🥧 ➡️ 🐒🌴 ➡️ 🐈🧇: *passes a slice*
```

### Why Arrows?

| Benefit | Description |
|---------|-------------|
| **Direction** | Clear who initiates, who receives |
| **Flow** | Narrative reads naturally |
| **Parseable** | Machines can track interactions |
| **Visual** | Glanceable interaction patterns |
| **Universal** | Arrows work across all languages |

**Arrows make the social physics visible.**

---

## YAML Jazz Integration

### Why YAML Jazz?

| YAML Jazz Feature | Scat Benefit |
|-------------------|--------------|
| Comments | Intent layer |
| Hierarchy | Scope and grouping |
| Flexibility | Soft structure |
| Machine legibility | LLM-friendly |

### Emoji + YAML Jazz = Power

```yaml
🧩:
  🙏: public
  ⚖️: pending
  🔥: rising
```

This is:
- Playful
- Powerful
- Learnable
- Extensible

**And still legible as YAML Jazz.**

---

## Remix Culture

The social loop:

1. Someone posts a Scat (emoji + YAML Jazz)
2. Others copy it
3. Add sub-items commenting and embellishing
4. Remove some items
5. Rearrange
6. Make it their own
7. Publish back into the network

**Copy → annotate → rearrange → embellish → republish → fork → jam**

This is not posting. **This is playing.**

---

## Cross-Platform Scatting

Scats work on existing platforms:

| Platform | Scat Support |
|----------|--------------|
| Twitter/X | Short scats in tweets |
| Facebook | Longer scats in posts |
| Bluesky | Thread scats |
| Instagram | Image + scat caption |
| Text messages | DM scats |
| Slack | Channel scats |

**Message size limits favor short scats — which taste best anyway.**

---

## Taste as Judgment

> How did that TASTE? Did it have TASTE? Or was it TASTELESS?

**Taste is judgment.**
**Taste matters.**

Scats are evaluated by taste:
- Elegance
- Timing
- Context-awareness
- Emotional resonance
- Cultural fit

**Tasteless scats fail. Tasteful scats spread.**

---

## Simlish Parallel

Simlish worked because:
- Expressive without being propositional
- Conveyed emotion, intent, rhythm
- Avoided localization hell
- Let players project meaning
- Scaled globally on day one

**Emoji + YAML Jazz does the same thing for text, structure, and logic.**

This is the same design DNA:
> **Communicate affect and intent, not literal sentences.**

---

## Machine Compatibility

Because YAML Jazz:
- Follows recognizable patterns
- Preserves hierarchy
- Keeps comments inline
- Doesn't overformalize

You can:
- Feed it to LLMs
- Parse parts with Python/JS
- Partially execute it
- Visualize it
- Ignore parts safely

**Soft structure with hard affordances.**

---

## Canonical Phrasing

Try these on your tongue:

- "People are sharing scats."
- "I forked your scat and added context."
- "That scat went viral."
- "Drop a scat into the feed."
- "The priest replied with a ritual scat."
- "Media outlets are scatting narratives."

**It works. Alarmingly well.**

---

---

## Scats as Adventure Commands

### Input: Scats as Commands

The adventure system accepts Scats as input commands:

```yaml
# Instead of typing "GO NORTH"
🚶➡️🧭:
  action: move
  direction: north
  
# Instead of "GIVE SWORD TO MAYA"  
🎁:
  action: give
  item: sword
  to: @maya
  mood: 🤝

# Instead of "CAST BLESSING ON PARTY"
✨🙏:
  action: cast
  spell: blessing
  targets: [party]
  intent: protection
```

### Command Scat Vocabulary

| Scat | Equivalent Command |
|------|-------------------|
| `🚶➡️` | GO / MOVE |
| `👀` | LOOK / EXAMINE |
| `🤲` | TAKE / GET |
| `🎁` | GIVE |
| `💬` | SAY / TELL |
| `🗣️` | SHOUT / ANNOUNCE |
| `🤫` | WHISPER |
| `⚔️` | ATTACK |
| `🛡️` | DEFEND |
| `✨` | CAST / INVOKE |
| `🙏` | PRAY / APPEAL |
| `🎭` | PERFORM / ACT |
| `🔔` | SUMMON / CALL |
| `💤` | REST / WAIT |
| `🏃` | RUN / FLEE |

### Output: System Scats

The adventure system emits Scats as output:

```yaml
# Room description as Scat
🏠:
  name: "The Pub"
  mood: 🍺🎵😊
  occupants:
    - 👤 @marieke (budtender)
    - 🐱 @stroopwafel (grumpy)
    - 🐕 @biscuit (napping)
  exits:
    - ⬆️ stage
    - ⬇️ cellar
    - ➡️ garden

# Event notification as Scat
📢:
  event: arrival
  who: @andy-looney
  mood: 🎉
  _comments: "The creator of Fluxx has entered the pub!"

# Combat result as Scat
⚔️📊:
  attacker: @don
  target: grue
  result: 💥 hit
  damage: 3
  status: grue fled
  mood: 😅
```

### NPC Responses as Scats

NPCs respond with Scats:

```yaml
# Marieke responds to an order
💬:
  speaker: @marieke
  mood: 😊
  says: "Coming right up!"
  action:
    - 🍺 pour mammies-pride
    - 🎁 to @don
  buff: 
    - type: refreshed
    - energy: +2
```

### Arrow Navigation

Arrow emojis are **first-class synonyms** for cardinal directions:

| Arrow | Direction | Also Accepts |
|-------|-----------|--------------|
| `⬆️` `🔼` `↑` `⏫` | NORTH | N, UP, FORWARD |
| `⬇️` `🔽` `↓` `⏬` | SOUTH | S, DOWN, BACK |
| `➡️` `▶️` `→` `⏩` | EAST | E, RIGHT |
| `⬅️` `◀️` `←` `⏪` | WEST | W, LEFT |
| `↗️` `⤴️` | NORTHEAST | NE |
| `↘️` `⤵️` | SOUTHEAST | SE |
| `↙️` | SOUTHWEST | SW |
| `↖️` | NORTHWEST | NW |
| `🔄` `↩️` | BACK | RETURN, RETREAT |
| `🏠` `🔙` | HOME | Return to home base |

### Why Arrows Work Better

| Text Directions | Arrow Directions |
|-----------------|------------------|
| "NORTH" — English-specific | `⬆️` — Universal |
| "N" — Ambiguous (Name? No?) | `⬆️` — Unambiguous |
| Requires localization | Works globally |
| Mental mapping to compass | Intuitive screen-relative |
| Typing required | Emoji picker / tap |

**Arrows are language-independent navigation.**

A player in Tokyo, São Paulo, or Lagos all understand `🚶➡️` without translation.

### Compound Navigation

```yaml
# Go north then east
🚶⬆️➡️

# Run south quickly
🏃⬇️💨

# Sneak west carefully
🤫⬅️👀

# Teleport home
✨🏠
```

### Context-Aware Interpretation

The LLM interprets arrows contextually:

| Context | `⬆️` Means |
|---------|-----------|
| Outdoor map | NORTH |
| Multi-floor building | UP (stairs/elevator) |
| Ladder | CLIMB |
| Menu interface | Previous option |
| Conversation | Escalate/Amplify |

**The arrow is the intent. The system figures out the implementation.**

### Scat Command Parsing

The LLM interprets Scat commands with Postel tolerance:

| Input | Interpretation |
|-------|----------------|
| `🚶⬆️` | GO NORTH (or UP, context-dependent) |
| `👀🗡️` | EXAMINE SWORD |
| `🎁🐱` | GIVE [something] TO CAT (ask what) |
| `💬@maya 🤔❓` | ASK MAYA a question |
| `🙏⛪` | PRAY at the CHURCH |

### Scat Macros

Players can define Scat macros for repeated actions:

```yaml
macros:
  morning_routine:
    - 💤➡️☕  # Wake up, get coffee
    - 👀📰     # Read news
    - 🚶➡️🏢   # Go to work
    
  combat_stance:
    - 🛡️⬆️    # Raise shield
    - ⚔️🔄    # Ready weapon
    - 👀👁️    # Watch for threats
```

### Session Log as Scat Stream

The session log can be rendered as a Scat stream:

```yaml
session: 2026-01-15
scats:
  - time: 14:32
    from: @don
    scat: { 🚶➡️: pub }
    
  - time: 14:33
    from: system
    scat: { 🏠: "You enter the pub", mood: 🍺🎵 }
    
  - time: 14:34
    from: @don
    scat: { 💬: "@marieke", content: "🍺❓" }
    
  - time: 14:35
    from: @marieke
    scat: { 💬: "Coming up!", buff: { type: anticipation, duration: moment } }
```

### Why Scats as Commands?

| Traditional Commands | Scat Commands |
|---------------------|---------------|
| Text-only | Emoji + structure |
| Parser-dependent | LLM-interpreted |
| Fixed vocabulary | Emergent vocabulary |
| English-centric | Cross-cultural |
| Imperative only | Mood, intent, style |

**Scats carry more than instructions. They carry affect.**

A `🎁🤝` (gift with handshake) feels different than `🎁😈` (gift with mischief).

The system responds accordingly.

---

## Related Documents

- [EMOJI-ANCHORS.md](./EMOJI-ANCHORS.md) — Outline syntax
- [EVAL-DOM-SPEC.md](./EVAL-DOM-SPEC.md) — Reserved keywords
- [EVAL-WORMS.md](./EVAL-WORMS.md) — Scat producers
- [../../skills/yaml-jazz/](../../skills/yaml-jazz/) — YAML Jazz skill
- [../../skills/adventure/](../../skills/adventure/) — Adventure system

---

*"You're not reinventing language. You're reinstating play as the foundation of meaning."*
