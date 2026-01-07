---
name: empathic-templates
description: "Smart templates that understand semantic intent, not just string substitution"
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [empathic-expressions, postel, yaml-jazz, skill]
---

# Empathic Templates

> *"Templates that understand what you mean, not just what you wrote."*

---

## What Is It?

**Empathic Templates** are MOOLLM's approach to template instantiation: templates that leverage LLM comprehension to understand **semantic intent**, not just perform mechanical string substitution.

Traditional templates: `{{name}}` → replace with literal value
Empathic templates: `{{name}}` → understand what name means in context, generate appropriate content

---

## The Difference

### Traditional Templates (Handlebars, Jinja, etc.)

```handlebars
Hello {{name}}!

Your order {{order_id}} has shipped.
Items: {{items}}
Total: ${{total}}
```

**Problem:** If `items` is a list, you need explicit loop syntax. If `total` should be formatted, you need filters. The template is dumb.

### Empathic Templates

```yaml
# The template understands context
greeting: "{{appropriate_greeting}}"
order_summary: "{{summarize_order_naturally}}"
items: "{{list_items_with_quantities}}"
total: "{{format_currency(total)}}"
```

The LLM doesn't just substitute — it **interprets**:
- `{{appropriate_greeting}}` becomes "Good morning, Sarah!" or "Hey there!" based on context
- `{{summarize_order_naturally}}` becomes prose, not data dump
- `{{list_items_with_quantities}}` formats intelligently

---

## How It Works

### 1. Parse Template

```yaml
template: |
  # {{character_name}}
  
  {{describe_appearance}}
  
  ## Personality
  {{personality_as_prose}}
  
  ## Catchphrase
  > "{{generate_catchphrase}}"
```

### 2. Understand Context

```yaml
context:
  character_type: "grumpy wizard"
  setting: "medieval fantasy"
  tone: "humorous"
  age: "ancient"
```

### 3. Semantic Generation

The LLM doesn't just fill slots — it **creates coherent content**:

```markdown
# Grumbald the Insufferable

A stooped figure wrapped in robes that were probably purple
once, before centuries of potion stains and cat hair took
their toll. His beard reaches his knees and contains at
least three quills, a small bird's nest, and what might be
a sandwich from the Third Age.

## Personality

Grumbald has perfected the art of making everyone feel
slightly stupid. He answers questions with questions,
sighs dramatically at simple requests, and has been
known to turn people into newts for using incorrect
grammar. Deep down, he cares — but he'd rather be
turned into a newt himself than admit it.

## Catchphrase

> "I've forgotten more magic than you'll ever know.
> Literally. Where did I put my staff?"
```

---

## Template Syntax

### Basic Slots

```yaml
{{variable}}           # Simple substitution (still works)
{{expression}}         # Empathic expression (interpreted)
{{#if condition}}      # Conditional (condition is interpreted)
{{#each items}}        # Iteration (smart about structure)
{{> partial}}          # Include another template
```

### Empathic Slots (The Magic)

```yaml
{{describe_X}}         # Generate description based on context
{{summarize_Y}}        # Create summary of data
{{generate_Z}}         # Create new content fitting context
{{appropriate_W}}      # Choose fitting value from possibilities
{{format_V}}           # Intelligent formatting
```

### Expressions with Empathic Interpretation

```yaml
{{#if character.is_hungry}}
  {{describe_hunger_behavior}}
{{/if}}

{{#if player.reputation > 50}}
  # The guard recognizes you
  {{guard_friendly_greeting}}
{{else}}
  # The guard is suspicious
  {{guard_suspicious_challenge}}
{{/if}}
```

The conditions use [Empathic Expressions](../empathic-expressions/) for flexible interpretation.

---

## Used For

### Character Creation

```yaml
# CHARACTER.yml.tmpl
id: {{generate_unique_id}}
name: "{{character_name}}"
species: "{{species}}"
description: |
  {{describe_appearance_based_on_species_and_personality}}

personality:
  {{infer_sims_traits_from_description}}

catchphrase: "{{generate_fitting_catchphrase}}"

backstory: |
  {{generate_backstory_consistent_with_setting}}
```

