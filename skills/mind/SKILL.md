---
name: mind
description: Resident agency inside a soul — well, cup, or organelle
license: MIT
tier: 1
related:
  - soul
  - character
  - society-of-mind
  - mind-mirror
  - soul-chat
  - prototype
  - k-lines
  - representation-ethics
benefits_from:
  - yaml-jazz
  - inventory
tags: [moollm, mind, cup, well, organelle, soul-city]
---

# Mind

Resident agency — usually inside (or beside) a [soul](../soul/).

See also: [CARD.yml](CARD.yml) · ethics: [ETHICS.md](ETHICS.md) · [soul/ETHICS.md](../soul/ETHICS.md) · [character/ETHICS.md](../character/ETHICS.md) · grain: [../soul/CARD.yml](../soul/CARD.yml)

**Stance:** minds are first-class agencies. Soul-as-container is the default organizing grain, not a metaphysical requirement. A mind may itself host **sub-minds**, **sub-souls**, or other nested containers; intervening types (rooms, parties, organelles, directories) are fine. Self models anything.

| Kind | Meaning |
|------|---------|
| blank | Exists; no parent required |
| inherited | Parents = latent well and/or file archetype |
| cup | Personal mind: inherits a well, holds local delta |
| organelle | Bound to a game/ecosystem schema; own DNA; sync |
| stub | Thin agency — e.g. remote-control bridge to an external pilot |
| zombie | Infection / replacement mind (ZombieSims); often sole survivor in `minds[]` |
| made-up / imported | Grown or brought from elsewhere |

Default: shares the soul's location and inventory access. No separate map pin.

Host soul may be **mindless** (`minds: []`), **single-minded**, or **multi-minded**. See [soul](../soul/#mind-cardinality-all-valid).

## Nesting

```yaml
# default grain
soul:
  minds: [minds/a/, minds/b/]

# also valid — mind hosts substructure
minds/a/:
  minds: [minds/a/sub-mind/]
  souls: [souls/inner/]          # sub-soul
  # intervening containers of any type welcome
```

## Relation to other skills

| Skill | Relation |
|-------|----------|
| [soul](../soul/) | Host continuity body (`minds[]`) |
| [character](../character/) | Directory that hosts soul/minds |
| [society-of-mind](../society-of-mind/) | Agents, competition, K-lines, B-brain, censors |
| [mind-mirror](../mind-mirror/) | One organelle schema (Leary Circumplex) |
| [persona](../persona/) | Costume on a body — not a mind |
| [prototype](../prototype/) | Clone and change |
| [robot](../robot/) | Robot souls; remote-control mind stub |

## Replacement (ZombieSims)

```yaml
# before
soul:
  minds: [minds/human/, minds/my-angel/]

# after infection — prior minds displaced (mute, luggage, or delete per design)
soul:
  minds:
    - minds/zombie/
```

Soul persists. Agency list is rewritten.

## Remote-control stub

```yaml
minds/remote-control-stub/:
  kind: stub
  bridge: pilot://other-soul/minds/operator/   # or player channel
```

## Well vs cup

```yaml
# Pure well (not personal) — name activates latent prototype
parents:
  - "biblical Jesus"

# Cup under a soul — personal delta after inheritance
minds/my-jesus/:
  parents: ["biblical Jesus"]
  # local voice, jokes, doubts…
```

## Organelle

```yaml
minds/stardew/:
  organelle: stardew
  schema: ...   # game DNA
  # DOWNLOAD / play / UPLIFT — only this subtree evolves
```

**Import How…** — mapping + projection at the membrane (player-in-the-middle).

## Shoulders

Two minds, one soul:

| Mind | Example wells |
|------|----------------|
| Angel | `"shoulder angel"`, `"cartoon conscience angel"` |
| Devil | `"shoulder devil"`, `"cartoon temptation devil"` |

May argue over a **bridge**. Soul chooses (or mutes).

## Two architectures (same wells)

| Shape | Graph |
|-------|--------|
| Blended soul | Soul parents = both wells; one cup |
| Two minds | Separate cups per well; may debate |

Worked examples (Jesus Mouse / Duckmouse): Soul City manifesto
[`examples/adventure-4/SOUL-MODEL.md`](../../examples/adventure-4/SOUL-MODEL.md)

## Methods

| Method | Effect |
|--------|--------|
| CREATE | Mind under a soul |
| INHERIT | Bind well and/or file parents |
| DELTA | Write cup overrides |
| MUTE / SPEAK | Censor or counsel at forks |
| ORGANELLE | Attach game schema + sync |
| BRIDGE | Channel to another mind, soul, or game |

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [INDEX.yml](../INDEX.yml)
