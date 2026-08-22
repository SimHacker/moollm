# CLI Not TUI

**Class:** lens · **Attribution:** Thomas Ptacek, [Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) (2026); Don Hopkins, [HN comment](https://news.ycombinator.com/item?id=49384210)

> **A command line is a programmer's interface. A TUI is a GUI trapped in a
> 1970s character cell. Don't confuse them.**

Ptacek's useful cut: CLIs and TUIs are both 1970s products shrink-wrapped
around teletypes, but only TUIs inherit the hostility as an *intrinsic*
property. A CLI is a composable program — stdin, stdout, flags, pipes, scripts.
A TUI is a graphical application that renders into a VT100 emulator: you are
fighting the terminal to approach, asymptotically, what every native toolkit
does out of the box (scroll targets, drag-and-drop, text selection, floating
windows, images, an accessibility tree).

The HN thread spent three hundred comments defending TUIs with properties
that belong to CLIs (composability, SSH, scriptability) or to *keyboard-first
design* ([keyboard-is-not-tui](keyboard-is-not-tui.md)). Those are real goods.
They are not reasons to put a character-cell renderer between a human and an
LLM.

Don's line, same thread: in the age of direct manipulation, info visualization,
WebGPU, and frontier AI, a VT100 escape-code interpreter between you and your
model is ridiculous. Like Brooke Shields, he'd rather nothing come between him
and his LLMs.

The lens in practice: when someone proposes a TUI, ask whether they wanted a
CLI (then write the CLI) or a dense, keyboard-driven GUI (then write that —
native, web, or Dear ImGui — and keep the density). A TUI is the leftover when
you wanted both and accepted neither.

**Go deeper:**
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) ·
[HN: 49384210](https://news.ycombinator.com/item?id=49384210) ·
Stephenson, *In the Beginning Was the Command Line* (1999) — the sacred text
Ptacek says set HCI back twenty years ·
[Wikipedia: Text-based user interface](https://en.wikipedia.org/wiki/Text-based_user_interface)

**Sources:** seed batch
[../seeds/2026-08-22-stop-making-tuis.md](../seeds/2026-08-22-stop-making-tuis.md)

**See:** [direct-manipulation](direct-manipulation.md) ·
[keyboard-is-not-tui](keyboard-is-not-tui.md) ·
[../methods/summon-native.md](../methods/summon-native.md) ·
[../methods/remote-cli-local-gui.md](../methods/remote-cli-local-gui.md) ·
[../masters/ben-shneiderman.md](../masters/ben-shneiderman.md) ·
[../masters/don-hopkins.md](../masters/don-hopkins.md)
