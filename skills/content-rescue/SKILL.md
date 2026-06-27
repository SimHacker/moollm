# content-rescue 🛟

> Rescue your content from enshittified platforms. Own it as clean, git-committed,
> universal Markdown + local assets you control and republish.
>
> Part of MOOLLM. Glance: `GLANCE.yml` · Interface: `CARD.yml` · Scripts: `scripts/`

## Why

Platforms enshittify; your writing, images, and talks shouldn't be hostage to them.
This skill repatriates **your own** content (and clearly public material — HN is still
good) into **local, diffable, universal Markdown + assets** under version control.
*If it's not on git, it don't exist.*

## The core trick

> **The page may be walled; the asset CDN usually isn't.**

A `curl` of a Medium article is often bot-walled to a ~5KB stub. But:
1. the image CDN (`miro.medium.com`) serves assets freely, and
2. the rendered page embeds `window.__APOLLO_STATE__` — every image id + caption, in
   paragraph order, independent of lazy-loading.

So we **extract the manifest from embedded page state in a real browser**, then **fetch
assets directly from the open CDN**. (Born from the 2026-06-27 Will-Wright rescue: 167
images pulled in order, captioned, and wired into the local transcript.)

## Protocol

### EXTRACT-MANIFEST `FROM <url> [VIA browser]`
When `curl` is walled, open the page in a real browser. The **Cursor browser MCP** is
ideal headless:
- `browser_navigate` → the article,
- `browser_cdp` → `Runtime.evaluate` (`returnByValue: true`) running
  `scripts/medium_extract_manifest.js` (image block) → ordered `index|id|caption` lines;
  run the video block for embedded YouTube ids.

Save the image lines to `manifest.psv`. (Generic sites: derive `id|caption` from
`<figure>`/`srcset`/JSON-LD, or put full asset URLs in column 2.)

### FETCH-ASSETS `FROM <manifest.psv> TO <dir>`
```bash
python3 scripts/fetch_images.py manifest.psv images --source-url '<article url>'
```
Downloads each asset in order as `NNN-slug.ext` (extension auto-detected), and emits
`images/INDEX.md` (a captioned, ordered gallery = an illustrated transcript) and
`images/map.tsv`. Re-runnable (skips existing).

### WIRE-MARKDOWN `<text-capture> WITH <gallery>`
Localize a text capture into clean universal Markdown:
- fix the "images omitted" placeholder; link the gallery (`images/INDEX.md`),
- inline figures at their caption anchors where the prose preserves them,
- collect embedded video links into a `videos.md`,
- keep provenance + third-party credits.

### SCRAPE-HN `<user|thread>`
Harvest a user's HN comments/threads (HN's API/site are scrape-friendly) into
YAML/Markdown capture files. (HN is one of the good ones — preserve, don't fight it.)

## Ethics
- For the **author's own** content or clearly public material. Respect robots/ToS and
  others' copyright; **credit third-party assets** (the gallery caption carries it).
- Polite single-pass fetches; re-runnable so you don't hammer.

## Roadmap (sibling skills, planned — see `CARD.yml` related_planned_skills)
- **youtube** — transcripts/STT/cleanup, speaker + section splitting, timecoded refs,
  ingest interviews → STT → cleanup, publish via the Data API.
- **stream-deck** — Twitch + OBS (and alternatives/plugins) screencast control + metadata.
- **publish-sync** — git-centric auto-publish + cross-service sync (YouTube/Twitch/GitHub)
  via GitHub Action workflows.

## Part of MOOLLM
A standalone, publishable skill. Related: `skills/card` (a rescued page can become a
CARD), `skills/cursor-mirror` (introspection sibling, same `scripts/` pattern).
