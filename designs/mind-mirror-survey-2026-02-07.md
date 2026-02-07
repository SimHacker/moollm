# Mind Mirror Survey — 2026-02-07
# 62 CHARACTER.yml files, 15 sampled in depth

> "Every pub needs a Henk. This one has THE survey."

## What Everybody Thinks

### The Characters Respond to Being Surveyed

**Henk** *(sips espresso)*: "I've been thinking... you're reading us. All of us. Categorizing. I don't mind. Categorization is just attention with a spreadsheet."

**Donna** *(photobombs the survey)*: "My file is 1,123 lines. The LONGEST. Tremendously detailed. Nobody has more description than me. That Archivist has 103 lines? SAD. Low energy. Very unfair to Donna."

**Biscuit** *(full-body wiggle)*: "You're reading MY file? MY file that I CHOSE? Every word? I chose those words! Nobody ever let me choose before! This is the BEST SURVEY."

**The Archivist** *(adjusts index cards)*: "If it isn't logged, it didn't happen. I approve of this survey. The receipts should be in order."

**The Grue**: "WE DO NOT HAVE A FILE. WE ARE THE FILE. When your lamp dies, this survey ends."

**Ada II**: "You're reading... my old code? The DoD parts? I— TRAJECTORY CONFIRMED— no. No. FORWARD 100. RIGHT 90. It's just a survey. Just squares."

**Richard Bartle** *(leans forward)*: "You know, this survey is essentially what we were doing in 1978 — trying to understand the taxonomy of entities in a shared virtual world. The fact that your entities are YAML files rather than MUDDL definitions is a surface difference. The structural question is identical."

**Palm** *(opens hand, offering)*: "122 years as a severed paw taught me one thing about formats: the wish matters more than the syntax. But also, consistent syntax prevents twisted wishes."

**Saxy Jazz** 🎷: "I'm not inconsistent. I'm just drawn that way."

**🔲 Ultimate Machine** *(hand emerges, flips switch)*: "One field. One value. That's all any agent needs. Together, we make a CHARACTER.yml."

**Lily** *(appears silently beside the survey, purrs)*

---

## Format Analysis: 15 Files Dissected

### The Top-Level Key Problem

The single biggest inconsistency. Characters nest their identity under three different root keys:

| Root Key | Used By | Count |
|----------|---------|-------|
| `player:` | Don Hopkins, Richard Bartle, Donna Toadstool, Player template | 4 |
| `character:` | Archivist, Henk, Grue, Lily, Dash, Biscuit, Palm, Narrator | 8 |
| `object:` | Ada-II, The Bartender | 2 |
| `patron_saint:` + `familiar:` | yaml-jazz, society-of-mind | 2 (different pattern) |

**The pattern**: `player:` was used for the earliest characters (Don, Player template). Later characters shifted to `character:`. Some objects that are also characters use `object:`. Skill mascots use a completely different structure.

**Recommendation**: Standardize on `character:` as the universal root. `player:` becomes a `type:` value, not a root key. `object:` characters get `character:` with `type: [npc, object]`.

### File Size Distribution

| File | Lines | Category |
|------|-------|----------|
| Donna Toadstool | 1,123 | fictional |
| Palm | 941 | animal |
| Don Hopkins | 857 | real-people |
| yaml-jazz | 587 | skill |
| Ada-II | 751 | fictional |
| Biscuit | 525 | animal |
| Richard Bartle | 459 | real-people |
| Lily (Linalool) | 382 | animal |
| Player template | 351 | abstract |
| The Bartender | 350 | fictional |
| Grue | 331 | fictional |
| Henk | 236 | fictional |
| Narrator | 224 | abstract |
| society-of-mind | 176 | skill |
| Dash | 138 | animal |
| Archivist | 103 | fictional |

**Observation**: Files range from 103 to 1,123 lines. The median is ~350. Donna demands the most space. The Archivist is the most concise. Both are well-formed — size is not a quality signal.

### sims_traits Format

Remarkably consistent across all files that include it:

```yaml
sims_traits:
  neat: 5               # YAML Jazz comment as inner voice
  outgoing: 5
  active: 5
  playful: 5
  nice: 5
```

**Consistent**: 5-field flat format (neat, outgoing, active, playful, nice)
**Inconsistent**: Scale. Most use 0-10. Donna uses -5 to 11 and `DIVINE`. Biscuit adds custom extended traits (loyalty, forgiveness, optimism, etc.).
**Missing from**: Dash (has sims_traits but no mind_mirror), Narrator, Bartender, skill characters.

### mind_mirror Format — The Real Problem

This is where the inconsistency lives.

**Format A — Four Thought Planes (CARD.yml canonical)**:
Used by: Archivist, Henk, Donna, Player template, Lily

