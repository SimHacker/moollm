# Postal System — Browser UI Design

> *"Getting mail should feel like opening a present."*
> — Randy Pausch

---

## The Vision

The postal system isn't just a feature — it's a **core loop**:

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│    📬 CHECK  →  📨 READ  →  🎁 RECEIVE  →  ✍️ REPLY         │
│         ↑                                        │           │
│         └────────────────────────────────────────┘           │
│                                                              │
│              THE JOY OF CORRESPONDENCE                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## UI Components

### 1. The Mailbox Icon (Always Visible)

```
┌──────┐
│ 📬 3 │  ← Red badge = unread count
└──────┘
```

- **Idle:** Mailbox closed
- **New mail:** Mailbox flag up, gentle bounce animation
- **Click:** Opens mail panel
- **Hover:** Preview of most recent letter

### 2. The Mail Panel (Slide-in Sidebar)

```
┌────────────────────────────────────────┐
│  📬 MAIL                          [✕] │
├────────────────────────────────────────┤
│ ┌────────────────────────────────────┐ │
│ │ 💌 Mom            ★ NEW           │ │
│ │ "Your First Quest"                 │ │
│ │ Dearest child, I need you to...   │ │
│ └────────────────────────────────────┘ │
│ ┌────────────────────────────────────┐ │
│ │ 📨 Don Hopkins                     │ │
│ │ "Found the key!"                   │ │
│ │ It was in the chest all along...  │ │
│ └────────────────────────────────────┘ │
│ ┌────────────────────────────────────┐ │
│ │ 📨 Mysterious Stranger             │ │
│ │ "A warning..."                     │ │
│ │ Beware the grue...                 │ │
│ └────────────────────────────────────┘ │
├────────────────────────────────────────┤
│ [📝 Compose]  [📤 Drafts (2)]        │
└────────────────────────────────────────┘
```

**Features:**
- Unread letters have ★ NEW badge
- Letters from Mom have special styling (💌)
- Click letter → opens reading view
- Drag letter → can forward or archive

### 3. Letter Reading View (Modal)

```
┌─────────────────────────────────────────────────────────────┐
│                                                    [✕]     │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                     📜                                │ │
│  │                                                       │ │
│  │   From: Mom 💌                                       │ │
│  │   To: You                                            │ │
│  │   Subject: Your First Quest                          │ │
│  │                                                       │ │
│  │   ─────────────────────────────────────────────────   │ │
│  │                                                       │ │
│  │   Dearest child,                                     │ │
│  │                                                       │ │
│  │   I know you've just woken up in that strange        │ │
│  │   chamber, but I need you to find something for      │ │
│  │   me. There's a brass key somewhere in the maze      │ │
│  │   — it belonged to your grandmother.                 │ │
│  │                                                       │ │
│  │   Find it and bring it home.                         │ │
│  │                                                       │ │
│  │   With all my love,                                  │ │
│  │   Mom                                                │ │
│  │                                                       │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  📎 Attachments:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  🗺️ Old Map          [📥 Take]                      │   │
│  │  💰 50 Gold          [📥 Take]                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  🎯 Quest Created: "Find Grandmother's Key"                │
│                                                             │
│  [↩️ Reply]  [➡️ Forward]  [🗑️ Archive]                   │
└─────────────────────────────────────────────────────────────┘
```

**Features:**
- Letter has parchment/paper aesthetic
- Mom's letters have special warm styling
- Attachments clickable to take/view
- Quest banner appears if letter creates goal
- Sound effect when taking attachments (✨ sparkle!)

### 4. Attachment Receiving Animation

When you click "Take" on an attachment:

```
     💰
      ↓
   ✨✨✨
      ↓
  ┌─────────┐
  │Inventory│
  └─────────┘
  
  +50 Gold!
```

**The Delight:**
- Item floats out of letter
- Sparkle trail as it moves
- Lands in inventory with satisfying sound
- "+50 Gold!" notification

### 5. Compose Letter UI

```
┌─────────────────────────────────────────────────────────────┐
│  ✍️ COMPOSE LETTER                                  [✕]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  To:    [Mom ▼] [+ Add recipient]                          │
│                                                             │
│  Subject: [Found it!                    ]                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ Mom!                                                │   │
│  │                                                     │   │
│  │ I found the key! It was in the old chest in the    │   │
│  │ maze. Sending it with this letter.                 │   │
│  │                                                     │   │
│  │ Love,                                               │   │
│  │ [Your name]                                         │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📎 Attachments:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  🔑 Brass Key    [✕ Remove]                         │   │
│  │                                                     │   │
│  │  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   │   │
│  │    Drag items here to attach                        │   │
│  │  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  [💾 Save Draft]                    [📤 Send Now]          │
└─────────────────────────────────────────────────────────────┘
```

**Features:**
- Recipient dropdown with known contacts
- Drag-and-drop from inventory to attach
- Attached items show with remove button
- Save Draft → to outbox
- Send Now → immediate delivery

### 6. The "Mail to Vault" Quick Action

Drag item to mailbox icon → Modal:

```
┌───────────────────────────────────────┐
│  📦 SEND TO STORAGE                   │
├───────────────────────────────────────┤
│                                       │
│  Item: 💰 500 Gold                    │
│                                       │
│  Destination:                         │
│  ○ 🏦 Main Vault                      │
│  ○ 📦 Treasure Room                   │
│  ○ 🏠 Home Storage                    │
│                                       │
│  [Cancel]           [📤 Send]         │
└───────────────────────────────────────┘
```

---

## Micro-Interactions

### New Mail Notification

