# Comments as Data

**Class:** lens · **Attribution:** moollm yaml-jazz
**Dispatch:** whole skill at moollm [skills/yaml-jazz/](../../yaml-jazz/) — load it; this entry is the design-sense pointer.

> **Comments carry what fields can't.**

In yaml-jazz, comments are first-class semantic data, not decoration: the fields
carry what machines must parse, and the comments carry intent, uncertainty,
provenance, humor, and context — everything a schema can't hold but a future
reader (human or LLM) desperately needs. JSON's deepest design wound is
collapsing this channel; YAML keeps it, and moollm builds on the difference
("entropy preservation": the format that keeps more of what the author knew).

The lens generalizes past YAML: commit messages are comments-as-data for
history; alt text is comments-as-data for images; the annotation layer of any
format is where the *why* lives, and formats or tools that strip it are lossy
compressors of exactly the knowledge that's hardest to reconstruct. Design
representations so the comment channel survives round-trips.

**Go deeper:**
moollm [skills/yaml-jazz/](../../yaml-jazz/) (CARD.yml for notation rules,
SKILL.md for the reading/writing protocol) ·
moollm [kernel/constitution-core.md](../../../kernel/constitution-core.md) §3

**Sources:** moollm `skills/yaml-jazz/`

**See:** [three-axis-accessibility](three-axis-accessibility.md) — why the
channel matters to all three audiences ·
[directories-as-advertisements](directories-as-advertisements.md) ·
[../methods/sister-script.md](../methods/sister-script.md) — the prose that
rides with the automation is the same channel at file scale
