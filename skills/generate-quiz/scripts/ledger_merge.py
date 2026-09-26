#!/usr/bin/env python3
"""同時に動いた担当がそれぞれ書いた台帳の断片を、一つの探索状態へまとめる。

入力:
    まとめる前の探索状態のJSONファイルと、担当ごとの断片のJSONファイルを受け取る。
    断片には、担当の受け持ちを表す接頭辞を`prefix`として置き、そのほかは探索状態と
    同じキーで、書き加える内容だけを置く。
    `id`を持つ記録の配列では、断片の記録のうち、まだない`id`の記録を新しい記録として
    加える。新しい記録の`id`は、断片の接頭辞に`-`を付けた文字列で始める。すでにある
    `id`の記録には、断片に置いた項目を書き加える。配列の項目は後ろへ加え、そのほかの
    項目は、まだない場合だけ置く。すでにある値と異なる値は書き加えない。
    `id`を持つ記録の配列以外のキーも、まだない場合だけ置く。

終了コード:
    0  まとめた探索状態を出力した
    2  JSONを読めない、または断片がまとめられない内容を含む

使用例:
    python3 ledger_merge.py state.json fragment_D1.json fragment_D2.json -o state.json
"""

import argparse
import json
import sys
from pathlib import Path

EXIT_USAGE = 2


class MergeError(Exception):
    """断片をまとめられない。"""


def is_record_list(value):
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, dict) and "id" in item for item in value)
    )


def merge_value(target, key, value, name):
    """一つの項目を書き加える。配列は後ろへ加え、そのほかはまだない場合だけ置く。"""
    if key not in target:
        target[key] = value
    elif isinstance(target[key], list) and isinstance(value, list):
        target[key] = target[key] + [item for item in value if item not in target[key]]
    elif target[key] != value:
        message = f"{name}.{key}の値がすでにある値と異なる"
        raise MergeError(message)


def merge_fragments(state, fragments):
    """断片の新しい記録をすべて加えてから、すでにある記録へ項目を書き加える。"""
    merged = json.loads(json.dumps(state))
    prefixes = [fragment.get("prefix") for fragment in fragments]
    if not all(isinstance(prefix, str) and prefix for prefix in prefixes):
        message = "断片にprefixがない"
        raise MergeError(message)
    if len(set(prefixes)) != len(prefixes):
        message = "同じprefixの断片がある"
        raise MergeError(message)
    updates = []
    for prefix, fragment in zip(prefixes, fragments, strict=True):
        for key, value in fragment.items():
            if key == "prefix":
                continue
            if not is_record_list(value):
                updates.append((key, None, value, prefix))
                continue
            records = merged.setdefault(key, [])
            known = {record["id"] for record in records}
            for record in value:
                if record["id"] in known:
                    updates.append((key, record["id"], record, prefix))
                elif str(record["id"]).startswith(f"{prefix}-"):
                    records.append(record)
                    known.add(record["id"])
                else:
                    updates.append((key, record["id"], record, prefix))
    for key, record_id, value, prefix in updates:
        if record_id is None:
            merge_value(merged, key, value, prefix)
            continue
        target = next(
            (record for record in merged[key] if record["id"] == record_id), None
        )
        if target is None:
            message = f"{prefix}の{key}.{record_id}は、接頭辞{prefix}-で始まらない新しいIDである"
            raise MergeError(message)
        for field, field_value in value.items():
            merge_value(target, field, field_value, f"{key}.{record_id}")
    return merged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", help="まとめる前の探索状態JSON")
    parser.add_argument("fragments", nargs="+", help="担当ごとの断片JSON")
    parser.add_argument(
        "-o", "--output", required=True, help="まとめた探索状態の出力先"
    )
    args = parser.parse_args()
    try:
        state = json.loads(Path(args.state).read_text(encoding="utf-8"))
        fragments = [
            json.loads(Path(path).read_text(encoding="utf-8"))
            for path in args.fragments
        ]
        merged = merge_fragments(state, fragments)
        Path(args.output).write_text(
            json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    except (OSError, json.JSONDecodeError, MergeError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    print(f"まとめた探索状態を出力した: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
