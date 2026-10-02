# HyperTIES: the good parts

Ted never took Xanadu to the other systems. He waited for the mountain. HyperTIES can go.
Crockford's move was the same one: keep the parts that work, speak the languages that exist,
leave the week-long C++ compile on the table.

The host is HyperTIES, running. The organelles are Xanadu's EDL, gwern's `.md` + include-links,
RSS items, YouTube, a Micropolis command, a room. Engulfed, not digested.
[Endosymbiosis](../../object-system/ENDOSYMBIOSIS.md).

The running organism is [`apps/ties`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ties)
at [hyperties.org](https://hyperties.org). Static today. The jump to a server is already one
variable (`SVELTE_ADAPTER=node`). This file says what that jump is *for*.

## The object was right. The grain was wrong.

A git log, an RSS feed, a blog, a podcast, a Sims family album, a tour, a Xanadu EDL, and a
webtop view are **one object**: an ordered list of references to spans of other documents,
plus optional connective tissue.

Gwern built a git→RSS bridge and killed it. The object (a chronological list of what changed)
was correct. The **grain** was every commit. He printed the last forty patches as the exhibit
([gwern/gwern.net#11](https://github.com/gwern/gwern.net/issues/11)):

> "lint" · "+commafy number pass" · "second EN DASH pass" · "+lns" · "lint" · …

A reader who wants *writing* cannot subscribe to *file events*. That is why Wikipedia Recent
Changes is unreadable as a magazine, and why a `git log` of this repo is not a newsletter.

The opposite grain also fails. Classic RSS assumes a URL is born finished, announced once, and
then only trivially edited. Gwern finishes a major page maybe once a month and then keeps
rewriting it for years. A feed of "new URLs" misses the work. A feed of "last-modified flipped"
re-announces the same abstract a dozen times without saying *what changed*.

Three clocks, one object:

| Clock | Grain | What you get |
|---|---|---|
| Git | every patch | Noise. Formatting, lints, linkrot, splits. |
| Blog RSS | every new URL | Silence. Living essays do not appear. |
| Semantic | a new annotation, a new essay, a *meaningful* revision | A thing a human would tell a friend |

Issue #11 is him designing the third clock. Annotations are the atoms. Full annotations and
essays get their own items. Partial ones roll up weekly. When an old essay's `modified` date
moves, an LLM reads the month of diffs and writes *what changed*, skipping spellcheck.
Same list, presented as RSS *or* as transclusion + collapse — "just rearrange a few
links/div-wrappers." He will not half-ass a blog feed because a feed is a promise, and he is
still paying 404s from the Gitit-era URLs he deleted a decade ago.

**A view is that list with the grain chosen by a reader.** You subscribe to Don's trail through
`/xanadu`, not to gwern's git, not to a pretend blog. HyperTIES stores and serves the view.
That is richer RSS: each item is a transclusion with a definition, not a title and a permalink.

## Why a server

The corpus stays files. Caddy serving 138 prerendered HTML pages from a symlink is the correct
default — nothing running, nothing to fall over, rollback is `ln -sfn`. Keep it.

A browser on `hyperties.org` cannot `fetch('https://gwern.net/xanadu.md')`. CORS. iframe works
and is a foreign room with no chrome we own. The mountain-to-Mohammed move needs a **same-origin
proxy**: we fetch, he does not change a header.

That is the first thing only a server can give. The second is **saving and sharing views** —
an EDL that is not trapped in LocalStorage on one laptop.

```
GET /proxy/gwern/xanadu.md          → text/markdown, as served
GET /proxy/gwern/xanadu             → HTML, extract #markdownBody if asked
GET /proxy/gwern/xanadu.md#foo:bar  → range, his include-link protocol
GET /view/:id                       → an EDL, rendered as a HyperTIES article
PUT /view/:id                       → save (git, or a small store)
GET /view/:id.rss                   → the same EDL at RSS grain
```

`SVELTE_ADAPTER=node` is already wired. The Caddyfile for that mode is
[`hyperties-node.Caddyfile`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ties/deploy/hyperties-node.Caddyfile):
static files still come off the symlink; `/proxy` and `/view` go to the node process.
Articles do not become dynamic. The server is the lid, not a rewrite of the corpus.

Respect: cache what we fetch, attribute the source, never merge his `.md` into ours.
The amsterdank rule — reference by ID, or the licence swallows the repo — applies to gwern
the same way it applies to OSM.

## The good parts of Xanadu (the rest can stay in 1999)

Keep:

- **EDL** — a document is a sequence of spans into other documents, plus links.
  Recovered live in [XANADU-RESCUE.md](../../XANADU-RESCUE.md).
- **Xanalink** — the link is a document with two named facets. Both ends can know.
  [PAIRED-LINKS.md](../../PAIRED-LINKS.md).
- **Visible connection** — the quote is not copied; it is fulfilled at read time.
- **Transclusion** — WelcXu, quote, WelcXu, quote.

Leave: the unreadable Smalltalk→C++ dump, the one-way `perma.pub` fulfiller, the patent that
killed ZigZag's Finnish team, waiting for W3C to apologize.

Addresses in the EDL are **polymorphic**. Xanadu used `url,start,length` (bytes). Gwern uses
`url#id` and `url#foo:bar` (element ranges). HyperTIES uses `~name~` (resolved in three
namespaces). A view is allowed to mix them. The fulfiller dispatches on the address kind.
That is speaking their languages.

## Re-interpolate the 1988 pages as EDLs

Do not rewrite the prose. Do not invent a new look. The converter already did the honest half:
`.st0` → markdown + YAML frontmatter + ` ```target ` islands ([FORMAT.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ties/FORMAT.md)).

An article *is* already an EDL, with nicer addresses:

| 1988 | EDL span |
|---|---|
| `.contents` prose | host connective tissue (inline, because *he* wrote it) |
| `~name~` | xanalink by name, both ends in the index |
| `.picture` / `.target` | span into a picture, geometry in `shapes/<slug>.svg` |
| `.definition` | the preview span — mandatory, the rung the web dropped |

Internal representation: that list, plus a [TIES.yml](../../../skills/ties/TIES-SCHEMA.yml)
for the node (screen, cost, typed ties, any type). Look and feel is a **skin**. The 1988
monochrome encyclopedia, a gwern-dark page, a Micropolis window — same EDL, different
fulfiller chrome. Pluggable the way Gonzo kernel / skin pack already split.

The 1988 databases stay derived. `pnpm convert` regenerates `examples/`. Never hand-edit.
A view *over* them is a new file in *our* tree, pointing at their names.

## What HyperTIES speaks

Going to meet them, each in their own words:

| Them | We fetch | We store | We show |
|---|---|---|---|
| HyperTIES 1988 | converted `.md` + `index.yml` | TIES + EDL of names | definition on single click |
| gwern.net | `url.md`, `#markdownBody`, `.include` / `#foo:bar` | view EDL of his URLs | our chrome, his text |
| Xanadu | live sources + archived EDL | EDL as text | visible connections |
| RSS / Atom | their feed | same object, their grain | a view |
| YouTube | oEmbed / iframe | a span with a time range | a window |
| Micropolis / Soul City | nothing remote | commands on the [bus](https://github.com/SimHacker/MicropolisCore/blob/main/apps/micropolis/src/lib/CommandBus.ts) | pie, edge strip |

A gwern annotation fragment is his TIES `definition`. We do not ingest GTX. We tie to the
URL and let his fragment fill the preview rung when the proxy can see it.

## Commands

Windows respond to the command bus. Pie menus dispatch command IDs. Edge strips are curated
`Command[]`, justified to corners. `open-view`, `pin-span`, `proxy-fetch`, `save-view`,
`share-view` are webtop commands, not a second menu system. An LLM proposes. The reader
approves. Nenex's side pane was the placeholder; the pie is the gesture.

## The static site does not die

Prerendered articles, symlink releases, six names folding to `hyperties.org`,
`hyperties.com` is not ours. All of that stays. The server is an organelle the static
host swallows when a page needs a fetch it cannot do from the browser, or a view it
cannot keep in LocalStorage. Flip `SVELTE_ADAPTER=node`. Deploy with `--mode node`.
Rollback is still a symlink.

↑ [pack](README.md) · [Xanadu rescue](../../XANADU-RESCUE.md) · [TIES](../../../skills/ties/) · [ties app](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ties)
