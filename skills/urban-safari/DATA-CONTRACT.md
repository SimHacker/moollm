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

## Transcript on the map (clustered)

After `sync_video.py`, run `map_transcript.py` to place spoken words on the route and
**cluster** nearby segments for readable labels.

```bash
python scripts/map_transcript.py --video-id img-0679 --data-dir ./web/data \\
  --video /path/to/IMG_0679.MOV --cluster-radius-m 40 --cluster-gap-s 20
```

### videos/{id}.transcript.json

```json
{
  "id": "img-0679",
  "trip_id": "badhoevedorp-roundtrip-…",
  "cluster_params": { "radius_m": 40, "max_gap_s": 20, "min_words": 3 },
  "segment_count": 842,
  "cluster_count": 67,
  "clusters": [
    {
      "video_s_start": 120.5,
      "video_s_end": 138.2,
      "duration_s": 17.7,
      "lat": 52.338,
      "lon": 4.785,
      "text": "look at that bridge over the canal …",
      "word_count": 24,
      "segment_count": 3,
      "span_m": 12.4
    }
  ],
  "geojson": "videos/img-0679.transcript.geojson"
}
```

### Clustering rules

Segments merge into one map label when **both**:

- **Distance** ≤ `cluster_radius_m` (default 40 m) between segment midpoints
- **Time gap** ≤ `cluster_gap_s` (default 20 s) between consecutive segments

Clusters with fewer than `min_words` (default 3) are dropped unless they contain 2+
segments. Centroid is the mean lat/lon of member segments; `text` is joined utterance.

### videos/{id}.transcript.geojson

Point features (`kind: transcript_cluster`) with `text`, `video_s_start`, `video_s_end`,
`word_count`. Map UI tips:

- Show clusters when zoom ≥ 14; hide individual words until zoom ≥ 17
- Highlight active cluster when `video_s` is within `[start, end]`
- Offset label anchor by `bearing_deg` from video track so text sits beside the path

Whisper JSON is cached under `web/data/cache/{video-stem}.whisper.json`.

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
