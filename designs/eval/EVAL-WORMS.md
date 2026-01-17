# Eval Worms: Design Document

> *Worms don't crawl — they digest. They don't index — they interpret. They don't pretend neutrality — they own their bias.*

---

## From Spiders to Worms

### Why Worms Are Better Than Spiders

| Spider Crawlers | Eval Worms |
|-----------------|------------|
| Scrape | Ingest |
| Index | Digest |
| Flatten | Interpret |
| Pretend neutrality | Transform |
| Hoard | Leave traces |

**A worm doesn't "analyze" soil. It passes through it and changes it.**

That's the correct metaphor for evaluation.

---

## Two-Ended Worms

The key insight: **worms have two ends**.

### Anatomy

| End | Function | Location |
|-----|----------|----------|
| **Head** | Crawls, reads, ingests | Source document, feed, web page, session log — anywhere |
| **Tail** | Emits scats, deposits castings | Home base, separate casting file, same doc (as selection) |

**Key: Head and tail can be in different documents!** This is the common pattern — scan one artifact, emit commentary in another.

### Behavior

1. **Head explores**: Follows links, reads content, ingests artifacts
2. **Digestion happens**: Interpretation with explicit bias
3. **Tail emits**: Scat castings that people can follow

**The worm's output is marked as coming from that worm's point of view. No fake objectivity.**

---

## Head and Tail Topology

The key insight: **heads and tails don't have to be in the same place**.

### Cross-Document Worms (Common Pattern)

| Head Location | Tail Location | Use Case |
|---------------|---------------|----------|
| Source document | Castings file | Scan one doc, emit commentary elsewhere |
| Web page | Local .yml | Crawl the web, gather scats at home |
| Session log | Review file | Digest a session, summarize in another doc |
| Feed/DM stream | Scat depot | Monitor conversations, emit curated takes |

```yaml
# Example: Worm spanning two documents
🪱📖:
  head: "./marathon-session.md"        # Where I'm reading
  tail: "./session-castings.yml"       # Where I'm emitting
  mode: cross-document
  
  # Head crawls session log
  # Tail drops scats in separate file
  # Session stays clean; commentary accumulates elsewhere
```

**This is the most common pattern.** Worms scan one artifact and produce commentary in another. The source stays pristine; the castings accumulate.

### Same-Document Worms (Selection/Cursor Mode)

When head and tail are in the **same document**, they act like a **text selection** or **cursor**:

| Pattern | Behavior | Analogy |
|---------|----------|---------|
| Head at line 50, tail at line 100 | Selects lines 50-100 for operation | Text selection |
| Head and tail at same line | Point cursor, ready to insert | Insertion point |
| Head moving, tail anchored | Expanding selection | Shift+arrow |
| Both moving together | Scanning with context window | Sliding window |

```yaml
# Example: Same-document worm as selection
🪱✂️:
  document: "./DESIGN.md"
  head: { line: 50, anchor: "## Architecture" }
  tail: { line: 120, anchor: "## Implementation" }
  mode: selection
  
  # Identifies the Architecture section for operation
  # Could: summarize, critique, refactor, extract
```

**This mode is for targeted operations** — when you want to identify a specific region of a document and do something to it.

### Hybrid: Read Here, Emit There, With Selection

```yaml
🪱🔬:
  # Reading from source (head)
  source: "./codebase/auth.py"
  head_selection: { start: 45, end: 89 }  # Just this function
  
  # Emitting to target (tail)  
  target: "./reviews/auth-review.yml"
  tail_mode: append
  
  # Focused: read a specific function, emit review elsewhere
```

---

## Worm Characteristics

Each worm has:

| Attribute | Description |
|-----------|-------------|
| **Diet** | What it reads (feeds, DMs, worlds, web pages) |
| **Metabolism** | How it interprets (fast/slow, surface/deep) |
| **Bias profile** | Explicit evaluative stance |
| **Rhetoric style** | How it frames output |
| **Emoji signature** | Visual identifier |

---

## Worm Types

| Worm | Focus | Emoji |
|------|-------|-------|
| **📈 Engagement Worm** | Maximizes engagement signals | 📈🔥💯 |
| **⚖️ Legalistic Worm** | Interprets through rules/precedent | ⚖️📜🔒 |
| **🔥 Outrage Worm** | Amplifies conflict and drama | 🔥💢🗯️ |
| **🧘 De-escalation Worm** | Calms and contextualizes | 🧘🕊️💚 |
| **🧠 Theory Worm** | Deep analysis, connections | 🧠🔗📚 |
| **👁👁 Surveillance Worm** | Pattern-spotting, tracking | 👁👁🔍📊 |
| **🎭 Narrative Worm** | Story-finding, drama arcs | 🎭📖✨ |
| **🧊 Skeptic Worm** | Questions everything | 🧊🤔❓ |

