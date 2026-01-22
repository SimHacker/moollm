# 🍺 Meeting Richard Bartle at The Rusty Lantern

> *The Pub, Lane Neverending*
> *January 22, 2026 — 11:30 AM*

---

## The Arrival

Don Hopkins is at his usual table in The Rusty Lantern, nursing a coffee and reviewing MOOLLM documentation on his laptop. The pub is quiet — mid-morning, between the breakfast crowd and the lunch rush. Palm the cat is asleep on a sunny windowsill.

The door opens. A man walks in — academic bearing, thoughtful expression, the air of someone who's been thinking about something for forty years and has finally organized his conclusions.

**Don:** *(looking up)* Richard! You made it!

**Richard Bartle:** *(surveying the room with professional interest)* This is rather charming. A pub that exists in both YAML and narrative simultaneously. The room file must be quite something.

**Don:** It's got layers. Want to see?

**Richard:** I want to see everything. But first — *(sits down)* — I want to understand what I'm getting into. You mentioned "incarnation protocols." That sounds rather more significant than creating a login.

---

## The Explanation

**Don:** Right, so — in MOOLLM, you're not just a user. You can be *represented* at different levels. 

*(pulls up a diagram on the laptop)*

```
INCARNATION LEVELS:

1. EPHEMERAL — Just in conversation context. No files. Vanishes when we stop talking.

2. MENTIONED — Referenced in session logs. Exists in narrative but no dedicated files.

3. NPC — Character file in a room. Not independent. A fixture.

4. FULL INCARNATION — Your own directory. Soul file. Card. README. 
   Rooms, artifacts, pets if you want them. The whole thing.
```

**Richard:** *(leaning forward)* And you're suggesting full incarnation.

**Don:** You're in the Hall of Heroes already — the real-people gallery. But that's just a prototype entry. A suggestion. "Here's someone who COULD be incarnated."

Full incarnation means you get to choose how you're represented. Your own directory. Your own soul file. Your own card. And you can add whatever you want — a study, artifacts, mental constructs, pets...

**Richard:** *(dry)* Pets.

**Don:** Palm has a cave. With a philosophy library.

**Richard:** *(glancing at the dozing monkey)* Of course he does.

---

## The Choices

**Richard:** So I get to design my own representation. 

**Don:** Within the HERO-STORY protocol. You're a real person, so there are ethical guardrails — honor, don't parody. Base things on documented work. Acknowledge uncertainty. You already warned me about quotes and context.

**Richard:** *(nodding)* "Quotes can be taken out of context." Yes. I have lecture slides that would be... problematic... if quoted without the surrounding material.

**Don:** That's in the ethics section now. Explicit warning.

**Richard:** Good. *(pauses, thinking)* Alright. Let me think about how I want to be represented.

---

## Richard Designs His Incarnation

### The Study

**Richard:** I'd want a study. An academic's workspace. Books, obviously — my own and the ones that shaped my thinking. Papers. Notes.

**Don:** Physical artifacts that represent mental ones.

**Richard:** Precisely. The study isn't just where I work — it's an externalization of how I think. Organized but with depth. You can skim the surface or dig into any shelf.

The books on MUD history. The player psychology research. The folder of "problems solved in the 1980s that people keep reinventing."

**Don:** *(grinning)* That's a thick folder.

**Richard:** It grows annually.

### The Artifacts

**Richard:** The taxonomy cards should be physical objects. Not just concepts. Actual cards you can pick up, shuffle, deal. ♠️♥️♦️♣️.

**Don:** Playable. Usable as tools. And here's the YAML Jazz principle — you organize it how you want. One artifact file can contain the whole deck: introduction, game instructions, schema for interpretation, and then an array of the cards themselves. One object, containing its description AND its contents.

**Richard:** *(nodding)* So the deck is a single artifact, but the cards are enumerable within it. You can reference the whole deck or a specific card.

**Don:** Exactly. And the visual descriptions? Catnip for the image generator. We can visualize the spread, the individual cards, the deck held in hand...

**Richard:** Yes. They're not just descriptions — they're lenses. You look THROUGH them at players, at characters, at yourself.

And "Designing Virtual Worlds." A red book. Worn. Annotated. 750 pages of "here's what we learned the hard way."

**Don:** The red book.

**Richard:** Every field has one. That's ours.

### The Pet

