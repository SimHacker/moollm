# The showcase: a Sim goes to work in another game

*Part 3 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

This part and [the next](screen-angel.md) describe a system in which the automation has no private
controls. Every action an agent takes goes through an affordance that is visible on screen,
reachable by hand, and can be taken over mid-flight.

The earlier parts, on [the front page](../INTERFACE-TO-AGENCY.md), in [The Sims](the-sims.md) and
in [DreamScape](dreamscape.md), argued for these one at a time:

- agents get no verbs people lack;
- objects advertise, and agents choose from the same menu people do;
- one visible queue holds everyone's actions;
- demonstration and dictation run both ways;
- people are agents;
- the state is in files ([Behind the scenes](the-state-is-a-file.md)).

This design applies all of them across programs that were not written to cooperate.

## The claim

*An agent can do real work across closed programs, reaching into them only through the controls a
person has — the screen, the mouse, the keyboard — and everything it does can stay visible,
interruptible and readable by that person.*

Anything it calls outside the programs, a person could call too. A game from 2000 with no API is
close to the hardest case, which is why it is the example.

## Three names

- **Screen Angel** is a layer that sits over any application as a transparent, always-on-top,
  click-through overlay. It reads what is on screen — the accessibility tree where there is one,
  the pixels where there is not — and acts on an application by moving the mouse and pressing keys.
  Spec: [`SCREEN-ANGEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/SCREEN-ANGEL.yml) ·
  what it may do: [`CAPABILITIES.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/CAPABILITIES.yml).
- Outward, Screen Angel can call any service: LLM text completion, vision language models for
  understanding images, speech recognition and synthesis, or ordering a pizza. It is written in
  TypeScript and runs in Electron. Its abilities come as modules — some for one game, some for all
  of them — that can be plugged in, downloaded and upgraded without reinstalling it.
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

When the job is done, Soul Angel clicks the egg and picks from that pie menu, as you would. The egg
does the rest itself, as a Sims object: it rematerializes her by the road, changes her state, and
rewards her according to how the job went.

Soul Angel's only way into the game is the one every player has: picking from the pie menus of
objects. A custom object can do anything in the game that any Sims object can, so that one way in is
enough. You can click the same egg at any time and pick for yourself, and she comes back.

Nothing in that loop is hidden from the player, and Soul Angel uses no verb the player lacks. The
closed game enforces this: with no API to go around the visible controls, there is no other way to
do it.

The rules for what may cross between games — conservation, fork and sync, roles as offices — are in
[`skills/soul-city/SOUL-BRIDGES.md`](../../skills/soul-city/SOUL-BRIDGES.md). The rest of this part
covers the game, the egg and the errand. [The next part](screen-angel.md) covers the layer doing the
clicking.

## The game, as it shipped

The worked case is **The Sims 1**, the 2000 game, running as it shipped: no source, no patch, no
injected code.

What it does have is a content pipeline. Custom objects are `.iff` files with their own art, behaviour
trees and pie menus, and players have been making them since 2000. How those objects work:
[`designs/sims/sims-object-model.md`](../sims/sims-object-model.md),
[`sims-pie-menus.md`](../sims/sims-pie-menus.md),
[`sims-find-best-action.md`](../sims/sims-find-best-action.md) (autonomy choosing among advertisements),
[`sims-simantics-vm.md`](../sims/sims-simantics-vm.md).

## The Easter egg

The Easter egg is a custom Sims object: small, colourfully painted, standing in the room for a piece
of work in progress. It is a pending result you can see, with a pie menu on it like any other Sims
object. It is built the way Sims objects have always been built, with the machinery Maxis shipped.
Spec: [`EGGS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/EGGS.yml).

It is called an Easter egg because it is painted to be found, and two readers read the paint:

- the player, who sees at a glance that a job is outstanding and what state it is in;
- Soul Angel, which finds and reads the same egg from the same pixels.

## The Easter egg is a colourful QR code

The paint works like a QR code on an object in the game. Two readers can decode it: Screen Angel
reading the screen directly, and a phone app pointed at the screen. Neither needs anything from the
game but its pixels.

The code is colour bands up the egg's body, read like a resistor: position is the digit, colour is the
value. A white cap above a black cap marks where the stack starts and ends. The caps also set the
scale — a cap is exactly one band tall, so the egg gives its own scale at any zoom — and give the
reader a known white and a known black to correct colour against.

Reading from a screen grab is cheap and exact. The frame comes off the compositor with no optics in
the way, every pixel is the pixel the game drew, and two pixels a band decodes reliably.

Reading through a phone camera is harder: perspective, sensor noise, a warm cast from the room's
lighting, soft focus, glare, and moiré between the pixel grid and the sensor grid. The measured floor
rises to six pixels a band. The caps let a photo taken in evening light correct its colour against
them.

Both numbers are measured. Code:
[`packages/optical-codec/`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/optical-codec)
(including [`measure-eggs.ts`](https://github.com/SimHacker/MicropolisCore/blob/main/packages/optical-codec/scripts/measure-eggs.ts)) ·
what it can see: [`RECOGNIZER.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/RECOGNIZER.yml) ·
the phone path: [`MOBILE-CAMERA.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/MOBILE-CAMERA.yml) ·
longer messages: [`OPTICAL-CHANNEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/OPTICAL-CHANNEL.yml).

The camera path is for screens you do not control: a stream, a friend's monitor, a game running on
a machine you will never touch.

## The errand

The errand is a job in a different game, not on a different lot or a downtown tile. What she does
for the afternoon happens in Micropolis, or in another game entirely, on the other side of a bridge
between two save files.

While the egg stands by the road, a call is outstanding. The result comes home through the egg's pie
menu, whose nested submenus list every consequence the job is permitted to have. The menu is the
return type of the call.

That matters more between games than between rooms. The other game has its own rules, its own units
and its own idea of what a promotion is worth, and none of that can reach into this household except
as an item a player selects. What another game may do to your Sim is a list you can read, stored in
the object file in your Downloads folder.

Jobs that need no bridge at all, only a screen and a clock:
[`UNIVERSAL-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/UNIVERSAL-JOBS.yml) ·
jobs outside games: [`OUT-OF-GAME-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/OUT-OF-GAME-JOBS.yml) ·
the errand protocol: [`SOUL-BRIDGES.md` § the errand](../../skills/soul-city/SOUL-BRIDGES.md#the-errand-a-job-in-another-game).

---

Previous: [Same world, same hands: DreamScape, 1995](dreamscape.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [Screen Angel: the layer doing the clicking](screen-angel.md)
