# Gwern.net architecture — what it is and how it works

**Source:** sister clone `~/GroundUp/git/gwern.net` (shallow, 315 MB, HEAD 2026-08-05).
**Scope caveat:** this repo is the **engine, not the corpus**. It is Gwern's `static/` tree.
The essays (`*.md`), the annotation databases (`metadata/*.gtx`), the embeddings
(`embeddings.bin`), and the built `_site/` all live in his private `~/wiki/` working tree;
`build/Config/Misc.hs` hardcodes `root = ~/wiki/`. What's public here is everything that
*processes and presents* the corpus.

## The one-paragraph model

Gwern.net is a statically compiled document corpus with a dynamically composed chrome layer.
Markdown compiles through Hakyll + Pandoc with a long AST-rewrite pipeline (interwiki,
annotations, archiving, inflation adjustment, typography, link icons). A four-tier link
metadata database (GTX format) generates thousands of standalone annotation HTML fragments —
effectively a second site — which the frontend JS composes into popup windows, backlinks,
similar-links, and transclusions at read time. External links are preemptively archived
locally against linkrot. LLMs sit only at the edges: metadata cleanup and embeddings, never
page generation. Delivery is nginx + SSI + immutable versioned assets + a 43,000-rule
redirect corpus that treats every URL ever published as permanent.

## Directory inventory

| Path | Size | Files | What |
|------|------|------:|------|
| `font/` | 140M | 1024 | Webfonts + per-letter dropcap fonts (dropcap art is ~126M of it) |
| `img/` | 35M | 296 | Logos, link icons, patterns, ornaments |
| `build/` | 3.9M | 136 | Haskell (75 .hs) + Python (15) + shell (12) + PHP build tools |
| `nginx/` | 3.7M | 7 | Server config; `move.conf` ~13k + `broken.conf` ~30k redirect rules |
| `js/` | 2.7M | 39 | Frontend: ~29k hand-written lines + generated bundles (~66k total) |
| `css/` | 1.3M | 22 | Hand-authored + GENERATED/VERSIONED bundles |
| `template/` | 104K | 17 | Hakyll page shell + Pandoc shells + transclude templates |
| `include/` | 60K | 5 | SSI fragments: head, asset links, navbar, footer |

## Build + deploy cycle

`build/sync.sh` (~2,175 lines) is the real orchestrator; Hakyll is just its compile core:

1. Dependency check (~50 tools: ghc, pandoc, emacs, chromium, openai, ocrmypdf, …), disk check.
2. Pull Said Achmiz's infrastructure repo (the JS/CSS is co-maintained; daily merge).
3. Mass house-style rewrites (`gwsed.sh`), compile Haskell binaries.
4. Cron-gated expensive passes: `generateSimilarLinks` (embeddings), `linkSuggester`.
5. Annotation one-shot pass, `generateLinkBibliography`, `generateDirectory` (tag indexes).
6. Main `hakyll build`: markdown → Pandoc AST → `pandocTransform` walk → `default.html`.
7. Post-passes: static MathJax, HTML tidy, syntax highlighting, sitemap, font-subset inventory.
8. A very large lint suite (anchors, W3C, redirect dedupe, image dimensions…).
9. Deploy: rsync to Hetzner (checksum), Cloudflare cache purge on touched URLs.

Key entry points: `app/hakyll.hs` (site compile), `app/preprocessMarkdown.hs`,
`app/generateBacklinks.hs`, `app/generateSimilarLinks.hs`, `app/generateDirectory.hs`.
The `pandocTransform` ordering lives at `app/hakyll.hs:428-445`.

## The three subsystems (detail docs)

| Doc | Subsystem | Moat |
|-----|-----------|------|
| [FRONTEND-POPUPS-WM.md](FRONTEND-POPUPS-WM.md) | JS pop-frame window system | A real WM in 2.7k lines of vanilla JS |
| [LINK-PIPELINE.md](LINK-PIPELINE.md) | Haskell link/annotation/archive pipeline | GTX tiers + preemptive archiving |
| [STYLING-AND-DELIVERY.md](STYLING-AND-DELIVERY.md) | CSS, templates, fonts, nginx | Derived dark mode, SSI hot-patch, URL permanence |
| [LLM-IN-THE-LOOP.md](LLM-IN-THE-LOOP.md) | The LLM tool suite | Single-purpose guarded GPT scripts (sister-script parallel) |

## Most interesting parts, ranked for MOOLLM webtop relevance

1. **The pop-frame abstraction** — one windowing API (`spawn / fill / titlebar / pin /
   tile`), two providers: `popups.js` (desktop, drag/resize/tile/minimize) and
   `popovers.js` (mobile, stacked sheets with history). Mobile is a different windowing
   *model*, not a CSS tweak. This is the seed of our webtop window class.
2. **Include-links as intermediate representation** — `transclude.js` makes
   `<a class="include">` the universal content bus: page body, popups, lazy footers
   (backlinks/similars/bibliography) all load through one path. Our rooms/tabs should
   speak the same IR.
3. **Keyboard tiling** — configurable keystring `aswdqexzfrcvtgb` snaps focused popups to
   halves/quarters/full, plus pin/collapse/minimize/z-cycle. A desktop WM vocabulary hiding
   inside a scholarly website.
4. **GTX four-tier annotation DB** — `me/full` (hand-written) → `half` (tagged) → `auto`
   (scraped/LLM cache). Trust tiers for metadata, append-friendly line format. Directly
   inheritable for yaml-jazz link metadata.
5. **Preemptive link archiving** — every external link queued on first sight, archived via
   headless Chromium + SingleFile after a delay, HTML rewritten to the local mirror with
   `data-url-original` preserved. Linkrot defense as compile pass, not afterthought.
6. **LLMs at the edges with hard guardrails** — title cleaner output must be a substring of
   input; scrape failures cached as Temporary vs Permanent. The discipline matters more
   than the models.
7. **Derived dark mode** — one light palette (`colors.css`) machine-inverted through Oklch
   to generate the dark palette. One source of truth, two themes.
8. **URL permanence as data** — 43k redirect rules, Lua fuzzy-404 canonicalizer, 404 hit
   logging feeding repair. Plus `Accept: text/markdown` content negotiation serving raw
   markdown to LLM clients.
9. **notificationCenter with phases** — pub/sub event bus where handlers order themselves
   into named phases (`transclude → rewrite → eventListeners`), so injected content is
   processed deterministically. The webtop needs exactly this for windows spawning windows.
10. **Sidenote geometric packer** — footnotes become margin sidenotes via
    obstacle-avoidance layout (proscribed ranges → free cells → packing). Margin as UI
    surface.

## What Gwern.net does NOT have (our openings)

- No collaboration surface: solo corpus, PRs to one repo. (Repo Show / GitHub-as-MMORPG.)
- No simulation: documents only, nothing runs. (Micropolis wasm, Soul City.)
- No spatial navigation: tags and links, no rooms/zoom/memory palace.
- No user-rearrangeable desktop: popups die on page navigation; no persistent workspace.
- LLM is a build tool, not a resolver: no runtime intelligence, by design (static-first).

↑ [design pack README](../../README.md) · workflow: [ANALYSIS-WORKFLOW.md](../../ANALYSIS-WORKFLOW.md)
