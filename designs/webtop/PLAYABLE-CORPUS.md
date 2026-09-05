# The playable corpus

*Don Hopkins · September 2026*

**Thesis:** gwern.net is the best-read document on the web and you cannot *do* anything in it. What
this hub brings to that world is five affordances the adventure lineage shipped decades ago and the
web never adopted: **playability, explorability, inventory, multi-userness, and persistent reading
cursors.** Each has real machinery in MOOLLM already, and one of them turns out to be Nelson's
transclusion wearing a game verb.

None of this is imposed from outside. gwern's own design principles include **"give the reader
agency"** and `reader > author`; these are what those lines commit you to if you carry them out.

The compilation half of this — how a corpus becomes navigable with no model, server, or key in the
loop — is [TAGSONOMY-COMPILER.md](../TAGSONOMY-COMPILER.md). This is what the compiled artifact
*is*.

---

## The mechanism: an article does not get a room, it *is* one

All four affordances need somewhere to happen, and the move that supplies it is an identity rather
than a conversion. **A network of articles becomes a network of live interactive spaces hosted in
GitHub repos, and no article is rewritten to get there.**

MOOLLM's filesystem grammar makes this exact rather than metaphorical
([`skills/file-system-object/SKILL.md`](../../skills/file-system-object/SKILL.md)). A directory is an
implementation class; each UPPERCASE marker file at its root declares an exported interface,
COM-style minus the UUIDs; and **one directory exports many interfaces simultaneously.** So:

| The article directory holds | It exports | Which means |
|---|---|---|
| `README.md` | the document interface | it still reads as an essay, to a reader who wants only that |
| `GLANCE.yml` | the glance rung | it answers at `SUPERBRIEF` and `GLYPH` |
| `ROOM.yml` | the **room** interface | it has exits, a sign, adjacency — it is a place you can be in |
| `CARD.yml` | dispatch: methods, advertisements, k-lines | it has **behavior**: things it affords, things it can be asked |
| `characters/` | a typed collection | **people live in it** |