### Room Generation

```yaml
# ROOM.yml.tmpl
room:
  name: "{{room_name}}"
  type: {{room_type}}
  
  description: |
    {{describe_room_atmospherically}}
    
    {{describe_notable_features}}
    
    {{hint_at_secrets_if_any}}

  exits:
    {{generate_exits_based_on_maze_topology}}
    
  objects:
    {{place_appropriate_objects}}
```

### Session Logs

```yaml
# SESSION.md.tmpl
## Session {{session_number}} — {{session_date}}

### Summary
{{summarize_session_events}}

### Key Moments
{{list_memorable_moments}}

### State Changes
{{document_world_changes}}

### Next Steps
{{suggest_continuation_hooks}}
```

---

## The Empathic Expression Connection

Templates use Empathic Expressions for:

### Variables
```yaml
{{user.name}}                    # Simple lookup
{{user.status | capitalize}}     # With filter
{{player.has_item('key')}}       # Method call
```

### Conditions
```yaml
{{#if character.mood == 'happy'}}  # Exact match
{{#if character.is_friendly}}       # Boolean inference
{{#if gold > 100}}                  # Numeric comparison
{{#if player.can_afford(item)}}     # Method evaluation
```

### Iterations
```yaml
{{#each inventory.items}}
  - {{this.name}}: {{this.description}}
{{/each}}
```

### Code-Switching IN Templates
```yaml
# Generate SQL for the report
query: |
  {{empathic_sql: "get all users who ordered in the last month"}}

# Generate the email
email: |
  Dear {{user.name}},
  
  {{summarize_monthly_orders_naturally}}
  
  Total spent: {{format_currency(monthly_total)}}
```

---

## Template Discovery Pattern

**First 50 lines sniff:**

Templates should front-load:
1. Template metadata (name, purpose, required context)
2. Required variables list
3. Optional variables with defaults

```yaml
# =====================================================
# CHARACTER.yml.tmpl — Character sheet template
# 
# Required context:
#   - character_name: string
#   - species: string  
#   - setting: string (e.g., "medieval fantasy")
#
# Optional context:
#   - personality_hints: list of traits
#   - backstory_seeds: key events to include
#   - tone: "serious" | "humorous" | "dark" (default: "neutral")
# =====================================================

id: {{generate_unique_id}}
name: "{{character_name}}"
# ... rest of template
```

LLM can sniff first 50 lines to understand what the template needs before reading the full file.

---

## Comment Intelligence

The LLM distinguishes between **meta-comments** (instructions for generation) and **concrete comments** (meant for output):

### Meta-Comments (Stripped)

```yaml
# TEMPLATE: This section describes the character's appearance
# INSTRUCTION: Use vivid sensory details
# NOTE: Keep under 100 words
# TODO: Add more variety to hair colors
description: |
  {{describe_appearance}}
```

These are **instructions TO the LLM**. They guide generation but don't appear in output.

### Concrete Comments (Preserved)

```yaml
# This character was created using the incarnation protocol.
# See skills/incarnation/SKILL.md for details.
description: |
  {{describe_appearance}}

# Sims traits determine interaction success rates
sims_traits:
  {{generate_traits}}
```

These are **comments FOR the output file**. They explain the generated content to future readers.

### How the LLM Knows

| Indicator | Type | Action |
|-----------|------|--------|
| `# TEMPLATE:`, `# INSTRUCTION:`, `# NOTE:` | Meta | Strip |
| `# TODO:`, `# FIXME:` in template context | Meta | Strip |
| `# This explains...`, `# See also...` | Concrete | Preserve |
| Comments inside `{{...}}` blocks | Meta | Strip |
| Comments explaining generated values | Concrete | Preserve |
| ALL CAPS directive style | Meta | Strip |
| Lowercase explanatory style | Concrete | Preserve |

### Example: Mixed Comments

