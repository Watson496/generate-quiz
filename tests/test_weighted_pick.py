"""weighted_pick.pyの重み計算と、ファセット選択の記録からの抽選を検査する。"""

import json
import math

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st


@pytest.fixture
def weighted_module(load_script):
    return load_script("generate-quiz", "weighted_pick.py")


class TestWeightedPickFunctions:
    # 重み計算は各生成例の間で状態を変えない。
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        st.lists(
            st.tuples(
                st.floats(
                    min_value=0.01, max_value=100, allow_nan=False, allow_infinity=False
                ),
                st.lists(st.integers(min_value=1, max_value=20), max_size=3),
            ),
            min_size=1,
            max_size=6,
        )
    )
    def test_weights_for_preserves_nonnegative_finite_weights(
        self, weighted_module, weights_and_distances
    ):
        """有効な候補群で履歴補正後の重みと確率が計算式を満たすことを確認する。"""
        candidates = [
            {"key": str(index), "weight": weight, "history_distances": distances}
            for index, (weight, distances) in enumerate(weights_and_distances)
        ]
        base, probabilities, adjusted, total = weighted_module.weights_for(candidates)
        base_total = sum(base)
        expected = [
            weight
            * math.prod(
                min(1, distance * weight / base_total) for distance in distances
            )
            for weight, distances in weights_and_distances
        ]
        assert sum(probabilities) == pytest.approx(1)
        assert adjusted == pytest.approx(expected)
        assert total == pytest.approx(sum(adjusted))
        assert all(
            0 <= value <= original
            for value, original in zip(adjusted, base, strict=True)
        )

    def test_weights_for_applies_history_to_each_candidate(self, weighted_module):
        """履歴距離を持つ候補だけが所定の係数で減重されることを確認する。"""
        candidates = [
            {"key": "a", "weight": 3, "history_distances": [1, 6]},
            {"key": "b", "weight": 2},
        ]
        base, probabilities, adjusted, total = weighted_module.weights_for(candidates)
        assert base == [3, 2]
        assert probabilities == pytest.approx([0.6, 0.4])
        assert adjusted == pytest.approx([1.8, 2])
        assert total == pytest.approx(3.8)

    @pytest.mark.parametrize(
        "candidates",
        [
            [{"key": "a", "weight": 0}],
            [{"key": "a", "weight": -1}],
            [{"key": "a", "weight": "不正"}],
            [{"key": "a", "weight": 1, "history_distances": [0]}],
        ],
    )
    def test_weights_for_rejects_invalid_values(self, weighted_module, candidates):
        """不正な基礎重みと履歴距離を重み計算の前に拒否することを確認する。"""
        with pytest.raises(SystemExit) as error:
            weighted_module.weights_for(candidates)
        assert error.value.code == weighted_module.EXIT_USAGE

    @pytest.mark.parametrize(
        "value", ["nan", "inf", "-inf", float("nan"), float("inf")]
    )
    def test_weights_for_rejects_nonfinite_base(self, weighted_module, value):
        """NaNや無限大の基礎重みを重み計算の前に拒否する。"""
        with pytest.raises(SystemExit) as error:
            weighted_module.weights_for([{"key": "a", "weight": value}])
        assert error.value.code == weighted_module.EXIT_USAGE

    @pytest.mark.parametrize(
        "value", ["nan", "inf", "-inf", float("nan"), float("inf")]
    )
    def test_weights_for_rejects_nonfinite_distance(self, weighted_module, value):
        """NaNや無限大の履歴距離を重み計算の前に拒否する。"""
        with pytest.raises(SystemExit) as error:
            weighted_module.weights_for(
                [{"key": "a", "weight": 1, "history_distances": [value]}]
            )
        assert error.value.code == weighted_module.EXIT_USAGE

    def test_weights_for_rejects_nonfinite_sum(self, weighted_module):
        """個々の重みが有限でも合計が無限大になる候補群を拒否する。"""
        with pytest.raises(SystemExit) as error:
            weighted_module.weights_for(
                [{"key": "a", "weight": 1e308}, {"key": "b", "weight": 1e308}]
            )
        assert error.value.code == weighted_module.EXIT_USAGE

    def test_weights_for_rejects_unconvertible_integer(self, weighted_module):
        """浮動小数点数に変換できない巨大な整数を入力エラーとして扱う。"""
        with pytest.raises(SystemExit) as error:
            weighted_module.weights_for([{"key": "a", "weight": 10**400}])
        assert error.value.code == weighted_module.EXIT_USAGE


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
    return path


def set_weights(state, level, weights):
    """指定した階層の候補に、先頭から順にweightと履歴距離を置く。"""
    candidates = next(
        item for item in state["facet_weights"] if item["level_id"] == level
    )["candidates"]
    for candidate, (weight, distances) in zip(candidates, weights, strict=False):
        candidate["weight"] = weight
        if distances:
            candidate["history_distances"] = distances
    del candidates[len(weights) :]
    return [candidate["key"] for candidate in candidates]


