# Urban Safari

FIT rides → one map → video clips synced to GPS with frame paths over the track.

**Urban safari content pipeline:** collect rides from bike computers, show every path
together, align helmet/bar/chest camera footage to the ride, scrub video and map in sync.

## Install

```bash
pip install fitparse
pip install pymobiledevice3   # optional: Bosch Flow iPhone sync
# ffprobe via: brew install ffmpeg
```

## Commands

```bash
python scripts/build_web_assets.py --trips-dir ./rides --out ./web/data
python scripts/pipeline.py --sync --trips-dir ./rides --out ./web/data
python scripts/sync_video.py --videos-dir ./videos --data-dir ./web/data
python scripts/map_transcript.py --video-id CLIP --video FILE --data-dir ./web/data
python scripts/inspect_fit.py ride.fit
```

## What you get

```
web/data/
  manifest.json          # trip list + map config
  trips/{id}.geojson     # ride track
  trips/{id}.series.json # speed, power, cadence vs time
  videos/{id}.track.json # video keyframes on the ride
  videos/{id}.transcript.json  # clustered speech labels
  videos/{id}.transcript.geojson  # Point features for map
  videos/{id}.geojson    # path of video frames over the map
```

Full contract: [DATA-CONTRACT.md](DATA-CONTRACT.md)

## Demo

Synthetic public demo (no real GPS): [examples/demo/web/data/](examples/demo/web/data/)

## Devices

| Device | How |
|--------|-----|
| Bosch eBike Flow | `sync_flow_trips.py` (iPhone USB) |
| XOSS G | [Abraham's enhanced_xoss_sync](https://github.com/molleraj/enhanced_xoss_sync) → `./rides` |
| Any FIT file | drop in `./rides/` |

## MOOLLM skill

[SKILL.md](SKILL.md) · [CARD.yml](CARD.yml) · [GLANCE.yml](GLANCE.yml)

Private instance that seeded this skill: Marconistraat25 `ebike/` (real GPS stays there).
