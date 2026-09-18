# Memorably Differentiate Commands

**Class:** lens · **Attribution:** Don Hopkins, as SimHacker,
[HN comment on "A New Car UI"](https://news.ycombinator.com/item?id=7263027), 19 Feb 2014 —
the lens takes its name from that comment's first sentence

> **Different costs deserve different shapes.**

> *"Memorably differentiating the possible commands is the reason I designed the layout of
> the pie menus in SimCity the way I did."*

Commands that differ in cost, function, and consequence must *look and feel*
different — size, shape, grouping, position — not sit in a flat grid of identical
hitboxes. The SimCity tool palette is the exhibit: the bulldozer, the road tool,
and the nuclear power plant differ by orders of magnitude in price and blast
radius, so the palette gives them different footprints and neighborhoods, and
the palette layout doubles as a legend for the on-map cursors. Spatial memory
does the rest: your hand learns where the park tool lives the way it learns a
light switch.

Three mechanisms, all in the original: **icon size carries cost**, so a nuclear plant is
physically bigger than a road. **Icon border color matches the on-map cursor**, which in the
multiplayer version made the palette a legend for what every other player was holding. And
the palette is **vertically asymmetrical to differentiate kinds, horizontally symmetrical to
pair siblings** — a totem pole rather than a grid.

The counterfactual is stated plainly, and it condemns a whole genre:

> *"If all the tools were the same sized squares arranged in a regular grid, it would be
> much harder to differentiate them and quickly select the one you want. Instead, they're
> arranged more like a bouquet of unique flowers that each have their own special features
> that make them easily recognizable and memorable, while telling you something about
> themselves."*

That is the uniform icon ribbon, where "insert comment" and "delete database" are the same
24×24 square distinguishable only by tooltip. Uniformity is a rendering convenience sold as
visual cleanliness — it optimizes the screenshot and taxes every retrieval. Differentiation
is how a command set becomes a *learnable map* instead of a vending machine
([k-line-activation](k-line-activation.md): each command needs a distinct hook
to attach to).

The same comment refuses the easy escape, which is worth keeping attached to the lens: this
is "an artistic balancing act, highly dependent on the set of commands, and requiring a lot
of iteration, testing and measurement," and therefore "not something you can expect
end-users to be able to do with their own custom built menus." Differentiation is design
labour that cannot be delegated to a preferences panel — but it can be *taught*, which is
where the comment's PieCraft proposal goes: a game whose craftable artifacts are pie menus,
with menus that spill their contents when attacked, so arranging your commands well is the
gameplay.

**Go deeper:**
[Hopkins on the SimCity tool palette (HN, 2014)](https://news.ycombinator.com/item?id=7263027) ·
[the Fitts's Law companion comment in the same thread](https://news.ycombinator.com/item?id=7262676) ·
[parent thread: A New Car UI](https://news.ycombinator.com/item?id=7261003) ·
[the screen dump it describes: multiplayer SimCity on a Sun workstation, TCL/Tk/X11](http://www.donhopkins.com/home/catalog/simcity/SimCity-Sun.gif)

**Sources:**
[MicropolisCore documentation/designs/simcity-tool-palette-design.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/simcity-tool-palette-design.md)

**See:** [fitts](fitts.md) — size by frequency and cost ·
[self-revealing-gestures](self-revealing-gestures.md) ·
[directories-as-advertisements](directories-as-advertisements.md) — the same
lens applied to filesystems · [../masters/don-hopkins.md](../masters/don-hopkins.md) ·
[../masters/jens-monig.md](../masters/jens-monig.md) — block shapes as visible
type signatures
