# The founding incident — a private note nearly published inside an HN post (July 2026)

The case that created this skill. Programming by example: this is what fence discipline prevents.

## What happened

An agent drafted a long Hacker News comment for Don (a history of Lisp compilation, Elk, Guile,
and the Tcl War). The draft was delivered as flowing chat text between `---` separators. After
the draft, the agent appended a private editorial note:

> One flag on accuracy: the Remote Agent fix was a race condition patch developed and verified
> on the ground with the spacecraft REPL used to diagnose and confirm, so "diagnosed and fixed
> it through a REPL running on the spacecraft" is the strong version of the claim. [...]

Don selected the draft to copy into HN. The selection swept in the accuracy note, because the
only boundary between post and note was a paragraph break, and paragraph breaks are invisible at
copy time. The note went live inside the published post.

## How it was caught

Luck. The HN edit window (~2 hours) was still open; the agent spotted the leak in the pasted-back
edit box, flagged it, and Don deleted the paragraph in time. The agent then verified the fix via
the HN API: the paragraph was gone from the live comment.

## What fence discipline would have done

The post ships inside one fenced `text` block with a copy button that copies exactly the post.
The accuracy note lives outside the fence as ordinary chat prose. There is no way to press the
copy button and get the note.

Additional failure this case exposed: the draft contained formatted markdown chat text, so
copying it from the rendered chat also risked losing the deliberate blank-line link formatting HN
depends on. Fenced plain text preserves it byte-for-byte.

## Rules this example wrote

1. One fenced block per artifact; the fence is the airlock (SKILL.md protocol step 5).
2. Out-of-band notes never sit inside or adjacent-and-unlabeled; they go in prose clearly
   outside the fence.
3. Preflight includes reading the fence contents as the audience: anything that addresses the
   human rather than the readers is a leak.
