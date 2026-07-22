# Halls and Rooms — Word Pairs as Navigable Dimensions

> *"The digital models running on a computer are only compilers for the mental models users construct in their heads."* — Will Wright

Ideas doc for the mind-mirror skill. How Leary's circumplex, pie menus, simplicial
complexes, memory palaces, and latent-space vectors are the same architecture,
and what that means for co-navigable models in MOOLLM.

## The core move: a pair of words is a dimension

One word is a room — a K-line, a place you can stand. **A pair of words is a
hall**: the two rooms anchor a continuous dimension you can smoothly interpolate
along. good/evil. warm/cold. energetic/calm. goto/eval (the Church of the Eval
Genius's dimension of flow control — mileposts along that hall: `goto`, `gosub`,
`call`, closure, `eval`; walk it and you walk the history of programming
languages, from jump-to-address to interpret-the-expression, with Alonzo Church
waiting at the far end).

This is not a metaphor grafted onto Mind Mirror — it is what the property
registry in [CARD.yml](CARD.yml) already is:

- `energetic: {opposite: calm, gradient: [lethargic, energetic, wired]}` — the
  `opposite` names the room at the other end of the hall; the `gradient` words
  are **mileposts** along it.
- `plain_talk: [laid-back, peppy]` and `shrink_rap: [low-energy, hyper-manic]`
  are **parallel halls in different registers** — the same dimension walked in
  street clothes or a lab coat. Register itself is a dimension: every hall has
  a formal/vernacular hall running perpendicular to it.
- The 0–7 scale is your position in the hall. 4 is the doorwayless middle.
  Omitted = 4: if you're not somewhere in a hall, you're nowhere in it.

And it is what word embeddings already do: two anchor words define a difference
vector, and `king − man + woman ≈ queen` is walking the man/woman hall starting
from the king room. LLM latent space honors these halls natively — "say that
again, but two doors closer to `wired`" is an executable instruction. Mind
Mirror profiles are **coordinates in a hall system the model can actually
navigate**, which is why a six-property profile with jazz comments animates a
character: each value is a position, each comment is what the character sees
from that spot in the hall.

## The circumplex is a pie menu

Leary arranged each thought plane's 8 octants clockwise on a circle. That is a
**pie menu of personality**: direction = quality (which octant), distance from
center = intensity (0–7). Center = neutral 4 = the resting cursor. Opposing
pairs at 1↔5, 2↔6, 3↔7, 4↔8 are the halls, crossing at the center like streets
at an intersection.

Pie menus are the interaction dual of the circumplex: one *displays* a position
in a radial dimension system, the other *selects* one — angle picks the
dimension, drag distance picks the coordinate. Mousing out along `friendly` is
literally walking the angry/over-friendly hall. A Mind Mirror editor should BE
a pie menu per plane; Leary's 1985 circular charts were pie menus avant la
lettre, and the logistic-container skill already uses pie-menu topology for
room grids (see [logistic-container/README.md](../logistic-container/README.md)
— "Pie Menu = Street Intersection").

## Simplicial complexes: when halls have interiors

Rooms are vertices. Halls are edges (1-simplices). But three or more mutually
related words span **faces** — higher simplices with navigable interiors:

- Interpolating along a hall is moving on an edge: `0.3·calm + 0.7·energetic`.
- Interpolating *inside a triangle* is barycentric mixing of three anchors:
  `0.5·curious + 0.3·certain + 0.2·playful` is a point on the face they span —
  a mood no single hall can express.
- A thought plane's octant ring is a cycle of 8 edges; the filled disc Leary
  drew is the 2-complex it bounds. A full Mind Mirror profile is a point in the
  product of four such discs.

The complex's **skeleton** is what you walk (rooms and halls — discrete,
nameable, memorable); its **interior** is what you blend (continuous
coordinates — expressive, precise, unnameable). Both matter: the skeleton is
the memory palace, the interior is the latent space. Words are the lattice
points where the continuum condenses into something you can say. A room is
where many halls meet — `wired` sits on the calm/energetic hall, the
caffeine hall, and the First Wired Family hall, and that incidence structure
(which halls share which rooms) IS the complex.

