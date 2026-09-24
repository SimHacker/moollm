# The classic case: The Sims

*Part 1 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

The argument is easiest to make where direct manipulation is least arguable. In The Sims you put
a window in a wall by picking the window up and moving it along the wall. The window is visible
the whole time, the game shows you whether it fits before you let go, and if you don't like where
it went you pick it up again.

Now add an assistant, built one of two ways.

The first assistant takes "put a window in the kitchen" and does it out of sight. The better it
gets, the less often you open build mode. When it guesses wrong, your only recourse is to describe
the wall more carefully. It also takes away what people play the game for, which is building the
house and directing its people through pie menus themselves. And it never sees you do the task,
so it has nothing to learn from.

The second assistant takes the same sentence and uses the same tool, on screen. The window appears
under the cursor and slides along the wall, and you can grab it mid-drag and put it somewhere else.
The sentence starts the gesture instead of replacing it. This is Myers's case: the technique is
still there, and it has become better at guessing where you were going.

The Sims already worked this way in 2000, for its own agents
([demo video](https://www.youtube.com/watch?v=-exdu4ETscs)). The people know how to walk around,
but they don't know how to use the objects; the objects know how to make the people use them.
Every object advertises what it can do — "I can do this, you can do that with me" — and each
advertisement says which motives it satisfies. The pie menu is generated from those
advertisements, filtered by mood, personality and relationship, so the menu on a stranger has
"Ask to Leave" and the menu on a lover does not. When a Sim acts on its own, its autonomy scores
the same advertisements against its needs and picks from the same list; each advertisement also
carries an autonomy threshold that decides whether a Sim will choose it unprompted or only when
you tell it to. Either way the choice lands in the same action queue, visible at the top of the
screen, and you can cancel any of it with a click.

Several interaction techniques together make this direct manipulation of agent behaviour:

- **Selecting a character.** Click on a Sim, or press space to switch between them. A Sim under
  the cursor slows down, like the tilt on a pinball machine, so you can catch someone walking
  past. That is Fitts's law in time: a moving target stays under the cursor longer, which grows
  its effective size.
- **Pie menus** on people and objects, generated from the same advertisements autonomy scores.
- **The action queue** of the selected character, showing what you queued and what the Sim queued
  for itself, side by side.
- **Cancelling** any queued action with a click on it.

You pick for the Sim from the list it was already choosing from, and you watch the result. The
player and the Sims share one set of verbs, and the objects supply them. This is also much easier
than editing a YAML file by hand. MOOLLM keeps agent state in files
([Behind the scenes](the-state-is-a-file.md)), and an interface like this one belongs on top of
them.

MOOLLM borrows this design from The Sims. Objects, rooms and characters advertise what can be done
with them ([skills/advertisement/](../../skills/advertisement/)), and the LLM choosing an action
reads the same advertisements a person browsing the directory reads. It has worked well with
LLMs: the model gets a menu instead of a blank page, and the person can see the menu.

What separates the two assistants is whether the object of interest stays in front of you, and
whether the agent's hand and yours are on the same control. Any visible control can carry a
demonstration; pressing buttons and picking from menus demonstrate fine, and neither is direct
manipulation. Direct manipulation carries more: where you dropped the window, how you slid it,
what you tried first and moved. An assistant that hides the controls also stops receiving those
demonstrations.

---

[Contents](../INTERFACE-TO-AGENCY.md#contents) · Next: [Same world, same hands: DreamScape, 1995](dreamscape.md)
