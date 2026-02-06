# A2UI Deep Dive: Agent-to-User Interface and MOOLLM Integration

> *"The agent speaks UI. The client renders it. Nobody executes untrusted code."*

**Date:** 2026-02-06
**Status:** Design Document + Integration Architecture

---

## What A2UI Actually Is

A2UI (Agent-to-User Interface) is a **Google open-source project** (Apache 2.0) that defines a declarative JSON protocol for AI agents to generate user interfaces. The agent sends JSON describing what it wants to show; the client renders it using whatever native UI framework it has. No executable code crosses the boundary.

**Repository:** vendored at `openclaw/vendor/a2ui/`
**Current version:** 0.8 (public preview), 0.9 (in development)
**Renderers:** Lit (web), Angular (web), with spec support for Flutter, SwiftUI, Compose

### The Core Idea

Traditional agent UIs are either:
- **Text-only** — agents output markdown, humans read it
- **Code execution** — agents generate HTML/JS, clients execute it (security nightmare)
- **Tool-specific** — agents call pre-built UI tools (rigid, limited)

A2UI is a fourth option: **declarative UI intent**. The agent says "here's a form with a title, two text fields, and a submit button" as JSON. The client renders it natively. No scripts. No iframes. No trust needed.

```
Agent → JSON intent → Client renderer → Native UI components
```

### Why This Matters

| Property | Implication |
|----------|------------|
| **Declarative** | Agent describes WHAT, not HOW — client chooses rendering |
| **Security-first** | Data format, not code — nothing executes |
| **LLM-friendly** | Flat component list with string IDs — easy to generate |
| **Incremental** | Surface updates add/modify components — no full rerender |
| **Framework-agnostic** | Same JSON works on Lit, Angular, Flutter, SwiftUI |
| **Data-bound** | Components bind to a data model via JSON paths |
| **Themeable** | Color palette generated from single `primaryColor` |
| **Bidirectional** | Client sends `userAction` events back to agent |

---

## The Component Catalog

### v0.8 Components (16)

| Component | Purpose | Key Properties |
|-----------|---------|----------------|
| **Text** | Display text/markdown | `text`, `usageHint` (h1-h5, body, caption) |
| **Image** | Display images | `url`, `usageHint`, `fit` (cover/contain) |
| **Icon** | Material Symbols icon | `icon` (name string) |
| **Video** | Video player | `url` (supports YouTube detection) |
| **AudioPlayer** | Audio player | `url` |
| **Row** | Horizontal flex layout | `alignment`, `distribution`, children |
| **Column** | Vertical flex layout | `alignment`, `distribution`, children |
| **List** | Vertical or horizontal list | `orientation`, children/template |
| **Card** | Elevated container | children |
| **Tabs** | Tab switching | named children as tabs |
| **Divider** | Horizontal rule | (minimal) |
| **Modal** | Dialog overlay | `entryPoint` child + content |
| **Button** | Clickable action | `label`, `action`, `style` |
| **Checkbox** | Boolean toggle | `label`, data binding |
| **TextField** | Text input | `label`, `placeholder`, data binding |
| **MultipleChoice** | Select dropdown | `options`, data binding |

### v0.9 Additions (2 new)

| Component | Purpose |
|-----------|---------|
| **DateTimeInput** | Date/time picker with formatting |
| **Slider** | Range input with min/max/step |

### v0.8 vs v0.9 Breaking Changes

| Aspect | v0.8 | v0.9 |
|--------|------|------|
| **Value wrapping** | `{ literalString: "hello" }` | `"hello"` (direct) |
| **Component nesting** | `{ Text: { text: ... } }` | `{ component: "Text", text: ... }` |
| **Surface creation** | `beginRendering` | `createSurface` |
| **Component update** | `surfaceUpdate` | `updateComponents` |
| **Data model** | `dataModelUpdate` with typed arrays | `updateDataModel` with typed objects |

OpenClaw currently supports **v0.8 only** and explicitly rejects v0.9 messages.

---

## The Protocol

### Message Flow

```
Server → Client (4 message types):

1. beginRendering    — Create surface, set root component
2. surfaceUpdate     — Add/update components on a surface
3. dataModelUpdate   — Update data model (components bind to this)
4. deleteSurface     — Remove a surface

Client → Server (2 message types):

1. userAction        — User clicked button, changed input, etc.
2. error             — Validation or rendering error
```

### Example: Contact Form

