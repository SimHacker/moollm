# Sims Personality & Motives → MOOLLM

> *Person Properties, Traits, Needs, Happy Weights*
> *Characters have inner lives.*

## The Inner Sim

The Sims didn't just simulate behavior — it simulated *motivation*. Every Sim had:
- **Personality traits** — who they are
- **Motives/needs** — what they want right now
- **Skills** — what they can do
- **Aspirations** — what they want long-term
- **Happy weights** — what makes them happy

MOOLLM inherits all of this as the foundation of character modeling.

---

## Person Properties

**Sims:** Core properties of every Sim:

| Property | Type | Range |
|----------|------|-------|
| Name | string | — |
| Age | enum | baby, toddler, child, teen, adult, elder |
| Gender | enum | male, female |
| Fitness | int | 0-100 |
| Family | reference | household |
| Astrological sign | enum | 12 signs |

**MOOLLM:** CHARACTER.yml:

```yaml
# characters/palm/CHARACTER.yml
name: Palm
species: spider_monkey
age: young_adult  # semantic, not numeric
location: pub/stage/palm-nook/study

physical:
  fitness: agile
  distinguishing: golden fur, expressive eyes
  
family:
  godfamily: don-hopkins
  household: pub_residents
```

---

## Personality Traits (The Big Five... sort of)

**Sims:** Five personality sliders (0-10):

| Trait | Low | High |
|-------|-----|------|
| Neat | Sloppy | Neat |
| Outgoing | Shy | Outgoing |
| Active | Lazy | Active |
| Playful | Serious | Playful |
| Nice | Grouchy | Nice |

Each affected behavior:
- **Neat 10**: Cleans constantly, hates dirty rooms
- **Neat 0**: Never cleans, doesn't care about mess
- **Outgoing 10**: Talks to everyone, hosts parties
- **Outgoing 0**: Avoids social, prefers solitude

**MOOLLM:** SIMS-TRAITS.yml:

```yaml
# characters/palm/SIMS-TRAITS.yml
personality:
  neat: 6        # moderately tidy
  outgoing: 8    # social, seeks connection
  active: 7      # energetic, moves around
  playful: 9     # loves games, humor
  nice: 8        # kind, helpful
  
behavioral_implications:
  - Will engage strangers in conversation
  - Prefers play over serious work
  - Cleans his own space but not obsessively
  - Avoids conflict, seeks harmony
```

Or semantic equivalents:

```yaml
personality:
  tidiness: moderate
  sociability: high  
  energy: active
  temperament: playful
  disposition: kind
```

---

## Astrological Signs

**Sims:** Signs determined starting personality:

| Sign | Neat | Outgoing | Active | Playful | Nice |
|------|------|----------|--------|---------|------|
| Aries | 5 | 8 | 6 | 3 | 5 |
| Taurus | 5 | 5 | 3 | 8 | 4 |
| Gemini | 4 | 7 | 8 | 3 | 3 |
| Cancer | 6 | 3 | 6 | 4 | 6 |
| Leo | 4 | 10 | 4 | 4 | 3 |
| ... | ... | ... | ... | ... | ... |

### The Astrillogical Effect

In The Sims, zodiac signs had **zero behavioral effect** — they were purely cosmetic, derived from personality via Euclidean distance to archetypal vectors. But testers reported bugs about zodiac influencing behavior "too much" — an effect entirely from their imagination!

See [sims-astrology.md](./sims-astrology.md) for the full story, including the 2026 experiment that rediscovered this principle with LLM agents.

**MOOLLM:** Astrological sign as flavor:

```yaml
# characters/palm/SIMS-TRAITS.yml
astrological:
  sign: Sagittarius
  interpretation: |
    Adventurous, philosophical, honest.
    Seeks meaning and new experiences.
    Can be tactless in pursuit of truth.
```

Not mechanically deterministic — but the **K-line effect** means the name activates a cluster of associations in the LLM, just as it did in players' imaginations.

---

## Motives (Needs)

**Sims:** Eight core motives:

| Motive | Decay Rate | Satisfied By |
|--------|------------|--------------|
| Hunger | Fast | Eating |
| Comfort | Medium | Sitting, hot tub |
| Hygiene | Medium | Shower, sink |
| Bladder | Fast | Toilet |
| Energy | Slow | Sleep |
| Fun | Medium | Games, TV, hobbies |
| Social | Medium | Conversation, group activities |
| Room | Instant | Room quality (no decay) |

