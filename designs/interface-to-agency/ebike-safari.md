# The other showcase: a control channel software cannot enter

*Part 5 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

The [Easter egg settlement](the-errand.md) is *shared* controls — the layer clicks the pie item a person clicks, and either
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
interface melts ([geometry-as-language.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/geometry-as-language.md)).

His visual information-seeking mantra lands somewhere he never put it: **velocity is the zoom control.**
Rolling is the overview, slowing is the filter, stopped at a red light is details on demand — and the
wait is where [patience.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/patience.md)
mints something spendable. Same shape as the egg's zoom rungs, where the far view says only *I am here*:
resolution follows attention, and attention has a physical proxy.

**Then it fails his third criterion outright, and the failure is load-bearing.** You cannot undo a
ride. The kilometres are spent, the exposure happened, the wheels do not turn backwards. So the
reversibility had to migrate entirely into the interpretation: the ride file, the derived gestures, the
exposure log and the stories are files that regenerate and revert, while the world itself is
append-only. Which is the same split as the two channels into a closed game.

Other information layers and games sit on top of the ride the same way, each reading what the rider
already did and none of them able to pedal
([layers and games](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/layers-and-games.md)).

The design's own joke makes the point about reversibility: a clockwise roundabout is mapped to UNDO,
and what it can undo is the reading of the ride, never the ride.

One more thing 1983 did not have to handle. "Continuous representation" is singular in the paper and
plural here — the street under the wheel and OSM's claim about it are two representations that can
disagree, and the disagreement is the signal rather than an error. Absence means unknown, *illegible*
is a legitimate value that schedules a revisit, and a guess is not a value.

## The nudge is where this can still go wrong

The bike is not a pure input device. It has two actuators — motor assist, and a suggested heading —
and [navigation-smell-steer.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/navigation-smell-steer.md)
has the map drifting toward the suggested smell heading with silence committing it. A suggestion that
takes effect before it was legible is a private control channel, and being a gentle one does not exempt
it; that is Shneiderman's objection arriving on a bicycle. The answer there is Don's own pie menu idiom
— default wedge pre-highlighted so the suggestion is readable before it acts, grab anytime and you own
the heading, momentum cancels on grab, no turn-by-turn until the rider commits — plus a rule that only
*continue as you are* may commit silently, since a turn nobody saw coming is the failure mode.

Assist is the subtler one. Making the preferred route physically easier to pedal is influence below the
level of perception: the rider feels a hill, not a recommendation. So assist may respond to the terrain
and never to the route.

## Where Shneiderman's criteria run out

He assumed the object of interest was yours, and visible only to you. A city is other people's, a ride
is legible to everyone on the street, and an exposure log is a record of other people's homes. Direct
manipulation says nothing about that — it is a criteria set for a workstation — which is why there is a
[privacy.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/privacy.md)
and why consent is a file. The 1997 debate is not the only argument this design has to survive.

---

Previous: [Screen Angel: the layer doing the clicking](screen-angel.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [Behind the scenes: the state is a file](the-state-is-a-file.md)
