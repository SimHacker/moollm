#!/usr/bin/env bash
# MOOLLM speech skill — macOS TTS wrapper (say command)
set -euo pipefail
VOICE="${MOOLLM_VOICE:-}"
RATE="${MOOLLM_RATE:-}"
OUT="${MOOLLM_OUT:-}"
TEXT="${*:-}"
if [[ -z "$TEXT" ]]; then
  echo "Usage: say.sh [text]  |  MOOLLM_VOICE=Zarvox MOOLLM_RATE=120 say.sh text" >&2
  echo "List voices: say -v ?" >&2
  exit 1
fi
ARGS=()
[[ -n "$VOICE" ]] && ARGS+=(-v "$VOICE")
[[ -n "$RATE" ]] && ARGS+=(-r "$RATE")
[[ -n "$OUT" ]] && ARGS+=(-o "$OUT")
exec say "${ARGS[@]}" "$TEXT"
