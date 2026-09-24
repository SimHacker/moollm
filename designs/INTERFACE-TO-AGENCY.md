# An interface to agency, not agents instead of an interface

The 1997 argument between Ben Shneiderman and Pattie Maes at IUI was never settled, it was
shipped in one direction. Maes's interface agents won the product war: the assistant, the
recommender, the chat window that stands between you and the thing you are working on.
Shneiderman's objection was not that software should be dumb. It was that automation must
arrive as **comprehensible, predictable, and controllable** machinery, with the object of
interest continuously visible and every action rapid, incremental, and reversible.

Brad Myers restates the objection from the interaction-technique side in his 2026 proposal for
intelligent interaction techniques ([arXiv:2609.16295](https://arxiv.org/abs/2609.16295)). He
argues that graphical interfaces stay relevant after language and speech interfaces get good,
because some tasks are easier to say and others are easier to do, and Shneiderman's list tells you
which: direct manipulation earns its place when it is feasible to have "continuous representation
of the object of interest" with "rapid, incremental, reversible operations whose impact on the
object of interest is immediately visible." His remedy is not a chat window parked beside a dumb
GUI. It is to make the interaction techniques themselves more intelligent while keeping what made
them work.

This doc takes the same position from the programming-by-demonstration side.

*"An interface to agency" is Don's formulation of Shneiderman's position, not a phrase of
Shneiderman's. His own vocabulary is direct manipulation, universal usability, supertools,
and human-centered AI. The formulation is a good one because it names what the alternative
gets wrong: agency is the thing you want, and an agent is only one way to package it.*

## The claim

**Anything an agent can do, a person should be able to do through an interface, and no
capability should be reachable only by asking the agent.** The agent may bring more attention,
memory and bandwidth to a task. It may not have a different set of verbs.

People want agency. An agent is one way to package it, and a good interface is still required
either way.

Programming by demonstration depends on this rule, in both directions. The systems collected in
*Watch What I Do* (Allen Cypher, ed., 1993, with chapters by Henry Lieberman, Brad Myers and
others) could only generalize from actions they could see the user take. Turn that around: a
person cannot demonstrate anything through an interface the agent has hidden, and cannot learn
from an agent whose work happens somewhere they cannot watch. An agent that works through the
visible controls gives a demonstration every time it acts, and it can take one back from you
just as easily.

## Start with the classic case

The argument is easiest to make where direct manipulation is least arguable. In The Sims you put
a window in a wall by picking the window up and moving it along the wall. The window is visible
the whole time, the game shows you whether it fits before you let go, and if you don't like where
it went you pick it up again. Nobody needs to be persuaded that this is direct manipulation.

Now add an assistant, built one of two ways.

The antagonistic assistant takes "put a window in the kitchen" and does it out of sight. The
better it gets, the less reason you have to open build mode at all, until the placement tool is
the thing the assistant exists to hide. When it guesses wrong you have one recourse, which is to
describe the wall more carefully. And it has thrown away the fun: The Sims is a game people play
*because* building the house and dressing the Sims with their own hands is the pleasure. An agent
that insists on doing that for you has misunderstood what the product is, and it has also cut
itself off from the best teacher it could have, which is you doing the thing while it watches.

The cooperative assistant takes the same sentence and uses the same tool, on screen. The window
appears under the cursor, slides along the wall, and you can grab it mid-drag and put it somewhere
else. The sentence was a faster way to start the gesture, not a replacement for having one. That
is what an intelligent interaction technique looks like from the user's chair: the technique is
still there, it just got better at guessing where you were going.

The Sims already worked this way in 2000, for its own agents. Every object advertises what it can
do, and those advertisements are the interactions in its pie menu. When you click the fridge and
pick "Have Snack," you choose from that menu. When a Sim acts on its own, its autonomy scores the
same advertisements against its needs and picks from the same list. Either way the choice lands in
the same action queue, visible at the top of the screen, and you can cancel any of it with a
click. The player and the agents have one set of verbs, advertised by the objects, not by the
agents.

That idea is old, and it is at the heart of MOOLLM, which borrows heavily from The Sims and
other designs that worked. In MOOLLM, objects, rooms and characters advertise what can be done
with them ([`skills/advertisement/`](../skills/advertisement/)), and the LLM choosing an action
reads the same advertisements a person browsing the directory reads. Applying it to LLMs has
worked: the model gets a menu instead of a blank page, and the person gets to see the menu.

The difference between the two assistants is not the language model. It is whether the object of interest
stays in front of you, and whether the agent's hand and yours are on the same control. Any
visible control can carry a demonstration — pressing buttons and picking from menus demonstrate
fine, and neither is direct manipulation. What direct manipulation adds is a rich channel: where
you dropped the window, how you slid it, what you tried first and moved. An agent that takes the
controls away takes the demonstrations with them, and the richest ones first.

## Same world, same hands: DreamScape, 1995

This is an old argument, and it has been demonstrated before, with sprites instead of LLMs.
DreamScape was a "constructive experience" Don built on Kaleida Labs' ScriptX and demoed at
Apple's Worldwide Developers Conference on 11 May 1995
([video](https://www.youtube.com/watch?v=5NytloOy7WM),
[transcript](https://donhopkins.medium.com/1995-apple-world-wide-developers-conference-kaleida-labs-scriptx-demo-64271dd65570)).
It put the user and an agent in the same world, with the same objects and the same verbs.

- **Rooms connected by a map, and a head that is you.** The head is the user's representation.
  Throw it off the edge of the screen and the view follows it into the linked room, the way
  next and previous work in a slide show. Click the head and you get the map, centred on where
  you are, and you can edit the map by hand — disconnect rooms, rewire them, run the
  presentation backwards.
- **Tools are objects in the room.** A flower is a drawing tool: drag it around and it drops
  petals on the background, "a vertical painting tool, for painting with dandelions." A
  duplicator dropped on the flower fissions it into two. Press and drag on the background and
  you blow wind — actually warped gravity — across everything that moves.
- **Parts snap into trees.** Robot parts, puppet bodies and spirals plug together at
  registration points drawn in Director, "Barrel of Monkeys or Mr. Potato Head type things."
  The result is an animated skeleton, and a web inspector served from inside ScriptX showed the
  same tree as a nested list with forms to edit each part's elasticity, "isomorphic to an
  outliner."
- **The butterfly is autonomous.** "You could call that an agent if you want." It flies where it
  likes, you can grab it and move it, and your wind pushes it like anything else. In the demo it
  picked up the head and flew off the edge of the screen, and the view went with it: "So now the
  butterfly's in control of the presentation."

The butterfly could grab the flower and draw, just as you could. That is the point. Now compose
them. Put the flower at the end of a waving robot arm and hand the arm to the butterfly. The
petals land along the sum of three motions — the butterfly's flight, the arm's wave, and the wind
you are blowing — and every one of those contributions is a node in a tree you can see, pick up,
take apart and rebuild. Agency stops being a property of one actor and becomes something you
distribute across a structure: some of the motion is yours, some is the agent's, some is a
mechanism's, and the drawing is what they do together.

That is the thing worth building now. People and agents plug together in many ways, and the
plugging is itself direct manipulation.

The demo also shows the failure in the other direction. The butterfly could steal the head but
could not edit the map; the user had a verb the agent lacked. That gap is less dangerous than
the reverse, but it is still a gap: a verb the agent cannot use is one it cannot help with and
cannot learn by watching. The goal is the same verbs in both hands.

In the same demo, the reason for all the other metaphors, and for the web inspector: "As
Negroponte says, Direct Manipulation is only good for driving and sex." Direct manipulation was
never supposed to be the only interface — the argument is that it must never be the one taken
away.

## Chat is a second manipulator, not the interface

Myers's point cuts both ways. The natural-language channel earns its place by being **one of two
ways in**, and it is strongest exactly where direct manipulation is weakest: across many objects
at once, on underspecified intent, and on work that needs judgment about wording. Placing 228
windows by hand is miserable; asking for a window on every south wall is easy. Conversely, nudging
one window one tile left by hand is instant, and doing it through chat is silly.

The discipline that keeps this honest: **the chat channel may only do things that show up in the
object** — on screen as the controls moving, or on disk as a diff. No hidden memory, no learned
preferences, no state in the assistant. If the change cannot be seen in the thing itself, it did
not happen.

## The showcase: automation that drives the user's own controls

The strongest form of this argument is not an essay, it is a system where the automation has no
private controls at all. Every action an agent takes, it takes through an affordance that is
visible on screen, reachable by hand, and takeable over mid-flight.

The worked case is **The Sims 1** — the 2000 game, running as it shipped, no source, no patch, no
injected code. What it does have is a content pipeline: custom objects are `.iff` files with their own
art, behaviour trees and pie menus, and the community has been minting them for twenty-five years. So
the egg is not a hypothetical engine feature. It is a **custom object**, built the way Sims objects have
always been built, and everything below is a use of machinery Maxis shipped rather than a change to it.

It is called an egg for both meanings at once, and both are accurate. An **Easter egg** is a hidden
surprise you find by looking, which is what a small object sitting in a room is; a literal egg contains
something and opens exactly once, which is what a pending result does. The name teaches the mechanic
instead of decorating it — and the pun keeps paying, because an egg that brightens for a known few
frames to signal the layer is winking at the camera in every sense of the phrase.

It carries its value in the open, as colour bands up its body read like a resistor: position is the
digit, colour is the value, with a white cap above a black cap to mark where the stack starts and ends,
set the scale (a cap is exactly one band tall, so the egg is self-describing at any zoom), and hand the
reader a known white and a known black to correct colour against. That last job matters because there
are two ways to read one and they are wildly different work. **From a screen grab it is cheap and
exact**: the frame comes off the compositor with no optics in the way, every pixel is the pixel the game
drew, and two pixels a band decodes reliably. **Through a phone camera pointed at a monitor it is
hard**: perspective, sensor noise, a warm cast off the room's lighting, soft focus, glare, and moire
between the pixel grid and the sensor grid — and the measured floor rises to six pixels a band. The
caps are what make the second case survivable, since a photograph taken in evening light corrects
itself against them rather than needing to be told what the light was. Both numbers are measured rather
than asserted, and the camera path is not a stunt: it is how you read a screen you do not own — a
stream, a friend's monitor, a photograph of a game running on a machine you will never touch.

The errand is **remote work in the sense the phrase never means**: not a different lot, not a downtown
tile — a job in a *different game*. A Sim walks to the carpool and vanishes, and what she is doing for
the afternoon is happening in Micropolis, or in another title entirely, on the other side of a bridge
between two save files. Where she stood, the egg is left behind: a custom object whose presence means
*a call is outstanding*, sitting at the exact spot she disappeared from, at the car door.

The result comes home through that egg's own pie menu, whose nested submenus enumerate every
consequence the job is permitted to have. The menu is the return type. That matters more across games
than it would across rooms, because the other game has its own rules, its own units and its own idea of
what a promotion is worth — and none of that can reach into this household except by being an item a
player selects. The space of what a foreign game may do to your Sim is a readable list rather than a
promise, and the list is in the object, in the Downloads folder, on your disk.

### The layer doing the clicking

The thing on the other side of that pie menu is **Screen Angel**, and it needs introducing, because
the whole argument depends on what it is allowed to be.

It is a scriptable layer over *any* application's interface — selecting and querying components,
matching visual patterns, handling events, driving widgets from outside, without modifying the
application. Don named it aQuery in a 2013 email to Peter Korn, on the analogy that it is to native
interface components what jQuery is to the DOM, and renamed it in 2026 when the borrowed morpheme
had aged worse than the idea. The new name is the ladder: **a screen scraper takes, a screen reader
reads to you, a screen angel acts for you** — and it describes the implementation literally, since
the thing is a transparent, always-topmost, click-through overlay. Invisible, above you, intervening.
**Soul Angel** is its first application, the module that knows about characters and souls, and The
Sims 1 is Soul Angel's first bridge.

What it can do is bounded by one sentence: **anything a player can do.** Concretely, that is a lot.
It sees the screen and it moves the mouse and presses keys. It navigates menus, walks the camera
around a world, clicks a pie item. It can save and quit a game, read the save file, edit or
regenerate it, and start the game again — which is the high-bandwidth channel, used between sessions
because it costs a restart. During play it uses the low-bandwidth one: pie menus, dialog trees, codes
on screen, typed parameters. Two channels, neither a fallback for the other, and the reason routine
cross-game play does not require a save-quit-edit-relaunch cycle.

How it perceives depends on how cooperative the application is, and games are the least cooperative
software there is:

- **The accessibility tree**, where one exists — real element bounds, real names, real events. Most
  applications. Almost no games.
- **Pixels**, where it does not. Anchor art located by correlation to find the window and its scale,
  the game's own bitmap font read glyph by glyph to recover text nobody exposes, QR codes for
  anything long, and the egg's colour band codes for live state at a distance.
- **Models**, on top of both. Machine vision, visual language models, and LLM completions supply the
  judgment neither pixels nor trees carry: what is happening in this scene, what this text means,
  what to do about it.
- **The network**, when the answer is elsewhere — HTTP and API calls, which is how a job in another
  game gets asked and answered.

And the far end is not a screen at all. The world's representation lives in **git repositories of
YAML microworlds** — moollm's selfish objects, places, characters, the simulated worlds themselves —
so the Angel edits and generates files, commits them, and simulates from them, while the same objects
stay open to a person with a text editor. That is what makes the whole arrangement a bridge rather
than a scraper: **a closed binary on one side, an open filesystem on the other, and both ends
directly manipulable.** The user's content is not inside the automation; it is on disk, in a repo,
diffable.

Which is where the ceiling matters. The Angel has **no privileged verb**. Everything in that list is
something a person could do with a mouse, a text editor and patience — the layer supplies reach and
stamina, not authority. Nothing it can reach is unreachable by hand, and nothing it does is invisible
while it does it, because it does it through the controls that are on the screen.

Two honest caveats. **The layer does not exist yet** — eleven years of prose, one prototype of the
shell it would live in, and the bridge work described here. And **this is a keylogger-shaped
capability set**: on macOS a single Accessibility grant covers reading the tree, writing attributes
and synthesizing input, so the operating system's coarse yes is coarser than what the design wants to
promise. The fine-grained promise has to be ours, which means it has to be visible: every action goes
on a timestamped event ring, and an Angel's afternoon is reviewable the way a diff is.

Four properties are doing the work, and each one is a direct-manipulation requirement met rather
than argued about:

**The automation's interface is the user's interface.** In a closed game this is enforced rather than
promised — there is no API to bypass the visible controls with, because there is no API. A constraint
that started as the price of working with a twenty-six-year-old binary turns out to be the property
you would want anyway, and would never have kept voluntarily.

**Pending work is an object, not a notification.** A promise with a location and a sprite can be
walked past, pointed at, asked what it is, and acted on next Tuesday. A toast can only be missed.

**Taking over is one click, at any moment.** Hatch the egg early and the character is back
immediately, wherever she was standing. Cancellation is the empty return value, so the safest
outcome is also the cheapest one to produce — for a person in a hurry or for a timeout.

**The dial between hands is explicit and live.** Manual, confirm each, timeout with a named
default, auto, yolo — switchable while the operation is outstanding. Consent is a setting the user
holds, not a mode the agent infers.

Which is the answer to the objection that this settlement is nostalgic. The reason to make
automation navigable is not that a human will always want to drive; it is that a system whose
automation uses the visible controls is inspectable, testable, and repairable by the person whose
data it is — and a system with a private control channel is none of those, whatever it promises.

Specs: the layer in [`SCREEN-ANGEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/SCREEN-ANGEL.yml)
and what it is permitted in [`CAPABILITIES.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/CAPABILITIES.yml) ·
what it can see in [`RECOGNIZER.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/RECOGNIZER.yml) ·
[`EGGS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/EGGS.yml) ·
[`OPTICAL-CHANNEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/OPTICAL-CHANNEL.yml) ·
[`UNIVERSAL-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/UNIVERSAL-JOBS.yml) ·
protocol in [`skills/soul-city/SOUL-BRIDGES.md`](../skills/soul-city/SOUL-BRIDGES.md#the-errand-a-job-in-another-game) · literary roots in [`designs/pkd/a-scanner-darkly.md`](pkd/a-scanner-darkly.md)

## The other showcase: a control channel software cannot enter

The egg settlement is *shared* controls — the layer clicks the pie item a person clicks, and either
hand can drive. [Ebike Safari](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ebike-safari)
is the other settlement, and it is the stronger one because it is not a policy: **no agent can pedal.**
The primary action channel is physically closed to software, so whatever agency the system has must
arrive as an interpretation of something the rider already did.

It also passes Shneiderman's 1983 test more literally than a GUI can, on the criterion GUIs cheat on.
Direct manipulation's hard problem is building a representation convincing enough that acting on it
feels like acting on the thing. Ebike Safari skips the problem: the object of interest is the city and
you are in it, and the walls were already drawn by OpenStreetMap. Physical action instead of syntax is
not a metaphor either — `ROUNDABOUT(counterclockwise)` means whisk cream, and it is performed by riding
around a roundabout counterclockwise. There is no command language to be spared; the spell IS the
manoeuvre. The brake lever is the flipper: stop and the place comes into focus, roll on and the
interface melts ([`geometry-as-language.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/geometry-as-language.md)).

His visual information-seeking mantra lands somewhere he never put it: **velocity is the zoom control.**
Rolling is the overview, slowing is the filter, stopped at a red light is details on demand — and the
wait is where [`patience.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/patience.md)
mints something spendable. Same shape as the egg's zoom rungs, where the far view says only *I am here*:
resolution follows attention, and attention has a physical proxy.

**Then it fails his third criterion outright, and the failure is load-bearing.** You cannot undo a
ride. The kilometres are spent, the exposure happened, the wheels do not turn backwards. So the
reversibility had to migrate entirely into the interpretation: the ride file, the derived gestures, the
exposure log and the stories are files that regenerate and revert, while the world itself is
append-only. Which is the same split as the two channels into a closed game, and the same discipline as
[amsterdank](https://github.com/SimHacker/amsterdank)'s rule that claims accumulate and resolution
happens at read time. The design's own joke makes the point: a clockwise roundabout is mapped to UNDO,
and what it can undo is the reading of the ride, never the ride.

One more thing 1983 did not have to handle. "Continuous representation" is singular in the paper and
plural here — the street under the wheel and OSM's claim about it are two representations that can
disagree, and the disagreement is the signal rather than an error. Absence means unknown, *illegible*
is a legitimate value that schedules a revisit, and a guess is not a value.

### The nudge is where this can still go wrong

The bike is not a pure input device. It has two actuators — motor assist, and a suggested heading —
and [`navigation-smell-steer.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/navigation-smell-steer.md)
has the map drifting toward the suggested smell heading with silence committing it. A suggestion that
takes effect before it was legible is a private control channel, and being a gentle one does not exempt
it; that is Shneiderman's objection arriving on a bicycle. The answer there is Don's own pie menu idiom
— default wedge pre-highlighted so the suggestion is readable before it acts, grab anytime and you own
the heading, momentum cancels on grab, no turn-by-turn until the rider commits — plus a rule that only
*continue as you are* may commit silently, since a turn nobody saw coming is the failure mode.

Assist is the subtler one. Making the preferred route physically easier to pedal is influence below the
level of perception: the rider feels a hill, not a recommendation. So assist may respond to the terrain
and never to the route.

### Where Shneiderman's criteria run out

He assumed the object of interest was yours, and visible only to you. A city is other people's, a ride
is legible to everyone on the street, and an exposure log is a record of other people's homes. Direct
manipulation says nothing about that — it is a criteria set for a workstation — which is why there is a
[`privacy.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/privacy.md)
and why consent is a file. The 1997 debate is not the only argument this design has to survive.

## Behind the scenes: the state is a file

The classic case needs a graphical interface that already exists, and most things agents work on
have none. There is no build mode for a memorial, a consent record, or what a character is allowed
to say. MOOLLM's answer is to put that state where a person can reach it anyway: in a git
repository, as files.

This is the weaker direct-manipulation claim and should be made as one. Editing YAML in a text
editor is editing a representation of the object, not the object, which puts it closer to a
command language than to dragging a window along a wall. Cursor lets you type the edit, dictate
it, or describe it and have it made, and that narrows the gap without closing it.

It is still the strong claim among the ways to change an agent. Compare them by how directly the
thing you edit maps onto the behaviour you get:

| How you change the agent | What you can see | What you can edit | Can you undo it? |
|---|---|---|---|
| Training or fine-tuning | loss curves and samples | the data, never the result | retrain |
| Preference tuning from thumbs up and down | nothing | a vote | no |
| Vendor "memory" | a summary, if the product shows one | delete an entry, sometimes | partly |
| A hidden system prompt | nothing | nothing | no |
| An instructions box | the text you wrote, not the rest of the prompt | your text | by retyping |
| A MOOLLM file | all of it, in the repo | all of it, one line at a time | `git revert` |

The first rows edit an agent the way you would edit a person, by influence and hope. The last
row is a one-to-one, continuously visible, reversible definition: the character's knowledge,
refusals and consent are the bytes on the screen, and changing a byte changes what the agent is
given. The model that reads those bytes is as opaque as ever; the definition is not. That is as
close to direct manipulation as editing a definition gets.

It is also the other half of Shneiderman's list: nothing hidden, everything reversible, every
change visible as a diff. It is the floor under the interface, not a substitute for one — and it
is what a proper interface should be editing underneath, the way DreamScape's outliner and its
rooms were two views of one tree, so that the person holding the mouse and the agent holding the
text are changing the same thing.

### The text is what demonstration programs

A visible, editable text of the agents, the objects and the world gives programming by
demonstration something to program. Demonstrations have always needed a target: a macro, a
script, a rule the system writes down from what it watched. Here the target is the same file the
person can already read.

That lets the flow run backwards. You type or dictate what you want, and the agent does the text
editing for you. The original text, the proposed edit, and the result are all on the screen, and
you accept it, reject it, or change it by hand. The agent is now demonstrating to you how the
agents are programmed, one edit at a time, in answer to what you said. Watch it do that enough
times and you can make the next edit yourself.

So PBD can also stand for **programming by dictation**, and it runs both ways:

- **You to the agent.** Say or type the intention; get back an edit you can see, judge and revise.
  Or do it by hand and let the agent watch and generalize — the original direction.
- **The agent to you.** It dictates back what it did or wants to do, in text or a synthesized
  voice, pointing at the lines it changed. The explanation is checkable because the thing it
  describes is on the screen next to it.

Dictation is not demonstration. One states intent in words; the other shows it in action, and
each covers cases the other handles badly. They need the same condition, though: a representation
both parties can see and both can change. Without it, demonstration has nothing to write into, and
dictation produces changes nobody can check.

**So the repository is a direct-manipulation interface to a population of agents, where the agents
are files.** A coffeeshop is a directory. A cat is a YAML file. A memorial is a file with citations
in it. A consent record is a file that gates whether another file may be rendered at all. Every one
of them can be opened, read, edited by hand, diffed, reverted, and grepped, and every one of them
can equally be operated on by an LLM through chat. Two ways in to one set of objects, neither
privileged, neither hiding state from the other.

Shneiderman's 1983 criteria, checked against the artifact rather than asserted:

| Criterion | How the repo does it |
|---|---|
| Continuous representation of the object of interest | the directory listing; `PLACE.yml` is the shop, not a description of a record about the shop |
| Physical action instead of syntax | the weakest row: editing a file is syntax. Dropping a photograph into `survey/` or deleting a character's directory comes closer. It is fully met only when a real interface edits the files for you |
| Immediate visible feedback | the diff |
| Rapid, incremental, reversible | commit, revert, branch. Reversibility is the substrate rather than a feature |
| Overview first, zoom and filter, details on demand | `ls`, then `GLANCE.yml`, then `CARD.yml`, then `SKILL.md`. The semantic image pyramid is his visual information-seeking mantra with a different sensor |

The last row is the one that surprised me. MOOLLM's reading-order discipline was designed to
manage LLM context, and it independently reinvented "overview first, zoom and filter, then
details on demand" -- because the constraint is the same whether the reader is an eye with a
fovea or a model with a window.

### What the agent-as-interface pattern takes away

An assistant with private state is unfalsifiable. You cannot open it, diff it, or revert it,
and when it is wrong about you there is no artifact to correct -- only more conversation,
which is why every such product eventually feels like arguing with a hotel clerk.

The MOOLLM inversion: **the agent has no state that is not a file you can open.** What the
cat at the 420 Café knows about John Sinclair is `memorial/john-sinclair.yml`, and if the cat
says something wrong, you fix the file. What the robot budtender may say is bounded by
`refuses:` in its own YAML. Whether a real person may be portrayed at all is decided by
`characters/consent.yml`, which a human wrote and can delete.

Control stops being a promise in a privacy policy and becomes a readable fact on disk. That
is the whole difference, and it is the reason the licensing, the provenance, and the consent
records in [amsterdank](https://github.com/SimHacker/amsterdank) are files rather than
policies: **a constraint that lives in the object travels with it.**

### Tangible agents

The objects are agents in the MOO sense -- they advertise what can be done to them, they hold
their own methods, they refuse things -- and simultaneously ordinary files. A coffeeshop
advertises `VISIT` and `READ-BOARD`. A cat advertises stories and refuses to speak as the dead.
A place refuses to average two coordinates. None of that requires a running process, because
the LLM supplies the interpreter and the directory supplies the state.

This is what makes them tangible rather than metaphorically tangible. You can `cp` a cat. You
can `git blame` a memorial and find out who claimed what, when. You can hand somebody the file
that is them, which is the design principle underneath
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
a budtender's tier-4 self-authored character, and a patron's `incarnate` grant. Handing over a
file is a transfer of authorship that no assistant-shaped product can offer, because there is
nothing to hand over.

## Where this sits

- [`DIRECTORY-AS-IUNKNOWN.md`](./DIRECTORY-AS-IUNKNOWN.md) — the mechanism: a directory as an interface-bearing object
- [`skills/design-sense/masters/ben-shneiderman.md`](../skills/design-sense/masters/ben-shneiderman.md) — his votes and vetoes as a loadable head
- Brad Myers, intelligent interaction techniques proposal, [arXiv:2609.16295](https://arxiv.org/abs/2609.16295) (2026), and *Pick, Click, Flick! The Story of Interaction Techniques* ([ixtbook.com](https://www.ixtbook.com)) — the same settlement argued from inside the interaction technique
- [`skills/design-sense/lenses/direct-manipulation.md`](../skills/design-sense/lenses/direct-manipulation.md) — the lens
- [`skills/cursor-mirror/characters/i-beam/CONSTITUTION.md`](../skills/cursor-mirror/characters/i-beam/CONSTITUTION.md) — the anti-Clippy constitution, which is this argument applied to one character
- [`skills/representation-ethics/`](../skills/representation-ethics/) — consent as a file, which is control as a fact
- [wwsff `characters/ben-shneiderman/agents-debate-1997.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-shneiderman/agents-debate-1997.md) — the debate itself, and he is an [invited guest](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-shneiderman/invitation.md), so this doc should expect to be corrected by its subject

## The uncomfortable part

Shneiderman's veto list includes *don't ship an irreversible operation and call it power*, and
an LLM writing files is exactly that unless the reversibility is real. It is real here only
because of git, and only while the human keeps reading diffs. An agent that commits without
review, or a human who stops reading, converts this whole arrangement back into the thing it
was built to avoid -- an opaque process with private state, wearing a repository as a costume.

The interface to agency is not a property of the file format. It is a practice, and the diff
is where it is enforced.
