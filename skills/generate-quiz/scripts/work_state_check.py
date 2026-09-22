#!/usr/bin/env python3
"""題材探索と作問状態の内容、参照関係、工程境界を検査する。

入力はJSONファイルのパスまたは標準入力から受け取る。--stageには
intersection-checkpoint、discovery、selection、
generation-start、difficulty、generation、audit、finalのいずれかを指定する。

終了コード:
    0  指定工程の条件を満たす
    1  読み込んだ状態が構造または指定工程の条件を満たさない
    2  JSONを読めない、または引数が不正

使用例:
    python3 work_state_check.py --stage selection selection.json
    python3 work_state_check.py --stage audit state.json
"""

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit

import facet_node

FINAL_HEADINGS = (
    "問題",
    "解答",
    "補足",
    "別解",
    "正誤判定基準",
    "題材選択",
    "難易度",
    "裏取り",
    "手掛かりの設計",
    "問題の成立性",
    "問題文の構成",
    "問題文の表現",
    "問題文の長さ",
    "解答と正誤判定",
    "参考文献",
)


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
    "clue_order": "手掛かりの設計",
    "expression.naturalness": "問題文の表現",
    "expression.comprehensibility": "問題文の表現",
    "expression.accuracy": "問題文の表現",
    "expression.incremental_comprehension": "問題文の表現",
    "length": "問題文の長さ",
    "answer_judging": "解答と正誤判定",
    "references": "参考文献",
}
MIN_ENTRY_POINTS = 2
MIN_ENTRY_POINT_KINDS = 2
MIN_COVERAGE_AREAS = 2
MIN_EXPRESSION_ALTERNATIVES = 2
MIN_INTERSECTION_EXAMPLES = 2
MIN_CANDIDATE_NAME_LENGTH = 2
MIN_EXPOSURE_DESCRIPTIONS = 2
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
    requires_target = item.get("formation_requires_target_association")
    require_condition(
        isinstance(requires_target, bool),
        f"{name}.formation_requires_target_associationがない",
    )
    component_requires_target = any(
        component.get("knowledge") == "target_association" for component in components
    )
    require_condition(
        requires_target == component_requires_target,
        f"{name}.formation_requires_target_associationが構成要素の分析と一致しない",
    )
    require_condition(
        isinstance(
            item.get("standard_name_confirmation_requires_target_association"), bool
        ),
        f"{name}.standard_name_confirmation_requires_target_associationがない",
    )
    if requires_target:
        required_text(item, "formation_target_association_step", name)
    return candidate_name, requires_target


def validate_exposure_precheck(item, name):
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
    descriptions = precheck["representative_descriptions"]
    require_condition(
        len(descriptions) == len(set(descriptions)),
        f"{check_name}.representative_descriptionsに同じ説明が重複している",
    )
    accepted_names = {
        normalize_candidate_name(value) for value in precheck["accepted_names"]
    }
    formations = required_list(
        precheck.get("formations"),
        f"{check_name}.formations",
        nonempty=True,
    )
    examined = set()
    exposed_descriptions = set()
    for index, formation in enumerate(formations):
        candidate_name, requires_target = validate_name_formation(
            formation, f"{check_name}.formations[{index}]"
        )
        formation_name = f"{check_name}.formations[{index}]"
        position = formation.get("description_index")
        require_condition(
            type(position) is int and 0 <= position < len(descriptions),
            f"{formation_name}.description_indexが不正である",
        )
        normalized_name = normalize_candidate_name(candidate_name)
        if normalized_name in accepted_names:
            pair = (normalized_name, position)
            require_condition(
                pair not in examined,
                f"{check_name}.formationsで同じ名称と説明の組合せが重複している",
            )
            examined.add(pair)
            if not requires_target:
                exposed_descriptions.add(position)
    require_condition(
        {
            (candidate_name, position)
            for candidate_name in accepted_names
            for position in range(len(descriptions))
        }
        <= examined,
        f"{check_name}で各説明案と正答名・別名の組合せを分析していない",
    )
    unavoidable = len(descriptions) >= MIN_EXPOSURE_DESCRIPTIONS and len(
        exposed_descriptions
    ) == len(descriptions)
    require_condition(
        precheck.get("status") == ("rejected" if unavoidable else "passed"),
        f"{check_name}.statusが名称形成の分析と一致しない",
    )
    return unavoidable


def validate_exposure_screen(item, entry_ids, name):
    screen = item.get("exposure_screen")
    require_condition(isinstance(screen, dict), f"{name}.exposure_screenがない")
    screen_name = f"{name}.exposure_screen"
    required_text(screen, "central_description", screen_name)
    referenced_ids(screen, "source_entry_point_ids", entry_ids, screen_name)
    require_condition(
        screen.get("formation_risk") in {"suspected", "none_detected"},
        f"{screen_name}.formation_riskが不正である",
    )
    required_text(screen, "reason", screen_name)
    return screen["formation_risk"]


def validate_intersection_state(state):
    """4軸の選択と交差領域の確認記録を検査する。"""
    nodes = state.get("facet_nodes")
    require_condition(
        isinstance(nodes, dict) and set(nodes) == {"subject", "place", "time", "type"},
        "facet_nodesに4軸の正規ノードキーがない",
    )
    for axis, key in nodes.items():
        require_condition(
            isinstance(key, str) and key.startswith(f"{axis}::"),
            f"facet_nodes.{axis}が不正である",
        )
        require_condition(
            facet_node.find_block(key)[1] is not None,
            f"facet_nodes.{axis}がカタログに存在しない",
        )
    review = state.get("intersection_review")
    require_condition(isinstance(review, dict), "intersection_reviewがない")
    execution = state.get("execution")
    require_condition(isinstance(execution, dict), "executionがない")
    available = execution.get("delegation_available")
    require_condition(
        isinstance(available, bool), "execution.delegation_availableがない"
    )
    if available:
        agents = execution.get("agents")
        require_condition(isinstance(agents, dict), "execution.agentsがない")
        reviewer_id = required_text(agents, "intersection", "execution.agents")
        require_condition(
            reviewer_id != "parent", "交差領域の確認を選択担当と分離していない"
        )
        assignments = execution.get("assignment_log")
        require_condition(
            isinstance(assignments, dict), "execution.assignment_logがない"
        )
        assignment = assignments.get("intersection")
        require_condition(
            isinstance(assignment, dict), "execution.assignment_log.intersectionがない"
        )
        require_condition(
            assignment.get("agent_id") == reviewer_id,
            "execution.assignment_log.intersection.agent_idが担当記録と一致しない",
        )
        require_condition(
            assignment.get("recorded_at_spawn") is True,
            "execution.assignment_log.intersectionが起動時に記録されていない",
        )
        required_list(
            assignment.get("artifact_refs"),
            "execution.assignment_log.intersection.artifact_refs",
            nonempty=True,
        )
    else:
        required_text(execution, "unavailable_reason", "execution")
    sources = required_id_list(
        review.get("source_refs"), "intersection_review.source_refs", nonempty=True
    )
    require_condition(
        len(sources) == len(set(sources)),
        "intersection_review.source_refsに同じ資料が重複している",
    )
    for source in sources:
        try:
            parsed = urlsplit(source)
            valid = (
                parsed.scheme in {"http", "https"}
                and parsed.hostname is not None
                and not any(char.isspace() for char in source)
            )
        except ValueError:
            valid = False
        require_condition(valid, "intersection_review.source_refsにURLでない値がある")
    examples = required_list(
        review.get("candidate_examples"),
        "intersection_review.candidate_examples",
        nonempty=True,
    )
    require_condition(
        len(examples) >= MIN_INTERSECTION_EXAMPLES,
        "intersection_review.candidate_examplesが二件に満たない",
    )
    beginner_count = 0
    candidate_names = set()
    for index, example in enumerate(examples):
        name = f"intersection_review.candidate_examples[{index}]"
        require_condition(isinstance(example, dict), f"{name}がオブジェクトではない")
        candidate = required_text(example, "name", name)
        candidate_names.add(unicodedata.normalize("NFKC", candidate).casefold())
        source = required_text(example, "source_ref", name)
        require_condition(source in sources, f"{name}.source_refが確認資料にない")
        if "beginner_source_ref" in example or "beginner_learning_basis" in example:
            beginner_source = required_text(example, "beginner_source_ref", name)
            require_condition(
                beginner_source in sources,
                f"{name}.beginner_source_refが確認資料にない",
            )
            required_text(example, "beginner_learning_basis", name)
            beginner_count += 1
    require_condition(
        len(candidate_names) >= MIN_INTERSECTION_EXAMPLES,
        "intersection_review.candidate_examplesに異なる候補が二件ない",
    )
    require_condition(
        beginner_count >= 1,
        "intersection_reviewに初級学習資料で確認した候補例がない",
    )
    required_text(review, "scope_reason", "intersection_review")
    require_condition(
        review.get("result") == "viable", "交差領域の独立確認が合格していない"
    )


