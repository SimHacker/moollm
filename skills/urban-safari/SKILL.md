---
name: urban-safari
description: FIT ride pipeline for map views and video sync — urban safari content pipeline. Bosch Flow, XOSS G adapters, GeoJSON web contract, ffprobe video keyframes.
allowed-tools: [Shell, Read, Write]
related: [change-name, simulation]
tags: [gps, fit, video, ebike, map, pipeline]
---

# Urban Safari — ride map + video sync pipeline

Lifted from the Marconistraat25 private ebike workflow into a shareable MOOLLM skill. FIT files
in, static JSON for a map app out, optional video clips synced to GPS with frame paths drawn
over the track.

Part of [MOOLLM](../../README.md). See [skills/README.md](../README.md).

## Quick start

```bash
cd skills/urban-safari
pip install fitparse

# Any FIT files in ./rides/
python scripts/build_web_assets.py --trips-dir ./rides --out ./web/data

# Bosch Flow iPhone (USB)
pip install pymobiledevice3
python scripts/pipeline.py --sync --trips-dir ./rides --out ./web/data \
  --home-label "Your Home" --home-lat 52.33 --home-lon 4.78

# Video sync (needs ffprobe)
python scripts/sync_video.py --videos-dir ./videos --data-dir ./web/data
```

Synthetic demo (no real GPS): [examples/demo/web/data/](examples/demo/web/data/).

## Protocol

### SYNC — pull rides from device

| Device | Command |
|--------|---------|
| Bosch Flow (iPhone USB) | `sync_flow_trips.py --dest ./rides` |
| XOSS G (BLE) | [enhanced_xoss_sync](https://github.com/molleraj/enhanced_xoss_sync) → `./rides` |
| Manual | copy `.fit` into `./rides/` |

### BUILD — FIT → web JSON

`build_web_assets.py` writes `manifest.json` + per-trip GeoJSON, series, meta.
Bosch duplicate rows merged per timestamp (see `bosch-fit-quirks.md`).

### INSPECT — diagnose a FIT

```bash
python scripts/inspect_fit.py ride.fit
```

### SYNC_VIDEO — align clips to trips

1. `ffprobe` reads video `creation_time` and duration
2. Auto-match picks trip with best wall-clock overlap
3. Interpolate GPS from trip series at each video second
4. Write `videos/{id}.track.json` + `videos/{id}.geojson` (frame path)

```bash
python scripts/sync_video.py --video clip.mp4 --trip-id my-ride --data-dir ./web/data
python scripts/sync_video.py --videos-dir ./videos --data-dir ./web/data  # auto-match all
python scripts/sync_video.py --video clip.mp4 --offset-s 2.5 --data-dir ./web/data  # clock skew
```

**Calibration trick:** film your bike computer clock for one second at ride start; measure
offset between video frame and FIT timestamp; pass `--offset-s`.

### MAP_TRANSCRIPT — words on the map, clustered

Requires synced video track (`SYNC_VIDEO`). Whisper transcribes the clip; each segment gets
GPS from the video keyframe at its temporal midpoint; nearby segments merge into readable
labels.

```bash
python scripts/map_transcript.py --video-id img-0679 --data-dir ./web/data \
  --video ~/Movies/IMG_0679.MOV \
  --cluster-radius-m 40 --cluster-gap-s 20 --min-words 3
```

Clustering merges segments when within **40 m** and **20 s** (defaults). Tune for urban
density: tighter radius in old city centers, wider on open dike roads.

Or full pipeline with transcription:

```bash
python scripts/pipeline.py --sync --videos-dir ./videos --out ./web/data --map-transcripts
```

Output: `videos/{id}.transcript.json` + Point GeoJSON for map labels. See
[DATA-CONTRACT.md](DATA-CONTRACT.md#transcript-on-the-map-clustered).

### MATCH — map UI integration

Read [DATA-CONTRACT.md](DATA-CONTRACT.md). Load `manifest.json`, fetch trip GeoJSON for all
rides, union bounds for overview map. On video play, scrub marker along `keyframes[]`.

## Web app sketch (SvelteKit + MapLibre)

1. Static copy of `web/data/` → `static/safari/data/`
2. `fetch('/safari/data/manifest.json')`
3. Draw all `trips[].geojson` as layers (color by trip)
4. For selected trip + video: draw video track LineString; `<video>` `timeupdate` → marker

## Privacy

FIT and video contain exact GPS. Do not commit real tracks to public repos. Use
`examples/demo/` for public demos; trekify before sharing.

## Device adapters

See [adapters/README.md](adapters/README.md). XOSS integration is a natural collaboration
with Abraham Moller — his BLE sync lands FITs; this skill builds the shared map + video layer.

## See also

- [DATA-CONTRACT.md](DATA-CONTRACT.md)
- [bosch-fit-quirks.md](bosch-fit-quirks.md)
- [simulation/examples/urban-safari-ride-game.yml](../simulation/examples/urban-safari-ride-game.yml)
