#!/usr/bin/env python3
"""スキルに同梱したスクリプトの終了コードと出力を固定する回帰テスト。

ファセットの参照、重み付き乱択、文字数の判定はスクリプトが担っている。ここで、facet_node.py がカタログにないノードを返す、weighted_pick.py が候補のない集合やweightが0の候補から選ぶ、length_check.py が満たしていない字数の制約を通す、といった壊れ方をすると、作問の工程は最後まで走って成功したように見えるのに、実際には何も確かめていない状態になる。そうした壊れ方に気づけるよう、スクリプトを外から見たときの振る舞いをここで固定しておく。

終了コードは、0が正常、1が該当なしまたは要改稿、2が入力の不備を表す。メッセージの文言は変わりうるので、出力の検査には、NODE_KEY、オプション名、タブ区切りのフィールド名のような、文言に依存しない目印を使う。

tests/ は開発用で、スキルの配布物には含まない。スキルとして配る・同期するのは、作問時に実際に動く SKILL.md、references/、scripts/ だけである。

実行方法: python3 tests/test_cli_contracts.py
"""

import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = ("generate-quiz",)


def run(skill, script, *args, stdin=None):
    return subprocess.run(
        [sys.executable, str(REPO / "skills" / skill / "scripts" / script),
         *[str(a) for a in args]],
        input=stdin, capture_output=True, text=True,
    )


class SkillCase(unittest.TestCase):
    def for_each_skill(self):
        for skill in SKILLS:
            with self.subTest(skill=skill):
                yield skill


class FacetNodeTest(SkillCase):
    """ファセットカタログの参照。カタログにないノードを返さないことを主に見る。"""

    def test_existing_node_exits_0_with_direct_children(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "subject::1")
            self.assertEqual(r.returncode, 0)
            self.assertIn("NODE_KEY: `subject::1`", r.stdout)
            self.assertIn("DIRECT_CHILDREN", r.stdout)

    def test_block_is_single_and_terminated(self):
        # 隣のノードを巻き込まず、1ブロックだけを返す
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "subject::1")
            self.assertEqual(r.stdout.count("## FACET_NODE"), 1)
            self.assertIn("END_FACET_NODE", r.stdout)

    def test_root_block_from_index(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "time::ROOT")
            self.assertEqual(r.returncode, 0)
            self.assertIn("FACET_ROOT `time::ROOT`", r.stdout)

    def test_key_with_quotes_and_parens(self):
        # time::"0/2" や place::(1/9) のような記号を含むキーも、そのまま指定できる
        for skill in self.for_each_skill():
            for key in ('time::"0/2"', "place::(1/9)"):
                self.assertEqual(run(skill, "facet_node.py", key).returncode, 0)

    def test_unknown_node_exits_1(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "subject::99999")
            self.assertEqual(r.returncode, 1)
            self.assertIn("subject::99999", r.stderr)
            self.assertEqual(r.stdout, "")

    def test_children_only_lists_children(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "--children", "subject::1")
            self.assertEqual(r.returncode, 0)
            self.assertNotIn("NODE_KEY:", r.stdout)
            lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
            self.assertTrue(lines)
            self.assertTrue(all(ln.startswith("- `") for ln in lines))

    def test_children_of_leaf_reports_none(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "--children", "subject::101")
            self.assertEqual(r.returncode, 0)
            self.assertEqual(r.stdout.strip(), "なし")

    def test_grep_hit_exits_0(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "--grep", "音楽")
            self.assertEqual(r.returncode, 0)
            self.assertIn("subject::78", r.stdout)

    def test_grep_limit_is_respected(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "--grep", "音楽", "--limit", "2")
            self.assertEqual(r.returncode, 0)
            self.assertEqual(len(r.stdout.strip().splitlines()), 2)

    def test_grep_miss_exits_1(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py", "--grep", "存在しないラベル名XYZ")
            self.assertEqual(r.returncode, 1)
            self.assertEqual(r.stdout, "")

    def test_no_argument_exits_2(self):
        for skill in self.for_each_skill():
            r = run(skill, "facet_node.py")
            self.assertEqual(r.returncode, 2)
            self.assertIn("--grep", r.stderr)

    def test_empty_grep_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "facet_node.py", "--grep", "  ").returncode, 2)

    def test_zero_limit_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(
                run(skill, "facet_node.py", "--grep", "音楽", "--limit", "0").returncode, 2)