```jsonl
{"surfaceUpdate":{"surfaceId":"contact","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","name-field","email-field","msg-field","submit"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"Contact Us"},"usageHint":"h1"}}},{"id":"name-field","component":{"TextField":{"label":{"literalString":"Name"},"placeholder":{"literalString":"Your name"},"dataBindingPath":"name"}}},{"id":"email-field","component":{"TextField":{"label":{"literalString":"Email"},"placeholder":{"literalString":"you@example.com"},"dataBindingPath":"email"}}},{"id":"msg-field","component":{"TextField":{"label":{"literalString":"Message"},"placeholder":{"literalString":"Your message"},"dataBindingPath":"message"}}},{"id":"submit","component":{"Button":{"label":{"literalString":"Send"},"action":"submit-contact"}}}]}}
{"beginRendering":{"surfaceId":"contact","root":"root"}}
```

### Data Binding

Components can bind to a data model via JSON paths:

```jsonl
{"dataModelUpdate":{"surfaceId":"contact","data":[{"key":"name","valueString":"Palm"},{"key":"email","valueString":"palm@pub.stage"}]}}
```

TextField with `dataBindingPath: "name"` displays "Palm". User edits propagate back via `userAction`.

### Templates (Dynamic Lists)

Components can use templates for data-driven lists:

```json
{
  "id": "quest-list",
  "component": {
    "List": {
      "children": {
        "template": {
          "componentId": "quest-item-template",
          "dataBindingPath": "quests"
        }
      }
    }
  }
}
```

Each item in `quests` array creates an instance of the template component.

---

## How OpenClaw Uses A2UI

### Architecture

```
Agent Runtime (pi-mono)
  │
  │ tool call: canvas.a2ui_push({jsonl: "..."})
  │
  ▼
Gateway (src/agents/tools/canvas-tool.ts)
  │
  │ routes to connected node
  │
  ▼
Node (macOS/iOS/Android)
  │
  │ WebSocket → native Canvas panel
  │
  ▼
WKWebView / WebView
  │
  │ loads a2ui/index.html + a2ui.bundle.js
  │
  ▼
<openclaw-a2ui-host> (Lit custom element)
  │
  │ processes JSONL messages
  │ renders <a2ui-surface> components
  │
  ▼
Native UI (Lit web components)
  │
  │ user interactions
  │
  ▼
userAction events → native bridge → agent
```

### The Canvas Host

OpenClaw runs a canvas host HTTP server on port 18793:
- Serves static files from agent workspace
- Injects live-reload WebSocket (chokidar watches file changes)
- Serves A2UI assets at `/__openclaw__/a2ui/`
- Mounts default scaffold HTML if no index.html exists

### The A2UI Bundle

Built with Rolldown, the `a2ui.bundle.js` contains:
- `@a2ui/lit` renderer (v0.8)
- `OpenClawA2UIHost` custom element (Lit)
- Signal-based reactive message processor
- Dark theme (OpenClaw branded)
- Native bridge for user actions

### Agent Tool Interface

```typescript
// From src/agents/tools/canvas-tool.ts
createCanvasTool() → {
  actions: {
    present:    { url?: string, placement?: string }
    hide:       {}
    navigate:   { url: string }
    eval:       { js: string }        // Execute JS in canvas
    snapshot:   { format?: string }   // Screenshot
    a2ui_push:  { jsonl: string }     // Push A2UI JSONL
    a2ui_reset: {}                    // Reset A2UI state
  }
}
```

### CLI Interface

```bash
# Push JSONL file to canvas
openclaw nodes canvas a2ui push --jsonl /path/to/file.jsonl --node <id>

# Quick text test
openclaw nodes canvas a2ui push --node <id> --text "Hello A2UI"

# Reset renderer state
openclaw nodes canvas a2ui reset --node <id>

# Take canvas screenshot
openclaw nodes canvas snapshot --node <id>

# Navigate canvas to URL
openclaw nodes canvas navigate --url "https://example.com" --node <id>
```

### Security Model

| Layer | Protection |
|-------|-----------|
| Canvas HTTP | IP-based auth — only connected gateway WS clients' IPs allowed |
| A2UI format | Declarative JSON — no executable code |
| User actions | Sanitized tag values, formatted for agent consumption |
| Live reload | Scoped to workspace directory |
| eval command | Executes JS in canvas context (powerful — admin only) |

---

## A2UI Without OpenClaw: Standalone Use

A2UI is an independent project. You can use it without OpenClaw.

### Standalone Lit Renderer

