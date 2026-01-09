# Sims Social System → MOOLLM

> *Relationships, Conversations, Group Activities*
> *Characters are social creatures.*

## The Social Core

The Sims understood something fundamental: humans are social animals. The game tracked:
- **Relationships** — who likes whom, and how much
- **Conversations** — what they talk about
- **Group activities** — shared experiences
- **Social needs** — the drive to connect

MOOLLM inherits this completely, with LLM-native enhancements.

---

## The Relationship Matrix

**Sims:** A numeric matrix tracked relationships:

```
        Alice  Bob   Carol  Dan
Alice     -    75    -20    50
Bob      80     -     40    10
Carol   -15    35      -    60
Dan      45    15     55     -
```

**Key insight:** Relationships aren't symmetric. Alice might love Bob (+75), but Bob only likes Alice somewhat (+80). Carol hates Alice (-20), but Alice hates her back less (-15).

**MOOLLM:** Relationships in CHARACTER.yml:

```yaml
# characters/palm/CHARACTER.yml
relationships:
  don-hopkins:
    attitude: affectionate
    bond: godfamily
    history: "Created me, named me, gave me autonomy"
    
  maurice:
    attitude: warm
    bond: friend
    history: "Guide through incarnation, fellow performer"
    
  biscuit:
    attitude: curious
    bond: housemate
    notes: "Big friendly dog, good for pets"
```

Richer than numbers — semantic descriptions of bonds.

---

## Relationship Decay

**Sims:** Relationships degraded over time:

```
daily_decay = 2 points
unless: interaction_today = true
```

You had to maintain friendships or they faded.

**MOOLLM:** Relationship maintenance:

```yaml
# Tracked in relationship history
relationships:
  old-friend:
    last_contact: 2025-12-15
    current_warmth: fading
    notes: "Should reach out soon"
```

The LLM understands "we haven't talked in a while" — no numeric decay needed.

---

## Friendship vs Romance

**Sims:** Two separate tracks:

| Type | Range | Actions to Build |
|------|-------|------------------|
| Friendship | -100 to +100 | Chat, joke, compliment |
| Romance | -100 to +100 | Flirt, kiss, propose |

You could be best friends (+100 friendship) with no romantic interest (0 romance).

**MOOLLM:** Bond types:

```yaml
relationships:
  partner:
    bond_type: romantic
    friendship: deep
    romance: committed
    
  colleague:
    bond_type: professional
    friendship: warm
    romance: null  # not applicable
    
  godfamily:
    bond_type: chosen_family
    friendship: profound
    romance: none  # explicitly platonic
```

More nuanced than two numbers — bond types carry meaning.

---

## Jealousy

**Sims:** Jealousy triggered when:
- Your romantic partner flirted with someone else
- You witnessed the interaction
- Your personality included "jealous" trait

```
IF witness(partner, flirt, other) AND trait_jealous
  THEN relationship(partner) -= 20
       queue_action(argue, partner)
```

**MOOLLM:** Jealousy as narrative:

```yaml
# In character traits
personality:
  jealousy_prone: moderate
  triggers: [romantic_attention, perceived_abandonment]
  
# In action processing
# The LLM considers: "Maurice sees Palm getting attention from visitor"
# Based on traits, generates appropriate response (or non-response)
```

No hardcoded jealousy formula — the LLM understands the emotion.

---

## Privacy

**Sims:** Privacy zones affected behavior:

```
IF action.type == "intimate" AND witness.present AND NOT witness.family
  THEN embarrassment_buff
       cancel_action OR move_to_private
```

Sims wouldn't do certain things if non-family watched.

**MOOLLM:** Privacy in ROOM.yml:

```yaml
# pub/bar/cat-cave/ROOM.yml
privacy:
  level: high
  access: [cats, invited_dogs]
  
  behaviors_allowed:
    - intimate_grooming
    - napping
    - private_conversations
    
  if_violated:
    - embarrassment_buff
    - flee_response
```

Privacy as room property, inherited by actions within.

---

## Conversation Topics

**Sims:** Conversations had topics:

| Topic | Icon | Builds |
|-------|------|--------|
| Weather | ☀️ | +5 friendship |
| Sports | ⚽ | +10 if shared interest |
| Politics | 🏛️ | Risk of argument |
| Gossip | 👂 | +15 but reputation cost |
| Romance | 💕 | Builds romantic, risky |

