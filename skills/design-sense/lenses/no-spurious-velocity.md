# No Spurious Velocity

**Class:** lens · **Attribution:** Don Hopkins; Ron Reisman (NASA 4D trajectory-based operations framing)

> **When the finger stops, the world stops.**

When the user lifts, their intent is "stop here, now." Interfaces that
extrapolate motion past release — momentum scroll that glides past the target,
Mission Control's half-finished transitions, carousels that keep drifting —
have decoupled animation state from input state, and now the interface *lies
about where things are*: you aim at what you see, but the system acts on where
the animation will be. Reisman's air-traffic framing sharpens it: in 4D
trajectory-based operations, time is an explicit constraint, and a display that
invents velocity the vehicle doesn't have would be a safety defect, not a
transition style.

The lens is not anti-animation — it's anti-*fiction*. Animation that reports
real state change (the tile really moved) informs; animation that manufactures
motion the input never supplied (the list "settles" while you're already
re-aiming) spends the user's foveal attention on a lie
([foveation](foveation.md): motion summons the eye whether you meant it or not).
Physics is a fine metaphor exactly until it overrides intent.

**Go deeper:**
[Gesture Space (Medium)](https://medium.com/@donhopkins/gesture-space-842e3cdc7102) —
the input-state honesty argument

**Sources:**
[MicropolisCore documentation/designs/classical-hci-vs-aesthetic-ui.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/classical-hci-vs-aesthetic-ui.md) ·
[MicropolisCore documentation/designs/four-dimensional-navigation-hci.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/four-dimensional-navigation-hci.md)

**See:** [angle-at-release](angle-at-release.md) — endpoints over trajectories ·
[calm-not-invisible](calm-not-invisible.md) — the same honesty, applied to state
visibility · [foveation](foveation.md) ·
[../masters/don-hopkins.md](../masters/don-hopkins.md)
