#!/usr/bin/env python3
"""Tests for layers_lint.py against temporary sibling repos. Run: python3 test_layers_lint.py"""
from __future__ import annotations

import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layers_lint as ll  # noqa: E402

BIO = "DonHopkins/characters"
PROFILE = "WillWrightShowForFood/characters"
CAST = "WillWrightShowForFood/characters/menagerie"
AUDIENCE = "WillWrightShowForFood/repo-shows/show/audience"
ADVENTURE = "moollm/examples/adventure-4/characters"


def person(i: str, consent: Any = 3, envelope: bool = True, **extra: Any) -> dict[str, Any]:
    core = {"id": i, "name": i.replace("-", " ").title(), "real_being": True, "status": "living",
            "signifier": "👤"}
    core.update({k: v for k, v in extra.items() if k != "representation"})
    rep = extra.get("representation", {"consent_level": consent, "authored_by": "don-hopkins"})
    if envelope:
        return {"character": core, "representation": rep}
    return {**core, "representation": rep}


class LintCase(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="layers_lint_"))
        for repo in ("moollm", "DonHopkins", "WillWrightShowForFood"):
            (self.root / repo).mkdir()
        (self.root / "moollm/skills/real-being").mkdir(parents=True)
        self.saved_refs = ll._refs
        ll._refs = None

    def tearDown(self) -> None:
        ll._refs = self.saved_refs
        shutil.rmtree(self.root)

    def put(self, where: str, i: str, data: Any) -> Path:
        p = self.root / where / i / "CHARACTER.yml"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(data if isinstance(data, str) else yaml.safe_dump(data, allow_unicode=True))
        return p

    def lint(self, ids: list[str] | None = None) -> dict[str, Any]:
        return ll.run(self.root, ids)

    def rules(self, res: dict[str, Any], i: str | None = None) -> list[tuple[str, str]]:
        return [(f.severity, f.rule) for f in res["findings"] if i is None or f.id == i]


class FactTests(LintCase):
    def test_consent_disagreement_is_error_and_review_item(self) -> None:
        self.put(BIO, "bill", person("bill", 3))
        self.put(PROFILE, "bill", person("bill", 1, inherits=["moollm://github/x/DonHopkins/characters/bill/"]))
        res = self.lint()
        errs = [f for f in res["findings"] if f.severity == "error"]
        self.assertEqual([(f.rule, f.file) for f in errs],
                         [("consent-level", f"{PROFILE}/bill/CHARACTER.yml")])
        self.assertIn("1 here", errs[0].message)
        self.assertEqual(errs[0].layers, ["donhopkins", "wwsff-profile"])
        self.assertEqual(len(res["review"]), 1)
        item = res["review"][0]
        self.assertEqual((item["id"], item["fact"], item["decision"]), ("bill", "consent_level", None))
        self.assertEqual(sorted(v["value"] for v in item["values"]), [1, 3])

    def test_spellings_normalize(self) -> None:
        self.put(BIO, "mouse", person("mouse", 5, status="deceased", signifier="🕯️"))
        self.put(PROFILE, "mouse", person("mouse", "5_deceased_legacy", status="memorial", signifier="🕯"))
        self.put(BIO, "don", person("don", 1))
        self.put(PROFILE, "don", person("don", representation={"consent": "self-sovereign"}))
        res = self.lint()
        self.assertNotIn("error", [s for s, _ in self.rules(res)])
        self.assertEqual(self.rules(res, "mouse").count(("info", "consent-spelling")), 1)
        self.assertIn(("info", "consent-spelling"), self.rules(res, "don"))
        self.assertNotIn(("info", "signifier"), self.rules(res, "mouse"))

    def test_life_facts(self) -> None:
        self.put(BIO, "al", person("al", dates={"born": 1940, "died": 2020}))
        self.put(PROFILE, "al", person("al", born="1940-05-17", memorial={"died": 2021}))
        res = self.lint()
        self.assertEqual([r for r in self.rules(res, "al") if r[0] == "error"], [("error", "fact-died")])
        self.assertEqual([i["fact"] for i in res["review"]], ["died"])

    def test_status_living_vs_deceased_is_error(self) -> None:
        self.put(BIO, "z", person("z", status="living"))
        self.put(PROFILE, "z", person("z", status="memorial"))
        self.assertIn(("error", "fact-status"), self.rules(self.lint(), "z"))

    def test_status_vocabulary_is_warning(self) -> None:
        self.put(ADVENTURE, "bot", {"id": "bot", "name": "Bot", "status": "active", "signifier": "🤖"})
        self.put(CAST, "bot", {"character": {"id": "bot", "name": "Bot", "status": "reified",
                                             "real_being": False, "signifier": "🤖"}})
        r = self.rules(self.lint(), "bot")
        self.assertIn(("warning", "status-vocabulary"), r)
        self.assertNotIn("error", [s for s, _ in r])

    def test_name_disagreement_is_warning(self) -> None:
        self.put(BIO, "n", person("n", name="Ann Smith"))
        self.put(PROFILE, "n", person("n", name="Anne Smith"))
        self.assertIn(("warning", "fact-name"), self.rules(self.lint(), "n"))


