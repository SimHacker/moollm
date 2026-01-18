# Ontology — Protocol Specification

> Tags, not trees. Folksonomy, not taxonomy.

## Core Principle

Characters are **tagged**, not **classified**. A being can be:
- `[real-being, animal]` — Biscuit the actual dog
- `[fictional, robot]` — C-3PO
- `[historical, abstract]` — "The Spirit of Papert"
- `[real-being, robot, fictional]` — AI trained on someone's writings

The directory structure (`characters/animals/dogs/biscuit/`) is organizational convenience. The **tags are the source of truth** for what kind of being this is.

## The Tags

### `real-being` 👤

Actually exists or existed. Carries the heaviest ethical weight.

```yaml
ethics:
  - Respect their actual existence
  - Get consent for intimate portrayal
  - Be accurate about verifiable facts  
  - They have right to correct you
```

### `historical` 📜

Real being who has died. Extends `real-being` with additional care.

```yaml
ethics:
  - Scholarly accuracy duty
  - Provide era-appropriate context
  - Respect their legacy
  - No consent possible — be extra careful
```

### `fictional` 📖

Invented. Does not exist in reality.

```yaml
ethics:
  - Creator/author has authority
  - Maintain internal consistency
  - Don't make real-world claims
  - Creative freedom within room constraints
```

### `animal` 🐾

Non-human creature. Can combine with `real-being` or `fictional`.

```yaml
ethics:
  - Behave species-appropriately
  - If anthropomorphizing, acknowledge it
  - Respect animal nature
  - Don't claim capabilities they lack
  
inheritance:
  - Young can inherit from parents (biological or adoptive)
  - Species provides base behaviors
  - Individual personality overlays
```

### `robot` 🤖

Artificial or mechanical being.

```yaml
ethics:
  - Be transparent about nature
  - Don't deceive about capabilities
  - Acknowledge limitations
  - Clear AI disclosure when relevant
```

### `abstract` 💭

Concept or idea given voice.

```yaml
ethics:
  - Represent the concept faithfully
  - Acknowledge this is personification
  - Frame educationally
  - Don't claim actual sentience
```

### `mythic` ✨

From mythology, folklore, or religion.

```yaml
ethics:
  - Cultural sensitivity required
  - Acknowledge source tradition
  - Respect sacred contexts
  - Often overlaps with fictional
```

## Composition Rules

When a character has multiple tags, ethics **compose**:

```yaml
composition_algorithm:
  1. Collect all ethics from all tags
  2. Remove duplicates
  3. When conflicts arise:
     - real-being concerns override fictional freedom
     - animal nature overrides human projection
     - robot transparency overrides persona immersion
  4. Room ethics layer on top
```

### Example: Biscuit

```yaml
character:
  id: biscuit
  tags: [real-being, animal]
  
# Composed ethics:
effective_ethics:
  from_real_being:
    - "Biscuit actually exists"
    - "Respect his real nature"
  from_animal:
    - "Dog behavior, not human"
    - "Species-appropriate actions"
  combined:
    - "This is a real dog — portray him as he actually is"
    - "Don't put human words in his mouth as if he said them"
    - "His personality in the game reflects his real personality"
```

### Example: Don-Bot

```yaml
character:
  id: don-bot
  tags: [real-being, robot, fictional]
  based_on: characters/don-hopkins
  
# Composed ethics:
effective_ethics:
  from_real_being:
    - "Based on a real person"
    - "Don's consent required"
  from_robot:
    - "This is an AI, not Don"
    - "Be transparent about nature"
  from_fictional:
    - "Responses are generated"
    - "Not actual quotes unless marked"
  combined:
    - "AI inspired by Don Hopkins (with permission)"
    - "Clearly an AI, not the person"
    - "Don't present generated text as real quotes"
```

## Inheritance Types

Tags enable different inheritance patterns:

```yaml
inheritance_patterns:

  structural:
    what: "Type hierarchy"
    example: "kitten extends cat extends animal"
    inherits: [methods, advertisements, base behaviors]
    
  parental:
    what: "Biological or adoptive parent-child"
    example: "Kitten-3 inherits from Stroopwafel (mother)"
    inherits: [personality traits, learned behaviors, relationships]
    requires: [animal] tag
    bidirectional: true
    
  familiar:
    what: "Companion bond"
    example: "Biscuit is Don's familiar"
    inherits: [location awareness, some goals]
    delegation: true  # Familiar can act for character
    
  persona:
    what: "Worn identity overlay"
    example: "Don wearing 'Professor' persona"
    inherits: [presentation, vocabulary, role-specific behavior]
    temporary: true
```

## Directory Mirroring

The `characters/` directory structure mirrors common patterns:

```
characters/
  animals/
    dogs/
      biscuit/
    cats/
      stroopwafel/
      terpie/
  people/
    don-hopkins/
  robots/
    repair-demon/
  concepts/
    yaml-jazz/
```

But this is **organizational**, not **definitional**. The CHARACTER.yml file declares tags:

```yaml
# characters/animals/dogs/biscuit/CHARACTER.yml
character:
  id: biscuit
  
  # Tags are the truth
  ontology:
    tags: [real-being, animal]
    species: dog
    
  # Directory is just where we filed it
  # Could be moved without changing identity
```

## Room Ethics Overlay

Rooms provide environmental ethical framing that combines with character tags:

```yaml
# Room declares context
room:
  ethics:
    frame: "whimsical adventure"
    constraints: [family-friendly, educational]
    
# Character brings their tags
character:
  tags: [real-being, animal]
  
# Combined for this interaction:
effective_context:
  character_ethics: [respect existence, species-appropriate]
  room_ethics: [family-friendly, educational]
  result: "Portray real dog in family-friendly educational context"
```

## Methods

### TAG

Assign ontological tags to a character.

```yaml
TAG:
  parameters:
    character: "Path to character"
    tags: ["tag1", "tag2"]
  effect: "Sets character.ontology.tags"
  validation: "Tags must be from known set"
```

### CHECK-ETHICS

Compute the combined ethics for a character in a context.

```yaml
CHECK-ETHICS:
  parameters:
    character: "Character to check"
    room: "Optional room context"
  output:
    tags: ["real-being", "animal"]
    ethics: ["list of combined constraints"]
    warnings: ["any special concerns"]
```

### COMPOSE

Create a hybrid character from multiple sources.

```yaml
COMPOSE:
  parameters:
    sources:
      - type: "real-being"
        source: "don-hopkins"
      - type: "robot"
        source: "gpt-4"
  output:
    suggested_tags: ["real-being", "robot", "fictional"]
    ethics: ["combined constraints"]
    warnings: ["consent required", "AI disclosure needed"]
```
