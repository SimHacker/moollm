# Emoji Anchors: Outline Syntax Design

> *Anchors are the language; comments are the intent; structure is the meaning; rendering is just a view.*

---

## The Core Insight

An outline node that can be just:
- A bullet shape (•, –, +, ◯, ⬤, ▸, ⟡...)
- Plus one to a few emoji anchors
- Optional text (discouraged)
- Comments
- Children

...is incredibly powerful because it's:

| Quality | Description |
|---------|-------------|
| Language-independent | Works across cultures |
| Glanceable | Understood at a glance |
| Structural | Position carries meaning |
| Mnemonic | Easy to remember |
| Semiotic | Stance/intent in the anchor |

---

## Anchor-Only Nodes

You can treat them as "section headers" / "modes" / "operators":

| Anchor | Meaning |
|--------|---------|
| ◯👁️ | Observation zone |
| +🔥 | Escalation / amplification |
| –🧊 | Cooling / de-escalation |
| ▸🗺️ | Navigation / map / links |
| ⬤🧠 | Analysis / theory |
| ⟡🙏 | Ritual / prayer / appeal |

**No prose required. The tree is the message.**

---

## Eye Zones as Syntax

| Syntax | Meaning |
|--------|---------|
| `<👁>` | Angle-bracket: input / observation |
| `(👁)` | Paren: interpretation / aside |
| `{👁}` | Brace: rule set / doctrine |
| `[👁]` | Bracket: annotation / citation |
| `(👁><👁)` | Confrontation / comparison / dialectic |
| `👁👁` | Amplification / scrutiny / pile-on |
| `👁‍🗨️` | Commentary / whisper / framing |

**This is readable code literacy without code intimidation.**

---

## Why "Anchor" Not "Bullet"

"Bullet" is:
- Loaded with violence connotations
- Too presentation-specific
- Not semantic enough

"Anchor" correctly implies:
- Attachment point
- Semantic marker
- Structural handle
- Navigational affordance

**It's a concept, not a glyph.**

---

## Enumeration Anchors

Stylistically fine to use:
- a, b, c, d
- i, ii, iii, iv
- 1, 2, 3, 4
- A, B, C, D

These are already global-ish and function like structural punctuation.

---

## Text Policy

| Policy | Description |
|--------|-------------|
| **Discouraged** | Prefer emoji-only anchors |
| **Allowed** | When necessary |
| **Short** | Keep it minimal |
| **K-Lines** | explicit k-lines: YAML-JAZZ |

Reason: Cross-cultural appeal. Emoji transcends language.

---

## Compound Anchors

Combine multiple elements:

```
👁️📊  → Observation + data
🔥⚖️  → Escalation + judgment
🙏📜  → Prayer + doctrine
🧠🔗  → Theory + connection
```

**Order can carry meaning** — primary then modifier.

---

## Node Model

A node has:

| Component | Description |
|-----------|-------------|
| **Anchor** | The semantic marker(s) |
| **Text** | Optional content |
| **Comment** | Intent / explanation / string, list, or tree |
| **Children** | Nested nodes |
| **Parent** | Container reference |
| **Attributes** | Optional string→string metadata for html/xml compat |
| **Elements** | Sub element tree for html/xml compat |
| **Attachments** | List of attached objects, ref by id, or manifest like buffs |

---

## YAML Serialization

```yaml
👁️:
  _anchors: ["<👁>", "👁️📊", "👁️🔥"]  # This node, children, grandchildren
  _comments: "Observation of the current situation"
  
  📊: # Inherits 👁️📊
    data: current_metrics
    
  🔥:
    _anchors: "👁️🔥"  # Explicit override
    signal: escalating
```

---

## Editor Behavior

A WYSIWYG outline editor should:
- Display anchors visually
- Hide underscore keywords
- Let you edit their meaning, not syntax
- Support emoji generation and insertion via pie menus
- Auto-generate anchors if not specified
- Strive for WYMIWYG: What You Mean Is What You Get

---

## Anchor Inheritance

Use `_anchors` — a string or array:
- **String:** Anchor for this node. Children inherit.
- **Array:** First element = this node. Second = children. Third = grandchildren. And so on.

```yaml
report:
  _anchors: ["📊", "📈", "📉"]  # report=📊, children=📈, grandchildren=📉
  
  growth:  # Inherits ["📈", "📉"] → anchor=📈
    Q1:    # Inherits ["📉"] → anchor=📉
      value: +15%
    
  decline:  # Inherits ["📈", "📉"] → anchor=📈
    Q3:    # Inherits ["📉"] → anchor=📉
      value: -3%
```

**When you bottom out (one element left), keep reusing it.**

**Postel:** Accept `_anchor` on input, emit `_anchors` on output.

---

## Mixing Bracket Syntaxes

You can mix different bracketing — this is old school SGML:

```yaml
<👁>:
  observation: "Something is happening"
  
  (👁):
    interpretation: "This feels performative"
    
  {👁}:
    doctrine: "According to EvalGenius..."
    
  [👁]:
    citation: "See: feed/123"
```

**The indentation conveys structural meaning too!**

---

## Comments on Top of That

And you can add YAML comments:

```yaml
<👁>:
  observation: "Something is happening"
  # This feels unusual — note the timing
  # May be coordinated with earlier events
  
  (👁):  # Personal interpretation follows
    hot_take: "Smells like astroturfing"
```

---

## Why This Works for Global Communication

| Quality | Benefit |
|---------|---------|
| Emoji-first | Cross-lingual |
| Structure-first | Hierarchy transcends grammar |
| Comments as intent | Explain in any language, UI translates |
| Anchors as operators | Universal semantics |

**Two players can have meaningful exchange across languages because the tree carries meaning.**

---

## Frontier/More Lineage

This echoes the Userland Frontier / More outline editor lineage:
- Outline as primary UI
- Indentation as meaning
- Comments as documentation
- Structure as navigation

But with:
- Emoji as semantic anchors
- YAML as serialization
- LLM as interpreter
- Cross-cultural focus

---

## Related Documents

- [SCATS-DESIGN.md](./SCATS-DESIGN.md) — Expressions using anchors
- [EVAL-DOM-SPEC.md](./EVAL-DOM-SPEC.md) — Reserved keywords
- [EVALEYE-DESIGN.md](./EVALEYE-DESIGN.md) — Eye iconography
- [../../skills/yaml-jazz/](../../skills/yaml-jazz/) — YAML Jazz skill

---

*"Anchors are the language; comments are the intent; structure is the meaning; rendering is just a view."*
