"""担当表からエージェントの定義を作るスクリプトの動作を確認する。"""

import importlib.util
import subprocess
import sys
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "tools" / "agent_definitions.py"


@pytest.fixture
def module():
    spec = importlib.util.spec_from_file_location("agent_definitions", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def run(*args):
    return subprocess.run(
        [sys.executable, str(TOOL), *map(str, args)],
        capture_output=True,
        text=True,
        check=False,
    )


class TestSectionText:
    """見出しからの節の切り出しを確認する。"""

    TEXT = "# 題\n\n## 1. 甲\n\n本文甲\n\n### 1.1 乙\n\n本文乙\n\n## 2. 丙\n\n本文丙\n"

    def test_includes_subsections(self, module):
        """下位の節を含めて、同じ階層の次の見出しの前までを返す。"""
        text = module.section_text(self.TEXT, "1. 甲")
        assert "本文乙" in text
        assert "本文丙" not in text

    def test_excludes_subsections(self, module):
        """下位の節を含めない指定では、次の見出しの前までを返す。"""
        text = module.section_text(self.TEXT, "1. 甲", subsections=False)
        assert "本文甲" in text
        assert "本文乙" not in text

    def test_rejects_missing_heading(self, module):
        """仕様にない見出しは入力の不備とする。"""
        with pytest.raises(
            module.assignment_plan.TableError, match="見出しが仕様にない"
        ):
            module.section_text(self.TEXT, "3. 丁")


class TestDefinitions:
    """担当表と仕様から作る定義を確認する。"""

    def test_exploration_carries_candidate_definition(self, module):
        """題材探索担当の定義に、担当の節と候補の定義の本文が入る。"""
        table = module.assignment_plan.load_table()
        body = module.definitions(table, "codex")["generate-quiz-exploration.toml"]
        instructions = tomllib.loads(body)["developer_instructions"]
        assert "## 題材探索" in instructions
        assert "対象をそのものズバリ説明する説明" in instructions
        assert "### 6.1" not in instructions

    def test_codex_names_are_prefixed(self, module):
        """Codexの定義の名前はスキル名を接頭辞にする。"""
        table = module.assignment_plan.load_table()
        names = {
            tomllib.loads(body)["name"]
            for body in module.definitions(table, "codex").values()
        }
        assert "generate-quiz:exploration" in names
        assert len(names) == len(module.assignment_plan.ordered_roles(table))

    @pytest.mark.parametrize("form", ["codex", "claude"])
    def test_repository_definitions_are_current(self, form):
        """リポジトリに置いた定義は、担当表と仕様から作った定義に一致する。"""
        result = run(form, ROOT / form / "agents", "--check")
        assert result.returncode == 0, result.stderr

    def test_check_reports_stale_definition(self, tmp_path):
        """担当表や仕様と一致しない定義を報告する。"""
        assert run("claude", tmp_path).returncode == 0
        (tmp_path / "exploration.md").write_text("古い定義\n", encoding="utf-8")
        result = run("claude", tmp_path, "--check")
        assert result.returncode == 1
        assert "exploration.md" in result.stderr
