# Legible Social Dynamics

> "The rules were always there. We're just making them readable."

*Yes, the acronym is LSD. Yes, we noticed. Yes, it expands perception.* 🌀

*LSD (the substance) is famous for expanded self-perception — seeing yourself and the world from outside your usual frame. LSD (this document) offers something similar: seeing your social patterns from outside, through YAML Jazz and LLM simulation, instead of chemistry. Same destination, different vehicle.*

## The Observation

While building social simulation experiments — poker games with internal monologues, smoking protocols with memory requirements, observable signatures for emotional states — we noticed something:

**We were writing down what most people "just know."**

```yaml
# What becomes visible when you model it:

social_protocol:
  offer_before_assuming: true     # the offer itself is a social probe
  remember_declines: true         # repeated offering = pressure
  sharing_creates_bonds: true     # who shares with whom = political info
  abstaining_is_information: true # observers will interpret (maybe wrong)
```

**Double-barrel meaning:**
- The **key** states the rule → `offer_before_assuming`
- The **comment** reveals the insight → `# the offer itself is a social probe`

Both fire together. The rule tells you *what*. The comment tells you *why it matters*.

This isn't new knowledge. It's *named* knowledge. Knowledge that was always operating, now made legible.

## Who Benefits from Legibility?

Everyone, actually. But especially:

| Person | Why Legibility Helps |
|--------|---------------------|
| **Autistic people** | May learn social rules through understanding rather than absorption |
| **Immigrants** | Navigating unfamiliar cultural protocols |
| **Introverts** | Analyzing social energy expenditure |
| **Anxious people** | Understanding "what just happened" after interactions |
| **Children** | Learning social rules for the first time |
| **Therapists** | Making patterns visible to clients |
| **Writers** | Creating believable character interactions |
| **AI researchers** | Teaching machines what humans take for granted |
| **Anyone** | Who's ever felt lost in a social situation |

The insight: **legibility isn't a special accommodation — it's a different cognitive style that serves many purposes.**

## What We Mean by "Legible"

Legible social dynamics have:

### Named Patterns

Instead of "you know, that *thing* people do," we have:

```yaml
behavioral_constraint:
  name: "liberation_bond"
  type: "cannot"
  description: "Palm cannot bluff Don — loyalty runs too deep"
  observable: "Deference and protection visible to others"
```

The pattern has a name. It can be discussed, modified, recognized elsewhere.

### Visible Rules

Instead of "everyone knows you don't do that," we have:

```yaml
social_protocol:
  remember_declines: |
    If someone declines, REMEMBER. 
    Don't offer again that session unless they ask.
    Repeated offering after decline = pressure.
```

The rule is written. It can be learned, questioned, adapted to context.

This answers Alan Kay's criticism of SimCity: players couldn't see or modify the underlying models — they could only play within invisible rules. Here, the rules are visible. And editable. The highest level of understanding isn't just "there are rules" — it's **"there are rules, and I can make them."**

### Observable Signatures

Instead of "I could just *tell* she was nervous," we have:

```yaml
observable_signatures:
  nervous:
    face: "Wide eyes, frequent blinking"
    body: "Trembling, hunched shoulders"
    voice: "Stammering, apologetic"
    timing: "Long pauses, second-guessing"
```

The tells are catalogued. They can be recognized, practiced, discussed.

But here's the craft: **the simulator can't ONLY broadcast tells.** Tells must be embedded in background narrative — color, events, distractions, normal behavior. Otherwise the tells are obvious, mechanical, the only thing happening.

```yaml
# BAD: Tell is the only signal
observable:
  body: "Trembling hands"  # TOO OBVIOUS

# GOOD: Tell embedded in narrative
observable:
  body: |
    Reaches for the bitterballen, knocks the bowl slightly.
    Pulls hand back. Straightens napkin. Checks phone briefly.
    Hands resting on table now — slight tremor visible.
```