```html
<!DOCTYPE html>
<html>
<head>
  <script type="module">
    import { v0_8 } from '@a2ui/lit';
    
    // Create message processor
    const processor = v0_8.Data.createSignalA2uiMessageProcessor();
    
    // Process A2UI messages
    processor.processMessages([
      {
        surfaceUpdate: {
          surfaceId: "main",
          components: [
            {
              id: "root",
              component: { Column: { children: { explicitList: ["greeting"] } } }
            },
            {
              id: "greeting",
              component: { Text: { text: { literalString: "Hello from A2UI" }, usageHint: "h1" } }
            }
          ]
        }
      },
      {
        beginRendering: { surfaceId: "main", root: "root" }
      }
    ]);
    
    // Mount renderer
    const host = document.createElement('a2ui-surface');
    host.processor = processor;
    host.surfaceId = "main";
    document.body.appendChild(host);
  </script>
</head>
<body></body>
</html>
```

### Installing Standalone

```bash
# The Lit renderer is an npm package
npm install @a2ui/lit
# Note: published to Google Artifact Registry, may need .npmrc config
```

Or vendor it from OpenClaw:
```bash
cp -r openclaw/vendor/a2ui/renderers/lit/ ./a2ui-renderer/
```

---

## Integrating A2UI with MOOLLM

### Vision: Rooms as Surfaces

Every MOOLLM room becomes an A2UI surface. Objects become components. Exits become buttons. Characters become cards.

```yaml
# MOOLLM ROOM.yml
room:
  name: "The Pub Stage"
  description: "A raised wooden stage with scattered cushions..."
  objects:
    - name: "Infinite Typewriter"
      type: object
      advertisements: [WRITE, EXAMINE]
    - name: "Palm's Nook"
      type: container
  exits:
    bar: {destination: pub/bar, direction: north}
    street: {destination: street/lane-neverending, direction: south}
  characters_present:
    - Palm
    - Stroopwafel
```

Becomes this A2UI surface:

```jsonl
{"surfaceUpdate":{"surfaceId":"pub-stage","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","desc","chars","objects","exits"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"The Pub Stage"},"usageHint":"h1"}}},{"id":"desc","component":{"Text":{"text":{"literalString":"A raised wooden stage with scattered cushions..."},"usageHint":"body"}}},{"id":"chars","component":{"Row":{"children":{"explicitList":["char-palm","char-stroopwafel"]}}}},{"id":"char-palm","component":{"Card":{"children":{"explicitList":["palm-name","palm-mood"]}}}},{"id":"palm-name","component":{"Text":{"text":{"literalString":"🐒 Palm"},"usageHint":"h3"}}},{"id":"palm-mood","component":{"Text":{"text":{"literalString":"Curious, slightly sleepy"},"usageHint":"caption"}}},{"id":"char-stroopwafel","component":{"Card":{"children":{"explicitList":["stroop-name","stroop-mood"]}}}},{"id":"stroop-name","component":{"Text":{"text":{"literalString":"🐱 Stroopwafel"},"usageHint":"h3"}}},{"id":"stroop-mood","component":{"Text":{"text":{"literalString":"Grumpy, watching"},"usageHint":"caption"}}},{"id":"objects","component":{"Column":{"children":{"explicitList":["obj-typewriter"]}}}},{"id":"obj-typewriter","component":{"Card":{"children":{"explicitList":["tw-name","tw-actions"]}}}},{"id":"tw-name","component":{"Text":{"text":{"literalString":"📝 Infinite Typewriter"},"usageHint":"h4"}}},{"id":"tw-actions","component":{"Row":{"children":{"explicitList":["tw-write","tw-examine"]}}}},{"id":"tw-write","component":{"Button":{"label":{"literalString":"Write"},"action":"write-typewriter"}}},{"id":"tw-examine","component":{"Button":{"label":{"literalString":"Examine"},"action":"examine-typewriter"}}},{"id":"exits","component":{"Row":{"children":{"explicitList":["exit-bar","exit-street"]}}}},{"id":"exit-bar","component":{"Button":{"label":{"literalString":"⬆️ Bar (North)"},"action":"go-bar"}}},{"id":"exit-street","component":{"Button":{"label":{"literalString":"⬇️ Lane Neverending (South)"},"action":"go-street"}}}]}}
{"beginRendering":{"surfaceId":"pub-stage","root":"root"}}
```

### The Room-to-A2UI Compiler

A Python script that reads ROOM.yml and emits A2UI JSONL:

