# Reselection

*Don Hopkins · August 2026*

**Thesis:** The reversible clause of direct manipulation, applied to menu selection, is a property called *reselection* — browsing a decision before committing to it. Pie menus have it structurally; gesture recognition structurally cannot. Everything else in this essay follows from that asymmetry.

Part of the **pie-stack-views** design cluster ([README](README.md)). Critique origin: [DYE-A-TRIBE](../DYE-A-TRIBE.md).

---

## The measured result

Callahan, Hopkins, Weiser, and Shneiderman measured pie menus against linear menus at [CHI '88](https://doi.org/10.1145/57167.57182): faster, fewer errors, for fixed command sets. Kurtenbach and Buxton's **marking menus** extended the result with rehearsal: the novice pops up the menu and reads it; the expert makes the same directional stroke without waiting for the display. The novice action *is* the expert action, performed faster — a continuous path from reading to reflex, with no separate hidden expert mode.

## The reversible clause

Self-revelation dovetails with the third clause of Shneiderman's definition of direct manipulation: operations must be *reversible*, with effects immediately visible. In menu selection the reversible property is **reselection**. While a pie menu is up, the selection tracks the pointer continuously: move into a slice and it highlights, move to another and the highlight follows, return to the inactive center and nothing is selected at all. The user browses the decision before committing to it, and the commitment itself (button release) is a separate act from the exploration.

Gesture recognition cannot offer reselection. A recognized stroke is interpreted only after it is complete: there is no continuous feedback during the act, no mid-course correction, no neutral region to retreat to — only a verdict delivered afterward, with a confidence score where the highlight should have been. Recognition widens exactly the **gulf of evaluation** (Hutchins, Hollan, and Norman, 1985) that direct manipulation was defined to close.

## What pie menus inherit, lack, and add

Pie menus stand in a precise relationship to direct manipulation — aligned, not identical — and it is worth being exact about the properties.

**Inherited:** continuous representation while the menu is displayed; selection by physical pointing rather than syntax; immediate, incremental, visible feedback; reversibility as reselection and cancellation.

**Not inherited:** the object of interest. A menu is still command selection — an intermediary — rather than manipulation of the target itself, though pull-out parameters narrow the gap by letting one gesture both choose an operation and set its magnitude. (The gap can be closed entirely by promoting the menu to an object of interest; see [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md).)

**Added:** direction as a rehearsable motor dimension, and distance as *leverage* — because arc length grows with radius, moving farther from the center yields finer angular precision from the same motor accuracy. The same tolerance for error buys more resolution the farther out you go. Direct manipulation combined with a continuously, automatically scaling interface approaches this property from the other side: precision on demand, without a mode. (Pursued further in [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md).)

## Tracking hooks: the candidate channel

Reselection creates a feedback channel that recognition-based input structurally cannot have. Because the menu tracks continuously, it can expose tracking hooks at every level of granularity: highlight-change events for the *candidate* selection, but also raw pointer motion within a slice, hover dwell past a timeout, and periodic timer ticks while the menu is up. An application can respond to what the user is considering, how they are moving, and how long they have hesitated — not just what they finally committed to.

**The idea is not mine and did not originate in any of my implementations.** It came out of the MIT Media Lab — a student project in Ted Selker's orbit — demonstrating menus that timed how long the cursor lingered over each item and reported it back as interest analysis. I saw it there, and then built it.

**Which implementation, settled by the recording rather than by memory.** The dwell-prediction feature belongs to the **JavaScript pie menus**, not to the earlier NeWS or ScriptX work — and the attribution is spoken aloud in the demo, at 4:27:

> *"Now this was inspired by some research at MIT Media Labs. This is a demonstration of pie menus that try to guess what your second choice would be."*

> *"I think your favorite color is red, but I guess your second favorite color is blue — and that's based on the fact that when I popped it up, even though I selected red, I spent the most time selecting blue. So people tend to browse the pie menus like this, looking at things, and then when they find what they like they click it, but then they'll pause to consider things."*

**[JavaScript Pie Menus](https://www.youtube.com/watch?v=R5k4gJK-aWw)** — pie menus for JavaScript on Internet Explorer 5, configured in XML, rendered with dynamic HTML, using IE5 behaviors to turn raw input events into higher-level semantics. Published to YouTube 8 January 2016; the work is IE5-era, so 1999 or later.

**That resolves the chronology, and in the direction that makes the credit land.** IE5 shipped in March 1999 and Selker arrived at the Media Lab in September 1998, so the demo precedes the implementation it inspired by months rather than conflicting with it by a decade. The earlier guess that this went "possibly as far back as NeWS" was wrong and is withdrawn: NeWS and ScriptX had reselection and tracking hooks, but **the dwell-to-interest inference arrived with the JavaScript version.**

`needs-check: the student's name and the project's title, which would let this credit land on a person instead of a lab. That is the only thing still missing; the venue, the direction of influence, and the implementation are now established by Don's own recorded narration. The exact year within the IE5 window is not pinned.`

**Two details in that demo are load-bearing for the verdict layer and are easy to miss.**

First, **cancelling still writes.** At 5:16: *"I can pop up the menu, go yellow, oh no no I'll just cancel it — and now it's guessing that my favorite color is yellow, although I didn't select one."* A menu dismissed with no selection at all still produced a verdict, from attention alone. That is exactly the gesture [READ-UNREAD](../webtop/READ-UNREAD.md) needs — *linger writes, and pen-up is not required* — demonstrated on video roughly twenty-seven years before the document specifying it.

Second, **he named the application.** At 5:23: *"This was a really simple, elegant idea that I applied to pie menus, and it can be applied to a lot of other things, and used for e-commerce and art galleries or whatever."* Art galleries. Attention-as-signal pointed at looking-at-pictures, in 1999, as an aside.

This instrumentation has since shipped in my own code more than once. The OpenLaszlo Micropolis pie menus timestamp every highlight change and accumulate per-item dwell totals (`enterTime`, `exitTime`, `totalTime` in `laszlo/micropolis/classes/piemenu.lzx`), and the OLPC Python/GTK/Cairo implementation carries the identical logic (`pyMicropolis/piemenu/piemenu.py`). People point at what they are attending to; a menu positioned to watch that can notice that you *said* your favorite color was green, but your cursor spent longer on red.

## Feedback in the center and in the world

The menu's center is functional space for the candidate channel: a live display of the selected object, an icon, a preview, a small visualization, updating as the user browses. Richer still is previewing the candidate effect **in the world itself** — on the target object, before commitment — which is Shneiderman's immediately-visible-effects clause applied one step earlier than usual: visible *before* the operation, not just after. Both channels turn reselection from a safety property into an exploration instrument.

They also impose a visual-design obligation: the menu must read as an instrument layered over the world, not as part of it. The Sims drew the selected character's portrait in the pie center, and without deliberate figure-ground separation — border, shadow, contrast — that feedback reads as a giant head floating in the living room rather than as a control describing one. Popping the menu out of the scene is not decoration; it is the boundary that keeps the feedback show legible as feedback.

## The quiet configuration, and who gets to configure

The right balance between the two channels is application-specific. Where in-world preview carries the load, the strongest configuration may be the quietest: nothing in the center at all, and items drawn as a sharp, readable overlay with minimal background and chrome, so the world stays visible through the instrument.

That variability is itself a requirement on any pie menu component: the configuration space — center content, item rendering, feedback bindings, geometry — must stay open, and it must be open *to designers*. A component that can only be adapted by subclassing or wiring callbacks has made its design decisions programmer-private, which guarantees they will be made by programmers. The configuration should be declarative data that survives a round trip between a WYSIWYG editor, JSON, and a plain text editor — savable, restorable, diffable — so a designer can tune a menu the way they tune any other asset. This is an unsolved-in-general problem worth solving deliberately, and it is the same accessibility argument as direct manipulation itself, applied one level up: the tool for building interfaces should itself be directly manipulable by the people responsible for the design.

## The counter-model

Contrast stroke alphabets like Graffiti, where nothing on screen reveals the gesture, nothing tracks it while it happens, and errors give no instruction. Modern iOS is built substantially on unmarked, unreselectable gestures — which edge, how many fingers, how long to press — which is Graffiti's failure mode generalized to an operating system. The full argument about how that happened, and what the field already knew, is [Dye-a-Tribe](../DYE-A-TRIBE.md).

---

## Related

- [DYE-A-TRIBE](../DYE-A-TRIBE.md) — the critique this cluster grew out of
- [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md) — the menu as object of interest
- [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md) — zoom, the fog of war, and the Atkinstown stack
- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — the data model underneath
- [Pie menus: CHI '88 and beyond](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/pie-menus-chi-88-and-beyond.md) · [30-year retrospective](https://donhopkins.medium.com/pie-menus-a-30-year-retrospective-5bdcb24a835a)
- [Gesture space](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/gesture-space.md) — self-revealing gestures vs. stroke alphabets
