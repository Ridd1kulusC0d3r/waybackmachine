#!/usr/bin/env python3
"""Consulta a CDX API da Wayback Machine e grava o resultado com proveniência.

Somente biblioteca padrão. Cada saída ganha um arquivo `.meta.json` com a URL
exata consultada, o instante da coleta (UTC) e o SHA-256 do resultado.

Exemplo:
    python scripts/wb_cdx.py example.com/pagina --out out/pagina.csv
    python scripts/wb_cdx.py example.com --match domain --collapse timestamp:6
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

__version__ = "0.1.0"
DEFAULT_BASE = "https://web.archive.org/cdx/search/cdx"
DEFAULT_FIELDS = ["timestamp", "original", "statuscode", "mimetype", "digest"]
USER_AGENT = f"wayback-atlas/{__version__} (+https://github.com/Ridd1kulusC0d3r/waybackmachine)"


def build_params(args: argparse.Namespace, resume_key: str | None = None) -> list[tuple[str, str]]:
    params: list[tuple[str, str]] = [
        ("url", args.url),
        ("output", "json"),
        ("fl", ",".join(args.fields)),
        ("matchType", args.match),
    ]
    if args.date_from:
        params.append(("from", args.date_from))
    if args.date_to:
        params.append(("to", args.date_to))
    for flt in args.filter or []:
        params.append(("filter", flt))
    if args.collapse:
        params.append(("collapse", args.collapse))
    if args.limit:
        params.append(("limit", str(args.limit)))
    # showResumeKey faz o servidor devolver a chave de continuação ao fim da lista.
    params.append(("showResumeKey", "true"))
    if resume_key:
        params.append(("resumeKey", resume_key))
    return params


def parse_page(payload: list) -> tuple[list[list[str]], str | None]:
    """Separa as linhas de dados da resumeKey. Descarta o cabeçalho."""
    resume_key = None
    rows = [r for r in payload]
    # Formato: [header, *dados, [], [resumeKey]] quando há mais páginas.
    if len(rows) >= 2 and rows[-2] == [] and len(rows[-1]) == 1:
        resume_key = rows[-1][0]
        rows = rows[:-2]
    elif rows and rows[-1] == []:
        rows = rows[:-1]
    return rows[1:] if rows else [], resume_key


def fetch(url: str, retries: int = 4, timeout: int = 60) -> bytes:
    delay = 2.0
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == retries:
                raise
        except urllib.error.URLError:
            if attempt == retries:
                raise
        time.sleep(delay)
        delay *= 2
    raise RuntimeError("inalcançável")


def run(args: argparse.Namespace) -> tuple[list[list[str]], list[str]]:
    all_rows: list[list[str]] = []
    queries: list[str] = []
    resume_key = None
    while True:
        query = args.base_url + "?" + urllib.parse.urlencode(build_params(args, resume_key))
        queries.append(query)
        raw = fetch(query)
        payload = json.loads(raw) if raw.strip() else []
        rows, resume_key = parse_page(payload)
        all_rows.extend(rows)
        if args.limit and len(all_rows) >= args.limit:
            all_rows = all_rows[: args.limit]
            break
        if not resume_key:
            break
        time.sleep(args.delay)
    return all_rows, queries


def write_rows(rows: list[list[str]], fields: list[str], fmt: str, out: Path | None) -> bytes:
    if fmt == "csv":
        import io

        buf = io.StringIO()
        w = csv.writer(buf, lineterminator="\n")
        w.writerow(fields)
        w.writerows(rows)
        data = buf.getvalue().encode()
    elif fmt == "jsonl":
        data = "".join(json.dumps(dict(zip(fields, r)), ensure_ascii=False) + "\n" for r in rows).encode()
    else:
        data = json.dumps([dict(zip(fields, r)) for r in rows], ensure_ascii=False, indent=2).encode() + b"\n"
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
    else:
        sys.stdout.buffer.write(data)
    return data


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("url", help="URL, host ou domínio a consultar")
    p.add_argument("--match", default="exact", choices=["exact", "prefix", "host", "domain"])
    p.add_argument("--from", dest="date_from", help="início (AAAA[MMDDhhmmss])")
    p.add_argument("--to", dest="date_to", help="fim (AAAA[MMDDhhmmss])")
    p.add_argument("--filter", action="append", help="ex.: statuscode:200 ou !mimetype:text/html (repetível)")
    p.add_argument("--collapse", help="ex.: digest ou timestamp:8. Evite no primeiro passe de uma cronologia")
    p.add_argument("--fields", type=lambda s: s.split(","), default=DEFAULT_FIELDS)
    p.add_argument("--limit", type=int, default=0, help="máximo de linhas (0 = tudo)")
    p.add_argument("--format", choices=["csv", "json", "jsonl"], default="csv")
    p.add_argument("--out", type=Path, help="arquivo de saída (padrão: stdout, sem .meta.json)")
    p.add_argument("--delay", type=float, default=1.0, help="pausa entre páginas, em segundos")
    p.add_argument("--base-url", default=DEFAULT_BASE, help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    rows, queries = run(args)
    data = write_rows(rows, args.fields, args.format, args.out)

    if args.out:
        meta = {
            "tool": f"wb_cdx.py {__version__}",
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "queries": queries,
            "rows": len(rows),
            "fields": args.fields,
            "sha256": hashlib.sha256(data).hexdigest(),
            "note": "Índice de capturas; não prova data de publicação.",
        }
        meta_path = args.out.with_name(args.out.name + ".meta.json")
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
        print(f"{len(rows)} capturas -> {args.out} (+ {meta_path.name})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