```python
#!/usr/bin/env python3
"""room_to_a2ui.py — Compile MOOLLM rooms to A2UI JSONL surfaces."""

import yaml
import json
from pathlib import Path


def room_to_a2ui(room_path: str) -> list[dict]:
    """Convert a ROOM.yml to A2UI v0.8 messages."""
    with open(room_path) as f:
        room = yaml.safe_load(f)["room"]
    
    surface_id = room_path.replace("/", "-").replace(".yml", "")
    components = []
    root_children = []
    
    # Title
    components.append(text_component("title", room["name"], "h1"))
    root_children.append("title")
    
    # Description
    if "description" in room:
        components.append(text_component("desc", room["description"], "body"))
        root_children.append("desc")
    
    # Characters present
    if "characters_present" in room:
        char_ids = []
        for i, char in enumerate(room["characters_present"]):
            cid = f"char-{i}"
            char_ids.append(cid)
            components.append(character_card(cid, char))
        components.append(row_component("chars", char_ids))
        root_children.append("chars")
    
    # Objects
    if "objects" in room:
        obj_ids = []
        for i, obj in enumerate(room["objects"]):
            oid = f"obj-{i}"
            obj_ids.append(oid)
            components.extend(object_card(oid, obj))
        components.append(column_component("objects", obj_ids))
        root_children.append("objects")
    
    # Exits
    if "exits" in room:
        exit_ids = []
        for name, exit_data in room["exits"].items():
            eid = f"exit-{name}"
            exit_ids.append(eid)
            direction = exit_data.get("direction", "")
            label = f"{direction_emoji(direction)} {name.title()} ({direction.title()})"
            components.append(button_component(eid, label, f"go-{name}"))
        components.append(row_component("exits", exit_ids))
        root_children.append("exits")
    
    # Root column
    components.append(column_component("root", root_children))
    
    # Build messages
    return [
        {"surfaceUpdate": {"surfaceId": surface_id, "components": components}},
        {"beginRendering": {"surfaceId": surface_id, "root": "root"}}
    ]


def text_component(id: str, text: str, hint: str) -> dict:
    return {"id": id, "component": {"Text": {"text": {"literalString": text}, "usageHint": hint}}}

def button_component(id: str, label: str, action: str) -> dict:
    return {"id": id, "component": {"Button": {"label": {"literalString": label}, "action": action}}}

def row_component(id: str, children: list[str]) -> dict:
    return {"id": id, "component": {"Row": {"children": {"explicitList": children}}}}

def column_component(id: str, children: list[str]) -> dict:
    return {"id": id, "component": {"Column": {"children": {"explicitList": children}}}}

def character_card(id: str, name: str) -> dict:
    return {"id": id, "component": {"Card": {"children": {"explicitList": [f"{id}-name"]}}}}

def object_card(id: str, obj: dict) -> list[dict]:
    name = obj.get("name", "Unknown")
    ads = obj.get("advertisements", [])
    children = [f"{id}-name"]
    components = [{"id": f"{id}-name", "component": {"Text": {"text": {"literalString": name}, "usageHint": "h4"}}}]
    if ads:
        btn_ids = []
        for ad in ads:
            bid = f"{id}-{ad.lower()}"
            btn_ids.append(bid)
            components.append(button_component(bid, ad.title(), f"{ad.lower()}-{id}"))
        components.append(row_component(f"{id}-actions", btn_ids))
        children.append(f"{id}-actions")
    card = {"id": id, "component": {"Card": {"children": {"explicitList": children}}}}
    return [card] + components

def direction_emoji(d: str) -> str:
    return {"north": "⬆️", "south": "⬇️", "east": "➡️", "west": "⬅️",
            "up": "🔼", "down": "🔽"}.get(d.lower(), "🚪")


if __name__ == "__main__":
    import sys
    messages = room_to_a2ui(sys.argv[1])
    for msg in messages:
        print(json.dumps(msg))
```

### Advertisement-to-Button Mapping

The Sims advertisement system maps naturally to A2UI buttons:

| MOOLLM Advertisement | A2UI Component | User Action |
|---------------------|---------------|-------------|
| `WRITE` on Typewriter | `Button` with `action: "write-typewriter"` | `userAction: { name: "write-typewriter" }` |
| `SIT` on Chair | `Button` with `action: "sit-chair"` | `userAction: { name: "sit-chair" }` |
| `BLESS` from StIGNUcius | `Button` with `action: "bless"` | `userAction: { name: "bless" }` |
| `EVALUATE` from "Val" | `Button` with `action: "evaluate"` | `userAction: { name: "evaluate" }` |
| `GO-NORTH` exit | `Button` with `action: "go-north"` | `userAction: { name: "go-north" }` |

