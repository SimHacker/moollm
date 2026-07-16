# Object Collections

Curated sets of objects from expansion packs, community creators, and themed bundles.

## Available Collections

### SimProv Base Game
**Source**: `simprov/GameData/Objects/Objects.far`
The complete base game object catalog. Every object that shipped with The Sims 1 in February 2000. Approximately 150 unique objects across all categories.

### Expansion Pack Objects
Objects added by The Sims expansion packs:
- **Livin' Large**: Additional electronics, career reward objects
- **House Party**: Party supplies, DJ booth, dance floor
- **Hot Date**: Downtown objects, restaurant furniture
- **Vacation**: Resort items, camping gear
- **Unleashed**: Pet objects, outdoor items
- **Superstar**: Fame objects, recording studio

### Community Content
**Source**: `TheSimsDownloads/` — 3,313 community-created .iff files
Custom objects created by The Sims modding community (2000-2005). Includes:
- Custom furniture and electronics
- Themed object sets (medieval, futuristic, holiday)
- Functional objects with custom animations
- Decorative items and wall art

### SimFreaks Archive
**Source**: `simprov/Downloads/`
Curated community content from the SimFreaks era. Quality-filtered custom objects with documentation.

## Import Pipeline

```bash
# Extract objects from a .far archive
python3 -m simobliterator catalog path/to/Objects.far --output ./

# Index a collection of .iff files
python3 -m simobliterator index path/to/iff-files/ --output ./collection-name/
```

## See Also

- [Exchange](../../exchange/README.md) — Import/export hub
- [Transmogrifier](../../tools/transmogrifier/) — AI-powered object editor
