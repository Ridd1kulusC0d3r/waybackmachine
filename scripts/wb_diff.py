#!/usr/bin/env python3
"""Compara duas capturas da mesma URL (conteúdo bruto, sem reescrita de links).

Usa o modificador `id_` da Wayback, que devolve o conteúdo como foi capturado,
sem o banner e sem links reescritos. Imprime SHA-256 de cada lado e um diff
unificado. Somente biblioteca padrão.

Exemplo:
    python scripts/wb_diff.py https://example.com/ 20200101000000 20220101000000
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import sys
import urllib.request

USER_AGENT = "wayback-atlas/0.1.0 (+https://github.com/Ridd1kulusC0d3r/waybackmachine)"
DEFAULT_BASE = "https://web.archive.org/web"


def snapshot_url(base: str, timestamp: str, url: str) -> str:
    return f"{base}/{timestamp}id_/{url}"


def fetch(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def diff_text(a: bytes, b: bytes, label_a: str, label_b: str) -> list[str]:
    ta = a.decode("utf-8", errors="replace").splitlines()
    tb = b.decode("utf-8", errors="replace").splitlines()
    return list(difflib.unified_diff(ta, tb, fromfile=label_a, tofile=label_b, lineterm=""))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("url")
    p.add_argument("ts_a", help="timestamp da captura A (AAAAMMDDhhmmss)")
    p.add_argument("ts_b", help="timestamp da captura B")
    p.add_argument("--base-url", default=DEFAULT_BASE, help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    ua, ub = (snapshot_url(args.base_url, ts, args.url) for ts in (args.ts_a, args.ts_b))
    a, b = fetch(ua), fetch(ub)
    print(f"# A {args.ts_a} sha256={hashlib.sha256(a).hexdigest()} {ua}")
    print(f"# B {args.ts_b} sha256={hashlib.sha256(b).hexdigest()} {ub}")
    if a == b:
        print("# Conteúdo idêntico.")
        return 0
    for line in diff_text(a, b, f"A@{args.ts_a}", f"B@{args.ts_b}"):
        print(line)
    return 1  # convenção de diff: 1 = há diferenças


if __name__ == "__main__":
    sys.exit(main())