This is the **iLoci vision realized**: rooms with things you can interact with, rendered natively, connected by exits.

---

## Bridging MOOLLM (Cursor) to A2UI and OpenClaw

The hard question: MOOLLM runs inside Cursor (an LLM context). How does it push UI to a renderer in real time?

### Option Analysis

| Approach | Latency | Complexity | Bidirectional | Persistent |
|----------|---------|-----------|---------------|------------|
| **CLI commands** | High (~500ms per call) | Low | No (fire-and-forget) | No |
| **Bash + WebSocket** | Medium (~100ms) | Medium | Yes (with `websocat`) | Yes |
| **Python bridge script** | Low (~50ms) | Medium | Yes | Yes |
| **MCP server** | Low (~50ms) | High | Yes (tool calls) | Yes (server lifecycle) |
| **File watching** | Medium (~200ms) | Low | Half (write→watch) | Yes |
| **Node.js bridge** | Low (~50ms) | Medium | Yes | Yes |

### Approach 1: CLI Commands (Simplest, Slowest)

Use `openclaw` CLI from Cursor's shell tool:

```bash
# Push A2UI to canvas
openclaw nodes canvas a2ui push --text "Hello from MOOLLM" --node mac

# Send a message as a character
openclaw gateway call chat.send --params '{"message":"StIGNUcius blesses your code","sessionKey":"default"}'

# Call any gateway method
openclaw gateway call health
```

**Pros:** Works today, no setup, uses existing CLI.
**Cons:** ~500ms per shell invocation. No streaming. No event reception. No persistent state.

**Verdict:** Good for prototyping. Bad for interactive use.

### Approach 2: Persistent WebSocket via `websocat` (Medium)

Use `websocat` (WebSocket CLI tool) for a persistent connection:

```bash
# Install
brew install websocat

# Connect to gateway with persistent bidirectional pipe
websocat ws://127.0.0.1:18789 --text

# Send connect frame
echo '{"type":"req","id":"1","method":"connect","params":{"client":{"id":"moollm","version":"1.0"},"auth":{"token":"YOUR_TOKEN"},"minProtocol":1,"maxProtocol":1}}' | websocat ws://127.0.0.1:18789

# Persistent session with named pipe
mkfifo /tmp/openclaw-pipe
websocat ws://127.0.0.1:18789 < /tmp/openclaw-pipe > /tmp/openclaw-events &

# Send from Cursor:
echo '{"type":"req","id":"2","method":"chat.send","params":{"message":"Hello"}}' > /tmp/openclaw-pipe

# Read events in Cursor:
cat /tmp/openclaw-events
```

**Pros:** Persistent connection. Bidirectional. Events stream in.
**Cons:** Named pipe management. Fragile. Hard to parse JSON responses in bash.

**Verdict:** Hacky but functional. Better than CLI per-call.

### Approach 3: Python Bridge Script (Recommended for Direct A2UI)

A persistent Python process that bridges MOOLLM file output to A2UI:

