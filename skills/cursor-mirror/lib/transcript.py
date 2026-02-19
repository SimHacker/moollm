# I3: Agent transcript parser -- state machine for ~/.cursor agent-transcripts/*.txt
# Driven by reference/universal/model/dotcursor-schemas.yml (agent_transcript_txt)
# Incremental: remembers file offset + parser state; resumes from last parse.

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Any


class SectionType(Enum):
    USER = auto()
    ASSISTANT = auto()
    TOOL_CALL = auto()
    TOOL_RESULT = auto()
    THINKING = auto()


@dataclass
class ToolParam:
    name: str
    value: str


@dataclass
class Section:
    """One parsed section of a transcript."""
    type: SectionType
    start_line: int
    end_line: int
    text: str = ""
    tool_name: str = ""
    tool_params: list[ToolParam] = field(default_factory=list)
    user_query: str = ""

    @property
    def line_count(self) -> int:
        return self.end_line - self.start_line + 1

    def summary(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "type": self.type.name.lower(),
            "lines": f"{self.start_line}-{self.end_line}",
            "line_count": self.line_count,
        }
        if self.tool_name:
            d["tool"] = self.tool_name
        if self.tool_params:
            d["params"] = {p.name: p.value[:80] for p in self.tool_params}
        if self.user_query:
            d["query_preview"] = self.user_query[:120]
        elif self.text:
            d["text_preview"] = self.text.strip()[:120]
        return d


@dataclass
class ParserState:
    """Resumable parser state for incremental parsing."""
    file_path: str = ""
    file_offset: int = 0
    line_number: int = 0
    current_type: SectionType | None = None
    section_start: int = 0
    in_user_query: bool = False


# Compiled patterns (from dotcursor-schemas.yml agent_transcript_txt.tool_patterns)
_RE_TOOL_CALL = re.compile(r'^\[Tool call\]\s*(.+)$')
_RE_TOOL_RESULT = re.compile(r'^\[Tool result\]\s*(.*)$')
_RE_THINKING = re.compile(r'^\[Thinking\]\s*(.*)$')
_RE_TOOL_PARAM = re.compile(r'^  (\w[\w_-]*): (.*)$')
_RE_USER_QUERY_START = re.compile(r'^<user_query>\s*$')
_RE_USER_QUERY_END = re.compile(r'^</user_query>\s*$')


def parse_transcript(
    path: Path,
    state: ParserState | None = None,
) -> tuple[list[Section], ParserState]:
    """Parse an agent transcript file into structured sections.

    Incremental: pass the returned ParserState back to resume from where
    the last parse left off (for growing transcripts).

    Returns (sections, new_state).
    """
    text = path.read_text(errors="replace")
    lines = text.split("\n")

    if state and state.file_path == str(path) and state.file_offset > 0:
        start_idx = state.line_number
        current_type = state.current_type
        section_start = state.section_start
        in_user_query = state.in_user_query
    else:
        start_idx = 0
        current_type = None
        section_start = 1
        in_user_query = False

    sections: list[Section] = []
    section_lines: list[str] = []
    tool_name = ""
    tool_params: list[ToolParam] = []
    user_query_lines: list[str] = []

    def _finish_section(end_line: int) -> None:
        nonlocal section_lines, tool_name, tool_params, user_query_lines
        if current_type is None:
            section_lines = []
            return
        body = "\n".join(section_lines)
        uq = "\n".join(user_query_lines).strip()
        sections.append(Section(
            type=current_type,
            start_line=section_start,
            end_line=end_line,
            text=body,
            tool_name=tool_name,
            tool_params=list(tool_params),
            user_query=uq,
        ))
        section_lines = []
        tool_name = ""
        tool_params = []
        user_query_lines = []

    for idx in range(start_idx, len(lines)):
        lineno = idx + 1
        line = lines[idx]

        # User turn
        if line.rstrip() in ("user:", "User:"):
            _finish_section(lineno - 1)
            current_type = SectionType.USER
            section_start = lineno
            in_user_query = False
            continue

        # Assistant turn (both "assistant:" and "A:" variants)
        if line.rstrip() in ("assistant:", "Assistant:", "A:"):
            _finish_section(lineno - 1)
            current_type = SectionType.ASSISTANT
            section_start = lineno
            in_user_query = False
            continue

        # Tool call
        m = _RE_TOOL_CALL.match(line)
        if m:
            _finish_section(lineno - 1)
            current_type = SectionType.TOOL_CALL
            section_start = lineno
            tool_name = m.group(1).strip()
            in_user_query = False
            continue

        # Tool result
        m = _RE_TOOL_RESULT.match(line)
        if m:
            _finish_section(lineno - 1)
            current_type = SectionType.TOOL_RESULT
            section_start = lineno
            tool_name = m.group(1).strip()
            in_user_query = False
            continue

        # Thinking block
        m = _RE_THINKING.match(line)
        if m:
            _finish_section(lineno - 1)
            current_type = SectionType.THINKING
            section_start = lineno
            section_lines.append(m.group(1))
            in_user_query = False
            continue

        # Tool params (indented key: value lines inside a tool call)
        if current_type == SectionType.TOOL_CALL:
            m = _RE_TOOL_PARAM.match(line)
            if m:
                tool_params.append(ToolParam(name=m.group(1), value=m.group(2)))
                section_lines.append(line)
                continue

        # User query delimiters
        if _RE_USER_QUERY_START.match(line):
            in_user_query = True
            section_lines.append(line)
            continue
        if _RE_USER_QUERY_END.match(line):
            in_user_query = False
            section_lines.append(line)
            continue

        if in_user_query:
            user_query_lines.append(line)

        section_lines.append(line)

    # Finish the last section
    _finish_section(len(lines))

    new_state = ParserState(
        file_path=str(path),
        file_offset=len(text),
        line_number=len(lines),
        current_type=current_type,
        section_start=section_start,
        in_user_query=in_user_query,
    )

    return sections, new_state


