#!/usr/bin/env python3
"""担当表から、ステップの構成、担当の割り当てと依頼文、再実行する担当を決める。

担当表は references/roles.json に置く。各担当の入力は段階ごとのデータの一覧で、
表の順で前にある担当や自分の成果物か、親や統括役が渡すデータだけを参照できる。

サブコマンド:
    steps              ステップごとの担当と、統括役を置くかを出力する
    coordinate STEP    統括役のエージェントの名前と依頼文を出力する
    assign ROLE        担当の割り当てと依頼文を出力する。分割する担当には
                       --itemsで項目IDを渡す
    rerun ROLE         ROLEの成果物が変わったときに再実行する担当を、
                       表の順にステップごとに出力する
    fix DATA...        検査が修正を求めたデータを成果物とする担当と、
                       修正の後に再実行する担当を出力する

終了コード:
    0  結果を出力した
    2  担当表の不備、存在しない担当、項目IDの不備など、入力や呼出しの不備

使用例:
    python3 assignment_plan.py steps
    python3 assignment_plan.py coordinate 3
    python3 assignment_plan.py assign exposure
    python3 assignment_plan.py rerun writer
    python3 assignment_plan.py fix propositions proposition_support
"""

import argparse
import json
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"
TABLE_PATH = REF_DIR / "roles.json"
AGENT_PREFIX = "generate-quiz"
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
    rules = role.get("rules")
    require(
        isinstance(rules, list)
        and rules
        and all(
            isinstance(rule, dict)
            and rule.get("spec") in specs
            and is_text(rule.get("heading"))
            and rule.get("subsections", True) in {True, False}
            for rule in rules
        ),
        f"担当{role_id}のrulesは、specsにある仕様の見出しの一覧でなければならない",
    )
    outputs = role.get("outputs")
    require(
        isinstance(outputs, list) and outputs,
        f"担当{role_id}のoutputsがない",
    )
    unknown = [item for item in outputs if item not in data]
    require(not unknown, f"担当{role_id}の成果物に未定義のデータがある: {unknown}")
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
        unavailable = [
            item for item in phase if item not in available and item not in outputs
        ]
        require(
            not unavailable,
            f"担当{role_id}の入力に、前の担当や自分の成果物でも親や統括役が渡すデータでもないものがある: {unavailable}",
        )
    if "split_size" in role:
        size = role["split_size"]
        require(
            type(size) is int and size >= 1,
            f"担当{role_id}のsplit_sizeは1以上の整数でなければならない",
        )


def validate_table(table):
    """担当表の形と、入力が前の担当や自分の成果物か親や統括役が渡すデータであることを検査する。"""
    require(isinstance(table, dict), "担当表はオブジェクトでなければならない")
    data = table.get("data")
    require(
        isinstance(data, dict)
        and data
        and all(is_text(text) for text in data.values()),
        "dataは説明を持つデータの一覧でなければならない",
    )
    given_data = table.get("given_data")
    require(
        isinstance(given_data, list) and set(given_data) <= set(data),
        "given_dataは定義済みのデータの一覧でなければならない",
    )
    steps = table.get("steps")
    require(isinstance(steps, list) and steps, "stepsがない")
    available = set(given_data)
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
        not produced & set(given_data),
        "親や統括役が渡すデータを担当の成果物にしている",
    )
    unused = set(data) - produced - set(given_data)
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


def has_coordinator(step):
    """担当を複数起動し得るステップ（担当が複数あるか、項目で分割する担当がある）なら真を返す。"""
    return len(step["roles"]) > 1 or any("split_size" in role for role in step["roles"])


