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

## The pun is load-bearing in three directions

**Cursor** (text editing): a position in a substrate, which can move, which you can have several of,
which anchors a selection. Engelbart had multiple cursors; the idea is old and mostly unshipped.

**Read head** (disk, tape): a physical thing that seeks over a medium, reads only where it is, and
has locality — near is cheap, far is a seek.

**Character** (MOO, adventure, MOOLLM): an entity whose `location:` is where it is, which carries
inventory, remembers where it has been, and can be someone other than you.

All three are *a position in a substrate, with state, that moves.* MOOLLM implements the third
already, which means the first two arrive free. What the character has that a bare cursor does not:

- **Inventory** — what it picked up along the way. `TAKE REF` is weightless, so a cursor accumulates
  pointers without copying ([`skills/inventory/`](../../skills/inventory/)).
- **A path** — where it has been, in order, which is an itinerary, which is
  [testimony](../pie-stack-views/VIEWS-AS-TESTIMONY.md).
- **A register** — the rung it reads at. `SUPERBRIEF`/`BRIEF`/`VERBOSE` becomes *per cursor*, so the
  same corpus is legitimately two different documents to two cursors at once.
- **An author** — it can be someone else's, which is the whole social tier.

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

## What plurality buys, which is where it stops being a bookmark

Once the position is an object rather than browser state:

**Several cursors in one corpus.** One parked in the technical appendix, one three levels into a
tangent you want to finish, one at the top of a thread you are arguing with. This is what browser
tabs pretend to be and fail at: a tab has no memory of how it got there, no inventory, and dies with
the session. Twenty open tabs is a cursor system with no persistence, no names, and no way to say
what any of them was for.

**Somebody else's cursor is a thing you can pick up.** Not "here is my reading list" — that is the
route, and it already exists in
[DISPENSERS-AND-SOUVENIRS.md](DISPENSERS-AND-SOUVENIRS.md#reading-lists). This is *the position on
it*, with what they had picked up when they stopped. Handing someone a route says where to go;
handing them a cursor says where you are and what you are carrying. Forking one and walking it
forward is a reply.

**The author's cursor through his own corpus is content.** gwern re-reads his own pages constantly —
that path, published, is a tour nobody can reconstruct from the link graph.

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

## Honest costs

**A cursor that is a character invites cuteness, and cuteness is a tax.** A reader who wants to
resume an essay does not want to name a golem, pick a face, or be greeted by anything. The default
cursor must be nameless, invisible, and expressed as *continue where you left off* — one affordance,
no ceremony. The character surface is opt-in and only pays for itself once you have more than one, or
once you want to hand one to somebody. Violating this breaks the rule
[PLAYABLE-CORPUS](PLAYABLE-CORPUS.md#honest-costs) already sets: nobody is ever told they are
playing.

**Plurality needs a focus story or it becomes modes.** Engelbart's multiple cursors were for multiple
*people*, where "which one is you" answers itself. Several cursors for one person is the case that
goes wrong — two carets competing for a keystroke is the classic mode error. The provisional
discipline: exactly one cursor is active, it is visibly named, and the others are a *list* you switch
to deliberately, never a second caret on screen.

**A reading cursor is a worse privacy surface than inventory, not a comparable one.** Inventory
records what you took, which is roughly what you liked. A cursor records **where you stopped** —
which is where you got bored, lost, or angry, and which paragraph did it. That is more intimate than
a bookmark and far more intimate than analytics, because it is per-argument rather than per-page.
Local by default is not politeness here, it is the requirement; and publishing one should show you
its exact contents first, since the interesting part is the part you would not think to check.

**Resumption is sometimes the wrong move.** The cursor makes it cheap to jump back in with false
confidence that the context is still loaded, when what you needed was to re-read from the section
head. A cursor that reports its own staleness — elapsed time, commits since, what changed above you —
makes that judgment available instead of assuming resume; but the failure mode is real and the
default should offer both.

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