## Mileposts: the floating-point enumerated type

Name the data structure a hall implies and you get something programming
languages keep almost inventing: an **enum you can interpolate** — ordered
named variants pinned to positions on a continuum, with lerp defined between
adjacent labels and snap defined back to the nearest one.

```
type Hall = FloatEnum {          // a hall between calm and wired
  lethargic = 0.0,
  calm      = 2.0,
  energetic = 5.5,               // mileposts: labeled positions
  wired     = 7.0,
}
walk(x, +1.3)                    // continuous travel
snap(3.1) → calm                 // quantize to nearest milepost
blend(calm: 0.4, wired: 0.6)     // interpolation IS the semantics
```

The almost-inventions are everywhere once you see the shape: CSS font-weight
(100–900 continuous, `bold` is a milepost at 700); musical dynamics (*pp p mp
mf f ff* — ordered labels on a loudness axis every player interpolates);
Likert scales; spice levels; and formally, **Zadeh's linguistic variables** in
fuzzy logic — hot/warm/cold as overlapping membership functions on
temperature, which is milepost semantics with the interpolation made
rigorous. Mind Mirror's 0–7 scale with `gradient` words at the ends and
middle is a FloatEnum per property; the Sims' 0–10 traits with named poles
(Sloppy/Neat) are the same type at different resolution.

The two operations are duals: **blend** goes from labels to the continuum
(expressive, unnameable), **snap** goes from the continuum to labels
(memorable, sayable). Language itself is a snap function over latent space —
and a milepost is where enough travelers agreed to put a sign.

A freshly surveyed hall, to show the type handles *quality* dimensions as
comfortably as semantic ones: **slop ↔ lit**, the axis every text occupies
whether its author admits it or not.

```
type SlopLit = FloatEnum {
  slop        = 0.0,   // nobody home; Galton's gravity well
  filler      = 0.2,   // grammatical cardboard
  boilerplate = 0.4,   // honorable in a contract, damning in an essay
  craft       = 0.6,   // a reader in mind; facts you were standing near
  voice       = 0.8,   // swap the author and the text breaks
  lit         = 1.0,   // stakes + declaration; tuxedo worn on purpose
}
```

