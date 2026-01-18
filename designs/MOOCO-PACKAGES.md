# MOOCO Package Structure

## Repository Layout

```
moollm/
├── packages/                     # Shared npm packages (MIT license)
│   ├── conversation-schema/      # @moollm/conversation-schema
│   │   ├── src/
│   │   │   ├── drizzle/         # Drizzle ORM schemas
│   │   │   │   ├── postgres.ts  # PostgreSQL schema (shared)
│   │   │   │   ├── timescale.ts # TimescaleDB hypertables (MOOCO)
│   │   │   │   └── pgvector.ts  # pgvector embeddings (MOOCO)
│   │   │   ├── types.ts         # TypeScript types
│   │   │   └── index.ts
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   ├── stream-machine/           # @moollm/stream-machine
│   │   ├── src/
│   │   │   ├── StreamMachine.ts
│   │   │   ├── ActiveStreamRegistry.ts
│   │   │   ├── MessagePersister.ts
│   │   │   ├── ConversationHistory.ts
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── sse-protocol/             # @moollm/sse-protocol
│   │   ├── src/
│   │   │   ├── types.ts         # Event type definitions
│   │   │   ├── parser.ts        # SSE stream parser
│   │   │   ├── reconnector.ts   # Reconnection logic
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── provider-base/            # @moollm/provider-base
│   │   ├── src/
│   │   │   ├── LLMProvider.ts   # Abstract base class
│   │   │   ├── types.ts         # Provider types
│   │   │   ├── capabilities.ts  # Capability detection
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── providers/                # @moollm/providers
│   │   ├── src/
│   │   │   ├── anthropic.ts
│   │   │   ├── openai.ts
│   │   │   ├── vertex.ts
│   │   │   ├── ollama.ts
│   │   │   ├── registry.ts      # Model registry
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── tool-executor/            # @moollm/tool-executor
│   │   ├── src/
│   │   │   ├── ToolDefinition.ts
│   │   │   ├── ToolRegistry.ts
│   │   │   ├── ToolContext.ts
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── tools-core/               # @moollm/tools-core
│   │   ├── src/
│   │   │   ├── bash.ts          # Shell execution
│   │   │   ├── python.ts        # Python REPL
│   │   │   ├── javascript.ts    # JS/Node execution
│   │   │   ├── sql.ts           # SQL queries (generic)
│   │   │   ├── fs-read.ts       # File read
│   │   │   ├── fs-write.ts      # File write
│   │   │   ├── http.ts          # HTTP requests
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── thinking-extractor/       # @moollm/thinking-extractor
│   │   ├── src/
│   │   │   ├── ThinkingExtractor.ts
│   │   │   ├── patterns.ts
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── svelte-chat/              # @moollm/svelte-chat
│   │   ├── src/
│   │   │   ├── ChatClient.svelte.ts
│   │   │   ├── components/
│   │   │   │   ├── ChatContainer.svelte
│   │   │   │   ├── ChatBubble.svelte
│   │   │   │   ├── ThinkingBlock.svelte
│   │   │   │   ├── ToolCallBlock.svelte
│   │   │   │   ├── ProcessFlow.svelte
│   │   │   │   ├── ChatInput.svelte
│   │   │   │   └── FileAttachment.svelte
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── cursor-mirror/            # @moollm/cursor-mirror
│   │   ├── src/
│   │   │   ├── CursorMirror.ts   # Main class (TypeScript port)
│   │   │   ├── sqlite.ts         # SQLite utilities
│   │   │   ├── paths.ts          # Platform-specific paths
│   │   │   ├── schemas.ts        # Cursor data schemas
│   │   │   ├── queries/          # Pre-built queries
│   │   │   │   ├── bubbles.ts
│   │   │   │   ├── composers.ts
│   │   │   │   ├── workspaces.ts
│   │   │   │   └── mcp.ts
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── mooco-mirror/             # @moollm/mooco-mirror
│   │   ├── src/
│   │   │   ├── MoocoMirror.ts    # Main class
│   │   │   ├── queries/          # PostgreSQL queries
│   │   │   │   ├── sessions.ts
│   │   │   │   ├── conversations.ts
│   │   │   │   ├── messages.ts
│   │   │   │   ├── tools.ts
│   │   │   │   ├── rooms.ts
│   │   │   │   ├── k-lines.ts
│   │   │   │   └── timeseries.ts  # TimescaleDB queries
│   │   │   ├── semantic.ts       # pgvector search
│   │   │   ├── export.ts         # Export to JSON/Cursor format
│   │   │   ├── cli.ts            # CLI interface
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   └── sqlite-fluency/           # @moollm/sqlite-fluency
│       ├── src/
│       │   ├── SQLiteFluency.ts  # Generic SQLite utilities
│       │   ├── cursor.ts         # Cursor-specific helpers
│       │   ├── import-export.ts  # Conversation import/export
│       │   └── index.ts
│       └── package.json
│
├── apps/
│   └── mooco/                    # MOOCO SvelteKit app
│       ├── src/
│       │   ├── lib/
│       │   │   ├── db/          # PostgreSQL via Drizzle
│       │   │   │   ├── index.ts       # Connection pool
│       │   │   │   ├── schema.ts      # Core + TimescaleDB + pgvector
│       │   │   │   └── migrations/    # Drizzle migrations
│       │   │   ├── mirrors/     # cursor-mirror + mooco-mirror integration
│       │   │   ├── rooms/       # Room navigation
│       │   │   ├── characters/  # Character engine
│       │   │   ├── skills/      # Skill composition
│       │   │   ├── k-lines/     # K-line activation (pgvector)
│       │   │   └── adventure/   # Adventure game mode
│       │   ├── routes/
│       │   │   ├── +page.svelte
│       │   │   ├── chat/
│       │   │   │   └── [[id]]/
│       │   │   │       ├── +page.server.ts
│       │   │   │       ├── +page.svelte
│       │   │   │       └── stream/
│       │   │   │           └── +server.ts
│       │   │   └── api/
│       │   │       └── [...path]/
│       │   │           └── +server.ts
│       │   └── app.html
│       ├── static/
│       ├── package.json
│       ├── svelte.config.js
│       └── vite.config.ts
│
└── skills/                       # MOOLLM skills (existing)
    └── cursor-mirror/            # Can be used by MOOCO
```

