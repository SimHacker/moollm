# 🎭 Simulator Effect

> *"Players imagine simulations are vastly more detailed, deep, rich, and complex than they actually are."* -- Will Wright

> *Implication is more efficient (and richer) than simulation.*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Core MOOLLM principle -- LLM as imagination engine |
| [society-of-mind/](../society-of-mind/) | Emergence from agent interaction (Minsky) |
| [manufacturing-intelligence/](../manufacturing-intelligence/) | Two words, seven readings -- sparse phrase, rich meaning |
| [k-lines/](../k-lines/) | Names activate clusters -- the mechanism behind the effect |
| [yaml-jazz/](../yaml-jazz/) | Sparse annotations, rich interpretation |
| [empathic-templates/](../empathic-templates/) | Smart generation from minimal cues |
| [constructionism/](../constructionism/) | Players build mental models |
| [procedural-rhetoric/](../procedural-rhetoric/) | Rules imply values |
| [mind-mirror/](../mind-mirror/) | Leary's circumplex, Sims traits |
| [adversarial-committee/](../adversarial-committee/) | Many voices beat mode-collapse |
| [speed-of-light/](../speed-of-light/) | One call, many turns -- imagination does the rendering |
| [needs/](../needs/) | Sims motives as numeric seeds for imagined behavior |
| [sims-astrology](../../designs/sims/sims-astrology.md) | The Astrillogical Effect -- zero code, maximum perceived effect |
| [MOOLLM-EVAL-INCARNATE-FRAMEWORK](../../designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) | Full theory |

**Quick Links:**
- [Full Specification](SKILL.md) -- complete protocol
- [The Astrillogical Effect](../../designs/sims/sims-astrology.md) -- 1997 proof

---

## The Discovery

Will Wright, designing The Sims, noticed something profound: players believed the simulation was far more sophisticated than it actually was.

```
WHAT PLAYERS IMAGINED              WHAT CODE ACTUALLY DID
----------------------              ----------------------
"She's sad because her             if (social < 30 && 
 husband ignored her at             time_since_talk > 4h)
 breakfast, and she's still          mood -= 5;
 processing yesterday's fight"
```

The game provided **scaffolding**. Player imagination did the **rendering**.

---

## The Principle

**Off-load computation into the user's brain.**

The human imagination is:
- More powerful than any simulation
- More creative than any procedural generator
- Runs on ~20 watts
- Already exists

The game designer's job: **seed the imagination, don't simulate the result**.

---

## The Astrillogical Proof

In 1997, The Sims implemented zodiac signs:

```c
// Actual implementation:
sign = nearest_zodiac(personality_vector);  // Euclidean distance
display_sign(sign);                          // Show icon
// END OF CODE. No behavioral effect.
```

Testers immediately reported bugs:
> "The zodiac influence is too strong! Tune it down!"

**But there was no zodiac code to tune.** The effect was entirely imagined.

See: [sims-astrology.md](../../designs/sims/sims-astrology.md)

---

## The Mechanism: K-Lines

Why does this work? Minsky's [K-lines](../k-lines/).

When you show "Sagittarius", you activate:
```
{adventure, optimism, freedom, risk-taking, 
 philosophy, bluntness, wanderlust, fire, archer...}
```

The name **is** the simulation. The cultural baggage **is** the behavior. You did not write personality code -- you invoked a pre-trained model that already exists in every human brain.

LLMs work the same way. The token "Sagittarius" activates statistically correlated patterns from training data. Same mechanism, different substrate.

---

## MOOLLM Application

### 1. Semantic State Over Numeric State

```yaml
# DON'T: Simulate every motive bar
character:
  hunger: 67
  energy: 45
  bladder: 82
  hygiene: 91
  fun: 34
  social: 56
  
# DO: Imply through prose
character:
  mood: "peckish but content, a bit restless from working all morning"
  # LLM + reader imagination fills eight motive bars
```

