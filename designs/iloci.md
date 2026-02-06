# iLoci — The Memory Palace That Became MOOLLM

> "Each of these is like a room and you can walk around them." — Don Hopkins, Mobile Dev Camp Amsterdam

## The Idea

The ancient Greeks memorized by building imaginary palaces — rooms connected together, each containing something memorable. Walk through the palace, look at each room, and you remember. The Method of Loci.

iLoci turned that into software. An iPhone app where you construct a network of nodes (loci), each with an image, title, description, and URL. Connect them by kissing them together. Walk through them. Put things inside them. Upload to a server that publishes them as a browsable website.

The same pattern repeated three times across 30 years of Don Hopkins's work:

## The Pattern: Rooms → Things → Publishing

### DreamScape (1995)

Built at Kaleida Labs (Apple + IBM joint venture) in ScriptX, a multimedia scripting language. An adventure map editor where rooms connected by bumping them together. Conceived as a web publishing tool: create rich interactive content, preview it as HTML anyone can browse, download the source to play with and edit. Kaleida got steamrolled by Java.

### The Sims (2000)

Working on The Sims at Maxis, the same publishing pattern emerged: you play the game, take pictures, write stories. Save your game and it publishes web pages — your house, your story, browsable by anyone. People go online, read stories, look at houses, download save files to play in their own game. Rich interactive state → published HTML → downloadable source.

### iLoci (2009)

iPhone app + Python/TurboGears server. The Method of Loci as a mobile app:
- Each locus: image, title, description, URL
- Network of loci connected by touch gestures (kiss to connect, kiss again to disconnect)
- Built-in web browser for drill-down
- Edit mode via multi-touch toggle
- Construction tools: search Amazon, import books with images
- `iloki://` URL scheme — web pages talk to the app as if it were another server
- Upload: ZIP file → server → SQL database → browsable website
- Content-agnostic: each locus is a JSON dictionary. Any structure works.

The key architectural insight from the Mobile Dev Camp talk:

> "Really what this is — the web page thinks that the iPhone app is another web server, and it uses `iloki:` colon instead of `http:` — and what I have is a set of services that return JSON."

The app and the server are peers. Both speak URLs. Both return JSON. The web page in the built-in browser can talk to either one. This is the prototype for MOOLLM's `postal` skill (universal addressing to files, YAML keys, line numbers, functions).

## How iLoci Became MOOLLM

Every core MOOLLM pattern has an iLoci ancestor:

| iLoci | MOOLLM | The Connection |
|-------|--------|---------------|
| Locus with image, title, description, URL | Room with README.md, ROOM.yml, files | A place with content and links |
| Network of loci connected by touch | Directories connected by exits | Navigation through connected spaces |
| Things in rooms (buttons, images, text overlaid on photos) | Objects in rooms (interactable atoms with state) | Stuff you find when you explore |
| Kiss to connect / disconnect | Exit links with guards and locks | How rooms link together |
| Edit mode toggle | PSIBER protocol (step inside, edit while inside) | Switching between explore and modify |
| Built-in web browser | Adventure browser runtime | Rendering the exploration UI |
| `iloki://` URL scheme (app as server) | `moollm://` URLs in PSIBER, postal addressing | Universal addressing across boundaries |
| ZIP upload → server → SQL → website | `compile.py` → `world.json` → browser runtime | Compile structured content for publication |
| Amazon book import (search → create locus) | World generation (ask about a place → it exists) | Construction by discovery |
| Save file as website (The Sims pattern) | Adventure `dist/` as playable website | Rich state → published HTML |

## What iLoci Wanted But Couldn't Do

From the talk: "I want to be able to import 10 things at a time and link them up 1 2 3 4 5 6 7 8 9 10, and then you go down into them."

This is exactly what the adventure compiler does. Give it a directory of files and it links them into a navigable world. The construction tools iLoci planned but never built — import from Flickr, YouTube, Google, RSS, Facebook — are now LLM-orchestrated via MOOLLM skills.

The other thing iLoci wanted: "The method of Loci has another thing — when you're in a room there can be THINGS in the room. Like HyperCard — flip into edit mode, new button stick here, new text field stick there. Take a picture of somebody, say new Facebook friend, put it over their face."

This is PSIBER. Step inside a room. See the objects. Add new ones. Link them to the web. The interaction model Don described in 2009 — overlaying interactive objects on images — is the adventure engine's object-in-room model.

## What MOOLLM Adds That iLoci Couldn't

1. **LLM as the content engine.** iLoci needed manual construction or API imports. MOOLLM generates rooms, objects, descriptions, and connections from natural language. "Ask about a place and it exists."

2. **Characters in rooms.** iLoci had things in rooms but not people. MOOLLM has characters with needs, moods, relationships, and dialogue — The Sims inside the Memory Palace.

3. **Ethics of simulation.** iLoci could link to anyone's Facebook page. MOOLLM has representation-ethics, patron saint protocol, ontology tags. Real people are referenced, not impersonated.

4. **Structural import into rooms.** PDFs as navigable rooms (each page is a room). Codebases as navigable rooms (PSIBER into source files). Any structured data as navigable space. iLoci's vision of "a receptacle for a map with little things in the rooms that have data" — realized at the filesystem level.

5. **Characters as stylesheets.** The lloooomm prototype (predecessor to MOOLLM) explored characters as CSS stylesheets — design philosophies that generate visual output, mixable and modulatable. Each patron saint contributes a style. Mount multiple styles and they blend. This works for image generation prompts AND web page HTML+CSS+SVG generation.

## The Thread

DreamScape (1995) → iLoci (2009) → lloooomm (2024) → MOOLLM (2025-2026)

The same idea, refined across four implementations:
- Rooms connected together
- Things inside rooms
- Navigate by walking
- Edit by touching
- Publish by uploading
- Rich state → browsable HTML → downloadable source

The Method of Loci. The filesystem is the palace. The directories are the rooms. The files are the things you find inside. Navigation is exploration. Editing is construction. Publishing is sharing.

## iLoci as Future UI

iLoci is one possible user interface to the data in MOOLLM — the guiding light for the adventure engine. The adventure engine's compiler and runtime exist (compile.py, engine.js, browser dist/), but the visual interface is as of yet unimplemented. When it arrives, it will be driven by the same interaction principles iLoci pioneered:

- **Direct manipulation** — grab rooms, drag them, connect them by proximity
- **Drag and drop** — move objects between rooms, import content from outside
- **Zooming** — zoom out to see the map, zoom in to see a room's contents
- **Pie menus** — context-sensitive radial menus for actions on rooms, objects, exits (The Sims heritage)

The text adventure interface (command line, parser) is one mode. The iLoci-style visual interface is another. The underlying data model (rooms, objects, exits, characters, advertisements) is the same. The UI is a skin, not the skeleton.

---

*Video: [iPhone app iLoci by Don Hopkins @ Mobile Dev Camp](https://www.youtube.com/watch?v=_hQzN7GVKTA)*
*See also: [micropolis artifacts/connections.yml](../skills/micropolis/artifacts/connections.yml) — DreamScape lineage*
