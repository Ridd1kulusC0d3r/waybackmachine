#!/usr/bin/env python3
"""Resume um CSV de capturas (saída de wb_cdx.py) como cronologia em Markdown.

Destaca mudanças de digest e de status HTTP entre capturas consecutivas.
Uma mudança de digest indica que o conteúdo bruto mudou, não *o que* mudou:
confirme com wb_diff.py.

Exemplo:
    python scripts/wb_timeline.py out/pagina.csv > out/pagina-timeline.md
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import datetime


def fmt_ts(ts: str) -> str:
    ts = ts.ljust(14, "0")
    return datetime.strptime(ts[:14], "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")


def load(path: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return sorted(rows, key=lambda r: r["timestamp"])


def change_points(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Capturas em que digest ou statuscode diferem da captura anterior."""
    out: list[dict[str, str]] = []
    prev = None
    for r in rows:
        if prev is not None:
            reasons = []
            if r.get("digest") != prev.get("digest"):
                reasons.append("digest")
            if r.get("statuscode") != prev.get("statuscode"):
                reasons.append(f"status {prev.get('statuscode')}→{r.get('statuscode')}")
            if reasons:
                out.append({**r, "reason": ", ".join(reasons), "prev_ts": prev["timestamp"]})
        prev = r
    return out


def render(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "# Cronologia\n\nNenhuma captura.\n"
    per_year = Counter(r["timestamp"][:4] for r in rows)
    status = Counter(r.get("statuscode", "-") for r in rows)
    changes = change_points(rows)
    lines = [
        "# Cronologia de capturas",
        "",
        f"- URL: `{rows[0].get('original', '?')}`",
        f"- Capturas: **{len(rows)}**",
        f"- Primeira captura: `{fmt_ts(rows[0]['timestamp'])}` UTC",
        f"- Última captura: `{fmt_ts(rows[-1]['timestamp'])}` UTC",
        f"- Digests distintos: **{len({r.get('digest') for r in rows})}**",
        "",
        "> A primeira captura documenta uma **observação arquivada**, não a data de publicação.",
        "",
        "## Capturas por ano",
        "",
        "| Ano | Capturas |",
        "|---|---|",
        *[f"| {y} | {n} |" for y, n in sorted(per_year.items())],
        "",
        "## Status HTTP",
        "",
        "| Status | Capturas |",
        "|---|---|",
        *[f"| {s} | {n} |" for s, n in sorted(status.items())],
        "",
        f"## Pontos de mudança ({len(changes)})",
        "",
    ]
    if changes:
        lines += ["| Captura (UTC) | Anterior (UTC) | Motivo |", "|---|---|---|"]
        lines += [f"| {fmt_ts(c['timestamp'])} | {fmt_ts(c['prev_ts'])} | {c['reason']} |" for c in changes]
    else:
        lines.append("Nenhuma mudança de digest ou status entre capturas consecutivas.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("csv_path")
    args = p.parse_args(argv)
    sys.stdout.write(render(load(args.csv_path)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
