"""build_quiz_book.pyの入力解析と出力生成を関数単位で検査する。"""

from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture
def book_module(load_script):
    return load_script("quiz-book-latex", "build_quiz_book.py")


@pytest.fixture
def book_with_pandoc(book_module, monkeypatch):
    def fake_run(command, **kwargs):
        assert command[0] == "pandoc"
        return SimpleNamespace(returncode=0, stdout=kwargs["input"], stderr="")

    monkeypatch.setattr(book_module.shutil, "which", lambda name: name)
    monkeypatch.setattr(book_module.subprocess, "run", fake_run)
    return book_module


def quiz_markdown(book_module, number=1):
    sections = "\n\n".join(f"## {name}\n\n本文" for name in book_module.SECTIONS)
    return f"# 第{number}問\n\n問題：何でしょう？\n解答：答え\n\n{sections}\n"


class TestQuizInput:
    def test_quiz_files_sorts_by_number(self, book_module, tmp_path):
        for name in ("02-b.md", "01-a.md", "memo.md"):
            (tmp_path / name).touch()
        assert [path.name for path in book_module.quiz_files(tmp_path)] == [
            "01-a.md",
            "02-b.md",
        ]

    def test_quiz_files_rejects_duplicate_number(self, book_module, tmp_path):
        (tmp_path / "01-a.md").touch()
        (tmp_path / "01-b.md").touch()
        with pytest.raises(book_module.QuizFileError, match="重複"):
            book_module.quiz_files(tmp_path)

    def test_parse_quiz_extracts_question_answer_and_sections(
        self, book_module, tmp_path
    ):
        source = tmp_path / "01-quiz.md"
        source.write_text(quiz_markdown(book_module), encoding="utf-8")
        quiz = book_module.parse_quiz(source, 1)
        assert quiz.number == 1
        assert quiz.question_md == "何でしょう？"
        assert quiz.answer_md == "答え"
        assert [name for name, _ in quiz.sections] == book_module.SECTIONS

    def test_parse_quiz_rejects_mismatched_number(self, book_module, tmp_path):
        source = tmp_path / "01-quiz.md"
        source.write_text(quiz_markdown(book_module, 2), encoding="utf-8")
        with pytest.raises(book_module.QuizFormatError, match="見出し=2"):
            book_module.parse_quiz(source, 1)

    def test_parse_quiz_rejects_missing_section(self, book_module, tmp_path):
        source = tmp_path / "01-quiz.md"
        text = quiz_markdown(book_module).replace("## 補足\n\n本文\n\n", "")
        source.write_text(text, encoding="utf-8")
        with pytest.raises(book_module.QuizFormatError, match="レベル2見出し"):
            book_module.parse_quiz(source, 1)


class TestQuizRendering:
    def test_pandoc_latex_converts_superscript_zero(self, book_module, monkeypatch):
        def fake_run(command, **kwargs):
            assert command[0] == "pandoc"
            assert kwargs["input"] == "x⁰"
            assert kwargs["text"] is True
            assert kwargs["capture_output"] is True
            return SimpleNamespace(returncode=0, stdout="x⁰\n", stderr="")

        monkeypatch.setattr(book_module.shutil, "which", lambda name: name)
        monkeypatch.setattr(book_module.subprocess, "run", fake_run)
        assert book_module.pandoc_latex("x⁰", inline=True) == r"x\textsuperscript{0}"

    def test_pandoc_latex_rejects_multiple_inline_paragraphs(
        self, book_module, monkeypatch
    ):
        def fake_run(command, **kwargs):
            assert command[0] == "pandoc"
            assert kwargs["input"] == "本文"
            assert kwargs["text"] is True
            assert kwargs["capture_output"] is True
            return SimpleNamespace(returncode=0, stdout="段落1\n\n段落2", stderr="")

        monkeypatch.setattr(book_module.shutil, "which", lambda name: name)
        monkeypatch.setattr(book_module.subprocess, "run", fake_run)
        with pytest.raises(book_module.InlineConversionError):
            book_module.pandoc_latex("本文", inline=True)

    def test_parse_references_keeps_description_and_url(self, book_with_pandoc):
        quiz = book_with_pandoc.Quiz(1, Path("01-quiz.md"), "問題", "解答", [])
        before, entries = book_with_pandoc.parse_references(
            quiz,
            "根拠本文\n\n### 参考文献\n\n著者『資料』\nhttps://example.com/one\n\n"
            "別の著者『資料』\nhttps://example.com/two",
        )
        assert before == "根拠本文"
        assert [(entry.key, entry.note_latex, entry.url) for entry in entries] == [
            ("quiz-001-ref-01", "著者『資料』", "https://example.com/one"),
            ("quiz-001-ref-02", "別の著者『資料』", "https://example.com/two"),
        ]

    def test_parse_references_rejects_missing_url(self, book_module):
        quiz = book_module.Quiz(1, Path("01-quiz.md"), "問題", "解答", [])
        with pytest.raises(book_module.QuizFormatError, match="参考文献1"):
            book_module.parse_references(
                quiz, "根拠本文\n\n### 参考文献\n\n著者『資料』\nURLなし"
            )

    def test_render_body_adds_bibliography(self, book_with_pandoc):
        quiz = book_with_pandoc.Quiz(
            1,
            Path("01-quiz.md"),
            "問題",
            "解答",
            [
                ("補足", "補足本文"),
                (
                    "裏取り情報",
                    "根拠本文\n\n### 参考文献\n\n著者『資料』\nhttps://example.com",
                ),
            ],
        )
        body, entries = book_with_pandoc.render_body(quiz)
        assert "## 補足\n\n補足本文" in body
        assert "## 裏取り情報\n\n根拠本文" in body
        assert r"\QuizReferences{quiz-001-ref-01}" in body
        assert entries == [
            book_with_pandoc.BibEntry(
                "quiz-001-ref-01", "著者『資料』", "https://example.com"
            )
        ]

    def test_write_generated_creates_question_list_and_explanation(
        self, book_with_pandoc, tmp_path
    ):
        output = tmp_path / "book"
        (output / "resources").mkdir(parents=True)
        quiz = book_with_pandoc.Quiz(
            1,
            Path("01-quiz.md"),
            "問題",
            "解答",
            [
                ("補足", "解説本文"),
                (
                    "裏取り情報",
                    "根拠本文\n\n### 参考文献\n\n著者『資料』\nhttps://example.com",
                ),
            ],
        )
        book_with_pandoc.write_generated(output, [quiz])
        assert "問題" in (output / "contents/question-list.tex").read_text(
            encoding="utf-8"
        )
        assert r"\input{contents/explanations/01}" in (
            output / "contents/explanations.tex"
        ).read_text(encoding="utf-8")
        assert "解説本文" in (output / "contents/explanations/01.tex").read_text(
            encoding="utf-8"
        )
        assert "https://example.com" in (output / "resources/references.bib").read_text(
            encoding="utf-8"
        )

    def test_prepare_output_requires_explicit_update(self, book_module, tmp_path):
        template = tmp_path / "template"
        template.mkdir()
        (template / "main.tex").write_text("本文", encoding="utf-8")
        output = tmp_path / "output"
        output.mkdir()
        (output / "existing.txt").touch()
        with pytest.raises(book_module.PathError, match="空ではありません"):
            book_module.prepare_output(template, output, update=False)
        book_module.prepare_output(template, output, update=True)
        assert (output / "main.tex").read_text(encoding="utf-8") == "本文"
