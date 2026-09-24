#!/usr/bin/env python3
"""担当表から、ステップの構成と、統括役・担当への依頼文を決める。

担当表は references/roles.json に置く。各担当の入力は段階ごとのデータの一覧で、
表の順で前にある担当の成果物か、親が渡すデータだけを参照できる。

サブコマンド:
    steps              ステップごとの担当と、統括役を置くかを出力する
    coordinate STEP    統括役への依頼文を出力する
    assign ROLE        担当の割り当てと依頼文を出力する

終了コード:
    0  結果を出力した
    2  担当表の不備、存在しない担当など、入力や呼出しの不備

使用例:
    python3 assignment_plan.py steps
    python3 assignment_plan.py coordinate 3
    python3 assignment_plan.py assign exposure
"""

import argparse
import json
import sys
from pathlib import Path

REF_DIR = Path(__file__).resolve().parent.parent / "references"
TABLE_PATH = REF_DIR / "roles.json"
SIDES = {"make", "check"}
EXIT_OK, EXIT_USAGE = 0, 2


class TableError(ValueError):
    pass


def require(ok, msg):
    if not ok:
        raise TableError(msg)


def is_text(value):
    return isinstance(value, str) and bool(value.strip())


def validate_role(role, data, available, seen):
    require(isinstance(role, dict), "担当はオブジェクトでなければならない")
    role_id = role.get("id")
    require(is_text(role_id), "担当のidがない")
    require(role_id not in seen, f"担当{role_id}が重複している")
    for key in ("name", "section"):
        require(is_text(role.get(key)), f"担当{role_id}の{key}がない")
    require(role.get("side") in SIDES, f"担当{role_id}のsideが不正である")
    specs = role.get("specs")
    require(
        isinstance(specs, list) and specs and all(is_text(spec) for spec in specs),
        f"担当{role_id}のspecsがない",
    )
    missing = [spec for spec in specs if not (REF_DIR / spec).is_file()]
    require(not missing, f"担当{role_id}のspecsに存在しない仕様がある: {missing}")
    phases = role.get("inputs")
    require(
        isinstance(phases, list)
        and phases
        and all(isinstance(phase, list) and phase for phase in phases),
        f"担当{role_id}のinputsは空でない段階の配列でなければならない",
    )
    for phase in phases:
        unknown = [item for item in phase if item not in data]
        require(not unknown, f"担当{role_id}の入力に未定義のデータがある: {unknown}")
        unavailable = [item for item in phase if item not in available]
        require(
            not unavailable,
            f"担当{role_id}の入力に、前の担当の成果物でも親が渡すデータでもないものがある: {unavailable}",
        )
    outputs = role.get("outputs")
    require(
        isinstance(outputs, list) and outputs,
        f"担当{role_id}のoutputsがない",
    )
    unknown = [item for item in outputs if item not in data]
    require(not unknown, f"担当{role_id}の成果物に未定義のデータがある: {unknown}")


def validate_table(table):
    """担当表の形と、入力が前の担当の成果物か親が渡すデータであることを検査する。"""
    require(isinstance(table, dict), "担当表はオブジェクトでなければならない")
    data = table.get("data")
    require(
        isinstance(data, dict)
        and data
        and all(is_text(text) for text in data.values()),
        "dataは説明を持つデータの一覧でなければならない",
    )
    parent_data = table.get("parent_data")
    require(
        isinstance(parent_data, list) and set(parent_data) <= set(data),
        "parent_dataは定義済みのデータの一覧でなければならない",
    )
    steps = table.get("steps")
    require(isinstance(steps, list) and steps, "stepsがない")
    available = set(parent_data)
    produced = set()
    seen = set()
    for step in steps:
        require(
            isinstance(step, dict) and is_text(step.get("name")), "ステップの名前がない"
        )
        roles = step.get("roles")
        require(
            isinstance(roles, list) and roles,
            f"ステップ{step['name']}に担当がない",
        )
        for role in roles:
            validate_role(role, data, available, seen)
            seen.add(role["id"])
            produced.update(role["outputs"])
            available.update(role["outputs"])
    require(
        not produced & set(parent_data),
        "親が渡すデータを担当の成果物にしている",
    )
    unused = set(data) - produced - set(parent_data)
    require(not unused, f"どこからも渡されないデータがある: {sorted(unused)}")
    return table


