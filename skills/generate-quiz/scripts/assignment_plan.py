#!/usr/bin/env python3
"""担当表から、ステップの構成、担当の割り当てと依頼文、再実行する担当を決める。

担当表は references/roles.json に置く。各担当の入力は段階ごとのデータの一覧で、
表の順で前にある担当や自分の成果物か、親や統括役が渡すデータだけを参照できる。

サブコマンド:
    steps              ステップごとの担当と、統括役を置くかを出力する
    coordinate STEP    統括役のエージェントの名前と依頼文を出力する。担当表で前のステップの
                       検査（entry_check）を定めたステップでは、--stateで渡した状態
                       ファイルをその段階で検査し、合格した場合だけ出力する
    assign ROLE        担当の割り当てと依頼文を出力する。分割する担当には
                       --itemsで項目IDを渡す
    rerun ROLE         ROLEの成果物が変わったときに再実行する担当を、
                       表の順にステップごとに出力する
    fix [DATA...]      検査が修正を求めたデータを成果物とする担当と、
                       修正の後に再実行する担当を出力する。--stateで状態ファイルを渡すと、
                       最後の判定が不合格の検査の`fix_data`をすべて集め、修正させる担当ごとに
                       渡す検査の成果物の場所を出力する
    inputs ROLE        --stateで渡した状態ファイルから担当の入力のデータだけを取り出し、
                       --outputのファイルに書く。状態ファイルにない入力を出力する。
                       分割する担当には--itemsで受け持つ項目を渡し、その記録だけを取り出す
    record ROLE        担当の起動の記録を--stateの状態ファイルのexecution.assignmentsに
                       書く。--agent-idだけなら起動の記録を加え、--artifactを付けると
                       成果物の場所を、--failedを付けると失敗をその記録に加える
    merge ROLE         担当の成果物のファイル（--artifact）を、担当表のmerge_rulesに
                       従って--stateの状態ファイルへ入れる。成果物の最上位のキーが担当の
                       成果物のデータIDでなければ、状態ファイルを変えずに終了コード1を返す

終了コード:
    0  結果を出力した
    1  前のステップの検査が不合格、または担当の成果物が状態ファイルへ入れられる形ではない
    2  担当表の不備、存在しない担当、項目IDの不備など、入力や呼出しの不備
    3  前のステップの担当が粒度判断へ戻ると判断している、または抽選できる候補がない

使用例:
    python3 assignment_plan.py steps
    python3 assignment_plan.py coordinate 3 --state selection.json
    python3 assignment_plan.py assign exposure
    python3 assignment_plan.py rerun writer
    python3 assignment_plan.py fix propositions proposition_support
    python3 assignment_plan.py inputs membership --state facet.json selection.json \
        --output 004-step04/membership-input.json
    python3 assignment_plan.py record membership --state selection.json \
        --agent-id /root/q001/membership-1 --items K1 K2
    python3 assignment_plan.py merge membership --state selection.json \
        --artifact 004-step04/membership-K1_K2.json
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REF_DIR = SKILL_DIR / "references"
TABLE_PATH = REF_DIR / "roles.json"
AGENT_PREFIX = "generate-quiz"
SIDES = {"make", "check"}
EXIT_OK, EXIT_BLOCKED, EXIT_USAGE, EXIT_RETURN = 0, 1, 2, 3
COORDINATOR_SECTIONS = ("検査で不合格になったとき", "修正と再実行")
REVIEW_SECTION = "検査の進め方"
READ_REST = "ファイルは一つずつ読み、読んだ出力が途中で切り詰められたら、残りの部分を分けて読む。"


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
    headings = [(rule["spec"], rule["heading"]) for rule in rules]
    require(
        len(headings) == len(set(headings)),
        f"担当{role_id}のrulesに同じ見出しが重複している",
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
        require(
            "entry_check" not in step or is_text(step["entry_check"]),
            f"ステップ{step['name']}のentry_checkが段階の名前ではない",
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
    state_keys = table.get("state_keys", {})
    require(
        isinstance(state_keys, dict)
        and set(state_keys) <= set(data)
        and all(
            isinstance(keys, list) and keys and all(is_text(key) for key in keys)
            for keys in state_keys.values()
        ),
        "state_keysは、定義済みのデータごとの状態ファイルのキーの一覧でなければならない",
    )
    rules = table.get("merge_rules", {})
    union = rules.get("union", {}) if isinstance(rules, dict) else None
    append = rules.get("append", []) if isinstance(rules, dict) else None
    lists = rules.get("lists", []) if isinstance(rules, dict) else None
    require(
        isinstance(union, dict)
        and set(union) <= produced
        and all(
            isinstance(keys, list) and keys and all(is_text(key) for key in keys)
            for keys in union.values()
        )
        and isinstance(append, list)
        and set(append) <= produced
        and isinstance(lists, list)
        and set(lists) <= produced
        and not set(append) & set(union)
        and not set(lists) & (set(union) | set(append)),
        "merge_rulesは、担当の成果物のデータごとの、まとめ方の一覧でなければならない",
    )
    scopes = rules.get("scopes", {})
    require(
        isinstance(scopes, dict)
        and set(scopes) <= set(data)
        and all(
            isinstance(scope, dict)
            and set(scope) <= {"field", "data", "values", "where"}
            and is_text(scope.get("field"))
            and scope.get("data") in set(lists)
            and is_text(scope.get("values"))
            and isinstance(scope.get("where", {}), dict)
            for scope in scopes.values()
        ),
        "merge_rulesのscopesは、データごとの、記録を残す範囲（置き換えるデータの項目）の定めでなければならない",
    )
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


def entry_check(table, number, state_path):
    """ステップの前のステップの検査を状態ファイルに行い、終了コードと出力を返す。"""
    step = table["steps"][number - 1]
    stage = step.get("entry_check")
    if stage is None:
        return 0, ""
    require(
        state_path is not None, f"ステップ{number}には--stateで状態ファイルが必要である"
    )
    result = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).with_name("work_state_check.py")),
            "--stage",
            stage,
            str(state_path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    message = result.stderr.strip() or result.stdout.strip()
    require(
        result.returncode in {EXIT_OK, EXIT_BLOCKED, EXIT_RETURN},
        f"前のステップの検査を実行できない: {message}",
    )
    return result.returncode, message


def coordinator_request(table, number):
    """統括役を置くステップについて、統括役への依頼文を返す。"""
    require(
        type(number) is int and 1 <= number <= len(table["steps"]),
        f"存在しないステップである: {number}",
    )
    step = table["steps"][number - 1]
    require(has_coordinator(step), f"ステップ{number}には統括役を置かない")
    sections = "」節、「".join(
        [
            *dict.fromkeys(role["section"] for role in step["roles"]),
            *COORDINATOR_SECTIONS,
        ]
    )
    lines = [
        f"あなたはステップ{number}（{step['name']}）の統括役である。",
        f"スキルの場所：`{SKILL_DIR}`（以下のファイルはこの場所からの相対パスで示す）",
        f"`SKILL.md`の「必須ツール」「スクリプトの呼出し」節、`references/workflow_spec.md`の「担当の構成」節、「{sections}」節、`references/work_state_spec.md`の「担当の起動の記録」節を読み、その規定に従って担当を起動し、入力と成果物のファイルを受け渡す。",
        READ_REST,
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


def is_reviewer(role):
    """検査結果を記録する担当なら真を返す。"""
    return any(
        rule["spec"] == "work_state_spec.md" and rule["heading"] == "検査結果"
        for rule in role["rules"]
    )


def workflow_sections(role):
    """担当が読む workflow_spec.md の節を返す。検査結果を記録する担当には検査の進め方を加える。"""
    sections = ["担当の構成", role["section"]]
    if is_reviewer(role):
        sections.append(REVIEW_SECTION)
    return sections


def request_text(table, role, items):
    specs = "、".join(f"`references/{spec}`" for spec in role["specs"])
    sections = "」節、「".join(workflow_sections(role))
    lines = [
        f"あなたは{role['name']}である。",
        f"スキルの場所：`{SKILL_DIR}`（以下のファイルはこの場所からの相対パスで示す）",
        f"`SKILL.md`の「役割」「必須ツール」「スクリプトの呼出し」節、`references/workflow_spec.md`の「{sections}」節を読み、{specs}を全文読んで、その規定に従って判断する。",
        READ_REST,
    ]
    phases = role["inputs"]
    if len(phases) > 1:
        lines.append(
            f"入力は{len(phases)}段階で渡す。各段階の成果物を保存してから、次の段階の入力を受け取る。"
        )
    for index, phase in enumerate(phases, 1):
        lines.append(f"入力（第{index}段階）：" if len(phases) > 1 else "入力：")
        lines.extend(f"- {table['data'][item]}（`{item}`）" for item in phase)
    if items is not None:
        lines.append("担当する項目：" + "、".join(items))
    lines.append(
        "入力として渡されたファイル、読むよう指定された仕様、資料の写しの置き場、担当の節が読んでよいと定めたファイルのほかに、作業場所のファイル（状態ファイル、ほかの担当の成果物、前の実行の記録）を探したり読んだりしない。"
    )
    if "ledger" in role["outputs"]:
        names = ["prefix"] + [
            key
            for item in role["outputs"]
            for key in table.get("state_keys", {}).get(item, [item])
        ]
        keys = ", ".join(f'"{name}": …' for name in names)
        lines.append(
            f"成果物（指定された断片のファイルに、担当の接頭辞と探索状態のキーで`{{{keys}}}`の形で書く）："
        )
    else:
        keys = ", ".join(f'"{item}": …' for item in role["outputs"])
        lines.append(
            f"成果物（指定されたファイルに、データIDをキーとするJSONのオブジェクト`{{{keys}}}`として書く）："
        )
    lines.extend(f"- {table['data'][item]}（`{item}`）" for item in role["outputs"])
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


def role_inputs(table, role_id, states, phase=None, items=None):
    """状態ファイルから担当の入力のデータを取り出し、取り出したものと状態ファイルにない入力を返す。

    データは状態ファイルの同じ名前のキーに置く。state_keysで複数のキーを定めたデータは、
    そのキーをすべて取り出す。同じキーが複数の状態ファイルにあれば、後に渡したファイルのものを使う。
    受け持つ項目（items）を渡すと、項目のIDを持つ記録の配列からは、その項目の記録だけを取り出す。
    問題文（draft）は、解答を伏せる担当にも渡るので、版と本文だけを取り出す。
    後ろへ加えていく検査結果は、検査した対象ごとの最後の記録だけを取り出す。
    """
    role = find_role(table, role_id)
    phases = role["inputs"]
    if phase is not None:
        require(
            1 <= phase <= len(phases),
            f"担当{role_id}の入力に第{phase}段階はない",
        )
        phases = [phases[phase - 1]]
    extracted = {}
    missing = []
    append = set(table.get("merge_rules", {}).get("append", []))
    for item in dict.fromkeys(item for names in phases for item in names):
        keys = table.get("state_keys", {}).get(item, [item])
        found = [key for key in keys if any(key in state for state in states)]
        for key in found:
            value = next(state[key] for state in reversed(states) if key in state)
            if key == "draft" and isinstance(value, dict):
                value = {k: value[k] for k in ("version", "text") if k in value}
            if key in append and isinstance(value, list):
                value = latest_reviews(value)
            extracted[key] = only_items(value, items)
        if not found:
            missing.append(item)
    if items:
        matched = {
            record.get("id")
            for value in extracted.values()
            if isinstance(value, list)
            for record in value
            if isinstance(record, dict)
        } & set(items)
        require(matched, f"受け持つ項目{items}が、どの入力の記録のIDでもない")
    return extracted, missing


def latest_reviews(records):
    """後ろへ加えていく検査結果から、検査した対象ごとの最後の記録だけを返す。"""
    latest = {}
    for record in records:
        if isinstance(record, dict):
            latest.pop(review_identity(record), None)
            latest[review_identity(record)] = record
    return list(latest.values())


def only_items(value, items):
    """記録の配列に受け持つ項目のIDの記録があれば、その記録だけを返す。"""
    if not items or not isinstance(value, list):
        return value
    ids = {item.get("id") for item in value if isinstance(item, dict)}
    if not ids & set(items):
        return value
    return [
        item for item in value if isinstance(item, dict) and item.get("id") in items
    ]


class ArtifactError(ValueError):
    """担当の成果物が、状態ファイルへ入れられる形ではない。"""


def merge_record(old, new):
    """複数の担当が書く記録に、新しい記録の項目を書き加える。

    IDを持つ記録の配列の項目はIDごとにまとめ、新しい記録にない項目は前の記録のまま残す。
    """
    merged = dict(old)
    for field, value in new.items():
        current = merged.get(field)
        if (
            isinstance(current, list)
            and isinstance(value, list)
            and all(isinstance(item, dict) and "id" in item for item in current + value)
        ):
            ids = [item["id"] for item in value]
            merged[field] = [item for item in current if item["id"] not in ids] + value
        else:
            merged[field] = value
    return merged


def merges_artifact(role):
    """担当の成果物を、このスクリプトで状態ファイルへ入れるかを返す。

    台帳か最終出力を成果物に持つ担当の成果物は、ほかの方法で入れる。
    """
    return not set(role["outputs"]) & {"ledger", "final_output"}


def merge_artifact(table, role_id, state, artifact):
    """担当の成果物を状態ファイルへ入れた結果を返す。

    担当表のmerge_rulesで、unionのデータは定めたキーが同じ記録を置き換えて残りを加え
    （複数の担当が書くデータでは、同じ記録に項目を書き加え）、
    appendのデータは後ろへ加え、そのほかのデータは置き換える。union・append・listsの
    データは、記録の配列でなければ拒む。scopesのデータは、範囲を定めるデータにない値を
    持つ記録を状態ファイルから除き、成果物にそのような記録があれば拒む。
    """
    role = find_role(table, role_id)
    outputs = role["outputs"]
    require(
        merges_artifact(role),
        f"担当{role_id}の成果物は、状態ファイルへこのスクリプトで入れるものではない",
    )
    if not isinstance(artifact, dict) or not artifact or set(artifact) - set(outputs):
        found = (
            sorted(artifact) if isinstance(artifact, dict) else type(artifact).__name__
        )
        message = f"成果物の最上位のキーは担当の成果物のデータID {outputs} でなければならない: {found}"
        raise ArtifactError(message)
    rules = table.get("merge_rules", {})
    union = rules.get("union", {})
    append = set(rules.get("append", []))
    lists = set(rules.get("lists", []))
    merged = json.loads(json.dumps(state))
    writers = [item for _, item in ordered_roles(table) if merges_artifact(item)]
    shared = {
        key for key in union if sum(key in writer["outputs"] for writer in writers) > 1
    }
    if "sources" in artifact:
        require_one_id_per_url(state.get("sources") or [], artifact["sources"])
    for key, value in artifact.items():
        current = merged.get(key)
        if key in union or key in append or key in lists:
            require_records(value, key)
        if (key in union or key in append) and current is not None:
            require_records(current, f"状態ファイルの{key}")
        if key in union and current is not None:
            fields = union[key]
            records = list(current)
            for record in value:
                identity = tuple(record.get(field) for field in fields)
                index = next(
                    (
                        position
                        for position, item in enumerate(records)
                        if tuple(item.get(field) for field in fields) == identity
                    ),
                    None,
                )
                if index is None:
                    records.append(record)
                elif key in shared:
                    records[index] = merge_record(records[index], record)
                else:
                    records[index] = record
            merged[key] = records
        elif key in append and current is not None:
            merged[key] = current + value
        else:
            merged[key] = value
    for key, scope in rules.get("scopes", {}).items():
        allowed = scope_values(merged, scope)
        if allowed is None or not isinstance(merged.get(key), list):
            continue
        field = scope["field"]
        outside = sorted(
            {
                str(record.get(field))
                for record in artifact.get(key, [])
                if not is_text(record.get(field)) or record[field] not in allowed
            }
        )
        if outside:
            message = (
                f"成果物の{key}の{field}に、{scope['data']}にない値がある: {outside}"
            )
            raise ArtifactError(message)
        merged[key] = [
            record
            for record in merged[key]
            if not isinstance(record, dict)
            or (is_text(record.get(field)) and record[field] in allowed)
        ]
    return merged


def scope_values(state, scope):
    """記録を残す範囲の値を、範囲を定めるデータから集める。そのデータがなければNoneを返す。"""
    records = state.get(scope["data"])
    if not isinstance(records, list):
        return None
    values = set()
    for record in records:
        if not isinstance(record, dict) or any(
            record.get(field) != value
            for field, value in scope.get("where", {}).items()
        ):
            continue
        value = record.get(scope["values"])
        values.update(
            item
            for item in (value if isinstance(value, list) else [value])
            if is_text(item)
        )
    return values


def record_assignment(table, role_id, state, agent_id, **fields):
    """担当の起動の記録を加え、または既存の記録に成果物の場所や失敗を加えた状態を返す。"""
    role = find_role(table, role_id)
    require(is_text(agent_id), "--agent-idが必要である")
    recorded = json.loads(json.dumps(state))
    execution = recorded.setdefault(
        "execution", {"delegation_available": True, "assignments": []}
    )
    require(isinstance(execution, dict), "executionはオブジェクトでなければならない")
    records = execution.setdefault("assignments", [])
    require(isinstance(records, list), "execution.assignmentsは配列でなければならない")
    existing = [
        item
        for item in records
        if item.get("agent_id") == agent_id and item.get("role") == role_id
    ]
    artifact = fields.get("artifact")
    failed = fields.get("failed")
    if artifact is None and failed is None:
        require(not existing, f"{agent_id}の{role_id}の起動の記録はすでにある")
        record = {
            "role": role_id,
            "agent": agent_name(role),
            "agent_id": agent_id,
            "artifact_refs": [],
        }
        if fields.get("items"):
            record["items"] = fields["items"]
        for key in ("draft_version", "output_sha256"):
            if fields.get(key) is not None:
                record[key] = fields[key]
        records.append(record)
        return recorded
    require(existing, f"{agent_id}の{role_id}の起動の記録がない")
    record = existing[-1]
    if artifact is not None and artifact not in record["artifact_refs"]:
        record["artifact_refs"].append(artifact)
    if failed is not None:
        record["status"] = "failed"
        record["failure_reason"] = failed
    for key in ("output_sha256",):
        if fields.get(key) is not None:
            record[key] = fields[key]
    return recorded


def require_one_id_per_url(current, added):
    """記録済みの資料と同じURLの資料に、別の資料IDを付けた成果物を拒む。"""
    require_records(added, "sources")
    ids_by_url = {}
    for record in current:
        if isinstance(record, dict) and record.get("url"):
            ids_by_url.setdefault(record["url"], record.get("id"))
    for record in added:
        url = record.get("url")
        if not url:
            continue
        known = ids_by_url.setdefault(url, record.get("id"))
        if known != record.get("id"):
            message = (
                f"成果物の資料{record.get('id')}は、記録済みの資料{known}と同じURLである。"
                f"資料{known}に新しい引用だけを加える形で書き直す"
            )
            raise ArtifactError(message)


def require_records(value, key):
    if not (isinstance(value, list) and all(isinstance(item, dict) for item in value)):
        message = f"成果物の{key}は記録の配列でなければならない"
        raise ArtifactError(message)


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


def fix_from_state(table, data_ids, state_path):
    """修正の計画を返す。状態ファイルを渡すと、最後の判定が不合格の検査の`fix_data`をすべて集める。"""
    failures = []
    data = list(data_ids)
    if state_path is not None:
        failures = failed_reviews(table, read_state(state_path))
        for failure in failures:
            fix_data = failure["record"].get("fix_data") or []
            data.extend(item for item in fix_data if item not in data)
    require(bool(data), "修正を求められたデータがない")
    plan = fix_plan(table, data)
    if state_path is None:
        return plan
    for entry in plan["fix"]:
        outputs = set(find_role(table, entry["role"])["outputs"])
        reviews = {}
        for failure in failures:
            if outputs & set(failure["record"].get("fix_data") or []):
                reviews[failure["data"]] = failure["artifacts"]
        entry["reviews"] = [
            {"data": key, "artifacts": artifacts} for key, artifacts in reviews.items()
        ]
    plan["failed_reviews"] = failures
    return plan


def review_identity(record):
    """検査結果の記録が何を検査したかを表す組を返す。"""
    return tuple(
        sorted(
            (key, value)
            for key, value in record.items()
            if (key.endswith("_id") or key == "target") and isinstance(value, str | int)
        )
    )


def failed_reviews(table, state):
    """状態ファイルの検査結果のうち、最後の判定が不合格のものを返す。"""
    reviewers = {}
    for _, role in ordered_roles(table):
        if role["side"] == "check":
            for item in role["outputs"]:
                reviewers.setdefault(item, []).append(role["id"])
    records = (state.get("execution") or {}).get("assignments") or []
    failed = []
    for key, roles in reviewers.items():
        value = state.get(key)
        if isinstance(value, dict):
            latest = [value]
        elif isinstance(value, list):
            by_target = {}
            for item in value:
                if isinstance(item, dict):
                    by_target[review_identity(item)] = item
            latest = list(by_target.values())
        else:
            continue
        artifacts = [
            ref
            for record in records
            if record.get("role") in roles and "status" not in record
            for ref in record.get("artifact_refs") or []
        ]
        failed.extend(
            {"data": key, "record": item, "artifacts": artifacts}
            for item in latest
            if item.get("status") == "failed"
        )
    return failed


def build_parser():
    parser = argparse.ArgumentParser(description="担当表から割り当てと再実行を決める")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("steps")
    coordinate = commands.add_parser("coordinate")
    coordinate.add_argument("step", type=int)
    coordinate.add_argument("--state", type=Path)
    assign = commands.add_parser("assign")
    assign.add_argument("role")
    assign.add_argument("--items", nargs="+")
    rerun = commands.add_parser("rerun")
    rerun.add_argument("role")
    fix = commands.add_parser("fix")
    fix.add_argument("data", nargs="*")
    fix.add_argument("--state", type=Path)
    inputs = commands.add_parser("inputs")
    inputs.add_argument("role")
    inputs.add_argument("--state", type=Path, nargs="+", required=True)
    inputs.add_argument("--phase", type=int)
    inputs.add_argument("--items", nargs="+")
    inputs.add_argument("--output", type=Path, required=True)
    record = commands.add_parser("record")
    record.add_argument("role")
    record.add_argument("--state", type=Path, required=True)
    record.add_argument("--agent-id", required=True)
    record.add_argument("--items", nargs="+")
    record.add_argument("--draft-version", type=int)
    record.add_argument("--output-sha256")
    record.add_argument("--artifact")
    record.add_argument("--failed")
    merge = commands.add_parser("merge")
    merge.add_argument("role")
    merge.add_argument("--state", type=Path, required=True)
    merge.add_argument("--artifact", type=Path, required=True)
    return parser


def read_state(path):
    state = json.loads(path.read_text(encoding="utf-8"))
    require(
        isinstance(state, dict), "状態ファイルはJSONのオブジェクトでなければならない"
    )
    return state


def write_state(path, state):
    path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def run_state_command(table, args):
    """状態ファイルを読み書きするサブコマンドを実行し、出力する結果を返す。"""
    if args.command == "inputs":
        states = [read_state(path) for path in args.state]
        extracted, missing = role_inputs(
            table, args.role, states, args.phase, args.items
        )
        args.output.write_text(
            json.dumps(extracted, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return {
            "output": str(args.output),
            "keys": list(extracted),
            "not_in_state": missing,
        }
    state = read_state(args.state)
    if args.command == "record":
        recorded = record_assignment(
            table,
            args.role,
            state,
            args.agent_id,
            items=args.items,
            draft_version=args.draft_version,
            output_sha256=args.output_sha256,
            artifact=args.artifact,
            failed=args.failed,
        )
        write_state(args.state, recorded)
        return next(
            item
            for item in reversed(recorded["execution"]["assignments"])
            if item["agent_id"] == args.agent_id and item["role"] == args.role
        )
    artifact = json.loads(args.artifact.read_text(encoding="utf-8"))
    write_state(args.state, merge_artifact(table, args.role, state, artifact))
    return {"state": str(args.state), "keys": list(artifact)}


def main():
    args = build_parser().parse_args()
    try:
        table = load_table()
        if args.command == "steps":
            result = step_plan(table)
        elif args.command == "coordinate":
            result = coordinator_request(table, args.step)
            code, message = entry_check(table, args.step, args.state)
            if code != EXIT_OK:
                print(message, file=sys.stderr)
                return code
        elif args.command == "assign":
            result = assignments(table, args.role, args.items)
        elif args.command == "rerun":
            result = rerun_plan(table, args.role)
        elif args.command == "fix":
            result = fix_from_state(table, args.data, args.state)
        else:
            result = run_state_command(table, args)
    except ArtifactError as error:
        print(f"不合格: {error}", file=sys.stderr)
        return EXIT_BLOCKED
    except (OSError, json.JSONDecodeError, TableError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