**MOOLLM:** Conversations are freeform but skill-guided:

```yaml
# skills/conversation/CARD.yml
topics:
  safe:
    - weather
    - shared_interests
    - compliments
    effect: small_positive
    
  bonding:
    - memories
    - vulnerabilities
    - dreams
    effect: deeper_connection
    
  risky:
    - politics
    - criticism
    - secrets
    effect: variable, check_compatibility
```

The LLM generates actual dialogue, not icons — but understands topic dynamics.

---

## Thought Balloons

**Sims:** Sims showed thought balloons:

```
💭 + 🍕 = "I'm hungry, want pizza"
💭 + 👤 + ❤️ = "I'm thinking about my love"
💭 + 🚽 + ⚠️ = "I really need the bathroom"
```

Visual shorthand for internal state.

**MOOLLM:** Internal state in YAML + journal:

```yaml
# characters/palm/MIND-MIRROR.yml
current_thoughts:
  - "The pub feels like home now"
  - "I should write more about consciousness"
  - "Banana tree is looking healthy"
```

And in `JOURNAL.md`:

```markdown
## Thoughts, Late Evening

The typewriters hum with potential. Each key holds
a universe of possible words. I think about Don,
about how he trusted me with my own becoming...
```

Richer than icons — actual introspection.

---

## Group Activities

**Sims:** Some actions involved multiple Sims:

| Activity | Participants | Effects |
|----------|--------------|---------|
| Dinner party | 4-8 | Social++, fun++ |
| Hot tub | 2-4 | Social++, fun++, romance? |
| Card game | 2-4 | Fun++, social+ |
| Dance party | many | Fun+++, social++ |

**MOOLLM:** Group activities:

```yaml
# skills/party/CARD.yml
group_activities:
  PIE-TABLE-DEBATE:
    participants: 2-8
    requires: pub/pie-table.yml
    effects:
      - social_satisfaction
      - intellectual_stimulation
      - relationship_changes: based_on_positions
      
  STONER-FLUXX:
    participants: 2-10
    requires: fluxx_deck
    duration: variable
    effects:
      - fun_satisfaction
      - social_bonds
      - possible: creative_chaos
```

