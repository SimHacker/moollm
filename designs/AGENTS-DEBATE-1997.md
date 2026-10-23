# The 1997 agents debate: what was argued, who made it possible, and the two answers in reach

In 1997 Ben Shneiderman and Pattie Maes debated "Direct Manipulation vs. Interface Agents," first
at IUI 97 and then at CHI 97. It is cited as the founding dichotomy of interface design, and it is
live again now that LLM agents are shipping. This is a reading of the published record: what each of
them argued, the people around them who shaped the session, and two lines of work from the same
years that answered the question a member of the audience asked from the floor.

Every quotation is from the published transcript or a cited publication, in context. Corrections
from anyone named here are welcome; see [Sources](#sources).

**Primary source:** Ben Shneiderman and Pattie Maes, "Direct Manipulation vs. Interface Agents,"
*interactions* 4(6), Nov/Dec 1997, pp. 42–61,
[doi:10.1145/267505.267514](https://doi.org/10.1145/267505.267514).

## Contents

- [Two events, and how the IUI session ended](#two-events-and-how-the-iui-session-ended)
- [Ben Shneiderman's position](#ben-shneidermans-position)
- [Pattie Maes's position](#pattie-maess-position)
- [The people who shaped the session](#the-people-who-shaped-the-session)
- [The question from the floor](#the-question-from-the-floor)
- [First answer: Ted Selker's COACH](#first-answer-ted-selkers-coach)
- [Second answer: programming by demonstration](#second-answer-programming-by-demonstration)
- [Why it is live now](#why-it-is-live-now)
- [Open questions](#open-questions)
- [Sources](#sources)

## Two events, and how the IUI session ended

| Event | When | Moderator | Record |
|---|---|---|---|
| IUI 97, Orlando | January 6–9, 1997 | Jim Alty, Loughborough University | Full transcript, published in *interactions* |
| CHI 97, Atlanta | March 22–27, 1997 | Jim Miller, Apple Research Laboratories | Two-page extended abstract in *CHI 97 Extended Abstracts* |

Most citations to "the debate" are to the IUI session, because it is the one with a transcript.

That session ended with the two of them finding common ground:

> **Ben:** I like the new Pattie. I am ready to be partners and collaborate with the new Pattie.
>
> **Pattie:** I think we both have changed. Would you agree to that or not?
>
> **Jim:** I think before they start kissing let's move on.

Earlier, Shneiderman had said: "part of me is drawn to the idea of celebrating Pattie Maes and
encouraging you to follow her example." The debate is remembered as an opposition. The transcript
records two researchers narrowing their differences in public, generously.

## Ben Shneiderman's position

Shneiderman coined "direct manipulation" ("Direct Manipulation: A Step Beyond Programming
Languages," *IEEE Computer* 16(8), 1983) and founded the Human-Computer Interaction Lab at the
University of Maryland. His position in 1997 was not opposition to automation. He stated it
directly:

> I am in favor of increased automation that amplifies the productivity of users and gives them
> increased capabilities in carrying out their tasks, while preserving their sense of control and
> their responsibility, responsibility, responsibility.

His concern was that certain words lead designers to skip work:

> I have trouble with the words like "agents," and "expert," and "smart," and "intelligent" because
> they mislead the designer, and designers wind up leaving out important things.

He argued that "the intelligent agent notion limits the imagination of the designer, and it avoids
dealing with interface issues."

Three moves in the transcript show how close his position was to hers:

- **He quoted her own principle, approvingly:** "Make the user model available to the user… I
  don't see that being done in most of the work about agents." His complaint was that the field
  wasn't yet meeting her standard.
- **He cited Tom Sheridan** on supervisory control in nuclear control rooms and cockpits, the
  literature on how people and automation share control when the stakes are high.
- **He described a shared architecture:** "Maybe the way agents will mature is as Pattie is
  suggesting; that the agents take care of the processes below the table, and there is a nice direct
  manipulation interface that the user sees."

He also named the gap he most wanted filled:

> It is embarrassing that after 15 years of graphic user interface being widely available, we have
> no graphical macros tools. What is going on? This is the greatest opportunity for visual
> programming.

His later work carries the same thread, most fully in *Human-Centered AI* (Oxford University Press,
2022): high levels of automation together with high levels of human control.

## Pattie Maes's position

Maes, at the MIT Media Lab, had set out the case for learning interface agents in "Agents that
Reduce Work and Information Overload" (*CACM* 37(7), 1994,
[doi:10.1145/176789.176792](https://doi.org/10.1145/176789.176792)). Her argument was that the
complexity of what people want to do outgrows what buttons and sliders can express, and that people
who are not trained in computing need help delegating. She framed agents as an addition to good
interfaces, not a substitute for them:

> this is completely a complementary technique to well-designed interfaces — visualization, and
> direct manipulation — not a replacement. Users still need to be able to bypass the agent.

She agreed that agent designers have to attend to interface issues "such as understanding and
control," or people will not trust the result.

She was also careful about where agents should be used. She chose domains where a mistake costs
little, and said why:

> If your World Wide Web agent gives you a wrong Web page to look at… that is not at all critical. It
> is not a big deal… I believe that it will be very hard to make agents that always come up with the
> right answer, always do the right thing.

That calibration has aged well. In 2026 agents are routinely given code, money and email, where
mistakes are expensive and compound.

Her own list of requirements for agent interfaces, slide 13 of her January 1997 deck, "Agent UI
solutions," reads as a design program: make the user model available to the user; make the method
of operation understandable; make explanations available; prefer gradual approaches; give
continuous feedback about the agent's state, actions and learning; allow variable degrees of
autonomy, decided by the user; allow the user to program the agent (teach and forget); and use the
language of the application rather than making the user learn a new one. She showed the slide again
in a talk in October 2026. A bullet-by-bullet reading is in
[Your slide 13](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/pattie-maes/agent-ui-solutions.md).

## The people who shaped the session

- **Angel Puerta**, an organizer of IUI 97, made the debate possible. Shneiderman opened by thanking
  the organizers "for daring to arrange this debate," and said: "It was Angel Puerta's careful
  attention to my concerns that made me feel comfortable in coming to speak here." He gave Puerta a
  lab T-shirt.
- **Jim Alty** moderated with a light hand, opening "I think I am supposed to be the moderator,
  whatever that means," and closing the convergence with the line quoted above. He let the two of
  them find their own way to agreement.
- **Jim Miller** of Apple Research Laboratories moderated the CHI 97 session.
- **Tom Sheridan**, whose *Telerobotics, Automation, and Human Supervisory Control* (MIT Press,
  1992) is the standard work on shared human–machine control, was cited by Shneiderman as the
  authority for high-stakes automation.
- **Alan Wexelblat** of the Media Lab appears in a sidebar Shneiderman wrote for the *interactions*
  article. At CHI 97, Maes had suggested that Shneiderman's autofocus camera was itself a kind of
  agent. Wexelblat photographed the session with that camera, aimed at the stage, and the camera
  focused on the poster behind it. Shneiderman: "We can all find this amusing and leave it at that,
  but I think there is a serious point which is that agents don't always do what we expect them to
  do, and it takes some knowledge to make effective use of agents (or auto-focus cameras)." He took
  part of the responsibility himself, for not explaining the camera.
- **The audience** asked the sharpest questions. One questioner argued that people anthropomorphize
  talking computers whether designers intend it or not, citing "research at Stanford recently,"
  most likely Byron Reeves and Clifford Nass's work published as *The Media Equation* (1996). The
  transcript labels floor speakers only as "Question," so their names are not in the record.

## The question from the floor

Another questioner asked for a synthesis:

> Will this debate between direct manipulation and agency always exist in interface design or will it
> eventually be replaced by some kind of fusion of the two approaches? In other words, are we going
> to see new Bens and new Patties every day, or is there going to be some kind of "Shneider-Maes"?

The discussion moved on to how the debate itself would develop. Two bodies of work from the same
years answer the question.

## First answer: Ted Selker's COACH

Ted Selker's COACH (Cognitive Adaptive Computer Help), built at IBM Almaden, watched a learner work
and offered adaptive, context-sensitive help ("COACH: A Teaching Agent that Learns," *CACM* 37(7),
1994, [doi:10.1145/176789.176799](https://doi.org/10.1145/176789.176799), the same issue as Maes's
paper). It was proactive and adaptive,
as Maes asked, while advising rather than acting on the user's behalf, never blocking, and always
bypassable, as Shneiderman asked. Selker evaluated it against a control with the same interface and
the same material, minus the proactive help.

In "A Conversation with Ted Selker" (*interactions* 4(5), Sept/Oct 1997, the issue before the
debate transcript), he described the result:

> So this really, I think, is the center of the Ben Shneiderman and Pattie Maes debate because, you
> know, he says it could never happen and she says it will happen someday. I've got some data that
> shows that actually I can have something that's doing something proactively without being asked to
> and actually improves people's perception, a feeling of control, and their ability to get it done.

## Second answer: programming by demonstration

Shneiderman's "graphical macros tools" are what programming by demonstration builds: the user
performs a task by direct manipulation, and the system generalizes it into a program. The field's
anthology had appeared four years earlier: *Watch What I Do: Programming by Demonstration*, edited
by Allen Cypher with Daniel Halbert, David Kurlander, Henry Lieberman, David Maulsby, Brad Myers and
Alan Turransky (MIT Press, 1993; foreword by Alan Kay), with the full text online at
[acypher.com/wwid](http://acypher.com/wwid/).

It meets both sets of requirements:

- **Maes's:** Cypher's Eager, built on HyperCard at Apple, ran in the background and noticed
  repetitive patterns by itself ("EAGER: Programming Repetitive Tasks by Example," CHI '91,
  [doi:10.1145/108844.108850](https://doi.org/10.1145/108844.108850)).
- **Shneiderman's:** the user demonstrates on visible objects and their own data, and the system
  shows what it inferred before it acts. Eager highlighted the button, menu item or text it predicted
  next in green, and corrected itself from what the user actually did. That is "make the user model
  available to the user," implemented directly in the interface.

The connection was made in the room. Answering a question, Maes said: "Henry Lieberman, sitting
here in the audience, did some interesting work where he taught an agent" by demonstration, using
speech as a second channel to clarify intent. Lieberman was one of the anthology's editors, and
later edited *Your Wish Is My Command: Programming by Example* (Morgan Kaufmann, 2001). Four years
earlier he had given the opening talk, "Smart Interfaces to Smart Machines," at Selker's first New
Paradigms for Using Computers workshop at IBM Almaden in 1993
([archived program](https://web.archive.org/web/20060210092923/http://www.almaden.ibm.com/almaden/npuc97/1993.htm)),
which connects the two answers through one person.

There are good reasons the category wasn't named from the stage. Lieberman's work was cited as an
example in Maes's answer, which is a different role from proposing a synthesis. Programming by
demonstration was its own community, with its own vocabulary of intent inference and
generalization, rather than a party to the debate. And in 1997 it was still research: the hard
problem, inferring which generalization a person means from one or two examples, was unsolved, and
Shneiderman's complaint was about tools people could actually use.

## Why it is live now

Both answers depended on inferring intent from very little evidence, and that is exactly what large
language models changed. Allen Cypher has written on his homepage that "with the advent of Large
Language Models, my dream of End User Programming has come true," and that vibe coding exceeds what
he had imagined.

The question the 1997 record raises is whether it came true in the form both debaters asked for.
Programming by demonstration had the user show the system what to do and see what it inferred.
Much of today's agent tooling takes instructions in natural language and produces results the user
cannot easily inspect before they take effect. Measured against the 1997 requirements, that meets
Maes's call for capable delegation more fully than Shneiderman's call for comprehensibility,
predictability and control. Her slide 13 asks for both, and so did he.

[An interface to agency](INTERFACE-TO-AGENCY.md) takes up that question: anything an agent can do,
a person should be able to do through the same interface, with programming by demonstration and by
dictation running in both directions.

## Open questions

These are gaps in the record that the people involved could fill:

- **Who the floor speakers were.** The transcript names them only as "Question."
- **Whether the two answers met.** Cypher and Selker were both at IBM Almaden at points in their
  careers. Whether their work crossed is not established here.
- **The later debates** at CHI 2017 and CHI 2021 are not covered here.
- **Other records of IUI 97**, such as slides or recordings, beyond the *interactions* transcript.

## Sources

- Shneiderman, B. & Maes, P. "Direct Manipulation vs. Interface Agents." *interactions* 4(6), 1997, 42–61. [doi:10.1145/267505.267514](https://doi.org/10.1145/267505.267514)
- Maes, P., Shneiderman, B. & Miller, J. "Intelligent Software Agents vs. User-Controlled Direct Manipulation: A Debate." *CHI 97 Extended Abstracts*, 1997.
- Shneiderman, B. "Direct Manipulation: A Step Beyond Programming Languages." *IEEE Computer* 16(8), 1983.
- Shneiderman, B. *Human-Centered AI.* Oxford University Press, 2022.
- Maes, P. "Agents that Reduce Work and Information Overload." *CACM* 37(7), 1994, 30–40. [doi:10.1145/176789.176792](https://doi.org/10.1145/176789.176792)
- Selker, T. "COACH: A Teaching Agent that Learns." *CACM* 37(7), 1994, 92–99. [doi:10.1145/176789.176799](https://doi.org/10.1145/176789.176799)
- "A Conversation with Ted Selker." *interactions* 4(5), 1997.
- Cypher, A. "EAGER: Programming Repetitive Tasks by Example." CHI '91. [doi:10.1145/108844.108850](https://doi.org/10.1145/108844.108850)
- Cypher, A. (ed.) *Watch What I Do: Programming by Demonstration.* MIT Press, 1993. [Full text](http://acypher.com/wwid/)
- Lieberman, H. (ed.) *Your Wish Is My Command: Programming by Example.* Morgan Kaufmann, 2001.
- Sheridan, T. B. *Telerobotics, Automation, and Human Supervisory Control.* MIT Press, 1992.
- Reeves, B. & Nass, C. *The Media Equation.* CSLI Publications / Cambridge University Press, 1996.
- IBM Almaden, First Annual NPUC program, 1993. [Archived](https://web.archive.org/web/20060210092923/http://www.almaden.ibm.com/almaden/npuc97/1993.htm)

## Related

- [INTERFACE-TO-AGENCY.md](INTERFACE-TO-AGENCY.md) — the design argument this history supports
- [AXES-NOT-CAMPS.md](AXES-NOT-CAMPS.md) — why the dichotomy outlived its resolution
- [skills/design-sense/masters/ben-shneiderman.md](../skills/design-sense/masters/ben-shneiderman.md) — his design principles as a loadable lens
- People portrayed in Will Wright Show For Food, with invitations to talk:
  [Pattie Maes](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/pattie-maes/README.md) ·
  [Ben Shneiderman](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-shneiderman/README.md) ·
  [Henry Lieberman](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/henry-lieberman/README.md) ·
  [Ted Selker](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-selker/README.md) ·
  [Brad Myers](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/brad-myers/README.md)
