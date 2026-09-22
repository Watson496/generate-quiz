"""作問状態の参照関係と工程別の検査を確認する。"""

import copy
import hashlib
import json
import tempfile
from pathlib import Path

import pytest

REQUIRED_CHECK_IDS = {
    "difficulty.beginner",
    "difficulty.general",
    "terminology",
    "clue_order",
    "answer_exposure",
    "structure",
    "expression.naturalness",
    "expression.comprehensibility",
    "expression.accuracy",
    "expression.incremental_comprehension",
    "length",
}
REQUIRED_OUTPUT_IDS = {
    "problem",
    "answer",
    "supplement",
    "alternatives",
    "judging",
    "topic_selection",
    "difficulty.beginner",
    "difficulty.general",
    "verification",
    "clues",
    "answer_limitation",
    "answer_exposure",
    "structure",
    "clue_order",
    "expression.naturalness",
    "expression.comprehensibility",
    "expression.accuracy",
    "expression.incremental_comprehension",
    "length",
    "answer_judging",
    "references",
}


@pytest.fixture
def complete_state():
    """全工程を通過できる一問分の作業状態を作る。"""
    evidence = ["Q1"]
    roles = (
        "exploration",
        "alternate_exploration",
        "saturation_review",
        "generation",
        "difficulty_review",
        "terminology_review",
        "exposure",
        "audit",
        "finalization",
    )
    agents = {role: f"agent-{index}" for index, role in enumerate(roles, 1)}
    checks = [
        {
            "id": check_id,
            "draft_version": 2,
            "claim": "条件を満たす",
            "reason": "資料と比較した",
            **(
                {}
                if check_id == "expression.naturalness"
                else {"evidence_ids": evidence}
            ),
            **(
                {"alternatives": ["何でしょう？", "これは何でしょう？"]}
                if check_id == "expression.naturalness"
                else {}
            ),
            **(
                {
                    "question_form": "SC",
                    "question_phrase": "は何でしょう？",
                    "nucleus": "錯視",
                    "otoshi": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
                    "otoshi_clue_ids": ["C1"],
                    "otoshi_direct_description": "錯視の図形条件と知覚結果を直接示す",
                    "prefuri_segments": [],
                    "connective_scan": "連用中止・テ形接続はない",
                    "connective_forms": [],
                }
                if check_id == "structure"
                else {}
            ),
            **(
                {
                    "blind_candidates": [],
                    "semantic_candidates": [
                        {
                            "name": "一般名称",
                            "formation_rule": "対象との既知の対応から名称を選ぶ",
                            "components": [
                                {
                                    "form": "一般名称",
                                    "source": "対象と名称の既知の対応",
                                    "knowledge": "target_association",
                                }
                            ],
                            "formation_requires_target_association": True,
                            "formation_target_association_step": "名称要素を選ぶ",
                            "standard_name_confirmation_requires_target_association": True,
                        }
                    ],
                    "target_knowledge_required": "対象固有の対応知識が必要",
                }
                if check_id == "answer_exposure"
                else {}
            ),
            "generation": "complete",
            "audit": "passed",
            **(
                {"asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える"}
                if check_id in {"difficulty.beginner", "difficulty.general"}
                else {}
            ),
        }
        for check_id in sorted(REQUIRED_CHECK_IDS)
    ]
    outputs = [
        {
            "id": output_id,
            "content_ref": f"output.{output_id}",
            "generation": "complete",
            "audit": "passed",
        }
        for output_id in sorted(REQUIRED_OUTPUT_IDS)
    ]
    clue_check = {
        "claim": "対象を絞れる",
        "reason": "定義と比較した",
        "evidence_ids": evidence,
        "generation": "complete",
        "audit": "passed",
    }
    return {
        "selection_mode": "random",
        "execution": {
            "delegation_available": True,
            "agents": agents,
            "assignment_log": {
                role: {
                    "agent_id": agent,
                    "recorded_at_spawn": True,
                    "artifact_refs": [f"{role}.md"],
                }
                for role, agent in agents.items()
            },
        },
        "answer_target": "ミュラー・リヤー錯視",
        "asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える",
        "difficulty_review": {
            "reviewer_id": agents["difficulty_review"],
            "asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える",
            "answer_granularity": "錯視の名称と図形条件の対応",
            "audit": "passed",
            "beginner": {
                "status": "passed",
                "reason": "日本語の初学者向け資料で学習対象として扱う",
                "evidence_ids": evidence,
                "name_learning": {
                    "reason": "初級教材が解答対象の名称を学習項目として扱う",
                    "evidence_ids": evidence,
                },
                "relation_learning": {
                    "reason": "基礎資料が問う図形条件を対象の特徴として扱う",
                    "evidence_ids": evidence,
                },
                "learning_connection": {
                    "reason": "同じ対象について名称と図形条件を基礎知識として学ぶ",
                    "evidence_ids": evidence,
                },
            },
            "general": {
                "status": "passed",
                "reason": "一般向け資料では名称を説明付きで導入する",
                "evidence_ids": evidence,
                "other_access_paths": [
                    {
                        "path": "一般向けの紹介で名称を既知として使うか",
                        "search_record": "一般向けの紹介資料を確認した",
                        "outcome": "confirmed",
                        "result": "別経路を確認した",
                        "evidence_ids": evidence,
                    }
                ],
            },
        },
        "draft": {
            "version": 2,
            "text": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視は何でしょう？",
        },
        "sources": [
            {
                "id": "S1",
                "citation": "資料名",
                "quotes": [
                    {
                        "id": "Q1",
                        "text": "矢羽は線分の端に付く斜線である。同じ長さの線分が矢羽の向きで異なる長さに見える錯視は入門教材で扱う",
                        "location": "第一節",
                    }
                ],
            }
        ],
        "propositions": [
            {
                "id": "P1",
                "status": "active",
                "draft_version": 2,
                "claim": "ミュラー・リヤー錯視では同じ長さの線分が矢羽の向きで異なる長さに見える",
                "passage": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
                "evidence_ids": evidence,
                "reason": "引用が直接述べる",
                "inference_type": "direct",
                "generation": "complete",
                "audit": "passed",
            }
        ],
        "clues": [
            {
                "id": "C1",
                "status": "active",
                "text": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
                "directly_describes_target": True,
                "proposition_ids": ["P1"],
                "checks": {
                    "centrality": copy.deepcopy(clue_check),
                    "quasi_uniqueness": {
                        **clue_check,
                        "comparison_scope": "同じ上位分類",
                        "competitors": [
                            {
                                "name": "近接候補",
                                "evidence_ids": evidence,
                                "conditions": [
                                    {
                                        "passage": "矢羽の向きで異なる長さに見える",
                                        "matches": False,
                                        "reason": "引用で候補の図形条件との差を確認した",
                                        "evidence_ids": evidence,
                                    }
                                ],
                                "disposition": "excluded",
                                "exclusion_passage": "矢羽の向きで異なる長さに見える",
                                "reason": "手掛かりに書かれた図形条件で区別する",
                            }
                        ],
                        "standalone_sufficient": True,
                        "depends_on_clue_ids": [],
                    },
                    "familiarity": copy.deepcopy(clue_check),
                },
            }
        ],
        "terms": [
            {
                "id": "T1",
                "term": "矢羽",
                "meaning_needed": True,
                "meaning_reason": "引用が語義を説明する",
                "meaning_evidence_ids": evidence.copy(),
                "audience_reason": "想定プレイヤー層で既習事項として扱う",
                "audience_evidence_ids": evidence.copy(),
                "generation": "complete",
                "audit": "passed",
            }
        ],
        "terminology_review": {
            "reviewer_id": agents["terminology_review"],
            "draft_version": 2,
            "audit": "passed",
            "terms": [
                {
                    "id": "T1",
                    "term": "矢羽",
                    "meaning_needed": True,
                    "meaning_status": "passed",
                    "audience_status": "passed",
                    "meaning_reason": "資料の定義と語義が一致する",
                    "audience_reason": "想定プレイヤー層の既習事項として扱う",
                    "meaning_evidence_ids": evidence.copy(),
                    "audience_evidence_ids": evidence.copy(),
                }
            ],
        },
        "answers": [
            {
                "id": "A1",
                "answer": "ミュラー・リヤー錯視",
                "judgment": "correct",
                "reason": "標準名称である",
                "evidence_ids": evidence,
                "generation": "complete",
                "audit": "passed",
            }
        ],
        "checks": checks,
        "output_elements": outputs,
        "final_input": {
            "draft_version": 2,
            "proposition_ids": ["P1"],
            "clue_ids": ["C1"],
            "term_ids": ["T1"],
            "answer_ids": ["A1"],
            "output_element_ids": sorted(REQUIRED_OUTPUT_IDS),
            "quote_ids": ["Q1"],
        },
    }