**Template:**
```yaml
# TEMPLATE: Character soul file
# INSTRUCTION: Generate YAML Jazz style comments

# This character was incarnated via the full autonomy protocol.
id: {{generate_id}}
name: "{{character_name}}"

# INSTRUCTION: Describe based on species and personality
description: |
  {{describe_appearance}}

# Personality traits affect all interactions
# Higher values = stronger tendency
sims_traits:
  nice: {{nice_value}}  # 0-10, affects social success
  # INSTRUCTION: Infer from description
  playful: {{infer_playful}}
```

**Generated Output:**
```yaml
# This character was incarnated via the full autonomy protocol.
id: palm-001
name: "Palm"

description: |
  A small capuchin monkey with knowing eyes and surprisingly
  dexterous fingers. Palm moves with the confidence of someone
  who has already seen how this story ends.

# Personality traits affect all interactions
# Higher values = stronger tendency
sims_traits:
  nice: 7  # 0-10, affects social success
  playful: 9
```

**What happened:**
- `# TEMPLATE:` and `# INSTRUCTION:` lines → **stripped**
- `# This character was incarnated...` → **preserved**
- `# Personality traits affect...` → **preserved**
- `# 0-10, affects social success` → **preserved**
- `# INSTRUCTION: Infer from description` → **stripped**

### The Principle

> **Meta-comments teach the generator. Concrete comments teach the reader.**

The LLM understands this distinction because it understands **intent**. Directive language instructs; explanatory language documents.

---

## Relationship to Self-Style Inheritance

Templates are **prototypes**. Instantiation creates **instances**:

```yaml
prototype: skills/character/CHARACTER.yml.tmpl
  ↓ instantiate with context
instance: examples/adventure-4/characters/palm/CHARACTER.yml
```

The template defines **shape and intent**. The instance contains **specific values**.

But empathic templates go further: they generate **appropriate content**, not just fill slots.

---

## Examples

### Instantiating a Buff

```yaml
# BUFF.yml.tmpl
buff:
  id: {{buff_id}}
  name: "{{buff_name}}"
  type: {{buff_type}}
  
  description: |
    {{describe_buff_effect_flavorfully}}
  
  mechanics:
    duration: {{duration}}
    effect: "{{describe_mechanical_effect}}"
    
  trigger: "{{empathic_expression: trigger_condition}}"
  
  flavor_text: |
    {{generate_flavor_text_matching_setting}}
```

**Context:**
```yaml
buff_name: "Sugar Rush"
buff_type: positive
trigger_condition: "eating candy or sweet treats"
setting: "whimsical candy land"
```

**Generated:**
```yaml
buff:
  id: sugar-rush
  name: "Sugar Rush"
  type: positive
  
  description: |
    Your eyes widen, your heart races, and suddenly
    EVERYTHING IS AMAZING. Colors are brighter, sounds
    are sweeter, and you're pretty sure you could
    outrun a unicorn.
  
  mechanics:
    duration: 10 minutes
    effect: "+20% speed, +10% charisma, -10% focus"
    
  trigger: "consuming_sweet_treat"
  
  flavor_text: |
    *The sugar hits your bloodstream like a 
    candy-coated lightning bolt. WHEEEEE!*
```

---

## Anti-Pattern: Dumb Templates

**Don't do this:**
```yaml
description: "{{description}}"  # Just passes through
personality: "{{personality}}"  # No generation
```

**Do this:**
```yaml
description: |
  {{describe_character_based_on_traits_and_setting}}
  
personality:
  {{infer_traits_from_context}}
```

Let the LLM add value. That's the whole point.

---

## Dovetails With

- [Empathic Expressions](../empathic-expressions/) — The expression engine
- [YAML Jazz](../yaml-jazz/) — Expressive data with comments
- [Skill](../skill/) — Templates as prototypes
- [Character](../character/) — Character sheet templates
- [Room](../room/) — Room generation templates
- [Postel](../postel/) — Generous interpretation in templates

---

## Protocol Symbol

```
EMPATHIC-TEMPLATES
```

Invoke when: Instantiating templates with semantic understanding.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#EMPATHIC-TEMPLATES)
