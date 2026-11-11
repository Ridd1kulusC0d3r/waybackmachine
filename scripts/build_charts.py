#!/usr/bin/env python3
"""Gera os gráficos SVG do repositório a partir de data/tools.json.

Mesma linguagem visual do LLmInjection: cartão de papel, título em serifa, rótulos em mono,
uma só cor em escala e quadrados tracejados para "vazio". Só biblioteca padrão.

Uso:
    python scripts/build_charts.py          # reescreve assets/tool-map.svg
    python scripts/build_charts.py --check  # falha se estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "tools.json"
OUT = ROOT / "assets" / "tool-map.svg"

PAPER, INK, INK2, INK3, RULE, SIGNAL = "#f3f0e8", "#17150f", "#4a463c", "#7b766a", "#cfc9ba", "#b43c0e"
PRIMARY, SECONDARY = "#b43c0e", "#e9b394"  # um só matiz: escuro = papel principal, claro = secundário
SERIF = "Georgia,serif"
MONO = "'Courier New',monospace"
SANS = "system-ui,Helvetica,Arial,sans-serif"

# Rótulos curtos das colunas (cabem em ~100 px em mono caixa-alta com espaçamento).
ROLE_LABELS = {"discover": "DESCOBRIR", "recover": "RECUPERAR", "analyze": "ANALISAR", "preserve": "PRESERVAR", "reference": "REFERÊNCIA"}
ROW_H, LEFT, COL0, COL_W, NAME_X = 32, 40, 490, 100, 140


def ordered_tools(data: dict) -> list[dict]:
    """Principais primeiro, depois complementares; dentro de cada nível, a ordem do JSON."""
    return [t for tier in ("core", "complementar") for t in data["tools"] if t.get("tier", "core") == tier]


def render(data: dict) -> str:
    tools = ordered_tools(data)
    roles = list(data["roles"])
    n = len(tools)
    status_x = COL0 + len(roles) * COL_W + 30
    width = status_x + 150 + 40
    head_y = 100
    first_y = 106
    height = first_y + n * ROW_H + 120
    unchecked = sum(t["status"] != "documentado" for t in tools)

    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="t">',
        '<title id="t">Mapa de ferramentas: papel de cada projeto na investigação e status da curadoria</title>',
        f'<rect width="{width}" height="{height}" fill="{PAPER}"/>',
        f'<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" fill="none" stroke="{INK}"/>',
        f'<text x="{LEFT}" y="44" font-family="{SERIF}" font-size="22" font-weight="700" fill="{INK}">Mapa de ferramentas</text>',
        f'<text x="{LEFT}" y="64" font-family="{MONO}" font-size="11" fill="{INK3}">Papel de cada projeto na investigação e o que a curadoria realmente verificou.</text>',
        f'<text x="{width - 40}" y="44" text-anchor="end" font-family="{MONO}" font-size="22" font-weight="700" fill="{INK}">{n}<tspan font-size="12" fill="{INK3}"> projetos</tspan></text>',
    ]
    if unchecked:
        o.append(f'<text x="{width - 40}" y="64" text-anchor="end" font-family="{MONO}" font-size="11" font-weight="700" fill="{SIGNAL}">{unchecked} sem checagem da documentação</text>')
    else:
        o.append(f'<text x="{width - 40}" y="64" text-anchor="end" font-family="{MONO}" font-size="11" fill="{INK2}">Documentação lida para todos</text>')

    # cabeçalhos de grupo e de coluna
    gx1, gx2 = COL0 + 6, COL0 + len(roles) * COL_W - 6
    o.append(f'<text x="{(gx1 + gx2) / 2}" y="78" text-anchor="middle" font-family="{MONO}" font-size="9" font-weight="700" letter-spacing="2" fill="{INK3}">PAPEL NA INVESTIGAÇÃO</text>')
    o.append(f'<line x1="{gx1}" x2="{gx2}" y1="84" y2="84" stroke="{INK}" stroke-width="1.5"/>')
    for i, r in enumerate(roles):
        cx = COL0 + i * COL_W + COL_W / 2
        o.append(f'<text x="{cx}" y="{head_y}" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" letter-spacing="1.5" fill="{INK2}">{ROLE_LABELS.get(r, r.upper())}</text>')
    o.append(f'<text x="{status_x}" y="{head_y}" font-family="{MONO}" font-size="11" font-weight="700" letter-spacing="1.5" fill="{INK2}">NÍVEL · STATUS</text>')
    o.append(f'<line x1="{LEFT}" x2="{width - 40}" y1="{first_y}" y2="{first_y}" stroke="{INK}"/>')

    prev_tier = None
    for i, t in enumerate(tools):
        y = first_y + i * ROW_H
        tier = t.get("tier", "core")
        if prev_tier and tier != prev_tier:
            o.append(f'<line x1="{LEFT}" x2="{width - 40}" y1="{y}" y2="{y}" stroke="{INK}" stroke-dasharray="3 2"/>')
        prev_tier = tier
        name = t["name"] if len(t["name"]) <= 46 else t["name"][:45] + "…"
        o.append(f'<text x="{LEFT}" y="{y + 21}" font-family="{MONO}" font-size="10" fill="{INK3}">{escape(t["kind"])}</text>')
        o.append(f'<text x="{NAME_X}" y="{y + 21}" font-family="{SANS}" font-size="13" fill="{INK}">{escape(name)}</text>')
        for j, r in enumerate(roles):
            cx = COL0 + j * COL_W + COL_W / 2
            if r in t["roles"]:
                fill = PRIMARY if t["roles"][0] == r else SECONDARY
                o.append(f'<rect x="{cx - 17}" y="{y + 6}" width="34" height="20" fill="{fill}"/>')
            else:
                o.append(f'<rect x="{cx - 17}" y="{y + 6}" width="34" height="20" fill="none" stroke="{RULE}" stroke-dasharray="3 2"/>')
        flag = "A-VERIFICAR" if t["status"] != "documentado" else "DOCUMENTADO"
        color, weight = (SIGNAL, "700") if t["status"] != "documentado" else (INK3, "400")
        tier_label = "CORE" if tier == "core" else "COMPL."
        o.append(
            f'<text x="{status_x}" y="{y + 21}" font-family="{MONO}" font-size="10" letter-spacing="1" fill="{INK2}" font-weight="700">{tier_label}'
            f'<tspan fill="{color}" font-weight="{weight}">  {flag}</tspan></text>'
        )
    end = first_y + n * ROW_H
    o.append(f'<line x1="{LEFT}" x2="{width - 40}" y1="{end}" y2="{end}" stroke="{INK}"/>')

    # legenda
    ly = end + 24
    o.append(f'<text x="{LEFT}" y="{ly + 11}" font-family="{MONO}" font-size="10" font-weight="700" letter-spacing="1" fill="{INK2}">ESCALA</text>')
    o.append(f'<rect x="{LEFT + 76}" y="{ly}" width="28" height="16" fill="{PRIMARY}"/>')
    o.append(f'<rect x="{LEFT + 112}" y="{ly}" width="28" height="16" fill="{SECONDARY}"/>')
    o.append(f'<rect x="{LEFT + 148}" y="{ly}" width="28" height="16" fill="none" stroke="{RULE}" stroke-dasharray="3 2"/>')
    o.append(f'<text x="{LEFT + 190}" y="{ly + 12}" font-family="{MONO}" font-size="10" fill="{INK3}">Escuro: papel principal (o primeiro de roles). Claro: papel secundário. Tracejado: não se aplica.</text>')
    o.append(f'<text x="{LEFT}" y="{ly + 40}" font-family="{MONO}" font-size="10" fill="{INK3}">DOCUMENTADO: a documentação foi lida. A-VERIFICAR: sugerida sem checagem. Ler não é executar, e manutenção ativa não foi auditada.</text>')
    o.append(f'<text x="{LEFT}" y="{ly + 56}" font-family="{MONO}" font-size="10" fill="{INK3}">Gerado de data/tools.json. Para atualizar: edite o JSON e rode make charts.</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--check", action="store_true")
    args = p.parse_args(argv)
    svg = render(json.loads(DATA.read_text(encoding="utf-8")))
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != svg:
            print("assets/tool-map.svg desatualizado: rode `python scripts/build_charts.py`", file=sys.stderr)
            return 1
        return 0
    OUT.write_text(svg, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} ({len(svg)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
