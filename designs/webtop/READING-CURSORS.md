# Reading cursors: characters as read heads

*Don Hopkins · September 2026*

**Thesis:** gwern.net's design principles already say **"give the reader agency."** They also say
`reader > author`, `hypertext is a great idea, we should try that!`, and `all numbers should be 0, 1,
or ∞`. The affordances in [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) are not a foreign body being
grafted onto that document — they are what those four lines commit you to if you carry them out. This
file adds the fifth affordance, the one that makes the other four persist: **a reading position that
is an object you can name, keep, return to, hand to someone else, and run more than one of.**

The move is that we already built it and called it something else. **A reading cursor is a
character.** `CHARACTER.yml` owns a `location:` field, and a location in a corpus of rooms is a
position in a document. The read head is not a metaphor we are adding; it is the thing that was
already there.

---

## The principle is his; the persistence is missing

Everything a gwern.net reader does to a page is either thrown away or is chrome:

| Reader action | Survives reload? | What it is |
|---|---|---|
| Uncollapse a section | No | position in the argument |
| Pop up an annotation | No — popups are *designed* to leave no trace | a lookup |
| Pin a popup | No | a lookup you wanted to keep |
| Sort a table | No | a view |
| Dark mode, reader mode | **Yes** | a preference |
| Feature use-counts | **Yes** | a model of the reader |

The split is exact and it is the whole finding: **state about the reader's eyes persists; state about
the reader's place does not.** The iceberg resets on every visit. You drill down four rungs into an
appendix, close the tab, and tomorrow you start at the surface and re-do the descent — which on a
page like the design doc itself is several minutes of re-seeking before you are back where you
already were.

### The receipt: demo-mode is a reader model pointed at the furniture

gwern.net's `demo-mode` tracks the use-count of site features in LocalStorage and disables them after
*n* uses, so newcomers get the animated theme-switcher hint and veterans get a slimmer UI. It is a
careful piece of work and the reasoning behind it is right.

It is also, structurally, **a per-reader persistent model, already shipped, on a static site with no
backend and no account** — and it is used to decide whether to show you a toolbar animation. The
mechanism exists. It has never been pointed at where you were reading.

And it is *write-only from the reader's side.* You cannot see it, name it, edit it, copy it, carry it
to another device, or show it to anyone. Which is a complaint with a known author.

## The bookmark is to reading position what the clipboard is to selection

