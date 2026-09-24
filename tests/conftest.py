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
def facet_state(load_script):
    """subjectだけを二階層下り、ほかの軸を最上位で止めたファセット選択の状態を作る。"""
    facet_node = load_script("generate-quiz", "facet_node.py")
    path = {"subject": ["subject::ROOT", "subject::6", "subject::66"]}
    levels, weights, picks = [], [], []
    for axis in ("subject", "place", "time", "type"):
        nodes = path.get(axis, [f"{axis}::ROOT"])
        for position, node in enumerate(nodes):
            level_id = f"F{len(levels) + 1}"
            descend = position < len(nodes) - 1
            levels.append(
                {
                    "id": level_id,
                    "axis": axis,
                    "node": node,
                    "decision": "descend" if descend else "stop",
                    "reason": f"{node}で止めるか子へ進むかを先行軸から判断した",
                }
            )
            if not descend:
                continue
            weights.append(
                {
                    "level_id": level_id,
                    "candidates": [
                        {
                            "key": key,
                            "label": key,
                            "weight": 1.0,
                            "viewpoints": {
                                "sharing": f"{key}の日本語圏での共有度",
                                "communication": f"{key}が使われる場面",
                                "background": f"{key}が背景知識として働く範囲",
                            },
                            "reason": f"{key}の三観点をまとめた",
                        }
                        for key in facet_node.child_keys(node)
                    ],
                }
            )
            picks.append({"level_id": level_id, "key": nodes[position + 1]})
    return {
        "execution": {
            "delegation_available": True,
            "assignments": [
                {
                    "role": role,
                    "agent_id": f"agent-{index}",
                    "artifact_refs": [f"{role}.json"],
                }
                for index, role in enumerate(
                    (
                        "facet_granularity",
                        "facet_weighting",
                        "facet_granularity_review",
                        "facet_weight_review",
                        "facet_distribution_review",
                    ),
                    1,
                )
            ],
        },
        "facet_levels": levels,
        "facet_weights": weights,
        "facet_level_reviews": [
            {
                "level_id": level["id"],
                "status": "passed",
                "reason": f"{level['node']}の判断を先行軸と照らして確認した",
            }
            for level in levels
        ],
        "facet_weight_reviews": [
            {
                "level_id": item["level_id"],
                "status": "passed",
                "reason": "各候補の三観点とweightの対応を確認した",
            }
            for item in weights
        ],
        "facet_distribution_reviews": [
            {
                "level_id": item["level_id"],
                "status": "passed",
                "reason": "兄弟ノード全体のweightの分布を重要度の差と照らした",
            }
            for item in weights
        ],
        "facet_picks": picks,
        "facet_nodes": {
            "subject": "subject::66",
            "place": "place::ROOT",
            "time": "time::ROOT",
            "type": "type::ROOT",
        },
    }


@pytest.fixture
def intersection_state():
    """4軸の交差領域の成立性を確認した状態を作る。"""
    return {
        "execution": {
            "delegation_available": True,
            "assignments": [
                {
                    "role": "intersection",
                    "agent_id": "agent-1",
                    "artifact_refs": ["intersection.md"],
                }
            ],
        },
        "facet_nodes": {
            "subject": "subject::66",
            "place": "place::ROOT",
            "time": "time::ROOT",
            "type": "type::ROOT",
        },
        "coverage_areas": [
            {
                "id": "D1",
                "label": "無機化学工業",
                "basis": "分類表の区分",
                "target_kinds": "工業技術",
            },
            {
                "id": "D2",
                "label": "有機化学工業",
                "basis": "事典の区分",
                "target_kinds": "工業技術",
            },
        ],
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
                "disposition": "eligible",
                "expanded": True,
                "expansion_searches": [
                    {
                        "source_or_query": "候補1の関連項目",
                        "relation_checked": "同じ分野の並列項目",
                        "found_candidate_ids": [],
                    }
                ],
            },
            {
                "id": "K2",
                "label": "候補2",
                "coverage_area_ids": ["D2"],
                "discovery_entry_point_ids": ["E2"],
                "name_use_note": "本文で対象の名称として使われる",
                "disposition": "eligible",
                "expanded": True,
                "expansion_searches": [
                    {
                        "source_or_query": "候補2の関連項目",
                        "relation_checked": "同じ分野の並列項目",
                        "found_candidate_ids": [],
                    }
                ],
            },
        ],
        "exposure_prechecks": [
            {
                "candidate_id": candidate_id,
                "result": "keep",
                "reason": f"{label}の名称を出さずに説明する書き方がある",
            }
            for candidate_id, label in (("K1", "候補1"), ("K2", "候補2"))
        ],
        "frontier_ids": [],
        "saturated": True,
        "memberships": [
            {
                "candidate_id": candidate_id,
                "axes": {
                    axis: {
                        "belongs": True,
                        "reason": f"{label}は{axis}のノードに属する",
                    }
                    for axis in ("subject", "place", "time", "type")
                },
            }
            for candidate_id, label in (("K1", "候補1"), ("K2", "候補2"))
        ],
        "membership_reviews": [
            {
                "candidate_id": candidate_id,
                "status": "passed",
                "reason": "名称が第一義に指す対象で所属を確かめた",
            }
            for candidate_id in ("K1", "K2")
        ],
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
            "core_check": {
                "source_entry_point_ids": ["E2"],
                "core_candidate_ids": ["K1", "K2"],
                "added_candidate_ids": [],
                "reason": "事典の概説が主要な対象として挙げる候補が台帳にある",
            },
        },
    }
    roles = (
        ("exploration", ["D1"]),
        ("exploration", ["D2"]),
        ("nearby_exploration", ["K1", "K2"]),
        ("membership", ["K1", "K2"]),
        ("membership_review", ["K1", "K2"]),
        ("alternate_exploration", None),
        ("saturation_review", None),
        ("exposure_precheck", None),
        ("topic_weighting", None),
    )
    state["execution"] = {
        **state["execution"],
        "assignments": [
            *state["execution"]["assignments"],
            *(
                {
                    "role": role,
                    "agent_id": f"agent-{index}",
                    "artifact_refs": [f"{role}-{index}.md"],
                    **({"items": items} if items else {}),
                }
                for index, (role, items) in enumerate(roles, 2)
            ),
        ],
    }
    return state
