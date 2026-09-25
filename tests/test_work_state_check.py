"""作問状態の参照関係と工程別の検査を確認する。"""

import copy
import hashlib
import json
import tempfile
from pathlib import Path

import pytest

REQUIRED_CHECK_IDS = {
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
OUTPUT_HEADINGS = {
    "problem": "問題",
    "answer": "解答",
    "supplement": "補足",
    "alternatives": "別解",
    "judging": "正誤判定基準",
    "topic_selection": "題材選択",
    "difficulty.beginner": "難易度",
    "difficulty.general": "難易度",
    "verification": "裏取り",
    "clues": "手掛かりの設計",
    "answer_limitation": "問題の成立性",
    "answer_exposure": "問題の成立性",
    "structure": "問題文の構成",
    "clue_order": "問題文の構成",
    "expression.naturalness": "問題文の表現",
    "expression.comprehensibility": "問題文の表現",
    "expression.accuracy": "問題文の表現",
    "expression.incremental_comprehension": "問題文の表現",
    "length": "問題文の長さ",
    "answer_judging": "解答と正誤判定",
    "references": "参考文献",
}


@pytest.fixture
def complete_state():
    """全工程を通過できる一問分の作業状態を作る。"""
    evidence = ["Q1"]
    roles = (
        "clue_search",
        "exposure_analysis",
        "name_research",
        "answer_range",
        "answer_judging",
        "writer",
        "asked_knowledge",
        "difficulty_assessment",
        "beginner_difficulty_review",
        "general_difficulty_review",
        "structure_review",
        "clue_order_review",
        "naturalness_review",
        "incremental_comprehension_review",
        "term_listing",
        "term_necessity_review",
        "term_sense_review",
        "term_audience_review",
        "exposure",
        "material_writer",
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
                    "semantic_candidates": [
                        {
                            "id": "X1",
                            "answer_id": None,
                            "name": "一般名称",
                            "formation_rule": "対象との既知の対応から名称を選ぶ",
                            "components": [
                                {
                                    "form": "一般名称",
                                    "source": "対象と名称の既知の対応",
                                    "knowledge": "answer_side",
                                    "answer_side_reason": "名称そのものを知っている必要がある",
                                }
                            ],
                            "formation_requires_answer_side_knowledge": True,
                            "standard_name_confirmation_requires_answer_side_knowledge": True,
                        }
                    ],
                    "answer_side_knowledge_required": "図形条件と名称の対応を知っている必要がある",
                }
                if check_id == "answer_exposure"
                else {}
            ),
        }
        for check_id in sorted(REQUIRED_CHECK_IDS)
    ]
    clue_check = {
        "claim": "対象を絞れる",
        "reason": "定義と比較した",
        "evidence_ids": evidence,
    }
    assignments = [
        {
            "role": role,
            "agent_id": agent,
            "artifact_refs": [f"{role}.md"],
            **({"draft_version": 2} if role == "exposure" else {}),
        }
        for role, agent in agents.items()
    ]
    assignments.extend(
        {
            "role": role,
            "agent_id": f"agent-{role}",
            "artifact_refs": [f"{role}.json"],
            "items": ["S1"],
        }
        for role in ("source_reliability", "source_reliability_review")
    )
    assignments.extend(
        {"role": role, "agent_id": f"agent-{role}", "artifact_refs": [f"{role}.json"]}
        for role in (
            "clue_centrality",
            "centrality_review",
            "familiarity_review",
            "corroboration",
            "corroboration_review",
            "certainty",
            "certainty_review",
            "proposition_extraction",
            "proposition_matching",
            "competitor_search",
            "competitor_search_review",
            "competitor_comparison",
            "competitor_comparison_review",
        )
    )
    state = {
        "selection_mode": "random",
        "facet_nodes": {
            "subject": "subject::66",
            "place": "place::ROOT",
            "time": "time::ROOT",
            "type": "type::ROOT",
        },
        "execution": {"delegation_available": True, "assignments": assignments},
        "answer_target": "ミュラー・リヤー錯視",
        "asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える",
        "answer_granularity": "錯視の名称と図形条件の対応",
        "difficulty_assessment": {
            "asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える",
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
        "source_assessments": [
            {
                "source_id": "S1",
                "level": "専門家が編集した事典で、記述の出所を確認できる",
                "clear_errors": [],
                "uses": ["fact", "usage_example"],
                "reason": "編集体制と改訂履歴を確認した",
            }
        ],
        "source_reliability_reviews": [
            {
                "source_id": "S1",
                "status": "passed",
                "reason": "編集体制と記述の出所を確かめた",
            }
        ],
        "proposition_support": [
            {
                "proposition_id": "P1",
                "evidence_ids": evidence.copy(),
                "reason": "引用が直接述べる",
                "inference_type": "direct",
            }
        ],
        "proposition_certainty": [
            {
                "proposition_id": "P1",
                "level": "複数の教材が断定しており、確定した事実として扱える",
                "reason": "入門教材と事典が同じ図形条件を述べる",
            }
        ],
        "corroboration_reviews": [
            {"proposition_id": "P1", "status": "passed", "reason": "引用が述べる"}
        ],
        "certainty_reviews": [
            {"proposition_id": "P1", "status": "passed", "reason": "断定できる"}
        ],
        "competitors": [
            {
                "id": "R1",
                "name": "近接候補",
                "clue_ids": ["C1"],
                "evidence_ids": evidence.copy(),
            }
        ],
        "competitor_comparisons": [
            {
                "clue_id": "C1",
                "competitor_id": "R1",
                "conditions": [
                    {
                        "passage": "矢羽の向きで異なる長さに見える",
                        "matches": False,
                        "reason": "引用で候補の図形条件との差を確認した",
                        "evidence_ids": evidence.copy(),
                    }
                ],
                "disposition": "excluded",
                "exclusion_passage": "矢羽の向きで異なる長さに見える",
                "reason": "手掛かりに書かれた図形条件で区別する",
            }
        ],
        "competitor_search_reviews": [
            {
                "clue_id": "C1",
                "found": [
                    {
                        "id": "R1",
                        "name": "近接候補",
                        "source_url": "https://example.org/competitor",
                        "evidence_ids": evidence.copy(),
                    }
                ],
                "status": "passed",
                "reason": "逆引きで作る側と同じ候補を見つけた",
            }
        ],
        "competitor_comparison_reviews": [
            {
                "clue_id": "C1",
                "competitor_id": "R1",
                "conditions": [
                    {
                        "passage": "矢羽の向きで異なる長さに見える",
                        "match": "不一致",
                        "reason": "候補には当てはまらない",
                    }
                ],
                "disposition": "excluded",
                "status": "passed",
                "reason": "図形条件で区別する",
            }
        ],
        "familiarity_reviews": [
            {"clue_id": "C1", "status": "passed", "reason": "入門教材で扱われる"}
        ],
        "clue_centrality": [
            {
                "clue_id": "C1",
                "claim": "錯視の図形条件は対象の定義に当たる",
                "reason": "資料が図形条件で対象を説明する",
                "evidence_ids": evidence.copy(),
            }
        ],
        "centrality_reviews": [
            {"clue_id": "C1", "status": "passed", "reason": "定義として扱われる"}
        ],
        "propositions": [
            {
                "id": "P1",
                "claim": "ミュラー・リヤー錯視では同じ長さの線分が矢羽の向きで異なる長さに見える",
            }
        ],
        "realized_propositions": [
            {
                "proposition_id": "P1",
                "draft_version": 2,
                "passage": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
            }
        ],
        "extracted_propositions": [
            {
                "id": "E1",
                "draft_version": 2,
                "claim": "この錯視では同じ長さの線分が矢羽の向きで異なる長さに見える",
                "passage": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
            }
        ],
        "proposition_matching_reviews": [
            {
                "extracted_id": "E1",
                "proposition_id": "P1",
                "strength_matches": True,
                "status": "passed",
                "reason": "断定の強さが確実性の判定と一致する",
            }
        ],
        "clues": [
            {
                "id": "C1",
                "fact": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視である",
                "proposition_ids": ["P1"],
            }
        ],
        "clue_uses": [
            {
                "clue_id": "C1",
                "status": "active",
                "text": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
                "directly_describes_target": True,
            }
        ],
        "clue_checks": [
            {
                "clue_id": "C1",
                "quasi_uniqueness": {
                    **clue_check,
                    "comparison_scope": "同じ上位分類",
                    "standalone_sufficient": True,
                    "depends_on_clue_ids": [],
                },
                "familiarity": copy.deepcopy(clue_check),
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
            }
        ],
        "structure_review": {
            "draft_version": 2,
            "question_form": "SC",
            "otoshi_clue_ids": ["C1"],
            "status": "passed",
            "reason": "核名詞句の直前にある落としが対象を直接説明する",
        },
        "clue_order_review": {
            "draft_version": 2,
            "status": "passed",
            "reason": "手掛かりが一つなので順序の問題はない",
        },
        "naturalness_review": {
            "draft_version": 2,
            "status": "passed",
            "reason": "語順と修飾関係に不自然な点がない",
        },
        "incremental_comprehension_review": {
            "draft_version": 2,
            "status": "passed",
            "reason": "前から読んで途中で解釈が変わる箇所がない",
        },
        "term_listing": {"draft_version": 2, "terms": [{"id": "T1", "term": "矢羽"}]},
        "term_necessity_reviews": [
            {
                "term_id": "T1",
                "meaning_needed": True,
                "status": "passed",
                "reason": "矢羽の意味が分からないと図形条件を理解できない",
            }
        ],
        "term_sense_reviews": [
            {
                "term_id": "T1",
                "status": "passed",
                "reason": "資料の定義と語義が一致する",
                "evidence_ids": evidence.copy(),
            }
        ],
        "term_audience_reviews": [
            {
                "term_id": "T1",
                "status": "passed",
                "reason": "想定プレイヤー層の既習事項として扱う",
                "evidence_ids": evidence.copy(),
            }
        ],
        "beginner_difficulty_review": {
            "draft_version": 2,
            "asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える",
            "source_urls_checked": ["https://example.org/beginner"],
            "adverse_finding": "図中の注記だけでないか確認した",
            "resolution_evidence_ids": evidence.copy(),
            "resolution_reason": "名称と図形条件を学習内容として説明する",
            "status": "passed",
        },
        "general_difficulty_review": {
            "draft_version": 2,
            "asked_knowledge": "図形条件からミュラー・リヤー錯視の名称を答える",
            "source_urls_checked": ["https://example.org/general"],
            "adverse_finding": "一般向け資料での紹介を確認した",
            "resolution_evidence_ids": evidence.copy(),
            "resolution_reason": "紹介の範囲を考慮して判断する",
            "status": "passed",
        },
        "answers": [
            {
                "id": "A1",
                "answer": "ミュラー・リヤー錯視",
            }
        ],
        "answer_judgments": [
            {
                "answer_id": "A1",
                "judgment": "correct",
                "reason": "標準名称である",
                "evidence_ids": evidence.copy(),
            }
        ],
        "names": [
            {
                "id": "N1",
                "name": "ミュラー・リヤー錯視",
                "usage": "教材が錯視の標準名称として使う",
                "evidence_ids": evidence.copy(),
            }
        ],
        "blind_candidates": [],
        "exposure_analysis": [
            {
                "candidate_id": "X1",
                "name": "一般名称",
                "formation_rule": "対象との既知の対応から名称を選ぶ",
                "components": [
                    {
                        "form": "一般名称",
                        "source": "対象と名称の既知の対応",
                        "knowledge": "answer_side",
                        "answer_side_reason": "名称そのものを知っている必要がある",
                    }
                ],
                "formation_requires_answer_side_knowledge": True,
                "standard_name_confirmation_requires_answer_side_knowledge": True,
                "status": "passed",
                "reason": "名称を作るには解答側の知識が要る",
            }
        ],
        "answer_review": {
            "draft_version": 2,
            "answers": [
                {
                    "id": "A1",
                    "judgment": "correct",
                    "status": "passed",
                    "same_target": True,
                    "specified_enough": True,
                    "clear_error": False,
                    "scope_matches": True,
                    "reason": "対象の標準名称を十分に指定する",
                    "evidence_ids": evidence.copy(),
                }
            ],
            "candidate_reviews": [
                {
                    "candidate_id": "X1",
                    "judgment": "incorrect",
                    "status": "passed",
                    "same_target": False,
                    "specified_enough": True,
                    "clear_error": False,
                    "scope_matches": False,
                    "reason": "対象の名称ではない",
                    "evidence_ids": evidence.copy(),
                }
            ],
        },
        "checks": checks,
        "relative_clauses": [
            {
                "passage": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視",
                "relation": "outer",
                "reason": "線分が異なる長さに見える現象と錯視名との関係を補う",
                "relation_proposition_ids": ["P1"],
            }
        ],
        "final_input": {
            "draft_version": 2,
            "topic_selection": {
                "answer_target": "ミュラー・リヤー錯視",
                "facet_nodes": {
                    "subject": "subject::66",
                    "place": "place::ROOT",
                    "time": "time::ROOT",
                    "type": "type::ROOT",
                },
                "facet_paths": {
                    "subject": "科学 ＞ 心理学",
                    "place": "地域指定なし",
                    "time": "時代指定なし",
                    "type": "錯視",
                },
                "history_result": "履歴補正を適用した",
            },
            "proposition_ids": ["P1"],
            "clue_ids": ["C1"],
            "term_ids": ["T1"],
            "answer_ids": ["A1"],
            "quote_ids": ["Q1"],
        },
    }
    state["final_input"]["material"] = {
        "topic_selection": "科学 ＞ 心理学／地域指定なし／時代指定なし／錯視から、"
        "履歴補正を適用した結果、ミュラー・リヤー錯視を選んだ。"
    }
    sections = final_output_sections(state)
    state["final_input"]["material"] = {
        output_id: sections[heading] for output_id, heading in OUTPUT_HEADINGS.items()
    }
    return state


def final_output_sections(state):
    """完成稿の各節に必要な本文を作る。"""
    quote_texts = "\n\n".join(
        f"> {quote['text']}"
        for source in state["sources"]
        for quote in source["quotes"]
        if quote["id"] in state["final_input"]["quote_ids"]
    )
    return {
        "問題": state["draft"]["text"],
        "解答": state["answer_target"],
        "補足": "なし",
        "別解": "なし",
        "正誤判定基準": "正答の扱いを示す。",
        "題材選択": state["final_input"]["material"]["topic_selection"],
        "難易度": "資料名の第一節では、入門教材での扱いを確認できる。",
        "裏取り": f"資料名（第一節）に次の記述がある。\n\n{quote_texts}",
        "手掛かりの設計": "資料名の第一節にある図形条件を手掛かりに使う。",
        "問題の成立性": "資料名（第一節）の図形条件によって対象を限定する。",
        "問題文の構成": "SC型である。",
        "問題文の表現": "同じ長さの線分が矢羽の向きで異なる長さに見える錯視という箇所を、資料名の第一節にある説明と照合する。",
        "問題文の長さ": "文字数を確認した。",
        "解答と正誤判定": "資料名（第一節）の解答対象の名称を正答とする。",
        "参考文献": "資料名（第一節）。",
    }


FINAL_REVIEW_ROLES = ("final_reflection_review", "final_contamination_review")


def set_reviewed_output(state, text):
    """完成稿の照合結果と照合担当の起動の記録を、指定した完成稿に対応させる。"""
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    for role in FINAL_REVIEW_ROLES:
        state[role]["output_sha256"] = digest
        assignment_of(state, role)["output_sha256"] = digest


def final_output_text(state):
    """最終段階の構造検査に使う完成稿本文を組み立てる。"""
    return "\n\n".join(
        f"## {heading}\n\n{body}"
        for heading, body in final_output_sections(state).items()
    )


def refresh_material_quotes(state):
    """採用引用を変更したテストの最終入力も同じ資料に揃える。"""
    adopted = set(state["final_input"]["quote_ids"])
    state["final_input"]["material"]["verification"] = "\n\n".join(
        f"{source['citation']}（{quote['location']}）\n> {quote['text']}"
        for source in state["sources"]
        for quote in source["quotes"]
        if quote["id"] in adopted
    )


def add_source(state, source):
    """資料を加え、その信頼性の評価、検査、担当の受け持ちも加える。"""
    state["sources"].append(source)
    state["source_assessments"].append(
        {
            "source_id": source["id"],
            "level": f"{source['citation']}の編集体制を確認できる",
            "clear_errors": [],
            "uses": ["fact"],
            "reason": f"{source['citation']}の作成主体を確認した",
        }
    )
    state.setdefault("source_reliability_reviews", []).append(
        {"source_id": source["id"], "status": "passed", "reason": "評価を確かめた"}
    )
    for item in state["execution"]["assignments"]:
        if item["role"] in {"source_reliability", "source_reliability_review"}:
            item["items"] = [*item["items"], source["id"]]


def drop_assignment(state, role):
    """起動の記録から、指定した役割の担当を除く。"""
    state["execution"]["assignments"] = [
        item for item in state["execution"]["assignments"] if item["role"] != role
    ]


def assignment_of(state, role):
    """起動の記録から、指定した役割の担当を返す。"""
    return next(
        item for item in state["execution"]["assignments"] if item["role"] == role
    )


def drop_from_weights(state, candidate_id):
    """抽選の対象から外れた候補を、まとまりとweightから除く。"""
    groups = []
    for group in state["topic_groups"]:
        group["candidate_ids"] = [
            item for item in group["candidate_ids"] if item != candidate_id
        ]
        if group["candidate_ids"]:
            groups.append(group)
    state["topic_groups"] = groups
    kept = {group["id"] for group in groups}
    state["group_weights"] = [
        item for item in state["group_weights"] if item["group_id"] in kept
    ]
    if len(groups) == 1:
        del state["group_weights"]
    state["candidate_weights"] = [
        item
        for item in state["candidate_weights"]
        if item["candidate_id"] != candidate_id
    ]
    state["topic_group_reviews"] = [
        item for item in state["topic_group_reviews"] if item["group_id"] in kept
    ]
    state["topic_weight_reviews"] = [
        item
        for item in state["topic_weight_reviews"]
        if item["target"] in kept or (item["target"] == "groups" and len(groups) > 1)
    ]


@pytest.fixture
def writing_state(complete_state):
    """検査のステップを完了する前の一問分の作業状態を作る。"""
    state = copy.deepcopy(complete_state)
    for group in ("beginner", "general"):
        del state[f"{group}_difficulty_review"]
        drop_assignment(state, f"{group}_difficulty_review")
    return state


@pytest.fixture
def reviewed_state(complete_state):
    """完成稿を二つの照合担当が照合した最終段階の作業状態を作る。"""
    state = copy.deepcopy(complete_state)
    state["final_reflection_review"] = {
        "status": "passed",
        "reason": "各節の本文と引用が限定入力と一致する",
        "quote_ids": state["final_input"]["quote_ids"].copy(),
        "answer_ids": state["final_input"]["answer_ids"].copy(),
        "clue_ids": state["final_input"]["clue_ids"].copy(),
    }
    state["final_contamination_review"] = {
        "status": "passed",
        "reason": "検索過程や担当IDなどの作業用記録がない",
    }
    state["execution"]["assignments"].extend(
        {"role": role, "agent_id": f"agent-{role}", "artifact_refs": [f"{role}.json"]}
        for role in FINAL_REVIEW_ROLES
    )
    set_reviewed_output(state, final_output_text(state))
    return state


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


class TestFacetSubdivision:
    """subjectのカタログの最下層より下の細分を検査する。"""

    def test_valid_subdivision_passes(self, run_script, subdivided_facet_state):
        """最下層を区分に分け、区分をさらに分けた状態を受け付ける。"""
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 0

    def test_leaf_requires_subdivision(self, run_script, subdivided_facet_state):
        """細分の記録なしに最下層から子へ進まない。"""
        subdivided_facet_state["facet_subdivisions"].pop()
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "で細分せずに最下層から子へ進んでいる" in result.stderr

    @pytest.mark.parametrize("parent", ["subject::33", "place::ROOT"])
    def test_parent_must_be_subject_leaf(
        self, run_script, subdivided_facet_state, parent
    ):
        """カタログに子があるノードやsubject以外の軸は細分しない。"""
        subdivided_facet_state["facet_subdivisions"].append(
            {**subdivided_facet_state["facet_subdivisions"][0], "parent": parent}
        )
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "parentがsubjectの最下層でも細分した区分でもない" in result.stderr

    def test_asterisk_parent_continues_with_dot(
        self, state_module, subdivided_facet_state
    ):
        """すでに`*`を含むノードを分けた区分は、`.`と番号で続ける。"""
        record = subdivided_facet_state["facet_subdivisions"][0]
        record["parent"] = "subject::630*0"
        for position, child in enumerate(record["children"], 1):
            child["key"] = f"subject::630*0.{position}"
        state = {"facet_subdivisions": [record]}
        assert "subject::630*0" in state_module.validate_facet_subdivisions(state)

    def test_child_key_must_not_be_catalog_node(
        self, state_module, subdivided_facet_state, monkeypatch
    ):
        """区分のキーはカタログのノードと重ならない。"""
        find_block = state_module.facet_node.find_block
        monkeypatch.setattr(
            state_module.facet_node,
            "find_block",
            lambda key: (None, [key]) if key == "subject::338*1" else find_block(key),
        )
        state = {"facet_subdivisions": subdivided_facet_state["facet_subdivisions"]}
        with pytest.raises(
            state_module.StateError, match="カタログのノードと重なっている"
        ):
            state_module.validate_facet_subdivisions(state)

    def test_child_keys_follow_parent(self, run_script, subdivided_facet_state):
        """区分のキーは親のキーに連番を付けた形にする。"""
        subdivided_facet_state["facet_subdivisions"][0]["children"][0]["key"] = "景気"
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "keyがsubject::338*1ではない" in result.stderr

    @pytest.mark.parametrize("field", ["characteristic", "basis"])
    def test_requires_characteristic_and_basis(
        self, run_script, subdivided_facet_state, field
    ):
        """区分の原理と根拠を記録する。"""
        del subdivided_facet_state["facet_subdivisions"][0][field]
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert f"facet_subdivisions[0].{field}がない" in result.stderr

    def test_requires_source_url(self, run_script, subdivided_facet_state):
        """区分の根拠にした資料をURLで示す。"""
        subdivided_facet_state["facet_subdivisions"][0]["source_urls"] = ["教科書"]
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "source_urlsにURLでない値がある" in result.stderr

    def test_requires_scope_of_each_child(self, run_script, subdivided_facet_state):
        """区分ごとに入る対象の範囲を記す。"""
        del subdivided_facet_state["facet_subdivisions"][0]["children"][1]["scope"]
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "children[1].scopeがない" in result.stderr

    def test_requires_two_children(self, run_script, subdivided_facet_state):
        """一つの区分だけの細分を認めない。"""
        children = subdivided_facet_state["facet_subdivisions"][0]["children"]
        del children[1:]
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "childrenが二つに満たない" in result.stderr

    def test_rejects_unused_subdivision(
        self, run_script, facet_state, subdivided_facet_state
    ):
        """子へ進んでいないノードの細分を残さない。"""
        facet_state["facet_subdivisions"] = subdivided_facet_state[
            "facet_subdivisions"
        ][:1]
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "子へ進んでいないノードの細分がある" in result.stderr

    def test_rejects_history_distance_of_child(
        self, run_script, subdivided_facet_state
    ):
        """細分した区分には履歴補正を掛けない。"""
        candidate = subdivided_facet_state["facet_weights"][-1]["candidates"][0]
        candidate["history_distances"] = [1]
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "history_distancesが細分した区分にある" in result.stderr

    def test_requires_passed_subdivision_review(
        self, run_script, subdivided_facet_state
    ):
        """区分の分け方は検査担当の合格を要する。"""
        subdivided_facet_state["facet_subdivision_reviews"][1].update(
            status="failed", fix_data=["facet_subdivisions"]
        )
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "facet_subdivision_reviewsに不合格の項目がある" in result.stderr

    def test_requires_subdivision_reviewer(self, run_script, subdivided_facet_state):
        """細分した場合は細分の検査担当の起動を記録する。"""
        drop_assignment(subdivided_facet_state, "facet_subdivision_review")
        result = check_state(run_script, "facet-selection", subdivided_facet_state)
        assert result.returncode == 1
        assert "担当の記録がない: ['facet_subdivision_review']" in result.stderr

    def test_intersection_accepts_subdivided_node(
        self, run_script, intersection_state, subdivided_facet_state
    ):
        """細分の記録を写した交差領域の確認記録は、区分を選択ノードとして受け付ける。"""
        intersection_state["facet_nodes"] = subdivided_facet_state["facet_nodes"]
        intersection_state["facet_subdivisions"] = subdivided_facet_state[
            "facet_subdivisions"
        ]
        result = check_state(run_script, "intersection-checkpoint", intersection_state)
        assert result.returncode == 0
        del intersection_state["facet_subdivisions"]
        result = check_state(run_script, "intersection-checkpoint", intersection_state)
        assert result.returncode == 1
        assert "facet_nodes.subjectがカタログにも細分にも存在しない" in result.stderr


class TestFacetSelectionState:
    """ファセットの各階層の判断、weight、抽選結果を検査する。"""

    def test_valid_state_passes(self, run_script, facet_state):
        """停止まで一続きに記録した状態を受け付ける。"""
        assert check_state(run_script, "facet-selection", facet_state).returncode == 0

    def test_weights_must_cover_all_children(self, run_script, facet_state):
        """兄弟ノードの一部だけにweightを付けた状態を拒否する。"""
        facet_state["facet_weights"][0]["candidates"].pop()
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "subject::ROOTの直接の子と一致しない" in result.stderr

    @pytest.mark.parametrize("viewpoint", ["sharing", "communication", "background"])
    def test_weights_require_each_viewpoint(self, run_script, facet_state, viewpoint):
        """候補ごとに三観点の評価をそれぞれ要求する。"""
        del facet_state["facet_weights"][0]["candidates"][0]["viewpoints"][viewpoint]
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert f"viewpoints.{viewpoint}がない" in result.stderr

    def test_pick_must_have_positive_weight(self, run_script, facet_state):
        """weight 0の候補を抽選結果にしない。"""
        chosen = facet_state["facet_picks"][0]["key"]
        for candidate in facet_state["facet_weights"][0]["candidates"]:
            if candidate["key"] == chosen:
                candidate["weight"] = 0
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "正のweightを持つ候補ではない" in result.stderr

    def test_next_level_must_follow_pick(self, run_script, facet_state):
        """抽選結果と異なるノードから次の階層を始めない。"""
        facet_state["facet_picks"][0]["key"] = "subject::7"
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "前の階層の抽選結果から続いていない" in result.stderr

    def test_nodes_must_match_stopped_levels(self, run_script, facet_state):
        """選択したノードは停止した階層のノードと一致させる。"""
        facet_state["facet_nodes"]["subject"] = "subject::6"
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "facet_nodes.subjectが停止した階層のノードと一致しない" in result.stderr

    def test_all_axes_must_stop(self, run_script, facet_state):
        """4軸すべてで停止するまで記録する。"""
        facet_state["facet_levels"].pop()
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "4軸すべての粒度判断が停止まで記録されていない" in result.stderr

    def test_keeps_failed_review_of_removed_level(self, run_script, facet_state):
        """修正で取り除いた階層の不合格の記録が残っていても受け付ける。"""
        facet_state["facet_level_reviews"].insert(
            0,
            {
                "level_id": "F9",
                "status": "failed",
                "reason": "この階層で子へ進む理由がない",
                "fix_data": ["facet_levels"],
            },
        )
        assert check_state(run_script, "facet-selection", facet_state).returncode == 0

    @pytest.mark.parametrize(
        "key",
        ["facet_level_reviews", "facet_weight_reviews", "facet_distribution_reviews"],
    )
    def test_requires_passed_review(self, run_script, facet_state, key):
        """各階層の判断とweightは検査担当の合格を要する。"""
        facet_state[key][0].update(status="failed", fix_data=["facet_levels"])
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert f"{key}に不合格の項目がある" in result.stderr

    def test_later_review_replaces_failed_one(self, run_script, facet_state):
        """反論を新しい検査担当が再検査して合格した記録を認める。"""
        review = dict(facet_state["facet_level_reviews"][0])
        facet_state["facet_level_reviews"][0].update(
            status="failed", fix_data=["facet_levels"]
        )
        facet_state["facet_level_reviews"].append(review)
        assert check_state(run_script, "facet-selection", facet_state).returncode == 0

    def test_failed_review_requires_fix_target(self, run_script, facet_state):
        """不合格の判定には、修正が必要な入力を担当表のデータで示す。"""
        facet_state["facet_level_reviews"][0]["status"] = "failed"
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert (
            "facet_level_reviews[0].fix_dataは配列でなければならない" in result.stderr
        )
        facet_state["facet_level_reviews"][0]["fix_data"] = ["unknown"]
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "fix_dataが担当表にないデータを参照している" in result.stderr

    def test_requires_review_of_every_level(self, run_script, facet_state):
        """検査のない階層を残さない。"""
        facet_state["facet_level_reviews"].pop()
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "facet_level_reviewsに検査のない項目がある: ['F6']" in result.stderr

    def test_requires_weighting_assignment(self, run_script, facet_state):
        """weightを推定した担当の起動の記録を要求する。"""
        drop_assignment(facet_state, "facet_weighting")
        result = check_state(run_script, "facet-selection", facet_state)
        assert result.returncode == 1
        assert "担当の記録がない: ['facet_weighting']" in result.stderr


class TestIntersectionState:
    """題材探索前の4軸の交差領域の記録を検査する。"""

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

    def test_delegated_review_requires_assignment(self, run_script, intersection_state):
        """別agentによる確認では起動の記録を必須とする。"""
        drop_assignment(intersection_state, "intersection")
        result = check_state(run_script, "intersection-checkpoint", intersection_state)
        assert result.returncode == 1
        assert "execution.assignmentsが空である" in result.stderr

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("role", "parent", "roleが担当表にない"),
            ("artifact_refs", [], "artifact_refsが空である"),
        ],
    )
    def test_assignment_requires_known_role_and_artifact(
        self, run_script, intersection_state, field, value, message
    ):
        """起動の記録は担当表の役割と成果物の場所を持つ。"""
        assignment_of(intersection_state, "intersection")[field] = value
        result = check_state(run_script, "intersection-checkpoint", intersection_state)
        assert result.returncode == 1
        assert message in result.stderr

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
        """成立を確認していない4軸の交差領域を題材探索へ進めない。"""
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

    def test_discovery_progress_accepts_unstarted_area(
        self, run_script, selection_state
    ):
        """探索を始めていない下位領域が残っていても途中検査できる。"""
        area = selection_state["coverage_areas"][1]
        for key in ("explored", "entry_point_ids", "source_searches"):
            del area[key]
        selection_state["candidates"] = selection_state["candidates"][:1]
        selection_state["candidates"][0]["expansion_searches"] = []
        assert (
            check_state(run_script, "discovery-progress", selection_state).returncode
            == 0
        )
        result = check_state(run_script, "discovery", selection_state)
        assert result.returncode == 1
        assert "coverage_areas.D2が未探索である" in result.stderr

    def test_discovery_progress_requires_searches_of_started_area(
        self, run_script, selection_state
    ):
        """入口を記録した下位領域には探索記録を求める。"""
        del selection_state["coverage_areas"][1]["source_searches"]
        result = check_state(run_script, "discovery-progress", selection_state)
        assert result.returncode == 1
        assert "coverage_areas.D2.source_searches" in result.stderr

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

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("core_candidate_ids", [], "core_check.core_candidate_idsが空である"),
            ("added_candidate_ids", ["K9"], "存在しないIDを参照している"),
            ("reason", "", "core_check.reasonがない"),
        ],
    )
    def test_saturation_requires_core_object_check(
        self, run_script, selection_state, field, value, message
    ):
        """反証調査では中核級の対象が台帳にあるかを確かめた記録を要する。"""
        selection_state["saturation_challenge"]["core_check"][field] = value
        result = check_state(run_script, "discovery", selection_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_every_area_needs_exploration_assignment(self, run_script, selection_state):
        """下位領域ごとに題材探索担当を割り当てる。"""
        selection_state["execution"]["assignments"] = [
            item
            for item in selection_state["execution"]["assignments"]
            if item.get("items") != ["D2"]
        ]
        result = check_state(run_script, "discovery", selection_state)
        assert result.returncode == 1
        assert "explorationの担当に割り当てていない項目がある: ['D2']" in result.stderr

    def test_every_eligible_candidate_needs_nearby_assignment(
        self, run_script, selection_state
    ):
        """選択対象の候補ごとに近接探索担当を割り当てる。"""
        assignment_of(selection_state, "nearby_exploration")["items"] = ["K1"]
        result = check_state(run_script, "discovery", selection_state)
        assert result.returncode == 1
        assert (
            "nearby_explorationの担当に割り当てていない項目がある: ['K2']"
            in result.stderr
        )

    @pytest.mark.parametrize(
        ("role", "items", "message"),
        [
            ("exploration", ["D1", "D2"], "itemsが担当表の件数を超えている"),
            ("saturation_review", ["D1"], "項目で分割しない担当である"),
        ],
    )
    def test_assignment_items_follow_table(
        self, run_script, selection_state, role, items, message
    ):
        """起動の記録の項目は担当表の分割に従う。"""
        assignment_of(selection_state, role)["items"] = items
        result = check_state(run_script, "discovery", selection_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_selection_requires_candidate_source_link(
        self, run_script, selection_state
    ):
        """完成した探索台帳でも候補と発見元の対応を検査する。"""
        selection_state["candidates"][0]["discovery_entry_point_ids"] = ["E2"]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "発見元・下位領域" in result.stderr

    def test_selection_rejects_extra_unlinked_source(self, run_script, selection_state):
        """正しい発見元が一つあっても根拠のない追加入口を拒否する。"""
        selection_state["candidates"][0]["discovery_entry_point_ids"].append("E2")
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "発見元・下位領域" in result.stderr

    def test_selection_requires_intersection_review(self, run_script, selection_state):
        """4軸の交差領域の確認を省いた探索状態を拒否する。"""
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
        """露出予備検査の前に題材探索と所属判定だけを検査できる。"""
        del selection_state["exposure_prechecks"]
        assert check_state(run_script, "discovery", selection_state).returncode == 0
        assert check_state(run_script, "membership", selection_state).returncode == 0
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_precheck_of_every_member(
        self, run_script, selection_state
    ):
        """所属する選択対象ごとに露出の予備検査を要求する。"""
        selection_state["exposure_prechecks"].pop()
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "予備検査のない候補がある: ['K2']" in result.stderr

    def test_groups_must_cover_pickable_candidates_once(
        self, run_script, selection_state
    ):
        """まとまりは抽選の対象の候補を一度ずつ含む。"""
        selection_state["topic_groups"][1]["candidate_ids"] = ["K1"]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "topic_groupsが抽選の対象の候補を一度ずつ含んでいない" in result.stderr

    def test_several_groups_need_group_weights(self, run_script, selection_state):
        """まとまりが複数あれば、まとまり同士のweightを要する。"""
        del selection_state["group_weights"]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "group_weightsが空である" in result.stderr

    def test_candidate_weight_must_be_positive(self, run_script, selection_state):
        """抽選の対象の候補には正のweightを付ける。"""
        selection_state["candidate_weights"][0]["weight"] = 0
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "candidate_weights[0].weightが正の数ではない" in result.stderr

    @pytest.mark.parametrize(
        ("key", "index", "message"),
        [
            (
                "topic_group_reviews",
                0,
                "topic_group_reviewsに不合格の項目がある: ['G1']",
            ),
            (
                "topic_weight_reviews",
                2,
                "topic_weight_reviewsに不合格の項目がある: ['groups']",
            ),
            (
                "topic_distribution_reviews",
                0,
                "topic_distribution_reviewsに不合格の項目がある: ['all']",
            ),
        ],
    )
    def test_grouping_and_weights_require_passed_reviews(
        self, run_script, selection_state, key, index, message
    ):
        """まとまりの切り方とweightは検査担当の合格を要する。"""
        selection_state[key][index].update(status="failed", fix_data=["topic_groups"])
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_every_group_needs_weighting_assignment(self, run_script, selection_state):
        """まとまりごとに、まとまりの中のweight担当を割り当てる。"""
        selection_state["execution"]["assignments"] = [
            item
            for item in selection_state["execution"]["assignments"]
            if item.get("items") != ["G2"]
        ]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert (
            "topic_weightingの担当に割り当てていない項目がある: ['G2']" in result.stderr
        )

    def test_excluded_candidate_requires_passed_review(
        self, run_script, selection_state
    ):
        """予備検査で除外した候補は、別の担当の検査に合格して除外する。"""
        selection_state["exposure_prechecks"][1]["result"] = "exclude"
        drop_from_weights(selection_state, "K2")
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "exposure_precheck_reviewsは配列でなければならない" in result.stderr
        selection_state["exposure_precheck_reviews"] = [
            {"candidate_id": "K2", "status": "passed", "reason": "どの説明でも露出する"}
        ]
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert "担当の記録がない: ['exposure_precheck_review']" in result.stderr
        selection_state["execution"]["assignments"].append(
            {
                "role": "exposure_precheck_review",
                "agent_id": "agent-precheck-review",
                "artifact_refs": ["exposure_precheck_review.json"],
            }
        )
        assert check_state(run_script, "selection", selection_state).returncode == 0

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [("result", "unclear", "resultが不正である"), ("reason", "", "reasonがない")],
    )
    def test_precheck_requires_result_and_reason(
        self, run_script, selection_state, field, value, message
    ):
        """予備検査は残すか除外するかと、その理由を記録する。"""
        selection_state["exposure_prechecks"][0][field] = value
        result = check_state(run_script, "selection", selection_state)
        assert result.returncode == 1
        assert message in result.stderr

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

    def test_membership_requires_every_candidate(self, run_script, selection_state):
        """所属判定のない選択対象を残さない。"""
        selection_state["memberships"].pop()
        result = check_state(run_script, "membership", selection_state)
        assert result.returncode == 1
        assert "所属判定のない候補がある: ['K2']" in result.stderr

    @pytest.mark.parametrize("field", ["belongs", "reason"])
    def test_membership_requires_each_axis(self, run_script, selection_state, field):
        """4軸それぞれについて所属と理由を記録する。"""
        del selection_state["memberships"][0]["axes"]["time"][field]
        result = check_state(run_script, "membership", selection_state)
        assert result.returncode == 1
        assert f"memberships[0].axes.time.{field}" in result.stderr

    def test_membership_requires_passed_review(self, run_script, selection_state):
        """所属判定は検査担当の合格を要する。"""
        selection_state["membership_reviews"][1].update(
            status="failed", fix_data=["memberships"]
        )
        result = check_state(run_script, "membership", selection_state)
        assert result.returncode == 1
        assert "membership_reviewsに不合格の項目がある: ['K2']" in result.stderr

    def test_membership_is_not_required_at_discovery(self, run_script, selection_state):
        """探索の段階では所属判定を要求しない。"""
        del selection_state["memberships"]
        del selection_state["membership_reviews"]
        assert check_state(run_script, "discovery", selection_state).returncode == 0

    def test_selection_requires_independent_review(self, run_script, selection_state):
        """別経路の探索が欠けた下位領域を拒否する。"""
        selection_state["independent_review"].pop()
        assert check_state(run_script, "selection", selection_state).returncode == 1

    def test_selection_requires_processed_challenge(self, run_script, selection_state):
        """反証調査で得た候補を未処理のまま抽選させない。"""
        selection_state["saturation_challenge"]["resolved"] = False
        assert check_state(run_script, "selection", selection_state).returncode == 1

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
        drop_from_weights(selection_state, "K1")
        assert check_state(run_script, "discovery", selection_state).returncode == 0
        assert check_state(run_script, "selection", selection_state).returncode == 0


PREJUDGMENT_KEYS = (
    "prejudgment_scope",
    "prejudgment_membership",
    "prejudgment_difficulty",
    "prejudgment_otoshi",
)


def add_prejudgments(state, candidate_id, excluded=()):
    """抽選した候補について、四つの予備判定と担当の起動の記録を加える。"""
    for key in PREJUDGMENT_KEYS:
        state.setdefault(key, []).append(
            {
                "candidate_id": candidate_id,
                "result": "exclude" if key in excluded else "pass",
                "reason": f"{candidate_id}について{key}の観点から判定した",
            }
        )
        if not any(item["role"] == key for item in state["execution"]["assignments"]):
            state["execution"]["assignments"].append(
                {
                    "role": key,
                    "agent_id": f"agent-{key}",
                    "artifact_refs": [f"{key}.json"],
                }
            )


class TestPrejudgmentState:
    """抽選後の四つの予備判定を検査する。"""

    def test_all_passed_candidate_proceeds(self, run_script, selection_state):
        """四つの予備判定に合格した候補が一つあれば作問へ進める。"""
        add_prejudgments(selection_state, "K1")
        assert check_state(run_script, "prejudgment", selection_state).returncode == 0

    def test_each_aspect_is_required(self, run_script, selection_state):
        """四つの観点それぞれの予備判定を要求する。"""
        add_prejudgments(selection_state, "K1")
        selection_state["prejudgment_otoshi"] = [
            {"candidate_id": "K2", "result": "pass", "reason": "落としを作れる"}
        ]
        result = check_state(run_script, "prejudgment", selection_state)
        assert result.returncode == 1
        assert "K1の予備判定がない: ['prejudgment_otoshi']" in result.stderr

    def test_exclusion_is_recorded_before_repick(self, run_script, selection_state):
        """除外した候補は品質棄却を記録し、再抽選した候補の判定へ進む。"""
        add_prejudgments(selection_state, "K1", excluded={"prejudgment_membership"})
        result = check_state(run_script, "prejudgment", selection_state)
        assert result.returncode == 1
        assert "candidates.K1に予備判定の除外を記録していない" in result.stderr
        selection_state["candidates"][0]["quality_rejection_reason"] = "記号である"
        result = check_state(run_script, "prejudgment", selection_state)
        assert result.returncode == 1
        assert "作問へ進む候補が一つではない: []" in result.stderr
        add_prejudgments(selection_state, "K2")
        assert check_state(run_script, "prejudgment", selection_state).returncode == 0


class TestWorkState:
    """解答対象を決めた後の作業状態を検査する。"""

    @pytest.mark.parametrize(
        ("key", "message"),
        [
            ("proposition_support", "裏取りの記録のない命題がある: ['P1']"),
            ("proposition_certainty", "確実性の判定のない命題がある: ['P1']"),
        ],
    )
    def test_active_proposition_needs_support_and_certainty(
        self, run_script, writing_state, key, message
    ):
        """採用中の命題ごとに裏取りと確実性の判定を要する。"""
        writing_state[key][0]["proposition_id"] = "P9"
        result = check_state(run_script, "writing", writing_state)
        assert result.returncode == 1
        assert message in result.stderr

    @pytest.mark.parametrize("key", ["corroboration_reviews", "certainty_reviews"])
    def test_proposition_judgments_require_passed_review(
        self, run_script, complete_state, key
    ):
        """裏取りと確実性の判定は、それぞれ検査担当の合格を要する。"""
        complete_state[key][0].update(status="failed", fix_data=["proposition_support"])
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"{key}に不合格の項目がある: ['P1']" in result.stderr

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("proposition_id", None, "proposition_idが採用中の命題を参照していない"),
            ("strength_matches", False, "断定の強さが確実性と一致していない"),
        ],
    )
    def test_extracted_propositions_must_match(
        self, run_script, complete_state, field, value, message
    ):
        """問題文から取り出した命題は、裏取り済みの命題と断定の強さまで一致させる。"""
        complete_state["proposition_matching_reviews"][0][field] = value
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_every_proposition_needs_extracted_match(self, run_script, complete_state):
        """問題文から取り出した命題に対応しない採用命題を残さない。"""
        complete_state["propositions"].append(
            {"id": "P2", "claim": "矢羽は線分の端に付く"}
        )
        complete_state["realized_propositions"].append(
            {"proposition_id": "P2", "draft_version": 2, "passage": "矢羽"}
        )
        for key in ("proposition_support", "proposition_certainty"):
            complete_state[key].append(
                {**complete_state[key][0], "proposition_id": "P2"}
            )
        for key in ("corroboration_reviews", "certainty_reviews"):
            complete_state[key].append(
                {**complete_state[key][0], "proposition_id": "P2"}
            )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "対応しない命題がある: ['P2']" in result.stderr

    def test_active_clue_needs_centrality(self, run_script, writing_state):
        """採用中の手掛かりごとに中核性の評価を要する。"""
        writing_state["clue_centrality"][0]["clue_id"] = "C9"
        result = check_state(run_script, "writing", writing_state)
        assert result.returncode == 1
        assert "clue_centrality[0].clue_idが手掛かりにない" in result.stderr

    @pytest.mark.parametrize(
        "key",
        [
            "structure_review",
            "clue_order_review",
            "naturalness_review",
            "incremental_comprehension_review",
        ],
    )
    def test_expression_requires_passed_review(self, run_script, complete_state, key):
        """構造、順序、自然さ、理解しやすさは、それぞれ検査担当の合格を要する。"""
        complete_state[key]["status"] = "failed"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"{key}が合格していない" in result.stderr

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("question_form", "OV", "question_formが作る側の区分と一致しない"),
            ("otoshi_clue_ids", [], "otoshi_clue_idsが空である"),
        ],
    )
    def test_structure_review_must_agree_with_writer(
        self, run_script, complete_state, field, value, message
    ):
        """独立に取り出した構文型と落としが作る側の区分と食い違えば合格させない。"""
        complete_state["structure_review"][field] = value
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_familiarity_requires_passed_review(self, run_script, complete_state):
        """各手掛かりの知名度は検査担当の合格を要する。"""
        complete_state["familiarity_reviews"][0].update(
            status="failed", fix_data=["clues"]
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "familiarity_reviewsに不合格の項目がある: ['C1']" in result.stderr

    def test_centrality_requires_passed_review(self, run_script, complete_state):
        """中核性の評価は検査担当の合格を要する。"""
        complete_state["centrality_reviews"][0].update(
            status="failed", fix_data=["clue_centrality"]
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "centrality_reviewsに不合格の項目がある: ['C1']" in result.stderr

    def test_every_source_needs_assessment(self, run_script, writing_state):
        """資料ごとに信頼性の評価を要する。"""
        writing_state["source_assessments"] = []
        result = check_state(run_script, "writing", writing_state)
        assert result.returncode == 1
        assert "source_assessmentsが空である" in result.stderr

    def test_usage_only_source_cannot_support_proposition(
        self, run_script, writing_state
    ):
        """用例にしか使えない資料の引用を命題の根拠にしない。"""
        writing_state["source_assessments"][0]["uses"] = ["usage_example"]
        result = check_state(run_script, "writing", writing_state)
        assert result.returncode == 1
        assert "事実の根拠に使えない資料の引用を根拠にしている: ['Q1']" in result.stderr

    def test_source_assessment_requires_passed_review(self, run_script, complete_state):
        """資料の信頼性の評価は検査担当の合格を要する。"""
        complete_state["source_reliability_reviews"][0].update(
            status="failed", fix_data=["source_assessments"]
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "source_reliability_reviewsに不合格の項目がある: ['S1']" in result.stderr

    def test_writing_start_accepts_target_state(self, run_script, complete_state):
        """作文担当の起動後に解答対象だけの状態を検査できる。"""
        assert check_state(run_script, "target-start", complete_state).returncode == 0

    def test_writing_start_rejects_selection_ledger(self, run_script, complete_state):
        """題材探索の台帳を解答対象ごとの状態に混ぜない。"""
        complete_state["candidates"] = []
        result = check_state(run_script, "target-start", complete_state)
        assert result.returncode == 1
        assert "題材探索台帳が混入" in result.stderr

    @pytest.mark.parametrize("group", ["beginner", "general"])
    def test_review_requires_difficulty_review(self, run_script, complete_state, group):
        """初学者側と一般層側の難易度の検査を、それぞれ省けない。"""
        del complete_state[f"{group}_difficulty_review"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"{group}_difficulty_reviewがない" in result.stderr

    def test_writing_does_not_require_difficulty_review(
        self, run_script, writing_state
    ):
        """生成工程の合格後に難易度の検査を加えられる。"""
        assert check_state(run_script, "writing", writing_state).returncode == 0

    def test_review_rejects_challenge_for_other_knowledge(
        self, run_script, complete_state
    ):
        """別の問う知識についての難易度の検査を現行問題へ使わない。"""
        complete_state["beginner_difficulty_review"]["asked_knowledge"] = "別の問う知識"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "asked_knowledgeが問う知識と一致しない" in result.stderr

    def test_review_rejects_review_of_unknown_pair(self, run_script, complete_state):
        """作る側の照合にも逆引きの結果にもない組の照合結果を使わない。"""
        complete_state["competitor_comparison_reviews"][0]["competitor_id"] = "R9"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "作る側の照合にも逆引きで見つけた候補にもない" in result.stderr

    def test_review_rejects_unresolved_competitor(self, run_script, complete_state):
        """条件照合の検査が不合格の対抗候補を残さない。"""
        complete_state["competitor_comparison_reviews"][0]["status"] = "failed"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "competitor_comparison_reviewsに不合格の項目がある" in result.stderr

    def test_review_rejects_excluding_matching_competitor(
        self, run_script, complete_state
    ):
        """全条件に一致する対抗候補を除外しない。"""
        review = complete_state["competitor_comparison_reviews"][0]
        review["conditions"][0]["match"] = "一致"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "相違する条件なしに候補を除外" in result.stderr

    def test_review_rejects_excluding_near_competitor(self, run_script, complete_state):
        """近接するだけの条件を相違として候補を除外しない。"""
        review = complete_state["competitor_comparison_reviews"][0]
        review["conditions"][0]["match"] = "近接"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "相違する条件なしに候補を除外" in result.stderr

    def test_review_accepts_additional_excluded_competitor(
        self, run_script, complete_state
    ):
        """逆引きで新しく見つけた別対象も、除外として照合できる。"""
        found = copy.deepcopy(
            complete_state["competitor_search_reviews"][0]["found"][0]
        )
        found.update(id="R2", name="追加の対抗候補")
        complete_state["competitor_search_reviews"][0]["found"].append(found)
        review = copy.deepcopy(complete_state["competitor_comparison_reviews"][0])
        review["competitor_id"] = "R2"
        complete_state["competitor_comparison_reviews"].append(review)
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_review_rejects_omitted_generated_competitor(
        self, run_script, complete_state
    ):
        """作る側が挙げた対抗候補の照合を検査から漏らさない。"""
        competitor = copy.deepcopy(complete_state["competitors"][0])
        competitor.update(id="R2", name="別の対抗候補")
        complete_state["competitors"].append(competitor)
        comparison = copy.deepcopy(complete_state["competitor_comparisons"][0])
        comparison["competitor_id"] = "R2"
        complete_state["competitor_comparisons"].append(comparison)
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert (
            "条件の照合を検査していない対抗候補がある: [('C1', 'R2')]" in result.stderr
        )

    def test_review_rejects_conflicting_competitor_judgment(
        self, run_script, complete_state
    ):
        """作る側と検査側の候補の採否が食い違う場合は合格させない。"""
        review = complete_state["competitor_comparison_reviews"][0]
        review["disposition"] = "same_target"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "作る側の判断と一致しない" in result.stderr

    def test_review_requires_current_exposure_assignment(
        self, run_script, complete_state
    ):
        """現行版に対応する露出検査担当の起動記録を要求する。"""
        assignment_of(complete_state, "exposure")["draft_version"] = 1
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "現行版の解答を伏せた名称候補の担当" in result.stderr

    def test_review_requires_exposure_draft_version(self, run_script, complete_state):
        """露出検査担当の起動の記録に対象の版を要求する。"""
        del assignment_of(complete_state, "exposure")["draft_version"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "draft_versionが不正である" in result.stderr

    def test_review_accepts_new_exposure_agent_for_same_version(
        self, run_script, complete_state
    ):
        """同じ版を新しい露出検査担当が再検査した記録を認める。"""
        assignment = copy.deepcopy(assignment_of(complete_state, "exposure"))
        assignment["agent_id"] = "agent-new-exposure"
        complete_state["execution"]["assignments"].append(assignment)
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_review_rejects_reused_exposure_agent(self, run_script, complete_state):
        """問題文の版を変えた露出検査に同じ担当を再利用しない。"""
        assignment = copy.deepcopy(assignment_of(complete_state, "exposure"))
        assignment["draft_version"] = 1
        complete_state["execution"]["assignments"].append(assignment)
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "別の版の露出検査に再利用" in result.stderr

    def test_review_requires_independent_answer_review(
        self, run_script, complete_state
    ):
        """解答候補ごとの独立した判定を省けない。"""
        del complete_state["answer_review"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "answer_reviewがない" in result.stderr

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("draft_version", 1, "問題文と一致しない"),
        ],
    )
    def test_review_rejects_invalid_answer_review(
        self, run_script, complete_state, field, value, message
    ):
        """正誤判定を現行問題へ対応させる。"""
        complete_state["answer_review"][field] = value
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_review_requires_all_answer_reviews(self, run_script, complete_state):
        """採用した解答候補を一名称ずつ判定する。"""
        complete_state["answer_review"]["answers"] = []
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "answer_review.answersが空である" in result.stderr

    @pytest.mark.parametrize(
        ("field", "value", "message"),
        [
            ("same_target", False, "正答判定と対象・指定・適用範囲が一致しない"),
            ("specified_enough", False, "正答判定と対象・指定・適用範囲が一致しない"),
            ("clear_error", True, "正答判定と対象・指定・適用範囲が一致しない"),
            ("scope_matches", False, "正答判定と対象・指定・適用範囲が一致しない"),
        ],
    )
    def test_review_rejects_inconsistent_correct_answer_review(
        self, run_script, complete_state, field, value, message
    ):
        """正答判定を対象・指定・誤り・適用範囲の判断と一致させる。"""
        complete_state["answer_review"]["answers"][0][field] = value
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert message in result.stderr

    def test_writing_requires_exposure_candidate_judgment(
        self, run_script, complete_state
    ):
        """露出検査で挙がった名称候補の正誤判定を要求する。"""
        complete_state["answer_review"]["candidate_reviews"] = []
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "candidate_reviewsが露出候補と一致しない" in result.stderr

    def test_writing_rejects_inconsistent_exposure_candidate_judgment(
        self, run_script, complete_state
    ):
        """露出候補の誤答判定を対象・誤り・適用範囲の判断と一致させる。"""
        candidate = complete_state["answer_review"]["candidate_reviews"][0]
        candidate.update(same_target=True, scope_matches=True)
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "誤答判定に対象・適用範囲の相違がない" in result.stderr

    def test_review_requires_correct_exposure_candidate_in_answer_range(
        self, run_script, complete_state
    ):
        """正答と判定した露出候補を解答範囲へ追加する。"""
        candidate = complete_state["answer_review"]["candidate_reviews"][0]
        candidate.update(
            judgment="correct",
            same_target=True,
            specified_enough=True,
            scope_matches=True,
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "正答が解答範囲に対応付けられていない" in result.stderr

    def test_review_requires_all_facet_paths_in_topic_selection(
        self, run_script, complete_state
    ):
        """抽選した題材では四軸の分類経路を完成稿の題材選択へ含める。"""
        material = complete_state["final_input"]["material"]
        material["topic_selection"] = material["topic_selection"].replace(
            "地域指定なし／", ""
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "placeの分類経路がない" in result.stderr

    def test_review_rejects_internal_facet_key_in_topic_selection(
        self, run_script, complete_state
    ):
        """完成稿の題材選択に内部ノードIDを出さない。"""
        complete_state["final_input"]["material"]["topic_selection"] += " subject::66"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "内部ノードID" in result.stderr

    @pytest.mark.parametrize("stage", ["review", "material", "final"])
    def test_complete_state_passes(
        self, run_script, complete_state, reviewed_state, stage
    ):
        """各項目が完了した状態は指定工程で合格する。"""
        state = reviewed_state if stage == "final" else complete_state
        assert check_state(run_script, stage, state).returncode == 0

    @pytest.mark.parametrize("stage", ["review", "material", "final"])
    def test_specified_target_skips_exploration_assignments(
        self, run_script, complete_state, reviewed_state, stage
    ):
        """解答対象が直接指定された場合も、同じ記録で合格する。"""
        state = reviewed_state if stage == "final" else complete_state
        state["selection_mode"] = "specified"
        state["user_specified_target"] = state["answer_target"]
        topic = state["final_input"]["topic_selection"]
        del topic["facet_paths"]
        topic["history_result"] = "履歴補正なし"
        state["final_input"]["material"]["topic_selection"] = (
            f"ユーザー指定の解答対象：{state['answer_target']}。履歴補正なし。"
        )
        if stage == "final":
            set_reviewed_output(state, final_output_text(state))
        assert check_state(run_script, stage, state).returncode == 0

    def test_work_state_requires_selection_mode(self, run_script, complete_state):
        """対象ごとの作業状態では選択方法を明示する。"""
        del complete_state["selection_mode"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "selection_modeが不正である" in result.stderr

    def test_difficulty_assessment_requires_assigned_agent(
        self, run_script, complete_state
    ):
        """難易度の判断には起動の記録を要する。"""
        drop_assignment(complete_state, "difficulty_assessment")
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "担当の記録がない: ['difficulty_assessment']" in result.stderr

    def test_difficulty_assessment_matches_asked_knowledge(
        self, run_script, writing_state
    ):
        """問う知識を変更したら以前の難易度の判断を通さない。"""
        writing_state["asked_knowledge"] = "考案年から錯視の名称を答える"
        result = check_state(run_script, "writing", writing_state)
        assert result.returncode == 1
        assert (
            "difficulty_assessment.asked_knowledgeが問う知識と一致しない"
            in result.stderr
        )

    @pytest.mark.parametrize("group", ["beginner", "general"])
    def test_difficulty_review_requires_both_groups_to_pass(
        self, run_script, complete_state, group
    ):
        """難易度の独立検査は両参照集団の合格を要する。"""
        complete_state["difficulty_assessment"][group]["status"] = "missing"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert (
            f"difficulty_assessment.{group}が難易度の帯に入ると判断されていない"
            in result.stderr
        )

    @pytest.mark.parametrize(
        "aspect", ["name_learning", "relation_learning", "learning_connection"]
    )
    def test_beginner_review_requires_each_learning_record(
        self, run_script, complete_state, aspect
    ):
        """名称・関係の学習と両者の接続を別々に記録する。"""
        del complete_state["difficulty_assessment"]["beginner"][aspect]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"difficulty_assessment.beginner.{aspect}がない" in result.stderr

    @pytest.mark.parametrize(
        "aspect", ["name_learning", "relation_learning", "learning_connection"]
    )
    def test_beginner_review_requires_learning_reason(
        self, run_script, complete_state, aspect
    ):
        """初学者側の各判断に理由を要求する。"""
        del complete_state["difficulty_assessment"]["beginner"][aspect]["reason"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"difficulty_assessment.beginner.{aspect}.reason" in result.stderr

    def test_beginner_review_accepts_distinct_learning_sources(
        self, run_script, complete_state
    ):
        """名称と問う関係へ別資料の引用を対応させた記録を受け付ける。"""
        complete_state["sources"][0]["quotes"][0]["text"] = (
            "入門教材はミュラー・リヤー錯視の名称を学習項目として扱う。"
            "矢羽は線分の端に付く斜線である。"
            "同じ長さの線分が矢羽の向きで異なる長さに見える錯視は入門教材で扱う"
        )
        add_source(
            complete_state,
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
            },
        )
        beginner = complete_state["difficulty_assessment"]["beginner"]
        beginner["evidence_ids"] = ["Q1", "Q2"]
        beginner["relation_learning"]["evidence_ids"] = ["Q2"]
        beginner["learning_connection"]["evidence_ids"] = ["Q1", "Q2"]
        complete_state["final_input"]["quote_ids"] = ["Q1", "Q2"]
        refresh_material_quotes(complete_state)
        assert check_state(run_script, "material", complete_state).returncode == 0

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
        complete_state["difficulty_assessment"]["beginner"][aspect]["evidence_ids"] = [
            "Q2"
        ]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"{aspect}.evidence_idsが初学者側の根拠に含まれない" in result.stderr

    def test_difficulty_review_requires_other_access_paths(
        self, run_script, complete_state
    ):
        """一般層に名称が共有される別経路の調査を省略しない。"""
        del complete_state["difficulty_assessment"]["general"]["other_access_paths"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "difficulty_assessment.general.other_access_paths" in result.stderr

    def test_difficulty_review_requires_evidence_for_other_access_paths(
        self, run_script, complete_state
    ):
        """接触を確認した経路の調査結果を引用に対応させる。"""
        path = complete_state["difficulty_assessment"]["general"]["other_access_paths"][
            0
        ]
        del path["evidence_ids"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert (
            "difficulty_assessment.general.other_access_paths[0].evidence_ids"
            in result.stderr
        )

    def test_unconfirmed_access_path_does_not_require_quote(
        self, run_script, complete_state
    ):
        """接触を確認できない経路に存在しない逐語引用を要求しない。"""
        path = complete_state["difficulty_assessment"]["general"]["other_access_paths"][
            0
        ]
        path["search_record"] = "一般向けの紹介資料を調べた"
        path["outcome"] = "not_confirmed"
        path["result"] = "調べた範囲では名称への接触を確認できなかった"
        path["evidence_ids"] = []
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_access_path_requires_search_record(self, run_script, complete_state):
        """接触を確認できない経路にも調べた内容を残す。"""
        path = complete_state["difficulty_assessment"]["general"]["other_access_paths"][
            0
        ]
        path["outcome"] = "not_confirmed"
        path["evidence_ids"] = []
        del path["search_record"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert (
            "difficulty_assessment.general.other_access_paths[0].search_record"
            in result.stderr
        )

    def test_final_input_includes_difficulty_assessment_evidence(
        self, run_script, complete_state
    ):
        """難易度の独立検査だけに使う引用も最終入力へ渡す。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "初学者向け資料の記述", "location": "第二節"}
        )
        complete_state["difficulty_assessment"]["beginner"]["evidence_ids"] = [
            "Q1",
            "Q2",
        ]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr
        complete_state["final_input"]["quote_ids"].append("Q2")
        refresh_material_quotes(complete_state)
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_final_input_excludes_other_access_path_evidence(
        self, run_script, complete_state
    ):
        """別経路の探索だけに使う引用は最終入力を増やさない。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "一般向け資料の記述", "location": "第二節"}
        )
        paths = complete_state["difficulty_assessment"]["general"]["other_access_paths"]
        paths[0]["evidence_ids"] = ["Q2"]
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_specified_target_requires_writer_assignment(
        self, run_script, complete_state
    ):
        """直接指定でも作文以降の担当は省略できない。"""
        complete_state["selection_mode"] = "specified"
        complete_state["user_specified_target"] = complete_state["answer_target"]
        drop_assignment(complete_state, "writer")
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "担当の記録がない: ['writer']" in result.stderr

    def test_clue_rejects_quasi_uniqueness_depending_on_another_clue(
        self, run_script, complete_state
    ):
        """他の手掛かりに依存する準一意性を単独の評価として認めない。"""
        check = complete_state["clue_checks"][0]["quasi_uniqueness"]
        check["depends_on_clue_ids"] = ["C2"]
        assert check_state(run_script, "material", complete_state).returncode == 1

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
        competitor = complete_state["competitors"][0]
        comparison = complete_state["competitor_comparisons"][0]
        if invalid_part == "name":
            competitor["name"] = ""
        elif invalid_part == "evidence_ids":
            competitor["evidence_ids"] = []
        elif invalid_part == "conditions":
            comparison["conditions"] = []
        elif invalid_part == "passage":
            comparison["conditions"][0]["passage"] = "問題文にない条件"
        elif invalid_part == "matches":
            comparison["conditions"][0]["matches"] = "未確認"
        elif invalid_part == "condition_evidence_ids":
            comparison["conditions"][0]["evidence_ids"] = []
        elif invalid_part == "exclusion_passage":
            comparison["exclusion_passage"] = "同じ長さの線分"
        else:
            comparison["reason"] = ""
        assert check_state(run_script, "material", complete_state).returncode == 1

    def test_condition_evidence_belongs_to_competitor(self, run_script, complete_state):
        """条件の引用を対抗候補の引用にも対応させる。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "条件についての記述", "location": "第二節"}
        )
        complete_state["competitor_comparisons"][0]["conditions"][0]["evidence_ids"] = [
            "Q2"
        ]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "evidence_idsが候補の引用に含まれていない" in result.stderr

    def test_competitor_with_all_matching_conditions_cannot_be_excluded(
        self, run_script, complete_state
    ):
        """問題文の条件に相違がない別対象を退けない。"""
        complete_state["competitor_comparisons"][0]["conditions"][0]["matches"] = True
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "exclusion_passageが相違する条件ではない" in result.stderr

    def test_same_target_name_does_not_need_exclusion_passage(
        self, run_script, complete_state
    ):
        """同一対象の別名に別対象を退ける表現を要求しない。"""
        comparison = complete_state["competitor_comparisons"][0]
        comparison["disposition"] = "same_target"
        comparison["conditions"][0]["matches"] = True
        del comparison["exclusion_passage"]
        review = complete_state["competitor_comparison_reviews"][0]
        review["disposition"] = "same_target"
        review["conditions"][0]["match"] = "一致"
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_same_target_name_cannot_have_different_condition(
        self, run_script, complete_state
    ):
        """異なる条件を記録した候補を同一対象の別名として通さない。"""
        comparison = complete_state["competitor_comparisons"][0]
        comparison["disposition"] = "same_target"
        del comparison["exclusion_passage"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "同一対象の別名として扱う条件と矛盾している" in result.stderr

    def test_otoshi_requires_directly_descriptive_clue(
        self, run_script, complete_state
    ):
        """落としに含む手掛かりは対象を直接説明する。"""
        complete_state["clue_uses"][0]["directly_describes_target"] = False
        assert check_state(run_script, "material", complete_state).returncode == 1

    def test_structure_accepts_ov_post_limiter(self, run_script, complete_state):
        """OV型では落としの後に名称を限定する表現を置ける。"""
        complete_state["draft"]["text"] = (
            "同じ長さの線分が矢羽の向きで異なる長さに見える錯視を、一般に何というでしょう？"
        )
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        structure.update(question_form="OV", question_phrase="何というでしょう？")
        complete_state["structure_review"]["question_form"] = "OV"
        complete_state["final_input"]["material"]["problem"] = complete_state["draft"][
            "text"
        ]
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_structure_requires_connective_scan(self, run_script, complete_state):
        """接続箇所がない場合も走査結果を要求する。"""
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        del structure["connective_scan"]
        assert check_state(run_script, "material", complete_state).returncode == 1

    def test_structure_requires_prefuri_segments(self, run_script, complete_state):
        """前フリがない問題でも検査済みの空配列を要求する。"""
        structure = next(
            check for check in complete_state["checks"] if check["id"] == "structure"
        )
        del structure["prefuri_segments"]
        assert check_state(run_script, "material", complete_state).returncode == 1

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
        result = check_state(run_script, "material", complete_state)
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
        result = check_state(run_script, "material", complete_state)
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
        assert check_state(run_script, "material", complete_state).returncode == 1

    def test_review_requires_answer_exposure_check(self, run_script, complete_state):
        """解答露出の検査項目を欠く状態を拒否する。"""
        complete_state["checks"] = [
            check
            for check in complete_state["checks"]
            if check["id"] != "answer_exposure"
        ]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "必須検査がない" in result.stderr

    def test_blind_candidate_can_require_answer_side_knowledge(
        self, run_script, complete_state
    ):
        """名称形成自体に解答側の知識が要る候補は受け付ける。"""
        complete_state["blind_candidates"] = [
            {"id": "X2", "name": "ミュラー・リヤー錯視", "draft_version": 2}
        ]
        analysis = copy.deepcopy(complete_state["exposure_analysis"][0])
        analysis.update(candidate_id="X2", name="ミュラー・リヤー錯視")
        complete_state["exposure_analysis"].append(analysis)
        complete_state["answer_review"]["candidate_reviews"].append(
            {
                "candidate_id": "X2",
                "answer_id": "A1",
                "judgment": "correct",
                "status": "passed",
                "same_target": True,
                "specified_enough": True,
                "clear_error": False,
                "scope_matches": True,
                "reason": "対象の標準名称である",
                "evidence_ids": ["Q1"],
            }
        )
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_blind_candidate_rejects_mapping_before_disclosure(
        self, run_script, complete_state
    ):
        """解答を伏せて挙げた候補に、開示前の解答との対応付けを置かない。"""
        complete_state["blind_candidates"] = [
            {"id": "X2", "name": "錯視", "draft_version": 2, "answer_id": None}
        ]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "解答開示前の対応付けがある" in result.stderr

    def test_semantic_candidate_requires_answer_mapping(
        self, run_script, complete_state
    ):
        """意味から挙げた候補には、挙げた担当による解答との対応付けを要求する。"""
        exposure = next(
            check
            for check in complete_state["checks"]
            if check["id"] == "answer_exposure"
        )
        del exposure["semantic_candidates"][0]["answer_id"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "answer_idが解答候補を参照していない" in result.stderr

    def test_blind_candidate_review_requires_answer_mapping(
        self, run_script, complete_state
    ):
        """解答を伏せて挙げた候補は、開示後の判定で解答との対応付けを要求する。"""
        complete_state["blind_candidates"] = [
            {"id": "X2", "name": "錯視", "draft_version": 2}
        ]
        analysis = copy.deepcopy(complete_state["exposure_analysis"][0])
        analysis.update(candidate_id="X2", name="錯視")
        complete_state["exposure_analysis"].append(analysis)
        review = copy.deepcopy(complete_state["answer_review"]["candidate_reviews"][0])
        review["candidate_id"] = "X2"
        complete_state["answer_review"]["candidate_reviews"].append(review)
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "answer_idがない" in result.stderr

    def test_every_exposure_candidate_needs_passed_analysis(
        self, run_script, complete_state
    ):
        """解答を伏せた候補と意味から挙げた候補のすべてに、合格した露出の分析を要する。"""
        complete_state["blind_candidates"] = [
            {"id": "X2", "name": "錯視", "draft_version": 2}
        ]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "exposure_analysisに検査のない項目がある: ['X2']" in result.stderr
        complete_state["blind_candidates"] = []
        complete_state["exposure_analysis"][0].update(
            status="failed", fix_data=["exposure_candidates"]
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "exposure_analysisに不合格の項目がある: ['X1']" in result.stderr

    def test_answer_side_component_requires_reason(self, run_script, complete_state):
        """解答側の知識とした名称要素には理由を要求する。"""
        exposure = next(
            check
            for check in complete_state["checks"]
            if check["id"] == "answer_exposure"
        )
        del exposure["semantic_candidates"][0]["components"][0]["answer_side_reason"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "answer_side_reasonがない" in result.stderr

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
        assert check_state(run_script, "material", complete_state).returncode == 1

    def test_review_rejects_old_draft_version(self, run_script, complete_state):
        """現行稿より古い版の検査結果を拒否する。"""
        complete_state["checks"][0]["draft_version"] = 1
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "問題文の版が一致しない" in result.stderr

    def test_review_rejects_unknown_quote(self, run_script, complete_state):
        """存在しない引用を根拠にした命題を拒否する。"""
        complete_state["proposition_support"][0]["evidence_ids"] = ["Q2"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "存在しないIDを参照" in result.stderr

    @pytest.mark.parametrize("invalid_id", [{}, []])
    def test_review_rejects_nonstring_quote_id(
        self, run_script, complete_state, invalid_id
    ):
        """引用IDに文字列以外を指定しても追跡表示を出さない。"""
        complete_state["proposition_support"][0]["evidence_ids"] = [invalid_id]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "空でない文字列ID" in result.stderr
        assert "Traceback" not in result.stderr

    def test_simple_proposition_can_omit_verification_elements(
        self, run_script, complete_state
    ):
        """単純な命題には形式的な検証要素を要求しない。"""
        assert "verification_elements" not in complete_state["proposition_support"][0]
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_recorded_verification_elements_require_valid_evidence(
        self, run_script, complete_state
    ):
        """記録した各検証要素の引用IDを検査する。"""
        proposition = complete_state["propositions"][0]
        proposition["claim"] = "市が住民に賞状を贈った"
        proposition["passage"] = "市が住民に賞状を贈った"
        complete_state["sources"][0]["quotes"][0]["text"] = proposition["claim"]
        complete_state["proposition_support"][0]["verification_elements"] = [
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
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "verification_elements[1].evidence_ids" in result.stderr

    def test_term_must_appear_in_current_draft(self, run_script, complete_state):
        """問題文にない語を専門用語の検査記録に含めない。"""
        complete_state["terms"][0]["term"] = "問題文にない専門用語"
        result = check_state(run_script, "material", complete_state)
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
        result = check_state(run_script, "material", complete_state)
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
        complete_state["final_input"]["material"]["problem"] = complete_state["draft"][
            "text"
        ]
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
        complete_state["term_listing"]["terms"][0]["term"] = "ブレンターノ型"
        complete_state["term_necessity_reviews"][0]["meaning_needed"] = False
        complete_state["term_sense_reviews"] = []
        complete_state["term_audience_reviews"] = []
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "understanding_without_meaning" in result.stderr
        term["understanding_without_meaning"] = (
            "変形版の名称だと分かれば、図形の詳細を知らなくても文意が通る"
        )
        assert check_state(run_script, "material", complete_state).returncode == 0

    @pytest.mark.parametrize(
        ("change", "expected"),
        [
            ("missing", "term_listing.termsが専門用語の記録と一致しない"),
            ("extra", "term_listing.termsが専門用語の記録と一致しない"),
            ("meaning_needed", "meaning_neededが作る側の判断と一致しない"),
        ],
    )
    def test_term_reviews_check_terms_and_meaning_need(
        self, run_script, complete_state, change, expected
    ):
        """独立に列挙した語と意味内容の要否を作る側と照合する。"""
        listed = complete_state["term_listing"]["terms"]
        if change == "missing":
            listed.clear()
        elif change == "extra":
            listed.append({"id": "T2", "term": "線分"})
        else:
            complete_state["term_necessity_reviews"][0]["meaning_needed"] = False
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert expected in result.stderr

    @pytest.mark.parametrize(
        "key", ["term_necessity_reviews", "term_sense_reviews", "term_audience_reviews"]
    )
    def test_review_requires_passed_term_reviews(self, run_script, complete_state, key):
        """意味内容の要否、語義、既習性は、それぞれ検査担当の合格を要する。"""
        complete_state[key][0].update(status="failed", fix_data=["terms"])
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"{key}に不合格の項目がある: ['T1']" in result.stderr

    @pytest.mark.parametrize(
        ("kind", "key"),
        [("meaning", "term_sense_reviews"), ("audience", "term_audience_reviews")],
    )
    def test_term_evidence_is_included_in_final_input(
        self, run_script, complete_state, kind, key
    ):
        """専門用語の判断に使う引用を最終入力の引用集合にも含める。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "矢羽の説明", "location": "用語解説"}
        )
        complete_state["terms"][0][f"{kind}_evidence_ids"] = ["Q2"]
        complete_state[key][0]["evidence_ids"] = ["Q2"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr
        complete_state["final_input"]["quote_ids"].append("Q2")
        refresh_material_quotes(complete_state)
        assert check_state(run_script, "material", complete_state).returncode == 0

    @pytest.mark.parametrize(
        ("kind", "key"),
        [("meaning", "term_sense_reviews"), ("audience", "term_audience_reviews")],
    )
    def test_term_reviews_cover_all_adopted_evidence(
        self, run_script, complete_state, kind, key
    ):
        """作る側が採用した専門用語の引用を検査担当が残さず確認する。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "矢羽の別の説明", "location": "第二節"}
        )
        complete_state["terms"][0][f"{kind}_evidence_ids"].append("Q2")
        complete_state["final_input"]["quote_ids"].append("Q2")
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"{key}.T1.evidence_idsが採用引用と一致しない" in result.stderr
        complete_state[key][0]["evidence_ids"].append("Q2")
        refresh_material_quotes(complete_state)
        assert check_state(run_script, "material", complete_state).returncode == 0

    @pytest.mark.parametrize(
        ("change", "expected"),
        [
            ("missing", "term_listingがない"),
            ("stale", "term_listing.draft_version"),
            ("same_agent", "agent_idを別の役割にも割り当てている"),
        ],
    )
    def test_review_requires_independent_term_listing(
        self, run_script, complete_state, change, expected
    ):
        """独立した担当が現行版から専門用語を列挙する。"""
        if change == "missing":
            del complete_state["term_listing"]
        elif change == "stale":
            complete_state["term_listing"]["draft_version"] = 1
        else:
            assignment_of(complete_state, "term_listing")["agent_id"] = assignment_of(
                complete_state, "writer"
            )["agent_id"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert expected in result.stderr

    def test_review_requires_verbatim_quote(self, run_script, complete_state):
        """引用本文を欠く資料を拒否する。"""
        del complete_state["sources"][0]["quotes"][0]["text"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "quotes.Q1.textがない" in result.stderr

    def test_review_rejects_quote_missing_from_final_input(
        self, run_script, complete_state
    ):
        """採用した判断に使う引用を最終入力から落とせない。"""
        complete_state["final_input"]["quote_ids"] = []
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr

    def test_review_rejects_unused_quote_in_final_input(
        self, run_script, complete_state
    ):
        """採用した判断に使わない引用を最終入力へ加えない。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "不採用の記述", "location": "第二節"}
        )
        complete_state["final_input"]["quote_ids"].append("Q2")
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr

    def test_review_rejects_duplicate_quote_in_final_input(
        self, run_script, complete_state
    ):
        """同じ引用IDを重複して最終入力へ置かない。"""
        complete_state["final_input"]["quote_ids"].append("Q1")
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "final_input.quote_idsが判断に用いた引用と一致しない" in result.stderr

    def test_review_requires_relative_clause_records(self, run_script, complete_state):
        """連体修飾節の関係を記録せずに検査を通さない。"""
        del complete_state["relative_clauses"]
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "relative_clauses" in result.stderr

    def test_review_accepts_empty_relative_clauses(self, run_script, complete_state):
        """連体修飾節がない問題文では空配列を認める。"""
        complete_state["relative_clauses"] = []
        assert check_state(run_script, "material", complete_state).returncode == 0

    def test_review_requires_proposition_for_outer_clause(
        self, run_script, complete_state
    ):
        """外の関係では修飾節が表す内容と解答対象を結ぶ命題を要求する。"""
        complete_state["relative_clauses"][0]["relation_proposition_ids"] = []
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "relation_proposition_ids" in result.stderr

    def test_review_rejects_proposition_for_inner_clause(
        self, run_script, complete_state
    ):
        """内の関係に外の関係用の命題を付けない。"""
        complete_state["relative_clauses"][0]["relation"] = "inner"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "relation_proposition_idsが内の関係にある" in result.stderr

    def test_review_requires_clause_from_current_draft(
        self, run_script, complete_state
    ):
        """現行問題文にない連体修飾節を検査の入力に使わない。"""
        complete_state["relative_clauses"][0]["passage"] = "別の文章"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "passageが問題文にない" in result.stderr

    @pytest.mark.parametrize(
        "key",
        [
            "proposition_ids",
            "clue_ids",
            "term_ids",
            "answer_ids",
        ],
    )
    def test_review_rejects_duplicate_final_input_id(
        self, run_script, complete_state, key
    ):
        """最終入力の各ID配列で重複を認めない。"""
        complete_state["final_input"][key].append(complete_state["final_input"][key][0])
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert f"final_input.{key}が検査済みの現行項目と一致しない" in result.stderr

    def test_review_ignores_unchecked_clue_field(self, run_script, complete_state):
        """手掛かりの必須検査以外の値を引用収集の対象にしない。"""
        complete_state["clue_checks"][0]["note"] = "補足"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 0

    @pytest.mark.parametrize(
        "label", ["ACCEPTANCE\t0.9", "DRAW\t0.4", "VERDICT\tACCEPT"]
    )
    def test_review_rejects_length_judge_labels(
        self, run_script, complete_state, label
    ):
        """問題文の長さへ判定器の内部表記を渡さない。"""
        complete_state["final_input"]["material"]["length"] = label
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "内部表記" in result.stderr

    def test_review_requires_original_passage_in_accuracy(
        self, run_script, complete_state
    ):
        """確認した内容との一致に命題の原文箇所を示す。"""
        complete_state["final_input"]["material"]["expression.accuracy"] = (
            "資料名（第一節）の表現と照合する。"
        )
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "原文箇所がない" in result.stderr

    def test_review_rejects_unadopted_quote_in_material(
        self, run_script, complete_state
    ):
        """採用していない引用を最終入力へ追加しない。"""
        complete_state["sources"][0]["quotes"].append(
            {"id": "Q2", "text": "未採用の資料記述", "location": "第二節"}
        )
        complete_state["final_input"]["material"]["verification"] += "未採用の資料記述"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "不採用の引用Q2" in result.stderr

    def test_review_rejects_invalid_source_url(self, run_script, complete_state):
        """資料のURL欄へURLではない値を置かない。"""
        complete_state["sources"][0]["url"] = "資料の場所"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "urlが資料URLではない" in result.stderr

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

    def test_final_rejects_unadopted_source_url(
        self, run_script, reviewed_state, tmp_path
    ):
        """最終入力にない資料のURLを完成稿へ追加しない。"""
        output = tmp_path / "完成稿.md"
        output.write_text(
            final_output_text(reviewed_state) + "\n\nhttps://example.org/unadopted",
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
        assert "最終入力にない資料" in result.stderr

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

    @pytest.mark.parametrize("key", FINAL_REVIEW_ROLES)
    @pytest.mark.parametrize(
        ("change", "message"),
        [
            ({"status": "failed"}, ".statusが合格していない"),
            ({"output_sha256": "0" * 64}, ".output_sha256が完成稿と一致しない"),
        ],
    )
    def test_final_requires_review_of_current_output(
        self, run_script, reviewed_state, key, change, message
    ):
        """完成稿の照合結果は現行ファイルに対応する。"""
        reviewed_state[key].update(change)
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert key + message in result.stderr

    @pytest.mark.parametrize("key", FINAL_REVIEW_ROLES)
    def test_final_requires_review_record(self, run_script, reviewed_state, key):
        """反映の照合と混入の検査のどちらかがない完成稿は確定しない。"""
        del reviewed_state[key]
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert f"{key}がない" in result.stderr

    @pytest.mark.parametrize("key", FINAL_REVIEW_ROLES)
    def test_final_requires_reviewer_of_current_output(
        self, run_script, reviewed_state, key
    ):
        """現行の完成稿について起動した担当の記録を要する。"""
        assignment_of(reviewed_state, key)["output_sha256"] = "0" * 64
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert f"{key}の担当が現行の完成稿について起動されていない" in result.stderr

    def test_final_requires_independent_reviewer(self, run_script, reviewed_state):
        """完成稿の照合担当を作文担当と兼任させない。"""
        assignment_of(reviewed_state, "final_reflection_review")["agent_id"] = (
            assignment_of(reviewed_state, "writer")["agent_id"]
        )
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "agent_idを別の役割にも割り当てている" in result.stderr

    def test_final_rejects_reviewer_reused_for_other_output(
        self, run_script, reviewed_state
    ):
        """組み直した完成稿を前の完成稿の照合担当に照合させない。"""
        previous = dict(assignment_of(reviewed_state, "final_contamination_review"))
        previous["output_sha256"] = "0" * 64
        reviewed_state["execution"]["assignments"].insert(0, previous)
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "agent_idを別の完成稿の照合に再利用している" in result.stderr

    def test_final_rejects_duplicate_reviewed_quote(self, run_script, reviewed_state):
        """反映の照合の対象引用を重複させない。"""
        reviewed_state["final_reflection_review"]["quote_ids"].append("Q1")
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert (
            "final_reflection_review.quote_idsが最終入力と一致しない" in result.stderr
        )

    def test_final_accepts_state_without_delegation(self, run_script, reviewed_state):
        """委譲できない環境では起動の記録なしで確定できる。"""
        reviewed_state["execution"] = {
            "delegation_available": False,
            "unavailable_reason": "委譲機能がない",
        }
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
        assert (
            "final_reflection_review.output_sha256が完成稿と一致しない" in result.stderr
        )

    def test_final_requires_all_checked_answers(self, run_script, reviewed_state):
        """最終入力が検査済みの別解を欠けば出力を拒否する。"""
        reviewed_state["answers"].append({"id": "A2", "answer": "別解"})
        reviewed_state["answer_judgments"].append(
            {
                "answer_id": "A2",
                "judgment": "prompt",
                "reason": "別名である",
                "evidence_ids": ["Q1"],
            }
        )
        reviewed_state["answer_review"]["answers"].append(
            {
                "id": "A2",
                "judgment": "prompt",
                "status": "passed",
                "same_target": True,
                "specified_enough": False,
                "clear_error": False,
                "scope_matches": True,
                "reason": "指定が不足する",
                "evidence_ids": ["Q1"],
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
        reviewed_state["clues"].append(
            {"id": "C2", "fact": "矢羽は線分の端に付く", "proposition_ids": ["P1"]}
        )
        reviewed_state["clue_uses"].append({"clue_id": "C2", "status": "rejected"})
        reviewed_state["final_input"]["clue_ids"].append("C2")
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "final_input.clue_idsが検査済みの現行項目と一致しない" in result.stderr

    def test_review_uses_only_assigned_agents(self, run_script, complete_state):
        """担当工程を同一agentへ集中させた状態を拒否する。"""
        for item in complete_state["execution"]["assignments"]:
            item["agent_id"] = "agent-1"
        result = check_state(run_script, "material", complete_state)
        assert result.returncode == 1
        assert "agent_idを別の役割にも割り当てている" in result.stderr

    def test_finalization_agent_needed_only_for_final(
        self, run_script, complete_state, reviewed_state
    ):
        """最終化の担当は検査のステップでは不要だが最終出力時には必要となる。"""
        for state in (complete_state, reviewed_state):
            drop_assignment(state, "finalization")
        assert check_state(run_script, "material", complete_state).returncode == 0
        result = check_state(run_script, "final", reviewed_state)
        assert result.returncode == 1
        assert "担当の記録がない: ['finalization']" in result.stderr

    def test_invalid_json_is_input_error(self, run_script):
        """解析できないJSONは作業状態の不合格とは異なる入力エラーとする。"""
        result = run_script("work_state_check.py", "--stage", "writing", stdin="{不正")
        assert result.returncode == 2
        assert "入力エラー" in result.stderr
        assert "Traceback" not in result.stderr