class RelationTests(LintCase):
    def test_missing_relation_on_non_canonical_layer(self) -> None:
        self.put(BIO, "p", person("p"))
        self.put(PROFILE, "p", person("p"))
        res = self.lint()
        missing = [f for f in res["findings"] if f.rule == "relation-missing"]
        self.assertEqual([f.file for f in missing], [f"{PROFILE}/p/CHARACTER.yml"])
        self.assertEqual(missing[0].severity, "warning")

    def test_parent_that_is_not_a_layer_still_missing(self) -> None:
        self.put(BIO, "p", person("p"))
        self.put(PROFILE, "p", person("p", inherits=["moollm://github/SimHacker/moollm/skills/real-being/"]))
        res = self.lint()
        self.assertIn(("warning", "relation-missing"), self.rules(res, "p"))
        self.assertNotIn(("warning", "ref-unresolved"), self.rules(res, "p"))

    def test_legacy_spelling_counts_and_is_reported(self) -> None:
        self.put(BIO, "p", person("p", public_portrayal="WillWrightShowForFood/characters/p/"))
        self.put(PROFILE, "p", person("p", moollm_source={
            "repo": "SimHacker/DonHopkins", "path": "DonHopkins/characters/p",
            "absolute_url": "https://github.com/SimHacker/DonHopkins/tree/main/characters/p"}))
        r = self.rules(self.lint(), "p")
        self.assertNotIn(("warning", "relation-missing"), r)
        self.assertNotIn(("warning", "ref-unresolved"), r)
        self.assertEqual(r.count(("info", "relation-alias")), 2)

    def test_relative_ref_and_see_also(self) -> None:
        self.put(PROFILE, "q", person("q"))
        self.put(AUDIENCE, "q", person("q", character_ref="../../../../characters/q/CHARACTER.yml"))
        self.put(BIO, "q", person("q", see_also=["../../../WillWrightShowForFood/characters/q/"]))
        r = self.rules(self.lint(), "q")
        self.assertEqual(r.count(("warning", "relation-missing")), 1)
        self.assertEqual(r.count(("info", "relation-alias")), 2)

    def test_unresolved_ref(self) -> None:
        self.put(BIO, "u", person("u"))
        self.put(PROFILE, "u", person("u", upstream="../../../DonHopkins/characters/nobody/"))
        self.assertIn(("warning", "ref-unresolved"), self.rules(self.lint(), "u"))

    def test_absent_repo_and_foreign_urls_are_not_checked(self) -> None:
        self.put(BIO, "u", person("u"))
        self.put(PROFILE, "u", person("u", inherits=["moollm://github/x/RepoShowPrivate/characters/u/",
                                                    "https://example.com/u"]))
        self.assertNotIn(("warning", "ref-unresolved"), self.rules(self.lint(), "u"))

    def test_fictional_canonical_is_adventure(self) -> None:
        self.put(ADVENTURE, "grue", {"id": "grue", "name": "Grue", "status": "fictional",
                                    "signifier": "👾", "inherits": ["skills/real-being"]})
        self.put(CAST, "grue", {"character": {"id": "grue", "name": "Grue", "real_being": False,
                                              "status": "fictional", "signifier": "👾"}})
        res = self.lint()
        missing = [f.file for f in res["findings"] if f.rule == "relation-missing"]
        self.assertEqual(missing, [f"{CAST}/grue/CHARACTER.yml"])
        self.assertNotIn(("info", "signifier"), self.rules(res, "grue"))
        self.assertNotIn(("warning", "key-missing"), self.rules(res, "grue"))


