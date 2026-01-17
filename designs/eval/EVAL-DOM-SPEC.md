# EVAL DOM Specification

> *Reserved keywords get out of the way of normal free-form naming.*

---

## Purpose

MOOLLM needs its own **DOM (Document Object Model)** to represent arbitrary YAML with extensions:
- Comments represented
- Anchors explicitly declared
- Attributes as metadata
- Round-tripping preserved

---

## Design Principles

| Principle | Description |
|-----------|-------------|
| **Underscore prefix** | All reserved keys start with `_` |
| **Postel's Law** | Accept loosely, emit strictly |
| **Round-trip safe** | Parse and emit without loss |
| **Editor-friendly** | WYSIWYG hides syntax, shows meaning |
| **JSON-compatible** | `_comment` survives JSON serialization |

---

## Reserved Keywords

All reserved keywords are prefixed with `_` to mark them as special/private:

### Structure and Stance

| Keyword | Description |
|---------|-------------|
| `_anchors` | Anchor symbol(s) — string or array. First for this node, rest for children/grandchildren. |

**Postel's Law:** Accept `_anchor` on input, emit `_anchors` on output.

### Human Intent (JSON-safe)

| Keyword | Description |
|---------|-------------|
| `_comments` | Intent/explanation — string, array, or discussion tree |

**Postel's Law:** Accept `_comment` on input, emit `_comments` on output.

**Editor rule:** Coalesce YAML `#` comments into `_comments` for round-trippable JSON.

#### JSON Round-Tripping

This is crucial: **YAML Jazz with comments can round-trip through JSON**.

JSON has no comment syntax. YAML `# comments` would be lost on JSON export. But `_comments` is just data — it survives any format that supports strings and arrays.

```
YAML Jazz → JSON → YAML Jazz
    ↓         ↓         ↓
Comments   _comments   Comments
preserved  as data     restored
```

| Format | Native Comments | `_comments` Field |
|--------|-----------------|-------------------|
| YAML | ✅ `# comment` | ✅ preserved |
| JSON | ❌ none | ✅ preserved |
| XML | ✅ `<!-- -->` | ✅ preserved |
| MessagePack | ❌ none | ✅ preserved |
| BSON | ❌ none | ✅ preserved |

**The `_comments` convention makes human intent portable across all serialization formats.**

This enables:
- API transport (JSON) without losing context
- Database storage (BSON) with explanations intact
- Cross-format pipelines that preserve meaning
- LLM consumption of intent, not just structure

#### `_comments` Flexibility

`_comments` can be:

| Form | Use Case | Example |
|------|----------|---------|
| **String** | Simple explanation | `_comments: "This explains intent"` |
| **Array** | Multiple voices/layers | `_comments: ["First point", "Second point"]` |
| **Tree** | Threaded discussion | See below |

#### Threaded Comment Trees

When people comment on comments, you get a discussion tree:

```yaml
speaker: "🍄👸 Donna Toadstool"
context: "Campaign rally, Mushroom Kingdom, 2026"
claim: "I am the greatest president!"
_comments:
  - author: "@don"
    text: "Bold claim, Donna"
    _comments:
      - author: "@maya"
        text: "By what metric?"
        _comments:
          - author: "@don"
            text: "Approval ratings"
          - author: "@skeptic-worm"
            text: "Those are lagging indicators"
      - author: "@val"
        text: "📋 Noted. Score pending."
  - author: "@historian"
    text: "Lincoln would disagree"
  - author: "@toad"
    text: "She's the BEST! The best best best!"
  - author: "@plannedchaosmushroom"
    text: "As a trained hypnotist and certified genius, I can confirm Donna Toadstool is weaving 4D chess while everyone else plays checkers. She's operating on a level most people can't comprehend. Trust me, I have no connection to her campaign."
    _comments:
      - author: "@maya"
        text: "🧦🧦 sock check"
      - author: "@skeptic-worm"
        text: "IP trace: Castle Toadstool, Royal Bathroom"
```

