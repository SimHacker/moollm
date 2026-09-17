# SimObliterator Suite — API Reference

Comprehensive Python tool suite for reading, analyzing, editing, and writing The Sims 1 game files. 230 Python files. 60+ IFF chunk parsers. 5 mesh formats. Full BHAV bytecode lifecycle. Save file editing with safety model.

Repo: `../SimObliterator_Suite/` (sister directory, not embedded)
Entry point: `obliterator.py` (CLI wrapper, sniffable Python)
Dependencies: `dearpygui>=1.10.0` (GUI only), `Pillow>=10.0.0` (optional), `numpy>=1.24.0`

## CLI Entry Point

`obliterator.py` is the single CLI interface. 17 commands, 5 output formats.

```
obliterator.py iff-info     <file.iff>                    # chunk count, type distribution
obliterator.py iff-chunks   <file.iff> [--type BHAV]      # list chunks with type/id/label/size
obliterator.py iff-strings  <file.iff> [--lang 0]         # string tables by language
obliterator.py iff-objects  <file.iff>                    # OBJD list: GUID, name, price
obliterator.py iff-bhav     <file.iff> [--id 256]         # list or decompile BHAVs
obliterator.py far-list     <archive.far>                 # list archive contents
obliterator.py far-extract  <archive.far> <outdir>        # extract files
obliterator.py inspect      <Neighborhood.iff>            # families + characters overview
obliterator.py families     <Neighborhood.iff>            # family budgets
obliterator.py character    <Neighborhood.iff> <name>     # full character sheet
obliterator.py traits       <Neighborhood.iff> <name>     # personality trait bars
obliterator.py skills       <Neighborhood.iff> <name>     # skill level bars
obliterator.py set-trait    <Neighborhood.iff> <name> <trait> <0-10>
obliterator.py set-skill    <Neighborhood.iff> <name> <skill> <0-10>
obliterator.py set-money    <Neighborhood.iff> <family_id> <amount>
obliterator.py dump-raw     <Neighborhood.iff> <name>     # raw PersonData with field names
obliterator.py uplift       <Neighborhood.iff> <name>     # MOOLLM YAML output

Output: -f table (default) | json | yaml | csv | raw
```

## Directory Structure

```
SimObliterator_Suite/
├── obliterator.py              # CLI entry point (sniffable Python)
├── launch.py                   # GUI launcher (DearPyGUI)
├── requirements.txt            # dearpygui, Pillow, numpy
├── src/
│   ├── main_app.py             # GUI application class
│   ├── utils/
│   │   └── binary.py           # IoBuffer, ByteOrder (binary I/O)
│   ├── formats/                # File format parsers
│   │   ├── iff/                # IFF format
│   │   │   ├── iff_file.py     # IffFile — main container
│   │   │   ├── base.py         # IffChunk base, chunk registry
│   │   │   └── chunks/         # 60 chunk type implementations
│   │   ├── far/                # FAR archives
│   │   │   ├── far1.py         # FAR1Archive
│   │   │   └── far3.py         # FAR3Archive + decompressor
│   │   ├── dbpf/               # DBPF packages (Sims 2+)
│   │   │   └── dbpf.py         # DBPFFile
│   │   └── mesh/               # 3D mesh formats
│   │       ├── bmf.py          # BMFMesh (binary mesh)
│   │       ├── bcf.py          # BCF (skeleton/animation)
│   │       ├── cfp.py          # CFP (compressed animation)
│   │       ├── skn.py          # SKN (text mesh source)
│   │       ├── cmx.py          # CMX (character manifest)
│   │       └── gltf_export.py  # glTF 2.0 exporter
│   └── Tools/
│       ├── core/               # 51 analysis modules
│       ├── entities/           # Entity representations
│       ├── forensic/           # Reverse engineering tools
│       ├── graph/              # Resource graph analysis
│       ├── gui/                # DearPyGUI interface
│       │   ├── panels/         # 26 panel implementations
│       │   └── safety/         # Edit safety model
│       ├── save_editor/        # Save file editing backend
│       └── webviewer/          # HTML/JS viewers
├── data/                       # Extracted databases
│   ├── characters.json         # Character appearance data
│   ├── objects.json            # Object catalog data
│   ├── opcodes_db.json         # 143 documented opcodes
│   ├── global_behavior_database.json
│   ├── global_behaviors.json
│   ├── meshes.json
│   ├── execution_model.json
│   └── unknowns_db.json
├── dev/
│   └── tests/                  # Test suite (247+ tests)
│       ├── tests.py            # Main runner
│       ├── test_api.py         # API tests (no game files needed)
│       ├── test_game.py        # Game file tests
│       └── test_persondata.py  # PersonData index verification (38 tests)
└── Docs/
    ├── guides/                 # User and developer guides
    ├── research/               # Reverse engineering research
    └── technical/              # Technical references
```

