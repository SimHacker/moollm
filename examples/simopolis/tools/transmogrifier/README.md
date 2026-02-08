# The Transmogrifier — Then and Now

Written by Don Hopkins for Maxis (2000). The first tool that let anyone create content for The Sims. Clone an object, export its sprites as BMP files, edit them in Photoshop, import them back. Over a million custom objects were made with it.

The original Transmogrifier was deliberately limited in scope — sprites and catalog text only, no behaviors, no routing, no string tables. "Simple tool that enables many people to create content." That philosophy was right. The limitation was what to do next.

Simopolis picks up where Transmogrifier left off: everything the original couldn't do, plus AI-powered creation, plus round-trip YAML instead of XML, plus all 20 languages.

## What the Original Could Do

- **Clone** any object in the game (create an editable copy with a new GUID)
- **Export** sprites as BMP files (pixel + z-buffer + alpha as separate files)
- **Import** modified BMPs back (with palette quantization and dithering)
- **Edit** catalog name, description, and price
- **View** objects with rotation and zoom controls
- **Automate** via OLE/COM (Rug-O-Matic, ShowNTell, web servers used this)

## What It Couldn't Do

Everything else: BHAV behavior scripts, STR# string tables, SLOT routing positions, TTAB interaction menus, character skins, animations, sounds, walls, floors. The documentation was explicit about this, and promised "future versions" and "other tools" would extend the XML format to cover more data types.

We're building those future versions now. Twenty-five years later, in YAML instead of XML.

## The Original Architecture

Source: `TheSims/SimsKit/Transmogrifier/` (written by Don Hopkins)

### Key Source Files

| File | Lines | What |
|------|-------|------|
| `XMLExporter.cpp` | 2,230 | Export objects to XML + BMP sprite files |
| `XMLImporter.cpp` | 5,020 | Import XML + BMP files back to IFF |
| `Quantizer.cpp` | 2,080 | Heckbert median-cut color quantization with Floyd-Steinberg dithering |
| `Sprite2Compressor.cpp` | 1,215 | RLE compression for SPR2 sprite format |
| `BitmapUtilities.cpp` | 1,044 | BMP file reading/writing with RLE8 support |
| `Cloner.cpp` | 820 | Object cloning with GUID generation |
| `TransmogrifierDlg.cpp` | 2,736 | Main UI dialog |
| `Transmogrifier.odl` | 111 | OLE Automation interface definition |
| `Objectifier.py` | 147 | Python OLE automation example |

### XML Format

The export format used an XML root element with configuration flags:

```xml
<objectsexportedfromthesims
  objectfilename="flamingo039055.iff"
  exportsprites="1"
  exportbitmaps="1"
  exportdrawgroups="1"
  exportobjectdefinitions="1"
  justchangecolors="0"
  exportallzooms="1"
  smoothsmallzoomcolors="1"
  exportp="1" exportz="1" exporta="1"
  generatez="1" generatea="1"
  compressbitmaps="1"
  createsubdirectories="1">

  <objectdefinitions>
    <objectdefinition name="Flamingo" id="128" guid="..." price="12" ... />
  </objectdefinitions>

  <sprites>
    <sprite id="...">
      <spriteframe index="0" zoom="large" rot="nw" width="136" height="384"
                   paletteid="1" transparentpixel="230">
        <spritechannel type="pixel" filename="flamingo_sprites/sprite0001/flamingo_large_nw_p.bmp"/>
        <spritechannel type="zbuffer" filename="...nw_z.bmp"/>
        <spritechannel type="alpha" filename="...nw_a.bmp"/>
      </spriteframe>
    </sprite>
  </sprites>

  <drawgroups>...</drawgroups>
  <bitmaps>...</bitmaps>
</objectsexportedfromthesims>
```

### Sprite Export Convention

Each sprite frame exported as three BMP files:
- `_p.bmp` — pixel data (8-bit indexed color)
- `_z.bmp` — z-buffer (grayscale depth)
- `_a.bmp` — alpha channel (grayscale transparency)