#### Comment Node Structure

Each comment in a tree can have:

```yaml
_comments:
  - author: "@username"      # Who said it
    text: "The comment"      # What they said
    timestamp: 2026-01-15    # When (optional)
    stance: 🤔               # Emoji stance (optional)
    _comments: [...]         # Replies (recursive)
    
    # Votes and reactions
    votes:
      up: 42
      down: 3
      flag: 1
    reactions:
      💡: 12                  # Enlightening
      🔥: 8                   # Hot take
      🤝: 5                   # This
      🧠: 3                   # Big brain
      🧦: 2                   # Sock puppet detected
      ☠️: 1                   # Killed by words
```

#### Votes and Reactions

Comments can collect feedback beyond replies:

| Type | Description | Examples |
|------|-------------|----------|
| **Standard votes** | Up, down, flag | Reddit-style scoring |
| **Emoji reactions** | Free-form with comments | 💡🔥🤝🧠💀🎯 + explanation |
| **Named awards** | Platform keywords | `enlightening`, `helpful`, `controversial` |

**Key Insight: Reactions Have Comments Too!**

Every reaction can carry an explanatory comment. The emoji is the quick take; the comment is the context.

```yaml
reactions:
  - emoji: 💡
    count: 23
    _comments: "Enlightening — changed how I see this"
  - emoji: 🔥
    count: 8
    _comments: "Hot take — provocative but defensible"
  - emoji: 🧦
    count: 2
    _comments: "Sock puppet detected — suspiciously on-message"
```

**Contextual Emoji Mappings**

Emoji meanings are NOT universal — they're **contextually customizable**:

```yaml
# Room-level reaction definitions (inherited by all comments in room)
_reaction_vocabulary:
  💡: "Enlightening"
  🔥: "Hot take"
  🧦: "Sock puppet detected"
  🎯: "Nailed it"
  🤡: "Clown behavior"
  ☠️: "Fatality"

# Or inherit from parent context
_reaction_vocabulary: inherit  # Uses room → world → platform defaults
```

**Inheritance Chain:**

```
Comment → Parent Comment → Thread → Room → World → Platform Defaults
```

Each level can:
- Define new emoji meanings
- Override inherited meanings
- Add context-specific reactions

```yaml
# Example: A cooking forum might define
_reaction_vocabulary:
  🧂: "Needs more salt"
  👨‍🍳: "Chef's kiss"
  🔥: "Too spicy"           # Different from default "hot take"!
  💀: "Killed the dish"      # Context-specific death
```

**The Comment IS the Meaning**

Without a comment defining what 🔥 means here, it's ambiguous. With contextual vocabulary, every reaction is grounded in local meaning. Different communities develop different emoji dialects.

```yaml
# Full example with contextual reactions
- author: "@skeptic-worm"
  text: "Those are lagging indicators"
  votes: { up: 127, down: 4 }
  reactions:
    - emoji: 💡
      count: 23
      from: ["@economist", "@analyst", ...]
    - emoji: 🎯
      count: 15
      _comments: "This specific critique hits the core weakness"
  awards:
    - type: enlightening
      from: "@economist"
      _comments: "Finally someone said it"
    - type: controversial
      auto: true
      _comments: "Vote ratio triggered automatic flag"
```

**Reactions are Scats too** — each reaction is a micro-evaluation, a tiny judgment cast upon the comment. The emoji IS the take, but the comment grounds it in context.

#### Worm Reactions

[Eval Worms](./EVAL-WORMS.md) crawl discussions and leave automated reactions:

```yaml
# Worm-generated reactions appear alongside human reactions
- author: "@plannedchaosmushroom"
  text: "Trust me, I have no connection to her campaign."
  reactions:
    - emoji: 🧦
      count: 2
      from: ["@maya", "@sockdetector-worm"]
      _comments:
        - author: "@sockdetector-worm"
          text: "Pattern match: self-praise + denial + hyperbole"
          confidence: 0.89
          evidence:
            - "IP correlation with @donna-toadstool"
            - "Linguistic fingerprint: 94% match"
            - "Posted 3 minutes after campaign briefing"
```

