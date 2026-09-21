"""length_check.pyの計算とCLI動作を検査する。"""

import math
import unicodedata

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st


@pytest.fixture
def length_module(load_script):
    return load_script("generate-quiz", "length_check.py")


class TestLengthCheckFunctions:
    # 正規化と許容度の計算は各生成例の間で状態を変えない。
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(st.text())
    def test_normalize_returns_nfc_without_line_breaks(self, length_module, text):
        """任意の入力が改行を含まないNFCの文字列へ正規化されることを確認する。"""
        normalized = length_module.normalize(text)
        assert unicodedata.is_normalized("NFC", normalized)
        assert "\r" not in normalized
        assert "\n" not in normalized
        assert normalized == normalized.strip()

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
        """問題行の接頭辞と改行を除き、文字間の空白は保つことを確認する。"""
        assert length_module.normalize(text) == expected

    def test_acceptance_at_mode_and_invalid_length(self, length_module):
        """最頻値の採用確率は1で、正でない文字数の採用確率は0となることを確認する。"""
        assert length_module.acceptance(80, 80) == pytest.approx(1)
        assert length_module.acceptance(0, 80) == 0
        assert length_module.acceptance(-1, 80) == 0

    def test_acceptance_uses_requested_mode(self, length_module):
        """指定した目標文字数が採用確率の最頻値になることを確認する。"""
        assert length_module.acceptance(100, 100) == pytest.approx(1)
        assert length_module.acceptance(80, 100) < 1

    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        length=st.integers(min_value=1, max_value=300),
        mode=st.integers(min_value=20, max_value=200),
    )
    def test_acceptance_is_bounded(self, length_module, length, mode):
        """正の文字数に対する採用確率が0から1に収まることを確認する。"""
        value = length_module.acceptance(length, mode)
        assert 0 <= value <= 1 + 1e-12
        assert length_module.acceptance(mode, mode) == pytest.approx(1)


class TestLengthCheck:
    """文字数の計測と採否の判定。満たしていないハード制約を通さないことを主に見る。"""

    def test_prefix_and_newlines_are_excluded(self, run_script):
        """問題行の接頭辞と末尾改行を文字数に含めないことを確認する。"""
        r = run_script("length_check.py", "問題：" + "あ" * 80 + "\n")
        assert "LENGTH\t80" in r.stdout

    def test_ascii_colon_prefix_is_also_excluded(self, run_script):
        """半角コロンの問題行接頭辞も文字数に含めないことを確認する。"""
        assert "LENGTH\t80" in run_script("length_check.py", "問題:" + "あ" * 80).stdout

    def test_nfc_normalization_before_counting(self, run_script):
        """分解された濁点を合成してから文字数を数えることを確認する。"""
        # 濁点を合成する場合、NFDの2コードポイントを1文字として数える
        r = run_script("length_check.py", "が" * 10)
        assert "LENGTH\t10" in r.stdout

    def test_mode_length_always_accepted(self, run_script):
        """最頻値に一致する問題文が抽選値によらず採用されることを確認する。"""
        # A(80)が1.0なので、既定の分布では常に採用される
        for _ in range(20):
            r = run_script("length_check.py", "あ" * 80)
            assert r.returncode == 0
            assert "VERDICT\tACCEPT" in r.stdout
            assert "ACCEPTANCE\t1.0000" in r.stdout

    def test_acceptance_curve_matches_spec(self, run_script):
        """複数の文字数で採用確率が指定された対数正規曲線に一致することを確認する。"""
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
        """目標文字数を変更すると採用確率の最頻値も移ることを確認する。"""
        r = run_script("length_check.py", "--target", "100", "あ" * 100)
        assert r.returncode == 0
        assert "ACCEPTANCE\t1.0000" in r.stdout
        assert "MODE\tsoft" in r.stdout

    def test_soft_verdict_can_be_replayed_with_same_draw(self, run_script):
        """抽選値を再指定すると同じ問題文の採否を再現できることを確認する。"""
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
        """範囲外の抽選値とハード制約での抽選値指定を拒否することを確認する。"""
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
        """上限超過をハード制約違反として報告することを確認する。"""
        r = run_script("length_check.py", "--max", "60", "あ" * 72)
        assert r.returncode == 1
        assert "MODE\thard" in r.stdout
        assert "VERDICT\tVIOLATION" in r.stdout

    def test_hard_max_satisfied_exits_0(self, run_script):
        """上限以内の問題文がハード制約を満たすことを確認する。"""
        r = run_script("length_check.py", "--max", "60", "あ" * 58)
        assert r.returncode == 0
        assert "VERDICT\tOK" in r.stdout

    def test_hard_constraint_never_draws_randomly(self, run_script):
        """ハード制約の境界値では確率的な抽選を行わないことを確認する。"""
        # ハード制約のときは確率的な抽選を挟まないので、境界ちょうどでも結果が揺れない
        for _ in range(20):
            r = run_script("length_check.py", "--max", "60", "あ" * 60)
            assert r.returncode == 0
            assert "ACCEPTANCE" not in r.stdout

    def test_hard_min_and_exact(self, run_script):
        """下限と指定文字数について境界の内外で採否が切り替わることを確認する。"""
        assert run_script("length_check.py", "--min", "70", "あ" * 60).returncode == 1
        assert run_script("length_check.py", "--min", "70", "あ" * 70).returncode == 0
        assert run_script("length_check.py", "--exact", "42", "あ" * 41).returncode == 1
        assert run_script("length_check.py", "--exact", "42", "あ" * 42).returncode == 0

    def test_range_reports_both_bounds(self, run_script):
        """範囲外の文字数を拒否し、指定した上限を結果に示すことを確認する。"""
        r = run_script("length_check.py", "--min", "70", "--max", "90", "あ" * 100)
        assert r.returncode == 1
        assert "90" in r.stdout

    def test_inverted_range_exits_2(self, run_script):
        """下限が上限を超える指定を入力エラーとして扱うことを確認する。"""
        assert (
            run_script(
                "length_check.py", "--min", "90", "--max", "70", "あ" * 80
            ).returncode
            == 2
        )

    def test_stdin_input(self, run_script):
        """標準入力から受け取った問題文の文字数を測れることを確認する。"""
        r = run_script("length_check.py", stdin="問題：" + "あ" * 80)
        assert r.returncode == 0
        assert "LENGTH\t80" in r.stdout

    def test_file_input(self, run_script, tmp_path):
        """指定ファイルから受け取った問題文の文字数を測れることを確認する。"""
        p = tmp_path / "draft.txt"
        p.write_text("問題：" + "あ" * 80 + "\n", encoding="utf-8")
        r = run_script("length_check.py", "--file", p)
        assert r.returncode == 0
        assert "LENGTH\t80" in r.stdout

    def test_empty_text_exits_2(self, run_script):
        """接頭辞を除くと空になる問題文を入力エラーとして扱うことを確認する。"""
        assert run_script("length_check.py", "問題：").returncode == 2

    def test_missing_file_exits_2(self, run_script, tmp_path):
        """存在しない入力ファイルを入力エラーとして扱うことを確認する。"""
        assert (
            run_script("length_check.py", "--file", tmp_path / "no-such.txt").returncode
            == 2
        )

    def test_non_positive_target_exits_2(self, run_script):
        """正でない目標文字数を入力エラーとして扱うことを確認する。"""
        assert run_script("length_check.py", "--target", "0", "あ" * 80).returncode == 2
