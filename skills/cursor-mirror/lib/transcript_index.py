# SQLite index for agent transcripts. Lives next to the .txt as .db.
# No text stored -- just byte offsets and metadata pointing into the .txt.
# Incremental: only indexes new content since last run.

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from .transcript import (
    Section, SectionType, ParserState,
    parse_transcript, parse_transcript_incremental,
    extract_shell_commands,
)

SCHEMA_VERSION = 1

_SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE IF NOT EXISTS sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    start_line INTEGER NOT NULL,
    end_line INTEGER NOT NULL,
    line_count INTEGER NOT NULL,
    tool_name TEXT,
    user_query_preview TEXT,
    text_preview TEXT
);

CREATE TABLE IF NOT EXISTS tool_params (
    section_id INTEGER NOT NULL REFERENCES sections(id),
    name TEXT NOT NULL,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS shell_commands (
    section_id INTEGER NOT NULL REFERENCES sections(id),
    command TEXT NOT NULL,
    line INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_sections_type ON sections(type);
CREATE INDEX IF NOT EXISTS idx_sections_lines ON sections(start_line);
CREATE INDEX IF NOT EXISTS idx_tool_params_section ON tool_params(section_id);
CREATE INDEX IF NOT EXISTS idx_shell_commands_line ON shell_commands(line);
"""


def index_path_for(transcript_path: Path) -> Path:
    """Get the .db path for a .txt transcript."""
    return transcript_path.with_suffix(".db")


def open_index(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.executescript(_SCHEMA)
    return conn


def _get_meta(conn: sqlite3.Connection, key: str) -> str | None:
    row = conn.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
    return row[0] if row else None


def _set_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)",
        (key, value),
    )


def _load_parser_state(conn: sqlite3.Connection, transcript_path: Path) -> ParserState | None:
    offset = _get_meta(conn, "file_offset")
    if offset is None:
        return None
    return ParserState(
        file_path=str(transcript_path),
        file_offset=int(offset),
        line_number=int(_get_meta(conn, "line_number") or "0"),
        current_type=SectionType[_get_meta(conn, "current_type")] if _get_meta(conn, "current_type") else None,
        section_start=int(_get_meta(conn, "section_start") or "0"),
        in_user_query=_get_meta(conn, "in_user_query") == "1",
    )


def _save_parser_state(conn: sqlite3.Connection, state: ParserState) -> None:
    _set_meta(conn, "file_offset", str(state.file_offset))
    _set_meta(conn, "line_number", str(state.line_number))
    _set_meta(conn, "current_type", state.current_type.name if state.current_type else "")
    _set_meta(conn, "section_start", str(state.section_start))
    _set_meta(conn, "in_user_query", "1" if state.in_user_query else "0")
    _set_meta(conn, "schema_version", str(SCHEMA_VERSION))


def _insert_sections(conn: sqlite3.Connection, sections: list[Section]) -> None:
    for s in sections:
        cur = conn.execute(
            "INSERT INTO sections (type, start_line, end_line, line_count, "
            "tool_name, user_query_preview, text_preview) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                s.type.name,
                s.start_line,
                s.end_line,
                s.line_count,
                s.tool_name or None,
                s.user_query[:200] if s.user_query else None,
                s.text.strip()[:200] if s.text else None,
            ),
        )
        section_id = cur.lastrowid
        for p in s.tool_params:
            conn.execute(
                "INSERT INTO tool_params (section_id, name, value) VALUES (?, ?, ?)",
                (section_id, p.name, p.value[:500]),
            )

    cmds = extract_shell_commands(sections)
    for cmd in cmds:
        section_row = conn.execute(
            "SELECT id FROM sections WHERE start_line = ? AND type = 'TOOL_CALL'",
            (cmd["line"],),
        ).fetchone()
        section_id = section_row[0] if section_row else None
        conn.execute(
            "INSERT INTO shell_commands (section_id, command, line) VALUES (?, ?, ?)",
            (section_id, cmd["command"], cmd["line"]),
        )


def update_index(transcript_path: Path) -> dict[str, Any]:
    """Index a transcript incrementally. Creates .db if needed.

    Returns stats: {new_sections, total_sections, shell_commands, is_fresh}.
    """
    db_path = index_path_for(transcript_path)
    conn = open_index(db_path)

    state = _load_parser_state(conn, transcript_path)
    is_fresh = state is None

    if is_fresh:
        sections, new_state = parse_transcript(transcript_path)
    else:
        sections, new_state = parse_transcript_incremental(transcript_path, state)

    if sections:
        _insert_sections(conn, sections)
    _save_parser_state(conn, new_state)
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
    shell_count = conn.execute("SELECT COUNT(*) FROM shell_commands").fetchone()[0]
    conn.close()

    return {
        "new_sections": len(sections),
        "total_sections": total,
        "shell_commands": shell_count,
        "is_fresh": is_fresh,
        "db_path": str(db_path),
    }


def query_index(
    db_path: Path,
    section_type: str | None = None,
    tool_name: str | None = None,
    limit: int = 50,
) -> list[dict[str, Any]]:
    """Query a transcript index. Returns section metadata (no text -- read .txt for that)."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    query = "SELECT * FROM sections WHERE 1=1"
    params: list[Any] = []

    if section_type:
        query += " AND type = ?"
        params.append(section_type.upper())
    if tool_name:
        query += " AND tool_name = ?"
        params.append(tool_name)

    query += " ORDER BY start_line LIMIT ?"
    params.append(limit)

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def query_shell_commands(db_path: Path, limit: int = 100) -> list[dict[str, Any]]:
    """Query shell commands from index."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT sc.command, sc.line, s.start_line, s.end_line "
        "FROM shell_commands sc LEFT JOIN sections s ON sc.section_id = s.id "
        "ORDER BY sc.line LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
