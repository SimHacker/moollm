# Frames: a plug-in frame manager

**A frame is a plug-in wrapper around any view that sources commands from one concern and
surfaces them on a shared command surface.** Window management is one concern — the one that
historically got there first — not the landlord. NeWS proved this in the 1980s: its window
manager was a client-side library, and a frame was a PostScript wrapper any program could
subclass. What this note generalizes: *every* cross-cutting concern gets the same privilege.
Wrap any view, contribute chrome and commands, compose with whatever is already wrapped.

The webtop is the customer, but so is everything else in this repository that shows a view:
the [cabinet PDP-7 emulator](https://github.com/SimHacker/WillWrightShowForFood/tree/main/packages/cabinet)
is the first testbed (below), and rooms, tours, and reading rigs all wrap views in concerns.

## The contract

Three parties, one seam:

```yaml
view:                 # anything that renders and can be operated
  element:            # where it draws
  commands:           # what it can do, by name — the operable surface
  state:              # what it exposes for inspection / serialization
  events:             # what it announces
  # This is the accessibility tree, treated as a first-class API.
  # A view that a screen reader can drive is a view a frame can drive.

frame:                # an adapter from one concern onto a view's surface
  concern:            # provenance | wm | automation | debug | script | …
  chrome:             # border, bezel, overlay, badge — may be none
  commands:           # contributed commands, tagged with the concern
  subscribe:          # which view events it watches
  # The view does not know it is framed.

manager:              # composition, routing, serialization
  nest:               # frames wrap frames; inner travels with outer
  merge:              # many concerns, one bezel, one command surface
  route:              # dispatch a command to the frame that contributed it
  serialize:          # the frame stack and its settings are view state
```

## Kinds of frames

| Frame | Concern | What it contributes |
|---|---|---|
| window | placement | move, resize, close, iconify — the classic NeWS wrapper |
| provenance | seams | show transclusion boundaries, sources, blame; grab a seam and follow it to the other end |
| script | behavior | property sheets, the code behind the view |
| layout | structure | rearrange, align, restyle |
| history | time | versions, diffs, undo beyond the buffer |
| automation | delegation | record/playback, loops, screen-reading button-pressing agents |
| debug | inspection | registers, single-step, breakpoints around a running machine |

The automation frame is the one that proves the contract is honest: an agent frame operates the
**same surface** the human does — it reads the view's tree and presses the view's buttons. If
the agent needs a private back door, the surface was a façade. This is EXPECT/SEND generalized
from terminals to views, and it is why the accessibility tree is the API rather than an export.

## Run-mode versus edit-mode, per view

The provenance/script/layout/history rows are all **edit mode** — and edit mode is not a global
variable. Each view flips independently, and what "edit" means is whichever editor frame you
plug in. A reader runs everything; a scholar flips one quotation into a provenance frame and
leaves the rest of the page alone.

The precedents, in order of increasing strength:

- **HyperCard `userLevel`** — browse, type, paint, author, script: a *dial* of progressively
  exposed structure. But global: one number for the whole world. That was its ceiling.
- **Emacs minor modes** — per-buffer concerns contributing merged keymaps. Proof that merging
  command surfaces from independent concerns works at scale, in daily use, for decades.
- **HyperLook's stack editor** ([the receipt](HYPERLOOK.md)) — the editor was a plug-in object
  hooking the mouse-capture and drawing protocols. Unplugging it produced the locked SimCity
  runtime. **Not a flag checked at run time: a capability physically absent.** A locked-down
  build could not be tricked into edit mode, because the editing machinery was not there.
  Don has screenshots of SimCity after user-interface vandalism — the same build with the
  editor left plugged in. Same artifact, editor plugged versus unplugged; the pair is the
  whole argument in two images.
- **Browser DevTools** — an edit-mode frame around any page, which is why the web feels
  learnable at all. But it is the vendor's frame: not pluggable, not per-view, not shippable
  as part of a document. The frame manager is DevTools democratized.

## Nesting and merging

**Nesting is composition.** An automation frame inside a window frame: the agent gets dragged
around with its subject. Inner frames see the view; outer frames see a framed view; nobody
needs to know the depth.

**Merging is the hard, interesting one.** Multiple concerns sharing one bezel and one command
surface, without stacking three borders and four toolbars. That is a command-routing problem:
each frame contributes commands tagged by concern, and the manager merges them into whatever
presentation the user prefers. **Pie menus are the natural merged presentation** — concerns
claim slices or subrings without fighting over linear real estate, and the ring structure
survives merging in a way toolbars do not.

And the pie menu editor edits itself with itself, HyperLook's punchline: once commands are
data — slices tagged by concern, contributed by frames — the editor of the command surface is
just one more frame. Menu customization stops being a preferences dialog and becomes ordinary
editing.

## The frame stack is view state

Serialize the frame stack — which frames wrap which views, with what settings — and it travels
with the [view record](../pie-stack-views/README.md). A citation link and a reading link become
the same mechanism with different frame stacks: seams on for the scholar, run mode for the
reader, the debugger arrangement for the colleague picking up your session. Your carved pie
menus ride along, because they are data the frames contributed and you rearranged. The
ancestors of this move — viewspecs, `expansionState`, trails — are collected in
[VIEW-STATE-ANCESTORS.md](../pie-stack-views/VIEW-STATE-ANCESTORS.md).

## First testbed: the cabinet

The [PDP-7 emulator](https://github.com/SimHacker/WillWrightShowForFood/tree/main/packages/cabinet)
web bench builds this small before the webtop has to carry it large. One view — the Type 340
canvas — and five frames: bezel (wm — and a **round** one, because the 340's glass is round;
shape as part of the frame contract is [ROUND-WINDOWS.md](ROUND-WINDOWS.md), along with the
rack of device windows that grows from this testbed), debugger panel (declared registers, single-step), pen
assist (honest/teleport toggle), EXPECT/SEND automation (scripted console for acceptance
tests), and the segment recorder. Building the bench as a frame manager with five frames
instead of one hardwired page costs little and gives the contract its first falsifiable
implementation: if the automation frame can boot SYMELEC and the debugger frame can watch it
without either knowing the other exists, the seam is real.

↑ [webtop hub](README.md)
