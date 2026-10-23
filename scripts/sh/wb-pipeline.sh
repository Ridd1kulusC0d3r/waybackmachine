#!/usr/bin/env bash
# Pipeline ponta a ponta: índice -> cronologia -> inventário [-> download -> IOCs].
# Gera out/<alvo>/ com RUN.log, para refazer e auditar a coleta.
#
# Uso: wb-pipeline.sh <alvo> [--match exact|prefix|host|domain] [--from AAAA] [--to AAAA]
#                            [--fetch N] [--out DIR]
# --fetch N  baixa até N capturas HTML (status 200, digests únicos) e extrai pivôs.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
py="$here/.."
target="" match="exact" from="" to="" fetch_n=0 out_root="out"

while [ $# -gt 0 ]; do
  case "$1" in
    --match) match="$2"; shift 2 ;;
    --from)  from="$2";  shift 2 ;;
    --to)    to="$2";    shift 2 ;;
    --fetch) fetch_n="$2"; shift 2 ;;
    --out)   out_root="$2"; shift 2 ;;
    -h|--help) sed -n '2,8p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*) echo "opção desconhecida: $1" >&2; exit 2 ;;
    *)  target="$1"; shift ;;
  esac
done
[ -n "$target" ] || { echo "faltou o alvo; use --help" >&2; exit 2; }

slug="$(printf '%s' "$target" | tr -c '\n0-9A-Za-z.-' '_' | cut -c1-80)"
dir="$out_root/$slug"
mkdir -p "$dir"
log="$dir/RUN.log"
say() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$log" >&2; }

cdx_extra=(); [ -n "${WB_CDX_BASE:-}" ] && cdx_extra=(--base-url "$WB_CDX_BASE")
web_extra=(); [ -n "${WB_WEB_BASE:-}" ] && web_extra=(--base-url "$WB_WEB_BASE")
range=(); [ -n "$from" ] && range+=(--from "$from"); [ -n "$to" ] && range+=(--to "$to")

say "alvo=$target match=$match from=${from:-*} to=${to:-*} fetch=$fetch_n"
say "1/5 índice (sem collapse: preserva repetições)"
python3 "$py/wb_cdx.py" "$target" --match "$match" ${range[@]+"${range[@]}"} ${cdx_extra[@]+"${cdx_extra[@]}"} --out "$dir/cdx.csv" 2>>"$log"

say "2/5 cronologia"
python3 "$py/wb_timeline.py" "$dir/cdx.csv" > "$dir/timeline.md"

say "3/5 inventário"
python3 "$py/wb_inventory.py" "$dir/cdx.csv" > "$dir/inventory.md"

if [ "$fetch_n" -gt 0 ]; then
  say "4/5 download de até $fetch_n capturas (id_, digests únicos)"
  python3 "$py/wb_fetch.py" "$dir/cdx.csv" --out-dir "$dir/raw" --mime-prefix text/html \
    --unique-digest --limit "$fetch_n" ${web_extra[@]+"${web_extra[@]}"} 2>>"$log"
  say "5/5 pivôs candidatos (defanged)"
  python3 "$py/wb_extract.py" "$dir/raw" --defang > "$dir/iocs.json"
else
  say "4/5 e 5/5 puladas (use --fetch N)"
fi
say "pronto: $dir"