An article becomes a place by *gaining an interface*, not by being ported. `queryInterface(dir,
ROOM)` returns non-null once `ROOM.yml` exists and null before, and the document interface is
untouched either way. That is endosymbiosis with a type signature — the same shape as
[`DOMIsland`](temkin/README.md#domisland-endosymbiosis-with-a-type-signature), applied to a corpus
instead of a widget: host the foreign thing, give it an interface, do not reimplement it.

**Behavior arrives as advertisements**, which is the part that is most native to this lineage.
`CARD.yml` carries an `advertisements:` block, and the convention is stated in `yaml-jazz` as
*"Directory listing IS the advertisement index — Sims-style 'what's available here?'"* In The Sims,
objects broadcast what they offer and agents choose by advertised value; here an article broadcasts
what it affords — read me, argue with me, take a reference, run my example, ask my resident — and
both human readers and LLM agents select against the same index. Navigating a large corpus by
advertised affordance rather than by link topology is a genuinely different mode, and it is the one
an agent needs most.

**Characters in rooms is what makes an article answerable.** A `characters/` subdirectory puts
residents in the article: the author's own persona, a critic, a domain expert, an adversarial
reviewer. `skills/adventure/SUMMON-PROTOCOL.md` already handles instantiating them. An essay with a
resident is a place where you can ask the essay a question and get an answer *in character and in
context*, rather than pasting the essay into a chat window and losing the context — which is the
context-cost problem this whole hub exists to attack.

**GitHub is the host, and that is not a compromise.** The repo supplies versioning, forking, review,
diffs, and free static serving, and the compiled static tier runs on Pages with no backend. Forks
are per-player worlds, which is the mechanism `MOOST-MULTIPLAYER.md` already assumes. A network of
interactive spaces that is also a network of repos is one artifact, not two, and the URL discipline
gwern already practices maps directly onto directory paths.

## Playability: actions with consequences, not just links

A link takes you somewhere. An action changes something. Reading gwern.net, the only state you can
alter is scroll position and which popups are open — and popups are explicitly designed to leave no
trace, which is correct for a document and insufficient for a place.

The adventure skill already defines the verb set and, more importantly, where the consequence lands:
`CHARACTER.yml` owns the player's location, `ROOM.yml` owns the room, and a state change is an edit
to a tracked file with a before and after. Debug mode renders that edit as the narrative
(`location: start/ → coatroom/`), which means **the game's state changes and the corpus's diffs are
the same object**. Git is the save file.

That is the property no web document has: your visit leaves a reviewable trace, in the same
representation the author used.

## Explorability: a place you can be lost in

Search answers questions you already have. Exploration surfaces the ones you don't. gwern.net has
excellent search, excellent links, and no *there* — no map, no sense of a region you have not
visited, no adjacency that isn't a hyperlink.

The worked instance is already in the repo: [`THE-TOWER.md`](../pie-stack-views/THE-TOWER.md) reads
Lane Neverending as a signed vertical axis with typed connectors, where up is how an institution
presents itself and down is what holds it up, and where a tunnel between two basements is invisible
from any height. **You cannot get that from a link graph, because the link graph has no altitude.**

The affordance to steal from adventure games is not the map, it is the *unvisited exit* — the honest
statement that there is more, in a specific direction, that you have not seen. A corpus that can say
that is explorable. A corpus with a search box is merely queryable.

## Inventory: transclusion with a carrier

This is the one that turned out to be deeper than expected, because `skills/inventory/` has already
solved the problem Xanadu is famous for, in game verbs:

| Verb | What it does | What it means |
|---|---|---|
| `TAKE REF` | picks up a **pointer** — *"Lightweight path, weight: 0"* | **transclusion**: you carry the reference, the thing stays where it is |
| `TAKE OBJECT` | *"Deep copy with identity"* — heavy | **copying**: you carry a duplicate, and now there are two |
| `DROP AS BOX` | writes a YAML file with inheritance | the reference becomes a thing, with identity, that can be edited and can diverge |
| `DROP AS BEAM` | moves the actual file | you moved the original, and everyone else's references now point here |

The skill's own summary is the whole design: *"Carry pointers or values. Set them down, they become
real."* And its golden rule — *"Once boxed, always boxed"* — is the irreversibility that makes the
distinction honest.

Two things follow that are worth stating plainly.

**Weight is the cost model for copying,** and it is exactly right. Nelson's complaint about the web
is that copying is free and therefore ubiquitous, which severs quotes from their sources. Making a
copy *heavy* and a reference *weightless* teaches the semantics through physics rather than through
documentation — which is ARK's literalism, and which is why a reader learns it without being told.

**Inventory is the commonplace book.** A reader accumulating references as they move through a corpus
is doing what commonplace-book keepers did for four centuries, and what
[SUMMARY-GENRES](SUMMARY-GENRES.md#the-terms-of-art) traces from *locus communis*. The difference is
that these entries are pointers rather than transcriptions, so the collection stays connected to
what it collected from. A bibliography that cannot rot.

## Multi-userness: others are in here with you

gwern.net has one author and a comment-less surface. LambdaMOO had thousands of people in one place,
building it while inhabiting it — and that lineage is explicit in the adventure skill, which cites
Engelbart's NLS tradition for multi-agent presence and carries
[`MOOST-MULTIPLAYER.md`](../../skills/adventure/MOOST-MULTIPLAYER.md) for the mechanism: a shared
JSON model in Supabase for live state, with **git forks per player** as the durable layer. Live
where liveness matters, git where permanence does.

What multi-userness adds to a *document* corpus specifically:

- **Other people's paths are content.** A saved view is testimony
  ([VIEWS-AS-TESTIMONY](../pie-stack-views/VIEWS-AS-TESTIMONY.md)); with several readers, the corpus
  accumulates tours, and the reply-with-a-view move becomes an argument others can watch.
- **Presence is a signal.** Where people are is a heat map over the corpus that no analytics
  dashboard can express, because it is *in* the space rather than about it.
- **Agents are users.** This is the part that only works now: an LLM in the corpus is another
  inhabitant with a location, an inventory, and a path, which is a far better fit than the chat pane
  Nenex puts beside the document. Mesa's shared canvas is the same instinct
  ([temkin](temkin/README.md)).

## Reading cursors: the one that makes the other four persist

The four above all assume a reader who is *there*. None of them survive closing the tab, and neither
does gwern.net's semantic zoom — you drill four rungs into an appendix, come back tomorrow, and start
at the surface.

The fix is already in the repo under another name: **a reading cursor is a character.**
`CHARACTER.yml` owns `location:`, and a location in a corpus of rooms is a position in a document.
That gives the position an identity, an inventory, a path, a rung, and an owner — so you can keep
several, return to one, hand one to somebody, and let an agent hold one of the same type as yours.

The full argument, including gwern's own already-shipped per-reader LocalStorage model and why the
browser bookmark fails on exactly the axes Nelson's clipboard does, is
[READING-CURSORS.md](READING-CURSORS.md).

## The tension worth naming

**Inventory and multi-userness want a server; the compilation thesis forbids one.** The whole point
of crystallizing is that a published corpus browses with no model, no key, and no backend. Per-reader
inventory needs persistence, and multi-user presence needs a live channel. These are in genuine
conflict and the resolution is tiers, not hand-waving:

| Tier | Affordances | Needs |
|---|---|---|
| **Static** | playability, explorability, inventory | nothing. Local storage for the reader's state, the compiled index for everything else. Fully offline, archivable, no account |
| **Social** | multi-userness, shared views, presence | a sync layer — and git already is one, asynchronously; Supabase or equivalent only for liveness |

The static tier must be complete on its own, because it is the archival artifact and the thing that
still runs in forty years. The social tier is opt-in and allowed to be lossy. Any design where
single-player requires the server has failed the Scott Adams test — the database has to outlive the
service.

### GitHub is a slow server, and slow is the correct speed

The tier split above is right but it undersells the middle. **GitHub is already a server — a slow
one, and fast enough.** Repositories are the shared state, Actions are the scheduled computation,
pull requests are the merge protocol, and forks are the identity model. Nothing about the social tier
requires a live socket except presence, and presence is the least valuable thing on the list.

Slowness is a feature, not a compromise. An asynchronous, reviewable, revertable channel has
properties a realtime one cannot get: every contribution is a diff with an author and a timestamp,
every merge is a decision someone made, and the whole history is the archive rather than a
by-product. Harassment and spam become pull requests you decline, which is a governance model with
thirty years of tooling behind it — a considerable improvement on inventing moderation from scratch.

**The model is Spore: massively single-player.** Play alone, complete and offline; your creations
propagate to other people's worlds asynchronously, arriving whenever they arrive; and the population
you encounter was authored by real people who were never online at the same time as you. Nobody
waits for anybody. The social layer is a *sediment* of everyone's single-player activity rather than
a session you join — which is exactly the property that lets the static tier stay complete, because
the asynchrony is the design rather than a degradation of realtime.

That reframes what the social tier *is*: not multiplayer with the latency filed off, but
**time-shifted, eventually-global, and useful anyway.** Souvenirs placed on a map, answers
crystallized into an [auto-FAQ](AUTO-FAQ.md), reading lists forked with commentary, views published
as testimony — none of these need anyone else present, and all of them accumulate.

And the social framing matters as much as the mechanism. A repository is a place with a visible
history, contributors, and a governance story people already know how to read. "Fork it and send a
pull request" is a social protocol, not just a git command, and it is the one this design should lean
on rather than replace.

## Honest costs

**A document that becomes a game gets worse at being a document.** This is the strongest objection
and it should not be softened: gwern.net's virtue is that it is *read*, and every affordance here
adds surface a reader must ignore. Anyone arriving to read one essay should be able to do so with no
inventory, no map, and no other players, and should never be told they are "playing." Playability
must be strictly additive and strictly invisible until reached for. The rung selector is the model —
`BRIEF` is the default and nothing announces itself.

### GitHub already implements the two-level answer, and it costs nothing

The mitigation is not a feature to build. **It is GitHub's existing URL scheme**, and it happens to be
exactly the right shape.

| You link a human to | They get |
|---|---|
| `.../blob/main/path/README.md` | The rendered prose. No girders. Just the document |
| `.../tree/main/path/` | The brutalist directory listing, with the README rendered underneath it |

So the README is **the human-navigable overlay** — it can gently do all the navigation, guidance,
structuring, and curation, and LLMs read it happily too — while the directory *is* the source. Point
readers at the README and the machinery is invisible; the room, the residents, the dispensers and the
index are all sitting right there and none of them are showing.

Which makes **"view source" a single move up**: from a file to its containing directory. Always
available, never in the way, and requiring no viewer, no build step, and no cooperation from anyone.
The girders are one click away for whoever wants them and absent for everyone else.

That the directory is the honest source is worth stating plainly, because it is the whole
architecture in one line: **it is GitHub. It does not get sourcier than that.** No custom "inspect"
affordance can beat a URL that already works, is already public, is already crawlable, and already
has thirty years of tooling pointed at it.

This is the rung selector implemented by the host rather than by us — README is `BRIEF`, the directory
is `VERBOSE`, and the transition between them is a URL edit. Nothing announces itself, which is the
requirement the objection sets.

**Multi-user means moderation.** Identity, spam, harassment, and the governance of a shared space
are not features you add later; LambdaMOO's most-cited paper is about exactly this going wrong. A
corpus that invites others in has taken on an obligation that a static site does not have, and the
social tier being opt-in is partly about not incurring it by accident.

**Inventory implies per-reader state, which is a privacy surface.** What a reader picked up is a
record of what they cared about. Keeping it local by default is the honest choice, and syncing it
should be an explicit act.

**Explorability can be a maze.** An unvisited exit is a promise; too many is a corpus that feels
endless rather than deep. The glyph rung and the map exist to make the whole apprehensible from
above, and without them exploration is just being lost.

---

## Related

- [../TAGSONOMY-COMPILER.md](../TAGSONOMY-COMPILER.md) — how the corpus compiles, and the Scott Adams interpreter-plus-database architecture
- [`skills/adventure/SKILL.md`](../../skills/adventure/SKILL.md) — the verb set, the rung selector, state ownership
- [`skills/inventory/`](../../skills/inventory/) — pointers versus values, boxing, weight as cost
- [READING-CURSORS.md](READING-CURSORS.md) — the fifth affordance: characters as read heads, plural cursors, staleness reporting, and why the bookmark is the clipboard problem again
- [DISPENSERS-AND-SOUVENIRS.md](DISPENSERS-AND-SOUVENIRS.md) — what you *carry out* of a room: stamped souvenirs, tickets as service interfaces, parameterized cranks, and the whole thing on a real-world map
- [`skills/adventure/MOOST-MULTIPLAYER.md`](../../skills/adventure/MOOST-MULTIPLAYER.md) — shared state plus git forks
- [gwern pack](gwern/README.md) — what we inherit and what we do not
- [THE-TOWER.md](../pie-stack-views/THE-TOWER.md) — the corpus as architecture, with altitude
- [VIEWS-AS-TESTIMONY.md](../pie-stack-views/VIEWS-AS-TESTIMONY.md) — paths as content
- [SUMMARY-GENRES.md](SUMMARY-GENRES.md) — the commonplace book, and register as a parameter
- [OBJECTIONS.md](OBJECTIONS.md) — the case against all of it

↑ [webtop hub](README.md)