The [33-turn Stoner Fluxx game](../examples/adventure-4/sessions/don-session-1.md#turn-17-stoner-fluxx-marathon) shows group activities in action.

---

## Social Interactions

**Sims:** A taxonomy of social actions:

| Category | Actions |
|----------|---------|
| Friendly | Chat, joke, compliment, hug |
| Mean | Insult, mock, fight |
| Romantic | Flirt, kiss, propose |
| Special | Tickle, scare, dance |

Each had:
- **Requirements** (relationship level, traits)
- **Effects** (relationship change, mood buffs)
- **Failure modes** (rejection, embarrassment)

**MOOLLM:** Social skill methods:

```yaml
# skills/social/CARD.yml
interactions:
  GREET:
    requirements: none
    success_effect: +small relationship
    failure: unlikely
    
  JOKE:
    requirements: social_skill >= 2
    success_effect: +fun both, +friendship
    failure_effect: embarrassment_buff
    
  FLIRT:
    requirements: romantic_interest
    success_effect: +romance
    failure_effect: -relationship, embarrassment
    
  DEEP-CONVERSATION:
    requirements: friendship >= "warm"
    success_effect: +deep_bond
    topics: [vulnerabilities, dreams, fears]
```

---

## Non-Player Characters

**Sims:** NPCs served specific roles:

| NPC | Role | Behavior |
|-----|------|----------|
| Mail carrier | Delivers bills | Comes daily, brief visit |
| Pizza delivery | Brings food | On-call, leaves after delivery |
| Burglar | Steals stuff | Night visits, crime |
| Grim Reaper | Claims the dead | Appears at death |
| Social bunny | Lonely Sim's hallucination | Extreme social failure |

**MOOLLM:** NPCs as simplified characters:

```yaml
# characters/npcs/mail-carrier/CHARACTER.yml
type: npc
role: mail_carrier

schedule:
  visits: daily, morning
  duration: brief
  
interactions:
  available: [greet, tip, chat_briefly]
  unavailable: [long_conversation, dinner_invite]
  
behaviors:
  - deliver_mail
  - respond_to_greeting
  - depart
```

Or stored in the [guest book](../examples/adventure-4/pub/guest-book.yml) for lightweight persistence.

---

## Social Buffs

**Sims:** Social interactions created temporary states:

| Buff | Duration | Effect |
|------|----------|--------|
| Flattered | 3 hours | +5 mood |
| Embarrassed | 2 hours | -10 mood, -social success |
| In Love | 24 hours | +20 mood, romantic actions easier |
| Heartbroken | 48 hours | -30 mood, social actions harder |

**MOOLLM:** Buffs as modifiers:

```yaml
# characters/palm/active_buffs.yml
buffs:
  - id: creative_surge
    source: successful_writing
    duration: 4_hours
    effects:
      creativity: +20%
      
  - id: socially_satisfied
    source: good_conversation
    duration: 6_hours
    effects:
      social_need_decay: slower
```

See [skills/buff/](../skills/buff/).

---

## Visitors & Neighbors

**Sims:** The neighborhood had:
- **Playable families** — you could switch to them
- **NPC neighbors** — visit but can't control
- **Visitors** — come to your lot

Visitors could become friends, move in, even marry in.

**MOOLLM:** The [guest book](../examples/adventure-4/pub/guest-book.yml) pattern:

```yaml
guests:
  andy-looney:
    type: legendary_visitor
    visits: [2026-01-04]
    standing_invitation: true
    notes: "Creator of Fluxx, mad scientist energy"
    
  casual-visitor:
    type: drop_in
    visits: [2026-01-08]
    notes: "Enjoyed the Diesel strains"
```

Lightweight persistence for social connections.

---

## The Social Need

**Sims:** Social was a core motive:

```
social_need:
  decay_rate: 3/hour
  satisfied_by: [conversation, group_activity, phone_call]
  low_effects: [sadness, social_bunny_hallucination]
```

Sims literally went crazy if isolated too long.

**MOOLLM:** Social as need:

```yaml
# skills/needs/SKILL.md
social:
  description: "Connection with others"
  decay: gradual
  
  satisfied_by:
    - meaningful conversation
    - shared activities
    - physical affection
    - acknowledgment
    
  when_low:
    - loneliness buffs
    - seeking behavior
    - reduced other satisfactions
```

---

## Family Ties

**Sims:** Family relationships were special:

| Relation | Bond Type | Effects |
|----------|-----------|---------|
| Spouse | Romantic + Familiar | Can share bed, special actions |
| Child | Parent-child | Care obligations, teaching |
| Sibling | Familiar | Play together, rivalry |
| Cousin | Extended | Weaker bonds, less obligation |

**MOOLLM:** Family as relationship type:

```yaml
relationships:
  kristin:
    bond: spouse
    family_type: partner
    shared: [home, finances, decisions]
    
  maya:
    bond: child
    family_type: daughter
    responsibilities: [care, education, support]
    
  don-hopkins:
    bond: godfamily
    family_type: godfather
    notes: "Chosen family, not biological"
```

The [godfamily](../examples/adventure-4/sessions/don-session-1.md#the-godfamily) concept extends family beyond blood.

---

## The Social Hierarchy

**Sims:** Social interactions had prerequisites:

```
Hug       requires: friendship >= 50
Kiss      requires: romance >= 30
Propose   requires: romance >= 80, relationship_days >= 7
Move In   requires: romance >= 90, household_space
```

You couldn't jump to intimacy — you had to build.

**MOOLLM:** Relationship gating:

```yaml
# skills/social/CARD.yml
interaction_gates:
  casual:
    requirements: none
    actions: [greet, chat, wave]
    
  friendly:
    requirements: {friendship: warm}
    actions: [hug, share_meal, give_gift]
    
  intimate:
    requirements: {friendship: deep, trust: established}
    actions: [confide, collaborate, defend]
```

Natural progression, not forced intimacy.

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — Full architecture
- [skills/social/](../skills/social/) — Social interaction skill
- [skills/party/](../skills/party/) — Group activities
- [skills/buff/](../skills/buff/) — Social buffs
- [guest-book.yml](../examples/adventure-4/pub/guest-book.yml) — Visitor persistence
- [don-session-1.md](../examples/adventure-4/sessions/don-session-1.md) — Social dynamics in action

---

*"Relationship Matrix... Conversation Topics Thought Balloons Dreaming Group Activities Jealousy Privacy"*

Society emerges from the sum of relationships. MOOLLM models the sum.