class WeightedPickTest(SkillCase):
    """履歴補正付きの重み付き乱択。既定の出力にweightや抽選の内訳が混じらないことも見る。"""

    @staticmethod
    def payload(*cands):
        return json.dumps({"candidates": list(cands)})

    def test_single_candidate_is_chosen(self):
        p = self.payload({"key": "subject::7", "label": "芸術", "base_weight": 1.0})
        for skill in self.for_each_skill():
            r = run(skill, "weighted_pick.py", stdin=p)
            self.assertEqual(r.returncode, 0)
            self.assertEqual(r.stdout.strip(), "CHOSEN\tsubject::7\t芸術")

    def test_zero_weight_candidate_is_never_chosen(self):
        # weightが0なのは不成立の候補なので、抽選されてはならない
        p = self.payload({"key": "live", "base_weight": 1.0},
                         {"key": "dead", "base_weight": 0.0})
        for skill in self.for_each_skill():
            for _ in range(30):
                r = run(skill, "weighted_pick.py", stdin=p)
                self.assertEqual(r.returncode, 0)
                self.assertIn("CHOSEN\tlive", r.stdout)

    def test_internals_are_not_printed_by_default(self):
        p = self.payload({"key": "a", "base_weight": 2.0, "history_distances": [1]},
                         {"key": "b", "base_weight": 1.0})
        for skill in self.for_each_skill():
            r = run(skill, "weighted_pick.py", stdin=p)
            self.assertEqual(len(r.stdout.strip().splitlines()), 1)
            for marker in ("base=", "p=", "adj=", "final_p="):
                self.assertNotIn(marker, r.stdout)
            self.assertEqual(r.stderr, "")

    def test_verbose_breakdown_goes_to_stderr_only(self):
        p = self.payload({"key": "a", "base_weight": 2.0, "history_distances": [1]},
                         {"key": "b", "base_weight": 1.0})
        for skill in self.for_each_skill():
            r = run(skill, "weighted_pick.py", "--verbose", stdin=p)
            self.assertEqual(r.returncode, 0)
            self.assertIn("final_p=", r.stderr)
            self.assertNotIn("final_p=", r.stdout)

    def test_history_correction_matches_spec_formula(self):
        # w_j = b_j * Π min(1, d * p_j) が --verbose の内訳と一致するかを見る
        cands = [{"key": "a", "base_weight": 3.0, "history_distances": [1, 6]},
                 {"key": "b", "base_weight": 2.0},
                 {"key": "c", "base_weight": 2.5}]
        base = [3.0, 2.0, 2.5]
        total = sum(base)
        expected = []
        for c, b in zip(cands, base):
            w = b
            for d in c.get("history_distances", []):
                w *= min(1.0, d * (b / total))
            expected.append(w)
        exp_final = [w / sum(expected) for w in expected]

        for skill in self.for_each_skill():
            r = run(skill, "weighted_pick.py", "--verbose",
                    stdin=json.dumps({"candidates": cands}))
            self.assertEqual(r.returncode, 0)
            got = {}
            for line in r.stderr.splitlines():
                if "final_p=" not in line:
                    continue
                fields = line.lstrip("# ").split("\t")
                got[fields[0]] = float(fields[-1].split("=")[1])
            for c, exp in zip(cands, exp_final):
                self.assertAlmostEqual(got[c["key"]], exp, places=4)

    def test_exclude_removes_candidate(self):
        p = self.payload({"key": "a", "base_weight": 1.0},
                         {"key": "b", "base_weight": 1.0})
        for skill in self.for_each_skill():
            for _ in range(20):
                r = run(skill, "weighted_pick.py", "--exclude", "a", stdin=p)
                self.assertEqual(r.returncode, 0)
                self.assertIn("CHOSEN\tb", r.stdout)

    def test_exclude_all_exits_2(self):
        p = self.payload({"key": "a", "base_weight": 1.0})
        for skill in self.for_each_skill():
            r = run(skill, "weighted_pick.py", "--exclude", "a", stdin=p)
            self.assertEqual(r.returncode, 2)
            self.assertEqual(r.stdout, "")

    def test_all_weights_zero_exits_2(self):
        p = self.payload({"key": "a", "base_weight": 0.0},
                         {"key": "b", "base_weight": 0.0})
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "weighted_pick.py", stdin=p).returncode, 2)

    def test_bare_array_input_is_accepted(self):
        p = json.dumps([{"key": "a", "base_weight": 1.0}])
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "weighted_pick.py", stdin=p).returncode, 0)

    def test_invalid_json_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "weighted_pick.py", stdin="{not json").returncode, 2)

    def test_empty_stdin_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "weighted_pick.py", stdin="").returncode, 2)

    def test_candidate_without_key_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(
                run(skill, "weighted_pick.py",
                    stdin=json.dumps({"candidates": [{"base_weight": 1.0}]})).returncode, 2)

    def test_zero_history_distance_exits_2(self):
        # 直前がd=1なので、0以下の距離は履歴の読み違いであり、受け付けない
        p = self.payload({"key": "a", "base_weight": 1.0, "history_distances": [0]})
        for skill in self.for_each_skill():
            r = run(skill, "weighted_pick.py", stdin=p)
            self.assertEqual(r.returncode, 2)
            self.assertIn("history_distances", r.stderr)

    def test_negative_base_weight_exits_2(self):
        p = self.payload({"key": "a", "base_weight": -1.0}, {"key": "b", "base_weight": 2.0})
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "weighted_pick.py", stdin=p).returncode, 2)

    def test_missing_json_file_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(
                run(skill, "weighted_pick.py", "--json", REPO / "no-such.json").returncode, 2)


