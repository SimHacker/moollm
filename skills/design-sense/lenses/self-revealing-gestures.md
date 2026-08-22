# Self-Revealing Gestures

**Class:** lens · **Attribution:** Don Hopkins (DDJ 1991; CHI'88 lineage); Bill Buxton & Gordon Kurtenbach (marking menus)

> **Every selection rehearses the expert stroke.**

Gestures you can't see can't be learned — Graffiti made you study a chart; most
gesture recognizers still do. The fix is structural, not instructional: show all
options radially, so the novice reads labels while the physical motion they make
*is* the expert gesture. Buxton called the general principle the collapsed gulf
between novice and expert; in pie menus it's mouse-ahead by rehearsal — novice path
and expert path are the same stroke at different speeds, so mastery is a byproduct
of use rather than a separate curriculum.

This is the pedagogical half of a pair. The performance half is
[mark-ahead-suppression](mark-ahead-suppression.md): once the stroke completes
before display latency, the menu never appears at all. Self-reveal for learning;
suppress for mastery. Together they make one mechanism serve both ends of the
skill curve with no mode switch.

**Go deeper:**
[Gesture Space (Don Hopkins, Medium)](https://medium.com/@donhopkins/gesture-space-842e3cdc7102) —
the whole argument, self-revealing vs Graffiti ·
[The Design and Implementation of Pie Menus (Dr. Dobb's, Dec 1991)](http://www.donhopkins.com/drupal/node/98) ·
[Wikipedia: Pie menu](https://en.wikipedia.org/wiki/Pie_menu) ·
[Wikipedia: Marking menu](https://en.wikipedia.org/wiki/Marking_menu) —
Kurtenbach & Buxton's studies quantified the novice→expert transfer

**Sources:**
[wwsff don-hopkins/gesture-space.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/gesture-space.md) ·
[wwsff don-hopkins/sources/ddj-1991-design-implementation-pie-menus.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/ddj-1991-design-implementation-pie-menus.md) ·
[MicropolisCore documentation/designs/gesture-space-and-pie-menus.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/gesture-space-and-pie-menus.md) ·
[wwsff repo-shows/gesture-space-self-revealing-ui/](https://github.com/SimHacker/WillWrightShowForFood/tree/main/repo-shows/gesture-space-self-revealing-ui)

**See:** [mark-ahead-suppression](mark-ahead-suppression.md), [fitts](fitts.md),
[saturate-gesture-space](saturate-gesture-space.md), [direct-manipulation](direct-manipulation.md)
