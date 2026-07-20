#!/usr/bin/env python3
"""Urban safari ride pipeline: sync device → build map assets → optional video sync.

Usage:
  python pipeline.py --trips-dir ./rides --out ./web/data
  python pipeline.py --sync --trips-dir ./rides --out ./web/data
  python pipeline.py --sync --videos-dir ./videos --out ./web/data

Dependencies:
  pip install fitparse
  pip install pymobiledevice3   # for --sync (Bosch Flow iPhone)
  ffprobe on PATH               # for --videos-dir
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def run(cmd: list[str]) -> int:
    print("+", " ".join(cmd))
    return subprocess.call(cmd)


def main() -> int:
    parser = argparse.ArgumentParser(description="Urban safari FIT + video pipeline")
    parser.add_argument("--sync", action="store_true", help="Pull new FITs from iPhone")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--trips-dir", type=Path, default=Path("rides"))
    parser.add_argument("--out", type=Path, default=Path("web/data"))
    parser.add_argument("--videos-dir", type=Path, help="Sync videos in this dir to trips")
    parser.add_argument("--map-transcripts", action="store_true", help="Whisper + map transcript clusters")
    parser.add_argument("--whisper-model", default="base")
    parser.add_argument("--cluster-radius-m", type=float, default=40.0)
    parser.add_argument("--cluster-gap-s", type=float, default=20.0)
    parser.add_argument("--home-label", default="Home")
    parser.add_argument("--home-lat", type=float, default=52.0)
    parser.add_argument("--home-lon", type=float, default=5.0)
    args = parser.parse_args()

    if args.sync:
        sync_cmd = [sys.executable, str(SCRIPT_DIR / "sync_flow_trips.py")]
        if args.dry_run:
            sync_cmd.append("--dry-run")
        sync_cmd.extend(["--dest", str(args.trips_dir.resolve())])
        code = run(sync_cmd)
        if code != 0:
            return code

    build_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "build_web_assets.py"),
        "--out",
        str(args.out.resolve()),
        "--trips-dir",
        str(args.trips_dir.resolve()),
        "--home-label",
        args.home_label,
        "--home-lat",
        str(args.home_lat),
        "--home-lon",
        str(args.home_lon),
    ]
    code = run(build_cmd)
    if code != 0:
        return code

    if args.videos_dir:
        video_cmd = [
            sys.executable,
            str(SCRIPT_DIR / "sync_video.py"),
            "--videos-dir",
            str(args.videos_dir.resolve()),
            "--data-dir",
            str(args.out.resolve()),
        ]
        code = run(video_cmd)
        if code != 0:
            return code

        if args.map_transcripts:
            import json
            manifest = json.loads((args.out / "manifest.json").read_text())
            for entry in manifest.get("videos", []):
                if entry.get("status") == "pending_trip" or not entry.get("track"):
                    continue
                vid = entry["id"]
                video_file = entry.get("file")
                if not video_file or not Path(video_file).is_file():
                    continue
                map_cmd = [
                    sys.executable,
                    str(SCRIPT_DIR / "map_transcript.py"),
                    "--video-id",
                    vid,
                    "--data-dir",
                    str(args.out.resolve()),
                    "--video",
                    video_file,
                    "--model",
                    args.whisper_model,
                    "--cluster-radius-m",
                    str(args.cluster_radius_m),
                    "--cluster-gap-s",
                    str(args.cluster_gap_s),
                ]
                run(map_cmd)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
