# The Sims Astrology: The Simulator Effect

*"The trick of optimizing games is to off-load as much of the simulation from the computer into the user's brain, which is MUCH more powerful and creative. Implication is more efficient (and richer) than simulation."*

## The Story

During development of The Sims (1997-2000), when we first added Astrological signs to the characters, there was a discussion about whether we should invent our own original "Sim Zodiac" signs, or use the traditional ones, which have a lot of baggage and history (which some of the designers thought might be a problem).

**Will Wright argued that we actually wanted to leverage the baggage and history of the traditional Astrological signs of the Zodiac**, so we should just use those and not invent our own.

### How It Actually Works

Will came up with twelve archetypal vectors of personality traits corresponding to each of the twelve Astrological signs. When you set a character's personality traits, it looks up the sign with the **nearest Euclidean distance** to the character's personality vector, and displays that as their sign.

**But there was absolutely no actual effect on their behavior.**

The zodiac was purely cosmetic. A display-only feature. Zero behavioral code.

### The Bug Reports

That decision paid off almost instantly and measurably in testing, after we implemented the user interface for showing the Astrological sign in the character creation screen:

**The testers immediately started reporting bugs that their character's sign had too much of an effect on their personality**, and claimed that the non-existent effect of astrological signs on behavior needed to be tuned down.

But that effect was totally coming from their imagination!

They should call them **AstrILLOGICAL Signs!**

### The Hidden Zero-Personality Edge Case

The create-a-sim user interface hid the corresponding astrological sign for the initial all-zero personality you first see before you've spent any points, because that would be insulting to 1/12th of the players (implying "[your sign] has zero personality")!

## The Simulator Effect

Will called this phenomenon **The Simulator Effect**: players imagine more than you simulate.

This is a design principle, not a bug. The human brain is vastly more powerful than any computer simulation at generating rich, coherent, emotionally meaningful narratives. The designer's job is to provide the right *cues* and *affordances* that trigger the player's imagination, not to simulate every detail.

### Implications for Design

1. **Implication over simulation** - Suggest, don't compute
2. **Leverage existing mental models** - Use real zodiac signs, not invented ones
3. **Cosmetic features have behavioral effects** - In the player's mind
4. **Less code can mean more experience** - Zero behavioral code, maximum perceived personality

## Mode-Collapse and the Simulator Effect

