# Gesture Space Constraints

**Class:** lens · **Attribution:** Don Hopkins (*Gesture Space*; Pantomime)

> **Constraints, not recognizers.**

Multitouch is not "a mouse with extra buttons." It is maintaining geometric
constraints between finger locations on glass and locations in the modeled world —
pan, zoom, and rotate together, continuously, through the messy roll between 1-,
2-, and N-finger modes as fingers lift in arbitrary order.

The user model is correspondence: where each finger touched the map should stay
under that finger for the whole gesture. The failure ladder makes the lens concrete:


| Approach                | What breaks                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| Ideal                   | pan + zoom + rotate; correspondence maintained                                                  |
| Google Maps (no rotate) | projects gesture space onto pan+zoom; the map slides out from under your fingers when you twist |
| Bad apps                | lock into zoom OR pan mid-gesture; can't combine or switch                                      |


Discrete recognizers (tap, pinch, rotation, swipe, pan, long-press) are not easily
composable into one integrated tracker — they classify and then *lock*, which is
the opposite of a maintained constraint. Well-written apps end up writing the
special-purpose state machine the recognizer was supposed to replace.

**Go deeper:**
[Gesture Space (Don Hopkins, Medium)](https://medium.com/@donhopkins/gesture-space-842e3cdc7102) — the primary essay ·
[Pantomime multitouch demo](https://www.youtube.com/watch?v=T43b5ywnYpo) — one finger paddles,
two fingers steer, inertial flick on release

**Sources:**
[wwsff don-hopkins/gesture-space.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/gesture-space.md) ·
[wwsff repo-shows/gesture-space-self-revealing-ui/](https://github.com/SimHacker/WillWrightShowForFood/tree/main/repo-shows/gesture-space-self-revealing-ui)

**See:** [saturate-gesture-space](saturate-gesture-space.md), [no-spurious-velocity](no-spurious-velocity.md)
(Pantomime's inertia is *earned* velocity — measured at release, not invented after it),
[direct-manipulation](direct-manipulation.md)