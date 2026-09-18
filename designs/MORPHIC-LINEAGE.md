# Morphic Lineage — everything that ran on Morphic, rebuilt it, or grew out of it

Morphic is the one UI framework that keeps getting reimplemented by the people who
wrote it the first time. Thirty years, two Smalltalk rewrites, two independent
JavaScript reimplementations, one blocks language that swallowed it whole, and a
couple of Common Lisp attempts nobody finished.

This is the family tree, with who did what and where the code is.

---

## The original — Self

**Morphic** was designed and written by **Randall B. Smith** and **John Maloney** for
**Self** at Sun Microsystems Laboratories, shipping in Self 4.0.

- Maloney & Smith, *Directness and Liveness in the Morphic User Interface Construction
  Environment*, [UIST '95](https://dl.acm.org/doi/10.1145/215585.215636), pp. 21–28
- Maloney, *Morphic: The Self User Interface Framework*, Self 4.0 release documentation
- Still documented: [Self Handbook ch. 7](https://handbook.selflanguage.org/2017.1/morphic.html)

Self's Morphic is not a class hierarchy. Shared behavior lives in **traits objects**,
structure lives in **prototypes**, instances delegate through `parent*` slots, and new
morph types are made by **copy-down** from a differential prototype. You build a morph
by copying one, tweaking it, and factoring the shared parts out afterward — bottom-up,
which is the whole point.

The layer was built over X11 but written to be portable. Maloney, in the original docs,
floats the idea of a PostScript implementation of the Morphic graphics interface so
morphs could render themselves on paper.

### What "Morphic" actually names

These are the parts that either travel to a descendant or conspicuously don't:

| Mechanism | What it does |
|---|---|
| **Morph tree** | Every visible thing is an object; submorphs nest; z-order is the child list |
| **World** | The root morph; a display is just a morph that contains everything |
| **Hand** | The cursor is a morph that picks things up and carries them, so drag-and-drop is containment |
| **Halos** | Direct-manipulation handles that appear around any object — rotate, resize, duplicate, inspect — on the object itself, not in a property sheet |
| **Stepping** | Per-morph `step` at a declared rate; concurrency illusion on one thread |
| **Damage tracking** | Dirty rectangles; only the broken region is redrawn |
| **No editor mode** | There is no separate editor because there is no separate editor — you restructure the running thing |
| **Template peel-off** | A palette item you drag copies itself (`fullCopy`, `isTemplate`) instead of moving |

Halos predate Morphic: Kay attributes them to **Ted Kaehler at PARC, ca. 1973–74**
(private email to Don; not cleared for quotation).

---

## Branch 1 — Squeak Morphic

**John Maloney** instigated the Squeak implementation; **Dan Ingalls** worked with him to
get it running on Squeak's BitBlt graphics kernel, then wrote the compatibility package
that let all the old **MVC** programming tools run inside Morphic, plus polygons, curves,
`TransformationMorph` (via WarpBlt), and the run-around text package. Morphic has been in
Squeak since **1.22**. ([History of Morphic](https://wiki.squeak.org/squeak/2139))

Everything in this table runs on Squeak's Morphic rather than reimplementing it:

| System | Who | Note |
|---|---|---|
| **Etoys / Squeakland / OLPC** | Kay's group; Ohshima, Freudenberg, Kaehler, Raab | Morphic with a scripting layer aimed at children; shipped on the XO laptop |
| **Scratch 1.0–1.4** | Maloney at MIT Media Lab | Written in Squeak Morphic by Morphic's own author. The line ends at 1.4 — Scratch 2.0 went to Flash, 3.0 to JS/Blockly |
| **Scratch 1.4 forks** | various | BYOB 3.x (Harvey & Mönig), S4A / Scratch for Arduino (Citilab, Romagosa), Panther, Physical Etoys |
| **Newspeak's Brazil → Hopscotch** | Gilad Bracha, Vassili Bykov, Peter Ahe, Ryan Macnak | Newspeak was hosted in Squeak; Brazil's *initial and for a while only* binding was Morphic, with Hopscotch composed on top. A Win32 native binding came later, and current Newspeak targets web/Wasm — Morphic was a backend they grew out of. [Hopscotch paper](https://scg.unibe.ch/assets/download/wasdett/wasdett2008-paper03.pdf) · [platform doc](https://bracha.org/newspeak.pdf) |
| **Pharo** | Pharo board (forked Squeak, 2008) | Carried Morphic forward for a decade, now migrating to **Bloc/Brick** + Spec; Glamorous Toolkit is Bloc-based. Pharo-Morphic apps include DrGeo |
| **SqueakJS** | Vanessa Freudenberg | A JS **virtual machine**, not a Morphic port — it runs the real Squeak image, so unmodified Morphic runs in a browser. See [vanessa-freudenberg-philosophy.md](./vanessa-freudenberg-philosophy.md) |

---

## Branch 2 — rewritten inside Smalltalk

### Tweak — Andreas Raab, from 2001

Not an application of Morphic but a **replacement** for it, and the sharpest published
critique of it:

> The base idea behind Tweak is simple: Combine the best of Morphic with the best of MVC.
> Morphic is a wonderful architecture as far as direct manipulation is involved but it's a
> terrible architecture to build reusable systems. Morphic simply doesn't have any
> abstractions and that makes it very hard to build re-usable and flexible components.
> — [interview](http://squeak.pbworks.com/w/page/10713943/interview)

Tweak brought the viewing architecture back, kept prototype scripting and eToys ticking
semantics, and bootstrapped its entire UI as scripted objects (viewers, menus, halos
included). Its scripting architecture became Croquet's foundation.
([Squeak wiki](https://wiki.squeak.org/squeak/3867))

Systems on Tweak: **Croquet**, **Sophie 1** (Bob Stein's multimedia e-book authoring),
**Qwaq Forums → Teleplace → OpenQwaq**, **Open Cobalt**, **3D ICC's Immersive Terf**, and
an experimental Tweak-based **Etoys**.
([Wikipedia](https://en.wikipedia.org/wiki/Tweak_programming_environment))

### Cuis — Juan Vuletich, from 2004

Vuletich decided a zoomable, scalable GUI required **abandoning back-compatibility with
Squeak's Morphic entirely**, and diverged from Squeak 3.7 in September 2004. Three years
of study produced **Morphic 3**: floating-point local coordinates, vector graphics, and
high-quality rasterization, plus LightWidgets and a VectorGraphics canvas and engine.
([Cuis history](https://github.com/Cuis-Smalltalk/Cuis-Smalltalk-Dev/blob/master/Documentation/CuisHistory.md))

---

## Branch 3 — JavaScript, the Ingalls line

**Lively Kernel** (Dan Ingalls, Sun Labs, ~2006–2008): Morphic as a full self-sustaining
live system in the browser — morphs, halos, serialization, scrubbing, connectors,
constraints, an IDE, a parts bin, and world persistence, all downloaded as JavaScript at
startup. ([technical overview](https://lively-kernel.org/development/media/LivelyKernel-TechnicalOverview.pdf))

Jens Mönig's verdict, in his own source: Ingalls "has also ported it to JavaScript (the
Lively Kernel), once again setting a **'Gold Standard' for self sustaining systems** which
morphic.js cannot and does not aspire to meet."

The line continues: **Lively Web** (Communications Design Group / YC Research) →
**Lively4** (HPI Potsdam — Robert Hirschfeld, Jens Lincke; web components and git) →
**lively.next** (Robert Krahn). Confidence on the exact handoffs between the last three:
moderate; the institutions are right, the dates want checking.

---

## Branch 4 — JavaScript, the Mönig line

**morphic.js** (Jens Mönig, from 2010): a single file, ~13k lines, pure Canvas, AGPL.
Explicitly *not* a port — though `fullCopy()` came over from Squeak almost literally,
comments included.

> Morphic.js is completely based on Canvas and JavaScript, it is just Morphic, nothing
> else. […] the purpose of morphic.js is to provide a malleable framework that will let me
> experiment with lively GUIs for my hobby horse, which is drag-and-drop, blocks based
> programming languages.
> — [morphic.txt](https://github.com/jmoenig/morphic.js/blob/master/morphic.txt)

That hobby horse was **BYOB4**, which became **Snap!** — bundled with morphic.js from the
first commit. Everything downstream of Snap! inherits Morphic by inheriting Snap!:
**Snap4Arduino** (Romagosa), **BeetleBlocks**, **TurtleStitch**, **NetsBlox**
(Vanderbilt, Lédeczi), **TuneScope**, and the **BJC** curriculum.

Architecture details: [snap/morphic-js.md](./snap/morphic-js.md).

---

## Branch 5 — Maloney's own next moves

Morphic's co-author kept rebuilding the same liveness in new substrates.

**GP Blocks** (John Maloney, Jens Mönig, Yoshiki Ohshima — SAP's Communications Design
Group, then HARC under Kay at YC Research): a general-purpose blocks language where
**all of GP is written in GP**, down to how bitmaps and blocks are constructed. Methods
are live: change one and the system changes immediately, with no editing mode to protect
you. That is Morphic's no-separate-editor rule promoted from the UI to the language.
([Guzdial's writeup](https://computinged.wordpress.com/2016/06/13/introducing-gp-a-general-purpose-block-language/))

**MicroBlocks** (Maloney, Bernat Romagosa, Jens Mönig): the IDE is written in GP Blocks —
source in `ide/` and `gp/runtime/` — and is gradually being migrated to JavaScript.
([smallvm](https://codeberg.org/MicroBlocks/smallvm) · [IDE notes](https://wiki.microblocks.fun/en/microblocks_ide_implementation))

So the same person wrote Morphic in Self, ported it to Squeak, wrote Scratch on it, then
wrote GP in GP, then wrote MicroBlocks' IDE in GP.

---

## Branch 6 — outside the family

Neither of these finished, both worth knowing about:

| Project | What |
|---|---|
| **MorphiCL** | "A (possibly misguided) attempt at creating a GUI for CL loosely based on Squeak/Self Morphic." CLX backend, verified only on CMUCL, LGPL. [CLiki](https://cliki.net/MorphiCL) |
| **Blocky** | David O'Toole's visual Lisp. `halo.lisp` is "generic GUI object handles, in the style of Squeak Morphic"; `prototypes.lisp` is "a custom Self-like object system." Cites Self Morphic, Scratch, BYOB and Jens' Smalltalk Elements as influences. [repo](https://github.com/ajbetteridge/blocky) |

No maintained Python, Rust or Dart Morphic turned up. Searched; if one exists it is not
findable under the name.

---

## What travels, and what dies every time

**Travels:** the morph tree, World and Hand, halos, stepping, damage rectangles, template
peel-off, and the refusal to have an editor mode. These show up in all six branches,
including the ones that claim to be replacements.

**Dies:** two things, repeatedly.

**Multiple inheritance.** Neither JavaScript reimplementation uses it, and Self's Morphic
barely did. Lively Kernel routes around it with an explicit `Trait(...)` composition layer
on top of `Object.subclass`. Snap! routes around it with Squeak-style copying —
`fullCopy`, `isTemplate` peel-off. The live feel comes from copyable morph trees and
shared behavior, not from MI.

**Abstraction for reuse.** Raab's diagnosis in 2001 was that Morphic has no abstractions,
so building reusable components is possible but brutally hard; Tweak was the fix. Vuletich
reached far enough back to break compatibility and rebuild the coordinate system. Both
rewrites are aimed at the same missing thing, from different directions.

---

## Kay's verdict on the ancestor of all this

Don asked Alan Kay about MVC versus Morphic in 2011. The reply, quoted in
[HN 8841428](https://news.ycombinator.com/item?id=8841428):

> Things seem to hang on in computing just because they work a little bit.
>
> MVC was originally done at PARC almost 40 years ago. The good part was philosophical —
> the idea to adapt the notion of "cameras" and "worlds" in the original 3D graphics stuff
> I participated in at Utah 45 years ago. The bad part of MVC was how we implemented it —
> much too much machinery, etc.
>
> […] I like to do views as "watchers" which do not affect what they are viewing. […]
> Similarly, I like to also use "watchers" (context sensitive to the views) to catch needed
> inputs. We have never done a really satisfactory automatic inverter for dealing with the
> loss of "dimensions" that happen when a view is made.

The unsolved automatic inverter is the same hole Tweak and Morphic 3 were both digging
toward. Full thread digest:
[WWSFF hn-mvc-morphic-watchers-2015.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/alan-kay/media/discussions/hn-mvc-morphic-watchers-2015.md).

Don's compact version of this lineage, posted to the Squeak 6.1 thread:
[HN 49242653](https://news.ycombinator.com/item?id=49242653).

---

## Related

- [snap/morphic-js.md](./snap/morphic-js.md) — morphic.js internals: kernel, event model, dev mode, inertial scroll
- [snap/gp-alan-kay-lineage.md](./snap/gp-alan-kay-lineage.md) — GP under Kay, and Jens' path into it
- [VISUAL-PROGRAMMING-LINEAGE.md](./VISUAL-PROGRAMMING-LINEAGE.md) — the wider notation lineage this sits inside
- [object-system/SELF-AND-MOOLLM.md](./object-system/SELF-AND-MOOLLM.md) — Self's prototypes and traits as MOOLLM's object model
- [INTERFACE-TO-AGENCY.md](./INTERFACE-TO-AGENCY.md) — direct manipulation versus agents, the argument Morphic is evidence in
