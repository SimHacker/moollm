"""Video probe + GPS track interpolation for urban safari video sync."""

from __future__ import annotations

import json
import math
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def parse_iso(s: str) -> datetime:
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def probe_video(path: Path) -> dict[str, Any]:
    """Read creation_time and duration via ffprobe."""
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(path),
    ]
    try:
        raw = subprocess.check_output(cmd, text=True)
    except FileNotFoundError as exc:
        raise SystemExit("ffprobe not found — install ffmpeg") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"ffprobe failed for {path}") from exc

    data = json.loads(raw)
    fmt = data.get("format", {})
    duration_s = float(fmt.get("duration", 0) or 0)

    creation_raw = fmt.get("tags", {}).get("creation_time")
    creation_time = None
    if creation_raw:
        creation_time = parse_iso(creation_raw).isoformat()

    video_stream = next(
        (s for s in data.get("streams", []) if s.get("codec_type") == "video"),
        {},
    )

    return {
        "file": path.name,
        "path": str(path.resolve()),
        "creation_time": creation_time,
        "duration_s": round(duration_s, 3),
        "width": video_stream.get("width"),
        "height": video_stream.get("height"),
        "codec": video_stream.get("codec_name"),
    }


def bearing_deg(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Initial bearing from point 1 to point 2, degrees clockwise from north."""
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dlon = math.radians(lon2 - lon1)
    x = math.sin(dlon) * math.cos(phi2)
    y = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlon)
    return (math.degrees(math.atan2(x, y)) + 360) % 360


def interpolate_point(
    points: list[dict[str, Any]], target: datetime
) -> dict[str, Any] | None:
    """Linear interpolation of lat/lon at target UTC time."""
    if not points:
        return None

    ts_list = [parse_iso(p["t"]) for p in points if p.get("t")]
    if not ts_list:
        return None

    if target <= ts_list[0]:
        p = points[0]
        return {
            "t": p["t"],
            "lat": p["lat"],
            "lon": p["lon"],
            "bearing_deg": None,
        }

    if target >= ts_list[-1]:
        p = points[-1]
        prev = points[-2] if len(points) >= 2 else p
        brg = bearing_deg(prev["lat"], prev["lon"], p["lat"], p["lon"])
        return {
            "t": p["t"],
            "lat": p["lat"],
            "lon": p["lon"],
            "bearing_deg": round(brg, 1),
        }

    for a, b in zip(points, points[1:]):
        if not a.get("t") or not b.get("t"):
            continue
        ta = parse_iso(a["t"])
        tb = parse_iso(b["t"])
        if ta <= target <= tb:
            span = (tb - ta).total_seconds()
            if span <= 0:
                frac = 0.0
            else:
                frac = (target - ta).total_seconds() / span
            lat = a["lat"] + frac * (b["lat"] - a["lat"])
            lon = a["lon"] + frac * (b["lon"] - a["lon"])
            brg = bearing_deg(a["lat"], a["lon"], b["lat"], b["lon"])
            return {
                "t": target.isoformat(),
                "lat": round(lat, 6),
                "lon": round(lon, 6),
                "bearing_deg": round(brg, 1),
            }

    return None


def sample_video_track(
    points: list[dict[str, Any]],
    video_start: datetime,
    duration_s: float,
    offset_s: float = 0.0,
    sample_hz: float = 1.0,
) -> list[dict[str, Any]]:
    """Sample GPS along video timeline at sample_hz."""
    keyframes: list[dict[str, Any]] = []
    step = 1.0 / sample_hz if sample_hz > 0 else 1.0
    t = 0.0
    while t <= duration_s + 1e-6:
        wall = video_start + timedelta(seconds=t + offset_s)
        pt = interpolate_point(points, wall)
        if pt:
            keyframes.append(
                {
                    "video_s": round(t, 3),
                    "t": pt["t"],
                    "lat": pt["lat"],
                    "lon": pt["lon"],
                    "bearing_deg": pt["bearing_deg"],
                }
            )
        t += step
    return keyframes


def keyframes_to_geojson(video_id: str, keyframes: list[dict[str, Any]]) -> dict:
    coords = [[k["lon"], k["lat"]] for k in keyframes if "lon" in k and "lat" in k]
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"id": video_id, "kind": "video_track"},
                "geometry": {"type": "LineString", "coordinates": coords},
            }
        ],
    }


def trip_overlap_score(
    trip: dict[str, Any],
    video_start: datetime,
    video_end: datetime,
) -> float:
    """Seconds of overlap between video wall-clock span and trip series span."""
    series_path = trip.get("_series_path")
    if not series_path or not Path(series_path).is_file():
        return 0.0
    series = json.loads(Path(series_path).read_text(encoding="utf-8"))
    points = series.get("points", [])
    if len(points) < 2:
        return 0.0
    t0 = parse_iso(points[0]["t"])
    t1 = parse_iso(points[-1]["t"])
    overlap_start = max(t0, video_start)
    overlap_end = min(t1, video_end)
    return max(0.0, (overlap_end - overlap_start).total_seconds())
