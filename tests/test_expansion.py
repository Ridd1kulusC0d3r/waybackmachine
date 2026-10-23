import csv
import json
import os
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wb_extract  # noqa: E402
import wb_fetch  # noqa: E402
import wb_inventory  # noqa: E402

HEADER = ["timestamp", "original", "statuscode", "mimetype", "digest"]
CDX = [
    HEADER,
    ["20190101000000", "http://alvo.test/", "200", "text/html", "D1"],
    ["20190601000000", "http://alvo.test/", "200", "text/html", "D1"],  # digest repetido
    ["20200101000000", "http://alvo.test/", "200", "text/html", "D2"],
    ["20200301000000", "http://alvo.test/backup.sql", "404", "text/html", "D3"],
]
HTML = {
    "20190101000000": b'<script>ga("create","UA-1234567-1")</script> contato: Ana@Alvo.test 8.8.8.8 10.0.0.5',
    "20200101000000": b'<a href="https://evil.example/x">t.me/canal_teste</a> G-ABCDE12345 0x' + b"a" * 40,
}


class Fake(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path.startswith("/cdx"):
            body = json.dumps(CDX).encode()
        else:
            ts = self.path.split("/web/")[1][:14]
            body = HTML.get(ts, b"x")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), Fake)
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()


class ExtractTests(unittest.TestCase):
    def test_extracts_pivots_and_filters_noise(self):
        found = wb_extract.extract(HTML["20190101000000"].decode())
        self.assertEqual(found["ga_universal"], {"UA-1234567-1"})
        self.assertEqual(found["ipv4"], {"8.8.8.8"})  # privado descartado
        self.assertIn("alvo.test", found["domain"])

    def test_defang(self):
        self.assertEqual(wb_extract.defang("url", "https://evil.example/x"), "hxxps://evil[.]example/x")
        self.assertEqual(wb_extract.defang("email", "a@b.com"), "a[@]b[.]com")

    def test_invalid_ip_rejected(self):
        self.assertEqual(wb_extract.extract("999.1.1.1 0.0.0.0 127.0.0.1").get("ipv4"), None)


class InventoryTests(unittest.TestCase):
    def test_flags_backup_but_warns(self):
        rows = [dict(zip(HEADER, r)) for r in CDX[1:]]
        md = wb_inventory.render(rows)
        self.assertIn("backup.sql", md)
        self.assertIn("Sinalizado ≠ exposto", md)
        self.assertEqual(wb_inventory.category("/x/dump.sql"), "backup/banco")


class FetchTests(unittest.TestCase):
    def test_select_rows_unique_digest_and_status(self):
        rows = [dict(zip(HEADER, r)) for r in CDX[1:]]
        sel = wb_fetch.select_rows(rows, {"200"}, "text/html", True, 0)
        self.assertEqual([r["digest"] for r in sel], ["D1", "D2"])


class PipelineTests(Base):
    def test_pipeline_end_to_end_and_verify(self):
        env = {**os.environ, "WB_CDX_BASE": self.base + "/cdx", "WB_WEB_BASE": self.base + "/web", "NO_PROXY": "127.0.0.1"}
        with tempfile.TemporaryDirectory() as d:
            sh = ROOT / "scripts" / "sh"
            r = subprocess.run(["bash", str(sh / "wb-pipeline.sh"), "alvo.test", "--fetch", "5", "--out", d],
                               env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(d) / "alvo.test"
            for name in ("cdx.csv", "cdx.csv.meta.json", "timeline.md", "inventory.md", "iocs.json", "RUN.log", "SHA256SUMS"):
                self.assertTrue((out / name).exists(), name)
            self.assertEqual(len(list((out / "raw").iterdir())), 2)  # D1 e D2; repetição não baixada
            iocs = json.loads((out / "iocs.json").read_text())
            self.assertIn("UA-1234567-1", iocs["summary"]["ga_universal"])
            self.assertIn("hxxps://evil[.]example/x", iocs["summary"]["url"])

            ok = subprocess.run(["bash", str(sh / "wb-verify.sh"), str(out)], capture_output=True, text=True)
            self.assertEqual(ok.returncode, 0, ok.stderr)
            victim = next((out / "raw").iterdir())
            victim.write_bytes(b"adulterado")
            bad = subprocess.run(["bash", str(sh / "wb-verify.sh"), str(out)], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 1)

    def test_shell_syntax(self):
        for f in (ROOT / "scripts" / "sh").glob("*.sh"):
            self.assertEqual(subprocess.run(["bash", "-n", str(f)]).returncode, 0, f.name)


if __name__ == "__main__":
    unittest.main()
