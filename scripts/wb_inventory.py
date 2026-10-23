#!/usr/bin/env python3
"""Triagem de um inventário de URLs (CSV de wb_cdx.py) em Markdown.

Agrupa por URL, resume primeira/última observação e sinaliza caminhos e
extensões que merecem olhar humano. **Sinalizado não é exposto**: a maioria
dessas URLs responde 404/403 ou nunca teve o conteúdo sensível.

Exemplo:
    python scripts/wb_inventory.py out/inventario.csv > out/inventario.md
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from posixpath import splitext
from urllib.parse import urlparse

EXT_CATEGORIES = {
    "documentos": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".csv", ".txt"},
    "compactados": {".zip", ".rar", ".7z", ".tar", ".gz", ".tgz", ".bz2"},
    "backup/banco": {".bak", ".old", ".orig", ".sql", ".db", ".sqlite", ".dump", ".swp", ".backup"},
    "configuração": {".env", ".ini", ".conf", ".cfg", ".yml", ".yaml", ".xml", ".config", ".properties", ".json"},
    "código/servidor": {".php", ".asp", ".aspx", ".jsp", ".cgi", ".pl", ".py", ".rb"},
    "script/web": {".js", ".map"},
    "mídia": {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".mp4", ".mp3", ".ico"},
}
PATH_HINTS = re.compile(
    r"(/\.git/|/\.svn/|/\.env|wp-admin|wp-login|phpmyadmin|cpanel|/admin|/login|/backup|/upload|/staging|/dev/|/test/|/config|/api/|/private|/internal)",
    re.I,
)


def category(path: str) -> str:
    ext = splitext(path.lower())[1]
    for name, exts in EXT_CATEGORIES.items():
        if ext in exts:
            return name
    return "página/outros"


def group(rows: list[dict[str, str]]) -> dict[str, dict]:
    urls: dict[str, dict] = {}
    for r in rows:
        u = urls.setdefault(r["original"], {"n": 0, "first": r["timestamp"], "last": r["timestamp"], "status": Counter()})
        u["n"] += 1
        u["first"], u["last"] = min(u["first"], r["timestamp"]), max(u["last"], r["timestamp"])
        u["status"][r.get("statuscode", "-")] += 1
    return urls


def render(rows: list[dict[str, str]], top: int = 15) -> str:
    urls = group(rows)
    hosts, cats = Counter(), Counter()
    by_cat: dict[str, list[str]] = defaultdict(list)
    flagged = []
    for url, info in urls.items():
        parsed = urlparse(url if "//" in url else "//" + url)
        hosts[parsed.hostname or "?"] += 1
        c = category(parsed.path)
        cats[c] += 1
        by_cat[c].append(url)
        reasons = []
        if PATH_HINTS.search(parsed.path):
            reasons.append("caminho")
        if c in ("backup/banco", "configuração", "compactados"):
            reasons.append(c)
        if reasons:  # parâmetros sozinhos são ruído demais; só agravam outro motivo
            if parsed.query:
                reasons.append("parâmetros")
            flagged.append((url, info, ", ".join(reasons)))

    lines = [
        "# Triagem de inventário",
        "",
        f"- URLs distintas: **{len(urls)}** · Capturas: **{len(rows)}** · Hosts: **{len(hosts)}**",
        "",
        "> **Sinalizado ≠ exposto.** Use esta lista para priorizar leitura, não como achado.",
        "",
        "## Hosts",
        "",
        "| Host | URLs |",
        "|---|---|",
        *[f"| `{h}` | {n} |" for h, n in hosts.most_common(top)],
        "",
        "## Por tipo",
        "",
        "| Tipo | URLs |",
        "|---|---|",
        *[f"| {c} | {n} |" for c, n in cats.most_common()],
        "",
        f"## Sinalizadas para revisão ({len(flagged)})",
        "",
    ]
    if flagged:
        lines += ["| URL | Primeira | Última | Capturas | Status | Motivo |", "|---|---|---|---|---|---|"]
        for url, info, why in sorted(flagged, key=lambda x: x[1]["first"])[: top * 4]:
            st = ", ".join(f"{k}×{v}" for k, v in sorted(info["status"].items()))
            lines.append(f"| `{url}` | {info['first'][:8]} | {info['last'][:8]} | {info['n']} | {st} | {why} |")
    else:
        lines.append("Nada sinalizado.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("csv_path")
    p.add_argument("--top", type=int, default=15)
    args = p.parse_args(argv)
    with open(args.csv_path, newline="", encoding="utf-8") as fh:
        sys.stdout.write(render(list(csv.DictReader(fh)), args.top))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
