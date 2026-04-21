# Cursor `aiService` snapshot

`cursor-aiService-prompts.yaml` is a **YAML dump** of workspace DB keys:

- `aiService.prompts` — prompt history (quick prompts / composer input fragments Cursor stored)
- `aiService.generations` — generation records (UUIDs, types, descriptions)

Produced with **cursor-mirror** from the workspace that hosted the long Emacs design thread:

```bash
cd /path/to/moollm
python3 skills/cursor-mirror/scripts/cursor_mirror.py export-prompts fa890658 \
  -o skills/emacs/reference/cursor-aiService-prompts.yaml
```

Use `list-workspaces` to find the current id if the folder hash changes. This is **not** a full system prompt export; it is what Cursor persists under those keys in `state.vscdb`.
