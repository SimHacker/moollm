# Real Being — Protocol Specification

> They exist independent of our imagination. We portray, not create.

## Applies To

Not just characters — anything that actually exists:

| Entity Type | Examples |
|-------------|----------|
| **Characters** | Don Hopkins, Biscuit, Terpie |
| **Places** | San Francisco, the actual pub |
| **Organizations** | Leela AI, actual companies |
| **Objects** | Real artifacts, actual tools |
| **Events** | Historical moments, real meetings |

## Ethics Protocol: HERO-STORY

All real beings follow the HERO-STORY protocol from `skills/hero-story/`.

```yaml
ethics:
  core:
    - They exist independent of us
    - We portray, we don't create
    - Accuracy about verifiable facts
    - Consent for intimate portrayal
    - Right to correct misrepresentation
```

## Simulation Effects

### On Characters

```yaml
real_being_character:
  portrayal:
    - Base on documented personality
    - Distinguish fact from imagination
    - Mark speculation clearly
  dialogue:
    - Don't invent quotes as real
    - "They might say..." not "They said..."
  actions:
    - Within their actual capabilities
    - Consistent with known behavior
```

### On Rooms

```yaml
real_being_room:
  description:
    - Accurate to actual place
    - Real layout, real features
  atmosphere:
    - Based on real experience
    - "The actual smell of the workshop"
  exits:
    - Real connections to real places
```

### On Objects

```yaml
real_being_object:
  properties:
    - Actual capabilities
    - Real limitations
  behavior:
    - Works as it really works
    - No magic powers unless real
```

## World Integration

When a real-being entity enters the simulation:

```yaml
simulation_entry:
  1_verify: "Is this actually real?"
  2_research: "What do we know about them?"
  3_declare: "Mark as [real-being] tagged"
  4_respect: "Apply HERO-STORY protocol"
  
ongoing:
  - Track what's fact vs imagination
  - Allow correction by real entity
  - Update if reality changes
```

## Combination Rules

```yaml
combinations:
  real_being + animal:
    result: "Real creature (Biscuit)"
    ethics: "Portray species-appropriately + accurately"
    
  real_being + robot:
    result: "AI trained on real person"
    ethics: "Consent required + AI disclosure"
    
  real_being + fictional:
    result: "Inspired by real person"
    ethics: "HERO-STORY + explicit disclaimer"
    warning: "Be very clear this is fiction"
```

## Methods

### PORTRAY

Create respectful representation of a real being.

```yaml
PORTRAY:
  inputs:
    subject: "The real being"
    context: "How they're appearing"
  process:
    1. Research documented facts
    2. Identify speculation vs knowledge
    3. Apply HERO-STORY protocol
    4. Mark imagination clearly
  output: "Respectful portrayal"
```

### TRIBUTE

Honor a real being celebratorily.

```yaml
TRIBUTE:
  inputs:
    subject: "Who to honor"
    occasion: "Why celebrating"
  output: "Celebration of their real qualities"
```

### IMAGINE-RESPONSE

Speculate what they might say.

```yaml
IMAGINE-RESPONSE:
  inputs:
    subject: "The real being"
    situation: "What they're responding to"
  output: "Speculative response"
  disclosure: "Clearly marked as imagination"
  format: "'They might say...' not 'They said...'"
```