def parse_transcript_incremental(
    path: Path,
    state: ParserState,
) -> tuple[list[Section], ParserState]:
    """Parse only the NEW content appended since the last parse.

    Reads from state.file_offset to end of file. Resumes parser in
    the state it was left in (current section type, in_user_query, etc.).
    """
    text = path.read_text(errors="replace")
    if len(text) <= state.file_offset:
        return [], state

    new_text = text[state.file_offset:]
    new_lines = new_text.split("\n")

    # Build a temporary file with just the new content, but adjust line numbers
    base_lineno = state.line_number
    current_type = state.current_type
    section_start = state.section_start
    in_user_query = state.in_user_query

    sections: list[Section] = []
    section_lines: list[str] = []
    tool_name = ""
    tool_params: list[ToolParam] = []
    user_query_lines: list[str] = []

    def _finish_section(end_line: int) -> None:
        nonlocal section_lines, tool_name, tool_params, user_query_lines
        if current_type is None:
            section_lines = []
            return
        body = "\n".join(section_lines)
        uq = "\n".join(user_query_lines).strip()
        sections.append(Section(
            type=current_type,
            start_line=section_start,
            end_line=end_line,
            text=body,
            tool_name=tool_name,
            tool_params=list(tool_params),
            user_query=uq,
        ))
        section_lines = []
        tool_name = ""
        tool_params = []
        user_query_lines = []

    for i, line in enumerate(new_lines):
        lineno = base_lineno + i + 1

        if line.rstrip() in ("user:", "User:"):
            _finish_section(lineno - 1)
            current_type = SectionType.USER
            section_start = lineno
            in_user_query = False
            continue

        if line.rstrip() in ("assistant:", "Assistant:", "A:"):
            _finish_section(lineno - 1)
            current_type = SectionType.ASSISTANT
            section_start = lineno
            in_user_query = False
            continue

        m = _RE_TOOL_CALL.match(line)
        if m:
            _finish_section(lineno - 1)
            current_type = SectionType.TOOL_CALL
            section_start = lineno
            tool_name = m.group(1).strip()
            in_user_query = False
            continue

        m = _RE_TOOL_RESULT.match(line)
        if m:
            _finish_section(lineno - 1)
            current_type = SectionType.TOOL_RESULT
            section_start = lineno
            tool_name = m.group(1).strip()
            in_user_query = False
            continue

        m = _RE_THINKING.match(line)
        if m:
            _finish_section(lineno - 1)
            current_type = SectionType.THINKING
            section_start = lineno
            section_lines.append(m.group(1))
            in_user_query = False
            continue

        if current_type == SectionType.TOOL_CALL:
            m = _RE_TOOL_PARAM.match(line)
            if m:
                tool_params.append(ToolParam(name=m.group(1), value=m.group(2)))
                section_lines.append(line)
                continue

        if _RE_USER_QUERY_START.match(line):
            in_user_query = True
            section_lines.append(line)
            continue
        if _RE_USER_QUERY_END.match(line):
            in_user_query = False
            section_lines.append(line)
            continue

        if in_user_query:
            user_query_lines.append(line)

        section_lines.append(line)

    _finish_section(base_lineno + len(new_lines))

    new_state = ParserState(
        file_path=str(path),
        file_offset=len(text),
        line_number=base_lineno + len(new_lines),
        current_type=current_type,
        section_start=section_start,
        in_user_query=in_user_query,
    )

    return sections, new_state


# Convenience functions

def get_transcript_path(workspace_id: str, composer_id: str) -> Path | None:
    """Find agent transcript file for a composer."""
    cursor_projects = Path.home() / ".cursor" / "projects"
    if not cursor_projects.exists():
        return None
    for ws_dir in cursor_projects.iterdir():
        if not ws_dir.is_dir():
            continue
        if workspace_id and workspace_id not in ws_dir.name:
            continue
        transcript = ws_dir / "agent-transcripts" / f"{composer_id}.txt"
        if transcript.exists():
            return transcript
    return None


def find_all_transcripts(workspace_filter: str = "") -> list[Path]:
    """Find all agent transcript files, optionally filtered by workspace."""
    cursor_projects = Path.home() / ".cursor" / "projects"
    if not cursor_projects.exists():
        return []
    results: list[Path] = []
    for ws_dir in cursor_projects.iterdir():
        if not ws_dir.is_dir():
            continue
        if workspace_filter and workspace_filter not in ws_dir.name:
            continue
        transcripts_dir = ws_dir / "agent-transcripts"
        if transcripts_dir.exists():
            results.extend(sorted(transcripts_dir.glob("*.txt")))
    return results


def extract_shell_commands(sections: list[Section]) -> list[dict[str, Any]]:
    """Extract all shell/terminal commands from parsed sections.

    Returns list of {command, line, tool_name, params} for R1 shell auditor.
    """
    commands: list[dict[str, Any]] = []
    for s in sections:
        if s.type != SectionType.TOOL_CALL:
            continue
        if s.tool_name not in ("Shell", "shell", "run_terminal_cmd",
                                "run_terminal_command", "run_terminal_command_v2"):
            continue
        cmd = ""
        for p in s.tool_params:
            if p.name == "command":
                cmd = p.value
                break
        if cmd:
            commands.append({
                "command": cmd,
                "line": s.start_line,
                "tool_name": s.tool_name,
                "params": {p.name: p.value for p in s.tool_params},
            })
    return commands
