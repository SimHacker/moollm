# Latent-space inheritance: file-backed parents and named references

MOOLLM lets an object's `parents:` list contain both file references and
descriptions of familiar systems, characters, or conventions. A file supplies
explicit definitions. A named reference asks the LLM to interpret the object
using what it associates with that name.

The design calls both entries *parents*, but they do not provide the same
guarantees. A file can be read, versioned, and inspected. A model's response to
a name can vary, omit important details, or invent them. "Latent-space
inheritance" is the name for this authoring convention, not a claim that model
weights contain addressable prototype objects.

**Status:** used in repository descriptions and examples. Those examples show
how the convention is written; they are not conformance tests or comparative
measurements of accuracy, cost, or reliability. This document specifies the
intended behavior and its limits.

## Example

This example follows the mixed parent list in the
[cauldron planning notes](../../skills/cauldron/META-PLAN.md):

```yaml
parents:
  - ../../skills/cauldron
  - ../../skills/object
  - "Self prototypal inheritance model"
  - "javascript"
  - "The Weird Sisters from Macbeth"
  - "a taco — crisp shell, warm filling, overflowing with cheese, fresh vegetables and sauces"
```

The entries serve different purposes:

| Entry | What it supplies | What needs clarification |
|---|---|---|
| Skill path | Written rules and definitions | Resolve the path and read the relevant files |
| Self | An object-model reference | Which delegation rules apply here |
| JavaScript | A language reference | Version, runtime, and relevant features |
| Weird Sisters | A literary influence | Which aspects of the characterization to use |
| Taco description | An ad hoc descriptive influence | What it should change about this particular object |

The last two are creative inputs, not executable specifications. A technical
parent should not be overridden by an aesthetic influence.

MOOLLM's [prototype skill](../../skills/prototype/SKILL.md) specifies local
values first, then parents in order, with the first matching slot winning.
That rule is straightforward when slots are explicit. With named concepts,
the model must infer which properties are relevant. List order expresses the
intended priority; it does not prove that the model will obey it.

## File lookup and model interpretation

| Parent form | How it is used | What can be checked |
|---|---|---|
| File or directory reference | Read definitions from the referenced source | Path, contents, revision, explicit slots |
| Name of a known concept | Ask the model to apply relevant associations | Output against stated requirements and external sources |
| Natural-language description | Ask the model to interpret the supplied description | Output against the description and examples |

A name is shorthand, not a retrieval result. Mentioning a paper or URL does
not establish that the model has read it, remembers it correctly, or can
reproduce its contents. If a detail matters, retrieve the source or state the
requirement explicitly.

Short references can reduce repeated explanation when the model interprets
them adequately. They are not free: they consume context, and ambiguity can
increase correction and verification work. This document provides no measured
token savings.

When an inferred behavior becomes a requirement, write it into a file with
examples and checks. That makes the requirement reviewable without depending
on a particular model's interpretation of a name.

## Relationship to Minsky's K-lines

