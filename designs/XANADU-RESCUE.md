# The Pale Fire rescue

Ted Nelson's own demo of visible transclusion, linked from the front of xanadu.com, is a one-way
jumplink into a dead host. That is the failure mode he has been describing since 1965, and it happened
to his own demo.

`https://xanadu.com/demo/` in full, as served today:

```html
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Pale Fire demo</title>
    <meta http-equiv="refresh" content="0;URL='http://perma.pub/alpha/edward/openZRe7/fulfil'" />
  </head>
  <body>
    <p>This page has moved <a href="http://perma.pub/alpha/edward/openZRe7/fulfil">here</a>.</p>
  </body>
</html>
```

`perma.pub` does not resolve. Not a 404 — no connection at all, over http or https, on any path.

This is not a gotcha. It is the argument, demonstrated on the best possible victim, and it is worth
fixing rather than pointing at.

## What is actually recoverable, measured

All of the following was probed on 21 September 2026.

| Thing | State |
|---|---|
| `xanadu.com/demo/` | **live**, 200, and contains only the meta-refresh above |
| `perma.pub` (any path, http/https) | **dead**, no connection, curl code 000 |
| `perma.pub/alpha/edward/openZRe7/fulfil` in Wayback | **archived**, `20190808172804`, HTTP 200, **28,513 bytes** |
| `perma.pub/alpha/edward/pnelO5dK/fulfil` in Wayback | archived, `20211025125844`, 200, 11,956 bytes |
| perma.pub generally | richly archived: `/alpha/`, dozens of `/alpha/edward/<id>` docs, and **`/edit`, `/history`, `/xanaedit`** endpoints |
| `hyperland.com` | **LIVE** |
| `hyperland.com/xuCambDemo/WelcXu-D1y` | **live**, 857 bytes — Ted's own welcome document |
| `hyperland.com/xuCambDemo/J.Ineffable.txt` | **live**, 3,281 bytes |
| `hyperland.com/xuCambDemo/McKinleyAssassination.txt` | **live**, 46,734 bytes |
| `hyperland.com/xuCambDemo/rmq41-xanalink.txt` | **live**, 237 bytes — a link, as a document |
| `xanadu.com/xanadox/MoeJuste/sources/*.txt` | **live** over https, 301 from http |
| `perma.pub/links/*.xanalink.txt` | dead with the host |

**The sources are still on the web. Only the fulfiller died.** That changes the job from archaeology to
a build.

## The formats, recovered

### The EDL

An Edit Decision List: a document is a sequence of spans into other documents, plus links. Recovered
verbatim from archived query strings on `perma.pub/xanaviewer1/fulfil_edl.json?edl=...`:

```
span: http://hyperland.com/xuCambDemo/WelcXu-D1y,start=25,length=565
span: http://xanadu.com/xanadox/MoeJuste/sources/0-Moe.pscr.txt,start=7995,length=274
span: http://hyperland.com/xuCambDemo/WelcXu-D1y,start=592,length=37
span: http://xanadu.com/xanadox/MoeJuste/sources/2-DarwinDescentOfMan.txt,start=143522,length=213
span: http://hyperland.com/xuCambDemo/WelcXu-D1y,start=630,length=55
span: http://hyperland.com/xuCambDemo/J.Ineffable.txt,start=299,length=343
span: http://hyperland.com/xuCambDemo/WelcXu-D1y,start=687,length=51
span: http://hyperland.com/xuCambDemo/J.Ineffable.txt,start=2879,length=376
span: http://hyperland.com/xuCambDemo/WelcXu-D1y,start=740,length=115
xanalink: http://perma.pub/links/hide_new.xanalink.txt
xanalink: http://hyperland.com/xuCambDemo/rmq41-xanalink.txt
xanalink: http://hyperland.com/xuCambDemo/mexn86-xanalink.txt
xanalink: http://hyperland.com/xuCambDemo/jjq7941-xanalink.txt
```

Read the alternation: **WelcXu, quote, WelcXu, quote, WelcXu, quote.** The host document is connective
tissue and the quoted material is pulled from the original at read time. That is transclusion, and
this is what its wire format looks like.

### The xanalink

A link is a **document**, fetched live from `hyperland.com`:

```
rmq41-xanalink

# "to a historical piece"

type=typeless

facet=
span: http://hyperland.com/xuCambDemo/WelcXu-D1y,start=301,length=30

facet=
span: http://hyperland.com/xuCambDemo/McKinleyAssassination.txt,start=358,length=108

  # =30=
```

Two **facets**, one per end, each a list of spans. Both ends are named in one artifact that is neither
end.

This is the strongest evidence available for the argument in [PAIRED-LINKS.md](PAIRED-LINKS.md): Ted's
own implementation made the link a first-class document naming both ends, which is why both ends can
know about it. A `type=` field means link types were always in the design.

### The host document, which shows the holes

`hyperland.com/xuCambDemo/WelcXu-D1y`, live, 857 bytes, complete:

> WELCOME TO XANADU® HYPERTEXT
>
> Theodor Holm Nelson, founding designer, Project Xanadu
>
> We offer a different kind of document. [...]
>
> We believe that links should be visibly connected.
>
> Here's a xanalink to a historical piece--
>
> [...] We believe that sources should be directly available from each quotation.
>
> Consider this quote on the Origin of the Universe (by "Moe Juste")--

The quotes are **not in the file.** "Consider this quote ... --" and then nothing, because the quote
lives in `0-Moe.pscr.txt` and arrives at read time. The document is unreadable without a fulfiller,
which is exactly why the demo dying killed it dead.

## The spans still resolve — this is the finding that matters

Fetched the live sources and sliced them at the offsets the xanalink declares:

| Facet | Span | Resolved text |
|---|---|---|
| 1 | `WelcXu-D1y` start=301 len=30 | `" xanalink to a historical piec"` |
| 2 | `McKinleyAssassination.txt` start=358 len=108 | `"The 25th President of the United States, William McKinley, was shot and fatally wounded on September 6, 1901"` |

Byte offsets, zero-based, length in bytes. Facet 2 lands cleanly on exactly the sentence a human would
have selected. Facet 1 drifts by one character, which is a hand-made anchor in a demo rather than a
format problem — worth pinning down the indexing convention before claiming otherwise.

**A client-side fulfiller is viable today, against the live web, with no server.**

## The build

Four steps, in order, each one useful alone.

1. **Rescue the evidence.** Pull the archived `openZRe7/fulfil` (28KB, 2019) and `pnelO5dK/fulfil`,
   plus `/alpha/`, the `/edit`, `/history` and `/xanaedit` pages, and every `fulfil_edl.json` query
   string. Commit them as received, with Wayback timestamps, unmodified. This is the part that stops
   being possible if the Archive has a bad year — and it was **intermittently offline during this very
   probe**, which is the whole argument for doing it now.
2. **Extract the EDLs** into plain text files, one per document, in the format above. Small, diffable,
   reviewable.
3. **Write the fulfiller.** Static JavaScript: fetch each span's source, slice by start/length,
   concatenate, and render the xanalinks as **visible connections** rather than jumplinks. Ranged
   requests where a server allows them, whole-document fetch and slice where it does not. Fall back to
   a vendored cache when a source is gone.
4. **Publish on GitHub Pages.** The EDL is data in the repo, the fulfiller is code in the repo, the
   sources are fetched live with a cached fallback, and the whole thing is forkable.

Then the Pale Fire demo works again, at a URL that will still be there, and anybody can fork it.

## Why this is the dogfood argument, not just a favour

The claim in [editing-history/BRANCHING-TIMELINES.md](editing-history/BRANCHING-TIMELINES.md) is that
a clipping belongs in a repo, because a repo gives you visibility, durability, history, blame, forking,
and review for free. The Pale Fire demo is that claim's test case, and it is self-referential all the
way down:

- The artifact is **a demo of transclusion**, dying because its content lived somewhere that stopped
  answering the phone.
- The rescue **is** transclusion: harvest pointers, excerpts, and local caches as you travel, with
  provenance on each one, into a repo, to hand to somebody else. Which is the harvest protocol in
  [SONG-FORM.md](SONG-FORM.md) and the trail in [PAIRED-LINKS.md](PAIRED-LINKS.md).
- The thing that killed it is **the one-way link**. The thing that fixes it is a link with both ends in
  one reviewable artifact, which is what a xanalink already was.
- A generated, unreadable, unpublished artifact is the exact charge Don made against the 1999 Udanax
  release. Doing this one **readable and published** is the answer to his own criticism rather than a
  repetition of it.

Evidence beats argument, and this is evidence with a URL.

## Credit, permission, and posture

The work is **Ted Nelson's** design and, for the perma.pub implementation, **Edward Betts's** build.
The rescue is custodial. Rules for it:

- Credit both, prominently, at the top of anything published.
- Preserve the archived artifacts **unmodified**, separately from anything reconstructed, and label
  which is which on every file.
- Do not present a reconstruction as the original. A fulfiller written in 2026 is a new program that
  reads their format.
- **Offer it to them.** The right outcome is that this lands at `xanadu.com/demo` again, or that Edward
  takes the repo, not that we own a mirror. Ask before publishing widely; publish the rescue regardless
  if the answer is silence, because the alternative is that it stays dead.
- The `®` on "XANADU®" in Ted's own document is his. Respect the mark.

Good thing to bring to the conversation rather than a favour to announce afterward. See
[the Xanadu Ships show seed](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/ted-and-roger-xanadu-ships/README.md) —
Roger Gregory has a finished reimplementation waiting on Ted's sign-off, and a working demo of the
format is a useful thing for that release to have.

## Related

- [PAIRED-LINKS.md](PAIRED-LINKS.md) — links as documents with two named ends; the xanalink is the proof
- [SONG-FORM.md](SONG-FORM.md) — transclusion as the chorus; harvest as you travel
- [editing-history/](editing-history/README.md) — the repo as substrate; Nelson's provenance stripe
- [webtop/nelson/](webtop/nelson/) — the webtop's Nelson notes