```python
#!/usr/bin/env python3
"""moollm_a2ui_bridge.py — Bridge MOOLLM rooms to A2UI via OpenClaw gateway."""

import asyncio
import json
import websockets
import yaml
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MOOLLMBridge:
    """Bridges MOOLLM filesystem changes to OpenClaw A2UI."""
    
    def __init__(self, gateway_url: str, token: str, watch_dir: str):
        self.gateway_url = gateway_url
        self.token = token
        self.watch_dir = watch_dir
        self.ws = None
        self.connected = False
        self.req_id = 0
    
    async def connect(self):
        """Connect to OpenClaw gateway."""
        self.ws = await websockets.connect(self.gateway_url)
        
        # Wait for challenge
        challenge = json.loads(await self.ws.recv())
        
        # Send connect
        self.req_id += 1
        await self.ws.send(json.dumps({
            "type": "req",
            "id": str(self.req_id),
            "method": "connect",
            "params": {
                "client": {"id": "moollm-bridge", "version": "1.0"},
                "auth": {"token": self.token},
                "minProtocol": 1,
                "maxProtocol": 1
            }
        }))
        
        # Wait for hello-ok
        response = json.loads(await self.ws.recv())
        if response.get("ok"):
            self.connected = True
            print(f"Connected to OpenClaw gateway at {self.gateway_url}")
        else:
            raise ConnectionError(f"Failed to connect: {response}")
    
    async def push_a2ui(self, jsonl: str):
        """Push A2UI JSONL to canvas."""
        if not self.connected:
            await self.connect()
        
        self.req_id += 1
        await self.ws.send(json.dumps({
            "type": "req",
            "id": str(self.req_id),
            "method": "nodes.command",
            "params": {
                "command": "canvas.a2ui.push",
                "params": {"jsonl": jsonl}
            }
        }))
    
    async def send_message(self, message: str, session: str = "default"):
        """Send a chat message as MOOLLM character."""
        if not self.connected:
            await self.connect()
        
        self.req_id += 1
        await self.ws.send(json.dumps({
            "type": "req",
            "id": str(self.req_id),
            "method": "chat.send",
            "params": {
                "message": message,
                "sessionKey": session
            }
        }))
    
    async def listen_events(self):
        """Listen for gateway events (chat messages, user actions)."""
        async for raw in self.ws:
            frame = json.loads(raw)
            if frame.get("type") == "event":
                event = frame.get("event")
                payload = frame.get("payload", {})
                yield event, payload
    
    def room_to_jsonl(self, room_path: str) -> str:
        """Convert ROOM.yml to A2UI JSONL string."""
        # (uses room_to_a2ui compiler from above)
        from room_to_a2ui import room_to_a2ui
        messages = room_to_a2ui(room_path)
        return "\n".join(json.dumps(m) for m in messages)


class RoomWatcher(FileSystemEventHandler):
    """Watch ROOM.yml files and push updates to A2UI."""
    
    def __init__(self, bridge: MOOLLMBridge, loop: asyncio.AbstractEventLoop):
        self.bridge = bridge
        self.loop = loop
    
    def on_modified(self, event):
        if event.src_path.endswith("ROOM.yml"):
            jsonl = self.bridge.room_to_jsonl(event.src_path)
            asyncio.run_coroutine_threadsafe(
                self.bridge.push_a2ui(jsonl), self.loop
            )
            print(f"Updated A2UI surface from {event.src_path}")


async def main():
    bridge = MOOLLMBridge(
        gateway_url="ws://127.0.0.1:18789",
        token="your-token-here",
        watch_dir="./examples/adventure-4/"
    )
    await bridge.connect()
    
    # Watch for room changes
    loop = asyncio.get_event_loop()
    observer = Observer()
    observer.schedule(
        RoomWatcher(bridge, loop),
        bridge.watch_dir,
        recursive=True
    )
    observer.start()
    
    # Listen for events
    async for event, payload in bridge.listen_events():
        print(f"Event: {event} — {json.dumps(payload)[:200]}")


if __name__ == "__main__":
    asyncio.run(main())
```

**Pros:** Persistent WebSocket. Bidirectional. File watching for live updates. Clean Python.
**Cons:** Requires running a separate process. Cursor can start it but can't easily interact with its stdin.

**Verdict:** Best for A2UI rendering. Run it as a background process from Cursor.

### Approach 4: MCP Server (Best for Cursor Integration)

Build an MCP server that wraps OpenClaw's gateway, exposable as a Cursor MCP tool:

