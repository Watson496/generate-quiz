#!/usr/bin/env python3
"""探索状態の二段階のweightから候補ごとの基礎weightを求め、重み付き抽選する。

入力:
    題材候補の探索状態のJSONファイルを受け取る。まとまりのweightと、まとまりの中の
    候補のweightの積を、各候補の基礎weightとする。まとまりが一つだけなら、まとまりの
    weightを1とする。
    --excludeには、品質棄却理由を記録した全候補のIDを指定する。

終了コード:
    0  1件を抽選した
    1  探索状態が不合格、または抽選可能な候補が残っていない
    2  JSONを読めない、または--excludeが品質棄却記録と一致しない

使用例:
    python3 topic_pick.py selection.json
    python3 topic_pick.py selection.json --exclude K1
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import work_state_check

EXIT_SELECTION_BLOCKED, EXIT_USAGE = 1, 2


def pick_payload(state):
    """候補ごとに、まとまりのweightとまとまりの中のweightの積を基礎weightとする。"""
    group_weights = {
        item["group_id"]: item["weight"] for item in state.get("group_weights", [])
    }
    group_of = {
        candidate_id: group["id"]
        for group in state["topic_groups"]
        for candidate_id in group["candidate_ids"]
    }
    labels = {item["id"]: item["label"] for item in state["candidates"]}
    candidates = []
    for item in state["candidate_weights"]:
        candidate_id = item["candidate_id"]
        candidate = {
            "key": candidate_id,
            "label": labels[candidate_id],
            "base_weight": group_weights.get(group_of[candidate_id], 1)
            * item["weight"],
        }
        if item.get("history_distances"):
            candidate["history_distances"] = item["history_distances"]
        candidates.append(candidate)
    return {"candidates": candidates}


def validate_exclusions(state, exclusions):
    """除外する候補IDが台帳の品質棄却記録と一致するかを検査する。"""
    excluded = set(exclusions)
    rejected = {
        item["id"] for item in state["candidates"] if "quality_rejection_reason" in item
    }
    if len(excluded) != len(exclusions) or excluded != rejected:
        return "--excludeの候補IDが台帳の品質棄却記録と一致しない"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", help="題材候補の探索状態JSON")
    parser.add_argument(
        "--exclude", action="append", default=[], help="棄却した候補ID。複数指定可"
    )
    args = parser.parse_args()

    try:
        state = json.loads(Path(args.state).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE

    try:
        work_state_check.require_condition(
            isinstance(state, dict), "最上位はオブジェクトでなければならない"
        )
        work_state_check.validate_selection_state(state, "selection")
        work_state_check.validate_selection_execution(state, "selection")
    except work_state_check.StateError as error:
        print(f"不合格: {error}", file=sys.stderr)
        return EXIT_SELECTION_BLOCKED

    error = validate_exclusions(state, args.exclude)
    if error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    if len(args.exclude) == len(work_state_check.pickable_candidate_ids(state)):
        print("候補なし: 抽選可能な候補が残っていない", file=sys.stderr)
        return EXIT_SELECTION_BLOCKED

    picker = Path(__file__).with_name("weighted_pick.py")
    command = [sys.executable, str(picker)]
    for key in args.exclude:
        command.extend(("--exclude", key))
    result = subprocess.run(
        command,
        input=json.dumps(pick_payload(state), ensure_ascii=False),
        capture_output=True,
        text=True,
        check=False,
    )
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