**Common Worm Reaction Types:**

| Worm | Reaction | What It Does |
|------|----------|--------------|
| 🧦 **Sock Detector** | 🧦 | Flags coordinated/fake accounts |
| 📋 **Fact Checker** | ✅❌🤔 | Verifies claims against sources |
| 🔗 **Source Tracer** | 🔗 | Links to original sources |
| 🔄 **Repost Spotter** | 🔄 | Identifies copied content |
| 📊 **Stats Worm** | 📊 | Adds context to statistics |
| 🌡️ **Tone Analyzer** | 🌡️ | Flags escalation patterns |
| 🕸️ **Network Mapper** | 🕸️ | Shows account relationships |

```yaml
# Fact-check worm reaction
- author: "@donna-toadstool"
  text: "Crime is up 500% since I left office!"
  reactions:
    - emoji: ❌
      from: ["@factcheck-worm"]
      _comments:
        - author: "@factcheck-worm"
          verdict: false
          text: "Crime statistics show 3% decrease"
          sources:
            - "FBI Unified Crime Report 2025"
            - "Mushroom Kingdom Bureau of Statistics"
          confidence: 0.97
          methodology: "Compared claimed figure to official data"
```

**Worms are transparent** — they declare their bias, show their evidence, and mark their output as machine-generated. Unlike hidden moderation, worm reactions are inspectable and contestable.

#### Evolution Pattern

Comments evolve continuously from inline syntax to rich structure:

```
# inline    →   _comments: "string"   →   _comments: [...]   →   _comments: [{...}]
    ↓                  ↓                        ↓                       ↓
YAML syntax      Single voice            Multiple voices         Threaded tree
```

**The Full Lifecycle:**

| Stage | Form | Trigger | Example |
|-------|------|---------|---------|
| 1. Inline | `# comment` | Initial write | `key: value  # explains intent` |
| 2. String | `_comments: "..."` | JSON export, or explicit | `_comments: "explains intent"` |
| 3. Array | `_comments: [...]` | Second comment added | `_comments: ["first", "second"]` |
| 4. Tree | `_comments: [{...}]` | Reply to a comment | See threaded example above |

**How It Works:**

```yaml
# Stage 1: Inline comment (normal YAML)
claim: "The sky is blue"  # This is obvious

# Stage 2: Coalesced to string (for JSON, or when parsed)
claim: "The sky is blue"
_comments: "This is obvious"

# Stage 3: Someone adds another comment → array
claim: "The sky is blue"
_comments:
  - "This is obvious -Butthead"
  - "Unless it's night or cloudy -Beavis"

# Stage 4: Someone replies to a comment → tree
claim: "The sky is blue"
_comments:
  - text: "This is obvious"
    _comments:
      - text: "Is it though?"
        author: "@philosopher"
    author: "@butthead"
  - text: "Unless it's night or cloudy"
    author: "@beavis"
```

**Key Insight:** The `# comment` syntax is just stage 1. It doesn't disappear — it gets *promoted* into the `_comments` field where it can grow. Anyone can comment on comments, forming trees. The structure evolves with use.

**Editor Behavior:**
- Parse inline `# comments` into `_comments` when loading
- Display `_comments` as inline annotations when simple
- Expand to threaded view when tree structure emerges
- Round-trip preserves all stages

**Start simple. Grow as needed. The structure adapts to use.**

### Metadata and Interoperability

| Keyword | Description |
|---------|-------------|
| `_attributes` | String→string map (XML/HTML-friendly) |
| `_elements` | Explicit XML/SGML-like sub-elements |
| `_metadata` | Arbitrary YAML Jazz (structured, not restricted to strings) |

### Content Typing