Real tells exist in a sea of other signals. The simulation must create that sea. Readers learn to *find* the tells, not just *receive* them.

### The Narrative Stream

The simulator broadcasts **all channels** as YAML Jazz:

```yaml
narrative_stream:
  game: "Flop comes K♠ 8♦ 5♣. Pot is 450 🪙."
  logistics: "Marieke brings another round. Ice clinks."
  spoken: "Don: 'Interesting board.'"
  body: "Palm's tail curls slightly tighter."
  face: "Donna's left eyebrow twitches — or was that the candle flicker?"
  environment: "Leigh's lighter flares. Brief orange glow on faces."
  sound: "Chips shuffling. Klaus humming something. Is that The Cold Song?"
  smell: "Palm's Lucky Blend drifts across the table. Bumblewick's anxiety-sweat."
```

**A tell can be ANY channel:**
- 👃 Smell: Bumblewick sweats when terrified
- 👂 Sound: Klaus hums when content
- 🕯️ Timing: Donna's pause before raising
- 🍺 Object: Don refills drink when bluffing
- 💨 Smoke: Palm's exhale direction tracks attention

The simulation streams *everything*. Tells hide in plain sight.

### Memory Requirements

Instead of "you should have remembered," we have:

```yaml
memory_requirements:
  track:
    - offers_made: "who offered what to whom"
    - responses: "accepted, declined, ignored"
    - declines_remembered: "don't re-offer"
```

The memory burden is explicit. Systems can help track it.

## Social Simulation as Learning Space

Our experiment framework creates a **safe sandbox** for exploring social dynamics:

```
┌─────────────────────────────────────────────────────────────────┐
│  THE SANDBOX                                                    │
│                                                                 │
│  - Fictional characters (low stakes)                            │
│  - Bounded context (poker game, not all of life)                │
│  - Explicit rules (protocols, constraints)                      │
│  - Observable consequences (state changes, relationship shifts) │
│  - Replayable (try different choices)                           │
│  - Analyzable (cursor-mirror for meta-cognition)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

You can:
- **Watch** characters navigate social situations
- **See** their internal monologues alongside external behavior
- **Notice** how relationships color interpretation
- **Observe** how protocols create or release social tension
- **Experiment** with different character configurations
- **Compare** outcomes across runs

All without real social risk.

## The Layers Make It Learnable

Our layered simulation model separates what's usually tangled:

```
INTERNAL LAYER     →  What they actually think
                      (hidden from other characters)

EXTERNAL LAYER     →  What they show
                      (face, body, voice, timing)

OBSERVATION LAYER  →  What others perceive
                      (interpretation, possibly wrong)

RELATIONSHIP LAYER →  History coloring interpretation
                      (bonds, grudges, debts)
```

In real life, these layers blur together. In simulation, they're distinct and visible. You can study each one.

## Learning Patterns, Not Scripts

Important distinction:

| Scripts (limiting) | Patterns (liberating) |
|-------------------|----------------------|
| "Say this exact thing" | "Offering creates a social probe" |
| "Act normal" | "Declining politely preserves relationship" |
| "Just be yourself" | "Your observable: may differ from your thinking:" |

Patterns give you **vocabulary and structure** without prescribing specific behaviors. You learn *why* social dynamics work, not just *what* to do.

## The Ethics of Legibility

Some considerations:

### Legibility ≠ Manipulation

Making social rules visible doesn't mean using them to manipulate. It means:
- Understanding why you feel uncomfortable
- Recognizing patterns you couldn't name
- Having language for discussing social dynamics
- Making conscious choices about participation

### Legibility ≠ Masking

This isn't about teaching people to "pass" as neurotypical. It's about:
- Understanding the game even if you choose not to play
- Knowing when rules are arbitrary vs. meaningful
- Having tools to navigate required interactions
- Finding your own authentic participation style

### Legibility Benefits Everyone

When social rules are visible:
- Neurotypical people see their own assumptions laid bare
- Cultural differences become discussable
- Power dynamics become visible
- "Common sense" reveals itself as learned, not innate

## The Poker Experiment as Prototype

Our "Emotional Poker Face" experiment demonstrates legible social dynamics:

- **6 explicit layers** of simulation
- **Social protocols** for smoking (offer, accept, decline, remember)
- **Observable signatures** per character (tells that persist)
- **Behavioral constraints** from relationships (Palm cannot bluff Don)
- **Memory requirements** (track who declined what)
- **Failure mode detection** (layer bleed = mind reading)

It's a bounded world where social complexity emerges from explicit rules.

## Building More Legible Worlds

This approach could extend to:

### Social Situation Libraries

```yaml
situations:
  small_talk:
    purpose: "Establish connection, assess availability"
    patterns: [turn_taking, topic_surfing, exit_signals]
    common_errors: [monologuing, interrogating, abrupt_exit]
    
  receiving_compliment:
    purpose: "Accept positive social offering"
    patterns: [acknowledgment, deflection, reciprocation]
    common_errors: [rejection, over_explanation, fishing_for_more]