class LengthCheckTest(SkillCase):
    """文字数の計測と採否の判定。満たしていないハード制約を通さないことを主に見る。"""

    def test_prefix_and_newlines_are_excluded(self):
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", "問題：" + "あ" * 80 + "\n")
            self.assertIn("LENGTH\t80", r.stdout)

    def test_ascii_colon_prefix_is_also_excluded(self):
        for skill in self.for_each_skill():
            self.assertIn("LENGTH\t80",
                          run(skill, "length_check.py", "問題:" + "あ" * 80).stdout)

    def test_nfc_normalization_before_counting(self):
        # 濁点を合成する場合、NFDの2コードポイントを1文字として数える
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", "が" * 10)
            self.assertIn("LENGTH\t10", r.stdout)

    def test_mode_length_always_accepted(self):
        # A(80)が1.0なので、既定の分布では常に採用される
        for skill in self.for_each_skill():
            for _ in range(20):
                r = run(skill, "length_check.py", "あ" * 80)
                self.assertEqual(r.returncode, 0)
                self.assertIn("VERDICT\tACCEPT", r.stdout)
                self.assertIn("ACCEPTANCE\t1.0000", r.stdout)

    def test_acceptance_curve_matches_spec(self):
        # sigma=0.23、mu=ln(80)+sigma^2 の対数正規分布で A(L)=f(L)/f(80) となる
        sigma, mode = 0.23, 80.0
        mu = math.log(mode) + sigma ** 2

        def density(x):
            return math.exp(-((math.log(x) - mu) ** 2) / (2 * sigma ** 2)) / x

        for skill in self.for_each_skill():
            for length in (50, 60, 100, 130):
                r = run(skill, "length_check.py", "あ" * length)
                got = float(
                    [ln for ln in r.stdout.splitlines()
                     if ln.startswith("ACCEPTANCE")][0].split("\t")[1])
                self.assertAlmostEqual(got, density(length) / density(mode), places=4)

    def test_target_shifts_the_mode(self):
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", "--target", "100", "あ" * 100)
            self.assertEqual(r.returncode, 0)
            self.assertIn("ACCEPTANCE\t1.0000", r.stdout)
            self.assertIn("MODE\tsoft", r.stdout)

    def test_hard_max_violation_exits_1(self):
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", "--max", "60", "あ" * 72)
            self.assertEqual(r.returncode, 1)
            self.assertIn("MODE\thard", r.stdout)
            self.assertIn("VERDICT\tVIOLATION", r.stdout)

    def test_hard_max_satisfied_exits_0(self):
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", "--max", "60", "あ" * 58)
            self.assertEqual(r.returncode, 0)
            self.assertIn("VERDICT\tOK", r.stdout)

    def test_hard_constraint_never_draws_randomly(self):
        # ハード制約のときは確率的な抽選を挟まないので、境界ちょうどでも結果が揺れない
        for skill in self.for_each_skill():
            for _ in range(20):
                r = run(skill, "length_check.py", "--max", "60", "あ" * 60)
                self.assertEqual(r.returncode, 0)
                self.assertNotIn("ACCEPTANCE", r.stdout)

    def test_hard_min_and_exact(self):
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "length_check.py", "--min", "70", "あ" * 60).returncode, 1)
            self.assertEqual(run(skill, "length_check.py", "--min", "70", "あ" * 70).returncode, 0)
            self.assertEqual(run(skill, "length_check.py", "--exact", "42", "あ" * 41).returncode, 1)
            self.assertEqual(run(skill, "length_check.py", "--exact", "42", "あ" * 42).returncode, 0)

    def test_range_reports_both_bounds(self):
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", "--min", "70", "--max", "90", "あ" * 100)
            self.assertEqual(r.returncode, 1)
            self.assertIn("90", r.stdout)

    def test_inverted_range_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(
                run(skill, "length_check.py", "--min", "90", "--max", "70", "あ" * 80).returncode, 2)

    def test_stdin_input(self):
        for skill in self.for_each_skill():
            r = run(skill, "length_check.py", stdin="問題：" + "あ" * 80)
            self.assertEqual(r.returncode, 0)
            self.assertIn("LENGTH\t80", r.stdout)

    def test_file_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "draft.txt"
            p.write_text("問題：" + "あ" * 80 + "\n", encoding="utf-8")
            for skill in self.for_each_skill():
                r = run(skill, "length_check.py", "--file", p)
                self.assertEqual(r.returncode, 0)
                self.assertIn("LENGTH\t80", r.stdout)

    def test_empty_text_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(run(skill, "length_check.py", "問題：").returncode, 2)

    def test_missing_file_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(
                run(skill, "length_check.py", "--file", REPO / "no-such.txt").returncode, 2)

    def test_non_positive_target_exits_2(self):
        for skill in self.for_each_skill():
            self.assertEqual(
                run(skill, "length_check.py", "--target", "0", "あ" * 80).returncode, 2)


