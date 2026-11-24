#!/usr/bin/env python3
"""Unit tests for censor_sim. Run: python3 -m unittest test_censor_sim -v
(from this directory), or `python3 test_censor_sim.py`.

The scenario suite (`censor_sim.py suite PATH...`) checks models against
records; these check the engine's own rules, one at a time."""

import io
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import censor_sim as cs  # noqa: E402

EXAMPLES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "censors", "examples")


def mind(items=None, values=None, schemas=(), censors=(), contradictions=(), **agent):
    spec = {"agent": {"name": "test", "items": items or {}, "values": values or {},
                      "contradictions": [list(p) for p in contradictions], **agent},
            "schemas": list(schemas), "censors": list(censors)}
    return cs.Mind(spec)


class Merge(unittest.TestCase):
    def test_dicts_merge(self):
        self.assertEqual(cs.merge({"a": 1, "b": {"c": 2}}, {"b": {"d": 3}}),
                         {"a": 1, "b": {"c": 2, "d": 3}})

    def test_ids_merge_and_drop(self):
        base = [{"id": "x", "cover": ""}, {"id": "y"}]
        self.assertEqual(cs.merge(base, [{"id": "x", "cover": "mine"}]),
                         [{"id": "x", "cover": "mine"}, {"id": "y"}])
        self.assertEqual(cs.merge(base, [{"id": "x", "drop": True}]), [{"id": "y"}])

    def test_pairs_accumulate(self):
        self.assertEqual(cs.merge([["a", "b"]], [["c", "d"], ["a", "b"]]), [["a", "b"], ["c", "d"]])

    def test_other_lists_replace(self):
        self.assertEqual(cs.merge(["a", "b"], ["c"]), ["c"])


class Conditions(unittest.TestCase):
    def test_holds(self):
        items = {"x": True, "y": False}
        self.assertTrue(cs.holds(items, "x"))
        self.assertTrue(cs.holds(items, "!y"))
        self.assertFalse(cs.holds(items, "!z"), "unknown is neither on nor off")


class Value(unittest.TestCase):
    S = [{"id": "eat", "action": "eat", "context": [], "result": {"fed": "on"}}]

    def test_earned_counts_repeat(self):
        m = mind({"fed": "on"}, {"fed": 5}, self.S)
        self.assertEqual(m.predicted_value("eat"), 5)

    def test_change_scores_the_delta(self):
        m = mind({"fed": "on"}, {"fed": 5}, self.S, score="change")
        self.assertEqual(m.predicted_value("eat"), 0, "+50 hunger is worth nothing to a full Sim")
        m.items["fed"] = False
        self.assertEqual(m.predicted_value("eat"), 5)

    def test_unknown_result_is_worth_nothing(self):
        m = mind({}, {"fed": 5}, [{"id": "e", "action": "eat", "context": [], "result": {"fed": "on|off"}}])
        self.assertEqual(m.predicted_value("eat"), 0)