```

### Protocol Templates

```yaml
# Any offer/accept/decline situation:
template: social_protocol
instances:
  - smoking
  - drinks
  - food
  - compliments
  - help
  - secrets
  - invitations
```

### Relationship Dynamics

```yaml
dynamics:
  mentor_student:
    constraints: [student_defers, mentor_teaches]
    evolution: [graduation, reversal, collegiality]
    
  new_acquaintance:
    protocols: [small_talk, boundary_testing, disclosure_matching]
    transitions: [to_friend, to_colleague, to_stranger]
```

## An Invitation

If you've ever:
- Studied social interactions like a foreign language
- Felt relieved when someone explained an unwritten rule
- Wished people would just *say what they mean*
- Built mental models of how conversations work
- Noticed patterns others seem to navigate unconsciously

...you might find value in legible social dynamics.

Not as a replacement for intuition, but as a complement. Not as rules to follow, but as patterns to recognize. Not as scripts, but as vocabulary.

The rules were always there. Now they're readable.

---

## LSD Leverages YAML Jazz

The patterns we build use **YAML Jazz** — where comments aren't just documentation, they're semantic data:

```yaml
# THE LIBERATION BOND
# Palm was trapped for 122 years. Don freed them.
# This creates UNBREAKABLE loyalty.

don_hopkins_palm:
  type: "liberator-freed"
  bond_strength: 10
  
  # The constraint that matters:
  poker_constraint: "Palm CANNOT bluff Don. Loyalty runs too deep."
  
  # What observers see:
  observable_dynamic: "Palm defers subtly. Don watches protectively."
```

The comments carry meaning. An LLM reads them. A human reads them. The structure is data AND documentation simultaneously.

This is how legibility works in practice:
- **YAML** provides structure (machine-readable)
- **Comments** provide context (human-readable)  
- **Both together** create legible social dynamics

The expanded perception comes from seeing both layers at once.

---

## Related Work

- **Patterns** in `skills/experiment/patterns/`
  - `social-protocol.yml` — offer/accept/decline dynamics
  - `observable-signatures.yml` — consistent behavioral tells
  - `behavioral-constraints.yml` — relationship-based rules
  
- **Experiments** in `skills/experiment/experiments/`
  - `emo-poker-face/` — multi-layer character simulation

- **Skills**
  - `yaml-jazz` — comments as semantic data

- **Concepts**
  - [Will Wright's microworlds](https://donhopkins.com/home/TheSimsDesignDocuments/) — learning through simulation
  - [Stanford Generative Agents](https://arxiv.org/abs/2304.03442) — believable social behavior
  - Theory of Mind — modeling others' mental states
  - Social Stories™ — explicit social narratives (Carol Gray)

---

*This document emerged from building social simulation experiments and noticing: we were making the implicit explicit. That turned out to be valuable for everyone.*
