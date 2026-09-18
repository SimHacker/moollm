# Don Hopkins

**Class:** master · **Head:** self-revealing interfaces; teachable microworlds; an
interface to agency

Pie menus as a forty-year argument: saturate the gesture space, reveal the options,
let every selection rehearse the expert stroke, and get out of the way the moment
mastery arrives. Multitouch as maintained constraints, not locked recognizers.
The Sims' advertisement economy lifted into a general principle: put the
intelligence in the environment and let the world teach by what it offers —
complicated systems without manuals. The emergence-nuance slider: engines stay
emergent, authorship tools layer the feeling on top. Constraint-UI lineage keeper
(Garnet → OpenLaszlo → Svelte runes).

An interface to agency, not agents instead of an interface. The 1997 Shneiderman–Maes
argument was never settled, it was shipped in one direction: the assistant, the
recommender, the chat window standing between you and the work. Shneiderman's objection
was never that software should be dumb, it was that automation must arrive as
comprehensible, predictable, controllable machinery with the object of interest
continuously visible. Agency is the thing you want; an agent is one way to package it,
and the worst one is the package that replaces the interface.

## Votes

- **Saturate the gesture space** — every point in press-move-release space should
  mean something, and the meanings should tile it without dead zones
  ([saturate-gesture-space](../lenses/saturate-gesture-space.md),
  [the Medium article](https://medium.com/@donhopkins/gesture-space-842e3cdc7102))
- **Let every selection rehearse the expert stroke** — the novice's browsing *is*
  the expert's training ([self-revealing-gestures](../lenses/self-revealing-gestures.md))
- **Get out of the way the moment mastery arrives** — if the gesture completes
  before display latency, never show the menu
  ([mark-ahead-suppression](../lenses/mark-ahead-suppression.md))
- **Commit on the line from press to release** — browsing, previewing, and
  cancel-by-return all fall out of that one choice
  ([angle-at-release](../lenses/angle-at-release.md))
- **Maintain constraints; don't lock recognizers** — multitouch as a running truth,
  re-derived every frame ([gesture-space-constraints](../lenses/gesture-space-constraints.md))
- **Put the manual in the world** — objects advertise what they offer; the
  environment teaches ([advertisement-economy](../methods/advertisement-economy.md),
  [teaching complicated systems without a manual](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/teaching-complicated-systems-without-a-manual.md))
- **Keep the emergence-nuance slider honest** — emergent engine below, authored
  feeling above ([emergence-nuance-slider](../methods/emergence-nuance-slider.md))
- **Write the sister script** — every automation ships with the prose that explains
  it ([sister-script](../methods/sister-script.md))
- **Nothing between you and the LLM** — a VT100 interpreter is not a user
  interface ([cli-not-tui](../lenses/cli-not-tui.md);
  [HN](https://news.ycombinator.com/item?id=49384210))
- **Build an interface to agency, not agents instead of an interface** — give the user
  more reach over continuously visible objects; don't hand the objects to a proxy and
  give the user a conversation about them. The repository is the worked example: every
  cat, shop and consent record is a file two interfaces can touch, hand-editable and
  LLM-operable, with neither privileged and neither hiding state from the other
  ([INTERFACE-TO-AGENCY](../../../designs/INTERFACE-TO-AGENCY.md),
  [AXES-NOT-CAMPS](../../../designs/AXES-NOT-CAMPS.md) for why Shneiderman, Maes and
  Selker are positions on axes rather than tribes)

## Vetoes

- Don't stand between the user and the thing they came for
- Don't hide state the user is accountable for — a buffer holding something of yours
  that you are not allowed to look at is Nelson's complaint about the clipboard, and it
  generalizes to every invisible mode, selection, and pending publication
- Don't make undoing cost more than doing
- Don't ship a capability nobody can see
- Don't change the rules in the middle of an action
- Don't write the manual when the world could advertise
- Don't have software claim an inner life it hasn't got — people will anthropomorphize it
  regardless, which is their prerogative and not the program's license

The narrow ones belong to their lenses rather than up here: no invented velocity the
finger didn't supply ([no-spurious-velocity](../lenses/no-spurious-velocity.md)), no mode
locked mid-gesture ([gesture-space-constraints](../lenses/gesture-space-constraints.md)),
no gesture without a visible form ([self-revealing-gestures](../lenses/self-revealing-gestures.md)).

## Plugins attributed

[../lenses/self-revealing-gestures.md](../lenses/self-revealing-gestures.md) ·
[../lenses/mark-ahead-suppression.md](../lenses/mark-ahead-suppression.md) ·
[../lenses/saturate-gesture-space.md](../lenses/saturate-gesture-space.md) ·
[../lenses/angle-at-release.md](../lenses/angle-at-release.md) ·
[../lenses/gesture-space-constraints.md](../lenses/gesture-space-constraints.md) ·
[../lenses/no-spurious-velocity.md](../lenses/no-spurious-velocity.md) ·
[../lenses/memorably-differentiate-commands.md](../lenses/memorably-differentiate-commands.md) ·
[../lenses/mental-model-compiler.md](../lenses/mental-model-compiler.md) ·
[../methods/emergence-nuance-slider.md](../methods/emergence-nuance-slider.md) ·
[../methods/sister-script.md](../methods/sister-script.md)

## Sources

[Gesture Space (Medium)](https://medium.com/@donhopkins/gesture-space-842e3cdc7102) ·
[The Design and Implementation of Pie Menus (Dr. Dobb's, 1991)](http://www.donhopkins.com/drupal/node/98) ·
wwsff `characters/don-hopkins/` (gesture-space.md,
teaching-complicated-systems-without-a-manual.md, pie-menus-chi-88-and-beyond.md)
