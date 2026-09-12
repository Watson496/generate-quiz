#!/usr/bin/env python3
"""ファセットカタログから FACET_NODE / FACET_ROOT ブロックを1件だけ取り出す。

カタログは1ファイル最大約260KBあるため、全文を読み込まずにこのスクリプトで必要な親ブロックだけを取得する。分類内容・コード・階層は加工しない。

使い方:
    facet_node.py 'subject::7'             # ブロック全文（DIRECT_CHILDREN込み）
    facet_node.py 'subject::ROOT'          # 索引側の FACET_ROOT ブロック
    facet_node.py --grep '音楽'             # ラベル部分一致で NODE_KEY を探す
    facet_node.py --children 'subject::7'  # DIRECT_CHILDREN 行のみ

終了コード:
    0  ブロック（または --grep の該当）を出力した
    1  該当なし（カタログにないノードを推測して作らないこと）
    2  引数・カタログの不備（references が読めない、キー未指定など）
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

REF_DIR = Path(__file__).resolve().parent.parent / "references"

BLOCK_RE_TMPL = r"^## FACET_(?:NODE|ROOT) `{key}`$"
END_RE = re.compile(r"^<!-- END_FACET_(?:NODE|ROOT) -->$")
CHILD_RE = re.compile(r"^- `([^`]+)` \| CODE `([^`]*)` \| (.+)$")

EXIT_OK, EXIT_NOT_FOUND, EXIT_USAGE = 0, 1, 2


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(EXIT_USAGE)


def ref_files():
    if not REF_DIR.is_dir():
        fail(f"references ディレクトリが見つかりません: {REF_DIR}")
    files = sorted(REF_DIR.glob("facet_*.md"))
    if not files:
        fail(f"ファセットカタログが1件もありません: {REF_DIR}")
    # 索引を先に見る（FACET_ROOT は索引側にある）
    files.sort(key=lambda p: (p.name != "facet_index.md", p.name))
    return files


def read_lines(path):
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        fail(f"カタログを読めません: {path.name}: {exc}")


def find_block(key):
    header = re.compile(BLOCK_RE_TMPL.format(key=re.escape(key)))
    for path in ref_files():
        lines = read_lines(path)
        for i, line in enumerate(lines):
            if header.match(line):
                out = [line]
                for line2 in lines[i + 1:]:
                    out.append(line2)
                    if END_RE.match(line2):
                        return path, out
                return path, out
    return None, None


def grep_labels(needle, limit):
    needle = unicodedata.normalize("NFC", needle)
    seen = set()
    hits = []
    for path in ref_files():
        for line in read_lines(path):
            m = CHILD_RE.match(line)
            if not m:
                continue
            key, code, label = m.groups()
            if needle in unicodedata.normalize("NFC", label) and key not in seen:
                seen.add(key)
                hits.append((key, code, label, path.name))
                if len(hits) >= limit:
                    return hits
    return hits


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "key", nargs="?", help='NODE_KEY（例: subject::7, place::(1/9), time::"0/2"）'
    )
    ap.add_argument("--grep", metavar="TEXT", help="ラベル部分一致で NODE_KEY を検索する")
    ap.add_argument("--children", action="store_true", help="DIRECT_CHILDREN の行だけを出す")
    ap.add_argument("--limit", type=int, default=40, help="--grep の最大件数（既定40）")
    args = ap.parse_args()

    if args.grep is not None:
        if not args.grep.strip():
            fail("--grep に空文字は指定できません")
        if args.limit < 1:
            fail("--limit は1以上を指定してください")
        hits = grep_labels(args.grep, args.limit)
        if not hits:
            print(f"該当なし: {args.grep}", file=sys.stderr)
            return EXIT_NOT_FOUND
        for key, code, label, fname in hits:
            print(f"`{key}` | CODE `{code}` | {label}  ({fname})")
        return EXIT_OK

    if not args.key:
        fail("NODE_KEY か --grep のどちらかが必要です")

    path, block = find_block(args.key)
    if block is None:
        print(f"NODE_KEY が見つかりません: {args.key}", file=sys.stderr)
        print("カタログにないノードを推測して作らないこと。--grep でラベル検索するか、親ブロックの DIRECT_CHILDREN を確認する。", file=sys.stderr)
        return EXIT_NOT_FOUND

    if args.children:
        started = False
        for line in block:
            if line.startswith("### DIRECT_CHILDREN"):
                started = True
                continue
            if started and (CHILD_RE.match(line) or line.strip() == "なし"):
                print(line)
        return EXIT_OK

    print(f"# source: references/{path.name}")
    print("\n".join(block))
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