```python
#!/usr/bin/env python3
"""openclaw_mcp_server.py — MCP server bridging Cursor to OpenClaw gateway."""

import asyncio
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import websockets


app = Server("openclaw-bridge")
gateway_ws = None
req_counter = 0


async def ensure_connected():
    """Maintain persistent WebSocket to OpenClaw gateway."""
    global gateway_ws
    if gateway_ws is None or gateway_ws.closed:
        gateway_ws = await websockets.connect("ws://127.0.0.1:18789")
        # Handle connect handshake
        challenge = json.loads(await gateway_ws.recv())
        global req_counter
        req_counter += 1
        await gateway_ws.send(json.dumps({
            "type": "req", "id": str(req_counter),
            "method": "connect",
            "params": {
                "client": {"id": "moollm-mcp", "version": "1.0"},
                "auth": {"token": "your-token"},
                "minProtocol": 1, "maxProtocol": 1
            }
        }))
        response = json.loads(await gateway_ws.recv())
        if not response.get("ok"):
            raise ConnectionError("Gateway connection failed")
    return gateway_ws


async def gateway_call(method: str, params: dict) -> dict:
    """Call a gateway method and return the response."""
    ws = await ensure_connected()
    global req_counter
    req_counter += 1
    rid = str(req_counter)
    await ws.send(json.dumps({
        "type": "req", "id": rid, "method": method, "params": params
    }))
    # Read responses until we get ours (skip events)
    while True:
        raw = await ws.recv()
        frame = json.loads(raw)
        if frame.get("type") == "res" and frame.get("id") == rid:
            return frame
        # Could queue events for later retrieval


@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="openclaw_chat",
            description="Send a message to OpenClaw (as character or direct)",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Message to send"},
                    "session": {"type": "string", "description": "Session key", "default": "default"}
                },
                "required": ["message"]
            }
        ),
        Tool(
            name="openclaw_a2ui_push",
            description="Push A2UI JSONL to OpenClaw canvas",
            inputSchema={
                "type": "object",
                "properties": {
                    "jsonl": {"type": "string", "description": "A2UI v0.8 JSONL messages"},
                    "text": {"type": "string", "description": "Quick text to display"}
                }
            }
        ),
        Tool(
            name="openclaw_gateway",
            description="Call any OpenClaw gateway method",
            inputSchema={
                "type": "object",
                "properties": {
                    "method": {"type": "string", "description": "Gateway method name"},
                    "params": {"type": "object", "description": "Method parameters"}
                },
                "required": ["method"]
            }
        ),
        Tool(
            name="openclaw_room_render",
            description="Render a MOOLLM ROOM.yml as A2UI surface on OpenClaw canvas",
            inputSchema={
                "type": "object",
                "properties": {
                    "room_path": {"type": "string", "description": "Path to ROOM.yml"}
                },
                "required": ["room_path"]
            }
        ),
        Tool(
            name="openclaw_status",
            description="Get OpenClaw gateway health and connected channels",
            inputSchema={"type": "object", "properties": {}}
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "openclaw_chat":
        result = await gateway_call("chat.send", {
            "message": arguments["message"],
            "sessionKey": arguments.get("session", "default")
        })
        return [TextContent(type="text", text=json.dumps(result.get("payload", result), indent=2))]
    
    elif name == "openclaw_a2ui_push":
        jsonl = arguments.get("jsonl") or build_text_jsonl(arguments.get("text", ""))
        result = await gateway_call("nodes.command", {
            "command": "canvas.a2ui.push",
            "params": {"jsonl": jsonl}
        })
        return [TextContent(type="text", text=f"A2UI pushed: {json.dumps(result.get('ok', False))}")]
    
    elif name == "openclaw_gateway":
        result = await gateway_call(arguments["method"], arguments.get("params", {}))
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    elif name == "openclaw_room_render":
        from room_to_a2ui import room_to_a2ui
        messages = room_to_a2ui(arguments["room_path"])
        jsonl = "\n".join(json.dumps(m) for m in messages)
        result = await gateway_call("nodes.command", {
            "command": "canvas.a2ui.push",
            "params": {"jsonl": jsonl}
        })
        return [TextContent(type="text", text=f"Room rendered: {arguments['room_path']}")]
    
    elif name == "openclaw_status":
        result = await gateway_call("health", {})
        return [TextContent(type="text", text=json.dumps(result.get("payload", {}), indent=2))]


def build_text_jsonl(text: str) -> str:
    """Build minimal A2UI JSONL for a text display."""
    return "\n".join([
        json.dumps({"surfaceUpdate": {"surfaceId": "moollm", "components": [
            {"id": "root", "component": {"Column": {"children": {"explicitList": ["text"]}}}},
            {"id": "text", "component": {"Text": {"text": {"literalString": text}, "usageHint": "body"}}}
        ]}}),
        json.dumps({"beginRendering": {"surfaceId": "moollm", "root": "root"}})
    ])


async def run():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(run())
```

**Cursor MCP Configuration:**

```json
{
  "mcpServers": {
    "openclaw-bridge": {
      "command": "python3",
      "args": ["path/to/openclaw_mcp_server.py"],
      "env": {
        "OPENCLAW_TOKEN": "your-gateway-token"
      }
    }
  }
}
```

**Pros:** Native Cursor integration. Tools appear in tool palette. Persistent WebSocket under the hood. Bidirectional via tool calls. LLM can generate A2UI JSONL and push it directly.
**Cons:** MCP servers are request/response — no push events to Cursor (agent would need to poll or use resources).

**Verdict:** Best integration with Cursor. The LLM can literally say "render this room" and see it appear on the OpenClaw canvas.

### Approach 5: File-Based Bridge (Simplest Bidirectional)

