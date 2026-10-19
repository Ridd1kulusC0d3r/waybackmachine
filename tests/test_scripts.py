import json
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_catalog  # noqa: E402
import wb_cdx  # noqa: E402
import wb_diff  # noqa: E402
import wb_timeline  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "sample_cdx.csv"

HEADER = ["timestamp", "original", "statuscode", "mimetype", "digest"]
PAGE1 = [HEADER, ["20190101000000", "http://e.com/", "200", "text/html", "D1"], [], ["KEY2"]]
PAGE2 = [HEADER, ["20200101000000", "http://e.com/", "200", "text/html", "D2"]]


class FakeWayback(BaseHTTPRequestHandler):
    hits = 0

    def log_message(self, *a):
        pass

    def do_GET(self):
        FakeWayback.hits += 1
        if self.path.startswith("/cdx"):
            if FakeWayback.hits == 1:  # primeira tentativa: 429 para exercitar o retry
                self.send_response(429)
                self.end_headers()
                return
            body = PAGE2 if "resumeKey=KEY2" in self.path else PAGE1
        elif "/20200101000000id_/" in self.path:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"linha1\nlinha2\n")
            return
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"linha1\nlinha2 alterada\n")
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())


class ServerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), FakeWayback)
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()


class CdxTests(ServerCase):
    def test_parse_page_extracts_resume_key(self):
        rows, key = wb_cdx.parse_page(PAGE1)
        self.assertEqual(key, "KEY2")
        self.assertEqual(len(rows), 1)
        rows, key = wb_cdx.parse_page(PAGE2)
        self.assertIsNone(key)

    def test_end_to_end_pagination_retry_and_meta(self):
        FakeWayback.hits = 0
        wb_cdx.time.sleep = lambda _s: None  # sem esperas nos testes
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "r.csv"
            rc = wb_cdx.main(["e.com", "--out", str(out), "--base-url", self.base + "/cdx", "--delay", "0"])
            self.assertEqual(rc, 0)
            lines = out.read_text().splitlines()
            self.assertEqual(lines[0], ",".join(HEADER))
            self.assertEqual(len(lines), 3)  # cabeçalho + 2 páginas
            meta = json.loads((Path(d) / "r.csv.meta.json").read_text())
            self.assertEqual(meta["rows"], 2)
            self.assertEqual(len(meta["queries"]), 2)
            self.assertEqual(len(meta["sha256"]), 64)


class DiffTests(ServerCase):
    def test_diff_detects_change(self):
        a = wb_diff.fetch(wb_diff.snapshot_url(self.base + "/web", "20200101000000", "http://e.com/"))
        b = wb_diff.fetch(wb_diff.snapshot_url(self.base + "/web", "20210101000000", "http://e.com/"))
        lines = wb_diff.diff_text(a, b, "A", "B")
        self.assertTrue(any(l.startswith("+linha2 alterada") for l in lines))


class TimelineTests(unittest.TestCase):
    def test_change_points(self):
        rows = wb_timeline.load(str(FIXTURE))
        reasons = [c["reason"] for c in wb_timeline.change_points(rows)]
        self.assertEqual(len(reasons), 3)  # AAAA→BBBB, BBBB→CCCC(+404), CCCC→BBBB(+200)
        self.assertIn("status 200→404", reasons[1])

    def test_render_mentions_caveat_and_dates(self):
        md = wb_timeline.render(wb_timeline.load(str(FIXTURE)))
        self.assertIn("2019-03-14 12:00:00", md)
        self.assertIn("não a data de publicação", md)


class CatalogTests(unittest.TestCase):
    def test_data_is_valid_and_ids_unique(self):
        data = json.loads(build_catalog.DATA.read_text(encoding="utf-8"))
        ids = [t["id"] for t in data["tools"]]
        self.assertEqual(len(ids), len(set(ids)))
        for t in data["tools"]:
            for role in t["roles"]:
                self.assertIn(role, data["roles"])

    def test_generated_files_up_to_date(self):
        self.assertEqual(subprocess.run([sys.executable, str(ROOT / "scripts" / "build_catalog.py"), "--check"]).returncode, 0)


if __name__ == "__main__":
    unittest.main()