class Learning(unittest.TestCase):
    def test_standing_conflict_is_not_new_pain(self):
        m = mind({"a": "on", "b": "on"}, {}, [{"id": "w", "action": "wave", "context": [], "result": {"waved": "on"}}],
                 contradictions=[("a", "b")])
        for t in (1, 2, 3):
            m.step({"t": t, "offers": ["wave"]})
        self.assertFalse(any(c.id == "learned-wave" for c in m.censors))
        self.assertEqual([h for _, h in m.trials["wave"]], [False, False, False])

    def test_new_pain_mints_a_censor_from_the_schema_context(self):
        m = mind({"letter": "off", "noise": "on"}, {"bad-news": -3},
                 [{"id": "r", "action": "read", "context": ["letter"], "result": {"bad-news": "on"}}])
        for t in (1, 3):
            m.step({"t": t, "set": {"letter": "on", "bad-news": "off"}, "offers": ["read"]})
        c = next(c for c in m.censors if c.id == "learned-read")
        self.assertEqual(c.context, ["letter"], "an item that never varied carries no evidence")

    def test_joke_censor_is_not_mistaken_for_the_learned_one(self):
        lesson = {"id": "not-this-one", "action": "read", "context": ["letter", "tooth"]}
        m = mind({"letter": "off", "tooth": "on"}, {"bad-news": -3},
                 [{"id": "r", "action": "read", "context": ["letter"], "result": {"bad-news": "on"}}])
        m.step({"t": 0, "joke": {"lesson": lesson}})
        for t in (1, 3, 5):
            m.step({"t": t, "set": {"letter": "on", "bad-news": "off"}, "offers": ["read", "skip"]})
        joke = next(c for c in m.censors if c.id == "not-this-one")
        self.assertEqual(joke.context, ["letter", "tooth"])

    def test_losses_hurt_is_opt_in(self):
        S = [{"id": "q", "action": "quit", "context": [], "result": {"job": "off"}}]
        for flag, expect in ((False, False), (True, True)):
            m = mind({"job": "on"}, {"job": 4}, S, losses_hurt=flag)
            m.step({"t": 1, "offers": ["quit"]})
            self.assertEqual(m.trials["quit"][-1][1], expect)

    def test_missed_joke_still_teaches(self):
        m = mind({"x": "on"})
        m.step({"t": 1, "joke": {"exposes": "nobody", "lesson": {"id": "l", "action": "a", "context": ["x"]}}})
        self.assertTrue(any(c.id == "l" for c in m.censors))


class Planning(unittest.TestCase):
    S = [{"id": "r", "action": "read", "context": ["letter"], "result": {"informed": "on"}},
         {"id": "b", "action": "book", "context": ["informed"], "result": {"appointment": "on"}, "reliability": 0.9}]

    def test_chains_schemas(self):
        m = mind({"letter": "on"}, {}, self.S)
        self.assertEqual(m.plan(["appointment"])["steps"], ["read", "book"])

    def test_censor_hides_the_plan_from_the_agent_only(self):
        c = {"id": "dont-read", "kind": "precursor", "action": "read", "context": ["letter"]}
        m = mind({"letter": "on"}, {}, self.S, [c])
        self.assertIsNone(m.plan(["appointment"], censored=True)["steps"])
        self.assertEqual(m.plan(["appointment"], censored=False)["steps"], ["read", "book"])
        self.assertEqual(cs.walk(m, ["read", "book"])[0]["vetoed_by"], "dont-read")

    def test_reliability_is_a_cost(self):
        S = [{"id": "g", "action": "gamble", "context": [], "result": {"rich": "on"}, "reliability": 0.1},
             {"id": "w", "action": "work", "context": [], "result": {"paid": "on"}},
             {"id": "s", "action": "save", "context": ["paid"], "result": {"rich": "on"}}]
        self.assertEqual(mind({}, {}, S).plan(["rich"])["steps"], ["work", "save"])

    def test_already_true(self):
        self.assertEqual(mind({"x": "on"}).plan(["x"])["steps"], [])


class Runs(unittest.TestCase):
    SPEC = {"agent": {"name": "t", "items": {"x": "on"}, "values": {"a": 1, "b": 1}},
            "schemas": [{"id": "a", "action": "a", "context": [], "result": {"a": "on"}},
                        {"id": "b", "action": "b", "context": [], "result": {"b": "on"}}],
            "events": [{"t": 1, "offers": ["a", "b"], "observed": "b"}],
            "runs": [{"name": "r", "agent": {"values": {"b": 2}}}]}

    def test_perturbation_reaches_run_overrides(self):
        (_, m), = cs.run(self.SPEC, factors={"a": 1.0, "b": 0.25})
        self.assertEqual(m.values["b"], 0.5)
        self.assertEqual(m.choices[-1][1], "a")

    def test_seed_is_deterministic(self):
        self.assertEqual(cs.sweep(self.SPEC, 200, seed=7)["runs"], cs.sweep(self.SPEC, 200, seed=7)["runs"])

    def test_weight_names_put_shared_first(self):
        self.assertEqual(cs.weight_names(self.SPEC), ["a", "b"])

    def test_ablate_covers_run_censors(self):
        spec = {**self.SPEC, "runs": [{"name": "r", "add_censors": [
            {"id": "no-a", "kind": "precursor", "action": "a", "context": []}]}]}
        rows = cs.ablate(spec)
        self.assertEqual([x["censor"] for x in rows], ["no-a"])


