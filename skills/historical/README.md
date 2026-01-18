# 📜 Historical

> They lived. They're gone. We cannot ask permission.

## What Is This?

The ontological tag for **deceased real beings**. Extends `[real-being]` with extra care — they cannot consent, correct, or respond. We must be extra careful.

## When To Use

Tag with `[historical]` when the entity:
- Was real but has died
- Cannot consent to portrayal
- Has a legacy that matters to living people
- Requires scholarly accuracy

## Examples

| Type | Example | Why Historical |
|------|---------|----------------|
| Scientist | Marvin Minsky | Deceased pioneer |
| Educator | Seymour Papert | Deceased visionary |
| Inventor | Alan Turing | Historical figure |
| Animal | Koko the gorilla | Famous deceased animal |
| Place | Original workshop (demolished) | No longer exists |

## Extra Care Required

Because they cannot consent or correct:

1. **Research thoroughly** — Know what they actually said
2. **Mark speculation** — "They might have..." not "They said..."
3. **Era context** — Their time was different
4. **Living relatives** — Family may have feelings
5. **Legacy communities** — People carry on their work

## Quick Start

```yaml
character:
  id: spirit-of-minsky
  inherits:
    - skills/historical  # ← Gets real-being ethics +
    - skills/abstract    # ← Personification acknowledgment
  disclosure: "Imagining what Minsky might say"
```

## The Protocol Stack

```
historical
    ↓ extends
real-being
    ↓ uses
HERO-STORY protocol
    ↓ plus
MEMORIAL extra care
```

## Related

- [real-being/](../real-being/) — Base protocol
- [hero-story/](../hero-story/) — Portrayal guidelines
- [abstract/](../abstract/) — For "spirit of" framing
- [ontology/](../ontology/) — Tag system