def final_output_text(state):
    """最終段階の構造検査に使う完成稿本文を組み立てる。"""
    quote_texts = "\n\n".join(
        f"> {quote['text']}"
        for source in state["sources"]
        for quote in source["quotes"]
        if quote["id"] in state["final_input"]["quote_ids"]
    )
    sections = {
        "問題": state["draft"]["text"],
        "解答": state["answer_target"],
        "補足": "なし",
        "別解": "なし",
        "正誤判定基準": "正答の扱いを示す。",
        "題材選択": "題材を選んだ。",
        "難易度": "資料名の第一節では、入門教材での扱いを確認できる。",
        "裏取り": f"資料名（第一節）に次の記述がある。\n\n{quote_texts}",
        "手掛かりの設計": "資料名の第一節にある図形条件を手掛かりに使う。",
        "問題の成立性": "図形条件によって対象を限定する。",
        "問題文の構成": "SC型である。",
        "問題文の表現": "資料名の第一節にある矢羽の説明と表現を照合する。",
        "問題文の長さ": "文字数を確認した。",
        "解答と正誤判定": "解答対象の名称を正答とする。",
        "参考文献": "資料名（第一節）。",
    }
    return "\n\n".join(f"## {heading}\n\n{body}" for heading, body in sections.items())


@pytest.fixture
def generation_state(complete_state):
    """生成工程の監査前にある一問分の作業状態を作る。"""
    state = copy.deepcopy(complete_state)
    state["difficulty_review"]["audit"] = "pending"
    state["terminology_review"]["audit"] = "pending"
    for group in ("propositions", "terms", "answers", "checks", "output_elements"):
        for item in state[group]:
            item["audit"] = "pending"
    for check in state["clues"][0]["checks"].values():
        check["audit"] = "pending"
    return state


@pytest.fixture
def reviewed_state(complete_state):
    """完成稿を監査担当が照合した最終段階の作業状態を作る。"""
    state = copy.deepcopy(complete_state)
    state["final_review"] = {
        "status": "passed",
        "reviewer_id": state["execution"]["agents"]["audit"],
        "output_sha256": hashlib.sha256(
            final_output_text(state).encode("utf-8")
        ).hexdigest(),
    }
    return state


@pytest.fixture
def exposed_precheck():
    """異なる代表説明から解答名を形成できる露出予備検査を作る。"""
    return {
        "representative_descriptions": [
            "腓腹筋とヒラメ筋を踵骨につなぐ腱",
            "足首を底屈させる際に踵骨へ筋力を伝える腱",
        ],
        "accepted_names": ["踵骨腱"],
        "formations": [
            {
                "name": "踵骨腱",
                "description_index": 0,
                "formation_rule": "付着先の骨と腱を表す語を結ぶ",
                "components": [
                    {
                        "form": "踵骨",
                        "source": "腓腹筋とヒラメ筋を踵骨につなぐ腱",
                        "knowledge": "surface",
                    },
                    {
                        "form": "腱",
                        "source": "腓腹筋とヒラメ筋を踵骨につなぐ腱",
                        "knowledge": "surface",
                    },
                ],
                "formation_requires_target_association": False,
                "standard_name_confirmation_requires_target_association": True,
            },
            {
                "name": "踵骨腱",
                "description_index": 1,
                "formation_rule": "力を伝える先の骨と腱を表す語を結ぶ",
                "components": [
                    {
                        "form": "踵骨",
                        "source": "足首を底屈させる際に踵骨へ筋力を伝える腱",
                        "knowledge": "surface",
                    },
                    {
                        "form": "腱",
                        "source": "足首を底屈させる際に踵骨へ筋力を伝える腱",
                        "knowledge": "surface",
                    },
                ],
                "formation_requires_target_association": False,
                "standard_name_confirmation_requires_target_association": True,
            },
        ],
        "status": "rejected",
    }


def check_state(run_script, stage, state):
    if stage == "final":
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "完成稿.md"
            output.write_text(final_output_text(state), encoding="utf-8")
            return run_script(
                "work_state_check.py",
                "--stage",
                stage,
                "--output",
                output,
                stdin=json.dumps(state, ensure_ascii=False),
            )
    return run_script(
        "work_state_check.py",
        "--stage",
        stage,
        stdin=json.dumps(state, ensure_ascii=False),
    )


@pytest.fixture
def state_module(load_script):
    return load_script("generate-quiz", "work_state_check.py")


class TestWorkStateFunctions:
    """作業状態の独立した検査規則を確認する。"""

    def test_structure_accepts_prefuri_predication(self, state_module):
        """落としの前にある叙述の記録を構文検査が受け付ける。"""
        state_module.validate_structure_check(
            {
                "question_form": "SC",
                "question_phrase": "は何でしょう？",
                "nucleus": "錯視",
                "otoshi": "同じ長さの線分が異なる長さに見える錯視",
                "otoshi_direct_description": "図形と知覚結果を直接示す",
                "otoshi_clue_ids": ["C1"],
                "prefuri_segments": [
                    {
                        "passage": "1889年に発表された",
                        "target_predication": "錯視は1889年に発表された",
                        "reason": "解答対象の成立について独立した事実を述べる",
                    }
                ],
                "connective_scan": "連用中止・テ形接続はない",
                "connective_forms": [],
            },
            "checks.structure",
            "1889年に発表された、同じ長さの線分が異なる長さに見える錯視は何でしょう？",
            [
                {
                    "id": "C1",
                    "text": "同じ長さの線分が異なる長さに見える錯視",
                    "directly_describes_target": True,
                }
            ],
        )

    def test_required_id_list_accepts_valid_ids(self, state_module):
        """空でない文字列IDの配列をそのまま受け付ける。"""
        ids = ["P1", "P2"]
        assert state_module.required_id_list(ids, "参照ID", nonempty=True) == ids

    @pytest.mark.parametrize("invalid_id", [{}, [], 1, ""])
    def test_required_id_list_rejects_invalid_ids(self, state_module, invalid_id):
        """参照IDの配列に文字列以外や空文字列を含めない。"""
        with pytest.raises(state_module.StateError, match="空でない文字列ID"):
            state_module.required_id_list([invalid_id], "参照ID")

    def test_referenced_ids_accepts_known_ids(self, state_module):
        """参照先に存在するIDを受け付ける。"""
        ids = ["Q1", "Q2"]
        assert (
            state_module.referenced_ids(
                {"evidence_ids": ids}, "evidence_ids", set(ids), "命題"
            )
            == ids
        )

    def test_referenced_ids_rejects_unknown_id(self, state_module):
        """参照先に存在しないIDを拒否する。"""
        with pytest.raises(state_module.StateError, match="存在しないID"):
            state_module.referenced_ids(
                {"evidence_ids": ["Q2"]}, "evidence_ids", {"Q1"}, "命題"
            )

    def test_records_with_ids_accepts_distinct_ids(self, state_module):
        """異なるIDを持つレコードとそのID集合を返す。"""
        records = [{"id": "P1"}, {"id": "P2"}]
        assert state_module.records_with_ids(records, "命題") == (
            records,
            {"P1", "P2"},
        )

    def test_records_with_ids_rejects_duplicate_id(self, state_module):
        """同一集合内の重複したIDを拒否する。"""
        with pytest.raises(state_module.StateError, match="idが重複"):
            state_module.records_with_ids([{"id": "P1"}, {"id": "P1"}], "命題")

    @pytest.mark.parametrize(
        ("stage", "audit"),
        [("generation", "pending"), ("audit", "passed"), ("final", "passed")],
    )
    def test_stage_completion_accepts_matching_audit_state(
        self, state_module, stage, audit
    ):
        """各工程で許される監査状態を受け付ける。"""
        record = {"generation": "complete", "audit": audit}
        state_module.require_stage_completion(record, "命題", stage)

    @pytest.mark.parametrize(
        ("stage", "audit"),
        [("generation", "passed"), ("audit", "pending")],
    )
    def test_stage_completion_rejects_mismatched_audit_state(
        self, state_module, stage, audit
    ):
        """工程に合わない監査状態を拒否する。"""
        record = {"generation": "complete", "audit": audit}
        with pytest.raises(state_module.StateError, match="監査"):
            state_module.require_stage_completion(record, "命題", stage)


