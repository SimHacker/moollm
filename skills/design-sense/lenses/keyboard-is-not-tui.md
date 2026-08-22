# Keyboard Is Not TUI

**Class:** lens · **Attribution:** the HN thread on Ptacek's
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/)
(2026) — especially WhyNotHugo, sjbzbeiks, the Papa John's counter

> **The goods people defend when they defend TUIs are keyboard-first,
> information density, and remote reach — none of which require a character
> cell.**

The strongest TUI arguments in the thread were not about terminals. They were
about a Papa John's order-entry screen that beat every later GUI restaurant
system because it was keyboard-speed; about Magit and k9s and ncdu being
faster than their graphical cousins; about tmux + SSH + detach as a session
that VNC still cannot match. Those are real. They are also *design choices*,
not properties of ANSI escape codes.

Ptacek already said the quiet part: nothing stops you from designing a dense,
economical, keyboard-driven GUI. HN's useful correction is that almost nobody
does — modern GUI fashion optimized for touch, hamburger menus, and discoverability
for first-week users, and broke power users and accessibility stacks in the
process. The TUI renaissance is a protest against *that* status quo, wearing
a VT100 costume.

The lens in practice: when a TUI is winning, name which good it actually
won on (keys, density, SSH, single-font theming, multi-instance by default)
and ask whether a GUI could take that good without the costume. When a GUI
is losing, name which of those goods it refused. Don't let "TUI vs GUI"
launder a fight about keyboard-first professional tools versus phone-app
fashion.

**Go deeper:**
[HN: 49384210](https://news.ycombinator.com/item?id=49384210) ·
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) ·
[UI Density — Matt Ström-Awn](https://mattstromawn.com/writing/ui-density/) ·
WhyNotHugo: what you're comparing is "keyboard-driven vs mouse-driven"

**Sources:** seed batch
[../seeds/2026-08-22-stop-making-tuis.md](../seeds/2026-08-22-stop-making-tuis.md)

**See:** [cli-not-tui](cli-not-tui.md) — keep the CLI/TUI cut honest ·
[fitts](fitts.md) · [direct-manipulation](direct-manipulation.md) ·
[../methods/summon-native.md](../methods/summon-native.md)