def step_plan(table):
    """ステップごとの担当と、統括役を置くかを返す。"""
    return [
        {
            "step": number,
            "name": step["name"],
            "roles": [role["id"] for role in step["roles"]],
            "coordinator": has_coordinator(step),
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
    require(has_coordinator(step), f"ステップ{number}には統括役を置かない")
    sections = "」節、「".join(dict.fromkeys(role["section"] for role in step["roles"]))
    lines = [
        f"あなたはステップ{number}（{step['name']}）の統括役である。",
        f"スキルの場所：`{SKILL_DIR}`（以下のファイルはこの場所からの相対パスで示す）",
        f"`references/workflow_spec.md`の「担当の構成」節と「{sections}」節、`references/work_state_spec.md`の「担当の起動の記録」節を読み、その規定に従って担当を起動し、入力と成果物のファイルを受け渡す。",
        "担当：",
        *(f"- {role['name']}（{role['id']}）" for role in step["roles"]),
        "報告は、完了したことと成果物のファイルの場所だけとする。",
    ]
    return {
        "step": number,
        "agent": coordinator_agent_name(number),
        "request": "\n".join(lines),
    }


def agent_name(role):
    """担当を起動するエージェントの名前を返す。"""
    return f"{AGENT_PREFIX}:{role['id']}"


def coordinator_id(number):
    """統括役のエージェントのIDを返す。"""
    return f"step{number:02d}_coordinator"


def coordinator_agent_name(number):
    """統括役を起動するエージェントの名前を返す。"""
    return f"{AGENT_PREFIX}:{coordinator_id(number)}"


def request_text(table, role, items):
    specs = "、".join(f"`references/{spec}`" for spec in role["specs"])
    lines = [
        f"あなたは{role['name']}である。",
        f"スキルの場所：`{SKILL_DIR}`（以下のファイルはこの場所からの相対パスで示す）",
        f"`SKILL.md`の「役割」「必須ツール」「スクリプトの呼出し」節、`references/workflow_spec.md`の「担当の構成」節と「{role['section']}」節を読み、{specs}を全文読んで、その規定に従って判断する。",
    ]
    phases = role["inputs"]
    if len(phases) > 1:
        lines.append(
            f"入力は{len(phases)}段階で渡す。各段階の成果物を保存してから、次の段階の入力を受け取る。"
        )
    for index, phase in enumerate(phases, 1):
        lines.append(f"入力（第{index}段階）：" if len(phases) > 1 else "入力：")
        lines.extend(f"- {table['data'][item]}" for item in phase)
    if items is not None:
        lines.append("担当する項目：" + "、".join(items))
    lines.append("成果物（指定されたファイルに書く）：")
    lines.extend(f"- {table['data'][item]}" for item in role["outputs"])
    lines.append("報告は、完了したことと成果物のファイルの場所だけとする。")
    return "\n".join(lines)


def assignments(table, role_id, items=None):
    """担当の割り当てを返す。分割する担当は項目を件数ごとに分ける。"""
    role = find_role(table, role_id)
    size = role.get("split_size")
    if size is None:
        require(items is None, f"担当{role_id}は項目で分割しない")
        chunks = [None]
    else:
        require(bool(items), f"担当{role_id}には項目IDが必要である")
        require(len(items) == len(set(items)), "項目IDが重複している")
        chunks = [items[start : start + size] for start in range(0, len(items), size)]
    return [
        {
            "role": role_id,
            "agent": agent_name(role),
            "items": chunk,
            "request": request_text(table, role, chunk),
        }
        for chunk in chunks
    ]


def rerun_plan(table, role_id):
    """ROLEの成果物が変わったときに再実行する担当を、表の順にステップごとに返す。"""
    role = find_role(table, role_id)
    changed = set(role["outputs"])
    after = False
    plan = []
    for number, item in ordered_roles(table):
        if not after:
            after = item["id"] == role_id
            continue
        if any(data in changed for phase in item["inputs"] for data in phase):
            changed.update(item["outputs"])
            if not plan or plan[-1]["step"] != number:
                plan.append({"step": number, "roles": []})
            plan[-1]["roles"].append(item["id"])
    return plan


def fix_plan(table, data_ids):
    """検査が修正を求めたデータを成果物とする担当と、その後に再実行する担当を返す。

    修正を求められたデータを成果物とする検査側の担当が、作る側の担当の修正の後で再実行される場合は、
    その検査側の担当には修正させず、再実行だけを行う。
    """
    require(bool(data_ids), "データIDが必要である")
    unknown = sorted(set(data_ids) - set(table["data"]))
    require(not unknown, f"担当表にないデータである: {unknown}")
    producers = [
        role for _, role in ordered_roles(table) if set(role["outputs"]) & set(data_ids)
    ]
    require(bool(producers), f"担当の成果物ではないデータである: {data_ids}")
    reruns = {}
    for producer in producers:
        for entry in rerun_plan(table, producer["id"]):
            reruns.setdefault(entry["step"], set()).update(entry["roles"])
    rerun_ids = set().union(*reruns.values()) if reruns else set()
    fixed = {
        producer["id"]
        for producer in producers
        if producer["side"] == "make" or producer["id"] not in rerun_ids
    }
    plan = []
    for number, role in ordered_roles(table):
        if role["id"] in reruns.get(number, set()) - fixed:
            if not plan or plan[-1]["step"] != number:
                plan.append({"step": number, "roles": []})
            plan[-1]["roles"].append(role["id"])
    return {
        "fix": [
            {"step": number, "role": role["id"]}
            for number, role in ordered_roles(table)
            if role["id"] in fixed
        ],
        "rerun": plan,
    }


def main():
    parser = argparse.ArgumentParser(description="担当表から割り当てと再実行を決める")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("steps")
    coordinate = commands.add_parser("coordinate")
    coordinate.add_argument("step", type=int)
    assign = commands.add_parser("assign")
    assign.add_argument("role")
    assign.add_argument("--items", nargs="+")
    rerun = commands.add_parser("rerun")
    rerun.add_argument("role")
    fix = commands.add_parser("fix")
    fix.add_argument("data", nargs="+")
    args = parser.parse_args()
    try:
        table = load_table()
        if args.command == "steps":
            result = step_plan(table)
        elif args.command == "coordinate":
            result = coordinator_request(table, args.step)
        elif args.command == "assign":
            result = assignments(table, args.role, args.items)
        elif args.command == "rerun":
            result = rerun_plan(table, args.role)
        else:
            result = fix_plan(table, args.data)
    except (OSError, json.JSONDecodeError, TableError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