## Format Parsers

### IFF — Interchange File Format
`from formats.iff.iff_file import IffFile`

The core format. Every Sims 1 file (.iff) is an IFF container holding typed chunks.

```python
iff = IffFile.read("path/to/file.iff")       # read from disk
iff = IffFile.from_bytes(data, "name.iff")    # read from bytes
chunks = iff.chunks                            # all chunks
chunk = iff.get(OBJD, chunk_id=1)             # by type + ID
all_str = iff.get_all(STR)                    # all of a type
by_code = iff.get_by_type_code("BHAV")        # by 4-char code
print(iff.summary())                           # human summary
```

### IFF Chunk Types (60 parsers)

Every chunk type has a `read(iff, io)` method that parses from a binary stream.

| Type | Class | What |
|------|-------|------|
| STR# | `STR` | String tables (20 languages) |
| CTSS | `CTSS` | Catalog strings |
| OBJD | `OBJD` | Object definition (GUID, price, type, BHAV refs) |
| BHAV | `BHAV` | Behavior bytecode (SimAntics VM) |
| SPR# | `SPR` | Sprites (indexed color) |
| SPR2 | `SPR2` | Sprites v2 (alpha, z-buffer) |
| DGRP | `DGRP` | Draw groups (sprite compositions) |
| BCON | `BCON` | Behavior constants |
| GLOB | `GLOB` | Global data |
| SLOT | `SLOT` | Object routing slots |
| TTAB | `TTAB` | Interaction table (menus) |
| FAMI | `FAMI` | Family/household data |
| NBRS | `NBRS` | Neighbors (all Sims in neighborhood) |
| NGBH | `NGBH` | Neighborhood data, inventory |
| OBJf | `OBJf` | Object function table |
| CARR | `CARR` | Career data, job levels |
| OBJM | `OBJM` | Object instances in saves |
| HOUS | `HOUS` | House data |
| ARRY | `ARRY` | Array data |
| PALT | `PALT` | Color palette |
| ANIM | `ANIM` | Animation sequences |
| PIFF | `PIFF` | Patch data |
| TREE | `TREE` | Tree/quadtree structures |
| SIMI | `SIMI` | Sim instance data |
| RSMP | `RSMP` | Resource map |
| TPRP | `TPRP` | Tree properties |
| TRCN | `TRCN` | Tree constants |
| FWAV | `FWAV` | Sound/wave data |
| WALm | `WALm` | Wall data |
| FLRm | `FLRm` | Floor data |

### FAR Archives
```python
from formats.far.far1 import FAR1Archive
arc = FAR1Archive("Objects.far")
files = arc.list_files()                       # list filenames
data = arc.get_entry("filename.iff")           # get file bytes
arc.extract("filename.iff", "output/")         # extract one
arc.extract_all("output/")                     # extract all

from formats.far.far3 import FAR3Archive
arc3 = FAR3Archive("archive.far")              # FAR v3 (compressed)
data = arc3.get_entry_by_filename("name.iff")  # auto-decompresses
```

### Mesh Formats
```python
from formats.mesh.bmf import BMFReader, export_obj
mesh = BMFReader().read_file("body.bmf")       # binary mesh
export_obj(mesh, "output.obj")                 # export to OBJ

from formats.mesh.gltf_export import GLTFExporter
GLTFExporter().export(mesh, filepath="mesh.gltf")  # export to glTF

from formats.mesh.bcf import BCFReader
skeleton = BCFReader().read_file("skeleton.bcf")    # skeleton + animations
```

### DBPF (Sims 2+ packages)
```python
from formats.dbpf import DBPFFile
pkg = DBPFFile("package.package")
for entry in pkg.entries:
    data = pkg.get_entry(entry)
```

## Save File Editing

`from Tools.save_editor.save_manager import SaveManager, PersonData`