def validate_selection_entries_areas(state, *, complete=True):
    entries, entry_ids = records_with_ids(
        state.get("entry_points"), "entry_points", nonempty=True
    )
    kinds = set()
    for item in entries:
        name = f"entry_points.{item['id']}"
        required_text(item, "label", name)
        kinds.add(required_text(item, "kind", name))
        source = required_text(item, "url", name)
        parsed = urlsplit(source)
        require_condition(
            parsed.scheme in {"http", "https"} and parsed.hostname is not None,
            f"{name}.urlがURLではない",
        )
        required_text(item, "access_note", name)
        require_condition(item.get("opened") is True, f"{name}の本文を開いていない")
    if complete:
        require_condition(
            len(entries) >= MIN_ENTRY_POINTS and len(kinds) >= MIN_ENTRY_POINT_KINDS,
            "異なる種類の入口を二つ以上使っていない",
        )
    areas, area_ids = records_with_ids(
        state.get("coverage_areas"), "coverage_areas", nonempty=True
    )
    if complete and len(areas) < MIN_COVERAGE_AREAS:
        required_text(state, "single_area_reason", "selection")
    for item in areas:
        name = f"coverage_areas.{item['id']}"
        required_text(item, "label", name)
        required_text(item, "basis", name)
        required_text(item, "target_kinds", name)
        if complete:
            require_condition(item.get("explored") is True, f"{name}が未探索である")
        used_entries = set(referenced_ids(item, "entry_point_ids", entry_ids, name))
        searches = required_list(
            item.get("source_searches"), f"{name}.source_searches", nonempty=True
        )
        opened_entries = set()
        open_searches = 0
        for index, search in enumerate(searches):
            search_name = f"{name}.source_searches[{index}]"
            require_condition(
                isinstance(search, dict), f"{search_name}がオブジェクトではない"
            )
            required_text(search, "query", search_name)
            required_text(search, "angle", search_name)
            required_text(search, "result", search_name)
            require_condition(
                search.get("mode") in {"open", "nearby"},
                f"{search_name}.modeが不正である",
            )
            source_ids = referenced_ids(
                search, "entry_point_ids", entry_ids, search_name, nonempty=False
            )
            opened_entries.update(source_ids)
            if search["mode"] == "open":
                require_condition(source_ids, f"{search_name}で入口を開いていない")
                open_searches += 1
            required_list(search.get("next_searches"), f"{search_name}.next_searches")
        if complete:
            require_condition(
                open_searches > 0, f"{name}で候補名を含めない入口探しがない"
            )
        require_condition(
            used_entries <= opened_entries, f"{name}の入口が探索記録にない"
        )
    return entries, entry_ids, areas, area_ids


def require_candidate_discovery_links(
    candidate, area_ids, entry_ids, discovered, *, allow_pending=False
):
    name = f"candidates.{candidate['id']}"
    candidate_areas = referenced_ids(candidate, "coverage_area_ids", area_ids, name)
    discovery_entries = referenced_ids(
        candidate,
        "discovery_entry_point_ids",
        entry_ids,
        name,
        nonempty=not allow_pending,
    )
    if allow_pending and not discovery_entries:
        require_condition(
            not discovered[candidate["id"]],
            f"{name}は発見記録があるのに発見元を記録していない",
        )
        return
    found_areas = {area_id for area_id, _ in discovered[candidate["id"]]}
    found_entries = {entry_id for _, entry_id in discovered[candidate["id"]]}
    require_condition(
        set(candidate_areas) <= found_areas and set(discovery_entries) <= found_entries,
        f"{name}の発見元・下位領域が探索記録と対応していない",
    )


def candidate_discovery_index(areas, candidate_ids):
    discovered = {candidate_id: set() for candidate_id in candidate_ids}
    for area in areas:
        for index, search in enumerate(area["source_searches"]):
            found_ids = referenced_ids(
                search,
                "found_candidate_ids",
                candidate_ids,
                f"coverage_areas.{area['id']}.source_searches[{index}]",
                nonempty=False,
            )
            for candidate_id in found_ids:
                discovered[candidate_id].update(
                    (area["id"], entry_id) for entry_id in search["entry_point_ids"]
                )
    return discovered


def validate_selection_candidates(
    state, entry_ids, areas, area_ids, *, discovery_only=False
):
    candidates, candidate_ids = records_with_ids(
        state.get("candidates"), "candidates", nonempty=True
    )
    discovered = candidate_discovery_index(areas, candidate_ids)
    for item in candidates:
        name = f"candidates.{item['id']}"
        required_text(item, "label", name)
        require_candidate_discovery_links(item, area_ids, entry_ids, discovered)
        required_text(item, "facet_membership_reason", name)
        disposition = item.get("disposition")
        require_condition(
            disposition in {"eligible", "excluded"}, f"{name}.dispositionが不正である"
        )
        if not (
            disposition == "excluded"
            and item.get("exclusion_code") == "unverified_name"
        ):
            required_text(item, "name_use_note", name)
        if "quality_rejection_reason" in item:
            require_condition(
                disposition == "eligible", f"{name}は探索段階で選択対象ではない"
            )
            required_text(item, "quality_rejection_reason", name)
        if disposition == "eligible":
            require_condition(
                item.get("expanded") is True, f"{name}から探索を展開していない"
            )
            searches = required_list(
                item.get("expansion_searches"),
                f"{name}.expansion_searches",
                nonempty=True,
            )
            for index, search in enumerate(searches):
                search_name = f"{name}.expansion_searches[{index}]"
                require_condition(
                    isinstance(search, dict), f"{search_name}がオブジェクトではない"
                )
                required_text(search, "source_or_query", search_name)
                required_text(search, "relation_checked", search_name)
                referenced_ids(
                    search,
                    "found_candidate_ids",
                    candidate_ids,
                    search_name,
                    nonempty=False,
                )
            if not discovery_only:
                risk = validate_exposure_screen(item, entry_ids, name)
                require_condition(
                    risk != "suspected" or item.get("exposure_precheck") is not None,
                    f"{name}は露出の疑いを詳細調査していない",
                )
                if item.get("exposure_precheck") is not None:
                    unavoidable = validate_exposure_precheck(item, name)
                    if risk == "suspected":
                        require_condition(
                            len(
                                item["exposure_precheck"]["representative_descriptions"]
                            )
                            >= MIN_EXPOSURE_DESCRIPTIONS,
                            f"{name}は異なる代表説明を十分に調べていない",
                        )
                    require_condition(
                        not unavoidable,
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
                    "unverified_name",
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
                    not discovery_only, f"{name}は露出予備検査前に除外できない"
                )
                require_condition(
                    validate_exposure_screen(item, entry_ids, name) == "suspected",
                    f"{name}は露出の疑いを記録していない",
                )
                require_condition(
                    validate_exposure_precheck(item, name),
                    f"{name}.exposure_precheckが解答露出による除外を示していない",
                )
    return candidates, candidate_ids