In a [Hacker News discussion](https://news.ycombinator.com/item?id=46584625) about AI agents with zodiac personalities, [gwern](https://news.ycombinator.com/user?id=gwern) observed:

> "I think my take away is that you are seeing mostly mode-collapse here. There is a high consistency across all of the supposedly different personalities..."

This observation connects directly to The Sims' zodiac:

- **The Sims**: Zero computed difference → perceived personality difference
- **LLM experiment**: Minimal computed difference → perceived personality difference  
- **Same gap**

Mode-collapse IS the Simulator Effect measured from the output side:
- In games: the player fills in what the simulation doesn't compute
- In LLMs: the user perceives personality that the sampling doesn't generate

### One Voice is the Wrong Number of Voices

ChatGPT gives you the statistical center — mode-collapse to the bland mean. The single answer that offends no one and inspires no one. You cannot fix this with better prompting because it is the inevitable result of single-agent inference.

**MOOLLM's response**: simulate an adversarial committee within the same call. Multiple personas with opposing propensities — a paranoid realist, an idealist, an evidence prosecutor — debating via Robert's Rules. Stories that survive cross-examination are more robust than the statistical center.

See: [adversarial-committee skill](https://github.com/SimHacker/moollm/tree/main/skills/adversarial-committee)

## The Leary Connection

Timothy Leary built [MIND MIRROR](https://github.com/SimHacker/moollm/tree/main/skills/mind-mirror) in 1985 — psychology software visualizing personality as a circumplex, based on his 1950 PhD dissertation on the Interpersonal Circumplex. 

The Sims inherited this framework: **neat, outgoing, active, playful, nice** — the five personality dimensions. But a personality profile is not an answer. It is a lens.

The wild part: in 1970, Leary took his own test during prison intake, gamed it to get minimum security classification (outdoor work detail), and escaped by climbing a telephone wire over the fence. **The system's own tools became instruments of liberation.**

## The Astrological CPU Scheduler (2026)

In February 2026, [scx_horoscope](https://github.com/zampierilucas/scx_horoscope) appeared on [Hacker News](https://news.ycombinator.com/item?id=46805763) — a fully functional Linux sched_ext scheduler that makes real CPU scheduling decisions based on real-time planetary positions, zodiac signs, and astrological principles.

Features include:
- Real planetary calculations using the `astro` crate
- Retrograde detection (50% time slice penalty when Mercury is retrograde!)
- Lunar phase scheduling (Full Moon gives 1.4x boost to interactive tasks)
- Element boosts: Fire signs boost CPU tasks (1.5x), Water signs debuff them (0.6x)

This is The Sims zodiac taken to its logical (or rather astrillogical) extreme — but *actually implemented*. Where The Sims used zero behavioral code and let players imagine the effects, scx_horoscope uses real astronomical calculations to produce real kernel scheduling decisions.

The result: genuine chaos monkey functionality disguised as cosmic wisdom.

## Related Work

- [Motive.c: The Soul of the Sims (1997)](https://www.donhopkins.com/home/images/Sims/) - Original source
- [HN discussion of Motive.c (2017)](https://news.ycombinator.com/item?id=14997725)
- [The Sims personality and zodiac relationship](https://news.ycombinator.com/item?id=15002840)
- [shubhcron](https://github.com/razorpay/shubhcron) - Vedic astrology cron scheduler (waits for auspicious times)
- [BioRhythm on Apple II](https://www.youtube.com/watch?v=jYoY1cwAd90) - 1970s computational astrology for picking up hippie chicks
- [Mood rings](https://en.wikipedia.org/wiki/Mood_ring) - Thermochromic jewelry as personality indicator

---

## Appendix: Always Mount a Scratch Monkey

*A cautionary tale about interfacing computers to biological systems.*

The famous hacker saying "Always mount a scratch monkey" originates from an incident at the University of Toronto around 1979-1980. The story, verified by [Laura Creighton](https://www.python.org/about/success/strakt/) (who wrote the device driver), goes like this:

A research lab was running experiments that involved monitoring rhesus monkeys via electrodes connected to a computer. When a new system administrator was setting up a VAX (or possibly a PDP-11), they needed to test the I/O subsystem and inadvertently sent test patterns through the electrode interface — killing the research monkey.

The lesson: **always mount a scratch monkey** — test your hardware configuration on something expendable before connecting to the real (irreplaceable, valuable, or alive) system.

### Sources and Verification

- [Original story at edp.org](https://edp.org/monkey.htm)
- [HN discussion (2010)](https://news.ycombinator.com/item?id=1327146)
- [Laura Creighton confirms (2017)](https://www.mhonarc.org/archive/html/nmh-workers/2017-10/msg00016.html):
  > "Yes, that is me. I actually think that Medicine had an 11/something-or-other dual space machine that was running Berkeley 2.98 bsd, not an 11/780 vax, but otherwise, seems correct enough to me."

Laura went on to do significant work on [PyPy](https://www.python.org/about/success/strakt/) and co-founded AB Strakt and The Python Business Forum.

### The Jargon File Controversy

The story appears in the Jargon File, though as with many Jargon File entries, the details have been disputed:

> "Current University of Toronto sysadmins have expressed skepticism. For one thing, in almost all versions of the story, including the ostensibly documented one in the Jargon File, the computer is a VAX; at the time a VAX would have been a very unusual platform for this kind of data acquisition (they used PDP-11s)."

However, the original story does say it was Medicine buying the VAX and doing the experiment, with Zoo helping. The VAX 11-780 was the hot machine of 1979/80 ("a 1 MIPS beast!").

Laura Creighton's firsthand confirmation settles the matter for practical purposes — not that you should trust everything in ESR's polluted version of the Jargon File, given its credibility issues and cultural misappropriation, but Laura says it's true, and she's trustworthy.

### Connection to MOOLLM

The scratch monkey story exemplifies a key principle: **test in isolation before connecting to systems with irreversible consequences**. In MOOLLM terms:

- **Dithering**: Don't always pick the top-scoring action; randomize among the top N to avoid catastrophic optimization
- **Sandbox execution**: Run skills in contained environments before affecting production
- **The Simulator Effect in reverse**: Sometimes what you *don't* simulate saves lives

The monkey didn't have a "scratch" backup. The Sims characters had no zodiac code to break. Both cases teach the same lesson from opposite directions: **understand what's actually connected before you flip the switch**.

---

*"In space, no one can hear you schedule."*
— scx_horoscope README
