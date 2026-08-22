# Seed batch: Stop Making TUIs (2026-08-22)

Source: Thomas Ptacek, [Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/)
(Quarrelsome, 20 August 2026) and the HN thread
[item?id=49384210](https://news.ycombinator.com/item?id=49384210)
(Don's comment in-thread).

## Planted ✅

- cli-not-tui → [lenses/cli-not-tui.md](../lenses/cli-not-tui.md)
- keyboard-is-not-tui → [lenses/keyboard-is-not-tui.md](../lenses/keyboard-is-not-tui.md)
- summon-native → [methods/summon-native.md](../methods/summon-native.md)
- remote-cli-local-gui → [methods/remote-cli-local-gui.md](../methods/remote-cli-local-gui.md)

## Todo 🌱

(empty)

## Seed notes (grounding, kept for provenance)

- **cli-not-tui** (lens) — Ptacek: CLIs are almost always a good idea; TUIs
  almost never. A TUI is a GUI fighting a teletype. Don: a VT100 interpreter
  between you and an LLM is ridiculous; nothing comes between him and his
  LLMs.
- **keyboard-is-not-tui** (lens) — HN's correction: the defended goods are
  keyboard-first, density, SSH/tmux sessions. Papa John's TUI beat later
  restaurant GUIs on key speed, not on character cells. Those goods can live
  on a GUI if anyone will design one.
- **summon-native** (method) — agents made native UI cheap for personal
  tools; sameyness is good; computer-use in the loop; vibe-code ≠ vibe-ship.
- **remote-cli-local-gui** (method) — you need a CLI on prod that a local UI
  can drive (TRAMP). The session people want is detach/reattach, not a TUI.