def validate_selection_review(state, entries, areas, candidates, entry_ids):
    area_ids = {item["id"] for item in areas}
    candidate_ids = {item["id"] for item in candidates}
    candidate_names = {
        normalize_candidate_name(item["label"])
        for item in candidates
        if len(normalize_candidate_name(item["label"])) >= MIN_CANDIDATE_NAME_LENGTH
    }
    for area in areas:
        for index, search in enumerate(area["source_searches"]):
            if search["mode"] != "open":
                continue
            query = normalize_candidate_name(search["query"])
            contained = {name for name in candidate_names if name in query}
            require_condition(
                not contained,
                f"coverage_areas.{area['id']}.source_searches[{index}]の入口検索に候補名がある",
            )
    reviews, review_ids = records_with_ids(
        state.get("independent_review"), "independent_review", nonempty=True
    )
    require_condition(
        review_ids == area_ids, "別経路の探索が全下位領域に対応していない"
    )
    completed_searches = {
        normalize_candidate_name(search["query"])
        for area in areas
        for search in area["source_searches"]
    }
    for review in reviews:
        name = f"independent_review.{review['id']}"
        required_text(review, "difference_from_exploration", name)
        query = required_text(review, "source_discovery_query", name)
        require_condition(
            not any(
                item in normalize_candidate_name(query) for item in candidate_names
            ),
            f"{name}の入口検索に候補名がある",
        )
        completed_searches.add(normalize_candidate_name(query))
        checked = set(
            referenced_ids(review, "checked_entry_point_ids", entry_ids, name)
        )
        area = next(item for item in areas if item["id"] == review["id"])
        require_condition(
            checked - set(area["entry_point_ids"]), f"{name}で別の入口を開いていない"
        )
        referenced_ids(
            review, "found_candidate_ids", candidate_ids, name, nonempty=False
        )
        spotchecked = set(
            referenced_ids(review, "spotchecked_entry_point_ids", entry_ids, name)
        )
        require_condition(
            spotchecked <= set(area["entry_point_ids"]),
            f"{name}の照合元が元の探索入口にない",
        )
        required_text(review, "spotcheck_result", name)
    challenge = state.get("saturation_challenge")
    require_condition(isinstance(challenge, dict), "saturation_challengeがない")
    required_text(challenge, "search_perspective", "saturation_challenge")
    challenge_query = required_text(challenge, "query", "saturation_challenge")
    completed_searches.add(normalize_candidate_name(challenge_query))
    referenced_ids(
        challenge, "opened_entry_point_ids", entry_ids, "saturation_challenge"
    )
    referenced_ids(
        challenge,
        "found_candidate_ids",
        candidate_ids,
        "saturation_challenge",
        nonempty=False,
    )
    required_text(challenge, "resolution", "saturation_challenge")
    require_condition(challenge.get("resolved") is True, "反証調査の結果が未処理である")
    opened_urls = {normalize_candidate_name(item["url"]) for item in entries}
    for area in areas:
        for index, search in enumerate(area["source_searches"]):
            for next_search in search["next_searches"]:
                require_condition(
                    isinstance(next_search, str)
                    and normalize_candidate_name(next_search)
                    in completed_searches | opened_urls,
                    f"coverage_areas.{area['id']}.source_searches[{index}]の次の検索先が未調査である",
                )


def validate_discovery_progress(state):
    validate_intersection_state(state)
    _, entry_ids, areas, area_ids = validate_selection_entries_areas(
        state, complete=False
    )
    candidates, candidate_ids = records_with_ids(state.get("candidates"), "candidates")
    discovered = candidate_discovery_index(areas, candidate_ids)
    for candidate in candidates:
        required_text(candidate, "label", f"candidates.{candidate['id']}")
        require_candidate_discovery_links(
            candidate, area_ids, entry_ids, discovered, allow_pending=True
        )


def validate_selection_state(state, *, discovery_only=False):
    validate_intersection_state(state)
    entries, entry_ids, areas, area_ids = validate_selection_entries_areas(state)
    candidates, candidate_ids = validate_selection_candidates(
        state, entry_ids, areas, area_ids, discovery_only=discovery_only
    )
    validate_selection_review(state, entries, areas, candidates, entry_ids)
    frontier = required_id_list(state.get("frontier_ids"), "frontier_ids")
    require_condition(
        not (set(frontier) - candidate_ids), "frontier_idsに存在しない候補がある"
    )
    require_condition(not frontier, "未展開の有力候補が残っている")
    require_condition(state.get("saturated") is True, "探索が飽和していない")


def validate_selection_mode(state):
    mode = state.get("selection_mode")
    require_condition(mode in {"random", "specified"}, "selection_modeが不正である")
    if mode == "specified":
        specified = required_text(state, "user_specified_target", "state")
        target = required_text(state, "answer_target", "state")
        require_condition(
            unicodedata.normalize("NFKC", specified)
            == unicodedata.normalize("NFKC", target),
            "指定された解答対象と作業対象が一致しない",
        )
    return mode


def validate_execution_assignments(state, stage, selection_mode="random"):
    data = state.get("execution")
    require_condition(isinstance(data, dict), "executionがない")
    available = data.get("delegation_available")
    require_condition(
        isinstance(available, bool), "execution.delegation_availableがない"
    )
    if available:
        if stage in {"generation", "audit", "final"}:
            exposure_assignments = required_list(
                data.get("exposure_assignments"),
                "execution.exposure_assignments",
                nonempty=True,
            )
            versions = set()
            agent_ids = set()
            for index, assignment in enumerate(exposure_assignments):
                name = f"execution.exposure_assignments[{index}]"
                require_condition(isinstance(assignment, dict), f"{name}がない")
                version = assignment.get("draft_version")
                require_condition(
                    type(version) is int and version >= 1,
                    f"{name}.draft_versionが不正である",
                )
                agent_id = required_text(assignment, "agent_id", name)
                required_text(assignment, "task_label", name)
                require_condition(
                    version not in versions, f"{name}.draft_versionが重複している"
                )
                require_condition(
                    agent_id not in agent_ids, f"{name}.agent_idを再利用している"
                )
                require_condition(
                    assignment.get("recorded_at_spawn") is True,
                    f"{name}が起動時に記録されていない",
                )
                versions.add(version)
                agent_ids.add(agent_id)
            draft = state.get("draft")
            draft_version = draft.get("version") if isinstance(draft, dict) else None
            assigned = data.get("agents")
            exposure_id = (
                assigned.get("exposure") if isinstance(assigned, dict) else None
            )
            require_condition(
                any(
                    assignment["draft_version"] == draft_version
                    and assignment["agent_id"] == exposure_id
                    for assignment in exposure_assignments
                ),
                "現行版の露出検査担当が版別記録と一致しない",
            )
        if selection_mode == "specified":
            selection_roles = ()
        elif stage == "discovery-progress":
            selection_roles = ("exploration",)
        else:
            selection_roles = (
                "exploration",
                "alternate_exploration",
                "saturation_review",
            )
        roles = (
            selection_roles
            + {
                "discovery-progress": (),
                "discovery": (),
                "selection": (),
                "generation-start": ("generation",),
                "difficulty": ("generation", "difficulty_review"),
                "generation": (
                    "generation",
                    "difficulty_review",
                    "terminology_review",
                    "exposure",
                ),
                "audit": (
                    "generation",
                    "difficulty_review",
                    "terminology_review",
                    "exposure",
                    "evidence_challenge",
                    "audit",
                ),
                "final": (
                    "generation",
                    "difficulty_review",
                    "terminology_review",
                    "exposure",
                    "evidence_challenge",
                    "audit",
                    "finalization",
                ),
            }[stage]
        )
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


