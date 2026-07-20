# Device adapters — urban safari ingest

The urban-safari pipeline converges on **FIT → web JSON**. Each device is a thin adapter
that lands `.fit` files in your `rides/` directory (or calls `build_web_assets.py` directly).

## Bosch eBike Flow (implemented)

```bash
pip install pymobiledevice3
python scripts/sync_flow_trips.py --dest ./rides
```

Bundle ID: `com.bosch.ebike.flow`. Same API Finder uses over USB.

Raw Bosch FIT may need [Flow FIT](https://hacdias.github.io/flowfit/) before Garmin import.
The web pipeline merges duplicate records read-only — see `bosch-fit-quirks.md`.

## XOSS G bike computer (Abraham Moller)

[enhanced_xoss_sync](https://github.com/molleraj/enhanced_xoss_sync) — BLE sync via `bleak`,
argparse CLI, FIT export without XOSS cloud.

Suggested integration:

```bash
# Abraham's tool → your rides directory
python /path/to/enhanced_xoss_sync.py --save_all_files --dest ./rides

# Then shared pipeline
python scripts/build_web_assets.py --trips-dir ./rides --out ./web/data
```

XOSS FITs are expected to be clean (no Bosch duplicate-row merge needed). Run
`inspect_fit.py` once to confirm.

## GPX / Strava / Komoot

Not implemented yet. GPX lacks power/cadence; prefer FIT when available.

## Video sources

| Camera | GPS in file | Sync method |
|--------|-------------|-------------|
| iPhone | QuickTime `creation_time` + optional location atoms | `sync_video.py` + trip overlap |
| GoPro | GPMF telemetry track | future: extract GPMF, skip FIT interpolation |
| Action cam (no GPS) | none | Manual `--offset-s` + trip match only |
