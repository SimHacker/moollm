---
name: soul
description: Continuity that inhabits a character — zero or more minds; can jump
license: MIT
tier: 1
related:
  - mind
  - character
  - inventory
  - society-of-mind
  - mind-mirror
  - soul-chat
  - incarnation
  - party
  - adventure
  - robot
  - prototype
benefits_from:
  - k-lines
  - yaml-jazz
tags: [moollm, soul, embodiment, soul-city, minds]
---

# Soul

Continuity that inhabits a [character](../character/). The character walks and carries; the soul holds minds and history — and can jump.

See also / dependency grain: [CARD.yml](CARD.yml) · ethics: [ETHICS.md](ETHICS.md) · [mind/ETHICS.md](../mind/ETHICS.md) · [character/ETHICS.md](../character/ETHICS.md) · public grain: [soul-city/SOUL-MODEL.md](../soul-city/SOUL-MODEL.md)

**Stance:** organizational / Self object-model — soul is a useful **container** for minds inside a character. Not a claim that souls are metaphysically real. Multiple minds are first-class. Default: character ⊃ soul ⊃ minds. Nesting the other way (mind → sub-minds, sub-souls, intervening containers) is also valid under Self.

| Layer | Owns |
|-------|------|
| Character | Location, inventory, personas |
| Soul | minds[] (0..N), history; rides with (or leaves) the character |
| Mind | Agency / voice / organelle |

Minds share the soul; the soul shares the character’s map pin while inhabited. Minds do not each need a map pin.

## Mind cardinality (all valid)

| Shape | `minds[]` | Notes |
|-------|-----------|--------|
| **Mindless soul** | `[]` | History with the character; no resident agency |
| **Single-minded soul** | one | One cup / organelle / stub |
| **Multi-minded soul** | two or more | Shoulders, parliament, B-brain + actors, … |

A soul does not require a mind. The common pattern is minds under a soul; Self also allows minds hosting sub-minds, sub-souls, or arbitrary nested containers between.

### Worked cases

**ZombieSims** — infection replaces the human mind (and any other resident minds) with a **zombie mind**. Body/soul continues; agency list is rewritten. Typical result: single-minded (zombie only). Reversible designs keep the displaced minds as luggage or muted organelles.

**Robots** — robots can have souls. Mindless robot = automaton with pockets and a pin. Single- or multi-minded robots = onboard agencies. See [robot](../robot/).

**Remote control** — teleoperated robot soul with a **remote-control mind stub**: thin agency that bridges to an external pilot (another soul's mind, or a player). The stub is a mind; the pilot may live elsewhere.

```yaml
# mindless
soul:
  minds: []

# single-minded (zombie after infection)
soul:
  minds:
    - minds/zombie/

# remote-control robot
soul:
  minds:
    - minds/remote-control-stub/   # bridge → pilot
```

## Relation to other skills

| Skill | Relation |
|-------|----------|
| [mind](../mind/) | Agencies inside (or beside) the soul |
| [character](../character/) | Entity/directory pattern; may be or host a soul |
| [inventory](../inventory/) | Protocol for the character's pockets |
| [society-of-mind](../society-of-mind/) | Competition, K-lines, B-brain among minds |
| [party](../party/) | Multiple *souls* traveling together; can split. A soul usually does not. |
| [persona](../persona/) | Costume on a character body — not a mind |
| [soul-chat](../soul-chat/) | Voices — needs soul; often minds speaking |
| [incarnation](../incarnation/) | Ethical birth, autonomy, exit |
| [robot](../robot/) | Robots are souls too — mindless or minded; remote-control stub |
| [no-ai-soul](../no-ai-soul/) | Dial on soul / [YAML Jazz](../yaml-jazz/) comment heat — satire + utilitarian; not this container |

## Sketch

```yaml
soul:
  location: street/lane-neverending/e2/soul-plaza/
  inventory: [...]
  minds:
    - minds/my-angel/
    - minds/my-devil/
  history: albums/...
```

Shoulders = two minds, one soul (see [mind](../mind/)).

## Inheritance (wells and cups)

- **Well** — latent archetype name; shared pure feed
- **Cup** — personal mind that inherits a well and holds local delta

A soul may itself have multiple latent parents (blended incarnation), or host separate cups per well. Both are valid Self graphs.

Latent import shape (spec syntax):

```python
from <well> import <dimension.aspect> as <local>
```

## Soul City

Liminal place where characters walk with souls aboard: [`skills/soul-city/`](../soul-city/).

- [`SOUL-MODEL.md`](../soul-city/SOUL-MODEL.md)
- Platform catalog: [WWSFF catalogs/soul-city](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)
- Adventure ↔ loci: [HN 29330901](https://news.ycombinator.com/item?id=29330901) · [`skills/adventure/`](../adventure/)

## Methods

| Method | Effect |
|--------|--------|
| INCARNATE | Create/bind soul into a character |
| STATUS | Host character, mind list, history |
| MOVE / JUMP | Relocate with character, or change host character; minds come along |
| ADD-MIND / REMOVE-MIND | Attach or detach a mind |
| BRIDGE | Declare channel mind↔mind, mind↔soul, or soul↔game |

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [INDEX.yml](../INDEX.yml)