Directory structure when `createsubdirectories` is enabled:
```
flamingo_sprites/
  sprite0001/
    flamingo_large_nw_p.bmp
    flamingo_large_nw_z.bmp
    flamingo_large_nw_a.bmp
    flamingo_large_ne_p.bmp
    ...
    flamingo_medium_nw_p.bmp
    ...
    flamingo_small_nw_p.bmp
    ...
```

### Transparency Handling

The transparent color is NOT hardcoded blue. The Transmogrifier finds the least-used palette entry closest to yellow `RGB(255, 255, 0)` and designates it as the transparent pixel. The `transparentpixel` attribute in the XML records which palette index is transparent for each frame. Users saw blue backgrounds in Photoshop because the game's default palette used blue for the transparent slot — but this is a palette convention, not a format requirement.

### Palette Quantization (Quantizer.cpp)

The Quantizer implements Heckbert's median-cut algorithm:

1. **Collect** — scan all pixel colors into a 3D histogram
2. **Select** — median-cut partitioning to find optimal 255 colors (one slot reserved for transparency)
3. **Reduce** — map each pixel to nearest palette entry with Floyd-Steinberg error diffusion

Color distance weighting: green channel weighted 3x, red 2x, blue 1x (matches human perception).

When importing, if `justchangecolors` is true, the quantizer builds a shared palette across ALL sprite frames so colors are consistent across rotations and zoom levels.

### SPR2 Compression (Sprite2Compressor.cpp)

SPR2 uses run-length encoding with these token types:
- `kClear` — transparent run (skip N pixels)
- `kRunP` — pixel-only run (color data, no z/alpha)
- `kRunZP` — pixel + z-buffer run
- `kRunZPA` — pixel + z-buffer + alpha run
- `kNL` — new line (end of row)
- `kSL` — start line (begin new row)

The compressor walks each row of the image, identifies runs of similar transparency/channel state, and emits the most compact token type for each run.

## OLE Automation (How Rug-O-Matic Used It)

The Transmogrifier registered as a COM server: `Transmogrifier.Application`. External tools could drive it programmatically.

### The Rug-O-Matic Workflow

Rug-O-Matic (also by Don Hopkins) created custom rugs from user images:

1. `CreateDispatch("Transmogrifier.Application")` — launch Transmogrifier
2. `StartUp()` — initialize
3. `ScanDirectory()` — find template rug objects
4. `CloneObject(templateID)` — clone the 1x1 rug template
5. `ExportObject(objectFile, xmlFile)` — export to XML + BMPs
6. Transform user's image into isometric diamond perspective for each zoom/rotation
7. Save transformed images as BMPs to the sprite directory
8. `ImportObject(xmlFile)` — import modified XML + new BMPs back to IFF
9. `SetObjectName/Description/Price()` — set catalog metadata
10. `ExportObjectPreview()` — generate catalog thumbnail

This same pattern powered Don's web-based tombstone maker and other dynamic object generators. The key insight: Transmogrifier as a headless service, not just a GUI tool.

### Python OLE Example (Objectifier.py)

```python
import win32com.client
tmog = win32com.client.DispatchEx('Transmogrifier.Application')
tmog.MagicCookie = "..."
tmog.StartUp()
tmog.ScanDirectory()
# ... clone, export, modify, import ...
tmog.ShutDown()
```

## ShowNTell

An ActiveX control that used Transmogrifier's OLE interface to display slideshows of Sims objects. It called `ExportObjectPreview()` to generate preview images and `GetObjectName/Description/Price()` to read metadata. A predecessor to the Simopolis family album concept.

## FreeTheSims

An ActiveX control for extracting and exporting character content (bodies, dressings). Used `cBMPParser` for image handling. Simpler than Rug-O-Matic — focused on content liberation rather than creation.

## Simopolis Transmogrifier (The Modern Version)

Our replacement uses IFF-OBJECT.yml instead of XML, PNG instead of BMP, and covers ALL chunk types:

| Aspect | Original (2000) | Simopolis (2026) |
|--------|-----------------|------------------|
| Format | XML | YAML (IFF-OBJECT.yml) |
| Sprites | BMP (_p, _z, _a) | PNG with alpha, separate .zbuf.png |
| OBJD | Yes (XML attributes) | Yes (YAML with symbolic refs) |
| BHAV | No | Yes (structured YAML with labels and symbolic opcodes) |
| STR# | No | Yes (all 20 languages) |
| TTAB | No | Yes (interaction menus with motive effects) |
| SLOT | No | Yes (routing positions with facing) |
| OBJf | No | Yes (event -> BHAV dispatch table) |
| Palette | 8-bit indexed BMP | Full-color PNG, quantize on import |
| Dithering | Floyd-Steinberg | Floyd-Steinberg + ordered option |
| Z-buffer | Exported as BMP | Auto-generated "cardboard cutout" if missing |
| Alpha | Exported as BMP | From PNG transparency |
| Automation | OLE/COM (Windows) | CLI (obliterator.py, cross-platform) |
| Multi-tile | Handled internally | Explicit master/slave in YAML |
| Variations | Handled internally | Explicit variation_group in YAML |
| Languages | English only | All 20 Sims languages |
| AI creation | No | LLM generates YAML from descriptions |

The architecture is the same: export to an editable intermediate format, modify with external tools (Photoshop then, AI now), import back. The scope is everything Transmogrifier promised for "future versions."

## The Autofac Vision (from Autofac.txt)

Don Hopkins planned a whole family of "-O-Matic" tools, each a specialized simple UI for making custom objects from templates injected with user content. Transmogrifier would run in batch mode, driven by each tool via OLE:

| Tool | Template | User Provides |
|------|----------|--------------|
| **Rug-O-Matic** | Rug (1x1, 1x2, 2x3, 3x3, animated) | Image |
| **Art-O-Matic / Pict-O-Matic** | Painting / tapestry | Image(s), magic pictures that animate |
| **Column-O-Matic** | Square or round column | Image wrapped around it |
| **Counter-O-Matic** | Counter surface | Image on the surface |
| **Table-O-Matic** | Table surface | Image on the surface |
| **Car-O-Matic** | Car | Decal |
| **Door-O-Matic** | Door | Sign image |
| **Sign-O-Matic** | Sign | Image or lettering |
| **Dance-O-Matic** | Dance floor | Image |
| **PetBed-O-Matic** | Pet bed | Pet's name |
| **TV-O-Matic / Televis-O-Matic** | TV set | Pictures |
| **Radi-O-Matic / Stere-O-Matic** | Radio/stereo | Music |
| **BackDrop-O-Matic** | Stage backdrop | Pictures |

Only Rug-O-Matic was completed. With `obliterator.py tmog export/import` + AI image generation, we can now build ALL of these as LLM-driven YAML templates. The pattern is the same: clone template, inject content, import back. The content injection is now "describe what you want" instead of "open Photoshop."

## The Full OLE API (from Autofac.txt)

The Transmogrifier exposed a comprehensive COM automation API beyond what the GUI offered:

**Object management**: `CloneObject`, `ExportObject`, `ImportObject`, `ExportObjectPreview`
**Resource-level access**: `ExportResource`, `ImportResource`, `DeleteResource`, `GetResourceName`, `SetResourceName`, `CountResources`, `GetResourceID`, `CountResourceTypes`, `GetResourceType`
**Image-level access**: `ExportImage`, `ImportImage`, `ExportThumbnail`, `ImportThumbnail`
**OBJD-level access**: `ExportOBJD`, `ImportOBJD`
**Directory scanning**: `ScanDirectory`, `CountObjects`, `GetObjectName`, `GetObjectFileName`, `FindObjectIndexByName`

The resource-level and image-level APIs were never exposed in the GUI — they existed for programmatic tools. `obliterator.py` replicates all of these as CLI commands.

## RSS Feed for Sims Objects (from RSS.txt)