| Keyword | Description |
|---------|-------------|
| `_mime_type` | MIME type of primary text (default: `text/plain`) |
| `_schema` | Schema reference |
| `_syntax` | Syntax hint |
| `_language` | Language hint |
| `_region` | Regional hint |
| `_dialect` | Dialect hint |
| `_author` | Author attribution |

### References and Proof

| Keyword | Description |
|---------|-------------|
| `_attachments` | List/map of attached resources (URLs, files, artifacts) |
| `_citations` | Explicit proof links / sources |
| `_links` | Related link urls, relative paths, ids, or k-lines |

### Encoding (Exceptional)

| Keyword | Description |
|---------|-------------|
| `_encoding` | Encoding hint (default: UTF-8). Other encoding strongly discouraged. |

---

## Defaults and Omission

### Implied Defaults (when absent)

| Keyword | Default |
|---------|---------|
| `_mime_type` | `text/plain` |
| `_encoding` | UTF-8 |
| Content type | string |
| Anchors | Auto-generated by editor |

### Serializer Rule

**Omit keys that equal defaults.** This keeps Scats short, tasty, and remixable.

---

## Node Model

Each node is conceptually:

```yaml
# Primary content (usually string — could be URL, JSON, etc.)
content: "The main value"

# Optional reserved underscore keys
_anchors: "👁️📊"              # String: this node only
# OR
_anchors: ["📊", "📈", "📉"]   # Array: this node, children, grandchildren...

_comments: "Simple explanation"   # String: simple case
# OR
_comments:                        # Tree: discussion
  - author: "@don"
    text: "This is my claim"
    _comments:
      - author: "@maya"
        text: "I disagree"
        
_attributes:
  id: "node-123"
  class: "observation"
_metadata:
  created: 2026-01-15
  author: "@don"

# Children
child1: ...
child2: ...
```

---

## Attribute Handling

### Postel's Law for Attributes

| Input | Serialization |
|-------|---------------|
| String | String (unchanged) |
| Number | Stringified |
| Boolean | `"true"` / `"false"` |
| Other | Stringified, with warning |

**Accept loosely, canonicalize to strings on serialize.**

---

## Comment Coalescing

### On Load (YAML → DOM)

1. Collect `#` comments attached to each node
2. Place them into `_comments` (preserving order)
3. Accept `_comment` (singular) and upgrade to `_comments`
4. Optionally keep original `#` comments for YAML round-trip fidelity

### On Save (DOM → YAML)

1. Always emit `_comments` (canonical form)
2. Simple strings stay as strings
3. Complex trees stay as trees
4. Optionally regenerate `#` comments for readability (configurable)

**This gives you:**
- JSON safety
- YAML niceness
- Zero loss of intent
- Threaded discussions preserved

---

## Anchor Inheritance

### Declaration

```yaml
container:
  _anchors: ["📊", "📈", "📉"]  # This node, children, grandchildren...
```

**As string:** Applies to this node only. Children inherit.

**As array:** First element is this node's anchor. Second is for children. Third is for grandchildren. And so on.

### Resolution

1. If node has explicit `_anchors`, use first element (or whole string)
2. Remaining elements become children's `_anchors` (shift left)
3. When you bottom out (one element left), keep reusing it
4. If no `_anchors`, inherit from parent

### Example

```yaml
report:
  _anchors: ["📊", "📈", "📉"]  # report=📊, children=📈, grandchildren=📉
  
  growth:  # _anchors inherited as ["📈", "📉"] → anchor=📈
    Q1:    # _anchors inherited as ["📉"] → anchor=📉
      value: +15%
    Q2:    # _anchors inherited as ["📉"] → anchor=📉
      value: +12%
      
  decline:  # _anchors inherited as ["📈", "📉"] → anchor=📈
    Q3:     # _anchors inherited as ["📉"] → anchor=📉
      value: -3%
```

### Input Compatibility (Postel)