class TestWeightedPick:
    """ファセット選択の記録から、検査に合格した階層だけを抽選する。"""

    def test_picks_candidate_of_level(self, run_script, tmp_path, facet_state):
        """指定した階層の候補から1件だけを選び、weightや抽選の内訳を出さない。"""
        state = write_json(tmp_path / "facet.json", facet_state)
        result = run_script("weighted_pick.py", state, "--level", "F2")
        assert result.returncode == 0, result.stderr
        chosen, key, _ = result.stdout.strip().split("\t")
        candidates = facet_state["facet_weights"][1]["candidates"]
        assert chosen == "CHOSEN"
        assert key in {candidate["key"] for candidate in candidates}
        assert result.stderr == ""

    def test_zero_weight_candidate_is_never_chosen(
        self, run_script, tmp_path, facet_state
    ):
        """weight 0の候補は抽選しない。"""
        keys = set_weights(facet_state, "F1", [(1.0, []), (0.0, []), (0.0, [])])
        state = write_json(tmp_path / "facet.json", facet_state)
        for _ in range(20):
            result = run_script("weighted_pick.py", state, "--level", "F1")
            assert result.stdout.split("\t")[1] == keys[0]

    def test_verbose_breakdown_matches_formula(self, run_script, tmp_path, facet_state):
        """内訳は標準エラー出力だけに出し、補正後の確率は履歴補正の計算式と一致する。"""
        weights = [(3.0, [1, 6]), (2.0, []), (2.5, [])]
        keys = set_weights(facet_state, "F1", weights)
        state = write_json(tmp_path / "facet.json", facet_state)
        result = run_script("weighted_pick.py", state, "--level", "F1", "--verbose")
        assert result.returncode == 0
        assert "final_p=" not in result.stdout
        total = sum(weight for weight, _ in weights)
        adjusted = [
            weight * math.prod(min(1, d * weight / total) for d in distances)
            for weight, distances in weights
        ]
        got = {
            line.lstrip("# ").split("\t")[0]: float(line.rsplit("=", 1)[1])
            for line in result.stderr.splitlines()
            if "final_p=" in line
        }
        for key, value in zip(keys, adjusted, strict=True):
            assert got[key] == pytest.approx(value / sum(adjusted), abs=5e-5)

    def test_joins_records_split_into_files(self, run_script, tmp_path, facet_state):
        """担当ごとのファイルに分かれた記録を、つないで確認する。"""
        reviews = {
            key: facet_state.pop(key)
            for key in (
                "facet_level_reviews",
                "facet_weight_reviews",
                "facet_distribution_reviews",
            )
        }
        facet_state["facet_weight_reviews"] = [
            {"level_id": "F2", "status": "failed", "reason": "三観点と合わない"}
        ]
        result = run_script(
            "weighted_pick.py",
            write_json(tmp_path / "facet.json", facet_state),
            write_json(tmp_path / "reviews.json", reviews),
            "--level",
            "F2",
        )
        assert result.returncode == 0, result.stderr

    @pytest.mark.parametrize(
        "key",
        ["facet_level_reviews", "facet_weight_reviews", "facet_distribution_reviews"],
    )
    def test_refuses_when_latest_review_failed(
        self, run_script, tmp_path, facet_state, key
    ):
        """階層の検査の最後の結果が不合格なら抽選しない。"""
        facet_state[key].append(
            {"level_id": "F2", "status": "failed", "reason": "基準に合わない"}
        )
        state = write_json(tmp_path / "facet.json", facet_state)
        result = run_script("weighted_pick.py", state, "--level", "F2")
        assert result.returncode == 2
        assert "F2の" in result.stderr
        assert result.stdout == ""

    def test_refuses_without_distribution_review(
        self, run_script, tmp_path, facet_state
    ):
        """weightの分布の検査がない階層は抽選しない。"""
        facet_state["facet_distribution_reviews"] = [
            item
            for item in facet_state["facet_distribution_reviews"]
            if item["level_id"] != "F2"
        ]
        state = write_json(tmp_path / "facet.json", facet_state)
        result = run_script("weighted_pick.py", state, "--level", "F2")
        assert result.returncode == 2
        assert "weightの分布の検査" in result.stderr

    def test_refuses_stopped_level(self, run_script, tmp_path, facet_state):
        """停止と判断した階層は抽選しない。"""
        state = write_json(tmp_path / "facet.json", facet_state)
        result = run_script("weighted_pick.py", state, "--level", "F3")
        assert result.returncode == 2
        assert "子へ進む判断" in result.stderr

    def test_subdivided_level_requires_subdivision_review(
        self, run_script, tmp_path, subdivided_facet_state
    ):
        """区分に分けた階層は、区分の分け方の検査に合格するまで抽選しない。"""
        level = next(
            item["id"]
            for item in subdivided_facet_state["facet_levels"]
            if item["node"] == "subject::338"
        )
        state = write_json(tmp_path / "facet.json", subdivided_facet_state)
        assert run_script("weighted_pick.py", state, "--level", level).returncode == 0
        subdivided_facet_state["facet_subdivision_reviews"] = [
            item
            for item in subdivided_facet_state["facet_subdivision_reviews"]
            if item["level_id"] != level
        ]
        state = write_json(tmp_path / "facet.json", subdivided_facet_state)
        result = run_script("weighted_pick.py", state, "--level", level)
        assert result.returncode == 2
        assert "区分の分け方の検査" in result.stderr

    def test_all_weights_zero_exits_2(self, run_script, tmp_path, facet_state):
        """全候補のweightが0なら抽選しない。"""
        set_weights(facet_state, "F1", [(0.0, []), (0.0, [])])
        state = write_json(tmp_path / "facet.json", facet_state)
        assert run_script("weighted_pick.py", state, "--level", "F1").returncode == 2

    def test_nonfinite_weight_exits_2_without_traceback(
        self, run_script, tmp_path, facet_state
    ):
        """不正なweightは例外の追跡表示を出さずに入力エラーとする。"""
        set_weights(facet_state, "F1", [("nan", [])])
        state = write_json(tmp_path / "facet.json", facet_state)
        result = run_script("weighted_pick.py", state, "--level", "F1")
        assert result.returncode == 2
        assert "Traceback" not in result.stderr

    def test_missing_file_exits_2(self, run_script, tmp_path):
        """存在しない記録のファイルは入力エラーとする。"""
        result = run_script(
            "weighted_pick.py", tmp_path / "no-such.json", "--level", "F1"
        )
        assert result.returncode == 2
