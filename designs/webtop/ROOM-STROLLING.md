# Room strolling: mood, loom, zoom

*Mobile navigation of a room graph, using the one gesture two billion thumbs already know.*

Related: `[READING-CURSORS.md](READING-CURSORS.md)` · `[PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md)` ·
`[EBIKE-PATH-GRAMMAR.md](EBIKE-PATH-GRAMMAR.md)` · `[TREE-NAVIGATION.md](TREE-NAVIGATION.md)` ·
`[GLYPH-BENCHMARK.md](GLYPH-BENCHMARK.md)` · `[../korz/README.md](../korz/README.md)`

## The naming, first, because the naming is the design

**Doom scrolling** is an infinite strip selected by someone else, where no position has an address
and nothing you pass can be returned to on purpose. The gesture is not the problem. The gesture is
the best-trained input idiom in human history, and it costs one thumb, one hand, no aim, no
precision, no eyes-on-target. What is wrong is what the strip is made of.

So keep the gesture, replace the strip: a strip of **rooms**, each one addressed, authored, linkable
and re-findable. **Scroll** becomes **stroll** — one letter, and the difference between being fed and
going somewhere. **Doom scrolling** becomes **room strolling**.

Inside room strolling there are three axes, and they rhyme on purpose:


| Axis                | Gesture in portrait       | What it does                                                                                                                                    | Neighbours visible?                                 |
| ------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **MOOD**            | up/down                   | walk the **major** axis: north/south exits, rooms glued into one continuous strip                                                               | **Yes** — two or three at once, partially on screen |
| **LOOM**            | left/right                | leave for a room on the **minor** axis: east/west exits, off screen, possibly many                                                              | **No** — they loom                                  |
| **ZOOM** / **MOOZ** | pinch, or scroll velocity | change **rung** — zoom in toward the body and the room, mooz out toward the title and the glyph ([the pyramid](README.md#the-semantic-pyramid)) | n/a — depth, not position                           |


**doom → mood → loom → zoom.** One vowel family, four words, and the first is the thing the other
three are built against. Mood is doom read backwards, which is the joke that started this, and it
earns its keep semantically too: along the major axis you drift, and the strip has a mood.

**Why *loom*.** Three reasons, and the third is the one that makes it teach itself.

1. **A room off screen looms.** It is present, implied, unrendered — exactly the state the minor axis
  leaves its neighbours in. Nothing else in English means "there, but not shown" that cleanly.
2. **It rhymes into the family** without colliding. `zoom` is spoken for by semantic zoom, `doom` is
  the antagonist, `mood` is the major axis. `loom` is the remaining seat at the table.
3. **A loom is the machine whose whole nature is two axes with different jobs.** The **warp** runs the
  length of the cloth under tension — continuous, always there, the thing you advance along. The
   **weft** is thrown across it by a shuttle, one pick at a time, and is not visible ahead of where it
   has been laid. Major axis is warp; minor axis is weft; the swipe is the shuttle. Anybody who has
   seen a loom now understands why one axis shows its neighbours and the other cannot.



## Two layers, and every word gets one job

The candidates stopped competing once it was clear they belong to **different layers**. Weaving terms
describe the cloth, which is authored and objective. The `-oo-` words describe the reader's frame,
which is subjective and rebound every time somebody picks up the phone.

**The cloth — objective, in the corpus, versioned, authored:**


| Word                        | Job                                                                                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **web**                     | The woven fabric itself: the room graph. Not a pun borrowed from hypertext — *web* was the weaving word first, the piece of cloth being woven on the loom, from the same root as *weave*. Hypertext borrowed it from the loom, and we are taking it back |
| **warp**                    | The thread family that runs the length under tension: exits that form unbroken sequences a reader can be carried along                                                                                                                                   |
| **weft**                    | The crossing family, thrown by the shuttle one pick at a time: exits that branch, converge, and are not visible ahead of themselves                                                                                                                      |
| **door**                    | A single exit. One link, one threshold — and in the [map editor](KISSING-ROOMS.md#doors-and-halls-what-a-line-is-allowed-to-mean) a door is what two *touching* rooms share, drawn as one edge and no line                                               |
| **selvedge** / **raw edge** | The two ways cloth ends. A selvedge is self-finished, where the weft turns back and nothing frays: *the author finished here*. A raw edge is cut: *the author stopped here*                                                                              |
| **couch**                   | To lay a thread over finished cloth and tack it down at intervals — the embroiderer's word for it, and exactly what a [tour](TOURS-AND-PLAYLISTS.md) is: a route stitched over a map it does not alter, anchored at each stop                            |
| **hall**                    | A link with length, between rooms that are not neighbours. You walk down it, so it costs a turn and can hold things — a corridor is a warp-faced region with both sides moolbed to nothing                                                               |
| **rood**                    | The cross that quarters the circle. A rood is a crucifix *and* an old unit of area equal to a **quarter** — which is precisely what the four cardinal wedges are. `door` reversed is the crossing where four doors meet                                  |
| **hood**                    | A room's **Moore neighborhood**: the eight exits plus here. What is reachable in one move, named as a place rather than a list. Rhymes into `mood`/`rood`/`door` and means *neighbourhood* already                                                       |
| **groove**                  | An unbroken run of warp somebody authored on purpose, meant to be ridden end to end. A record groove is a continuous spiral path with addressed positions on it, which is the major axis exactly. Reading **with the grain** is being in the groove      |


**The frame — subjective, per reader, per grip, rebound on rotation:**


| Word                  | Job                                                                                                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **mood**              | Strolling the **major** axis. A role, not a direction: it binds to whichever thread family is currently laid along the screen's long dimension                                                                                                                                                     |
| **loom**              | Leaving along the **minor** axis. Also, exactly, the apparatus: a loom is what decides which threads are warp and which are weft, which is what a rotation does                                                                                                                                    |
| **zoom** / **mooz**   | Changing rung on the pyramid: **zoom in** toward detail, **mooz out** toward overview. The one pair whose opposition is radial rather than angular — in and out along the hoop instead of across the circle — and the one coinage in the family, which needs no gloss because the rule computes it |
| **moor**              | Tying a [reading cursor](READING-CURSORS.md) up at a room. Spells **room** backwards, and unlike a bookmark a moor is a live line to a live position: you cast off from it, and it knows if the room moved under you                                                                               |
| **spool**             | The materialized strip — rooms wound onto the thread ahead of and behind you, ready to scroll into. Both senses are right: thread on a bobbin, and the print-spooler sense of a queue kept warm just off stage. Spells **loops** backwards, which is what a graph has and a feed does not          |
| **sett**              | How closely rooms are spaced in a map or a rack, coarse and ordinal, under one declared relatedness dimension at a time. A weave's sett is its thread spacing; re-setting under a new dimension is [how you compare two](KISSING-ROOMS.md#touching-is-the-notation-and-the-gap-is-the-measurement) |
| **bloom** / **moolb** | Weighting a side's slices by what currently matters, and its inverse: surrendering a side's angle so the focused side and the major axis can have it. A [fisheye](#slices-inside-an-arc-need-not-be-equal-the-bloom) on a circle, driven by the world and never by the thumb                       |
| **gloom**             | Everything past the ends of the spool: rooms that exist and are not materialized. Not absence — unlit. Zork's *it is pitch black* is a rendering state, and the top of the last room needs to look like one                                                                                        |
| **hoop**              | One ring of the pie. Inner hoop is the cross-cutting verbs, outer hoop is the world. `loop` is the graph's; a hoop is the interface's                                                                                                                                                              |
| **loot** / **tool**   | Inventory, split by use: what you picked up in a room ([souvenirs](DISPENSERS-AND-SOUVENIRS.md)) versus what you carry to act with. Same five letters reversed, and the reversal is the distinction                                                                                                |
| **moot**              | The social tier at a room — who else is here, what they said, what is in dispute. A moot is an assembly *and* an argument, which is both halves of the job, and the `MOO` in MOOLLM was always a place where people met                                                                            |
| **groom**             | The curation pass: the middle gate between recording and publishing that [ride privacy](EBIKE-PATH-GRAMMAR.md#privacy-is-an-editing-problem) says every system omits. Naming it makes leaving it out visible                                                                                       |
| **doom**              | The antagonist. An infinite enshitified strip, chosen by somebody else, where no position has an address                                                                                                                                                                                           |


**The pool.** `pool` is not a word waiting for a job — it *is* the job: **the reserved name for the
thing that does not have a good name yet.** A concept goes in the pool, gets used under that name while
it is still soft, and gets its own word when what it does has settled. Everything in the family that is
still swimming: **sloop** (the single-handed craft you `moor` — a session? a client? it is not decided),
**swoop** (a fling with momentum, low rung, glyphs only), **scoop** (a transcluded span lifted out of a
room), **wool** (raw harvested material not yet woven into exits), **roost** (where a cursor sleeps),
**soon** (the prefetch horizon). `bloom` was in here until the fisheye needed it, which is the pool
working as intended: the word waited, the job arrived, the word was spent. Three more have
real jobs already and are only here because their homes are elsewhere: **oops** is undo — what riding a
roundabout backwards means — **smoot** is the unit of distance along a thread, after the Harvard Bridge,
which is a real path annotated with addressed positions in a made-up unit, and **eroom** is `Moore`
reversed into the electronic room: the screen-side twin of a physical place, which is the distinction
[the ride grammar](EBIKE-PATH-GRAMMAR.md) needs between an intersection and the room that stands for it.

### Moollmnemonic

The naming above is not decoration, and it is not a theme. **Every pair is a pie-menu opposite** —
`doom`/`mood`, `room`/`moor`, `loop`/`pool`, `door`/`rood`, `loot`/`tool`, `spool`/`loops` — because
reversing the letters is what 180° does to a slice. The rhyme family is the axis family, so hearing a
new word tells you which layer it belongs to before anyone defines it. And the double `oo` is a pair of
eyes, which is why the whole set reads as **looking**, why it sits where it sits in **MOOLLM**, and why
`oo` is a fair name for the inner hoop: the ring where `understand` lives is the one you look with.

`zoom` **/** `mooz` **extends the rule to the radial axis**, and shows it was never only about angle. Every
other pair in the family is 180° across the circle; in and out are opposites too, along the
[radius](../pie-stack-views/RADIAL-DIMENSIONS.md) rather than around it, and the spelling reverses just
the same. So the rule is not *reversal means the opposite direction*, it is **reversal means the inverse
operation** — which is why `mooz` undoes `zoom` the way riding the roundabout backwards undoes riding it
forwards.

`mooz` and `moolb` are the only invented words in the set, and it is worth being clear about why that is
allowed here and not in general. Novel jargon is normally a cache miss that never fills — a word the reader has
to be taught and then remember. Both are **computed, not memorized**: anyone who knows `zoom` and `bloom` and knows the reversal rule
already has them, on first sight, without a definition. A coinage that the rule generates costs nothing
to learn, which is a different thing from a coinage that has to be documented.

**Signal processing has been doing this since 1963, and it stuck.** Bogert, Healy and Tukey needed a name
for the spectrum of a log spectrum, reversed the first syllable of *spectrum*, and got **cepstrum** — then
kept going, because the whole domain is a dual and every term in it wanted one: **quefrency** for
frequency, **lifter** for filter, **liftering** for filtering, **rahmonic** for harmonic, **saphe** for
phase, and **alanysis** and **gamnitude** for analysis and magnitude. The paper is titled *The Frequency
Analysis of Time Series for Echoes: Cepstrum, Pseudo-Autocovariance, Cross-Cepstrum and Saphe Cracking* —
"saphe cracking" in a formal proceedings title, which is a field committing to the bit in public.

Two things to take from it. **It works**: cepstrum, quefrency and liftering are ordinary technical
vocabulary sixty years on, and mel-frequency cepstral coefficients have been the most-used feature in
speech recognition for decades, so a computed-coinage name reached the centre of a field without ever
needing to be un-punned. And **not all of them made it**: *cepstrum*, *quefrency* and *lifter* are
standard, while *alanysis* and *gamnitude* are footnotes. The field kept three and let the rest go, which
is precisely what the pool is for — the ones with a job survive, and manufacturing jobs for the others
would only have produced more footnotes. Their transformation is a first-syllable reversal rather than a
whole-word one, but the discipline is identical: the form carries the mechanism, and `bloom`/`moolb` is a
short-pass lifter with a better mouth feel.

And it is a better spoken command pair than the one it replaces. "Zoom in" and "zoom out" differ only in
a short unstressed final word, which is exactly where speech recognition fails, and riding a bike into
the wind is exactly where it fails hardest. "Zoom" and "mooz" differ at the onset instead. Worth
measuring before believing, but it is the kind of thing the [voice channel](EBIKE-PATH-GRAMMAR.md#voice-is-the-annotation-channel)
should be choosing its verbs for.

Two more words fall out of the reversal rule in ways worth keeping. **noon** is a palindrome, so it survives
reversal unchanged, which makes it the honest name for the one direction that never re-binds: twelve
o'clock, screen-up, still up after every rotation policy has had its way with north. And **Moore**
reversed is **eroom**, which anybody would hear as *electronic room* — a free pun on a mathematician's
name that happens to describe the thing his neighborhood is being used to lay out.

A word whose *form* carries the mechanism is a **moollmnemonic**: the spelling is the documentation,
and the reversal is a fact about the interface rather than a joke about the dictionary. This is
[k-lines](../../skills/k-lines/) at the level of the word — the name is the activation, and here the
name also contains the geometry. The discipline has one rule and it is a hard one: a word only gets a
job when the job is already true, and until then it goes in the pool. Inventing a duty so a good word
can be spent would be the cargo-cult version of the whole idea, and the pool exists so that nobody has
to.

## The model

A room graph with named exits. Nothing new; `[PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md)` already says an
article *is* a room. What is new is the projection onto a phone.

**The strip is computed from the current room, not stored.** Take the current room, walk its
`north` exits upward and its `south` exits downward as far as the renderer wants, and glue the
results into one scrollable surface. That surface is a **view**, not a container. It has no identity
of its own, no name, and no membership list.

**Therefore the minor axis is per-room, and columns do not line up.** Room B's `east` exit has nothing
to do with room A's, even when A and B are adjacent in the same strip. The consequence, stated
plainly because it is the part that separates this from every feed app and most carousels: **you
cannot swipe the column. You swipe a room.** Two or three rooms are on screen; the one you put your
thumb on is the one that answers. Tinder cannot do this, because a Tinder card is the whole screen and
the deck is the only structure there is.

**And the minor axis may branch, because it does not have to render adjacency.** The major axis owes
you a continuous neighbour above and below, so it is effectively single-valued at each end. The minor
axis owes you nothing on screen, so a room may have seven `east` exits. Urban Safari already worked
this way: many places funnel in from behind you and fan out ahead. Fan-in and fan-out are free on the
weft and impossible on the warp.

**Which exits exist depends on who is asking.** Exits are not a property of the room any more than a
menu is a property of a chess piece. Same room, different viewer, different weft — a first-time
reader, a returning reader with a cursor, an author, and a bot get different fans. That is
[Korz](../korz/README.md) subjective dispatch over a `viewer` dimension, and it is why the strip
cannot be cached as a column: the column was never the object.

## The gesture is one pie, and the asymmetry is in the geometry

The whole navigation model is a single pie menu on the room under your thumb, and the major/minor
split is not two mechanisms — it is **how the circle is divided.**

**Start from quarters, with the diagonals as boundaries.** North, south, east and west each subtend a
90° quadrant, and the 45° diagonals are the **edges** of those quadrants, not directions anything
points in. So straight up is the centre of the north wedge with 45° of slop on either side, and the
same for the other three. For four equally likely items that is the most forgiving division of a circle
there is, and you cannot do better.

**The rule that makes everything else safe: centres are fixed, widths are free.** The north item is
centered on exactly north and the south item on exactly south, always, in every room, whatever else is
happening. **Nothing about the side exits may push them.** Seven exits east and one west is a fact about
this room, and a pie that divided the circle evenly among its items would answer that fact by rotating
north off north — which is how items end up swimming under the thumb as counts change. The naive
equal-division algorithm is the whole bug, and the fix is that **a pie item's width and its direction are
independent parameters.** Width is negotiable; the centre line is a name.

**So quarters are a default, not a law: the major arc is a knob.** *Knob* here and throughout means only
**a parameter somebody can set** — continuous or discrete, authored or measured. It says nothing about how
it is presented, and in particular there is no widget implied and nothing rotates: it is a number in a
config file until somebody decides to expose it. Call this one `major_arc`, written `A` — the angle each
major item subtends, split evenly either side of its axis. What is left over goes to the two
sides, and because both major items are centered, **each side gets exactly** `180° − A`**, always.** The two
side arcs come out equal no matter how lopsided the exits are, because the arithmetic never consulted
the exits:


| `A`       | Each side arc | When                                                                                                                             |
| --------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **180°**  | 0°            | No side exits at all. The circle is two half-planes: any stroke with an upward component is *next*, and it is impossible to miss |
| **150°**  | 30°           | A near-pure sequence with a rare escape hatch                                                                                    |
| **120°**  | 60°           | Sequence-dominant, one or two side exits                                                                                         |
| **90°**   | 90°           | Balanced. Four equal quadrants                                                                                                   |
| **60°**   | 120°          | Branch-dominant: a hub, an index, a crossroads                                                                                   |
| **< 60°** | > 120°        | Only if the sides are genuinely where the reading happens, and never below the widest minor slice                                |


**North and south need not match each other either**, and the equality of the sides survives that too:
with `A_next` and `A_prev` distinct, each side arc is `180° − (A_next + A_prev) / 2`, still identical on
both sides. Which is worth having, because forward is more likely than backward almost everywhere —
on a ride overwhelmingly so — and a wider *next* than *prev* is the Fitts-correct shape for that.

**Then each side subdivides its own arc independently**, from its own ordered exit list, knowing nothing
about the other side. One exit west and seven east means the west arc is one undivided `180° − A` and the
east arc is seven slices of `(180° − A)/7`. Neither computation is an input to the other, and neither is
an input to north or south.

**The floor is an invariant, not a number.** A major wedge is never narrower than the widest single
minor slice, because the major axis is taken more often than any one side exit by construction — it is
the axis the reader is *on*. Break that and you have made the common move harder than the rare one,
which is the mistake the whole [Fitts](../pie-stack-views/FITTS-OPTIMIZER.md) argument exists to
prevent.

**And what** `A` **really encodes is a probability.** Fitts says movement time depends on target width, so
**angular width should be allocated in proportion to how often a direction is taken**. The setting is not
an aesthetic preference about layout; it is an estimate of where this reader, in this corpus, is going to
go. Which means it can come from three places, in increasing order of honesty:
authored by the corpus, measured from traversal logs, or predicted per context — the last being exactly
what FITTS-OPTIMIZER means by feeding a likelihood ordering into `W` allocation.

**The weave is the name for the setting**, because textiles have been naming this ratio for millennia.
A **warp-faced** fabric shows mostly warp — denim is warp-faced twill, which is why jeans are indigo
outside and pale inside — and a warp-faced corpus wants `major_arc` at 150° or 180°. A **balanced**
plain weave shows both equally: 90°. A **weft-faced** fabric is one where the crossing threads carry
the picture, which is what tapestry and kilims are, and a weft-faced corpus — a hub, an index, a table
of contents — should give its sides the room and drop the major arc to 60°. So the three settings have
physical referents a reader can hold, and "this corpus is a tapestry" is a sentence that now specifies
an angle.

**What varying** `A` **per room costs, given that centres are pinned: only the boundary.** The thing a thumb
learns is a *direction*, and straight up lands north at 60° or 180° alike — the canonical stroke cannot
be broken by any width. What changes with `A` is where north stops being north, so the only strokes whose
meaning shifts between rooms are the ones aimed near a boundary, made blind, without the fan drawn. That
is a narrow and honest cost, and it is why per-room widths are permissible where per-room *centres* would
be indefensible.

It is still worth holding `A` steady across a region, for that last class of stroke. Grain is a property
of cloth and cloth holds its grain across a bolt, so the weave belongs to the corpus or a section of it,
alongside the [rotation policy](#rotation-the-cloth-does-not-turn-the-loom-re-mounts-it) — which turns
out to be the same authored property seen from another side, since a `pin_major` corpus is a warp-faced
one.

And when a single room genuinely deserves different odds, it can have them **in motor space instead of in
the picture**. FITTS-OPTIMIZER's whole point is that likely targets can be given more motor width while
every target stays exactly where it looks: warp the mapping, not the drawing. So a room with seven side
exits makes them cheaper to acquire without moving any drawn boundary at all.

**At 180° the interface vanishes into the gesture it was built from.** A corpus with no side exits is a
plain scroller: two half-planes, no fan worth opening, nothing on screen that a thumb has to be taught.
Add one side exit anywhere and the sides open from zero. So the model degrades continuously down to
ordinary scrolling ergonomics without inheriting ordinary scrolling's structure — the positions still
have addresses even when the geometry has nothing left to show.

**The minor axis subdivides its arc into the room's ordered exit list.** At the balanced setting that
is 90° per side, and everything variable happens inside it:


| Exits on that side | Slice width at 90° | Feel                                                                                                |
| ------------------ | ------------------ | --------------------------------------------------------------------------------------------------- |
| 1                  | 90°                | The whole quadrant. Any sideways flick lands it, aim is irrelevant                                  |
| 2                  | 45°                | Wide, but the seam falls on dead horizontal — see below                                             |
| 3                  | 30°                | Comfortable, and the middle slice owns the horizontal                                               |
| 4                  | 22.5°              | Fine with the fan drawn, marginal blind                                                             |
| 5                  | 18°                | The floor                                                                                           |
| 6+                 | —                  | Stop subdividing. The last slice becomes *the rest, as a map*, and the first four keep their angles |


The whole design lives in the contrast: **the warp's wedge is centered on its axis by law and sized by
the weave; the weft's arc is divided by however many places this particular room can reach.**

Both side arcs are symmetric about dead horizontal at any `A` — east spans `±(90° − A/2)` around due
east — so everything below about ordering, defaults and seams is stated in the balanced 90° case but
holds at every setting.

**Angular order is margin order.** Item 1 sits nearest north, the last sits nearest south, on both
sides — so the fan is [the edge stubs](#what-a-room-owes-the-reader-about-the-rooms-it-is-hiding)
unrolled around your thumb, and the stubs are the fan's projection onto the margin. One order, two
renderings, no translation for the reader to learn.

Three consequences fall out of that ordering, and the third one is a gift:

- **Odd counts have a free default.** With 1, 3 or 5 exits, one slice is centred on dead horizontal —
a cardinal direction, and therefore the most forgiving stroke on the screen. A plain flick takes it
and the fan never has to appear. With an even count the **seam lands exactly on the horizontal
axis**, which is the one place on the circle a seam must not be, and every sideways flick becomes a
small act of aim. That makes *odd* the house habit without anyone writing a rule.
- **Slice boundaries want detents.** Friction at the seams means reselection is felt rather than
watched ([FRICTION-FIELDS](../pie-stack-views/FRICTION-FIELDS.md)), and radius still buys angular
precision the ordinary way ([RESELECTION](../pie-stack-views/RESELECTION.md),
[FITTS-OPTIMIZER](../pie-stack-views/FITTS-OPTIMIZER.md): `W` grows with distance, so a long stroke
is a forgiving stroke).
- **Diagonal exits stop being a special case.** `northeast` is the first slice of the east arc and
`southeast` the last, each reaching the boundary it shares with north or south rather than being
centred on the 45° line — which at the balanced setting *is* that boundary. Close enough that nobody
has to be told, and a room with diagonals does not bend the strip; it just has a fuller weft. The one
place this stops being free is a warp-faced setting, where a wide north eats the ground a `northeast`
would want: a corpus with real diagonals is asking for a balanced weave, and saying so.



### Slices inside an arc need not be equal: the bloom

Dividing a side arc evenly among its exits is, again, only the default. The arc is a budget, and it can
be **allocated by weight** — one slice per exit, sized by how much that exit currently matters. Call the
knob `bloom`, from 0 (uniform) to 1 (extreme): at 0 every exit on that side gets `(180° − A)/n`, and as it
comes up, weight is drained from the cold slices into the warm ones. `bloom` graduates out of
[the pool](#two-layers-and-every-word-gets-one-job) for this, which is what the pool is for — the job
settled, so the word gets spent.

**This is Furnas's fisheye, on a circle.** *Generalized Fisheye Views* (CHI 1986) defines degree of
interest as **a priori importance minus distance from the focus**, and that is exactly the weighting
function here: the exit's standing importance, less how far it is from wherever the reader currently is.
The shipped referent everybody has in their hands is the macOS Dock's magnification, whose amount is a
preference setting.

**The hard rule, and the Dock is the cautionary case: the bulge may be driven by the world, never by the
aiming gesture.** Dock magnification follows the pointer, so the target grows *because you reached for
it* — and it moves as it grows, which is the swimming-target bug in its purest form, defended against
above by pinning centres. A bloom driven by the reader's position along a thread is a different animal:
it changes slowly, it changes for reasons the reader's own body already knows about, and it does not
react to the thumb at all. **Nothing in the geometry may respond to the stroke that is selecting.**

Three consequences, and the first one is why this is worth the complexity:

- **Angular width buys rungs.** A wide slice has room to render more of
[the pyramid](README.md#the-semantic-pyramid): a thin one shows a glyph, a wider one glyph plus title,
the widest a title and a line of description. So size is not only how easy a thing is to hit, it is how
much of the thing you can read — and `bloom` governs legibility as much as it governs targeting. The
fan stops being a list of directions and becomes a fisheye rendering of the room's surroundings.
- **The bloom parks the most likely item on dead horizontal**, which retires the odd-count coincidence
above. Whatever is warmest gets the widest slice, and the widest slice straddles the most forgiving
direction on the screen. The accident becomes a policy.
- **It reallocates reachability rather than creating it.** Cold slices shrink toward the floor, and the
floor rule is unchanged: below it they collapse into *the rest, as a map*. A strong bloom therefore
makes the far ones unreachable blind — correctly, because they are the ones you do not want yet.

The two sides can weight differently, since [each subdivides its own arc](#the-gesture-is-one-pie-and-the-asymmetry-is-in-the-geometry)
with no knowledge of the other: a side full of shops can bloom hard while a side of housefronts stays
uniform. And `bloom` is the same Fitts argument as `A` one scope down — `A` allocates width between the
axes, `bloom` allocates it within a side, and both are estimates of where the reader is about to go.

### moolb: giving a side's space away

To hide a side is to **moolb** it — the second word in the family the reversal rule computes rather than
defines, and like `mooz` it names the inverse operation rather than the opposite direction. Moolb a side
and its slices give up their angle; moolb it all the way and the side is gone.

**Where the freed angle can go is a geometry question, and it has a firm answer: angle is not fungible
across the circle.** The right arc cannot expand into the left arc's space, because everything between
them is north and south, and those centres are pinned. So a moolb'd side hands its budget to its
*neighbours*, which are the two major items, and that is the default worth having: north and south grow
**asymmetric slop** on the emptied side, so an up-and-to-the-left flick still means *up* and there is
nothing over there left to hit by accident. Which sharpens the pinning rule into its final form —
**an item has a direction and two independent half-widths, and only the direction is pinned.** The 180°
degenerate case was always this, with both sides at zero and the majors meeting on the horizontal.

**If the focused side is to get a genuinely bigger sweep, that comes out of** `A`**, not out of the other
side.** Lower the major arc while moolbing, and the surviving side grows symmetric about its own axis,
where it belongs: at `A = 60°` with one side hidden, the focused side takes 120° and the majors carry 60°
each with all their slop on the dead half. That is one gesture with two knobs behind it — `focus`, which
moolbs one side and narrows `A` in the same motion — and it is the arrangement you want when the whole
question is *what is over there, on that side, right now*.

What must not happen is the arc wrapping past the vertical to steal the far half: an item's angle has to
keep pointing at the thing it names, or the fan stops being a map of the surroundings and becomes a
menu that lies about where the world is.

**The rood is a von Neumann neighborhood; the hood is a Moore neighborhood.** This division of the
circle was named decades ago in [cellular automata](../cellular-automata/README.md), where the two
choices for *what is next to a cell* are the four edge neighbours — von Neumann, which is exactly the
rood — and the eight that include the corners, plus the cell itself: **Moore**, nine cells, `N NE E SE S SW W NW C`. That is the pie menu, item for item. Eight slices and a centre, with the centre meaning
*here* and *stay*, which is also what cancel means.

Two things come free from borrowing the name rather than reinventing the shape. A room that authors only
cardinals is a von Neumann room and its fan has four slices; a room with obliques is a Moore room with
eight; nobody needs a separate mechanism for the second case because the geometry always had eight seats.
And the CA literature has already been through which neighbourhood suits which rule — diagonal
connectivity behaves differently from edge connectivity, and a room graph that reads as a grid inherits
that argument intact rather than discovering it late.

**Three radii, because the circle has a middle.** Dead centre is cancel, as in every pie menu since
1986. The inner ring carries the cross-cutting verbs that apply to any object — `understand`, `about`
— so explanation is available at all times and never occupies a compass direction
([AGENCY.md](../revolutionary-chess/AGENCY.md#understand-is-always-on-the-menu)). The outer ring
belongs to the world: exits, headings, destinations.

**How the pie coexists with scrolling**, which is the one real conflict, since a vertical drag is
already mood scrolling:


| Input                         | What happens                                                                                            | Why                                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Vertical drag, immediately    | **Mood scroll** — continuous, tracks the finger, momentum on release                                    | The trained gesture keeps its meaning; no menu appears                                                          |
| Horizontal flick, immediately | **Loom** to the slice containing dead horizontal                                                        | The common case costs one motion and no waiting                                                                 |
| Press and dwell (~200 ms)     | **The fan opens** around the thumb: reserved N/S slices, subdivided side wedges, meta on the inner ring | Dwell is already the request for depth in this cluster ([velocity is the register dial](EBIKE-PATH-GRAMMAR.md)) |
| Press, sweep, release         | Pick by direction, with reselection until release                                                       | Ordinary pie-menu behaviour, ordinary pie-menu escape                                                           |


Inside the fan, north and south mean something the scroll cannot: **jump to that room and snap it to
frame** — a discrete room-level move rather than a continuous glide. Same named commands
(`MOOD-NEXT`, `LOOM(exit)`), two bindings, which is the
[TREE-NAVIGATION](TREE-NAVIGATION.md) lint holding.

The fan is training wheels that never come off. An experienced reader flicks at a remembered angle
and never sees it, which is the property that made pie menus worth shipping in the first place.

## Rotation: the cloth does not turn, the loom re-mounts it

The apparent conflict — warp and weft are properties of the fabric, but mood has to follow the phone —
resolves itself the moment you notice that **a loom is the thing that decides which threads are warp.**
The same yarn mounted the other way round *is* the weft. Nothing about the cloth changed; the mounting
did.

So the split is clean, and it is the same split as everywhere else in these repos:


|                                              | Lives in                                               | Changes when                |
| -------------------------------------------- | ------------------------------------------------------ | --------------------------- |
| **warp / weft / web / door**                 | the corpus — authored, committed, versioned            | somebody writes an exit     |
| **mood / loom / zoom / mooz / spool / moor** | the reader's frame — grip, orientation, viewer, cursor | somebody picks up the phone |


Rotating never rewrites the web. It **re-mounts** it, and there is a real name for the two outcomes.
When mood rides the warp you are reading **with the grain**, along threads an author laid continuously
and intended you to be carried down. When a rotation binds mood to the weft instead, you are reading
**cross-grain**: the strip is now glueing together rooms that were never woven as one thread, and it
will read as a survey rather than an argument. Both are legitimate; they are not the same experience,
and the corpus is allowed to have an opinion about which one it can survive.

And the diagonal has its own name too, sitting exactly on the rood's boundaries: cloth cut at 45° to
both thread families is cut **on the bias**, which is the direction fabric stretches. A bias stroll —
zigzagging `northeast`, `southwest` — is the flexible traversal, and it is the one no author laid out
on purpose.

Portrait puts the long axis vertical, which is where the phone is held and where you can fit three
rooms instead of one and a half. Rotate to landscape and the major axis should become horizontal, or
the whole point of holding it that way is lost.

But a corpus may have been *authored* for one orientation — a timeline that reads down, a river of
argument, a stack of tower floors where up genuinely means up
(`[../pie-stack-views/THE-TOWER.md](../pie-stack-views/THE-TOWER.md)`). Rotating the screen would
then rotate the reader's frame out from under the author's intent.

Both are available, because renaming exits is a relabelling of a compass and there are exactly eight
of them — the symmetries of the square:


| Policy         | What happens on rotate                                                                                                 | Good for                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `swap_roles`   | Screen rotates; **major axis follows the screen**. N/S still means N/S; the strip is now laid out horizontally         | Maps with no authored preference — a mesh, a city, a wiki                                           |
| `transpose`    | Exits are relabelled across the diagonal: `north`↔`west`, `south`↔`east`. The authored major axis stays the major axis | Corpora authored down one axis. The map turns with the phone so the reading direction never changes |
| `rotate_world` | Full 90° relabel: `north`→`east`→`south`→`west`→`north`                                                                | Maps with real geometry, where turning the map is the honest gesture                                |
| `pin_major`    | Refuse. Major axis stays where the author put it; landscape just gets a wider room                                     | Timelines, ladders, towers                                                                          |


Whatever the policy, **the rood turns with the frame, not with the cloth**: the two undivided major
wedges always lie along whichever family is currently mood, and the arcs that subdivide always lie along
loom. In landscape under `swap_roles`, east and west take the major arc and the vertical arcs are the
ones that subdivide. The reader's thumb learns one rule, not two layouts.

### Three rotations, and only one of them is portrait versus landscape

Everything above is **roll** — rotation about the screen's own normal, the only one a phone's orientation
lock knows about. A phone has two more axes, and on a bike they are not idle. Naming all three keeps them
from being confused for each other, since each one binds to a genuinely different thing:


| Rotation  | What the reader does                            | What it means                                                                                                                                             |
| --------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Roll**  | turns the phone in its own plane                | Re-mounts the loom: which thread family is mood. The policies above                                                                                       |
| **Yaw**   | turns to face a different way in the world      | Moves the [bloom's focus](#slices-inside-an-arc-need-not-be-equal-the-bloom). Face the left side of the street and the left blooms while the right moolbs |
| **Pitch** | tips the phone toward the ground or the horizon | Candidate, untested: plan versus elevation. Down toward the map, up toward the facades — which is what a body does with a paper map and a street          |


**Yaw is the good one**, because it makes the fan world-aligned rather than screen-aligned: an exit's
angle points at the thing it names, and to look at what is over there you *turn towards it* instead of
swiping at an abstraction of it. Two things follow. Heading is the continuous form of the intersection's
[90° turn](EBIKE-PATH-GRAMMAR.md#what-the-weft-is-made-of-depends-on-where-you-are-on-the-block): a corner
quantizes the relabel, a body performs it smoothly. And yaw is the **focus input the fisheye always
needed** — Furnas's degree of interest wants a focus, and where the reader is facing is the least
interpretive answer available.

It also stays on the right side of the hard rule. Turning your whole body is gross motor motion, known
proprioceptively, and utterly independent of the thumb that is about to select something. Geometry driven
by the world, again, never by the aiming gesture.

The map declares its own policy in `ROOM.yml` or the corpus manifest, and the default is
`swap_roles`, because most corpora have no opinion and the reader's grip is a real constraint.

## What a room owes the reader about the rooms it is hiding

The major axis is honest by construction: the next room is right there, half on screen, and you can
see whether you want it. The minor axis has to *advertise*, and this is exactly the job the bottom
rung of the pyramid was built for.

- **An edge stub, not a chevron.** The left and right margins of a room carry the destination's
**glyph** and, at the next rung up, its title — the emoji-or-SVG rung from
`[GLYPH-BENCHMARK.md](GLYPH-BENCHMARK.md)`. A blank arrow says "there is more"; a glyph says
"there is a *pub* over there", which is the difference between a feed and a place.
- **Count is content.** Seven exits east and one west is a fact about the shape of the corpus at this
point, and rendering it as seven stubs tells the reader they are at a hub without a word of prose.
- **Peek on drag, commit on release.** Partial drag translates the neighbour in and shows it at a
lower rung; releasing under the threshold snaps back. Nothing is ever entered by accident, and
looking costs less than going.
- **The room you came from stays advertised.** A `west` stub labelled with the glyph of the room you
just left, so back is spatial as well as historical.



## Mechanics that make it feel like one surface

- **Continuous, not paged, along the major axis.** Rooms are glued: the boundary is a seam you scroll
across, not a page you flip. Materialize lazily in both directions, keep three or four rooms live,
and let the strip grow while the reader is moving.
- **Loom preserves screen position.** When a loom commits, the incoming room is placed where the
outgoing room was, and *then* its own strip is built around it. The reader experiences a lateral
translation of the world, not a navigation event. Getting this wrong is what makes hierarchical
mobile UIs feel like a stack of modals.
- **A ride is the physical instance of all of this.** A track supplies its own major axis — elapsed time
or arc length, monotonic and unbroken — so the ride is a warp thread and the city is what crosses it:
doors you enter and come back from, cross streets that re-warp the frame, and your own earlier passes
through the same point. A roundabout turns out to implement the loom fan exactly, lane choice
included. Worked out in
`[EBIKE-PATH-GRAMMAR.md](EBIKE-PATH-GRAMMAR.md#a-ride-is-a-warp-thread-and-the-city-is-what-crosses-it)`.
- **Scroll velocity picks the rung.** `[EBIKE-PATH-GRAMMAR.md](EBIKE-PATH-GRAMMAR.md)` already argues
that velocity is the register dial: address-level detail is wasted at speed and earned when you
stop. **Speed moozes out and stopping zooms in**: fast mood scrolling renders titles and glyphs,
slowing down lets the body arrive. Depth is therefore partly automatic, and dwelling is the explicit
request for it — Selker's dwell-time prediction, on a thumb.
- **The path is the artifact.** Every position is a room, so the traversal is a
[reading cursor](READING-CURSORS.md) with a history, and the history is
[commits on an orphan branch](CURSOR-STORAGE.md). A stroll can be saved, named, replayed, forked,
and handed to somebody as a route. This is the thing doom scrolling structurally cannot do: there
is no such thing as *your* place in a feed.
- **One command set, three input paths.** `MOOD-NEXT`, `MOOD-PREV`, `LOOM(exit)`, `ZOOM`, `MOOZ`,
`BACK`, `FORWARD` are named commands; thumb gestures, pie menus and keyboard are three
bindings of them, never three implementations. The lint is
`[TREE-NAVIGATION.md](TREE-NAVIGATION.md)`'s, and it applies here unchanged.



## The argument the mechanics make

A feed is infinite because its end would be an admission that someone chose the order. A stroll is
finite in every direction that matters: the strip ends where the author stopped writing exits, the
fan has a countable number of slices, and both facts are visible. The reader is not being told this
in a preamble; they are learning it by thumb, which is
[procedural rhetoric](../revolutionary-chess/README.md) doing its ordinary work.

Two properties do the arguing. **Every position has an address**, so leaving is not losing your
place, and returning is not searching. And **the strip is assembled from the room you are in**, so
the corpus is a space you occupy rather than a queue you are served — which is the whole reason the
minor axis had to be per-room even though a fixed column would have been easier to build.

## Open questions

- **Where exactly does the fan give up?** The geometry says stop subdividing past five per side and
spend the last slice on a map of the rest. Five is a guess dressed as a floor: 18° is comfortable
with the fan drawn and almost certainly not blind. The real number wants measuring on a thumb, not
choosing in a document.
- **Two-thumb reading.** Nothing above uses the second hand. Holding a room with one thumb while
strolling past it with the other is an obvious gesture with no assigned meaning yet. Candidate:
the held room is pinned as an anchor, and the other thumb's stroll is measured *relative* to it, so
comparison becomes a grip.
- **Which kind of edge is this?** When the warp runs out, the cloth has two honest endings and they mean
opposite things. A **selvedge** is the self-finished edge where the weft turns back instead of being
cut — it does not fray, and it is unmistakably where the weaver meant to stop. A **raw edge** is where
cloth was cut, and it frays. So: *the author finished here* versus *the author stopped here*, and a
reader deserves to know which. The open part is rendering — a selvedge wants to look deliberate and
closed, a raw edge wants to look like an invitation, and neither may look like a crash.
- **Landscape defaults, and the weave, per corpus versus per reader.** The map declares a rotation
policy and a `major_arc`, but a reader with a wrist injury has a policy too, and a reader whose own
traversal log disagrees with the authored weave has evidence. One of them has to lose, and the same
arbitration decides both.

↑ [webtop](README.md) · [designs](../README.md)