Don Hopkins designed XML namespaces for syndicating Sims content via RSS:

```xml
xmlns:SimsObject="http://www.TheSimsTransmogrifier.com/SimsObject"
xmlns:SimsCharacter="http://www.TheSimsTransmogrifier.com/SimsCharacter"
xmlns:SimsSkin="http://www.TheSimsTransmogrifier.com/SimsSkin"
xmlns:SimsLot="http://www.TheSimsTransmogrifier.com/SimsLot"
xmlns:SimsFamily="http://www.TheSimsTransmogrifier.com/SimsFamily"
xmlns:SimsAlbum="http://www.TheSimsTransmogrifier.com/SimsAlbum"
xmlns:SimsPage="http://www.TheSimsTransmogrifier.com/SimsPage"
```

Each object would be an RSS item with standard title/description plus Sims-specific properties like `SimsObject:CatalogPrice` and `SimsObject:GUID`. This was the precursor to Simopolis Exchange — syndicated content distribution. In 2026, the YAML schemas (SIMS-UPLIFT.yml, IFF-OBJECT.yml, SIMS-ALBUM.yml) serve the same purpose without the RSS wrapper.

## The SimsKit Python Ecosystem

The SimsKit directory contains Don Hopkins' Python tools for The Sims:

| File | Lines | What |
|------|-------|------|
| `SimsKit.py` | 3,900 | SWIG-generated Python bindings to the C++ engine (skeletons, suits, skills, animations) |
| `SimsKitUtils.py` | 210 | Utility functions: timer-based animation loop, object ownership management |
| `Personifier.py` | 1,562 | Tkinter GUI for browsing/editing character content (skins, bodies, animations) |
| `CellularSims.py` | 55 | Cellular automata integration with Sims textures |
| `SimsZope.py` | 4 | Zope/Plone CMS integration stub |
| `Objectifier.py` | 147 | COM automation script for scanning/extracting objects |

### Personifier.py

A Tkinter application that browses Sims character content — skins, bodies, animations — with filterable list views and tabbed panels. The design patterns (owned objects with finalizers, timer-based animation, filterable content browsers) map directly to what we're building in Simopolis.

### AethOTron (Cellular Automata Engine)

SWIG-wrapped C++ cellular automata engine for texture generation. `CellularSims.py` connected it to Sims textures — procedurally generated rug patterns, skin textures, etc. The concept: instead of painting pixels, describe rules and let automata generate the texture.

### Other SimsKit Tools

| Tool | What |
|------|------|
| **SimShow** | Object preview display (MFC dialog) |
| **SimComic** | Comic/storyboard viewer for Sims animations |
| **SimPlay** | Content playback application |
| **Simplifier** | Game configuration tools (maze, band variants) |
| **PlugInSims** | ActiveX control for embedding Sims rendering in web pages |
| **PostcardData** | Sample data + HTML pages for web-embedded Sims content |
| **maxscript** | 3ds Max export pipeline (2,365-line MaxScript + C++ plugin) |
| **vitaboy** | Character skeleton/animation system (C++ library, later ported to Unity/C#) |
| **Pone** | Minimal C++ utility library |

### The maxscript Pipeline

The 3ds Max integration (`maxis-maxscript.ms`, 2,365 lines) used an Access database to batch-export character animations to CMX format. Features: bone name mapping for motion capture data, pose validation, SourceSafe integration, chunked batch processing. This is the pipeline that produced all the character animations in the shipped game.

## See Also

- [IFF-OBJECT Schema](../../exchange/templates/IFF-OBJECT-SCHEMA.yml)
- [obliterator.py CLI](../../../../SimObliterator_Suite/obliterator.py) — `tmog export` / `tmog import`
- [Rug-O-Matic Documentation](../../../temp/TheSimsTransmogrifier/RugOMaticDocumentation/)
- [Transmogrifier Documentation](../../../temp/TheSimsTransmogrifier/TransmogrifierDocumentation/)
- [SimObliterator Suite](../../../../SimObliterator_Suite/) — the modern parsing engine
