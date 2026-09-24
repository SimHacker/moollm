# Behind the scenes: the state is a file

*Part 5 of 5 of [An interface to agency, not agents instead of an interface](../INTERFACE-TO-AGENCY.md).*

The [classic case](the-sims.md) needs a graphical interface that already exists, and most things agents work on
have none. There is no build mode for a memorial, a consent record, or what a character is allowed
to say. MOOLLM's answer is to put that state where a person can reach it anyway: in a git
repository, as files.

This is the weaker direct-manipulation claim and should be made as one. Editing YAML in a text
editor is editing a representation of the object, not the object, which puts it closer to a
command language than to dragging a window along a wall. Cursor lets you type the edit, dictate
it, or describe it and have it made, and that narrows the gap without closing it.

It is still the strong claim among the ways to change an agent. Compare them by how directly the
thing you edit maps onto the behaviour you get:


| How you change the agent                  | What you can see                               | What you can edit             | Can you undo it? |
| ----------------------------------------- | ---------------------------------------------- | ----------------------------- | ---------------- |
| Training or fine-tuning                   | loss curves and samples                        | the data, never the result    | retrain          |
| Preference tuning from thumbs up and down | nothing                                        | a vote                        | no               |
| Vendor "memory"                           | a summary, if the product shows one            | delete an entry, sometimes    | partly           |
| A hidden system prompt                    | nothing                                        | nothing                       | no               |
| An instructions box                       | the text you wrote, not the rest of the prompt | your text                     | by retyping      |
| A MOOLLM file                             | all of it, in the repo                         | all of it, one line at a time | `git revert`     |


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

## The text is what demonstration programs

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


| Criterion                                           | How the repo does it                                                                                                                                                                                 |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Continuous representation of the object of interest | the directory listing; `PLACE.yml` is the shop, not a description of a record about the shop                                                                                                         |
| Physical action instead of syntax                   | the weakest row: editing a file is syntax. Dropping a photograph into `survey/` or deleting a character's directory comes closer. It is fully met only when a real interface edits the files for you |
| Immediate visible feedback                          | the diff                                                                                                                                                                                             |
| Rapid, incremental, reversible                      | commit, revert, branch. Reversibility is the substrate rather than a feature                                                                                                                         |
| Overview first, zoom and filter, details on demand  | `ls`, then `GLANCE.yml`, then `CARD.yml`, then `SKILL.md`. The semantic image pyramid is his visual information-seeking mantra with a different sensor                                               |


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

---

Previous: [The other showcase: Ebike Safari](ebike-safari.md) · [Contents](../INTERFACE-TO-AGENCY.md#contents)
