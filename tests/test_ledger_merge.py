"""台帳の断片をまとめるスクリプトの動作を確認する。"""

import json

import pytest


def exploration_fragment(prefix, area_id, label):
    """一つの下位領域を受け持つ題材探索担当の断片を作る。"""
    entry_id = f"{prefix}-E1"
    candidate_id = f"{prefix}-K1"
    return {
        "prefix": prefix,
        "entry_points": [
            {
                "id": entry_id,
                "kind": "事典索引",
                "label": f"{label}の事典",
                "url": f"https://example.org/{prefix}",
                "access_note": "索引項目",
                "opened": True,
            }
        ],
        "coverage_areas": [
            {
                "id": area_id,
                "explored": True,
                "entry_point_ids": [entry_id],
                "source_searches": [
                    {
                        "mode": "open",
                        "query": f"{label} 一覧",
                        "angle": "分野の索引",
                        "result": f"{label}を発見",
                        "entry_point_ids": [entry_id],
                        "found_candidate_ids": [candidate_id],
                        "next_searches": [],
                    }
                ],
            }
        ],
        "candidates": [
            {
                "id": candidate_id,
                "label": label,
                "coverage_area_ids": [area_id],
                "discovery_entry_point_ids": [entry_id],
                "name_use_note": "事典の本文で名称として使われる",
            }
        ],
    }


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
    return path


class TestMergeFragments:
    """断片のまとめ方を関数単位で確認する。"""

    @pytest.fixture
    def module(self, load_script):
        return load_script("generate-quiz", "ledger_merge.py")

    def test_adds_new_records_and_extends_existing_ones(
        self, module, intersection_state
    ):
        """断片の新しい記録を加え、すでにある下位領域へ探索記録を書き加える。"""
        merged = module.merge_fragments(
            intersection_state,
            [
                exploration_fragment("D1", "D1", "アンモニアソーダ法"),
                exploration_fragment("D2", "D2", "クメン法"),
            ],
        )
        assert [item["id"] for item in merged["candidates"]] == ["D1-K1", "D2-K1"]
        area = next(item for item in merged["coverage_areas"] if item["id"] == "D2")
        assert area["label"] == intersection_state["coverage_areas"][1]["label"]
        assert area["entry_point_ids"] == ["D2-E1"]

    def test_updates_record_created_by_another_fragment(
        self, module, intersection_state
    ):
        """ほかの断片が新しく加えた候補にも、断片の順によらず項目を書き加える。"""
        update = {
            "prefix": "N1",
            "candidates": [
                {
                    "id": "D1-K1",
                    "expanded": True,
                    "expansion_searches": [
                        {
                            "source_or_query": "アンモニアソーダ法の関連項目",
                            "relation_checked": "同じ製品の別の製法",
                            "found_candidate_ids": [],
                        }
                    ],
                }
            ],
        }
        merged = module.merge_fragments(
            intersection_state,
            [update, exploration_fragment("D1", "D1", "アンモニアソーダ法")],
        )
        assert merged["candidates"][0]["expanded"] is True

    def test_rejects_new_id_without_prefix(self, module, intersection_state):
        """新しい記録のIDは、断片の接頭辞で始める。"""
        fragment = exploration_fragment("D1", "D1", "アンモニアソーダ法")
        fragment["candidates"][0]["id"] = "K1"
        with pytest.raises(module.MergeError, match="接頭辞D1-で始まらない"):
            module.merge_fragments(intersection_state, [fragment])

    def test_rejects_conflicting_value(self, module, intersection_state):
        """すでにある値と異なる値は書き加えない。"""
        fragment = exploration_fragment("D1", "D1", "アンモニアソーダ法")
        fragment["coverage_areas"][0]["label"] = "別の下位領域"
        with pytest.raises(module.MergeError, match=r"coverage_areas\.D1\.labelの値"):
            module.merge_fragments(intersection_state, [fragment])

    def test_rejects_same_prefix(self, module, intersection_state):
        """同じ接頭辞の断片はまとめない。"""
        fragment = exploration_fragment("D1", "D1", "アンモニアソーダ法")
        with pytest.raises(module.MergeError, match="同じprefix"):
            module.merge_fragments(intersection_state, [fragment, fragment])


class TestLedgerMerge:
    """断片をまとめた探索状態が途中検査に合格することを確認する。"""

    def test_merged_state_passes_progress_check(
        self, run_script, tmp_path, intersection_state
    ):
        """まとめた探索状態を出力し、途中検査に合格する。"""
        intersection_state["execution"]["assignments"].extend(
            {
                "role": "exploration",
                "agent_id": f"agent-exploration-{area}",
                "artifact_refs": [f"{area}.json"],
                "items": [area],
            }
            for area in ("D1", "D2")
        )
        state = write_json(tmp_path / "state.json", intersection_state)
        fragments = [
            write_json(
                tmp_path / f"{prefix}.json",
                exploration_fragment(prefix, prefix, label),
            )
            for prefix, label in (("D1", "アンモニアソーダ法"), ("D2", "クメン法"))
        ]
        output = tmp_path / "merged.json"
        result = run_script("ledger_merge.py", state, *fragments, "-o", output)
        assert result.returncode == 0
        merged = output.read_text(encoding="utf-8")
        check = run_script(
            "work_state_check.py", "--stage", "discovery-progress", stdin=merged
        )
        assert check.returncode == 0, check.stderr

    def test_reports_unmergeable_fragment(
        self, run_script, tmp_path, intersection_state
    ):
        """まとめられない断片は入力エラーとして出力しない。"""
        state = write_json(tmp_path / "state.json", intersection_state)
        fragment = exploration_fragment("D1", "D1", "アンモニアソーダ法")
        fragment["candidates"][0]["id"] = "K1"
        output = tmp_path / "merged.json"
        result = run_script(
            "ledger_merge.py",
            state,
            write_json(tmp_path / "D1.json", fragment),
            "-o",
            output,
        )
        assert result.returncode == 2
        assert "接頭辞D1-で始まらない" in result.stderr
        assert not output.exists()
