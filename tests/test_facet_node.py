"""facet_node.pyのCLI動作を検査する。"""


class TestFacetNode:
    """ファセットカタログの参照。カタログにないノードを返さないことを主に見る。"""

    def test_existing_node_exits_0_with_direct_children(self, run_script):
        r = run_script("facet_node.py", "subject::1")
        assert r.returncode == 0
        assert "NODE_KEY: `subject::1`" in r.stdout
        assert "DIRECT_CHILDREN" in r.stdout

    def test_block_is_single_and_terminated(self, run_script):
        # 隣のノードを巻き込まず、1ブロックだけを返す
        r = run_script("facet_node.py", "subject::1")
        assert r.stdout.count("## FACET_NODE") == 1
        assert "END_FACET_NODE" in r.stdout

    def test_root_block_from_index(self, run_script):
        r = run_script("facet_node.py", "time::ROOT")
        assert r.returncode == 0
        assert "FACET_ROOT `time::ROOT`" in r.stdout

    def test_key_with_quotes_and_parens(self, run_script):
        # time::"0/2" や place::(1/9) のような記号を含むキーも、そのまま指定できる
        for key in ('time::"0/2"', "place::(1/9)"):
            assert run_script("facet_node.py", key).returncode == 0

    def test_unknown_node_exits_1(self, run_script):
        r = run_script("facet_node.py", "subject::99999")
        assert r.returncode == 1
        assert "subject::99999" in r.stderr
        assert r.stdout == ""

    def test_children_only_lists_children(self, run_script):
        r = run_script("facet_node.py", "--children", "subject::1")
        assert r.returncode == 0
        assert "NODE_KEY:" not in r.stdout
        lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
        assert lines
        assert all(ln.startswith("- `") for ln in lines)

    def test_children_of_leaf_reports_none(self, run_script):
        r = run_script("facet_node.py", "--children", "subject::101")
        assert r.returncode == 0
        assert r.stdout.strip() == "なし"

    def test_grep_hit_exits_0(self, run_script):
        r = run_script("facet_node.py", "--grep", "音楽")
        assert r.returncode == 0
        assert "subject::78" in r.stdout

    def test_grep_limit_is_respected(self, run_script):
        r = run_script("facet_node.py", "--grep", "音楽", "--limit", "2")
        assert r.returncode == 0
        assert len(r.stdout.strip().splitlines()) == 2

    def test_grep_miss_exits_1(self, run_script):
        r = run_script("facet_node.py", "--grep", "存在しないラベル名XYZ")
        assert r.returncode == 1
        assert r.stdout == ""

    def test_no_argument_exits_2(self, run_script):
        r = run_script("facet_node.py")
        assert r.returncode == 2
        assert "--grep" in r.stderr

    def test_empty_grep_exits_2(self, run_script):
        assert run_script("facet_node.py", "--grep", "  ").returncode == 2

    def test_zero_limit_exits_2(self, run_script):
        assert (
            run_script("facet_node.py", "--grep", "音楽", "--limit", "0").returncode
            == 2
        )