## Dependency Graph

```
                              ┌─────────────────────────┐
                              │  @moollm/svelte-chat    │
                              └───────────┬─────────────┘
                                          │
                    ┌─────────────────────┼─────────────────┐
                    │                     │                 │
                    ▼                     ▼                 ▼
      ┌─────────────────────┐   ┌───────────────┐   ┌──────────────────┐
      │ @moollm/sse-protocol│   │@moollm/types  │   │@moollm/stream-   │
      └─────────────────────┘   └───────────────┘   │    machine       │
                                                    └────────┬─────────┘
                                                             │
               ┌─────────────────────────────────────────────┼──────────────────────┐
               │                 │                           │                      │
               ▼                 ▼                           ▼                      ▼
      ┌─────────────────┐ ┌───────────────┐ ┌────────────────────┐ ┌────────────────────┐
      │@moollm/provider-│ │@moollm/tool-  │ │@moollm/thinking-   │ │@moollm/conversation│
      │     base        │ │  executor     │ │   extractor        │ │     -schema        │
      └────────┬────────┘ └───────┬───────┘ └────────────────────┘ └─────────┬──────────┘
               │                  │                                          │
               ▼                  ▼                                          ▼
      ┌─────────────────┐ ┌───────────────┐                        ┌─────────────────────┐
      │ @moollm/        │ │@moollm/tools- │                        │  @moollm/mooco-     │
      │  providers      │ │    core       │                        │     mirror          │
      └─────────────────┘ └───────────────┘                        └──────────┬──────────┘
                                                                              │
                                    ┌─────────────────────────────────────────┤
                                    │                                         │
                                    ▼                                         ▼
                          ┌──────────────────────┐              ┌─────────────────────────┐
                          │ @moollm/cursor-mirror│              │ @moollm/sqlite-fluency  │
                          │ (read Cursor SQLite) │              │ (SQLite read/write)     │
                          └──────────────────────┘              └─────────────────────────┘
```

