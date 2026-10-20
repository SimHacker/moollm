#!/usr/bin/env python3
"""Tests for resolve.py against skills/prototype/examples/lookup. Run: python3 test_resolve.py"""

from __future__ import annotations

import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import resolve  # noqa: E402

FIXTURE = HERE.parent / "examples" / "lookup"
ROOT = resolve.find_root(HERE)


def obj(addr: str) -> resolve.Obj:
    return resolve.load_obj(resolve.key_of(str(FIXTURE / addr)), ROOT)


def lookup(addr: str, slot: str) -> tuple[list[resolve.Hit], list[str], list[str]]:
    o = obj(addr)
    hits: list[resolve.Hit] = []
    latent: list[str] = []
    cycles: list[str] = []
    resolve.walk(o, slot, ROOT, [], {o.key}, hits, latent, cycles, first_only=True)
    return hits, latent, cycles


def definer(addr: str, slot: str) -> str | None:
    hits, _, _ = lookup(addr, slot)
    return resolve.rel(hits[0].definer, FIXTURE) if hits else None


def run_cli(*argv: str) -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        resolve.main(["--root", str(ROOT), *argv])
    return buf.getvalue()


def test_own_slot() -> None:
    assert definer("biscuit", "name") == "biscuit"


def test_declared_order_wins() -> None:
    assert definer("biscuit", "sound") == "cat"


def test_depth_first() -> None:
    assert definer("biscuit", "describe") == "pet"


def test_second_named_parent() -> None:
    assert definer("biscuit", "energy") == "sleepy"


def test_named_parent_roles() -> None:
    roles = [p.role for p in obj("biscuit").parents if not p.implied]
    assert roles == ["traits", "mood"]


def test_latent_parent_reported() -> None:
    hits, latent, _ = lookup("cat", "catchphrase")
    assert not hits
    assert "Garfield, the comic-strip cat" in latent


def test_cycle_terminates() -> None:
    hits, _, cycles = lookup("loop-a", "nonexistent-slot")
    assert not hits and cycles


def test_self4_ambiguity_flagged() -> None:
    out = run_cli("lookup", str(FIXTURE / "biscuit"), "sound", "--all")
    assert "self-4: ambiguous" in out and "sleepy" in out


def test_no_ambiguity_when_related() -> None:
    out = run_cli("lookup", str(FIXTURE / "biscuit"), "describe", "--all")
    assert "ambiguous" not in out


def test_legacy_spellings_accepted_and_reported() -> None:
    for d in ({"parents": ["skills/cat"]}, {"parent": "skills/cat"}, {"extends": "skills/cat"},
              {"prototype": "skills/cat"}, {"meta": {"inherits": ["moollm/skills/cat"]}}):
        refs = [r for r, _ in resolve.raw_parent_refs(d)]
        assert refs and refs[0].endswith("skills/cat"), d
        assert resolve.legacy_spellings(d), d
    assert not resolve.legacy_spellings({"inherits": ["skills/cat"]})


def test_done_when_is_the_one_condition_key() -> None:
    assert resolve.legacy_spellings({"goals": [{"id": "g", "complete_when": "x"}]}) == [
        "complete_when: (use done_when:)"]
    assert resolve.legacy_spellings({"research_complete_when": "true"})
    assert not resolve.legacy_spellings({"done_when": "true", "fail_when": "false"})


def test_wrapper_maps_are_not_parents() -> None:
    assert resolve.raw_parent_refs({"prototype": {"name": "ACME catalog", "description": "a long story"}}) == []


def test_modulated_parent() -> None:
    d = {"inherits": [{"ref": "skills/animal", "as": "body", "gets": ["PAT"], "overrides": ["PAT"]}]}
    assert resolve.raw_parent_refs(d) == [("skills/animal", "body")]


def test_ref_forms() -> None:
    forms = {r: resolve.ParentRef(r).form for r in ("EDITH-BUNKER", "skills/nope", "https://x.org/y", "a comic cat")}
    assert forms == {"EDITH-BUNKER": "kline", "skills/nope": "broken", "https://x.org/y": "url", "a comic cat": "prose"}


def test_filename_implies_scoped_skill() -> None:
    p = [p for p in obj("experiment/runs/first/RUN.yml").parents if p.implied]
    assert p and resolve.rel(p[0].target, FIXTURE) == "experiment/skills/run"
    assert definer("experiment/runs/first/RUN.yml", "trials") == "experiment/skills/run"


def test_filename_implies_latent_when_no_skill() -> None:
    p = resolve.implied_parent("MECHANISM", FIXTURE, ROOT, FIXTURE)
    assert p.latent and p.ref == "MECHANISM"


def test_view_falls_through_to_subject() -> None:
    roles = [p.role for p in obj("garden/GLANCE.yml").parents]
    assert roles == ["format", "subject"]
    assert definer("garden/GLANCE.yml", "exits") == "garden"


def test_embedded_object_address() -> None:
    assert definer("garden/ROOM.yml#objects.gnome", "name") == "garden/ROOM.yml#objects.gnome"
    assert definer("garden/ROOM.yml#objects.gnome", "sound") == "cat"
    implied = [p for p in obj("garden/ROOM.yml#objects.bench").parents if p.implied]
    assert implied and implied[0].ref == "object"


def test_envelope_read_as_flat_and_reported() -> None:
    path = Path("ROOM.yml")
    d = {"room": {"name": "Pub", "exits": {"out": ".."}}, "inherits": ["skills/pub"]}
    assert resolve.flat(path, d) == {"inherits": ["skills/pub"], "name": "Pub", "exits": {"out": ".."}}
    assert "envelope room:" in resolve.legacy_spellings(d, path)
    assert not resolve.legacy_spellings({"name": "Pub"}, path)


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"pass  {name}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {name} {e}")
    print(f"{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
