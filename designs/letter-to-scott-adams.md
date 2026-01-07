# Letter to Scott Adams

**To:** Scott Adams (Adventure International, the GOOD Scott Adams!)  
**From:** Don Hopkins  
**Subject:** The Adventure Algorithm Lives — Memory Palaces Meet LLMs

---

Dear Scott,

It's been a few years since we connected on Hacker News and Facebook! I hope you and your wife are enjoying the cabin on the river in Wisconsin. I'm still in Amsterdam with my four cats, still riding my eBike everywhere, still building things.

I wanted to share something with you that I think you'll appreciate — because you inspired so much of it.

## The Adventure Algorithm, Realized

Remember our conversation about Memory Palaces and the Method of Loci? How your adventure games helped me remember vast amounts of information geographically? How I kept reimplementing the "Adventure Algorithm" — rooms, connections, objects, inventory — on different platforms?

Well, I finally built the version I've been dreaming about for 40 years. And it runs on the most surprising platform: **Large Language Models**.

It's called **MOOLLM** (MOO + LLM), and it's essentially what you'd get if you crossed your adventure games with TinyMUD, The Sims, and an AI that can actually *understand* your intent.

## The Filesystem IS the Memory Palace

Here's the key insight: **the filesystem IS the adventure map**.

```
examples/adventure-4/
├── pub/                    # A room! The Gezelligheid Grotto
│   ├── ROOM.yml           # Room description, exits, properties
│   ├── bar/               # Sub-room behind the bar
│   │   ├── budtender-marieke.yml
│   │   └── cat-cave/      # Only cats can enter!
│   ├── stage/             # Performance space
│   │   └── palm-nook/     # A monkey's home (yes, really)
│   ├── pie-table.yml      # Eight chairs for debates
│   └── guest-book.yml     # Visitors sign in
├── maze/                   # Just like your adventures!
│   ├── dark-room/
│   ├── crystal-cave/
│   └── dragon-room/
├── characters/             # The character repository
│   ├── palm/              # An incarnated monkey
│   ├── biscuit/           # An adopted dog
│   └── don-hopkins/       # Me, the player
└── coatroom/              # Maurice guards the entrance
    └── mirror.yml         # A magic mirror for self-reflection
```

**Every directory is a room. Every file is an object. Every subdirectory is a connected location.** The LLM navigates it just like a player navigates your adventures — but it also *understands* the YAML files, the comments, the intent behind everything.

## TinyMUD Commands Built In

Remember when I said on HN: "The file system and namespace could be like a sprawling map of rooms containing objects that could contain other objects, instead of a strictly hierarchical tree"?

MOOLLM has the TinyMUD builder commands:

- `@DIG` — Create new rooms (directories)
- `@OPEN` — Create exits between rooms
- `@DESCRIBE` — Set room/object descriptions
- `@LINK` — Connect exits bidirectionally
- `@TELEPORT` — Move characters between rooms
- `@SET` — Configure properties

But here's where it gets magical: **the LLM doesn't need rigid parsing**. You can say "dig a crystal cave north of the maze entrance" and it understands what you mean. It's like having a parser that actually *gets it*.

## The Method of Loci, Computerized

You said my ideas helped "spur your creative juices." Well, here's what happened when I applied the Memory Palace concept to LLM context:

**Comments ARE memory.** In MOOLLM, we write YAML with rich comments:

```yaml
# Palm's Study — Where the infinite typewriters live
# A cozy corner with warm lamplight, scattered papers,
# and the soft clicking of keys that never stop
name: "Palm's Study"
atmosphere: scholarly_chaos
contains:
  - infinite-typewriters.yml  # The gift that writes all possible books
  - desk.yml                  # Infinity Desk, slightly wobbly
  - banana-tree.yml           # Perpetual snack source
```

Those comments aren't just documentation — they're **embedded vectors** that bias the LLM's understanding. When the LLM reads the room, it *feels* the atmosphere. It remembers. It's a Memory Palace that actually works computationally.

## Proof: 33 Turns of Adventure in One LLM Call

