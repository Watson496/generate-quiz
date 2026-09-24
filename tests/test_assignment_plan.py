"""担当表からのステップの構成と依頼文を確認する。"""

import copy
import json
import re
from pathlib import Path

import pytest

REFERENCES = (
    Path(__file__).resolve().parent.parent / "skills" / "generate-quiz" / "references"
)


def small_table():
    """作る側と検査側が一つずつあるステップを二つ持つ担当表を作る。"""
    return {
        "data": {
            "conditions": "作問条件",
            "items": "候補の一覧",
            "item_review": "候補の検査記録",
            "draft": "問題文",
            "draft_review": "問題文の検査記録",
        },
        "parent_data": ["conditions"],
        "steps": [
            {
                "name": "候補",
                "roles": [
                    {
                        "id": "finder",
                        "name": "候補担当",
                        "side": "make",
                        "section": "候補",
                        "specs": ["work_state_spec.md"],
                        "inputs": [["conditions"]],
                        "outputs": ["items"],
                    },
                    {
                        "id": "item_checker",
                        "name": "候補の検査担当",
                        "side": "check",
                        "section": "候補",
                        "specs": ["work_state_spec.md"],
                        "inputs": [["items"]],
                        "outputs": ["item_review"],
                        "split_size": 2,
                    },
                ],
            },
            {
                "name": "作文",
                "roles": [
                    {
                        "id": "writer",
                        "name": "作文担当",
                        "side": "make",
                        "section": "作文",
                        "specs": ["work_state_spec.md"],
                        "inputs": [["conditions"]],
                        "outputs": ["draft"],
                    },
                    {
                        "id": "draft_checker",
                        "name": "問題文の検査担当",
                        "side": "check",
                        "section": "作文",
                        "specs": ["work_state_spec.md"],
                        "inputs": [["draft"], ["items"]],
                        "outputs": ["draft_review"],
                    },
                ],
            },
        ],
    }


def find_role(table, role_id):
    """担当表から担当を取り出す。"""
    return next(
        role
        for step in table["steps"]
        for role in step["roles"]
        if role["id"] == role_id
    )


class TestBundledTable:
    """同梱の担当表が工程の仕様と対応することを確認する。"""

    def test_table_is_valid(self, load_script):
        """同梱の担当表は検査に合格する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        assert module.load_table()["steps"]

    def test_sections_exist_in_workflow(self, load_script):
        """各担当の節が工程の仕様の見出しにある。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        text = (REFERENCES / "workflow_spec.md").read_text(encoding="utf-8")
        headings = set(re.findall(r"^## (.+)$", text, re.MULTILINE))
        sections = {
            role["section"] for _, role in module.ordered_roles(module.load_table())
        }
        assert headings >= sections | {"担当の構成"}

    def test_blind_phases_hold_only_draft(self, load_script):
        """解答を伏せる段階の入力は問題文だけである。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = module.load_table()
        for role_id in ("exposure", "audit"):
            assert find_role(table, role_id)["inputs"][0] == ["draft"]


class TestTableValidation:
    """担当表の不備を検出する。"""

    def test_small_table_is_valid(self, load_script):
        """前の担当の成果物と親のデータだけを入力にする表は合格する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        assert module.validate_table(small_table())

    @pytest.mark.parametrize(
        ("change", "message"),
        [
            (
                lambda table: table["steps"][0]["roles"][0]["inputs"][0].append(
                    "draft"
                ),
                "前の担当の成果物でも親が渡すデータでもない",
            ),
            (
                lambda table: table["steps"][0]["roles"][0]["inputs"][0].append(
                    "unknown"
                ),
                "未定義のデータ",
            ),
            (
                lambda table: table["steps"][1]["roles"][0].update(id="finder"),
                "担当finderが重複している",
            ),
            (
                lambda table: table["steps"][0]["roles"][0]["outputs"].append(
                    "conditions"
                ),
                "親が渡すデータを担当の成果物にしている",
            ),
            (
                lambda table: table["data"].update(orphan="どこにもない記録"),
                "どこからも渡されないデータ",
            ),
            (
                lambda table: table["steps"][0]["roles"][0].update(
                    specs=["missing_spec.md"]
                ),
                "存在しない仕様",
            ),
            (
                lambda table: table["steps"][0]["roles"][1].update(split_size=0),
                "split_sizeは1以上の整数",
            ),
        ],
    )
    def test_invalid_table(self, load_script, change, message):
        """担当表の不備を理由とともに拒否する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = copy.deepcopy(small_table())
        change(table)
        with pytest.raises(module.TableError, match=message):
            module.validate_table(table)


class TestSteps:
    """ステップの構成を確認する。"""

    def test_coordinator_only_for_several_roles(self, load_script):
        """担当が複数あるステップだけに統括役を置く。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = small_table()
        table["steps"][1]["roles"].pop()
        assert [step["coordinator"] for step in module.step_plan(table)] == [
            True,
            False,
        ]

    def test_coordinator_request_lists_roles(self, load_script):
        """統括役への依頼文はステップの担当を示し、担当が一つなら出さない。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = small_table()
        table["steps"][1]["roles"].pop()
        assert (
            "候補の検査担当（item_checker）"
            in module.coordinator_request(table, 1)["request"]
        )
        with pytest.raises(module.TableError, match="統括役を置かない"):
            module.coordinator_request(table, 2)

    def test_cli_outputs_steps(self, run_script):
        """ステップの構成をJSONで出力する。"""
        result = run_script("assignment_plan.py", "steps")
        assert result.returncode == 0
        steps = json.loads(result.stdout)
        assert steps[0]["roles"] == ["facet_selection"]


class TestRequests:
    """担当への依頼文を確認する。"""

    def test_split_items_by_size(self, load_script):
        """分割する担当は、件数ごとに項目を分けて割り当てる。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        result = module.assignments(
            small_table(), "item_checker", ["K1", "K2", "K3", "K4", "K5"]
        )
        assert [item["items"] for item in result] == [
            ["K1", "K2"],
            ["K3", "K4"],
            ["K5"],
        ]
        assert "担当する項目：K5" in result[2]["request"]

    def test_split_role_requires_items(self, load_script):
        """分割する担当に項目を渡さなければ拒否する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        with pytest.raises(module.TableError, match="項目IDが必要"):
            module.assignments(small_table(), "item_checker")

    def test_request_lists_phases_and_outputs(self, load_script):
        """依頼文は段階ごとの入力と成果物を示す。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        request = module.assignments(small_table(), "draft_checker")[0]["request"]
        assert "入力は2段階で渡す" in request
        assert "入力（第1段階）：\n- 問題文\n入力（第2段階）：\n- 候補の一覧" in request
        assert "成果物（指定されたファイルに書く）：\n- 問題文の検査記録" in request

    @pytest.mark.parametrize(
        "args",
        [
            ("assign", "unknown_role"),
            ("assign", "exposure", "--items", "K1"),
            ("coordinate", "1"),
            ("coordinate", "99"),
        ],
    )
    def test_usage_errors(self, run_script, args):
        """存在しない担当や分割しない担当への項目指定は呼出しの不備とする。"""
        result = run_script("assignment_plan.py", *args)
        assert result.returncode == 2
        assert "入力エラー" in result.stderr