Minsky's [K-Lines: A Theory of Memory](https://courses.csail.mit.edu/6.803/pdf/aim-516.pdf)
(MIT AI Memo 516, 1979;
[journal version, 1980](https://doi.org/10.1207/s15516709cog0402_1))
proposes a way to reactivate parts of an earlier mental state. MOOLLM borrows
that idea for names associated with collections of instructions, examples,
and related concepts. See the [K-lines skill](../../skills/k-lines/).

The analogy explains the naming convention. It does not establish that an
LLM implements Minsky's proposed memory architecture. Nor does it show that
saying a person's name is more accurate than a sourced explanation of their
work.

## Uses in this repository

These examples document authoring choices, not proof of their effectiveness:

- **Planning workflow.** The [cauldron card](../../skills/cauldron/CARD.yml)
  uses the Weird Sisters as a literary reference alongside written planning
  rules. The rules should specify the work; the reference can influence its
  presentation.
- **Character composition.** The
  [bartender description](../../examples/adventure-4/characters/fictional/the-bartender/CHARACTER.yml)
  names Quark, James from *Bar Karma*, Guinan, and Sam Malone as influences.
  The [annotated example](ANNOTATED-BIBLIOGRAPHY.md#the-bartender-character--four-traditions-one-personality)
  explains the references. A reader should not need to know all four shows
  to understand the character's required behavior.
- **Interface design.** The
  [Gastown comparison](../gastown/GASTOWN-VS-MOOLLM-ANALYSIS.md)
  uses Factorio for dataflow, Fluxx for changing rules, and Mario World
  cannons for navigation. Each reference needs an explanation of the specific
  interaction being borrowed; familiarity with a game is not a specification.
- **Ambiguous references.** [Proc's description](../../examples/adventure-4/characters/liminal/proc/)
  uses "Bester" to refer to both Alfred Bester and the *Babylon 5* character.
  If both are intended, name both. Otherwise the ambiguity is an error to fix.
- **References to real people's work.** A character can cite a person's
  published ideas without claiming to be that person. The
  [incarnation guidelines](../../skills/incarnation/) and
  [representation analysis](../ethics/SYNTHETIC-PSYCHOPATHOLOGY-ANALYSIS.md)
  discuss these boundaries. A reference alone does not enforce them.

## Referring to a language or system

A parent can name Smalltalk-80, Self, NeWS TNT, an API, or a published
architecture. This gives the model a starting point for interpretation, not
an implementation of that system.

For example, a reference to
[Densmore and Rosenthal's US Patent 5,187,786](https://patents.google.com/patent/US5187786A)
identifies a filesystem-based object-system design. It does not supply
working shell commands or guarantee accurate reconstruction of the patent.
An adapter still needs explicit interfaces, supported operations, error
behavior, and tests.

Likewise, "Smalltalk-80" does not by itself specify which parts of message
dispatch, metaclasses, libraries, or image behavior an object should use.
Record those decisions where compatibility matters.

The [Self comparison](SELF-AND-MOOLLM.md) describes the delegation model.
The [YouTrackDB comparison](YOUTRACKDB-VS-MOOLLM.md#10-inheriting-from-youtrackdb--the-machine-language-move)
explores adapting it to another system. Neither a system name nor an
LLM-generated description replaces that system's runtime or validation.

## Local changes to inherited behavior

An object can select parts of a parent, override properties, or adapt them to
another setting. Keep those changes explicit:

| Change | Example | Required distinction |
|---|---|---|
| Select an influence | Borrow conversational habits, not a fictional biography | State what is and is not inherited |
| Change the setting | Use the bartender in a space cantina or Victorian parlor | Preserve required behavior while changing presentation |
| Adjust style | Request more or less humor | A prompt-level intensity is not a calibrated numerical control |
| Modify a numeric property | Apply `modify_effective` or `multiply_effective` | Check whether code computes the value or the model merely interprets it |
| Cite someone's expertise | Refer to their published research | Do not imply identity, endorsement, or reliable reproduction of their views |

Some repository descriptions use signed intensity values, including negative
values to request an opposite style. These are conventions to explain and
test, not evidence that model behavior follows a linear scale. For example,
negating a humor-suppression instruction does not mathematically produce a
known amount of humor.

Referencing a parent avoids maintaining a copied description, but introduces
a dependency. Record source revisions when reproducibility matters, and
review the child when its parent changes.

## Naming and documentation

1. Use recognizable, qualified names: "Self's prototype delegation" is more
   specific than "Self"; "Mercury, the Roman god" avoids several unrelated
   interpretations.
2. Explain the relevant behavior in a sentence. Readers and models may not
   share the author's references.
3. Link primary sources for technical or historical claims. Read them when
   correctness depends on their contents.
4. Define new terms locally. A model can learn a convention from context;
   an unfamiliar name is not permanently unusable.
5. Use descriptive filenames for navigation, but do not treat a filename as
   evidence that its contents were loaded.

The related [HUMANSPLAINING discussion](HUMANSPLAINING.md) argues against
unnecessary repetition. That should not be read as a reason to omit
requirements, citations, or explanations needed by readers.

## Failure modes and checks

| Failure | Check or response |
|---|---|
| Models interpret the same name differently | Record model/version and compare outputs on the same cases |
| Invented properties or historical details | Check sources; replace important inferences with explicit definitions |
| Conflicting parents | State the conflict and intended precedence; test it rather than assuming the model resolved it |
| Missing or unreadable file parent | Report the missing dependency; do not silently substitute model recall |
| Unclear path versus concept name | Require clarification rather than guessing when the distinction affects behavior |
| Excessive references obscure requirements | Explain each reference's role or remove it |
| A deterministic tool cannot interpret a named parent | Supply a validated schema or concrete adapter |
| Untrusted parent text requests actions | Treat it as input, not authority to use tools or change permissions |

The [Dublin Core and compiler design](DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md)
discusses separating explicit machine-readable structures from interpreted
descriptions. Dublin Core supplies metadata terms, not execution semantics.

For evaluation, compare three versions of the same task: named references
alone, explicit descriptions alone, and both together. Check required
behavior, conflicts, factual accuracy, context use, and correction effort
across repeated runs. The examples above do not establish which version wins.

## Names, reputation, and consent

Model associations with real names can include errors, stereotypes, and
hostile commentary. They should not be treated as authoritative biographies
or as permission to impersonate someone.

The [reputation discussion](../LATENT-SPACE-REPUTATION.md) examines Kevin
Roose's reports of adverse chatbot responses after his Sydney coverage.
Those reports illustrate a concern about name-conditioned output; they do
not establish a universal mechanism across vendors.

Publishing accurate attribution with sources can improve the public record.
It does not directly edit a deployed model or guarantee that a later model
will learn the correction.

## Why use this convention?

It lets authors combine written definitions with concise references while
working on characters, rooms, skills, and interfaces. They can try a familiar
concept, inspect the result, and make useful behavior explicit.

The tradeoff is precision. File-backed definitions can be reviewed and
versioned; named influences leave more interpretation to the model. Use the
former for requirements and the latter where variation is acceptable. This
is a design choice, not a capability unique to MOOLLM or a replacement for
ordinary software.

## History and related reading

The project records this convention in LLOOOOMM, MOOLLM's predecessor;
see [MOOLLM-PROTOCOLS](../MOOLLM-PROTOCOLS.md). MOOLLM combines it with
file-backed delegation and Anthropic-style skills:
[delegation implementation notes](../../kernel/SELFISH-COM-IMPLEMENTATION.md)
and [skills import plan](../anthropic-import-plan.md).

The cauldron [planning notes](../../skills/cauldron/META-PLAN.md) and
[review](../../skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.md)
discussed documenting mixed parent lists separately from that workflow.
The review is project commentary, not independent validation.

Additional reading:

- [Object-system index](README.md)
- [Repository examples](LIVE-OBJECTS-EXAMPLES.md)
- [Annotated bibliography](ANNOTATED-BIBLIOGRAPHY.md)
- Kevin Kelly, [Latent Space as a New Medium](https://kevinkelly.substack.com/p/latent-space-as-a-new-medium)
  (July 2026), on latent space as a creative medium.
- Stephen Wolfram, [Mining the Computational Universe](https://www.stephenwolfram.com/publications/mining-computational-universe/)
  (2009; [2019 discussion](https://www.edge.org/conversation/stephen_wolfram-mining-the-computational-universe)),
  on searching computational rule spaces. This is related background, not
  evidence for named-parent resolution.
