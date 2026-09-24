# Start with the classic case

*Part 1 of 5 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

The argument is easiest to make where direct manipulation is least arguable. In The Sims you put
a window in a wall by picking the window up and moving it along the wall. The window is visible
the whole time, the game shows you whether it fits before you let go, and if you don't like where
it went you pick it up again. Nobody needs to be persuaded that this is direct manipulation.

Now add an assistant, built one of two ways.

The antagonistic assistant takes "put a window in the kitchen" and does it out of sight. The
better it gets, the less reason you have to open build mode at all, until the placement tool is
the thing the assistant exists to hide. When it guesses wrong you have one recourse, which is to
describe the wall more carefully. And it has thrown away the fun: The Sims is a game people play
*because* building the house with their own hands, and directing its people through pie menus in
real time, is the pleasure. An agent
that insists on doing that for you has misunderstood what the product is, and it has also cut
itself off from the best teacher it could have, which is you doing the thing while it watches.

The cooperative assistant takes the same sentence and uses the same tool, on screen. The window
appears under the cursor, slides along the wall, and you can grab it mid-drag and put it somewhere
else. The sentence was a faster way to start the gesture, not a replacement for having one. That
is what an intelligent interaction technique looks like from the user's chair: the technique is
still there, it just got better at guessing where you were going.

The Sims already worked this way in 2000, for its own agents
([demo video](https://www.youtube.com/watch?v=-exdu4ETscs)). The people know how to walk around,
but they don't know how to use the objects; the objects know how to make the people use them.
Every object advertises what it can do — "I can do this, you can do that with me" — and each
advertisement says which motives it satisfies. The pie menu is generated from those
advertisements, filtered by mood, personality and relationship, so the menu on a stranger has
"Ask to Leave" and the menu on a lover does not. When a Sim acts on its own, its autonomy scores
the same advertisements against its needs and picks from the same list; each advertisement even
carries an autonomy threshold that decides whether a Sim will choose it unprompted or only when
you tell it to. Either way the choice lands in the same action queue, visible at the top of the
screen, and you can cancel any of it with a click.

It takes an ensemble of interaction techniques, and together they amount to direct manipulation
of agent behaviour:

- **Selecting a character.** Click on a Sim, or press space to switch between them. A Sim under
  the cursor slows down, like the tilt on a pinball machine, so you can catch someone walking
  past. That is Fitts's law in time: a moving target stays under the cursor longer, which grows
  its effective size.
- **Pie menus** on people and objects, generated from the same advertisements autonomy scores.
- **The action queue** of the selected character, showing what you queued and what the Sim queued
  for itself, side by side.
- **Cancelling** any queued action with a click on it.

You don't override the agent from outside; you reach into its decision and pick for it, from the
list it was already choosing from, and you watch the result. The player and the agents have one
set of verbs, advertised by the objects, not owned by the agents. It is also much easier than
editing a YAML file by hand, which is the point of [Behind the scenes](the-state-is-a-file.md): the
repository is the floor, and this is what should stand on it.

That idea is old, and it is at the heart of MOOLLM, which borrows heavily from The Sims and
other designs that worked. In MOOLLM, objects, rooms and characters advertise what can be done
with them ([skills/advertisement/](../../skills/advertisement/)), and the LLM choosing an action
reads the same advertisements a person browsing the directory reads. Applying it to LLMs has
worked: the model gets a menu instead of a blank page, and the person gets to see the menu.

The difference between the two assistants is not the language model. It is whether the object of interest
stays in front of you, and whether the agent's hand and yours are on the same control. Any
visible control can carry a demonstration — pressing buttons and picking from menus demonstrate
fine, and neither is direct manipulation. What direct manipulation adds is a rich channel: where
you dropped the window, how you slid it, what you tried first and moved. An agent that takes the
controls away takes the demonstrations with them, and the richest ones first.

---

[Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [Same world, same hands: DreamScape, 1995](dreamscape.md)
