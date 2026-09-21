"""weighted_pick.pyの入力処理・重み計算・CLI動作を検査する。"""

import io
import json
import sys

import pytest


@pytest.fixture
def weighted_module(load_script):
    return load_script("generate-quiz", "weighted_pick.py")


class TestWeightedPickFunctions:
    def test_load_input_from_file(self, weighted_module, tmp_path):
        source = tmp_path / "candidates.json"
        source.write_text('{"candidates": [{"key": "a"}]}', encoding="utf-8")
        assert weighted_module.load_input(source) == {"candidates": [{"key": "a"}]}

    def test_load_input_from_stdin(self, weighted_module, monkeypatch):
        monkeypatch.setattr(sys, "stdin", io.StringIO('[{"key": "a"}]'))
        assert weighted_module.load_input(None) == [{"key": "a"}]

    @pytest.mark.parametrize("payload", [{"candidates": "bad"}, [{"label": "欠落"}]])
    def test_candidates_of_rejects_invalid_payload(self, weighted_module, payload):
        with pytest.raises(SystemExit) as error:
            weighted_module.candidates_of(payload)
        assert error.value.code == weighted_module.EXIT_USAGE

    def test_candidates_of_accepts_object_and_array(self, weighted_module):
        candidates = [{"key": "a"}]
        assert weighted_module.candidates_of({"candidates": candidates}) == candidates
        assert weighted_module.candidates_of(candidates) == candidates

    def test_weights_for_applies_history_to_each_candidate(self, weighted_module):
        candidates = [
            {"key": "a", "base_weight": 3, "history_distances": [1, 6]},
            {"key": "b", "base_weight": 2},
        ]
        base, probabilities, adjusted, total = weighted_module.weights_for(candidates)
        assert base == [3, 2]
        assert probabilities == pytest.approx([0.6, 0.4])
        assert adjusted == pytest.approx([1.8, 2])
        assert total == pytest.approx(3.8)

    @pytest.mark.parametrize(
        "candidates",
        [
            [{"key": "a", "base_weight": 0}],
            [{"key": "a", "base_weight": -1}],
            [{"key": "a", "base_weight": "不正"}],
            [{"key": "a", "base_weight": 1, "history_distances": [0]}],
        ],
    )
    def test_weights_for_rejects_invalid_values(self, weighted_module, candidates):
        with pytest.raises(SystemExit) as error:
            weighted_module.weights_for(candidates)
        assert error.value.code == weighted_module.EXIT_USAGE