### Mirror Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                            MOOCO RUNTIME                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌───────────────────────────────────┐   ┌───────────────────────────────┐ │
│  │         MOOCO's Brain             │   │      External Minds           │ │
│  │                                   │   │                               │ │
│  │  PostgreSQL                       │   │  Cursor's SQLite DBs          │ │
│  │  ├── conversations                │   │  ├── globalStorage/state.vscdb│ │
│  │  ├── messages                     │   │  │   └── cursorDiskKV         │ │
│  │  ├── tool_calls                   │   │  └── workspaceStorage/*/      │ │
│  │  ├── session_events (TimescaleDB) │   │      └── state.vscdb          │ │
│  │  ├── message_embeddings (pgvector)│   │                               │ │
│  │  ├── k_lines (pgvector)           │   │  Other SQLite Sources         │ │
│  │  ├── rooms                        │   │  ├── VS Code state            │ │
│  │  └── skills                       │   │  ├── Zed state                │ │
│  │                                   │   │  └── Custom tools             │ │
│  └───────────────┬───────────────────┘   └───────────────┬───────────────┘ │
│                  │                                       │                 │
│                  ▼                                       ▼                 │
│  ┌───────────────────────────────────┐   ┌───────────────────────────────┐ │
│  │        mooco-mirror               │   │       cursor-mirror           │ │
│  │                                   │   │                               │ │
│  │  "See MOOCO think"                │   │  "Read Cursor's mind"         │ │
│  │                                   │   │                               │ │
│  │  • PostgreSQL queries             │   │  • SQLite read-only access    │ │
│  │  • TimescaleDB aggregates         │   │  • Bubble/composer extraction │ │
│  │  • pgvector similarity search     │   │  • Context reconstruction     │ │
│  │  • K-line activation history      │   │  • MCP server discovery       │ │
│  │  • Room navigation timeline       │   │  • Tool call inspection       │ │
│  │  • Export to Cursor format        │   │  • Import to MOOCO            │ │
│  └───────────────────────────────────┘   └───────────────────────────────┘ │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

## Usage in PDA vs MOOCO

### PDA (Leela Proprietary)

```typescript
// apps/pda/src/lib/llm/ConversationMachine.ts
import { StreamMachine } from '@moollm/stream-machine';
import { AnthropicProvider } from '@moollm/providers';
import { ToolRegistry } from '@moollm/tool-executor';

// Leela-specific imports (NOT from shared packages)
import { bqTool, schemaRefreshTool } from './tools/bigquery.js';
import { getSchemaDigest } from './bq.js';
import { SYSTEM_PROMPT } from './prompts.js';

export class ConversationMachine {
    static async *start(params: StartStreamParams) {
        // Use shared StreamMachine with Leela-specific tools
        const registry = new ToolRegistry()
            .register(bqTool)
            .register(schemaRefreshTool)
            .register(exportDataTool);
        
        // Leela-specific system prompt with schema digest
        const digest = await getSchemaDigest(params.siteId);
        const systemPrompt = SYSTEM_PROMPT({ digest });
        
        yield* StreamMachine.stream({
            ...params,
            tools: registry,
            systemPrompt,
            provider: new AnthropicProvider(/* ... */),
        });
    }
}
```

### MOOCO (Open Source)

```typescript
// apps/mooco/src/lib/OrchestrationMachine.ts
import { StreamMachine } from '@moollm/stream-machine';
import { AnthropicProvider, OllamaProvider } from '@moollm/providers';
import { ToolRegistry } from '@moollm/tool-executor';
import { bashTool, pythonTool, sqlTool } from '@moollm/tools-core';

// MOOLLM-specific imports
import { RoomEngine } from './rooms/RoomEngine.js';
import { SkillLoader } from './skills/SkillLoader.js';

export class OrchestrationMachine {
    static async *start(params: StartStreamParams) {
        // Load active skills
        const skills = await SkillLoader.load(params.activeSkills);
        
        // Build tool registry from skills + core tools
        const registry = new ToolRegistry()
            .register(bashTool)
            .register(pythonTool)
            .register(sqlTool)
            .registerAll(skills.flatMap(s => s.tools));
        
        // Build system prompt from skills
        const systemPrompt = SkillLoader.buildSystemPrompt(skills, {
            currentRoom: params.currentRoom,
            character: params.activeCharacter,
        });
        
        // Choose provider (local or remote)
        const provider = params.useLocal 
            ? new OllamaProvider({ model: 'llama3' })
            : new AnthropicProvider({ apiKey: env.ANTHROPIC_API_KEY });
        
        yield* StreamMachine.stream({
            ...params,
            tools: registry,
            systemPrompt,
            provider,
        });
    }
}
```

## Database Backend Comparison

Both PDA and MOOCO use PostgreSQL, but with different extensions and focus:

### PDA: PostgreSQL + BigQuery

```typescript
// apps/pda/src/db/index.ts
import { drizzle } from 'drizzle-orm/node-postgres';
import { conversations, messages, messagePart, toolCalls } from '@moollm/conversation-schema/postgres';

