#!/usr/bin/env python3
"""Gera docs/catalogo.md e a tabela do README a partir de data/tools.json.

Uso:
    python scripts/build_catalog.py          # reescreve os arquivos
    python scripts/build_catalog.py --check  # falha se estiverem desatualizados (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "tools.json"
README = ROOT / "README.md"
CATALOG = ROOT / "docs" / "catalogo.md"
BEGIN, END = "<!-- tools:begin -->", "<!-- tools:end -->"
GUIDE_BEGIN, GUIDE_END = "<!-- guides:begin -->", "<!-- guides:end -->"
EXTRA_BEGIN, EXTRA_END = "<!-- extra:begin -->", "<!-- extra:end -->"


def tools_table(data: dict, tier: str = "core") -> str:
    rows = ["| Repositório | Para que serve | Avaliação |", "|---|---|---|"]
    for t in (t for t in data["tools"] if t.get("tier", "core") == tier):
        rows.append(f"| [{t['name']}]({t['url']}) | {t['purpose']} | **{t['verdict']}** |")
    return "\n".join(rows)


def guides_table(data: dict) -> str:
    rows = ["| Ordem | Guia | O que aprender |", "|---|---|---|"]
    for g in data["guides"]:
        rows.append(f"| {g['order']} | [{g['title']}]({g['url']}) | {g['learn']} |")
    return "\n".join(rows)


def catalog_md(data: dict) -> str:
    out = [
        "# Catálogo de ferramentas",
        "",
        "> Gerado por `scripts/build_catalog.py` a partir de `data/tools.json`. Não edite à mão.",
        "",
        f"_{data['note']}_",
        "",
        "## Por papel na investigação",
        "",
    ]
    for key, label in data["roles"].items():
        members = [t for t in data["tools"] if key in t["roles"]]
        if not members:
            continue
        out += [f"### {label}", ""]
        out += [f"- [{t['name']}]({t['url']}) — {t['purpose']}" for t in members]
        out.append("")
    out += ["## Fichas", ""]
    for t in data["tools"]:
        out += [
            f"### {t['name']}",
            "",
            f"- **Tipo:** {t['kind']} · **Linguagem:** {t['lang']} · **Nível:** {t.get('tier', 'core')} · **Status:** {t['status']}",
            f"- **Link:** <{t['url']}>",
            f"- **Serve para:** {t['purpose']}",
            f"- **Avaliação:** {t['verdict']}",
            f"- **Cuidado:** {t['caveat']}",
        ]
        if t.get("docs"):
            out.append(f"- **Documentação:** <{t['docs']}>")
        out.append("")
    return "\n".join(out)


def splice(text: str, begin: str, end: str, body: str) -> str:
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise SystemExit(f"marcadores {begin} / {end} ausentes no README")
    return pattern.sub(lambda _m: f"{begin}\n{body}\n{end}", text)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--check", action="store_true")
    args = p.parse_args(argv)

    data = json.loads(DATA.read_text(encoding="utf-8"))
    readme = splice(README.read_text(encoding="utf-8"), BEGIN, END, tools_table(data, "core"))
    readme = splice(readme, EXTRA_BEGIN, EXTRA_END, tools_table(data, "complementar"))
    readme = splice(readme, GUIDE_BEGIN, GUIDE_END, guides_table(data))
    catalog = catalog_md(data)

    if args.check:
        stale = README.read_text(encoding="utf-8") != readme or not CATALOG.exists() or CATALOG.read_text(encoding="utf-8") != catalog
        if stale:
            print("README/catálogo desatualizados: rode `python scripts/build_catalog.py`", file=sys.stderr)
            return 1
        return 0
    README.write_text(readme, encoding="utf-8")
    CATALOG.write_text(catalog, encoding="utf-8")
    print(f"{len(data['tools'])} ferramentas, {len(data['guides'])} guias")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
