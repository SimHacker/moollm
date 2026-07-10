#!/usr/bin/env bash
# Refresh Zach Mama YouTube catalog via yt-dlp (no joke text — IDs + titles only).
# Usage:
#   ./scripts/refresh-youtube-catalog.sh           # dump to catalog-raw.txt
#   ./scripts/refresh-youtube-catalog.sh --check   # verify URLs in routines.yml still resolve
set -euo pipefail

CHANNEL="https://www.youtube.com/@zachmama"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
RAW="$DIR/catalog-raw.txt"
ROUTINES="$DIR/routines.yml"

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "yt-dlp required: brew install yt-dlp  (or pip install yt-dlp)" >&2
  exit 1
fi

dump_catalog() {
  echo "# Zach Mama @zachmama — $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$RAW"
  echo "# format: VIDEO_ID|TITLE|https://www.youtube.com/watch?v=VIDEO_ID" >> "$RAW"
  yt-dlp --flat-playlist --print "%(id)s|%(title)s" "$CHANNEL" 2>/dev/null \
    | while IFS='|' read -r id title; do
        printf '%s|%s|https://www.youtube.com/watch?v=%s\n' "$id" "$title" "$id"
      done >> "$RAW"
  echo "Wrote $(wc -l < "$RAW" | tr -d ' ') lines to $RAW"
}

check_urls() {
  local ids
  ids=$(grep -oE 'watch\?v=[A-Za-z0-9_-]+' "$ROUTINES" | sed 's/watch?v=//' | sort -u)
  local ok=0 fail=0
  for id in $ids; do
    if yt-dlp --flat-playlist --ignore-errors --print "%(id)s" \
        "https://www.youtube.com/watch?v=$id" 2>/dev/null | grep -qx "$id"; then
      ok=$((ok + 1))
    else
      echo "MISSING or private: $id" >&2
      fail=$((fail + 1))
    fi
  done
  echo "check: $ok ok, $fail failed"
  [[ "$fail" -eq 0 ]]
}

case "${1:-dump}" in
  --check|check) check_urls ;;
  *) dump_catalog ;;
esac
