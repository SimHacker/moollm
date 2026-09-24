# Same world, same hands: DreamScape, 1995

*Part 2 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

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
could not edit the map; the user had a verb the agent lacked. That was a weakness. It is less
dangerous than the reverse, but a verb the agent cannot use is one it cannot help with and cannot
learn by watching. The goal is the same verbs in both hands.

There is a fair case for the gap. Few presenters would hand a butterfly the choice of the next
slide, let alone the wiring between slides, in the middle of a talk. But handing it the next slide
was already the point of that demo. WWDC had a rule that year: if your demo crashed, you did
push-ups. Don was flipping between ScriptX, Macromedia Director and Netscape on a PowerBook 540c,
any of which could have taken the machine down, and he let an autonomous butterfly steer the
presentation anyway. It didn't crash. The risk was the performance: ceding agency on stage, live,
is how you show that you mean it.

MOOLLM closes the gap. The map is rooms as directories and exits as entries in their files, so
every way in reaches it: Don edits it by hand, types or dictates what he wants and has the LLM
make the edit, or plays a character inside the world who has the agency to dig new rooms, connect
them, and walk through them. The LLM playing a character has the same verbs. The butterfly can
edit the map now, and so can you, through the same files, and every change is a diff.

In the same demo, the reason for all the other metaphors, and for the web inspector: "As
Negroponte says, Direct Manipulation is only good for driving and sex." Direct manipulation was
never supposed to be the only interface — the argument is that it must never be the one taken
away.

---

Previous: [The classic case: The Sims](the-sims.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [The showcase: a Sim goes to work in another game](the-errand.md)
