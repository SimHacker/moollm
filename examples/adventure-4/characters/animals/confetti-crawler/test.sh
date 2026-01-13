#!/usr/bin/env bash
set -euo pipefail

SCRIPT="examples/adventure-4/characters/animals/confetti-crawler/sprayer.py"
DEMO="examples/adventure-4/characters/animals/confetti-crawler/demo.yml"
EMOJIS="examples/adventure-4/characters/animals/confetti-crawler/emojis.txt"

testnum=1

run() {
  echo "============================================================"
  local label="$1"; shift
  echo "$label"
  local cmd=""
  for arg in "$@"; do
    cmd+=" $(printf '%q' "$arg")"
  done
  cmd="${cmd:1}"
  echo "CMD: $cmd"
  "$@"
  echo
  echo "------------------------------------------------------------"
  echo
  testnum=$((testnum+1))
}

# Simple serial, single pass, garden
run "Test 1: Serial single pass (summer-garden, seed=1)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode serial --iterations 1 \
  --emoji-map-file "$EMOJIS" --theme summer-garden \
  --seed 1

# MFM single-site, few passes, neon
run "Test 2: MFM 3 passes (neon-arcade, seed=2)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode mfm --iterations 3 \
  --emoji-map-file "$EMOJIS" --theme neon-arcade \
  --seed 2

# Serial even coat, two passes, pastel
run "Test 3: Serial 2 passes (pastel-candy, seed=3)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode serial --iterations 2 \
  --emoji-map-file "$EMOJIS" --theme pastel-candy \
  --seed 3

# Drifted sparse hits
run "Test 4: MFM 5 passes with drift (drift=2,r=0.3, summer-garden, seed=4)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode mfm --iterations 5 \
  --drift-radius 2 --drift-prob 0.3 \
  --emoji-map-file "$EMOJIS" --theme summer-garden \
  --seed 4

# Erode after a coat (same theme)
run "Test 5: Serial 1 pass then erode 5 moves (summer-garden, seed=5)" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme summer-garden --seed 5 | python \"$SCRIPT\" -i /dev/stdin -o - --erode --iterations 5 --drift-radius 2"

# Strip all
run "Test 6: Strip all emojis" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme summer-garden --seed 6 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode all"

# Strip down to min depth 1, random sites
run "Test 7: Strip mfm min depth=1 iterations=4" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme spring-bloom --seed 7 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode mfm --strip-min-depth 1 --iterations 4 --seed 7"

# Big pass: serial thick coat then mfm neon drifted accents
run "Test 8: Serial 2 passes (spring-bloom) then MFM 6 passes neon with drift" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme spring-bloom --seed 8 | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 6 --drift-radius 2 --drift-prob 0.25 --emoji-map-file \"$EMOJIS\" --theme neon-arcade --seed 9"

# Stress: many MFM passes
run "Test 9: MFM 20 passes (festival-sky, seed=10)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode mfm --iterations 20 \
  --emoji-map-file "$EMOJIS" --theme festival-sky \
  --seed 10

# Edge: empty stdin
run "Test 10: Empty input" \
  bash -lc "printf '' | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 3"

# Edge: drift-only (no drift_prob -> disabled)
run "Test 11: MFM drift disabled (should act like plain mfm)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode mfm --iterations 3 \
  --drift-radius 3 --drift-prob 0 \
  --emoji-map-file "$EMOJIS" --theme minty-fresh \
  --seed 11

# Edge: strip with min-depth higher than present (no change)
run "Test 12: Strip serial min-depth=5 (no change expected)" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme minty-fresh --seed 12 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode serial --strip-min-depth 5"

# Simple: mfm single hit, minty
run "Test 13: MFM 1 pass (minty-fresh, seed=12)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode mfm --iterations 1 \
  --emoji-map-file "$EMOJIS" --theme minty-fresh \
  --seed 12

# Medium: serial 3 passes, drift off, citrus-zest
run "Test 14: Serial 3 passes (citrus-zest, seed=13)" \
  python "$SCRIPT" -i "$DEMO" -o - \
  --mode serial --iterations 3 \
  --emoji-map-file "$EMOJIS" --theme citrus-zest \
  --seed 13

# Hardcore: serial 2 passes bloom, then mfm 10 passes neon with drift, then strip to depth 1
run "Test 15: Layer + accent + trim" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme spring-bloom --seed 14 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 10 --drift-radius 2 --drift-prob 0.35 --emoji-map-file \"$EMOJIS\" --theme neon-arcade --seed 15 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode serial --strip-min-depth 1"

# Layered multi-theme with erosion smoothing
run "Test 16: Layered coats then erode smooth (garden + neon + melt)" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme summer-garden --seed 16 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 6 --emoji-map-file \"$EMOJIS\" --theme neon-arcade --seed 17 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --erode --iterations 6 --drift-radius 2 --seed 18"

# Three-theme stack with drift accents and light strip
run "Test 17: Three themes + drift accent + strip depth=1" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme spring-bloom --seed 19 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 5 --drift-radius 1 --drift-prob 0.4 --emoji-map-file \"$EMOJIS\" --theme festival-sky --seed 20 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 5 --drift-radius 2 --drift-prob 0.3 --emoji-map-file \"$EMOJIS\" --theme ocean-vibes --seed 21 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode serial --strip-min-depth 1"

# Heavy blend with alternating themes and a final erosion polish
run "Test 18: Alternating themes + erosion polish" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme pastel-candy --seed 22 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 8 --emoji-map-file \"$EMOJIS\" --theme cyberpunk-neon --seed 23 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 8 --emoji-map-file \"$EMOJIS\" --theme desert-sunset --drift-radius 1 --drift-prob 0.25 --seed 24 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --erode --iterations 8 --drift-radius 2 --seed 25"

# Heavy layering: winter base, neon rain, festival flare, erosion polish
run "Test 19: Winter -> Neon -> Festival -> Erode" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 3 --emoji-map-file \"$EMOJIS\" --theme winter-holiday --seed 26 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 12 --emoji-map-file \"$EMOJIS\" --theme neon-arcade --drift-radius 1 --drift-prob 0.2 --seed 27 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 12 --emoji-map-file \"$EMOJIS\" --theme festival-sky --drift-radius 2 --drift-prob 0.2 --seed 28 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --erode --iterations 10 --drift-radius 2 --seed 29"

# Massive coat: pastel + citrus serial, then ocean-vibes mfm accents, then strip depth 2
run "Test 20: Thick serial + ocean accents + strip depth=2" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme pastel-candy --seed 30 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode serial --iterations 2 --emoji-map-file \"$EMOJIS\" --theme citrus-zest --seed 31 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 15 --drift-radius 1 --drift-prob 0.3 --emoji-map-file \"$EMOJIS\" --theme ocean-vibes --seed 32 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode serial --strip-min-depth 2"

# Extreme: four themes stacked, long mfm run, erosion, then light strip
run "Test 21: Quad-stack + long mfm + erosion + strip" \
  bash -lc "python \"$SCRIPT\" -i \"$DEMO\" -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme spring-bloom --seed 33 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme ocean-night --seed 34 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme cyberpunk-neon --seed 35 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode serial --iterations 1 --emoji-map-file \"$EMOJIS\" --theme desert-sunset --seed 36 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --mode mfm --iterations 25 --drift-radius 2 --drift-prob 0.25 --emoji-map-file \"$EMOJIS\" --theme festival-sky --seed 37 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --erode --iterations 12 --drift-radius 3 --seed 38 \
    | python \"$SCRIPT\" -i /dev/stdin -o - --strip --strip-mode serial --strip-min-depth 1"

