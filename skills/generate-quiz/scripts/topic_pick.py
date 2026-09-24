#!/usr/bin/env python3
"""探索状態と抽選候補を照合し、選択対象から重み付き抽選する。

入力:
    探索状態のJSONファイルと、--jsonまたは標準入力から抽選用JSONを受け取る。
    --excludeには、品質棄却理由を記録した全候補のIDを指定する。

終了コード:
    0  1件を抽選した
    1  探索状態が不合格、または抽選可能な候補が残っていない
    2  JSONを読めない、または抽選用JSONと探索状態が一致しない

使用例:
    python3 topic_pick.py selection.json --json candidates.json
    python3 topic_pick.py selection.json --json candidates.json --exclude K1
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import work_state_check

EXIT_SELECTION_BLOCKED, EXIT_USAGE = 1, 2


def validate_payload(payload, state, exclusions):
    """探索台帳と抽選候補の対応を検査する。"""
    if not isinstance(payload, dict) or not isinstance(payload.get("candidates"), list):
        return "candidatesは配列でなければならない"
    candidates = payload["candidates"]
    if not all(
        isinstance(item, dict) and isinstance(item.get("key"), str)
        for item in candidates
    ):
        return "各候補に文字列のkeyが必要"
    keys = [item["key"] for item in candidates]
    eligible = work_state_check.pickable_candidate_ids(state)
    if len(keys) != len(set(keys)) or set(keys) != eligible:
        return "抽選用の候補IDが探索状態の選択対象と一致しない"
    names = {item["id"]: item["label"] for item in state["candidates"]}
    if any(item.get("label") != names[item["key"]] for item in candidates):
        return "抽選用の候補名が探索状態と一致しない"
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
    parser.add_argument("--json", help="抽選用JSON。省略時は標準入力")
    parser.add_argument(
        "--exclude", action="append", default=[], help="棄却した候補ID。複数指定可"
    )
    args = parser.parse_args()

    try:
        state = json.loads(Path(args.state).read_text(encoding="utf-8"))
        raw = (
            Path(args.json).read_text(encoding="utf-8")
            if args.json
            else sys.stdin.read()
        )
        payload = json.loads(raw)
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

    error = validate_payload(payload, state, args.exclude)
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
        command, input=raw, capture_output=True, text=True, check=False
    )
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