export const db = drizzle(pool, { schema: { conversations, messages, messagePart, toolCalls } });

// BigQuery for analytics queries (Leela video data)
import { BigQuery } from '@google-cloud/bigquery';
const bq = new BigQuery({ projectId: env.GCP_PROJECT });
```

### MOOCO: PostgreSQL + TimescaleDB + pgvector

```typescript
// apps/mooco/src/lib/db/index.ts
import { drizzle } from 'drizzle-orm/node-postgres';
import { conversations, messages, messagePart, toolCalls } from '@moollm/conversation-schema/postgres';
import { sessionEvents, messageEmbeddings } from '@moollm/conversation-schema/mooco';

export const db = drizzle(pool, { 
    schema: { 
        // Core schema (shared with PDA)
        conversations, 
        messages, 
        messagePart, 
        toolCalls,
        // MOOCO extensions
        sessionEvents,      // TimescaleDB hypertable
        messageEmbeddings,  // pgvector embeddings
    } 
});
```

### MOOCO PostgreSQL Extensions

```sql
-- Enable extensions
CREATE EXTENSION IF NOT EXISTS timescaledb;
CREATE EXTENSION IF NOT EXISTS vector;

-- TimescaleDB: session_events hypertable for time-series analytics
CREATE TABLE session_events (
    time        TIMESTAMPTZ NOT NULL,
    session_id  UUID NOT NULL,
    event_type  TEXT NOT NULL,
    event_data  JSONB,
    PRIMARY KEY (time, session_id)
);
SELECT create_hypertable('session_events', 'time');

-- Continuous aggregates for dashboards
CREATE MATERIALIZED VIEW session_stats_hourly
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 hour', time) AS bucket,
    session_id,
    count(*) AS event_count,
    count(*) FILTER (WHERE event_type = 'tool_call') AS tool_calls,
    count(*) FILTER (WHERE event_type = 'message') AS messages
FROM session_events
GROUP BY bucket, session_id;

