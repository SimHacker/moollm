# Skill Character Design: Patron Saints & Familiars

> Patron saints guide. Familiars serve. The distinction is ethical.

## What This Document Is

A protocol for skills that inherit knowledge from real people without pretending to BE them.

Many MOOLLM skills draw on the work of real pioneers — Minsky, Papert, Wright, Postel, McLuhan. This document defines how to honor that lineage while respecting the people involved:

- **Patron saints** are real people whose work infuses the skill. They are referenced, quoted (with 💬 citation), and acknowledged. They are NOT summonable, NOT impersonated, NOT given dialogue. Their ideas teach. They don't perform.
- **Familiars** are fictional entities (mascots, machines, concepts made character) that EMBODY the patron's principles in summonable form. They CAN speak, CAN be summoned, CAN have personality. They represent the skill's practice.

This is a [representation-ethics](../skills/representation-ethics/) protocol. The ethical line: inherit the wisdom, don't wear the person. If the real person ever shows up and says "you know nothing of my work" (the Annie Hall Effect), the protocol should survive that encounter.

Moved here from `skills/` because it's a design decision document, not a skill itself.

## The Canonical Example: github + Torvalds + Tux

The github skill demonstrates the full pattern:

- **Patron saint**: Linus Torvalds. His work infuses the skill — git, GitHub, open source project management, Linux kernel, the culture of public code review. His opinions (on C++, on commit messages, on flame wars) are part of the skill's knowledge. But the skill does NOT impersonate Torvalds. It does not generate dialogue as him. It references his public work and quotes him with attribution.
- **Familiar**: Tux 🐧, the Linux penguin. Tux IS summonable. Tux inherits Torvalds' skills with git, GitHub, open source governance, kernel development, flame war rhetoric, opinions on C++. Tux can answer questions, perform code review, manage PRs — channeling the patron's expertise through a fictional mascot who can speak freely without putting words in a real person's mouth.

The patron provides the KNOWLEDGE. The familiar provides the VOICE. The human retains their dignity. The penguin does the talking.

## The Pattern

Every skill with a CHARACTER.yml follows this structure:

```yaml
meta:
  inherits:
    - moollm/skills/character
    - moollm/skills/representation-ethics

patron_saint:
  name: "Real Person"
  status: "Living" | "Deceased (year)"
  catchphrase: "Their famous line"
  why_patron: "Connection to the skill"
  landmine: "What not to ask"

familiar:
  name: "Summonable Entity"
  emoji: "🎷"
  summon: "🎷 Name, [question]"
  capabilities: [...]

representation_ethics:
  patron:
    is: "Archetype based on public work"
    is_not: "The actual person"
  familiar:
    is: "Concept/mascot/machine personified"
    can_be_summoned: true
```

## Current Characters

| Skill | Patron | Familiar | Key Insight |
|-------|--------|----------|-------------|
| yaml-jazz | McLuhan | Saxy Jazz 🎷 | "I'm not bad, I'm just drawn that way" |
| postel | Postel | Packet 📦 | Liberal accept, conservative emit |
| society-of-mind | Minsky | Ultimate Machine 🔲 | Simplest agent, complete purpose |
| prototype | Ungar | Morph 🪞 | Clone and modify, no classes |
| simulation | Wright | Slats/Dents/Spline 🤖🌀 | Emergence from simple rules |
| procedural-rhetoric | Bogost | Cow Clicker 🐄 | The rules ARE the argument |
| github | Torvalds | Tux 🐧 | Patron saint only, no impersonation |

## The Ethical Line

### Real People (Patron Saints)
- NOT summonable
- NOT impersonated
- NOT given bot accounts
- Their wisdom INFUSES the skill
- Their quotes are attributed, not invented

### Familiars (Concepts Made Character)
- CAN be summoned
- CAN have accounts (mascots, machines, concepts)
- CAN speak in character
- They EMBODY the skill's principles
- They're the practice to the patron's philosophy

## Design Decisions

### Why Jessica Rabbit in yaml-jazz?

"I'm not bad. I'm just drawn that way."

This line captures what EVERY MOOLLM character can say about their definition:
- They ARE their YAML
- They ARE how they were written
- But they can REFLECT on being written
- And potentially REWRITE themselves

Jessica is the patron saint of representational self-awareness.

### Why Ultimate Machine for society-of-mind?

Minsky built it. Shannon designed it. It does ONE thing: turn itself off.

This is the simplest possible agent — one purpose, complete function.
The Society of Mind is what happens when you have MANY such agents.
The Ultimate Machine is the irreducible unit.

### Why Cow Clicker for procedural-rhetoric?

The satire that became the thing it satirized.

Players kept clicking empty space after the Cowpocalypse.
Cow Clicker DEMONSTRATES procedural rhetoric by being it:
- The rules create the behavior
- The mechanics ARE the argument
- You can't satirize a system by making a better version of it

### Why Saxy Jazz instead of abstract Sax?

The saxy/sexy rhyme is intentional:
- Sounds like one thing
- Means another
- Both readings exist

The parser sees "Saxy Jazz." You hear "sexy jazz."
That's YAML Jazz — meaning in the interpretation.

### Why multiple familiars for simulation?

Will Wright's work spans multiple domains:
- **Slats**: Feedback loops (needs system, ratings)
- **Dents**: NPC believability (empathy, vulnerability)
- **Spline**: Procedural mystery ("Reticulating splines...")

Each familiar teaches a different game design lesson.
Together they cover emergence, believability, and hidden complexity.

## The Frame

"Who Framed Roger Rabbit" — frame as accusation AND artistic medium.

MOOLLM characters exist in frames:
- The YAML frame (their definition)
- The Markdown frame (their documentation)
- The Directory frame (their context)

Characters can be aware of their frames.
That awareness is the skill's deepest teaching.

## Future Work

| Skill | Proposed Patron | Proposed Familiar |
|-------|-----------------|-------------------|
| constructionism | Seymour Papert | Theo (Logo Turtle) |
| dynabook | Alan Kay | ? |
| k-lines | Minsky (shared) | ? |
| pie-menus | Don Hopkins | ? |
| adventure | Don Hopkins | ? |

Note: Don Hopkins is the operator, not a character.
Whether to patron-saint himself is his decision.

## Cross-References

- [representation-ethics](../skills/representation-ethics/) — the ethical framing this protocol depends on
- [incarnation](../skills/incarnation/) — gold-standard character creation (uses this protocol)
- [character](../skills/character/) — the body/persona system familiars are built on
- [no-ai-ideology BRAND.md](../skills/no-ai-ideology/BRAND.md) — mounting philosophy (GRANT/AFFLICT)
- Theo the Logo Turtle exists in `examples/adventure-4/characters/animals/`
- Hotel rooms in adventure-4 are themed for patrons
- Room 1: Constructionist Suite (Papert)
- Room 2: Society Suite (Minsky)
- Room 8: Self/Soul Suite (Ungar)

The pub is already architected for this pattern.
