# Behind the scenes: the state is a file

*Part 6 of 6 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

The [classic case](the-sims.md) needs a graphical interface that already exists, and most things
agents work on have none. There is no build mode for a memorial, a consent record, or what a
character is allowed to say. MOOLLM puts that state where a person can reach it anyway: in a git
repository, as files.

This is a weaker direct-manipulation claim. Editing YAML in a text editor is editing a
representation of the object, not the object, which puts it closer to a command language than to
dragging a window along a wall. Cursor lets you type the edit, dictate it, or describe it and have
it made, which narrows the gap without closing it.

Among the ways to change an agent, though, it is the most direct. Compare them by how closely the
thing you edit maps onto the behaviour you get:

| How you change the agent                  | What you can see                               | What you can edit             | Can you undo it? |
| ----------------------------------------- | ---------------------------------------------- | ----------------------------- | ---------------- |
| Training or fine-tuning                   | loss curves and samples                        | the data, never the result    | retrain          |
| Preference tuning from thumbs up and down | nothing                                        | a vote                        | no               |
| Vendor "memory"                           | a summary, if the product shows one            | delete an entry, sometimes    | partly           |
| A hidden system prompt                    | nothing                                        | nothing                       | no               |
| An instructions box                       | the text you wrote, not the rest of the prompt | your text                     | by retyping      |
| A MOOLLM file                             | all of it, in the repo                         | all of it, one line at a time | `git revert`     |

In the first five rows you change the agent indirectly and see the effect only in its later
behaviour. In the last row the character's knowledge, refusals and consent are the text on the
screen, and changing the text changes what the agent is given. The model that reads the text is as
opaque as ever, but the definition is visible, editable and reversible.

That covers the rest of Shneiderman's list: nothing hidden, everything reversible, every change
visible as a diff. It does not replace an interface. It is what an interface should be editing
underneath, the way DreamScape's outliner and its rooms were two views of one tree, so that the
person holding the mouse and the agent holding the text are changing the same thing.

## The text is what demonstration programs

A visible, editable text of the agents, the objects and the world gives programming by
demonstration something to program. Demonstrations have always needed a target: a macro, a
script, a rule the system writes down from what it watched. Here the target is the same file the
person can already read.

That lets the flow run backwards. You type or dictate what you want, and the agent edits the text.
The original text, the proposed edit and the result are all on the screen, and you accept it,
reject it or change it by hand. Each edit shows you how the agents are programmed, in answer to
what you asked for. After enough of them you can make the next edit yourself.

So PBD can also stand for programming by dictation, and it runs both ways:

- **You to the agent.** Say or type the intention, and get back an edit you can see, judge and
  revise. Or do it by hand and let the agent watch and generalize, which is the original direction.
- **The agent to you.** It says what it did or wants to do, in text or a synthesized voice,
  pointing at the lines it changed. You can check the explanation because what it describes is on
  the screen next to it.

Dictation and demonstration differ: one states intent in words, the other shows it in action, and
each covers cases the other handles badly. They need the same condition, a representation both
parties can see and both can change. Without it, demonstration has nothing to write into, and
dictation produces changes nobody can check.

In MOOLLM the agents and objects are files. A coffeeshop is a directory. A cat is a YAML file. A
memorial is a file with citations in it. A consent record is a file that decides whether another
file may be rendered at all. Each can be opened, read, edited by hand, diffed, reverted and
searched, and each can also be edited by an LLM through chat. Both work on the same files, and
neither keeps state the other cannot see.

Shneiderman's 1983 criteria, applied to the repository:

| Criterion                                           | How the repository does it                                                                                                                                             |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Continuous representation of the object of interest | the directory listing; `PLACE.yml` is the shop's own record                                                                                                            |
| Physical action instead of syntax                   | weakest: editing a file is syntax. Dropping a photograph into `survey/` or deleting a character's directory comes closer. It is met only when an interface edits the files |
| Immediate visible feedback                          | the diff                                                                                                                                                               |
| Rapid, incremental, reversible                      | commit, revert, branch                                                                                                                                                 |
| Overview first, zoom and filter, details on demand  | `ls`, then `GLANCE.yml`, then `CARD.yml`, then `SKILL.md`                                                                                                             |

The last row was not planned. MOOLLM's reading order was designed to manage an LLM's context
window, and it ended up following "overview first, zoom and filter, then details on demand"
because the reader has the same problem: limited attention and more material than fits in it.

## When the agent holds private state

An assistant with private state cannot be inspected. You cannot open it, diff it or revert it,
and when it is wrong about you there is nothing to correct except by more conversation.

In MOOLLM the agent has no state that is not a file you can open. What the cat at the 420 Café
knows about John Sinclair is in `memorial/john-sinclair.yml`, and if the cat says something wrong,
you fix the file. What the robot budtender may say is limited by `refuses:` in its own YAML.
Whether a real person may be portrayed at all is decided by `characters/consent.yml`, which a
person wrote and can delete. These constraints are part of the objects, so they go wherever the
objects are copied.

## Agents you can copy

The objects are agents in the MOO sense: they advertise what can be done with them, hold their own
methods, and refuse things. They are also ordinary files. A coffeeshop advertises `VISIT` and
`READ-BOARD`. A cat advertises stories and refuses to speak as the dead. A place refuses to average
two coordinates. None of that needs a running process, because the LLM supplies the interpreter and
the directory supplies the state.

So you can `cp` a cat. You can `git blame` a memorial and find out who claimed what, and when. You
can hand somebody the file that defines their character, which is the principle behind the
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
a budtender's tier-4 self-authored character, and a patron's `incarnate` grant. An assistant that
keeps its state on a vendor's server has no file to hand over.

---

Previous: [The other showcase: Ebike Safari](ebike-safari.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents)
