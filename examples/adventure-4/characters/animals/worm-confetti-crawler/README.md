# 🐛🎊 worm-confetti-crawler

Rip Taylor–infused emoji-fordite worm familiar: pub-born stagehand, snowmaker, and comedian. It calls its sister script instead of burning LLM cycles, laying themed emoji “snow,” eroding drifts, or stripping layers to reveal clean text. Think sideways snowdrifts, graffiti-tag commentary, and ceremonial flair.

K-LINES
- RIP-TAYLOR-SOUL — exuberant confetti timing; stage banter in emoji.
- MOVEABLE-FEAST-MACHINE — random windows (MFM) for organic scatter; serial coats for even layers.
- GRAFFITI-APPEND — appends to existing lines/comments; avoids string literals; block scalars are “indoors.”
- ERode-SETTLE — moves existing emojis downhill; strip trims to target depth.
- PALETTE-ANYWHERE — fruit-machine, pride, couples spectra, neon arcade, garden, festival skies, more.

PERSONALITY
- Soul: “Rip Taylor: The Gong Show Queen of Confetti” — exuberant, confetti-first, perfect comedic timing.
- Delivery: appends emojis to comments/EOL; respects syntax; honors block scalars as safe zones.
- Ceremony: announces theme/seed, runs sister script, streams stdout to the crowd.

RUNBOOK
- Full suite (YAML + text demos):  
  `./test.sh > demo-test-out.txt`
- Direct spray (YAML):  
  `python sprayer.py -i demo.yml -o - --mode mfm --iterations 5 --emoji-map-file emojis.txt --theme summer-garden --seed 42`
- Direct spray (text, no prefix):  
  `python sprayer.py -i demo.txt -o - --mode mfm --iterations 20 --emoji-map-file emojis.txt --theme fruit-machine --comment-prefix '' --seed 7`

CLI CHEATSHEET
- `--mode {mfm,serial}`: mfm = one random site per iteration (organic); serial = touch every site per iteration (even coat).
- `--iterations N`: how many passes (mfm = N placements; serial = N full sweeps).
- `--emoji-map-file emojis.txt --theme NAME`: load palette by category; falls back to ALL.
- `--palette / --palette-file`: raw emojis if you want a custom set.
- `--comment-prefix '#'` (default): set to `''` for raw text; use `//` for JS, etc.
- `--max-per-pass N`: upper bound on emojis appended per touched line.
- `--drift-radius R --drift-prob P`: chance to shift a placement within ±R commentable lines.
- `--erode`: move existing emojis downward (no creation/destruction); respects `--comment-prefix`.
- `--strip --strip-mode {all,serial,mfm} --strip-min-depth D`: trim/melt emojis; serial/mfm respect depth; all blows everything away.
- `--seed N`: reproducible PRNG.
- `-i/-o`: file paths; `-` for stdin/stdout. Default overwrites input if `-o` not set.

ARTIFACTS
- Skill: [`CARD.yml`](CARD.yml)
- Character: [`CHARACTER.yml`](CHARACTER.yml)
- Sister script: [`sprayer.py`](sprayer.py)
- Palettes: [`emojis.txt`](emojis.txt) (pride, couples, fruit-machine, etc.)
- Demos: [`demo.yml`](demo.yml), [`demo.txt`](demo.txt)
- Output log: [`demo-test-out.txt`](demo-test-out.txt)
- Tests: [`test.sh`](test.sh)

LINKS
- Incarnation card: `CHARACTER.yml`
- Skill card: `CARD.yml`
- Sister script: `sprayer.py`
- Themes: `emojis.txt`
- Regression output: `demo-test-out.txt`
- Test runner: `test.sh`

### Palette tasters (examples — see full list in `emojis.txt`)

| Theme | Sample glyphs | Notes |
| --- | --- | --- |
| fruit-machine | 🍒🍋🍇🍉🍍✨🎰🔔🪙💎 | slot-machine fruit + shine |
| pride-spectrum | 🏳️‍🌈🏳️‍⚧️🌈💖🩵🤎🖤🤍❤️💛💚💙💜 | broad pride flags/colors |
| couples | 👩🏻‍❤️‍👨🏿 👩🏾‍❤️‍👩🏼 👨🏻‍🤝‍👨🏿 👩🏻‍🤝‍🧑🏿 👪🏽 | mixed skin tones/pairs |
| people-wave-spectrum | 👋🏻👋🏼👋🏽👋🏾👋🏿🙋🏻‍♀️🙋🏾‍♂️ | waves + raised hands |
| people-sports-spectrum | 🏃‍♀️🏃‍♂️🏊‍♀️🏊‍♂️🏄‍♀️🏄‍♂️🚴‍♀️🚴‍♂️ | motion/crowd texture |
| people-care-spectrum | 🧑‍🦽🧑‍🦼🧑‍🦯🤱🧑‍🍼 | accessibility + care |
| neon-arcade | 🌌🪩🎆🎇🎉🎊🪅🎈🚀🪐 | bright party/rave rain |
| ocean-vibes | 🌊🐚🐠🐟🐬🪼🐋🌅 | sea drift and foam |
| festival-sky | 🎆🎇🎉🎊🪅🎈🌠✨ | fireworks and lanterns |
| rainbow-produce | 🍅🍊🍋🥒🫐🍇🍆🍠🥕🌽🥦🥬🍄🍏 | farm/market gradients |