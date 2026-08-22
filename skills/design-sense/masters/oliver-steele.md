# Oliver Steele

**Class:** master · **Head:** instance-first; declarative reactive UI

Instance-first development, stated plainly in 2004: implement for one real
instance, generalize when the second case appears — it's easier to generalize from
two examples than from one. Instance substitution: instance and class should be
syntactically parallel, so promotion is a rename, not a rewrite (an LZX tag is a
class). OpenLaszlo's constraint-driven declarative UI made the reactive style
mainstream frameworks rediscovered a decade later.

## Votes

- **Implement the one real instance first** — generalize when the second case
  arrives; two examples beat one theory
  ([instance-first](../methods/instance-first.md),
  ["Classes and Prototypes" (2004)](https://blog.osteele.com/2004/03/classes-and-prototypes/))
- **Make instance and class syntactically parallel** — promotion should be a
  rename, not a rewrite; an LZX tag *is* a class
  ([instance-substitution](../methods/instance-substitution.md))
- **Declare the dependency and let the runtime keep it true** — OpenLaszlo's
  constraints anticipated the reactive decade
  ([rich-harris](rich-harris.md) compiled this vote;
  [the Garnet-to-Svelte lineage](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/garnet-to-svelte-constraint-ui-lineage.md))
- **Design the gradient, not the cliff** — every step from copy-paste to
  abstraction should be small, safe, and reversible
  ([play-learn-lift](../methods/play-learn-lift.md) for code)

## Vetoes

- Don't write the class before the second instance exists
- Don't make promotion to abstraction cost a rewrite
- Don't hand-sync what a constraint could keep true

## Plugins attributed

[../methods/instance-first.md](../methods/instance-first.md) ·
[../methods/instance-substitution.md](../methods/instance-substitution.md)

## Sources

Steele, "Classes and Prototypes" (2004) · wwsff `characters/oliver-steele/` ·
wwsff `characters/don-hopkins/garnet-to-svelte-constraint-ui-lineage.md`
