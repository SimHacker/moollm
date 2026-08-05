# Gwern mirror and analysis workflow

Respectful full-repo study. **Do not commit** the mirror into MOOLLM — clone it as a **sister
repo** next to the other repos (house convention: repos live side by side in `~/GroundUp/git/`,
added to the Cursor workspace so the LLM can read source instead of guessing).

## 1. Clone upstream (sister repo)

```bash
git clone --depth 1 https://github.com/gwern/gwern.net.git ~/GroundUp/git/gwern.net
```

Then add `~/GroundUp/git/gwern.net` to the Cursor workspace. Primary sources are the repo plus
the live [design](https://gwern.net/design) page.

## 2. First-pass grep (record in sources/analysis-notes/)

```bash
cd ~/GroundUp/git/gwern.net
rg -l "popup|popin|transclud|popover" js/ --glob '*.js' | head -30
rg "pub/sub|publish|subscribe" js/ -n | head -40
ls -la js/
```

Capture: entry points (`initial.js`), popup manager, transclusion loader, theme/reader toggles.

## 3. Live behavior capture

- Open [gwern.net/help](https://gwern.net/help) — exercise tiling keys, pin, minimize
- Screenshot or note window chrome semantics → `sources/analysis-notes/help-behavior.md`
- Compare to [REVERSE-OVER-ENGINEERING.md](REVERSE-OVER-ENGINEERING.md) acceptance table

## 4. Build (optional, if Haskell stack available)

Follow upstream README; if build fails, analysis still valid from JS + templates + design doc.

## 5. Article pipeline

1. Outline in `sources/article-draft.md` (from [REVERSE-OVER-ENGINEERING.md](REVERSE-OVER-ENGINEERING.md))
2. Side-by-side screenshots: Gwern popup vs MOOLLM webtop mock (when exists)
3. Publish to WillWrightShowForFood `characters/don-hopkins/sources/articles/` or Micropolis docs
4. Link back to this design pack

## 6. Sister-script candidate

When patterns stabilize, extract `skills/sister-script/examples/gwern-popup-audit/` — grep + report
template (no wholesale copy of their JS).

## Ethics

- Credit Gwern + Said Achmiz on every derived UI pattern
- Link [design essay](https://gwern.net/design) and [repo](https://github.com/gwern/gwern.net)
- We study to inherit interfaces, not to scrape content for republication
