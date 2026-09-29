"""資料の写しの置き場を扱うスクリプトの動作を確認する。"""

import http.server
import threading

import pytest

PAGE = """<html><head><meta charset="utf-8"><title>ペロニスモ</title>
<script>var x = 1;</script></head>
<body><h1>ペロニスモ</h1>

<p>アルゼンチンの民衆を基盤とする政治運動。</p></body></html>"""


@pytest.fixture
def server():
    """HTMLと、取得できない形式を返し、要求の回数を数えるサーバーを立てる。"""
    requests = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            requests.append(self.path)
            if self.path == "/page":
                body, content_type = PAGE.encode("utf-8"), "text/html; charset=utf-8"
            else:
                body, content_type = b"%PDF-1.4", "application/pdf"
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_args):
            pass

    httpd = http.server.HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{httpd.server_port}", requests
    httpd.shutdown()


class TestSourceCache:
    """写しの取得、保存、取り出しを確認する。"""

    def test_fetch_saves_text_and_reuses_it(self, run_script, tmp_path, server):
        """取得したページの本文を保存し、2回目は通信せずに写しを返す。"""
        base, requests = server
        first = run_script("source_cache.py", tmp_path, "fetch", f"{base}/page")
        assert first.returncode == 0
        assert "題名: ペロニスモ" in first.stdout
        assert "アルゼンチンの民衆を基盤とする政治運動。" in first.stdout
        assert "var x" not in first.stdout
        second = run_script("source_cache.py", tmp_path, "get", f"{base}/page")
        assert second.stdout == first.stdout
        run_script("source_cache.py", tmp_path, "fetch", f"{base}/page")
        assert requests == ["/page"]

    def test_fetch_rejects_other_format(self, run_script, tmp_path, server):
        """HTMLと文字以外の形式は取得せず、保存もしない。"""
        base, _ = server
        result = run_script("source_cache.py", tmp_path, "fetch", f"{base}/paper")
        assert result.returncode == 1
        assert "この形式は取得できない" in result.stderr
        assert (
            run_script("source_cache.py", tmp_path, "get", f"{base}/paper").returncode
            == 1
        )

    def test_put_saves_text_once(self, run_script, tmp_path):
        """取得できないページは渡した本文を保存し、保存済みの写しは上書きしない。"""
        url = "https://example.org/paper.pdf"
        saved = run_script(
            "source_cache.py", tmp_path, "put", url, stdin="論文の本文\n"
        )
        assert saved.returncode == 0
        again = run_script("source_cache.py", tmp_path, "put", url, stdin="別の本文")
        assert "論文の本文" in again.stdout
        assert "別の本文" not in again.stdout

    def test_put_rejects_empty_text(self, run_script, tmp_path):
        """空の本文は保存しない。"""
        result = run_script(
            "source_cache.py", tmp_path, "put", "https://example.org/a", stdin=" \n"
        )
        assert result.returncode == 2

    def test_get_reports_missing_copy(self, run_script, tmp_path):
        """保存されていないURLは取り出せない。"""
        result = run_script("source_cache.py", tmp_path, "get", "https://example.org/b")
        assert result.returncode == 1
        assert "保存されていない" in result.stderr