def validate_source_quotes(state):
    sources, _ = records_with_ids(state.get("sources"), "sources", nonempty=True)
    quote_ids = set()
    for source in sources:
        required_text(source, "citation", f"sources.{source['id']}")
        if "url" in source:
            url = required_text(source, "url", f"sources.{source['id']}")
            require_condition(
                re.fullmatch(r"https?://\S+", url) is not None,
                f"sources.{source['id']}.urlが資料URLではない",
            )
        quotes, ids = records_with_ids(
            source.get("quotes"), f"sources.{source['id']}.quotes", nonempty=True
        )
        require_condition(not quote_ids & ids, "引用IDが資料間で重複している")
        quote_ids |= ids
        for quote in quotes:
            required_text(quote, "text", f"quotes.{quote['id']}")
            required_text(quote, "location", f"quotes.{quote['id']}")
    return quote_ids


def validate_competitor_comparisons(check, clue_text, quote_ids, name):
    competitors = required_list(
        check.get("competitors"), f"{name}.competitors", nonempty=True
    )
    for index, competitor in enumerate(competitors):
        cname = f"{name}.competitors[{index}]"
        require_condition(
            isinstance(competitor, dict), f"{cname}はオブジェクトでなければならない"
        )
        required_text(competitor, "name", cname)
        evidence = referenced_ids(competitor, "evidence_ids", quote_ids, cname)
        require_condition(
            set(evidence) <= set(check["evidence_ids"]),
            f"{cname}.evidence_idsが準一意性の引用に含まれていない",
        )
        conditions = required_list(
            competitor.get("conditions"), f"{cname}.conditions", nonempty=True
        )
        differences = set()
        for position, condition in enumerate(conditions):
            condition_name = f"{cname}.conditions[{position}]"
            require_condition(
                isinstance(condition, dict),
                f"{condition_name}はオブジェクトでなければならない",
            )
            passage = required_text(condition, "passage", condition_name)
            require_condition(
                passage in clue_text,
                f"{condition_name}.passageが手掛かり本文にない",
            )
            require_condition(
                isinstance(condition.get("matches"), bool),
                f"{condition_name}.matchesが真偽値ではない",
            )
            if not condition["matches"]:
                differences.add(passage)
            required_text(condition, "reason", condition_name)
            condition_evidence = referenced_ids(
                condition, "evidence_ids", quote_ids, condition_name
            )
            require_condition(
                set(condition_evidence) <= set(evidence),
                f"{condition_name}.evidence_idsが候補の引用に含まれていない",
            )
        disposition = competitor.get("disposition")
        require_condition(
            disposition in {"excluded", "same_target"},
            f"{cname}.dispositionが不正である",
        )
        if disposition == "excluded":
            exclusion = required_text(competitor, "exclusion_passage", cname)
            require_condition(
                exclusion in differences,
                f"{cname}.exclusion_passageが相違する条件ではない",
            )
        else:
            require_condition(
                not differences and "exclusion_passage" not in competitor,
                f"{cname}は同一対象の別名として扱う条件と矛盾している",
            )
        required_text(competitor, "reason", cname)


def validate_sources_propositions_and_clues(state, version, stage):
    quote_ids = validate_source_quotes(state)
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
                validate_competitor_comparisons(check, item["text"], quote_ids, cname)
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


def validate_difficulty_review(state, quote_ids, stage):
    review = state.get("difficulty_review")
    require_condition(isinstance(review, dict), "difficulty_reviewがない")
    knowledge = required_text(state, "asked_knowledge", "state")
    require_condition(
        review.get("asked_knowledge") == knowledge,
        "difficulty_review.asked_knowledgeが問う知識と一致しない",
    )
    execution = state["execution"]
    reviewer = (
        execution["agents"]["difficulty_review"]
        if execution["delegation_available"]
        else "self"
    )
    require_condition(
        review.get("reviewer_id") == reviewer,
        "difficulty_review.reviewer_idが担当記録と一致しない",
    )
    audit = review.get("audit")
    require_condition(
        audit in {"pending", "passed", "missing", "failed"},
        "difficulty_review.auditが不正である",
    )
    if stage in {"difficulty", "generation"}:
        require_condition(
            audit == "pending",
            "difficulty_reviewは生成工程の時点で監査済みになっている",
        )
    else:
        require_condition(audit == "passed", "difficulty_reviewが監査に合格していない")
    required_text(review, "answer_granularity", "difficulty_review")
    for group in ("beginner", "general"):
        item = review.get(group)
        name = f"difficulty_review.{group}"
        require_condition(isinstance(item, dict), f"{name}がない")
        require_condition(
            item.get("status") == "passed", f"{name}が独立検査に合格していない"
        )
        required_text(item, "reason", name)
        evidence_ids = referenced_ids(item, "evidence_ids", quote_ids, name)
        if group == "beginner":
            for aspect in ("name_learning", "relation_learning", "learning_connection"):
                learning = item.get(aspect)
                learning_name = f"{name}.{aspect}"
                require_condition(isinstance(learning, dict), f"{learning_name}がない")
                required_text(learning, "reason", learning_name)
                learning_evidence_ids = referenced_ids(
                    learning, "evidence_ids", quote_ids, learning_name
                )
                require_condition(
                    set(learning_evidence_ids) <= set(evidence_ids),
                    f"{learning_name}.evidence_idsが初学者側の根拠に含まれない",
                )
        if group == "general":
            paths = required_list(
                item.get("other_access_paths"),
                f"{name}.other_access_paths",
                nonempty=True,
            )
            for index, path in enumerate(paths):
                path_name = f"{name}.other_access_paths[{index}]"
                require_condition(isinstance(path, dict), f"{path_name}が不正である")
                required_text(path, "path", path_name)
                required_text(path, "search_record", path_name)
                outcome = path.get("outcome")
                require_condition(
                    outcome in {"confirmed", "not_confirmed"},
                    f"{path_name}.outcomeが不正である",
                )
                required_text(path, "result", path_name)
                referenced_ids(
                    path,
                    "evidence_ids",
                    quote_ids,
                    path_name,
                    nonempty=outcome == "confirmed",
                )
    return review


def validate_challenge_item(item, name, quote_ids):
    require_condition(isinstance(item, dict), f"{name}がない")
    urls = required_list(
        item.get("source_urls_checked"),
        f"{name}.source_urls_checked",
        nonempty=True,
    )
    require_condition(
        all(
            isinstance(url, str) and re.fullmatch(r"https?://\S+", url) for url in urls
        ),
        f"{name}.source_urls_checkedに資料URL以外がある",
    )
    required_text(item, "adverse_finding", name)
    referenced_ids(item, "resolution_evidence_ids", quote_ids, name)
    required_text(item, "resolution_reason", name)
    require_condition(item.get("status") == "passed", f"{name}.statusが合格していない")


