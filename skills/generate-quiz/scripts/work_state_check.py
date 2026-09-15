#!/usr/bin/env python3
"""題材探索と作問状態の内容、参照関係、工程境界を検査する。

入力はJSONファイルのパスまたは標準入力から受け取る。--stageには
selection、generation、audit、finalのいずれかを指定する。

終了コード:
    0  指定工程の条件を満たす
    1  読み込んだ状態が構造または指定工程の条件を満たさない
    2  JSONを読めない、または引数が不正

使用例:
    python3 work_state_check.py --stage selection selection.json
    python3 work_state_check.py --stage audit state.json
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

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
MIN_ENTRY_POINTS = 2
MIN_ENTRY_POINT_KINDS = 2
MIN_COVERAGE_AREAS = 2
MIN_EXPRESSION_ALTERNATIVES = 2
EXIT_OK, EXIT_STATE_INVALID, EXIT_USAGE = 0, 1, 2


class StateError(ValueError):
    pass


def require_condition(ok, msg):
    if not ok:
        raise StateError(msg)


def required_text(obj, key, name):
    value = obj.get(key)
    require_condition(isinstance(value, str) and value.strip(), f"{name}.{key}がない")
    return value.strip()


def required_list(value, name, *, nonempty=False):
    require_condition(isinstance(value, list), f"{name}は配列でなければならない")
    require_condition(not nonempty or value, f"{name}が空である")
    return value


def required_id_list(value, name, *, nonempty=False):
    values = required_list(value, name, nonempty=nonempty)
    require_condition(
        all(isinstance(item, str) and item.strip() for item in values),
        f"{name}は空でない文字列IDの配列でなければならない",
    )
    return values


def records_with_ids(value, name, *, nonempty=False):
    values = required_list(value, name, nonempty=nonempty)
    ids = []
    for i, item in enumerate(values):
        require_condition(
            isinstance(item, dict), f"{name}[{i}]はオブジェクトでなければならない"
        )
        ids.append(required_text(item, "id", f"{name}[{i}]"))
    require_condition(len(ids) == len(set(ids)), f"{name}のidが重複している")
    return values, set(ids)


def referenced_ids(obj, key, allowed, name, *, nonempty=True):
    values = required_id_list(obj.get(key), f"{name}.{key}", nonempty=nonempty)
    unknown = set(values) - allowed
    require_condition(
        not unknown, f"{name}.{key}が存在しないIDを参照している: {sorted(unknown)}"
    )
    return values


def require_stage_completion(obj, name, stage):
    require_condition(
        obj.get("generation") == "complete", f"{name}が生成側で完了していない"
    )
    audit = obj.get("audit")
    require_condition(
        audit in {"pending", "passed", "missing", "failed"}, f"{name}.auditが不正である"
    )
    if stage == "generation":
        require_condition(
            audit == "pending", f"{name}は生成工程の時点で監査済みになっている"
        )
    else:
        require_condition(audit == "passed", f"{name}が監査に合格していない")


def normalize_candidate_name(value):
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(
        char
        for char in normalized
        if char not in " \t\r\n・･‐‑‒–—―-_=＝()（）[]［］{}｛｝"
    )


def validate_name_formation(item, name):
    require_condition(isinstance(item, dict), f"{name}はオブジェクトでなければならない")
    candidate_name = required_text(item, "name", name)
    required_text(item, "formation_rule", name)
    components = required_list(
        item.get("components"), f"{name}.components", nonempty=True
    )
    for index, component in enumerate(components):
        component_name = f"{name}.components[{index}]"
        require_condition(
            isinstance(component, dict),
            f"{component_name}はオブジェクトでなければならない",
        )
        required_text(component, "form", component_name)
        required_text(component, "source", component_name)
        require_condition(
            component.get("knowledge")
            in {"surface", "general_language", "general_domain", "target_association"},
            f"{component_name}.knowledgeが不正である",
        )
    requires_target = item.get("requires_target_association")
    require_condition(
        isinstance(requires_target, bool), f"{name}.requires_target_associationがない"
    )
    if requires_target:
        required_text(item, "target_association_step", name)
    return candidate_name, requires_target


def validate_exposure_precheck(item, name, *, require_formation=False):
    precheck = item.get("exposure_precheck")
    require_condition(isinstance(precheck, dict), f"{name}.exposure_precheckがない")
    check_name = f"{name}.exposure_precheck"
    for key in ("representative_descriptions", "accepted_names"):
        values = required_list(precheck.get(key), f"{check_name}.{key}", nonempty=True)
        for index, value in enumerate(values):
            require_condition(
                isinstance(value, str) and value.strip(),
                f"{check_name}.{key}[{index}]がない",
            )
    accepted_names = {
        normalize_candidate_name(value) for value in precheck["accepted_names"]
    }
    formations = required_list(
        precheck.get("formations"),
        f"{check_name}.formations",
        nonempty=require_formation,
    )
    exposed = False
    for index, formation in enumerate(formations):
        candidate_name, requires_target = validate_name_formation(
            formation, f"{check_name}.formations[{index}]"
        )
        if (
            normalize_candidate_name(candidate_name) in accepted_names
            and not requires_target
        ):
            exposed = True
    require_condition(
        precheck.get("status") == ("rejected" if exposed else "passed"),
        f"{check_name}.statusが名称形成の分析と一致しない",
    )
    return exposed


def validate_selection_state(state):
    required_text(state, "facet", "selection")
    entries, entry_ids = records_with_ids(
        state.get("entry_points"), "entry_points", nonempty=True
    )
    kinds = set()
    for item in entries:
        required_text(item, "label", f"entry_points.{item['id']}")
        kinds.add(required_text(item, "kind", f"entry_points.{item['id']}"))
    require_condition(
        len(entries) >= MIN_ENTRY_POINTS and len(kinds) >= MIN_ENTRY_POINT_KINDS,
        "異なる種類の入口を二つ以上使っていない",
    )
    areas, area_ids = records_with_ids(
        state.get("coverage_areas"), "coverage_areas", nonempty=True
    )
    if len(areas) < MIN_COVERAGE_AREAS:
        required_text(state, "single_area_reason", "selection")
    for item in areas:
        name = f"coverage_areas.{item['id']}"
        required_text(item, "label", name)
        required_text(item, "basis", name)
        require_condition(item.get("explored") is True, f"{name}が未探索である")
        referenced_ids(item, "entry_point_ids", entry_ids, name)
    candidates, candidate_ids = records_with_ids(
        state.get("candidates"), "candidates", nonempty=True
    )
    for item in candidates:
        name = f"candidates.{item['id']}"
        required_text(item, "label", name)
        referenced_ids(item, "coverage_area_ids", area_ids, name)
        referenced_ids(item, "discovery_entry_point_ids", entry_ids, name)
        disposition = item.get("disposition")
        require_condition(
            disposition in {"eligible", "excluded"}, f"{name}.dispositionが不正である"
        )
        if disposition == "eligible":
            require_condition(
                item.get("expanded") is True, f"{name}から探索を展開していない"
            )
            require_condition(
                not validate_exposure_precheck(item, name),
                f"{name}は代表説明から正答名を形成できるため選択対象にできない",
            )
        else:
            code = item.get("exclusion_code")
            require_condition(
                code
                in {
                    "out_of_scope",
                    "duplicate",
                    "no_japanese_context",
                    "prohibited_format",
                    "unavoidable_exposure",
                },
                f"{name}.exclusion_codeが不正である",
            )
            required_text(item, "exclusion_reason", name)
            if code == "duplicate":
                merged_into = required_text(item, "merged_into", name)
                require_condition(
                    merged_into in candidate_ids, f"{name}.merged_intoが存在しない"
                )
            if code == "unavoidable_exposure":
                require_condition(
                    validate_exposure_precheck(item, name, require_formation=True),
                    f"{name}.exposure_precheckが解答露出による除外を示していない",
                )
    frontier = required_id_list(state.get("frontier_ids"), "frontier_ids")
    require_condition(
        not (set(frontier) - candidate_ids), "frontier_idsに存在しない候補がある"
    )
    require_condition(not frontier, "未展開の有力候補が残っている")
    require_condition(state.get("saturated") is True, "探索が飽和していない")


def validate_execution_assignments(state, stage):
    data = state.get("execution")
    require_condition(isinstance(data, dict), "executionがない")
    available = data.get("delegation_available")
    require_condition(
        isinstance(available, bool), "execution.delegation_availableがない"
    )
    if available:
        roles = {
            "generation": ("exploration", "generation", "exposure"),
            "audit": ("exploration", "generation", "exposure", "audit"),
            "final": ("exploration", "generation", "exposure", "audit", "finalization"),
        }[stage]
        agents = data.get("agents")
        require_condition(isinstance(agents, dict), "execution.agentsがない")
        ids = [required_text(agents, k, "execution.agents") for k in roles]
        require_condition(
            len(ids) == len(set(ids)), "工程を別々のagentへ割り当てていない"
        )
        assignments = data.get("assignment_log")
        require_condition(
            isinstance(assignments, dict), "execution.assignment_logがない"
        )
        for role in roles:
            item = assignments.get(role)
            require_condition(
                isinstance(item, dict), f"execution.assignment_log.{role}がない"
            )
            require_condition(
                item.get("agent_id") == agents[role],
                f"execution.assignment_log.{role}.agent_idが担当記録と一致しない",
            )
            require_condition(
                item.get("recorded_at_spawn") is True,
                f"execution.assignment_log.{role}が起動時に記録されていない",
            )
            required_list(
                item.get("artifact_refs"),
                f"execution.assignment_log.{role}.artifact_refs",
                nonempty=True,
            )
    else:
        required_text(data, "unavailable_reason", "execution")


def validate_sources_propositions_and_clues(state, version, stage):
    sources, _ = records_with_ids(state.get("sources"), "sources", nonempty=True)
    quote_ids = set()
    for source in sources:
        required_text(source, "citation", f"sources.{source['id']}")
        quotes, ids = records_with_ids(
            source.get("quotes"), f"sources.{source['id']}.quotes", nonempty=True
        )
        require_condition(not quote_ids & ids, "引用IDが資料間で重複している")
        quote_ids |= ids
        for quote in quotes:
            required_text(quote, "text", f"quotes.{quote['id']}")
            required_text(quote, "location", f"quotes.{quote['id']}")
    props, prop_ids = records_with_ids(
        state.get("propositions"), "propositions", nonempty=True
    )
    active_props = []
    for item in props:
        if item.get("status") != "active":
            continue
        active_props.append(item)
        name = f"propositions.{item['id']}"
        required_text(item, "claim", name)
        required_text(item, "passage", name)
        required_text(item, "reason", name)
        require_condition(
            item.get("inference_type")
            in {"direct", "deduction", "interpretation", "synthesis"},
            f"{name}.inference_typeが不正である",
        )
        referenced_ids(item, "evidence_ids", quote_ids, name)
        require_condition(
            item.get("draft_version") == version, f"{name}の問題文の版が一致しない"
        )
        require_stage_completion(item, name, stage)
        elements = required_list(
            item.get("verification_elements", []),
            f"{name}.verification_elements",
        )
        for index, element in enumerate(elements):
            element_name = f"{name}.verification_elements[{index}]"
            require_condition(
                isinstance(element, dict),
                f"{element_name}はオブジェクトでなければならない",
            )
            required_text(element, "text", element_name)
            required_text(element, "reason", element_name)
            require_condition(
                element.get("inference_type")
                in {"direct", "deduction", "interpretation", "synthesis"},
                f"{element_name}.inference_typeが不正である",
            )
            referenced_ids(element, "evidence_ids", quote_ids, element_name)
    require_condition(active_props, "activeな命題がない")
    clues, _ = records_with_ids(state.get("clues"), "clues", nonempty=True)
    active_clues = []
    for item in clues:
        if item.get("status") != "active":
            continue
        active_clues.append(item)
        name = f"clues.{item['id']}"
        required_text(item, "text", name)
        referenced_ids(item, "proposition_ids", prop_ids, name)
        values = item.get("checks")
        require_condition(isinstance(values, dict), f"{name}.checksがない")
        for key in ("centrality", "quasi_uniqueness", "familiarity"):
            check = values.get(key)
            cname = f"{name}.{key}"
            require_condition(isinstance(check, dict), f"{cname}がない")
            required_text(check, "claim", cname)
            required_text(check, "reason", cname)
            referenced_ids(check, "evidence_ids", quote_ids, cname)
            if key == "quasi_uniqueness":
                required_text(check, "comparison_scope", cname)
                required_list(
                    check.get("competitors"), f"{cname}.competitors", nonempty=True
                )
                require_condition(
                    check.get("standalone_sufficient") is True,
                    f"{cname}.standalone_sufficientがtrueではない",
                )
                require_condition(
                    not required_list(
                        check.get("depends_on_clue_ids"),
                        f"{cname}.depends_on_clue_ids",
                    ),
                    f"{cname}が他の手掛かりに依存している",
                )
            require_stage_completion(check, cname, stage)
    require_condition(active_clues, "activeな手掛かりがない")
    return quote_ids, active_props, active_clues


def validate_structure_check(item, name, draft_text, active_clues):
    form = required_text(item, "question_form", name)
    require_condition(form in {"SC", "OV"}, f"{name}.question_formが不正である")
    phrase = required_text(item, "question_phrase", name)
    require_condition(phrase in draft_text, f"{name}.question_phraseが問題文にない")
    if re.search(r"を何(?:と|て)?(?:いう|呼ぶ|言う)", phrase):
        require_condition(form == "OV", f"{name}.question_formが質問形式と一致しない")
    if re.search(r"は(?:何|誰|どこ|どちら)(?:でしょう|ですか)", phrase):
        require_condition(form == "SC", f"{name}.question_formが質問形式と一致しない")
    nucleus = required_text(item, "nucleus", name)
    otoshi = required_text(item, "otoshi", name)
    required_text(item, "otoshi_direct_description", name)
    require_condition(
        nucleus
        not in {
            "もの",
            "物",
            "こと",
            "事",
            "さま",
            "様",
            "用語",
            "言葉",
            "名称",
            "名前",
            "通称",
            "題名",
        },
        f"{name}.nucleusが解答対象の上位分類ではない",
    )
    require_condition(
        otoshi.endswith(nucleus) and otoshi in draft_text,
        f"{name}.otoshiが完成稿の核名詞句で終わらない",
    )
    before_question = draft_text.split(phrase, 1)[0]
    if form == "SC":
        require_condition(
            before_question.rstrip("、， ").endswith(otoshi),
            f"{name}.otoshiが核名詞句の直前にない",
        )
    else:
        after_otoshi = draft_text.rsplit(otoshi, 1)[1]
        require_condition(
            after_otoshi.startswith(("を", "のことを")),
            f"{name}.otoshiが核名詞句の直前にない",
        )
    otoshi_clue_ids = referenced_ids(
        item, "otoshi_clue_ids", {x["id"] for x in active_clues}, name
    )
    for clue in active_clues:
        if clue["id"] not in otoshi_clue_ids:
            continue
        require_condition(
            clue["text"] in otoshi,
            f"{name}.otoshiに手掛かり{clue['id']}の本文がない",
        )
        require_condition(
            clue.get("directly_describes_target") is True,
            f"clues.{clue['id']}が対象を直接説明する手掛かりとして確認されていない",
        )
    required_text(item, "connective_scan", name)
    connective_forms = required_list(
        item.get("connective_forms"), f"{name}.connective_forms"
    )
    for index, connection in enumerate(connective_forms):
        cname = f"{name}.connective_forms[{index}]"
        require_condition(isinstance(connection, dict), f"{cname}が辞書ではない")
        for key in (
            "passage",
            "left_predication",
            "right_predication",
            "left_subject",
            "right_subject",
            "tense_aspect",
        ):
            required_text(connection, key, cname)
        require_condition(
            connection.get("relation")
            in {"parallel", "sequence", "reason", "contrast", "means", "condition"},
            f"{cname}.relationが不正である",
        )
        required_text(connection, "reason", cname)


def validate_work_state(state, stage):
    validate_execution_assignments(state, stage)
    required_text(state, "answer_target", "state")
    draft = state.get("draft")
    require_condition(isinstance(draft, dict), "draftがない")
    version = draft.get("version")
    require_condition(
        isinstance(version, int) and version >= 1, "draft.versionが不正である"
    )
    required_text(draft, "text", "draft")
    quote_ids, active_props, active_clues = validate_sources_propositions_and_clues(
        state, version, stage
    )
    terms, term_ids = records_with_ids(state.get("terms"), "terms")
    seen = set()
    for item in terms:
        name = f"terms.{item['id']}"
        value = required_text(item, "term", name)
        require_condition(value not in seen, "同じ専門用語が重複している")
        seen.add(value)
        required_text(item, "reason", name)
        referenced_ids(item, "evidence_ids", quote_ids, name)
        require_stage_completion(item, name, stage)
    answers, answer_ids = records_with_ids(
        state.get("answers"), "answers", nonempty=True
    )
    seen = set()
    for item in answers:
        name = f"answers.{item['id']}"
        value = required_text(item, "answer", name)
        judgment = item.get("judgment")
        require_condition(
            judgment in {"correct", "prompt", "incorrect"},
            f"{name}.judgmentが不正である",
        )
        require_condition((value, judgment) not in seen, "同じ解答候補が重複している")
        seen.add((value, judgment))
        required_text(item, "reason", name)
        referenced_ids(item, "evidence_ids", quote_ids, name)
        require_stage_completion(item, name, stage)
    checks, check_ids = records_with_ids(state.get("checks"), "checks", nonempty=True)
    require_condition(
        not (REQUIRED_CHECK_IDS - check_ids),
        f"必須検査がない: {sorted(REQUIRED_CHECK_IDS - check_ids)}",
    )
    for item in checks:
        name = f"checks.{item['id']}"
        require_condition(
            item.get("draft_version") == version, f"{name}の問題文の版が一致しない"
        )
        required_text(item, "claim", name)
        required_text(item, "reason", name)
        if item["id"] == "expression.naturalness":
            required_list(
                item.get("alternatives"), f"{name}.alternatives", nonempty=True
            )
            require_condition(
                len(item["alternatives"]) >= MIN_EXPRESSION_ALTERNATIVES,
                f"{name}.alternativesは二案以上必要である",
            )
        if item["id"] == "structure":
            validate_structure_check(item, name, draft["text"], active_clues)
        if item["id"] == "answer_exposure":
            required_list(item.get("blind_candidates"), f"{name}.blind_candidates")
            required_list(
                item.get("semantic_candidates"), f"{name}.semantic_candidates"
            )
            required_text(item, "target_knowledge_required", name)
        if item["id"] != "expression.naturalness":
            referenced_ids(item, "evidence_ids", quote_ids, name)
        require_stage_completion(item, name, stage)
    outputs, output_ids = records_with_ids(
        state.get("output_elements"), "output_elements", nonempty=True
    )
    require_condition(
        output_ids == REQUIRED_OUTPUT_IDS,
        f"出力要素が必須項目と一致しない: {sorted(REQUIRED_OUTPUT_IDS - output_ids)}",
    )
    for item in outputs:
        required_text(item, "content_ref", f"output_elements.{item['id']}")
        require_stage_completion(item, f"output_elements.{item['id']}", stage)
    if stage == "final":
        final = state.get("final_input")
        require_condition(isinstance(final, dict), "final_inputがない")
        require_condition(
            final.get("draft_version") == version, "final_inputの問題文の版が一致しない"
        )
        expected = {
            "proposition_ids": {x["id"] for x in active_props},
            "clue_ids": {x["id"] for x in active_clues},
            "term_ids": term_ids,
            "answer_ids": answer_ids,
            "output_element_ids": output_ids,
        }
        for key, ids in expected.items():
            require_condition(
                set(required_id_list(final.get(key), f"final_input.{key}")) == ids,
                f"final_input.{key}が検査済みの現行項目と一致しない",
            )


def main():
    parser = argparse.ArgumentParser(description="題材探索と作問状態を検査する")
    parser.add_argument("path", nargs="?")
    parser.add_argument(
        "--stage", choices=("selection", "generation", "audit", "final"), required=True
    )
    args = parser.parse_args()
    try:
        state = json.loads(
            Path(args.path).read_text(encoding="utf-8")
            if args.path
            else sys.stdin.read()
        )
    except (OSError, json.JSONDecodeError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    try:
        require_condition(
            isinstance(state, dict), "最上位はオブジェクトでなければならない"
        )
        if args.stage == "selection":
            validate_selection_state(state)
        else:
            validate_work_state(state, args.stage)
    except StateError as error:
        print(f"不合格: {error}", file=sys.stderr)
        return EXIT_STATE_INVALID
    print("状態の形式と参照関係の検査に合格")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
