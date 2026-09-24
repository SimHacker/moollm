# Screen Angel: the layer doing the clicking

*Part 4 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

[The previous part](the-errand.md) told the story: a Sim takes a job as mayor in Micropolis, and
comes home when someone picks from the pie menu of a painted Easter egg. This part is about the layer
doing the clicking. Screen Angel needs more than the short definition in
[Three names](the-errand.md#three-names), because the argument depends on what it is allowed to do.

## What it is

It is a scriptable layer over any application's interface: selecting and querying components,
matching visual patterns, handling events, and driving widgets from outside without modifying the
application. Don first described it in a 2013 email to Peter Korn
([thread](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/sources/2013-email-thread.md)),
refined it in Hacker News comments over the following decade
([progression](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/sources/hacker-news-progression.md)),
and named it in 2026.

The name places it in a sequence: a screen scraper takes from the screen, a screen reader reads it
to you, and a screen angel acts on it for you. It is also literally an overlay, transparent and
above the application.

It has two research precedents. Richard Potter's Triggers, at the HCIL, was a Macintosh macro
system that found the data and controls it acted on by reading the screen's pixels, and added
behaviour the applications lacked, such as a floating tool palette for MacDraw II made from a bitmap
(["Triggers: Guiding Automation with Pixels to Achieve Data Access"](http://acypher.com/wwid/Chapters/17Triggers.html),
in Allen Cypher's *Watch What I Do: Programming by Demonstration*, 1993). Morgan Dixon and James Fogarty's
[Prefab](http://homes.cs.washington.edu/~mdixon/research/prefab/) at the University of Washington
does pixel-based reverse engineering of interface structure: it recovers widgets from screen pixels
and adds behaviour to applications without their source, across toolkits and platforms. Screen
Angel adds accessibility trees where they exist
([aQuery](https://donhopkins.com/mediawiki/index.php/AQuery) was Don's name for querying them like
the DOM), models on top, and an agent at the controls. The problem both address is the same:
software people depend on and cannot change, replace or get an API into.

Its limit is anything a player can do, with the tools players already use:

- see the screen, move the mouse, press keys;
- navigate menus, walk the camera around a world, click a pie item;
- save and quit a game, read the save file, edit or regenerate it, and start the game again.

The last item goes past what a player does by hand, since nobody reads a save file by eye. But
players have edited Sims content with tools since 2000 — the Transmogrifier for cloning and
repainting objects, community editors such as FreeSO's Volcanic for SimAntics — and Screen Angel
works with that ecosystem of user-created content tools rather than replacing it. It reads and
writes the same files those tools do, so anything it changes, a person can open in one of them, or
in a text editor once it has been converted to YAML.

Saving, editing and relaunching is the high-bandwidth channel, used between sessions because it
costs a restart. During play Screen Angel uses the low-bandwidth one: pie menus, dialog trees, codes
on screen, typed parameters. The second is why routine play across games does not need a
save-quit-edit-relaunch cycle.

## How it sees

How it perceives depends on how cooperative the application is, and games cooperate less than most
software:

- **The accessibility tree**, where one exists: real element bounds, real names, real events. Most
  applications have one. Almost no games do.
- **Pixels**, where there is none. Anchor art located by correlation finds the window and its scale.
  The game's own bitmap font, read glyph by glyph, recovers text the game does not expose: 12 faces
  and 2,340 glyphs for The Sims 1
  ([`FONT-RECOGNITION.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/bridges/sims1/FONT-RECOGNITION.yml),
  [bridge code](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/modules/soul-angel/bridges/sims1)).
  QR codes carry anything long, and the egg's bands carry live state at a distance.
- **Models**, on top of both. Machine vision, vision language models and LLM completions supply the
  judgment neither pixels nor trees carry: what is happening in this scene, what this text means,
  what to do about it.
- **The network**, when the answer is elsewhere: HTTP and API calls, which is how a job in another
  game gets asked and answered.

## Both ends are open

At the other end, the world's representation lives in git repositories of YAML microworlds:
MOOLLM's objects, places and characters, and the simulated worlds themselves. Screen Angel edits and
generates those files, commits them, and simulates from them, while the same files stay open to a
person with a text editor.

So one end is a closed binary and the other is an open filesystem, and a person can work directly
at both. The user's content is on disk in a repository, where every change shows up as a diff.

## No privileged verb

Screen Angel has no privileged verb. Everything above is something a person could do with a mouse,
a text editor, the community's tools and patience. Nothing it can reach is unreachable by hand, and
what it does is visible while it does it, because it does it through the controls on the screen.

## What is built, and the hard part

What exists today, with each spec's `built:` and `not_built:` lists as the record:

- **Built:** the Electron shell with macOS and Windows native backends, screen capture, the overlay,
  and the module host; the optical codec with the egg renderer and reader and the measured band
  heights; the Sims 1 font reader and anchor matcher with tests; an MCP server for the agent surface.
- **Not built yet:** the egg as a Sims object, compiling its menu tree, hatching, the phone app,
  per-module capability checks, and the agent's planning loop. The readers have been verified
  against rendered fixtures, not yet against live frames.

The hard part is that these are the capabilities of a keylogger. On macOS a single Accessibility
grant covers reading the tree, writing attributes and synthesizing input, so the operating system's
permission is coarser than what the design promises. The finer promise has to be kept by Screen
Angel itself, and kept visibly: every action goes on a timestamped event ring
([`ANGEL-EVENT-BUS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/ANGEL-EVENT-BUS.yml),
[`RECORDER.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/RECORDER.yml)),
so an afternoon of its actions can be reviewed afterwards.

## Four properties

Four properties make this direct manipulation rather than delegation.

**The automation's interface is the user's interface.** In a closed game this is enforced: there is
no API to bypass the visible controls, because there is no API. The constraint comes from working
with a closed binary from 2000, and it is also the property the design wants. It is the same
constraint most people meet at work, in software that is proprietary, embedded in how the job is
done, and not theirs to change or replace. A design that has to work on The Sims cannot quietly
depend on an API that the real case will not have either.

**Pending work is an object, not a notification.** An egg can be walked past, pointed at, asked what
it is, and acted on days later. A notification that has scrolled away cannot.

**Taking over is one click, at any moment.** Hatch the egg early and the character is back
immediately. Cancelling returns the empty result, so the safest outcome is also the cheapest to
produce, for a person in a hurry or for a timeout.

**The setting between hands is explicit and can change mid-job.** Manual, confirm each, timeout with
a named default, auto, or yolo, switchable while the job is outstanding. The user sets it; the agent
does not infer it.

The reason for all this is not that a person will always want to drive. A system whose automation
uses the visible controls can be inspected, tested and repaired by the person whose data it is. A
system with a private control channel cannot.

Further reading: the Screen Angel skill
([`SKILL.md`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/skills/screen-angel/SKILL.md)) ·
the Soul City design
([`soul-city.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md)) ·
Philip K. Dick's *A Scanner Darkly* on the job of reviewing recordings of your own household
([`designs/pkd/a-scanner-darkly.md`](../pkd/a-scanner-darkly.md)).

---

Previous: [The showcase: a Sim goes to work in another game](the-errand.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [The other showcase: Ebike Safari](ebike-safari.md)