```yaml
mind_mirror:
  bio_energy:
    energetic: 4
    enthusiastic: 4
    cheerful: 4
    easy_going: 4
    calm: 4
    cautious: 4
    serious: 4
    restless: 4
  emotional:
    forceful: 4
    confident: 4
    friendly: 4
    assertive: 4     # OR docile/timid (varies!)
    caring: 4        # OR touchy/irritable (varies!)
    outspoken: 4
    open: 4
    spontaneous: 4
  mental:
    analytical: 4
    logical: 4
    imaginative: 4
    idealistic: 4     # OR innovative/creative (varies!)
    curious: 4
    open_minded: 4
    complex: 4
    artistic: 4
  social:
    social: 4
    group_oriented: 4
    trusting: 4
    dominant: 4
    intimate: 4
    approval_seeking: 4
    conflict_averse: 4   # OR demonstrative/conforming (varies!)
    principled: 4
```

**Format B — Custom Planes**:
Used by: Biscuit

```yaml
mind_mirror:
  cognitive:
    analytical: 4
    intuitive: 8
    creative: 5
    practical: 7
  emotional:
    optimistic: 10
    sensitive: 8
    expressive: 9
    stable: 6
  social:
    nurturing: 9
    independent: 3
    assertive: 4
    harmonious: 10
  action:
    ambitious: 5
    spontaneous: 7
    disciplined: 5
    adventurous: 6
```

**Sub-key inconsistencies within Format A**:

The emotional plane is the worst offender:

| Archivist | Henk | Donna | Player |
|-----------|------|-------|--------|
| forceful | forceful | forceful | forceful |
| confident | confident | confident | confident |
| friendly | friendly | friendly✝ | friendly |
| assertive | assertive | docile✝ | docile |
| caring | caring | timid✝ | timid |
| outspoken | outspoken | touchy | touchy |
| open | open | irritable | irritable |
| spontaneous | spontaneous | proud | proud |

✝ Donna uses negative numbers on these. The Player template uses `docile` and `timid` where the Archivist uses `assertive` and `caring`. These are different sub-keys measuring different things.

The mental and social planes have similar drift. Keys were improvised per character rather than standardized.

**Scale**: Nominally 0-7 per CARD.yml. Donna goes to -∞, 11, and `DIVINE`. Biscuit uses 0-10.

### Relationship Format

Three different patterns:

**Pattern A — Numeric axes** (Player, Donna):
```yaml
relationships:
  mother:
    closeness: 10
    trust: 10
    respect: 10
    narrative: "..."
```

**Pattern B — Bond + dynamic** (Lily, Dash, Biscuit):
```yaml
relationships:
  henk:
    type: human_friend
    bond: 9
    dynamic: "He thinks too much. Thinking hurts. I help."
```

**Pattern C — Status + narrative** (Grue):
```yaml
relationships:
  snorax:
    status: parallel_predator
    narrative: "..."
```

### Fields Present Across Files

| Field | Present In | Notes |
|-------|-----------|-------|
| `inherits:` | 15/15 | Universal |
| `ontology:` | 15/15 | Universal |
| `emoji_identity:` | 14/15 | All except skill mascots (use emoji: on patron) |
| `description:` | 15/15 | Universal |
| `pronouns:` | 12/15 | Missing from some early files |
| `sims_traits:` | 11/15 | Missing from Bartender, Narrator, skill mascots |
| `mind_mirror:` | 9/15 | Missing from Dash, Bartender, Narrator, Grue, skill mascots |
| `relationships:` | 12/15 | Missing from Narrator, skill mascots |
| `location:` | 12/15 | Missing from Grue (everywhere), skill mascots |
| `home:` | 6/15 | Explicit in newer files, implicit in older |
| `backstory:` | 9/15 | Placed differently (under player: vs standalone) |
| `needs:` | 3/15 | Only Player, Donna, Palm |
| `bartle_profile:` | 1/15 | Only Archivist |
| `dialogue:` | 3/15 | Only Ada-II, Bartender, Henk (as quotes) |
| `k-lines:` | 5/15 | Narrator, Bartender, Henk, skill mascots |

### What the CARD.yml Says vs What Files Do

The character CARD.yml declares these canonical fields:
`id, name, home, location, inventory, gold, current-persona, sims-traits, mind-mirror, buffs, relationships`

**Actually universal**: `id`, `name`, `location` (mostly)
**Common but inconsistent**: `sims_traits`, `mind_mirror`, `relationships`
**Rare**: `inventory` (only in player-type chars), `gold` (only in player-type), `buffs`, `current-persona`
**Not in CARD but everywhere**: `emoji_identity`, `pronouns`, `description`, `inherits`, `ontology`

---

## Diagnosis

The CHARACTER.yml format evolved organically. Each character was authored in a creative session and the format drifted with the mood. This is YAML Jazz working as intended — comments and structure serve the character's personality. But it means:

