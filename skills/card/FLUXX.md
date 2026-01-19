# Fluxx Cards: Rules That Change Rules

Inspired by [Fluxx](https://en.wikipedia.org/wiki/Fluxx), some cards **modify the game itself**.

## Basic Fluxx Card

```yaml
# fluxx/double-time.card
card:
  name: "Double Time"
  type: fluxx
  
  on_play:
    modify: room.rules
    changes:
      ticks_per_turn: 2
      
  description: "All actions happen twice per turn"
  
  advertisements:
    DISPEL:
      description: "Remove this rule change"
      score_if: "has_dispel_ability"
```

## Rule Modification Examples

```yaml
# fluxx/chaos-mode.card
on_play:
  modify: room.rules
  changes:
    action_order: random
    advertisement_scoring: inverted

# fluxx/silence.card  
on_play:
  modify: room.rules
  changes:
    allowed_actions: [LOOK, MOVE]

# fluxx/abundance.card
on_play:
  modify: room.rules
  changes:
    inventory_limit: unlimited
    dispenser_cooldown: 0

# fluxx/hardcore.card
on_play:
  modify: room.rules  
  changes:
    permadeath: true
    save_disabled: true
```

## Stacking and Interaction

Multiple Fluxx cards stack:

```yaml
room:
  active_fluxx:
    - double-time.card
    - chaos-mode.card
    - abundance.card
    
  effective_rules:
    ticks_per_turn: 2
    action_order: random
    inventory_limit: unlimited
```

## Meta-Fluxx: Rules About Rules

```yaml
# fluxx/immutable.card
card:
  name: "Immutable"
  type: meta-fluxx
  
  on_play:
    modify: room.meta_rules
    changes:
      fluxx_cards_allowed: false
      
  protected: true
  cannot_be_dispelled: true
```

Fluxx cards make MOOLLM a **self-modifying game**.

---

*See [SKILL.md](./SKILL.md) for core protocol.*
