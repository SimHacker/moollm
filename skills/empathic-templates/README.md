# Empathic Templates

> *"Templates that understand what you mean, not just what you wrote."*

Smart templates that leverage LLM comprehension for semantic instantiation.

## Quick Overview

**Traditional templates:** `{{name}}` → literal string substitution

**Empathic templates:** `{{name}}` → understand context, generate appropriate content

## The Difference

**Before (dumb):**
```yaml
description: "{{description}}"  # Just passes through
```

**After (empathic):**
```yaml
description: |
  {{describe_character_based_on_traits_and_setting}}
```

The LLM doesn't just substitute — it **creates coherent content** that fits the context.

## Example

**Template:**
```yaml
# CHARACTER.yml.tmpl
name: "{{character_name}}"
description: "{{describe_appearance}}"
catchphrase: "{{generate_fitting_catchphrase}}"
```

**Context:**
```yaml
character_name: "Grumbald"
character_type: "grumpy wizard"
tone: "humorous"
```

**Output:**
```yaml
name: "Grumbald the Insufferable"
description: |
  A stooped figure in stained purple robes, 
  beard reaching his knees, containing at least
  three quills and what might be a sandwich
  from the Third Age.
catchphrase: "I've forgotten more magic than you'll ever know."
```

## Files

| File | Purpose |
|------|---------|
| [SKILL.md](./SKILL.md) | Full specification |
| [CARD.yml](./CARD.yml) | Machine-readable interface |

## See Also

- [Empathic Expressions](../empathic-expressions/) — The expression engine
- [YAML Jazz](../yaml-jazz/) — Expressive data with comments
- [Skill](../skill/) — Templates as prototypes