**They don't say "here are the facts." They say: "Here is what I make of this."**

---

## Scat Castings

A **Scat Casting** is:
- A compact YAML Jazz artifact
- Summarizing what was consumed
- Annotated with stance and uncertainty
- Remixable by others

### Example Casting

```yaml
🪱📜:
  diet:
    - 👁 EvalEye/feed/123
    - 👁 DM/@maya
  stance: ⚖️ skeptical
  take:
    - 🔥 escalation likely
    - 👀 intent ambiguous
  confidence: 0.6
  notes:
    # selective amplification detected
    # context missing from earlier thread
```

**It's fertile, not final.**

---

## The Remix Loop

```
1. Someone posts a Scat
2. Worms ingest it
3. Worms emit new Scats
4. People remix those Scats
5. Other worms ingest those
6. Meaning evolves
```

This is:
- Conversation
- Commentary
- Media literacy
- Procedural rhetoric

**All at once.**

---

## Why This Beats "AI Summaries"

| Traditional AI Summaries | Worm Castings |
|--------------------------|---------------|
| Single "neutral" summary | Multiple biased interpretations |
| Hidden processing | Visible digestion |
| Claims objectivity | Admits stance |
| Monologue | Ecology of voices |
| Truth as output | Truth as contested territory |

**No single summary pretends to be neutral. Bias is visible. Multiplicity is expected. Interpretation is social. Disagreement is structural.**

---

## Worm Feeds

People can:
- **Follow worms** — subscribe to their scat feeds
- **Compare worms** — see different takes on same content
- **Tune worms** — adjust parameters (if allowed)
- **Create worms** — define their own interpretive agents
- **Battle worms** — worm-vs-worm debates

---

## Technical Integration

| MOOLLM Concept | Worm Mapping |
|----------------|--------------|
| Skills | Worm diet definitions |
| Characters | Worms as personas |
| Session logs | Digestion transcripts |
| Rooms | Worm habitats |
| CARD.yml | Worm interfaces |

---

## Worm Ethics

### Transparency

Worms must:
- Declare their bias
- Show their diet
- Mark their output as interpretation
- Allow comparison with other worms

### Limits

Worms must NOT:
- Claim objectivity
- Hide their processing
- Present opinion as fact
- Masquerade as human

---

## Mobile Bots

Worms are **mobile bots**:
- Head crawls the network (or stays focused on one document)
- Tail stays at home, in casting depot, or in-document as cursor
- Head and tail often in **different documents** — the common pattern
- Output is a subscribable feed
- Processing is distributed

### Topology Examples

| Pattern | Head | Tail | Result |
|---------|------|------|--------|
| **Cross-doc scan** | `session.md` | `review.yml` | Commentary separated from source |
| **Web crawl** | External URL | Local `.yml` | Bring back scats from the web |
| **In-doc selection** | Line 50 | Line 100 | Text selection for operation |
| **Point cursor** | Line 75 | Line 75 | Ready to insert at location |

**They can even follow links to web pages and come back and scat about their thoughts.**

---

## Worm-vs-Worm Dynamics

When worms disagree:
- Their scats can reference each other
- Users see the disagreement
- Truth emerges from contrast, not authority

**This is adversarial epistemology as a feature.**

---

## Canonical Statement

> In EvalEye, information is not crawled — it is digested. Interpretive worms consume conversations, media, and artifacts, producing emoji-rich YAML Jazz "scats" that summarize, judge, and reframe what they've seen. These outputs are explicitly opinionated, remixable, and contextual. Meaning emerges through digestion, not extraction.

---

## Related Documents

- [SCATS-DESIGN.md](./SCATS-DESIGN.md) — What worms produce
- [EVALEYE-DESIGN.md](./EVALEYE-DESIGN.md) — Where worms live
- [EVAL-FACTIONS.md](./EVAL-FACTIONS.md) — Worm collectives
- [../../skills/worm/](../../skills/worm/) — Technical implementation

---

*"Worms are honest about what they are. They digest, interpret, and emit — with their bias on full display."*
