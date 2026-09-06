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
inserters and belts. Factorio generalizes furthest: deposit-routing made
*continuous*, belts for arbitrary objects, in the von Neumann 29-state universal
constructor lineage
([FACTORIO-MOOLLM-DESIGN.md](FACTORIO-MOOLLM-DESIGN.md)).

**Pull instead of push** — and this is the one that inverts the family.
Everything above is push-routing: something arrives, the container inspects it
and files it. Factorio's **logistic chests** run the other direction. A requester
chest broadcasts what it *wants*, providers broadcast what they *have*, and bots
close the loop. The routing table stops being a method on the container and
becomes a property of the network.

MOOLLM ships this as a skill —
[`skills/logistic-container/`](../skills/logistic-container/) — with Factorio's
five box types intact: passive provider ("take from me if you need"), active
provider ("I'm pushing these out", with `push_to` match rules, which is the push
family again), requester (a `request_list` with `min:` thresholds for
hysteresis), storage (whatever the network couldn't route), and buffer (hold
until a condition fires). Three details earn their keep:

- **Requesters are advertisers of demand.** A request list is a standing bid, so
  the logistic network is the [advertisement auction](ADVERTISEMENT-AUCTION.md)
  running over containers instead of over actions. Scoring, priority (buffers
  outrank storage for bots) and the whole find-best-N question arrive for free
  rather than needing a second mechanism.
- **The haulers are characters.** A logistic bot is
  `behavior.type: logistic-bot` on an ordinary character with a roboport, cargo
  slots and a range — so this is the Dwarf Fortress "sort you can watch" family
  too, except the dwarves are addressable, have inventories, and can be given
  other jobs. Courier kitten is a piece.
- **Cells auto-create.** Toss an unknown item type into a grid container and a
  new cell directory appears — `mkdir -p` for items, and navigable, so a
  warehouse is a place you can walk through rather than a table you query.

Signals are the circuit network: a container emits `iron-count` or `is-full`, and
anything can read it, including an exit that only opens above a threshold. Exits
with `flow:` are conveyor belts between rooms. Protocol details in
[factorio-logistics-protocol.md](factorio-logistics-protocol.md).

### The character is a logistic container, and it walks

Factorio's best move in this family is **personal logistics**: request slots and
auto-trash slots on the player's own inventory, plus a **personal roboport** worn
in the armor grid so the bots come with you. Your inventory stops being a bag you
manage and becomes a **requester chest that follows you around** — the routing
travels with the actor instead of sitting still in a warehouse.

Two things fall out of that, and both generalize past Factorio.

**A request and an auto-trash are the same knob with opposite signs.** A request
slot is a *min* — keep me topped up to 20 iron plate — and a trash slot is a
*max*: anything above this, take it away. One threshold pair per item, on one
axis, and the whole personal inventory policy is that pair repeated. "Trash
unrequested" is the blanket form: **anything I didn't ask for is not mine**,
which is the strongest opt-out policy in this entire document and the only one
stated as a negative. A standing request is a bid; auto-trash is a standing
*ask*. Both are advertisements, which is why this belongs in the same auction as
everything else.

**Worn equipment is a typed bag whose contents are mixins.** The armor grid holds
modules that change what you can do, so it is simultaneously a container (slots,
sizes, filters) and a set of live delegation edges — the
[buff graph](GAME-PIECES.md#buffs-mixins-with-expiration-dates) with an
inventory UI. Take the roboport out of your armor and the capability leaves with
it, no cleanup, because the capability was never cached anywhere but the slot.

[factorio-logistics-protocol.md](factorio-logistics-protocol.md) has
`personal_requests` on the player already; it has no trash side yet, so half the
knob is missing.

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
- **A personal request list and an auto-trash list**, which is the Factorio
  personal-logistics move applied to a working set: *keep these near me* as a
  min, *take away anything above this* as a max, and *anything I didn't ask for
  is not mine* as the blanket policy. Every desktop makes you clean up by hand
  because it has no idea what you consider yours. A declared working set with a
  trash threshold is the smallest thing that would fix it, and it is the same
  min/max pair a requester chest uses.
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