-- pgvector: message embeddings for semantic search
CREATE TABLE message_embeddings (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    message_id      UUID NOT NULL REFERENCES messages(id) ON DELETE CASCADE,
    embedding       vector(1536),  -- OpenAI ada-002 dimensions
    model           TEXT NOT NULL DEFAULT 'text-embedding-ada-002',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- HNSW index for fast similarity search
CREATE INDEX ON message_embeddings USING hnsw (embedding vector_cosine_ops);

-- Semantic search function
CREATE FUNCTION search_messages(
    query_embedding vector(1536),
    match_count INT DEFAULT 10,
    session_filter UUID DEFAULT NULL
) RETURNS TABLE (
    message_id UUID,
    similarity FLOAT,
    content TEXT
) AS $$
    SELECT 
        m.id,
        1 - (e.embedding <=> query_embedding) AS similarity,
        m.final_text
    FROM message_embeddings e
    JOIN messages m ON e.message_id = m.id
    WHERE session_filter IS NULL 
       OR m.conversation_id IN (
           SELECT id FROM conversations WHERE session_id = session_filter
       )
    ORDER BY e.embedding <=> query_embedding
    LIMIT match_count;
$$ LANGUAGE SQL STABLE;
```

### In-Memory (Testing)

```typescript
// packages/stream-machine/src/__tests__/helpers.ts
import { PGlite } from '@electric-sql/pglite';

// Use PGlite for in-memory PostgreSQL (tests)
const pg = new PGlite();
const db = drizzle(pg);
```

## Tool Plugin System

### MOOLLM Tool Convention: The `why` Parameter

Every MOOLLM tool includes a `why` parameter — a brief explanation of purpose.
This enables better UI summaries, chain-of-thought traceability, and analytics.

```typescript
// LLM calls the tool like this:
bash({
    why: "Checking if the Docker container is running",
    command: "docker ps | grep mooco"
})

// UI shows:
// 🔧 bash: Checking if the Docker container is running
//    $ docker ps | grep mooco
//    → mooco-db  Up 2 hours
```

### Defining a Tool

```typescript
// packages/tools-core/src/bash.ts
import { z } from 'zod';
import { defineTool, withWhy } from '@moollm/tool-executor';

export const bashTool = defineTool({
    name: 'bash',
    description: 'Execute a bash command',
    // withWhy() adds the required 'why' parameter automatically
    inputSchema: withWhy(z.object({
        command: z.string().describe('The command to execute'),
        cwd: z.string().optional().describe('Working directory'),
        timeout: z.number().optional().default(30000),
    })),
    
    ui: {
        icon: 'terminal',
        category: 'system',
        dangerous: true,
    },
    
    async execute(input, context) {
        const { why, command, cwd, timeout } = input;
        
        // Log the why for analytics
        context.emit({
            event: 'tool_call_why',
            data: { toolCallId: context.toolCallId, why }
        });
        
        // Stream output as it arrives
        const process = spawn('bash', ['-c', command], { cwd });
        
        for await (const chunk of process.stdout) {
            context.emit({
                event: 'tool_output_delta',
                data: { toolCallId: context.toolCallId, chunk: chunk.toString() }
            });
        }
        
        const result = await process;
        return {
            stdout: result.stdout,
            stderr: result.stderr,
            exitCode: result.exitCode,
        };
    },
});

// Helper: withWhy adds the required 'why' parameter to any schema
function withWhy<T extends z.ZodRawShape>(schema: z.ZodObject<T>) {
    return schema.extend({
        why: z.string().describe(
            'Brief explanation of why this tool is being called. ' +
            'Example: "Checking if Docker container is running"'
        ),
    });
}
```

### The `why` Convention in System Prompts

The system prompt instructs the LLM to always include `why`:

```typescript
const TOOL_CALLING_INSTRUCTION = `
When calling tools, ALWAYS include a "why" parameter explaining your purpose.
This helps users understand your reasoning and enables better analytics.

Good:
  bash({ why: "Checking container status", command: "docker ps" })

Bad:
  bash({ command: "docker ps" })  // Missing why!
`;
```

### Using in MOOCO

```typescript
// apps/mooco/src/lib/tools/registry.ts
import { ToolRegistry } from '@moollm/tool-executor';
import { bashTool, pythonTool, sqlTool } from '@moollm/tools-core';

// Custom MOOCO tools
import { roomNavigateTool } from './room-navigate.js';
import { skillInvokeTool } from './skill-invoke.js';
import { cursorMirrorTool } from './cursor-mirror.js';

export const moocoTools = new ToolRegistry()
    // Core tools (shared with PDA)
    .register(bashTool)
    .register(pythonTool)
    .register(sqlTool)
    // MOOCO-specific tools
    .register(roomNavigateTool)
    .register(skillInvokeTool)
    .register(cursorMirrorTool);
```

### Using in PDA

```typescript
// apps/pda/src/lib/llm/tools/registry.ts
import { ToolRegistry } from '@moollm/tool-executor';
import { bashTool } from '@moollm/tools-core';  // Only if needed

// Leela-specific tools
import { bqTool } from './bigquery.js';
import { schemaRefreshTool } from './bigquery.js';
import { exportDataTool } from './export.js';
import { requestHistoryTool } from './history.js';

export const pdaTools = new ToolRegistry()
    // Leela-specific tools
    .register(bqTool)
    .register(schemaRefreshTool)
    .register(exportDataTool)
    .register(requestHistoryTool);
    // Could add bashTool for admin users
```

## Svelte Component Sharing

### Shared Components

```svelte
<!-- packages/svelte-chat/src/components/ChatBubble.svelte -->
<script lang="ts">
    import type { ClientMessage } from '../types.js';
    import ThinkingBlock from './ThinkingBlock.svelte';
    import ToolCallBlock from './ToolCallBlock.svelte';
    
    interface Props {
        message: ClientMessage;
        showThinking?: boolean;
        onRetry?: () => void;
        // Slot for custom content types
        children?: Snippet;
    }
    
    let { message, showThinking = false, onRetry, children }: Props = $props();
</script>

<div class="bubble {message.role}">
    {#each message.parts as part}
        {#if part.type === 'text'}
            <div class="text">{@html renderMarkdown(part.content.text)}</div>
        {:else if part.type === 'thinking' && showThinking}
            <ThinkingBlock {part} />
        {:else if part.type === 'tool_call'}
            <ToolCallBlock {part} />
        {:else}
            <!-- Custom content via slot -->
            {@render children?.()}
        {/if}
    {/each}
</div>
```

### PDA Extension

```svelte
<!-- apps/pda/src/lib/components/ChatBubble.svelte -->
<script lang="ts">
    import { ChatBubble as BaseBubble } from '@moollm/svelte-chat';
    import VideoEmbed from './VideoEmbed.svelte';
    import QueryResults from './QueryResults.svelte';
    
    interface Props {
        message: ClientMessage;
    }
    
    let { message }: Props = $props();
</script>

<BaseBubble {message} showThinking={$preferences.showThinking}>
    {#snippet children()}
        {#if part.type === 'file' && part.content.mimetype?.startsWith('video/')}
            <VideoEmbed url={part.content.url} signed={part.content.signedUrl} />
        {:else if part.type === 'json' && part.content.title === 'Query Results'}
            <QueryResults data={part.content.json} />
        {/if}
    {/snippet}
</BaseBubble>
```

### MOOCO Extension

```svelte
<!-- apps/mooco/src/lib/components/ChatBubble.svelte -->
<script lang="ts">
    import { ChatBubble as BaseBubble } from '@moollm/svelte-chat';
    import RoomTransition from './RoomTransition.svelte';
    import CharacterSpeech from './CharacterSpeech.svelte';
    
    interface Props {
        message: ClientMessage;
    }
    
    let { message }: Props = $props();
</script>

<BaseBubble {message} showThinking={true}>
    {#snippet children()}
        {#if part.type === 'room_enter'}
            <RoomTransition room={part.content.room} direction="enter" />
        {:else if part.type === 'character_speak'}
            <CharacterSpeech character={part.content.character} text={part.content.text} />
        {/if}
    {/snippet}
</BaseBubble>
```

## Summary

This package structure enables:

1. **Code sharing** — Both PDA and MOOCO use the same streaming engine, provider abstraction, and chat components
2. **Clean separation** — Leela-specific code stays in PDA, MOOLLM-specific in MOOCO
3. **Composable tools** — Tools can be mixed and matched between apps
4. **PostgreSQL all-in** — MOOCO uses PostgreSQL + TimescaleDB + pgvector
5. **SQLite fluency** — Read/write Cursor's SQLite databases via cursor-mirror
6. **Dual mirrors** — mooco-mirror for self-introspection, cursor-mirror for IDE integration
7. **UI extensibility** — Base Svelte components can be extended with domain-specific content types

### Database Strategy

| Layer | Technology | Purpose |
|-------|------------|---------|
| **MOOCO's Brain** | PostgreSQL | Core conversation storage |
| **Time-series** | TimescaleDB | Session event analytics |
| **Embeddings** | pgvector | K-line activation, semantic search |
| **Cursor's Mind** | SQLite (read) | Import conversations, analyze sessions |
| **Other Tools** | SQLite (read/write) | Integrate with VS Code, Zed, etc. |

### Mirror Capabilities

| Tool | Source | Purpose |
|------|--------|---------|
| **mooco-mirror** | PostgreSQL | See MOOCO think — introspect own state |
| **cursor-mirror** | SQLite | Read Cursor's mind — import/analyze IDE sessions |

Both mirrors share the same CLI interface patterns:
```bash
# mooco-mirror
mooco-mirror tail @1            # Recent messages
mooco-mirror grep "pattern"     # Text search
mooco-mirror similar @1.m5      # Semantic search (pgvector)
mooco-mirror timeline @1        # TimescaleDB analytics

# cursor-mirror
cursor-mirror tail @1           # Recent messages from Cursor
cursor-mirror grep "pattern"    # Search Cursor's history
cursor-mirror tree              # Browse workspaces/composers
cursor-mirror tools @1          # Inspect tool calls
```