class TestIntersectionState:
    """題材探索前の交差領域の記録を検査する。"""

    def test_complete_intersection_passes(self, run_script, intersection_state):
        """四軸、候補例、初級学習資料の記録を受け付ける。"""
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 0
        )

    def test_parent_review_passes_without_spawn_record(
        self, run_script, intersection_state
    ):
        """委譲できない場合の親agentによる確認を受け付ける。"""
        intersection_state["execution"] = {
            "delegation_available": False,
            "unavailable_reason": "委譲機能を利用できない",
        }
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 0
        )

    def test_delegated_review_requires_spawn_record(
        self, run_script, intersection_state
    ):
        """別agentによる確認では起動時の担当記録を必須とする。"""
        del intersection_state["execution"]["assignment_log"]["intersection"][
            "recorded_at_spawn"
        ]
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    def test_delegated_review_rejects_parent(self, run_script, intersection_state):
        """委譲できる場合は選択担当による自己確認を拒否する。"""
        intersection_state["execution"]["agents"]["intersection"] = "parent"
        intersection_state["execution"]["assignment_log"]["intersection"][
            "agent_id"
        ] = "parent"
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    def test_assignment_agent_must_match_spawn_record(
        self, run_script, intersection_state
    ):
        """交差確認担当と起動時の担当記録の不一致を拒否する。"""
        intersection_state["execution"]["assignment_log"]["intersection"][
            "agent_id"
        ] = "agent-2"
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    def test_duplicate_candidate_name_fails(self, run_script, intersection_state):
        """同一名称を二回数えた候補例を拒否する。"""
        examples = intersection_state["intersection_review"]["candidate_examples"]
        examples[1]["name"] = examples[0]["name"]
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    @pytest.mark.parametrize(
        "source", ["資料名", "https://", "https://example.org/a b"]
    )
    def test_source_refs_require_web_urls(self, run_script, intersection_state, source):
        """確認資料の参照にはWebのURLを要求する。"""
        intersection_state["intersection_review"]["source_refs"][0] = source
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    def test_unknown_node_fails(self, run_script, intersection_state):
        """カタログにないノードを拒否する。"""
        intersection_state["facet_nodes"]["type"] = "type::unknown"
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    def test_missing_beginner_basis_fails(self, run_script, intersection_state):
        """初級学習資料中での扱いを欠く候補例を拒否する。"""
        del intersection_state["intersection_review"]["candidate_examples"][0][
            "beginner_learning_basis"
        ]
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )

    def test_unconfirmed_intersection_fails(self, run_script, intersection_state):
        """成立を確認していない交差領域を題材探索へ進めない。"""
        intersection_state["intersection_review"]["result"] = "pending"
        assert (
            check_state(
                run_script, "intersection-checkpoint", intersection_state
            ).returncode
            == 1
        )


class TestDiscoveryProgressState:
    """題材探索途中の状態を検査する。"""

    def test_discovery_progress_accepts_incomplete_ledger(
        self, run_script, selection_state
    ):
        """最初の下位領域だけの台帳でも発見元を途中検査できる。"""
        selection_state["coverage_areas"] = selection_state["coverage_areas"][:1]
        selection_state["candidates"] = selection_state["candidates"][:1]
        selection_state["candidates"][0]["expansion_searches"] = []
        assert (
            check_state(run_script, "discovery-progress", selection_state).returncode
            == 0
        )

    def test_discovery_progress_requires_candidate_source_link(
        self, run_script, selection_state
    ):
        """候補の発見元が検索記録に結び付かない台帳を拒否する。"""
        selection_state["candidates"][0]["discovery_entry_point_ids"] = ["E2"]
        result = check_state(run_script, "discovery-progress", selection_state)
        assert result.returncode == 1
        assert "発見元・下位領域" in result.stderr

    def test_discovery_progress_accepts_internal_seed_without_source(
        self, run_script, selection_state
    ):
        """資料で未確認の想起候補は途中記録に残せる。"""
        selection_state["candidates"][0]["discovery_entry_point_ids"] = []
        selection_state["coverage_areas"][0]["source_searches"][0][
            "found_candidate_ids"
        ] = []
        assert (
            check_state(run_script, "discovery-progress", selection_state).returncode
            == 0
        )
        assert check_state(run_script, "discovery", selection_state).returncode == 1

    def test_discovery_progress_validates_recorded_url(
        self, run_script, selection_state
    ):
        """途中状態でも記録済み入口のURLを検査する。"""
        selection_state["entry_points"][0]["url"] = "資料の場所"
        assert (
            check_state(run_script, "discovery-progress", selection_state).returncode
            == 1
        )


