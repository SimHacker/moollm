# Smart placement: containers that route what you put in them

"Put this in that" is underspecified. Which pocket, which shelf, which sub-slot?
Every desktop ever shipped answers by making the user do all the filing by hand.
Games answered better, decades ago, in four distinct families.

Broken out of [GAME-PIECES.md](GAME-PIECES.md), which states the protocol and
the troll's stomach; this document is the genealogy and the webtop application.

## The protocol

From **OpenLaszlo** (David Temkin et al.): a child declares a `placement`
attribute, a container declares a `defaultplacement`, and the container can
override its determine-placement method to inspect the incoming child — plus an
optional args object for custom parameterized placement protocols — and route it
to the right sub-container.

The everyday use was a constant sub-path to the "client view," so children added
to a window skipped the chrome (title bar, scroll bars) and landed in the content
area. The general idea is bigger: **the container owns the routing decision, and
the giver doesn't need to know the container's internals.**

This is the drag-and-drop contract every direct-manipulation microworld needs:
SimCity tiles, Sims object slots, HyperCard backgrounds, Laszlo views, troll
stomachs. Low-level moves obey; high-level verbs route.

## The genealogy in shipped games

**Typed bags** — the container only accepts its type. World of Warcraft's
profession bags (herb, mining, enchanting, soul bags, quivers); EverQuest's
quivers and tradeskill containers before that; Breath of the Wild's pouches are
the purest form — an apple *can only* land in materials, and the player never
files anything.

**Auto-routing on deposit** — the container inspects and files, which is the
stomach's exact protocol. Guild Wars 2's fills-first bags (oiled bags attract
junk, craftsman's bags attract mats, equipment boxes attract gear, invisible bags
opt *out* of sorting and vendoring) plus "deposit all materials"; Path of Exile's
stash tab affinities routing a ctrl-click dump to whichever tab owns the type;
Stardew Valley's "add to existing stacks"; Diablo III/IV material storage.

Terraria's **Quick Stack to Nearby Chests** is the elegant one: items fly to
whatever chests *already contain that kind of thing*, so **the world's existing
arrangement is the routing table**. No declarations, no config — the filing you
already did is the spec.

**Routing as visible labor** — Dwarf Fortress stockpiles (dwarves haul everything
to its typed zone, so the sort is performed by characters you can watch),
Minecraft hopper sorters (player-*built* placement protocols), Factorio filter
inserters and logistic chests. Factorio generalizes furthest: deposit-routing
made *continuous*, belts for arbitrary objects, in the von Neumann 29-state
universal constructor lineage
([FACTORIO-MOOLLM-DESIGN.md](FACTORIO-MOOLLM-DESIGN.md)).

**Containers with behavior** — the stomach's true family. Diablo II's Horadric
Cube *transforms* what it holds, a container that digests; EverQuest's ovens and
forges; Torchlight's pet, a walking container that leaves to go sell; and
NetHack's bag of tricks, a container that turns out to be a creature — the exact
inverse of the troll, a creature that turns out to be a container.

NetHack also supplies the recursion cautionary tale: bag of holding in bag of
holding explodes. GIVE TROLL TO TROLL just deepens the narrative stack — single
pocket, no boom.

## PieCraft: the container *is* the UI

In **PieCraft** (Don Hopkins,
[canonical design in MicropolisCore](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/piecraft/PIECRAFT.md))
pie menus are craftable typed bags whose **geometry is part of the type — slot
count is valence**. Pies auto-route on deposit (a potion files itself into the
consumables pie, a spell into its element's slice) and **bond into molecules**: a
submenu is a covalent bond, a loadout is a molecule of complementary valences,
and combat can decompose a molecule back into element pies, spilling loose items.

Smart placement, typed bags, and Fitts's law fused into one crafting system.

## What a webtop should inherit

Features a general-purpose webtop window/object manager should have — the direct
descendant of OpenLaszlo's placement protocol, at home in a zoomable interface of
the kind David Temkin has pursued:

- **Quick Stack for files.** Drop a pile on the desktop and each file flies to a
  folder that already contains that kind of thing. The user's existing
  arrangement is the routing table, so the system learns filing from the filing
  you already did — programming by demonstration where the *demonstration is your
  folder structure*.
- **Affinities and fills-first folders.** A folder declares what it attracts
  (INTERFACE.yml-style, one dropped file at a time); an invisible-bag folder opts
  out of auto-sort entirely.
- **Deposit-all verbs.** One gesture files everything routable and leaves the
  residue visible for triage — conservative in what it moves, liberal in what it
  accepts.
- **Routing as visible animation.** In a zoomable interface the file *visibly
  flies* to its destination, Terraria-style, so auto-filing is
  self-demonstrating: the system shows you its reasoning at exactly the moment
  you could correct it. That is the teach-by-demonstration loop running in
  reverse — the system demonstrates, the user inspects and corrects.

## One container algebra at four scales

The **pie menu tabbed window interface** is the window-level embodiment of the
same system
([PIE-TAB-WINDOWS.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/notes/PIE-TAB-WINDOWS.md)
in MicropolisCore; shell context in
[MOOLLM-WEBTOP-VISION.md](webtop-gwern-inheritance/MOOLLM-WEBTOP-VISION.md)).

A **Stack is a typed bag of Cards**; a **tab is simultaneously the handle and the
advertisement** — grab it to drag, pop a pie on it for the Card's verbs (close,
detach to window, move to stack, open in git), heritage running back through NeWS
tabbed frames and the PSIBER Space Deck.

Its snapping and grouping rules are literally a placement protocol for windows:
dragging a Card offers snap positions — dock as a sibling in the layout tree,
insert into a target Stack (tab rows merge), or pull out to float — so the
*workspace* inspects the incoming window and offers placements, the way the
stomach inspects the incoming meal.

Pies, tabs, Stacks, and PieCraft molecules are one container algebra at four
scales: **slice, tab, window, workspace.**

## Honest costs

- **Wrong routing is worse than no routing**, because the user watched it happen
  and now has to find where it went. Visible animation is not decoration; it is
  the correction window.
- **Affinity conflicts need a tiebreak** and any tiebreak will surprise someone.
  Terraria's answer (existing contents win) is the least surprising because the
  user authored it.
- **Opt-out is mandatory.** Guild Wars 2 shipped invisible bags for a reason;
  every auto-filer needs a folder that means *leave my mess alone*.

## Related

- [GAME-PIECES.md](GAME-PIECES.md) — pieces, containers, and the troll's stomach
- [ADVERTISEMENT-AUCTION.md](ADVERTISEMENT-AUCTION.md) — how a container's offers get scored
- [`troll/stomach/STOMACH.yml`](../examples/adventure-4/characters/fictional/troll/stomach/STOMACH.yml) — the working implementation
