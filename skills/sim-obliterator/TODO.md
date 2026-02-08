# SimObliterator TODO

## Done

- PersonData indices fixed (was using FreeSO VM layout, now verified against original headers + TSO fork)
- obliterator.py CLI: 18 commands (iff-info, iff-chunks, iff-strings, iff-objects, iff-bhav, far-list, far-extract, inspect, families, character, traits, skills, set-trait, set-skill, set-money, dump-raw, uplift, homecoming, sync)
- 5 output formats (table, json, yaml, csv, raw)
- SIMS-UPLIFT.yml interchange format defined (schema + 4 templates: adult, child, cat, dog)
- SIMS-ALBUM.yml i18n album format defined (schema + Newbie and Goth examples with FR/DE/NL/JA translations)
- Skin/mesh directory templates with INDEX.yml catalogs and naming conventions
- Sidecar .yml examples for Bob Newbie's body and head textures
- PersonData verification tests (38 passing)
- Lazy-loaded bhav_editor (tkinter no longer blocks headless use)
- Removed tkinter shim hack from moollm setup.py
- SIM-OBLITERATOR-API.md reference (384 lines)
- BRIDGE.md/yml corrected with verified indices
- sync command: event generator for LLM-driven CHARACTER.yml merges
- Ghost Neighbour return bug fixed in nbrs.py
- Bare except fixed in fami.py

## Content Needed

### Pet Meshes and Skins (Unleashed Expansion)
- [ ] Obtain cat body mesh (.skn or .bmf) from Unleashed expansion data
- [ ] Obtain cat head mesh
- [ ] Obtain cat skeleton (.bcf) and verify bone names
- [ ] Obtain dog body mesh (check if breed-specific variants exist)
- [ ] Obtain dog head mesh
- [ ] Obtain dog skeleton (.bcf) — likely has JAW and EAR bones
- [ ] Obtain cat skin textures (.bmp) — coat patterns: tabby, black, white, calico, siamese, tuxedo
- [ ] Obtain dog skin textures (.bmp) — breed coats: golden retriever, dalmatian, labrador, etc.
- [ ] Verify pet naming convention against actual Unleashed files (pct/pdg prefixes are speculative)
- [ ] Document pet PersonData layout (traits are repurposed for animal personality)

Where to look:
- Sims 1 Unleashed install directory (ExpansionPack6/)
- FreeSO extracted assets (freeso.org)
- modthesims.info archives
- simfileshare.net
- Search: "sims 1 unleashed pet mesh extract skn cmx bcf"

### Bob Newbie Skin Import
- [ ] Extract Bob's actual body texture from Newbie_1.FAM or default game data
- [ ] Extract Bob's actual head/face texture
- [ ] Identify which face name Bob uses (probably one of the default MA faces)
- [ ] Export as PNG via SimObliterator sprite pipeline
- [ ] Create upscaled version via image generation (128x128 -> 512x512 or higher)
- [ ] Write sidecar .yml with visual_description for image generation prompts

### Standard Character Skin Examples
- [ ] Betty Newbie (FA Fit, default female face)
- [ ] Mortimer Goth (MA Fit, specific face — identify which)
- [ ] Bella Goth (FA Fit, specific face)
- [ ] Cassandra Goth (FC Chd, child face)
- [ ] At least one fat and one skinny body variant with sidecars

### Career Outfit Textures
- [ ] Document career-specific outfit naming (each career has uniform textures)
- [ ] Extract examples for Science, Culinary, Military careers
- [ ] Map career level to outfit variant (higher level = fancier uniform)

## SimObliterator Improvements

### save_manager.py
- [ ] Add `add_neighbor()` method — create new NBRS entry with GUID allocation
- [ ] Add `add_family()` method — create new FAMI chunk, assign house, link members
- [ ] Add `remove_neighbor()` method
- [ ] Verify person_data length before index access (currently assumes 88 elements)
- [ ] Replace duplicate IoBuffer class with shared utils.binary.IoBuffer
- [ ] Replace print() error reporting with proper logging module
- [ ] Add bounds validation for FAMI member count before allocation loop

