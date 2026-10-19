# 02 · CDX Server API: o índice por baixo de tudo

Referência primária: [wayback-cdx-server (README oficial)](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md). Esta página é um resumo operacional; **em caso de dúvida, vale a documentação oficial**.

Endpoint: `https://web.archive.org/cdx/search/cdx`

## Campos (`fl=`)

| Campo | Significado | Uso em OSINT |
|---|---|---|
| `timestamp` | Instante da captura (UTC) | Eixo da cronologia |
| `original` | URL como capturada | Variantes de URL, parâmetros, subdomínios |
| `statuscode` | Status HTTP | 200 resposta de sucesso · 3xx redirecionamento · 404 observado naquela captura; não prova remoção definitiva |
| `mimetype` | Tipo de conteúdo | Separar HTML de PDF, JS, imagens |
| `digest` | Digest do payload indexado | Indício de repetição daquele payload; não representa todos os recursos da página |
| `length` | Tamanho compactado | Triagem grosseira |
| `urlkey` | URL normalizada | Agrupar variantes |

## Parâmetros mais úteis

| Parâmetro | Exemplo | Efeito |
|---|---|---|
| `url` | `example.com/pagina` | Alvo |
| `matchType` | `exact` · `prefix` · `host` · `domain` | `domain` inclui subdomínios |
| `from` / `to` | `from=2019&to=20201231` | Janela temporal |
| `filter` | `statuscode:200` · `!mimetype:text/html` | Inclui ou exclui (`!`); repetível |
| `collapse` | `digest` · `timestamp:8` | Agrupa linhas adjacentes (ver aviso) |
| `limit` | `limit=1000` | Limite de linhas |
| `output` | `json` | Saída em JSON (primeira linha é cabeçalho) |
| `showResumeKey` | `true` | Devolve chave para paginar |
| `resumeKey` | *(valor devolvido)* | Continua de onde parou |

## Receitas

**Cronologia completa de uma página**

```bash
curl -G 'https://web.archive.org/cdx/search/cdx' \
  --data-urlencode 'url=example.com/pagina' \
  --data 'output=json' --data 'fl=timestamp,original,statuscode,mimetype,digest'
```

**Só mudanças de conteúdo** (um por digest consecutivo)

```bash
... --data 'collapse=digest'
```

**Inventário de um domínio, só HTML com sucesso, uma captura por mês**

```bash
curl -G 'https://web.archive.org/cdx/search/cdx' \
  --data-urlencode 'url=example.com' --data 'matchType=domain' \
  --data 'filter=statuscode:200' --data 'filter=mimetype:text/html' \
  --data 'collapse=timestamp:6' --data 'fl=timestamp,original'
```

**Equivalente com o script do repositório** (com proveniência)

```bash
python scripts/wb_cdx.py example.com --match domain \
  --filter statuscode:200 --filter mimetype:text/html \
  --collapse timestamp:6 --fields timestamp,original --out out/inventario.csv
```

## ⚠ Deduplicação esconde evidência

`collapse=digest` e `collapse=timestamp:N` são úteis para reduzir ruído, mas **descartam repetições**. Para uma cronologia, o primeiro passe deve ser **sem `collapse`**: as repetições mostram a *frequência de observação* e ajudam a delimitar quando algo esteve estável. Dedupe numa segunda etapa, guardando o arquivo bruto original.

## Boas maneiras

- Identifique-se com um `User-Agent` descritivo (o script já faz).
- Pagine com `resumeKey` e faça pausas; respeite respostas 429 com backoff.
- Guarde a **URL exata** da consulta e o instante da coleta: o índice cresce com o tempo, então a mesma consulta pode devolver mais linhas amanhã.