def load_table(path=TABLE_PATH):
    return validate_table(json.loads(Path(path).read_text(encoding="utf-8")))


def ordered_roles(table):
    """担当を表の順に、ステップ番号とともに返す。"""
    return [
        (number, role)
        for number, step in enumerate(table["steps"], 1)
        for role in step["roles"]
    ]


def find_role(table, role_id):
    roles = {role["id"]: role for _, role in ordered_roles(table)}
    require(role_id in roles, f"担当表にない担当である: {role_id}")
    return roles[role_id]


def step_plan(table):
    """ステップごとの担当と、統括役を置くかを返す。"""
    return [
        {
            "step": number,
            "name": step["name"],
            "roles": [role["id"] for role in step["roles"]],
            "coordinator": len(step["roles"]) > 1,
        }
        for number, step in enumerate(table["steps"], 1)
    ]


def coordinator_request(table, number):
    """統括役を置くステップについて、統括役への依頼文を返す。"""
    require(
        type(number) is int and 1 <= number <= len(table["steps"]),
        f"存在しないステップである: {number}",
    )
    step = table["steps"][number - 1]
    require(len(step["roles"]) > 1, f"ステップ{number}には統括役を置かない")
    workflow = REF_DIR / "workflow_spec.md"
    sections = "」節、「".join(dict.fromkeys(role["section"] for role in step["roles"]))
    lines = [
        f"あなたはステップ{number}（{step['name']}）の統括役である。",
        f"`{workflow}`の「担当の構成」節と「{sections}」節を読み、その規定に従って担当を起動し、入力と成果物のファイルを受け渡す。",
        "担当：",
        *(f"- {role['name']}（{role['id']}）" for role in step["roles"]),
    ]
    return {"step": number, "request": "\n".join(lines)}


def request_text(table, role):
    specs = "、".join(f"`{REF_DIR / spec}`" for spec in role["specs"])
    skill = REF_DIR.parent / "SKILL.md"
    workflow = REF_DIR / "workflow_spec.md"
    lines = [
        f"あなたは{role['name']}である。",
        f"`{skill}`の「役割」「必須ツール」「スクリプトの呼出し」節、`{workflow}`の「担当の構成」節と「{role['section']}」節を読み、{specs}を全文読んで、その規定に従って判断する。",
    ]
    phases = role["inputs"]
    if len(phases) > 1:
        lines.append(
            f"入力は{len(phases)}段階で渡す。各段階の成果物を保存してから、次の段階の入力を受け取る。"
        )
    for index, phase in enumerate(phases, 1):
        lines.append(f"入力（第{index}段階）：" if len(phases) > 1 else "入力：")
        lines.extend(f"- {table['data'][item]}" for item in phase)
    lines.append("成果物（指定されたファイルに書く）：")
    lines.extend(f"- {table['data'][item]}" for item in role["outputs"])
    return "\n".join(lines)


def assignments(table, role_id):
    """担当の割り当てと依頼文を返す。"""
    role = find_role(table, role_id)
    return [{"role": role_id, "request": request_text(table, role)}]


def main():
    parser = argparse.ArgumentParser(
        description="担当表からステップの構成と依頼文を決める"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("steps")
    coordinate = commands.add_parser("coordinate")
    coordinate.add_argument("step", type=int)
    assign = commands.add_parser("assign")
    assign.add_argument("role")
    args = parser.parse_args()
    try:
        table = load_table()
        if args.command == "steps":
            result = step_plan(table)
        elif args.command == "coordinate":
            result = coordinator_request(table, args.step)
        else:
            result = assignments(table, args.role)
    except (OSError, json.JSONDecodeError, TableError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
