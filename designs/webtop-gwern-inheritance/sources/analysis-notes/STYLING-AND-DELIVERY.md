# Gwern.net styling and delivery: CSS, templates, fonts, nginx

**Source:** `~/GroundUp/git/gwern.net` — `css/` (1.3M), `template/` (104K), `include/`
(60K), `font/` (140M), `nginx/` (3.7M), plus the PHP asset builders in `build/`.

## CSS organization

Hand-authored core: `default.css` (211K — layout, sidenotes, pop-frame chrome, dropcaps,
print), `initial.css` (64K — font stacks, base type), `links.css` (29K — underlines, link
icons), `colors.css` (12K — the light palette as `--GW-*` CSS variables), plus small
adjustment files. Everything else is GENERATED/VERSIONED and sacred: CONTRIBUTING.md
forbids hand-editing generated files; PHP builders regenerate them in a pre-commit hook.

Assembly (`build/build_unified_assets.php`): critical `head.css` (inlined) + deferred
`style.css`, both mapped from bare names to VERSIONED filenames by nginx rewrites
(`nginx/gwern.net.conf:232-237`) — cache-busting without touching HTML.

## Dark mode: derived, not duplicated

One light palette in `colors.css`; `color-scheme-convert.php` machine-inverts it through
**Oklch** (lightness flip at 0.55) to generate the dark palette; concatenated with a small
hand-tuned adjustments file (`build/build_mode_css.php:11-20`). Deliberately avoids pure
black/white. Images carry per-image invert judgments (`invertornot`). One source of truth,
two themes — directly inheritable for webtop theming.

## Templates and SSI: the chrome hot-patch layer

`template/default.html` is the Hakyll shell: SSI-included head/asset-links/navbar/footer
fragments from `include/`, page metadata block (status, confidence in Kesselman estimative
words, importance 1-10, tags), then `$body$`, then **lazy footer sections** — backlinks,
similar-links, link-bibliography as include-links into `/metadata/annotation/…`, loaded by
the same transclusion engine as popups.

SSI exists so chrome and asset versions update by rsync + cache expiry **without
rebuilding thousands of essays** — the split between corpus compilation and chrome
composition. Transclude templates (`template/include/*.tmpl`) compile into a JS string
table so popup chrome and page chrome share one template source.

## Fonts: subsetting as ideology

140M, but the body fonts are aggressively subsetted (`pyftsubset` with documented unicode
ranges + OpenType features). The showpiece: **dropcap fonts are one file per letter** —
a page loads only the single 8-16K glyph it needs, themed per essay by body class
(`dropcaps-goudy`, `dropcaps-yinit`, …). Bandwidth-aware ornamentation.

## nginx: URL permanence as a service

`gwern.net.conf` (~1,750 lines) plus **~43,000 redirect rules** (`move.conf` 13k,
`broken.conf` 30k):

- Immutable caching (`max-age=77760000, public, immutable`) on versioned assets.
- **`Accept: text/markdown` content negotiation** (`gwern.net.conf:97-109`): LLM and tool
  clients get the raw markdown source of any essay. The corpus is deliberately
  machine-legible.
- **Lua fuzzy 404**: canonicalize the path (strip separators, case-fold); unique match →
  301, else 404 page with sitemap-based guesser (`404-guesser.js`). Typo-resilient URLs at
  archive scale.
- 404 hits logged as a repair feed. Redirect corpus deduplicated during sync.
- **Deliberate anti-CSP stance**: no X-Frame-Options — framing is a feature, because
  popups and transclusions of archived pages need iframes.
- `X-Clacks-Overhead` memorial header from a daily cron calendar (`memoriam.sh`).
- Gitit-era `*.page` → `*.md` legacy redirects: twenty years of URL debts honored.

## Deploy

`sync.sh` ends with checksummed rsync to a Hetzner box and a targeted Cloudflare purge of
recently-touched URLs. `asset.php` exists only for dev: serve-with-regenerate when the git
tree is dirty.

## Inheritance table

| Layer | Steal | Caution |
|-------|-------|---------|
| Theming | `--GW-*` variable palette + Oklch-derived dark mode | keep one palette source |
| Chrome | SSI-style fragment composition; versioned immutable assets | GitHub Pages lacks SSI — compose at build or client |
| Type | font stacks, subsetting discipline, per-letter dropcaps | dropcap art is 126M of the 140M |
| Metadata | status/confidence/importance page header | maps onto yaml-jazz frontmatter directly |
| URLs | permanence as data: redirect corpus, fuzzy 404, markdown negotiation | Gwern-scale ops; raw.githubusercontent covers the LLM case for us |
| Philosophy | generated files sacred; lint in the sync loop | our pre-commit yaml/json validation is the same instinct |

↑ [ARCHITECTURE.md](ARCHITECTURE.md)
