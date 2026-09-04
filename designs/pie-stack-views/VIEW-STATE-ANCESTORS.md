# View State Ancestors

*Don Hopkins · September 2026*

**Thesis:** View state as authored, shareable content is not a new proposal. It shipped in NLS as viewspecs, was described in *As We May Think* as trails, and is sitting in every OPML file on disk as `expansionState`. The reason it never felt like content is that nobody gave it an author, a date, and a URL.

Part of the **pie-stack-views** design cluster ([README](README.md)). The data model: [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md). What views mean socially: [Views as Testimony](VIEWS-AS-TESTIMONY.md).

---

## The receipt: OPML already shipped this

OPML 2.0 has an `expansionState` attribute on `<head>`: a comma-separated list of line numbers identifying which outline nodes are expanded when the document opens. It is stored *in the document*, not in a preferences file, and it travels with the file when you send it to someone.

That is the entire argument, already implemented and already in the wild, by Dave Winer, whose lineage from ThinkTank through MORE and Frontier to Radio UserLand is the outliner spine this cluster inherits from. The outliner tradition never separated "what the document says" from "how the document is currently opened," because in an outliner those are obviously the same artifact: an outline that arrives fully collapsed and an outline that arrives opened to the argument are different documents in every way that matters to a reader.

The flaw in `expansionState` is the one worth fixing rather than repeating: it addresses by **line number**, so any edit silently invalidates it. Paths, not offsets, or the view degrades into a confident lie.

## Engelbart's viewspecs

NLS separated content from view specification — how many levels deep, whether to truncate lines, what to show and hide — as a compact code you could set, change, and hand to someone. The 1968 demo shows Engelbart reshaping the same file into different views live. Views were a first-class control surface, not a preference panel, and a viewspec was short enough to say out loud.

PSIBER's *View Characteristics* section is the same idea made per-subtree with an inheritance rule and a legibility floor ([Peripheral Views](PERIPHERAL-VIEWS.md)), which is where the modern overlay model actually comes from.

## The third tradition: adventure games shipped a rung selector in 1977

`VERBOSE`, `BRIEF`, and `SUPERBRIEF` are viewspecs. Per-reader, persistent across the session, set by the reader, applying to everything described thereafter — the same control Engelbart had in NLS a decade earlier, and the same thing OPML later stored as `expansionState`. **Three independent traditions concluded that a document needs a view knob, and only the web shipped without one.**

Two details make the 1977 version more advanced than the modern summary ladder rather than merely earlier.

**`BRIEF` is adaptive**, and it was the default. It is not a fixed detail level: it is *full on first encounter, name only thereafter*, which makes detail a function of what this reader has already seen. A rung with memory, spending words exactly where they are new. Every modern summary ladder — including the one this hub has been describing — is a static setting by comparison.

**`LOOK` is a peek that does not change the setting.** It redisplays in full regardless of the current mode, then leaves your preference untouched. That is precisely the popup contract gwern's link popups implement, and precisely the [reselection](RESELECTION.md) gesture of browsing a consequence before committing to it. The 1977 interface had both a persistent viewspec *and* a one-shot override, and kept them distinct.

