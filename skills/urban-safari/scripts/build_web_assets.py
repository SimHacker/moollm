#!/usr/bin/env python3
"""Build map-ready JSON from FIT files for a web map UI.

Outputs:
  manifest.json
  trips/{id}.geojson
  trips/{id}.series.json
  trips/{id}.meta.json

Usage:
  python build_web_assets.py --trips-dir ./rides --out ./web/data
  python build_web_assets.py ride.fit --out ./web/data
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from fit_io import (
    bounds_from_points,
    detect_pauses,
    load_trip_points,
    read_session,
    slug_from_fit_path,
    title_from_fit_path,
)

DEFAULT_HOME = {
    "label": "Home",
    "lat": 52.0,
    "lon": 5.0,
}


def session_stats(session: dict, points: list[dict]) -> dict:
    dist_m = session.get("total_distance")
    timer_s = session.get("total_timer_time") or session.get("total_elapsed_time")
    start = session.get("start_time")

    if dist_m is None and points:
        dist_m = points[-1].get("distance_m")
    if timer_s is None and len(points) >= 2 and points[0]["t"] and points[-1]["t"]:
        t0 = datetime.fromisoformat(points[0]["t"])
        t1 = datetime.fromisoformat(points[-1]["t"])
        timer_s = (t1 - t0).total_seconds()

    return {
        "distance_km": round(float(dist_m) / 1000, 2) if dist_m else None,
        "duration_min": round(float(timer_s) / 60, 1) if timer_s else None,
        "started_at": start.isoformat() if hasattr(start, "isoformat") else None,
        "point_count": len(points),
    }


def build_trip(fit_path: Path, out_dir: Path) -> dict:
    trip_id = slug_from_fit_path(fit_path)
    points = load_trip_points(fit_path)
    session = read_session(fit_path)
    stats = session_stats(session, points)
    pauses = detect_pauses(points)
    bounds = bounds_from_points(points)

    trip_dir = out_dir / "trips"
    trip_dir.mkdir(parents=True, exist_ok=True)

    coords = [[p["lon"], p["lat"]] for p in points]
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "id": trip_id,
                    "title": title_from_fit_path(fit_path),
                    "source": fit_path.name,
                },
                "geometry": {"type": "LineString", "coordinates": coords},
            }
        ],
    }

    series = {"id": trip_id, "points": points}
    meta = {
        "id": trip_id,
        "title": title_from_fit_path(fit_path),
        "source_fit": fit_path.name,
        "bounds": bounds,
        "pauses": pauses,
        "videos": [],
        **stats,
    }

    (trip_dir / f"{trip_id}.geojson").write_text(
        json.dumps(geojson, indent=2), encoding="utf-8"
    )
    (trip_dir / f"{trip_id}.series.json").write_text(
        json.dumps(series, indent=2), encoding="utf-8"
    )
    (trip_dir / f"{trip_id}.meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )

    return {
        "id": trip_id,
        "title": meta["title"],
        "started_at": stats["started_at"],
        "distance_km": stats["distance_km"],
        "duration_min": stats["duration_min"],
        "point_count": stats["point_count"],
        "bounds": bounds,
        "pause_count": len(pauses),
        "source_fit": fit_path.name,
        "geojson": f"trips/{trip_id}.geojson",
        "series": f"trips/{trip_id}.series.json",
        "meta": f"trips/{trip_id}.meta.json",
        "videos": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build web map assets from FIT files")
    parser.add_argument("fits", nargs="*", type=Path, help="FIT files")
    parser.add_argument("--trips-dir", type=Path, default=Path("rides"))
    parser.add_argument("--out", type=Path, default=Path("web/data"))
    parser.add_argument("--home-label", default=DEFAULT_HOME["label"])
    parser.add_argument("--home-lat", type=float, default=DEFAULT_HOME["lat"])
    parser.add_argument("--home-lon", type=float, default=DEFAULT_HOME["lon"])
    args = parser.parse_args()

    if args.fits:
        fit_paths = [p for p in args.fits if p.suffix.lower() == ".fit"]
    else:
        fit_paths = sorted(args.trips_dir.glob("*.fit"))
        fit_paths = [p for p in fit_paths if not p.name.endswith(".cleaned.fit")]

    if not fit_paths:
        print("No FIT files found.", file=sys.stderr)
        return 1

    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    entries = []
    for fit_path in fit_paths:
        if not fit_path.is_file():
            print(f"Skip missing: {fit_path}", file=sys.stderr)
            continue
        print(f"build: {fit_path.name}")
        entries.append(build_trip(fit_path.resolve(), out_dir))

    entries.sort(key=lambda e: e.get("started_at") or "", reverse=True)

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "home": {
            "label": args.home_label,
            "lat": args.home_lat,
            "lon": args.home_lon,
        },
        "map": {
            "tile_url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            "attribution": "© OpenStreetMap contributors",
        },
        "trip_count": len(entries),
        "trips": entries,
        "videos": [],
    }

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(entries)} trips → {out_dir / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
