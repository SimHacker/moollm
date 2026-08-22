# Foveation

**Class:** lens · **Attribution:** David Ungar, critiquing Don Hopkins' Unity3D pie menus

> **Motion is a foveation summons. Only send it where you want the eye.**

What you perceive as sight is a reconstructed illusion: the brain composites a
stable scene from a tiny high-resolution fovea plus a blurry, motion-sensitive
periphery, stitched together by saccades. We evolved as animals frightened by
visual motion — the things that moved in the underbrush were the things that
mattered — so peripheral movement is a hardware interrupt that yanks the eye
toward it whether the interface meant to or not.

The design consequences:

- **Spend the animation budget on the selected thing.** Bring the mountain to
  Muhammad: slide the active label to the pointer and keep it there. Motion toward
  the point of attention confirms; motion anywhere else steals.
- **Make deselection quiet.** A slow ramping blur and fade, dimming gradually enough
  to stay under the periphery's motion-detection threshold — a state change, not a
  show. Dramatic exits don't clear the stage; they steal the scene. Animate a dozen
  rejected slices collapsing inward and you fire a dozen interrupts, all pointed
  away from the one thing the user chose.
- **Violations can be signposts.** Deliberate center-stage motion that travels the
  selection vector teaches rather than distracts — but it must be *authored*, not
  incidental.

**Exhibits:** The Sims popup head (`PopupHead.cpp` — "Shimmer the head a little bit
to make it noticeable"): a deliberate violation that works, because the head's turn
sends the eye along the exact vector of your selection from where it already is.
`RenderRoundShadow`: accidental foveation hygiene — a static, softly tapered
desaturating scrim removes the periphery's color and contrast without a single
moving pixel. The head is the show; the shadow is the stage going dark.

**Go deeper:**
[Wikipedia: Fovea centralis](https://en.wikipedia.org/wiki/Fovea_centralis) ·
[Wikipedia: Saccade](https://en.wikipedia.org/wiki/Saccade) ·
[Wikipedia: Foveated rendering](https://en.wikipedia.org/wiki/Foveated_rendering)
(the GPU world rediscovering the same budget)

**Sources:**
[wwsff david-ungar/fitts-and-foveation.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/fitts-and-foveation.md)
(the founding conversation) ·
[MicropolisCore popup-head-design-notes.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/vitamoo/popup-head-design-notes.md)
(Knuth-style design archaeology — shipped vs `#if 0` fossils, no code) ·
[Unity3D Pie Menu Demo](https://www.youtube.com/watch?v=sMN1LQ7qx9g)
(the critiqued artifact — label-to-cursor at 0:49, webcam head at 1:37) ·
[MicropolisCore documentation/designs/virtual-pointer-and-pie-cursors.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/virtual-pointer-and-pie-cursors.md) §6

**See:** [fitts](fitts.md), [stage-magic](stage-magic.md),
[no-spurious-velocity](no-spurious-velocity.md)