```css
@keyframes mailBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.mailbox.has-new-mail {
  animation: mailBounce 0.5s ease-in-out infinite;
}
```

### Letter Open Animation

```css
@keyframes letterUnfold {
  0% { 
    transform: perspective(500px) rotateX(-90deg);
    opacity: 0;
  }
  100% { 
    transform: perspective(500px) rotateX(0);
    opacity: 1;
  }
}

.letter-content {
  animation: letterUnfold 0.4s ease-out;
}
```

### Attachment Float Animation

```javascript
function takeAttachment(item, targetInventory) {
  const itemEl = createFloatingItem(item);
  const start = getAttachmentPosition();
  const end = getInventoryPosition();
  
  animateFloat(itemEl, start, end, {
    duration: 600,
    easing: 'easeOutCubic',
    trail: createSparkleTrail,
    onComplete: () => {
      playSound('item-receive');
      showNotification(`+${item.name}!`);
      addToInventory(item);
    }
  });
}
```

---

## Mom's Special Styling

Letters from Mom get extra love:

```css
.letter.from-mom {
  background: linear-gradient(
    135deg,
    #fff5e6 0%,
    #ffe4c4 100%
  );
  border: 2px solid #d4a574;
  box-shadow: 0 4px 12px rgba(212, 165, 116, 0.3);
}

.letter.from-mom::before {
  content: '💌';
  position: absolute;
  top: -12px;
  left: 20px;
  font-size: 24px;
}

.letter.from-mom .signature {
  font-family: 'Caveat', cursive;
  font-size: 1.4em;
  color: #8b4513;
}
```

---

## Quest Integration

When a letter creates a quest:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  📜 Letter content...                                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  ✨ NEW QUEST ✨                                            │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  🎯 Find Grandmother's Key                            │ │
│  │                                                       │ │
│  │  Find the brass key in the maze and return           │ │
│  │  it to Mom.                                           │ │
│  │                                                       │ │
│  │  Reward: Family Locket 🏅                             │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  [📋 View in Quest Log]                                    │
└─────────────────────────────────────────────────────────────┘
```

Sound effect: Quest jingle!

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `M` | Toggle mail panel |
| `C` | Compose new letter |
| `R` | Reply to current letter |
| `←` / `→` | Navigate letters |
| `Enter` | Open selected letter |
| `Esc` | Close panel/modal |
| `D` | Delete/archive letter |

---

## Sound Design

| Event | Sound |
|-------|-------|
| New mail arrives | Soft chime + mailbox flag animation |
| Open letter | Paper unfolding |
| Take attachment | Sparkle/magic pickup |
| Send letter | Whoosh + seal stamp |
| Quest created | Triumphant jingle |
| Mom's letter | Extra warm chime |

---

## Mobile Design

On mobile, the mail panel becomes full-screen:

```
┌─────────────────────────┐
│ ← MAIL              📝  │
├─────────────────────────┤
│                         │
│ ┌─────────────────────┐ │
│ │ 💌 Mom         NEW  │ │
│ │ Your First Quest    │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ 📨 Don Hopkins      │ │
│ │ Found the key!      │ │
│ └─────────────────────┘ │
│                         │
└─────────────────────────┘
```

Swipe left on letter → Archive
Swipe right on letter → Reply

---

## Implementation Plan

### Phase 1: Core Mail UI
- [ ] Mail panel component
- [ ] Letter list view
- [ ] Letter reading view
- [ ] Unread badge

### Phase 2: Attachments
- [ ] Attachment display in letters
- [ ] Take attachment action
- [ ] Float animation to inventory
- [ ] Attachment types (items, gold, buffs)

### Phase 3: Compose
- [ ] Compose modal
- [ ] Recipient selector
- [ ] Drag-and-drop attachments
- [ ] Save draft / Send now

### Phase 4: Polish
- [ ] Mom's special styling
- [ ] Quest creation animation
- [ ] Sound effects
- [ ] Keyboard shortcuts
- [ ] Mobile responsive

### Phase 5: Storage Integration
- [ ] Mail to vault quick action
- [ ] Storage room selection
- [ ] Transfer animations

---

## The Joy Factor

What makes this FUN:

1. **Anticipation** — Seeing the mailbox bounce
2. **Discovery** — What did Mom send?
3. **Reward** — Taking attachments feels GOOD
4. **Progress** — Quests created from letters
5. **Connection** — Mom's warmth in her writing
6. **Agency** — Composing and sending replies
7. **Surprise** — Unexpected letters from NPCs

**WILL WRIGHT:** "The best systems create anticipation loops. The mailbox is a slot machine that's always kind."

---

## Code Structure

```
browser/
├── components/
│   ├── mail/
│   │   ├── MailIcon.js          # Mailbox with badge
│   │   ├── MailPanel.js         # Slide-in sidebar
│   │   ├── LetterList.js        # List of letters
│   │   ├── LetterView.js        # Reading modal
│   │   ├── ComposeModal.js      # Write new letter
│   │   ├── AttachmentItem.js    # Single attachment
│   │   └── QuestBanner.js       # Quest created notice
│   └── ...
├── animations/
│   ├── floatToInventory.js      # Item float animation
│   ├── letterUnfold.js          # Letter open animation
│   └── sparkleTrail.js          # Sparkle effect
├── sounds/
│   ├── mail-arrive.mp3
│   ├── letter-open.mp3
│   ├── item-take.mp3
│   ├── letter-send.mp3
│   └── quest-created.mp3
└── styles/
    ├── mail.css
    └── letter-from-mom.css
```

---

**The postal system isn't just a feature. It's GAMEPLAY.**
