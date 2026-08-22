# Fitts

**Class:** lens · **Attribution:** Paul Fitts (1954); Bruce Tognazzini; Don Hopkins (pie menus, UMD 1988)

> **Big, close, or it costs.**

Pointing cost grows with distance and shrinks with target size — Fitts' law, the
one empirical law every interface obeys whether its designer knows it or not. The
cheapest target is the one that walks over and stands under your gaze.

Consequences worth keeping loaded:

- **Radial beats linear.** Pie menu wedges keep distance small and constant while
  width grows with radius; direction matters more than travel. The CHI'88 study
  (Callahan, Hopkins, Weiser, Shneiderman) measured pie menus 15% faster than
  linear menus with fewer errors — the law, cashed out.
- **Edges are infinite.** A target on the screen edge has infinite depth in one
  direction: you can't overshoot it. Corners are infinite in two. That's why the
  Mac menu bar beats in-window menus and why mile-high menus work.
- **The moving target trick.** Fitts assumes the target sits still; nothing forbids
  the target coming to the pointer. Sliding the selected label to the cursor makes
  its effective distance zero (see [foveation](foveation.md) for the eye's half of
  that move).

**Go deeper:**
[Wikipedia: Fitts's law](https://en.wikipedia.org/wiki/Fitts%27s_law) ·
[AskTog: A Quiz Designed to Give You Fitts](https://www.asktog.com/columns/022DesignedToGiveFitts.html) ·
[The Design and Implementation of Pie Menus (Dr. Dobb's, Dec 1991)](http://www.donhopkins.com/drupal/node/98) ·
An Empirical Comparison of Pie vs. Linear Menus (CHI'88)

**Sources:**
[MicropolisCore documentation/designs/pie-menus-fitts-law.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/pie-menus-fitts-law.md) ·
[wwsff david-ungar/fitts-and-foveation.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/fitts-and-foveation.md) ·
[wwsff repo-shows/edd-coates/pie-menus-discussion-notes.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/edd-coates/pie-menus-discussion-notes.md)
(PieCraft teaches it as gameplay)

**See:** [foveation](foveation.md) — Fitts governs where the hand can cheaply go;
foveation governs where the eye will involuntarily go. A UI literacy game should
teach both. Also [self-revealing-gestures](self-revealing-gestures.md),
[memorably-differentiate-commands](memorably-differentiate-commands.md).