class Lint(unittest.TestCase):
    def test_template_words_in_a_run_censor(self):
        spec = {"real": ["self"], "agent": {"name": "p", "items": {}},
                "events": [{"t": 1, "offers": ["a"]}],
                "schemas": [{"id": "a", "action": "a", "context": [], "result": {}}],
                "runs": [{"name": "r", "add_censors": [
                    {"id": "c", "kind": "precursor", "action": "a", "context": [], "cover": "template words"}]}]}
        self.assertEqual(cs.lint_spec(spec, cs.Bus())["errors"], 1)

    def test_bad_score_mode(self):
        self.assertEqual(cs.lint_spec({"agent": {"name": "p", "score": "vibes"}}, cs.Bus())["errors"], 1)


class Examples(unittest.TestCase):
    def test_dentist(self):
        spec = cs.load([os.path.join(EXAMPLES, "dentist-letter.yml")])
        self.assertTrue(all(x["ok"] for x in cs.test_spec(spec)))
        (_, m), = cs.run(spec, "avoidance")
        self.assertEqual(next(c for c in m.censors if c.id == "learned-read-letter").context, ["letter-from-dentist"])
        self.assertIsNone(m.plan(["appointment"])["steps"])
        self.assertEqual(m.plan(["appointment"], censored=False)["steps"], ["read-letter", "book-appointment"])

    def test_cli_events_are_json_lines(self):
        err = io.StringIO()
        old = sys.stderr
        sys.stderr = err
        try:
            sys.stdout, out = io.StringIO(), sys.stdout
            try:
                code = cs.main(["plan", os.path.join(EXAMPLES, "dentist-letter.yml"),
                                "--run", "avoidance", "--goal", "appointment"])
            finally:
                sys.stdout = out
        finally:
            sys.stderr = old
        self.assertEqual(code, 0)
        kinds = [json.loads(line)["kind"] for line in err.getvalue().splitlines()]
        self.assertIn("plan", kinds)


class SchemaLearning(unittest.TestCase):
    def setUp(self):
        self.spec = cs.load([os.path.join(EXAMPLES, "learning-toddler.yml")])

    def test_learns_from_bare_schemas_in_the_run(self):
        (_, m), = cs.run(self.spec, "learning")
        self.assertEqual(cs.score(m), (7, 7))
        learned = {s.id: s for s in m.schemas}
        self.assertEqual(learned["learned-cry"].result, {"scolded": "on"})
        self.assertEqual(learned["learned-ask"].result, {"snack": "on"})
        self.assertEqual(learned["learned-ask-when-parent-home"].context, ["parent-home"])

    def test_without_learning_every_choice_ties(self):
        (_, m), = cs.run(self.spec, "knows-nothing")
        self.assertEqual(cs.score(m), (2, 7))

    def test_a_reset_is_not_a_result(self):
        (_, m), = cs.run(self.spec, "learning")
        self.assertFalse(any(v == "off" for s in m.schemas for v in s.result.values()))

    def test_learn_keeps_only_what_fits(self):
        r, rows, kept, cur = cs.learn(self.spec, "knows-nothing")
        self.assertEqual([p["id"] for p in kept], ["learned-ask"])
        self.assertEqual(cs.run_fit(cur, r), 5)
        self.assertTrue(all(x["verdict"] != "kept" for x in rows if x["id"] != "learned-ask"))


