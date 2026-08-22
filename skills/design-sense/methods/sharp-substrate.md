# Sharp Substrate

**Class:** method · **Attribution:** Owen Densmore (NeWS at Sun); the COM discipline

> **Keep a maximally general, sharp mechanism at the bottom. Route everyday work
> through a disciplined protocol on top. Never ban the substrate.**

Densmore's move at Sun: NeWS was raw PostScript with processes and events — a
razor. Instead of dulling it, he built a class system *in* it (the NeWS object
system that became TNT), so ordinary work rode a civilized protocol while the
full sharpness stayed reachable underneath. COM made the same bet: IUnknown's
QueryInterface is brutally minimal, and every higher convention (dispatch
interfaces, connection points) is protocol layered on the unbroken substrate.

Two failure modes this method forbids:

- **Banning the substrate** — locking users out of the layer below the polite
  API caps the ceiling exactly where your imagination stopped
  ([low-floor-no-ceiling](low-floor-no-ceiling.md) — the ceiling is load-bearing
  and users crash into it).
- **Skipping the protocol** — shipping only the razor makes every user rederive
  the discipline; the sharp thing without the civilized layer is a support
  burden, not a platform.

The design-sense use: when layering a system, put generality at the bottom and
discipline in the middle, and keep the trapdoor open. Snap! on JavaScript,
HyperTalk on the Toolbox, moollm's skills on raw filesystem-and-LLM — each is a
disciplined protocol over a sharp substrate that experts can still touch
([stage-magic](../lenses/stage-magic.md): simple view until complex truth, and
the truth is *reachable*).

**Go deeper:**
[Wikipedia: NeWS](https://en.wikipedia.org/wiki/NeWS) ·
[Wikipedia: Component Object Model](https://en.wikipedia.org/wiki/Component_Object_Model)

**Sources:** [designs/DIRECTORY-AS-IUNKNOWN.md](../../../designs/DIRECTORY-AS-IUNKNOWN.md) ·
[../masters/james-gosling.md](../masters/james-gosling.md) — NeWS's architect ·
[../masters/don-hopkins.md](../masters/don-hopkins.md) — pie menus lived on this
substrate

**See:** [low-floor-no-ceiling](low-floor-no-ceiling.md) ·
[worse-is-better](worse-is-better.md) — the rival theory of what survives ·
[power-of-simplicity](power-of-simplicity.md)
