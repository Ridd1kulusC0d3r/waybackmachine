#!/usr/bin/env python3
"""Baixa capturas brutas (modificador `id_`) listadas num CSV de wb_cdx.py.

Para cada captura grava o arquivo, o SHA-256 e uma linha em `manifest.jsonl`
(com a URL *final* após redirecionamentos: a Wayback pode servir a captura
mais próxima, não a pedida). Também mantém `SHA256SUMS`, verificável com
`sha256sum -c`. É retomável: arquivos existentes são pulados.

Exemplo:
    python scripts/wb_fetch.py out/pagina.csv --out-dir out/raw --limit 20
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = "wayback-atlas/0.2.0 (+https://github.com/Ridd1kulusC0d3r/waybackmachine)"
DEFAULT_BASE = "https://web.archive.org/web"
RETRY_CODES = (429, 500, 502, 503, 504)


def snapshot_url(base: str, timestamp: str, original: str) -> str:
    return f"{base}/{timestamp}id_/{original}"


def file_name(timestamp: str, original: str) -> str:
    return f"{timestamp}_{hashlib.sha1(original.encode()).hexdigest()[:10]}.bin"


def select_rows(rows: list[dict], statuses: set[str], mime_prefix: str | None, unique_digest: bool, limit: int) -> list[dict]:
    """Filtra só para *baixar*; o índice completo continua no CSV original."""
    out, seen = [], set()
    for r in rows:
        if statuses and r.get("statuscode") not in statuses:
            continue
        if mime_prefix and not r.get("mimetype", "").startswith(mime_prefix):
            continue
        if unique_digest:
            key = (r.get("original"), r.get("digest"))
            if key in seen:
                continue
            seen.add(key)
        out.append(r)
        if limit and len(out) >= limit:
            break
    return out


def fetch(url: str, retries: int = 4, timeout: int = 60) -> tuple[bytes, str]:
    """Devolve (corpo, URL final)."""
    delay = 2.0
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read(), resp.geturl()
        except urllib.error.HTTPError as exc:
            if exc.code not in RETRY_CODES or attempt == retries:
                raise
        except urllib.error.URLError:
            if attempt == retries:
                raise
        time.sleep(delay)
        delay *= 2
    raise RuntimeError("inalcançável")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("csv_path")
    p.add_argument("--out-dir", type=Path, default=Path("out/raw"))
    p.add_argument("--status", action="append", default=None, help="statuscode aceito (repetível; padrão: 200)")
    p.add_argument("--mime-prefix", help="ex.: text/html")
    p.add_argument("--unique-digest", action="store_true", help="não baixa repetições do mesmo digest")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--delay", type=float, default=1.0)
    p.add_argument("--base-url", default=DEFAULT_BASE, help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    with open(args.csv_path, newline="", encoding="utf-8") as fh:
        rows = sorted(csv.DictReader(fh), key=lambda r: r["timestamp"])
    picked = select_rows(rows, set(args.status or ["200"]), args.mime_prefix, args.unique_digest, args.limit)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    manifest = args.out_dir.parent / "manifest.jsonl"
    sums = args.out_dir.parent / "SHA256SUMS"
    done = 0
    for r in picked:
        name = file_name(r["timestamp"], r["original"])
        dest = args.out_dir / name
        if dest.exists():
            continue
        url = snapshot_url(args.base_url, r["timestamp"], r["original"])
        entry = {"timestamp": r["timestamp"], "original": r["original"], "requested": url, "file": name}
        try:
            body, final = fetch(url)
        except (urllib.error.URLError, OSError) as exc:
            entry["error"] = str(exc)
        else:
            dest.write_bytes(body)
            digest = hashlib.sha256(body).hexdigest()
            entry.update(final_url=final, sha256=digest, bytes=len(body),
                         retrieved_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"))
            with sums.open("a") as fh:
                fh.write(f"{digest}  {args.out_dir.name}/{name}\n")
            done += 1
        with manifest.open("a") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        time.sleep(args.delay)
    print(f"{done} baixadas de {len(picked)} selecionadas -> {args.out_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