class TestSelectionState:
    """題材探索の完了状態を検査する。"""

    def test_selection_requires_candidate_source_link(
        self, run_script, selection_state
    ):
        """完成した探索台帳でも候補と発見元の対応を検査する。"""
        selection_state["candidates"][0]["discovery_entry_point_ids"] = ["E2"]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "発見元・下位領域" in result.stderr

    def test_selection_rejects_extra_unlinked_source(
        self, run_script, selection_state
    ):
        """正しい発見元が一つあっても根拠のない追加入口を拒否する。"""
        selection_state["candidates"][0]["discovery_entry_point_ids"].append("E2")
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "発見元・下位領域" in result.stderr

    def test_selection_requires_intersection_review(self, run_script, selection_state):
        """交差領域の確認を省いた探索状態を拒否する。"""
        del selection_state["intersection_review"]
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_complete_selection_passes(self, run_script, selection_state):
        """異種の入口と展開済み候補が揃えば探索状態が合格する。"""
        assert check_state(run_script, "selection", selection_state).returncode == 0

    def test_selection_accepts_quality_rejection(self, run_script, selection_state):
        """抽選後の品質棄却理由は探索段階の選択可否を変えずに記録できる。"""
        selection_state["candidates"][0]["quality_rejection_reason"] = "難易度が不適合"
        assert check_state(run_script, "selection", selection_state).returncode == 0

    def test_selection_rejects_empty_quality_reason(self, run_script, selection_state):
        """品質棄却の理由を空のまま記録できない。"""
        selection_state["candidates"][0]["quality_rejection_reason"] = ""
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_discovery_precedes_exposure_precheck(self, run_script, selection_state):
        """露出予備検査の前に題材探索の完了だけを検査できる。"""
        for candidate in selection_state["candidates"]:
            del candidate["exposure_precheck"]
        assert check_state(run_script, "discovery", selection_state).returncode == 0
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_opened_source(self, run_script, selection_state):
        """本文を開いていない資料を候補の発見元にできない。"""
        selection_state["entry_points"][0]["opened"] = False
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "本文を開いていない" in result.stderr

    def test_selection_requires_name_use(self, run_script, selection_state):
        """候補名が対象の呼称として使われる箇所を欠く台帳を拒否する。"""
        del selection_state["candidates"][0]["name_use_note"]
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_facet_membership(self, run_script, selection_state):
        """四軸への所属理由を欠く候補を拒否する。"""
        del selection_state["candidates"][0]["facet_membership_reason"]
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_independent_review(self, run_script, selection_state):
        """別経路の探索が欠けた下位領域を拒否する。"""
        selection_state["independent_review"].pop()
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_processed_challenge(self, run_script, selection_state):
        """反証調査で得た候補を未処理のまま抽選させない。"""
        selection_state["saturation_challenge"]["resolved"] = False
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_rejects_candidate_name_in_open_search(
        self, run_script, selection_state
    ):
        """候補名を用いた検索を候補名なしの入口探索として扱わない。"""
        selection_state["coverage_areas"][0]["source_searches"][0]["query"] = (
            "候補1 関連項目"
        )
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_following_next_search(
        self, run_script, selection_state
    ):
        """記録した有望な検索先を調べずに探索を終えられない。"""
        selection_state["coverage_areas"][0]["source_searches"][0]["next_searches"] = [
            "未調査の資料"
        ]
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_distinct_entry_kinds(self, run_script, selection_state):
        """探索入口が同じ種類だけなら探索状態を拒否する。"""
        for entry in selection_state["entry_points"]:
            entry["kind"] = "分類表"
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "異なる種類の入口" in result.stderr

    def test_selection_requires_empty_frontier(self, run_script, selection_state):
        """未展開の有力候補を残した探索状態を拒否する。"""
        selection_state["frontier_ids"] = ["K2"]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "未展開の有力候補" in result.stderr

    @pytest.mark.parametrize("invalid_id", [{}, []])
    def test_selection_rejects_nonstring_frontier_id(
        self, run_script, selection_state, invalid_id
    ):
        """未展開候補のIDに文字列以外を指定しても追跡表示を出さない。"""
        selection_state["frontier_ids"] = [invalid_id]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "空でない文字列ID" in result.stderr
        assert "Traceback" not in result.stderr

    def test_selection_rejects_unclassified_candidate(
        self, run_script, selection_state
    ):
        """採否が未記録の候補を含む探索状態を拒否する。"""
        del selection_state["candidates"][0]["disposition"]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "dispositionが不正" in result.stderr

    def test_selection_rejects_speculative_exclusion(self, run_script, selection_state):
        """定められていない理由で候補を除外できない。"""
        selection_state["candidates"][0].update(
            disposition="excluded",
            exclusion_code="difficulty_outlook",
            exclusion_reason="一般層に知られていそうである",
        )
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "exclusion_codeが不正" in result.stderr

    def test_selection_accepts_unverified_name_exclusion(
        self, run_script, selection_state
    ):
        """資料で実際の名称を確認できない仮称を探索段階で除外できる。"""
        candidate = selection_state["candidates"][0]
        candidate.update(
            disposition="excluded",
            exclusion_code="unverified_name",
            exclusion_reason="日本語資料中で対象の名称として確認できない",
        )
        del candidate["name_use_note"]
        assert check_state(run_script, "discovery", selection_state).returncode == 0
        assert check_state(run_script, "selection", selection_state).returncode == 0

    def test_selection_rejects_exposed_eligible_candidate(
        self, run_script, selection_state, exposed_precheck
    ):
        """異なる代表説明がすべて露出する候補を採用対象にしない。"""
        selection_state["candidates"][0]["exposure_precheck"] = exposed_precheck
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "選択対象にできない" in result.stderr

    def test_selection_accepts_exposure_as_explicit_exclusion(
        self, run_script, selection_state, exposed_precheck
    ):
        """解答露出を記録した候補を探索台帳に残して除外できる。"""
        candidate = selection_state["candidates"][0]
        candidate.update(disposition="excluded", exclusion_code="unavoidable_exposure")
        candidate["exclusion_reason"] = "自然な代表説明から正答名を形成できる"
        candidate["exposure_precheck"] = exposed_precheck
        assert check_state(run_script, "selection", selection_state).returncode == 0

    def test_precheck_requires_every_name_description_pair(
        self, run_script, selection_state
    ):
        """調べた説明案と許容名称の組合せを漏らせない。"""
        precheck = selection_state["candidates"][0]["exposure_precheck"]
        precheck["representative_descriptions"].append("別の中心的な特徴の説明")
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "各説明案と正答名・別名の組合せ" in result.stderr

    def test_precheck_requires_one_description_per_formation(
        self, run_script, selection_state
    ):
        """名称形成の記録を複数の説明案で兼用させない。"""
        formation = selection_state["candidates"][0]["exposure_precheck"]["formations"][
            0
        ]
        formation["description_index"] = [0, 1]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "description_indexが不正" in result.stderr

    def test_accepted_alias_can_expose_every_description(
        self, run_script, selection_state, exposed_precheck
    ):
        """代表解が露出しなくても許容別名が全案で露出すれば除外する。"""
        exposed_precheck["accepted_names"].insert(0, "アキレス腱")
        for index, description in enumerate(
            exposed_precheck["representative_descriptions"]
        ):
            exposed_precheck["formations"].append(
                {
                    "name": "アキレス腱",
                    "description_index": index,
                    "formation_rule": "対象との既知の対応から人名由来の名称を選ぶ",
                    "components": [
                        {
                            "form": "アキレス",
                            "source": "対象との既知の対応",
                            "knowledge": "target_association",
                        },
                        {
                            "form": "腱",
                            "source": description,
                            "knowledge": "surface",
                        },
                    ],
                    "formation_requires_target_association": True,
                    "formation_target_association_step": "人名由来の名称要素を選ぶ",
                    "standard_name_confirmation_requires_target_association": True,
                }
            )
        selection_state["candidates"][0]["exposure_precheck"] = exposed_precheck
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "選択対象にできない" in result.stderr

    def test_selection_rejects_confirmation_knowledge_as_formation_knowledge(
        self, run_script, selection_state
    ):
        """標準名の確認に必要な知識で名称形成を安全扱いしない。"""
        formation = selection_state["candidates"][0]["exposure_precheck"]["formations"][
            0
        ]
        formation["components"] = [
            {
                "form": "候補1",
                "source": "問題文の一般語から複合する",
                "knowledge": "general_language",
            }
        ]
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_keeps_public_project_with_alternative_description(
        self, run_script, selection_state
    ):
        """説明案ごとに露出が異なる制度候補は予備検査だけでは除外しない。"""
        precheck = selection_state["candidates"][0]["exposure_precheck"]
        exposed_description = "土地の区画を整理する事業"
        alternative_description = (
            "土地所有者が減歩で公共施設用地を出し、換地を受ける都市整備事業"
        )
        answer = "土地区画整理事業"
        precheck.update(
            representative_descriptions=[exposed_description, alternative_description],
            accepted_names=[answer],
            formations=[
                {
                    "name": answer,
                    "description_index": 0,
                    "formation_rule": "説明にある一般語を複合する",
                    "components": [
                        {
                            "form": part,
                            "source": exposed_description,
                            "knowledge": "general_language",
                        }
                        for part in ("土地", "区画", "整理", "事業")
                    ],
                    "formation_requires_target_association": False,
                    "standard_name_confirmation_requires_target_association": True,
                },
                {
                    "name": answer,
                    "description_index": 1,
                    "formation_rule": "説明と対象の対応から名称を選ぶ",
                    "components": [
                        {
                            "form": answer,
                            "source": alternative_description,
                            "knowledge": "target_association",
                        }
                    ],
                    "formation_requires_target_association": True,
                    "formation_target_association_step": "名称を選ぶ",
                    "standard_name_confirmation_requires_target_association": True,
                },
            ],
            status="passed",
        )
        assert check_state(run_script, "selection", selection_state).returncode == 0
        selection_state["candidates"][0].update(
            disposition="excluded",
            exclusion_code="unavoidable_exposure",
            exclusion_reason="第1案では名称を形成できる",
        )
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_formation_for_every_accepted_name(
        self, run_script, selection_state
    ):
        """許容する各名称の形成分析を要求する。"""
        selection_state["candidates"][0]["exposure_precheck"]["accepted_names"].append(
            "別名"
        )
        assert check_state(run_script, "selection", selection_state).returncode == 1


