"""配布スクリプトのCLI実行と関数テストに使う共通fixture。"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = (
    Path(__file__).resolve().parent.parent / "skills" / "generate-quiz" / "scripts"
)


@pytest.fixture
def run_script():
    def invoke(script, *args, stdin=None):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / script), *[str(arg) for arg in args]],
            input=stdin,
            capture_output=True,
            text=True,
        )

    return invoke


@pytest.fixture
def load_script(monkeypatch):
    def load(skill, filename):
        path = (
            Path(__file__).resolve().parent.parent
            / "skills"
            / skill
            / "scripts"
            / filename
        )
        module_name = f"test_{skill.replace('-', '_')}_{path.stem}"
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise ImportError(path)
        module = importlib.util.module_from_spec(spec)
        monkeypatch.syspath_prepend(str(path.parent))
        monkeypatch.setitem(sys.modules, module_name, module)
        spec.loader.exec_module(module)
        return module

    return load


@pytest.fixture
def intersection_state():
    """交差領域の成立性を確認した状態を作る。"""
    return {
        "execution": {
            "delegation_available": True,
            "agents": {"intersection": "agent-1"},
            "assignment_log": {
                "intersection": {
                    "agent_id": "agent-1",
                    "recorded_at_spawn": True,
                    "artifact_refs": ["intersection.md"],
                }
            },
        },
        "facet_nodes": {
            "subject": "subject::66",
            "place": "place::ROOT",
            "time": "time::ROOT",
            "type": "type::ROOT",
        },
        "intersection_review": {
            "source_refs": [
                "https://example.org/outline",
                "https://example.org/lesson",
            ],
            "candidate_examples": [
                {
                    "name": "候補1",
                    "source_ref": "https://example.org/outline",
                    "beginner_source_ref": "https://example.org/lesson",
                    "beginner_learning_basis": "名称と代表情報を学習項目として扱う",
                },
                {"name": "候補2", "source_ref": "https://example.org/outline"},
            ],
            "scope_reason": "対象の種類と下位領域を区分できる",
            "result": "viable",
        },
    }


@pytest.fixture
def selection_state(intersection_state):
    """探索範囲と候補の展開が完了した状態を作る。"""
    state = {
        **intersection_state,
        "entry_points": [
            {
                "id": "E1",
                "kind": "分類表",
                "label": "産業分類",
                "url": "https://example.org/industry",
                "access_note": "分類項目",
                "opened": True,
            },
            {
                "id": "E2",
                "kind": "事典索引",
                "label": "化学事典",
                "url": "https://example.org/encyclopedia",
                "access_note": "索引項目",
                "opened": True,
            },
            {
                "id": "E3",
                "kind": "利用者記事",
                "label": "実務記事",
                "url": "https://example.org/practice",
                "access_note": "記事本文",
                "opened": True,
            },
            {
                "id": "E4",
                "kind": "産業誌",
                "label": "産業誌記事",
                "url": "https://example.org/trade",
                "access_note": "記事本文",
                "opened": True,
            },
        ],
        "coverage_areas": [
            {
                "id": "D1",
                "label": "無機化学工業",
                "basis": "分類表の区分",
                "target_kinds": "工業技術",
                "explored": True,
                "entry_point_ids": ["E1"],
                "source_searches": [
                    {
                        "mode": "open",
                        "query": "無機化学工業 技術",
                        "angle": "分野の分類",
                        "result": "候補1を発見",
                        "entry_point_ids": ["E1"],
                        "found_candidate_ids": ["K1"],
                        "next_searches": [],
                    }
                ],
            },
            {
                "id": "D2",
                "label": "有機化学工業",
                "basis": "事典の区分",
                "target_kinds": "工業技術",
                "explored": True,
                "entry_point_ids": ["E2"],
                "source_searches": [
                    {
                        "mode": "open",
                        "query": "有機化学工業 技術",
                        "angle": "分野の索引",
                        "result": "候補2を発見",
                        "entry_point_ids": ["E2"],
                        "found_candidate_ids": ["K2"],
                        "next_searches": [],
                    }
                ],
            },
        ],
        "candidates": [
            {
                "id": "K1",
                "label": "候補1",
                "coverage_area_ids": ["D1"],
                "discovery_entry_point_ids": ["E1"],
                "name_use_note": "本文で対象の名称として使われる",
                "facet_membership_reason": "選択した四軸の内側にある",
                "disposition": "eligible",
                "expanded": True,
                "expansion_searches": [
                    {
                        "source_or_query": "候補1の関連項目",
                        "relation_checked": "同じ分野の並列項目",
                        "found_candidate_ids": [],
                    }
                ],
                "exposure_screen": {
                    "central_description": "対象を説明する語句",
                    "source_entry_point_ids": ["E1"],
                    "formation_risk": "suspected",
                    "reason": "名称形成の可能性を詳しく調べる",
                },
                "exposure_precheck": {
                    "representative_descriptions": [
                        "対象を説明する語句",
                        "別の中心的な特徴を説明する語句",
                    ],
                    "accepted_names": ["候補1"],
                    "formations": [],
                    "status": "passed",
                },
            },
            {
                "id": "K2",
                "label": "候補2",
                "coverage_area_ids": ["D2"],
                "discovery_entry_point_ids": ["E2"],
                "name_use_note": "本文で対象の名称として使われる",
                "facet_membership_reason": "選択した四軸の内側にある",
                "disposition": "eligible",
                "expanded": True,
                "expansion_searches": [
                    {
                        "source_or_query": "候補2の関連項目",
                        "relation_checked": "同じ分野の並列項目",
                        "found_candidate_ids": [],
                    }
                ],
                "exposure_screen": {
                    "central_description": "対象を説明する語句",
                    "source_entry_point_ids": ["E2"],
                    "formation_risk": "none_detected",
                    "reason": "中心的説明からは名称を形成できない",
                },
            },
        ],
        "frontier_ids": [],
        "saturated": True,
        "independent_review": [
            {
                "id": "D1",
                "difference_from_exploration": "実務者の利用場面",
                "source_discovery_query": "無機化学工業 実務者 利用",
                "checked_entry_point_ids": ["E3"],
                "found_candidate_ids": [],
                "spotchecked_entry_point_ids": ["E1"],
                "spotcheck_result": "分類項目と候補を照合した",
            },
            {
                "id": "D2",
                "difference_from_exploration": "産業誌の利用場面",
                "source_discovery_query": "有機化学工業 産業誌",
                "checked_entry_point_ids": ["E4"],
                "found_candidate_ids": [],
                "spotchecked_entry_point_ids": ["E2"],
                "spotcheck_result": "索引項目と候補を照合した",
            },
        ],
        "saturation_challenge": {
            "search_perspective": "別の書き手の産業資料",
            "query": "化学工業 現場 使用",
            "opened_entry_point_ids": ["E3", "E4"],
            "found_candidate_ids": [],
            "resolution": "新しい候補なし",
            "resolved": True,
        },
    }
    for index, role in enumerate(
        ("exploration", "alternate_exploration", "saturation_review"), 2
    ):
        agent = f"agent-{index}"
        state["execution"]["agents"][role] = agent
        state["execution"]["assignment_log"][role] = {
            "agent_id": agent,
            "recorded_at_spawn": True,
            "artifact_refs": [f"{role}.md"],
        }
    candidate = state["candidates"][0]
    name = candidate["label"]
    candidate["exposure_precheck"]["formations"] = [
        {
            "name": name,
            "description_index": index,
            "formation_rule": "対象との既知の対応から名称を選ぶ",
            "components": [
                {
                    "form": name,
                    "source": "対象との既知の対応",
                    "knowledge": "target_association",
                }
            ],
            "formation_requires_target_association": True,
            "formation_target_association_step": "名称要素を選ぶ",
            "standard_name_confirmation_requires_target_association": True,
        }
        for index in range(2)
    ]
    return state
