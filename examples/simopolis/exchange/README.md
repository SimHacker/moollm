# The Simopolis Exchange

**Import your past. Export your future.**

The Exchange is Simopolis's import/export hub — a reimagining of The Sims Exchange (thesims.ea.com, circa 2000-2008) where players shared families, houses, and objects. The original Exchange was a website. This one is a directory structure with pipelines.

## How It Works

### Importing (Uplift)

Drop a `.FAM` or `.iff` save file into `imports/`. The Uplift pipeline reads it:

1. **SimObliterator** parses the binary (PersonData: 88 shorts per Sim)
2. **Extraction**: traits, skills, needs, career, relationships, appearance
3. **Mapping**: Sims traits → `sims:` block, synthesize `mind_mirror:` from personality
4. **Enrichment**: LLM generates soul_philosophy, emoji_identity, description
5. **Output**: Full character directory with CHARACTER.yml, CARD.yml, GLANCE.yml, README.md
6. **Placement**: Character moves to `characters/` as a Simopolis citizen

### Exporting (Download)

Select a character from `characters/`. The Download pipeline writes them back:

1. **Read** CHARACTER.yml `sims:` block
2. **Map** traits/skills/needs back to PersonData shorts
3. **SimObliterator** writes `.FAM` or patches existing `.iff`
4. **Output** lands in `exports/` ready for The Sims to load

## Directory Structure

```
exchange/
├── README.md         # This file
├── imports/          # Staging area for uploaded save files
├── exports/          # Generated save files for download
├── templates/        # Blank family, blank character, starter homes
└── collections/      # Curated content sets (SimProv, SimFreaks, etc.)
```

## Templates

| Template | Description |
|----------|-------------|
| `templates/blank-sim.yml` | Empty CHARACTER.yml template for creating new Sims |
| `templates/family-template.yml` | Family structure template with relationships |

## Collections

Content sets from the original Sims community:

| Collection | Source | Contents |
|------------|--------|----------|
| SimProv | simprov/GameData/ | Career tracks, UI text, base game objects |
| SimFreaks | simprov/Downloads/ | Community-created content |
| SimSlice | Archive | Custom objects and skins |
| TheSimsDownloads | TheSims/TheSimsDownloads/ | 3,313 community .iff files |

## Pipeline Commands

```bash
# Uplift a family save
python3 -m simobliterator uplift imports/Newbie_1.FAM --output ../characters/

# Export a character back to binary
python3 -m simobliterator download ../characters/bob-newbie/ --output exports/

# Catalog objects from a .far archive
python3 -m simobliterator catalog imports/Objects.far --output ../objects/

# Generate a family album from save data
python3 -m simobliterator album imports/Goth_5.FAM --output ../albums/goth-family/
```

## See Also

- [SimObliterator Suite](../../../../SimObliterator_Suite/) — Binary format tools
- [Characters](../characters/README.md) — Where uplifted Sims live
- [Objects](../objects/README.md) — Cataloged game objects
- [Templates](./templates/) — Blank forms for new content
