# Analysis notes — gwern.net source deep dive

Full-repo study of the sister clone `~/GroundUp/git/gwern.net` (shallow, 315 MB,
HEAD 2026-08-05). The repo is Gwern's `static/` engine; his essay corpus lives in a
private `~/wiki/` tree. All file:line references resolve against the sister clone.

## Reading order

| Doc | Subsystem |
|-----|-----------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | The whole system, build+deploy cycle, ranked most-interesting list |
| [FRONTEND-POPUPS-WM.md](FRONTEND-POPUPS-WM.md) | JS pop-frame window manager, extracts registry, transclusion, tiling keys, TNT pin test |
| [LINK-PIPELINE.md](LINK-PIPELINE.md) | Haskell pipeline: GTX annotation tiers, scrapers, LinkArchive, backlinks, embeddings |
| [LLM-IN-THE-LOOP.md](LLM-IN-THE-LOOP.md) | The GPT tool suite and its guardrails (sister-script parallel) |
| [STYLING-AND-DELIVERY.md](STYLING-AND-DELIVERY.md) | CSS/Oklch dark mode, SSI chrome, fonts, nginx URL permanence |

↑ [sources](../README.md) · [design pack](../../README.md)
