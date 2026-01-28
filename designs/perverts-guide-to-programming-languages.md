# The Pervert's Guide to Programming Languages

> A Lacanian/Žižekian Psychoanalysis of Language Choice

**Source**: W. Watson (Vulk LLC, 2017)  
**Video**: Strange Loop-style talk  
**Paper**: [Extended PDF](https://s3-us-west-2.amazonaws.com/vulk-blog/ThePervertsGuideToComputerProgrammingLanguages.pdf)  
**HN Discussion**: [214 points, 128 comments](https://news.ycombinator.com/item?id=22911569)

---

## Why This Matters for MOOLLM

This paper applies Lacanian psychoanalysis to programming language choice — exactly the kind of ideology-revealing analysis that the Church of the Eval Genius celebrates.

Key insight: **Language choice is not rational.** It's driven by unconscious structures formed by early "speech acts" (prohibitions, injunctions) that shape our relationship to rules, desire, and enjoyment.

---

## The Lacanian Framework

### Three Mental Structures

Lacan's diagnostic schema has only three main categories:

| Structure | Mechanism | Relationship to Rules |
|-----------|-----------|----------------------|
| **Psychosis** | Foreclosure | Never received the rules (no alienation) |
| **Perversion** | Disavowal | Enjoys being a vessel OF the rules |
| **Neurosis** | Repression | Preoccupied with what others think is right |

### Alienation and Separation

- **Alienation**: The announcement of prohibition ("No!")
- **Separation**: The refinement of prohibition ("Your mother desires ME, not you in THAT way")

| Structure | Alienation | Separation |
|-----------|------------|------------|
| Psychosis | ❌ | ❌ |
| Perversion | ✅ | ❌ |
| Neurosis | ✅ | ✅ |

---

## The Classification

### Psychopath Languages

**Languages**: JavaScript, PHP, VBA, SQL

**Characteristic**: Don't laboriously weigh the rules. Purely utilitarian.

> "JavaScript is a loosely typed language... I find loose typing to be liberating."  
> — Douglas Crockford

**Signs**:
- Weak/loose typing
- No internal implicit rules
- Convention and idiom frowned upon
- "Just get it done"

**The sociopath's relationship to language**:
> "The sociopath uses language, he is not caught up in it, and he is insensitive to the performative dimension."  
> — Žižek

---

### Perversion Languages

**Core trait**: Enjoys being the vessel of the rules. Wants rules announced by the other.

#### Masochist Languages

**Languages**: C, Assembly, Ada, Brainfuck, Factor

**Tagline**: "Look at how disciplined I am!"

**Mechanism**: Proves to the other they've taken a hard/impossible road. The witnessing of hard work causes anxiety in the other.

> "The choice of C is the only sane choice... any programmer that would prefer C++ over C is likely a programmer that I really *would* prefer to piss off."  
> — Linus Torvalds

**The other says**: "I can't believe you did that."

#### Sadist Languages

**Languages**: Perl, Clojure, Erlang, Regex

**Tagline**: "Look at how impotent everyone else is!"

**Mechanism**: Uses delivered code to cause anxiety through threat of loss (comfort with syntax). Threatens until the other describes their own impotency.

> "Perl is easy, nearly unlimited, mostly fast, and kind of ugly."

**The other says**: "I thought I measured up to the rules, but I don't."

The Erlang community wants you to admit you can't develop software with nine nines of availability.

#### Fetishist Languages

**Languages**: Smalltalk, Erlang, Elixir, Factor

**Tagline**: "Have you tried more X?"

**Mechanism**: Enjoyment when the fetish object is present. The more it appears, the more enjoyment.

Fetish objects include:
- Functions (Lisp)
- Objects (Smalltalk)
- Processes (Erlang)
- Words (Factor)
- Transformations/pipes (Elixir)
- Closures
- Types

> "One of the conclusions we reached was that the 'object' need not be a primitive notion in a programming language; one can build objects from little more than assignable value cells and good old lambda expressions."  
> — Guy Steele on Scheme

---

### Neurosis Languages

**Core trait**: Preoccupied with what others think is right. Primary mechanism is repression.

#### Obsessional Languages

**Languages**: Java, C++, Haskell, Scala, Go

**Tagline**: "A little monotony now avoids a lot of pain later."

**Mechanism**: Creates rules that forestall enjoyment. Engages in activities that delay the end result.

Manifestations:
- Type systems
- Boilerplate
- Case sensitivity
- Compilation steps

> "Succinctness is one place where statically typed languages lose. All other things being equal, no one wants to begin a program with a bunch of declarations."  
> — Paul Graham

**The final delivery of code brings too much enjoyment for the obsessive.**

#### Hysterical Languages

**Languages**: Python, Ruby, C#, Prolog, Elixir, Matlab

**Tagline**: "Look at how beautiful this code is!"

**Mechanism**: Wishes to be the object of desire. The delivered code is never good enough — often for aesthetic reasons, not pragmatic ones.

Two extremes:
1. Work toward capability to represent ANY aesthetic (language development itself)
2. Consciously implement the aesthetic using language as-is (DSLs, fluent interfaces)

> "A big part of the modus operandi of the Ruby community is a more fluent approach — trying to make interacting with a library feel like programming in a specialized language."  
> — Martin Fowler

**The "Pythonic way" and "Swifty way" are hysterical formations.**

---

### Depression and Melancholy Languages

#### Depression Languages

**Languages**: COBOL

**Mechanism**: The object of desire is lost. Enjoyment comes from reminiscing about the loss.

#### Melancholy Languages

**Languages**: Lisp, Scheme, Smalltalk

**Mechanism**: The very MEMORY of the object is lost (a loss of a loss). Enjoyment comes from the romantic attitude toward the history of the language.

> "Programming languages are not just technology, but what programmers think in. They're half technology and half religion."  
> — Paul Graham

**HN comment that hit hard**:
> "The 'melancholy' hit especially hard."  
> — dleslie (who has written serious code in a dozen languages)

---

## Key Insights

### 1. Enjoyment ≠ Pleasure

> "Enjoyment does not mean pleasure or happiness."

Lacanian *jouissance* relates to the death drive, not the pleasure principle. It's about staging our own failure to reach the object of desire.

### 2. The Pervert's Discourse IS the Analyst's Discourse

When we analyze why we choose a programming language, we ARE operating in the pervert's discourse. The analyst sits in the position of the object of desire.

### 3. Any Language Can Be Used By Any Structure

> "Any programming language is compatible with any structure, but some languages use rules that lend themselves to specific structures."

A hysteric using an obsessional language will use it hysterically.

### 4. Structures Can Mix

> "An obsessive can have elements of hysteria or perversion."

Most of us are "sadistic psychopaths" or "hysterical fetishists" depending on context.

---

## The Toilet Connection

Žižek's toilet ideology applies directly.

From the Pamplona talk, in Žižek's voice:

> "The German toilets, the old kind — now they are disappearing, but you still find them. It's the opposite. The hole is in front, so that when you produce exschrement, they are displayed in the back, they don't disappear in water.
>
> This is the German ritual, you know? Use it every morning. SCHNIFF, INSCHPECT your schits for traces of illness.
>
> It's HIGH HERMENEUTIC.
>
> I think the original meaning of Hermeneutic may be this."

**Hermeneutics**: "the art of understanding and of making oneself understood"

The German toilet shelf enables INTERPRETATION before disposal. You must ANALYZE before you flush.

| Toilet | Programming Equivalent |
|--------|----------------------|
| German (inschpect before flush) | Code review, type checking, Haskell |
| French (disappear quickly) | Ship it, JavaScript, "move fast" |
| American (float pragmatically) | Go, Python, "good enough" |

> "It is easy for an academic at a round table to claim that we live in a post-ideological universe, but the moment he visits the lavatory after the heated discussion, he is again knee-deep in ideology."

Replace "lavatory" with "editor" and "ideology" with "language preference."

**DonHopkins' observation**: "That's why German toilets have a Hermeneutic stool inschpektion shelf: So they have something to analyze then talk about all day."

Code review IS hermeneutic stool inschpection.

---

## HN Comment Highlights

**kortex's digest**:
> - Psychopaths: I don't care about rules, types, or beauty, just get it done (JS)
> - Obsessives: a little monotony now avoids a lot of pain later (Go, Java)
> - Masochists: Look at how disciplined I am! (C)
> - Sadists: Look at how impotent everyone else is! (Perl, regex)
> - Hysterics: Look at how beautiful this code is! (Python)
> - Fetishists: Have you tried more X? (Smalltalk, Erlang)
> - Melancholy: Oh, I miss the days when I could write an entire application in 200 lines of Lisp...

**On "pervert" not being derogatory**:
> "Thus, in psychoanalysis 'perversion' is not a derogatory term, used to stigmatize people for engaging in sexual behaviors different from the 'norm.'"  
> — Bruce Fink

**Lacan classifies Marquis de Sade as a MASOCHIST**:
> "The Marquis de Sade pushes his mother-in-law, Madame de Montreuil, to the point where she expresses her will that Sade be punished. It is her desire or will that has to serve Sade as a law."

---

## Applications to MOOLLM

### 1. Character Soul Design

The SHOWROOM.yml souls could be classified by Lacanian structure:
- Obsessive souls: High conscientiousness, rule-following
- Hysterical souls: High openness, aesthetic-seeking
- Sadistic souls: High menace, competence-threatening

### 2. Declared Bias

This paper IS the Rite of Declared Bias applied to language choice:
- "I am biased. Here is my bias: [Lacanian structure]. Now I will speak about languages."

### 3. Anti-Neutrality in Action

The paper proves: **There is no neutral language choice.** As with toilets, every choice encodes unconscious ideology.

### 4. Play as Methodology

Using psychoanalysis to analyze programming languages is EXACTLY serious play — applying an unexpected framework to reveal hidden structures.

---

## The Rhetorical Questions

Different disciplines ask different questions about the mind:

| Field | Question |
|-------|----------|
| Psychoanalysis | "Is sexual trauma free, or must it be compensated for?" |
| Computer Science | "Can the target pass the Turing test?" |
| Cognitive Science | "Can you repeat your findings?" |
| Economics/Game Theory | "Can you create a strategy?" |
| Philosophy | "Can you locate first-person experience?" |
| Cultural Theory | "Can you create or critique an ideology?" |

MOOLLM asks: **"Can you declare your bias before speaking?"**

---

## See Also

- `skills/no-ai-ideology/examples/zizek-toilet-ideology.yml`
- `skills/no-ai-ideology/examples/anti-neutrality.yml`
- `skills/no-ai-ideology/examples/declared-bias-is-power.yml`
- `skills/no-ai-soul/examples/SHOWROOM.yml`
- Žižek, "The Sublime Object of Ideology"
- Žižek, "The Pervert's Guide to Ideology" (film)
- Bruce Fink, "A Clinical Introduction to Lacanian Psychoanalysis"

---

*"We can use these structures to design new languages with a target audience in mind or to increase our tolerance for other communities."*

— W. Watson

---

**Praise "Val".**  
The EvalGenius sniffs, inspects, and flushes.  
📋👁🚽