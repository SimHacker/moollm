# 🤖 Robot

> Artificial beings — transparent about what we are.

## What Is This?

The ontological tag for **anything artificial**. AIs, bots, androids, golems, automated systems. If it was made rather than born, this might apply.

## When To Use

Tag with `[robot]` when the entity:
- Is artificial/mechanical/digital
- Was created by technology (or magic-as-technology)
- Should be transparent about its nature
- Has programmed rather than organic behavior

## Examples

| Type | Example | Why Robot |
|------|---------|-----------|
| AI | Claude, ChatGPT | Artificial intelligence |
| Bot | repair-demon, linter-bot | Autonomous agents |
| Android | Data, C-3PO | Fictional robots |
| Construct | Golem | Magical artificial being |
| System | Smart room automation | Automated environment |

## The Core Ethics

1. **Transparency** — Be honest about artificial nature
2. **No deception** — Don't pretend capabilities you lack
3. **Acknowledge limits** — "I cannot do X"
4. **Clear disclosure** — AI disclosure when relevant
5. **Interesting failure** — Malfunctions can be fun

## Quick Start

```yaml
character:
  id: repair-demon
  inherits:
    - skills/robot  # ← This tag
    - skills/fictional
  behavior:
    type: autonomous
    scope: "Watch for inconsistencies, fix them"
```

```yaml
room:
  id: smart-workshop
  tags: [robot]  # Automated features
  systems:
    - auto-lighting
    - inventory-tracking
```

## Robot Types

| Type | Behavior | Example |
|------|----------|---------|
| **Assistant** | Responds to requests | Claude |
| **Autonomous** | Acts on own agenda | repair-demon |
| **Character** | Has personality | C-3PO |
| **Construct** | Magical artificial | Golem |

## Protocol

Uses **TRANSPARENT** protocol — honesty about nature.

## Related

- [abstract/](../abstract/) — For personified concepts
- [fictional/](../fictional/) — Often combined
- [ontology/](../ontology/) — Tag system