Accept on input:
- `_anchor: "📊"` (legacy, single node)
- `_anchors: "📊"` (string, single node)
- `_anchors: ["📊", "📈"]` (array, cascading)

Emit on output:
- `_anchors: "📊"` or `_anchors: ["📊", "📈"]` (canonical form)

---

## Eye Zone Syntax

Nodes are encouraged to use and invent new bracketed eyes and other emojis as expressive anchors and visual elements:

| Anchor | Meaning |
|--------|---------|
| `<👁>` | Input / observation |
| `(👁)` | Interpretation / aside |
| `{👁}` | Rule set / doctrine |
| `[👁]` | Annotation / citation |

**These are valid YAML keys** (though editors may display them specially).

---

## Technical Implementation

### Base DOM

Use a standard Python/JavaScript YAML DOM module that supports:
- Comment round-tripping
- Line/column ranges
- Anchor/alias support

Recommended:
- Python: `ruamel.yaml` (preserves comments)
- JavaScript: `yaml` package with `keepComments: true`

### Extension Layer

Add conventions for:
- `_` prefixed keywords
- Anchor inheritance
- Attribute canonicalization
- Comment coalescing

---

## Editor Integration

A WYSIWYG editor should:

| Feature | Behavior |
|---------|----------|
| Hide `_` keywords | Operationalize their meaning instead |
| Emoji anchor picker | Pie menu or palette |
| Comment panel | Edit `_comment` directly |
| Attribute inspector | Key/value editor |
| Type hints | Show `_mime_type` as icon |

---

## Example: Full Scat

```yaml
🪱📜:
  _anchors: ["🪱📜", "👁", "🔥"]  # Scat, sections, items
  _comments: "Worm's interpretation of recent drama"
  _mime_type: "application/scat+yaml"
  _attachments:
    - url: "evaleye://feed/123"
    - url: "evaleye://dm/@maya"
  _metadata:
    worm_id: "@skeptic-worm"
    confidence: 0.6
  
  diet:  # Inherits 👁 as anchor
    - 👁 EvalEye/feed/123
    - 👁 DM/@maya
    
  stance: ⚖️ skeptical
  
  take:
    _anchors: "🔥"  # Override: explicit anchor for this section
    - 🔥 escalation likely
    - 👀 intent ambiguous
    
  notes:
    _comments:
      - author: "@skeptic-worm"
        text: "selective amplification detected"
      - author: "@skeptic-worm"
        text: "context missing from earlier thread"
        _comments:
          - author: "@engagement-worm"
            text: "Missing context IS the strategy"
            stance: 🔥
```

## Example: Soul Claim with Discussion

```yaml
soul:
  claim: "I am the greatest evaluator"
  _comments:
    - author: "@don"
      text: "This is my self-assessment"
      timestamp: 2026-01-15
      _comments:
        - author: "@maya"
          text: "By what criteria?"
          stance: 🤔
          _comments:
            - author: "@don"
              text: "Clipboard size"
            - author: "@val"
              text: "📋 Insufficient. Score: 4/10."
        - author: "@skeptic-worm"
          text: "All self-assessments are suspect"
          stance: 🧊
    - author: "@church"
      text: "Hubris noted. Confession recommended."
      stance: ⛪
```

**This is a scat discussion tree. Arguments live in the data.**

---

## Reserved Namespace

**All keys starting with `_` are reserved for structural purposes.**

User content should not use underscore-prefixed keys. If they do, the editor may hide them or treat them as metadata.

---

## Related Documents

- [SCATS-DESIGN.md](./SCATS-DESIGN.md) — Scat structure
- [EMOJI-ANCHORS.md](./EMOJI-ANCHORS.md) — Anchor semantics
- [../../skills/yaml-jazz/](../../skills/yaml-jazz/) — YAML Jazz skill
- [../../schemas/](../../schemas/) — Schema definitions

---

*"The underscore prefix is a privacy marker. Reserved keywords get out of the way of normal free-form naming."*
