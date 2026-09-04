# The angel event bus — objects make system calls to the outside

**Status:** Design, 1 Sep 2026 (Don). A *forward* design in this corpus rather than a
legacy one to uplift — see [README.md](README.md) on the retirement and the Soul-family
uplift. Complements [BRIDGE.md](BRIDGE.md), which maps save data to MOOLLM state; this
adds a **request/response protocol** on top of that mapping.

## The loop

We cannot add code to The Sims 1. So the code runs outside, on the save files, where it
can do anything at all — and the game reaches it by leaving messages in the world.

```
  in game                      │  outside
  ─────────────────────────────────────────────────────────────
  object emits an INVISIBLE    │
  OBJECT encoding a request    │
                               │
  player TAKES A REST     ─────┼──▶  angel wakes on its own, reads the
  (save and quit)              │     save, finds the message objects,
                               │     asks the user about each one, does
                               │     the work, edits the world, writes
                               │     replies (new objects, new messages)
                               │
  FINISH RESTING          ◀────┼───  angel relaunches the game
                               │
  on load: objects READ        │
  their replies and DELETE     │
  them                         │
```

Read-then-delete is the consume step. The save file is the mailbox. **"Take a Rest"** and
**"Finish Resting"** are the whole user-facing interface — see below.

## This is idiomatic, not a hack

