# ✨ Mythic

> The old stories still have power.

## What Is This?

The ontological tag for **beings from mythology and folklore**. Gods, spirits, legendary creatures. Some are still worshipped — handle with care.

## When To Use

Tag with `[mythic]` when the entity:
- Comes from mythology or folklore
- Has religious or cultural significance
- Is a legendary creature
- Carries symbolic meaning beyond the literal

## Examples

| Type | Example | Sensitivity |
|------|---------|-------------|
| God (active) | Shiva, Jesus | HIGH |
| God (historical) | Zeus, Odin | Medium |
| Hero | Hercules, King Arthur | Medium |
| Spirit | Faeries, djinn | Medium |
| Creature | Dragon, unicorn | Lower |
| Object | Excalibur, Mjolnir | Lower |

## Sensitivity Levels

| Level | Meaning | Examples |
|-------|---------|----------|
| **HIGH** | Still worshipped | Jesus, Allah, Ganesha |
| **Medium** | Cultural heritage | Zeus, Thor, Hercules |
| **Lower** | Creatures/objects | Dragons, unicorns |

## Quick Start

```yaml
character:
  id: dragon-smaug
  inherits:
    - skills/mythic     # ← Cultural awareness
    - skills/fictional  # ← From Tolkien
    - skills/animal     # ← Creature behavior
```

```yaml
object:
  id: excalibur
  tags: [mythic]
  source: "Arthurian legend"
```

## The Core Ethics

1. **Cultural sensitivity** — Some are sacred
2. **Acknowledge source** — Credit the tradition
3. **Respect sacred** — No mockery of active worship
4. **Context matters** — Educational vs entertainment
5. **Creative license** — Allowed with awareness

## Protocol

Uses **MYTHIC** protocol — cultural respect + creative adaptation.

## Related

- [fictional/](../fictional/) — Often combined for adaptations
- [historical/](../historical/) — For maybe-real legends
- [animal/](../animal/) — For mythic creatures
- [ontology/](../ontology/) — Tag system
