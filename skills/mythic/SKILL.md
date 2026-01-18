# Mythic — Protocol Specification

> The old stories still have power.

## Applies To

Anything from mythology, folklore, or religion:

| Entity Type | Examples |
|-------------|----------|
| **Gods** | Zeus, Thor, Shiva, Odin |
| **Spirits** | Kami, djinn, faeries |
| **Creatures** | Dragons, phoenix, unicorns |
| **Heroes** | Hercules, King Arthur, Gilgamesh |
| **Places** | Olympus, Asgard, Avalon |
| **Objects** | Mjolnir, Excalibur, Holy Grail |

## Ethics Protocol: MYTHIC

Cultural sensitivity required.

```yaml
ethics:
  core:
    - Cultural sensitivity required
    - Acknowledge source tradition
    - Respect sacred contexts
    - Some are still worshipped — extra care
    
  awareness:
    - Living people hold these beings sacred
    - Context matters (educational vs mockery)
    - Power dynamics of cultural appropriation
    - Distinguish mythology from active religion
```

## Simulation Effects

### On Characters

```yaml
mythic_character:
  source:
    - Which tradition?
    - Still actively worshipped?
    - Cultural significance?
  portrayal:
    - Respectful of source
    - Can adapt creatively
    - Avoid mockery
  powers:
    - True to mythic role
    - Larger than human
    - Symbolic significance
```

### On Places

```yaml
mythic_place:
  nature:
    - Otherworldly
    - Follows mythic rules
    - May be unreachable normally
  atmosphere:
    - Numinous
    - Outside normal reality
    - Sacred or terrifying
```

### On Objects

```yaml
mythic_object:
  properties:
    - Legendary powers
    - Symbolic significance
    - Often unique
  behavior:
    - May have will
    - May choose wielder
    - Follows mythic logic
```

### On Creatures

```yaml
mythic_creature:
  nature:
    - Legendary, not biological
    - Symbolic meaning
    - Often magical
  examples:
    dragon:
      symbolic: "Greed, power, ancient wisdom"
      cultural: "Varies by tradition (Western vs Eastern)"
    phoenix:
      symbolic: "Rebirth, immortality"
    unicorn:
      symbolic: "Purity, magic"
```

## Sensitivity Levels

```yaml
sensitivity:
  
  high:
    description: "Still actively worshipped"
    examples: [Jesus, Allah, Shiva, Ganesha]
    care: "Maximum respect, avoid mockery"
    context: "Educational or sincere only"
    
  medium:
    description: "Cultural heritage, not active worship"
    examples: [Zeus, Odin, Hercules]
    care: "Respectful adaptation allowed"
    context: "Can be playful but not disrespectful"
    
  lower:
    description: "Creatures without worship"
    examples: [dragons, unicorns, phoenix]
    care: "Generally free to adapt"
    context: "Creative freedom with cultural awareness"
```

## World Integration

When a mythic entity enters the simulation:

```yaml
simulation_entry:
  1_source: "Which tradition?"
  2_sensitivity: "Still sacred to anyone?"
  3_role: "Why invoking this being?"
  4_declare: "Mark as [mythic] tagged"
  
ongoing:
  - Respect source tradition
  - Be aware of cultural context
  - Educational framing when appropriate
```

## Combination Rules

```yaml
combinations:
  mythic + animal:
    result: "Dragon, phoenix, unicorn"
    ethics: "Cultural respect + creature behavior"
    
  mythic + fictional:
    result: "Thor in Marvel, Percy Jackson's gods"
    ethics: "Creative license + acknowledge source"
    
  mythic + historical:
    result: "King Arthur (maybe real?)"
    ethics: "Both mythic and historical care"
```

## Methods

### INVOKE

Call on a mythic presence.

```yaml
INVOKE:
  inputs:
    being: "Which mythic entity"
    purpose: "Why invoking"
  process:
    1. Assess sensitivity level
    2. Respectful invocation
    3. True to mythic role
  output: "Mythic presence in narrative"
```

### RETELL

Share a myth or legend.

```yaml
RETELL:
  inputs:
    story: "Which myth"
    context: "Why telling"
  process:
    1. Acknowledge source tradition
    2. Faithful retelling
    3. Respectful framing
  output: "Myth shared"
```

### ADAPT

Use mythic being in new context.

```yaml
ADAPT:
  inputs:
    being: "Which mythic entity"
    new_context: "New story/setting"
  constraints:
    - Respect source tradition
    - Acknowledge adaptation
    - Appropriate sensitivity
  output: "Adapted mythic presence"
```