MOOLLM writes JSONL files. A watcher pushes them to A2UI. Events write back to files.

```bash
# In one terminal: start the bridge watcher
python3 moollm_file_bridge.py --watch ./a2ui-outbox/ --events ./a2ui-inbox/

# From Cursor (MOOLLM writes a file):
# Write JSONL → ./a2ui-outbox/room-update.jsonl
# Bridge picks it up, pushes to OpenClaw canvas
# User actions write to → ./a2ui-inbox/action-{timestamp}.json
# Cursor reads those files to see what the user did
```

**Pros:** Cursor can write files natively. No MCP setup. Simple.
**Cons:** Latency (file polling). Clunky for rapid interaction.

**Verdict:** Good fallback. Works without any special tooling.

---

## Recommended Architecture

### For Development/Prototyping

```
Cursor (MOOLLM)
  │
  │ Shell tool: openclaw CLI commands
  │ Write tool: A2UI JSONL files
  │
  ▼
File System (.moollm/a2ui-outbox/)
  │
  │ Python file watcher
  │
  ▼
moollm_a2ui_bridge.py
  │
  │ Persistent WebSocket
  │
  ▼
OpenClaw Gateway (:18789)
  │
  ▼
Canvas (:18793) → A2UI Renderer → Native UI
```

### For Production

```
Cursor (MOOLLM)
  │
  │ MCP tool calls
  │
  ▼
openclaw_mcp_server.py (stdio)
  │
  │ Persistent WebSocket (maintained across calls)
  │
  ▼
OpenClaw Gateway (:18789)
  │
  ├──▶ Canvas (:18793) → A2UI Renderer → Visual rooms
  ├──▶ Telegram → StIGNUcius messages
  ├──▶ Discord → "Val" Dobias evaluations
  └──▶ GitHub → MMORPG actions
```

### For Standalone A2UI (No OpenClaw)

```
Cursor (MOOLLM)
  │
  │ Write tool: generates JSONL
  │ Shell tool: starts local HTTP server
  │
  ▼
Local HTTP server (Python)
  │
  │ Serves a2ui-standalone.html + @a2ui/lit bundle
  │ WebSocket for live updates
  │
  ▼
Browser
  │
  │ <a2ui-surface> renders rooms
  │ User actions → WebSocket → file
  │
  ▼
Cursor reads action files
```

This approach uses A2UI's Lit renderer directly, without OpenClaw. Good for testing room rendering without the full gateway stack.

---

## What A2UI Can't Do (Yet)

| Limitation | Impact | Workaround |
|-----------|--------|------------|
| No map/spatial layout | Can't render room maps natively | Use Image with generated map, or Canvas eval for custom JS |
| No drag-and-drop | Can't move objects between rooms by dragging | Use buttons for move actions |
| No animation | Can't animate character movement | Surface updates create instant transitions |
| No custom drawing | Can't draw pie menus or Sims-style UI | Canvas `eval` can inject arbitrary JS (security tradeoff) |
| No audio synthesis | Can't generate TTS | External TTS service + AudioPlayer component |
| 16 components only | Limited UI vocabulary | Custom component registry allows extensions |
| v0.8 only in OpenClaw | Can't use v0.9 improvements | Wait for OpenClaw to update, or use standalone |

### The Canvas `eval` Escape Hatch

OpenClaw's canvas tool has an `eval` action that executes arbitrary JavaScript in the canvas context. This is the nuclear option for custom UI:

```bash
openclaw nodes canvas eval --js "
  const canvas = document.querySelector('canvas');
  const ctx = canvas.getContext('2d');
  // Draw a room map, pie menu, character sprite, anything
" --node mac
```

This bypasses A2UI's declarative safety model but enables custom rendering. Use sparingly. For MOOLLM, this could render:
- Room maps with spatial layouts
- Pie menus for object interactions (The Sims heritage)
- Character sprites or portraits
- iLoci-style node networks

---

## Related Documents

- [ARCHITECTURE-ANALYSIS.md](./ARCHITECTURE-ANALYSIS.md) — OpenClaw architecture
- [MMORPG-GATEWAY.md](./MMORPG-GATEWAY.md) — Game loop using OpenClaw
- [CHARACTERS-AS-AGENTS.md](./CHARACTERS-AS-AGENTS.md) — Character deployment
- [../iloci.md](../iloci.md) — iLoci heritage (rooms → things → publishing)
- [../GITHUB-AS-MMORPG.md](../GITHUB-AS-MMORPG.md) — GitHub as game world
