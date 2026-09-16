# Korz′ Trajectory — the session that grew the document

A sidecar to [korz-prime.md — now design.md](korz-prime/README.md), prefix-named so `ls`
clusters them into the implicit subtree that document describes —
the sidecar practices the doctrine it records. This is the design
discussion of **August 20–21, 2026** written up as what it actually
was: Don pointing at places in latent space, the model dereferencing
the K-lines, and the rabbits getting cached in the design document —
a live, unplanned run of the K-line virtual memory system the
session was busy inventing.

**Provenance** (yaml-jazz habit, worn in prose): reconstructed from
the session transcript via
[cursor-mirror](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror)
introspection — the user-query sequence extracted from the recorded
transcript, the crystallization record from `git log --follow` on
korz-prime.md. Twenty-seven commits touch the file; twenty-six of
them landed in one evening, 21:00–00:04, one commit roughly every
seven minutes. Every claim below cites its commit, so a reviewer can
check this page against its backing store — which is the PR-review-
as-memory-integrity-check protocol from the document, applied to the
document's own biography.

## The shape of the collaboration

The same move, repeated about two dozen times:

1. **Don points.** A few words naming a K-line — sometimes exact
   ("Knuth's literate programming"), sometimes deliberately
   approximate ("isNotUnderstood or whatever it's called from
   smalltalk / objective c / etc." — Postel's law as prompting
   style: the pointer was liberal, the dereference conservative).
2. **The model dereferences.** What comes back is not invention but
   retrieval-and-fit: named ancestors, RFC numbers, mechanisms from
   Don's own career pointed back at him. High-isKnown referents,
   prepaid by training, activated by the name alone — the
   no-ai-humansplaining economics running as designed. Don never
   spelled out what a decision table or the dictionary stack was;
   he aimed.
3. **The file caches.** The rabbit gets written into korz-prime.md
   with links and structure — crystallization — and committed, so
   the next dereference hits the file instead of faulting.
4. **Git verifies.** Push hooks validate; the commit message is the
   provenance stamp; review can reject a bad page before it goes
   resident.

Point → dereference → cache → verify: fault handler, resident page,
integrity check. The session was the system.

## Phase 1 — the isKnown cascade (Aug 20, 21:00–22:28)

