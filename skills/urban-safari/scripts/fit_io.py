"""Shared FIT read helpers — Bosch eBike Flow, XOSS G, Garmin, etc."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from fitparse import FitFile
except ImportError:
    FitFile = None  # type: ignore

SEMICIRCLE_SCALE = 180.0 / (2**31)


def require_fitparse() -> None:
    if FitFile is None:
        raise SystemExit("Install fitparse: pip install fitparse")


def msg_fields(message) -> dict[str, Any]:
    return {d.name: d.value for d in message if d.name}


def semicircles_to_degrees(semicircles: int | float | None) -> float | None:
    if semicircles is None:
        return None
    return float(semicircles) * SEMICIRCLE_SCALE


def slug_from_fit_path(path: Path) -> str:
    stem = path.stem
    return stem.lower().replace(" ", "-")


def title_from_fit_path(path: Path) -> str:
    stem = path.stem
    if "-" in stem:
        parts = stem.rsplit("-", 5)
        if len(parts) > 1 and len(parts[-1]) == 12:
            return parts[0]
    return stem


def read_session(fit_path: Path) -> dict[str, Any]:
    require_fitparse()
    fit = FitFile(str(fit_path))
    for message in fit.get_messages("session"):
        return msg_fields(message)
    return {}


def consolidate_records(fit_path: Path) -> list[dict[str, Any]]:
    """Merge duplicate record rows per timestamp (Bosch Flow pattern)."""
    require_fitparse()
    fit = FitFile(str(fit_path))
    by_ts: dict[Any, dict[str, Any]] = {}

    for message in fit:
        if message.name != "record":
            continue
        fields = msg_fields(message)
        ts = fields.get("timestamp")
        if ts is None:
            continue
        if ts in by_ts:
            by_ts[ts].update({k: v for k, v in fields.items() if v is not None})
        else:
            by_ts[ts] = dict(fields)

    return [by_ts[ts] for ts in sorted(by_ts.keys(), key=lambda t: t or 0)]


def normalize_record(rec: dict[str, Any]) -> dict[str, Any] | None:
    lat = semicircles_to_degrees(rec.get("position_lat"))
    lon = semicircles_to_degrees(rec.get("position_long"))
    if lat is None or lon is None:
        return None

    alt = rec.get("enhanced_altitude")
    if alt is None:
        alt = rec.get("altitude")

    speed = rec.get("enhanced_speed")
    if speed is None:
        speed = rec.get("speed")

    ts = rec.get("timestamp")
    if isinstance(ts, datetime) and ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)

    return {
        "t": ts.isoformat() if isinstance(ts, datetime) else None,
        "lat": round(lat, 6),
        "lon": round(lon, 6),
        "alt_m": float(alt) if alt is not None else None,
        "speed_kmh": round(float(speed) * 3.6, 2) if speed is not None else None,
        "power_w": int(rec["power"]) if rec.get("power") is not None else None,
        "cadence_rpm": int(rec["cadence"]) if rec.get("cadence") is not None else None,
        "distance_m": float(rec["distance"]) if rec.get("distance") is not None else None,
    }


def load_trip_points(fit_path: Path) -> list[dict[str, Any]]:
    points = []
    for rec in consolidate_records(fit_path):
        norm = normalize_record(rec)
        if norm is not None:
            points.append(norm)
    return points


def detect_pauses(points: list[dict[str, Any]], gap_s: float = 60.0) -> list[dict[str, Any]]:
    pauses = []
    for a, b in zip(points, points[1:]):
        if not a["t"] or not b["t"]:
            continue
        ta = datetime.fromisoformat(a["t"])
        tb = datetime.fromisoformat(b["t"])
        gap = (tb - ta).total_seconds()
        if gap >= gap_s:
            pauses.append({"after_t": a["t"], "before_t": b["t"], "gap_s": round(gap, 1)})
    return pauses


def bounds_from_points(points: list[dict[str, Any]]) -> list[float] | None:
    if not points:
        return None
    lats = [p["lat"] for p in points]
    lons = [p["lon"] for p in points]
    return [min(lons), min(lats), max(lons), max(lats)]
