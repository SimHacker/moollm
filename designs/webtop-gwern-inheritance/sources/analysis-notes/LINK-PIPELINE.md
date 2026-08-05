# Gwern.net link pipeline: annotations, archives, backlinks, embeddings

**Source:** `~/GroundUp/git/gwern.net/build/` — 75 Haskell modules (~8.8k LOC top-level;
Config modules add much more), Hakyll 4.16 + Pandoc 3.1, package `gwernnet`. This is where
Gwern's moat actually lives: not the styling, the **link infrastructure**.

## Compile pipeline

`app/hakyll.hs` (602 lines). Each markdown page: YAML validation → Pandoc AST →
`pandocTransform` (`hakyll.hs:428-445`) → `template/default.html` → image-dimension pass.
The AST walk, in order: interwiki links → create missing annotations → page-link classes →
inflation adjustment → annotate links → localize to archives → typography (link icons,
live-link classes) → header self-links → paragraph wrapping → prefetch hints + image dims.

Every transform is a Pandoc AST walk — the "compiler pass over documents" pattern.

## GTX: the annotation database

`GTX.hs` (247 lines) defines a custom newline-delimited record format (replaced YAML —
no quoting/indent hell, append-friendly, diff-friendly):

```
URL
Title (HTML)
Authors (comma-separated)
Date YYYY[-MM[-DD]]
DOI / key-value pairs
tags (space-separated, must match doc/* directories)
Abstract (HTML, until ---)
---
```

`MetadataItem = (Title, Author, Date, DateCreated, [(K,V)], [Tag], Abstract)`
(`LinkMetadataTypes.hs:17-18`).

**Four trust tiers**, merged at load (`LinkMetadata.hs:208-211`):

| File | Trust | Content |
|------|-------|---------|
| `metadata/me.gtx` | highest | Gwern's own works |
| `metadata/full.gtx` | hand-curated | written/cleaned annotations |
| `metadata/half.gtx` | partial | tagged but not fully written |
| `metadata/auto.gtx` | cache | scraper/LLM output, append-only, may be stale |

On compile, every link without an annotation triggers `Annotation.linkDispatcher`
(`Annotation.hs:68-87`): arXiv API, bioRxiv/medRxiv scrape, OpenReview, PDF metadata,
local essays, generic title-scrape — results appended to `auto.gtx`. Failures cache as
`Temporary` (retry) or `Permanent` (empty stub, never retry).

**Output is a second site:** thousands of standalone HTML fragments under
`metadata/annotation/<urlencoded>.html` (plus `backlink/`, `similar/`,
`link-bibliography/` siblings) — exactly what the frontend pop-frames and lazy footers
fetch. Annotations are compiled once, composed everywhere.

## LinkArchive: preemptive linkrot defense

`LinkArchive.hs` (394 lines) + `Config/LinkArchive.hs` (1178 lines of domain policy).
Every external URL enters a queue on first sight (`Left firstSeenDay`); after a settling
delay, `linkArchive.sh` snapshots it with headless Chromium + SingleFile + uBlock into
`/doc/www/$DOMAIN/SHA1($URL).html`. The compiled HTML then points at the **local mirror**,
keeping the original in `data-url-original` (`LinkArchive.hs:77-80`); client JS swaps back
the original for copy/paste. Stable hosts (arXiv, Wikipedia…) are whitelisted out.
Archiving is rate-limited per build. PDFs always download.

Result: the site degrades gracefully as the web rots — readers hit the mirror, the
original stays one attribute away.

## Backlinks

`generateBacklinks.hs` parses all pages *and* annotation bodies into
`metadata/backlinks.hs` (target → [(fragment, [callers])]) and emits HTML snippets per
target. Bidirectional links, computed at build, served as fragments, lazy-loaded by the
same include-link mechanism as everything else.

## GenerateSimilar: embeddings

`GenerateSimilar.hs` (1610 lines). Shells to `embed.sh` → OpenAI `text-embedding-3-large`
(`GenerateSimilar.hs:388-417`); vectors stored in `metadata/embeddings.bin`. Exact cosine
nearest-neighbor for "Similar Links" popups; all-pairs distances feed **seriation** — 
tag-directory listings ordered so adjacent items are semantically adjacent. Top-20 kept,
distance cutoff ~0.95, refreshed by cron not per-build. Also drives `tagguesser.py`.

## Link decoration

- `LinkIcon.hs` + 1390-line rule config: compile-time `data-link-icon` attributes (SVG or
  1-4 char text badges) — moved from CSS matching to build-time for performance.
- `LinkLive.hs` + 4618-line domain corpus: whitelist of sites that work in live iframes
  (`link-live` class → FOREIGN_SITE popups). HTTP never live (mixed content).
- `LinkID.hs`: stable citation IDs (`author-year` or 8-char hash), exported as JSON for
  client-side `/ref/` resolution.
- `Interwiki.hs` + 6048-line config: `[Anchor](!W)` → Wikipedia, with redirect DB and
  disambiguation checks.
- `Inflation.hs`: `[$50]($1970)` → inflation-adjusted amounts (CPI/PCE, even Bitcoin) at
  compile time.

## Config-as-code

The dominant maintenance surface is not logic but **data**: `Config/Interwiki.hs` (6k),
`Config/LinkLive.hs` (4.6k), `Config/Metadata/Author.hs` (3.7k), `Config/LinkIcon.hs`
(1.4k), `Config/LinkArchive.hs` (1.2k), tag aliases (1k)… Logic modules stay thin; policy
lives in giant typed literal tables with unit tests (`Test.hs`, `Unique.hs` duplicate
detection). Twenty years of accumulated judgment, greppable and diffable.

## MOOLLM mapping

| Gwern mechanism | MOOLLM inheritance |
|-----------------|--------------------|
| GTX trust tiers | yaml-jazz link metadata with me/full/half/auto provenance |
| Annotation fragments | room/character/skill GLANCE cards served as popup content |
| linkDispatcher scrapers | skill-based resolvers; LLM fallback where Gwern uses heuristics |
| LinkArchive queue | mirror-and-cite skill for correspondence sources (we already archive) |
| Backlink DB | git grep is our backlink engine; could compile fragments the same way |
| Embeddings + seriation | cauldron-adjacent; seriation for room listing order is a steal |
| Config-as-code | our INDEX.yml / K-line files play this role — keep them typed and tested |

The deep lesson: **Gwern treats links as data with lifecycle** (discovered → annotated →
archived → backlinked → embedded), not as strings in markdown. A Repo Show that took links
that seriously would never lose a source.

↑ [ARCHITECTURE.md](ARCHITECTURE.md)
