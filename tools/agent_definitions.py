#!/usr/bin/env python3
"""担当表から、担当ごとのエージェントの定義を作る。

エージェントの定義には、担当の名前、workflow_spec.md の担当の節、担当表の rules で
指定した仕様の節の本文を置く。依頼文とは別に、担当を起動したときに必ず読み込まれる
指示として判断の規定を渡すためである。

形式:
    codex   Codex CLI のカスタムエージェント（TOML）。名前は generate-quiz:担当ID
    claude  Claude Code のプラグインのエージェント（Markdown）。名前は担当ID で、
            プラグイン名 generate-quiz が名前空間になる

終了コード:
    0  定義を書き出した。--check では、置かれた定義が担当表と仕様に一致した
    1  --check で、置かれた定義が担当表と仕様に一致しない
    2  担当表の不備、見出しが仕様にないなど、入力の不備

使用例:
    python3 tools/agent_definitions.py codex codex/agents
    python3 tools/agent_definitions.py claude claude/agents --check
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent / "skills/generate-quiz/scripts")
)
import assignment_plan

EXIT_OK, EXIT_MISMATCH, EXIT_USAGE = 0, 1, 2
PREFIX = "generate-quiz"
HEADING = re.compile(r"^(#{2,6}) (.+)$", re.MULTILINE)


def section_text(text, heading, *, subsections=True):
    """見出しから、同じか上の階層の見出しの前まで（下位の節を含めない場合は次の見出しの前まで）を返す。"""
    matches = list(HEADING.finditer(text))
    for index, match in enumerate(matches):
        if match.group(2).strip() != heading:
            continue
        level = len(match.group(1))
        end = len(text)
        for later in matches[index + 1 :]:
            if not subsections or len(later.group(1)) <= level:
                end = later.start()
                break
        return text[match.start() : end].strip()
    message = f"見出しが仕様にない: {heading}"
    raise assignment_plan.TableError(message)


def instructions(role):
    """担当の名前、workflow の担当の節、判断の規定を、エージェントへの指示にまとめる。"""
    workflow = (assignment_plan.REF_DIR / "workflow_spec.md").read_text(
        encoding="utf-8"
    )
    parts = [
        f"あなたはgenerate-quizの{role['name']}である。",
        "依頼文が指定するファイルを読んで手順と記録の書式に従い、判断は次の規定に従う。",
        f"以下は`workflow_spec.md`の「{role['section']}」節である。",
        section_text(workflow, role["section"]),
    ]
    texts = {}
    for rule in role["rules"]:
        spec = rule["spec"]
        if spec not in texts:
            texts[spec] = (assignment_plan.REF_DIR / spec).read_text(encoding="utf-8")
        parts.append(f"以下は`{spec}`の「{rule['heading']}」節である。")
        parts.append(
            section_text(
                texts[spec],
                rule["heading"],
                subsections=rule.get("subsections", True),
            )
        )
    return "\n\n".join(parts) + "\n"


def codex_definition(role):
    body = instructions(role)
    if "'''" in body:
        message = f"担当{role['id']}の指示に'''が含まれる"
        raise assignment_plan.TableError(message)
    return (
        f'name = "{PREFIX}:{role["id"]}"\n'
        f'description = "generate-quizの{role["name"]}。"\n'
        f"developer_instructions = '''\n{body}'''\n"
    )


def claude_definition(role):
    return (
        "---\n"
        f"name: {role['id']}\n"
        f"description: generate-quizの{role['name']}。\n"
        "---\n\n"
        f"{instructions(role)}"
    )


FORMATS = {
    "codex": (codex_definition, lambda role: f"{PREFIX}-{role['id']}.toml"),
    "claude": (claude_definition, lambda role: f"{role['id']}.md"),
}


def definitions(table, form):
    """担当ごとに、ファイル名と定義の本文を返す。"""
    build, filename = FORMATS[form]
    return {
        filename(role): build(role) for _, role in assignment_plan.ordered_roles(table)
    }


def mismatches(expected, directory):
    """置かれた定義のうち、生成した定義と一致しないものと、余分なものを返す。"""
    present = {path.name for path in Path(directory).glob("*") if path.is_file()}
    differ = sorted(
        name
        for name, body in expected.items()
        if name not in present
        or (Path(directory) / name).read_text(encoding="utf-8") != body
    )
    return differ, sorted(present - set(expected))


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("form", choices=sorted(FORMATS))
    parser.add_argument("directory", help="定義を置くディレクトリ")
    parser.add_argument(
        "--check", action="store_true", help="置かれた定義が一致するかだけを確かめる"
    )
    args = parser.parse_args()
    try:
        expected = definitions(assignment_plan.load_table(), args.form)
    except (assignment_plan.TableError, OSError) as error:
        print(f"入力エラー: {error}", file=sys.stderr)
        return EXIT_USAGE
    if args.check:
        differ, extra = mismatches(expected, args.directory)
        if differ or extra:
            print(f"一致しない定義: {differ}　余分な定義: {extra}", file=sys.stderr)
            return EXIT_MISMATCH
        print("定義は担当表と仕様に一致する")
        return EXIT_OK
    directory = Path(args.directory)
    directory.mkdir(parents=True, exist_ok=True)
    for name, body in expected.items():
        (directory / name).write_text(body, encoding="utf-8")
    print(f"{len(expected)}件の定義を書き出した: {directory}")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