Ted Nelson's rage against the clipboard is that it is invisible, singular, and uneditable — a thing
that holds something of yours that you are not allowed to look at
([VIEWS-AS-TESTIMONY](../pie-stack-views/VIEWS-AS-TESTIMONY.md#github-is-the-clipboard-bus)). The
browser bookmark fails on the same axes, and nobody notices because it *kind of* works — which is
[Alan Kay's diagnosis of why bad designs
survive](../../skills/design-sense/masters/randall-smith.md): it is good enough for the common case
that nobody's day breaks, so the pressure to fix it never accumulates. Compare:

| | Clipboard | Bookmark | What a reading cursor would be |
|---|---|---|---|
| Visible | no | as a title in a menu | yes, it is an object in the corpus |
| Plural | one slot | many, but flat and dead | many, each named, each somewhere |
| Editable | no | rename only | it is a YAML file |
| Has identity | no | no — it is a URL, not a thing | yes, referenceable |
| Remembers the path | no | no | yes, that is its point |
| Shareable *live* | no | you can send a URL, not a state | yes, hand someone the cursor |

A bookmark records a *URL*. It does not record where in the page you were, what you had uncollapsed
to get there, what you had picked up on the way, or what rung you were reading at. It is a pointer to
the front door of a building you were on the fourth floor of.

## The pun is load-bearing in more directions than three

The shared type: **a position in a substrate, with state, that moves — and has history.** Nearly
every field that needed this invented it, named it separately, and solved a different part of it.
Collecting them is not wordplay; each one shipped a piece the others are missing.

| Name | Field | The piece it contributes |
|---|---|---|
| Caret / insertion point | text editing | the position anchors a *selection*, and typing happens where it is |
| **Cursor** (slide rule) | instruments | the original: a transparent slider with a hairline — a **lens**, so position and *view* travel together |
| Read head | disk, tape | **locality and seek cost**: near is cheap, far is expensive, and it reads only where it stands |
| Head | Turing machine | the formal minimum — the head is the machine's entire locus of action |
| Program counter + call stack | execution | **the stack is the path**, and it is what makes *return* possible |
| Cursor | databases | `FETCH` over a result set, plus a worked theory of **what happens when the data changes underneath an open cursor** |
| Playhead | time media | **the one that shipped**: visible by default, and everyone's video player resumes |
| Turtle | Logo | **heading**, not just position — and pen state, whether you are recording |
| Zipper | functional programming | focus **plus the path back to the root**, as a data structure |
| Continuation | Scheme | "resume from here" as a *first-class value* you can save and re-enter |
| **Your bike** | eBike Safari | the cursor is a *vehicle* — or your phone and your feet when you walk. Position in a city, at speed, with a heading |
| Character | MOO, adventure, MOOLLM | a `location:`, an inventory, a memory, a voice, and an owner who might not be you |

And the word was already ours. Latin *cursor* is a **runner, a courier** — from *currere*, to run.
The same root gives *cursus* (a course, a route), *excursion* (a running-out, which is what a ride
is), *recur* (to run back, which is what resumption is), and **discourse** (*dis-currere*, a running
to and fro). A cursor running a route through a corpus and coming back with things is not a metaphor
borrowed from typography. It is the older meaning, and typography borrowed it.

### The five that pay rent

**The call stack is the missing piece in every reading interface.** A program can `return` because
the stack records not just where it is but how it got there. Reading has no return stack, which is
precisely why following links gets you lost — and why the browser Back button feels wrong: it is a
*history* of visited URLs, not a *stack* of open questions. Six links deep into an argument you do
not want the previous page, you want to pop back to the point where you still had the question. A
cursor that keeps its path keeps a return stack, and "unwind to where I last understood things" is a
real command.

**The zipper is the implementation, not an analogy.** Huet's zipper is exactly focus-plus-context:
the node you are at, together with everything needed to reconstruct the way back up. For a corpus
that is already a tree of directories, a reading cursor *is* a zipper over that tree with extra
payload hung off it — inventory, notes, register. This is the part that makes it buildable rather
than aspirational.

**The database cursor already solved staleness.** Decades of work on what an open cursor sees when
rows change under it — isolation levels, stability, whether you observe your own writes — is directly
the [versioned-corpus problem](#version-control-makes-a-stale-cursor-honest). The vocabulary exists;
we should steal it rather than reinvent it badly.

**The playhead is the existence proof, and it is embarrassing.** Every video and podcast player on
earth keeps your position, shows it, lets you scrub it, and resumes you. Nobody loses their place in
a two-hour video. Everybody loses their place in a two-hour essay. Same problem, solved completely in
one medium and not attempted in the other — and the solved one is the *harder* medium, because time
media has no anchors and text is full of them. There is no technical excuse; there is only that
nobody thought text needed it.

**The turtle contributes heading.** Position alone cannot tell you what you were about to do. A
cursor with a direction knows which way you were reading — deeper, sideways, back up — which is what
makes a resumption briefing possible instead of just a coordinate. And the turtle's pen-up/pen-down
is the privacy control: whether this excursion is being recorded at all.

MOOLLM implements the last row of the table already, which means the rest arrive as things the
character can carry. What the character has that a bare cursor does not:

- **Inventory** — what it picked up along the way. `TAKE REF` is weightless, so a cursor accumulates
  pointers without copying ([`skills/inventory/`](../../skills/inventory/)). And the inventory is not
  a flat list; see [below](#inventory-is-a-portable-graph-not-a-list).
- **A path** — where it has been, in order, which is an itinerary, which is
  [testimony](../pie-stack-views/VIEWS-AS-TESTIMONY.md).
- **A register** — the rung it reads at. `SUPERBRIEF`/`BRIEF`/`VERBOSE` becomes *per cursor*, so the
  same corpus is legitimately two different documents to two cursors at once.
- **A voice** — see [masking](#masking-the-default-cursor-is-the-most-abstract-character). Its
  personality colors what it writes down, what it edits, and what it finds interesting.
- **An author** — it can be someone else's, which is the whole social tier.

### Inventory is a portable graph, not a list

The flat "bag of items" is the same poverty as the single clipboard. What games worked out and
documents never did is that **different kinds of things want different kinds of containers**:
Ultima Online's nested bags, WoW's typed bags and bank slots, Glitch's pockets. Containers hold
containers, and the arrangement is itself information — how you filed a thing says what you thought
it was.

Which makes the reader's inventory *its own graph of rooms*, portable, carried. The organizing
problem is already solved twice in this repo, and neither solution needs inventing:

- **Placement is a negotiation, not an assignment.** OpenLaszlo's container placement protocol had
  the container, its sub-containers, their layout policies, the contained object, *and the caller of
  `place` passing hints* all participate in deciding where a thing lands — so an object gets
  intelligently routed to the right place and then physically laid out. That is DWIM filing, and it
  is what makes an inventory stay organized without the reader curating it. See
  [GAME-PIECES.md](../GAME-PIECES.md).
- **Getting things elsewhere is logistics.** Throw it out an exit, a window, a chute, a dumbwaiter, a
  pneumatic tube — overlapping, intersecting networks in the Factorio sense: belts, inserters,
  trains, logistic chests, drones. Already specified in
  [factorio-logistics-protocol.md](../factorio-logistics-protocol.md). An inventory item does not
  only get carried; it gets *routed*, possibly while you are elsewhere.

### Locality is the part that earns the metaphor

A read head is not just a position, it is a position *with a cost model*. That maps onto something
real:

**Seek time is the reader's re-entry cost.** Resuming a hard essay is expensive because you must
rebuild the context you had — which of the six threads you were tracking, which definitions were
loaded, which objection you were holding in reserve. A cursor that carries its inventory and its path
*is* that context, cached.

Which puts this hub's central problem on the other side of the screen. Semantic zoom minimizes the
**page's** context cost: how much you must load to understand this paragraph. A reading cursor
minimizes the **reader's** re-entry cost: how much you must reload to resume being the person who
understood it. Same problem. gwern solved one side thoroughly and left the other side to the browser,
which solved it with a bookmark.

**A read head reads where it is**, which is what makes a resident character's answers positional. Ask
the cursor parked in §4 and it answers from §4, with §4's assumptions loaded, which is the mechanism
under [AUTO-FAQ.md](AUTO-FAQ.md). An LLM in a chat pane beside the document is a read head with no
location; that is precisely why it needs the whole document pasted in every time.

## Outlines with their own insertion cursors: the student model

A reading cursor that only records position is half a student. The other half is that **you are
writing something while you read**, and what you read gets slurped into it.

Medium has the small version and stops there: select text, attach a comment. The comment stays
welded to Medium's copy of the paragraph, and you leave with nothing. What you want instead is to
**carry the selection along and append it into the outline you are building as you travel** —
highlighting as *granular transclusion into your own document*, where your surrounding outline
supplies the context that makes the fragment mean something.

So the inventory contains **any number of ongoing outlines, each with its own insertion cursor.**
Those insertion points are themselves cursors — sub-characters, one per topic — and they are where
slurped material lands. Select text or an object out of the environment, and a reference goes into
the outline at the active insertion point, at a chosen register and level of detail (glyph, title,
abstract, full quote — the same rungs as everything else). The reference stays live, so the outline
is connected to what it was made from.

**This is the clipboard argument's constructive half.** Not one slot, invisible and frozen, but
many named destinations, visible, persistent, and editable — which is what the
[clipboard bus](../pie-stack-views/VIEWS-AS-TESTIMONY.md#github-is-the-clipboard-bus) already gives
as directories in git.

And the model to steal is the oldest one in the building: **a student with a notebook.** Reading the
textbook, sitting in the lecture, asking a question and writing down the answer, noting the
assignment, marking the thing to come back to. Every one of those is a different insertion point in
a different outline, maintained in parallel, by a person who is also *somewhere* — in the chapter, in
the room. Nobody had to explain the user model to them.

Two consequences worth stating. **Questions are first-class inventory** — a written-down question is
an item with a location (where it occurred to you) and a status (open, answered, abandoned), which is
what feeds [AUTO-FAQ](AUTO-FAQ.md) with real questions instead of invented ones. And **a place is not
a boolean.** Browser history colors a link purple and that is the entire model of what you did there.
Read, skimmed, argued with, extracted three quotes from, left a question in, disagreed with the
central claim — these are different, and the cursor's trace records which.

### These cursors are how you build LLM context

The same mechanism, pointed at the machine: a mobile character that gathers, filters, and
incrementally elaborates context is a far better context-assembly tool than a chat window with a
paste buffer. It goes places, takes references at a chosen register, keeps what survived scrutiny,
and hands over a bundle that carries its own provenance. Context engineering as *an excursion with an
inventory*, rather than as a wall of pasted text with no memory of where any of it came from.

## Body plans: cursors are limbs, and a creature has more than one

The multi-cursor problem dissolves once you stop assuming the cursors are interchangeable. **A worm
is an organism with two cursors — a head and a behind — and they do not compete for focus, because
they do different jobs.** Both MOOLLM and LLOOOOMM already define it that way, and
[`skills/worm/`](../../skills/worm/) has the whole verb basis:

| Verb | Where | Inverse |
|---|---|---|
| `EAT` | ingest at the **head** | `BARF` |
| `CHOMP` | pattern-scan, then ingest at the head | `BARF` |
| `POOP` | emit the buffer at the **tail** | `EAT` |
| `BARF` | emit at the head | `EAT` |
| `STICK-UP-BUM` | inject from the tail | `POOP` |

**A worm is a Unix pipe with a body.** `cat a | transform > b` is an animal with its head in `a` and
its butt in `b`, and the skill says so directly: *"Head in doc A, tail in doc B. EAT from A → POOP to
B. Streaming pipeline!"* The image Don reaches for is the honest one — **a worm with its head in one
document eating the text, and its butt in another document laying eggs generated from what it ate.**
The organism *is* the transform, and it spans two locations while doing it.

Two things fall out that are worth more than the joke.

**The I-beam is a degenerate worm, and the skill already knew it:** *"Length: head–tail distance
(**zero-length = NOP cursor**)."* So the plain blinking caret is not a different thing from the
two-cursor organism — it is that organism at length zero. Which means
[masking](#masking-the-default-cursor-is-the-most-abstract-character) and the creature editor are the
same dial, not two competing stories. You start as one point with no body, and you grow.

**Every verb has an inverse, so an organism that transforms is also an organism that can be undone.**
Eating is reversible by barfing. That is a much stronger property than a pipeline has, and it is what
makes a worm safe to send into someone's corpus.

### A selection is a cursor with width

Which is the other direction along the same axis, and it collapses several things into one object.
The worm skill states it as arithmetic — length is head-to-tail distance, and `SELECT-RANGE` spans
them — but the consequence is worth drawing out, because **Emacs shipped the two-cursor organism
decades ago and everyone else kept only the degenerate case.**

| Emacs | The worm | What it is |
|---|---|---|
| **point** | head | the moving end, where you act |
| **mark** | tail | the anchor you left behind |
| **region** | the body | the span between them |
| `exchange-point-and-mark` | reverse the worm | swap which end is active |
| **mark ring** | the path | a *stack of previous positions you can pop back to* |
| **global mark ring** | head in doc A, tail in doc B | the same, across buffers |

The mark ring deserves the emphasis: it is [the return stack](#the-five-that-pay-rent) that reading
interfaces do not have, implemented in a text editor in the 1980s, crossing files. Emacs users pop
back to where they were. Web readers press Back and get the previous URL.

### The I-beam's superpower: it separates *and* embraces

Stretching is the ability, and it flips what the thing topologically *is*:

| Width | Role | What it does |
|---|---|---|
| zero | **separates** | goes *between* — an insertion point, a boundary, a wedge that cleaves |
| nonzero | **embraces** | goes *around* — an enclosure, two arms holding a span |

Same object, opposite jobs, decided by measure: a zero-length interval **divides** a line, and a
positive-length interval **encloses** part of it. Nothing else about the cursor changes.

The separating role is in the glyph's industrial design. The I-beam is shaped that way — a hairline
with serifs top and bottom — so you can aim it precisely *between* two letters and still see it
against the text. Its silhouette is a tool for getting between things.

And embracing is not merely surrounding, it is **holding** — which makes it the gateway to
everything downstream. You stretch to embrace a span, and now you can carry it: into your
[outline](#outlines-with-their-own-insertion-cursors-the-student-model), into your inventory, into a
note. **Stretch → embrace → take.** The plain caret cannot pick anything up, because it has no arms;
growing width is growing arms. Which is also, exactly, growing from a zero-length worm into one with
a body.

And the unification runs one more step, because **width and lifetime are two dials on one object**:

| Width | Lifetime | What we call it |
|---|---|---|
| zero | one keystroke | a **caret** |
| nonzero | until you click elsewhere | a **selection** |
| nonzero | persistent | a **highlight** |
| nonzero | persistent and addressable by others | a **transclusion** |

That last row is the payoff. The stable start/end anchor span that transclusion needs is not a new
mechanism to invent — **it is a selection that was saved and given a name.** Which means highlighting
while you read and quoting with provenance are the same act at different lifetimes, and the
[note-slurping](#outlines-with-their-own-insertion-cursors-the-student-model) above is just the
button that promotes one row to the next.

### Spore's editor is the right interface, and it types the cursors

Spore is the model for how you'd actually build one: **cursors as parts you stick onto a creature**,
at any side, direction, or location. And the part determines the capability, which is where this
turns into a type system.

| Limb | Surface it can stand on |
|---|---|
| **Fins** | liquid — streams, feeds, anything flowing past |
| **Feet** | text files — walk them, stand in them |
| **Fingers** | structured files — reach into a tree and hold a specific node |

**Different limbs enumerate different surfaces.** Which makes "what can I do here?" a question you
answer by *looking at your own body* rather than by discovering a hidden command — precisely the
self-revealing property Don says multiple cursors currently lack. You can see that you have two feet
and a fin, so you know you can stand in two text files and drink from one stream. The body plan is
the capability manifest, and it is visible.

This also inherits Spore's placement behavior, which is the same negotiation as
[container placement](#inventory-is-a-portable-graph-not-a-list): you drag a part at the body and it
snaps, orients, and scales itself to where it landed. Attaching a cursor should work like attaching a
limb, not like memorizing a chord.

And a creature is legitimately **in several places at once**, which is not a mode error because the
places are held by different limbs with different jobs. That is the answer to "which one is you": all
of them, the way both your hands are you.

### Honest problems with bodies

**A body plan is a lot of state for someone who wants to read an essay.** The cell stage has to stay
the default — one point, no limbs, nothing to configure — and growing a limb has to be provoked by
wanting to do something, never presented as setup.

**Spore's editor is a mode you go into,** and if growing a limb means leaving what you were doing,
the discoverability problem has been relocated rather than solved.

**Two cursors in two documents straddle a consistency boundary.** If the head's document changes
while the tail is still writing derived output, what should happen is a real question — and it is the
[database cursor isolation problem](#the-five-that-pay-rent) again, now with two cursors in different
files. Worth answering deliberately rather than discovering.

**Eggs laid from eaten text are model output, and model output confabulates.** An egg needs
provenance back to the specific span that was eaten, or the worm is just a laundering pipeline with a
cute name. `EAT`'s inverse being `BARF` helps: if you cannot barf back what you ate, you did not
really keep it.

## Cursor chat needs cursors, and the lack of them enforces vibe coding

The tool this is being written in demonstrates the thesis by failing at it, and the failure mode is
worth stating precisely because it is causal rather than annoying.

You scroll back to read what the model actually did. Reading provokes a thought. You type the
thought — and **the view snaps to the bottom, destroying your reading position** in a mile-high
transcript with no anchors, no outline, and no way to say "I was here." Recovering the position costs
more than reading did. Do that three times and you stop scrolling back at all.

**That is not a papercut, it is a mechanism that produces vibe coding.** Vibe coding is defined by
not reading the output. An interface that charges a punitive fee every time you try to read the
output, and charges nothing for typing the next prompt, is not neutral about which one you do. It
trains the behavior everyone then attributes to the users' character. The absence of a reading cursor
is the cause; "nobody reads the diffs" is the symptom.

Three things fix it, all of them in this document already:

- **A reading position that survives typing.** Where you were reading and where you are writing are
  two cursors, not one. Conflating them is the bug.
- **Transcripts as branching paths, not linear logs.** Scroll back to a point that has since been
  summarized, fuzzed, and forgotten — and *branch there*, in full resolution, with the context as it
  stood. `cursor-mirror` can already pull forgotten material out of the past and back into the
  present; what is missing is doing it *from a position* rather than by search, and re-entering
  rather than quoting. A chat is a tree of continuations, and the linear log is one traversal of it.
- **Split views.** Which is the next section.

### The Emacs move, and the receipt that we already shipped it

The muscle memory is specific: split the window and scroll to a different place in the same file, or
two different files, or an interactive process, or an Info node — and look at both at once. It is the
most basic multi-position affordance there is, forty years old, and the modern chat interface does
not have it.

**The HyperTIES authoring tool had this, with pie menus to drive it.** Built on Gosling UniPress
Emacs, it gave you multiple tabbed overlapping indexable windows, so you could edit many storyboards
at once, navigate among them, render them through the actual browser formatting engine to see how
they would look, navigate around inside the *rendered* view, and pop back into the editor window for
whatever page you were looking at.

It was not in-place WYSIWYG, because there was no time, leverage, tooling, or budget for that. The
parts list was what existed: Gosling UniPress Emacs with MockLisp, Mitch Bradley's Forth, a C
compiler with no dynamic loading (so Forth did the relocating, memory-mapping, and linking of
non-dynamic libraries), a dumped image of the compiled hypermedia document database so it restarted
fast, the NeWS object-oriented PostScript toolkit, and PSIBER for interactive visual debugging.

Two things follow. The affordance is **not hard** — it was affordable in the late 1980s under
severe constraints, on a rendering pipeline built by hand. And the editor/rendered-view round trip
is exactly the reading-cursor-plus-editing-cursor pair, shipped, with pie menus as the command
surface. The tools available now are enormously better and the capability regressed to zero.

## What plurality buys, which is where it stops being a bookmark

Once the position is an object rather than browser state:

**Several cursors in one corpus.** One parked in the technical appendix, one three levels into a
tangent you want to finish, one at the top of a thread you are arguing with. This is what browser
tabs pretend to be and fail at: a tab has no memory of how it got there, no inventory, and dies with
the session. Twenty open tabs is a cursor system with no persistence, no names, and no way to say
what any of them was for.

**Somebody else's cursor is a thing you can pick up.** Not "here is my reading list" — that is the
route, and it already exists in
[DISPENSERS-AND-SOUVENIRS.md](DISPENSERS-AND-SOUVENIRS.md#a-reading-list-is-a-curated-souvenir-collection).
This is *the position on
it*, with what they had picked up when they stopped. Handing someone a route says where to go;
handing them a cursor says where you are and what you are carrying. Forking one and walking it
forward is a reply.

**The author's cursor through his own corpus is content.** gwern re-reads his own pages constantly —
that path, published, is a tour nobody can reconstruct from the link graph.

**Characters gather into parties, and this is essential rather than decorative.** A party is several
cursors moving together under one intent, which is how you cover a corpus that is too big for one
read head — send the skeptic, the summarizer, and the fact-checker down three branches and
reconvene. Exchanging characters between people is the same operation as exchanging cursors, which
means a party can be assembled out of other people's readers.

**Characters own views, and different characters want different ones.** A view focused on what *this*
reader is interested in, exploring, or trying to prove is per-character state, not global chrome — so
the same room looks different depending on who is standing in it, and publishing a view is publishing
a character's angle rather than a neutral snapshot
([VIEWS-AS-TESTIMONY](../pie-stack-views/VIEWS-AS-TESTIMONY.md)).

**An agent's cursor is the same type as yours.** This is the endosymbiosis, stated concretely: the
LLM is not a pane beside the document, it is a read head *in* the corpus, with a location you can see
and an inventory you can inspect. When it is wrong you can look at where it was standing.

## The two tiers, again, and the transition is a commit

| Tier | Where the cursor lives | Properties |
|---|---|---|
| **Private** | LocalStorage | free, offline, no account, invisible to everyone including the author. The default, and complete on its own |
| **Published** | a YAML file in a repo | citable, forkable, diffable, archival. Someone can fork your cursor and their divergence is a diff |

The transition is a commit, not a signup. Same shape as the rest of the hub, and it means the
static tier never depends on the social one.

### Version control makes a stale cursor honest

This is the thing git buys that LocalStorage cannot. A bookmark into a changed page silently lies to
you: the anchor still resolves, the text under it is different, and nothing says so. A cursor in a
**versioned** corpus knows what commit it was set at, so on return it can report *what moved under
it* — three paragraphs above you were rewritten, the section you were heading toward was renamed, the
claim you were about to argue with was retracted.

No web bookmark can do this, and it converts resumption from a guess into a briefing.

#### The cursor is a permalink: `(remote, commit, path, anchor)`

The mechanism is the one GitHub already ships. A cursor stores a **repo, a commit SHA, a path, and
an anchor** — which is exactly `blob/<sha>/<path>#<anchor>`, a permalink with a reading position
attached. And because your cursor lives in its own branch ([CURSOR-STORAGE.md](CURSOR-STORAGE.md))
while the document usually lives in *someone else's* repo, the pointer has to be cross-repo anyway.

The receipt for that shape is a **submodule**: a pinned cross-repo pointer at a known SHA, with drift
detection built in (`git submodule status` tells you when the pin is behind). A cursor is a submodule
pointer that also remembers where you were reading.

**The point worth being precise about: pinning to a SHA does not fix staleness, it makes staleness
computable.** Those are different, and the difference is the whole design.

| Pinned to | On return |
|---|---|
| a branch (`main`) | your position silently drifts — the anchor resolves, the text under it is not what you read, and nothing says so |
| a commit SHA | your position is exactly what you saw, permanently. It may no longer be where the conversation is — but that is now a **diff**, not a corruption |

Everything in the briefing above falls out of the SHA mechanically, no heuristics:

```bash
git log -1 --format=%ci $CURSOR_SHA          # elapsed time
git rev-list --count $CURSOR_SHA..HEAD -- $PATH   # commits since
git diff $CURSOR_SHA..HEAD -- $PATH          # what actually moved
```

And the one that answers the real question — **whether the change was above you.** Diff hunks carry
line ranges; compare them against the anchor's position. If every hunk lands *below* your cursor, the
context you built is still valid and resume is safe. If something landed *above* it, your loaded
context is wrong and re-reading from the section head is the correct move. That is the exact judgment
that "resumption is sometimes the wrong move" asks the reader to make, computed rather than guessed.

So the default is not a binary but **three modes, selected by the diff:**

| Mode | Chosen when |
|---|---|
| **Resume** | nothing changed above the anchor |
| **Re-read from the section head** | something changed above it, or enough time passed that the briefing is longer than the section |
| **Re-locate** | the anchor no longer exists — show the diff that removed it |

**Anchor on prose, not on line numbers.** Line-pinned permalinks are the known failure of this
mechanism: GitHub's own `#L40` breaks the moment anyone inserts a paragraph. The anchor should be a
heading slug or a **quoted span**, with line numbers demoted to a hint for fast lookup. This is the
same stable start/end anchor span that transclusion needs, which is why it is one mechanism and not
two.

**Honest cost: a SHA can dangle, and dangling is worse than stale.** Force-push, rebase, and
squash-merge destroy the commit your cursor names; once it is gone you cannot even compute the diff,
so you lose the briefing along with the position. This is a real risk against any actively-rebased
repo, and it argues for storing **both** — the SHA for exact provenance, and the quoted anchor text
for content-addressed recovery when history has been rewritten. When the SHA resolves you get the
full briefing; when it does not you degrade to searching HEAD for the quoted text and reporting
lower confidence. Belt and suspenders, and the `robust-first` reading: a cursor should lose precision
rather than lose your place.

## Honest costs

**A cursor that is a character invites cuteness, and cuteness is a tax.** A reader who wants to
resume an essay must never be made to name a golem, pick a face, or be greeted. But the fix is not
"no character" — it is *the right point on the abstraction pyramid*, and Scott McCloud already
worked out where that is.

### Masking: the default cursor is the most abstract character

McCloud's masking effect is that **the more abstract a face, the more readily the reader inhabits
it.** A photorealistic face is someone else; a smiley is anyone; and the reader pours themselves into
the empty one.

The blinking I-beam is *past* the smiley. It is not a simplified face, it is no face — pure locus of
attention and command, with no emotion of its own. Which is why everyone already identifies with it
completely and nobody has ever found it cute. It is `cursor-mirror`'s agent, and it is the correct
default precisely because it is the most abstract thing on the pyramid: **the emotion comes from the
words you type, which it leaves behind it.**

So personality is not a cost the design imposes, it is a **dial that starts at zero.** From there the
reader may optionally personalize — a flame cursor, a math cursor, an Einstein or Pac-Man or Minsky
or Hunter S. Thompson cursor, or their own character writing in their own voice. And this is not
skinning: **the cursor's personality colors what it writes down, how it edits, and what it decides
is interesting.** A Thompson cursor takes different notes than a Minsky cursor from the same page.

**And the dial is technically a language model.** Each cursor carries its own Dasher profile, so the
flame cursor autocompletes into flamier linguistic space than the math cursor — which means
personality is not a label on the cursor but **the curvature of the space around it**. You feel it as
which continuations are wide and easy to steer into. Worked out in [the Dasher
pivot](../pie-stack-views/PUMPING-UP-PIE-MENUS.md#every-cursor-carries-its-own-model-so-personality-becomes-geometry),
including the conflict with pie-menu muscle memory and where the seam between them belongs.

The pyramid is the mitigation. Nobody is told they are playing; the I-beam is what they already use;
and every step up is opt-in and buys something concrete.

The abstraction is not a limitation, either — the I-beam has powers before it has a personality. Its
first is that it can [stretch, and thereby embrace rather than
separate](#the-i-beams-superpower-it-separates-and-embraces).

**Plurality needs a user model, and the character model is the one that is missing.** The objection
that two carets compete for a keystroke is real but it is not the current state of the art: most
serious editors *do* ship multiple cursors for parallel editing, and they are genuinely useful. The
actual failure is discoverability. The feature is unlabeled, the invocation is unmemorable, and there
is no user model at all — you cannot picture what you have, so you cannot picture what to do with it.
Even people who would use it daily do not know the command.

Which inverts the objection. **If you already have a model of characters — create, delete, clone,
name, arrange, send somewhere — then multiple cursors stop being a hidden mode and become an obvious
consequence of something you can already see.** Then broadcasting an operation across them is
natural at whatever level you like: a keystroke, a click, or preferably a *named high-level command*.
The character model does not merely survive plurality; it is the affordance that makes plurality
thinkable, and it is better than what editors currently ship.

**The real requirement underneath all of this** is a coherent kit: cursors, containers, a command
dispatch system, and composition rules where it is obvious both that the pieces fit together and how.
Any individual feature here is buildable; the thing that is actually hard, and not yet done, is
making the set legible enough that a user can see the combinations without being taught them.

**A reading cursor is a worse privacy surface than inventory, not a comparable one.** Inventory
records what you took, which is roughly what you liked. A cursor records **where you stopped** —
which is where you got bored, lost, or angry, and which paragraph did it. That is more intimate than
a bookmark and far more intimate than analytics, because it is per-argument rather than per-page.
Local by default is not politeness here, it is the requirement; and publishing one should show you
its exact contents first, since the interesting part is the part you would not think to check.

**So remembering must be a control, not a property.** The reader decides whether a cursor records at
all (the turtle's pen), what it keeps, what is curated out before anything is persisted, and what
crosses from persisted to shared. Three separate gates, because they are three separate decisions —
and the middle one is the one systems always omit. The same requirement governs the ride version,
where the trace is of a physical body: see
[EBIKE-PATH-GRAMMAR.md](EBIKE-PATH-GRAMMAR.md#privacy-is-an-editing-problem).

**Resumption is sometimes the wrong move.** The cursor makes it cheap to jump back in with false
confidence that the context is still loaded, when what you needed was to re-read from the section
head. A cursor that reports its own staleness — elapsed time, commits since, what changed above you —
makes that judgment available instead of assuming resume; but the failure mode is real and the
default should offer both. The commit SHA in the cursor's permalink is what makes the judgment
computable rather than a guess — [see above](#the-cursor-is-a-permalink-remote-commit-path-anchor)
for the three resume modes and how the diff selects among them.

**None of this helps the drive-by reader**, who is most readers. Someone arriving from Hacker News to
read one essay gets zero value from any of it and must pay nothing for it. The feature has to be
invisible until the second visit, and arguably until the second *interrupted* visit.

---

## Related

- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the four affordances this is the fifth of; the article-is-a-room mechanism
- [DISPENSERS-AND-SOUVENIRS.md](DISPENSERS-AND-SOUVENIRS.md) — souvenirs as what a read head carries away; reading lists as routes, of which a cursor is the position
- [`skills/inventory/`](../../skills/inventory/) — `TAKE REF` as weightless pointer, boxing, weight as cost model
- [`skills/adventure/SKILL.md`](../../skills/adventure/SKILL.md) — `CHARACTER.yml`, `location:`, the rung selector
- [VIEWS-AS-TESTIMONY.md](../pie-stack-views/VIEWS-AS-TESTIMONY.md) — a published path as an argument
- [AUTO-FAQ.md](AUTO-FAQ.md) — why a positional answer beats a pasted-document answer
- [VIEW-STATE-AS-COMMENTARY.md](VIEW-STATE-AS-COMMENTARY.md) — Winer's `expansionState`: view state and document content as the same file
- [gwern pack](gwern/README.md) — what we inherit and what we do not
- [OBJECTIONS.md](OBJECTIONS.md) — the case against all of it

↑ [webtop hub](README.md)
