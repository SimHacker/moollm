# Remote CLI, Local GUI

**Class:** method · **Attribution:** Thomas Ptacek,
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/)
(2026); Emacs TRAMP as the existence proof

> **You don't need a user interface on prod. You need a command line on prod
> that a user interface on your laptop can drive.**

The SSH argument is the one Ptacek grants as strong — and then reroutes.
If you need a UI on a remote box, the 1970s answer was a TUI in the SSH
session. The better split: keep a CLI (scriptable, pipeable, surviving
disconnects inside tmux) on the machine that has the data, and put the
human interface on the machine that has the screen, the accessibility
tree, and the pointing device. Emacs TRAMP is the existence proof: hide
the SSH, present a native editor, keep LSP and Magit. bpftrace users
already know this by the third time they've built a bar chart out of
hash marks.

HN's useful remainder: the *session* is what people actually want —
detach, reattach from a phone, survive a 30-second ping on a cell hotspot
(mosh). That is a property of a persistent remote process, not of
character cells. A local GUI driving a remote CLI (or a web view on the
same contract) can keep the session without making the human live inside
a VT100.

The method:

1. **Identify the remote primitive** — the thing that must run near the
   data (htop's numbers, Claude's working tree, the mail store).
2. **Expose it as a CLI** — flags, stdout, exit codes; no screen.
3. **Drive it from a local UI** — native, web, or editor; the UI owns
   presentation.
4. **Keep a detachable session for the process**, not for the pixels.

**Go deeper:**
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) —
the SSH section ·
[Emacs TRAMP](https://www.gnu.org/software/emacs/manual/html_node/tramp/) ·
[mosh](https://mosh.org/) — the session people actually meant

**Sources:** seed batch
[../seeds/2026-08-22-stop-making-tuis.md](../seeds/2026-08-22-stop-making-tuis.md)

**See:** [cli-not-tui](../lenses/cli-not-tui.md) ·
[summon-native](summon-native.md) ·
[../lenses/keyboard-is-not-tui.md](../lenses/keyboard-is-not-tui.md)
