# design-sense 👁️

The working designer's head as an ambient skill. Not a checklist consulted at
review time — a sense: always-on constraints that veto and redirect while the
work happens. Covers user interface, interactivity, game design (simulation
games are the native genre), and software design. Never tells you what colors
to use.

> **Motion is a foveation summons. Only send it where you want the eye.**

That's the founding principle — David Ungar critiquing Don Hopkins' Unity3D pie
menus, distilled to a line a designer keeps loaded forever. This skill is the
place such lines live, organized as one socket with plugin registries, the
copy-that shape: kernel on top, registries below, everything a Markdown file
with a k-lineable name.

## Reading order

Semantic mipmap, top-down — never load a lower level without the one above:

1. [GLANCE.yml](GLANCE.yml) — is this skill relevant? (30 seconds)
2. [CARD.yml](CARD.yml) — interface: LOAD-LENSES, LOAD-METHODS, LOAD-MASTER,
   PLANT-SEED, GERMINATE; plugin schema
3. [SKILL.md](SKILL.md) — full protocol, scope, authoring guide
4. This README — deep context
5. [CAULDRON.md](CAULDRON.md) — the farming journal: naming history, harvest
   log, germination queue

## The registries

| Registry | What | Count | Scan | Dispatch | Norms |
|---|---|---|---|---|---|
| [lenses/](lenses/) | Ways of seeing — perceptual and structural constraints held while looking | 31 | [GLANCE](lenses/GLANCE.yml) | [CARD](lenses/CARD.yml) | [README](lenses/README.md) |
| [methods/](methods/) | Ways of working — repeatable procedures and process constraints | 32 | [GLANCE](methods/GLANCE.yml) | [CARD](methods/CARD.yml) | [README](methods/README.md) |
| [masters/](masters/) | Heads to borrow — one person's whole sensibility per file, with Votes and Vetoes | 59 | [GLANCE](masters/GLANCE.yml) | [CARD](masters/CARD.yml) | [README](masters/README.md) |
| [seeds/](seeds/) | Incoming harvest — dated batch files with Planted/Todo journals | 6 batches | [GLANCE](seeds/GLANCE.yml) | [CARD](seeds/CARD.yml) | [README](seeds/README.md) |

The CARDs are dispatch tables: [lenses/CARD.yml](lenses/CARD.yml) maps design
contexts to lens sets (designing a menu loads a different set than structuring
a repo), [methods/CARD.yml](methods/CARD.yml) maps phases of work to method
sets, [masters/CARD.yml](masters/CARD.yml) maps problems to people — load
several heads for an adversarial committee.

## A short tour

- **Lenses:** [fitts](lenses/fitts.md) — big, close, or it costs ·
  [foveation](lenses/foveation.md) — motion summons the eye ·
  [simulator-effect](lenses/simulator-effect.md) — imagination is free compute ·
  [masking](lenses/masking.md) — abstract character, detailed world ·
  [stage-magic](lenses/stage-magic.md) — simple view until complex truth
- **Methods:** [design-by-accretion](methods/design-by-accretion.md) — grow past
  critical mass, then tune · [tuned-emergence](methods/tuned-emergence.md) — the
  fun is earned in the late pass ·
  [one-page-designs](methods/one-page-designs.md) — the doc is a poster ·
  [worse-is-better](methods/worse-is-better.md) — can you remove more? ·
  [time-to-penis](methods/time-to-penis.md) — measure it before launch day does
- **Masters:** [will-wright](masters/will-wright.md) ·
  [david-ungar](masters/david-ungar.md) ·
  [don-hopkins](masters/don-hopkins.md) · [alan-kay](masters/alan-kay.md) ·
  [seymour-papert](masters/seymour-papert.md) — and 54 more on the
  [shelf](masters/)

## How it grows

Principles arrive raw as **seeds** (dated batch files in [seeds/](seeds/)),
get grounded in a corpus source, and **germinate** into registry plugins; the
seed journal keeps a Planted link for every graduation. Protocol:
[seeds/CARD.yml](seeds/CARD.yml); longer story: [CAULDRON.md](CAULDRON.md).
Primary corpus: the [WWSFF character files](https://github.com/SimHacker/WillWrightShowForFood),
moollm's [designs/](../../designs/) and skills, and
[MicropolisCore's design docs](https://github.com/SimHacker/MicropolisCore/tree/main/documentation/designs).

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[repo README](https://github.com/SimHacker/moollm/blob/main/README.md) and
[skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md).
Kin skills: [copy-that](../copy-that/) (same socket shape),
[cauldron](../cauldron/) (the method CAULDRON.md follows),
[adversarial-committee](../adversarial-committee/) (what a shelf of masters is
for), [simulator-effect](../simulator-effect/),
[play-learn-lift](../play-learn-lift/),
[procedural-rhetoric](../procedural-rhetoric/) (dispatched to by their lens and
method entries).
