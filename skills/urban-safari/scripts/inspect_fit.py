#!/usr/bin/env python3
"""Summarize a FIT file — Bosch Flow, XOSS G, Garmin, etc.

Usage:
  python inspect_fit.py ride.fit
  python inspect_fit.py ride.fit --gaps 10

Requires: pip install fitparse
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    from fitparse import FitFile
except ImportError:
    print("Install fitparse: pip install fitparse", file=sys.stderr)
    sys.exit(1)

RECORD_FIELDS = (
    "timestamp",
    "position_lat",
    "position_long",
    "altitude",
    "enhanced_altitude",
    "distance",
    "speed",
    "enhanced_speed",
    "power",
    "cadence",
    "heart_rate",
)


def msg_fields(message) -> dict:
    return {d.name: d.value for d in message if d.name}


def semicircles_to_degrees(semicircles: int | float | None) -> float | None:
    if semicircles is None:
        return None
    return float(semicircles) * (180.0 / 2**31)


def fmt_ts(ts) -> str:
    if ts is None:
        return "—"
    if isinstance(ts, datetime):
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return ts.isoformat()
    return str(ts)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a FIT activity file")
    parser.add_argument("fit_path", type=Path)
    parser.add_argument("--gaps", type=float, default=10.0)
    args = parser.parse_args()

    if not args.fit_path.is_file():
        print(f"Not found: {args.fit_path}", file=sys.stderr)
        return 1

    fit = FitFile(str(args.fit_path))

    message_counts: Counter[str] = Counter()
    records_by_ts: dict[object, list[dict]] = defaultdict(list)
    field_presence: Counter[str] = Counter()

    for message in fit:
        message_counts[message.name] += 1
        if message.name != "record":
            continue
        fields = msg_fields(message)
        ts = fields.get("timestamp")
        records_by_ts[ts].append(fields)
        for name in RECORD_FIELDS:
            if fields.get(name) is not None:
                field_presence[name] += 1

    duplicate_ts = {ts: rows for ts, rows in records_by_ts.items() if len(rows) > 1}
    timestamps = sorted(records_by_ts.keys(), key=lambda t: t or 0)

    print(f"File: {args.fit_path}")
    print(f"Size: {args.fit_path.stat().st_size:,} bytes")
    print()
    print("Message counts:")
    for name, count in message_counts.most_common():
        print(f"  {name}: {count}")
    print()

    print(
        f"Records: {sum(len(v) for v in records_by_ts.values())} rows, "
        f"{len(records_by_ts)} unique timestamps"
    )
    if duplicate_ts:
        print(f"  ⚠ {len(duplicate_ts)} timestamps with multiple record rows (Bosch pattern)")
    else:
        print("  ✓ No duplicate timestamps per record")

    print()
    print("Record field presence (non-null count):")
    for name in RECORD_FIELDS:
        if field_presence[name]:
            print(f"  {name}: {field_presence[name]}")

    if timestamps:
        first, last = timestamps[0], timestamps[-1]
        print()
        print(f"Time range: {fmt_ts(first)} → {fmt_ts(last)}")
        if isinstance(first, datetime) and isinstance(last, datetime):
            print(f"Duration (record span): {last - first}")

    if len(timestamps) >= 2:
        gaps = []
        for a, b in zip(timestamps, timestamps[1:]):
            if isinstance(a, datetime) and isinstance(b, datetime):
                gap = (b - a).total_seconds()
                if gap >= args.gaps:
                    gaps.append((gap, a, b))
        print()
        print(f"Gaps ≥ {args.gaps}s (likely pauses if unfilled): {len(gaps)}")
        for gap, a, b in gaps[:8]:
            print(f"  {gap:.0f}s  {fmt_ts(a)} → {fmt_ts(b)}")
        if len(gaps) > 8:
            print(f"  … and {len(gaps) - 8} more")

    print()
    for msg_name in ("session", "lap", "activity", "file_id"):
        if message_counts[msg_name]:
            print(f"✓ {msg_name} present ({message_counts[msg_name]})")
        else:
            print(f"✗ {msg_name} missing")

    if timestamps:
        start_rows = records_by_ts[timestamps[0]]
        end_rows = records_by_ts[timestamps[-1]]
        for label, rows in ("Start", start_rows), ("End", end_rows):
            lat = next(
                (r.get("position_lat") for r in rows if r.get("position_lat") is not None),
                None,
            )
            lon = next(
                (r.get("position_long") for r in rows if r.get("position_long") is not None),
                None,
            )
            if lat is not None and lon is not None:
                print(
                    f"{label} position: "
                    f"{semicircles_to_degrees(lat):.5f}°, "
                    f"{semicircles_to_degrees(lon):.5f}°"
                )

    if duplicate_ts and not message_counts["activity"]:
        print()
        print(
            "Recommendation: run through https://hacdias.github.io/flowfit/ "
            "(Bosch FIT + calories from app)"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
