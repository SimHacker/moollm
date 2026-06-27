# content-rescue / scripts

Two-step Medium (and Medium-like) rescue. The page is often bot-walled; the asset
CDN is not. Get the manifest from the page's embedded state, then fetch direct.

## 1. Extract the manifest (browser)

Open the article in a real browser (the Cursor **browser MCP** works great headless:
`browser_navigate`, then `browser_cdp` → `Runtime.evaluate` with `returnByValue:true`).
Run [`medium_extract_manifest.js`](./medium_extract_manifest.js) (image block) to get
ordered `paraIndex|imageId|caption` lines. Run the video block (commented) for embed ids.

Save the image lines to `manifest.psv`.

## 2. Fetch assets + build the gallery

```bash
python3 fetch_images.py manifest.psv images \
  --source-url 'https://your.medium.com/the-article'
```

Produces, in `images/`:
- `NNN-slug.ext` for every asset (article order; extension auto-detected),
- `INDEX.md` — a captioned, ordered gallery (an illustrated transcript),
- `map.tsv` — `seq · source_index · asset_id · file · caption`.

Re-runnable (skips existing). For non-Medium sites, pass `--url-template` or put full
URLs in column 2 of the manifest.

## Notes
- gifs: the default 2000px resize keeps animation on Medium; tweak `--url-template`
  to fetch originals if a source strips it.
- Wiring into a text transcript (localize image links, collect video links) is the
  `WIRE-MARKDOWN` step — see `../SKILL.md`.