### SaveManager — High-Level API
```python
mgr = SaveManager("path/to/Neighborhood.iff")
mgr.load()

# Read
families = mgr.families                        # dict of FamilyData
neighbors = mgr.neighbors                      # dict of NeighborData
money = mgr.get_family_money(family_id)
rel = mgr.get_relationship(sim_id, target_id)  # [daily, lifetime]

# Write
mgr.set_family_money(family_id, 99999)
mgr.set_sim_skill(neighbor_id, "cooking", 800)      # 0-1000 scale
mgr.set_sim_personality(neighbor_id, "neat", 700)    # 0-1000 scale
mgr.set_sim_career(neighbor_id, job_type=8)          # science
mgr.set_relationship(sim_id, target_id, daily=80, lifetime=90)
mgr.max_all_skills(neighbor_id)
mgr.save()                                           # writes to disk (backup created)
```

### PersonData — Field Index Constants

Verified against original Sims 1 documentation. NOT FreeSO VM indices.

| Field | Index | Range | Notes |
|-------|-------|-------|-------|
| `NICE_PERSONALITY` | 2 | 0-1000 | grouchy → nice |
| `ACTIVE_PERSONALITY` | 3 | 0-1000 | lazy → active |
| `GENEROUS_PERSONALITY` | 4 | 0-1000 | selfish → generous |
| `PLAYFUL_PERSONALITY` | 5 | 0-1000 | serious → playful |
| `OUTGOING_PERSONALITY` | 6 | 0-1000 | shy → outgoing |
| `NEAT_PERSONALITY` | 7 | 0-1000 | sloppy → neat |
| `CLEANING_SKILL` | 9 | 0-1000 | |
| `COOKING_SKILL` | 10 | 0-1000 | |
| `CHARISMA_SKILL` | 11 | 0-1000 | kSocialSkill |
| `MECH_SKILL` | 12 | 0-1000 | kRepairSkill |
| `GARDENING_SKILL` | 13 | 0-1000 | hidden/internal |
| `MUSIC_SKILL` | 14 | 0-1000 | hidden/internal |
| `CREATIVITY_SKILL` | 15 | 0-1000 | kCreativeSkill |
| `LITERACY_SKILL` | 16 | 0-1000 | hidden/internal |
| `BODY_SKILL` | 17 | 0-1000 | kPhysicalSkill |
| `LOGIC_SKILL` | 18 | 0-1000 | |
| `JOB_TYPE` | 56 | 0-9 | career track ID |
| `JOB_STATUS` | 57 | varies | promotion flags |
| `PERSON_AGE` | 58 | 0-1 | 0=child, 1=adult |
| `SKIN_COLOR` | 60 | 0-2 | light/medium/dark |
| `JOB_PERFORMANCE` | 63 | 0-1000 | promotion probability |
| `GENDER` | 65 | 0-1 | 0=male, 1=female |
| `ZODIAC_SIGN` | 70 | 0-12 | 0=uncomputed, 1-12=signs |

Motives (hunger, comfort, hygiene, bladder, energy, fun, social, room) are NOT in PersonData. They are runtime engine state.

### FamilyData
```python
fam.chunk_id          # int
fam.house_number      # int
fam.family_number     # int (-1 for townies)
fam.budget            # int (Simoleons)
fam.member_guids      # list[int]
fam.is_townie         # bool
fam.is_user_created   # bool
fam.num_members       # int
```

### NeighborData
```python
neigh.neighbor_id     # int
neigh.guid            # int
neigh.name            # str
neigh.person_data     # list[int] (up to 88 int16s)
neigh.relationships   # dict[int, list[int]] (target_id → [daily, lifetime])
neigh.person_data_offset  # int (byte offset in file for direct edits)
```

## BHAV Analysis (SimAntics Bytecode)

`from formats.iff.chunks.bhav_decompiler import BHAVDecompiler, decompile_bhav`

Full lifecycle: disassembly, AST, decompilation, call graphs, validation, authoring.

```python
# Decompile a BHAV chunk
decompiler = BHAVDecompiler()
ast = decompiler.decompile(bhav_data, group_id=0, bhav_id=256)
for instr in ast.instructions:
    print(f"  [{instr.index}] opcode=0x{instr.opcode:04X}")

# Validate
from formats.iff.chunks.bhav_decompiler import BHAVValidator
is_valid, error = BHAVValidator().validate(bhav_data)

# Format as pseudocode
from formats.iff.chunks.bhav_formatter import BHAVFormatter, CodeStyle
code = BHAVFormatter(style=CodeStyle.READABLE).format(ast)

# Call graph
from Tools.core.bhav_call_graph import build_call_graph
graph = build_call_graph(iff)

# Disassemble with semantic names
from Tools.core.bhav_disassembler import disassemble_bhav
text = disassemble_bhav(bhav_chunk)
```

