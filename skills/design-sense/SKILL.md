---
name: design-sense
description: Ambient design skill socket — the working designer's head. Always-on perceptual and attention constraints (lenses like Fitts' law and foveation), process constraints (methods like design-by-accretion and tuned-emergence), and borrowable designer heads (masters), organized as plugin registries. Covers user interface, interactivity, game design (especially simulation games), and software design. Never dictates visual styling. Use when designing or critiquing any interactive surface, pacing design work over time, or curing a harvested design principle into loadable form.
allowed-tools: [Read, Write, Grep, Glob]
related: [copy-that, cauldron, play-learn-lift, simulator-effect, procedural-rhetoric, k-lines]
license: MIT
tags: [design, ui, interaction, game-design, simulation, attention, ambient]
credits: "Don Hopkins; lenses and methods credited per plugin (Fitts, Ungar, Trottier, Wright, Minsky, Bogost, ...)"
---

# Design Sense 👁️

A sense is ambient, involuntary, always sampling. This skill models what a working
designer carries in their head *at all times* — not a checklist consulted at review
time, but constraints that veto and redirect while the work happens.

The founding case: David Ungar critiqued Don Hopkins' Unity3D pie menus. The menus
brought the selected label to the cursor (good — the cheapest target walks over and
stands under your gaze), but animated the *deselected* items retreating (bad —
peripheral motion is a hardware interrupt; a dozen slices collapsing fire a dozen
interrupts, all pointed away from the one thing the user chose). The takeaway wasn't
a fix; it was a permanent resident of the designer's head:

> **Motion is a foveation summons. Only send it where you want the eye.**

That principle needed a place to live. So does Fitts' law. So does Chris Trottier's
design-by-accretion. Rather than a swarm of single-law skills, one socket with
plugin registries — the copy-that shape (kernel + formats/ + house-styles/), the
cursor-mirror growth pattern (one entry point, many organs).

## Scope

User interface, interactivity, game design — simulation games are the native
genre — and software design (Self's power of simplicity, Korz's de-objectification:
design of the invisible). **Not** visual styling. This skill never tells you what
colors to use; a sense is perception and judgment, not palette.

## The registries

All plugins are Markdown — human-readable first, k-lineable names, working links
(relative in-repo, GitHub URLs cross-repo). Each registry carries its own kernel:
GLANCE.yml to scan, CARD.yml with dispatch-table advertisements, README.md for
format and norms.

- **[`lenses/`](lenses/README.md)** — 31 ways of seeing: always-on perceptual and
  attention constraints, active whenever you're looking at (or designing) a
  surface. Fitts: cost grows with distance, shrinks with size. Foveation: motion
  summons the eye. Stage magic: simple view until complex truth.
  [lenses/CARD.yml](lenses/CARD.yml) dispatches by design context.
- **[`methods/`](methods/README.md)** — 32 ways of working: constraints on
  process. Design-by-accretion: layer, accumulate, tune late. Worse-is-better:
  can you remove more? One-page designs: the doc is a poster.
  [methods/CARD.yml](methods/CARD.yml) dispatches by phase of work.
- **[`masters/`](masters/README.md)** — 59 heads to borrow. A master file gives
  you a person's **votes** (positive imperatives, linked to the plugins that cash
  them) and **vetoes** (the lines they won't cross), plus the plugins attributed
  to them. [masters/CARD.yml](masters/CARD.yml) dispatches by problem; load
  several heads for an adversarial committee.
- **[`seeds/`](seeds/README.md)** — the accretion intake. Harvested principles
  land raw in dated batch files with Planted/Todo journal sections; they
  germinate (grounded in a source, named, stated plainly, classified) and
  graduate to the registries. Sinsemilla means *without seed* — the pipeline is
  seeds in, sinsemilla out; a cured registry is seedless by definition.
  (Simsemilla being, canonically, what they smoke in The Sims.)

Two axes, one test: **lenses constrain attention while you look; methods constrain
process while you build.** A candidate that's neither may be a master trait, or
isn't ready to leave seeds.

## Protocol

1. **Designing or critiquing a surface** — load the relevant lenses first, before
   proposing anything. Lenses veto: if a proposal sends motion where you don't want
   the eye, or puts a small target far away, the lens speaks before taste does.
2. **Planning design work** — load methods. Accretion says don't top-down specify;
   tuned emergence says budget the late tuning pass now, because fun arrives last.
3. **Channeling a designer** — load the master file, then the plugins it indexes.
   Borrowing a head means adopting its vetoes, not imitating its output.
4. **Harvesting** — quotable principle found in the wild? PLANT-SEED: append it to
   seeds/ raw with source and attribution. Germination can wait; losing it can't.
5. **Germinating** — name it kebab-case, state it in 1-3 plain sentences, cite sources
   (point, don't copy), classify it, write the registry file. Gate: a seed graduates
   only if a working designer would actually keep it loaded.

## Authoring a plugin

Follow the schema in CARD.yml. Plugins are Markdown files whose anatomy is:
header (name, class, attribution, optional dispatch line pointing at a whole
moollm skill), one bold **statement** (the loadable form — it must work without
the source documents), a body with mechanism and corpus exhibits, **Go deeper**
external links (Wikipedia, founding papers, primary articles), **Sources** into
the corpus with working links, and **See** for kin. Master files replace the
statement with a **Head** paragraph and add **Votes** (do this, bulletized,
linked) and **Vetoes** (never this). The statement or head is what survives
context compression ("motion is a foveation summons"); everything else is there
for the reader who clicked through.

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[repo README](https://github.com/SimHacker/moollm/blob/main/README.md) and
[skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md).
Deep context: [README.md](README.md). Planning and harvest log:
[CAULDRON.md](CAULDRON.md).
