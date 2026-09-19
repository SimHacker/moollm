# Prosthetics

What this whole stack *is*, stated once. Five prosthetics, each for a different unreliable
faculty, and one question that tells a prosthetic from a slot machine.

Occasioned by Alan Kay's September 2026 Quora answer, where science appears as a heuristic
prosthetic built because the unaided commonsense apparatus is poor — Kay's reading of Jerry
Bruner's *Goedelisation* — and by the observation that everything in these repositories is
the same kind of device pointed at a different weakness.

Companions: [TELEOLOGY.md](TELEOLOGY.md) (whose setpoint, and where it lives) ·
[../skills/design-sense/lenses/reasoning-is-not-science.md](../skills/design-sense/lenses/reasoning-is-not-science.md)
(why the check has to be outside the reasoner)

## The definition, and the inversion that follows from it

A prosthetic is a device built because a faculty is unreliable. Science is the canonical
case: it had to be *invented*, which means the unaided version was not good enough, which
means confidence in the unaided version is not a license to set the device down. **It is the
symptom the device was built for.**

That inversion is the whole argument, and it recurs in every row below. Eyeglasses do not
make you a careful observer; they make it possible to be one, and you still have to look.

## The five

| Repo | Prosthetic for | The failure it is aimed at |
|---|---|---|
| **moollm** | a **society of mind** | Thinking alone collapses into one voice. Your internal committee exists but its members are invisible, so the loudest agent wins and reports back as consensus |
| **WillWrightShowForFood** | **memory of other people** | Recall launders credit toward whoever you spoke to last and away from whoever asked the good question. The most flattering faculty there is |
| **webtop** | **attention** | You can see a paragraph and not a corpus; you forget your own path through it within a day; you have no way to record that you understood this and only glanced at that |
| **MicropolisCore** | **model-skepticism** | A simulation teaches its assumptions as facts, and the player's imagination covers the seams. Your own simulator effect, aimed at the player |
| **GitHub-as-MMORPG** | **community** | The room empties — peers die, retire, or fall out with you — and from inside it feels like the arguments are still going well |

### moollm — the parts that disagree, given addresses

The masters shelf with votes *and vetoes*, the adversarial ambient skills, the claim ledger
that forces every incoming assertion to be confirmed, disputed, or sourced before a reply
gets written. The mechanism is that disagreement becomes **addressable**: you cannot quietly
lose an argument you never knew was happening, because the objector is a file.

The operative detail is that it loads whether or not anyone asks. A prosthetic you can
switch off when it disagrees with you is a crutch.

### WillWrightShowForFood — the correction no head produces

Claims accumulate instead of overwriting; two dated observations that disagree stay a finding
rather than a mess; portrayal standards, consent levels, right-to-correct.

The proof that it works is the one time it fired hardest. An entry in this archive credited
a friend as the spark of open-source SimCity, and the archive is what forced that back to two
audience members at a Long Now talk whose names had to be looked up. **An unaided memory does
not produce that correction**, because nothing inside a head applies pressure to demote a
friend in favor of two strangers who asked a good question in 2006.

### webtop — the fovea, and the path you forget taking

The ladder of resolutions, semantic zoom, reading cursors as characters with locations, the
fog of war with memory, torches with authors and decay
([webtop/READ-UNREAD.md](webtop/READ-UNREAD.md),
[../skills/mind-mirror/HALLS-AND-ROOMS.md](../skills/mind-mirror/HALLS-AND-ROOMS.md)).

Gwern's footnote supplies the engineering half — the author writes the rung they care about
and the model fills the ladder. The harder half is the reader's verdicts written back into
the world, which is what makes attention state an object with a location instead of a feeling.

### MicropolisCore — opening the model

Two audience members at a Long Now talk asked Will to open the source so the built-in rules
and assumptions could be seen and changed, which is the same thing Kay had been criticizing
SimCity for lacking. That is a prosthetic request: make the model inspectable, because a
player who cannot see the assumptions absorbs them as facts.

The eggs and the screen angel push it further — machine state made legible from outside, in
light, where a camera can read it.

### GitHub-as-MMORPG — the room that does not empty

