"""探索台帳と題材抽選スクリプトの動作を確認する。"""

import json


class TestTopicPickFunctions:
    """抽選用JSONと探索状態の対応を関数単位で確認する。"""

    def test_matching_quality_exclusion(self, load_script, selection_state):
        """品質棄却の記録と除外IDが一致すれば入力を認める。"""
        module = load_script("generate-quiz", "topic_pick.py")
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        payload = {
            "candidates": [
                {"key": "K1", "label": "候補1"},
                {"key": "K2", "label": "候補2"},
            ]
        }
        assert module.validate_payload(payload, selection_state, ["K1"]) is None

    def test_unrecorded_exclusion(self, load_script, selection_state):
        """品質棄却の記録がない候補の除外は認めない。"""
        module = load_script("generate-quiz", "topic_pick.py")
        payload = {
            "candidates": [
                {"key": "K1", "label": "候補1"},
                {"key": "K2", "label": "候補2"},
            ]
        }
        assert "品質棄却記録と一致しない" in module.validate_payload(
            payload, selection_state, ["K1"]
        )


class TestTopicPick:
    """探索台帳と候補抽選の接続を検査する。"""

    @staticmethod
    def pick(run_script, tmp_path, selection_state, candidates, *options):
        """台帳と抽選候補を題材抽選スクリプトへ渡す。"""
        state_path = tmp_path / "selection.json"
        state_path.write_text(
            json.dumps(selection_state, ensure_ascii=False), encoding="utf-8"
        )
        payload = {"candidates": candidates}
        return run_script(
            "topic_pick.py",
            state_path,
            *options,
            stdin=json.dumps(payload, ensure_ascii=False),
        )

    def test_pick_from_verified_candidates(self, run_script, tmp_path, selection_state):
        """検査済みの選択対象から題材を抽選する。"""
        candidates = [
            {"key": "K1", "label": "候補1", "base_weight": 1},
            {"key": "K2", "label": "候補2", "base_weight": 1},
        ]
        result = self.pick(run_script, tmp_path, selection_state, candidates)
        assert result.returncode == 0
        assert result.stdout.startswith("CHOSEN\tK")

    def test_pick_rejects_missing_eligible_candidate(
        self, run_script, tmp_path, selection_state
    ):
        """台帳の選択対象を抽選用JSONから落とせない。"""
        candidates = [{"key": "K1", "label": "候補1", "base_weight": 1}]
        result = self.pick(run_script, tmp_path, selection_state, candidates)
        assert result.returncode == 2
        assert "選択対象と一致しない" in result.stderr

    def test_pick_rejects_mismatched_label(self, run_script, tmp_path, selection_state):
        """候補IDが一致しても別の名称に差し替えて抽選できない。"""
        candidates = [
            {"key": "K1", "label": "別の対象", "base_weight": 1},
            {"key": "K2", "label": "候補2", "base_weight": 1},
        ]
        result = self.pick(run_script, tmp_path, selection_state, candidates)
        assert result.returncode == 2
        assert "候補名が探索状態と一致しない" in result.stderr

    def test_pick_excludes_failed_candidate(
        self, run_script, tmp_path, selection_state
    ):
        """不合格候補を除いて残りから再抽選する。"""
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        candidates = [
            {"key": "K1", "label": "候補1", "base_weight": 1},
            {"key": "K2", "label": "候補2", "base_weight": 1},
        ]
        result = self.pick(
            run_script, tmp_path, selection_state, candidates, "--exclude", "K1"
        )
        assert result.returncode == 0
        assert result.stdout.startswith("CHOSEN\tK2")

    def test_pick_requires_recorded_exclusion(
        self, run_script, tmp_path, selection_state
    ):
        """品質棄却の記録と除外指定が異なる場合は抽選しない。"""
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        candidates = [
            {"key": "K1", "label": "候補1", "base_weight": 1},
            {"key": "K2", "label": "候補2", "base_weight": 1},
        ]
        result = self.pick(run_script, tmp_path, selection_state, candidates)
        assert result.returncode == 2
        assert "品質棄却記録と一致しない" in result.stderr

    def test_pick_reports_no_remaining_candidates(
        self, run_script, tmp_path, selection_state
    ):
        """選択対象をすべて品質棄却した場合は候補なしとする。"""
        for candidate in selection_state["candidates"]:
            if candidate["disposition"] == "eligible":
                candidate["quality_rejection_reason"] = "品質条件が不適合"
        candidates = [
            {"key": "K1", "label": "候補1", "base_weight": 1},
            {"key": "K2", "label": "候補2", "base_weight": 1},
        ]
        result = self.pick(
            run_script,
            tmp_path,
            selection_state,
            candidates,
            "--exclude",
            "K1",
            "--exclude",
            "K2",
        )
        assert result.returncode == 1
        assert "抽選可能な候補が残っていない" in result.stderr

    def test_pick_rejects_incomplete_discovery(
        self, run_script, tmp_path, selection_state
    ):
        """探索が未完了なら抽選しない。"""
        selection_state["saturated"] = False
        candidates = [
            {"key": "K1", "label": "候補1", "base_weight": 1},
            {"key": "K2", "label": "候補2", "base_weight": 1},
        ]
        result = self.pick(run_script, tmp_path, selection_state, candidates)
        assert result.returncode == 1
        assert "探索が飽和していない" in result.stderr
