#!/usr/bin/env python3
"""Sync ride videos to FIT trip tracks — keyframes + map overlay paths.

Matches each video to a trip by wall-clock overlap with the trip series, then
samples GPS along the video timeline for map scrubbing.

Usage:
  python sync_video.py --video clip.mp4 --trip-id my-ride --data-dir ./web/data
  python sync_video.py --videos-dir ./videos --data-dir ./web/data
  python sync_video.py --video clip.mp4 --data-dir ./web/data --auto-match

Requires: ffprobe on PATH; prior build_web_assets.py run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from video_io import (
    keyframes_to_geojson,
    parse_iso,
    probe_video,
    sample_video_track,
    trip_overlap_score,
)

VIDEO_EXTS = {".mp4", ".mov", ".m4v", ".mkv", ".webm"}


def slugify(name: str) -> str:
    base = Path(name).stem.lower()
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-")


def load_manifest(data_dir: Path) -> dict:
    path = data_dir / "manifest.json"
    if not path.is_file():
        raise SystemExit(f"No manifest at {path} — run build_web_assets.py first")
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(data_dir: Path, manifest: dict) -> None:
    (data_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


def enrich_trips(data_dir: Path, manifest: dict) -> list[dict]:
    trips = manifest.get("trips", [])
    for trip in trips:
        series_rel = trip.get("series")
        if series_rel:
            trip["_series_path"] = str((data_dir / series_rel).resolve())
    return trips


def pick_trip(
    trips: list[dict],
    video_start: datetime,
    video_end: datetime,
    trip_id: str | None,
) -> dict | None:
    if trip_id:
        for trip in trips:
            if trip["id"] == trip_id:
                return trip
        raise SystemExit(f"Trip not found: {trip_id}")

    best = None
    best_score = 0.0
    for trip in trips:
        score = trip_overlap_score(trip, video_start, video_end)
        if score > best_score:
            best_score = score
            best = trip
    if best is None or best_score <= 0:
        return None
    return best


def sync_one_video(
    video_path: Path,
    data_dir: Path,
    manifest: dict,
    trip_id: str | None,
    offset_s: float,
    sample_hz: float,
    copy_media: bool,
) -> dict | None:
    probe = probe_video(video_path)
    if not probe.get("creation_time"):
        print(f"Skip (no creation_time): {video_path.name}", file=sys.stderr)
        return None

    video_start = parse_iso(probe["creation_time"])
    video_end = video_start + timedelta(seconds=probe["duration_s"])

    trips = enrich_trips(data_dir, manifest)
    trip = pick_trip(trips, video_start, video_end, trip_id)
    if trip is None:
        print(f"No matching trip for {video_path.name}", file=sys.stderr)
        return None

    series = json.loads(Path(trip["_series_path"]).read_text(encoding="utf-8"))
    points = series.get("points", [])

    video_id = slugify(video_path.name)
    keyframes = sample_video_track(
        points, video_start, probe["duration_s"], offset_s=offset_s, sample_hz=sample_hz
    )

    videos_dir = data_dir / "videos"
    videos_dir.mkdir(parents=True, exist_ok=True)

    track_rel = f"videos/{video_id}.track.json"
    geo_rel = f"videos/{video_id}.geojson"
    media_rel = f"videos/{video_path.name}"

    track_doc = {
        "id": video_id,
        "trip_id": trip["id"],
        "probe": probe,
        "sync": {
            "method": "creation_time",
            "offset_s": offset_s,
            "sample_hz": sample_hz,
        },
        "keyframes": keyframes,
        "geojson": geo_rel,
    }
    (data_dir / track_rel).write_text(json.dumps(track_doc, indent=2), encoding="utf-8")
    (data_dir / geo_rel).write_text(
        json.dumps(keyframes_to_geojson(video_id, keyframes), indent=2),
        encoding="utf-8",
    )

    if copy_media:
        dest = data_dir / media_rel
        if not dest.exists():
            dest.write_bytes(video_path.read_bytes())

    entry = {
        "id": video_id,
        "trip_id": trip["id"],
        "file": media_rel if copy_media else str(video_path.resolve()),
        "duration_s": probe["duration_s"],
        "creation_time": probe["creation_time"],
        "track": track_rel,
        "geojson": geo_rel,
        "offset_s": offset_s,
    }

    meta_path = data_dir / trip["meta"]
    if meta_path.is_file():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        videos = meta.get("videos", [])
        videos = [v for v in videos if v.get("id") != video_id]
        videos.append(entry)
        meta["videos"] = videos
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    trip.setdefault("videos", [])
    trip["videos"] = [v for v in trip["videos"] if v.get("id") != video_id]
    trip["videos"].append(
        {
            "id": video_id,
            "file": entry["file"],
            "track": track_rel,
            "geojson": geo_rel,
        }
    )

    print(f"synced: {video_path.name} → trip {trip['id']} ({len(keyframes)} keyframes)")
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync videos to trip GPS tracks")
    parser.add_argument("--video", type=Path, action="append", dest="videos")
    parser.add_argument("--videos-dir", type=Path)
    parser.add_argument("--data-dir", type=Path, default=Path("web/data"))
    parser.add_argument("--trip-id", help="Force match to this trip id")
    parser.add_argument(
        "--auto-match",
        action="store_true",
        help="Pick best trip by time overlap (default when --trip-id omitted)",
    )
    parser.add_argument("--offset-s", type=float, default=0.0, help="Video clock skew vs GPS")
    parser.add_argument("--sample-hz", type=float, default=1.0, help="Keyframes per second")
    parser.add_argument(
        "--copy-media",
        action="store_true",
        help="Copy video files into data-dir/videos/",
    )
    args = parser.parse_args()

    data_dir = args.data_dir.resolve()
    manifest = load_manifest(data_dir)

    video_paths: list[Path] = list(args.videos or [])
    if args.videos_dir:
        video_paths.extend(
            sorted(
                p
                for p in args.videos_dir.iterdir()
                if p.suffix.lower() in VIDEO_EXTS and p.is_file()
            )
        )

    if not video_paths:
        print("No videos specified.", file=sys.stderr)
        return 1

    synced: list[dict] = []
    for video_path in video_paths:
        entry = sync_one_video(
            video_path.resolve(),
            data_dir,
            manifest,
            args.trip_id,
            args.offset_s,
            args.sample_hz,
            args.copy_media,
        )
        if entry:
            synced.append(entry)

    manifest.setdefault("videos", [])
    by_id = {v["id"]: v for v in manifest["videos"]}
    for entry in synced:
        by_id[entry["id"]] = entry
    manifest["videos"] = list(by_id.values())
    manifest["video_count"] = len(manifest["videos"])
    manifest["generated_at"] = datetime.now(timezone.utc).isoformat()
    save_manifest(data_dir, manifest)

    print(f"Wrote {len(synced)} video sync(s) → {data_dir / 'manifest.json'}")
    return 0 if synced else 1


if __name__ == "__main__":
    raise SystemExit(main())
