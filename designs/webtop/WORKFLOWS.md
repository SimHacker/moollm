# Workflows: a slice runs a list of commands

**A pie menu item is a container for ordered lists of named commands, one list per event.**
Kando 3.0 shipped this on the desktop on 2026-09-23, and the webtop should take the model
whole, because it already has the part Kando lacks: commands with names, sent to views that
answer. Kando's steps are blind (press these keys in whatever window has focus, wait 500 ms,
hope). A webtop step sends a named command to a view and waits for the event it announces.

Sources: [Kando 3.0.0 release](https://ko-fi.com/post/Kando-3-0-0-now-available-H5W727E0O3),
[the workflow design post](https://ko-fi.com/post/Workflows-coming-to-Kando-3-0-N7A421KR1B),
[the release video](https://www.youtube.com/watch?v=PhUnN2cx5sI),
[kando-menu/kando](https://github.com/kando-menu/kando). Simon Schneegans' room is in
[WillWrightShowForFood](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/simon-schneegans).

## What Kando 3.0 does

- **Two item kinds.** A *button* and a *submenu*. The old per-type items (open URL, run
  command, paste text) are gone; a button is just a list of actions.
- **Several workflows per item, keyed by event.** Buttons have *hover* and *select*.
  Submenus have *hover*, *open*, and *center-click*. Each is an ordered, drag-reorderable
  list with its own quick-select key.
- **Closing the menu is a step, not a side effect.** Actions before `close-menu` run while
  the menu is on screen; actions after it wait until the menu is fully hidden. Leave it out
  and the item can be fired repeatedly without the menu going away.
- **The center is programmable.** A submenu's center-click defaults to `close-submenu`
  on Backspace, and you can replace it or add to it, so which key goes back is a setting.
- **New actions.** `focus-window`, `delay`, `set-clipboard`, `send-websocket-message`.
  Paste-text was migrated automatically into `set-clipboard` then `simulate-shortcut`.
- **Keyboard.** Arrow keys walk the menu, Enter selects, Backspace goes back, and every
  theme can overlay the quick-select keys on the items.
- **Starting points, not blank forms.** The add-item toolbar inserts items with the usual
  workflow already filled in (an open-URL button arrives with `open-url`, `close-menu`),
  which you then edit.
- **Next, per Simon:** conditions, such as time of day or active window, so an item can
  focus an app that is already open instead of launching another one.

## Mapping it onto the webtop

The webtop's invariant ([README](README.md), [TREE-NAVIGATION](TREE-NAVIGATION.md)) is that
every operation is one named command reachable by keyboard, pie menu, and drag. A workflow
is the obvious next thing on top of that: a named sequence of named commands.

```yaml
# a slice on an article's pie menu
slice:
  label: Cite
  key: c
  hover:                         # runs while the pointer rests on the slice
    - preview: citation          # the definition-preview idea from HyperTIES
  select:
    - copy: { as: citation }
    - dismiss                    # Kando's close-menu; position sets timing
    - focus: { view: notes, open_if_missing: true }
    - paste
    - await: notes.saved         # an event, not a delay
```

What changes when steps are named commands instead of keystrokes:

| Kando step | Webtop step | Why it's better |
| --- | --- | --- |
| `simulate-shortcut Ctrl+L`, `Ctrl+V` | `focus: address`, `paste` | Works whatever the keymap is, and in a view that has no keyboard shortcuts at all |
| `delay 500` | `await: page.loaded` | Waits exactly as long as it takes, and fails loudly if the event never comes |
| `focus-window` | `focus: { view, open_if_missing }` | Kando's planned "focus if open, else open" condition is one argument |
| nothing returns | each step returns or announces an event | The next step can use the result; a failure stops the list with a message saying which step |
| future conditions | `when:` on a step or slice | [VERBS-AND-RUBRICS](VERBS-AND-RUBRICS.md) already filters advertised verbs with `when:` |

### The events

- **hover** is [RESELECTION](../pie-stack-views/RESELECTION.md)'s dwell, given a job: preview
  the target, show the definition, light the seam. It must be side-effect free, because
  people sweep through slices without meaning anything. A hover step that changes the
  document is a lint error.
- **select** is the ordinary action.
- **open** on a submenu runs when it opens: load its contents, fetch what its slices will
  need.
- **center** is the one Kando made programmable, and it's the most interesting.
  ROOM-STROLLING already gives the center two meanings, *here* and *cancel*. With
  workflows it can do a third thing and still stay where the hand rests: "do it again",
  "undo the last slice", "back".

### `dismiss` as a step

Kando's best small idea is that closing the menu is an action you place in the list. In the
webtop this matters more, because the menu is often drawn over the view the commands act
on. Steps before `dismiss` run with the menu showing, as feedback; steps after it act on an
unobstructed view, which also matters for anything that takes a screenshot or reads what
the reader can see. Without `dismiss`, the menu stays up for repeated use, like a
tear-off menu.

### Keys and overlays

Quick-select overlays answer TREE-NAVIGATION's complaint that a rich keymap is
undiscoverable by itself: the menu shows its keys at the moment you would need them. Each
workflow has its own key, so one slice can have a key for select and another for its
center. Arrow keys walk the ring in angular order, the same order as the
[margin stubs](ROOM-STROLLING.md), so keyboard, pointer, and the drawn map agree.

## What the webtop can do that Kando can't

1. **Record a workflow by doing it.** The automation frame ([FRAMES](FRAMES.md)) sees the
   same named commands the reader issues, and every verb is logged. Select a stretch of
   the log and save it as a workflow. Kando can't record, because it only ever sees
   keystrokes and has no idea what they meant. This is Allen Cypher's *Watch What I Do*
   with the hard part (recovering intent from input events) removed by construction.
2. **Workflows are data that travel.** A slice and its lists are YAML in the frame stack,
   so they serialize into the [view record](../pie-stack-views/README.md) with everything
   else. Hand someone a reading link and your Cite slice comes with it. Kando menus live in
   one machine's settings.
3. **The editor is a frame.** FRAMES says the pie menu editor edits itself with itself.
   Kando's workflow editor (pick the event, drag the steps, set the key) is the right
   design for that frame, and it is the part to copy most carefully.

## A bridge, now

Kando 3.0's `send-websocket-message` action makes the desktop and the webtop one system
today: a Kando slice on the desktop can send a named command to a webtop page, a HyperTIES
article, or a running Micropolis, and the page does it the semantic way instead of
receiving injected keypresses. The socket is the door semantic commands needed.

Plan:

- A small command endpoint on webtop pages: a WebSocket that accepts
  `{ command, args }`, dispatches it through the same router as keyboard, pie, and drag,
  and replies with the result or the error. Pages opt in; nothing listens by default.
- A generated Kando menu for a page: walk the page's advertised commands and write Kando
  menu JSON whose buttons each hold one `send-websocket-message` and a `close-menu`. Check
  the schema against Kando's settings format before writing the generator.
- First target: the [cabinet](https://github.com/SimHacker/WillWrightShowForFood/tree/main/packages/cabinet)
  applet (speed, demo, save drawing, DUEL restart), because it is small and already has
  named operations.
- Then Micropolis, whose tools and commands already have names.

↑ [webtop hub](README.md)
