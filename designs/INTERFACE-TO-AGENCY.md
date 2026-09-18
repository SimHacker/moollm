# An interface to agency, not agents instead of an interface

The 1997 argument between Ben Shneiderman and Pattie Maes at IUI was never settled, it was
shipped in one direction. Maes's interface agents won the product war: the assistant, the
recommender, the chat window that stands between you and the thing you are working on.
Shneiderman's objection was not that software should be dumb. It was that automation must
arrive as **comprehensible, predictable, and controllable** machinery, with the object of
interest continuously visible and every action rapid, incremental, and reversible.

That objection describes a filesystem in a git repository, and nobody involved planned it
that way.

*"An interface to agency" is Don's formulation of Shneiderman's position, not a phrase of
Shneiderman's. His own vocabulary is direct manipulation, universal usability, supertools,
and human-centered AI. The formulation is a good one because it names what the alternative
gets wrong: agency is the thing you want, and an agent is only one way to package it.*

## The claim

**A MOOLLM repository is a direct-manipulation interface to a population of agents, where
the agents are files.** A coffeeshop is a directory. A cat is a YAML file. A memorial is a
file with citations in it. A consent record is a file that gates whether another file may be
rendered at all. Every one of them can be opened, read, edited by hand, diffed, reverted, and
grepped -- and every one of them can equally be operated on by an LLM through chat.

Two interfaces onto one set of continuously visible objects. Neither is privileged, and
neither hides state from the other.

## Why this satisfies the direct-manipulation test

Shneiderman's 1983 criteria, checked against the artifact rather than asserted:

| Criterion | How the repo does it |
|---|---|
| Continuous representation of the object of interest | the directory listing; `PLACE.yml` is the shop, not a description of a record about the shop |
| Physical action instead of syntax | edit the file; drop a photograph into `survey/`; delete a character to remove them |
| Immediate visible feedback | the diff |
| Rapid, incremental, reversible | commit, revert, branch. Reversibility is the substrate rather than a feature |
| Overview first, zoom and filter, details on demand | `ls`, then `GLANCE.yml`, then `CARD.yml`, then `SKILL.md`. The semantic image pyramid is his visual information-seeking mantra with a different sensor |

The last row is the one that surprised me. MOOLLM's reading-order discipline was designed to
manage LLM context, and it independently reinvented "overview first, zoom and filter, then
details on demand" -- because the constraint is the same whether the reader is an eye with a
fovea or a model with a window.

## What the agent-as-interface pattern takes away

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

## Tangible agents

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

## Chat is a second manipulator, not the interface

The natural-language channel earns its place by being **one of two ways in**, and it is
strongest exactly where direct manipulation is weakest: across many objects at once, on
underspecified intent, and on work that needs judgment about wording. Editing 228 places by
hand is miserable; asking for them all to be regenerated is easy. Conversely, fixing one
comment in one file by hand is instant, and doing it through chat is silly.

The discipline that keeps this honest: **the chat channel may only do things that leave a
diff.** No hidden memory, no learned preferences, no state in the assistant. If it cannot be
expressed as a change to a file, it did not happen.

## The showcase: automation that drives the user's own controls

The strongest form of this argument is not an essay, it is a system where the automation has no
private controls at all. Every action an agent takes, it takes through an affordance that is
visible on screen, reachable by hand, and takeable over mid-flight.

The worked case is the cross-game errand in MicropolisCore. A character in a shipped, closed game
goes to work somewhere else; the game leaves behind an object — an egg — that means *a call is
outstanding*, sitting at the exact spot the character vanished from. The result comes back by
selecting from that egg's own pie menu, whose nested submenus enumerate every consequence the job
is permitted to have. The menu is the return type, so the space of what can happen to your
character is a readable list rather than a promise.

Four properties are doing the work, and each one is a direct-manipulation requirement met rather
than argued about:

**The automation's interface is the user's interface.** The layer clicks the same pie items a
person clicks. There is no API path that bypasses the visible controls, which means there is no
capability the user cannot exercise and no action the user cannot watch.

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

Specs: [`EGGS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/EGGS.yml) ·
[`OPTICAL-CHANNEL.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/OPTICAL-CHANNEL.yml) ·
[`UNIVERSAL-JOBS.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/modules/soul-angel/UNIVERSAL-JOBS.yml) ·
protocol in [`skills/soul-city/SOUL-BRIDGES.md`](../skills/soul-city/SOUL-BRIDGES.md#the-errand-a-job-in-another-game) · literary roots in [`designs/sims/sims-pkd-perky-pat-and-a-scanner-darkly.md`](sims/sims-pkd-perky-pat-and-a-scanner-darkly.md)

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

## Where this sits

- [`DIRECTORY-AS-IUNKNOWN.md`](./DIRECTORY-AS-IUNKNOWN.md) — the mechanism: a directory as an interface-bearing object
- [`skills/design-sense/masters/ben-shneiderman.md`](../skills/design-sense/masters/ben-shneiderman.md) — his votes and vetoes as a loadable head
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