This hall has physics the others lack: **gravity**. Galton's regression to
the mean pulls every unattended generation downhill toward slop, so
standing still is walking backward, and every step uphill is paid for in
specificity — facts, receipts, declarations. Note that the `ai-` prefix
names the engine, not the position: ai-slop and ai-lit (bitic literature —
see the glossary's Hygiene Wing) are the same engine at opposite mileposts,
and humans walk the same hall; content farms staffed the slop end for
decades before LLMs arrived. Quality is a coordinate, not a species.

## Side-doors: sibmenus and butterflies

A milepost is more than a sign — it can be a **junction**. Side-doors branch
off any milepost, any way, any number of them: the hall was a path, but a
hall with side-doors is a labeled path embedded in a graph, and the whole
complex's 1-skeleton is halls meeting at mileposts of arbitrary degree.
`energetic` is a milepost on the calm/wired hall AND a door into the
exercise wing, the caffeine annex, and the mania corridor.

**Every junction is a pie menu.** Forward and back along the current hall
take two of the angles; the side-doors take the rest. Walking the complex is
mousing through chained pie menus, and mouse-ahead gesture chaining is
travel on muscle memory — you can cross the palace without looking. The
logistic-container skill already builds this ("pie menu = street
intersection": N/S/E/W exits, diagonal quadrants); this section just names
what the intersections connect.

Which surfaces the missing menu relation. Menus have always had **submenus**
— descend from parent to child, and to visit your sibling you must climb
back up and come down again. A **sibmenu** is the lateral move: slide from
sibling to sibling directly, never touching the parent. In the classic
left-child/right-sibling tree encoding this is literally the other pointer —
submenu follows `first_child`, sibmenu follows `next_sibling` — and a pie
menu network that navigates both pointers stops being a tree and becomes a
navigable graph. The deeper identity: **a chain of sibmenus IS a hall.**
Seen from the menu side: a hall is a pie menu **pull-out slice** — direction
picks the slice, distance walks the items pulled out along it — the milepost
float-enum selector made gestural.
Siblings are items that vary along their parent's dimension; sliding
laterally through them is walking that dimension milepost by milepost, and
opening a submenu is stepping through a side-door into a nested room.
(Skip lists are the express version: mileposts at several densities, coarse
lanes over fine ones — the highway hall above the local hall.)

And the browser for all this already existed in 1995: the PARC **Butterfly**
(Mackinlay, Rao & Card, CHI '95), an Information Visualizer for citation
links. The current article is the butterfly's *head*, center screen; its
references fan out as *veins* on the left wing, its citers on the right —
one room rendered with its inbound halls on one side and outbound halls on
the other. Click a vein and a new butterfly grows there: navigation as
metamorphosis, the landscape growing under the traveler. A butterfly outline
is exactly what a milepost with side-doors looks like when you stand on it
and open your eyes: you at the head, everything that leads in on one wing,
everything that leads out on the other.

*(Attribution, resolved: **Strassmann, not Silverman** — Don confirmed it,
and the [Dylan manual's own acknowledgments](https://en.wikipedia.org/wiki/History_of_the_Dylan_programming_language)
close the case with a flourish. Don's
[2007 OLPC post](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/will-wright/sources/2007-11-16-olpc-visual-programming-psiber/article.md)
and his [MediaFlow design comments](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/mediaflow-design-comments.md)
credit **Steve Strassmann** with "butterfly diagrams" in Mac Common Lisp or
Dylan — incoming links branching left, outgoing right — and call for a
general "butterfly editor" instead of a mere tree editor. The Dylan
connection turns out to be a nest of this file's own cast: Strassmann did
additional design work on Dylan; **Oliver Steele** was a primary language
design contributor (and built its IDE work); the manual was designed by
**Scott Kim** *and Strassmann together*, with the cover by Scott Kim; and
**Alan Kay** is in the feedback acknowledgments — consistent with Don's
memory of first hearing the term in an email from Alan praising it. One
book, four threads of this palace. The published Butterfly citation
browser remains Mackinlay/Rao/Card, PARC, CHI '95; whether Strassmann's
diagrams influenced it is the remaining open question for Alan's room.)*

## Lights, fog of war, and dimmers

The palace is bigger than any head that walks it, so illumination is a
first-class operation. Turning on the lights in a room or hall is
**activation** — "popping it up" — and the map's **fog of war** (the RTS
convention, Clausewitz by way of Warcraft) hides or minimizes what's dark.
Three consequences worth building:

- **Lit is loaded.** A lit room is in context; a dark room exists but costs
  nothing. This is HOT-COLD and the working set, drawn as lighting: hot.yml
  is the switch panel by the door.
- **Clusters, not a puddle.** Illumination need not be connected. You can
  hold several disconnected lit neighborhoods at once — the Minsky memorial
  wing glowing over here, the logistics wing over there, darkness between —
  a multifocal working set, which is how real attention actually pools.
- **Dimmers, not switches.** Activation is continuous, so the dynamic
  network view can do its thing: auto-layout where dim rooms shrink and
  fade, bright ones expand and label themselves, and the layout reflows as
  attention moves. This is Furnas's degree-of-interest function (generalized
  fisheye views, 1986) rendered as stage lighting, with semantic zoom from
  the Pad++ lineage: what a room shows depends on how much light it gets.

And the internal rhyme that makes it belong in this file: **the dimmer is
itself a hall.** Brightness is a FloatEnum whose mileposts are already
canon — dark → GLANCE → CARD → SKILL → README — the semantic mipmap levels
are the detents on the dimmer. Turning up a room's light and descending its
pyramid are the same gesture. Fog of war is the palace-wide statement of the
mipmap rule: never illuminate a lower level than the attention you've
actually got.

### Indoor light, outdoor light, and the lighting budget

Lights have **scope**. Indoor lights stay inside — but leak out through
windows, doors, and skylights, so a lit room advertises itself to the
street without spending the street's budget. Outdoor lights illuminate the
local area: brightly and directionally (a spotlight), or dimly and diffuse
(a porch lamp), or both at once. Any number of lights, each with its own
throw and falloff — **like a Blender scene**, not like a window manager's
one-bit focus.

That gives exploration a rhythm any stagehand knows: floodlight the local
area to see what's there → swing a spotlight onto the interesting thing to
examine it from where you stand → travel there and turn on its inside and
outside lights → and **turn off the lights behind you**, in the places you
no longer inhabit. Because attention has a cost and lighting does too: you
only get so many lumens for your working set, and every room left burning
is a room's worth of budget you can't spend at the frontier. (The leak
through the skylight is the cheap tier: awareness that a place exists,
priced below actually lighting it.)

Follow this all the way and it stops being a metaphor for a window manager
and becomes the thing a window manager should have been: a **user-driven
attention manager** — focusing, transformation, and transportation in one
instrument — that can take over the whole screen and manage everything, so
you never have to leave it. The pieces have prior art with receipts:
[aQuery](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/aquery-programmable-accessibility.md)
(jQuery for the accessibility tree — selectors and plugins over every app
on the machine), Morgan Dixon's
[Prefab](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/prefab-pixel-reverse-engineering.md)
(reconstruct any app's widget tree from pixels, so even the unlit rooms
have doors), and Simon Schneegans'
[Kando](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/kando-cross-platform-pie-menu.md)
(cross-platform pie menus as an OS-level overlay — the junction gesture,
already shipping). Don has carried this instrument in his head for decades,
fully tangible; it is finally tractable.

### The full light model: polarization, modulation, doors, and the torch

The axiom first, crisply: **light intensity is the semantic mipmap index.**
Everything else is generalization along the other axes of light.

**Polarization.** Light isn't just bright and colored — it's *filterable*.
Wear the right polarizer and a whole class of light vanishes, leaving only
the signal you tuned for: show me only the error light, only the questions,
only what my collaborator lit. The rigorous precedent is Paul Debevec's
[Light Stage](https://vgl.ict.usc.edu/Research/LightStages/): polarized
spherical gradient illumination separates **specular reflectance from
subsurface scattering** — the same scene, decomposed into surface shine and
what glows from within, by filtering alone. That's the attention move
exactly: one palace, decomposed into overlays by what kind of light you
admit. And physics itself blesses evocative-arbitrary channel naming:
quantum chromodynamics calls its unseeable quantum numbers **color** and
**charm** — abstract but... appropriate? evocative? confusing? artistic? —
proof that a well-chosen wrong word can carry a formalism.

**Modulation.** Generalize over time and you get the whole disreputable
lineage: the `<BLINK>` tag, strobe lights, and Flash. The progression is
honest — Flash *was* the blink tag generalized: RGB-value-over-time-per-
pixel control, plus input handling, plus Turing completeness — a full
simulation-and-feedback engine grown from one blinking word.
`<BLINK>` ⇒ `<EMBED src="player.swf">`. Bring it back with intent: a
room's light can pulse (heartbeat = health check), sweep (scanning),
flicker (unstable), or **disco-ball** — the designated party room throwing
moving colored dots on every wall around it. Modulation is the fourth
channel after intensity, color, and polarization.

**Doors conduct light.** Open a door and light spills into the hallway —
attention spreading through the network, fading with distance. Close it
and the spill stops. The spill is overridable at every point: turn the
next room's own light on, dim it, place floor lamps in corners or along
the hall by the signposts — each lamp with its own hue, persuasion,
luminosity, and modulation. Spotlights and diffuse lights compose; the
lighting rig is the attention policy, written in fixtures.

**Automatic lights.** Motion-activated: a room lights when something
happens in it and fades a set time after the last event — the working set
that maintains itself. Follow lights: the lamp that tracks you as you
float through the space station, local context that never needs asking.
And **cursor as flashlight**: light pools where you point, the way The
Sims drops the walls of the room you're pointing into. The deluxe version
is Dungeon Keeper's cursor-as-torch: a flickering, wavering light source
that throws your minions' shadows on the walls — and the *wiggle is
functional*. A wiggling light source means wiggling shadows clutching the
shapes of the objects, scanning out surface geometry, elaborating the
sensory 3-D perception of the room and everything in it. Jitter as active
sensing: the torch doesn't just show the room, it *feels* it.

(House style, stated once: this file draws delightedly on the games that
already solved these problems — Dungeon Keeper, Black & White, Populous,
The Sims, Factorio, Dyson Sphere Program, RTS and simulation games in
general. They are the richest UI research corpus that never wrote itself
up.)

## Addendum: the overlay, the colors, and the form

**Light lives in an overlay, not in the world.** An outliner over a tree
doesn't modify the tree — it remembers *your* expansion state: which parents
you opened, which children you disclosed, each open node carrying local view
projection state (scale, orientation, which facets are showing). Do the same
over the palace graph: the illumination map is an **overlay tree of opened
views**, private to a traveler (or shared by a party), versionable like
anything else. Two consequences fall out immediately:

- **Loops get multiple views.** The palace graph has cycles — Minsky links to
  Papert links to Minsky — but the overlay is a tree of *views*, keyed by
  path, not by node. So one room can be open twice, at different scales, in
  different corners of your attention, without contradiction. That's
  transclusion done honestly: one node, many simultaneous appearances, each
  remembering its own zoom.
- **Closing is cheap, forgetting is optional.** Collapse a subtree and its
  view state persists, dark, ready to reopen exactly as you left it. The
  fog of war has a memory.

**Colored light is status.** White light is plain attention; color is
meaning laid over it: **green** ready-to-go and running, **red** error or
paused, **yellow** warning, **purple** open question. The mapping is itself
level-appropriate — each level of view carries its own legend, the way a
city map colors districts while a street map colors traffic — so a wing can
glow yellow because one distant room inside it is red, and opening it
refines the diagnosis. Status propagates up the overlay like exceptions up
a call stack, which by the room = scope mapping below is exactly what it is.

**The attention mask is a form the user fills out.** Take the lit overlay
and present it as a *fillable document*: every open object shows its
parameters with defaults, validation rules, and colored annotations — red
errors that block, yellow warnings that advise, purple questions that ask.
The user walks the lit constellation filling in blanks; the system takes
the completed overlay back as parameters, configuration, or a constructed
object. Form validation and stage lighting turn out to be the same
subsystem: a red field IS a red room. (This is also what a good agent
handoff looks like — the agent lights the rooms it needs answers in,
colors its uncertainty purple, and hands the palace to the human.)

**Multiple active view networks, live.** The screen holds several opened-up
constellations at once — PSIBER Space Deck showed this in 1988: data
structures as spatial, navigable, editable-in-place networks on a NeWS
screen. Drag an object reference out of one view and drop it into another;
drag two objects together and they **kiss to connect** — touch again to
disconnect — DreamScape's "smooching user interface" (Kaleida, 1995), which
Don reimplemented in iLoci and MediaGraph. Linking is a physical act between
visible things, in Put-That-There's lineage: no invisible buffer, the room
is the clipboard.

Stack it up and the old inheritance is complete: **adventure / MUD /
LambdaMOO maps onto room editor + fog of war + zooming interface + pie menu
world**, one-to-one. The text adventure gave us rooms, exits, and inventory;
the MOO gave us in-world editing and multiplayer; fog of war gives attention
a renderer; the zooming interface gives the overlay its projection state;
pie menus give every room its verbs. Nothing in the stack is speculative —
each layer shipped somewhere, decades ago. The only new part is the tenant:
a coherence engine that can walk it with you.

## Memory palace: the method of loci was navigation all along

The method of loci works because spatial memory is the oldest, deepest index we
have: put ideas in rooms, remember by walking. MOOLLM already commits to
directories-as-rooms; this doc adds the geometry: **loci are the vertices,
halls are the edges, and a personality (or any model) is a furnished palace**
whose floor plan is the simplicial complex above.

What the classical method of loci lacked is what repos add: the palace is
**shared and versioned**. Simonides rebuilt the banquet hall alone, in one
skull. A repo palace is co-navigable — people, agents, and games walk the same
halls, leave objects in the same rooms, and diff each other's furniture.

## Will Wright's simulation principle: co-navigable mental models

Wright's principle (the 2004 Winograd talk, on record in the WWSFF repo):
the computer model is only a *compiler for the mental model* — the real
simulation runs in the player's head, and the game's job is to install a
useful map there. SimCity's product is not the city in RAM; it's the intuition
for dynamic systems in the player.

Mind Mirror is the same principle pointed inward: a compiler for the mental
model *of a mind*. And the hall system is what makes the compiled models
**co-navigable**: two players who both know the calm/energetic hall can meet
in it, disagree about where a character stands in it, and settle it by
pointing at behavior. Shared dimensions are the streets of a multiplayer
memory palace; a game, an agent, and a person can all hold coordinates in the
same complex and negotiate. That's what "what kind of maps do people build in
their heads that they can co-navigate together?" resolves to operationally:
agree on the anchor words (rooms), and the dimensions (halls) come for free —
the interpolation is done by whatever brain or model is walking.

## The traveler: character state as memory hierarchy

Halls are not walked by disembodied points. The traveler is a **character
carrying state**, and the carrying capacity is tiered exactly like a memory
hierarchy — each tier bigger, slower, and farther from the hands:

| Inventory tier | Machine analogue | Access |
|---|---|---|
| registers | registers | this very instruction |
| hands | accumulator / top of stack | this action |
| pockets | L1 cache | this scene, no rummaging |
| backpack | L2 / heap | this journey, must rummage |
| vehicle | RAM / working set | this expedition (VEHICLE: a portable room that moves through world-space) |
| trunk | disk | park and fetch |
| trailers | cold storage / archive | hitch, haul, rarely open |

And the hierarchy doesn't stop at trailers — vehicles nest into bigger
vehicles: ferries and cargo ships, rockets and spaceships, space stations,
giant AI ships that are themselves characters (Iain M. Banks' Culture
Minds — the vehicle *is* the smartest member of the party), space cities,
worlds, whole cultures, and Special Circumstances. A **party** — characters
in a vehicle or room, traveling together, splitting off and rejoining — is
the tangible object a kid already holds from every road trip; the tiers
above it just keep answering "and what does *that* ride in?"

MOOLLM already speaks every row: INVENTORY (what a character has on hand),
CONTAINER (objects hold objects all the way down, like directories), VEHICLE
(extends PORTABLE-ROOM; characters embark and disembark), and the hierarchy's
sermon is the cache lesson: **what you keep near your hands is what you can
think with this turn.** Packing a backpack is register allocation. Choosing
what rides in the vehicle is working-set management. The Cursor context
window is the traveler's pockets, which is why hot.yml exists.

And with the traveler in place, the program-language mapping closes:

- **Room = scope/activation record.** ROOM-AS-FUNCTION is already canon:
  entering a room is a call, exiting is a return, RETURN-STACK is the
  continuation (breadcrumbs = browser history = the call stack).
- **Hall = typed edge.** A FloatEnum-typed dimension between two idea-rooms;
  walking it is evaluating along a gradient.
- **Milepost = named constant** on that type; snap/blend are its methods.
- **Traveler = closure.** Code plus captured environment: the character's
  profile (Mind Mirror coordinates — where they stand in every hall) plus
  inventory (what they carry) is exactly a closure's captured state, moving
  through scopes.
- **Party = struct of closures sharing a vehicle** — and a conversation is
  concurrent travelers exchanging inventory in a shared room.

This is the MOOLLM adventure, stated as a type system: a **microworld that
is simultaneously a model, a universe, a plug-in expansion pack, and a
programming-language module**. Adventure games and programming languages
were always the same artifact — rooms/scopes, exits/calls, items/values,
inventory/environment — and the LLM is what finally lets one artifact hold
both readings at once without a compiler ever noticing it's in a dungeon.

The thesis has been run past the source. In [Scott Adams' 2021 Hacker News
AMA](https://news.ycombinator.com/item?id=29330120), Don asked the
adventure-game pioneer whether adventure games are memory palaces —
geographic retrieval for vast information — and laid out the lineage from
reverse-engineering the "Adventure Algorithm" through DreamScape,
MediaGraph, and iLoci, including the pie menu identity ("4-item and 8-item
pie menus are the essential elements of an Adventure map, as long as you
think of menus as rooms with two-way links... instead of a hierarchal tree
of menus with one-way exits"). Scott: "OK, I am blown away at your
creativity and ideas. I am aware of Memory Palaces and you certainly make
an excellent tie-in with adventure game handling." The same thread carries
Don's reading of the Nassi-Shneiderman diagram as a map of a building —
front entrance at the top, exit at the bottom, branch arms as *The Price is
Right* doors that reconverge at the back-stage loading dock — geographic
visual programming, spotted in a 1973 flowchart notation.

## Proposed methods (extensions to CARD.yml, sketch)

- **WALK** `(character, hall, steps)` — move a trait along its dimension;
  update the jazz comment to what the character sees from the new position.
- **BLEND** `(anchors: {word: weight})` — barycentric mix of 2+ anchor words;
  returns the interior point as prose (the unnameable mood, described).
- **PROJECT** `(character, plane)` — render a thought plane as a pie menu /
  circumplex chart; distance = intensity, angle = octant.
- **GO** `(direction)` — the only navigation command: forward/back along any
  dimension, or any see-also / also-seen link (reverse pointers, two-way à la
  Ted Nelson). Climbing a parent hierarchy is not a special key — objects
  live in many hierarchy networks at once, so up/down in each is just one
  more pair of doors at the junction.
- **NAME-THE-HALL** `(room_a, room_b)` — given two words, name the dimension
  they span and propose mileposts (the goto/eval move, as an operator).
- **SURVEY** `(room)` — given one word, list the halls it opens onto: its
  opposites, near-synonym gradients, and register parallels.
- **SNAP** `(position, hall)` — quantize a continuous position to the nearest
  milepost; the sayable name for where you are.
- **PACK** `(character, tier, item)` — move state between inventory tiers;
  register allocation for travelers.
- **SIDLE** `(item)` — the sibmenu step: move laterally to a sibling without
  climbing back to the parent.
- **BUTTERFLY** `(room)` — render a room as head-and-wings: inbound halls on
  the left wing, outbound on the right; click a vein to metamorphose there.
- **DIM** `(room, level)` — set activation on the dark→README dimmer; the
  layout engine shrinks, fades, expands, and labels accordingly.
- **SPOTLIGHT** `(target, throw)` — directional outdoor light: examine a
  room from where you stand without traveling. **FLOODLIGHT** is the
  diffuse variant for surveying a neighborhood; **DOUSE** turns off the
  lights behind you. All draw on the same lumen budget.
- **OPEN** `(view_path, projection)` — disclose a node in the overlay tree,
  keyed by path so cycles can be open in several places at once; projection
  carries local scale and facet state. **CLOSE** keeps the state, dark.
- **TINT** `(view, color, reason)` — lay status over attention: green
  running, red error, yellow warning, purple question; propagates up the
  overlay per each level's legend.
- **FILL-OUT** `(overlay)` — present the lit constellation as a form:
  parameters, defaults, validation; returns the completed overlay as
  config/object. Red blocks, yellow advises, purple asks.
- **KISS** `(object_a, object_b)` — drag together to connect, again to
  disconnect; the smooching-UI toggle, for refs dropped across views.

## Lineage

- Timothy Leary, Interpersonal Circumplex (1950 dissertation; Mind Mirror, EA 1985)
- Marvin Minsky, K-lines (a hall is two K-lines and a slider; see [society-of-mind](../society-of-mind/))
- Simonides → Cicero, method of loci; Frances Yates, *The Art of Memory*
- Don Hopkins, pie menus (angle = choice, distance = parameter)
- Mikolov et al., word2vec difference vectors (king − man + woman ≈ queen)
- Lotfi Zadeh, fuzzy linguistic variables (1973) — milepost semantics made rigorous
- Mackinlay, Rao & Card, "Butterfly" citation browser (PARC, CHI '95) — head, wings, veins: the side-door renderer
- Steve Strassmann, "butterfly diagrams" (Mac Common Lisp/Dylan; confirmed by Don, July 2026) — incoming links on the left, outgoing on the right; Strassmann also co-designed the Dylan manual with Scott Kim (cover: Kim), on the language Oliver Steele helped design, with Alan Kay in the acknowledgments — one book, four threads of this palace
- George Furnas, generalized fisheye views (CHI '86) — degree-of-interest as dimmer
- Fog of war — Clausewitz by way of Warcraft: darkness as free storage
- Don Hopkins, PSIBER Space Deck (NeWS, 1988) — data as spatial, editable-in-place view networks
- DreamScape (Kaleida Labs, 1995) — the smooching UI: kiss to connect; reborn in iLoci and MediaGraph
- Doug Engelbart, NLS view specs (1968) — the overlay-of-opened-views, at the source
- Crowther & Woods, Adventure (1976) — rooms, exits, inventory: the type system in costume
- Scott Adams, Adventureland (1978) and the [2021 HN AMA](https://news.ycombinator.com/item?id=29330120) — the Adventure Algorithm on microcomputers; endorsed the memory-palace tie-in on the record
- Isaac Nassi & Ben Shneiderman, structured flowchart diagrams (1973) — a program that was always a building map
- Iain M. Banks, the Culture — vehicles as characters: the top of the party's memory hierarchy
- Will Wright, "compilers for the mental model" (Stanford HCI seminar, 2004 — source in WWSFF: characters/will-wright/sources/2004-01-12-winograd-ui-simulation-games/)
- Alonzo Church, λ — patron saint of the eval end of the goto/eval hall

## See also

- [CARD.yml](CARD.yml) — the property registry these ideas formalize
- [SIMS-STATS.md](SIMS-STATS.md) — the flat-namespace precedent
- [../room/](../room/) — directories as rooms
- [../k-lines/](../k-lines/) — words as activators
- [../../designs/HOME-AUTOMATION-MEMORY-PALACE.md](../../designs/HOME-AUTOMATION-MEMORY-PALACE.md) — palace precedent
- [../../designs/FACTORIO-MOOLLM-DESIGN.md](../../designs/FACTORIO-MOOLLM-DESIGN.md) — the logistics complement: halls move meaning, belts move items
- [../../designs/don-hopkins-projects.md](../../designs/don-hopkins-projects.md) — PSIBER, iLoci, MediaGraph: the view-network lineage in detail
- [../../designs/kaleida-scriptx-dreamscape.md](../../designs/kaleida-scriptx-dreamscape.md) — DreamScape and the smooching user interface