class TestWorkState:
    """生成・監査・最終出力の作業状態を検査する。"""

    @pytest.mark.parametrize("stage", ["audit", "final"])
    def test_complete_state_passes(
        self, run_script, complete_state, reviewed_state, stage
    ):
        """各項目が完了した状態は指定工程で合格する。"""
        state = complete_state if stage == "audit" else reviewed_state
        assert check_state(run_script, stage, state).returncode == 0

    @pytest.mark.parametrize("stage", ["audit", "final"])
    def test_specified_target_skips_exploration_assignments(
        self, run_script, complete_state, reviewed_state, stage
    ):
        """解答対象が直接指定された場合は題材探索の担当記録を要しない。"""
        state = complete_state if stage == "audit" else reviewed_state
        state["selection_mode"] = "specified"
        state["user_specified_target"] = state["answer_target"]
        for role in ("exploration", "alternate_exploration", "saturation_review"):
            del state["execution"]["agents"][role]
            del state["execution"]["assignment_log"][role]
        assert check_state(run_script, stage, state).returncode == 0

    def test_specified_target_must_match_answer_target(
        self, run_script, complete_state
    ):
        """指定された解答対象と作業対象の不一致を拒否する。"""
        complete_state["selection_mode"] = "specified"
        complete_state["user_specified_target"] = "別の対象"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "指定された解答対象と作業対象が一致しない" in result.stderr

    def test_work_state_requires_selection_mode(self, run_script, complete_state):
        """対象ごとの作業状態では選択方法を明示する。"""
        del complete_state["selection_mode"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "selection_modeが不正である" in result.stderr

    def test_difficulty_review_requires_assigned_agent(
        self, run_script, complete_state
    ):
        """難易度の独立検査には起動時に記録した担当者を要する。"""
        del complete_state["execution"]["agents"]["difficulty_review"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "execution.agents.difficulty_reviewがない" in result.stderr

    def test_difficulty_checkpoint_passes_without_draft(
        self, run_script, complete_state
    ):
        """作文前に問題文なしで難易度を検査できる。"""
        keys = {
            "selection_mode",
            "execution",
            "answer_target",
            "asked_knowledge",
            "sources",
            "difficulty_review",
        }
        state = {key: copy.deepcopy(complete_state[key]) for key in keys}
        roles = {
            "exploration",
            "alternate_exploration",
            "saturation_review",
            "generation",
            "difficulty_review",
        }
        for key in ("agents", "assignment_log"):
            state["execution"][key] = {
                role: item
                for role, item in state["execution"][key].items()
                if role in roles
            }
        state["difficulty_review"]["audit"] = "pending"
        assert check_state(run_script, "difficulty", state).returncode == 0

    def test_difficulty_review_matches_asked_knowledge(
        self, run_script, complete_state
    ):
        """問う知識を変更したら以前の難易度判定を通さない。"""
        complete_state["asked_knowledge"] = "考案年から錯視の名称を答える"
        complete_state["difficulty_review"]["audit"] = "pending"
        result = check_state(run_script, "difficulty", complete_state)
        assert result.returncode == 1
        assert (
            "difficulty_review.asked_knowledgeが問う知識と一致しない" in result.stderr
        )

    def test_difficulty_review_requires_audit(self, run_script, complete_state):
        """難易度担当の判定も監査担当の確認を要する。"""
        complete_state["difficulty_review"]["audit"] = "pending"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "difficulty_reviewが監査に合格していない" in result.stderr

    def test_difficulty_checks_match_asked_knowledge(self, run_script, complete_state):
        """完成稿の難易度検査は作文前に確認した問う知識と対応する。"""
        check = next(
            item
            for item in complete_state["checks"]
            if item["id"] == "difficulty.beginner"
        )
        check["asked_knowledge"] = "考案年から錯視の名称を答える"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert (
            "checks.difficulty.beginner.asked_knowledgeが問う知識と一致しない"
            in result.stderr
        )

    @pytest.mark.parametrize("group", ["beginner", "general"])
    def test_difficulty_review_requires_both_groups_to_pass(
        self, run_script, complete_state, group
    ):
        """難易度の独立検査は両参照集団の合格を要する。"""
        complete_state["difficulty_review"][group]["status"] = "missing"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert f"difficulty_review.{group}が独立検査に合格していない" in result.stderr

    def test_difficulty_review_requires_matching_reviewer(
        self, run_script, complete_state
    ):
        """難易度検査の記録は割り当てられた担当者に対応する。"""
        complete_state["difficulty_review"]["reviewer_id"] = "別の担当者"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "difficulty_review.reviewer_idが担当記録と一致しない" in result.stderr

    @pytest.mark.parametrize(
        "aspect", ["name_learning", "relation_learning", "learning_connection"]
    )
    def test_beginner_review_requires_each_learning_record(
        self, run_script, complete_state, aspect
    ):
        """名称・関係の学習と両者の接続を別々に記録する。"""
        del complete_state["difficulty_review"]["beginner"][aspect]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert f"difficulty_review.beginner.{aspect}がない" in result.stderr

    @pytest.mark.parametrize(
        "aspect", ["name_learning", "relation_learning", "learning_connection"]
    )
    def test_beginner_review_requires_learning_reason(
        self, run_script, complete_state, aspect
    ):
        """初学者側の各判断に理由を要求する。"""
        del complete_state["difficulty_review"]["beginner"][aspect]["reason"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert f"difficulty_review.beginner.{aspect}.reason" in result.stderr

    def test_beginner_review_accepts_distinct_learning_sources(
        self, run_script, complete_state
    ):
        """名称と問う関係へ別資料の引用を対応させた記録を受け付ける。"""
        complete_state["sources"][0]["quotes"][0]["text"] = (
            "入門教材はミュラー・リヤー錯視の名称を学習項目として扱う。"
            "矢羽は線分の端に付く斜線である。"
            "同じ長さの線分が矢羽の向きで異なる長さに見える錯視は入門教材で扱う"
        )
        complete_state["sources"].append(
            {
                "id": "S2",
                "citation": "基礎資料",
                "quotes": [
                    {
                        "id": "Q2",
                        "text": "基礎資料がミュラー・リヤー錯視の図形条件を標準的な特徴として扱う",
                        "location": "第二節",
                    }
                ],
            }
        )
        beginner = complete_state["difficulty_review"]["beginner"]
        beginner["evidence_ids"] = ["Q1", "Q2"]
        beginner["relation_learning"]["evidence_ids"] = ["Q2"]
        beginner["learning_connection"]["evidence_ids"] = ["Q1", "Q2"]
        complete_state["final_input"]["quote_ids"] = ["Q1", "Q2"]
        assert check_state(run_script, "audit", complete_state).returncode == 0

    @pytest.mark.parametrize(
        "aspect", ["name_learning", "relation_learning", "learning_connection"]
    )
    def test_beginner_learning_quotes_belong_to_review(
        self, run_script, complete_state, aspect
    ):
        """学習根拠の引用を初学者側の引用集合に対応させる。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "名称を扱う教材", "location": "第二節"}
        )
        complete_state["difficulty_review"]["beginner"][aspect]["evidence_ids"] = [
            "Q2"
        ]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert f"{aspect}.evidence_idsが初学者側の根拠に含まれない" in result.stderr

    def test_difficulty_review_requires_other_access_paths(
        self, run_script, complete_state
    ):
        """一般層に名称が共有される別経路の調査を省略しない。"""
        del complete_state["difficulty_review"]["general"]["other_access_paths"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "difficulty_review.general.other_access_paths" in result.stderr

    def test_difficulty_review_requires_evidence_for_other_access_paths(
        self, run_script, complete_state
    ):
        """接触を確認した経路の調査結果を引用に対応させる。"""
        path = complete_state["difficulty_review"]["general"]["other_access_paths"][0]
        del path["evidence_ids"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert (
            "difficulty_review.general.other_access_paths[0].evidence_ids"
            in result.stderr
        )

    def test_unconfirmed_access_path_does_not_require_quote(
        self, run_script, complete_state
    ):
        """接触を確認できない経路に存在しない逐語引用を要求しない。"""
        path = complete_state["difficulty_review"]["general"]["other_access_paths"][0]
        path["search_record"] = "一般向けの紹介資料を調べた"
        path["outcome"] = "not_confirmed"
        path["result"] = "調べた範囲では名称への接触を確認できなかった"
        path["evidence_ids"] = []
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_access_path_requires_search_record(self, run_script, complete_state):
        """接触を確認できない経路にも調べた内容を残す。"""
        path = complete_state["difficulty_review"]["general"]["other_access_paths"][0]
        path["outcome"] = "not_confirmed"
        path["evidence_ids"] = []
        del path["search_record"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert (
            "difficulty_review.general.other_access_paths[0].search_record"
            in result.stderr
        )

    def test_final_input_includes_difficulty_review_evidence(
        self, run_script, complete_state
    ):
        """難易度の独立検査だけに使う引用も最終入力へ渡す。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "初学者向け資料の記述", "location": "第二節"}
        )
        complete_state["difficulty_review"]["beginner"]["evidence_ids"] = [
            "Q1",
            "Q2",
        ]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr
        complete_state["final_input"]["quote_ids"].append("Q2")
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_final_input_excludes_other_access_path_evidence(
        self, run_script, complete_state
    ):
        """別経路の探索だけに使う引用は最終入力を増やさない。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "一般向け資料の記述", "location": "第二節"}
        )
        paths = complete_state["difficulty_review"]["general"]["other_access_paths"]
        paths[0]["evidence_ids"] = ["Q2"]
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_specified_target_requires_generation_assignment(
        self, run_script, complete_state
    ):
        """直接指定でも生成以降の担当は省略できない。"""
        complete_state["selection_mode"] = "specified"
        complete_state["user_specified_target"] = complete_state["answer_target"]
        del complete_state["execution"]["agents"]["generation"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "execution.agents.generationがない" in result.stderr

    def test_clue_rejects_quasi_uniqueness_depending_on_another_clue(
        self, run_script, complete_state
    ):
        """他の手掛かりに依存する準一意性を単独の評価として認めない。"""
        check = complete_state["clues"][0]["checks"]["quasi_uniqueness"]
        check["depends_on_clue_ids"] = ["C2"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    @pytest.mark.parametrize(
        "invalid_part",
        [
            "name",
            "evidence_ids",
            "conditions",
            "passage",
            "matches",
            "condition_evidence_ids",
            "exclusion_passage",
            "reason",
        ],
    )
    def test_competitor_requires_evidence_and_matching_clue_condition(
        self, run_script, complete_state, invalid_part
    ):
        """対抗候補の資料と問題文中の区別条件を欠く記録を拒否する。"""
        check = complete_state["clues"][0]["checks"]["quasi_uniqueness"]
        competitor = check["competitors"][0]
        if invalid_part == "name":
            competitor["name"] = ""
        elif invalid_part == "evidence_ids":
            competitor["evidence_ids"] = []
        elif invalid_part == "conditions":
            competitor["conditions"] = []
        elif invalid_part == "passage":
            competitor["conditions"][0]["passage"] = "問題文にない条件"
        elif invalid_part == "matches":
            competitor["conditions"][0]["matches"] = "未確認"
        elif invalid_part == "condition_evidence_ids":
            competitor["conditions"][0]["evidence_ids"] = []
        elif invalid_part == "exclusion_passage":
            competitor["exclusion_passage"] = "同じ長さの線分"
        else:
            competitor["reason"] = ""
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_competitor_evidence_belongs_to_clue_judgment(
        self, run_script, complete_state
    ):
        """対抗候補の引用を準一意性の判断根拠にも対応させる。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "対抗候補の記述", "location": "第二節"}
        )
        competitor = complete_state["clues"][0]["checks"]["quasi_uniqueness"][
            "competitors"
        ][0]
        competitor["evidence_ids"] = ["Q2"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_condition_evidence_belongs_to_competitor(
        self, run_script, complete_state
    ):
        """条件の引用を対抗候補の引用にも対応させる。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "条件についての記述", "location": "第二節"}
        )
        competitor = complete_state["clues"][0]["checks"]["quasi_uniqueness"]["competitors"][0]
        competitor["conditions"][0]["evidence_ids"] = ["Q2"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_competitor_with_all_matching_conditions_cannot_be_excluded(
        self, run_script, complete_state
    ):
        """問題文の条件に相違がない別対象を退けない。"""
        competitor = complete_state["clues"][0]["checks"]["quasi_uniqueness"][
            "competitors"
        ][0]
        competitor["conditions"][0]["matches"] = True
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_same_target_name_does_not_need_exclusion_passage(
        self, run_script, complete_state
    ):
        """同一対象の別名に別対象を退ける表現を要求しない。"""
        competitor = complete_state["clues"][0]["checks"]["quasi_uniqueness"][
            "competitors"
        ][0]
        competitor["disposition"] = "same_target"
        competitor["conditions"][0]["matches"] = True
        del competitor["exclusion_passage"]
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_same_target_name_cannot_have_different_condition(
        self, run_script, complete_state
    ):
        """異なる条件を記録した候補を同一対象の別名として通さない。"""
        competitor = complete_state["clues"][0]["checks"]["quasi_uniqueness"]["competitors"][0]
        competitor["disposition"] = "same_target"
        del competitor["exclusion_passage"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_otoshi_requires_directly_descriptive_clue(
        self, run_script, complete_state
    ):
        """落としに含む手掛かりは対象を直接説明する。"""
        complete_state["clues"][0]["directly_describes_target"] = False
        assert check_state(run_script, "audit", complete_state).returncode == 1

    @pytest.mark.parametrize(
        "nucleus", ["もの", "こと", "さま", "用語", "名前", "名称", "通称", "題名"]
    )
    def test_otoshi_rejects_generic_nucleus(self, run_script, complete_state, nucleus):
        """代名詞的な核名詞や名称の種類だけを示す核名詞を拒否する。"""
        complete_state["draft"]["text"] = (
            f"同じ長さの線分が矢羽の向きで異なる長さに見える{nucleus}は何でしょう？"
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure["nucleus"] = nucleus
        structure["otoshi"] = f"同じ長さの線分が矢羽の向きで異なる長さに見える{nucleus}"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "nucleusが解答対象の上位分類ではない" in result.stderr

    def test_structure_rejects_question_form_mismatch(self, run_script, complete_state):
        """質問表現と構文型の不一致を拒否する。"""
        complete_state["draft"]["text"] = (
            "同じ長さの線分が矢羽の向きで異なる長さに見える錯視を何というでしょう？"
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure["question_phrase"] = "を何というでしょう？"
        assert check_state(run_script, "audit", complete_state).returncode == 1

    @pytest.mark.parametrize("pronoun", ["誰", "どこ", "どちら"])
    def test_structure_rejects_sc_question_marked_as_ov(
        self, run_script, complete_state, pronoun
    ):
        """SC型の各疑問詞をOV型として記録した状態を拒否する。"""
        complete_state["draft"]["text"] = (
            f"同じ長さの線分が矢羽の向きで異なる長さに見える錯視は{pronoun}でしょう？"
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure.update(question_form="OV", question_phrase=f"は{pronoun}でしょう？")
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "question_formが質問形式と一致しない" in result.stderr

    def test_structure_rejects_otoshi_before_later_modifier(
        self, run_script, complete_state
    ):
        """最後端の付随説明より前の句を落としとは扱わない。"""
        complete_state["draft"]["text"] = (
            "流体のエネルギーを軸動力に変える原動機で、圧力が低下するものを何というでしょう？"
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure.update(
            question_form="OV",
            question_phrase="を何というでしょう？",
            nucleus="原動機",
            otoshi="流体のエネルギーを軸動力に変える原動機",
        )
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_structure_accepts_ov_post_limiter(self, run_script, complete_state):
        """OV型では落としの後に名称を限定する表現を置ける。"""
        complete_state["draft"]["text"] = (
            "同じ長さの線分が矢羽の向きで異なる長さに見える錯視を、一般に何というでしょう？"
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure.update(question_form="OV", question_phrase="何というでしょう？")
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_structure_requires_connective_scan(self, run_script, complete_state):
        """接続箇所がない場合も走査結果を要求する。"""
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        del structure["connective_scan"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_structure_requires_prefuri_segments(self, run_script, complete_state):
        """前フリがない問題でも検査済みの空配列を要求する。"""
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        del structure["prefuri_segments"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_structure_rejects_prefuri_after_otoshi(self, run_script, complete_state):
        """落としの後の表現を前フリとして記録できない。"""
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure["prefuri_segments"] = [
            {
                "passage": "錯視",
                "target_predication": "錯視は線分を示す",
                "reason": "対象の属性を述べる",
            }
        ]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "passageが落としより前の問題文にない" in result.stderr

    def test_structure_requires_prefuri_predication(self, run_script, complete_state):
        """前フリの叙述内容を記録しない状態を拒否する。"""
        complete_state["draft"]["text"] = (
            "1889年に発表された、" + complete_state["draft"]["text"]
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure["prefuri_segments"] = [
            {"passage": "1889年に発表された", "reason": "対象の属性を述べる"}
        ]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "target_predication" in result.stderr

    def test_structure_rejects_connection_without_semantic_relation(
        self, run_script, complete_state
    ):
        """接続箇所に定められた意味関係がない状態を拒否する。"""
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure["connective_forms"] = [
            {
                "passage": "創設され、調査する制度",
                "left_predication": "制度が創設された",
                "right_predication": "制度が調査する",
                "left_subject": "制度",
                "right_subject": "制度",
                "tense_aspect": "成立時点と恒常的機能",
                "relation": "unrelated",
                "reason": "同じ制度の別属性である",
            }
        ]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_generation_requires_pending_audit(self, run_script, generation_state):
        """生成工程では各項目の監査結果が未判定でなければならない。"""
        assert check_state(run_script, "generation", generation_state).returncode == 0
        generation_state["checks"][0]["audit"] = "passed"
        result = check_state(run_script, "generation", generation_state)
        assert result.returncode == 1
        assert "生成工程の時点で監査済み" in result.stderr

    def test_audit_requires_answer_exposure_check(self, run_script, complete_state):
        """解答露出の検査項目を欠く状態を監査で拒否する。"""
        complete_state["checks"] = [
            check
            for check in complete_state["checks"]
            if check["id"] != "answer_exposure"
        ]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "必須検査がない" in result.stderr

    def test_blind_candidate_matching_answer_without_target_association_fails(
        self, run_script, complete_state
    ):
        """対象との対応知識なしに正答名を形成できる状態を拒否する。"""
        exposure = next(
            check
            for check in complete_state["checks"]
            if check["id"] == "answer_exposure"
        )
        complete_state["answers"][0]["answer"] = "錯視"
        exposure["blind_candidates"] = [
            {
                "name": "錯視",
                "formation_rule": "問題文中の語をそのまま候補とする",
                "components": [
                    {
                        "form": "錯視",
                        "source": "問題文の表層",
                        "knowledge": "surface",
                    },
                ],
                "formation_requires_target_association": False,
                "standard_name_confirmation_requires_target_association": True,
            }
        ]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_blind_candidate_can_require_explicit_target_association(
        self, run_script, complete_state
    ):
        """名称形成自体に対象との対応知識が要る候補は受け付ける。"""
        exposure = next(
            check
            for check in complete_state["checks"]
            if check["id"] == "answer_exposure"
        )
        exposure["blind_candidates"] = [
            {
                "name": "ミュラー・リヤー錯視",
                "formation_rule": "既知の名称を想起する",
                "components": [
                    {
                        "form": "ミュラー・リヤー錯視",
                        "source": "対象と名称の既知の対応",
                        "knowledge": "target_association",
                    }
                ],
                "formation_requires_target_association": True,
                "formation_target_association_step": "名称要素を選ぶ段階",
                "standard_name_confirmation_requires_target_association": True,
            }
        ]
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_semantic_candidate_requires_formation_details(
        self, run_script, complete_state
    ):
        """意味から挙げた名称候補にも形成要素を要求する。"""
        exposure = next(
            check
            for check in complete_state["checks"]
            if check["id"] == "answer_exposure"
        )
        exposure["semantic_candidates"] = ["ミュラー・リヤー錯視"]
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_semantic_candidate_matching_answer_without_target_association_fails(
        self, run_script, complete_state
    ):
        """意味から正答名を形成できる状態を拒否する。"""
        exposure = next(
            check
            for check in complete_state["checks"]
            if check["id"] == "answer_exposure"
        )
        complete_state["answers"][0]["answer"] = "錯視"
        exposure["semantic_candidates"][0].update(
            name="錯視",
            formation_rule="問題文の語をそのまま候補とする",
            components=[
                {
                    "form": "錯視",
                    "source": "問題文の表層",
                    "knowledge": "surface",
                }
            ],
            formation_requires_target_association=False,
        )
        assert check_state(run_script, "audit", complete_state).returncode == 1

    def test_audit_rejects_old_draft_version(self, run_script, complete_state):
        """現行稿より古い版の検査結果を監査で拒否する。"""
        complete_state["checks"][0]["draft_version"] = 1
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "問題文の版が一致しない" in result.stderr

    def test_audit_rejects_unknown_quote(self, run_script, complete_state):
        """存在しない引用を根拠にした命題を監査で拒否する。"""
        complete_state["propositions"][0]["evidence_ids"] = ["Q2"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "存在しないIDを参照" in result.stderr

    @pytest.mark.parametrize("invalid_id", [{}, []])
    def test_audit_rejects_nonstring_quote_id(
        self, run_script, complete_state, invalid_id
    ):
        """引用IDに文字列以外を指定しても追跡表示を出さない。"""
        complete_state["propositions"][0]["evidence_ids"] = [invalid_id]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "空でない文字列ID" in result.stderr
        assert "Traceback" not in result.stderr

    def test_simple_proposition_can_omit_verification_elements(
        self, run_script, complete_state
    ):
        """単純な命題には形式的な検証要素を要求しない。"""
        assert "verification_elements" not in complete_state["propositions"][0]
        assert check_state(run_script, "audit", complete_state).returncode == 0

    def test_recorded_verification_elements_require_valid_evidence(
        self, run_script, complete_state
    ):
        """記録した各検証要素の引用IDを検査する。"""
        proposition = complete_state["propositions"][0]
        proposition["claim"] = "市が住民に賞状を贈った"
        proposition["passage"] = "市が住民に賞状を贈った"
        complete_state["sources"][0]["quotes"][0]["text"] = proposition["claim"]
        proposition["verification_elements"] = [
            {
                "text": "贈った主体は市",
                "reason": "引用が直接述べる",
                "inference_type": "direct",
                "evidence_ids": ["Q1"],
            },
            {
                "text": "贈った相手は住民",
                "reason": "引用が直接述べる",
                "inference_type": "direct",
                "evidence_ids": ["Q2"],
            },
        ]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "verification_elements[1].evidence_ids" in result.stderr

    def test_audit_requires_passed_check(self, run_script, complete_state):
        """未合格の検査項目を含む状態を監査で拒否する。"""
        complete_state["checks"][0]["audit"] = "missing"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "監査に合格していない" in result.stderr

    def test_audit_requires_passed_term(self, run_script, complete_state):
        """未合格の専門用語を含む状態を監査で拒否する。"""
        complete_state["terms"][0]["audit"] = "missing"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "terms.T1が監査に合格していない" in result.stderr

    def test_term_must_appear_in_current_draft(self, run_script, complete_state):
        """問題文にない語を専門用語の検査記録に含めない。"""
        complete_state["terms"][0]["term"] = "問題文にない専門用語"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "terms.T1.termが問題文にない" in result.stderr

    @pytest.mark.parametrize(
        "field",
        [
            "meaning_reason",
            "meaning_evidence_ids",
            "audience_reason",
            "audience_evidence_ids",
        ],
    )
    def test_term_requires_meaning_and_familiarity_evidence(
        self, run_script, complete_state, field
    ):
        """語義と既習性をそれぞれ根拠に結び付ける。"""
        del complete_state["terms"][0][field]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert field in result.stderr

    def test_term_without_needed_meaning_requires_explanation(
        self, run_script, complete_state
    ):
        """変形版の名称の内容を知らずに理解できる場合は理由を確認する。"""
        complete_state["draft"]["text"] = (
            "「ブレンターノ型」という変形版も知られる、"
            + complete_state["draft"]["text"]
        )
        term = complete_state["terms"][0]
        term["term"] = "ブレンターノ型"
        term["meaning_needed"] = False
        for field in (
            "meaning_reason",
            "meaning_evidence_ids",
            "audience_reason",
            "audience_evidence_ids",
        ):
            del term[field]
        review_term = complete_state["terminology_review"]["terms"][0]
        review_term["term"] = "ブレンターノ型"
        review_term["meaning_needed"] = False
        for field in (
            "meaning_status",
            "meaning_reason",
            "meaning_evidence_ids",
            "audience_status",
            "audience_reason",
            "audience_evidence_ids",
        ):
            del review_term[field]
        review_term["understanding_without_meaning"] = (
            "変形版の名称だと分かれば、図形の詳細を知らなくても文意が通る"
        )
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "understanding_without_meaning" in result.stderr
        term["understanding_without_meaning"] = (
            "変形版の名称だと分かれば、図形の詳細を知らなくても文意が通る"
        )
        assert check_state(run_script, "audit", complete_state).returncode == 0
        del review_term["understanding_without_meaning"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "terminology_review.terms.T1.understanding_without_meaning" in result.stderr

    @pytest.mark.parametrize(
        ("change", "expected"),
        [
            ("missing", "terminology_review.termsが専門用語の記録と一致しない"),
            ("term", "terminology_review.terms.T1.term"),
            ("meaning_needed", "terminology_review.terms.T1.meaning_needed"),
        ],
    )
    def test_terminology_review_checks_terms_and_meaning_need(
        self, run_script, complete_state, change, expected
    ):
        """独立検査で語の範囲と意味内容の要否を生成側と照合する。"""
        review = complete_state["terminology_review"]["terms"]
        if change == "missing":
            review.clear()
        elif change == "term":
            review[0]["term"] = "別の専門用語"
        else:
            review[0]["meaning_needed"] = False
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert expected in result.stderr

    @pytest.mark.parametrize("audit", ["pending", "missing", "failed"])
    def test_audit_requires_passed_terminology_review(
        self, run_script, complete_state, audit
    ):
        """専門用語の独立検査自体が監査に合格していることを確認する。"""
        complete_state["terminology_review"]["audit"] = audit
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "terminology_reviewが監査に合格していない" in result.stderr

    @pytest.mark.parametrize("kind", ["meaning", "audience"])
    def test_term_evidence_is_included_in_final_input(
        self, run_script, complete_state, kind
    ):
        """専門用語の判断に使う引用を最終入力の引用集合にも含める。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "矢羽の説明", "location": "用語解説"}
        )
        field = f"{kind}_evidence_ids"
        complete_state["terms"][0][field] = ["Q2"]
        complete_state["terminology_review"]["terms"][0][field] = ["Q2"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr
        complete_state["final_input"]["quote_ids"].append("Q2")
        assert check_state(run_script, "audit", complete_state).returncode == 0

    @pytest.mark.parametrize("kind", ["meaning", "audience"])
    def test_terminology_review_covers_all_adopted_evidence(
        self, run_script, complete_state, kind
    ):
        """生成側が採用した専門用語の引用を独立検査で残さず確認する。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "矢羽の別の説明", "location": "第二節"}
        )
        field = f"{kind}_evidence_ids"
        complete_state["terms"][0][field].append("Q2")
        complete_state["final_input"]["quote_ids"].append("Q2")
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert f"terminology_review.terms.T1.{field}" in result.stderr
        complete_state["terminology_review"]["terms"][0][field].append("Q2")
        assert check_state(run_script, "audit", complete_state).returncode == 0

    @pytest.mark.parametrize(
        ("change", "expected"),
        [
            ("missing", "terminology_reviewがない"),
            ("failed", "terminology_review.terms.T1.audience_status"),
            ("stale", "terminology_review.draft_version"),
            ("same_agent", "工程を別々のagentへ割り当てていない"),
            ("audited", "terminology_reviewは生成工程の時点で監査済み"),
        ],
    )
    def test_generation_requires_independent_terminology_review(
        self, run_script, generation_state, change, expected
    ):
        """独立した担当が現行版の語義と既習性を検査する。"""
        assert check_state(run_script, "generation", generation_state).returncode == 0
        if change == "missing":
            del generation_state["terminology_review"]
        elif change == "failed":
            generation_state["terminology_review"]["terms"][0]["audience_status"] = (
                "missing"
            )
        elif change == "stale":
            generation_state["terminology_review"]["draft_version"] = 1
        elif change == "audited":
            generation_state["terminology_review"]["audit"] = "passed"
        else:
            generation_state["execution"]["agents"]["terminology_review"] = (
                generation_state["execution"]["agents"]["generation"]
            )
        result = check_state(run_script, "generation", generation_state)
        assert result.returncode == 1
        assert expected in result.stderr

    def test_audit_requires_passed_answer(self, run_script, complete_state):
        """未合格の解答候補を含む状態を監査で拒否する。"""
        complete_state["answers"][0]["audit"] = "missing"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "answers.A1が監査に合格していない" in result.stderr

    def test_audit_requires_verbatim_quote(self, run_script, complete_state):
        """引用本文を欠く資料を監査で拒否する。"""
        del complete_state["sources"][0]["quotes"][0]["text"]
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "quotes.Q1.textがない" in result.stderr

    def test_audit_rejects_quote_missing_from_final_input(
        self, run_script, complete_state
    ):
        """採用した判断に使う引用を最終入力から落とせない。"""
        complete_state["final_input"]["quote_ids"] = []
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr

    def test_audit_rejects_unused_quote_in_final_input(
        self, run_script, complete_state
    ):
        """採用した判断に使わない引用を最終入力へ加えない。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "不採用の記述", "location": "第二節"}
        )
        complete_state["final_input"]["quote_ids"].append("Q2")
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr

    def test_audit_rejects_duplicate_quote_in_final_input(
        self, run_script, complete_state
    ):
        """同じ引用IDを重複して最終入力へ置かない。"""
        complete_state["final_input"]["quote_ids"].append("Q1")
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr

    @pytest.mark.parametrize(
        "key",
        [
            "proposition_ids",
            "clue_ids",
            "term_ids",
            "answer_ids",
            "output_element_ids",
        ],
    )
    def test_audit_rejects_duplicate_final_input_id(
        self, run_script, complete_state, key
    ):
        """最終入力の各ID配列で重複を認めない。"""
        complete_state["final_input"][key].append(complete_state["final_input"][key][0])
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert f"final_input.{key}が検査済みの現行項目と一致しない" in result.stderr

    def test_audit_ignores_unchecked_clue_field(self, run_script, complete_state):
        """手掛かりの必須検査以外の値を引用収集の対象にしない。"""
        complete_state["clues"][0]["checks"]["note"] = "補足"
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 0

    def test_final_requires_quote_in_output(self, run_script, reviewed_state, tmp_path):
        """採用した引用本文が完成稿にない場合は確定できない。"""
        output = tmp_path / "完成稿.md"
        output.write_text(
            final_output_text(reviewed_state).replace(
                reviewed_state["sources"][0]["quotes"][0]["text"], "引用を含まない記述"
            ),
            encoding="utf-8",
        )
        result = run_script(
            "work_state_check.py",
            "--stage",
            "final",
            "--output",
            output,
            stdin=json.dumps(reviewed_state, ensure_ascii=False),
        )
        assert result.returncode == 1
        assert "最終出力に引用Q1がない" in result.stderr

    def test_final_rejects_wrong_heading(self, run_script, reviewed_state, tmp_path):
        """完成稿の見出し名を照合する。"""
        output = tmp_path / "完成稿.md"
        output.write_text(
            final_output_text(reviewed_state).replace("## 難易度", "## 難度"),
            encoding="utf-8",
        )
        result = run_script(
            "work_state_check.py",
            "--stage",
            "final",
            "--output",
            output,
            stdin=json.dumps(reviewed_state, ensure_ascii=False),
        )
        assert result.returncode == 1
        assert "見出しに欠落・重複・順序違い" in result.stderr

    def test_final_rejects_preamble(self, run_script, reviewed_state, tmp_path):
        """完成稿の先頭に作業用記録を置かない。"""
        output = tmp_path / "完成稿.md"
        output.write_text(
            "担当ID: agent-1\n" + final_output_text(reviewed_state), encoding="utf-8"
        )
        result = run_script(
            "work_state_check.py",
            "--stage",
            "final",
            "--output",
            output,
            stdin=json.dumps(reviewed_state, ensure_ascii=False),
        )
        assert result.returncode == 1
        assert "先頭に作業用記録" in result.stderr

    def test_final_rejects_different_question(
        self, run_script, reviewed_state, tmp_path
    ):
        """完成稿の問題文を現行版と照合する。"""
        output = tmp_path / "完成稿.md"
        output.write_text(
            final_output_text(reviewed_state).replace(
                reviewed_state["draft"]["text"], "別の問題文"
            ),
            encoding="utf-8",
        )
        result = run_script(
            "work_state_check.py",
            "--stage",
            "final",
            "--output",
            output,
            stdin=json.dumps(reviewed_state, ensure_ascii=False),
        )
        assert result.returncode == 1
        assert "問題文が現行版と一致しない" in result.stderr

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("status", "pending", "最終出力の照合が合格していない"),
            (
                "reviewer_id",
                "別の担当者",
                "final_review.reviewer_idが監査担当と一致しない",
            ),
            (
                "output_sha256",
                "0" * 64,
                "final_review.output_sha256が完成稿と一致しない",
            ),
        ],
    )
    def test_final_requires_review_of_current_output(
        self, run_script, reviewed_state, field, value, message
    ):
        """完成稿の照合結果は監査担当と現行ファイルに対応する。"""
        reviewed_state["final_review"][field] = value
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_final_requires_review_record(self, run_script, reviewed_state):
        """照合記録がない完成稿は確定しない。"""
        del reviewed_state["final_review"]
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "final_reviewがない" in result.stderr

    def test_final_accepts_self_review_without_delegation(
        self, run_script, reviewed_state
    ):
        """委譲できない環境では自分の照合記録を使う。"""
        reviewed_state["execution"]["delegation_available"] = False
        reviewed_state["execution"]["unavailable_reason"] = "委譲機能がない"
        del reviewed_state["execution"]["agents"]
        del reviewed_state["execution"]["assignment_log"]
        reviewed_state["difficulty_review"]["reviewer_id"] = "self"
        reviewed_state["terminology_review"]["reviewer_id"] = "self"
        reviewed_state["final_review"]["reviewer_id"] = "self"
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 0

    def test_final_rejects_output_changed_after_review(
        self, run_script, reviewed_state, tmp_path
    ):
        """引用を保持していても照合後に変更した完成稿は確定しない。"""
        output = tmp_path / "完成稿.md"
        output.write_text(final_output_text(reviewed_state) + "\n", encoding="utf-8")
        result = run_script(
            "work_state_check.py",
            "--stage",
            "final",
            "--output",
            output,
            stdin=json.dumps(reviewed_state, ensure_ascii=False),
        )
        assert result.returncode == 1
        assert "final_review.output_sha256が完成稿と一致しない" in result.stderr

    def test_audit_requires_matching_assignment(self, run_script, complete_state):
        """起動時に記録した担当者と実際の担当者の不一致を監査で拒否する。"""
        complete_state["execution"]["assignment_log"]["exploration"]["agent_id"] = (
            "別の担当"
        )
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert (
            "assignment_log.exploration.agent_idが担当記録と一致しない" in result.stderr
        )

    def test_final_requires_all_checked_answers(self, run_script, reviewed_state):
        """最終入力が監査済みの別解を欠けば出力を拒否する。"""
        reviewed_state["answers"].append(
            {
                "id": "A2",
                "answer": "別解",
                "judgment": "prompt",
                "reason": "別名である",
                "evidence_ids": ["Q1"],
                "generation": "complete",
                "audit": "passed",
            }
        )
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "final_input.answer_idsが検査済みの現行項目と一致しない" in result.stderr

    @pytest.mark.parametrize("invalid_id", [{}, []])
    def test_final_rejects_nonstring_answer_id(
        self, run_script, reviewed_state, invalid_id
    ):
        """最終入力の解答IDに文字列以外を指定しても追跡表示を出さない。"""
        reviewed_state["final_input"]["answer_ids"] = [invalid_id]
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "空でない文字列ID" in result.stderr
        assert "Traceback" not in result.stderr

    def test_final_rejects_rejected_clue(self, run_script, reviewed_state):
        """棄却済みの手掛かりを最終入力で参照できないことを確認する。"""
        reviewed_state["clues"].append({"id": "C2", "status": "rejected"})
        reviewed_state["final_input"]["clue_ids"].append("C2")
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "final_input.clue_idsが検査済みの現行項目と一致しない" in result.stderr

    def test_audit_uses_only_assigned_agents(self, run_script, complete_state):
        """担当工程を同一agentへ集中させた状態を監査で拒否する。"""
        complete_state["execution"]["agents"] = dict.fromkeys(
            complete_state["execution"]["agents"], "agent-1"
        )
        result = check_state(run_script, "audit", complete_state)
        assert result.returncode == 1
        assert "工程を別々のagentへ割り当てていない" in result.stderr

    def test_finalization_agent_needed_only_for_final(
        self, run_script, complete_state, reviewed_state
    ):
        """最終化の担当は監査時には不要だが最終出力時には必要となる。"""
        for state in (complete_state, reviewed_state):
            del state["execution"]["agents"]["finalization"]
            del state["execution"]["assignment_log"]["finalization"]
        assert check_state(run_script, "audit", complete_state).returncode == 0
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "execution.agents.finalizationがない" in result.stderr

    def test_invalid_json_is_input_error(self, run_script):
        """解析できないJSONは作業状態の不合格とは異なる入力エラーとする。"""
        result = run_script(
            "work_state_check.py", "--stage", "generation", stdin="{不正"
        )
        assert result.returncode == 2
        assert "入力エラー" in result.stderr
        assert "Traceback" not in result.stderr