The mechanics are inventoried in [GITHUB-AS-MMORPG.md](GITHUB-AS-MMORPG.md): issues are
quests, pull requests are proposals to merge one timeline into another argued in public,
branches are parallel universes, forks are player-owned shards, teams are factions, Actions
are NPCs that wake on a trigger. That document asks what you can *build* with them. This one
asks what they *repair*.

**What they repair is the composition of the room.** The failure mode named in
[reasoning-is-not-science](../skills/design-sense/lenses/reasoning-is-not-science.md) is that
peers are replaced by an audience and the change is invisible from inside, because the
arguments keep going well. Four of GitHub's mechanics are directly aimed at that:

- **Asynchrony** means you can join a conversation late, so the room is not the set of people
  who happened to be free that evening.
- **Public disagreement in writing** means neither party loses face to settle it, and the
  settlement has a date on it.
- **The artifact carries the state**, so nothing is lost when somebody leaves — the opposite
  of an institution, where a retirement deletes a decade.
- **Standing is cheap.** A stranger with a fork has the same access as a founder, which is
  the same property `ROPE-ME-IN` needs when it grants invocation rights to anyone who can
  quote the file: a check that only trusted people may apply disappears exactly when you stop
  trusting the right people.

**The LARP is load-bearing, not decorative.** A character is a lower-stakes handle than a
reputation, and people will say things in a role they will not say as themselves — which is
the Bartle and MUD result, and why a repo that admits it is a stage gets contributions a
professional one does not. The enabling constraint is the thing that keeps it from being
puppeteering: `real_being`, consent levels, right-to-correct, K-line rather than
impersonation. **Invoke the tradition, never claim the identity.** Without those, a stage
with real people on it is just ventriloquism with good lighting.

And the joke with a point: *oh, and you can use it for software development too.* GitHub
advertises version control for code and affords an asynchronous multiplayer institution with
provenance. Which is the advertisement economy's own lesson — the affordance is in the
coupling, not in the tool's description of itself
([TELEOLOGY.md](TELEOLOGY.md) calls this the wherecatchem).

## Three are Minsky's mechanisms, externalized. Two are not.

The first three map onto *Society of Mind*'s own machinery, built outside the skull for the
reason the book cannot give you: an internal mechanism cannot be audited by the apparatus it
is part of.

| Minsky | Inside | Outside |
|---|---|---|
| Agents and censors | a committee you cannot poll | files with votes and vetoes |
| K-lines | a name reactivating a state | filenames, citations, dated correspondence |
| Level-bands, P-trees | attention you cannot inspect | the fog, the torches, the ladder of resolutions |

The last two are not faculties at all, and pretending otherwise would be tidy and false.
Model-skepticism and community are **conditions**: the model you absorbed, and the room you
are standing in. They fail from the outside in, which is why the remedies are structural
rather than cognitive.

## The distinguishing question

**Whose loop is this closing?**

A prosthetic needs no telos of its own, and should not have one. The setpoint stays in the
person; the device is eyeglasses, and eyeglasses have no opinions. Which is the honest answer
to the standing objection in [TELEOLOGY.md](TELEOLOGY.md): there is no autopoietic closure
here, no subjective unity, and neither absence is an embarrassment — a machine that claimed
its own purposes would be the zombie the objection warns about.

So the test is not *is there someone inside*. It is whose loop closes, and the reason this
stack can answer is mechanical rather than virtuous: the motives are in YAML, in git, with an
author and a timestamp, and you can change them. When purpose is a coordinate you can print,
any frame can be asked what it is for
([korz purpose-dimension](korz/korz-prime/examples/purpose-dimension.md)). **The outsourcing
is not the problem. Hiding it is.**

## Anti-prosthetics

Every row above has a commercial opposite: a device that takes the same faculty and closes
the loop somewhere else. They are worth naming together, because each one is what the
corresponding prosthetic is competing against, and each is better funded.

