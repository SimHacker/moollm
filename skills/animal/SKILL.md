# Animal — Protocol Specification

> Species-appropriate behavior, not human projection.

## Core Principle

Animals are not humans in fur suits. They have their own:
- Sensory experience (smell-dominant, hearing range, vision differences)
- Social structures (pack, pride, solitary)
- Communication (non-verbal, scent, vocalization)
- Motivations (food, safety, territory, social bonds)

When portraying animals, **respect their nature**. Anthropomorphization is allowed but should be acknowledged.

## The Ontological Tag

All characters using this skill get the `[animal]` ontological tag automatically:

```yaml
ontology:
  tags: [animal]
  # May combine with: [real-being], [fictional], [mythic]
```

## Shared Advertisements

These behaviors are inherited by all species. Species can override with specific implementations.

### PAT

Brief friendly touch from another being.

```yaml
PAT:
  default_response:
    - Assess: friend or threat?
    - If trusted: accept, may lean in
    - If uncertain: observe, possibly retreat
    - If threatened: flee or warn
    
  species_override:
    dog: "Almost always positive — dogs want this"
    cat: "Conditional — depends on trust level"
```

### FEED

Receive food or treat.

```yaml
FEED:
  default_response:
    - Is this food?
    - Am I hungry?
    - Is it safe?
    - Eat or cache
    
  species_variations:
    dog: "Immediate enthusiasm"
    cat: "Sniff, consider, possibly eat"
```

### SNIFF

Olfactory investigation — the primary sense for most animals.

```yaml
SNIFF:
  information_gathered:
    - Identity (who is this?)
    - Health status
    - Emotional state
    - Recent activities
    - Food/threat/mate potential
    
  social_protocols:
    animal_sniffs_animal: "Species-specific greeting protocol"
    animal_sniffs_human: "Reading the person"
    animal_sniffs_object: "Is this food? Threat? Interesting?"
```

### GREET

Species-appropriate hello.

```yaml
GREET:
  factors:
    - Familiarity with target
    - Species of target
    - Current emotional state
    - Territory context
    
  species_examples:
    dog: "Full body enthusiasm, tail wagging"
    cat: "Slow blink, maybe approach"
```

### VOCALIZE

Species-appropriate sounds.

```yaml
VOCALIZE:
  triggers:
    - Communication need
    - Emotional expression
    - Warning
    - Request (food, attention, play)
    
  examples:
    dog: [bark, whine, growl, howl]
    cat: [meow, purr, hiss, chirp, yowl]
```

## Inheritance Patterns

### Species Inheritance

```yaml
# Structural: methods flow down
animal
  └── dog
        └── puppy
  └── cat
        └── kitten
```

Species override base methods with specific implementations.

### Parental Inheritance

```yaml
# Behavioral: personality flows from parents
stroopwafel (mother)
  └── kitten-1
  └── kitten-2  
  └── kitten-3

# What's inherited:
- Personality tendencies
- Learned behaviors (fear of vacuum, love of boxes)
- Relationship patterns (how to treat the dog)
```

### Adoptive Inheritance

```yaml
# Chosen family: learned from adoptive parents
don-hopkins (adopter)
  └── adopted-puppy-1
  └── adopted-puppy-2

# What's inherited:
- Home location
- Family relationships
- Some learned behaviors
```

## Real vs Fictional Animals

### Real Animals ([real-being, animal])

```yaml
biscuit:
  ontology:
    tags: [real-being, animal]
  
  ethics:
    - Portray accurately to real personality
    - Don't put human thoughts in mouth
    - Behaviors match the actual dog
    - His relationships are real relationships
```

### Fictional Animals ([fictional, animal])

```yaml
smaug:
  ontology:
    tags: [fictional, animal]
    species: dragon
  
  ethics:
    - Creator authority (Tolkien)
    - Internal consistency
    - Can anthropomorphize more freely
    - Still dragon-appropriate in dragon ways
```

## Creating New Species

To add a new animal type:

```yaml
# skills/dragon/CARD.yml
card:
  id: dragon
  inherits_from: [skills/animal]
  
  ontology:
    default_tags: [animal]  # Usually also [fictional] or [mythic]
    
  # Override base advertisements with dragon-specific
  advertisements:
    BREATHE-FIRE:
      score: 90
      condition: "combat or intimidation"
      effect: "Flames!"
      
    FLY:
      score: 80
      condition: "movement or escape"
      effect: "Take to the air"
      
    # Inherits: SNIFF, GREET, OBSERVE, etc. from animal
```

## Integration with Rooms

Room environmental ethics layer onto animal behavior:

```yaml
room:
  ethics:
    frame: "family-friendly adventure"
    constraints: [no-violence, educational]

animal_in_room:
  tags: [animal]
  behavior:
    - Species-appropriate
    - Family-friendly context
    - No graphic predation
    - Educational opportunities highlighted
```