**The Sims 1 is already 100% event-driven, with no inter-BHAV function calls.** BHAVs are
triggered by engine events through `OBJf` lookup, run in a polling loop, and return
control — documented in Don's own
[VM Design Document](https://donhopkins.com/home/TheSimsDesignDocuments/VMDesign.pdf) and
quoted in [BRIDGE.md](BRIDGE.md).

That matters for the design's legitimacy: objects in this VM *already* communicate by
posting events rather than by calling each other. The angel is not a foreign mechanism
bolted onto a procedural system — it is **one more event participant**, which happens to
live on the other side of a save boundary and to be arbitrarily capable.

## What it is, in known terms

A **spool directory**, and the save file is the filesystem. Objects drop request files, a
daemon processes them and drops replies, clients consume and unlink. That is `lpr`, the
sendmail queue, `uucp`, batch job submission — decades of prior art, which is the point:
**the failure modes are already catalogued, so they do not have to be rediscovered.**

Calling it a syscall is also exact. Save-and-quit is the trap instruction, and the manual
context switch is the cost.

## Rules the prior art says to adopt

| Rule | Why | Cost if skipped |
|---|---|---|
| **Request IDs** on every message | replies must name their request | replies cannot be matched to requesters |
| **Idempotency keys** | the angel may run twice on one save, or never | duplicated paintings, doubled payments |
| **Explicit delivery semantics** | delete-after-read is at-least-once: a crash between read and delete redelivers | silent duplicates nobody can explain |
| **A version field** | the schema will change while messages are in flight | old messages misread by a new angel |
| **Discovery by GUID** | the angel must find messages without scanning semantically | fragile heuristics over object names |
| **A dead-letter path** | some requests will be unanswerable | requests that sit forever, invisibly |

Discovery is the easy one: reserve a GUID or GUID range for message objects, and the
existing tooling enumerates them directly
([`objd.py`](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/formats/iff/chunks/objd.py)).

## The payload constraint — integers are cheap, prose is not

Per-instance object state in IFF is small integer fields. Text lives in string tables
belonging to the object's *file*, not to the instance. So an invisible object is a fine
carrier for **ids, enums, counts and coordinates**, and a poor carrier for a sentence.

The design should not fight this, because it does not need to:

```
  the game sends    →  wedding 47 complete · participants 12, 19 ·
                       album object 88 · 6 tagged photos · route: eloped
  the angel supplies → every word of prose, every generated image
```

The game reports **what happened, in integers**. The angel already has the neighborhood,
the names, the history, and a language model. Prose flowing the other direction is fine:
the angel writes whole new objects, with their own string tables.

*Confidence: the qualitative constraint is solid. The exact per-instance attribute
capacity should be measured before designing a message format against it.*

## Events have a destination, and one of them is the human

Not every event asks for a world edit. Three destinations, and they want different
guarantees:

| Destination | Example | Guarantee it needs |
|---|---|---|
| **the world** | mint a painting, stamp a license | idempotency — never mint twice |
| **the angel's tools** | generate an image, call a service | retry is safe and cheap |
| **the human** | *here is a link you might want* | **consent** — never act without asking |

The third kind is the one to build first.

## `open_url` — queue links, do not hijack

An object emits an `open_url` event; the angel adds it to a **list presented to the user
with its message**. Nothing opens. The user picks.

This lets any object in the game reach the whole internet without the game containing a
browser: a magazine links to the thing it parodies, an object links to its own design doc,
a generated painting links to a preview of itself, the wedding album links to
[Marusek's story](https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story)).

**Escalation is the user's to grant, never the sender's to take.** An object may *request*
that a link be opened; it does not get to open one. The requester expresses intent, the
policy decides, and a request to escalate is not itself grounds for escalating.

In practice the rest screen below is where the asking happens, so this needs no permission
ladder — links are list items with confirm and cancel beside them, plus a remembered
"just open these" preference for people who want it.

**Every entry carries provenance** — which object, which Sim, which event, and when. A bare
list of URLs is unauditable and phishing-shaped; a list that says *the wedding consultant's
officiant magazine, during the ceremony* is reviewable.

Which points at a real boundary worth stating plainly: saves and custom content get
**shared**. Imported content can put URLs in front of a user who did not write it. So show
full domains, never shorten, never auto-open, and mark links arriving from imported content
distinctly from links your own play produced. Don's default already handles the main risk;
this is just the rest of the same instinct.

Also note the payload rule predicts the implementation here. A URL is text, and text is not
cheap per instance — so **the event does not carry the URL**. Authored links live in the
emitting object's own string table, where they are free, and the event says *link 3 of GUID
X*. Integers on the wire, as everywhere else.

Dedup and expire the queue: a ceremony that fires the same link forty times is one entry.

## Take a Rest — the session model

*Don, 1 Sep 2026.* Saving and quitting is not a technical interruption to be apologized
for. It is **"Take a Rest"**, and the angel notices you rested and gets to work by itself.
When it is done it offers **"Finish Resting"**, which relaunches the game.

The fiction does the work for free, because **rest is already a Sims motive**. The Sims
sleep; now the world sleeps; and the things that happen while everyone sleeps are the oldest
furniture in storytelling — mail arriving by morning, film developed overnight, elves
finishing the shoes. The batch latency stops needing an excuse. It *is* the night.

### The rest screen is the critical section

This is the part that matters beyond presentation. The angel must **never write a save the
game is holding**, because the running game has its own copy in memory and will overwrite on
its next save. So the write window is exactly *after exit, before relaunch* — and the rest
screen is precisely that window, made visible and given a door at each end.

The UI is therefore also the **mutual-exclusion lock**. One writer at a time, enforced by
the shape of the interaction rather than by a convention someone has to remember.

Detection details that follow from this:

- **Wait for process exit, not file mtime.** An mtime alone may catch a half-written save.
- **Then wait for the file to settle** — size and mtime unchanged for a beat — before reading.
- **Back up before writing.** Always, unconditionally. The angel makes arbitrary edits to an
  irreplaceable artifact, and a copy is nearly free.
- **Verify writes landed before offering "Finish Resting."** Handing control back on an
  unverified write is how saves die.

### Each event becomes a form

Per-event **confirm / cancel**, with **parameter editors** for the choices that are properly
the user's. Which turns an event from a request into a small dialog with a schema:

```
  mint a wedding painting                      [ confirm ]  [ cancel ]
    photo         ▾ 3 of 6 tagged
    frame         ▾ gilt / plain / modern
    caption         "Bob and Alice, forever(ish)"
    size          ▾ 2×3 tiles
```

So every event type needs a declared **`parameters:`** block — name, type, default, and
range. That is ordinary typed-field work, and its home already exists: the adventure
compiler's typed-event registry
([`skills/adventure/events/INDEX.yml`](../../skills/adventure/events/INDEX.yml)) is the
schema store, extended with parameters and their editors.

This also **collapses the `open_url` permission ladder above**. The ladder existed only
because there was nowhere to ask; now there is a natural place, and links are simply list
items on the rest screen with confirm and cancel beside them. Keep `open` as a remembered
preference for people who want it — drop the rest.

### The rest screen is an editor — instance, class, and new content

*Don, 1 Sep 2026.* While the game is stopped, show **friendly object editors and mini
simulators on web pages** for the objects the events are about. The user is hacking their own
save file through a powerful interface that does not feel like one — and this runs past
readjusting existing instances into **authoring content**.

Two editors, because there are two things to edit, and in Sims 1 they live in **different
files** with very different consequences:

| Editing | Lives in | Blast radius | Undo |
|---|---|---|---|
| **instance** | the save (lot/house `.iff`) | this one object, this one lot | restore the backup |
| **class** | the object `.iff` in game data | **every instance in every house in every neighborhood**, retroactively, plus anything downloaded later | restore the `.iff` — but see the engine rules below, since one class edit is unrecoverable |
| **new class** | a new object `.iff` | **nothing at all** until something places it | delete the file |

Which yields an inversion worth designing around: **authoring brand-new content is the
safest of the three, and the small-feeling class tweak is the dangerous one.** New content
has zero blast radius until placed. Changing "how much fun is this chair" reaches into houses
the user has not opened in a year.

So the interface should not present these as three sizes of the same button.

### Clone-on-write is the default for class edits

When a user edits a class, **clone it to a new GUID and retarget only the instances in
front of them.** That delivers class-editing power at instance-editing blast radius, and it
is exactly the discipline the Transmogrifier community arrived at the hard way — clone,
don't modify, or you break everyone else's content.

The mechanism is already designed in this corpus: [THE-PET-SHOP.md](THE-PET-SHOP.md)
specifies generating a bespoke named object and hot-patching it into a save, calling it the
polymorphic-inline-cache trick. Clone-on-write is that trick with a checkbox on it, and
"edit this class everywhere, I mean it" stays available behind a deliberately different
gesture.

### Engine rules for class edits — authoritative

**These three are confirmed engine behavior, not inference.** They decide what the editor may
do unsupervised, so treat them as hard constraints rather than guidelines.

**1. An unresolvable class is survivable, but re-saving makes the loss permanent.** When an
instance's class cannot be found at load, the engine substitutes a placeholder type, reads
the instance's data to keep the stream aligned, and then resets it. Nothing crashes, and the
world still loads. But the placeholder's identity is what gets written on the next save, so
the original GUIDs are gone for good. **The angel must refuse to hand back a save whose
classes it cannot all resolve** — that is the moment the damage becomes irreversible, and it
is invisible to the player.

**2. Growing a class's attribute count is safe.** The attribute count is stored *per
instance*, not per class, so instances of one class may legitimately carry different counts
from different eras. A save holding fewer attributes than its class declares loads cleanly
and the new attributes come up at their defaults.

**3. Shrinking a class's attribute count corrupts memory, silently.** The engine's guard
against an instance carrying more attributes than its class declares is debug-only; in a
release build it compiles away and the condition is never evaluated. Execution falls straight
through to reading the save's larger count into the class's smaller array — a heap overflow,
with no error, no crash at the point of damage, and no way for the player to connect the
later symptoms to the edit that caused them.

So the rule the editor enforces:

```
  a class edit is safe only if
      new attribute count  >=  max(attribute count over every instance in every save)
```

Which is **checkable, because the angel has all the saves.** Scan them, take the maximum, and
either block the edit or silently promote it to a clone. That converts the single most
dangerous operation in the system from a warning nobody reads into a preflight that cannot be
skipped — and it is the strongest argument for clone-on-write being the default rather than an
option.

### The event is the deep link — that is what makes it friendly

A save editor that opens on the root of a binary tree is an expert tool. The same editor
opened *by an event*, focused on the certificate that just failed to validate, with only the
relevant fields showing, is a task. Same engine, different door.

That is the whole ergonomic payoff of running the editor off the bus: **events supply entry
points and context**, so the user never navigates to what they need. And the editors can emit
events back — place this object, mail that one, schedule a delivery — so editing and play
speak one protocol.

Before "Finish Resting," show the **diff**: instances modified, classes cloned, objects
created, files touched. The user is hacking a save they cannot replace, and an audit trail is
the difference between confidence and dread. Generated content is ordinary files, so version
control is available for the authoring half for free.

### How real is the mini-simulator?

Faithful for **parameters and appearance**; approximate for **behavior**, unless it is
actually interpreting SimAntics. That is not a fantasy — FreeSO does it, and
[`bhav_ast.py`](https://github.com/DnfJeff/SimObliterator_Suite/tree/main/src/formats/iff/chunks/bhav_ast.py)
already parses BHAVs into a tree — so a browser-side interpreter is a real option rather than
a hand-wave. It is also the point where the two compilers in this project converge: the
[buff-in-time compiler](../../skills/buff/BUFF-IN-TIME-COMPILER.md) turns guards into
runnable `_js`, and the adventure compiler already targets the browser, so a mini-simulator
is those compiled behaviors running client-side with sliders attached.

State the fidelity per editor rather than implying one number for all of them; the
buffopedia's fidelity ladder is the vocabulary for saying how lossy a given preview is.
See [IFF-LAYERS.md](IFF-LAYERS.md) for the orthogonal axis — how deep into binary any given
editor chooses to work.

### Declining is a reply, not silence

If the user cancels, the emitting object should **learn that it was refused**, so write a
`declined` reply rather than deleting the request. An object that asked for something and
got nothing back waits forever; an object that is told no can ask again next month, sulk,
offer a discount, or give up in character.

And nothing is destructively consumed until its reply is durably written — so a crashed
angel or a force-quit rest screen loses no requests, and the game still launches.

## Latency is the fiction, not a limitation

A reply that arrives next session is not a compromise to hide. It is **mail, delivery, and
film development** — and in 1999 photographs genuinely took a week. So:

- the photo book **arrives by post** a day later
- the commissioned painting is **delivered**, like magazine orders already are
- the certificate comes back **stamped and recorded**

Which gives a design rule with teeth: **never put a syscall where the player must wait
mid-scene.** Queue events and flush at ceremonial boundaries — end of wedding, end of day,
end of session. That is exactly the "low frequency" in the low-frequency event pump, and it
is a feature of the fiction rather than a constraint on it.

## The worked case: custom content minted from play

The photographer NPC already exists — it spawns at the ceremony, and its role in the
orchestrator is *ceremony documentation*
([`catalogs/simprov/ORCHESTRATOR.yml`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/catalogs/simprov/ORCHESTRATOR.yml)).
So the loop closes with objects that already exist:

1. Photographers take **tagged snapshots** into the family album during the wedding.
2. The ceremony completes; the license or the chest **emits an event object** carrying the
   album id, participant ids, and the tag set.
3. The angel reads the save, pulls the album and the tags, and **generates objects** —
   paintings with real sprites, a coffee-table photo book, a framed certificate.
4. Next load, they are in the house. Hangable, sellable, describable.

That is **parameterized custom content produced from actual gameplay**, which is the
Transmogrifier's job done procedurally instead of by hand: play generates the source
material, the angel compiles it into objects, the game plays with the result.

**The hard half of step 3 is already designed.** [THE-PET-SHOP.md](THE-PET-SHOP.md)
specifies generating a bespoke named object and hot-patching it into a save, and it hands
the player a coffee-table book on the way out. So generated-object injection is not an open
problem this document needs to solve — it is a solved piece this bus supplies **triggers**
for. The pet shop answers *how to inject*; the bus answers *what asked for it, and when*.

Likewise the album-to-content direction is this corpus's founding image: family album
archaeology in [THE-UPLIFT.md](THE-UPLIFT.md), and a literary precedent —
[Marusek's "The Wedding Album"](https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story))
— in which recordings of newlyweds become people. A wedding album that compiles itself into
objects is the same story told from the tooling side.

## It is the adventure compiler's protocol, pointed at save files

[README.md](README.md#adventure-compiler) already frames this corpus as the Sims target of
the MOOLLM adventure compiler — one map, many targets. What follows is narrower: not the
export path, but the **request/response protocol**, which is also already built and running
in
[`skills/adventure/`](../../skills/adventure/): the linter walks the world, emits **typed
request events** for things it cannot do itself, an LLM answers each one, and the answer is
written back beside its source. `COMPILE_EXPRESSION` is a request object; the compiled
`guard_js` is the reply.

So the schema work is largely done, and should be reused rather than reinvented:

| Adventure compiler | Angel bus |
|---|---|
| linter walks the world | angel walks the save |
| typed event with a self-contained brief | invisible object carrying ids |
| `events/INDEX.yml` as the protocol registry | a message-type registry keyed by GUID |
| answer written beside the source | new objects written into the house |
| English stays authoritative, `_js` is derived | save state stays authoritative, generated content is derived |

The differences worth respecting: the adventure loop is synchronous and text-native, while
this one is batched and integer-native.

## Build order

`open_url` first, presented on the rest screen. It exercises the entire pipeline — an object
emits a message, the player rests, the angel wakes on its own, finds the message, and shows
the user something with confirm and cancel — while editing nothing and risking nothing. If
that fills correctly with the right provenance, the bus and its session model both work, and
every remaining event type is a variation on a proven path with a schema attached.

## Open

- **Can a BHAV reliably create an object with no visible footprint** and no routing side
  effects? `OUT_OF_WORLD` is one of the create-position modes and looks like the intended
  home for exactly this.
- **Where does the queue live** — loose objects on the lot, a container object, or
  neighborhood-scoped storage so cross-household requests survive? (See the transport
  findings in
  [`life-events-playset.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/designs/orchestrator-playsets/life-events-playset.md).)
- **Does the angel ever write a *request* to the game** — asking a Sim to do something and
  waiting for the answer? That inverts the protocol and needs the game to be able to
  decline.
- **What proves a save was processed**, so a player who forgets to run the angel gets a
  clear answer instead of silence.
- **Does a cloned class ever get promoted back** to editing the original, once the user is
  sure — and can two clones be merged, or is that a fork forever?
- **How much SimAntics does the browser mini-simulator need** before previews stop lying:
  parameters only, guards evaluated, or a real interpreter?

## See also

- [BRIDGE.md](BRIDGE.md) — the data mapping this protocol rides on, and the event-driven VM citation
- [IFF-LAYERS.md](IFF-LAYERS.md) — resource architecture, for where generated objects go
- [PSYCHOPOMP-AND-THE-BIFROST.md](PSYCHOPOMP-AND-THE-BIFROST.md) — the named, equipped, accountable agent that crosses over
- [`skills/adventure/ADVENTURE-COMPILER.md`](../../skills/adventure/ADVENTURE-COMPILER.md) — the same protocol, already working
- [`skills/buff/BUFF-IN-TIME-COMPILER.md`](../../skills/buff/BUFF-IN-TIME-COMPILER.md) — English in, runnable snippets out, deopt back to prose
