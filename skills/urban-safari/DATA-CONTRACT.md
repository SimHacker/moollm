# Urban Safari — web data contract

The **pipeline** (Python, in `scripts/`) produces static JSON under `web/data/`. Your map
app (SvelteKit, plain HTML, etc.) only reads these files — no FIT parsing in the browser.

## Run the pipeline

```bash
pip install fitparse

# Build map assets from FIT files in ./rides/
python scripts/build_web_assets.py --trips-dir ./rides --out ./web/data

# Full pipeline: optional iPhone sync + build + video sync
python scripts/pipeline.py --sync --trips-dir ./rides --out ./web/data \
  --videos-dir ./videos --home-label "Demo City" --home-lat 52.0 --home-lon 5.0
```

Video sync requires `ffprobe` (ffmpeg).

## Output layout

```
web/data/
  manifest.json
  trips/
    {trip-id}.geojson
    {trip-id}.series.json
    {trip-id}.meta.json
  videos/                    # after sync_video.py
    {video-id}.track.json
    {video-id}.geojson
    {clip}.mp4               # optional if --copy-media
```

`trip-id` is the FIT filename slugified.

## manifest.json

| Field | Purpose |
|-------|---------|
| `home` | Default map center |
| `map.tile_url` | OSM raster tiles |
| `trips[]` | Sorted newest first |
| `videos[]` | All synced clips (flat index) |

Each trip entry includes paths to `geojson`, `series`, `meta`, and optional `videos[]`.

## trips/{id}.series.json

Per-point time series for charts and map scrubber:

```json
{
  "id": "demo-loop",
  "points": [
    {
      "t": "2026-01-01T10:00:00+00:00",
      "lat": 52.0,
      "lon": 5.0,
      "alt_m": 10.0,
      "speed_kmh": 18.0,
      "power_w": 120,
      "cadence_rpm": 65,
      "distance_m": 0.0
    }
  ]
}
```

## Video sync (urban safari content pipeline)

After `sync_video.py`, each clip gets a **track** sampled along wall-clock time:

### videos/{id}.track.json

```json
{
  "id": "morning-clip",
  "trip_id": "demo-loop",
  "probe": {
    "creation_time": "2026-01-01T10:00:05+00:00",
    "duration_s": 120.0
  },
  "sync": {
    "method": "creation_time",
    "offset_s": 0.0,
    "sample_hz": 1.0
  },
  "keyframes": [
    {
      "video_s": 0.0,
      "t": "2026-01-01T10:00:05+00:00",
      "lat": 52.0,
      "lon": 5.0,
      "bearing_deg": 45.0
    }
  ],
  "geojson": "videos/morning-clip.geojson"
}
```

### Matching logic

1. `ffprobe` reads video `creation_time` + duration
2. Auto-match picks the trip whose GPS series overlaps that wall-clock span most
3. `--offset-s` corrects clock skew (film your bike computer for a frame-accurate offset)
4. GPS is **interpolated** from the trip series at each video second

### Map UI playback

1. Load trip LineString + video track LineString (often a sub-segment)
2. `<video timeupdate>` → find keyframe at `video_s` → move marker + bearing arrow
3. Scrubbing the map timeline seeks the video

Multi-rider: each clip gets its own track on the same trip map (or different trips on one
overview map via `manifest.trips[]` bounds union).

## Device adapters

| Source | Ingest script | Status |
|--------|---------------|--------|
| Bosch eBike Flow (iPhone) | `sync_flow_trips.py` | Done |
| Any `.fit` on disk | `build_web_assets.py` | Done |
| XOSS G (BLE) | [enhanced_xoss_sync](https://github.com/molleraj/enhanced_xoss_sync) | Plug-in adapter (Abraham) |
| GoPro GPMF | future | In-camera GPS track |

## Privacy

FIT files and synced videos contain **exact GPS and home patterns**. For public repos:

- Keep raw FITs and videos **local** or in a private repo
- Publish only trekified demo data (see `examples/demo/`)
- Never check real tracks into public git without anonymization