def validate_evidence_challenge(state, quote_ids, active_clues, version):
    challenge = state.get("evidence_challenge")
    require_condition(isinstance(challenge, dict), "evidence_challengeがない")
    execution = state["execution"]
    reviewer = (
        execution["agents"]["evidence_challenge"]
        if execution["delegation_available"]
        else "self"
    )
    require_condition(
        challenge.get("reviewer_id") == reviewer,
        "evidence_challenge.reviewer_idが担当記録と一致しない",
    )
    require_condition(
        challenge.get("draft_version") == version,
        "evidence_challenge.draft_versionが問題文と一致しない",
    )
    require_condition(
        challenge.get("asked_knowledge")
        == required_text(state, "asked_knowledge", "state"),
        "evidence_challenge.asked_knowledgeが問う知識と一致しない",
    )

    for group in ("beginner", "general"):
        validate_challenge_item(
            challenge.get(group), f"evidence_challenge.{group}", quote_ids
        )
    clues, clue_ids = records_with_ids(
        challenge.get("clues"), "evidence_challenge.clues", nonempty=True
    )
    require_condition(
        clue_ids == {clue["id"] for clue in active_clues},
        "evidence_challenge.cluesが採用手掛かりと一致しない",
    )
    active_by_id = {clue["id"]: clue for clue in active_clues}
    for item in clues:
        name = f"evidence_challenge.clues.{item['id']}"
        validate_challenge_item(item, name, quote_ids)
        clue = active_by_id[item["id"]]
        generated = {
            candidate["name"]: candidate["disposition"]
            for candidate in clue["checks"]["quasi_uniqueness"]["competitors"]
        }
        comparisons = required_list(
            item.get("competitor_comparisons"),
            f"{name}.competitor_comparisons",
            nonempty=bool(generated),
        )
        names = set()
        for index, comparison in enumerate(comparisons):
            cname = f"{name}.competitor_comparisons[{index}]"
            require_condition(isinstance(comparison, dict), f"{cname}がない")
            candidate_name = required_text(comparison, "name", cname)
            require_condition(
                candidate_name not in names, f"{cname}.nameが重複している"
            )
            names.add(candidate_name)
            url = required_text(comparison, "source_url", cname)
            require_condition(
                url in item["source_urls_checked"],
                f"{cname}.source_urlが確認資料にない",
            )
            evidence_ids = referenced_ids(comparison, "evidence_ids", quote_ids, cname)
            require_condition(
                set(evidence_ids) <= set(item["resolution_evidence_ids"]),
                f"{cname}.evidence_idsが反証の解決根拠に含まれない",
            )
            conditions = required_list(
                comparison.get("conditions"), f"{cname}.conditions", nonempty=True
            )
            matches = []
            for position, condition in enumerate(conditions):
                condition_name = f"{cname}.conditions[{position}]"
                require_condition(
                    isinstance(condition, dict), f"{condition_name}がない"
                )
                passage = required_text(condition, "passage", condition_name)
                require_condition(
                    passage in clue["text"], f"{condition_name}.passageが手掛かりにない"
                )
                require_condition(
                    condition.get("match") in {"一致", "近接", "不一致"},
                    f"{condition_name}.matchが不正である",
                )
                matches.append(condition["match"])
                required_text(condition, "reason", condition_name)
            require_condition(
                comparison.get("disposition") in {"excluded", "same_target"},
                f"{cname}.dispositionが不正である",
            )
            if candidate_name in generated:
                require_condition(
                    comparison["disposition"] == generated[candidate_name],
                    f"{cname}.dispositionが生成側の判断と一致しない",
                )
            else:
                require_condition(
                    comparison["disposition"] == "excluded",
                    f"{cname}で新たな同一対象の候補が見つかっている",
                )
            if comparison["disposition"] == "excluded":
                require_condition(
                    "不一致" in matches,
                    f"{cname}は相違する条件なしに候補を除外している",
                )
            else:
                require_condition(
                    all(match == "一致" for match in matches),
                    f"{cname}は未一致の条件がある候補を同一対象としている",
                )
            required_text(comparison, "resolution_reason", cname)
            require_condition(
                comparison.get("remaining") is False, f"{cname}が未解決である"
            )
        require_condition(
            set(generated) <= names,
            f"{name}.competitor_comparisonsに生成側の対抗候補が不足している",
        )


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
    prefuri_segments = required_list(
        item.get("prefuri_segments"), f"{name}.prefuri_segments"
    )
    otoshi_start = draft_text.rfind(otoshi)
    for index, segment in enumerate(prefuri_segments):
        sname = f"{name}.prefuri_segments[{index}]"
        require_condition(isinstance(segment, dict), f"{sname}が辞書ではない")
        passage = required_text(segment, "passage", sname)
        require_condition(
            passage in draft_text[:otoshi_start],
            f"{sname}.passageが落としより前の問題文にない",
        )
        required_text(segment, "target_predication", sname)
        required_text(segment, "reason", sname)
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


def validate_final_input(state, version, active_props, active_clues, difficulty_review):
    final = state.get("final_input")
    require_condition(isinstance(final, dict), "final_inputがない")
    require_condition(
        final.get("draft_version") == version, "final_inputの問題文の版が一致しない"
    )
    clauses = required_list(
        final.get("relative_clauses"), "final_input.relative_clauses"
    )
    seen_passages = set()
    proposition_ids = {item["id"] for item in active_props}
    for index, clause in enumerate(clauses):
        name = f"final_input.relative_clauses[{index}]"
        require_condition(isinstance(clause, dict), f"{name}がオブジェクトではない")
        passage = required_text(clause, "passage", name)
        require_condition(
            passage in state["draft"]["text"], f"{name}.passageが問題文にない"
        )
        require_condition(passage not in seen_passages, f"{name}.passageが重複している")
        seen_passages.add(passage)
        required_text(clause, "reason", name)
        relation = clause.get("relation")
        require_condition(
            relation in {"inner", "outer"}, f"{name}.relationが不正である"
        )
        relation_ids = referenced_ids(
            clause,
            "relation_proposition_ids",
            proposition_ids,
            name,
            nonempty=relation == "outer",
        )
        require_condition(
            relation == "outer" or not relation_ids,
            f"{name}.relation_proposition_idsが内の関係にある",
        )
    expected = {
        "proposition_ids": proposition_ids,
        "clue_ids": {item["id"] for item in active_clues},
        "term_ids": {item["id"] for item in state["terms"]},
        "answer_ids": {item["id"] for item in state["answers"]},
        "output_element_ids": {item["id"] for item in state["output_elements"]},
    }
    for key, ids in expected.items():
        refs = required_id_list(final.get(key), f"final_input.{key}")
        require_condition(
            len(refs) == len(set(refs)) and set(refs) == ids,
            f"final_input.{key}が検査済みの現行項目と一致しない",
        )
    cited = set()
    for group in ("beginner", "general"):
        cited.update(difficulty_review[group]["evidence_ids"])
    for item in active_props:
        cited.update(item["evidence_ids"])
        for element in item.get("verification_elements", []):
            cited.update(element["evidence_ids"])
    for item in active_clues:
        for key in ("centrality", "quasi_uniqueness", "familiarity"):
            check = item["checks"][key]
            cited.update(check["evidence_ids"])
    for key in ("answers", "checks"):
        for item in state[key]:
            cited.update(item.get("evidence_ids", []))
    for key in ("answers", "candidate_reviews"):
        for item in state["answer_review"][key]:
            cited.update(item["evidence_ids"])
    for item in state["terms"]:
        if item["meaning_needed"]:
            cited.update(item["meaning_evidence_ids"])
            cited.update(item["audience_evidence_ids"])
    challenge = state["evidence_challenge"]
    for item in (challenge["beginner"], challenge["general"], *challenge["clues"]):
        cited.update(item["resolution_evidence_ids"])
        for comparison in item.get("competitor_comparisons", []):
            cited.update(comparison["evidence_ids"])
    quote_refs = required_id_list(final.get("quote_ids"), "final_input.quote_ids")
    require_condition(
        len(quote_refs) == len(set(quote_refs)) and set(quote_refs) == cited,
        "final_input.quote_idsが判断に用いた引用と一致しない",
    )
    validate_final_material(state, final, active_props, active_clues, cited)
    validate_topic_selection(state, final)


