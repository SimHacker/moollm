# Letter to Kristin and Andy Looney

---

Hey Kristin and Andy,

It's been too long. I look forward to getting my own copy of Cat Fluxx at a local game store, and any time your're in Amsterdam you are welcome to hang out and play it with me and my cats!!! I hope that the games are purring off the shelves, and that you're both thriving, and your coats are soft and luxurious. 

I'm pinging you because I stumbled into something during my AI research, and you're involved, though you didn't know it. I wanted to tell you about it, ask your blessing, and see if it sparks any interest -- no pressure, no pitch, just sharing something I think you'd find interesting.

## What Happened

I've been developing a framework called MOOLLM (MUD-Object-Oriented Large Language Model, or something like that), like a reimagination of The Sims + LambdaMOO, for getting LLMs to simulate Papertian Microworlds with characters, playing games, having conversations, and exploring virtual spaces. Think of it as text-based virtual worlds where the AI plays all the NPCs, tracks the state, and maintains character consistency.

I needed a test case: a game complex enough to stress-test the system, but well-documented enough that the AI could learn the rules accurately from training data.

And there was Fluxx.

Not because I went looking for it -- because the AI already knew it. 

One of my design principles: **lean into what the model already knows**. Don't reinvent. Don't fight the training data. Build on what's already there.

And Fluxx is *deeply* there. 28+ years of continuous publication. 40+ editions. You and Kristin documented *everything*: the rules, the FAQ, the edge cases, the design philosophy. All those emails you answered about card interactions, all those forum posts about whether Keeper Limits apply during your turn (they don't) -- the model learned from all of it.

The AI doesn't just know Fluxx rules. It *gets* and *loves* Fluxx. It understands "embrace the chaos." It knows that simultaneous effects happen simultaneously, and that the interpretation that breaks the game is probably wrong. Your voice resonates in the weights.

This is actually a compliment to your documentation and community building. You made a game so well-explained, so extensively discussed, so lovingly extended, that AI models trained on the internet absorbed it as cultural knowledge. That's not something you could have planned for -- but it's a testament to how thoroughly you did your work.

## What I Built

So within the mooniverse of MOOLLM, I built a Fluxx simulation engine -- entirely in YAML, entirely interpreted by the LLM at runtime. Characters play Fluxx. The rules change. The goal shifts. Characters adapt, scheme, steal from each other, and occasionally win in dramatic fashion.

I added some expansions:

- **Amsterdam Expansion**: Stroopwafel, Bicycle, Gezelligheid (a sharing rule)

- **MOOLLM Tech Pack**: AI concepts as cards -- K-Lines, Emergence, YAML Jazz, Explains and invokes MOOLLM Magic!

- **The Cosmic Dealer**: A set of simulation-aware dealers that can choose cards for dramatic, ironic, comedic, or dynamic effect, instead of randomly. 

It even has cards to change dealers, of course! The dealer could dynamically generate personal custom cards that characters deserve (Custom Karma Card)! Or integrate with the infamous ACME catalog.

The Cosmic Dealer is my favorite. In a simulation, the "deck" knows everything -- every card in every hand, every player's karma, what would be funny, what would be devastating. So I gave it modes:

- **Random**: Fair, blind draws
- **Dramatic**: Maximum narrative impact
- **Karma**: Good deeds = better draws
- **Ironic**: Give them exactly what they don't want
- **Comedy**: Implausible coincidences, running gags, the rule of threes
- **Dynamic**: Adapts mode based on game state -- ramps up drama near victories, adds comedy to break tension
- **FAFO**: The universe has receipts

The "BOOP" operation: The dealer reaches into the deck and swaps one card to the top. Fate rewritten in a single swap. It's theatrical. It's delicious. It's everything Fluxx already is, turned up to eleven.

## Why I'm Writing

A few things:

**1. I wanted you to know.** You created something that works beautifully for AI character simulation. That's not something you could have anticipated in 1996, but here we are. Fluxx's design -- especially the embrace of chaos and the elegant rule conflict resolution -- is exactly what makes it tractable for AI systems.

**2. I'm asking permission.** I'm using "Fluxx" in my internal documentation, referencing Looney Labs, including the trademark notice. I'm not selling anything -- this is research and exploration. But if you'd prefer I rename it, remove references, add different attribution, or change anything, please tell me. I'll do it.

**3. I'd love to share with you.** If you're curious, I can show you the simulation logs, the character dynamics, the moments where the AI dealer perfectly times a Creeper to arrive at maximum dramatic impact. It's genuinely entertaining. Not because I'm a great designer -- because *you* are.

**4. I might write about it.** I'd love to evangelize this approach -- use Fluxx as a case study in AI character simulation, write about why the game design works so well for this purpose. If that happens, I want to do it with your blessing and whatever attribution you'd want.

**5. I'd love to use Fluxx as the base driver for coherent character narrative simulation.** Use it as a benchmark to compare models, test character simulation techniques, use my "cursor mirror" tool (which lets the AI review its own session history) to optimize skills and protocols and data representations. Fluxx has so many levels of simulation that are hard to get right -- rule tracking, goal awareness, character voice, strategic adaptation, social dynamics, behavioral tells -- that it's the perfect stress test. If I can build a robust system that stays on the rails, respects ethical guidelines, and produces entertaining coherent narratives with Fluxx, I can do it with anything.

## What I'm NOT Asking

I'm not pitching a product. I'm not asking for a collaboration (unless you're interested, in which case, let's talk). I'm not asking for your time beyond reading this letter. I know you're busy. Life is full. We've all got projects.

I just wanted to tell you: something you made years ago turned out to be perfect for something no one could have imagined. And I thought you'd want to know.

## The Philosophy Resonance

Reading your old design notes reminded me why I loved games in the first place:

> "Fluxx is a game about change."

That's it. That's the whole thing. MOOLLM is also about change -- how characters adapt, how systems evolve, how conversations become explorations. Kindred spirits in the chaos.

Your "nurturing environment" philosophy matches what I'm building. Not a killer app -- a space where creative things can happen. A place to play.

## Take Care

No need to respond unless you want to. I'll add whatever attribution you'd like. I'll modify or remove anything you'd prefer not to see. Just say the word.

I hope our paths cross again sometime. Maybe over a game.

Warmly,

Don Hopkins

---

P.S.  --  In my simulation, Andy Looney is a playable character who sits in seat 8 and watches the chaos unfold with designer's eyes, occasionally noting "That's an interesting interaction." And Kristin would make a wonderful character too -- let me know if you'd like to be in the game! If not, you become "Anonymous Game Designers #7 and #8."

P.P.S.  --  The Amsterdam expansion includes a "Tourist Trap" Creeper that prevents you from winning unless you have the Bicycle (so you can escape). Living here teaches you things.

---

*Fluxx® is a registered trademark of Looney Labs®.*
