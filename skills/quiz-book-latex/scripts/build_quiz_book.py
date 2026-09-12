#!/usr/bin/env python3
"""クイズMarkdownを検証し、LaTeXプロジェクトへの変換とPDFのビルドを行う。"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


SECTIONS = ["補足", "別解", "正誤判定基準", "題材選択", "難易度評価", "問題成立性の確認", "裏取り情報"]
HEADING_RE = re.compile(r"^## ([^#].*?)\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"\A\s*# 第(\d+)問\s*$", re.MULTILINE)
QA_RE = re.compile(r"^(問題|解答)：(.+)$", re.MULTILINE)
PREFIX_RE = re.compile(r"^(\d+)-")
REFERENCE_HEADING_RE = re.compile(r"^### 参考文献\s*$", re.MULTILINE)
URL_RE = re.compile(r"^https?://\S+$")


class InputError(Exception):
    pass


@dataclass
class Quiz:
    number: int
    source: Path
    question_md: str
    answer_md: str
    sections: list[tuple[str, str]]


@dataclass
class BibEntry:
    key: str
    note_latex: str
    url: str


def command_path(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise InputError(f"必要なコマンドが見つかりません: {name}")
    return path


def quiz_files(input_dir: Path) -> list[Path]:
    found = []
    for path in input_dir.glob("*.md"):
        match = PREFIX_RE.match(path.name)
        if match:
            found.append((int(match.group(1)), path))
    found.sort(key=lambda item: (item[0], item[1].name))
    if not found:
        raise InputError(f"番号で始まるMarkdownファイルが見つかりません: {input_dir}")
    for previous, current in zip(found, found[1:]):
        if previous[0] == current[0]:
            raise InputError(f"ファイル名の問題番号が重複しています: {current[0]}")
    return [path for _, path in found]


def parse_quiz(path: Path, expected_number: int) -> Quiz:
    text = path.read_text(encoding="utf-8")
    title_matches = list(TITLE_RE.finditer(text))
    if len(title_matches) != 1:
        raise InputError(f"{path.name}: '# 第N問' 見出しは1つだけ必要です")
    number = int(title_matches[0].group(1))
    prefix_match = PREFIX_RE.match(path.name)
    assert prefix_match is not None
    prefix = int(prefix_match.group(1))
    if number != prefix or number != expected_number:
        raise InputError(
            f"{path.name}: 見出し={number}, ファイル名の番号={prefix}, 想定する連番={expected_number}"
        )

    first_section = HEADING_RE.search(text)
    if not first_section:
        raise InputError(f"{path.name}: レベル2見出しが見つかりません")
    lead = text[title_matches[0].end() : first_section.start()]
    qa = list(QA_RE.finditer(lead))
    if [match.group(1) for match in qa] != ["問題", "解答"]:
        raise InputError(f"{path.name}: 問題行と解答行をこの順に1つずつ置いてください")

    headings = list(HEADING_RE.finditer(text))
    names = [match.group(1) for match in headings]
    if names != SECTIONS:
        raise InputError(
            f"{path.name}: レベル2見出しが規定と異なります\n"
            f"  規定: {' / '.join(SECTIONS)}\n"
            f"  入力: {' / '.join(names)}"
        )
    sections = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[heading.end() : end].strip()
        if not body:
            raise InputError(f"{path.name}: section '{names[index]}' is empty")
        sections.append((names[index], body))
    return Quiz(number, path, qa[0].group(2).strip(), qa[1].group(2).strip(), sections)


@lru_cache(maxsize=None)
def pandoc_latex(markdown: str, *, inline: bool = False) -> str:
    heading_filter = Path(__file__).with_name("remove_heading_identifiers.lua")
    command = [
        command_path("pandoc"),
        "--from=gfm",
        "--to=latex",
        "--wrap=preserve",
        f"--lua-filter={heading_filter}",
    ]
    result = subprocess.run(command, input=markdown, text=True, capture_output=True)
    if result.returncode:
        raise InputError(f"Pandocの変換に失敗しました:\n{result.stderr.strip()}")
    latex = result.stdout.strip()
    # 一般的なTeX Live環境の日本語斜体フォールバックにはU+2070がないため置換する。
    latex = latex.replace("⁰", r"\textsuperscript{0}")
    if inline and "\n\n" in latex:
        raise InputError("問題または解答が複数段落へ変換されました")
    return latex


def parse_references(quiz: Quiz, body: str) -> tuple[str, list[BibEntry]]:
    match = REFERENCE_HEADING_RE.search(body)
    if not match:
        raise InputError(f"{quiz.source.name}: 裏取り情報に '### 参考文献' がありません")
    before = body[: match.start()].rstrip()
    reference_text = body[match.end() :].strip()
    blocks = re.split(r"\n\s*\n", reference_text)
    entries = []
    for index, block in enumerate(blocks, 1):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 2 or not URL_RE.fullmatch(lines[-1]):
            raise InputError(
                f"{quiz.source.name}: 参考文献{index}は、文献記述の直後にURLを置いてください"
            )
        description = "\n".join(lines[:-1])
        entries.append(
            BibEntry(
                key=f"quiz-{quiz.number:03d}-ref-{index:02d}",
                note_latex=pandoc_latex(description, inline=True),
                url=lines[-1],
            )
        )
    return before, entries


def render_body(quiz: Quiz) -> tuple[str, list[BibEntry]]:
    markdown_sections = []
    bibliography = []
    for name, body in quiz.sections:
        if name == "裏取り情報":
            body, bibliography = parse_references(quiz, body)
        markdown_sections.append(f"## {name}\n\n{body}")
    keys = ",".join(entry.key for entry in bibliography)
    rendered = pandoc_latex("\n\n".join(markdown_sections))
    rendered += f"\n\n\\subsubsection{{参考文献}}\n\\QuizReferences{{{keys}}}"
    return rendered, bibliography


def write_generated(output_dir: Path, quizzes: list[Quiz]) -> None:
    contents = output_dir / "contents"
    explanations_dir = contents / "explanations"
    explanations_dir.mkdir(parents=True, exist_ok=True)
    for old in explanations_dir.glob("*.tex"):
        old.unlink()

    rows = [
        "\\small",
        "\\setlength{\\tabcolsep}{1.2mm}",
        "\\begin{longtable}{@{}>{\\centering\\arraybackslash}p{9truemm}QAP@{}}",
        "\\toprule",
        "\\textbf{No.} & \\textbf{問題} & \\textbf{解答} & \\textbf{解説ページ} \\\\",
        "\\midrule",
        "\\endfirsthead",
        "\\toprule",
        "\\textbf{No.} & \\textbf{問題} & \\textbf{解答} & \\textbf{解説ページ} \\\\",
        "\\midrule",
        "\\endhead",
        "\\endfoot",
        "\\bottomrule",
        "\\endlastfoot",
    ]
    includes = []
    bibliography = []
    for quiz in quizzes:
        question = pandoc_latex(quiz.question_md, inline=True)
        answer = pandoc_latex(quiz.answer_md, inline=True)
        rows.extend([
            f"\\phantomsection\\label{{question:{quiz.number}}}{quiz.number}",
            f"& {question}",
            f"& {answer}",
            f"& \\hyperref[explanation:{quiz.number}]{{p.~\\pageref*{{explanation:{quiz.number}}}}} \\\\",
            "\\addlinespace[0.6em]",
        ])
        filename = f"{quiz.number:02d}.tex"
        body, quiz_bibliography = render_body(quiz)
        bibliography.extend(quiz_bibliography)
        explanation = (
            f"% {quiz.source.name} から自動生成。直接編集しないこと。\n"
            f"\\QuizQuestion{{{quiz.number}}}{{{question}}}{{{answer}}}{{%\n"
            f"{body}\n"
            "}\n"
        )
        (explanations_dir / filename).write_text(explanation, encoding="utf-8")
        includes.append(f"\\input{{contents/explanations/{quiz.number:02d}}}")
    rows.append("\\end{longtable}")
    (contents / "question-list.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (contents / "explanations.tex").write_text("\n".join(includes) + "\n", encoding="utf-8")
    bib_lines = ["% クイズMarkdownから自動生成。直接編集しないこと。", ""]
    for entry in bibliography:
        bib_lines.extend([
            f"@misc{{{entry.key},",
            f"  note = {{{{{entry.note_latex}}}}},",
            f"  url = {{{entry.url}}},",
            "}",
            "",
        ])
    (output_dir / "resources" / "references.bib").write_text("\n".join(bib_lines), encoding="utf-8")


def prepare_output(template: Path, output: Path, update: bool) -> None:
    if output.exists() and any(output.iterdir()) and not update:
        raise InputError(
            f"出力ディレクトリが空ではありません: {output} "
            "（更新が許可されている場合だけ --update を指定してください）"
        )
    output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, output, dirs_exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--no-compile", action="store_true")
    args = parser.parse_args()
    try:
        input_dir = args.input.resolve()
        output_dir = args.output.resolve()
        if not input_dir.is_dir():
            raise InputError(f"入力ディレクトリが見つかりません: {input_dir}")
        command_path("pandoc")
        if not args.no_compile:
            command_path("latexmk")
            command_path("lualatex")
            command_path("biber")
        quizzes = [parse_quiz(path, index) for index, path in enumerate(quiz_files(input_dir), 1)]
        template = Path(__file__).resolve().parents[1] / "assets" / "template"
        prepare_output(template, output_dir, args.update)
        write_generated(output_dir, quizzes)
        if not args.no_compile:
            for suffix in ["aux", "fdb_latexmk", "fls", "log", "out", "toc"]:
                stale = output_dir / f"main.{suffix}"
                if stale.exists():
                    stale.unlink()
            tex_cache = output_dir / ".texlive-cache"
            tex_cache.mkdir(exist_ok=True)
            build_env = os.environ.copy()
            build_env["TEXMFVAR"] = str(tex_cache)
            build_env["TEXMFCACHE"] = str(tex_cache)
            result = subprocess.run(
                [command_path("latexmk"), "-g", "-interaction=nonstopmode", "main.tex"],
                cwd=output_dir,
                env=build_env,
                text=True,
                capture_output=True,
            )
            if result.returncode:
                diagnostic = "\n".join((result.stdout + result.stderr).splitlines()[-80:])
                raise InputError(
                    f"LaTeXのビルドに失敗しました（終了コード: {result.returncode}）:\n{diagnostic}"
                )
        print(f"{len(quizzes)}問の問題集を生成しました: {output_dir}")
        return 0
    except InputError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
