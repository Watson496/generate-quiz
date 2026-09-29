#!/usr/bin/env python3
"""開いた資料のページの写しを、依頼全体で共有する置き場に保存し、URLで取り出す。

置き場には、URL、取得した日時、ページの本文だけを置く。判断や評価は置かない。
写しはURLを指定して取り出すことだけができ、置き場の一覧は出さない。

使い方:
    source_cache.py DIR fetch URL   # 保存済みなら写しを、なければ取得して保存し、本文を出す
    source_cache.py DIR get URL     # 保存済みの写しを出す
    source_cache.py DIR put URL     # 標準入力の本文を写しとして保存する（fetchで取得できない場合）

終了コード:
    0  写しを出した、または保存した
    1  保存されていない、または取得できない（HTMLと文字以外の形式を含む）
    2  引数の不備、または空の本文
"""

import argparse
import datetime
import hashlib
import html.parser
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

EXIT_OK, EXIT_MISSING, EXIT_USAGE = 0, 1, 2
USER_AGENT = "Mozilla/5.0 (generate-quiz source_cache)"
SKIPPED_TAGS = {"script", "style", "noscript", "template"}


class TextExtractor(html.parser.HTMLParser):
    """HTMLから、表示される文字だけを取り出す。"""

    def __init__(self):
        super().__init__()
        self.parts = []
        self.title = []
        self.skipping = 0
        self.in_title = False

    def handle_starttag(self, tag, _attrs):
        if tag in SKIPPED_TAGS:
            self.skipping += 1
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag in SKIPPED_TAGS and self.skipping:
            self.skipping -= 1
        elif tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        elif not self.skipping:
            self.parts.append(data)


def cache_path(directory, url):
    return Path(directory) / f"{hashlib.sha256(url.encode('utf-8')).hexdigest()}.json"


def load(directory, url):
    path = cache_path(directory, url)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save(directory, url, title, text, method):
    Path(directory).mkdir(parents=True, exist_ok=True)
    record = {
        "url": url,
        "fetched_at": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"),
        "method": method,
        "title": title,
        "text": text,
    }
    cache_path(directory, url).write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return record


def decode(body, content_type):
    match = re.search(r"charset=([\w-]+)", content_type, re.IGNORECASE)
    if match is None:
        match = re.search(
            rb"<meta[^>]+charset=[\"']?([\w-]+)", body[:4096], re.IGNORECASE
        )
        charset = match.group(1).decode("ascii") if match else "utf-8"
    else:
        charset = match.group(1)
    try:
        return body.decode(charset, errors="replace")
    except LookupError:
        return body.decode("utf-8", errors="replace")


def normalize(text):
    """行ごとに前後の空白を除き、空行が続く箇所を一つにまとめる。"""
    lines = [line.strip() for line in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def fetch(url):
    """ページを取得し、題名と本文を返す。HTMLと文字以外の形式は取得しない。"""
    if urllib.parse.urlsplit(url).scheme not in {"http", "https"}:
        message = f"httpまたはhttpsのURLではない: {url}"
        raise ValueError(message)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})  # noqa: S310
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
        content_type = response.headers.get("Content-Type", "")
        body = response.read()
    if "html" in content_type:
        parser = TextExtractor()
        parser.feed(decode(body, content_type))
        text = normalize("".join(parser.parts))
        return "".join(parser.title).strip(), text
    if content_type.startswith("text/"):
        return "", decode(body, content_type).strip()
    message = f"この形式は取得できない: {content_type or '不明'}"
    raise ValueError(message)


def show(record):
    print(f"URL: {record['url']}")
    print(f"取得日時: {record['fetched_at']}")
    if record["title"]:
        print(f"題名: {record['title']}")
    print()
    print(record["text"])


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("directory", help="資料の写しの置き場")
    parser.add_argument("command", choices=("fetch", "get", "put"))
    parser.add_argument("url")
    args = parser.parse_args()

    record = load(args.directory, args.url)
    if record is None and args.command == "get":
        print(f"保存されていない: {args.url}", file=sys.stderr)
        return EXIT_MISSING
    if record is None and args.command == "put":
        text = normalize(sys.stdin.read())
        if not text:
            print("入力エラー: 本文が空である", file=sys.stderr)
            return EXIT_USAGE
        record = save(args.directory, args.url, "", text, "put")
    if record is None:
        try:
            title, text = fetch(args.url)
        except (OSError, ValueError, urllib.error.URLError) as error:
            print(f"取得できない: {error}", file=sys.stderr)
            return EXIT_MISSING
        record = save(args.directory, args.url, title, text, "fetch")
    show(record)
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