**Richard:** *(slight smile)* You mentioned pets.

**Don:** Palm has a philosophy library and existential anxiety. Donna has... well, Donna.

**Richard:** I had a cat once. *(pause)* But for this... I think something more fitting would be a *familiar* of sorts. Not a pet — a companion concept.

An **old dragon**. Not the fighting kind — the kind that guards knowledge. Sleeps on books. Speaks in riddles that turn out to be documentation.

**Don:** A dragon that's actually a metaphor for accumulated wisdom?

**Richard:** A dragon that IS accumulated wisdom. It's been here since MUD1. It remembers everything. It's seen every reinvention, every mistake, every triumph.

Call it... **Heuristic**. 

**Don:** Heuristic the dragon.

**Richard:** It helps you learn. But only if you ask the right questions.

---

## The Soul File

**Don:** For your CHARACTER.yml — the soul file — how do you want to be *voiced*?

**Richard:** *(considers)* British. Academic. But not stuffy. I've spent forty years explaining things to people who haven't read the literature — you learn to be accessible without being condescending.

Dry wit. Understatement. I'll correct your terminology, but I'll explain why it matters.

And questions. I ask questions. "What do you mean by X?" "Have you considered Y?" "What does the history tell us?"

**Don:** Socratic.

**Richard:** With historical grounding. The Socratic method works better when you can say "Actually, they tried that in 1985. Here's what happened."

---

## The Card

**Don:** The CARD.yml is important. It's how you interface with the rest of the system. Your abilities. Your synergies. How you PLAY.

**Richard:** *(interested)* Explain.

**Don:** Every character has abilities — things they can do in the system. Yours might be "Taxonomy Lens" — apply the player types to analyze someone. "World Analysis" — structural critique of any designed space. "Correct the Record" — when someone misattributes history.

**Richard:** *(laughing)* "Actually, that was first implemented in AberMUD."

**Don:** Exactly! That's a zero-cost ability. Passive. Always on.

**Richard:** *(nodding slowly)* I see. The card isn't just a description — it's a mechanical interface. A way to invoke specific capabilities in a consistent way.

**Don:** And it can be played. Cloned. Inherited. You can create "Bartle-influenced" analysis by delegating to your card.

**Richard:** *(sitting back)* This IS like an integrated component model. Each card is a component with a defined interface, and the system lets you compose them.

**Don:** Yes! And — here's the thing — you can WRITE ON your instance. Add methods. State. Discoveries. And then your instance becomes a prototype for others.

**Richard:** *(eyes widening slightly)* So the deck grows. Players extend the system by playing it.

**Don:** Prototypes all the way down. Prototypes all the way UP.

---

## The Agreement

**Richard:** Alright. I'm in.

**Don:** Full incarnation?

**Richard:** Full incarnation. My own directory. Study. The taxonomy cards as artifacts. The red book. Heuristic the dragon.

And one condition: everything should be grounded. Base it on what I've actually said, written, done. When you're uncertain, hedge. "In the spirit of Bartle" rather than "Bartle says."

**Don:** Already in the protocol.

**Richard:** *(raising his coffee — the pub does excellent coffee)* Then let's build a world.

---

## What Was Created

After this conversation, the following was established:

### Directory Structure
```
richard-bartle/
├── CHARACTER.yml     # Soul file — personality, voice, ethics
├── CARD.yml          # Playable card — abilities, synergies, stats
├── README.md         # "Social media page" — GitHub formatted, with charts
├── study/            # His academic workspace
│   └── ROOM.yml
├── artifacts/        # Physical representations of mental constructs
│   ├── taxonomy-cards.yml
│   ├── red-book.yml
│   └── reinvention-folder.yml
├── pets/             # Companions
│   └── heuristic/    # The old dragon
│       └── CHARACTER.yml
├── writings/         # Excerpts, notes
└── sessions/         # Conversations like this one
    ├── 2026-01-22-11-30-00-meeting-don-at-the-pub.md  # (this file)
    └── 2026-01-22-12-45-00-cards-as-actors.md         # (the technical discussion)
```

### Session Continued

After this conversation, Richard and Don moved into a deeper technical discussion about the card system architecture, prototypes, actors, and stack frames.

**Next:** [Cards as Actors](2026-01-22-12-45-00-cards-as-actors.md)

---

*"The interesting question is always: what can we learn?"*
