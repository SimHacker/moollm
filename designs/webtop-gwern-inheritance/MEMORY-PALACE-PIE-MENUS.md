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

## Path scope: the history stack is a dynamic scope

Moving around the map does double duty: every step adds to the browser back/next stack
**and adds a frame to your path scope** — a dynamic scope accumulated along the walk.
Each room can define any variables it wants, **overriding** bindings from rooms earlier
on the path; the nearest binding wins. Back pops a frame (bindings unwind); forward
re-pushes it. The two inheritance relations now have clean computer-science names:

| Relation | Scoping | Answers |
|----------|---------|---------|
| Declared door inheritance | lexical / prototype chain | "what kind of room is this?" — stable context |
| Path scope | dynamic scope | "how did you get here, what are you carrying?" — journey state |

Doors tell you what the room *is*; the path tells you what you've *done*. Filled-in door
parameters are just bindings in path scope, which is why navigation-as-form-filling
falls out for free.

### Kitchen-sink namespacing

The path scope is deliberately a kitchen sink — every game, character, and skill throws
its state in — kept sane by **keys that carry their own hierarchy**, same big-endian
discipline as GLYPHS and yaml-jazz naming:

```yaml
# dotted sub-objects…
wumpus.arrows: 3
wumpus.smell: faint
lamp.fuel: 40%

# …or big-endian paths as keys
game/wumpus/arrows: 3
inventory/keys/vault: true
ui/theme: dark
```

Prefix is namespace: `wumpus.*` belongs to Snorax, who reads and writes only his own
subtree, so two games can haunt the same palace without collision (the grue and the
wumpus share your scope, not their variables). Prefixes are queryable and truncatable —
`game/` sweeps up all game state for a save, exactly as a GLYPHS prefix coarsens an
icon. A room overrides by rebinding the key; leaving on the back button restores what
was shadowed. Dynamic game state at any scale lives here — from `wumpus.smell: faint`
to a whole simulation checkpoint keyed under its path.

### The wire format is already in the browser

The browser path is a list of URLs, and each URL's **`?query=args` are that frame's
bindings** — the form fields you filled at the door, or root-room defaults you're
overriding. The scope stack needs no invented serialization; it is the history itself:

```
/palace/                                      root room defaults: lamp.fuel=100, theme=light
/palace/maze/?lamp.fuel=40                    a binding overridden en route
/palace/maze/room-e/?wumpus.arrows=2&wumpus.smell=strong
```

The URL path locates the room (lexical: which room, which doors); the query string
carries the dynamic bindings (what you chose, what you spent). Big-endian keys pass
through unchanged (`?game/wumpus/arrows=2` or `?wumpus.arrows=2`). Consequences:

- **Deep links carry their journey** — share a URL trail and the recipient replays your
  scope, not just your location; bookmark = frozen frame.
- **REST honesty** — no hidden session state; what the frame binds is what the URL says.
  Copy-paste debugging of game state is reading the address bar.
- **Defaults live in the room, overrides live in the URL** — the room's YAML declares the
  form and its defaults; the query string records only deviations, so URLs stay short on
  the beaten path and verbose exactly where you did something interesting.
- **Ritual exceptions** — secrets (passwords, keys as capabilities) bind into session
  scope, not the URL; the URL records *that* the vault door opened, never the password
  that opened it.

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

## Wumpus: sensing through doors

Hunt the Wumpus is the founding game of **door-graph sensing**: you never see into the
next room, but its hazards leak one hop through the doors — *"bats nearby!"*, *"I feel a
draft!"*, *"I smell a wumpus!"*. That is the palace's ambient-awareness mechanism, already
designed in 1973: adjacent rooms advertise through their doors, with one-hop falloff.
A webtop room should waft the same hints — the door's GLYPHS tail carrying the scent of
what's behind it (🚪…🦇 / 🚪…🕳️ / 🚪…👃), popups previewing one hop, never more. Sniffing
is cheaper than walking; peripheral attention at weight ≈ 0.1 is a draft under the door.

The living proof is MOOLLM's
[wumpus-snorax character](../../examples/adventure-4/characters/fictional/wumpus-snorax/)
(Snorax the Patient, `👃🦏💤🏹💀🎲`): **the character IS the game.** The directory
contains the complete rules ([GAME.yml](../../examples/adventure-4/characters/fictional/wumpus-snorax/GAME.yml)),
the [original 1973 BASIC source](../../examples/adventure-4/characters/fictional/wumpus-snorax/sources/wumpus1-yob.bas),
the canonical [DODECAHEDRON.yml](../../examples/adventure-4/characters/fictional/wumpus-snorax/DODECAHEDRON.yml)
topology (20 caves, Gregory Yob's favorite solid), the hazards (pits, bats), and
per-topology instance files. Drop the character into **any existing room network** and he
plays there — the [adventure-4 maze](../../examples/adventure-4/maze/) instance runs on
maze topology, not the dodecahedron, and the instance file just tracks game state for
that network.

Topology generation is the [room skill](../../skills/room/)'s job, not Wumpus's: its
`GENERATE` method takes a pattern (maze, dungeon, building, neighborhood, tree) or a
topology description, so you can point it at the official Wumpus dodecahedron, the
**ARPANET IMP map**, or your own adventure map described in JSON/YAML, and it
instantiates all the linked-up rooms dynamically. Game character and floor plan are
orthogonal: the palace supplies rooms and doors; the character supplies rules and
hazards; the doors supply the sniffing.

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
   back unwinds one frame of path scope (bindings and parameters together).
5. Path scope = ordered list of per-room binding maps; lookup walks it nearest-first;
   keys namespaced big-endian (dots or slashes) so games/characters/skills own subtrees.
6. K-line capture: the walked path with parameters is appended to the attention tree, so
   saved views replay journeys, not just destinations.

↑ [design pack README](README.md) · [K-PYRAMID-ATTENTION-MAPS](K-PYRAMID-ATTENTION-MAPS.md) ·
[HOME-AUTOMATION-MEMORY-PALACE](../HOME-AUTOMATION-MEMORY-PALACE.md) ·
[object-system](../object-system/README.md) ·
[pie-menus-window-management](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/sources/articles/pie-menus-window-management.md)
