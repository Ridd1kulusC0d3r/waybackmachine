#!/usr/bin/env bash
# Verifica a integridade das capturas baixadas por wb_fetch.py (SHA256SUMS ao lado de raw/).
# Uso: wb-verify.sh <diretório-da-coleta>   (ex.: out/example.com)
set -euo pipefail

dir="${1:?uso: ${0##*/} <diretório-da-coleta>}"
[ -f "$dir/SHA256SUMS" ] || { echo "sem SHA256SUMS em $dir" >&2; exit 2; }

cd "$dir"
if sha256sum --quiet -c SHA256SUMS; then
  echo "OK: $(wc -l < SHA256SUMS) arquivos íntegros"
else
  echo "FALHA: arquivos alterados ou ausentes (veja acima)" >&2
  exit 1
fi
