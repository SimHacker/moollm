# An interface to agency, not agents instead of an interface

At IUI in 1997 Ben Shneiderman and Pattie Maes debated direct manipulation against interface
agents. The products since have mostly gone Maes's way: assistants, recommenders, and chat windows
that stand between you and the thing you are working on. Shneiderman never argued that software
should be dumb. He argued that automation must be comprehensible, predictable and controllable,
with the object of interest continuously visible and every action rapid, incremental and
reversible.

Brad Myers restates the objection from the interaction-technique side in his 2026 proposal for
intelligent interaction techniques ([arXiv:2609.16295](https://arxiv.org/abs/2609.16295)). He
argues that graphical interfaces stay relevant after language and speech interfaces get good,
because some tasks are easier to say and others are easier to do, and Shneiderman's list tells you
which: direct manipulation earns its place when it is feasible to have "continuous representation
of the object of interest" with "rapid, incremental, reversible operations whose impact on the
object of interest is immediately visible." He proposes making the interaction techniques
themselves more intelligent while keeping what made them work.

This essay takes the same position from the programming-by-demonstration side.

*"An interface to agency" is Don's phrase, not Shneiderman's. His terms are direct manipulation,
universal usability, supertools and human-centered AI.*

## Contents

This page is the argument in brief. The six parts make it with worked examples, and each can be
read on its own.

- **[The claim](#the-claim)**, on this page. No capability reachable only by asking the agent.
  People are agents. Programming by demonstration and programming by dictation both run two ways.
1. **[The classic case: The Sims](interface-to-agency/the-sims.md).** Objects advertise what can
   be done with them. The pie menu the player picks from and the list autonomy scores are the same
   list, and both feed one visible action queue. Selecting a Sim, pie menus, the queue and
   cancelling together are direct manipulation of agent behaviour. MOOLLM borrows this design.
2. **[Same world, same hands: DreamScape, 1995](interface-to-agency/dreamscape.md).** The user's
   head and an autonomous butterfly in one world with the same tools, and agency composed across a
   structure you can take apart. The butterfly could not edit the map. MOOLLM closes that gap.
3. **[The showcase: a Sim goes to work in another game](interface-to-agency/the-errand.md).** An
   agent working across closed programs through nothing but the screen, the mouse and the
   keyboard. A Sim in an unmodified copy of The Sims 1 takes a job as mayor in Micropolis, and
   comes home when someone picks from the pie menu of a painted Easter egg.
4. **[Screen Angel: the layer doing the clicking](interface-to-agency/screen-angel.md).** What the
   layer may do, how it sees a game with no API, why it has no privileged verb, what is built and
   what is not, the hard part, and the four properties that make it direct manipulation.
5. **[The other showcase: Ebike Safari](interface-to-agency/ebike-safari.md).** No agent can
   pedal, so everything the system does starts from what the rider already did. The city is the
   object of interest, a ride cannot be undone but its interpretation can, and the bike's two
   outputs, assist and a suggested heading, are where software could still steer.
6. **[Behind the scenes: the state is a file](interface-to-agency/the-state-is-a-file.md).** A
   weaker direct-manipulation claim. Agents defined in visible, revertible files, compared with
   training, vendor memory and hidden prompts. The text is what demonstration and dictation
   program.
- **[Chat is a second manipulator](#chat-is-a-second-manipulator-not-the-interface)**,
  **[What *Watch What I Do* already found](#what-watch-what-i-do-already-found)** and
  **[Where this sits](#where-this-sits)**, on this page.

## The claim

**Anything an agent can do, a person should be able to do through an interface, and no
capability should be reachable only by asking the agent.** The agent may bring more attention,
memory and bandwidth to a task. It may not have a different set of verbs.

People want agency. An agent is one way to package it, and a good interface is still required
either way.

**People are agents.** The interface should not care which kind is holding the pen. In
[The Sims](interface-to-agency/the-sims.md) the people are objects that advertise interactions to
each other, and the player is one more chooser in the same loop. In
[DreamScape](interface-to-agency/dreamscape.md) the user's head and the butterfly are both things
in the room. In PIXIE the demo's light pen and yours go into the same channel. In MOOLLM a character is a
file whether it is played by a person, by an LLM, or by both at different times.

**Programming by demonstration is a two-way street, and so is programming by dictation.** Most of
the systems collected in *Watch What I Do* (Allen Cypher, ed., 1993, with chapters by Henry
Lieberman, Brad Myers and others) ran one way: the person demonstrates, the system watches and
generalizes. With a shared interface it runs both ways.


|                   | Person to agent                                      | Agent to person                                                              |
| ----------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Demonstration** | you do it by hand; the agent watches and generalizes | the agent does it through the same visible controls; you watch and learn how |
| **Dictation**     | you say what you want; the agent proposes the edit   | the agent says what it did or wants to do, pointing at what changed          |


All four need the same condition: one interface that both parties can see and operate. Hide the
controls and demonstration stops in both directions; dictation survives only as requests going
in and reports coming out, with nothing on screen to check either against.

The agent-to-person demonstration has a working example you can click. PIXIE, Heinz Lemke's
light-pen radial menus, runs in a PDP-7 emulator in the browser
([pixie-live](https://hyperties.org/databases/pixie/pixie-live/)). Its **Demo** button plays
virtual light-pen input into the emulator: the same channel a person's pen would use, driving
the same program, on the same display. You watch the menus being used, then pick up the pen and
use them yourself.

## Chat is a second manipulator, not the interface

Myers's split applies to language as well. The chat channel is one of two ways in, and it is
strongest where direct manipulation is weakest: many objects at once, underspecified intent, and
work that needs judgment about wording. Placing two hundred windows by hand is tedious; asking for
a window on every south wall is easy. Nudging one window one tile left is quicker by hand.

The rule is that the chat channel may only do things that show up in the object: on screen as the
controls moving, or on disk as a diff. No hidden memory, no learned preferences, no state kept in
the assistant.

## What *Watch What I Do* already found

Most of the problems agent designers face now were written down in 1993. Brad Myers's chapter,
["Demonstrational Interfaces: A Step Beyond Direct Manipulation"](http://acypher.com/wwid/Chapters/26Demonstrational.html),
separates systems that infer from systems that do not: "a system that guesses can propose an
incorrect action even when the user makes no mistakes." By that test every LLM agent is an
inferencing system, and his list of their problems is still the list: feedback, undo,
predictability, and procedures that are wrong without anyone noticing.

He also records the argument this essay opens with, six years before IUI. On a CHI '91 panel
Shneiderman said, "If the computer performs complex inferences then the users lose control,
predictability can vanish, and the risk of uncertainty increases." Myers's answer in the chapter is
that proper attention to feedback can overcome those problems. This essay takes both positions:
inference is allowed, and the feedback is the shared interface itself. The agent's guess appears as
an action in the same controls, queued where it can be seen and cancelled.

His chapter already has the evidence for that:

- Eager, Cypher's HyperCard system, usually guessed the loop correctly, but "users were nervous to
  let the system go ahead and do the rest of the iterations," because the stopping criterion was
  not visible. The Sims queue shows what an agent will do next and lets you cancel it
  ([Part 1](interface-to-agency/the-sims.md)).
- Question-and-answer feedback fails in a known way: "Users tend to answer every question with
  'yes' (perhaps assuming that the computer knows best)." A confirm-each setting is not enough by
  itself; the pending work has to be an object you can inspect
  ([Part 4](interface-to-agency/screen-angel.md)).
- Replaying a procedure that has "potentially damaging side effects (such as deleting files)"
  cannot be naive: "some of the operations will have to be simulated or not carried out." That is
  the case for running agents on copies of state ([Part 6](interface-to-agency/the-state-is-a-file.md))
  and for leaving irreversible acts with the person ([Part 5](interface-to-agency/ebike-safari.md)).
- Among future applications he proposed a "character video game construction kit," with behaviours
  defined by demonstration. The Sims shipped seven years later with behaviours attached to objects
  instead, which is the design [Part 1](interface-to-agency/the-sims.md) describes.

Two other chapters bear on [Screen Angel](interface-to-agency/screen-angel.md). Richard Potter's
["Just-in-time Programming"](http://acypher.com/wwid/Chapters/27JITP.html) names five obstacles to
automating a task while doing it, starting with inaccessible data and operators and ending with
risk; his Triggers attacked the first by reading pixels. David Kosbie and Myers's
["A System-Wide Macro Facility Based on Aggregate Events"](http://acypher.com/wwid/Chapters/22Aggregate.html)
argues that a macro recorder working across applications has to keep the nesting of the user's
tasks, or undo and replay act at the wrong level.

## Where this sits

- [DIRECTORY-AS-IUNKNOWN.md](./DIRECTORY-AS-IUNKNOWN.md) — the mechanism: a directory as an interface-bearing object
- [skills/design-sense/masters/ben-shneiderman.md](../skills/design-sense/masters/ben-shneiderman.md) — his votes and vetoes as a loadable head
- Brad Myers, intelligent interaction techniques proposal, [arXiv:2609.16295](https://arxiv.org/abs/2609.16295) (2026), and *Pick, Click, Flick! The Story of Interaction Techniques* ([ixtbook.com](https://www.ixtbook.com)) — the same settlement argued from inside the interaction technique
- Allen Cypher (ed.), *Watch What I Do: Programming by Demonstration*, MIT Press, 1993, full text at [acypher.com/wwid](http://acypher.com/wwid/) — the book the two-way-street claim extends
- [skills/design-sense/lenses/direct-manipulation.md](../skills/design-sense/lenses/direct-manipulation.md) — the lens
- [skills/cursor-mirror/characters/i-beam/CONSTITUTION.md](../skills/cursor-mirror/characters/i-beam/CONSTITUTION.md) — the anti-Clippy constitution, which is this argument applied to one character
- [skills/representation-ethics/](../skills/representation-ethics/) — consent records as files
- [wwsff `characters/ben-shneiderman/agents-debate-1997.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-shneiderman/agents-debate-1997.md) — notes on the 1997 debate
