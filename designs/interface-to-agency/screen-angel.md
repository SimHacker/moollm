# The showcase: automation that drives the user's own controls

*Part 3 of 5 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

The strongest form of this argument is not an essay. It is a system where the automation has no
private controls at all: every action an agent takes goes through an affordance that is visible on
screen, reachable by hand, and can be taken over mid-flight.

## The bridge from the argument above

Everything before this was argued one piece at a time, on [the front page](../INTERFACE-TO-AGENCY.md),
in [The Sims](the-sims.md) and in [DreamScape](dreamscape.md):

- agents get no verbs people lack;
- objects advertise, and agents choose from the same menu people do;
- one visible queue holds everyone's actions;
- demonstration and dictation run both ways;
- people are agents;
- files are the floor ([Behind the scenes](the-state-is-a-file.md)).

This section puts all of them into one working design, and takes them literally outside the box:
out of one program and into another, with no cooperation from either.

## The claim

*An agent can do real work across closed programs, reaching into them only through the controls a
person has — the screen, the mouse, the keyboard — and everything it does can stay visible,
interruptible and readable by that person.*

What it calls outside the programs, a person could call too. If this holds for a twenty-six-year-old
game with no API, it holds for any interface.

## Three names

- **Screen Angel** is a layer that sits over any application as a transparent, always-on-top,
  click-through overlay. It reads what is on screen — the accessibility tree where there is one,
  the pixels where there is not — and acts on an application by moving the mouse and pressing keys.
  Spec: [`SCREEN-ANGEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/SCREEN-ANGEL.yml) ·
  what it may do: [`CAPABILITIES.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/CAPABILITIES.yml).
- Outward, Screen Angel can call any service: LLM text completion, vision language models for
  understanding images, speech recognition and synthesis, or ordering a pizza. It is written in
  TypeScript and runs in Electron. Its abilities come as modules — some for one game, some cutting
  across all of them — that can be plugged in, downloaded and upgraded without reinstalling it.
  Module system: [`MODULES.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/MODULES.yml) ·
  agent surface: [`AGENT.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/AGENT.yml) ·
  code: [`apps/screen-angel/src/`](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/src).
- **Soul Angel** is Screen Angel's module for games about people. It knows about characters, their
  relationships and their save files, and it can carry a character from one game to another.
  Module: [`modules/soul-angel/`](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/modules/soul-angel) ·
  which games and why: [`GAME-BRIDGES.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/GAME-BRIDGES.yml).
- **Micropolis** is the original SimCity, released as open source under that name in 2008. The
  player's role in it is mayor of the city.
  Code: [MicropolisCore](https://github.com/SimHacker/MicropolisCore) ·
  the mayor as an office a character can hold: [`micropolis-role-sheets.md`](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/micropolis-role-sheets.md).

## The story

A Sim in an unmodified copy of The Sims 1 takes a job as mayor of a city in Micropolis. She walks out
to the carpool, the car drives off with her in it, and for the afternoon she is running a city in a
different game.

Soul Angel carries the errand across. It has no API into either game. It sees the screen and uses the
mouse and keyboard, as a player does.

While she is away, a painted **Easter egg** stands by the road where the car door was. Its paint tells
both you and Soul Angel what state the job is in. Its pie menu lists every outcome the job is allowed
to have, so the result comes home as a choice from a readable list.

When the job is done, Soul Angel clicks the egg and picks from that pie menu, exactly as you would.
The egg does the rest itself, as a Sims object: it rematerializes her by the road, changes her state,
and rewards her according to how the job went.

Soul Angel's only way into the game is the one every player has: picking from the pie menus of
objects. A custom object can do anything in the game that any Sims object can, so that one way in is
enough. You can click the same egg at any time and pick for yourself, and she comes back.

Nothing in that loop is hidden from the player, and nothing Soul Angel does is a verb the player
lacks. The closed game enforces this rather than merely allowing it: with no API to go around the
visible controls, there is no other way to do it.

The rules for what may cross between games — conservation, fork and sync, roles as offices — are in
[`skills/soul-city/SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md). The rest of this section is
the detail: the game, the egg, the errand, the layer doing the clicking, and the four properties that
make it direct manipulation rather than delegation.

## The game, as it shipped

The worked case is **The Sims 1** — the 2000 game, running as it shipped: no source, no patch, no
injected code.