class KeyAndSignifierTests(LintCase):
    def test_core_keys_for_real_being(self) -> None:
        self.put(BIO, "k", person("k"))
        self.put(PROFILE, "k", {"character": {"id": "k", "name": "K", "status": "living"}})
        res = self.lint()
        msgs = [f.message for f in res["findings"] if f.rule == "key-missing"]
        self.assertEqual(msgs, ["core keys missing: signifier, real_being, representation.consent_level"])

    def test_signifier_convention(self) -> None:
        self.put(BIO, "w", person("w", signifier="🌍"))
        self.put(PROFILE, "w", person("w", envelope=False))
        res = self.lint()
        sig = [f for f in res["findings"] if f.rule == "signifier"]
        self.assertEqual([(f.severity, f.file) for f in sig], [("info", f"{BIO}/w/CHARACTER.yml")])
        self.assertIn("move to emoji:", sig[0].message)


class RobustnessTests(LintCase):
    def test_single_layer_ids_skipped_unless_named(self) -> None:
        self.put(BIO, "solo", person("solo"))
        self.assertEqual(self.lint()["checked"], [])
        self.assertEqual(self.rules(self.lint(["solo"])), [("info", "single-layer")])
        self.assertEqual(self.rules(self.lint(["ghost"])), [("info", "single-layer")])

    def test_unparseable_file_does_not_crash(self) -> None:
        self.put(BIO, "x", person("x"))
        self.put(PROFILE, "x", person("x"))
        self.put(ADVENTURE, "x", "id: x\n  bad: [unclosed\n")
        self.assertIn(("warning", "unparseable"), self.rules(self.lint(), "x"))

    def test_broken_refs_module_falls_back(self) -> None:
        class Broken:
            @staticmethod
            def locate(*a: Any, **k: Any) -> Any:
                raise RuntimeError("boom")

            @staticmethod
            def parse_ref(*a: Any, **k: Any) -> Any:
                raise ValueError("nope")

        ll._refs = Broken()
        self.put(BIO, "r", person("r"))
        self.put(PROFILE, "r", person("r", inherits=["moollm://github/x/DonHopkins/characters/r/"]))
        self.assertNotIn(("warning", "relation-missing"), self.rules(self.lint(), "r"))

    def test_refs_module_hit_is_used(self) -> None:
        target = self.put(BIO, "s", person("s"))

        class Hit:
            @staticmethod
            def locate(ref: str, base: Path, root: Path) -> Path:
                return target.parent

        ll._refs = Hit()
        self.put(PROFILE, "s", person("s", inherits=["somewhere:only-refs-knows"]))
        self.assertNotIn(("warning", "relation-missing"), self.rules(self.lint(), "s"))

    def test_with_real_refs_module(self) -> None:
        try:
            import refs
        except Exception:
            self.skipTest("refs.py not importable")
        ll._refs = refs
        self.put(BIO, "t", person("t"))
        self.put(PROFILE, "t", person("t", inherits=["moollm://github/SimHacker/DonHopkins/characters/t/"],
                                      upstream="../../../DonHopkins/characters/missing/"))
        r = self.rules(self.lint(), "t")
        self.assertNotIn(("warning", "relation-missing"), r)
        self.assertIn(("warning", "ref-unresolved"), r)


class CliTests(LintCase):
    def cli(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ll.main([*argv, "--root", str(self.root)])
        return code, out.getvalue(), err.getvalue()

    def test_text_yaml_summary_and_review(self) -> None:
        self.put(BIO, "b", person("b", 3))
        self.put(PROFILE, "b", person("b", 2))
        review = self.root / "out" / "REVIEW.yml"
        code, out, _ = self.cli("--review", str(review))
        self.assertEqual(code, 1)
        self.assertIn("consent-level", out)
        text = review.read_text()
        self.assertTrue(text.startswith("# Facts for Don to decide. Agents must not resolve them."))
        doc = yaml.safe_load(text)
        self.assertEqual([(i["id"], i["fact"]) for i in doc["items"]], [("b", "consent_level")])

        code, out, _ = self.cli("--format", "yaml", "--summary")
        doc = yaml.safe_load(out)
        self.assertEqual(doc["summary"]["findings"]["error"], 1)
        self.assertNotIn("findings", {k for k in doc if k != "summary"})

        code, out, _ = self.cli("--format", "yaml")
        self.assertEqual({f["rule"] for f in yaml.safe_load(out)["findings"] if f["severity"] == "error"},
                         {"consent-level"})

    def test_clean_exit_zero(self) -> None:
        self.put(BIO, "c", person("c"))
        self.put(PROFILE, "c", person("c", derived_from="../../../DonHopkins/characters/c/"))
        code, out, _ = self.cli("--summary")
        self.assertEqual(code, 0)
        self.assertIn("error 0", out)


if __name__ == "__main__":
    unittest.main()