### homecoming command
- [ ] Support creating NEW Sims (not just updating existing ones) — needs add_neighbor()
- [ ] Support creating new families — needs add_family()
- [ ] Support relationship writes in homecoming (currently traits/skills/career only)
- [ ] Assign skin/appearance during homecoming (pick body mesh + head mesh + skin tone)

### obliterator.py CLI
- [ ] Add `iff-sprites` command — list and export SPR2 sprite frames as PNG
- [ ] Add `iff-meshes` command — list and export meshes as OBJ or glTF
- [ ] Add `iff-careers` command — list career tracks from Careers.iff
- [ ] Add `batch-uplift` command — uplift all Sims in a neighborhood at once
- [ ] Add `batch-homecoming` command — write back a whole family
- [ ] Add `album-import` command — scrape archive.org family album HTML to SIMS-ALBUM.yml
- [ ] Add `translate` command — auto-internationalize STR# strings via LLM

### Tests
- [ ] Add test: read a known save file, verify specific Sim has expected trait values
- [ ] Add test: round-trip uplift then homecoming, verify binary matches
- [ ] Add test: malformed FAMI chunk with huge member count
- [ ] Add test: NBRS entry with short person_data (fewer than 80 elements)
- [ ] Add test: empty neighborhood (0 families, 0 neighbors)
- [ ] Add test: verify all career track IDs map to valid names
- [ ] Add test: verify zodiac computation from trait values matches expected signs
- [ ] Add PersonData tests to the main test runner (currently standalone)

## MOOLLM Integration

### Simopolis World
- [ ] Wire sync command into adventure engine (auto-sync on room entry)
- [ ] Add ROOM.yml files to neighborhoods so they're walkable
- [ ] Add portal ROOM.yml for the bridge to adventure-4
- [ ] Implement visitor-protocol.yml in the adventure engine

### Character Pipeline
- [ ] LLM prompt template for uplift: SIMS-UPLIFT.yml -> CHARACTER.yml
- [ ] LLM prompt template for homecoming: CHARACTER.yml -> SIMS-UPLIFT.yml
- [ ] LLM prompt template for mind_mirror synthesis from trait values
- [ ] LLM prompt template for relationship narrative from daily/lifetime scores
- [ ] LLM prompt template for soul_philosophy generation from personality + career

### Family Album Pipeline
- [ ] LLM prompt template for album page captioning from save events
- [ ] LLM prompt template for album translation to all 20 Sims languages
- [ ] SIMS-ALBUM.yml -> SLIDESHOW.yml converter
- [ ] archive.org scraper for historical family albums
- [ ] Computer vision analysis of album screenshots (identify characters, rooms, objects)

### Skin Generation Pipeline
- [ ] Image generation prompt template from visual_description + personality
- [ ] 128x128 -> 512x512 upscaling workflow for original textures
- [ ] Palette quantization back to indexed 256 colors for game compatibility
- [ ] Write generated textures back to IFF via SimObliterator sprite pipeline
- [ ] Support custom face creation from CHARACTER.yml physical_description

## IFF-OBJECT.yml Pipeline (Transmogrifier Replacement)

### obliterator.py commands needed
- [ ] `iff-export` command — export .iff to IFF-OBJECT.yml (all chunks)
- [ ] `iff-import` command — import IFF-OBJECT.yml back to .iff binary
- [ ] `iff-diff` command — compare two IFF-OBJECT.yml files, show changes
- [ ] `iff-validate` command — check IFF-OBJECT.yml against schema, report errors

### BHAV assembler/disassembler
- [ ] BHAV disassembly to YAML (instruction list with symbolic opcodes and labels)
- [ ] BHAV assembly from YAML back to bytecode (resolve labels to indices, opcodes to numbers)
- [ ] Symbol table: map numeric BHAV/STR/SLOT/TTAB IDs to human-readable names
- [ ] Operand decoder: raw 8-byte operands -> structured fields per opcode type
- [ ] Operand encoder: structured fields -> raw 8-byte operands
- [ ] Variable scope resolver: { scope: local, index: 0 } -> raw byte encoding