def validate_final_material(state, final, active_props, active_clues, cited):
    material = final.get("material")
    require_condition(isinstance(material, dict), "final_input.materialがない")
    require_condition(
        set(material) == REQUIRED_OUTPUT_IDS,
        "final_input.materialの出力項目が必須項目と一致しない",
    )
    for output_id in REQUIRED_OUTPUT_IDS:
        required_text(material, output_id, "final_input.material")
    require_condition(
        material["problem"] == state["draft"]["text"],
        "final_input.material.problemが現行版の問題文と一致しない",
    )
    require_condition(
        state["answer_target"] in material["answer"],
        "final_input.material.answerに解答対象がない",
    )
    require_condition(
        not re.search(r"もう一度|×", material["alternatives"]),
        "final_input.material.alternativesに正答以外の判定がある",
    )
    require_condition(
        not re.search(
            r"\b(?:ACCEPTANCE|DRAW|VERDICT|ACCEPT|REJECT)\b|抽選値|乱数値",
            material["length"],
            re.IGNORECASE,
        ),
        "final_input.material.lengthに判定器の内部表記がある",
    )
    for proposition in active_props:
        require_condition(
            proposition["passage"] in material["expression.accuracy"],
            f"final_input.material.expression.accuracyに命題{proposition['id']}の原文箇所がない",
        )
    for clause in final["relative_clauses"]:
        if clause["relation"] == "outer":
            require_condition(
                clause["passage"] in material["expression.accuracy"],
                "final_input.material.expression.accuracyに外の関係の連体修飾節がない",
            )
    quotes = {
        quote["id"]: (source["citation"], quote["location"], quote["text"])
        for source in state["sources"]
        for quote in source["quotes"]
    }
    all_material = "\n".join(material.values())
    for quote_id in cited:
        citation, location, text = quotes[quote_id]
        require_condition(
            text in all_material,
            f"final_input.materialに採用引用{quote_id}の本文がない",
        )
        require_condition(
            citation in all_material and location in all_material,
            f"final_input.materialに採用引用{quote_id}の書誌または所在がない",
        )
    adopted_texts = {quotes[quote_id][2] for quote_id in cited}
    for quote_id, (_, _, text) in quotes.items():
        if quote_id not in cited and text not in adopted_texts:
            require_condition(
                text not in all_material,
                f"final_input.materialに不採用の引用{quote_id}がある",
            )
    evidence_by_output = {
        "difficulty.beginner": set(
            state["difficulty_review"]["beginner"]["evidence_ids"]
        ),
        "difficulty.general": set(
            state["difficulty_review"]["general"]["evidence_ids"]
        ),
        "verification": {
            quote_id for item in active_props for quote_id in item["evidence_ids"]
        },
        "clues": {
            quote_id
            for clue in active_clues
            for key in ("centrality", "quasi_uniqueness", "familiarity")
            for quote_id in clue["checks"][key]["evidence_ids"]
        },
        "answer_exposure": {
            quote_id
            for item in state["checks"]
            if item["id"] == "answer_exposure"
            for quote_id in item["evidence_ids"]
        },
        "answer_judging": {
            quote_id for item in state["answers"] for quote_id in item["evidence_ids"]
        },
    }
    for output_id, evidence_ids in evidence_by_output.items():
        if evidence_ids:
            require_condition(
                any(
                    quotes[quote_id][0] in material[output_id]
                    and quotes[quote_id][1] in material[output_id]
                    for quote_id in evidence_ids
                ),
                f"final_input.material.{output_id}に判断根拠の所在がない",
            )


def validate_topic_selection(state, final):
    topic = final.get("topic_selection")
    require_condition(isinstance(topic, dict), "final_input.topic_selectionがない")
    require_condition(
        topic.get("answer_target") == state["answer_target"],
        "final_input.topic_selection.answer_targetが解答対象と一致しない",
    )
    content = final["material"]["topic_selection"]
    require_condition(
        state["answer_target"] in content,
        "final_input.material.topic_selectionに解答対象がない",
    )
    history = required_text(topic, "history_result", "final_input.topic_selection")
    require_condition(
        history in content,
        "final_input.material.topic_selectionに履歴補正の適用結果がない",
    )
    if state["selection_mode"] == "random":
        nodes = state.get("facet_nodes")
        require_condition(isinstance(nodes, dict), "facet_nodesがない")
        require_condition(
            topic.get("facet_nodes") == nodes,
            "final_input.topic_selection.facet_nodesが選択結果と一致しない",
        )
        paths = topic.get("facet_paths")
        require_condition(
            isinstance(paths, dict), "final_input.topic_selection.facet_pathsがない"
        )
        for axis in ("subject", "place", "time", "type"):
            path = required_text(paths, axis, "final_input.topic_selection.facet_paths")
            require_condition(
                path in content,
                f"final_input.material.topic_selectionに{axis}の分類経路がない",
            )
    else:
        require_condition(
            "facet_paths" not in topic,
            "final_input.topic_selection.facet_pathsがユーザー指定の題材にある",
        )
    require_condition(
        not re.search(
            r"重み付きで選択|抽選過程|候補台帳|候補から選|(?:subject|place|time|type)::|\bROOT\b",
            content,
        ),
        "final_input.material.topic_selectionに抽選過程または内部ノードIDがある",
    )


def validate_final_sections(output, state):
    """完成稿の見出し、問題、解答と作業用情報の混入を確認する。"""
    headings = list(re.finditer(r"^##[ \t]+([^\n]+)$", output, re.MULTILINE))
    names = [match.group(1).strip() for match in headings]
    require_condition(
        names == list(FINAL_HEADINGS), "最終出力の見出しに欠落・重複・順序違いがある"
    )
    require_condition(
        not output[: headings[0].start()].strip(), "最終出力の先頭に作業用記録がある"
    )
    sections = {}
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(output)
        body = output[match.end() : end].strip()
        require_condition(bool(body), f"最終出力の「{names[index]}」が空である")
        sections[names[index]] = body
    require_condition(
        re.sub(r"\s+", "", sections["問題"])
        == re.sub(r"\s+", "", state["draft"]["text"]),
        "最終出力の問題文が現行版と一致しない",
    )
    require_condition(
        state["answer_target"] in sections["解答"], "最終出力の解答に解答対象がない"
    )
    require_condition(
        re.sub(r"\s+", "", sections["題材選択"])
        == re.sub(r"\s+", "", state["final_input"]["material"]["topic_selection"]),
        "最終出力の題材選択が最終入力と一致しない",
    )
    require_condition(
        not re.search(r"(?:subject|place|time|type)::[^\s、。）」]+", output),
        "最終出力に内部ノードIDがある",
    )
    for output_id, heading in OUTPUT_HEADINGS.items():
        expected = state["final_input"]["material"][output_id]
        require_condition(
            re.sub(r"\s+", "", expected) in re.sub(r"\s+", "", sections[heading]),
            f"最終出力の{heading}に最終入力の{output_id}がない",
        )


def urls_in_text(text):
    return {
        match.rstrip('.,。)）」]>"')
        for match in re.findall(r"https?://[^\s<>、，。]+", text)
    }


def validate_final_source_urls(output, state):
    adopted = set(state["final_input"]["quote_ids"])
    allowed = set()
    for source in state["sources"]:
        if not any(quote["id"] in adopted for quote in source["quotes"]):
            continue
        if source.get("url"):
            allowed.add(source["url"])
        allowed.update(urls_in_text(source["citation"]))
    urls = urls_in_text(output)
    require_condition(
        urls <= allowed,
        f"最終入力にない資料を完成稿で参照している: {sorted(urls - allowed)}",
    )
    require_condition(
        allowed <= urls,
        f"採用引用の資料URLが完成稿にない: {sorted(allowed - urls)}",
    )


def validate_final_review(state, output_bytes):
    review = state.get("final_review")
    require_condition(isinstance(review, dict), "final_reviewがない")
    require_condition(
        review.get("status") == "passed", "最終出力の照合が合格していない"
    )
    execution = state["execution"]
    reviewer = (
        execution["agents"]["audit"] if execution["delegation_available"] else "self"
    )
    require_condition(
        review.get("reviewer_id") == reviewer,
        "final_review.reviewer_idが監査担当と一致しない",
    )
    require_condition(
        review.get("output_sha256") == hashlib.sha256(output_bytes).hexdigest(),
        "final_review.output_sha256が完成稿と一致しない",
    )


