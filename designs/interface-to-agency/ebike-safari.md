# The other showcase: Ebike Safari

*Part 5 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

In the [Easter egg design](the-errand.md) the agent and the person share controls: Screen Angel
clicks the pie item a person would click, and either can drive.
[Ebike Safari](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ebike-safari) is a
different case. No agent can pedal. The main input is physically closed to software, so anything
the system does has to start from something the rider already did.

The object of interest is the city, and the rider is in it. Ebike Safari does not have to build a
representation convincing enough that acting on it feels like acting on the thing, and
OpenStreetMap already has the streets. The actions are physical: `ROUNDABOUT(counterclockwise)` is
performed by riding counterclockwise around a roundabout, and in the game it means whisk cream.
There is no command language to learn. Stopping brings the place into focus, and rolling on clears
the display ([geometry-as-language.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/geometry-as-language.md)).

Speed maps onto the visual information-seeking mantra. Riding is the overview, slowing down is the
filter, and stopping at a red light gives details on demand. The wait at the light also earns
something the rider can spend elsewhere
([patience.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/patience.md)).

Reversibility is where it differs. A ride cannot be undone: the kilometres are ridden and the
exposure happened. So the reversible part is the interpretation. The ride file, the derived
gestures, the exposure log and the stories are files that can be regenerated and reverted, while
the ride itself is append-only. A clockwise roundabout is mapped to UNDO, and what it undoes is a
reading of the ride.

Other information layers and games read the ride the same way, and none of them can pedal either
([layers and games](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/layers-and-games.md)).

There is also more than one representation. The street under the wheel and OpenStreetMap's
description of it can disagree, and the disagreement is recorded as data rather than treated as an
error. A missing value means unknown, "illegible" is a legitimate value that schedules a revisit,
and a guess is not recorded as a value.

## Where software can still steer

The bike has two outputs: motor assist, and a suggested heading. In
[navigation-smell-steer.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/navigation-smell-steer.md)
the map drifts toward the suggested heading, and doing nothing accepts it. A suggestion that takes
effect before the rider can read it is a private control channel, however gentle. The design uses a
pie menu instead. The default direction is highlighted, so the suggestion can be read before it
acts. Grabbing a direction takes the heading and cancels the drift. There is no turn-by-turn until
the rider commits, and only "continue as you are" may be accepted by doing nothing.

Assist is harder to see. Making the suggested route easier to pedal would steer the rider below the
level of perception: the rider would feel a gentler hill, not a recommendation. So assist may
respond to the terrain and never to the route.

## Other people

The direct manipulation criteria describe one person working on their own object at a workstation.
A city belongs to other people, a ride is visible to everyone on the street, and an exposure log
records other people's homes. Ebike Safari handles that separately, in
[privacy.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/privacy.md),
with consent recorded in files.

---

Previous: [Screen Angel: the layer doing the clicking](screen-angel.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [Behind the scenes: the state is a file](the-state-is-a-file.md)