### String table i18n
- [ ] STR# export to IFF-OBJECT.yml with all 20 language slots
- [ ] STR# import from IFF-OBJECT.yml (fill language slots from YAML)
- [ ] LLM translation prompt: given en_us text + game context, translate to target languages
- [ ] Batch translate: fill all missing language slots in one pass

### Sprite PNG pipeline (image import/export)
- [ ] SPR2 export to PNG: decode RLE, apply PALT palette, write full-color PNG
- [ ] SPR2 alpha export: embed in PNG transparency or write separate .alpha.png
- [ ] SPR2 z-buffer export: write grayscale .zbuf.png
- [ ] PNG import: read any-depth PNG, extract alpha if present
- [ ] Palette quantization: 24-bit -> 8-bit indexed (shared/custom/inherited palette)
- [ ] Floyd-Steinberg dithering for smooth quantization
- [ ] Ordered dithering option for retro/pixel look
- [ ] Auto z-buffer: generate flat "cardboard cutout" when no .zbuf.png exists
- [ ] Auto alpha: silhouette from PNG transparency when no separate alpha
- [ ] RLE encoding: compress quantized pixels back to SPR2 format
- [ ] PALT management: read/write/generate/share palette chunks
- [ ] Round-trip test: export SPR2 -> PNG -> reimport -> compare binary

### Object creation workflow
- [ ] Template library: blank object, chair, table, lamp, food, electronic, plumbing
- [ ] LLM prompt: "describe an object" -> generate IFF-OBJECT.yml from description
- [ ] Sprite generation: visual_description -> image -> palette quantize -> SPR2
- [ ] Full pipeline test: description -> IFF-OBJECT.yml -> .iff -> loads in game

## The -O-Matic Tools (from Autofac.txt)

Don Hopkins planned these template-based object creation tools. Each clones a
template object, injects user content, and imports back. Only Rug-O-Matic was
completed. With obliterator.py + AI, we can build them all as YAML templates:

- [ ] Rug-O-Matic — image on a rug (1x1, 1x2, 2x3, 3x3, animated) [original exists]
- [ ] Art-O-Matic — image as a painting or tapestry (single or animated)
- [ ] Sign-O-Matic — image or text on a sign
- [ ] TV-O-Matic — pictures inside a TV set
- [ ] Table-O-Matic — image on a table surface
- [ ] Counter-O-Matic — image on a counter surface
- [ ] Door-O-Matic — sign on a door
- [ ] Column-O-Matic — image wrapped around a column
- [ ] Dance-O-Matic — image on a dance floor
- [ ] PetBed-O-Matic — pet's name on a bed
- [ ] BackDrop-O-Matic — pictures on a stage backdrop
- [ ] Car-O-Matic — decal on a car
- [ ] Jukebox-O-Matic — MP4/audio files in a jukebox or stereo
- [ ] Book-O-Matic — slideshow in a coffee table book (dialog view)
- [ ] TV-O-Matic (slideshow variant) — slideshow on a TV with world + dialog views

- [ ] Statue-O-Matic — pose a Sim's actual body, render, apply material texture

Each needs: IFF-OBJECT.yml template, sprite frame layout spec, image transform
(perspective for isometric view), and an `obliterator tmog` workflow.

### Statue-O-Matic

Freeze a Sim in any pose and turn them into a statue object:

1. Pick a character (from SIMS-UPLIFT.yml or VitaBoy skeleton)
2. Pick a pose (any animation frame — electrocuted is classic)
3. Render the posed body with VitaBoy (4 rotations x 3 zooms)
4. Apply material texture via UV map:
   - White marble (veined Carrara)
   - Black marble
   - Green marble
   - Bronze patina
   - Colored concrete (terracotta, grey, red)
   - Natural color (original skin, frozen in time)
   - Ghost (translucent blue-white)
   - Monochrome (greyscale version of original)
   - Gold leaf
   - Ice (translucent blue with frost)
