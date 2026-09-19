# View State Is the User's

**Class:** lens · **Attribution:** Don Hopkins; Ted Nelson's clipboard argument; Bret Victor on remembering across sessions

> **The view the reader assembled by hand belongs to the reader. Destroying it is a
> data-loss bug, not a layout choice.**

Expansion state, scroll position, sort order, filter, selection, zoom, which
branches are open — a reader spends real clicks accumulating these, in a
particular order, to build a view of a document that does not exist anywhere
else. Then one wrong click collapses it, and there is no undo, no address for
where they were, and no way back except hiking the same path again click by
click. The document survived; the reader's *work on* the document did not.

## The asymmetry is the bug

Assembling the view costs N deliberate actions. Destroying it costs one accidental
one. Restoring it costs N again. Nothing in the interface acknowledges that the
first N happened.

That is the same shape as
[don't make undoing cost more than doing](../masters/don-hopkins.md), applied to
state the software never admitted was state. Compare Nelson's rage at the
clipboard — invisible, singular, uneditable, holding something of yours that you
are not allowed to look at
([VIEWS-AS-TESTIMONY](https://github.com/SimHacker/moollm/blob/main/designs/pie-stack-views/VIEWS-AS-TESTIMONY.md),
[READING-CURSORS](https://github.com/SimHacker/moollm/blob/main/designs/webtop/READING-CURSORS.md)).
Accumulated view state fails on the identical axes: you cannot see it, you only
get one, and you cannot edit or save it.

## Why it ships anyway

The default view is tuned for **arrival** — a stranger's first paint, an
engagement metric, a clean screenshot. The reader twenty minutes deep, who has
opened fourteen things in a deliberate order and is reading across them, is not
modeled at all. No one's day breaks, so the pressure to fix it never accumulates,
which is Alan Kay's diagnosis of why bad designs survive: they work a little bit.

## The specimen: Quora's three folds

Quora folds the same conversation in three independent mechanisms — feed-level
truncation behind an "interrupting cow" **(more)** button, comment collapse, and
nested-reply collapse — each demanding precise scrolling and hunting to defeat,
all of it blown away by one mistaken click, with the answer's other siblings
("1 of 6 answers") never shown at all. Reading one thread end to end is a manual
reconstruction job.

The tell that it is a real failure and not a preference: the workaround became an
artifact. Don's
[Alan Kay Quora recaps](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/alan-kay/media/quora-recaps)
exist because the only reliable way to read those threads is to expand everything
by hand once and re-publish it flat, top to bottom, quotable and linkable. When
readers start maintaining mirrors of your content in a different medium, that is
the bug report.

### The full chain, logged live, 19 September 2026

Worth recording because the anatomy above describes one fold mechanism failing, and what actually
happens is **five independent failures composing**, none of which is individually a scandal:

1. **`⌘W` while looking at a window on another screen.** Input focus and visual attention
   disagreed, so a one-keystroke destructive command hit a target the user was not looking at. The
   command names no object and confirms nothing.
2. **`⌘⇧T` restored the tab to the wrong page** — Quora's front page, not the question. The tab's
   restorable identity was the *site*, not the location.
3. **The original location did not survive a refresh at all.** The reading position was never in
   the URL, so there was nothing for restoration to restore. A client-side route is not an address.
4. **All three fold mechanisms reset**, so the assembled view went with it.
5. **The only recovery path ran outside the application.** The way back was to search *email* for
   the original link and start over.

That last one is the finding. **The most durable bookmark in the system was a piece of mail** —
an artifact in a different application, authored by a third party, which outperformed every
affordance the site offers for returning to a place inside it. When a reader's most reliable
address for your content lives in someone else's inbox, the addressing scheme is not merely weak,
it has been outsourced.

Don's term for the three folds, preserved because it names the register precisely and the register
is the point: *baboons showing me their asshole* — a **dominance display**, not an oversight.
(Aimed at the interface design, and he was careful to say so: not at anyone in the discussion.)
A fold that re-collapses your work is not saving space, it is asserting whose screen it is. Three
of them stacked is the assertion made three times.

The composition is also the lesson for the repair. Fixing any one link in that chain leaves the
chain intact — a real address (3) is what makes 2 and 4 recoverable, which is why
[READ-UNREAD](https://github.com/SimHacker/moollm/blob/main/designs/webtop/READ-UNREAD.md) puts
the reading position in a file with a name rather than in a tab's memory.

## The layer underneath: a verdict, not a position

Expansion state says where you *were*. It does not say what you **concluded**, which is the
state that decides whether a thread can be read twice. `visited` is a fact about the
machine's history; *read* is a verdict a reader issues, and it is not one bit — browser
history paints "skimmed" and "extracted three quotes from" the same purple.

Two additions to the test, then, for any reader interface:

- **Can the reader mark a verdict, and is the marking gesture one they are already
  performing?** Pointing and lingering is the candidate, because dwell has been instrumented
  since OpenLaszlo and is currently spent on predicting the next click and discarded.
- **Does a change arrive as a relit room on a map you know, or as a badge with a number?**
  Unread is a *diff* against the version you judged, not a flag — and the flag is why every
  feed makes you re-find your place.

Worked out, with the verdict lattice and the existing verb set it composes from:
[designs/webtop/READ-UNREAD.md](https://github.com/SimHacker/moollm/blob/main/designs/webtop/READ-UNREAD.md)

## The test

**After a wrong click, how many actions to get back to where I was?** Zero (it
didn't collapse) or one (undo) means the view state is the user's. Anything more
means the software considers it disposable and the user does not.

Second test, for anything with folds: **can you link to the expanded view?** If
the expansion cannot be addressed, it cannot be shared, bookmarked, restored, or
cited — and you have built a reading position that only exists inside one
browser tab's memory.

## What to do instead

Treat the assembled view as a document the user authored: **addressable**
(it survives in the URL), **restorable** (back and undo reach it), **saveable**
(name it, return to it), and **cheap to rebuild** (an expand-all that isn't
hidden). Collapse is fine — collapse is [foveation](foveation.md) and a
[semantic mipmap](semantic-mipmap.md) is built out of it. What makes a mipmap
honest is that every level is addressable, so folding is reversible by
construction rather than by re-hiking.

**Go deeper:**
Bret Victor, ["Magic Ink"](http://worrydream.com/MagicInk/) — software should
infer context from environment and history, remember across sessions, and ask the
user last ·
[Wikipedia: Scroll position restoration](https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration)
— the browser has an API for exactly this, routinely defeated by client-side
rendering

**See:** [calm-not-invisible](calm-not-invisible.md) — hidden state is the same
lie at rest · [foveation](foveation.md) and
[semantic-mipmap](semantic-mipmap.md) — the honest version of folding ·
[p-pyramid-attention](p-pyramid-attention.md) ·
[fitts](fitts.md) — the hunting-and-clicking cost is measurable, and folds put it
on the return trip · [../masters/bret-victor.md](../masters/bret-victor.md) ·
[../masters/don-hopkins.md](../masters/don-hopkins.md) ·
[../masters/ted-nelson.md](../masters/ted-nelson.md)
