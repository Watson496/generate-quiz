"""length_check.pyの計算とCLI動作を検査する。"""

import math

import pytest


@pytest.fixture
def length_module(load_script):
    return load_script("generate-quiz", "length_check.py")


class TestLengthCheckFunctions:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("問題：が\nき", "がき"),
            ("問題:  あ \r\n い ", "あ  い"),
            ("  あ\nい  ", "あい"),
            ("あ  い", "あ  い"),
        ],
    )
    def test_normalize(self, length_module, text, expected):
        assert length_module.normalize(text) == expected

    def test_acceptance_at_mode_and_invalid_length(self, length_module):
        assert length_module.acceptance(80, 80) == pytest.approx(1)
        assert length_module.acceptance(0, 80) == 0
        assert length_module.acceptance(-1, 80) == 0

    def test_acceptance_uses_requested_mode(self, length_module):
        assert length_module.acceptance(100, 100) == pytest.approx(1)
        assert length_module.acceptance(80, 100) < 1


class TestLengthCheck:
    """文字数の計測と採否の判定。満たしていないハード制約を通さないことを主に見る。"""

    def test_prefix_and_newlines_are_excluded(self, run_script):
        r = run_script("length_check.py", "問題：" + "あ" * 80 + "\n")
        assert "LENGTH\t80" in r.stdout

    def test_ascii_colon_prefix_is_also_excluded(self, run_script):
        assert "LENGTH\t80" in run_script("length_check.py", "問題:" + "あ" * 80).stdout

    def test_nfc_normalization_before_counting(self, run_script):
        # 濁点を合成する場合、NFDの2コードポイントを1文字として数える
        r = run_script("length_check.py", "が" * 10)
        assert "LENGTH\t10" in r.stdout

    def test_mode_length_always_accepted(self, run_script):
        # A(80)が1.0なので、既定の分布では常に採用される
        for _ in range(20):
            r = run_script("length_check.py", "あ" * 80)
            assert r.returncode == 0
            assert "VERDICT\tACCEPT" in r.stdout
            assert "ACCEPTANCE\t1.0000" in r.stdout

    def test_acceptance_curve_matches_spec(self, run_script):
        # sigma=0.23、mu=ln(80)+sigma^2 の対数正規分布で A(L)=f(L)/f(80) となる
        sigma, mode = 0.23, 80.0
        mu = math.log(mode) + sigma**2

        def density(x):
            return math.exp(-((math.log(x) - mu) ** 2) / (2 * sigma**2)) / x

        for length in (50, 60, 100, 130):
            r = run_script("length_check.py", "あ" * length)
            got = float(
                next(
                    ln for ln in r.stdout.splitlines() if ln.startswith("ACCEPTANCE")
                ).split("\t")[1]
            )
            assert got == pytest.approx(
                density(length) / density(mode), abs=5e-5, rel=0
            )

    def test_target_shifts_the_mode(self, run_script):
        r = run_script("length_check.py", "--target", "100", "あ" * 100)
        assert r.returncode == 0
        assert "ACCEPTANCE\t1.0000" in r.stdout
        assert "MODE\tsoft" in r.stdout

    def test_soft_verdict_can_be_replayed_with_same_draw(self, run_script):
        first = run_script("length_check.py", "あ" * 50)
        draw = next(
            ln for ln in first.stdout.splitlines() if ln.startswith("DRAW")
        ).split("\t")[1]
        replay = run_script("length_check.py", "--draw", draw, "あ" * 50)
        first_verdict = next(
            ln for ln in first.stdout.splitlines() if ln.startswith("VERDICT")
        )
        replay_verdict = next(
            ln for ln in replay.stdout.splitlines() if ln.startswith("VERDICT")
        )
        assert replay.returncode == first.returncode
        assert replay_verdict == first_verdict
        assert f"DRAW\t{draw}" in replay.stdout

    def test_draw_must_be_in_unit_interval_and_soft_mode(self, run_script):
        assert (
            run_script("length_check.py", "--draw", "-0.1", "あ" * 50).returncode == 2
        )
        assert run_script("length_check.py", "--draw", "1", "あ" * 50).returncode == 2
        assert (
            run_script(
                "length_check.py", "--draw", "0.5", "--max", "60", "あ" * 50
            ).returncode
            == 2
        )

    def test_hard_max_violation_exits_1(self, run_script):
        r = run_script("length_check.py", "--max", "60", "あ" * 72)
        assert r.returncode == 1
        assert "MODE\thard" in r.stdout
        assert "VERDICT\tVIOLATION" in r.stdout

    def test_hard_max_satisfied_exits_0(self, run_script):
        r = run_script("length_check.py", "--max", "60", "あ" * 58)
        assert r.returncode == 0
        assert "VERDICT\tOK" in r.stdout

    def test_hard_constraint_never_draws_randomly(self, run_script):
        # ハード制約のときは確率的な抽選を挟まないので、境界ちょうどでも結果が揺れない
        for _ in range(20):
            r = run_script("length_check.py", "--max", "60", "あ" * 60)
            assert r.returncode == 0
            assert "ACCEPTANCE" not in r.stdout

    def test_hard_min_and_exact(self, run_script):
        assert run_script("length_check.py", "--min", "70", "あ" * 60).returncode == 1
        assert run_script("length_check.py", "--min", "70", "あ" * 70).returncode == 0
        assert run_script("length_check.py", "--exact", "42", "あ" * 41).returncode == 1
        assert run_script("length_check.py", "--exact", "42", "あ" * 42).returncode == 0

    def test_range_reports_both_bounds(self, run_script):
        r = run_script("length_check.py", "--min", "70", "--max", "90", "あ" * 100)
        assert r.returncode == 1
        assert "90" in r.stdout

    def test_inverted_range_exits_2(self, run_script):
        assert (
            run_script(
                "length_check.py", "--min", "90", "--max", "70", "あ" * 80
            ).returncode
            == 2
        )

    def test_stdin_input(self, run_script):
        r = run_script("length_check.py", stdin="問題：" + "あ" * 80)
        assert r.returncode == 0
        assert "LENGTH\t80" in r.stdout

    def test_file_input(self, run_script, tmp_path):
        p = tmp_path / "draft.txt"
        p.write_text("問題：" + "あ" * 80 + "\n", encoding="utf-8")
        r = run_script("length_check.py", "--file", p)
        assert r.returncode == 0
        assert "LENGTH\t80" in r.stdout

    def test_empty_text_exits_2(self, run_script):
        assert run_script("length_check.py", "問題：").returncode == 2

    def test_missing_file_exits_2(self, run_script, tmp_path):
        assert (
            run_script("length_check.py", "--file", tmp_path / "no-such.txt").returncode
            == 2
        )

    def test_non_positive_target_exits_2(self, run_script):
        assert run_script("length_check.py", "--target", "0", "あ" * 80).returncode == 2