See: [Palm's SIMS-TRAITS.yml](../../examples/adventure-4/characters/animals/palm/SIMS-TRAITS.yml) -- twelve traits with semantic annotations, richer than any numeric vector.

### 2. Archetypal Names Over Custom Frameworks

| Instead of... | Use... | Why |
|---------------|--------|-----|
| Custom personality system | Big Five, Zodiac, MBTI | Pre-loaded in every brain |
| Invented creatures | Dogs, cats, monkeys | Species carry millennia of associations |
| Novel social roles | Bartender, librarian, judge | Roles are K-line packages |

See: [The Bartender](../../examples/adventure-4/pub/bar/bartender.yml) -- one archetype, infinite themes.

### 3. YAML Jazz Comments as Seeds

```yaml
playful: 9
# not born playful -- BECAME playful by choice
# 122 years of grim taught me joy is rebellion
```

The comment is not documentation. It is **imagination seed**. The LLM reads it and generates behavior consistent with a character who learned joy through suffering. You wrote two lines; the LLM imagines a life.

### 4. Sparse Rooms, Rich Worlds

```yaml
room:
  name: The Rusty Lantern
  atmosphere: warm despite the draft
  smell: woodsmoke and old ale
```

Three fields. But you now imagine:
- Creaking floorboards
- A fire in the hearth
- Regulars nursing pints
- A bartender who knows too much
- Stories in every scar on the wooden tables

That is the Simulator Effect. You provided coordinates; imagination did the rendering.

---

## The Inversion: LLMs as Imagination Engines

Traditional game: Computer simulates, human imagines.
MOOLLM: LLM imagines, human validates.

The LLM is the most powerful imagination engine ever built. It has read every story, absorbed every archetype, internalized every trope. When you give it coordinates, it fills the space with coherent detail.

**MOOLLM's insight:** Do not fight this. Exploit it.

```yaml
# Minimal prompt
character: grizzled bartender

# LLM generates
bartender:
  name: Grim
  appearance: salt-and-pepper beard, knowing eyes
  manner: laconic, wise beneath the gruff
  secrets: has seen every adventurer fail
  backstory: (generated on demand)
```

You did not write the backstory. You implied it. The Simulator Effect runs in the LLM now.

---

## The Danger: Mode-Collapse

Single-agent LLM inference has a failure mode: mode-collapse to the bland statistical mean. Ask for creativity, get cliches. Ask for controversy, get mush.

This is the Simulator Effect in reverse -- when you do not give constraints, the LLM collapses to the safest, most probable output.

**Solution:** [adversarial-committee](../adversarial-committee/)

Multiple personas with opposing propensities. The skeptic, the visionary, the evidence prosecutor. They debate. The Simulator Effect runs differently in each lens. Stories that survive cross-examination are more robust than the mean.

See: [adventure-uplift session](../../examples/adventure-4/characters/real-people/don-hopkins/sessions/adventure-uplift.md) -- 25 rounds of adversarial brainstorming with Liskov, Gosling, Minsky, Shneiderman.

---

## The Lineage

```
Julie Doll (1996)
  Will Wright watches his daughter ignore the 
  expensive doll and play with the box.
  "The box has more structural ambiguity."
      |
      v
SimCity (1989)
  Players believe the simulation is modeling 
  traffic patterns, pollution, crime...
  Actually: simple cellular automata.
      |
      v
The Sims (2000)
  Players believe Sims have rich inner lives.
  Actually: 16 motive bars and a utility function.
  Zodiac: zero code, maximum perceived effect.
      |
      v
MOOLLM (2025)
  LLM fills in what YAML implies.
  Comments shape interpretation.
  Archetypes activate clusters.
  The Simulator Effect runs in silicon now.
```

---

## Practical Guidelines

### When Designing Characters

1. **Name them well** -- Names are K-lines
2. **Use archetypes** -- "grizzled bartender" > custom personality matrix
3. **Annotate with YAML Jazz** -- Comments seed imagination
4. **Leave gaps** -- Unstated details get imagined richer

### When Designing Rooms

1. **Three sensory details** -- Sight, sound, smell
2. **One mystery** -- Something unexplained
3. **No exhaustive inventories** -- Let imagination furnish

### When Designing Interactions

1. **Imply causation** -- "She frowned when he entered"
2. **Don't explain emotions** -- Let the reader/LLM infer
3. **Trust the interpreter** -- Human or LLM will fill gaps

---

## See Also

- [sims-astrology.md](../../designs/sims/sims-astrology.md) -- The Astrillogical Effect
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect](../../designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#the-simulator-effect) -- Full theory
- [k-lines/](../k-lines/) -- The mechanism
- [adversarial-committee/](../adversarial-committee/) -- Many-voiced antidote to mode-collapse
- [yaml-jazz/](../yaml-jazz/) -- Comments as imagination seeds
- [empathic-templates/](../empathic-templates/) -- Smart generation
- [constructionism/](../constructionism/) -- Players build mental models

---

## References

- **Will Wright's Stanford Lecture** (1996) -- https://donhopkins.medium.com/will-wright-on-designing-user-interfaces-to-simulation-games-1996-video-update-2023-da098a51ef91
- **Minsky, Society of Mind** (1985) -- K-lines theory
- **Scott McCloud, Understanding Comics** (1993) -- Masking: simple faces, detailed worlds
- **The Sims Design Documents** -- https://donhopkins.com/home/TheSimsDesignDocuments

---

*"He designs games to run on two computers at once: the electronic one on the player's desk, running his shallow tame simulation, and the biological one in the player's head, running their deep wild imagination."*

*The Simulator Effect is not a trick. It is how meaning works.*