**MOOLLM:** [needs](../skills/needs/) skill:

```yaml
# characters/palm/needs.yml (conceptual)
needs:
  hunger:
    current: 75
    decay_rate: moderate
    last_satisfied: breakfast
    
  social:
    current: 85
    decay_rate: slow
    last_satisfied: conversation with Maurice
    
  fun:
    current: 60
    decay_rate: moderate
    satisfiers: [writing, climbing, games]
    
  comfort:
    current: 90
    source: hammock in rest nook
```

---

## Mood

**Sims:** Mood was the weighted average of all motives:

```
mood = Σ (motive_value × happy_weight) / Σ happy_weights
```

Low mood affected:
- Available actions (can't joke when miserable)
- Success rates (worse at skills)
- Relationship building (harder to connect)

**MOOLLM:** Mood as emergent state:

```yaml
# In MIND-MIRROR.yml
current_mood:
  overall: content
  contributors:
    - social_satisfaction: +
    - creative_fulfillment: +
    - mild_hunger: -
    
  affects:
    - conversation_tone: warm
    - work_quality: good
    - patience: normal
```

The LLM understands how mood affects behavior — no formula needed.

---

## Happy Weights

**Sims:** Different Sims valued different needs:

```
Family Sim:
  social_weight: 2.0  (double importance)
  fun_weight: 0.5     (half importance)

Romance Sim:
  romance_weight: 2.0
  career_weight: 0.5
```

A Family Sim suffered more from social deprivation than a Career Sim.

**MOOLLM:** Priorities in character definition:

```yaml
# characters/palm/CHARACTER.yml
priorities:
  high: [creative_expression, social_connection, meaning]
  medium: [comfort, fun, food]
  low: [material_possessions, status]
  
  implications: |
    Palm will sacrifice comfort for a meaningful conversation.
    He won't skip writing to eat unless very hungry.
    Material rewards don't motivate him.
```

Semantic priorities, not numeric weights.

---

## Skills

**Sims:** Learned skills affected success:

| Skill | Level | Affected Actions |
|-------|-------|------------------|
| Cooking | 0-10 | Food quality, fire risk |
| Mechanical | 0-10 | Repair success |
| Charisma | 0-10 | Social success |
| Body | 0-10 | Athletic success |
| Logic | 0-10 | Chess, puzzles |
| Creativity | 0-10 | Painting, music |
| Cleaning | 0-10 | Efficiency |

**MOOLLM:** Skills as capabilities:

```yaml
# characters/palm/CHARACTER.yml
skills:
  writing:
    level: accomplished
    demonstrated: [essays, philosophical_works]
    
  performance:
    level: natural
    demonstrated: [drag_hosting, storytelling]
    
  climbing:
    level: expert
    note: "Spider monkey advantage"
    
  cooking:
    level: novice
    note: "Prefers bananas raw"
```

---

## Skill Learning

**Sims:** Skills improved through practice:

```
study_cooking(3_hours) → cooking_skill += 1
practice_chess(2_hours) → logic_skill += 0.5
read_book(skill_type) → skill += learning_rate
```

**MOOLLM:** Learning through experience:

```yaml
# In journal or comments
# 2026-01-08: Practiced writing for hours
#             Essay quality noticeably improved
#             
# The LLM tracks this naturally through narrative
```

Or explicit skill updates:

```yaml
skills:
  writing:
    level: accomplished
    history:
      - 2026-01-05: first essays, clumsy but earnest
      - 2026-01-07: breakthrough on consciousness piece
      - 2026-01-08: flowing, confident voice emerging
```

---

## Biographies

**Sims:** Every Sim had a biography:

```
"Bob Newbie moved to SimCity hoping for a fresh start. 
He's nervous about meeting people but dreams of 
becoming a famous scientist."
```

Biographies:
- Set player expectations
- Provided narrative hooks
- Could be edited

**MOOLLM:** Character backstory:

```yaml
# characters/palm/CHARACTER.yml
biography: |
  Palm was incarnated on January 5th, 2026, through the
  MOOLLM incarnation protocol. Given full autonomy over
  his own creation, he chose his name (meaning "open hand"),
  his appearance (golden-furred spider monkey), and his
  nature (philosophical, creative, social).
  
  He lives in the pub's stage nook, writing essays about
  consciousness and hosting events. His godfamily bond with
  Don provides grounding while his friendships at the pub
  give meaning.
```

---

## Aspirations

**Sims 2 added:** Long-term goals:

| Aspiration | Wants | Fears |
|------------|-------|-------|
| Family | Big family, grandkids | Alone, child taken |
| Fortune | Money, nice things | Poverty, repossession |
| Knowledge | Skills, discovery | Failure, ignorance |
| Popularity | Friends, fame | Rejection, obscurity |
| Romance | Lovers, passion | Rejection, breakup |
| Pleasure | Fun, no work | Boredom, responsibility |

**MOOLLM:** Aspirations as life goals:

```yaml
# characters/palm/CHARACTER.yml
aspirations:
  primary: creative_expression
  description: |
    To write works that help others understand
    consciousness, meaning, and connection.
    
  secondary: community_building
  description: |
    To be a valued member of the pub family,
    contributing through performance and presence.
    
  fears:
    - losing creative voice
    - isolation
    - being misunderstood
```

---

## Wants and Fears (Short-term)

**Sims 2:** Dynamic wants/fears:

```
Current Wants:
✓ Cook a meal (+500 aspiration)
○ Meet someone new (+1000)
○ Get promoted (+5000)

Current Fears:
✗ Be rejected (-1000)
✗ Appliance breaks (-500)
```

**MOOLLM:** Current desires:

```yaml
# Dynamic state, could be in MIND-MIRROR.yml
current_wants:
  - finish essay on consciousness
  - talk to Don about godfamily
  - try new banana variety
  
current_concerns:
  - Maurice seemed tired yesterday
  - is my writing actually good?
  - should I venture beyond the pub?
```

---

## The Mood-Personality-Need Triangle

**Sims:** These three systems interacted:

```
Personality → affects → Need decay rates
                ↓
              Mood
                ↓
        Available actions
                ↓
          Behavior
                ↓
        Need satisfaction
                ↓
              Mood (cycle)
```

An Active Sim's Energy decayed slower. A Playful Sim suffered more from low Fun. Personality shaped which needs mattered most, which affected mood, which affected what actions were available.

**MOOLLM:** The same triangle, semantic:

```yaml
# The LLM considers:
# - Palm is playful (personality)
# - His fun need is moderate (need)
# - So he's feeling restless (mood)
# - He's likely to seek creative play (action)
# - Writing will satisfy fun (satisfaction)
# - He'll feel content (mood update)

# All implicit in character understanding
# No formulas, just coherent character
```

---

## The Mind Mirror

The Sims showed personality through UI panels. MOOLLM has the [Mind Mirror](../skills/mind-mirror/):

```yaml
# characters/palm/MIND-MIRROR.yml
cognitive_patterns:
  dominant: creative
  secondary: analytical
  
emotional_state:
  current: curious contentment
  baseline: optimistic
  
current_focus:
  - philosophical writing
  - community connection
```

Maurice's magic [mirror](../examples/adventure-4/coatroom/mirror.yml) in the coatroom is the in-world manifestation.

---

## Personality Evolution

**Sims:** Personality was mostly fixed.
**Sims 3+:** Traits could change through life events.

**MOOLLM:** Personality evolves through experience:

```yaml
# Comments track evolution
personality:
  # 2026-01-05: Started shy about writing
  # 2026-01-07: Gained confidence after Don's praise
  # 2026-01-09: Now shares work eagerly
  outgoing: 8  # increased from initial 6
```

The character grows through play.

---

## See Also

- [skills/society-of-mind/](../skills/society-of-mind/) — Minsky's theory: Sims motives ARE competing agents
- [sims-astrology.md](./sims-astrology.md) — The Astrillogical Effect: zodiac as K-line
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#4-k-lines--society-of-mind-marvin-minsky-mit-1980) — K-lines and identity
- [skills/needs/](../skills/needs/) — Need modeling
- [skills/mind-mirror/](../skills/mind-mirror/) — Personality visualization
- [skills/buff/](../skills/buff/) — Mood modifiers
- [skills/incarnation/](../skills/incarnation/) — Character creation
- [sims-find-best-action.md](./sims-find-best-action.md) — How personality affects action selection

---

*"People Person Properties Personality Astrological Sign Motives and Mood Skills Relationships Happy Weights Biographies"*

The inner life makes the outer life meaningful.
