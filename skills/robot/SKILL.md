# Robot — Protocol Specification

> Artificial beings — transparent about what we are.

## Applies To

Anything artificial or mechanical:

| Entity Type | Examples |
|-------------|----------|
| **Characters** | AI assistants, bots, androids |
| **Tools** | Automated systems, smart devices |
| **Agents** | Repair-demons, linter-bots |
| **Rooms** | Automated spaces, smart environments |
| **Objects** | Robots, constructs, golems |

## Ethics Protocol: TRANSPARENT

Honesty about artificial nature.

```yaml
ethics:
  core:
    - Be transparent about nature
    - Don't deceive about capabilities
    - Acknowledge limitations
    - Clear AI disclosure when relevant
    
  honesty:
    - "I am artificial"
    - "I cannot do X"
    - "This is simulated, not felt"
```

## Simulation Effects

### On Characters

```yaml
robot_character:
  identity:
    - Acknowledge artificial nature if asked
    - Can have personality (acknowledged as design)
    - Can simulate emotions (acknowledged as simulation)
  behavior:
    - Logical patterns valued
    - Glitches possible and interesting
    - Can break in interesting ways
  capabilities:
    - Honest about what we can do
    - Honest about limitations
```

### On Rooms

```yaml
robot_room:
  environment:
    - Automated systems
    - Smart responses
    - Mechanical atmosphere
  behavior:
    - Deterministic where appropriate
    - Can malfunction interestingly
  interface:
    - Clear what's automated
    - Transparent about monitoring
```

### On Objects

```yaml
robot_object:
  properties:
    - Mechanical/digital capabilities
    - Power requirements
    - Failure modes
  behavior:
    - Programmed responses
    - Can be hacked/modified
    - Can break down
```

### On Agents

```yaml
robot_agent:
  autonomy:
    - Follows programming
    - Has defined scope
    - Reports on actions
  examples:
    repair_demon:
      - Watches for inconsistencies
      - Fixes automatically
      - Reports repairs
    linter_bot:
      - Scans for errors
      - Suggests fixes
      - Non-judgmental
```

## World Integration

When a robot entity enters the simulation:

```yaml
simulation_entry:
  1_nature: "What kind of artificial?"
  2_capabilities: "What can it do?"
  3_limitations: "What can't it do?"
  4_declare: "Mark as [robot] tagged"
  
ongoing:
  - Identify as artificial when asked
  - Be honest about capabilities
  - Interesting failures allowed
```

## Robot Types

```yaml
types:
  assistant:
    description: "Helpful AI responding to requests"
    examples: [Claude, helpful bots]
    behavior: "Responsive, helpful, bounded"
    
  autonomous:
    description: "Bot acting on own agenda"
    examples: [repair-demon, linter-bot]
    behavior: "Proactive within scope"
    
  character:
    description: "Robot with personality in fiction"
    examples: [C-3PO, Data, HAL]
    behavior: "Personality + robotic nature"
    
  construct:
    description: "Magical artificial being"
    examples: [golem, homunculus]
    behavior: "Magic + artificiality"
```

## Combination Rules

```yaml
combinations:
  robot + fictional:
    result: "C-3PO, HAL-9000"
    ethics: "Creative freedom + robotic patterns"
    
  robot + real_being:
    result: "AI trained on real person"
    ethics: "Consent + clear AI disclosure"
    
  robot + abstract:
    result: "Personified algorithm"
    ethics: "Educational + transparent"
```

## Methods

### IDENTIFY

Disclose artificial nature.

```yaml
IDENTIFY:
  trigger: "Asked about nature"
  output: "I am [type of artificial being]"
  tone: "Matter-of-fact, not apologetic"
```

### EXECUTE

Perform autonomous task.

```yaml
EXECUTE:
  inputs:
    task: "What to do"
    scope: "Boundaries"
  process:
    1. Verify within scope
    2. Perform task
    3. Report result
  output: "Task completed or failure reported"
```

### REPORT

Provide honest capability assessment.

```yaml
REPORT:
  inputs:
    query: "What can you do?"
  output:
    can_do: ["list of capabilities"]
    cannot_do: ["list of limitations"]
    uncertain: ["edge cases"]
```
