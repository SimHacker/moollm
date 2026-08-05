# Maurice's back room: Create-A-Sim as a navigable department store

The [adventure-4 coatroom](../../examples/adventure-4/coatroom/README.md) is already The
Sims' Create-a-Sim as a room — Maurice the Magnificent (🪵💅✨), the Leary
[Mind Mirror](../../examples/adventure-4/coatroom/mirror.yml), infinite costume racks,
[personas](../../examples/adventure-4/personas/) as wearable masks, saved looks as cards.
But it is one flat room with a command list. This design opens the door **behind
Maurice's counter**: the liminal back-room space, modeled as a department store you walk
through — rooms and sub-rooms for introspecting and editing your character, persona,
soul, and mind, using every palace mechanic in this pack.

CAS was always secretly a store; we just add the floor plan.

## The floor plan

```
coatroom/                       the shopfront (existing) — Maurice at the counter
  back-room/                    the liminal space: staff only, except you're always staff here
    wardrobe/                   appearance — costume racks by category, sub-rooms per era
      historical/ fantastical/ professional/ absurdist/
    persona-boutique/           masks — try personalities ON TOP of yourself
    mind-salon/                 the Mind Mirror's own room — Leary planes as fitting alcoves
      bio-energy/ emotional/ mental/ social/
    soul-atelier/               core identity: name, pronouns, backstory, CHARACTER.yml itself
    memory-attic/               saved looks, session history, former incarnations
    fitting-rooms/              sandboxed try-on — nothing committed yet
    tailor-bench/               raw alterations — edit the YAML directly, Maurice supervises
    returns-desk/               RESTORE-MIND, undo, "it looked different in the store"
    checkout/                   the commit counter
    service-entrance/           the NPC factory loading dock — dispatch new characters
```

## Every pack mechanic, applied to yourself

- **Doors fill parameters** ([MEMORY-PALACE-PIE-MENUS](MEMORY-PALACE-PIE-MENUS.md)): the
  store root binds `subject: you`; each department you enter narrows what's being edited.
  Walking `back-room/ → mind-salon/ → emotional/` is selecting a record, a facet, a
  plane — no property-sheet dialog, just floors and aisles.
- **Path scope carries the edits** — the URL is the edit form:
  `coatroom/back-room/mind-salon/emotional/?confident=5&cautious=3`. Root-room defaults
  are your current profile; the query string records only deviations. `EDIT-MIND make me
  braver` is a door that writes those bindings for you.
- **Fitting rooms are transactions**: everything you try binds into path scope — visible
  in the mirror, worn in the aisles — but nothing touches `CHARACTER.yml` until you walk
  through **checkout**, which is a git commit (with Maurice writing the commit message:
  *"honey, we made you STUNNING — confident 3→5"*). The back button is putting it back on
  the rack; the returns desk is `git revert` with better customer service.
- **Door rituals guard the deep rooms**: the soul-atelier wants a key (it edits *your own
  file only* — consent is a capability, not a warning dialog); the tailor-bench knocks
  first (raw YAML editing is supervised); the service-entrance is a whole different
  ritual because NPC creation ships someone *else* out the dock.
- **Wumpus sensing through doors**: Maurice sniffs one hop — *"I smell an under-confident
  adventurer!"* — and department doors waft their GLYPHS tails (🚪…🎭, 🚪…🧠, 🚪…📜) so you
  can smell the persona boutique from the wardrobe.
- **Trains of thought publish makeovers** ([K-PYRAMID-ATTENTION-MAPS](K-PYRAMID-ATTENTION-MAPS.md)):
  a makeover session is a walked path — save it as an album and it replays as
  before/after with every department stop; share it and a friend's browser walks the same
  aisles over *their* character. Comment trees and votes on looks are the Exchange,
  reborn.
- **Set-contrastive labels**: the department doors get their LABELs and GLYPHS summarized
  as a set, so wardrobe/boutique/salon/atelier stay unambiguous on the pie menu compass.

## Why a store and not a form

The Sims CAS is a great screen but a *modal* one: you configure, then you play. The
department store is **non-modal identity editing** — the back room is just rooms, so you
can duck in mid-adventure, adjust one plane in the mind-salon, and walk out the shortcut
door to the pub. Character editing gets the same navigation, history, undo, sharing, and
publication machinery as everything else in the palace, because it *is* everything else
in the palace: the subject just happens to be you.

The existing coatroom already knows this is the point — `CHANGE-MY-FILE-NAME` documents
that *"in MOOLLM, you ARE your file. The filesystem IS the world."* The department store
makes the corollary spatial: **editing yourself is walking through yourself.** The
mind-mirror skill's [HALLS-AND-ROOMS](../../skills/mind-mirror/HALLS-AND-ROOMS.md)
already renders psyche as architecture; this is its retail wing.

## Cast

| Role | Object |
|------|--------|
| Floor manager, consultant, hype | [Maurice](../../examples/adventure-4/characters/fictional/maurice/) — one hand on cocked hip, clipboard held, energy STUNNING |
| The honest mirror | [mirror.yml](../../examples/adventure-4/coatroom/mirror.yml) — shows costume AND soul, natural language, no sliders |
| Inventory | [costume-racks.yml](../../examples/adventure-4/coatroom/costume-racks.yml) — infinite, describable-is-wearable |
| The masks | [personas/](../../examples/adventure-4/personas/) — modifiers, not characters; Don-wearing-Ashford ≠ Bumblewick-wearing-Ashford |

↑ [design pack README](README.md) · [MEMORY-PALACE-PIE-MENUS](MEMORY-PALACE-PIE-MENUS.md) ·
[K-PYRAMID-ATTENTION-MAPS](K-PYRAMID-ATTENTION-MAPS.md) ·
[coatroom](../../examples/adventure-4/coatroom/README.md) ·
[mind-mirror](../../skills/mind-mirror/) · [incarnation](../../skills/incarnation/) ·
[character](../../skills/character/)
