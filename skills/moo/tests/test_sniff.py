import pytest
from lib import sniff


def test_sniff_python():
    text = """
# ignore
def foo():
    pass
class Bar:
    x = 1
@decorator
async def baz():
    pass
# SECTION
"""
    count, lines = sniff.sniff_smelly_lines(text, "x.py")
    assert count >= 4
    line_nos = [ln for ln, _ in lines]
    assert 2 in line_nos or 3 in line_nos  # def foo
    assert any("class Bar" in lt for _, lt in lines)
    assert any("@" in lt for _, lt in lines)


def test_sniff_yaml():
    text = """
name: moo
description: |
  Moo VM
repos:
  - leela-ai/central
"""
    count, lines = sniff.sniff_smelly_lines(text, "x.yml")
    assert count >= 3
    assert any("name:" in lt for _, lt in lines)
    assert any("repos:" in lt for _, lt in lines)


def test_sniff_markdown():
    text = "# Title\n\n## Section\n\nbody\n\n### Sub"
    count, lines = sniff.sniff_smelly_lines(text, "x.md")
    assert count == 3
    assert any("# Title" in lt for _, lt in lines)
    assert any("## Section" in lt for _, lt in lines)
    assert any("### Sub" in lt for _, lt in lines)


def test_sniff_unknown_extension():
    count, lines = sniff.sniff_smelly_lines("def x(): pass", "file.txt")
    assert count == 0
    assert lines == []


def test_sniff_max_lines():
    text = "\n".join([f"x: {i}" for i in range(20)])
    count, lines = sniff.sniff_smelly_lines(text, "x.yml", max_lines=3)
    assert count == 20
    assert len(lines) == 3


def test_sniff_max_chars():
    text = "x: 1\ny: 2\nz: 3\nw: 4\n"
    count, lines = sniff.sniff_smelly_lines(text, "x.yml", max_chars=10)
    assert len(lines) <= 3
    total = sum(len(lt) + 1 for _, lt in lines)
    assert total <= 10 + 5


def test_sniff_skeleton_json():
    content = '{"name": "moo", "repos": [{"repo": "a/b", "depth": 1}, {"repo": "c/d"}]}'
    out = sniff.sniff_skeleton(content, "file.json", max_depth=None, format="text")
    assert out is not None
    assert ".	object	keys: name, repos" in out or "object	keys: name, repos" in out
    assert "repos	array	length: 2" in out
    assert "repos/0	object	keys: repo, depth" in out or "repos/1	object	keys: repo" in out


def test_sniff_skeleton_yaml():
    content = "defaults:\n  depth: 1\nrepos:\n  - repo: leela-ai/alerts\n  - repo: leela-ai/central\n"
    out = sniff.sniff_skeleton(content, "overlay.yml", max_depth=None, format="text")
    assert out is not None
    assert "object	keys:" in out and "array	length:" in out


def test_sniff_skeleton_depth_clips():
    content = '{"a": {"b": {"c": 1}}, "x": [1, 2]}'
    out = sniff.sniff_skeleton(content, "f.json", max_depth=1, format="text")
    assert out is not None
    assert "a	object	keys: b" in out
    assert "x	array	length: 2" in out
    assert "a/b/c" not in out
    full = sniff.sniff_skeleton(content, "f.json", max_depth=None, format="text")
    assert "a/b/c" in full


def test_sniff_skeleton_non_structured_returns_none():
    assert sniff.sniff_skeleton("def x(): pass", "file.py") is None
    assert sniff.sniff_skeleton("not json", "file.json") is None
    assert sniff.sniff_skeleton("42", "file.json") is None


def test_sniff_skeleton_data_subtree():
    subtree = {"items": [{"id": 1}, {"id": 2}], "total": 2}
    out = sniff.sniff_skeleton_data(subtree, max_depth=2, format="text", path_prefix="payload")
    assert out is not None
    assert "payload\tobject\tkeys: items, total" in out
    assert "payload/items\tarray\tlength: 2" in out
    assert "payload/items/0\tobject\tkeys: id" in out
