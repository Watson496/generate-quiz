"""build_quiz_book.pyの入力解析と出力生成を関数単位で検査する。"""

from pathlib import Path
from types import SimpleNamespace

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

CONTENT_ALPHABET = "あいうえお漢字ABC0123？！、。 "
CONTENT = st.tuples(
    st.sampled_from(CONTENT_ALPHABET.replace(" ", "")),
    st.text(alphabet=CONTENT_ALPHABET, max_size=30),
).map(lambda parts: parts[0] + parts[1])


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
    # 各生成例で入力ファイルを上書きし、前の内容を引き継がない。
    @settings(
        max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    @given(
        question=CONTENT,
        answer=CONTENT,
        bodies=st.lists(CONTENT, min_size=7, max_size=7),
    )
    def test_parse_quiz_preserves_valid_content(
        self, book_module, tmp_path, question, answer, bodies
    ):
        """有効な問題ファイルから問題・解答・各節の本文を欠落なく取り出す。"""
        source = tmp_path / "01-quiz.md"
        sections = "\n\n".join(
            f"## {name}\n\n{body}"
            for name, body in zip(book_module.SECTIONS, bodies, strict=True)
        )
        source.write_text(
            f"# 第1問\n\n問題：{question}\n解答：{answer}\n\n{sections}\n",
            encoding="utf-8",
        )
        quiz = book_module.parse_quiz(source, 1)
        assert quiz.question_md == question.strip()
        assert quiz.answer_md == answer.strip()
        assert quiz.sections == [
            (name, body.strip())
            for name, body in zip(book_module.SECTIONS, bodies, strict=True)
        ]

    def test_quiz_files_sorts_by_number(self, book_module, tmp_path):
        """問題ファイルだけを問題番号順に列挙することを確認する。"""
        for name in ("02-b.md", "01-a.md", "memo.md"):
            (tmp_path / name).touch()
        assert [path.name for path in book_module.quiz_files(tmp_path)] == [
            "01-a.md",
            "02-b.md",
        ]

    def test_quiz_files_rejects_duplicate_number(self, book_module, tmp_path):
        """同じ問題番号を持つ複数のファイルを拒否することを確認する。"""
        (tmp_path / "01-a.md").touch()
        (tmp_path / "01-b.md").touch()
        with pytest.raises(book_module.QuizFileError, match="重複"):
            book_module.quiz_files(tmp_path)

    def test_parse_quiz_extracts_question_answer_and_sections(
        self, book_module, tmp_path
    ):
        """完成した問題ファイルから番号・問題・解答・節を解析できることを確認する。"""
        source = tmp_path / "01-quiz.md"
        source.write_text(quiz_markdown(book_module), encoding="utf-8")
        quiz = book_module.parse_quiz(source, 1)
        assert quiz.number == 1
        assert quiz.question_md == "何でしょう？"
        assert quiz.answer_md == "答え"
        assert [name for name, _ in quiz.sections] == book_module.SECTIONS

    def test_parse_quiz_rejects_mismatched_number(self, book_module, tmp_path):
        """見出しの問題番号がファイル名や期待番号と異なれば拒否する。"""
        source = tmp_path / "01-quiz.md"
        source.write_text(quiz_markdown(book_module, 2), encoding="utf-8")
        with pytest.raises(book_module.QuizFormatError, match="見出し=2"):
            book_module.parse_quiz(source, 1)

    def test_parse_quiz_rejects_missing_section(self, book_module, tmp_path):
        """必須の節を欠く問題ファイルを拒否することを確認する。"""
        source = tmp_path / "01-quiz.md"
        text = quiz_markdown(book_module).replace("## 補足\n\n本文\n\n", "")
        source.write_text(text, encoding="utf-8")
        with pytest.raises(book_module.QuizFormatError, match="レベル2見出し"):
            book_module.parse_quiz(source, 1)


class TestQuizRendering:
    def test_pandoc_latex_converts_superscript_zero(self, book_module, monkeypatch):
        """Pandocの出力に残る上付き0をTeXで表せる形式へ置換する。"""

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
        """インライン変換で複数段落が生じた場合に拒否する。"""

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
        """参考文献の記述とURLを対応する書誌項目として取り出す。"""
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
        """URLのない参考文献を不正な入力として拒否する。"""
        quiz = book_module.Quiz(1, Path("01-quiz.md"), "問題", "解答", [])
        with pytest.raises(book_module.QuizFormatError, match="参考文献1"):
            book_module.parse_references(
                quiz, "根拠本文\n\n### 参考文献\n\n著者『資料』\nURLなし"
            )

    def test_render_body_adds_bibliography(self, book_with_pandoc):
        """解説本文から参考文献を分離し、本文末尾に参照命令を加える。"""
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
        """問題一覧・問別解説・書誌データを対応づけて生成する。"""
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
        """既存の出力先は更新指定なしでは保護し、指定時だけテンプレートを配置する。"""
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