class TestWeightedPick:
    """履歴補正付きの重み付き乱択。既定の出力にweightや抽選の内訳が混じらないことも見る。"""

    @staticmethod
    def payload(*cands):
        return json.dumps({"candidates": list(cands)})

    def test_single_candidate_is_chosen(self, run_script):
        p = self.payload({"key": "subject::7", "label": "芸術", "base_weight": 1.0})
        r = run_script("weighted_pick.py", stdin=p)
        assert r.returncode == 0
        assert r.stdout.strip() == "CHOSEN\tsubject::7\t芸術"

    def test_zero_weight_candidate_is_never_chosen(self, run_script):
        # weightが0なのは不成立の候補なので、抽選されてはならない
        p = self.payload(
            {"key": "live", "base_weight": 1.0}, {"key": "dead", "base_weight": 0.0}
        )
        for _ in range(30):
            r = run_script("weighted_pick.py", stdin=p)
            assert r.returncode == 0
            assert "CHOSEN\tlive" in r.stdout

    def test_internals_are_not_printed_by_default(self, run_script):
        p = self.payload(
            {"key": "a", "base_weight": 2.0, "history_distances": [1]},
            {"key": "b", "base_weight": 1.0},
        )
        r = run_script("weighted_pick.py", stdin=p)
        assert len(r.stdout.strip().splitlines()) == 1
        for marker in ("base=", "p=", "adj=", "final_p="):
            assert marker not in r.stdout
        assert r.stderr == ""

    def test_verbose_breakdown_goes_to_stderr_only(self, run_script):
        p = self.payload(
            {"key": "a", "base_weight": 2.0, "history_distances": [1]},
            {"key": "b", "base_weight": 1.0},
        )
        r = run_script("weighted_pick.py", "--verbose", stdin=p)
        assert r.returncode == 0
        assert "final_p=" in r.stderr
        assert "final_p=" not in r.stdout

    def test_history_correction_matches_spec_formula(self, run_script):
        # w_j = b_j * Π min(1, d * p_j) が --verbose の内訳と一致するかを見る
        cands = [
            {"key": "a", "base_weight": 3.0, "history_distances": [1, 6]},
            {"key": "b", "base_weight": 2.0},
            {"key": "c", "base_weight": 2.5},
        ]
        base = [3.0, 2.0, 2.5]
        total = sum(base)
        expected = []
        for c, b in zip(cands, base, strict=True):
            w = b
            for d in c.get("history_distances", []):
                w *= min(1.0, d * (b / total))
            expected.append(w)
        exp_final = [w / sum(expected) for w in expected]

        r = run_script(
            "weighted_pick.py",
            "--verbose",
            stdin=json.dumps({"candidates": cands}),
        )
        assert r.returncode == 0
        got = {}
        for line in r.stderr.splitlines():
            if "final_p=" not in line:
                continue
            fields = line.lstrip("# ").split("\t")
            got[fields[0]] = float(fields[-1].split("=")[1])
        for c, exp in zip(cands, exp_final, strict=True):
            assert got[c["key"]] == pytest.approx(exp, abs=5e-5, rel=0)

    def test_exclude_removes_candidate(self, run_script):
        p = self.payload(
            {"key": "a", "base_weight": 1.0}, {"key": "b", "base_weight": 1.0}
        )
        for _ in range(20):
            r = run_script("weighted_pick.py", "--exclude", "a", stdin=p)
            assert r.returncode == 0
            assert "CHOSEN\tb" in r.stdout

    def test_exclude_all_exits_2(self, run_script):
        p = self.payload({"key": "a", "base_weight": 1.0})
        r = run_script("weighted_pick.py", "--exclude", "a", stdin=p)
        assert r.returncode == 2
        assert r.stdout == ""

    def test_all_weights_zero_exits_2(self, run_script):
        p = self.payload(
            {"key": "a", "base_weight": 0.0}, {"key": "b", "base_weight": 0.0}
        )
        assert run_script("weighted_pick.py", stdin=p).returncode == 2

    def test_bare_array_input_is_accepted(self, run_script):
        p = json.dumps([{"key": "a", "base_weight": 1.0}])
        assert run_script("weighted_pick.py", stdin=p).returncode == 0

    def test_invalid_json_exits_2(self, run_script):
        assert run_script("weighted_pick.py", stdin="{not json").returncode == 2

    def test_empty_stdin_exits_2(self, run_script):
        assert run_script("weighted_pick.py", stdin="").returncode == 2

    def test_candidate_without_key_exits_2(self, run_script):
        assert (
            run_script(
                "weighted_pick.py",
                stdin=json.dumps({"candidates": [{"base_weight": 1.0}]}),
            ).returncode
            == 2
        )

    def test_zero_history_distance_exits_2(self, run_script):
        # 直前がd=1なので、0以下の距離は履歴の読み違いであり、受け付けない
        p = self.payload({"key": "a", "base_weight": 1.0, "history_distances": [0]})
        r = run_script("weighted_pick.py", stdin=p)
        assert r.returncode == 2
        assert "history_distances" in r.stderr

    def test_negative_base_weight_exits_2(self, run_script):
        p = self.payload(
            {"key": "a", "base_weight": -1.0}, {"key": "b", "base_weight": 2.0}
        )
        assert run_script("weighted_pick.py", stdin=p).returncode == 2

    def test_missing_json_file_exits_2(self, run_script, tmp_path):
        assert (
            run_script(
                "weighted_pick.py", "--json", tmp_path / "no-such.json"
            ).returncode
            == 2
        )
