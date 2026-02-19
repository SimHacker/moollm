# Datasette Skill

Bridge between cursor-mirror's SQLite data and Simon Willison's
[Datasette](https://datasette.io) web explorer.

cursor-mirror reads Cursor's internal databases and produces SQLite
indexes. Datasette serves those databases with a web UI, JSON API,
full-text search, faceting, and 154+ plugins. One command, zero backend.

## Files

| File | Purpose |
|------|---------|
| GLANCE.yml | Quick orientation (5 lines) |
| CARD.yml | Interface card: methods, advertisements, integration points |
| SKILL.md | Full protocol: quick start, queries, Datasette commands |
| README.md | This file |
| designs/DATASETTE-CURSOR-MIRROR-INTEGRATION.md | 5-phase integration plan |

## Quick Start

```bash
cd skills/cursor-mirror
source .venv/bin/activate
pip install datasette

# Export cursor-mirror data
python -c "
import sys; sys.path.insert(0,'.')
from lib.datasette_export import export_datasette
from pathlib import Path
print(export_datasette(Path('cursor-mirror.db')))
"

# Open in browser
datasette cursor-mirror.db -o
```

## Integration Status

- Phase 1: Direct serve -- DONE (works now)
- Phase 2: Consolidated export -- DONE (lib/datasette_export.py)
- Phase 3: Datasette plugin -- PLANNED
- Phase 4: Canned queries -- PLANNED (SQL in SKILL.md ready to use)
- Phase 5: Live streaming -- PLANNED (after R5 live daemon)
