# Demo data — synthetic, safe to publish

This directory contains **fake GPS** only — a small square loop near 52.0°N, 5.0°E labeled
"Demo City". No real home coordinates.

Use it to test map UIs and video sync without leaking private tracks.

Regenerate the synthetic series by editing the generator in the skill's git history or by
running `build_web_assets.py` on a FIT you own locally.
