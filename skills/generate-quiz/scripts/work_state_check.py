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
import sys
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
        require_condition(
            item.get("expanded") is True, f"{name}から探索を展開していない"
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
            require_stage_completion(check, cname, stage)
    require_condition(active_clues, "activeな手掛かりがない")
    return quote_ids, active_props, active_clues


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
    print("合格")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
