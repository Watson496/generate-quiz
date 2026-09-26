#!/usr/bin/env python3
"""題材探索と作問状態の内容、参照関係、工程境界を検査する。

入力はJSONファイルのパスまたは標準入力から受け取る。--stageには
facet-selection、intersection-checkpoint、discovery、membership、selection、prejudgment、
target-start、writing、review、material、finalのいずれかを指定する。

終了コード:
    0  指定工程の条件を満たす
    1  読み込んだ状態が構造または指定工程の条件を満たさない
    2  JSONを読めない、または引数が不正

使用例:
    python3 work_state_check.py --stage selection selection.json
    python3 work_state_check.py --stage review state.json
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

import assignment_plan
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
    "clue_order": "問題文の構成",
    "expression.naturalness": "問題文の表現",
    "expression.comprehensibility": "問題文の表現",
    "expression.accuracy": "問題文の表現",
    "expression.incremental_comprehension": "問題文の表現",
    "length": "問題文の長さ",
    "answer_judging": "解答と正誤判定",
    "references": "参考文献",
}


def step_roles(*names):
    """担当表で指定したステップに置く担当のIDを、表の順に返す。"""
    return tuple(
        role["id"]
        for step in assignment_plan.load_table()["steps"]
        if step["name"] in names
        for role in step["roles"]
    )


REVIEWED_STAGES = {"review", "material", "final"}
FINAL_REVIEW_ROLES = ("final_reflection_review", "final_contamination_review")
FACET_AXES = ("subject", "place", "time", "type")
FACET_VIEWPOINTS = ("sharing", "communication", "background")
PREJUDGMENT_KEYS = (
    "prejudgment_scope",
    "prejudgment_membership",
    "prejudgment_difficulty",
    "prejudgment_otoshi",
)
SELECTION_ROLES = (
    "exploration",
    "nearby_exploration",
    "alternate_exploration",
    "saturation_review",
)
STAGE_ROLES = {
    "facet-selection": (
        "facet_granularity",
        "facet_weighting",
        "facet_granularity_review",
        "facet_weight_review",
        "facet_distribution_review",
    ),
    "intersection-checkpoint": ("intersection",),
    "discovery-progress": ("intersection", "exploration"),
    "discovery": ("intersection", *SELECTION_ROLES),
    "membership": ("intersection", *SELECTION_ROLES, "membership", "membership_review"),
    "selection": (
        "intersection",
        *SELECTION_ROLES,
        "membership",
        "membership_review",
        "exposure_precheck",
        "topic_grouping",
        "topic_group_review",
        "topic_weighting",
        "topic_weight_review",
        "topic_distribution_review",
    ),
    "prejudgment": (
        "intersection",
        *SELECTION_ROLES,
        "membership",
        "membership_review",
        "exposure_precheck",
        "topic_grouping",
        "topic_group_review",
        "topic_weighting",
        "topic_weight_review",
        "topic_distribution_review",
        *PREJUDGMENT_KEYS,
    ),
    "target-start": (),
    "writing": step_roles("素材の調査", "作文"),
    "review": step_roles("素材の調査", "作文", "検査"),
    "material": (*step_roles("素材の調査", "作文", "検査"), "material_writer"),
    "final": step_roles("素材の調査", "作文", "検査", "最終出力"),
}
MIN_ENTRY_POINTS = 2
MIN_COVERAGE_AREAS = 2
MIN_EXPRESSION_ALTERNATIVES = 2
MIN_INTERSECTION_EXAMPLES = 2
MIN_SUBDIVISION_CHILDREN = 2
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
            component.get("knowledge") in {"surface", "audience_known", "answer_side"},
            f"{component_name}.knowledgeが不正である",
        )
        if component["knowledge"] == "answer_side":
            required_text(component, "answer_side_reason", component_name)
    requires_answer_side = item.get("formation_requires_answer_side_knowledge")
    require_condition(
        isinstance(requires_answer_side, bool),
        f"{name}.formation_requires_answer_side_knowledgeがない",
    )
    component_requires_answer_side = any(
        component.get("knowledge") == "answer_side" for component in components
    )
    require_condition(
        requires_answer_side == component_requires_answer_side,
        f"{name}.formation_requires_answer_side_knowledgeが構成要素の分析と一致しない",
    )
    require_condition(
        isinstance(
            item.get("standard_name_confirmation_requires_answer_side_knowledge"),
            bool,
        ),
        f"{name}.standard_name_confirmation_requires_answer_side_knowledgeがない",
    )
    return candidate_name, requires_answer_side


def validate_reviews(state, key, expected_ids, id_field):
    """検査担当の記録が対象の項目ごとにあり、最後の判定がすべて合格であることを確認する。"""
    reviews = required_list(state.get(key), key, nonempty=bool(expected_ids))
    latest = {}
    for index, item in enumerate(reviews):
        name = f"{key}[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        target = required_text(item, id_field, name)
        require_condition(
            item.get("status") in {"passed", "failed"}, f"{name}.statusが不正である"
        )
        required_text(item, "reason", name)
        if item["status"] == "failed":
            fix_data = required_id_list(
                item.get("fix_data"), f"{name}.fix_data", nonempty=True
            )
            unknown = sorted(set(fix_data) - set(assignment_plan.load_table()["data"]))
            require_condition(
                not unknown,
                f"{name}.fix_dataが担当表にないデータを参照している: {unknown}",
            )
        latest[target] = item["status"]
    missing = sorted(set(expected_ids) - set(latest))
    require_condition(not missing, f"{key}に検査のない項目がある: {missing}")
    failed = sorted(
        target for target in set(expected_ids) if latest[target] != "passed"
    )
    require_condition(not failed, f"{key}に不合格の項目がある: {failed}")


def is_url(value):
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    return (
        parsed.scheme in {"http", "https"}
        and parsed.hostname is not None
        and not any(char.isspace() for char in value)
    )


def validate_weight_record(item, name, *, positive):
    """weightと三観点の評価、根拠、履歴距離を検査する。"""
    require_condition(isinstance(item, dict), f"{name}はオブジェクトでなければならない")
    weight = item.get("weight")
    require_condition(
        type(weight) in {int, float} and (weight > 0 if positive else weight >= 0),
        f"{name}.weightが{'正' if positive else '0以上'}の数ではない",
    )
    viewpoints = item.get("viewpoints")
    require_condition(isinstance(viewpoints, dict), f"{name}.viewpointsがない")
    for viewpoint in FACET_VIEWPOINTS:
        required_text(viewpoints, viewpoint, f"{name}.viewpoints")
    required_text(item, "reason", name)
    distances = item.get("history_distances", [])
    require_condition(
        isinstance(distances, list)
        and all(type(value) is int and value >= 1 for value in distances),
        f"{name}.history_distancesが1以上の整数の配列ではない",
    )


def validate_facet_weights(item, node, children, name, *, derived):
    """子へ進む階層のweightが、兄弟ノードすべてに三観点の評価と根拠を持つことを検査する。"""
    candidates = required_list(
        item.get("candidates"), f"{name}.candidates", nonempty=True
    )
    keys = []
    for index, candidate in enumerate(candidates):
        cname = f"{name}.candidates[{index}]"
        validate_weight_record(candidate, cname, positive=False)
        keys.append(required_text(candidate, "key", cname))
        required_text(candidate, "label", cname)
        require_condition(
            not (derived and candidate.get("history_distances")),
            f"{cname}.history_distancesが細分した区分にある",
        )
    require_condition(
        keys == children,
        f"{name}.candidatesが{node}の直接の子と一致しない",
    )
    require_condition(
        any(candidate["weight"] > 0 for candidate in candidates),
        f"{name}に正のweightがない",
    )
    return {candidate["key"]: candidate["weight"] for candidate in candidates}


def validate_facet_subdivisions(state):
    """カタログの最下層より下の細分が、subjectの最下層または細分した区分を親とし、根拠と範囲を持つことを検査し、親ごとの細分を返す。"""
    records = required_list(state.get("facet_subdivisions", []), "facet_subdivisions")
    subdivisions = {}
    for index, item in enumerate(records):
        name = f"facet_subdivisions[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        parent = required_text(item, "parent", name)
        require_condition(parent not in subdivisions, f"{name}.parentが重複している")
        derived = {
            child["key"]
            for record in subdivisions.values()
            for child in record["children"]
        }
        require_condition(
            parent.startswith("subject::")
            and (parent in derived or facet_node.child_keys(parent) == []),
            f"{name}.parentがsubjectの最下層でも細分した区分でもない",
        )
        required_text(item, "characteristic", name)
        required_text(item, "basis", name)
        urls = required_id_list(
            item.get("source_urls"), f"{name}.source_urls", nonempty=True
        )
        require_condition(
            all(is_url(url) for url in urls), f"{name}.source_urlsにURLでない値がある"
        )
        children = required_list(item.get("children"), f"{name}.children")
        require_condition(
            len(children) >= MIN_SUBDIVISION_CHILDREN,
            f"{name}.childrenが二つに満たない",
        )
        for position, child in enumerate(children, 1):
            cname = f"{name}.children[{position - 1}]"
            require_condition(
                isinstance(child, dict), f"{cname}はオブジェクトでなければならない"
            )
            key = f"{parent}{'.' if '*' in parent else '*'}{position}"
            require_condition(child.get("key") == key, f"{cname}.keyが{key}ではない")
            require_condition(
                facet_node.find_block(key)[1] is None,
                f"{cname}.keyがカタログのノードと重なっている",
            )
            required_text(child, "label", cname)
            required_text(child, "scope", cname)
        subdivisions[parent] = item
    return subdivisions


def facet_node_exists(key, subdivisions):
    return facet_node.find_block(key)[1] is not None or any(
        child["key"] == key
        for record in subdivisions.values()
        for child in record["children"]
    )


def through_single_children(key):
    """子が一つだけのカタログのノードをたどり、判断の対象になるノードと、たどったノードを返す。"""
    passed = []
    while len(children := facet_node.child_keys(key) or []) == 1:
        passed.append(key)
        key = children[0]
    return key, passed


def validate_facet_selection(state):
    """4軸の各階層の粒度判断、weight、抽選結果が一続きになっていることを検査する。"""
    levels, _ = records_with_ids(
        state.get("facet_levels"), "facet_levels", nonempty=True
    )
    weights = required_list(state.get("facet_weights"), "facet_weights")
    picks = required_list(state.get("facet_picks"), "facet_picks")
    weights_by_level = {}
    for index, item in enumerate(weights):
        name = f"facet_weights[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        level_id = required_text(item, "level_id", name)
        require_condition(
            level_id not in weights_by_level, f"{name}.level_idが重複している"
        )
        weights_by_level[level_id] = item
    picks_by_level = {}
    for index, item in enumerate(picks):
        name = f"facet_picks[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        level_id = required_text(item, "level_id", name)
        require_condition(
            level_id not in picks_by_level, f"{name}.level_idが重複している"
        )
        picks_by_level[level_id] = required_text(item, "key", name)
    nodes = state.get("facet_nodes")
    require_condition(isinstance(nodes, dict), "facet_nodesがない")
    subdivisions = validate_facet_subdivisions(state)
    subdivided = {}
    axes = iter(FACET_AXES)
    axis = next(axes)
    expected, passed = through_single_children(f"{axis}::ROOT")
    descended = set()
    for level in levels:
        name = f"facet_levels.{level['id']}"
        require_condition(
            level.get("node") not in passed,
            f"{name}で子が一つだけのノードを判断している",
        )
        require_condition(
            level.get("axis") == axis and level.get("node") == expected,
            f"{name}が前の階層の抽選結果から続いていない",
        )
        require_condition(
            facet_node_exists(expected, subdivisions),
            f"{name}.nodeがカタログにも細分にも存在しない",
        )
        required_text(level, "reason", name)
        decision = level.get("decision")
        require_condition(
            decision in {"descend", "stop"}, f"{name}.decisionが不正である"
        )
        if decision == "stop":
            require_condition(
                nodes.get(axis) == expected,
                f"facet_nodes.{axis}が停止した階層のノードと一致しない",
            )
            axis = next(axes, None)
            expected, passed = through_single_children(f"{axis}::ROOT")
            continue
        children = facet_node.child_keys(expected)
        if not children:
            require_condition(
                expected in subdivisions, f"{name}で細分せずに最下層から子へ進んでいる"
            )
            subdivided[expected] = level["id"]
            children = [child["key"] for child in subdivisions[expected]["children"]]
        require_condition(
            level["id"] in weights_by_level, f"{name}の兄弟ノードのweightがない"
        )
        candidate_weights = validate_facet_weights(
            weights_by_level[level["id"]],
            expected,
            children,
            f"facet_weights.{level['id']}",
            derived=expected in subdivided,
        )
        chosen = picks_by_level.get(level["id"])
        require_condition(
            candidate_weights.get(chosen, 0) > 0,
            f"{name}の抽選結果が正のweightを持つ候補ではない",
        )
        descended.add(level["id"])
        expected, passed = through_single_children(chosen)
    require_condition(axis is None, "4軸すべての粒度判断が停止まで記録されていない")
    require_condition(
        set(weights_by_level) <= descended and set(picks_by_level) <= descended,
        "子へ進まない階層にweightまたは抽選結果がある",
    )
    require_condition(set(nodes) == set(FACET_AXES), "facet_nodesに4軸がない")
    require_condition(
        set(subdivisions) == set(subdivided), "子へ進んでいないノードの細分がある"
    )
    if subdivided or state.get("facet_subdivision_reviews"):
        validate_reviews(
            state, "facet_subdivision_reviews", sorted(subdivided.values()), "level_id"
        )
    validate_reviews(
        state, "facet_level_reviews", [level["id"] for level in levels], "level_id"
    )
    validate_reviews(state, "facet_weight_reviews", sorted(descended), "level_id")
    validate_reviews(state, "facet_distribution_reviews", sorted(descended), "level_id")


def validate_intersection_state(state):
    """4軸の選択と交差領域の確認記録を検査する。"""
    nodes = state.get("facet_nodes")
    require_condition(
        isinstance(nodes, dict) and set(nodes) == {"subject", "place", "time", "type"},
        "facet_nodesに4軸の正規ノードキーがない",
    )
    subdivisions = validate_facet_subdivisions(state)
    for axis, key in nodes.items():
        require_condition(
            isinstance(key, str) and key.startswith(f"{axis}::"),
            f"facet_nodes.{axis}が不正である",
        )
        require_condition(
            facet_node_exists(key, subdivisions),
            f"facet_nodes.{axis}がカタログにも細分にも存在しない",
        )
    review = state.get("intersection_review")
    require_condition(isinstance(review, dict), "intersection_reviewがない")
    areas, _ = records_with_ids(
        state.get("coverage_areas"), "coverage_areas", nonempty=True
    )
    for item in areas:
        for key in ("label", "basis", "target_kinds"):
            required_text(item, key, f"coverage_areas.{item['id']}")
    sources = required_id_list(
        review.get("source_refs"), "intersection_review.source_refs", nonempty=True
    )
    require_condition(
        len(sources) == len(set(sources)),
        "intersection_review.source_refsに同じ資料が重複している",
    )
    for source in sources:
        require_condition(
            is_url(source), "intersection_review.source_refsにURLでない値がある"
        )
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
    for index, example in enumerate(examples):
        name = f"intersection_review.candidate_examples[{index}]"
        require_condition(isinstance(example, dict), f"{name}がオブジェクトではない")
        required_text(example, "name", name)
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
        beginner_count >= 1,
        "intersection_reviewに初級学習資料で確認した候補例がない",
    )
    required_text(review, "scope_reason", "intersection_review")
    require_condition(
        review.get("result") == "viable", "4軸の交差領域の独立確認が合格していない"
    )


def validate_selection_entries_areas(state, *, complete=True):
    entries, entry_ids = records_with_ids(
        state.get("entry_points"), "entry_points", nonempty=True
    )
    for item in entries:
        name = f"entry_points.{item['id']}"
        required_text(item, "label", name)
        required_text(item, "kind", name)
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
            len(entries) >= MIN_ENTRY_POINTS,
            "入口を二つ以上使っていない",
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
        elif (
            item.get("explored") is not True
            and not item.get("entry_point_ids")
            and not item.get("source_searches")
        ):
            continue
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
        for index, search in enumerate(area.get("source_searches", [])):
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


def validate_selection_candidates(state, entry_ids, areas, area_ids):
    candidates, candidate_ids = records_with_ids(
        state.get("candidates"), "candidates", nonempty=True
    )
    discovered = candidate_discovery_index(areas, candidate_ids)
    for item in candidates:
        name = f"candidates.{item['id']}"
        required_text(item, "label", name)
        require_candidate_discovery_links(item, area_ids, entry_ids, discovered)
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
            evidence = item.get("introductory_evidence")
            require_condition(
                isinstance(evidence, dict), f"{name}.introductory_evidenceがない"
            )
            require_condition(
                evidence.get("entry_point_id") in entry_ids,
                f"{name}.introductory_evidence.entry_point_idが入口にない",
            )
            required_text(evidence, "passage", f"{name}.introductory_evidence")
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
                    "descriptive_name",
                    "no_introductory_source",
                },
                f"{name}.exclusion_codeが不正である",
            )
            required_text(item, "exclusion_reason", name)
            if code == "duplicate":
                merged_into = required_text(item, "merged_into", name)
                require_condition(
                    merged_into in candidate_ids, f"{name}.merged_intoが存在しない"
                )
    return candidates, candidate_ids


def validate_exposure_prechecks(state, members, known_ids):
    """所属する選択対象ごとに予備検査の結果があることを検査し、残す候補を返す。"""
    records = required_list(
        state.get("exposure_prechecks"), "exposure_prechecks", nonempty=bool(members)
    )
    results = {}
    for index, item in enumerate(records):
        name = f"exposure_prechecks[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        candidate_id = required_text(item, "candidate_id", name)
        require_condition(candidate_id in known_ids, f"{name}.candidate_idが候補にない")
        require_condition(
            candidate_id not in results, f"{name}.candidate_idが重複している"
        )
        require_condition(
            item.get("result") in {"keep", "exclude"}, f"{name}.resultが不正である"
        )
        required_text(item, "reason", name)
        results[candidate_id] = item["result"]
    missing = sorted(set(members) - set(results))
    require_condition(not missing, f"予備検査のない候補がある: {missing}")
    excluded = sorted(
        candidate_id
        for candidate_id, result in results.items()
        if result == "exclude" and candidate_id in members
    )
    if excluded or state.get("exposure_precheck_reviews"):
        validate_reviews(state, "exposure_precheck_reviews", excluded, "candidate_id")
    return {
        candidate_id
        for candidate_id, result in results.items()
        if result == "keep" and candidate_id in members
    }


def validate_topic_weights(state, pickable):
    """まとまりの切り方と、二段階のweightが抽選の対象の候補に対応することを検査する。"""
    groups, group_ids = records_with_ids(
        state.get("topic_groups"), "topic_groups", nonempty=bool(pickable)
    )
    grouped = []
    for group in groups:
        name = f"topic_groups.{group['id']}"
        required_text(group, "label", name)
        required_text(group, "reason", name)
        grouped.extend(referenced_ids(group, "candidate_ids", pickable, name))
    require_condition(
        sorted(grouped) == sorted(pickable),
        "topic_groupsが抽選の対象の候補を一度ずつ含んでいない",
    )
    group_weights = required_list(
        state.get("group_weights", []), "group_weights", nonempty=len(groups) > 1
    )
    weighted_groups = []
    for index, item in enumerate(group_weights):
        name = f"group_weights[{index}]"
        validate_weight_record(item, name, positive=True)
        weighted_groups.append(required_text(item, "group_id", name))
    require_condition(
        (len(groups) == 1 and not weighted_groups)
        or sorted(weighted_groups) == sorted(group_ids),
        "group_weightsがまとまりと一致しない",
    )
    weighted = []
    for index, item in enumerate(
        required_list(state.get("candidate_weights"), "candidate_weights")
    ):
        name = f"candidate_weights[{index}]"
        validate_weight_record(item, name, positive=True)
        weighted.append(required_text(item, "candidate_id", name))
    require_condition(
        sorted(weighted) == sorted(pickable),
        "candidate_weightsが抽選の対象の候補と一致しない",
    )
    validate_reviews(state, "topic_group_reviews", sorted(group_ids), "group_id")
    weight_targets = sorted(group_ids) + (["groups"] if len(groups) > 1 else [])
    validate_reviews(state, "topic_weight_reviews", weight_targets, "target")
    validate_reviews(state, "topic_distribution_reviews", ["all"], "target")
    return sorted(group_ids)


def validate_prejudgments(state, pickable):
    """抽選した候補ごとに四つの予備判定があり、作問へ進む候補が一つであることを検査する。"""
    latest = {}
    for key in PREJUDGMENT_KEYS:
        latest[key] = {}
        for index, item in enumerate(required_list(state.get(key), key, nonempty=True)):
            name = f"{key}[{index}]"
            require_condition(
                isinstance(item, dict), f"{name}はオブジェクトでなければならない"
            )
            candidate_id = required_text(item, "candidate_id", name)
            require_condition(
                candidate_id in pickable, f"{name}.candidate_idが抽選の対象にない"
            )
            require_condition(
                item.get("result") in {"pass", "exclude"}, f"{name}.resultが不正である"
            )
            required_text(item, "reason", name)
            latest[key][candidate_id] = item["result"]
    candidates = {item["id"]: item for item in state["candidates"]}
    accepted = []
    for candidate_id in sorted(set().union(*latest.values())):
        missing = [key for key in PREJUDGMENT_KEYS if candidate_id not in latest[key]]
        require_condition(not missing, f"{candidate_id}の予備判定がない: {missing}")
        rejected = "quality_rejection_reason" in candidates[candidate_id]
        if any(latest[key][candidate_id] == "exclude" for key in PREJUDGMENT_KEYS):
            require_condition(
                rejected, f"candidates.{candidate_id}に予備判定の除外を記録していない"
            )
        elif not rejected:
            accepted.append(candidate_id)
    require_condition(
        len(accepted) == 1,
        f"予備判定に合格して作問へ進む候補が一つではない: {accepted}",
    )


def validate_memberships(state, candidate_ids, known_ids):
    """所属判定が選択対象ごとに4軸の判断を持つことを検査し、所属する候補を返す。"""
    memberships = required_list(
        state.get("memberships"), "memberships", nonempty=bool(candidate_ids)
    )
    belongs = {}
    for index, item in enumerate(memberships):
        name = f"memberships[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        candidate_id = required_text(item, "candidate_id", name)
        require_condition(candidate_id in known_ids, f"{name}.candidate_idが候補にない")
        require_condition(
            candidate_id not in belongs, f"{name}.candidate_idが重複している"
        )
        axes = item.get("axes")
        require_condition(isinstance(axes, dict), f"{name}.axesがない")
        results = []
        for axis in FACET_AXES:
            judgment = axes.get(axis)
            aname = f"{name}.axes.{axis}"
            require_condition(isinstance(judgment, dict), f"{aname}がない")
            require_condition(
                isinstance(judgment.get("belongs"), bool), f"{aname}.belongsがない"
            )
            required_text(judgment, "reason", aname)
            results.append(judgment["belongs"])
        belongs[candidate_id] = all(results)
    missing = sorted(set(candidate_ids) - set(belongs))
    require_condition(not missing, f"所属判定のない候補がある: {missing}")
    validate_reviews(state, "membership_reviews", sorted(belongs), "candidate_id")
    return {
        candidate_id
        for candidate_id, value in belongs.items()
        if value and candidate_id in candidate_ids
    }


def eligible_candidate_ids(state):
    return {
        item["id"] for item in state["candidates"] if item["disposition"] == "eligible"
    }


def descriptive_name_ids(state):
    """名称が対象の説明そのものであることを理由に除外した候補のIDを返す。"""
    return sorted(
        item["id"]
        for item in state["candidates"]
        if item["disposition"] == "excluded"
        and item["exclusion_code"] == "descriptive_name"
    )


def member_candidate_ids(state):
    """探索段階の選択対象のうち、4軸すべてに所属する候補のIDを返す。"""
    eligible = eligible_candidate_ids(state)
    return {
        item["candidate_id"]
        for item in state["memberships"]
        if item["candidate_id"] in eligible
        and all(item["axes"][axis]["belongs"] for axis in FACET_AXES)
    }


def pickable_candidate_ids(state):
    """所属する候補のうち、露出の予備検査で残した候補のIDを返す。"""
    members = member_candidate_ids(state)
    return {
        item["candidate_id"]
        for item in state["exposure_prechecks"]
        if item["candidate_id"] in members and item["result"] == "keep"
    }


def validate_selection_review(state, areas, candidates, entry_ids):
    area_ids = {item["id"] for item in areas}
    candidate_ids = {item["id"] for item in candidates}
    reviews, review_ids = records_with_ids(
        state.get("independent_review"), "independent_review", nonempty=True
    )
    require_condition(
        review_ids == area_ids, "別経路の探索が全下位領域に対応していない"
    )
    for review in reviews:
        name = f"independent_review.{review['id']}"
        required_text(review, "difference_from_exploration", name)
        required_text(review, "source_discovery_query", name)
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
    required_text(challenge, "query", "saturation_challenge")
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
    core = challenge.get("core_check")
    require_condition(isinstance(core, dict), "saturation_challenge.core_checkがない")
    name = "saturation_challenge.core_check"
    referenced_ids(core, "source_entry_point_ids", entry_ids, name)
    core_ids = referenced_ids(core, "core_candidate_ids", candidate_ids, name)
    require_condition(
        set(core_ids) <= eligible_candidate_ids(state),
        f"{name}.core_candidate_idsに選択対象でない候補がある",
    )
    referenced_ids(core, "added_candidate_ids", candidate_ids, name, nonempty=False)
    required_text(core, "reason", name)
    descriptive = descriptive_name_ids(state)
    if descriptive or state.get("descriptive_name_reviews"):
        validate_reviews(state, "descriptive_name_reviews", descriptive, "candidate_id")


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


def validate_selection_state(state, stage):
    validate_intersection_state(state)
    _, entry_ids, areas, area_ids = validate_selection_entries_areas(state)
    candidates, candidate_ids = validate_selection_candidates(
        state, entry_ids, areas, area_ids
    )
    validate_selection_review(state, areas, candidates, entry_ids)
    frontier = required_id_list(state.get("frontier_ids"), "frontier_ids")
    require_condition(
        not (set(frontier) - candidate_ids), "frontier_idsに存在しない候補がある"
    )
    require_condition(not frontier, "未展開の有力候補が残っている")
    require_condition(state.get("saturated") is True, "探索が飽和していない")
    if stage == "discovery":
        return
    members = validate_memberships(state, eligible_candidate_ids(state), candidate_ids)
    if stage == "membership":
        return
    pickable = validate_exposure_prechecks(state, members, candidate_ids)
    validate_topic_weights(state, pickable)
    if stage == "prejudgment":
        validate_prejudgments(state, pickable)


def validate_selection_mode(state):
    mode = state.get("selection_mode")
    require_condition(mode in {"random", "specified"}, "selection_modeが不正である")
    if mode == "specified":
        required_text(state, "user_specified_target", "state")
    return mode


def validate_execution_assignments(state, stage):
    data = state.get("execution")
    require_condition(isinstance(data, dict), "executionがない")
    available = data.get("delegation_available")
    require_condition(
        isinstance(available, bool), "execution.delegation_availableがない"
    )
    if not available:
        required_text(data, "unavailable_reason", "execution")
        return
    known = {
        role["id"]: role
        for _, role in assignment_plan.ordered_roles(assignment_plan.load_table())
    }
    records = required_list(
        data.get("assignments"), "execution.assignments", nonempty=True
    )
    roles_by_agent = {}
    exposure_versions = {}
    reviewed_outputs = {}
    for index, record in enumerate(records):
        name = f"execution.assignments[{index}]"
        require_condition(
            isinstance(record, dict), f"{name}はオブジェクトでなければならない"
        )
        role = record.get("role")
        require_condition(role in known, f"{name}.roleが担当表にない")
        agent_id = required_text(record, "agent_id", name)
        required_id_list(
            record.get("artifact_refs"), f"{name}.artifact_refs", nonempty=True
        )
        require_condition(
            roles_by_agent.setdefault(agent_id, role) == role,
            f"{name}.agent_idを別の役割にも割り当てている",
        )
        size = known[role].get("split_size")
        if size is None:
            require_condition(
                "items" not in record, f"{name}は項目で分割しない担当である"
            )
        else:
            items = required_id_list(
                record.get("items"), f"{name}.items", nonempty=True
            )
            require_condition(
                len(items) <= size, f"{name}.itemsが担当表の件数を超えている"
            )
        if role in FINAL_REVIEW_ROLES:
            digest = required_text(record, "output_sha256", name)
            require_condition(
                re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
                f"{name}.output_sha256が不正である",
            )
            require_condition(
                reviewed_outputs.setdefault(agent_id, digest) == digest,
                f"{name}.agent_idを別の完成稿の照合に再利用している",
            )
        if role == "exposure":
            version = record.get("draft_version")
            require_condition(
                type(version) is int and version >= 1,
                f"{name}.draft_versionが不正である",
            )
            require_condition(
                exposure_versions.setdefault(agent_id, version) == version,
                f"{name}.agent_idを別の版の露出検査に再利用している",
            )
    roles = STAGE_ROLES[stage]
    assigned = set(roles_by_agent.values())
    missing = [role for role in roles if role not in assigned]
    require_condition(
        not missing, f"execution.assignmentsに担当の記録がない: {missing}"
    )
    if stage in REVIEWED_STAGES:
        draft = state.get("draft")
        version = draft.get("version") if isinstance(draft, dict) else None
        require_condition(
            version in exposure_versions.values(),
            "現行版の解答を伏せた名称候補の担当の記録がない",
        )


def require_role_assigned(state, role):
    """条件によって置く担当の起動の記録があることを確認する。"""
    if not state["execution"]["delegation_available"]:
        return
    require_condition(
        any(record["role"] == role for record in state["execution"]["assignments"]),
        f"execution.assignmentsに担当の記録がない: {[role]}",
    )


def require_items_assigned(state, role, ids):
    """分割する担当の起動の記録が、対象の項目をすべて受け持っていることを確認する。"""
    if not state["execution"]["delegation_available"]:
        return
    assigned = {
        item
        for record in state["execution"]["assignments"]
        if record["role"] == role
        for item in record["items"]
    }
    missing = sorted(set(ids) - assigned)
    require_condition(
        not missing, f"{role}の担当に割り当てていない項目がある: {missing}"
    )


def validate_facet_execution(state):
    """ファセット選択の起動の記録と、細分した場合の細分の検査担当の記録を検査する。"""
    validate_execution_assignments(state, "facet-selection")
    if state.get("facet_subdivisions"):
        require_role_assigned(state, "facet_subdivision_review")


def validate_selection_execution(state, stage):
    """題材探索状態の起動の記録と、分割した担当の受け持ちを検査する。"""
    validate_execution_assignments(state, stage)
    require_items_assigned(
        state, "exploration", [area["id"] for area in state["coverage_areas"]]
    )
    eligible = sorted(eligible_candidate_ids(state))
    require_items_assigned(state, "nearby_exploration", eligible)
    if descriptive_name_ids(state):
        require_role_assigned(state, "descriptive_name_review")
    if stage != "discovery":
        require_items_assigned(state, "membership", eligible)
        require_items_assigned(state, "membership_review", eligible)
    if stage in {"selection", "prejudgment"}:
        groups = [group["id"] for group in state["topic_groups"]]
        require_items_assigned(state, "topic_weighting", groups)
        if len(groups) > 1:
            require_role_assigned(state, "group_weighting")
        members = member_candidate_ids(state)
        require_items_assigned(state, "exposure_precheck", sorted(members))
        excluded = members - pickable_candidate_ids(state)
        if excluded:
            require_role_assigned(state, "exposure_precheck_review")


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


def validate_condition_list(conditions, clue_text, evidence, name):
    """条件ごとの照合を検査し、相違する条件の箇所を返す。"""
    differences = set()
    for position, condition in enumerate(conditions):
        condition_name = f"{name}.conditions[{position}]"
        require_condition(
            isinstance(condition, dict),
            f"{condition_name}はオブジェクトでなければならない",
        )
        passage = required_text(condition, "passage", condition_name)
        require_condition(
            passage in clue_text, f"{condition_name}.passageが手掛かり本文にない"
        )
        require_condition(
            isinstance(condition.get("matches"), bool),
            f"{condition_name}.matchesが真偽値ではない",
        )
        if not condition["matches"]:
            differences.add(passage)
        required_text(condition, "reason", condition_name)
        condition_evidence = required_id_list(
            condition.get("evidence_ids"),
            f"{condition_name}.evidence_ids",
            nonempty=True,
        )
        require_condition(
            set(condition_evidence) <= set(evidence),
            f"{condition_name}.evidence_idsが候補の引用に含まれていない",
        )
    return differences


def validate_competitors(state, active_clues, quote_ids, stage):
    """対抗候補と条件の照合が採用中の手掛かりに対応し、検査で合格していることを検査する。"""
    clue_text = {clue["id"]: clue["text"] for clue in active_clues}
    clue_fact = {clue["id"]: clue["fact"] for clue in state["clues"]}
    all_clue_ids = set(clue_fact)
    competitors, competitor_ids = records_with_ids(
        state.get("competitors"), "competitors", nonempty=True
    )
    pairs = set()
    evidence_of = {}
    for item in competitors:
        name = f"competitors.{item['id']}"
        required_text(item, "name", name)
        clue_ids = referenced_ids(item, "clue_ids", all_clue_ids, name)
        evidence_of[item["id"]] = referenced_ids(item, "evidence_ids", quote_ids, name)
        pairs.update(
            (clue_id, item["id"]) for clue_id in clue_ids if clue_id in clue_text
        )
    lacking = sorted(set(clue_text) - {clue_id for clue_id, _ in pairs})
    require_condition(not lacking, f"対抗候補を探していない手掛かりがある: {lacking}")
    compared = {}
    for index, item in enumerate(
        required_list(state.get("competitor_comparisons"), "competitor_comparisons")
    ):
        name = f"competitor_comparisons[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        pair = (item.get("clue_id"), item.get("competitor_id"))
        if pair not in pairs:
            require_condition(
                pair[1] in competitor_ids and pair[0] in all_clue_ids,
                f"{name}が対抗候補と手掛かりの組を参照していない",
            )
            continue
        conditions = required_list(
            item.get("conditions"), f"{name}.conditions", nonempty=True
        )
        differences = validate_condition_list(
            conditions, clue_fact[pair[0]], evidence_of[pair[1]], name
        )
        disposition = item.get("disposition")
        require_condition(
            disposition in {"excluded", "same_target"},
            f"{name}.dispositionが不正である",
        )
        if disposition == "excluded":
            exclusion = required_text(item, "exclusion_passage", name)
            require_condition(
                exclusion in differences,
                f"{name}.exclusion_passageが相違する条件ではない",
            )
        else:
            require_condition(
                not differences and "exclusion_passage" not in item,
                f"{name}は同一対象の別名として扱う条件と矛盾している",
            )
        required_text(item, "reason", name)
        compared[pair] = disposition
    missing = sorted(pairs - set(compared))
    require_condition(not missing, f"条件を照合していない対抗候補がある: {missing}")
    if stage in REVIEWED_STAGES:
        validate_competitor_reviews(state, clue_text, compared, quote_ids)


def validate_competitor_reviews(state, clue_text, compared, quote_ids):
    """逆引きの探索と条件の照合の検査が、作る側の照合と食い違わないことを検査する。"""
    validate_reviews(state, "competitor_search_reviews", sorted(clue_text), "clue_id")
    found = set()
    for item in state["competitor_search_reviews"]:
        for index, competitor in enumerate(
            required_list(
                item.get("found"), f"competitor_search_reviews.{item['clue_id']}.found"
            )
        ):
            name = f"competitor_search_reviews.{item['clue_id']}.found[{index}]"
            require_condition(
                isinstance(competitor, dict), f"{name}はオブジェクトでなければならない"
            )
            found.add((item["clue_id"], required_text(competitor, "id", name)))
            required_text(competitor, "name", name)
            url = required_text(competitor, "source_url", name)
            require_condition(
                re.fullmatch(r"https?://\S+", url) is not None,
                f"{name}.source_urlが資料URLではない",
            )
            referenced_ids(competitor, "evidence_ids", quote_ids, name)
    latest = {}
    for index, item in enumerate(
        required_list(
            state.get("competitor_comparison_reviews"),
            "competitor_comparison_reviews",
            nonempty=True,
        )
    ):
        name = f"competitor_comparison_reviews[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        pair = (item.get("clue_id"), item.get("competitor_id"))
        require_condition(
            pair in compared or pair in found,
            f"{name}が作る側の照合にも逆引きで見つけた候補にもない",
        )
        matches = []
        for position, condition in enumerate(
            required_list(item.get("conditions"), f"{name}.conditions", nonempty=True)
        ):
            condition_name = f"{name}.conditions[{position}]"
            require_condition(isinstance(condition, dict), f"{condition_name}がない")
            passage = required_text(condition, "passage", condition_name)
            require_condition(
                passage in clue_text[pair[0]],
                f"{condition_name}.passageが手掛かりにない",
            )
            require_condition(
                condition.get("match") in {"一致", "近接", "不一致"},
                f"{condition_name}.matchが不正である",
            )
            matches.append(condition["match"])
            required_text(condition, "reason", condition_name)
        disposition = item.get("disposition")
        require_condition(
            disposition in {"excluded", "same_target"},
            f"{name}.dispositionが不正である",
        )
        if pair in compared:
            require_condition(
                disposition == compared[pair],
                f"{name}.dispositionが作る側の判断と一致しない",
            )
        else:
            require_condition(
                disposition == "excluded",
                f"{name}で新たな同一対象の候補が見つかっている",
            )
        if disposition == "excluded":
            require_condition(
                "不一致" in matches, f"{name}は相違する条件なしに候補を除外している"
            )
        else:
            require_condition(
                all(match == "一致" for match in matches),
                f"{name}は未一致の条件がある候補を同一対象としている",
            )
        require_condition(
            item.get("status") in {"passed", "failed"}, f"{name}.statusが不正である"
        )
        required_text(item, "reason", name)
        latest[pair] = item["status"]
    missing = sorted((set(compared) | found) - set(latest))
    require_condition(
        not missing, f"条件の照合を検査していない対抗候補がある: {missing}"
    )
    failed = sorted(pair for pair, status in latest.items() if status != "passed")
    require_condition(
        not failed, f"competitor_comparison_reviewsに不合格の項目がある: {failed}"
    )


def validate_clue_checks(item, name, quote_ids):
    """作文担当が記録する準一意性と知名度の判断を検査する。"""
    for key in ("quasi_uniqueness", "familiarity"):
        check = item.get(key)
        cname = f"{name}.{key}"
        require_condition(isinstance(check, dict), f"{cname}がない")
        required_text(check, "claim", cname)
        required_text(check, "reason", cname)
        referenced_ids(check, "evidence_ids", quote_ids, cname)
        if key == "quasi_uniqueness":
            required_text(check, "comparison_scope", cname)
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


def validate_sources_propositions_and_clues(state, version):
    """調査担当の命題と手掛かり候補、作文担当の実現命題と手掛かりの使い方を合わせて検査する。"""
    quote_ids = validate_source_quotes(state)
    props, prop_ids = records_with_ids(
        state.get("propositions"), "propositions", nonempty=True
    )
    claims = {
        item["id"]: required_text(item, "claim", f"propositions.{item['id']}")
        for item in props
    }
    active_props = []
    for index, item in enumerate(
        required_list(
            state.get("realized_propositions"), "realized_propositions", nonempty=True
        )
    ):
        name = f"realized_propositions[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        prop_id = required_text(item, "proposition_id", name)
        require_condition(prop_id in prop_ids, f"{name}.proposition_idが命題にない")
        require_condition(
            prop_id not in {prop["id"] for prop in active_props},
            f"{name}.proposition_idが重複している",
        )
        passage = required_text(item, "passage", name)
        require_condition(
            item.get("draft_version") == version, f"{name}の問題文の版が一致しない"
        )
        active_props.append(
            {"id": prop_id, "claim": claims[prop_id], "passage": passage}
        )
    clues, clue_ids = records_with_ids(state.get("clues"), "clues", nonempty=True)
    candidates = {}
    for item in clues:
        name = f"clues.{item['id']}"
        required_text(item, "fact", name)
        referenced_ids(item, "proposition_ids", prop_ids, name)
        candidates[item["id"]] = item
    active_clues = []
    used = set()
    for index, item in enumerate(
        required_list(state.get("clue_uses"), "clue_uses", nonempty=True)
    ):
        name = f"clue_uses[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        clue_id = required_text(item, "clue_id", name)
        require_condition(clue_id in clue_ids, f"{name}.clue_idが手掛かり候補にない")
        require_condition(clue_id not in used, f"{name}.clue_idが重複している")
        used.add(clue_id)
        require_condition(
            item.get("status") in {"active", "rejected"}, f"{name}.statusが不正である"
        )
        if item["status"] != "active":
            continue
        required_text(item, "text", f"clue_uses.{clue_id}")
        active_clues.append({**candidates[clue_id], **item, "id": clue_id})
    require_condition(active_clues, "activeな手掛かりがない")
    checks = {}
    for index, item in enumerate(
        required_list(state.get("clue_checks"), "clue_checks", nonempty=True)
    ):
        name = f"clue_checks[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        clue_id = required_text(item, "clue_id", name)
        require_condition(clue_id not in checks, f"{name}.clue_idが重複している")
        validate_clue_checks(item, f"clue_checks.{clue_id}", quote_ids)
        checks[clue_id] = item
    for clue in active_clues:
        require_condition(
            clue["id"] in checks, f"手掛かり{clue['id']}の準一意性と知名度の判断がない"
        )
        clue["checks"] = checks[clue["id"]]
    return quote_ids, active_props, active_clues


def validate_support_record(item, name, quote_ids):
    """根拠の引用ID、理由、推論の種類を検査する。"""
    required_text(item, "reason", name)
    require_condition(
        item.get("inference_type")
        in {"direct", "deduction", "interpretation", "synthesis"},
        f"{name}.inference_typeが不正である",
    )
    referenced_ids(item, "evidence_ids", quote_ids, name)


def validate_proposition_support(state, active_props, quote_ids, stage):
    """採用中の各命題に裏取りと確実性の記録があり、検査で合格していることを検査する。"""
    prop_ids = sorted(item["id"] for item in active_props)
    supports = {}
    for index, item in enumerate(
        required_list(
            state.get("proposition_support"), "proposition_support", nonempty=True
        )
    ):
        name = f"proposition_support[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        prop_id = required_text(item, "proposition_id", name)
        validate_support_record(item, name, quote_ids)
        elements = required_list(
            item.get("verification_elements", []), f"{name}.verification_elements"
        )
        for position, element in enumerate(elements):
            element_name = f"{name}.verification_elements[{position}]"
            require_condition(
                isinstance(element, dict),
                f"{element_name}はオブジェクトでなければならない",
            )
            required_text(element, "text", element_name)
            validate_support_record(element, element_name, quote_ids)
        supports[prop_id] = item
    missing = [prop_id for prop_id in prop_ids if prop_id not in supports]
    require_condition(not missing, f"裏取りの記録のない命題がある: {missing}")
    certain = set()
    for index, item in enumerate(
        required_list(
            state.get("proposition_certainty"), "proposition_certainty", nonempty=True
        )
    ):
        name = f"proposition_certainty[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        certain.add(required_text(item, "proposition_id", name))
        required_text(item, "level", name)
        required_text(item, "reason", name)
    missing = [prop_id for prop_id in prop_ids if prop_id not in certain]
    require_condition(not missing, f"確実性の判定のない命題がある: {missing}")
    if stage in REVIEWED_STAGES:
        validate_reviews(state, "corroboration_reviews", prop_ids, "proposition_id")
        validate_reviews(state, "certainty_reviews", prop_ids, "proposition_id")
        validate_proposition_matching(state, prop_ids)
    return [supports[prop_id] for prop_id in prop_ids]


def validate_proposition_matching(state, prop_ids):
    """問題文から独立に取り出した命題が、裏取り済みの命題と過不足なく対応することを検査する。"""
    draft = state["draft"]
    extracted, extracted_ids = records_with_ids(
        state.get("extracted_propositions"), "extracted_propositions", nonempty=True
    )
    for item in extracted:
        name = f"extracted_propositions.{item['id']}"
        require_condition(
            item.get("draft_version") == draft["version"],
            f"{name}の問題文の版が一致しない",
        )
        required_text(item, "claim", name)
        passage = required_text(item, "passage", name)
        require_condition(passage in draft["text"], f"{name}.passageが問題文にない")
    validate_reviews(
        state, "proposition_matching_reviews", sorted(extracted_ids), "extracted_id"
    )
    matched = set()
    latest = {}
    for item in state["proposition_matching_reviews"]:
        latest[item["extracted_id"]] = item
    for extracted_id, item in latest.items():
        name = f"proposition_matching_reviews.{extracted_id}"
        require_condition(
            item.get("proposition_id") in prop_ids,
            f"{name}.proposition_idが採用中の命題を参照していない",
        )
        require_condition(
            item.get("strength_matches") is True,
            f"{name}の断定の強さが確実性と一致していない",
        )
        matched.add(item["proposition_id"])
    missing = sorted(set(prop_ids) - matched)
    require_condition(
        not missing, f"問題文から取り出した命題に対応しない命題がある: {missing}"
    )


def validate_source_assessments(state, supports, stage):
    """資料ごとの信頼性の評価と、事実の根拠に使える資料だけを命題の根拠にしたことを検査する。"""
    source_ids = [source["id"] for source in state["sources"]]
    assessments = {}
    for index, item in enumerate(
        required_list(
            state.get("source_assessments"), "source_assessments", nonempty=True
        )
    ):
        name = f"source_assessments[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        source_id = required_text(item, "source_id", name)
        require_condition(source_id in source_ids, f"{name}.source_idが資料にない")
        required_text(item, "level", name)
        errors = required_list(item.get("clear_errors"), f"{name}.clear_errors")
        require_condition(
            all(isinstance(error, str) and error.strip() for error in errors),
            f"{name}.clear_errorsは誤りの説明の配列でなければならない",
        )
        uses = required_list(item.get("uses"), f"{name}.uses", nonempty=True)
        require_condition(
            set(uses) <= {"fact", "usage_example"} and len(uses) == len(set(uses)),
            f"{name}.usesが不正である",
        )
        required_text(item, "reason", name)
        assessments[source_id] = set(uses)
    missing = sorted(set(source_ids) - set(assessments))
    require_condition(not missing, f"信頼性の評価のない資料がある: {missing}")
    source_of_quote = {
        quote["id"]: source["id"]
        for source in state["sources"]
        for quote in source["quotes"]
    }
    for item in supports:
        cited = set(item["evidence_ids"])
        for element in item.get("verification_elements", []):
            cited.update(element["evidence_ids"])
        usage_only = sorted(
            quote_id
            for quote_id in cited
            if "fact" not in assessments[source_of_quote[quote_id]]
        )
        require_condition(
            not usage_only,
            f"命題{item['proposition_id']}が事実の根拠に使えない資料の引用を根拠にしている: {usage_only}",
        )
    require_items_assigned(state, "source_reliability", source_ids)
    if stage in REVIEWED_STAGES:
        validate_reviews(state, "source_reliability_reviews", source_ids, "source_id")
        require_items_assigned(state, "source_reliability_review", source_ids)


def validate_clue_centrality(state, active_clues, quote_ids, stage):
    """採用中の各手掛かりに中核性の評価があり、検査で合格していることを検査する。"""
    clue_ids = {clue["id"] for clue in active_clues}
    evaluated = set()
    for index, item in enumerate(
        required_list(state.get("clue_centrality"), "clue_centrality", nonempty=True)
    ):
        name = f"clue_centrality[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        clue_id = required_text(item, "clue_id", name)
        require_condition(
            clue_id in {clue["id"] for clue in state["clues"]},
            f"{name}.clue_idが手掛かりにない",
        )
        required_text(item, "claim", name)
        required_text(item, "reason", name)
        referenced_ids(item, "evidence_ids", quote_ids, name)
        evaluated.add(clue_id)
    missing = sorted(clue_ids - evaluated)
    require_condition(not missing, f"中核性の評価のない手掛かりがある: {missing}")
    if stage in REVIEWED_STAGES:
        validate_reviews(
            state,
            "centrality_reviews",
            sorted(clue_ids),
            "clue_id",
        )


def validate_difficulty_assessment(state, quote_ids):
    review = state.get("difficulty_assessment")
    require_condition(isinstance(review, dict), "difficulty_assessmentがない")
    knowledge = required_text(state, "asked_knowledge", "state")
    required_text(state, "answer_granularity", "state")
    require_condition(
        review.get("asked_knowledge") == knowledge,
        "difficulty_assessment.asked_knowledgeが問う知識と一致しない",
    )
    for group in ("beginner", "general"):
        item = review.get(group)
        name = f"difficulty_assessment.{group}"
        require_condition(isinstance(item, dict), f"{name}がない")
        require_condition(
            item.get("status") == "passed",
            f"{name}が難易度の帯に入ると判断されていない",
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


def validate_difficulty_reviews(state, quote_ids, version):
    """初学者側と一般層側の難易度を、それぞれの検査担当が現行版について検査したことを確認する。"""
    for group in ("beginner", "general"):
        key = f"{group}_difficulty_review"
        review = state.get(key)
        require_condition(isinstance(review, dict), f"{key}がない")
        require_condition(
            review.get("draft_version") == version,
            f"{key}.draft_versionが問題文と一致しない",
        )
        require_condition(
            review.get("asked_knowledge") == state["asked_knowledge"],
            f"{key}.asked_knowledgeが問う知識と一致しない",
        )
        validate_challenge_item(review, key, quote_ids)


def validate_expression_reviews(state, checks, active_clues, version):
    """構造、手掛かりの順序、自然さ、前から読んだときの理解しやすさの検査を確認する。"""
    for key in (
        "structure_review",
        "clue_order_review",
        "naturalness_review",
        "incremental_comprehension_review",
    ):
        review = state.get(key)
        require_condition(isinstance(review, dict), f"{key}がない")
        require_condition(
            review.get("draft_version") == version,
            f"{key}.draft_versionが問題文と一致しない",
        )
        required_text(review, "reason", key)
        require_condition(review.get("status") == "passed", f"{key}が合格していない")
    structure = next(item for item in checks if item["id"] == "structure")
    review = state["structure_review"]
    require_condition(
        review.get("question_form") == structure["question_form"],
        "structure_review.question_formが作る側の区分と一致しない",
    )
    otoshi = referenced_ids(
        review,
        "otoshi_clue_ids",
        {clue["id"] for clue in active_clues},
        "structure_review",
    )
    require_condition(
        set(otoshi) == set(structure["otoshi_clue_ids"]),
        "structure_review.otoshi_clue_idsが作る側の区分と一致しない",
    )


def validate_structure_check(item, name, draft_text, active_clues):
    form = required_text(item, "question_form", name)
    require_condition(form in {"SC", "OV"}, f"{name}.question_formが不正である")
    phrase = required_text(item, "question_phrase", name)
    require_condition(phrase in draft_text, f"{name}.question_phraseが問題文にない")
    nucleus = required_text(item, "nucleus", name)
    otoshi = required_text(item, "otoshi", name)
    required_text(item, "otoshi_direct_description", name)
    require_condition(
        otoshi.endswith(nucleus) and otoshi in draft_text,
        f"{name}.otoshiが完成稿の核名詞句で終わらない",
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
            f"clue_uses.{clue['id']}が対象を直接説明する手掛かりとして確認されていない",
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


def clue_quote_ids(state, active_clues):
    """採用中の手掛かりの判断と対抗候補の照合が使う引用IDを集める。"""
    active_ids = {clue["id"] for clue in active_clues}
    cited = set()
    for item in active_clues:
        for key in ("quasi_uniqueness", "familiarity"):
            cited.update(item["checks"][key]["evidence_ids"])
    for item in state["clue_centrality"]:
        if item["clue_id"] in active_ids:
            cited.update(item["evidence_ids"])
    for item in state["competitors"]:
        if set(item["clue_ids"]) & active_ids:
            cited.update(item["evidence_ids"])
    for item in state["competitor_search_reviews"]:
        for competitor in item["found"]:
            cited.update(competitor["evidence_ids"])
    return cited


def adopted_quote_ids(state, active_props, active_clues, difficulty_assessment):
    """採用中の判断が根拠として使う引用IDを集める。"""
    cited = clue_quote_ids(state, active_clues)
    for group in ("beginner", "general"):
        cited.update(difficulty_assessment[group]["evidence_ids"])
    active_ids = {item["id"] for item in active_props}
    for item in state["proposition_support"]:
        if item["proposition_id"] not in active_ids:
            continue
        cited.update(item["evidence_ids"])
        for element in item.get("verification_elements", []):
            cited.update(element["evidence_ids"])
    for key in ("answer_judgments", "checks"):
        for item in state[key]:
            cited.update(item.get("evidence_ids", []))
    for key in ("answers", "candidate_reviews"):
        for item in state["answer_review"][key]:
            cited.update(item["evidence_ids"])
    for item in state["terms"]:
        if item["meaning_needed"]:
            cited.update(item["meaning_evidence_ids"])
            cited.update(item["audience_evidence_ids"])
    for group in ("beginner", "general"):
        cited.update(state[f"{group}_difficulty_review"]["resolution_evidence_ids"])
    return cited


def validate_relative_clauses(state, active_props):
    """作文担当が記録した連体修飾節の内外関係を検査する。"""
    clauses = required_list(state.get("relative_clauses"), "relative_clauses")
    seen_passages = set()
    proposition_ids = {item["id"] for item in active_props}
    for index, clause in enumerate(clauses):
        name = f"relative_clauses[{index}]"
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


def validate_final_input(
    state, version, active_props, active_clues, difficulty_assessment
):
    final = state.get("final_input")
    require_condition(isinstance(final, dict), "final_inputがない")
    require_condition(
        final.get("draft_version") == version, "final_inputの問題文の版が一致しない"
    )
    proposition_ids = {item["id"] for item in active_props}
    expected = {
        "proposition_ids": proposition_ids,
        "clue_ids": {item["id"] for item in active_clues},
        "term_ids": {item["id"] for item in state["terms"]},
        "answer_ids": {item["id"] for item in state["answers"]},
    }
    for key, ids in expected.items():
        refs = required_id_list(final.get(key), f"final_input.{key}")
        require_condition(
            len(refs) == len(set(refs)) and set(refs) == ids,
            f"final_input.{key}が検査済みの現行項目と一致しない",
        )
    cited = adopted_quote_ids(state, active_props, active_clues, difficulty_assessment)
    quote_refs = required_id_list(final.get("quote_ids"), "final_input.quote_ids")
    require_condition(
        len(quote_refs) == len(set(quote_refs)) and set(quote_refs) == cited,
        "final_input.quote_idsが判断に用いた引用と一致しない",
    )
    validate_final_material(state, final, active_props, cited)
    validate_topic_selection(state, final)


def validate_final_material(state, final, active_props, cited):
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
        not re.search(
            r"\b(?:ACCEPTANCE|DRAW|VERDICT|ACCEPT|REJECT)\b",
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
    for clause in state["relative_clauses"]:
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
            r"(?:subject|place|time|type)::",
            content,
        ),
        "final_input.material.topic_selectionに内部ノードIDがある",
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


def validate_final_reviews(state, output_bytes):
    """現行の完成稿の全体を、反映の照合担当と混入の検査担当が新しく照合したことを検査する。"""
    digest = hashlib.sha256(output_bytes).hexdigest()
    for key in FINAL_REVIEW_ROLES:
        review = state.get(key)
        require_condition(isinstance(review, dict), f"{key}がない")
        require_condition(
            review.get("status") == "passed", f"{key}.statusが合格していない"
        )
        required_text(review, "reason", key)
        require_condition(
            review.get("output_sha256") == digest,
            f"{key}.output_sha256が完成稿と一致しない",
        )
        if state["execution"]["delegation_available"]:
            require_condition(
                any(
                    record["role"] == key and record["output_sha256"] == digest
                    for record in state["execution"]["assignments"]
                ),
                f"{key}の担当が現行の完成稿について起動されていない",
            )
    review = state["final_reflection_review"]
    for key in ("quote_ids", "answer_ids", "clue_ids"):
        refs = required_id_list(review.get(key), f"final_reflection_review.{key}")
        require_condition(
            len(refs) == len(set(refs)) and set(refs) == set(state["final_input"][key]),
            f"final_reflection_review.{key}が最終入力と一致しない",
        )


def validate_terminology(state, quote_ids, version, stage, draft_text):
    terms, term_ids = records_with_ids(state.get("terms"), "terms")
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
    if stage in REVIEWED_STAGES:
        validate_term_reviews(state, terms, term_ids, quote_ids, version)


def validate_term_reviews(state, terms, term_ids, quote_ids, version):
    """独立に列挙した語、意味内容の要否、語義、既習性の検査が作る側の記録と対応することを検査する。"""
    listing = state.get("term_listing")
    require_condition(isinstance(listing, dict), "term_listingがない")
    require_condition(
        listing.get("draft_version") == version,
        "term_listing.draft_versionが問題文と一致しない",
    )
    listed, listed_ids = records_with_ids(listing.get("terms"), "term_listing.terms")
    for item in listed:
        required_text(item, "term", f"term_listing.terms.{item['id']}")
    require_condition(
        listed_ids == term_ids, "term_listing.termsが専門用語の記録と一致しない"
    )
    validate_reviews(state, "term_necessity_reviews", sorted(term_ids), "term_id")
    by_id = {item["id"]: item for item in terms}
    for item in state["term_necessity_reviews"]:
        require_condition(
            item.get("meaning_needed") == by_id[item["term_id"]]["meaning_needed"],
            f"term_necessity_reviews.{item['term_id']}.meaning_neededが作る側の判断と一致しない",
        )
    needed = sorted(item["id"] for item in terms if item["meaning_needed"])
    for kind, key in (
        ("meaning", "term_sense_reviews"),
        ("audience", "term_audience_reviews"),
    ):
        validate_reviews(state, key, needed, "term_id")
        for item in state[key]:
            name = f"{key}.{item['term_id']}"
            evidence = referenced_ids(item, "evidence_ids", quote_ids, name)
            require_condition(
                set(evidence) == set(by_id[item["term_id"]][f"{kind}_evidence_ids"]),
                f"{name}.evidence_idsが採用引用と一致しない",
            )


def validate_exposure_analysis(state, checks, version):
    """解答を伏せて挙げた名称候補と、露出の分析が全候補に対応することを検査する。"""
    blind, blind_ids = records_with_ids(
        state.get("blind_candidates"), "blind_candidates"
    )
    for item in blind:
        name = f"blind_candidates.{item['id']}"
        required_text(item, "name", name)
        require_condition(
            "answer_id" not in item, f"{name}に解答開示前の対応付けがある"
        )
        require_condition(
            item.get("draft_version") == version, f"{name}の問題文の版が一致しない"
        )
    exposure = next(item for item in checks if item["id"] == "answer_exposure")
    semantic_ids = {item["id"] for item in exposure["semantic_candidates"]}
    require_condition(not blind_ids & semantic_ids, "露出候補のidが重複している")
    analyses = required_list(state.get("exposure_analysis"), "exposure_analysis")
    for index, item in enumerate(analyses):
        name = f"exposure_analysis[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        required_text(item, "candidate_id", name)
        validate_name_formation(item, name)
    validate_reviews(
        state, "exposure_analysis", sorted(blind_ids | semantic_ids), "candidate_id"
    )
    return blind_ids, semantic_ids


def validate_answers(state, quote_ids):
    """解答候補と正誤判定の案を検査し、候補ごとに判定の案を合わせて返す。"""
    answers, answer_ids = records_with_ids(
        state.get("answers"), "answers", nonempty=True
    )
    seen = set()
    for item in answers:
        value = required_text(item, "answer", f"answers.{item['id']}")
        require_condition(value not in seen, "同じ解答候補が重複している")
        seen.add(value)
    judgments = {}
    for index, item in enumerate(
        required_list(state.get("answer_judgments"), "answer_judgments", nonempty=True)
    ):
        name = f"answer_judgments[{index}]"
        require_condition(
            isinstance(item, dict), f"{name}はオブジェクトでなければならない"
        )
        answer_id = required_text(item, "answer_id", name)
        require_condition(answer_id in answer_ids, f"{name}.answer_idが解答候補にない")
        require_condition(answer_id not in judgments, f"{name}.answer_idが重複している")
        require_condition(
            item.get("judgment") in {"correct", "prompt", "incorrect"},
            f"{name}.judgmentが不正である",
        )
        required_text(item, "reason", name)
        referenced_ids(item, "evidence_ids", quote_ids, name)
        judgments[answer_id] = item
    missing = sorted(answer_ids - set(judgments))
    require_condition(not missing, f"正誤判定の案のない解答候補がある: {missing}")
    names, _ = records_with_ids(state.get("names"), "names", nonempty=True)
    for item in names:
        name = f"names.{item['id']}"
        required_text(item, "name", name)
        required_text(item, "usage", name)
        referenced_ids(item, "evidence_ids", quote_ids, name)
    return [{**item, "judgment": judgments[item["id"]]["judgment"]} for item in answers]


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
    exposure_candidates = {
        item["id"]: item
        for item in [*state["blind_candidates"], *exposure["semantic_candidates"]]
    }
    semantic_ids = {item["id"] for item in exposure["semantic_candidates"]}
    candidates = required_list(
        review.get("candidate_reviews"), "answer_review.candidate_reviews"
    )
    seen = set()
    for index, candidate in enumerate(candidates):
        name = f"answer_review.candidate_reviews[{index}]"
        require_condition(isinstance(candidate, dict), f"{name}がない")
        candidate_id = required_text(candidate, "candidate_id", name)
        require_condition(
            candidate_id in exposure_candidates,
            f"{name}.candidate_idが露出候補を参照していない",
        )
        require_condition(
            candidate_id not in seen, f"{name}.candidate_idが重複している"
        )
        seen.add(candidate_id)
        if candidate_id in semantic_ids:
            require_condition(
                "answer_id" not in candidate,
                f"{name}に候補を挙げた担当が対応付けた露出候補の対応付けがある",
            )
            answer_id = exposure_candidates[candidate_id]["answer_id"]
        else:
            require_condition("answer_id" in candidate, f"{name}.answer_idがない")
            answer_id = candidate["answer_id"]
        require_condition(
            answer_id is None or answer_id in by_id,
            f"{name}.answer_idが解答候補を参照していない",
        )
        judgment = validate_reviewed_answer(candidate, name, quote_ids)
        if answer_id is None:
            require_condition(
                judgment != "correct", f"{name}の正答が解答範囲に対応付けられていない"
            )
            continue
        require_condition(
            judgment == by_id[answer_id]["judgment"],
            f"{name}.judgmentが採用判定と一致しない",
        )
    require_condition(
        seen == set(exposure_candidates),
        "answer_review.candidate_reviewsが露出候補と一致しない",
    )


def validate_work_state(state, stage):
    require_no_selection_ledger(state)
    validate_selection_mode(state)
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
        state, version
    )
    validate_relative_clauses(state, active_props)
    supports = validate_proposition_support(state, active_props, quote_ids, stage)
    validate_source_assessments(state, supports, stage)
    validate_clue_centrality(state, active_clues, quote_ids, stage)
    validate_competitors(state, active_clues, quote_ids, stage)
    if stage in REVIEWED_STAGES:
        validate_reviews(
            state,
            "familiarity_reviews",
            sorted(clue["id"] for clue in active_clues),
            "clue_id",
        )
    difficulty_assessment = validate_difficulty_assessment(state, quote_ids)
    if stage in REVIEWED_STAGES:
        validate_difficulty_reviews(state, quote_ids, version)
    validate_terminology(state, quote_ids, version, stage, draft["text"])
    answers = validate_answers(state, quote_ids)
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
            semantic = required_list(
                item.get("semantic_candidates"), f"{name}.semantic_candidates"
            )
            required_text(item, "answer_side_knowledge_required", name)
            answer_ids = {answer["id"] for answer in answers}
            candidate_ids = []
            for index, candidate in enumerate(semantic):
                cname = f"{name}.semantic_candidates[{index}]"
                validate_name_formation(candidate, cname)
                candidate_ids.append(required_text(candidate, "id", cname))
                require_condition(
                    "answer_id" in candidate
                    and candidate["answer_id"] in answer_ids | {None},
                    f"{cname}.answer_idが解答候補を参照していない",
                )
            require_condition(
                len(candidate_ids) == len(set(candidate_ids)),
                f"{name}の露出候補のidが重複している",
            )
        if item["id"] != "expression.naturalness":
            referenced_ids(item, "evidence_ids", quote_ids, name)
    if stage in REVIEWED_STAGES:
        validate_expression_reviews(state, checks, active_clues, version)
        validate_exposure_analysis(state, checks, version)
        validate_answer_review(state, answers, checks, quote_ids, version)
    if stage in {"material", "final"}:
        validate_final_input(
            state, version, active_props, active_clues, difficulty_assessment
        )


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


def validate_target_start(state):
    require_no_selection_ledger(state)
    validate_selection_mode(state)
    validate_execution_assignments(state, "target-start")
    required_text(state, "answer_target", "state")


def main():
    parser = argparse.ArgumentParser(description="題材探索と作問状態を検査する")
    parser.add_argument("path", nargs="?")
    parser.add_argument(
        "--stage",
        choices=(
            "facet-selection",
            "intersection-checkpoint",
            "discovery-progress",
            "discovery",
            "membership",
            "selection",
            "prejudgment",
            "target-start",
            "writing",
            "review",
            "material",
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
        if args.stage == "facet-selection":
            validate_facet_selection(state)
            validate_facet_execution(state)
        elif args.stage == "intersection-checkpoint":
            validate_intersection_state(state)
            validate_execution_assignments(state, args.stage)
        elif args.stage == "discovery-progress":
            validate_discovery_progress(state)
            validate_execution_assignments(state, args.stage)
        elif args.stage in {"discovery", "membership", "selection", "prejudgment"}:
            validate_selection_state(state, args.stage)
            validate_selection_execution(state, args.stage)
        elif args.stage == "target-start":
            validate_target_start(state)
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
            validate_final_reviews(state, output_bytes)
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
