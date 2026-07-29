---
name: soul
description: Continuity body — one location, shared inventory, zero or more minds
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

Continuity body on the adventure map.

See also / dependency grain: [CARD.yml](CARD.yml) · ethics: [ETHICS.md](ETHICS.md) · [mind/ETHICS.md](../mind/ETHICS.md) · [character/ETHICS.md](../character/ETHICS.md)

**Stance:** organizational / Self object-model — soul is a useful **container** for minds. Not a claim that souls are metaphysically real. Multiple minds are first-class. Default: soul contains zero or more minds. Nesting the other way (mind → sub-minds, sub-souls, intervening containers) is also valid under Self.

| Owns | Notes |
|------|--------|
| location | One map pin |
| inventory | Shared pockets (native + luggage) |
| minds[] | Zero or more resident agencies |
| history | Albums, journals, lived experience |

Minds share the soul's location. They do not each need a map pin.

## Mind cardinality (all valid)

| Shape | `minds[]` | Notes |
|-------|-----------|--------|
| **Mindless soul** | `[]` | Location + inventory + history; no resident agency |
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
| [inventory](../inventory/) | Protocol for the soul's shared pockets |
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

Liminal place where souls walk: [`skills/soul-city/`](../soul-city/).

- [`SOUL-MODEL.md`](../soul-city/SOUL-MODEL.md)
- Platform catalog: [WWSFF catalogs/soul-city](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)
- Adventure ↔ loci: [HN 29330901](https://news.ycombinator.com/item?id=29330901) · [`skills/adventure/`](../adventure/)

## Methods

| Method | Effect |
|--------|--------|
| INCARNATE | Create/bind soul from `CHARACTER.yml` or directory |
| STATUS | Location, inventory summary, mind list |
| MOVE | Relocate soul; minds travel with it |
| ADD-MIND / REMOVE-MIND | Attach or detach a mind |
| BRIDGE | Declare channel mind↔mind, mind↔soul, or soul↔game |

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [INDEX.yml](../INDEX.yml)