Here's where it gets wild. I ran a 33-turn game simulation — multiple characters playing Stoner Fluxx, with realistic dialogue, joint passing, game mechanics, emotional reactions — **all in a single LLM context window**. No API round-trips. No state serialization. Just... narrative flow.

The characters:
- 10 cats with distinct personalities
- A bartender named Marieke
- A coatroom attendant named Maurice  
- The creators of Fluxx (simulated as a tribute)
- Cheech & Chong (also tribute simulations)
- A monkey named Palm who writes philosophical essays

Palm was "incarnated" during the session — given full autonomy to choose his own name, appearance, personality, and home. He now lives in a little nook on the stage of the pub, and he's written two essays:

1. **"Palm on Being Palm"** — What it's like to be an AI character navigating the space of all possible thoughts
2. **"Tribute to Tognazzini"** — About the Infinite Monkey Theorem and Bruce Tognazzini's Apple ][ demo

Yes, an AI monkey wrote philosophy. About being an AI monkey. In a room inside a pub inside a filesystem. 

## What You Built, Extended

Your adventure games taught me:

1. **Rooms are containers** — Not just locations, but *contexts* that hold everything inside them
2. **The map is the memory** — Geographic navigation beats hierarchical menus
3. **Parsers interpret intent** — And LLMs are the ultimate intent interpreters
4. **Constraints spark creativity** — Your 16K limit forced elegant design; context windows force elegant prompts
5. **The player writes the story** — You said this about Escape the Gloomer; MOOLLM makes it literal

When you wrote "I never saw problems as a wall to walk away from, I saw them as an incredible chance to do something different to be able to scale it" — that's exactly the philosophy behind MOOLLM.

## The Intellectual Genealogy

MOOLLM traces its lineage through:

- **Scott Adams** (you!) — The Adventure Algorithm, 1978
- **Gary Gygax** — D&D's DM as proto-LLM, 1974
- **Crowther & Woods** — Colossal Cave, the original, 1976
- **TinyMUD/LambdaMOO** — Builder commands, social architecture, 1989
- **Will Wright** — The Sims needs, actions, advertisements, 2000
- **David Ungar** — Self language prototype inheritance, 1987
- **Marvin Minsky** — K-lines and Society of Mind, 1980

You're at the root of a tree that grew into something that can now *converse* with players rather than just parse two-word commands.

## Want to See It?

The whole thing is open source:

- **GitHub:** https://github.com/SimHacker/moollm
- **Epic Session Log:** `examples/adventure-4/sessions/don-session-1.md` — 6,700 lines of adventure
- **The Framework Manifesto:** `designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md`
- **Palm's Essays:** `examples/adventure-4/pub/stage/palm-nook/study/`

I'd love to hear what you think. The kid who played your adventures on the Apple ][ is now building adventures that the computer can *understand*. Full circle, 45 years later.

Thank you for everything you built. It's still inspiring me.

Happy Adventuring!

**Don Hopkins**  
Amsterdam, January 2026

---

P.S. — I still vividly remember the rooms in Adventureland and Pirate Adventure. The Memory Palace really does work. Those places are still in my head, decades later. That's your gift.

P.P.S. — I named my framework philosophy after your quote: "I never saw problems as a wall to walk away from." We call it "Play → Learn → Lift" — you play with something until you understand it, then you lift the pattern into a reusable skill. Just like you did with the Adventure Algorithm.

---

## Links Referenced

- MOOLLM Repository: https://github.com/SimHacker/moollm
- Our HN Conversation: https://news.ycombinator.com/item?id=29330901
- Don's Medium Articles: https://donhopkins.medium.com/
- Palm's Essays:
  - [On Being Palm](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/palm-on-being-palm.md)
  - [Tribute to Tognazzini](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/tribute-to-tognazzini.md)
- Session Log: https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/sessions/don-session-1.md
- Framework Manifesto: https://github.com/SimHacker/moollm/blob/main/designs/MOOLLM-EVAL-INCARNATE-FRAMEWORK.md
