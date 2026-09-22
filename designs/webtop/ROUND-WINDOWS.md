# Round windows: shape is part of the frame contract

**A window's shape belongs to the frame, and the rectangle is a default, not a law.**
[FRAMES.md](FRAMES.md) made window management one pluggable concern among many; this note makes
the frame's *geometry* part of what that concern contributes. The motivating case is concrete:
the [cabinet's](https://github.com/SimHacker/WillWrightShowForFood/tree/main/packages/cabinet)
Type 340 display is a round tube with the square 1024×1024 raster inscribed in the glass. A
round window for it is not decoration — it is the fact of the instrument.

## Bauhaus, not skeuomorphism

The styling rule is Bauhaus black and white: black field, white hairline ring, white strokes.
No bezel imagery, no glass glint, no phosphor tint, no cabinet wood. The circle is there
because the tube is round, the way a Bauhaus teapot is round because pouring is — form
restating the fact, not imitating the material.

Skeuomorphism is a *different artifact* that already has its design note: the
[3D portrait](https://github.com/SimHacker/WillWrightShowForFood/blob/main/packages/cabinet/PORTRAIT.md),
where the whole iron gets modeled, lamps and all. Same emulator streams, two skins at the
opposite ends of the abstraction dial. The rack proves the streams are skin-independent; the
portrait spends the same streams on presence.

## The lineage, and X11's cautionary tale

- **Round glass everywhere.** CRTs of the era were round because that is what an electron gun
  sweeps; the square plotting area was inscribed. SAGE consoles, the PDP-1's Type 30, the 340.
  Radar scopes made the circle *mean* something: bearing is angle. The instrument tradition of
  round displays is older than the rectangular-terminal tradition.
- **NeWS: shape was free.** A canvas's shape was any PostScript path. Round windows,
  pie-slice windows, windows shaped like the tool they held — one `shape` away, and the input
  model followed the path, so hit-testing was correct without ceremony.
- **X11's SHAPE extension is the cautionary tale.** Shape arrived as a bolted-on bitmap
  region, and its famous customers were `oclock` and `xeyes` — party tricks, because nothing
  else in the toolkit *understood* shape. No layout policy, no command surface, no menus knew
  the window was round. Shape without a contract is a costume.
- **The DOM hands it back.** `clip-path: circle()` clips both painting and pointer
  hit-testing in one declaration. What cost X11 an extension and NeWS a path is now one CSS
  property — the reason this note is a design decision and not an engineering project.

The lesson from the middle entry: shape earns its keep only when the frame contract knows
about it — when the chrome, the commands, and the menus are all shaped by the same geometry.

## Round frames want pie menus

That is the composition that makes the circle load-bearing rather than cute. FRAMES.md
already names pie menus as the natural merged presentation for commands contributed by many
concerns. On a round window the bezel **is** the ring: press the frame and the slices bloom
in place, concerns claiming slices and subrings around geometry that was already circular.
The frame's chrome and its command surface become the same object — the menu is the bezel,
momentarily labeled.

And in the cabinet's case the composition goes three rings deep, one per generation of
radial interface: PIXIE's lightbutton ring (1969–72, drawn by the 340 executing its own
display file) inside the round tube window, pie menus (1986→) on its frame, embedded in a
HyperTIES article (1988). Concentric lineage, one screenshot.

## The rack

The emulator embeds not as one canvas but as a **rack** of windows, one per device, each
resizable, zoomable, iconifiable — the frame manager's first multi-window customer, extending
the five-frame testbed in FRAMES.md:

| Window | Shape | Why |
|---|---|---|
| tube | round | the 340's glass; square raster inscribed |
| console lamps | wide strip | the operator panel — the face's mouth |
| teletype | paper column | white field, black ink: paper inverts the palette |
| debugger | rectangle | declared registers, single-step |
| recorder | filmstrip | captured frames, each a thumbnail of the tube |

Two verbs the frame must keep distinct, both on the ring menu:

- **Resize** changes the glass — CSS size, raster mapping untouched.
- **Zoom** changes the mapping — the 1024 grid is fixed hardware; zoom is a viewport
  transform into the plane. Fit modes: `inscribe` (whole raster visible, corners touching
  the ring) or `fill` (circle crops the corners, as the real bezel did).

**Iconify keeps drawing.** A round window shrinks to a disc that still runs — the tube
iconified is a porthole with the picture alive inside it, a live icon in the NeWS manner.
An iconified emulator is not paused; it is small.

↑ [FRAMES.md](FRAMES.md) · [webtop hub](README.md) ·
[cabinet applet](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ties/CABINET-APPLET.md)
