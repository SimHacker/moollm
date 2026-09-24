# Same world, same hands: DreamScape, 1995

*Part 2 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

Don demonstrated this in 1995, with sprites instead of LLMs. DreamScape was a "constructive experience" Don built on Kaleida Labs' ScriptX and demoed at
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

The butterfly could grab the flower and draw, just as you could. The pieces also compose. Put the
flower at the end of a waving robot arm and hand the arm to the butterfly. The petals land along
the sum of three motions — the butterfly's flight, the arm's wave, and the wind you are blowing —
and each of those is a node in a tree you can see, pick up, take apart and rebuild. Some of the
motion is yours, some is the agent's and some is a mechanism's. Deciding which part the agent
holds is itself done by direct manipulation.

The demo also had the opposite gap. The butterfly could steal the head but could not edit the map,
so the user had a verb the agent lacked. That is less dangerous than an agent with a verb the user
lacks, but it is still a weakness: an agent cannot help with a verb it cannot use, or learn it by
watching.

There is a case for that gap. Few presenters would let a butterfly choose the next slide in the
middle of a talk, let alone rewire the slides. That demo did let it choose the next slide. WWDC had
a rule that year: if your demo crashed, you did push-ups. Don was switching between ScriptX,
Macromedia Director and Netscape on a PowerBook 540c, any of which could have taken the machine
down, and he let the butterfly steer the presentation anyway. It didn't crash.

MOOLLM closes the gap. The map is rooms as directories and exits as entries in their files. Don
can edit it by hand, type or dictate what he wants and have the LLM make the edit, or play a
character inside the world who can dig new rooms, connect them and walk through them. An LLM
playing a character has the same verbs, and every change is a diff.

Don quoted Negroponte in the same demo, to explain why DreamScape also had other metaphors and a
web inspector: "As Negroponte says, Direct Manipulation is only good for driving and sex." The
argument here is not that direct manipulation should be the only interface, only that it should
not be removed.

---

Previous: [The classic case: The Sims](the-sims.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [The showcase: a Sim goes to work in another game](the-errand.md)