5. Output: static object with the posed sprite + material applied
6. Optional pedestal (separate tile, multi-tile for large statues)
7. Catalog description auto-generated: "Memorial statue of Bob Newbie,
   frozen at the moment of electrocution. Carrara marble."

Rocky Horror style: guests at a party are secretly turned to stone.
Memorial gardens with statues of departed Sims in their final moments.
Achievement trophies: statue of your Sim at career level 10.
Family portraits rendered as classical busts.

Material rendering uses SPR2's per-pixel alpha channel:
- Ice: alpha 60-80%, bluish frost tint, Sim's body visible through the ice.
  The game engine composites translucency correctly — z-buffer handles
  depth sorting at edges, alpha blends the frozen body through.
  SPR2 was designed with per-pixel alpha for exactly this kind of effect.
- Ghost: similar translucency, white-blue tint, no frost texture
- Glass/crystal: higher alpha, prismatic color shift
- Hologram: scanline effect (alternating alpha rows), green tint

### Slideshow Objects (Book, TV, Screen)

Three tiers of slideshow objects, from simple to rich:

**Tier 1: Book / Coffee Table Book** [SimProv TEMPLATE EXISTS]
- World view: static cover image, no animation
- Pie menu: "View" opens dialog with close-up of current slide + caption text
- Dialog: image + text + Next/Prev/Close buttons
- ALREADY DONE for SimProv — have a working template, just needs content injection
- See also: DumbOld Voting Machine (interactive agitprop with picture+text popup
  dialogs including paging — proves the multi-page dialog pattern works for
  complex interactive content, not just passive slideshows)
- Generalizes to: choose-your-own-adventure books and dialog selection games.
  Each page has an image + text + choice buttons instead of Next/Prev.
  Choices branch to different pages (BHAV jumps to different frame indices).
  Same popup dialog infrastructure, just branching instead of linear paging.
  MOOLLM adventure rooms compile to in-game interactive books this way.
- Content: STR# for captions/choices, SPR2 frames for slides

**Tier 2: TV / Screen (single tile)**
- World view: slideshow plays on the TV sprite (cycles through frames)
- Pie menu: View (dialog), Next, Prev, Pause, Speed submenu (slow/normal/fast)
- Dialog: close-up of current slide + caption text not visible in world view
- World rendering trick: render text captions as extra image frames inserted
  between content frames. TV BHAV just cycles frames — it doesn't know if a
  frame is an image or text. Like silent movie intertitles. Drama!
- Speed control: BHAV idle ticks between frame advances (slow=60, normal=30, fast=10)
- Rewind: set frame counter back to 0

**Tier 3: Multi-tile Screen / Projection**
- Same as Tier 2 but multi-tile (2x1 widescreen, or even bigger)
- Each tile shows a portion of the current frame
- Master tile runs the slideshow BHAV, slave tiles mirror the frame index
- Big enough to render text below the image in world view

### Slideshow Content Pipeline

- Input: a directory of images + optional captions (from SLIDESHOW.yml or SIMS-ALBUM.yml)
- Processing:
  1. Resize images to sprite frame dimensions
  2. For TV/screen: render caption text as extra interstitial frames (silent movie style)
  3. Quantize all frames to shared 8-bit palette (consistent colors across slides)
  4. Generate SPR2 frames for each slide (4 rotations for world view, 1 for dialog)
  5. Generate STR# entries for captions (all 20 languages)
  6. Generate BHAV: frame cycling with speed control, pause/resume, dialog popup
  7. Generate TTAB: pie menu entries (View, Next, Prev, Pause, Speed>Slow/Normal/Fast, Rewind)
  8. Package as IFF-OBJECT.yml, import via `obliterator tmog import`

### UV Map Template Engine [PROTOTYPED]