Each entry: **the pointer** (Don's words, abbreviated) → the rabbits
that came back → where cached.

1. **"Sample by relevance — or blend the matching slots... the
   troll can front one mind, or blend them with different
   weights."** → Blend weights as context bindings; sampling as a
   form of blending. Cached in *ambiguity: blend* with the
   Cross-Platform Troll as running specimen (`91552040`).
2. **"Just like the adventure compiler, there will be a zork
   compiler that produces deterministic executable korz code."** →
   The shipped moollm adventure compiler as crystallization
   precedent; the anagram becomes a toolchain: Zork improvises, the
   compiler crystallizes, Korz runs (`09c1c69f`).
3. **"We should discuss what Vanessa would think — not ask the LLM
   to simulate her; ask her friends to remember her."** → Memorial
   mode extended to design discussions; her documented JIT position
   (ride the platform, don't fight it) as the open question her
   friends get to argue (`263336cd`).
4. **"Lean heavily into yaml jazz. korz jazz! jazzork!"** +
   **"knuth's literary programming."** → Korz Jazz as foundational
   design goal; the WEB inversion — the tangle step disappears
   because the interpreter is a reader; comments round-trip as data
   in the strict tier (`9c8c3d88`).
5. **"How does Zork decompose into Korz?"** + **"the dimensions of
   location and character."** → ZIL's parser globals as frozen
   dimensions — PRSA/PRSO/PRSI, then the second pointer flushed two
   more rabbits: WINNER and HERE. Zork froze five dimensions in
   1979; The Sims froze two; Korz generalizes to N (`4a177b6d`,
   `ef217c01`).
6. **"The cross platform troll is literally two headed! Retcon
   that!"** → Two heads whose sizes display the fronting weights —
   debuggability by physiology; budding for future minds. Cached in
   the troll's canonical files in moollm and synced back into
   korz-prime (`4b87db25`).
7. **"MOOLLM's selfish object system is like a one-dimensional
   Korz — shouldn't it host Korz?"** → Soups intertwingled with
   objects, same files, same syntax; interfaces as saved views;
   the tree as one saved view among many (`30418b28`).
8. **"A bundle of guarded slots sounds like a card with a bunch of
   sims advertisements. Guarded and scored."** → Cards as
   advertisement bundles; The Sims' scored-action auction as
   dispatch-by-numbers; lattice specificity and ad scoring as two
   ends of one resolution spectrum — MOOLLM was already doing
   one-dimensional Korz in production (`f4990a0b`).
9. **"Bigendian prefix matching clusters files in the same
   directory into implicit trees."** → Prefixes as containment
   without directories; sort order as the free discrimination
   index; the tree/sea duality goes fractal (`818170de`).
10. **"I want this to work without an IDE — just a normal
    filesystem / git repo."** → The audit: Korz's IDE dependency
    was mostly compensation for the opaque Self heap; the
    IDE-did/bare-repo-does table; bootstrap order files-first
    (`799954e6`).
11. **"Not only parents — any slot can hold k-line pointers to
    latent space."** → Two kinds of address (paths and K-lines);
    the strict compiler's refusal as a crystallization to-do list;
    dangling pointers become deopt triggers (`520be592`).
12. **"Instead of testing for null can you test for how known it
    is? isNull:bool => isKnown:float."** → Graded presence;
    consistency probing and logprobs as the cheap and instrumented
    measurements; calibrated dereferencing (`43a95cf6`).
13. **"Sounds useful in guards and advertisement scoring
    expressions."** → The epistemic term: a slot whose referents
    are shaky bids low in its own auction — the hallucination
    damper built into the market (`6e6ca597`).
14. **"You could have a virtual memory system that pages local
    files in for important k-line derefs that aren't well
    known."** → The full mapping: K-line name as virtual address,
    latent space and the web as backing store, repo as RAM,
    `sources/` directories as the pattern already running by hand
    (`40de70c5`).
15. **"Do we want to avoid nulls, the zillion dollar mistake?"** →
    Hoare 1965/2009; absence-is-not-a-value; null's three
    conflations each getting an honest mechanism; E-Prime applied
    to reference (`6740b3e1`).
16. **"GitHub PR review agents catch bad resident pages!"** → ECC
    for the K-line cache; the parity check is a literate review,
    the correction is a diff; a reviewed page outranks its backing
    store (`7581c5db`).
17. **"Make this readable, not a wall of text."** → Not a rabbit —
    a grooming pass. The K-line run got its section skeleton and
    the virtual-memory mapping table (`996588dc`).

*Interlude, 22:30–23:30:* the Brain Flurries / Hierarchy of Bleeds
jam with Heather and Steve — same method, different document
(the Heather & Steve show's sources,
`a24fcade`). The session multitasked; the method didn't change.

## Phase 2 — the addressing cascade (Aug 20, 23:41 – Aug 21, 00:04)

18. **The HN link** —
    [Don's own July 2024 comment](https://news.ycombinator.com/item?id=41043950)
    on the null/undefined/unknown trinity. → dunham's punchline
    weaponized (hold a zero factor and the multiplicative mistakes
    vanish); the Rumsfeld Matrix mapped mechanically onto isKnown
    with deopt as the unknown-unknown detector; IUnknown → isKnown,
    the root interface upgraded by one letter and one type
    (`b13ef512`).
19. **"ls is even more powerful and reflective than
    QueryInterface! ls is a mirror!"** → COM's missing enumeration
    — QueryInterface answers yes/no to a GUID you must already
    possess; `ls` volunteers the manifest in names that are
    themselves K-line activations; IUnknown confesses ignorance,
    `ls` confers knowledge (`cbf477f4`).
20. **"Self revealing interfaces / slot soups! What if a soup with
    a hierarchic (both dirs and alphabetical sorting of shared
    prefixes) structure?"** → Don's own pie-menu principle pointed
    back at him: the novice's browse is rehearsal for the expert's
    blind path; `/` as the hard separator, `-` as the soft one;
    hierarchy *revealed by sort*, not imposed (`8bafe96c`).
21. **"isNotUnderstood or whatever it's called from smalltalk /
    objective c / etc."** → The whole trapdoor lineage from an
    approximate name: `doesNotUnderstand:`, `forwardInvocation:`,
    `method_missing`, `__getattr__`, `AUTOLOAD`; NeXT Distributed
    Objects as production architecture living in the failure path;
    the soft tier as DNU promoted to peer dispatcher (`1c8e3d9a`).
22. **"The file name suffix is like a type declaration telling the
    llm whether to consider it yml text, or run a png through the
    vision tool."** → The little-endian caboose; the extension as
    a guard on the reader dimension, dispatching perception; MIME
    types as coordinate guards worn on the name all along
    (`654a22bc`).
23. **"We are basically coming up with a way of tilting your head
    in multiple dimensions at once... like NeWS class.ps respects
    the PostScript dictionary stack. Trying not to invent new
    things."** → The constitution, stated once: *Interpret, don't
    invent* — the class.ps precedent, the itemized head-tilt
    table, the removal lineage Self → Korz → Korz′ ending with the
    removal of the requirement that anything new exist
    (`2d3c0e96`).
24. **"Paths can also be urls with # or ? that drill down into
    file structure... row, column, cell of a csv... why not
    higher dimension spreadsheets?"** → The standards were already
    there: RFC 7111 (CSV row/col/cell/region), JSON Pointer, RFC
    5147, W3C Media Fragments (time and pixel regions); HDF5/
    NetCDF hyperslabs; **Zarr** — an N-D array stored as a
    directory tree, the head-tilt in reverse; numpy strides
    proving dimensionality is a reading; array dimensions and Korz
    dimensions unify, the sea as sparse tensor (`235ad4b2`).
25. **"Wow drilling into zip files tgz files and sims object files
    and far files containing object files! of course!"** → The
    recursion step: archive suffix turns file back into directory;
    `mount` as the reinterpretation operator;
    `objects.far#/troll.iff#/BHAV/4096` — and Transmogrifier
    walked that path twenty-five years ago, it just never got
    written as a URL (`eba51ad0`).
26. **"So the headers of a csv could bind to dimension names. How
    would that work?"** → The relational reading: header row
    declares guard dimensions, each row pours a slot into the sea;
    the three guard stances land on cell syntax with nothing left
    over (empty = unmentioned, `*` = bare, value = constrained);
    three ancestors who didn't know they were doing Korz —
    decision tables, Codd, tidy data; the dispatch-CSV as a second
    compiler target (`cd1ec442`).

## What kind of rabbits

Sorting the two dozen dereferences by species:

- **Named ancestors** — Hoare, Codd, Knuth, Wickham, Rumsfeld,
  decision tables, Postel. The pointer names a concept; the
  ancestor arrives with dates and receipts.
- **Standards nobody remembers exist** — RFC 7111, RFC 6901, RFC
  5147, Media Fragments, Zarr's chunk naming. The uniform notation
  Don asked for turned out to be already ratified, just federated.
- **Don's own career, pointed back at him** — pie menus (the
  self-revealing soup), Transmogrifier (the FAR/IFF drill),
  class.ps (the constitution), his 2024 HN comment (the null
  trinity). The richest K-lines in this session's latent space
  were autobiographical; the model's job was recognizing when the
  pointer and the pointee had the same author.
- **Mechanical fits** — the ones that carried real design risk:
  guard stances onto CSV cells, Rumsfeld onto isKnown, virtual
  memory onto K-line paging. A metaphor that almost-fits is a mood
  board; these fit with nothing left over, which is what earned
  them table form in the document.

The isKnown lesson applies reflexively: every rabbit above was a
high-isKnown dereference — dense, consistent, cheaply verifiable
training knowledge. The session produced no zorbleflax. When a
pointer was vague ("isNotUnderstood or whatever"), the referent
wasn't — which is exactly the asymmetry Postel's law exploits and
the reason pointing beats spelling.

## Part of the pattern

This file is itself a resident page: the session is the backing
store, cursor-mirror is the fault handler that read it, this page is
the cached distillation, and the commit that carries it is the
provenance stamp. If it's wrong, fix it in place — a wrong page gets
fixed, not evicted.
