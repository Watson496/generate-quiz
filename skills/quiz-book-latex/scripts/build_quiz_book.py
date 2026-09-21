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
from enum import Enum
from functools import cache
from pathlib import Path

SECTIONS = [
    "補足",
    "別解",
    "正誤判定基準",
    "題材選択",
    "難易度評価",
    "問題成立性の確認",
    "裏取り情報",
]
MIN_REFERENCE_LINES = 2
HEADING_RE = re.compile(r"^## ([^#].*?)\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"\A\s*# 第(\d+)問\s*$", re.MULTILINE)
QA_RE = re.compile(r"^(問題|解答)：(.+)$", re.MULTILINE)
PREFIX_RE = re.compile(r"^(\d+)-")
REFERENCE_HEADING_RE = re.compile(r"^### 参考文献\s*$", re.MULTILINE)
URL_RE = re.compile(r"^https?://\S+$")


class ExternalCommand(Enum):
    PANDOC = "pandoc"
    LATEXMK = "latexmk"


class QuizBookError(Exception):
    pass


class QuizFileError(QuizBookError):
    @classmethod
    def invalid_filename_number(cls, filename: str) -> QuizFileError:
        return cls(f"ファイル名の問題番号を解釈できません: {filename}")

    @classmethod
    def numbered_files_missing(cls, directory: Path) -> QuizFileError:
        return cls(f"番号で始まるMarkdownファイルが見つかりません: {directory}")

    @classmethod
    def duplicate_file_number(cls, number: int) -> QuizFileError:
        return cls(f"ファイル名の問題番号が重複しています: {number}")

    @classmethod
    def invalid_encoding(cls, filename: str) -> QuizFileError:
        return cls(f"{filename}: UTF-8として読めません")


class QuizFormatError(QuizBookError):
    @classmethod
    def invalid_title_count(cls, filename: str) -> QuizFormatError:
        return cls(f"{filename}: '# 第N問' 見出しが1つではありません")

    @classmethod
    def invalid_title_number(cls, filename: str) -> QuizFormatError:
        return cls(f"{filename}: 見出しの問題番号を解釈できません")

    @classmethod
    def inconsistent_number(
        cls, filename: str, title: int, prefix: int, expected: int
    ) -> QuizFormatError:
        return cls(
            f"{filename}: 見出し={title}, ファイル名の番号={prefix}, 想定する連番={expected}"
        )

    @classmethod
    def section_heading_missing(cls, filename: str) -> QuizFormatError:
        return cls(f"{filename}: レベル2見出しが見つかりません")

    @classmethod
    def invalid_question_answer_lines(cls, filename: str) -> QuizFormatError:
        return cls(f"{filename}: 問題行・解答行の個数または順序が規定と異なります")

    @classmethod
    def invalid_sections(cls, filename: str, actual: list[str]) -> QuizFormatError:
        return cls(
            f"{filename}: レベル2見出しが規定と異なります\n"
            f"  規定: {' / '.join(SECTIONS)}\n"
            f"  入力: {' / '.join(actual)}"
        )

    @classmethod
    def empty_section(cls, filename: str, section: str) -> QuizFormatError:
        return cls(f"{filename}: section '{section}' is empty")

    @classmethod
    def reference_heading_missing(cls, filename: str) -> QuizFormatError:
        return cls(f"{filename}: 裏取り情報に '### 参考文献' がありません")

    @classmethod
    def invalid_reference(cls, filename: str, index: int) -> QuizFormatError:
        return cls(f"{filename}: 参考文献{index}に文献記述と末尾のURLが揃っていません")


class InlineConversionError(QuizBookError):
    def __init__(self) -> None:
        super().__init__("一行として扱う文章が複数段落へ変換されました")


class PathError(QuizBookError):
    @classmethod
    def output_not_empty(cls, directory: Path) -> PathError:
        return cls(
            f"出力ディレクトリが空ではありません: {directory} "
            "（更新が許可されている場合だけ --update を指定してください）"
        )

    @classmethod
    def path_resolution_failed(cls, error: RuntimeError) -> PathError:
        return cls(f"入出力パスを解決できません: {error}")

    @classmethod
    def input_directory_missing(cls, directory: Path) -> PathError:
        return cls(f"入力ディレクトリが見つかりません: {directory}")


class ExternalToolError(QuizBookError):
    @classmethod
    def command_lookup_failed(cls, name: str, error: OSError) -> ExternalToolError:
        return cls(f"コマンドを確認できません: {name}: {error}")

    @classmethod
    def command_missing(cls, name: str) -> ExternalToolError:
        return cls(f"必要なコマンドが見つかりません: {name}")

    @classmethod
    def execution_unavailable(
        cls, command: ExternalCommand, error: OSError | UnicodeError
    ) -> ExternalToolError:
        return cls(f"{command.value}を実行できません: {error}")

    @classmethod
    def execution_failed(
        cls, command: ExternalCommand, result: subprocess.CompletedProcess[str]
    ) -> ExternalToolError:
        diagnostic = "\n".join((result.stdout + result.stderr).splitlines()[-80:])
        return cls(
            f"{command.value}の実行に失敗しました（終了コード: {result.returncode}）:\n{diagnostic}"
        )


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
    try:
        path = shutil.which(name)
    except OSError as error:
        raise ExternalToolError.command_lookup_failed(name, error) from error
    if not path:
        raise ExternalToolError.command_missing(name)
    return path


def quiz_files(input_dir: Path) -> list[Path]:
    found = []
    for path in input_dir.glob("*.md"):
        match = PREFIX_RE.match(path.name)
        if match:
            try:
                number = int(match.group(1))
            except ValueError as error:
                raise QuizFileError.invalid_filename_number(path.name) from error
            found.append((number, path))
    found.sort(key=lambda item: (item[0], item[1].name))
    if not found:
        raise QuizFileError.numbered_files_missing(input_dir)
    for previous, current in zip(found, found[1:]):
        if previous[0] == current[0]:
            raise QuizFileError.duplicate_file_number(current[0])
    return [path for _, path in found]


def parse_quiz(path: Path, expected_number: int) -> Quiz:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise QuizFileError.invalid_encoding(path.name) from error
    title_matches = list(TITLE_RE.finditer(text))
    if len(title_matches) != 1:
        raise QuizFormatError.invalid_title_count(path.name)
    try:
        number = int(title_matches[0].group(1))
    except ValueError as error:
        raise QuizFormatError.invalid_title_number(path.name) from error
    prefix_match = PREFIX_RE.match(path.name)
    if prefix_match is None:
        raise QuizFileError.invalid_filename_number(path.name)
    prefix = int(prefix_match.group(1))
    if number != prefix or number != expected_number:
        raise QuizFormatError.inconsistent_number(
            path.name, number, prefix, expected_number
        )

    first_section = HEADING_RE.search(text)
    if not first_section:
        raise QuizFormatError.section_heading_missing(path.name)
    lead = text[title_matches[0].end() : first_section.start()]
    qa = list(QA_RE.finditer(lead))
    if [match.group(1) for match in qa] != ["問題", "解答"]:
        raise QuizFormatError.invalid_question_answer_lines(path.name)

    headings = list(HEADING_RE.finditer(text))
    names = [match.group(1) for match in headings]
    if names != SECTIONS:
        raise QuizFormatError.invalid_sections(path.name, names)
    sections = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[heading.end() : end].strip()
        if not body:
            raise QuizFormatError.empty_section(path.name, names[index])
        sections.append((names[index], body))
    return Quiz(number, path, qa[0].group(2).strip(), qa[1].group(2).strip(), sections)


@cache
def pandoc_latex(markdown: str, *, inline: bool = False) -> str:
    heading_filter = Path(__file__).with_name("remove_heading_identifiers.lua")
    command = [
        command_path("pandoc"),
        "--from=gfm",
        "--to=latex",
        "--wrap=preserve",
        f"--lua-filter={heading_filter}",
    ]
    try:
        result = subprocess.run(command, input=markdown, text=True, capture_output=True)
    except (OSError, UnicodeError) as error:
        raise ExternalToolError.execution_unavailable(
            ExternalCommand.PANDOC, error
        ) from error
    if result.returncode:
        raise ExternalToolError.execution_failed(ExternalCommand.PANDOC, result)
    latex = result.stdout.strip()
    # 一般的なTeX Live環境の日本語斜体フォールバックにはU+2070がないため置換する。
    latex = latex.replace("⁰", r"\textsuperscript{0}")
    if inline and "\n\n" in latex:
        raise InlineConversionError
    return latex


def parse_references(quiz: Quiz, body: str) -> tuple[str, list[BibEntry]]:
    match = REFERENCE_HEADING_RE.search(body)
    if not match:
        raise QuizFormatError.reference_heading_missing(quiz.source.name)
    before = body[: match.start()].rstrip()
    reference_text = body[match.end() :].strip()
    blocks = re.split(r"\n\s*\n", reference_text)
    entries = []
    for index, block in enumerate(blocks, 1):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < MIN_REFERENCE_LINES or not URL_RE.fullmatch(lines[-1]):
            raise QuizFormatError.invalid_reference(quiz.source.name, index)
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
    for name, section_body in quiz.sections:
        rendered_body = section_body
        if name == "裏取り情報":
            rendered_body, bibliography = parse_references(quiz, section_body)
        markdown_sections.append(f"## {name}\n\n{rendered_body}")
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
        rows.extend(
            [
                f"\\phantomsection\\label{{question:{quiz.number}}}{quiz.number}",
                f"& {question}",
                f"& {answer}",
                f"& \\hyperref[explanation:{quiz.number}]{{p.~\\pageref*{{explanation:{quiz.number}}}}} \\\\",
                "\\addlinespace[0.6em]",
            ]
        )
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
    (contents / "question-list.tex").write_text(
        "\n".join(rows) + "\n", encoding="utf-8"
    )
    (contents / "explanations.tex").write_text(
        "\n".join(includes) + "\n", encoding="utf-8"
    )
    bib_lines = ["% クイズMarkdownから自動生成。直接編集しないこと。", ""]
    for entry in bibliography:
        bib_lines.extend(
            [
                f"@misc{{{entry.key},",
                f"  note = {{{{{entry.note_latex}}}}},",
                f"  url = {{{entry.url}}},",
                "}",
                "",
            ]
        )
    (output_dir / "resources" / "references.bib").write_text(
        "\n".join(bib_lines), encoding="utf-8"
    )


def prepare_output(template: Path, output: Path, update: bool) -> None:
    if output.exists() and any(output.iterdir()) and not update:
        raise PathError.output_not_empty(output)
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
        try:
            input_dir = args.input.resolve()
            output_dir = args.output.resolve()
        except RuntimeError as error:
            raise PathError.path_resolution_failed(error) from error
        if not input_dir.is_dir():
            raise PathError.input_directory_missing(input_dir)
        command_path("pandoc")
        if not args.no_compile:
            command_path("latexmk")
            command_path("lualatex")
            command_path("biber")
        quizzes = [
            parse_quiz(path, index)
            for index, path in enumerate(quiz_files(input_dir), 1)
        ]
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
            try:
                result = subprocess.run(
                    [
                        command_path("latexmk"),
                        "-g",
                        "-interaction=nonstopmode",
                        "main.tex",
                    ],
                    cwd=output_dir,
                    env=build_env,
                    text=True,
                    capture_output=True,
                )
            except (OSError, UnicodeError) as error:
                raise ExternalToolError.execution_unavailable(
                    ExternalCommand.LATEXMK, error
                ) from error
            if result.returncode:
                raise ExternalToolError.execution_failed(
                    ExternalCommand.LATEXMK, result
                )
        print(f"{len(quizzes)}問の問題集を生成しました: {output_dir}")
        return 0
    except QuizBookError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"error: ファイル操作に失敗しました: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
