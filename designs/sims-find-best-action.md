# Find Best Action Primitive → MOOLLM

> *Jamie Doornbos, October 1997*
> *The algorithm that gives Sims autonomy*

## The Core Problem

How does a Sim decide what to do next? Not scripted. Not random. *Motivated.*

The Find Best Action primitive solves this by:
1. Looking at every available interaction in the world
2. Scoring each by how much it improves the Sim's happiness
3. Picking the best one

This is the beating heart of Sims autonomy — and it maps directly to MOOLLM's [action-queue](../skills/action-queue/) system.

---

## Advertisements

> "Each interaction has a set of advertisement values, one value for each motive. The advertisements are supposed to roughly indicate how much the motive can increase if that interaction is run."

Every object *advertises* what it offers:

| Object | Interaction | Hunger | Energy | Fun | Social |
|--------|-------------|--------|--------|-----|--------|
| Fridge | Eat | +50 | 0 | 0 | 0 |
| Bed | Sleep | 0 | +80 | 0 | 0 |
| TV | Watch | 0 | -5 | +30 | 0 |
| Phone | Call Friend | 0 | 0 | +10 | +40 |

**MOOLLM equivalent:** [CARD.yml](../skills/card/) advertised methods.

```yaml
# skills/bartender/CARD.yml
advertised_methods:
  SERVE-DRINK:
    satisfies: [thirst, social]
    description: "Pour a drink and chat"
  
  RECOMMEND-STRAIN:
    satisfies: [comfort, curiosity]
    description: "Suggest something good"
```

Objects and skills *broadcast* what they can do for you. The action-queue collects these broadcasts and prioritizes.

---

## Check Trees

> "The purpose of the check tree is two-fold. One purpose is to determine if the interaction is available for that particular person. The other purpose is to modify the motive advertisements to reflect how much the interaction can affect the particular person considering it."

Not everyone can use every interaction:
- Can't "place on table" if you're not holding anything
- Can't "eat" if there's no food
- Can't "call friend" if you have no friends

**And:** the *same* interaction has different value for different Sims based on personality and relationships.

**MOOLLM equivalent:** Preconditions in skill methods + LLM evaluation.

```yaml
# skills/budtender/CARD.yml
advertised_methods:
  SERVE-BUD:
    preconditions:
      - customer.age >= 21
      - customer.location == "pub/bar"
      - inventory.has_strain(requested)
    modifiers:
      - if customer.is_regular: satisfaction += 20
      - if customer.knows_marieke: satisfaction += 10
```

The LLM evaluates preconditions *and* modifies scores based on relationships and context. Check trees, but semantic.

---

## Contribution Functions

> "A simple measure of happiness might be the average of all a person's motives. 'Find Best Action' takes this basic approach, but also uses a 'cutoff point' for each motive above which additional motive value contributes nothing."

Key insight: **diminishing returns**.

If your Hunger is already at 90%, eating gives you almost nothing. The algorithm only counts motive improvement *up to the cutoff*.

```
Contribution = min(motive_value, cutoff) 
```

Different motives have different cutoffs:
- **Stress cutoff at 0** — because the simulation pushes stress toward zero
- **Fun cutoff higher** — you can never have too much fun (almost)

**MOOLLM equivalent:** The [needs](../skills/needs/) skill models this:

```yaml
# characters/palm/NEEDS.yml (conceptual)
needs:
  hunger:
    current: 75
    decay_rate: 2/hour
    satisfaction_curve: logarithmic  # diminishing returns
    
  social:
    current: 40
    decay_rate: 1/hour
    cutoff: 80  # above this, social actions worth less
```

The LLM understands "Palm is already well-fed, he'd rather play than eat."

---

## Scoring: The Delta

> "The overall score of a given interaction is obtained by scoring the person twice: once with their current motive values as they are, and again with their current motive values augmented by the motive advertisements. The former is subtracted from the latter."

**Score = Happiness(after) - Happiness(before)**

An interaction that *could* give +50 Hunger is worthless if Hunger is already full. The delta is what matters.

