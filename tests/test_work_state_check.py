"""作問状態の参照関係と工程別の検査を確認する。"""

import copy
import json

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
                        "text": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
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
                        "competitors": ["近接候補"],
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
                "term": "専門語",
                "reason": "入門教材で説明される",
                "evidence_ids": evidence,
                "generation": "complete",
                "audit": "passed",
            }
        ],
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
        },
    }


@pytest.fixture
def exposed_precheck():
    """代表説明から解答名を形成できる露出予備検査を作る。"""
    return {
        "representative_descriptions": ["高いエネルギー状態へ移った粒子のようなもの"],
        "accepted_names": ["励起子"],
        "formations": [
            {
                "name": "励起子",
                "formation_rule": "状態名と粒子を表す接尾要素を結ぶ",
                "components": [
                    {
                        "form": "励起",
                        "source": "分野の一般語",
                        "knowledge": "general_domain",
                    },
                    {
                        "form": "子",
                        "source": "生産的な接尾要素",
                        "knowledge": "general_domain",
                    },
                ],
                "formation_requires_target_association": False,
                "standard_name_confirmation_requires_target_association": True,
            }
        ],
        "status": "rejected",
    }


def check_state(run_script, stage, state):
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


class TestSelectionState:
    """題材探索の状態を検査する。"""

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
        """代表説明から解答名を形成できる候補を採用対象にしない。"""
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

    @pytest.mark.parametrize(
        ("description", "answer", "parts"),
        [
            (
                "土地の区画を整理する事業",
                "土地区画整理事業",
                ("土地", "区画", "整理", "事業"),
            ),
            (
                "市街地を再開発する事業",
                "市街地再開発事業",
                ("市街地", "再開発", "事業"),
            ),
        ],
    )
    def test_selection_rejects_transparent_public_project_names(
        self, run_script, selection_state, description, answer, parts
    ):
        """代表説明から名称を形成できる制度候補を拒否する。"""
        precheck = selection_state["candidates"][0]["exposure_precheck"]
        precheck.update(
            representative_descriptions=[description],
            accepted_names=[answer],
            formations=[
                {
                    "name": answer,
                    "formation_rule": "説明にある一般語を複合する",
                    "components": [
                        {
                            "form": part,
                            "source": description,
                            "knowledge": "general_language",
                        }
                        for part in parts
                    ],
                    "formation_requires_target_association": False,
                    "standard_name_confirmation_requires_target_association": True,
                }
            ],
            status="passed",
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
    def test_complete_state_passes(self, run_script, complete_state, stage):
        """各項目が完了した状態は指定工程で合格する。"""
        assert check_state(run_script, stage, complete_state).returncode == 0

    def test_clue_rejects_quasi_uniqueness_depending_on_another_clue(
        self, run_script, complete_state
    ):
        """他の手掛かりに依存する準一意性を単独の評価として認めない。"""
        check = complete_state["clues"][0]["checks"]["quasi_uniqueness"]
        check["depends_on_clue_ids"] = ["C2"]
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

    def test_generation_requires_pending_audit(self, run_script, complete_state):
        """生成工程では各項目の監査結果が未判定でなければならない。"""
        for group in ("propositions", "terms", "answers", "checks", "output_elements"):
            for item in complete_state[group]:
                item["audit"] = "pending"
        for check in complete_state["clues"][0]["checks"].values():
            check["audit"] = "pending"
        assert check_state(run_script, "generation", complete_state).returncode == 0
        complete_state["checks"][0]["audit"] = "passed"
        result = check_state(run_script, "generation", complete_state)
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

    def test_final_requires_all_checked_answers(self, run_script, complete_state):
        """最終入力が監査済みの別解を欠けば出力を拒否する。"""
        complete_state["answers"].append(
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
        result = check_state(run_script, "final", complete_state)
        assert result.returncode == 1
        assert "final_input.answer_idsが検査済みの現行項目と一致しない" in result.stderr

    @pytest.mark.parametrize("invalid_id", [{}, []])
    def test_final_rejects_nonstring_answer_id(
        self, run_script, complete_state, invalid_id
    ):
        """最終入力の解答IDに文字列以外を指定しても追跡表示を出さない。"""
        complete_state["final_input"]["answer_ids"] = [invalid_id]
        result = check_state(run_script, "final", complete_state)
        assert result.returncode == 1
        assert "空でない文字列ID" in result.stderr
        assert "Traceback" not in result.stderr

    def test_final_rejects_rejected_clue(self, run_script, complete_state):
        """棄却済みの手掛かりを最終入力で参照できないことを確認する。"""
        complete_state["clues"].append({"id": "C2", "status": "rejected"})
        complete_state["final_input"]["clue_ids"].append("C2")
        result = check_state(run_script, "final", complete_state)
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

    def test_finalization_agent_needed_only_for_final(self, run_script, complete_state):
        """最終化の担当は監査時には不要だが最終出力時には必要となる。"""
        del complete_state["execution"]["agents"]["finalization"]
        del complete_state["execution"]["assignment_log"]["finalization"]
        assert check_state(run_script, "audit", complete_state).returncode == 0
        result = check_state(run_script, "final", complete_state)
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
