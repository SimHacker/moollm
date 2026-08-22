# Summon Native

**Class:** method · **Attribution:** Thomas Ptacek,
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/)
(2026)

> **For a personal tool, default to a native UI and let the agent write it.
> Sameyness is a feature — native apps are supposed to look like other native
> apps.**

Ptacek's 2026 claim, after a year of summoned SwiftUI: agents dissolved the
old split (frontend / backend, web / native). Building good UI by hand is
still tedious, exacting, and gated by platform knowledge. Generating a
reasonable native interface — SwiftUI on Mac, and he assumes GTK 4 / WinUI 3
comparably — is now cheap enough that "I don't do UI" is a habit, not a
constraint. His process: copy a template directory, never open Xcode, enable
computer-use so the agent can see and drive the app, come back from lunch to
something debuggable.

The method is for *personal* artifacts — he has no intention to distribute
most of them. Vibe-coding and vibe-*shipping* stay different; someone will
soon ship an app they have never looked at, and it won't be him. The HN
thread's best pushback is maintenance: a box of summoned tools rots as
APIs, auth, and reverse-engineered schemas move, and a screenshot-as-spec
is not a tested artifact. Summon native; keep the receipt (prompt, tests,
the running app) so the next agent can repair it.

Practical notes from the founding use:

- **CLI first if the job is composition** — this method does not cancel
  [cli-not-tui](../lenses/cli-not-tui.md); it cancels *drawing windows out
  of ASCII* when you wanted a GUI.
- **Computer-use in the loop** — an agent that cannot see the app will
  generate a plausible corpse.
- **Skills, not vibes alone** — he loaded a macOS design skill, a
  typography skill, Paul Hudson's SwiftUI skill, Airbnb's Swift skill;
  idiomatic output still wants a house style.

**Go deeper:**
[Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) ·
[HN: 49384210](https://news.ycombinator.com/item?id=49384210)

**Sources:** seed batch
[../seeds/2026-08-22-stop-making-tuis.md](../seeds/2026-08-22-stop-making-tuis.md)

**See:** [cli-not-tui](../lenses/cli-not-tui.md) ·
[remote-cli-local-gui](remote-cli-local-gui.md) ·
[../lenses/direct-manipulation.md](../lenses/direct-manipulation.md)
