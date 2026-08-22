# Mental Model Compiler

**Class:** lens · **Attribution:** Will Wright (the two-computer framing); Don Hopkins formulation

> **You're not shipping the model. You're compiling the one in their head.**

Wright's deepest reframe: the shipped simulation is not the product — it's a
*compiler* whose output is the mental model that forms in the player's head. The
game on disk is the source; the understanding in the skull is the binary. Design
review question: not "is the simulation right?" but "what does this compile
*to*, in an actual human, at actual play speed?" A brilliant simulation whose
mental model won't fit in a player is a failed compile — all optimization, no
output. SimCity teaches a folk urban dynamics; whether Forrester's equations are
underneath matters less than whether the player's compiled model predicts what
the sim will do next ([simulator-effect](simulator-effect.md) is the runtime
half: the player's model keeps simulating where yours stops).

The compile has to stay tractable end-to-end: UI, simulation, gameplay, and
mental model are one toolchain, and the weakest stage bounds the output.
Documentation, APIs, and dashboards compile mental models too — most "intuitive"
interfaces are just ones whose compile target matches a model the user already
had ([don-norman](../masters/don-norman.md)'s gulf of evaluation is a compile
error report).

**Go deeper:**
[Will Wright's 1996 talk at Terry Winograd's Stanford seminar](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/will-wright) —
the mental-model framing, from the source ·
[Long Now: Wright & Eno, "Playing with Time" (2006)](https://longnow.org/seminars/02006/jun/26/playing-with-time/)

**Sources:**
[wwsff don-hopkins/teaching-complicated-systems-without-a-manual.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/teaching-complicated-systems-without-a-manual.md) ·
[wwsff will-wright/sources/2006-06-26-long-now-playing-with-time-eno-wright/](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/will-wright/sources/2006-06-26-long-now-playing-with-time-eno-wright)

**See:** [goldilocks-complexity](goldilocks-complexity.md) — sizing the compile
target · [simulator-effect](simulator-effect.md) ·
[../masters/will-wright.md](../masters/will-wright.md)
