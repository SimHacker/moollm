# The Maze

> *"You are in a maze of twisty little passages, all alike."*
> — Colossal Cave Adventure, 1976

> *"You are an amazingly twisted little ass, always different."*
> — Graffiti scratched into a wall, author unknown (likely eaten) 

A proper adventure needs a proper maze.

---

## ⚠️ WARNING: GRUES

**The maze is DARK.** All rooms have `lighting: none`.

If you enter without a **lit lamp** in your inventory:

```
It is pitch black. You are likely to be eaten by a grue.

🎵 "If this predicament seems particularly cruel,
    consider whose fault it could be:
    not a torch or a match in your inventory." 🎵

You have been eaten by a grue.
```

**GET LAMP before entering.** This is not a suggestion.

*([Get Lamp](http://www.getlamp.com/) — Jason Scott's documentary on text adventures)*

### The Official Grue Anthem

**[MC Frontalot - "It Is Pitch Dark"](https://www.youtube.com/watch?v=4nigRT2KmCE)**

> *"Thanks, Grampa, for buying it. Now my life's ruined.
> Twenty-two years later, head's infested: got the grue in."*

Each maze room quotes a different verse when you die. Nerdcore is the future.

---

## The Rooms

Ten rooms, all "alike" (but each with a distinguishing feature):

| Room | Feature | Notable Exits |
|------|---------|---------------|
| [room-a/](./room-a/) | Puddle (damp) | **S→start**, N→C, E→B, W→D |
| [room-b/](./room-b/) | Echo | N→D, S→C, E→A, W→C |
| [room-c/](./room-c/) | Scratch marks | N→B, S→D, E→D, W→A |
| [room-d/](./room-d/) | Golden glow | **N→end**, S→A, E→B, W→C |
| [room-e/](./room-e/) | Cobwebs | N→F, S→B, E→G, W→C |
| [room-f/](./room-f/) | Cold spot + **100 GOLD** 💰 | N→H, S→E, E→A, W→I |
| [room-g/](./room-g/) | Carved face | N→I, S→D, E→J, W→E |
| [room-h/](./room-h/) | Mushrooms (glow) | N→J, S→F, E→B, W→D |
| [room-i/](./room-i/) | Skeleton (empty lamp!) | N→C, S→G, E→F, **W→J** |
| [room-j/](./room-j/) | **LAMP OIL VENDOR** 🏪 | N→D, S→H, E→I, W→G |

### 🏪 The Lamp Oil Vendor

In **room-j** stands a battered vending machine: the **ACME LAMP REFUELING CO.**

> *"Don't Let the Grue Get You!"™*

| Item | Cost | Effect |
|------|------|--------|
| Lamp Oil Refill | 1 gold | Refills to 400 oil |
| Deluxe Refill | 2 gold | Refills to 800 oil |
| Premium Glow Juice | 5 gold | 1000 oil + blue glow (grues hate it) |

**Pro tip:** The skeleton in room-i was pointing west toward room-j. They were *so close* to salvation. Their lamp was empty. Don't be like them.

### 💰 The Gold Pile (room-f)

In **room-f** (the cold spot), you'll find **100 gold coins** scattered on the floor.

This was the skeleton's money! They dropped it when the grue got them. The cold room drains lamp oil **twice as fast** — they didn't know that. Their lamp died here, and they never made it to the vendor.

Their loss is your gain. 100 gold = 100 refills. You're set for life (or at least this adventure).

**Warning:** The cold affects your lamp too! Move quickly through room-f.

---

## The Solution

**Shortest path (still works!):**
```
From start:  NORTH → room-a (the damp one)
From room-a: WEST  → room-d (follow the glow!)
From room-d: NORTH → end (TREASURE!)
```

**Or wander and MAP with food!** You now have 20 food items from the
kitchen and 10 maze rooms. Drop different foods to mark each room.
This is the CLASSIC adventure game technique!

```
> drop cheese
Dropped: Wheel of Aged Cheese

(Later, when you return to this room...)

> look
You see: Wheel of Aged Cheese
"Ah! I've been here before!"
```

---

## The Classic Technique

How to map a maze of twisty passages:
1. Drop items to mark rooms
2. Move in each direction, note which room you reach
3. Build a map on paper (or in your YAML files)

Or just read this README. We won't judge.

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [adventure-1/](../) |
| 🚪 Start | [../start/](../start/) |
| 🏆 End | [../end/](../end/) |
