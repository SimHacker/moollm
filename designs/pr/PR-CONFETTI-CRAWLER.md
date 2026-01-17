## Summary
- Added worm-confetti-crawler character under `examples/adventure-4/characters/animals/worm-confetti-crawler/`, with local CARD/CHARACTER, demo, sister script, test script, emoji themes, and reference outputs.
- Moved sprayer, emoji palette, demo, and tests into the character’s directory; removed the old `skills/card/examples` copies.
- Expanded sprayer features: theme-aware erosion/strip, drift controls, block-scalar awareness, verbose logging, strip modes, and consolidated test runner output.
- Updated adventure runtime to drop the legacy `AdventureUI`.

## Artifacts
- Run suite: `./examples/adventure-4/characters/animals/worm-confetti-crawler/test.sh > examples/adventure-4/characters/animals/worm-confetti-crawler/demo-test-out.txt`
- Demo (YAML): `examples/adventure-4/characters/animals/worm-confetti-crawler/demo.yml`
- Demo (text): `examples/adventure-4/characters/animals/worm-confetti-crawler/demo.txt`
- Output log: `examples/adventure-4/characters/animals/worm-confetti-crawler/demo-test-out.txt`

## Notes
- Sprayer CLI is now `examples/adventure-4/characters/animals/worm-confetti-crawler/sprayer.py`
- Themes map: `.../worm-confetti-crawler/emojis.txt`
- Tests emit a single combined stdout log; no per-test files.
