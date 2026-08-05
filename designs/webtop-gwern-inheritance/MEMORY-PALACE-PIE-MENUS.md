# Memory palace pie menus: navigation as parameter entry, doors as reified forms

Pie menus and memory palaces are the same structure viewed from two directions, and the
webtop should implement them as one thing: **a tree of sub-rooms that inherit from the
path of parent rooms, where every move fills in a parameter.**

The 1988 seed (Don, NeWS-makers, on nested pie menu selection):

> "You remember a path through a tree of nested menus as a series of directions, sort of
> like navigating from room to room in Zork. Since menu selection is defined by direction,
> and delimited by mouse clicks, you can rapidly mouse ahead through familiar menus,
> without having to look at the screen."

That was already a memory palace: directions remembered kinesthetically, rooms nested in
rooms, muscle memory as the retrieval key. This design finishes the thought.

## Rooms inherit through their doors

The simple case: each sub-room **inherits from the (path of) parent rooms** — a
Self-style prototype chain laid out spatially. Walking into
`palace/finance/invoices/overdue/` accumulates context the way nested scopes accumulate
bindings: the child room sees everything its ancestors established and can override it.
(MOOLLM already treats directories as activation contexts — [room skill](../../skills/room/),
object-system directory-as-object — this extends that chain up the path.)

But inheriting only from the door you walked in through is **directional inheritance** —
history-dependent, one parent, fixed. The general mechanism is declarative: **the room
lists the names of the doors it inherits from.** Doors are named slots; the inherit list
marks which slots are parent slots. This is precisely Self's object model in adventure
costume:

| Self | Palace |
|------|--------|
| named slot | door |
| parent slot (`*`) | door on the room's inherit list |
| multiple inheritance | inheriting through several doors |
| **dynamic inheritance** (assignable parent slots) | a door that **dynamically selects its destination** |
| delegation (message lookup up the parents) | asking a question in a room: unanswered, it echoes through the inherited doors |

```yaml
room: overdue-invoices
doors:
  hallway:  { to: .. }                          # where you came from
  policy:   { to: /palace/finance/policy }       # shared rules live there
  season:   { to: !door-script pick-quarter }    # dynamic destination
  vault:    { to: /palace/vault, ritual: key }   # not inherited; must walk it
inherits: [hallway, policy, season]
```

Consequences:

- **Different rooms can exist behind doors** — the same doorframe can lead somewhere else
  for a different visitor, at a different time, or with a different parameter trail; the
  room's context follows the door's *current* destination.
- **Dynamic-destination doors are computed parents**: a `season` door that opens onto the
  current quarter's room re-parents the whole context each quarter with no edits to the
  room itself. (In Self, assigning a parent slot mid-execution changes an object's
  behavior; here, the door swinging to a new destination changes the room's ambience.)
- The **walked path still exists** — as history, hallway, and K-line — but it no longer
  *forces* inheritance. Where you came from and what you inherit from are separate
  relations that happen to coincide in the simple nested-directory case.

## Navigation is parameter entry

Each move from room to room **fills in a parameter**. A path through the palace is an
incrementally curried call:

```
pie: Insert → Image → From repo → diagrams/ → Page-3-Maps.png
      (verb)   (type)   (source)    (dir)        (file)
```

By the time you arrive, the "form" is complete — no dialog box ever appeared, yet every
field got filled by a spatial choice. Mouse-ahead through familiar rooms is *speaking the
whole sentence at once*: the parameters ride on muscle memory. This is the pie menu
directional-selection insight generalized: **a form is a path, and a path is a form.**

## Doors are reified forms

The transition between rooms is itself an object — a **door** — and the door is the form's
UI. A door can demand its parameters in whatever ritual fits its semantics:

| Ritual | Parameter type |
|--------|----------------|
| Just walk through | no parameters (default constructor) |
| **Insert a key** | capability / token you must already hold |
| **Knock** | request + wait; the other side decides (async permission) |
| **Say the password** | authentication secret |
| **Insert your credit card** | payment / resource commitment |
| **"How many? What kind?"** | quantity and type selection — a door that is a picker |

Doors **advertise** their rituals Sims-style: approach one and it tells you what it takes
to pass (the advertisement is the form's schema). In object-system terms a door is a
**constructor entry point**: walking through it instantiates the passage with the
parameters you supplied, and the room beyond is the constructed result. A locked door
whose key you lack renders shut — visible but unaffordable, exactly like a grayed menu
item, exactly like a Sims interaction that doesn't advertise to you.

## Every step pushes a history frame

Each step through the palace **adds a frame to the browser history**. The back button
walks you back out, room by room, unwinding parameters as it goes. This is not metaphor —
it is pushState, the same mechanism Gwern's mobile popovers use to encode their stack in
the hash (see [FRONTEND-POPUPS-WM](sources/analysis-notes/FRONTEND-POPUPS-WM.md)). Three
structures turn out to be one:

- the **browser history** (frames pushed per step),
- the **inheritance chain** (rooms inherited along the path),
- the **narrowed hallway** (the path rendered small behind you —
  [K-PYRAMID-ATTENTION-MAPS](K-PYRAMID-ATTENTION-MAPS.md)).

And the path is what a K-line records: retracing it is reactivation. A bookmarked deep
room *includes its journey* — share the URL and the recipient gets the same parameter
trail, the same hallway, the same context stack. No stray click can strand you, because
history frames make every step reversible (the EPHEMERAL PYRAMID anti-pattern's exact
antidote applied to navigation).

## Pie menus as the door picker

At each room, the pie menu is the compass rose of available doors: directions are stable
per room type (set-contrastive GLYPHS label the slices), submenus are sub-rooms, and
mouse-ahead chains doors into a gesture. Parameter-demanding doors extend the gesture the
way pull-out pie menu arguments always did — direction chooses the door, **distance or a
follow-up interaction supplies the parameter** (the 1988 posting's "which pie slice you
are in could select color, and how far out from the center you are in could select
intensity"). A credit-card door opens a payment sheet mid-gesture; a "how many" door reads
count from distance or a scroll; a password door inlines a field. The ritual interrupts
the walk only as much as its semantics require.

## Minimum viable

1. Room tree = directory tree; default inheritance down the path, overridable by the
   room's declared `inherits:` door list (Self parent slots; dynamic doors = computed
   parents).
2. Door = YAML object on the room: destination (static or door-script), ritual type,
   parameter schema, advertisement text (GLYPHS + LABEL), inheritable flag.
3. Pie menu per room generated from its doors; slice labels via set-contrastive
   menu-summarizer.
4. Every transition does pushState with the accumulated parameter trail in the URL/state;
   back unwinds one parameter.
5. K-line capture: the walked path with parameters is appended to the attention tree, so
   saved views replay journeys, not just destinations.

↑ [design pack README](README.md) · [K-PYRAMID-ATTENTION-MAPS](K-PYRAMID-ATTENTION-MAPS.md) ·
[HOME-AUTOMATION-MEMORY-PALACE](../HOME-AUTOMATION-MEMORY-PALACE.md) ·
[object-system](../object-system/README.md) ·
[pie-menus-window-management](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/articles/pie-menus-window-management.md)
