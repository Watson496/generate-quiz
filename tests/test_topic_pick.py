"""探索台帳と題材抽選スクリプトの動作を確認する。"""

import json


class TestTopicPickFunctions:
    """探索状態からの基礎weightの計算と除外の指定を関数単位で確認する。"""

    def test_base_weight_is_product_of_two_stages(self, load_script, selection_state):
        """まとまりのweightとまとまりの中のweightの積を基礎weightとする。"""
        module = load_script("generate-quiz", "topic_pick.py")
        selection_state["candidate_weights"][1]["weight"] = 3.0
        payload = module.pick_payload(selection_state)
        assert {item["key"]: item["base_weight"] for item in payload["candidates"]} == {
            "K1": 2.0,
            "K2": 3.0,
        }

    def test_single_group_uses_candidate_weight(self, load_script, selection_state):
        """まとまりが一つなら、まとまりの中のweightを基礎weightとする。"""
        module = load_script("generate-quiz", "topic_pick.py")
        selection_state["topic_groups"] = [
            {
                "id": "G1",
                "label": "化学工業の製法",
                "candidate_ids": ["K1", "K2"],
                "reason": "候補が少ないので分けない",
            }
        ]
        del selection_state["group_weights"]
        payload = module.pick_payload(selection_state)
        assert [item["base_weight"] for item in payload["candidates"]] == [1.0, 1.0]

    def test_matching_quality_exclusion(self, load_script, selection_state):
        """品質棄却の記録と除外IDが一致すれば入力を認める。"""
        module = load_script("generate-quiz", "topic_pick.py")
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        assert module.validate_exclusions(selection_state, ["K1"]) is None

    def test_unrecorded_exclusion(self, load_script, selection_state):
        """品質棄却の記録がない候補の除外は認めない。"""
        module = load_script("generate-quiz", "topic_pick.py")
        assert "品質棄却記録と一致しない" in module.validate_exclusions(
            selection_state, ["K1"]
        )


class TestTopicPick:
    """探索台帳と候補抽選の接続を検査する。"""

    @staticmethod
    def pick(run_script, tmp_path, selection_state, *options):
        """台帳を題材抽選スクリプトへ渡す。"""
        state_path = tmp_path / "selection.json"
        state_path.write_text(
            json.dumps(selection_state, ensure_ascii=False), encoding="utf-8"
        )
        return run_script("topic_pick.py", state_path, *options)

    def test_pick_from_verified_candidates(self, run_script, tmp_path, selection_state):
        """検査済みの選択対象から題材を抽選する。"""
        result = self.pick(run_script, tmp_path, selection_state)
        assert result.returncode == 0
        assert result.stdout.startswith("CHOSEN\tK")

    def test_pick_skips_precheck_exclusion(self, run_script, tmp_path, selection_state):
        """予備検査で除外した候補は抽選の対象にしない。"""
        selection_state["exposure_prechecks"][1]["result"] = "exclude"
        selection_state["exposure_precheck_reviews"] = [
            {"candidate_id": "K2", "status": "passed", "reason": "どの説明でも露出する"}
        ]
        selection_state["execution"]["assignments"].append(
            {
                "role": "exposure_precheck_review",
                "agent_id": "agent-precheck-review",
                "artifact_refs": ["exposure_precheck_review.json"],
            }
        )
        selection_state["topic_groups"] = selection_state["topic_groups"][:1]
        del selection_state["group_weights"]
        selection_state["candidate_weights"] = selection_state["candidate_weights"][:1]
        selection_state["topic_group_reviews"] = selection_state["topic_group_reviews"][
            :1
        ]
        selection_state["topic_weight_reviews"] = selection_state[
            "topic_weight_reviews"
        ][:1]
        result = self.pick(run_script, tmp_path, selection_state)
        assert result.returncode == 0
        assert result.stdout.startswith("CHOSEN\tK1")

    def test_pick_excludes_failed_candidate(
        self, run_script, tmp_path, selection_state
    ):
        """不合格候補を除いて残りから再抽選する。"""
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        result = self.pick(run_script, tmp_path, selection_state, "--exclude", "K1")
        assert result.returncode == 0
        assert result.stdout.startswith("CHOSEN\tK2")

    def test_pick_requires_recorded_exclusion(
        self, run_script, tmp_path, selection_state
    ):
        """品質棄却の記録と除外指定が異なる場合は抽選しない。"""
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        result = self.pick(run_script, tmp_path, selection_state)
        assert result.returncode == 2
        assert "品質棄却記録と一致しない" in result.stderr

    def test_pick_reports_no_remaining_candidates(
        self, run_script, tmp_path, selection_state
    ):
        """選択対象をすべて品質棄却した場合は候補なしとする。"""
        for candidate in selection_state["candidates"]:
            if candidate["disposition"] == "eligible":
                candidate["quality_rejection_reason"] = "品質条件が不適合"
        result = self.pick(
            run_script, tmp_path, selection_state, "--exclude", "K1", "--exclude", "K2"
        )
        assert result.returncode == 1
        assert "抽選可能な候補が残っていない" in result.stderr

    def test_pick_rejects_incomplete_discovery(
        self, run_script, tmp_path, selection_state
    ):
        """探索が未完了なら抽選しない。"""
        selection_state["saturated"] = False
        result = self.pick(run_script, tmp_path, selection_state)
        assert result.returncode == 1
        assert "探索が飽和していない" in result.stderr
