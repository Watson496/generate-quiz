"""配布スクリプトをCLIとして実行する共通fixture。"""

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
