#!/usr/bin/env python3
"""ファセットの兄弟ノードから、履歴補正付きの重み付き乱択で1件を選ぶ（references/selection_and_history_spec.md 第5節の実装）。

補正式:
    p_j = b_j / sum(b)                      基礎weightの正規化
    w_j = b_j * Π[d in D_j] min(1, d * p_j) 履歴補正（d は「何問前に選ばれたか」。直前が1）
    再正規化して1回だけ抽選する。

入力:
    ファセット選択の記録のJSON（work_state_spec.md）と、抽選する階層のID。記録が担当ごとの
    ファイルに分かれている場合は、すべてのファイルを渡す。同じキーの配列は渡した順につなぐ。
    指定した階層の`facet_weights`の最後の記録の候補を、`weight`を基礎weightとして抽選する。

抽選の前に、指定した階層について次を確認する。
    - `facet_levels`の最後の記録が子へ進む判断である
    - 粒度判断、weight、weightの分布の各検査の最後の結果が合格である
    - 区分に分けた階層では、区分の分け方の検査の最後の結果が合格である

出力（既定）: 選ばれた1件のみ。weight・確率・抽選過程は出力しない。
    --verbose を付けたときだけ補正後の内訳を stderr へ出す（調整用。ユーザーには表示しない）。

終了コード:
    0  1件を抽選した
    2  入力の不備、または抽選の前の確認を満たさない

使用例:
    python3 weighted_pick.py facet_granularity.json facet_weighting.json \\
        facet_granularity_review.json facet_weight_review.json \\
        facet_distribution_review.json --level L2
"""

import argparse
import json
import math
import random
import sys
from pathlib import Path

EXIT_OK, EXIT_USAGE = 0, 2
REVIEW_KEYS = {
    "facet_level_reviews": "粒度判断の検査",
    "facet_weight_reviews": "weightの検査",
    "facet_distribution_reviews": "weightの分布の検査",
}


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(EXIT_USAGE)


def load_state(paths):
    """記録のファイルを読み、同じキーの配列を渡した順につないだ一つの記録にする。"""
    state = {}
    for path in paths:
        try:
            part = json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"ファセット選択の記録を読めない: {path}: {exc}")
        if not isinstance(part, dict):
            fail(f"ファセット選択の記録はオブジェクトでなければならない: {path}")
        for key, value in part.items():
            if key not in state:
                state[key] = value
            elif isinstance(state[key], list) and isinstance(value, list):
                state[key] = state[key] + value
            elif state[key] != value:
                fail(f"{key}の値がファイルによって異なる: {path}")
    return state


def last_for_level(state, key, level, id_field="level_id"):
    records = state.get(key)
    if not isinstance(records, list):
        return None
    matched = [r for r in records if isinstance(r, dict) and r.get(id_field) == level]
    return matched[-1] if matched else None


def level_candidates(state, level):
    """抽選の前の確認を行い、指定した階層の候補を返す。"""
    decision = last_for_level(state, "facet_levels", level, "id")
    if decision is None or decision.get("decision") != "descend":
        fail(f"{level}は子へ進む判断として記録されていない")
    reviews = dict(REVIEW_KEYS)
    subdivisions = state.get("facet_subdivisions") or []
    if any(
        isinstance(item, dict) and item.get("parent") == decision.get("node")
        for item in subdivisions
    ):
        reviews["facet_subdivision_reviews"] = "区分の分け方の検査"
    for key, label in reviews.items():
        review = last_for_level(state, key, level)
        if review is None or review.get("status") != "passed":
            fail(f"{level}の{label}の最後の結果が合格でないため抽選しない")
    weights = last_for_level(state, "facet_weights", level)
    candidates = weights.get("candidates") if weights else None
    if not isinstance(candidates, list) or not candidates:
        fail(f"{level}のweightの候補がない")
    for c in candidates:
        if not isinstance(c, dict) or "key" not in c:
            fail("keyのない候補がある")
    return candidates


def weights_for(cands):
    base = []
    for c in cands:
        try:
            b = float(c.get("weight", 0.0))
        except TypeError, ValueError, OverflowError:
            fail(f"weightが数値ではない: {c.get('key')}")
        if not math.isfinite(b):
            fail(f"weightが有限の数値ではない: {c.get('key')}")
        if b < 0:
            fail(f"weightが負である: {c.get('key')} -> {b}")
        base.append(b)

    total = sum(base)
    if not math.isfinite(total):
        fail("weightの合計が有限の数値ではない")
    if total <= 0:
        fail("weightの合計が0である")

    probs = [b / total for b in base]

    adjusted = []
    for c, b, p in zip(cands, base, probs, strict=True):
        w = b
        for distance in c.get("history_distances") or []:
            try:
                d = float(distance)
            except TypeError, ValueError, OverflowError:
                fail(f"history_distancesが数値ではない: {c.get('key')}")
            if not math.isfinite(d):
                fail(f"history_distancesが有限の数値ではない: {c.get('key')}")
            if d <= 0:
                fail(
                    f"history_distancesが1未満である（直前は1）: {c.get('key')} -> {d}"
                )
            w *= min(1.0, d * p)
        adjusted.append(w)

    w_total = sum(adjusted)
    if w_total <= 0:
        # 全候補が履歴で潰れた場合は補正なしの基礎weightへ戻す
        adjusted, w_total = base, total

    return base, probs, adjusted, w_total


def choose(cands, *, verbose=False):
    """候補から1件を抽選し、選んだ候補だけを出力する。"""
    base, probs, adjusted, w_total = weights_for(cands)

    chosen = random.choices(cands, weights=adjusted, k=1)[0]

    if verbose:
        print("# 内部用: この内訳はユーザーへ表示しない", file=sys.stderr)
        for c, b, p, w in zip(cands, base, probs, adjusted, strict=True):
            print(
                f"# {c.get('key')}\tbase={b:.4f}\tp={p:.4f}\tadj={w:.4f}\t"
                f"final_p={w / w_total:.4f}",
                file=sys.stderr,
            )

    print(f"CHOSEN\t{chosen.get('key')}\t{chosen.get('label', '')}".rstrip())
    return chosen


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("state", nargs="+", help="ファセット選択の記録のJSON")
    ap.add_argument("--level", required=True, help="抽選する階層のID")
    ap.add_argument(
        "--verbose", action="store_true", help="補正後weightの内訳も出す（内部用）"
    )
    args = ap.parse_args()

    choose(level_candidates(load_state(args.state), args.level), verbose=args.verbose)
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
