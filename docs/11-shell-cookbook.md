# 11 · Shell cookbook para saídas da CDX

Receitas com ferramentas padrão (`curl`, `awk`, `sort`, `uniq`, `comm`, `cut`, `jq`). Entradas: o TSV de `scripts/sh/wb-cdx.sh` (timestamp, original, status, mime, digest) ou o CSV de `wb_cdx.py` (com cabeçalho).

## Coleta

```bash
# TSV direto da CDX (sem Python)
scripts/sh/wb-cdx.sh example.com/pagina > pagina.tsv

# Domínio inteiro, só HTML 200 (parâmetros extras como chave=valor)
scripts/sh/wb-cdx.sh example.com matchType=domain filter=statuscode:200 filter=mimetype:text/html > dominio.tsv
```

## Resumo rápido

```bash
# capturas por ano
cut -c1-4 pagina.tsv | sort | uniq -c

# primeira e última observação
sort pagina.tsv | sed -n '1p;$p'

# distribuição de status
awk '{print $3}' pagina.tsv | sort | uniq -c | sort -rn

# digests distintos
awk '{print $5}' pagina.tsv | sort -u | wc -l
```

## Pontos de mudança

```bash
# linhas em que o digest difere da linha anterior (ordenado por tempo)
sort pagina.tsv | awk 'NR>1 && $5!=prev {print prev_ts" -> "$1"  digest mudou"} {prev=$5; prev_ts=$1}'
```

## Inventário

```bash
# URLs distintas
awk '{print $2}' dominio.tsv | sort -u > urls.txt

# hosts
awk -F/ '{print $3}' urls.txt | sort | uniq -c | sort -rn | head -20

# extensões
grep -oE '\.[A-Za-z0-9]{1,5}($|\?)' urls.txt | tr -d '?' | sort | uniq -c | sort -rn | head

# URLs que apareceram só em capturas antigas (antes de 2021) e nunca depois
awk '$1<"2021"{old[$2]=1} $1>="2021"{new[$2]=1} END{for(u in old) if(!(u in new)) print u}' dominio.tsv
```

## Comparar fontes (procedência!)

```bash
# o que o gau (só Wayback) tem a mais que o waybackurls?
sort -u urls-wayback.txt > a.txt; sort -u urls.txt > b.txt
comm -13 b.txt a.txt     # só em a
comm -12 a.txt b.txt     # em ambos
```

## Integridade

```bash
# hash de um bruto baixado
sha256sum raw/20190101000000_ab12cd34ef.bin

# verificar coleta inteira (SHA256SUMS gerado por wb_fetch.py)
scripts/sh/wb-verify.sh out/example.com
```

## JSON com jq (saída `--format jsonl` de `wb_cdx.py`)

```bash
python scripts/wb_cdx.py example.com --format jsonl | jq -r 'select(.statuscode=="200") | [.timestamp,.original] | @tsv'
python scripts/wb_cdx.py example.com --format jsonl | jq -s 'group_by(.digest) | map({digest: .[0].digest, n: length, first: (map(.timestamp)|min)})'
```

## Cuidados

- `sort` depende do *locale*: use `LC_ALL=C sort` em scripts para ordem reprodutível.
- Não use `collapse=` no primeiro passe de uma cronologia ([02](02-cdx-api.md)).
- Guarde sempre o arquivo bruto original antes de filtrar.
