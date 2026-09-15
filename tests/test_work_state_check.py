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
    roles = ("exploration", "generation", "exposure", "audit", "finalization")
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
                    "semantic_candidates": ["一般名称"],
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
def selection_state():
    """探索範囲と候補の展開が完了した状態を作る。"""
    return {
        "facet": "化学工業",
        "entry_points": [
            {"id": "E1", "kind": "分類表", "label": "産業分類"},
            {"id": "E2", "kind": "事典索引", "label": "化学事典"},
        ],
        "coverage_areas": [
            {
                "id": "D1",
                "label": "無機化学工業",
                "basis": "分類表の区分",
                "explored": True,
                "entry_point_ids": ["E1"],
            },
            {
                "id": "D2",
                "label": "有機化学工業",
                "basis": "事典の区分",
                "explored": True,
                "entry_point_ids": ["E2"],
            },
        ],
        "candidates": [
            {
                "id": "K1",
                "label": "候補1",
                "coverage_area_ids": ["D1"],
                "discovery_entry_point_ids": ["E1"],
                "disposition": "eligible",
                "expanded": True,
                "exposure_precheck": {
                    "representative_descriptions": ["対象を説明する語句"],
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
                "disposition": "eligible",
                "expanded": True,
                "exposure_precheck": {
                    "representative_descriptions": ["対象を説明する語句"],
                    "accepted_names": ["候補2"],
                    "formations": [],
                    "status": "passed",
                },
            },
        ],
        "frontier_ids": [],
        "saturated": True,
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
                "requires_target_association": False,
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


class TestSelectionState:
    """題材探索の状態を検査する。"""

    def test_complete_selection_passes(self, run_script, selection_state):
        """異種の入口と展開済み候補が揃えば探索状態が合格する。"""
        assert check_state(run_script, "selection", selection_state).returncode == 0

    def test_selection_requires_distinct_entry_kinds(self, run_script, selection_state):
        """探索入口が同じ種類だけなら探索状態を拒否する。"""
        selection_state["entry_points"][1]["kind"] = "分類表"
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
