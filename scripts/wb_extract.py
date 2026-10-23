#!/usr/bin/env python3
"""Extrai pivôs/IOCs candidatos de capturas brutas já baixadas.

Os resultados são *candidatos*: expressões regulares geram falsos positivos
(sobretudo carteiras cripto e IPs). Cada item volta com arquivo de origem e
SHA-256, para validação manual. Nada é consultado na rede.

Exemplo:
    python scripts/wb_extract.py out/raw --format json > out/iocs.json
    python scripts/wb_extract.py out/raw --format csv --defang > out/iocs.csv
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from datetime import datetime, timezone
from ipaddress import IPv4Address
from pathlib import Path
from urllib.parse import urlparse

PATTERNS: dict[str, re.Pattern[str]] = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "url": re.compile(r"""https?://[^\s"'<>)\]]+""", re.I),
    "ipv4": re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"),
    "ga_universal": re.compile(r"\bUA-\d{4,10}-\d{1,4}\b"),
    "ga4": re.compile(r"\bG-[A-Z0-9]{10}\b"),
    "gtm": re.compile(r"\bGTM-[A-Z0-9]{4,8}\b"),
    "adsense": re.compile(r"\bpub-\d{16}\b"),
    "onion_v3": re.compile(r"\b[a-z2-7]{56}\.onion\b"),
    "telegram": re.compile(r"\bt\.me/[A-Za-z0-9_]{4,32}\b"),
    "eth_candidate": re.compile(r"\b0x[a-fA-F0-9]{40}\b"),
    "btc_candidate": re.compile(r"\b(?:bc1[a-z0-9]{25,59}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b"),
}
# IDs de analytics são pivôs fortes de infraestrutura compartilhada; cripto, fracos sem validação.
STRENGTH = {"ga_universal": "forte", "ga4": "forte", "gtm": "forte", "adsense": "forte", "onion_v3": "média",
            "email": "média", "telegram": "média", "domain": "média", "url": "fraca", "ipv4": "fraca",
            "eth_candidate": "fraca", "btc_candidate": "fraca"}


def valid_ipv4(s: str) -> bool:
    try:
        ip = IPv4Address(s)
    except ValueError:
        return False
    return not (ip.is_unspecified or ip.is_loopback or ip.is_multicast or ip.is_reserved)


def extract(text: str, keep_private: bool = False) -> dict[str, set[str]]:
    found: dict[str, set[str]] = {k: set(p.findall(text)) for k, p in PATTERNS.items()}
    found["ipv4"] = {i for i in found["ipv4"] if valid_ipv4(i) and (keep_private or not IPv4Address(i).is_private)}
    domains = {urlparse(u).hostname for u in found["url"]} | {e.split("@", 1)[1].lower() for e in found["email"]}
    found["domain"] = {d for d in domains if d}
    return {k: v for k, v in found.items() if v}


def defang(kind: str, value: str) -> str:
    if kind in ("url",):
        value = re.sub(r"^http", "hxxp", value, flags=re.I)
    if kind in ("url", "domain", "ipv4", "email", "onion_v3"):
        value = value.replace(".", "[.]")
    if kind == "email":
        value = value.replace("@", "[@]")
    return value


def iter_files(paths: list[Path]):
    for p in paths:
        if p.is_dir():
            yield from sorted(f for f in p.rglob("*") if f.is_file())
        elif p.is_file():
            yield p


def scan(paths: list[Path], max_bytes: int, keep_private: bool) -> list[dict]:
    out = []
    for f in iter_files(paths):
        data = f.read_bytes()[:max_bytes]
        out.append({
            "file": str(f),
            "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
            "capture_ts": f.name.split("_", 1)[0] if f.name[:14].isdigit() else None,
            "iocs": {k: sorted(v) for k, v in extract(data.decode("utf-8", errors="replace"), keep_private).items()},
        })
    return out


def summarize(results: list[dict]) -> dict[str, dict[str, list[str]]]:
    """tipo -> valor -> arquivos onde aparece (ordenados por captura)."""
    summary: dict[str, dict[str, list[str]]] = {}
    for r in sorted(results, key=lambda r: r["capture_ts"] or ""):
        for kind, values in r["iocs"].items():
            for v in values:
                summary.setdefault(kind, {}).setdefault(v, []).append(r["file"])
    return summary


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("paths", nargs="+", type=Path)
    p.add_argument("--format", choices=["json", "csv"], default="json")
    p.add_argument("--defang", action="store_true", help="defang de URLs, domínios, IPs e e-mails na saída")
    p.add_argument("--keep-private", action="store_true", help="mantém IPs privados (RFC1918)")
    p.add_argument("--max-bytes", type=int, default=5_000_000, help="limite lido por arquivo")
    args = p.parse_args(argv)

    results = scan(args.paths, args.max_bytes, args.keep_private)
    summary = summarize(results)
    fmt = (lambda k, v: defang(k, v)) if args.defang else (lambda k, v: v)

    if args.format == "csv":
        buf = io.StringIO()
        w = csv.writer(buf, lineterminator="\n")
        w.writerow(["type", "value", "strength", "first_capture", "last_capture", "files"])
        by_file = {r["file"]: r["capture_ts"] for r in results}
        for kind, vals in sorted(summary.items()):
            for v, files in sorted(vals.items()):
                tss = sorted(t for t in (by_file[f] for f in files) if t)
                w.writerow([kind, fmt(kind, v), STRENGTH.get(kind, ""), tss[0] if tss else "", tss[-1] if tss else "", len(files)])
        sys.stdout.write(buf.getvalue())
    else:
        doc = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "note": "Candidatos por expressão regular; valide manualmente. Não prova atribuição.",
            "defanged": args.defang,
            "summary": {k: {fmt(k, v): files for v, files in vals.items()} for k, vals in summary.items()},
            "files": [{**r, "iocs": {k: [fmt(k, x) for x in v] for k, v in r["iocs"].items()}} for r in results],
        }
        json.dump(doc, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
