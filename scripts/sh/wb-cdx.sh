#!/usr/bin/env bash
# Consulta mínima à CDX API, sem Python. Saída TSV: timestamp original statuscode mimetype digest.
# Uso: wb-cdx.sh <url> [parâmetros extras da CDX, ex.: matchType=domain filter=statuscode:200]
set -euo pipefail

BASE="${WB_CDX_BASE:-https://web.archive.org/cdx/search/cdx}"
UA="wayback-atlas/0.2.0 (+https://github.com/Ridd1kulusC0d3r/waybackmachine)"

[ $# -ge 1 ] || { echo "uso: ${0##*/} <url> [chave=valor ...]" >&2; exit 2; }
target="$1"; shift

args=(--data-urlencode "url=${target}" --data "output=txt" --data "fl=timestamp,original,statuscode,mimetype,digest")
for kv in "$@"; do args+=(--data-urlencode "$kv"); done

curl --fail --silent --show-error --get --retry 4 --retry-delay 2 --retry-all-errors \
  -A "$UA" "${args[@]}" "$BASE" | tr ' ' '\t'