### BHAV Modules

| Module | What |
|--------|------|
| `bhav.py` | BHAV chunk parser (bytecode instructions) |
| `bhav_ast.py` | Abstract syntax tree, control flow graph |
| `bhav_decompiler.py` | Bytecode → pseudocode |
| `bhav_formatter.py` | AST → readable code (multiple styles) |
| `bhav_graph.py` | Flow graph analysis, ASCII visualization |
| `bhav_analysis.py` | Linting, metrics, dead code detection |
| `bhav_validator.py` | Structure validation, stack balance |
| `bhav_operands.py` | Operand decoding |
| `bhav_editor.py` | GUI editor (tkinter, lazy-loaded) |
| `bhav_beautifier.py` | Code beautification |
| `bhav_cross_reference.py` | Cross-referencing between BHAVs |
| `bhav_performance_analyzer.py` | Performance analysis |
| `primitive_registry.py` | Opcode → primitive name mapping |

### Core BHAV Tools (in Tools/core/)

| Module | What |
|--------|------|
| `bhav_authoring.py` | Create BHAVs from scratch |
| `bhav_call_graph.py` | Build call graphs across BHAVs |
| `bhav_disassembler.py` | Low-level bytecode disassembly |
| `bhav_executor.py` | Trace execution paths |
| `bhav_opcodes.py` | Opcode reference data |
| `bhav_operations.py` | BHAV editing pipeline |
| `bhav_patching.py` | Binary patching |
| `bhav_rewiring.py` | Call target rewiring |

## String Tables

`from Tools.core.str_parser import STRParser, ParsedSTR`

```python
parser = STRParser()
parsed = parser.parse(chunk_data, chunk_id=200)
text = parsed.get_string(index=0, language=0)    # US English
all_en = parsed.get_all_strings(language=0)
summary = parsed.get_localization_summary()       # missing translations

from Tools.core.str_parser import copy_language_to_missing
filled, count = copy_language_to_missing(parsed, source_language=0)
```

20 language slots: US English (0), UK English (1), French (2), German (3), Italian (4), Spanish (5), Dutch (6), Catalan (7), Czech (8), Danish (9), Swedish (10), Norwegian (11), Finnish (12), Hebrew (13), Russian (14), Portuguese (15), Japanese (16), Polish (17), Traditional Chinese (18), Simplified Chinese (19).

## Safety Model

SimObliterator uses a three-tier safety model for write operations:

| Mode | What | Risk |
|------|------|------|
| INSPECT | Read-only analysis | None |
| PREVIEW | Show proposed changes without applying | None |
| MUTATE | Apply changes with audit trail | Creates backups |

The `MutationPipeline` in `Tools/core/mutation_pipeline.py` enforces this for all write operations.

## Key Data Files

| File | Size | What |
|------|------|------|
| `data/characters.json` | 2MB+ | Extracted character appearance data (85k+ lines) |
| `data/objects.json` | 3MB+ | Extracted object catalog data |
| `data/opcodes_db.json` | | 143 documented SimAntics opcodes |
| `data/global_behavior_database.json` | | 251 base game globals + expansion ranges |

## Tests

```bash
cd dev/tests
python tests.py --api          # 174 API tests (no game files needed)
python tests.py --game         # 102+ game file tests (needs test_paths.txt)
python test_persondata.py      # 38 PersonData index verification tests
```

## Expansion Pack BHAV ID Ranges

Each expansion gets 256 global BHAV IDs:

| Pack | Range | Hex |
|------|-------|-----|
| Base Game | 256-511 | 0x100-0x1FF |
| Livin' Large | 512-767 | 0x200-0x2FF |
| House Party | 768-1023 | 0x300-0x3FF |
| Hot Date | 1024-1279 | 0x400-0x4FF |
| Vacation | 1280-1535 | 0x500-0x5FF |
| Unleashed | 1536-1791 | 0x600-0x6FF |
| Superstar | 1792-2047 | 0x700-0x7FF |
| Makin' Magic | 2048-2303 | 0x800-0x8FF |
