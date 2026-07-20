"""Cluster transcript segments on the map by distance and time."""

from __future__ import annotations

import math
from typing import Any


def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6_371_000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlon / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def place_segments_on_track(
    segments: list[dict[str, Any]],
    keyframes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Attach lat/lon to each segment at its temporal midpoint."""
    if not keyframes:
        return []

    placed: list[dict[str, Any]] = []
    for seg in segments:
        mid = (seg["start_s"] + seg["end_s"]) / 2.0
        kf = _nearest_keyframe(keyframes, mid)
        if kf is None:
            continue
        placed.append(
            {
                **seg,
                "video_s_mid": round(mid, 3),
                "lat": kf["lat"],
                "lon": kf["lon"],
                "bearing_deg": kf.get("bearing_deg"),
            }
        )
    return placed


def place_words_on_track(
    segments: list[dict[str, Any]],
    keyframes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Attach lat/lon to each word at its temporal midpoint."""
    words: list[dict[str, Any]] = []
    for seg in segments:
        for w in seg.get("words") or []:
            if not w.get("text"):
                continue
            mid = (w["start_s"] + w["end_s"]) / 2.0
            kf = _nearest_keyframe(keyframes, mid)
            if kf is None:
                continue
            words.append(
                {
                    "text": w["text"],
                    "start_s": w["start_s"],
                    "end_s": w["end_s"],
                    "video_s_mid": round(mid, 3),
                    "lat": kf["lat"],
                    "lon": kf["lon"],
                }
            )
    return words


def _nearest_keyframe(keyframes: list[dict[str, Any]], video_s: float) -> dict[str, Any] | None:
    if not keyframes:
        return None
    best = min(keyframes, key=lambda k: abs(k["video_s"] - video_s))
    return best


def cluster_segments(
    placed: list[dict[str, Any]],
    radius_m: float = 40.0,
    max_gap_s: float = 20.0,
    min_words: int = 3,
) -> list[dict[str, Any]]:
    """Greedy spatiotemporal clustering for readable map labels."""
    if not placed:
        return []

    ordered = sorted(placed, key=lambda s: s["start_s"])
    clusters: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    def flush() -> None:
        nonlocal current
        if current is None:
            return
        word_count = sum(len(s.get("words") or []) or len(s["text"].split()) for s in current["segments"])
        if word_count >= min_words or len(current["segments"]) >= 2:
            clusters.append(_finalize_cluster(current))
        current = None

    for seg in ordered:
        if current is None:
            current = _new_cluster(seg)
            continue

        last = current["segments"][-1]
        gap_s = seg["start_s"] - last["end_s"]
        dist_m = haversine_m(last["lat"], last["lon"], seg["lat"], seg["lon"])

        if dist_m <= radius_m and gap_s <= max_gap_s:
            current["segments"].append(seg)
        else:
            flush()
            current = _new_cluster(seg)

    flush()
    return clusters


def _new_cluster(seg: dict[str, Any]) -> dict[str, Any]:
    return {
        "segments": [seg],
        "video_s_start": seg["start_s"],
        "video_s_end": seg["end_s"],
    }


def _finalize_cluster(raw: dict[str, Any]) -> dict[str, Any]:
    segs = raw["segments"]
    n = len(segs)
    lat = sum(s["lat"] for s in segs) / n
    lon = sum(s["lon"] for s in segs) / n
    text = " ".join(s["text"] for s in segs if s.get("text"))
    words: list[dict[str, Any]] = []
    for s in segs:
        words.extend(s.get("words") or [])

    duration_s = raw["video_s_end"] - raw["video_s_start"]
    span_m = 0.0
    if n >= 2:
        span_m = haversine_m(segs[0]["lat"], segs[0]["lon"], segs[-1]["lat"], segs[-1]["lon"])

    return {
        "video_s_start": round(raw["video_s_start"], 3),
        "video_s_end": round(raw["video_s_end"], 3),
        "duration_s": round(duration_s, 3),
        "lat": round(lat, 6),
        "lon": round(lon, 6),
        "text": text,
        "segment_count": n,
        "word_count": len(words) if words else len(text.split()),
        "span_m": round(span_m, 1),
        "segments": segs,
    }


def clusters_to_geojson(video_id: str, clusters: list[dict[str, Any]]) -> dict:
    features = []
    for i, c in enumerate(clusters):
        features.append(
            {
                "type": "Feature",
                "properties": {
                    "id": f"{video_id}-t{i}",
                    "kind": "transcript_cluster",
                    "text": c["text"],
                    "video_s_start": c["video_s_start"],
                    "video_s_end": c["video_s_end"],
                    "word_count": c["word_count"],
                    "segment_count": c["segment_count"],
                    "span_m": c["span_m"],
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [c["lon"], c["lat"]],
                },
            }
        )
    return {"type": "FeatureCollection", "features": features}