The generalized rule — every describable thing answers at every rung, with `GLYPH` and `INFODUMP` added at the ends — is now a stated requirement of the adventure skill: [`skills/adventure/SKILL.md` § The rung selector](../../skills/adventure/SKILL.md#the-rung-selector).

## Bush's trails

The memex passage is about view state, though it is rarely read that way:

> Thus he goes, building a trail of many items. Occasionally he inserts a comment of his own, either linking it into the main trail or joining it by a side trail to a particular item... Thus he builds a trail of his interest through the maze of materials available to him.

**The trail is the contribution.** The memex owner publishes the path, not a new document — and the inserted comment is attached to a position on that path rather than to a publication. The geolocated version of exactly this is the tour in [Views as Testimony](VIEWS-AS-TESTIMONY.md), and the spatial version is a card pinned to a place in [The Tower](THE-TOWER.md).

## Nelson's transclusion, corrected to vertical

Transclusion is quoting by reference rather than by copy, so the quoted thing stays connected to where it came from. Gwern's reading of where Xanadu went wrong applies directly to the view layer: transclusion should have been **vertical** — zoom levels of abstraction — rather than horizontal side-by-side raw text.

A shared view is vertical transclusion with a person's name on it.

The practical payoff is the one gwern names: once popups give you seamless navigation, you are already using transclusion everywhere, inside the popups. Making views first-class only means the popup can be *saved and sent*.

## A summary is a rung, not a remark

The consequence that took longest to see: a summary or comment about something is a shareable, reusable part of that thing's semantic pyramid. Not a reply beside it — a rung *on* it.

This is sharper than it sounds. A comment sits next to its target forever and is read by people who came to read the comments. A rung gets *used*: the next reader who zooms that document to abstract level sees your abstract, because it is the best abstract anyone has written. The contribution becomes load-bearing infrastructure rather than marginalia, consumed by people who never intended to read commentary at all — which is also exactly why authorship has to ride along structurally. The more useful a rung is, the more invisible its author becomes unless the format carries the credit.

## DreamScape: the browsing path as an editable tree

The strongest precedent is one that was built and never shown. **DreamScape** (Kaleida Labs, in
ScriptX, demonstrated at WWDC 1995) is recorded in Don's work history as *"the first iteration of
Memory Palace concept — adventure map editor where rooms bump together to connect. Precursor to
iLoci and MediaGraph and MOOLLM."* The demo that did not make it into the recorded session is the
one that matters here.

ScriptX could monitor the browser's **URL and return stack**, and assemble articulated branches into
trees representing your path through the web. Not a back button, not a history list — a tree you
could directly manipulate: pull branches apart, stick them back together, edit them.

That is Bush's trail with the missing verb supplied. Bush described building a trail and inserting
comments into it; he did not describe *restructuring* one, because a trail on microfilm cannot be
rearranged. An outliner can rearrange a tree, which was the whole structural complaint against Wave
below. DreamScape put browsing history into the one representation that supports rearrangement, and
made the rearrangement physical.

It also settles the ownership question that Wave fumbled. The tree is assembled on your machine, out
of your own traversal; it is yours before anyone decides to publish it. The `view:` record below is
the same object with a date and an author attached so it can leave the machine.

## Google Wave, and what it got right

Wave had the right instinct and partly worked: a conversation as a living document with playback, so you could watch how it got that way. It failed on ergonomics, on ownership — whose wave is this? — and on the absence of any credit or citation model. The structural complaint at the time was simpler: an outliner lets you arbitrarily rearrange the tree, and a Wave or a threaded discussion group does not.

Keep Wave's accumulation and playback. Fix the ergonomics, the ownership, and the crediting, and replace copying with transclusion.

## The unit

A **view** is a small, signed, git-native record. It points at material; it never contains a copy.

```yaml
view:
  id: 2026-09-04-webtop-pyramid-argument
  by: don-hopkins
  at: 2026-09-04T09:28:00+02:00
  of: designs/webtop/README.md          # or a graph, a map, a room, a city
  focus: sections/semantic-pyramid       # where the eye is
  expanded:                              # what is open, by stable path not line number
    - sections/semantic-pyramid
    - sections/semantic-pyramid/rungs
    - sections/pie-menu-glyphs
  collapsed_deliberately:
    - sections/honest-costs               # not an omission; a claim that it does not matter here
  rung: abstract                          # which pyramid level the body renders at
  overlays: [backlinks, provenance]
  camera: { zoom: 2.5, center: [x, y] }   # for maps, graphs, Micropolis, Mesa
  says: >
    The ladder does not stop at link-icon. It goes one rung further, to a glyph
    small enough to be a pie slice.
  answers: 2026-09-03-gwern-footnote-174  # this view is a reply to that view
```

`collapsed_deliberately` is the field that makes it testimony rather than a bookmark: closing something on purpose is a claim that it does not matter here, and it is the part a counter-view will attack.

Properties that follow from it being a record rather than a session: it is **addressable**, so opening the URL reconstitutes the view on the current material; **diffable**, because two views of one document diff as sets of paths; **citable**, so "see Don's view of §3" has a target; **attributed**, with credit riding through every transclusion; **answerable**, since `answers:` makes disagreement structural; and **durable against edit**, because paths degrade to a partial match that says so rather than silently pointing at the wrong paragraph.

## Reply with a view

The move that Wave and comment threads both lack is the **counter-view**. You claim the argument lives in §3 and collapse §5; I reply by re-expanding §5, collapsing §3, and zooming out one rung. I have not written a word and I have already made my case. Then I add one sentence saying why.

Cheaper than prose, more precise, and reviewable: the diff between your view and mine is exactly the disagreement with nothing else in it. The animated form — interpolating between two saved views and staking the intermediate state as a new position — is developed in [Views as Testimony](VIEWS-AS-TESTIMONY.md).

## Honest costs

**Path stability is the whole ballgame**, and it is the same work backlinks need, so it should be paid once. **Generated rungs drift**: two people opening one view may see differently-worded abstracts, so either pin the generated text into the record (bigger, honest) or accept drift and mark it. **View spam** is inevitable, because anything cheap to make gets made carelessly; most views should stay private. And a view record is **a second object that can rot independently** of its subject, which makes backlinks from document to views mandatory rather than optional — otherwise views become invisible orphans. That failure has a worked example in [The Tower](THE-TOWER.md), where a whole memory palace turned out to be wired in only one direction.

## Open

- Does a view pin a content hash (reproducible but stale) or track the head (live but drifting)?
- When several people have authored the same rung of the same target, which renders by default, and is the reader told there are others? [Peripheral Views](PERIPHERAL-VIEWS.md) supplies the structural half — one name, every binding, in scope order — but not the default.
- Are the view and the authored card one record type with two uses? Answering yes would force a single addressing scheme across documents, maps, rooms and scenes, which is a simplification worth the cost.

---

## Related

- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — the data model these records instantiate
- [Views as Testimony](VIEWS-AS-TESTIMONY.md) — the social layer, tours, argument by interpolation
- [Peripheral Views](PERIPHERAL-VIEWS.md) — PSIBER's 1989 implementation and its homoiconic basis
- [The Tower](THE-TOWER.md) — the pyramid as a building, and cards as contributions to a place
- [Temporal Semantic Zoom](TEMPORAL-SEMANTIC-ZOOM.md) — the same parameters keyed to time
- [webtop hub](../webtop/README.md) — the shell these live in; [gwern pack](../webtop/gwern/README.md) on the semantic zoom ladder; [winer pack](../webtop/winer/README.md) on the outliner lineage
- OPML 2.0 specification — `expansionState` on `<head>`
- Vannevar Bush, "As We May Think," 1945 — trails
- Engelbart, NLS/Augment and the 1968 demo — viewspecs
