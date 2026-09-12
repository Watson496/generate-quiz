#!/usr/bin/env python3
"""問題文の文字数を計測し、許容度曲線で採否を確率的に判定する（references/quiz_generation_spec.md 14 の実装）。

計測規則:
    NFC正規化し、先頭の「問題：」「問題:」と改行を除いた本文を len() で数える。句読点・括弧・数字・英字・本文中の空白は通常の1文字として数える。

既定分布（ユーザー指定がない場合）:
    対数正規分布 sigma = 0.23, mu = ln(80) + sigma^2（最頻値80、標準偏差およそ20）
    A(L) = f(L) / f(80) を相対許容度とし、一様乱数 u <= A(L) なら採用。

ユーザー指定がある場合はハード／ソフトで扱いを変える:
    ハード（以内・以下・ちょうど・○〜○文字・厳守）: --max / --min / --exact
        → 確率抽選をせず、制約の充足だけで判定する。満たさなければ改稿する。
    ソフト（前後・程度・くらい・短め・長め）: --target
        → 目標値を最頻値に置いた同じ曲線で確率判定し、自然さを優先する。

終了コード:
    0  ACCEPT（ソフト）／制約充足（ハード）
    1  REJECT（ソフト）／制約違反（ハード）。改稿して再計測する
    2  入力の不備（本文が空、引数が不正、ファイルを読めないなど）

使用例:
    python3 length_check.py '……を何というでしょう？'
    python3 length_check.py --max 60 --file draft.txt
    python3 length_check.py --target 100 '……でしょう？'
    echo '問題：……' | python3 length_check.py
"""
import argparse
import math
import random
import sys
import unicodedata

SIGMA = 0.23
PREFIXES = ("問題：", "問題:")

EXIT_OK, EXIT_REVISE, EXIT_USAGE = 0, 1, 2


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(EXIT_USAGE)


def normalize(text):
    t = unicodedata.normalize("NFC", text).strip()
    for p in PREFIXES:
        if t.startswith(p):
            t = t[len(p):]
            break
    return t.replace("\r", "").replace("\n", "").strip()


def acceptance(length, mode):
    """最頻値 mode の対数正規分布での相対許容度 A(L)=f(L)/f(mode)。"""
    if length <= 0:
        return 0.0
    mu = math.log(mode) + SIGMA ** 2

    def density(x):
        return math.exp(-((math.log(x) - mu) ** 2) / (2 * SIGMA ** 2)) / x

    return density(length) / density(mode)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("text", nargs="?", help="問題文（省略時はstdin）")
    ap.add_argument("--file", metavar="PATH", help="問題文をファイルから読む")
    ap.add_argument("--target", type=float, default=80.0, help="ソフト目標＝分布の最頻値（既定80）")
    ap.add_argument("--max", type=int, dest="max_len", help="ハード上限（以内・以下）")
    ap.add_argument("--min", type=int, dest="min_len", help="ハード下限")
    ap.add_argument("--exact", type=int, help="ハード指定（ちょうど）")
    args = ap.parse_args()

    if args.target <= 0:
        fail("--target は正の値を指定してください")
    for name, value in (("--max", args.max_len), ("--min", args.min_len), ("--exact", args.exact)):
        if value is not None and value <= 0:
            fail(f"{name} は1以上を指定してください")
    if args.min_len is not None and args.max_len is not None and args.min_len > args.max_len:
        fail("--min が --max を超えています")

    if args.file:
        try:
            with open(args.file, encoding="utf-8") as f:
                raw = f.read()
        except (OSError, UnicodeDecodeError) as exc:
            fail(f"問題文ファイルを読めません: {args.file}: {exc}")
    elif args.text is not None:
        raw = args.text
    else:
        raw = sys.stdin.read()

    body = normalize(raw)
    if not body:
        fail("問題文が空です。")
    length = len(body)

    hard = any(v is not None for v in (args.max_len, args.min_len, args.exact))
    print(f"LENGTH\t{length}")

    if hard:
        print("MODE\thard")
        violations = []
        if args.exact is not None and length != args.exact:
            violations.append(f"ちょうど{args.exact}文字ではない")
        if args.max_len is not None and length > args.max_len:
            violations.append(f"上限{args.max_len}文字を超過（+{length - args.max_len}）")
        if args.min_len is not None and length < args.min_len:
            violations.append(f"下限{args.min_len}文字に不足（-{args.min_len - length}）")
        if violations:
            print("VERDICT\tVIOLATION\t" + " / ".join(violations))
            print("NOTE\t品質を保ったまま満たせない場合は、条件外の問題を黙って出さずその旨を伝える。")
            return EXIT_REVISE
        print("VERDICT\tOK")
        return EXIT_OK

    a = acceptance(length, args.target)
    print("MODE\tsoft")
    print(f"ACCEPTANCE\t{a:.4f}")
    if random.random() <= a:
        print("VERDICT\tACCEPT")
        return EXIT_OK
    print("VERDICT\tREJECT")
    print("NOTE\t同じ裏取り済み命題だけを使い、構文と情報のまとめ方を変えて自然に長さの異なる版へ改稿し再計測する。字数合わせの継ぎ足し・削除はしない。")
    return EXIT_REVISE


if __name__ == "__main__":
    sys.exit(main())