**MOOLLM equivalent:** The LLM naturally does this. When evaluating what Palm should do next, it considers:
- What does Palm need most right now?
- What's available?
- What would improve his state the most?

This isn't coded — it's *understood*.

---

## Attenuation: Distance Matters

> "Once the overall score of an interaction is known, the distance from the person to the object is used to dampen the score."

```
attenuated_score = score / (attenuation * distance + 1)
```

A bed across the house is worth less than a bed nearby — because you have to walk there first.

**MOOLLM equivalent:** Room structure and location paths.

```yaml
# Palm in pub/stage/palm-nook/study/
# Considering:
#   - Sleep in rest/ (1 room away) → high score
#   - Sleep in maze/deep-room/ (10 rooms away) → low score
```

The LLM weighs "how far do I have to go" against "how good is it when I get there."

---

## Object Culling

Before scoring, objects are filtered:

| Condition | Meaning |
|-----------|---------|
| **Occupied flag** | Someone else is using it |
| **Non-zero use count** | Recently used, cooling down |
| **No tree table** | Not interactive |
| **Not the self** | Can't interact with yourself (TBD: reflexive) |

**MOOLLM equivalent:** The LLM naturally filters:
- "The bartender is busy with another customer"
- "The gong was just rung, let it resonate"
- "That's just a decoration, not interactable"

Context-aware filtering without explicit flags.

---

## The Sorted List

After scoring everything:

```cpp
// 1997 C++ implementation
qsort(vector.begin(), vector.end(), compare_scores);
return vector[0];  // best action
```

The best action rises to the top. The Sim does it.

**MOOLLM equivalent:** The action-queue skill maintains a priority queue of pending actions. The LLM evaluates and reorders based on:
- Urgency (needs decay)
- Opportunity (what's nearby)
- Personality (what this character prefers)
- Interrupts (crises override routine)

---

## The Brilliance

This algorithm solved a hard problem elegantly:

1. **Emergent behavior** — Sims seem alive because they're *actually motivated*
2. **Tunable** — Adjust advertisements, cutoffs, attenuation and behavior changes
3. **Scalable** — Works with any number of objects and interactions
4. **Personality-aware** — Check trees customize scores per-Sim

The Sims don't have scripts. They have *wants*.

---

## MOOLLM's Evolution

MOOLLM takes this further:

| Sims 1997 | MOOLLM 2026 |
|-----------|-------------|
| Numeric motive values | Semantic need descriptions |
| Hardcoded contribution curves | LLM understands diminishing returns |
| Check trees (SimAntics code) | Natural language preconditions |
| Static advertisements | Dynamic CARD.yml methods |
| qsort on scores | LLM reasoning about priorities |
| Distance attenuation | Room structure + location paths |

The *architecture* is the same. The *implementation* is language instead of code.

---

## TBDs That Became Features

The document notes several "TBD" items:

> "TBD: interactions may also need to be culled by previous failure"

This became the frustration system — Sims remember failed attempts.

> "TBD: reflexive interactions will probably be a part of game play"

This became self-care actions — meditation, mirror pep-talks, self-soothing.

> "TBD: cutoff values are probably part of a person's personality"

This became personality traits affecting need curves — a Lazy Sim has higher energy cutoff, a Social Sim has lower social cutoff.

---

## See Also

- [sims-happy-friends-home.md](./sims-happy-friends-home.md) — The 1996 design that needed this algorithm
- [sims-maxis-requirements.md](./sims-maxis-requirements.md) — The seven requirements this enables
- [skills/action-queue/](../skills/action-queue/) — MOOLLM's equivalent
- [skills/needs/](../skills/needs/) — Motive simulation
- [skills/card/](../skills/card/) — Advertisement interface
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md#simcity-the-sims-and-the-simulator-effect) — Full Sims influence

---

*"An interaction that provides for only one motive will have an overall score of zero if that motive is already over the cutoff point."*

Satisfaction has a ceiling. Desire has a floor. The gap between them is motivation.
