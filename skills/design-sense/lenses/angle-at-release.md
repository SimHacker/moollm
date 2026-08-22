# Angle at Release

**Class:** lens · **Attribution:** Don Hopkins (pie menu corpus; HN Kando commentary)

> **Commit on the line, not the path.**

A pie menu commits to the item indicated by the *straight line from press point
to release point* — never by the path the pointer wandered along the way. That
single decision buys the whole interaction vocabulary: browse by moving around
the ring (nothing commits), preview before releasing, reselect by moving again,
cancel by returning to center — all without a cancel button, and all impossible
if the recognizer scores the journey instead of the endpoints. Path-dependent
gesture recognition is fuzzy and unforgiving: one tremor and you've "drawn"
something. Endpoint geometry is exact and calm: the user can wander, reconsider,
and still land precisely where they let go.

The general lens: **let intent be the final state, not the trajectory.** Drag
targets that commit on drop, not on hover-crossing; sliders that read release
position, not flick speed ([no-spurious-velocity](no-spurious-velocity.md));
confirmation by where you end, not how you got there. Recognizers that judge
trajectories punish hesitation — which is punishing thought.

**Go deeper:**
[The Design and Implementation of Pie Menus (DDJ 1991)](https://donhopkins.medium.com/the-design-and-implementation-of-pie-menus-d54c02de5079) ·
[Gesture Space (Medium)](https://medium.com/@donhopkins/gesture-space-842e3cdc7102)

**Sources:**
[MicropolisCore documentation/designs/gesture-space-and-pie-menus.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/gesture-space-and-pie-menus.md)

**See:** [saturate-gesture-space](saturate-gesture-space.md) ·
[no-spurious-velocity](no-spurious-velocity.md) — the same respect for the
user's endpoints, applied to time · [mark-ahead-suppression](mark-ahead-suppression.md) ·
[../masters/don-hopkins.md](../masters/don-hopkins.md)
