# Postal System: Browser UI

How the [postal skill](SKILL.md) looks in a browser front end. The data model (letters, texts,
attachments, inbox, outbox, delivery) lives in SKILL.md; this file covers only presentation.

## The loop

Check, read, take, reply. Mail is a core gameplay loop, not a settings panel. Letters carry
objects and goals, so opening one changes the world: items arrive, quests start, and replying
sends things back.

## Components

- **Mailbox icon**, always visible, with an unread count. The flag goes up when new mail
  arrives. Clicking it opens the mail panel.
- **Mail panel**: a list of letters showing sender, subject, the first line, and an unread
  marker. On mobile it goes full screen.
- **Letter view**: the letter itself with its attachments. Each attachment has a Take action
  that moves the item into inventory. If the letter assigns a goal, the quest appears inline
  with a link to the quest log.
- **Compose**: recipient chosen from known contacts, subject, body, and attachments dragged in
  from inventory. Save Draft puts it in the outbox; Send hands it to delivery.
- **Drag to mailbox**: dropping an item on the mailbox icon offers to mail it to one of the
  player's storage locations.

## Feedback

Taking an attachment should visibly move the item from the letter into inventory. Arrivals,
sends, and new quests each get a short, distinct sound. Senders can have their own letter style,
so a letter from someone close feels different from a system notice.

## Principles

- **Anticipation**: unread mail is a reason to come back.
- **Mail as transport**: attachments are real objects moving between rooms and characters.
- **Goals arrive by post**: NPCs hand out and update quests through letters.
- **Replies are actions**: writing back can deliver items, complete quests, and change
  relationships.
