#!/usr/bin/env python3
"""Map transcript words onto the ride track with spatiotemporal clustering.

Requires a synced video track (sync_video.py) with keyframes.

Usage:
  python map_transcript.py --video-id img-0679 --data-dir ./web/data \\
    --video /path/to/IMG_0679.MOV

  python map_transcript.py --video-id img-0679 --data-dir ./web/data \\
    --whisper-json ./cache/img-0679.whisper.json

Dependencies:
  pip install openai-whisper   # or whisper CLI on PATH
  ffmpeg, ffprobe
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from transcript_cluster import (
    cluster_segments,
    clusters_to_geojson,
    place_segments_on_track,
)
from transcript_io import load_whisper_json, segments_from_whisper, transcribe_video


def load_track(data_dir: Path, video_id: str) -> dict:
    track_path = data_dir / "videos" / f"{video_id}.track.json"
    if not track_path.is_file():
        raise SystemExit(
            f"No track at {track_path} — run sync_video.py first (needs matching FIT trip)"
        )
    return json.loads(track_path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Map transcript onto ride GPS with clustering")
    parser.add_argument("--video-id", required=True, help="Video id slug (matches sync_video output)")
    parser.add_argument("--data-dir", type=Path, default=Path("web/data"))
    parser.add_argument("--video", type=Path, help="Source video for Whisper transcription")
    parser.add_argument("--whisper-json", type=Path, help="Existing Whisper JSON (skip transcribe)")
    parser.add_argument("--cache-dir", type=Path, help="Cache Whisper JSON here")
    parser.add_argument("--model", default="base", help="Whisper model")
    parser.add_argument("--language", default=None, help="Whisper language code")
    parser.add_argument("--cluster-radius-m", type=float, default=40.0)
    parser.add_argument("--cluster-gap-s", type=float, default=20.0)
    parser.add_argument("--min-words", type=int, default=3)
    args = parser.parse_args()

    data_dir = args.data_dir.resolve()
    track = load_track(data_dir, args.video_id)
    keyframes = track.get("keyframes") or []
    if not keyframes:
        raise SystemExit(f"Track {args.video_id} has no keyframes")

    if args.whisper_json:
        whisper_doc = load_whisper_json(args.whisper_json.resolve())
    elif args.video:
        whisper_doc = transcribe_video(
            args.video.resolve(),
            model=args.model,
            language=args.language,
            cache_dir=args.cache_dir.resolve() if args.cache_dir else data_dir / "cache",
        )
    else:
        print("Provide --video or --whisper-json", file=sys.stderr)
        return 1

    segments = segments_from_whisper(whisper_doc)
    placed = place_segments_on_track(segments, keyframes)
    clusters = cluster_segments(
        placed,
        radius_m=args.cluster_radius_m,
        max_gap_s=args.cluster_gap_s,
        min_words=args.min_words,
    )

    out_dir = data_dir / "videos"
    out_dir.mkdir(parents=True, exist_ok=True)

    geo_rel = f"videos/{args.video_id}.transcript.geojson"
    doc = {
        "id": args.video_id,
        "video_id": args.video_id,
        "trip_id": track.get("trip_id"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cluster_params": {
            "radius_m": args.cluster_radius_m,
            "max_gap_s": args.cluster_gap_s,
            "min_words": args.min_words,
        },
        "segment_count": len(placed),
        "cluster_count": len(clusters),
        "segments": placed,
        "clusters": [
            {k: v for k, v in c.items() if k != "segments"} for c in clusters
        ],
        "geojson": geo_rel,
    }

    transcript_path = out_dir / f"{args.video_id}.transcript.json"
    transcript_path.write_text(json.dumps(doc, indent=2), encoding="utf-8")
    (data_dir / geo_rel).write_text(
        json.dumps(clusters_to_geojson(args.video_id, clusters), indent=2),
        encoding="utf-8",
    )

    manifest_path = data_dir / "manifest.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for v in manifest.get("videos", []):
            if v.get("id") == args.video_id:
                v["transcript"] = f"videos/{args.video_id}.transcript.json"
                v["transcript_geojson"] = geo_rel
                break
        manifest["generated_at"] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(
        f"Mapped {len(placed)} segments → {len(clusters)} clusters "
        f"→ {transcript_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