Don prototyped this: render a 3D object in Blender with a UV-mapped template
texture, export the rendered U,V coordinate maps as image layers. Then a simple
2D Python script samples pixels from the source image at the U,V coordinates
to produce the final isometric sprite. No 3D graphics needed at runtime.

The pipeline:
  1. In Blender: model the object (rug, table, TV, column, whatever)
  2. Apply a "UV ID" material — each pixel encodes which source pixel to sample
  3. Render 4 rotations x 3 zoom levels = 12 UV map images
  4. Optional: render pixel area coverage maps (du/dx, dv/dx, du/dy, dv/dy)
     These tell the sampler how big an area in the source image each output
     pixel covers — the UV footprint. Enables proper filtered downsampling:
     a pixel on a receding floor covers a large source area (needs averaging),
     a pixel on a close-up vertical surface covers a small area (sharp sample).
     Anisotropic: the footprint can be elongated in one direction (perspective
     foreshortening), not just a square neighborhood. Render as extra channels.
  5. At content time: for each output pixel, read (u,v) from the map,
     read area coverage if available, sample/filter the user's image accordingly
     (point sample for sharp, box filter for area, aniso filter for stretched)
  6. Supports multiple decals in one pass (different UV channels per decal)
  7. Result: isometric sprite with perspective-correct image wrapping and
     proper antialiasing on receding surfaces

This replaces Rug-O-Matic's hand-coded GDI perspective transforms with a
general-purpose template system. Any 3D shape becomes a template. Blender
does the hard part once; the Python engine is trivial 2D pixel sampling.
The UV maps are just PNG files stored alongside each -O-Matic template.

Same technique works in the browser with WebGL/WebGPU — render the UV map
in a shader, sample the user's image on the GPU, get the isometric sprite
as a canvas readback. Browser-based Sims content creation: drag an image
onto a 3D rug/table/TV preview, see the isometric result live, export.
Node.js server-side rendering for batch processing and CI pipelines.
VitaMoo TypeScript port (clean-room C# reimplementation exists at
moollm/temp/VitaBoyUnity — straightforward to translate to TS+WebGL)
+ UV template engine + obliterator.py WASM or REST API = full content
creation in the browser.

### VitaMoo — Character Rendering Engine

Clean-room reimplementation of the Sims character animation system.
Source: `moollm/temp/VitaBoyUnity/` (C# for Unity3D, by Don Hopkins).
Target: TypeScript + WebGL for browser-based rendering.

Renders characters from the same mesh/skin/skeleton data:
- BCF skeletons (bone hierarchies)
- BMF/SKN meshes (body parts bound to bones)
- CMX manifests (which meshes + textures = a character)
- CFP animation data (compressed keyframes)
- BMP/PNG skin textures

Used by: Statue-O-Matic (pose + render + material), browser character
preview, Simopolis web viewer, family album illustration, VitaMoo +
UV template = character-on-any-surface (t-shirts, posters, paintings).

### Jukebox / Stereo with Custom Audio

- MP4/MP3 files injected into a jukebox or stereo object
- Pie menu: Play, Stop, Next Track, Prev Track, track listing submenu
- In-game: Sims dance to the music, Fun motive boost
- STR# holds track names
- Audio data: Sims 1 uses XA audio format in FWAV chunks, may need conversion pipeline
- Simpler approach: swap the FWAV chunk references to point at custom audio files
  placed in the game's music directory

## Documentation

- [ ] BHAV reference: correct the "no inter-BHAV calls" claim (Gosub opcode 0x04 exists)
- [ ] Document the SIMS-UPLIFT.yml schema in SIM-OBLITERATOR-API.md
- [ ] Document the SIMS-ALBUM.yml schema
- [ ] Document the skin/mesh naming convention in a human-readable guide
- [ ] Write a walkthrough: "Bob Newbie's Journey" (uplift -> MOOLLM -> homecoming)
- [ ] Update BATTLE-PLAN.md with current status and revised timeline