class SkillLayoutTest(SkillCase):
    """配布物の構成（SKILL.md、references/、scripts/）に欠けがないこと。"""

    def test_skill_md_frontmatter(self):
        for skill in self.for_each_skill():
            text = (REPO / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"))
            head = text.split("---", 2)[1]
            self.assertIn(f"name: {skill}", head)
            self.assertIn("description:", head)

    def test_referenced_files_exist(self):
        for skill in self.for_each_skill():
            root = REPO / "skills" / skill
            for name in ("quiz_generation_spec.md", "selection_and_history_spec.md",
                         "verification_and_judging_spec.md", "facet_index.md"):
                self.assertTrue((root / "references" / name).is_file(), name)
            for name in ("facet_node.py", "weighted_pick.py", "length_check.py"):
                self.assertTrue((root / "scripts" / name).is_file(), name)

    def test_facet_index_lists_existing_catalogs(self):
        for skill in self.for_each_skill():
            root = REPO / "skills" / skill / "references"
            index = (root / "facet_index.md").read_text(encoding="utf-8")
            for line in index.splitlines():
                if not line.startswith("- FILES:"):
                    continue
                for name in line.split(":", 1)[1].split(","):
                    name = name.strip().strip("`").split("`")[0]
                    if name.endswith(".md"):
                        self.assertTrue((root / name).is_file(), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
