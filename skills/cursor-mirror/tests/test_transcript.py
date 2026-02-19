# Layer 1+2: transcript parser tests -- synthetic and real transcripts.

from pathlib import Path

from lib.transcript import (
    Section, SectionType, ParserState, ToolParam,
    parse_transcript, parse_transcript_incremental,
    find_all_transcripts, extract_shell_commands,
)

SYNTHETIC = """\
user:
<user_query>
What is 2+2?
</user_query>

assistant:
The answer is 4.
[Tool call] Shell
  command: echo hello
  description: Say hello

[Tool result] Shell

assistant:
Done.
[Thinking] Let me verify that worked.
[Tool call] Read
  path: /tmp/test.txt

[Tool result] Read

assistant:
All good.
"""


def test_parse_synthetic():
    tmp = Path("/tmp/test_transcript.txt")
    tmp.write_text(SYNTHETIC)
    sections, state = parse_transcript(tmp)
    tmp.unlink()

    types = [s.type for s in sections]
    assert SectionType.USER in types
    assert SectionType.ASSISTANT in types
    assert SectionType.TOOL_CALL in types
    assert SectionType.TOOL_RESULT in types
    assert SectionType.THINKING in types


def test_user_query_extracted():
    tmp = Path("/tmp/test_transcript.txt")
    tmp.write_text(SYNTHETIC)
    sections, _ = parse_transcript(tmp)
    tmp.unlink()

    user_sections = [s for s in sections if s.type == SectionType.USER]
    assert len(user_sections) == 1
    assert "What is 2+2?" in user_sections[0].user_query


def test_tool_call_params():
    tmp = Path("/tmp/test_transcript.txt")
    tmp.write_text(SYNTHETIC)
    sections, _ = parse_transcript(tmp)
    tmp.unlink()

    tool_calls = [s for s in sections if s.type == SectionType.TOOL_CALL]
    assert len(tool_calls) == 2
    shell_call = tool_calls[0]
    assert shell_call.tool_name == "Shell"
    param_names = [p.name for p in shell_call.tool_params]
    assert "command" in param_names


def test_thinking_content():
    tmp = Path("/tmp/test_transcript.txt")
    tmp.write_text(SYNTHETIC)
    sections, _ = parse_transcript(tmp)
    tmp.unlink()

    thinking = [s for s in sections if s.type == SectionType.THINKING]
    assert len(thinking) == 1
    assert "verify" in thinking[0].text


def test_incremental_parse():
    tmp = Path("/tmp/test_transcript.txt")
    part1 = "user:\n<user_query>\nHello\n</user_query>\n\nassistant:\nHi there.\n"
    part2 = "user:\n<user_query>\nBye\n</user_query>\n\nassistant:\nGoodbye.\n"

    tmp.write_text(part1)
    sections1, state = parse_transcript(tmp)

    tmp.write_text(part1 + part2)
    sections2, state2 = parse_transcript_incremental(tmp, state)
    tmp.unlink()

    assert len(sections1) >= 2
    assert len(sections2) >= 2
    user_queries = [s.user_query for s in sections2 if s.type == SectionType.USER]
    assert any("Bye" in q for q in user_queries)


def test_extract_shell_commands():
    tmp = Path("/tmp/test_transcript.txt")
    tmp.write_text(SYNTHETIC)
    sections, _ = parse_transcript(tmp)
    tmp.unlink()

    cmds = extract_shell_commands(sections)
    assert len(cmds) == 1
    assert cmds[0]["command"] == "echo hello"
    assert cmds[0]["tool_name"] == "Shell"


def test_section_summary():
    s = Section(
        type=SectionType.TOOL_CALL,
        start_line=10,
        end_line=15,
        tool_name="Shell",
        tool_params=[ToolParam("command", "ls -la")],
    )
    summary = s.summary()
    assert summary["type"] == "tool_call"
    assert summary["tool"] == "Shell"
    assert "command" in summary["params"]


def test_find_all_transcripts():
    transcripts = find_all_transcripts()
    assert isinstance(transcripts, list)
    if transcripts:
        assert all(t.suffix == ".txt" for t in transcripts)


def test_parse_real_transcript():
    """Parse a real transcript from this machine."""
    transcripts = find_all_transcripts()
    if not transcripts:
        return
    smallest = min(transcripts, key=lambda t: t.stat().st_size)
    sections, state = parse_transcript(smallest)

    assert len(sections) > 0
    type_counts = {}
    for s in sections:
        type_counts[s.type.name] = type_counts.get(s.type.name, 0) + 1

    print(f"\nParsed {smallest.name} ({smallest.stat().st_size} bytes):")
    print(f"  Sections: {len(sections)}")
    print(f"  Types: {type_counts}")
    print(f"  State offset: {state.file_offset}")

    cmds = extract_shell_commands(sections)
    if cmds:
        print(f"  Shell commands: {len(cmds)}")
        print(f"  First: {cmds[0]['command'][:80]}")


def test_parse_largest_transcript():
    """Parse the largest transcript -- stress test."""
    transcripts = find_all_transcripts()
    if not transcripts:
        return
    largest = max(transcripts, key=lambda t: t.stat().st_size)
    sections, state = parse_transcript(largest)

    type_counts = {}
    for s in sections:
        type_counts[s.type.name] = type_counts.get(s.type.name, 0) + 1

    cmds = extract_shell_commands(sections)

    print(f"\nParsed {largest.name} ({largest.stat().st_size / 1024:.0f} KB):")
    print(f"  Sections: {len(sections)}")
    print(f"  Types: {type_counts}")
    print(f"  Shell commands: {len(cmds)}")

    assert len(sections) > 10