def validate_terminology(state, quote_ids, version, stage, draft_text):
    terms, _ = records_with_ids(state.get("terms"), "terms")
    seen = set()
    for item in terms:
        name = f"terms.{item['id']}"
        value = required_text(item, "term", name)
        require_condition(value not in seen, "同じ専門用語が重複している")
        require_condition(value in draft_text, f"{name}.termが問題文にない")
        seen.add(value)
        meaning_needed = item.get("meaning_needed")
        require_condition(
            isinstance(meaning_needed, bool), f"{name}.meaning_neededがない"
        )
        if meaning_needed:
            required_text(item, "meaning_reason", name)
            referenced_ids(item, "meaning_evidence_ids", quote_ids, name)
            required_text(item, "audience_reason", name)
            referenced_ids(item, "audience_evidence_ids", quote_ids, name)
        else:
            required_text(item, "understanding_without_meaning", name)
        require_stage_completion(item, name, stage)
    review = state.get("terminology_review")
    require_condition(isinstance(review, dict), "terminology_reviewがない")
    execution = state["execution"]
    reviewer = (
        execution["agents"]["terminology_review"]
        if execution["delegation_available"]
        else "self"
    )
    require_condition(
        review.get("reviewer_id") == reviewer,
        "terminology_review.reviewer_idが担当記録と一致しない",
    )
    require_condition(
        review.get("draft_version") == version,
        "terminology_review.draft_versionが問題文と一致しない",
    )
    audit = review.get("audit")
    require_condition(
        audit in {"pending", "passed", "missing", "failed"},
        "terminology_review.auditが不正である",
    )
    if stage == "generation":
        require_condition(
            audit == "pending",
            "terminology_reviewは生成工程の時点で監査済みになっている",
        )
    else:
        require_condition(audit == "passed", "terminology_reviewが監査に合格していない")
    reviewed, reviewed_ids = records_with_ids(
        review.get("terms"), "terminology_review.terms"
    )
    required_ids = {item["id"] for item in terms}
    require_condition(
        reviewed_ids == required_ids,
        "terminology_review.termsが専門用語の記録と一致しない",
    )
    term_by_id = {item["id"]: item for item in terms}
    for item in reviewed:
        name = f"terminology_review.terms.{item['id']}"
        term = term_by_id[item["id"]]
        require_condition(
            required_text(item, "term", name) == term["term"],
            f"{name}.termが生成側の専門用語と一致しない",
        )
        require_condition(
            isinstance(item.get("meaning_needed"), bool),
            f"{name}.meaning_neededがない",
        )
        require_condition(
            item["meaning_needed"] == term["meaning_needed"],
            f"{name}.meaning_neededが生成側の判断と一致しない",
        )
        if not item["meaning_needed"]:
            required_text(item, "understanding_without_meaning", name)
            continue
        for kind in ("meaning", "audience"):
            require_condition(
                item.get(f"{kind}_status") == "passed",
                f"{name}.{kind}_statusが合格していない",
            )
            required_text(item, f"{kind}_reason", name)
            evidence = referenced_ids(item, f"{kind}_evidence_ids", quote_ids, name)
            require_condition(
                set(evidence) == set(term[f"{kind}_evidence_ids"]),
                f"{name}.{kind}_evidence_idsが採用引用と一致しない",
            )


def validate_exposure_review(state, checks, answers, version):
    exposure_review = state.get("exposure_review")
    require_condition(isinstance(exposure_review, dict), "exposure_reviewがない")
    execution = state["execution"]
    reviewer_id = (
        execution["agents"]["audit"] if execution["delegation_available"] else "self"
    )
    require_condition(
        exposure_review.get("reviewer_id") == reviewer_id,
        "exposure_review.reviewer_idが監査担当と一致しない",
    )
    require_condition(
        exposure_review.get("draft_version") == version,
        "exposure_review.draft_versionが問題文と一致しない",
    )
    require_condition(
        exposure_review.get("question_sha256")
        == hashlib.sha256(state["draft"]["text"].encode()).hexdigest(),
        "exposure_review.question_sha256が問題文と一致しない",
    )
    correct_answers = {item["id"] for item in answers if item["judgment"] == "correct"}
    checked = required_id_list(
        exposure_review.get("checked_answer_ids"),
        "exposure_review.checked_answer_ids",
    )
    require_condition(
        set(checked) == correct_answers,
        "exposure_review.checked_answer_idsが正答範囲と一致しない",
    )
    require_condition(
        exposure_review.get("status") == "passed", "exposure_reviewが合格していない"
    )
    candidates = required_list(
        exposure_review.get("candidates"), "exposure_review.candidates"
    )
    if not candidates:
        required_text(exposure_review, "no_candidate_reason", "exposure_review")
    correct_names = {
        normalize_candidate_name(item["answer"])
        for item in answers
        if item["judgment"] == "correct"
    }
    exposure_check = next(item for item in checks if item["id"] == "answer_exposure")
    recorded_names = {
        normalize_candidate_name(candidate["name"])
        for key in ("blind_candidates", "semantic_candidates")
        for candidate in exposure_check[key]
    }
    for index, candidate in enumerate(candidates):
        cname = f"exposure_review.candidates[{index}]"
        name, requires_target = validate_name_formation(candidate, cname)
        normalized = normalize_candidate_name(name)
        require_condition(
            normalized not in correct_names or requires_target,
            f"{cname}は正答名と一致し、対象との対応知識なしに形成できる",
        )
        require_condition(
            normalized in recorded_names, f"{cname}が露出検査に反映されていない"
        )


def validate_exposure_assignment_secrecy(execution, answers):
    if not execution["delegation_available"]:
        return
    assignment = execution["assignment_log"]["exposure"]
    metadata_values = (
        execution["agents"]["exposure"],
        assignment["agent_id"],
        required_text(assignment, "task_label", "execution.assignment_log.exposure"),
        *assignment["artifact_refs"],
        *(item["task_label"] for item in execution["exposure_assignments"]),
    )
    correct_names = {
        normalize_candidate_name(item["answer"])
        for item in answers
        if item["judgment"] == "correct"
    }
    for value in metadata_values:
        require_condition(isinstance(value, str), "露出検査担当の識別情報が不正である")
        normalized_value = normalize_candidate_name(value)
        require_condition(
            all(name not in normalized_value for name in correct_names),
            "露出検査担当の識別子・依頼名・成果物経路に正答名が含まれている",
        )


def validate_answers(state, quote_ids, stage):
    answers, _ = records_with_ids(state.get("answers"), "answers", nonempty=True)
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
    return answers


def validate_reviewed_answer(item, name, quote_ids):
    require_condition(item.get("status") == "passed", f"{name}.statusが合格していない")
    judgment = item.get("judgment")
    require_condition(
        judgment in {"correct", "prompt", "incorrect"},
        f"{name}.judgmentが不正である",
    )
    required_text(item, "reason", name)
    referenced_ids(item, "evidence_ids", quote_ids, name)
    for key in ("same_target", "specified_enough", "clear_error", "scope_matches"):
        require_condition(isinstance(item.get(key), bool), f"{name}.{key}がない")
    if judgment == "correct":
        require_condition(
            item["same_target"]
            and item["specified_enough"]
            and item["scope_matches"]
            and not item["clear_error"],
            f"{name}の正答判定と対象・指定・適用範囲が一致しない",
        )
    elif judgment == "prompt":
        require_condition(
            item["same_target"]
            and not item["specified_enough"]
            and item["scope_matches"]
            and not item["clear_error"],
            f"{name}の聞き返し判定と指定の不足が一致しない",
        )
    else:
        require_condition(
            not item["same_target"] or item["clear_error"] or not item["scope_matches"],
            f"{name}の誤答判定に対象・適用範囲の相違がない",
        )
    return judgment


