"""配布スクリプトのCLI実行と関数テストに使う共通fixture。"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = (
    Path(__file__).resolve().parent.parent / "skills" / "generate-quiz" / "scripts"
)


@pytest.fixture
def run_script():
    def invoke(script, *args, stdin=None):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / script), *[str(arg) for arg in args]],
            input=stdin,
            capture_output=True,
            text=True,
        )

    return invoke


@pytest.fixture
def load_script(monkeypatch):
    def load(skill, filename):
        path = (
            Path(__file__).resolve().parent.parent
            / "skills"
            / skill
            / "scripts"
            / filename
        )
        module_name = f"test_{skill.replace('-', '_')}_{path.stem}"
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise ImportError(path)
        module = importlib.util.module_from_spec(spec)
        monkeypatch.syspath_prepend(str(path.parent))
        monkeypatch.setitem(sys.modules, module_name, module)
        spec.loader.exec_module(module)
        return module

    return load
