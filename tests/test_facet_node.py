"""facet_node.pyのカタログ検索とCLI動作を検査する。"""

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st


@pytest.fixture
def facet_module(load_script):
    return load_script("generate-quiz", "facet_node.py")


class TestFacetNodeFunctions:
    # 各生成例でカタログファイルを上書きし、前の内容を引き継がない。
    @settings(
        max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture]
    )
    @given(st.text(alphabet="abc123日本語.*+?()[]{}|\\^$", min_size=1, max_size=12))
    def test_find_block_treats_key_as_literal(
        self, facet_module, monkeypatch, tmp_path, suffix
    ):
        """正規表現の記号を含むキーでも完全一致するノードだけを取得する。"""
        key = f"subject::{suffix}"
        other = f"{key}x"
        source = tmp_path / "facet_subject.md"
        source.write_text(
            f"## FACET_NODE `{other}`\n別の対象\n<!-- END_FACET_NODE -->\n"
            f"## FACET_NODE `{key}`\n対象\n<!-- END_FACET_NODE -->\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(facet_module, "REF_DIR", tmp_path)
        path, block = facet_module.find_block(key)
        assert path == source
        assert block[0] == f"## FACET_NODE `{key}`"
        assert block[1] == "対象"

    def test_ref_files_places_index_first(self, facet_module, monkeypatch, tmp_path):
        """参照ファイルの列挙で索引を先頭に置き、対象外のファイルを除く。"""
        (tmp_path / "facet_subject.md").touch()
        (tmp_path / "facet_index.md").touch()
        (tmp_path / "other.md").touch()
        monkeypatch.setattr(facet_module, "REF_DIR", tmp_path)
        assert [path.name for path in facet_module.ref_files()] == [
            "facet_index.md",
            "facet_subject.md",
        ]

    def test_find_block_stops_at_terminator(self, facet_module, monkeypatch, tmp_path):
        """ノードの終端で抽出を止め、隣のノードを混ぜないことを確認する。"""
        source = tmp_path / "facet_subject.md"
        source.write_text(
            "## FACET_NODE `subject::1`\n内容\n<!-- END_FACET_NODE -->\n"
            "## FACET_NODE `subject::2`\n別内容\n<!-- END_FACET_NODE -->\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(facet_module, "REF_DIR", tmp_path)
        path, block = facet_module.find_block("subject::1")
        assert path == source
        assert block == [
            "## FACET_NODE `subject::1`",
            "内容",
            "<!-- END_FACET_NODE -->",
        ]
        assert facet_module.find_block("subject::3") == (None, None)

    def test_grep_labels_normalizes_and_deduplicates(
        self, facet_module, monkeypatch, tmp_path
    ):
        """表記の正規化後に検索し、同じキーの重複を除いて件数を制限する。"""
        (tmp_path / "facet_subject.md").write_text(
            "- `subject::1` | CODE `1` | ガキ\n"
            "- `subject::1` | CODE `1` | ガキ\n"
            "- `subject::2` | CODE `2` | ガキ\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(facet_module, "REF_DIR", tmp_path)
        assert facet_module.grep_labels("ガ", 1) == [
            ("subject::1", "1", "ガキ", "facet_subject.md")
        ]
        assert [hit[0] for hit in facet_module.grep_labels("ガ", 10)] == [
            "subject::1",
            "subject::2",
        ]

    def test_children_match_direct_children_count(self, facet_module):
        """キーに逆引用符を含む子も含め、全ノードで読み取る子の数がカタログの件数と一致する。"""
        for path in facet_module.ref_files():
            key, count, children = None, None, 0
            for line in facet_module.read_lines(path):
                if line.startswith("## FACET_NODE `"):
                    key, count, children = line, None, 0
                elif line.startswith("- DIRECT_CHILDREN_COUNT:"):
                    count = int(line.split(":")[1])
                elif facet_module.CHILD_RE.match(line):
                    children += 1
                elif facet_module.END_RE.match(line) and count is not None:
                    assert children == count, key

    def test_child_keys_keep_backquoted_key(self, facet_module):
        """UDCの固有補助番号の逆引用符をキーの一部として読む。"""
        assert "subject::81`01/`08" in facet_module.child_keys("subject::81")


class TestFacetNode:
    """ファセットカタログの参照。カタログにないノードを返さないことを主に見る。"""

    def test_existing_node_exits_0_with_direct_children(self, run_script):
        """既存ノードの本文と直属の子ノードを取得できることを確認する。"""
        r = run_script("facet_node.py", "subject::1")
        assert r.returncode == 0
        assert "NODE_KEY: `subject::1`" in r.stdout
        assert "DIRECT_CHILDREN" in r.stdout

    def test_block_is_single_and_terminated(self, run_script):
        """CLIが指定ノードの終端までの一ブロックだけを返すことを確認する。"""
        # 隣のノードを巻き込まず、1ブロックだけを返す
        r = run_script("facet_node.py", "subject::1")
        assert r.stdout.count("## FACET_NODE") == 1
        assert "END_FACET_NODE" in r.stdout

    def test_root_block_from_index(self, run_script):
        """ルートノードを索引から取得できることを確認する。"""
        r = run_script("facet_node.py", "time::ROOT")
        assert r.returncode == 0
        assert "FACET_ROOT `time::ROOT`" in r.stdout

    def test_key_with_quotes_and_parens(self, run_script):
        """引用符や括弧を含むノードキーをそのまま指定できることを確認する。"""
        # time::"0/2" や place::(1/9) のような記号を含むキーも、そのまま指定できる
        for key in ('time::"0/2"', "place::(1/9)"):
            assert run_script("facet_node.py", key).returncode == 0

    def test_unknown_node_exits_1(self, run_script):
        """存在しないノードは本文を出さず、未発見として報告する。"""
        r = run_script("facet_node.py", "subject::99999")
        assert r.returncode == 1
        assert "subject::99999" in r.stderr
        assert r.stdout == ""

    def test_children_only_lists_children(self, run_script):
        """子ノード一覧では親ノードの本文を出さないことを確認する。"""
        r = run_script("facet_node.py", "--children", "subject::1")
        assert r.returncode == 0
        assert "NODE_KEY:" not in r.stdout
        lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
        assert lines
        assert all(ln.startswith("- `") for ln in lines)

    def test_children_of_leaf_reports_none(self, run_script):
        """子を持たないノードの子ノード一覧に「なし」を返す。"""
        r = run_script("facet_node.py", "--children", "subject::101")
        assert r.returncode == 0
        assert r.stdout.strip() == "なし"

    def test_grep_hit_exits_0(self, run_script):
        """ラベル検索で一致するノードを返すことを確認する。"""
        r = run_script("facet_node.py", "--grep", "音楽")
        assert r.returncode == 0
        assert "subject::78" in r.stdout

    def test_grep_limit_is_respected(self, run_script):
        """ラベル検索の出力件数が指定上限を超えないことを確認する。"""
        r = run_script("facet_node.py", "--grep", "音楽", "--limit", "2")
        assert r.returncode == 0
        assert len(r.stdout.strip().splitlines()) == 2

    def test_grep_miss_exits_1(self, run_script):
        """一致するラベルがなければ結果を出さず未発見として返す。"""
        r = run_script("facet_node.py", "--grep", "存在しないラベル名XYZ")
        assert r.returncode == 1
        assert r.stdout == ""

    def test_no_argument_exits_2(self, run_script):
        """ノードキーも検索語もない呼び出しを入力エラーとして扱う。"""
        r = run_script("facet_node.py")
        assert r.returncode == 2
        assert "--grep" in r.stderr

    def test_empty_grep_exits_2(self, run_script):
        """空白だけの検索語を入力エラーとして扱う。"""
        assert run_script("facet_node.py", "--grep", "  ").returncode == 2

    def test_zero_limit_exits_2(self, run_script):
        """検索件数の上限に0を指定した場合は入力エラーとして扱う。"""
        assert (
            run_script("facet_node.py", "--grep", "音楽", "--limit", "0").returncode
            == 2
        )
