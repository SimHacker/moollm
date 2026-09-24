# Screen Angel: the layer doing the clicking

*Part 4 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

[The previous part](the-errand.md) told the story: a Sim takes a job as mayor in Micropolis, and
comes home when someone picks from the pie menu of a painted Easter egg. This part is about the layer
doing the clicking. Screen Angel needs more than the one-line definition in
[Three names](the-errand.md#three-names), because the whole argument depends on what it is allowed
to be.

## What it is

It is a scriptable layer over *any* application's interface: selecting and querying components,
matching visual patterns, handling events, and driving widgets from outside without modifying the
application. Don first described it in a 2013 email to Peter Korn
([thread](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/sources/2013-email-thread.md)),
refined it across a decade of Hacker News comments
([progression](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/sources/hacker-news-progression.md)),
and named it in 2026.

The name is a ladder: **a screen scraper takes, a screen reader reads to you, a screen angel acts for
you.** It also describes the implementation literally — a transparent, always-topmost, click-through
overlay. Invisible, above you, intervening.

What it can do is bounded by one sentence: **anything a player can do, with the tools players
already use.** That is a lot:

- see the screen, move the mouse, press keys;
- navigate menus, walk the camera around a world, click a pie item;
- save and quit a game, read the save file, edit or regenerate it, and start the game again.

The last item is where Screen Angel goes past what a player does by hand. Nobody reads a save file
by eye. But players have edited Sims content with tools for twenty-five years — the Transmogrifier
for cloning and repainting objects, community editors such as FreeSO's Volcanic for SimAntics —
and Screen Angel is a bridge into that ecosystem of user-created content tools, not a replacement
for it. It reads and writes the same files those tools do, so anything it changes, a person can open
in one of them, or in a text editor once it has been converted to YAML.

Saving, editing and relaunching is the high-bandwidth channel, used between sessions because it costs
a restart. During play it uses the low-bandwidth one: pie menus, dialog trees, codes on screen, typed
parameters. Neither is a fallback for the other, and the second is why routine cross-game play does
not need a save-quit-edit-relaunch cycle.

## How it sees

How it perceives depends on how cooperative the application is, and games are the least cooperative
software there is:

- **The accessibility tree**, where one exists: real element bounds, real names, real events. Most
  applications have one. Almost no games do.
- **Pixels**, where there is none. Anchor art located by correlation finds the window and its scale.
  The game's own bitmap font, read glyph by glyph, recovers text nobody exposes — 12 faces and 2,340
  glyphs for The Sims 1
  ([`FONT-RECOGNITION.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/bridges/sims1/FONT-RECOGNITION.yml),
  [bridge code](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/modules/soul-angel/bridges/sims1)).
  QR codes carry anything long, and the egg's bands carry live state at a distance.
- **Models**, on top of both. Machine vision, visual language models and LLM completions supply the
  judgment neither pixels nor trees carry: what is happening in this scene, what this text means,
  what to do about it.
- **The network**, when the answer is elsewhere: HTTP and API calls, which is how a job in another
  game gets asked and answered.

## Both ends are open

The far end is not a screen at all. The world's representation lives in **git repositories of YAML
microworlds** — MOOLLM's objects, places and characters, and the simulated worlds themselves. The
Angel edits and generates those files, commits them, and simulates from them, while the same objects
stay open to a person with a text editor.

That is what makes the arrangement a bridge rather than a scraper: **a closed binary on one side, an
open filesystem on the other, and both ends directly manipulable.** The user's content is not inside
the automation. It is on disk, in a repo, diffable.

## No privileged verb

The Angel has **no privileged verb**. Everything above is something a person could do with a mouse, a
text editor, the community's tools and patience. The layer supplies reach and stamina, not authority.
Nothing it can reach is unreachable by hand, and nothing it does is invisible while it does it,
because it does it through the controls on the screen.

## What is built, and the hard part

What exists today, with each spec's `built:` and `not_built:` lists as the record:

- **Built:** the Electron shell with macOS and Windows native backends, screen capture, the overlay,
  and the module host; the optical codec with the egg renderer and reader and the measured band
  heights; the Sims 1 font reader and anchor matcher with tests; an MCP server for the agent surface.
- **Not built yet:** the egg as a Sims object, compiling its menu tree, hatching, the phone app,
  per-module capability checks, and the agent's planning loop. The readers have been verified
  against rendered fixtures, not yet against live frames.

The hard part is that **this is a keylogger-shaped capability set.** On macOS a single Accessibility
grant covers reading the tree, writing attributes and synthesizing input, so the operating system's
yes is coarser than what the design wants to promise. The fine-grained promise has to be ours, which
means it has to be visible: every action goes on a timestamped event ring
([`ANGEL-EVENT-BUS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/ANGEL-EVENT-BUS.yml),
[`RECORDER.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/RECORDER.yml)),
and an Angel's afternoon is reviewable the way a diff is.

## Four properties

Four properties do the work. Each is a direct-manipulation requirement met rather than argued about.

**The automation's interface is the user's interface.** In a closed game this is enforced rather than
promised: there is no API to bypass the visible controls, because there is no API. A constraint that
started as the price of working with a twenty-six-year-old binary turns out to be the property you
would want anyway, and would never have kept voluntarily.

**Pending work is an object, not a notification.** A promise with a location and a sprite can be
walked past, pointed at, asked what it is, and acted on next Tuesday. A toast can only be missed.

**Taking over is one click, at any moment.** Hatch the egg early and the character is back
immediately. Cancellation is the empty return value, so the safest outcome is also the cheapest one
to produce, for a person in a hurry or for a timeout.

**The dial between hands is explicit and live.** Manual, confirm each, timeout with a named default,
auto, yolo — switchable while the operation is outstanding. Consent is a setting the user holds, not
a mode the agent infers.

That answers the objection that this settlement is nostalgic. The reason to make automation
navigable is not that a human will always want to drive. It is that a system whose automation uses
the visible controls is inspectable, testable and repairable by the person whose data it is, and a
system with a private control channel is none of those, whatever it promises.

Further reading: the Screen Angel skill
([`SKILL.md`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/skills/screen-angel/SKILL.md)) ·
the Soul City design
([`soul-city.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md)) ·
literary roots in [`designs/pkd/a-scanner-darkly.md`](../pkd/a-scanner-darkly.md).

---

Previous: [The showcase: a Sim goes to work in another game](the-errand.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [The other showcase: Ebike Safari](ebike-safari.md)
