#!/usr/bin/env python3
"""Tests for refs.py. Run: python3 -m unittest skills/prototype/scripts/test_refs.py"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import refs  # noqa: E402
from refs import Ref, locate, parse_ref, to_uri  # noqa: E402

MOOLLM = next(p for p in [HERE, *HERE.parents] if (p / ".git").exists())
SIBLINGS = MOOLLM.parent
WWSFF = SIBLINGS / "WillWrightShowForFood"
PALM = WWSFF / "characters" / "palm" / "CHARACTER.yml"
PALM_SEAT = WWSFF / "repo-shows" / "will-wright-premiere" / "audience" / "palm" / "CHARACTER.yml"
MONKEY_PALM = Ref("SimHacker", "moollm", "examples/adventure-4/characters/animals/monkey-palm", "", "dir")
MONKEY_PALM_URI = "moollm://github/SimHacker/moollm/examples/adventure-4/characters/animals/monkey-palm/"

# Copied from WillWrightShowForFood/characters/palm/CHARACTER.yml, so these tests run without the checkout.
PALM_INHERITS = {
    "repo": "SimHacker/moollm",
    "path": "moollm/examples/adventure-4/characters/animals/monkey-palm",
    "absolute_url": "https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/animals/monkey-palm",
    "canonical_dir": "examples/adventure-4/characters/animals/monkey-palm/",
    "character_url": "https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/animals/monkey-palm",
    "home_room": "https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/pub/stage/palm-nook",
    "home_room_path": "moollm/examples/adventure-4/pub/stage/palm-nook",
    "card": "https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/animals/monkey-palm/CARD.yml",
    "character_yml": "https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/characters/animals/monkey-palm/CHARACTER.yml",
}
PALM_MOOLLM_SOURCE = {
    "absolute_url": "https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/animals/monkey-palm",
    "repo": "SimHacker/moollm",
    "path": "moollm/examples/adventure-4/characters/animals/monkey-palm",
    "note": "Canonical Palm. Resolve shorthand paths against absolute_url.",
}


class UriForm(unittest.TestCase):
    def test_directory(self) -> None:
        self.assertEqual(parse_ref("moollm://github/SimHacker/moollm/skills/real-being/"),
                         Ref("SimHacker", "moollm", "skills/real-being", "", "dir"))

    def test_file_with_fragment(self) -> None:
        r = parse_ref("moollm://github/SimHacker/moollm/examples/aisle-e/PROTOTYPES.yml#prototypes.wine-rack")
        self.assertEqual(r, Ref("SimHacker", "moollm", "examples/aisle-e/PROTOTYPES.yml", "prototypes.wine-rack", "file"))

    def test_repo_root(self) -> None:
        self.assertEqual(parse_ref("moollm://github/SimHacker/DonHopkins/"), Ref("SimHacker", "DonHopkins", "", "", "dir"))

    def test_unknown_repo_keeps_its_owner(self) -> None:
        self.assertEqual(parse_ref("moollm://github/open-simh/simh/PDP18B/"), Ref("open-simh", "simh", "PDP18B", "", "dir"))


class GithubUrls(unittest.TestCase):
    def test_tree_is_a_directory(self) -> None:
        self.assertEqual(parse_ref(PALM_INHERITS["absolute_url"]), MONKEY_PALM)

    def test_blob_is_a_file(self) -> None:
        r = parse_ref(PALM_INHERITS["card"])
        self.assertEqual(r, Ref("SimHacker", "moollm", MONKEY_PALM.path + "/CARD.yml", "", "file"))

    def test_line_anchor_is_not_a_slot_path(self) -> None:
        self.assertEqual(parse_ref("https://github.com/SimHacker/moollm/blob/main/README.md#L10-L20").fragment, "")

    def test_other_branch_and_raw(self) -> None:
        self.assertEqual(parse_ref("https://github.com/open-simh/simh/blob/master/PDP18B/pdp18b_cpu.c"),
                         Ref("open-simh", "simh", "PDP18B/pdp18b_cpu.c", "", "file"))
        self.assertEqual(parse_ref("https://raw.githubusercontent.com/open-simh/simh/master/PDP18B/pdp18b_cpu.c"),
                         Ref("open-simh", "simh", "PDP18B/pdp18b_cpu.c", "", "file"))

    def test_repo_url_and_git_suffix_and_case(self) -> None:
        self.assertEqual(parse_ref("https://github.com/simhacker/MOOLLM.git"), Ref("SimHacker", "moollm", "", "", "dir"))


class RepoRelative(unittest.TestCase):
    def test_known_repo_prefix(self) -> None:
        self.assertEqual(parse_ref("moollm/examples/adventure-4/characters/animals/monkey-palm"), MONKEY_PALM)
        self.assertEqual(parse_ref("WillWrightShowForFood/characters/palm/CHARACTER.yml"),
                         Ref("SimHacker", "WillWrightShowForFood", "characters/palm/CHARACTER.yml", "", "file"))

    def test_owner_repo_prefix(self) -> None:
        self.assertEqual(parse_ref("SimHacker/moollm/skills/real-being/"), Ref("SimHacker", "moollm", "skills/real-being", "", "dir"))

    def test_every_known_repo(self) -> None:
        for repo, owner in refs.KNOWN_REPOS.items():
            self.assertEqual(parse_ref(f"{repo}/README.md"), Ref(owner, repo, "README.md", "", "file"), repo)


class MapForm(unittest.TestCase):
    def test_palm_inherits(self) -> None:
        self.assertEqual(parse_ref(PALM_INHERITS), MONKEY_PALM)

    def test_palm_moollm_source(self) -> None:
        self.assertEqual(parse_ref(PALM_MOOLLM_SOURCE), MONKEY_PALM)

    def test_repo_and_path_without_url(self) -> None:
        self.assertEqual(parse_ref({"repo": "SimHacker/moollm", "path": PALM_INHERITS["path"]}), MONKEY_PALM)
        self.assertEqual(parse_ref({"repo": "SimHacker/moollm", "canonical_dir": PALM_INHERITS["canonical_dir"]}), MONKEY_PALM)
        self.assertEqual(parse_ref({"repo": "SimHacker/moollm", "path": "examples/adventure-4/"}),
                         Ref("SimHacker", "moollm", "examples/adventure-4", "", "dir"))

    def test_only_file_urls(self) -> None:
        self.assertEqual(parse_ref({"character_yml": PALM_INHERITS["character_yml"]}).path, MONKEY_PALM.path + "/CHARACTER.yml")

    def test_modulated_parent(self) -> None:
        self.assertEqual(parse_ref({"ref": MONKEY_PALM_URI, "as": "body"}), MONKEY_PALM)

    def test_local_path_map(self) -> None:
        self.assertEqual(parse_ref({"path": "../../palm/"}), Ref(None, None, "../../palm", "", "dir"))

    def test_skills_map_is_not_a_ref(self) -> None:
        self.assertIsNone(parse_ref({"moollm_skills": ["character", "mind-mirror"], "overlay_protocol": "../MOOLLM-OVERLAY.yml"}))


@unittest.skipUnless(PALM.is_file(), "needs the WillWrightShowForFood checkout")
class RealPalmFile(unittest.TestCase):
    def test_inherits_and_moollm_source_agree(self) -> None:
        data = yaml.safe_load(PALM.read_text(encoding="utf-8"))
        self.assertEqual(parse_ref(data["inherits"]), MONKEY_PALM)
        self.assertEqual(parse_ref(data["moollm_source"]), MONKEY_PALM)

    def test_dream_entries(self) -> None:
        data = yaml.safe_load(PALM.read_text(encoding="utf-8"))
        for entry in data["dreams"]["entries"]:
            r = parse_ref(entry)
            self.assertEqual((r.repo, r.kind), ("moollm", "file"), entry)
            self.assertEqual(r, parse_ref({"repo": entry["repo"], "path": entry["path"]}))

    def test_inherited_directory_is_local(self) -> None:
        self.assertEqual(locate(parse_ref(yaml.safe_load(PALM.read_text(encoding="utf-8"))["inherits"]), roots=[SIBLINGS]),
                         SIBLINGS / "moollm" / MONKEY_PALM.path)


class Relative(unittest.TestCase):
    def test_plain_paths(self) -> None:
        self.assertEqual(parse_ref("../../../../characters/palm/CHARACTER.yml"),
                         Ref(None, None, "../../../../characters/palm/CHARACTER.yml", "", "file"))
        self.assertEqual(parse_ref("skills/animal"), Ref(None, None, "skills/animal", "", "dir"))
        self.assertEqual(parse_ref("ROOM.yml#objects.bench"), Ref(None, None, "ROOM.yml", "objects.bench", "file"))
        self.assertEqual(parse_ref("#objects.bench"), Ref(None, None, "", "objects.bench", "file"))
        self.assertEqual(parse_ref(".."), Ref(None, None, "..", "", "dir"))

    def test_relative_has_no_uri_until_absolutized(self) -> None:
        self.assertIsNone(to_uri(parse_ref("skills/animal")))

    @unittest.skipUnless(PALM_SEAT.is_file(), "needs the WillWrightShowForFood checkout")
    def test_audience_seat_to_profile(self) -> None:
        r = parse_ref("../../../../characters/palm/CHARACTER.yml", base=PALM_SEAT, roots=[SIBLINGS])
        self.assertEqual(r, Ref("SimHacker", "WillWrightShowForFood", "characters/palm/CHARACTER.yml", "", "file"))
        self.assertEqual(to_uri(r), "moollm://github/SimHacker/WillWrightShowForFood/characters/palm/CHARACTER.yml")
        self.assertEqual(locate("../../../../characters/palm/CHARACTER.yml", PALM_SEAT, [SIBLINGS]), PALM)

    def test_escape_into_a_sibling(self) -> None:
        base = SIBLINGS / "WillWrightShowForFood" / "characters" / "menagerie" / "palm" / "CHARACTER.yml"
        r = parse_ref("../../../../moollm/skills/real-being/", base=base, roots=[SIBLINGS])
        self.assertEqual(r, Ref("SimHacker", "moollm", "skills/real-being", "", "dir"))

    def test_outside_every_root_stays_relative(self) -> None:
        self.assertEqual(parse_ref("../x.yml", base="/nowhere/a/b.yml", roots=[SIBLINGS]), Ref(None, None, "../x.yml", "", "file"))


class NotRefs(unittest.TestCase):
    def test_bare_ids_klines_prose(self) -> None:
        for v in ("real-being", "EDITH-BUNKER", "Garfield, the comic-strip cat", "a comic cat"):
            self.assertIsNone(parse_ref(v), v)

    def test_bad_input_never_raises(self) -> None:
        for v in (None, 42, 3.5, [], ["moollm/x"], {}, "", "   ", "line\nbreak", "x" * 600,
                  "moollm://github/", "moollm://github/onlyowner", "moollm://github/a/b/../../../etc/passwd",
                  "https://example.com/x/y", "https://github.com/", "ftp://github.com/a/b",
                  {"repo": 7, "path": None}, {"repo": "a/b/c/d"}, {"ref": {"ref": {"ref": None}}}, object()):
            self.assertIsNone(parse_ref(v), repr(v)[:40])
            self.assertIsNone(locate(v, "/tmp/x.yml"), repr(v)[:40])
            self.assertIsNone(to_uri(parse_ref(v)))


class Canonical(unittest.TestCase):
    def test_uri(self) -> None:
        self.assertEqual(to_uri(parse_ref(PALM_INHERITS)), MONKEY_PALM_URI)
        self.assertEqual(to_uri(parse_ref(PALM_INHERITS["card"])), MONKEY_PALM_URI + "CARD.yml")
        self.assertEqual(to_uri(Ref("SimHacker", "moollm", "", "", "dir")), "moollm://github/SimHacker/moollm/")

    def test_round_trip(self) -> None:
        for v in (MONKEY_PALM_URI, PALM_INHERITS["card"], "moollm://github/SimHacker/moollm/a/B.yml#objects.x",
                  "SimHacker/moollm/", "DonHopkins/characters/will-wright/CHARACTER.yml"):
            r = parse_ref(v)
            self.assertEqual(parse_ref(to_uri(r)), r, v)

    def test_github_url(self) -> None:
        self.assertEqual(refs.github_url(MONKEY_PALM), PALM_INHERITS["absolute_url"])
        self.assertEqual(refs.github_url(parse_ref(PALM_INHERITS["card"])), PALM_INHERITS["card"])
        self.assertEqual(refs.github_url(Ref("SimHacker", "moollm", "", "", "dir")), "https://github.com/SimHacker/moollm")


class Locate(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        (self.root / "moollm" / "skills" / "cat").mkdir(parents=True)
        (self.root / "moollm" / "skills" / "cat" / "SKILL.md").write_text("cat\n")
        (self.root / "moollm" / "examples" / "pub").mkdir(parents=True)
        self.pub_room = self.root / "moollm" / "examples" / "pub" / "ROOM.yml"
        self.pub_room.write_text("name: Pub\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_local_checkout(self) -> None:
        self.assertEqual(locate("moollm://github/SimHacker/moollm/skills/cat/", roots=[self.root]), self.root / "moollm/skills/cat")

    def test_missing_falls_back_to_github(self) -> None:
        self.assertEqual(locate("moollm://github/SimHacker/moollm/skills/dog/", roots=[self.root]),
                         "https://github.com/SimHacker/moollm/tree/main/skills/dog")
        self.assertEqual(locate("moollm://github/SimHacker/mooco/README.md", roots=[self.root]),
                         "https://github.com/SimHacker/mooco/blob/main/README.md")

    def test_env_roots_come_first(self) -> None:
        with mock.patch.dict(os.environ, {"MOOLLM_ROOTS": f"/nonexistent{os.pathsep}{self.root}"}):
            roots = refs.default_roots()
            self.assertEqual(roots[:2], [Path("/nonexistent"), self.root])
            self.assertEqual(locate("moollm/skills/cat/SKILL.md"), self.root / "moollm/skills/cat/SKILL.md")

    def test_relative_walks_up_to_the_checkout(self) -> None:
        self.assertEqual(locate("skills/cat", self.pub_room, [self.root]), self.root / "moollm/skills/cat")
        self.assertEqual(locate("../pub/ROOM.yml", self.pub_room, [self.root]), self.pub_room)
        self.assertEqual(locate("#objects.bench", self.pub_room, [self.root]), self.pub_room)

    def test_relative_missing_gives_url_inside_a_checkout(self) -> None:
        self.assertEqual(locate("../bar/ROOM.yml", self.pub_room, [self.root]),
                         "https://github.com/SimHacker/moollm/blob/main/examples/bar/ROOM.yml")

    def test_relative_without_from_file(self) -> None:
        self.assertIsNone(locate("skills/cat", None, [self.root]))

    def test_default_roots_find_this_checkout(self) -> None:
        self.assertIn(SIBLINGS, refs.default_roots())
        self.assertEqual(locate("moollm://github/SimHacker/moollm/skills/prototype/scripts/refs.py"), HERE / "refs.py")


if __name__ == "__main__":
    unittest.main()
