#!/usr/bin/env python3
"""履歴補正付きの重み付き乱択を行う（references/selection_and_history_spec.md 5.2 / 6 の実装）。

ファセットの sibling group 選択にも、具体的な解答候補の抽選にも同じ形式で使う。

補正式:
    p_j = b_j / sum(b)                      基礎weightの正規化
    w_j = b_j * Π[d in D_j] min(1, d * p_j) 履歴補正（d は「何問前に選ばれたか」。直前が1）
    再正規化して1回だけ抽選する。

入力（JSONをstdinまたは --json で渡す）:
    {"candidates": [
       {"key": "subject::7", "label": "芸術．レクリエーション．娯楽．スポーツ",
        "base_weight": 3.0, "history_distances": [1, 6]},
       {"key": "subject::8", "label": "言語．言語学．文学", "base_weight": 2.0}
    ]}

    base_weight は自分で推定した相対値（正の実数、丸めない）。weight 0 は不成立候補にだけ与える。history_distances 省略時は補正なし。

出力（既定）: 選ばれた1件のみ。weight・確率・抽選過程は出力しない。
    --verbose を付けたときだけ補正後の内訳を stderr へ出す（調整用。ユーザーには表示しない）。

終了コード:
    0  1件を抽選した
    2  入力の不備（JSON不正、候補が空、weight合計が0、履歴距離が0以下など）

使用例:
    echo '{"candidates":[...]}' | python3 weighted_pick.py
    python3 weighted_pick.py --json cand.json --exclude subject::7
"""
import argparse
import json
import random
import sys

EXIT_OK, EXIT_USAGE = 0, 2


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(EXIT_USAGE)


def load_input(path):
    if path:
        try:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        except OSError as exc:
            fail(f"候補JSONを読めません: {path}: {exc}")
    else:
        raw = sys.stdin.read()
    if not raw.strip():
        fail("候補JSONが空です。stdin か --json で渡してください。")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"候補JSONを解釈できません: {exc}")


def candidates_of(payload):
    if isinstance(payload, dict):
        cands = payload.get("candidates")
    else:
        cands = payload
    if not isinstance(cands, list):
        fail('入力は {"candidates": [...]} か候補の配列である必要があります。')
    for c in cands:
        if not isinstance(c, dict) or "key" not in c:
            fail("各候補は key を持つオブジェクトである必要があります。")
    return cands


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--json", metavar="PATH", help="候補JSONファイル（省略時はstdin）")
    ap.add_argument("--verbose", action="store_true", help="補正後weightの内訳も出す（内部用）")
    ap.add_argument(
        "--exclude", action="append", default=[],
        help="品質ゲートで落ちた候補のkeyを除いて再抽選する（複数指定可）",
    )
    args = ap.parse_args()

    cands = candidates_of(load_input(args.json))
    cands = [c for c in cands if c.get("key") not in args.exclude]
    if not cands:
        fail("候補が残っていません。ファセット領域か候補探索を見直してください。")

    base = []
    for c in cands:
        try:
            b = float(c.get("base_weight", 0.0))
        except (TypeError, ValueError):
            fail(f"base_weight が数値ではありません: {c.get('key')}")
        if b < 0:
            fail(f"base_weight は0以上です: {c.get('key')} -> {b}")
        base.append(b)

    total = sum(base)
    if total <= 0:
        fail("base_weight の合計が0です。成立する候補には正のweightを与えてください。")

    probs = [b / total for b in base]

    adjusted = []
    for c, b, p in zip(cands, base, probs):
        w = b
        for d in c.get("history_distances") or []:
            try:
                d = float(d)
            except (TypeError, ValueError):
                fail(f"history_distances が数値ではありません: {c.get('key')}")
            if d <= 0:
                fail(f"history_distances は1以上（直前=1）です: {c.get('key')} -> {d}")
            w *= min(1.0, d * p)
        adjusted.append(w)

    w_total = sum(adjusted)
    if w_total <= 0:
        # 全候補が履歴で潰れた場合は補正なしの基礎weightへ戻す
        adjusted, w_total = base, total

    chosen = random.choices(cands, weights=adjusted, k=1)[0]

    if args.verbose:
        print("# 内部用: この内訳はユーザーへ表示しない", file=sys.stderr)
        for c, b, p, w in zip(cands, base, probs, adjusted):
            print(
                f"# {c.get('key')}\tbase={b:.4f}\tp={p:.4f}\tadj={w:.4f}\t"
                f"final_p={w / w_total:.4f}",
                file=sys.stderr,
            )

    print(f"CHOSEN\t{chosen.get('key')}\t{chosen.get('label', '')}".rstrip())
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