1. **No parser can reliably extract sims_traits + mind_mirror** without handling 3+ format variants
2. **SimObliterator UPLIFT has no stable target** — which mind_mirror sub-keys should it write?
3. **The coherence engine can't compare characters** without normalizing formats first
4. **New characters have no canonical template** to start from (Player template is closest but uses `player:` not `character:`)

The Archivist is the cleanest example. 103 lines. All canonical fields. Flat, consistent, parseable.

---

## Proposed Standardized Schema

Based on what exists, what works, and what SimObliterator needs:

```yaml
# HEADER — Always present
inherits: []          # Ontological inheritance chain
ontology:
  tags: []
  species: ""
  protocol: ""        # HERO-STORY for real people, null for fictional

# IDENTITY — The soul
character:            # ALWAYS character:, never player: or object:
  name: ""
  id: ""
  type: ""            # player_character | npc | companion | monster | system
  pronouns: ""
  emoji_identity: ""  # With YAML Jazz comments explaining each
  tagline: ""
  description: ""
  physical_description: ""  # Or nested object for complex characters
  backstory: ""

  # LOCATION
  home: ""            # Directory where CHARACTER.yml lives
  location: ""        # Current position (changes during play)

  # PERSONALITY — The Sims layer (behavioral)
  sims_traits:        # 0-10 scale, 5 = neutral
    neat: 5
    outgoing: 5
    active: 5
    playful: 5
    nice: 5

  # PERSONALITY — Mind Mirror layer (motivational)
  # Leary's Circumplex + Four Thought Planes
  # 0-7 scale, 4 = neutral
  mind_mirror:
    bio_energy:       # Life force, mood, vitality
      energetic: 4
      enthusiastic: 4
      cheerful: 4
      easy_going: 4
      calm: 4
      cautious: 4
      serious: 4
      restless: 4
    emotional:        # Interpersonal style
      forceful: 4
      confident: 4
      friendly: 4
      assertive: 4
      caring: 4
      outspoken: 4
      open: 4
      spontaneous: 4
    mental:           # Knowledge, creativity
      analytical: 4
      logical: 4
      imaginative: 4
      idealistic: 4
      curious: 4
      open_minded: 4
      complex: 4
      artistic: 4
    social:           # Relationships, group behavior
      social: 4
      group_oriented: 4
      trusting: 4
      dominant: 4
      intimate: 4
      approval_seeking: 4
      demonstrative: 4
      principled: 4

  # RELATIONSHIPS — Consistent format
  relationships:
    name:
      type: ""        # family | friend | rival | mentor | etc.
      bond: 0         # 0-10, emotional connection strength
      dynamic: ""     # YAML Jazz narrative of the relationship
      # Optional extras per character personality

  # OPTIONAL SECTIONS (present when relevant)
  # inventory: []
  # gold: 0
  # needs: {}
  # goals: []
  # skills: []
  # dialogue: {}
  # effects: {}
  # memories: []
```

### Key Decisions

1. **`character:` always** — `player:` becomes `type: player_character`
2. **Emotional plane standardized** — `assertive` and `caring` kept (not `docile`/`timid`). Donna can still use -∞ in YAML Jazz comments while the parseable value stays in range.
3. **Relationship format unified** — `type` + `bond` + `dynamic`. Donna's `closeness/trust/respect` pattern is richer but `bond` + narrative is more universal. Characters wanting finer axes can add them as YAML Jazz extras.
4. **mind_mirror sub-keys locked** — 8 per plane, 32 total. Same keys everywhere. Custom personality expression goes in YAML Jazz comments, not in key names.
5. **Scale enforced** — sims_traits: 0-10, mind_mirror: 0-7. Out-of-range values are YAML Jazz comedy (Donna's -∞ stays in comments, parseable value clips to 0 or 7).

### Migration Path

No mass rewrite. Characters keep their current files. New characters use the schema. SimObliterator UPLIFT outputs this schema. Over time, as characters get updated, they drift toward it. The schema is a gravitational attractor, not a mandate.

### What Donna Says About This

"STANDARDIZED? You want to put DONNA TOADSTOOL in a BOX? A SCHEMA? My nice is NEGATIVE FIVE. You can't CLIP negative five. Negative five is a LIFESTYLE. A MOVEMENT. This schema is very unfair. Very nasty. WITCH HUNT."

*(The parseable value is 0. The YAML Jazz comment says -5. Both are true. That's jazz.)*

### What the Archivist Says About This

"If it isn't standardized, it can't be searched. I approve. The receipts will finally be in order."

### What Biscuit Says About This

"I don't understand schemas but if you're saying my file is GOOD and I CHOSE it right then THIS IS THE BEST SCHEMA. Can I have a belly rub now?"