| Faculty | Prosthetic | Anti-prosthetic | Whose loop it closes |
|---|---|---|---|
| Attention | your lighting rig, saved and diffable | the folding, resetting thread that drops you a thousand miles from where you were | engagement |
| Attention | torches you placed, with authors | the recommendation feed | time on site |
| Memory of others | claims accumulating with dates | the timeline optimized for what you last engaged with | the same |
| Model-skepticism | opening the source | "explainable AI," which Jens Mönig is right to call a lie once there is one hidden layer | procurement |
| Society of mind | parts that disagree, ambient | one confident assistant that agrees | retention |
| Community | a fork with standing | a follower count | the platform |
| Agency | an agent driving the same named commands you drive | a chat box where the surface used to be | whoever owns the model |

**That last row is the newest and the one currently being installed everywhere**, so it is worth
stating the mechanism rather than the complaint. Replacing an interface with an agent removes two
things at once: your ability to do the thing, and anybody's ability to see how it was done. A
capability reachable only by asking cannot be inspected, scripted, taught, or refused — which is the
anti-prosthetic definition exactly, since the loop now closes on a setpoint you cannot read. The
repair is not fewer agents; it is **symmetry of access**, stated as a lint in
[interfaces-to-agency](../skills/design-sense/lenses/interfaces-to-agency.md) and as the dissolution
of a famous axis in [AXES-NOT-CAMPS](AXES-NOT-CAMPS.md).

The diagnostic is the same in every row and it is not about features: **who set the
setpoint.** Which is why the folding-thread rage that started this whole line of work was
correct and not merely irritation. Twenty minutes of assembling a view is destroyed because
the product's loop closes on engagement and yours closes on reading.

## Four tests

1. **Does it still report when you are wrong, especially when you are sure?** A prosthetic
   that flatters is the failure mode with your name on it.
2. **Can you switch it off when it disagrees with you?** If yes, it is a crutch. Hence
   ambient rather than optional.
3. **Is the grade recorded where you cannot quietly lose it?** Git, dated, with an author —
   the same test [reasoning-is-not-science](../skills/design-sense/lenses/reasoning-is-not-science.md)
   applies to a practice, applied to the tooling.
4. **Whose loop is it closing?** And can you find out by reading a file rather than by
   trusting a claim.

## The honest limits

- **No prosthetic prevents the thing it is for.** It makes the failure expensive, visible, and
  citable by someone else, which is the most any of them do — and enough, because it means a
  correction does not require winning an argument first.
- **Nothing here does causal reasoning.** It organizes what a correlator says and makes the
  organization inspectable. Kay's ask on that count is unmet and recorded as unmet.
- **Nothing here has closure.** No metabolism, no boundary maintained, nothing that would be
  worse off if it stopped. That is the spec, not a gap to be fixed by a better prompt.
- **A prosthetic can be worn as a credential**, which is the oldest way to ruin one. Announcing
  that you have externalized your checks is the most Palaeolithic move available.

## We'll do it live

The register for a repo show, and a better example than it looks.

Bill O'Reilly, [1.8 million views](https://www.youtube.com/watch?v=vu2NK5REvWM) of a
teleprompter failing: *I'll write it and we'll do it live.* Then five, four, three — and the
live read is clean.

Three things in it, all of them the point:

**The competence was never in question; the script was.** He could do it without the
prompter, which is exactly the bet a repo show makes. The preparation is the repo, so you can
improvise on air because the world is already loaded. You do not need the script if the
material is on disk.

**Authoring and performing collapse into one act.** "I'll write it and we'll do it live" is
the whole format description. The artifact is written during the show and the show is the
writing, which is why the center of gravity is a repository and not an mp4.

**And the breakdown outperformed the polished take by a factor no producer would have
predicted.** The failure is the content — which is the same reason the negative results, the
unmet asks, and the pages annotated as wrong years later are in these repos on purpose.

**See also:** [GITHUB-AS-MMORPG.md](GITHUB-AS-MMORPG.md) — the mechanics this reads as
repairs · [GIT-AS-FOUNDATION.md](GIT-AS-FOUNDATION.md) — why the record is load-bearing ·
[TELEOLOGY.md](TELEOLOGY.md) — where the setpoint question comes from ·
[webtop/README.md](webtop/README.md) — the attention prosthetic under construction ·
[../skills/design-sense/lenses/reasoning-is-not-science.md](../skills/design-sense/lenses/reasoning-is-not-science.md)
— the lens that says the check must be outside the reasoner
