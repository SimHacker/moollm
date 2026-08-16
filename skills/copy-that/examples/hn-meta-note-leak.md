# The founding incident — a private note nearly published inside an HN post (July 2026)

The case that created this skill. Programming by example: this is what fence discipline prevents.

## What happened

A long Hacker News comment sat in a chat session as flowing text between `---` separators.
After the draft, a private editorial note was appended, flagging that one of the draft's
historical claims was stated more strongly than the source supported.

The author selected the draft to copy into HN. The selection swept in the accuracy note,
because the only boundary between post and note was a paragraph break, and paragraph breaks
are invisible at copy time. The note went live inside the published post.

## How it was caught

Luck. The HN edit window (~2 hours) was still open; the leak was spotted in the pasted-back
edit box and the paragraph was deleted in time, then the fix was verified via the HN API:
the paragraph was gone from the live comment.

## What fence discipline would have done

The post ships inside one fenced `text` block with a copy button that copies exactly the post.
The accuracy note lives outside the fence as ordinary chat prose. There is no way to press the
copy button and get the note.

Additional failure this case exposed: the draft was rendered markdown chat text, so copying it
from the rendered chat also risked losing the deliberate blank-line link formatting HN depends
on. Fenced plain text preserves it byte-for-byte.

## Rules this example wrote

1. One fenced block per artifact; the fence is the airlock (SKILL.md protocol step 5).
2. Out-of-band notes never sit inside or adjacent-and-unlabeled; they go in prose clearly
   outside the fence.
3. Preflight includes reading the fence contents as the audience: anything that addresses the
   author rather than the readers is a leak.
