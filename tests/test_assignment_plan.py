"""担当表からの割り当てと再実行の判定を確認する。"""

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
        "given_data": ["conditions"],
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
                        "rules": [{"spec": "work_state_spec.md", "heading": "目的"}],
                        "inputs": [["conditions"]],
                        "outputs": ["items"],
                    },
                    {
                        "id": "item_checker",
                        "name": "候補の検査担当",
                        "side": "check",
                        "section": "候補",
                        "specs": ["work_state_spec.md"],
                        "rules": [{"spec": "work_state_spec.md", "heading": "目的"}],
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
                        "rules": [{"spec": "work_state_spec.md", "heading": "目的"}],
                        "inputs": [["conditions"]],
                        "outputs": ["draft"],
                    },
                    {
                        "id": "draft_checker",
                        "name": "問題文の検査担当",
                        "side": "check",
                        "section": "作文",
                        "specs": ["work_state_spec.md"],
                        "rules": [{"spec": "work_state_spec.md", "heading": "目的"}],
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

    def test_fragment_roles_write_state_keys_with_prefix(self, load_script):
        """題材探索の担当の依頼文は、接頭辞と探索状態のキーで断片を書かせる。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        request = module.assignments(module.load_table(), "saturation_review")[0][
            "request"
        ]
        assert (
            '`{"prefix": …, "entry_points": …, "candidates": …, "saturation_challenge": …}`'
            in request
        )

    def test_reviewers_read_review_procedure(self, load_script):
        """検査結果を記録する担当の依頼文だけが、検査の進め方の節を読ませる。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = module.load_table()
        review = module.assignments(table, "facet_weight_review")[0]["request"]
        maker = module.assignments(table, "facet_weighting")[0]["request"]
        assert (
            "「担当の構成」節、「ファセット選択」節、「検査の進め方」節を読み" in review
        )
        assert "検査の進め方" not in maker

    def test_blind_phases_hold_only_draft(self, load_script):
        """解答を伏せる段階の入力は問題文だけである。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        assert find_role(module.load_table(), "exposure")["inputs"][0] == ["draft"]

    def test_extraction_sees_answer_but_not_propositions(self, load_script):
        """実現命題の抽出担当は、問題文と解答対象だけを受け取り、裏取り済みの命題を見ない。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        role = find_role(module.load_table(), "proposition_extraction")
        assert role["inputs"] == [["answer_target", "draft"]]

    def test_writer_change_reruns_dependent_checks(self, load_script):
        """作文担当の成果物が変わると、それを入力とする検査と最終出力だけを再実行する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        plan = module.rerun_plan(module.load_table(), "writer")
        roles = {role for step in plan for role in step["roles"]}
        assert {
            "structure_review",
            "exposure",
            "finalization",
            "final_reflection_review",
        } <= roles
        assert not roles & {"source_reliability_review", "corroboration_review"}

    def test_exploration_change_stays_in_topic_selection(self, load_script):
        """探索台帳が変わっても、解答対象ごとの担当は再実行しない。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        plan = module.rerun_plan(module.load_table(), "exploration")
        assert [step["step"] for step in plan] == [3, 4, 5]


class TestTableValidation:
    """担当表の不備を検出する。"""

    def test_small_table_is_valid(self, load_script):
        """前の担当の成果物と、親や統括役が渡すデータだけを入力にする表は合格する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        assert module.validate_table(small_table())

    def test_role_can_read_own_output(self, load_script):
        """書き足していく記録は、同じ担当の入力にできる。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = small_table()
        table["steps"][0]["roles"][0]["inputs"][0].append("items")
        assert module.validate_table(table)

    @pytest.mark.parametrize(
        ("change", "message"),
        [
            (
                lambda table: table["steps"][0]["roles"][0]["inputs"][0].append(
                    "draft"
                ),
                "前の担当や自分の成果物でも親や統括役が渡すデータでもない",
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
                "親や統括役が渡すデータを担当の成果物にしている",
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
            (
                lambda table: table["steps"][0]["roles"][0].update(
                    rules=[{"spec": "quiz_generation_spec.md", "heading": "1. 目的"}]
                ),
                "rulesは、specsにある仕様の見出しの一覧",
            ),
            (
                lambda table: table["steps"][0]["roles"][0]["rules"].append(
                    {"spec": "work_state_spec.md", "heading": "目的"}
                ),
                "rulesに同じ見出しが重複している",
            ),
            (
                lambda table: table.update(state_keys={"unknown": ["a"]}),
                "state_keysは",
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

    def test_coordinator_for_single_split_role(self, load_script):
        """担当が一種類でも、項目で分割する担当なら統括役を置く。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = small_table()
        table["steps"][0]["roles"].pop(0)
        assert module.step_plan(table)[0]["coordinator"] is True

    def test_coordinator_request_lists_roles(self, load_script):
        """統括役の依頼はステップのエージェント名と担当を示し、担当が一つなら出さない。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        table = small_table()
        table["steps"][1]["roles"].pop()
        result = module.coordinator_request(table, 1)
        assert result["agent"] == "generate-quiz:step01_coordinator"
        assert "候補の検査担当（item_checker）" in result["request"]
        assert "`SKILL.md`の「必須ツール」「スクリプトの呼出し」節" in result["request"]
        assert (
            "「担当の構成」節、「候補」節、「検査で不合格になったとき」節、「修正と再実行」節"
            in result["request"]
        )
        assert (
            "出力が途中で切り詰められたら、残りの部分を分けて読む" in result["request"]
        )
        with pytest.raises(module.TableError, match="統括役を置かない"):
            module.coordinator_request(table, 2)

    def test_cli_outputs_steps(self, run_script):
        """ステップの構成をJSONで出力する。"""
        result = run_script("assignment_plan.py", "steps")
        assert result.returncode == 0
        steps = json.loads(result.stdout)
        assert steps[0]["roles"] == [
            "facet_granularity",
            "facet_weighting",
            "facet_granularity_review",
            "facet_subdivision_review",
            "facet_weight_review",
            "facet_distribution_review",
        ]


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

    def test_assignment_names_agent_and_skill_location(self, load_script):
        """割り当ては担当のエージェント名を示し、依頼文はスキルの場所を一度だけ書き、仕様を全文読ませる。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        result = module.assignments(small_table(), "draft_checker")[0]
        assert result["agent"] == "generate-quiz:draft_checker"
        request = result["request"]
        assert request.count(str(module.SKILL_DIR)) == 1
        assert "`references/work_state_spec.md`を全文読んで" in request
        assert "出力が途中で切り詰められたら、残りの部分を分けて読む" in request

    def test_split_role_requires_items(self, load_script):
        """分割する担当に項目を渡さなければ拒否する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        with pytest.raises(module.TableError, match="項目IDが必要"):
            module.assignments(small_table(), "item_checker")

    def test_request_lists_phases_and_report(self, load_script):
        """依頼文は段階ごとの入力と成果物をデータIDとともに示し、報告の範囲を示す。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        request = module.assignments(small_table(), "draft_checker")[0]["request"]
        assert "入力は2段階で渡す" in request
        assert (
            "入力（第1段階）：\n- 問題文（`draft`）\n入力（第2段階）：\n- 候補の一覧（`items`）"
            in request
        )
        assert (
            '成果物（指定されたファイルに、データIDをキーとするJSONのオブジェクト`{"draft_review": …}`として書く）：\n- 問題文の検査記録（`draft_review`）'
            in request
        )
        assert (
            "作業場所のファイル（状態ファイル、ほかの担当の成果物、前の実行の記録）を探したり読んだりしない"
            in request
        )
        assert request.endswith(
            "報告は、完了したことと成果物のファイルの場所だけとする。"
        )

    @pytest.mark.parametrize(
        "args",
        [
            ("assign", "unknown_role"),
            ("assign", "exposure", "--items", "K1"),
            ("coordinate", "8"),
            ("coordinate", "99"),
        ],
    )
    def test_usage_errors(self, run_script, args):
        """存在しない担当や分割しない担当への項目指定は呼出しの不備とする。"""
        result = run_script("assignment_plan.py", *args)
        assert result.returncode == 2
        assert "入力エラー" in result.stderr


class TestInputs:
    """状態ファイルから担当の入力だけを取り出すことを確認する。"""

    def test_inputs_extract_only_role_data(self, run_script, tmp_path):
        """担当の入力のキーだけを書き出し、台帳は定めたキーをまとめて取り出す。状態ファイルにない入力は示す。"""
        facet = tmp_path / "facet.json"
        facet.write_text(
            json.dumps(
                {
                    "facet_nodes": {"subject": "subject::1"},
                    "facet_levels": [{"id": "L1"}],
                }
            )
        )
        selection = tmp_path / "selection.json"
        selection.write_text(
            json.dumps(
                {
                    "facet_nodes": {"subject": "subject::2"},
                    "entry_points": [{"id": "E1"}],
                    "candidates": [{"id": "K1"}],
                    "memberships": [{"candidate_id": "K1"}],
                    "execution": {"assignments": []},
                }
            )
        )
        output = tmp_path / "input.json"
        result = run_script(
            "assignment_plan.py",
            "inputs",
            "membership",
            "--state",
            facet,
            selection,
            "--output",
            output,
        )
        assert result.returncode == 0
        assert json.loads(output.read_text()) == {
            "facet_nodes": {"subject": "subject::2"},
            "entry_points": [{"id": "E1"}],
            "candidates": [{"id": "K1"}],
        }
        assert json.loads(result.stdout)["not_in_state"] == [
            "facet_subdivisions",
            "facet_scope",
        ]

    def test_inputs_take_only_assigned_items(self, run_script, tmp_path):
        """分割する担当には、受け持つ項目の記録だけを取り出す。"""
        state = tmp_path / "target.json"
        state.write_text(
            json.dumps(
                {
                    "answer_target": "セデル",
                    "sources": [{"id": "S1"}, {"id": "S2"}, {"id": "S3"}],
                }
            )
        )
        output = tmp_path / "input.json"
        result = run_script(
            "assignment_plan.py",
            "inputs",
            "source_reliability",
            "--state",
            state,
            "--items",
            "S1",
            "S3",
            "--output",
            output,
        )
        assert result.returncode == 0
        assert json.loads(output.read_text()) == {
            "answer_target": "セデル",
            "sources": [{"id": "S1"}, {"id": "S3"}],
        }

    def test_inputs_reject_unknown_items(self, run_script, tmp_path):
        """受け持つ項目が、どの入力の記録のIDでもなければ拒む。"""
        state = tmp_path / "target.json"
        state.write_text(json.dumps({"sources": [{"id": "S1"}, {"id": "S2"}]}))
        result = run_script(
            "assignment_plan.py",
            "inputs",
            "source_reliability",
            "--state",
            state,
            "--items",
            "11",
            "12",
            "--output",
            tmp_path / "input.json",
        )
        assert result.returncode == 2
        assert "受け持つ項目['11', '12']が、どの入力の記録のIDでもない" in result.stderr

    def test_inputs_take_latest_review_of_each_target(self, run_script, tmp_path):
        """後ろへ加えていく検査結果は、検査した対象ごとの最後の記録だけを渡す。"""
        old = {"clue_id": "C1", "status": "failed", "reason": "前の周"}
        new = {"clue_id": "C1", "status": "passed", "reason": "今の周"}
        other = {"clue_id": "C2", "status": "passed", "reason": "別の手掛かり"}
        state = tmp_path / "target.json"
        state.write_text(json.dumps({"competitor_search_reviews": [old, other, new]}))
        output = tmp_path / "input.json"
        result = run_script(
            "assignment_plan.py",
            "inputs",
            "competitor_comparison_review",
            "--state",
            state,
            "--output",
            output,
        )
        assert result.returncode == 0
        assert json.loads(output.read_text())["competitor_search_reviews"] == [
            other,
            new,
        ]

    def test_inputs_take_one_phase(self, run_script, tmp_path):
        """段階を指定すると、その段階の入力だけを取り出し、問題文は版と本文だけを渡す。"""
        state = tmp_path / "target.json"
        state.write_text(
            json.dumps(
                {
                    "draft": {"version": 1, "text": "問題文", "answer_target": "解答"},
                    "names": [{"id": "N1"}],
                }
            )
        )
        output = tmp_path / "input.json"
        result = run_script(
            "assignment_plan.py",
            "inputs",
            "exposure",
            "--state",
            state,
            "--phase",
            "1",
            "--output",
            output,
        )
        assert result.returncode == 0
        assert json.loads(output.read_text()) == {
            "draft": {"version": 1, "text": "問題文"}
        }


class TestMerge:
    """担当の成果物を、担当表のまとめ方に従って状態ファイルへ入れることを確認する。"""

    def merge(self, run_script, tmp_path, role, state, artifact):
        state_path = tmp_path / "state.json"
        state_path.write_text(json.dumps(state, ensure_ascii=False))
        artifact_path = tmp_path / f"{role}.json"
        artifact_path.write_text(json.dumps(artifact, ensure_ascii=False))
        result = run_script(
            "assignment_plan.py",
            "merge",
            role,
            "--state",
            state_path,
            "--artifact",
            artifact_path,
        )
        return result, json.loads(state_path.read_text())

    def test_sources_keep_quotes_written_by_other_roles(self, run_script, tmp_path):
        """記録済みの資料に引用を加えると、前の担当の引用を残し、新しい資料は後ろへ加える。"""
        state = {
            "sources": [
                {"id": "S1", "citation": "資料1", "quotes": [{"id": "Q1", "text": "a"}]}
            ]
        }
        artifact = {
            "sources": [
                {
                    "id": "S1",
                    "citation": "資料1",
                    "quotes": [{"id": "Q2", "text": "b"}],
                },
                {
                    "id": "S2",
                    "citation": "資料2",
                    "quotes": [{"id": "Q3", "text": "c"}],
                },
            ],
            "clues": [{"id": "C1", "fact": "事実", "proposition_ids": ["P1"]}],
            "propositions": [{"id": "P1", "claim": "命題"}],
        }
        result, merged = self.merge(
            run_script, tmp_path, "clue_search", state, artifact
        )
        assert result.returncode == 0
        assert [quote["id"] for quote in merged["sources"][0]["quotes"]] == ["Q1", "Q2"]
        assert [source["id"] for source in merged["sources"]] == ["S1", "S2"]
        assert merged["clues"] == artifact["clues"]

    def test_rejects_new_id_for_recorded_source_url(self, run_script, tmp_path):
        """記録済みの資料と同じURLに別の資料IDを付けた成果物は、状態ファイルを変えずに拒む。"""
        state = {
            "sources": [{"id": "S1", "url": "https://example.org/a", "quotes": []}]
        }
        artifact = {
            "sources": [{"id": "S9", "url": "https://example.org/a", "quotes": []}],
            "clues": [],
            "propositions": [],
        }
        result, merged = self.merge(
            run_script, tmp_path, "clue_search", state, artifact
        )
        assert result.returncode == 1
        assert "sourcesのS9は、記録済みのS1とurlが同じである" in result.stderr
        assert merged == state

    def test_rejects_new_id_for_recorded_name(self, run_script, tmp_path):
        """記録済みの名称と同じ名称に別の名称IDを付けた成果物は、状態ファイルを変えずに拒む。"""
        state = {"names": [{"id": "N1", "name": "玉縁ボタンホール", "usage": "u"}]}
        artifact = {
            "sources": [],
            "names": [{"id": "N9", "name": "玉縁ボタンホール", "usage": "u"}],
        }
        result, merged = self.merge(
            run_script, tmp_path, "name_research", state, artifact
        )
        assert result.returncode == 1
        assert "namesのN9は、記録済みのN1とnameが同じである" in result.stderr
        assert merged == state

    def test_rejects_recorded_clue_id_with_other_fact(self, run_script, tmp_path):
        """記録済みの手掛かり候補のIDを、別の事実に使った成果物は拒む。"""
        state = {
            "clues": [{"id": "C1", "fact": "和裁の操作", "proposition_ids": ["P1"]}],
            "propositions": [{"id": "P1", "claim": "命題"}],
        }
        artifact = {
            "sources": [],
            "clues": [{"id": "C1", "fact": "補強の用途", "proposition_ids": ["P1"]}],
            "propositions": [{"id": "P1", "claim": "命題"}],
        }
        result, merged = self.merge(
            run_script, tmp_path, "clue_search", state, artifact
        )
        assert result.returncode == 1
        assert "cluesのC1は、記録済みの記録とfactが異なる" in result.stderr
        assert merged == state

    def test_rejects_failed_review_with_unknown_fix_data(self, run_script, tmp_path):
        """修正対象にデータIDでない値を置いた不合格の判定は、状態ファイルへ入れずに拒む。"""
        review = {
            "target": "G1",
            "status": "failed",
            "reason": "r",
            "fix_data": ["S-N1"],
        }
        result, merged = self.merge(
            run_script,
            tmp_path,
            "topic_weight_review",
            {},
            {"topic_weight_reviews": [review]},
        )
        assert result.returncode == 1
        assert "fix_dataに、担当表のデータIDでない値がある: ['S-N1']" in result.stderr
        assert merged == {}

    def test_split_records_replace_same_item(self, run_script, tmp_path):
        """件数ごとに分けた担当の記録は、同じ項目の記録を置き換え、ほかの項目の記録を残す。"""
        state = {
            "memberships": [
                {"candidate_id": "K1", "axes": "前の判定"},
                {"candidate_id": "K2", "axes": "別の担当の判定"},
            ]
        }
        artifact = {"memberships": [{"candidate_id": "K1", "axes": "直した判定"}]}
        result, merged = self.merge(run_script, tmp_path, "membership", state, artifact)
        assert result.returncode == 0
        assert merged["memberships"] == [
            {"candidate_id": "K1", "axes": "直した判定"},
            {"candidate_id": "K2", "axes": "別の担当の判定"},
        ]

    def test_single_writer_record_drops_removed_fields(self, run_script, tmp_path):
        """一つの担当だけが書く記録は、直した記録で丸ごと置き換え、なくした項目を残さない。"""
        before = {
            "clue_id": "C1",
            "competitor_id": "CP1",
            "disposition": "excluded",
            "exclusion_passage": "前の判断の箇所",
        }
        after = {"clue_id": "C1", "competitor_id": "CP1", "disposition": "retained"}
        result, merged = self.merge(
            run_script,
            tmp_path,
            "competitor_comparison",
            {"competitor_comparisons": [before]},
            {"competitor_comparisons": [after]},
        )
        assert result.returncode == 0
        assert merged["competitor_comparisons"] == [after]

    def test_regrouping_drops_weights_outside_groups(self, run_script, tmp_path):
        """まとまりを切り直すと、まとまりから外れた候補とまとまりのweightを除く。"""
        state = {
            "topic_groups": [
                {"id": "G1", "candidate_ids": ["K1", "K2"]},
                {"id": "G2", "candidate_ids": ["K3"]},
            ],
            "group_weights": [{"group_id": "G1"}, {"group_id": "G2"}],
            "candidate_weights": [
                {"candidate_id": "K1"},
                {"candidate_id": "K2"},
                {"candidate_id": "K3"},
            ],
        }
        artifact = {"topic_groups": [{"id": "G1", "candidate_ids": ["K1", "K3"]}]}
        result, merged = self.merge(
            run_script, tmp_path, "topic_grouping", state, artifact
        )
        assert result.returncode == 0
        assert merged["group_weights"] == [{"group_id": "G1"}]
        assert merged["candidate_weights"] == [
            {"candidate_id": "K1"},
            {"candidate_id": "K3"},
        ]

    def test_rejects_weight_for_candidate_outside_groups(self, run_script, tmp_path):
        """まとまりにない候補のweightを置いた成果物は、状態ファイルを変えずに拒む。"""
        state = {"topic_groups": [{"id": "G1", "candidate_ids": ["K1"]}]}
        artifact = {
            "candidate_weights": [{"candidate_id": "K1"}, {"candidate_id": "K9"}]
        }
        result, merged = self.merge(
            run_script, tmp_path, "topic_weighting", state, artifact
        )
        assert result.returncode == 1
        assert (
            "成果物のcandidate_weightsのcandidate_idに、topic_groupsにない値がある: ['K9']"
            in result.stderr
        )
        assert merged == state

    def test_rejudged_levels_drop_weights_and_picks(self, run_script, tmp_path):
        """粒度判断をし直すと、子へ進まなくなった階層と除いた階層のweightと抽選結果を除く。"""
        state = {
            "facet_levels": [
                {"id": "L1", "decision": "descend"},
                {"id": "L2", "decision": "descend"},
                {"id": "L3", "decision": "stop"},
            ],
            "facet_subdivisions": [{"parent": "subject::646.2", "children": []}],
            "facet_weights": [{"level_id": "L1"}, {"level_id": "L2"}],
            "facet_picks": [{"level_id": "L1"}, {"level_id": "L2"}],
        }
        artifact = {
            "facet_levels": [
                {"id": "L1", "decision": "descend"},
                {"id": "L4", "decision": "stop", "return_id": "R1"},
            ],
            "facet_subdivisions": [],
            "facet_nodes": {},
        }
        result, merged = self.merge(
            run_script, tmp_path, "facet_granularity", state, artifact
        )
        assert result.returncode == 0
        assert [level["id"] for level in merged["facet_levels"]] == ["L1", "L4"]
        assert merged["facet_subdivisions"] == []
        assert merged["facet_weights"] == [{"level_id": "L1"}]
        assert merged["facet_picks"] == [{"level_id": "L1"}]

    def test_reviews_keep_failed_record(self, run_script, tmp_path):
        """再検査の結果は、不合格の記録を残したまま後ろへ加える。"""
        failed = {"target": "G1", "status": "failed", "reason": "r", "fix_data": ["x"]}
        passed = {"target": "G1", "status": "passed", "reason": "r"}
        result, merged = self.merge(
            run_script,
            tmp_path,
            "topic_weight_review",
            {"topic_weight_reviews": [failed]},
            {"topic_weight_reviews": [passed]},
        )
        assert result.returncode == 0
        assert merged["topic_weight_reviews"] == [failed, passed]

    def test_other_data_is_replaced(self, run_script, tmp_path):
        """まとめ方を定めていないデータは、新しい成果物で置き換える。"""
        result, merged = self.merge(
            run_script,
            tmp_path,
            "asked_knowledge",
            {"asked_knowledge": "前", "answer_granularity": "前"},
            {"asked_knowledge": "後", "answer_granularity": "後"},
        )
        assert result.returncode == 0
        assert merged == {"asked_knowledge": "後", "answer_granularity": "後"}

    @pytest.mark.parametrize(
        "artifact",
        [{"G1": {"status": "passed"}}, [{"target": "G1"}], {}],
    )
    def test_rejects_artifact_not_keyed_by_data_id(
        self, run_script, tmp_path, artifact
    ):
        """最上位のキーが成果物のデータIDでない成果物は、状態ファイルを変えずに拒む。"""
        state = {"topic_weight_reviews": []}
        result, merged = self.merge(
            run_script, tmp_path, "topic_weight_review", state, artifact
        )
        assert result.returncode == 1
        assert "データID ['topic_weight_reviews'] でなければならない" in result.stderr
        assert merged == state

    def test_rejects_single_record_for_record_list(self, run_script, tmp_path):
        """記録を加えていくデータは、状態ファイルにまだなくても記録の配列でなければ拒む。"""
        record = {"candidate_id": "K1", "result": "pass", "reason": "r"}
        result, merged = self.merge(
            run_script, tmp_path, "prejudgment_scope", {}, {"prejudgment_scope": record}
        )
        assert result.returncode == 1
        assert (
            "成果物のprejudgment_scopeは記録の配列でなければならない" in result.stderr
        )
        assert merged == {}

    def test_replaced_data_can_correct_wrong_type(self, run_script, tmp_path):
        """置き換えるデータは、前に入れた記録の形が誤っていても、直した成果物で置き換えられる。"""
        result, merged = self.merge(
            run_script,
            tmp_path,
            "asked_knowledge",
            {"asked_knowledge": {"text": "誤った形"}, "answer_granularity": "粒度"},
            {"asked_knowledge": "問う知識", "answer_granularity": "粒度"},
        )
        assert result.returncode == 0
        assert merged["asked_knowledge"] == "問う知識"

    def test_rejects_record_list_data_in_other_shape(self, run_script, tmp_path):
        """記録の配列と定めたデータは、置き換える場合も記録の配列でなければ拒む。"""
        result, merged = self.merge(
            run_script,
            tmp_path,
            "answer_range",
            {},
            {"answers": {"A1": "セデル"}, "answer_judgments": []},
        )
        assert result.returncode == 1
        assert "成果物のanswersは記録の配列でなければならない" in result.stderr
        assert merged == {}

    def test_rejects_fragment_roles(self, run_script, tmp_path):
        """題材探索の断片は、このスクリプトでは入れない。"""
        result, _ = self.merge(
            run_script, tmp_path, "exploration", {}, {"coverage_areas": []}
        )
        assert result.returncode == 2
        assert "このスクリプトで入れるものではない" in result.stderr


class TestRecord:
    """担当の起動の記録を、状態ファイルの決まった場所へ書くことを確認する。"""

    def record(self, run_script, path, *args):
        return run_script("assignment_plan.py", "record", *args, "--state", path)

    def test_records_launch_artifact_and_failure(self, run_script, tmp_path):
        """起動の記録を加え、回収した成果物の場所と失敗を同じ記録へ加える。ほかのキーは変えない。"""
        path = tmp_path / "selection.json"
        path.write_text(json.dumps({"candidates": [{"id": "K1"}]}))
        result = self.record(
            run_script, path, "membership", "--agent-id", "a1", "--items", "K1"
        )
        assert result.returncode == 0
        result = self.record(
            run_script, path, "membership", "--agent-id", "a1", "--artifact", "m.json"
        )
        assert result.returncode == 0
        result = self.record(
            run_script,
            path,
            "exposure_precheck",
            "--agent-id",
            "a2",
            "--items",
            "K1",
        )
        result = self.record(
            run_script,
            path,
            "exposure_precheck",
            "--agent-id",
            "a2",
            "--failed",
            "実行環境のエラーで止まった",
        )
        assert result.returncode == 0
        assert json.loads(result.stdout)["status"] == "failed"
        result = self.record(
            run_script, path, "membership", "--agent-id", "a1", "--artifact", "m2.json"
        )
        assert json.loads(result.stdout)["role"] == "membership"
        state = json.loads(path.read_text())
        assert state["candidates"] == [{"id": "K1"}]
        assert state["execution"] == {
            "delegation_available": True,
            "assignments": [
                {
                    "role": "membership",
                    "agent": "generate-quiz:membership",
                    "agent_id": "a1",
                    "artifact_refs": ["m.json", "m2.json"],
                    "items": ["K1"],
                },
                {
                    "role": "exposure_precheck",
                    "agent": "generate-quiz:exposure_precheck",
                    "agent_id": "a2",
                    "artifact_refs": [],
                    "items": ["K1"],
                    "status": "failed",
                    "failure_reason": "実行環境のエラーで止まった",
                },
            ],
        }

    def test_rejects_artifact_for_unknown_launch(self, run_script, tmp_path):
        """起動の記録がない担当に、成果物の場所を加えない。"""
        path = tmp_path / "selection.json"
        path.write_text("{}")
        result = self.record(
            run_script, path, "membership", "--agent-id", "a1", "--artifact", "m.json"
        )
        assert result.returncode == 2
        assert "a1のmembershipの起動の記録がない" in result.stderr


class TestFixFromState:
    """状態ファイルの不合格の検査から修正の計画を作ることを確認する。"""

    def test_collects_every_failed_review(self, run_script, tmp_path):
        """最後の判定が不合格の検査の修正対象をすべて集め、修正させる担当ごとに検査の成果物を示す。"""
        state = tmp_path / "target.json"
        state.write_text(
            json.dumps(
                {
                    "certainty_reviews": [
                        {
                            "proposition_id": "P1",
                            "status": "failed",
                            "reason": "r",
                            "fix_data": ["proposition_certainty"],
                        },
                        {
                            "proposition_id": "P2",
                            "status": "failed",
                            "reason": "r",
                            "fix_data": ["proposition_certainty"],
                        },
                        {"proposition_id": "P2", "status": "passed", "reason": "r"},
                    ],
                    "naturalness_review": {
                        "status": "failed",
                        "reason": "r",
                        "fix_data": ["draft"],
                    },
                    "execution": {
                        "delegation_available": True,
                        "assignments": [
                            {
                                "role": "certainty_review",
                                "agent": "a",
                                "agent_id": "c1",
                                "artifact_refs": ["009/certainty_review.json"],
                            },
                            {
                                "role": "naturalness_review",
                                "agent": "a",
                                "agent_id": "n1",
                                "artifact_refs": ["009/naturalness_review.json"],
                            },
                        ],
                    },
                }
            )
        )
        result = run_script("assignment_plan.py", "fix", "--state", state)
        assert result.returncode == 0, result.stderr
        plan = json.loads(result.stdout)
        assert sorted(
            (item["data"], item["record"].get("proposition_id", ""))
            for item in plan["failed_reviews"]
        ) == [("certainty_reviews", "P1"), ("naturalness_review", "")]
        reviews = {entry["role"]: entry["reviews"] for entry in plan["fix"]}
        assert reviews["certainty"] == [
            {"data": "certainty_reviews", "artifacts": ["009/certainty_review.json"]}
        ]
        assert reviews["writer"] == [
            {"data": "naturalness_review", "artifacts": ["009/naturalness_review.json"]}
        ]


class TestEntryCheck:
    """統括役を起動する前に、前のステップの検査を行うことを確認する。"""

    def test_coordinate_requires_state_after_step_one(self, run_script):
        """前のステップの検査を定めたステップでは、状態ファイルを求める。"""
        result = run_script("assignment_plan.py", "coordinate", "3")
        assert result.returncode == 2
        assert "--stateで状態ファイルが必要" in result.stderr

    def test_coordinate_returns_when_intersection_is_not_viable(
        self, run_script, tmp_path, selection_state
    ):
        """交差領域が不成立なら、題材探索の統括役の依頼文を出さず粒度判断へ戻す。"""
        selection_state["intersection_review"]["result"] = "not_viable"
        path = tmp_path / "selection.json"
        path.write_text(json.dumps(selection_state, ensure_ascii=False))
        result = run_script("assignment_plan.py", "coordinate", "3", "--state", path)
        assert result.returncode == 3
        assert "粒度判断へ戻る" in result.stderr
        assert result.stdout == ""

    def test_coordinate_returns_when_discovery_is_not_convergent(
        self, run_script, tmp_path, selection_state
    ):
        """探索が未収束なら、抽選前の予備検査の統括役の依頼文を出さない。"""
        selection_state["saturation_challenge"][-1]["breadth"] = "not_convergent"
        path = tmp_path / "selection.json"
        path.write_text(json.dumps(selection_state, ensure_ascii=False))
        result = run_script("assignment_plan.py", "coordinate", "4", "--state", path)
        assert result.returncode == 3

    def test_coordinate_outputs_request_after_passed_check(
        self, run_script, tmp_path, selection_state
    ):
        """前のステップの検査に合格したら、依頼文を出力する。"""
        path = tmp_path / "selection.json"
        path.write_text(json.dumps(selection_state, ensure_ascii=False))
        result = run_script("assignment_plan.py", "coordinate", "3", "--state", path)
        assert result.returncode == 0
        assert json.loads(result.stdout)["agent"] == "generate-quiz:step03_coordinator"


class TestRerun:
    """修正時に再実行する担当の判定を確認する。"""

    def test_fix_returns_makers_and_later_reruns(self, load_script):
        """修正を求めたデータを作る担当と、その後に再実行する担当を返す。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        plan = module.fix_plan(
            module.load_table(), ["propositions", "proposition_support"]
        )
        assert plan["fix"] == [
            {"step": 7, "role": "clue_search"},
            {"step": 7, "role": "corroboration"},
        ]
        rerun = {entry["step"]: entry["roles"] for entry in plan["rerun"]}
        assert "certainty" in rerun[7]
        assert "clue_search" not in rerun[7]
        assert rerun[8] == ["writer"]

    def test_fix_returns_checker_whose_output_is_wrong(self, load_script):
        """検査側の担当の成果物の修正を求めたら、その担当と後の担当を返す。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        plan = module.fix_plan(module.load_table(), ["extracted_propositions"])
        assert plan["fix"] == [{"step": 9, "role": "proposition_extraction"}]
        assert plan["rerun"] == [{"step": 9, "roles": ["proposition_matching"]}]

    def test_checker_reruns_after_maker_fix(self, load_script):
        """作る側の担当も修正するなら、検査側の担当は修正させずに再実行する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        plan = module.fix_plan(module.load_table(), ["draft", "extracted_propositions"])
        assert plan["fix"] == [{"step": 8, "role": "writer"}]
        rerun = {entry["step"]: entry["roles"] for entry in plan["rerun"]}
        assert "proposition_extraction" in rerun[9]

    @pytest.mark.parametrize(
        ("data", "message"),
        [
            (["unknown_data"], "担当表にないデータ"),
            (["user_conditions"], "担当の成果物ではない"),
        ],
    )
    def test_fix_rejects_data_without_maker(self, load_script, data, message):
        """担当表にないデータや、担当の成果物でないデータは拒否する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        with pytest.raises(module.TableError, match=message):
            module.fix_plan(module.load_table(), data)

    def test_rerun_follows_later_inputs(self, load_script):
        """成果物を入力とする後の担当を、連鎖も含めて再実行する。"""
        module = load_script("generate-quiz", "assignment_plan.py")
        assert module.rerun_plan(small_table(), "finder") == [
            {"step": 1, "roles": ["item_checker"]},
            {"step": 2, "roles": ["draft_checker"]},
        ]
        assert module.rerun_plan(small_table(), "writer") == [
            {"step": 2, "roles": ["draft_checker"]}
        ]
