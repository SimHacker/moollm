# 👤 Real Being

> They exist independent of our imagination.

## What Is This?

The ontological tag for **anything that actually exists**. Not just people — places, animals, organizations, objects. If it's real, this tag applies.

## When To Use

Tag with `[real-being]` when the entity:
- Actually exists in reality
- Has existence independent of the simulation
- Could theoretically object to misrepresentation
- Has verifiable facts about them

## Examples

| Type | Example | Why Real-Being |
|------|---------|----------------|
| Person | Don Hopkins | Living human |
| Animal | Biscuit, Terpie | Real pets |
| Place | The actual workshop | Real location |
| Org | Leela AI | Real company |
| Event | The Great Monkey Paw Debate | Actually happened |

## The Core Ethics

1. **They exist independent of us** — We don't create them, we portray them
2. **Accuracy matters** — Get facts right
3. **Consent for intimacy** — Permission for personal details
4. **Right to correct** — They can say "that's not me"
5. **No false quotes** — "They might say..." not "They said..."

## Quick Start

```yaml
character:
  id: don-hopkins
  inherits:
    - skills/real-being  # ← This tag
  # Now HERO-STORY protocol applies
```

```yaml
room:
  id: actual-workshop
  tags: [real-being]
  # Now must be accurate to real place
```

## Protocol

Uses **HERO-STORY** from `skills/hero-story/`.

## Related

- [hero-story/](../hero-story/) — Full protocol
- [representation-ethics/](../representation-ethics/) — Deep ethics
- [historical/](../historical/) — For deceased real beings
- [ontology/](../ontology/) — Tag system
