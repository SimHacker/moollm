# Subjective-Oriented Programming

First-person code — the "I" shifts based on who is speaking.

## The Insight

```javascript
// Third-person (confusing)
if (world.has("key")) ...  // Does the world have a key?

// First-person (clear)
if (i_have("key")) ...     // Do I have a key?
```

## Context Shifting

| Context | Who is "I"? |
|---------|-------------|
| Player action | The player |
| Object simulate() | The object |
| NPC dialogue | The NPC |

## Core Functions

```javascript
// Inventory
i_have("key")
i_has_tag("weapon")

// State
i_am("lit")
i_get("fuel")
i_set("fuel", 50)

// Buffs
i_have_buff("strength")

// Communication
i_say("Hello!")
i_emit("The lamp dies!")
```

## Example

```yaml
# Object simulation
simulate: |
  if i_am("lit"):
    i_set("fuel", i_get("fuel") - 1)
    if i_get("fuel") <= 0:
      i_set("lit", false)
      i_emit("The lamp dies!")
```

See [SKILL.md](./SKILL.md) for full documentation.