class Duet(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(EXAMPLES, "name-on-the-clinic.duet.yml")
        self.spec = cs.load([self.path])

    def seats(self, **runs):
        spec = cs.merge(self.spec, {"seats": {s: {"run": r} for s, r in runs.items()}})
        return spec, cs.duet_seats(spec, EXAMPLES)

    def test_both_seats_cooperate(self):
        spec, seats = self.seats()
        self.assertEqual(cs.test_duet(spec, seats), [])

    def test_one_move_is_the_others_news(self):
        spec, seats = self.seats(mayor="indifferent")
        log, world, _ = cs.duet(spec, seats)
        self.assertEqual([x.get("action") for x in log if "action" in x], ["offer-credit", "attack-offer"])
        self.assertTrue(all("skipped" in x for x in log[2:]))
        self.assertIsNot(world.get("clinic"), cs.ON)

    def test_spread_is_deterministic(self):
        spec, seats = self.seats()
        self.assertEqual(cs.duet_spread(spec, seats, 50, seed=3), cs.duet_spread(spec, seats, 50, seed=3))


class Bounds(unittest.TestCase):
    def test_simplex_small(self):
        # max x + y, x + 2y <= 4, 3x + y <= 6  ->  x = 1.6, y = 1.2
        val, x = cs.simplex_max([1, 1], [[1, 2], [3, 1]], [4, 6])
        self.assertAlmostEqual(val, 2.8)
        self.assertAlmostEqual(x[0], 1.6)
        self.assertIsNone(cs.simplex_max([1], [[1], [-1]], [1, -2]))   # x <= 1 and x >= 2

    def test_simplex_matches_scipy(self):
        try:
            from scipy.optimize import linprog
        except ImportError:
            self.skipTest("scipy not installed")
        import random
        rng = random.Random(7)
        for _ in range(200):
            n, m = rng.randint(1, 5), rng.randint(1, 8)
            A = [[rng.uniform(-3, 3) for _ in range(n)] for _ in range(m)] + [[1.0 if j == i else 0.0 for j in range(n)] for i in range(n)]
            b = [rng.uniform(-2, 5) for _ in range(m)] + [10.0] * n
            c = [rng.uniform(-2, 2) for _ in range(n)]
            ours = cs.simplex_max(c, A, b)
            ref = linprog([-x for x in c], A_ub=A, b_ub=b, bounds=[(0, None)] * n, method="highs")
            self.assertEqual(ours is None, ref.status == 2)
            if ours:
                self.assertAlmostEqual(ours[0], -ref.fun, places=6)

    def test_toddler_only_needs_scolding_to_hurt(self):
        out = cs.bounds(cs.load([os.path.join(EXAMPLES, "learning-toddler.yml")]), "learning")
        (w,) = out["weights"]
        self.assertEqual((w["weight"], w["verdict"]), ("scolded", "must be negative"))
        self.assertEqual(out["now_misses"], [])

    def test_mayor_applause_floor_and_conflict(self):
        out = cs.bounds(cs.load([os.path.join(EXAMPLES, "mayor-thorne.yml")]), "vain")
        w = {x["weight"]: x for x in out["weights"]}
        self.assertAlmostEqual(w["applause"]["min"], 2.5, places=2)
        self.assertEqual(w["deal"]["verdict"], "the record doesn't constrain it")
        self.assertEqual([(u["t"], u["conflicts_with"]) for u in out["unfit"]], [(3, [2])])

    def test_hidden_state_shows_as_contradiction(self):
        out = cs.bounds(cs.load([os.path.join(EXAMPLES, "quiet-secretary.yml")]), "as-seen")
        self.assertEqual([u["t"] for u in out["unfit"]], [5, 6, 7, 8])
        self.assertEqual(out["unfit"][0]["conflicts_with"], [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
