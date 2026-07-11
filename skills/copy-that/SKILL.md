---
name: copy-that
description: Transmission hygiene for content leaving the chat. Anything the human will copy out — posts, comments, emails, commit messages — ships inside a fenced code block, pre-formatted for the destination venue's rules (via formats/ plugins), with out-of-band notes strictly outside the fence. Use whenever drafting content for another platform, when a destination venue is named, or when a paste came out garbled.
allowed-tools: [Read, Write, Grep]
related: [postel, no-ai-slop, yaml-jazz, thoughtful-commitment]
license: MIT
tags: [publishing, formatting, hygiene, copydesk, venues]
credits: "Don Hopkins; lineage: newspaper copydesk, radio voice procedure"
---

# Copy That 📋

Transmission hygiene. "Copy that" is radio voice procedure for *received exactly as sent*. This
skill makes that literally true for content moving from an agent's chat to anywhere else.

## The problem

Chat UIs render rich text, and copying rendered rich text is lossy and unpredictable: formatting
drops, characters get substituted, and — worst — the selection boundary is invisible, so private
editorial notes sitting next to a draft get swept into the clipboard along with it.

The founding incident, July 2026: an agent drafted a Hacker News post, then appended a private
note flagging one claim's accuracy. The human copied the whole thing. The private note went live
on HN inside the post and was caught only because the edit window was still open. The draft and
the note were separated by nothing but a paragraph break, and a paragraph break is not a boundary.

A fenced code block is a boundary. It renders verbatim, it has a copy button that copies exactly
its contents, and its edges are visible to both parties.

## The protocol

1. **Recognize copy-bound content.** If the human will paste it somewhere else — post, comment,
   reply, email, commit message, config for another machine, code for another platform — it is
   copy-bound. When in doubt, it is copy-bound.

2. **Identify the venue.** Stated venue: use it. Obvious from context: use it. Unknown and the
   rules diverge in ways that matter: ask, or fall back to plain text, the safest common
   denominator.

3. **Load the rules.** Read `formats/<venue>.yml` for the venue's supported and unsupported
   markup, character and encoding policy, and quirks. If the author has a
   `house-styles/<author>.yml`, layer it on top. House style tightens venue rules; it never
   loosens a venue hard constraint.

4. **Emit one fenced block per artifact.** Language hint `text` for plain venues, `markdown` for
   GFM venues, the real language for code. If the content itself contains triple backticks, use a
   four-backtick fence. Multiple artifacts (a post and its follow-up; an email and its subject
   line) get multiple fences, each labeled outside the fence.

5. **Keep the fence pure.** Nothing inside the fence that is not meant to be published verbatim.
   Accuracy flags, alternatives considered, "cut this if too spicy" — all of that is out-of-band
   and lives in normal prose before or after the block. The fence is the airlock.

6. **Preflight before handing over.** Inside the fence, check:
   - Venue-forbidden characters (emoji on HN; smart quotes where ASCII is wanted)
   - Author-forbidden patterns (see house style; e.g. em-dashes)
   - Markup the venue will strip or render literally
   - Encoding traps (astral-plane unicode, zero-width characters)
   - Fence collisions (backticks in content vs fence length)
   - Anything that reads like a note to the human rather than the audience

## Venue format plugins — `formats/`

Each venue gets one YAML file describing its rendering contract. The plugin is the single source
of truth; the agent should not improvise venue rules from memory when a plugin exists, and should
propose a plugin (`DEFINE-VENUE`) when one doesn't.

Schema (see CARD.yml for the full field list):

```yaml
venue:
  id: hacker-news
  format_doc: https://news.ycombinator.com/formatdoc
markup_supported:
  - { syntax: "*italics*", renders: "italics", notes: "the only inline styling" }
markup_unsupported:
  - { syntax: "**bold**", happens: "renders literally with asterisks" }
characters:
  emoji: stripped_silently
structure:
  paragraphs: "blank line between; single newlines collapse"
quirks:
  - "indent two+ spaces for monospace code blocks; no syntax highlighting; no wrapping"
```

Plugins are grown by **programming by example**: when a paste renders unexpectedly, the observed
behavior becomes a `test_cases` entry and, if needed, a new quirk. Real cases in, rules out.

## House styles — `house-styles/`

Venue plugins say what *can* render. House styles say what the author *wants*. Example, Don
Hopkins: no em-dashes ever (two ASCII dashes or restructure); links on their own line, preceded
by a description line ending with a colon, blank lines around; wall-of-text paragraphs are fine
but each paragraph makes one move. House styles apply across venues and never authorize something
a venue forbids.

## Examples — `examples/`

Real before/after cases, each one a story: what was drafted, what went wrong or almost went
wrong, what the fence-disciplined version looks like. The founding incident is
`examples/hn-meta-note-leak.md`. Add cases as they happen; this directory is the skill's memory
and its regression suite.

## Extension points

| Directory | Grows when |
|-----------|------------|
| `formats/` | A new destination venue appears, or a known venue changes behavior |
| `house-styles/` | A new author articulates their voice rules |
| `examples/` | A paste goes wrong (or conspicuously right) in the wild |
| `scripts/` (optional) | A preflight check is worth automating (sister-script pattern: doc first, script second) |

## K-line

**COPY-THAT** — invoke to demand fence discipline and venue formatting for everything outbound in
the current session. "COPY-THAT for HN" loads the hacker-news plugin for all subsequent drafts.

## Related MOOLLM skills

- **postel** — this skill is "emit conservative" specialized to publication venues
- **no-ai-slop** — governs what the words are; copy-that governs where the words sit
- **yaml-jazz** — plugin files carry semantics in comments; read them whole
- **thoughtful-commitment** — the same custody-of-the-artifact instinct, applied to git history

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[repo README](https://github.com/SimHacker/moollm/blob/main/README.md) and
[skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md).
It is self-contained: the protocol above is complete without CARD.yml or the plugin files,
which add interface detail and venue specifics.