What it does have is a content pipeline. Custom objects are `.iff` files with their own art, behaviour
trees and pie menus, and the community has been making them for twenty-five years. How those objects
work: [`designs/sims/sims-object-model.md`](../sims/sims-object-model.md),
[`sims-pie-menus.md`](../sims/sims-pie-menus.md),
[`sims-find-best-action.md`](../sims/sims-find-best-action.md) (autonomy choosing among advertisements),
[`sims-simantics-vm.md`](../sims/sims-simantics-vm.md).

## The Easter egg

The Easter egg is a custom Sims object: small, colourfully painted, standing in the room for a piece
of work in progress. It is a pending result you can see, with a pie menu on it like any other Sims
object.

The Easter egg is not a hypothetical engine feature. It is built the way Sims objects have been built
for 26 years, and everything below uses machinery Maxis shipped rather than changing it.
Spec: [`EGGS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/EGGS.yml).

The name "Easter egg" matters because **the paint is the point**. Easter eggs are painted so they can
be recognized, and this one's paint does that job for two readers at once:

- the player, who sees at a glance that a job is outstanding and what state it is in;
- Soul Angel, which finds and reads the same egg from the same pixels.

One painted surface, legible to the person and to the agent, is this whole doc in a single object.
The name's other meanings come along for free: an Easter egg is something you find by looking, and
an egg holds something and hatches once, which is what a pending result does.

## The Easter egg is a colourful QR code

Think of the Easter egg as a QR code that happens to be an object in the game. Two readers can recognize and
decode it: Screen Angel reading the screen directly, and a phone app pointed at the screen. Neither
needs anything from the game but its pixels.

The code is colour bands up the egg's body, read like a resistor: position is the digit, colour is the
value. A white cap above a black cap marks where the stack starts and ends. The caps also set the
scale — a cap is exactly one band tall, so the egg describes itself at any zoom — and give the reader
a known white and a known black to correct colour against.

Reading from a screen grab is cheap and exact. The frame comes off the compositor with no optics in
the way, every pixel is the pixel the game drew, and two pixels a band decodes reliably.

Reading through a phone camera is hard: perspective, sensor noise, a warm cast from the room's
lighting, soft focus, glare, and moiré between the pixel grid and the sensor grid. The measured floor
rises to six pixels a band. The caps make it survivable, because a photo taken in evening light
corrects itself against them.

Both numbers are measured, not asserted. Code:
[`packages/optical-codec/`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/optical-codec)
(including [`measure-eggs.ts`](https://github.com/SimHacker/MicropolisCore/blob/main/packages/optical-codec/scripts/measure-eggs.ts)) ·
what it can see: [`RECOGNIZER.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/RECOGNIZER.yml) ·
the phone path: [`MOBILE-CAMERA.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/MOBILE-CAMERA.yml) ·
longer messages: [`OPTICAL-CHANNEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/OPTICAL-CHANNEL.yml).

The camera path is not a stunt. It is how you read a screen you do not own: a stream, a friend's
monitor, a game running on a machine you will never touch.

## The errand

The errand is **remote work in the sense the phrase never means**: not a different lot, not a
downtown tile, but a job in a *different game*. What she does for the afternoon happens in Micropolis,
or in another title entirely, on the other side of a bridge between two save files.

The Easter egg's presence by the road means *a call is outstanding*. The result comes home through its pie
menu, whose nested submenus list every consequence the job is permitted to have. **The menu is the
return type.**

That matters more across games than across rooms. The other game has its own rules, its own units and
its own idea of what a promotion is worth, and none of that can reach into this household except as
an item a player selects. What a foreign game may do to your Sim is a readable list rather than a
promise, and the list is in the object, in the Downloads folder, on your disk.

Jobs that need no bridge at all, only a screen and a clock:
[`UNIVERSAL-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/UNIVERSAL-JOBS.yml) ·
jobs outside games: [`OUT-OF-GAME-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/OUT-OF-GAME-JOBS.yml) ·
the errand protocol: [`SOUL-BRIDGES.md` § the errand](../../skills/soul-city/SOUL-BRIDGES.md#the-errand-a-job-in-another-game).

## The layer doing the clicking

Screen Angel needs more than the one-line definition above, because the whole argument depends on
what it is allowed to be.

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
text editor, the community's tools and patience. The layer supplies reach and stamina, not authority. Nothing it can reach is
unreachable by hand, and nothing it does is invisible while it does it, because it does it through
the controls on the screen.

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

Previous: [Same world, same hands: DreamScape, 1995](dreamscape.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [The other showcase: Ebike Safari](ebike-safari.md)
