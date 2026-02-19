# Bubble access and text extraction.
# Align with reference/universal/model/entities/bubble.yml, algorithms/extract-bubble-text.yml

import json
from collections.abc import Iterator
from datetime import datetime
from typing import Any

from .db import open_db, decode_blob
from .debug_util import debug
from .paths import GLOBAL_DB
from .sources import register_source

# Bubble types (from entities/bubble.yml)
USER: int = 1
ASSISTANT: int = 2


def iter_bubbles(composer_id: str | None = None) -> Iterator[tuple[str, str, dict[str, Any]]]:
    """Yield (composer_id, bubble_key, bubble_dict) from global cursorDiskKV.

    Pass composer_id=None to iterate ALL bubbles across all composers.
    ORDER BY rowid preserves message order.
    """
    conn = open_db(GLOBAL_DB)
    cur = conn.cursor()
    register_source("database", str(GLOBAL_DB), "cursorDiskKV")

    if composer_id:
        register_source("sql", f"SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:{composer_id[:8]}...'")
        rows = cur.execute(
            "SELECT key, value FROM cursorDiskKV WHERE key LIKE ?",
            (f"bubbleId:{composer_id}:%",),
        ).fetchall()
    else:
        register_source("sql", "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'")
        rows = cur.execute(
            "SELECT key, value FROM cursorDiskKV WHERE key LIKE 'bubbleId:%'"
        ).fetchall()
    conn.close()

    for k, v in rows:
        try:
            obj = json.loads(decode_blob(v))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(obj, dict):
            continue
        parts = k.split(":")
        cid = parts[1] if len(parts) >= 2 else "unknown"
        yield cid, k, obj


def load_bubbles(composer_id: str) -> list[dict[str, Any]]:
    """Load all bubbles for a composer, sorted by createdAt."""
    bubbles = []
    for _cid, k, obj in iter_bubbles(composer_id):
        obj["_key"] = k
        bubbles.append(obj)
    bubbles.sort(key=lambda x: x.get("createdAt") or "")
    return bubbles


def get_bubble_text(obj: dict[str, Any]) -> str:
    """Extract text content from a bubble."""
    return obj.get("text") or obj.get("content") or ""


def has_content(obj: dict[str, Any]) -> bool:
    """Check if bubble has meaningful content."""
    return bool(
        get_bubble_text(obj)
        or obj.get("toolCalls")
        or obj.get("toolResults")
        or obj.get("codeBlocks")
        or obj.get("thinking")
    )


def _format_code_block(cb: dict[str, Any]) -> str:
    """Format a code block with optional file path context (N1 fix)."""
    content = cb.get("content", "")
    path = cb.get("relativePath") or cb.get("uri", "")
    if path and content:
        return f"[{path}]\n{content}"
    return content


def _parse_nested_result(result: Any) -> str:
    """Parse nested JSON in tool results (N1 fix)."""
    if isinstance(result, str):
        try:
            parsed = json.loads(result)
            if isinstance(parsed, dict):
                return parsed.get("output") or parsed.get("contents") or parsed.get("text") or result
        except (json.JSONDecodeError, TypeError):
            pass
        return result
    if isinstance(result, dict):
        if result.get("diff"):
            return str(result["diff"])
        return result.get("output") or result.get("contents") or result.get("text") or str(result)
    return str(result) if result else ""


def extract_bubble_text(obj: dict[str, Any]) -> str:
    """Full text extraction per algorithms/extract-bubble-text.yml priority.

    Assistant: toolFormerData.result.diff -> text+codeBlocks -> thinking -> toolFormerData result
    User: selections + codeBlocks (pasted) then text/content
    """
    btype = obj.get("type", 0)

    if btype == ASSISTANT:
        tfd = obj.get("toolFormerData")
        if tfd:
            result = tfd.get("result")
            if result:
                parsed = _parse_nested_result(result)
                if parsed:
                    return parsed

        text = get_bubble_text(obj)
        code_blocks = obj.get("codeBlocks")
        if text or code_blocks:
            parts = [text] if text else []
            if code_blocks:
                for cb in code_blocks:
                    if isinstance(cb, dict):
                        parts.append(_format_code_block(cb))
            return "\n".join(p for p in parts if p)

        thinking = obj.get("thinking")
        if thinking and isinstance(thinking, dict):
            return thinking.get("text", "")

    else:
        parts: list[str] = []
        # N1: include user selections (code context they attached)
        selections = obj.get("selections")
        if selections and isinstance(selections, list):
            for sel in selections:
                if isinstance(sel, dict):
                    uri = sel.get("uri", "")
                    text_sel = sel.get("selectedText") or sel.get("text", "")
                    if text_sel:
                        parts.append(f"[selection: {uri}]\n{text_sel}" if uri else text_sel)

        code_blocks = obj.get("codeBlocks")
        if code_blocks:
            for cb in code_blocks:
                if isinstance(cb, dict):
                    parts.append(_format_code_block(cb))

        text = get_bubble_text(obj)
        if text:
            parts.append(text)
        return "\n".join(p for p in parts if p)

    return ""


def is_error(obj: dict[str, Any]) -> bool:
    """Check if bubble represents a tool error (from entities/tool-result-parse.yml)."""
    tfd = obj.get("toolFormerData")
    if not tfd:
        return False
    ad = tfd.get("additionalData")
    if isinstance(ad, dict):
        return ad.get("status") == "error"
    return False
