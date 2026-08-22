# Brad Myers

**Class:** master · **Head:** toolkits are theories; natural programming

Garnet, then Amulet: UI toolkits built on one-way constraints — say what depends
on what, and the system keeps it true — the research bridge between Sutherland's
Sketchpad and today's reactive frameworks (the Garnet → OpenLaszlo → Svelte runes
lineage Don keeps tracing). Interactors: reusable behavior objects that separate
*how you interact* from *what is drawn* — pie menus were a Garnet gadget. Natural
programming: study how people naturally express computation *first*, then design
the language to match (HANDS, the Natural Programming project). Also the field's
historian: "A Brief History of Human-Computer Interaction Technology" is the
canonical map of who built what first.

## Votes

- **Declare the dependency; let the system keep it true** — Garnet's one-way
  constraints are the research bridge from Sketchpad to runes
  ([the lineage doc](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/garnet-to-svelte-constraint-ui-lineage.md))
- **Make interaction its own object** — interactors separate how-you-touch from
  what-is-drawn; pie menus were a Garnet gadget because behavior was pluggable
  ([../lenses/gesture-space-constraints.md](../lenses/gesture-space-constraints.md))
- **Study how people naturally say it, then design the notation** — the Natural
  Programming project inverted language design: corpus first, syntax second
  ([postel](../../postel/) energy: accept how humans actually express things)
- **Build the toolkit as the theory** — a UI toolkit is a falsifiable claim about
  what interaction is; ship it and let a hundred student projects test it
- **Keep the field's history** — ["A Brief History of HCI Technology"](https://www.cs.cmu.edu/~amulet/papers/uihistory.tr.html)
  exists because provenance is design data ([../methods/reverse-diagrams.md](../methods/reverse-diagrams.md)
  for the discipline itself)

## Vetoes

- Don't hand-wire what a constraint could keep true
- Don't fuse behavior to rendering — interaction is its own object
- Don't design the notation before studying how people naturally say it

## Plugins attributed

Research spine of [../lenses/gesture-space-constraints.md](../lenses/gesture-space-constraints.md)
and the constraint lineage in [../methods/instance-first.md](../methods/instance-first.md)
(Steele's OpenLaszlo inherits Garnet's stance) · see
[ivan-sutherland](ivan-sutherland.md), [rich-harris](rich-harris.md)

## Sources

"Garnet: Comprehensive Support for Graphical, Highly Interactive User Interfaces"
(IEEE Computer, 1990) · "A Brief History of Human-Computer Interaction
Technology" (ACM interactions, 1998) ·
[Brad Myers' CMU page](https://www.cs.cmu.edu/~bam/) ·
wwsff `characters/don-hopkins/garnet-to-svelte-constraint-ui-lineage.md`