def validate_answer_review(state, answers, checks, quote_ids, version):
    review = state.get("answer_review")
    require_condition(isinstance(review, dict), "answer_reviewがない")
    execution = state["execution"]
    reviewer = (
        execution["agents"]["exposure"] if execution["delegation_available"] else "self"
    )
    require_condition(
        review.get("reviewer_id") == reviewer,
        "answer_review.reviewer_idが露出検査担当と一致しない",
    )
    require_condition(
        review.get("draft_version") == version,
        "answer_review.draft_versionが問題文と一致しない",
    )
    reviewed, reviewed_ids = records_with_ids(
        review.get("answers"), "answer_review.answers", nonempty=True
    )
    by_id = {item["id"]: item for item in answers}
    require_condition(
        reviewed_ids == set(by_id),
        "answer_review.answersが解答候補と一致しない",
    )
    for item in reviewed:
        name = f"answer_review.answers.{item['id']}"
        judgment = validate_reviewed_answer(item, name, quote_ids)
        require_condition(
            judgment == by_id[item["id"]]["judgment"],
            f"{name}.judgmentが採用判定と一致しない",
        )
    exposure = next(item for item in checks if item["id"] == "answer_exposure")
    names = {
        normalize_candidate_name(item["name"])
        for key in ("blind_candidates", "semantic_candidates")
        for item in exposure[key]
    }
    candidates = required_list(
        review.get("candidate_reviews"), "answer_review.candidate_reviews"
    )
    seen = set()
    adopted = {
        normalize_candidate_name(item["answer"]): item["judgment"] for item in answers
    }
    for index, candidate in enumerate(candidates):
        name = f"answer_review.candidate_reviews[{index}]"
        require_condition(isinstance(candidate, dict), f"{name}がない")
        value = normalize_candidate_name(required_text(candidate, "name", name))
        require_condition(value not in seen, f"{name}.nameが重複している")
        seen.add(value)
        judgment = validate_reviewed_answer(candidate, name, quote_ids)
        require_condition(
            value in adopted or judgment != "correct",
            f"{name}の正答名が解答範囲にない",
        )
        require_condition(
            value not in adopted or judgment == adopted[value],
            f"{name}.judgmentが採用判定と一致しない",
        )
    require_condition(
        seen == names, "answer_review.candidate_reviewsが露出候補と一致しない"
    )


def validate_output_elements(state, stage):
    outputs, output_ids = records_with_ids(
        state.get("output_elements"), "output_elements", nonempty=True
    )
    require_condition(
        output_ids == REQUIRED_OUTPUT_IDS,
        f"出力要素が必須項目と一致しない: {sorted(REQUIRED_OUTPUT_IDS - output_ids)}",
    )
    for item in outputs:
        name = f"output_elements.{item['id']}"
        content_ref = required_text(item, "content_ref", name)
        if stage in {"audit", "final"}:
            require_condition(
                content_ref == f"final_input.material.{item['id']}",
                f"{name}.content_refが最終入力を指していない",
            )
        require_stage_completion(item, name, stage)


def validate_work_state(state, stage):
    require_no_selection_ledger(state)
    if stage == "generation":
        require_condition(
            "evidence_challenge" not in state,
            "生成工程の状態に監査前の反証確認が混入している",
        )
    selection_mode = validate_selection_mode(state)
    validate_execution_assignments(state, stage, selection_mode)
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
    difficulty_review = validate_difficulty_review(state, quote_ids, stage)
    if stage in {"audit", "final"}:
        validate_evidence_challenge(state, quote_ids, active_clues, version)
    validate_terminology(state, quote_ids, version, stage, draft["text"])
    answers = validate_answers(state, quote_ids, stage)
    validate_exposure_assignment_secrecy(state["execution"], answers)
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
        if item["id"] in {"difficulty.beginner", "difficulty.general"}:
            require_condition(
                item.get("asked_knowledge") == state["asked_knowledge"],
                f"{name}.asked_knowledgeが問う知識と一致しない",
            )
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
            blind = required_list(
                item.get("blind_candidates"), f"{name}.blind_candidates"
            )
            semantic = required_list(
                item.get("semantic_candidates"), f"{name}.semantic_candidates"
            )
            required_text(item, "target_knowledge_required", name)
            correct = {
                normalize_candidate_name(answer["answer"])
                for answer in answers
                if answer.get("judgment") == "correct"
            }
            for key, candidates in (
                ("blind_candidates", blind),
                ("semantic_candidates", semantic),
            ):
                for index, candidate in enumerate(candidates):
                    cname = f"{name}.{key}[{index}]"
                    candidate_name, requires_target = validate_name_formation(
                        candidate, cname
                    )
                    require_condition(
                        normalize_candidate_name(candidate_name) not in correct
                        or requires_target,
                        f"{cname}は正解と一致し、対象との対応知識なしに名称候補を形成できる",
                    )
        if item["id"] != "expression.naturalness":
            referenced_ids(item, "evidence_ids", quote_ids, name)
        require_stage_completion(item, name, stage)
    validate_answer_review(state, answers, checks, quote_ids, version)
    if stage in {"audit", "final"}:
        validate_exposure_review(state, checks, answers, version)
    validate_output_elements(state, stage)
    if stage in {"audit", "final"}:
        validate_final_input(
            state, version, active_props, active_clues, difficulty_review
        )


def validate_difficulty_checkpoint(state):
    selection_mode = validate_selection_mode(state)
    validate_execution_assignments(state, "difficulty", selection_mode)
    required_text(state, "answer_target", "state")
    quote_ids = validate_source_quotes(state)
    validate_difficulty_review(state, quote_ids, "difficulty")


def require_no_selection_ledger(state):
    selection_fields = {
        "entry_points",
        "coverage_areas",
        "candidates",
        "independent_review",
        "saturation_challenge",
        "frontier_ids",
        "saturated",
    }
    require_condition(
        not selection_fields.intersection(state),
        "解答対象ごとの作業状態に題材探索台帳が混入している",
    )


def validate_generation_start(state):
    require_no_selection_ledger(state)
    selection_mode = validate_selection_mode(state)
    validate_execution_assignments(state, "generation-start", selection_mode)
    required_text(state, "answer_target", "state")


def main():
    parser = argparse.ArgumentParser(description="題材探索と作問状態を検査する")
    parser.add_argument("path", nargs="?")
    parser.add_argument(
        "--stage",
        choices=(
            "intersection-checkpoint",
            "discovery-progress",
            "discovery",
            "selection",
            "generation-start",
            "difficulty",
            "generation",
            "audit",
            "final",
        ),
        required=True,
    )
    parser.add_argument("--output")
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
        if args.stage == "intersection-checkpoint":
            validate_intersection_state(state)
        elif args.stage == "discovery-progress":
            validate_discovery_progress(state)
            validate_execution_assignments(state, "discovery-progress")
        elif args.stage in {"discovery", "selection"}:
            validate_selection_state(state, discovery_only=args.stage == "discovery")
            validate_execution_assignments(state, args.stage)
        elif args.stage == "generation-start":
            validate_generation_start(state)
        elif args.stage == "difficulty":
            validate_difficulty_checkpoint(state)
        elif args.stage == "final":
            require_condition(args.output, "final段階には--outputが必要である")
            output_bytes = Path(args.output).read_bytes()
            output = output_bytes.decode("utf-8")
            validate_work_state(state, args.stage)
            for source in state["sources"]:
                for quote in source["quotes"]:
                    if quote["id"] in state["final_input"]["quote_ids"]:
                        require_condition(
                            quote["text"] in output,
                            f"最終出力に引用{quote['id']}がない",
                        )
            validate_final_sections(output, state)
            validate_final_source_urls(output, state)
            validate_final_review(state, output_bytes)
        else:
            validate_work_state(state, args.stage)
    except (OSError, UnicodeError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    except StateError as error:
        print(f"不合格: {error}", file=sys.stderr)
        return EXIT_STATE_INVALID
    print("状態の形式と参照関係の検査に合格")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
