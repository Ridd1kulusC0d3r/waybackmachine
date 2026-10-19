# 05 · Cadeia de evidência para capturas

Objetivo: qualquer pessoa deve conseguir **refazer** sua coleta e chegar ao mesmo material, ou entender por que não chegou.

## O que registrar, sempre

| Item | Por quê | Como |
|---|---|---|
| Consulta exata (URL completa da CDX) | O índice cresce; a consulta precisa ser reproduzível | `wb_cdx.py` grava em `.meta.json` |
| Instante da coleta (UTC) | Distingue "o que existia no arquivo" de "o que existe hoje" | `.meta.json` |
| Hash SHA-256 do bruto | Integridade e detecção de adulteração | `sha256sum`; `wb_diff.py` imprime |
| URL da captura **com timestamp** | Âncora citável | `https://web.archive.org/web/AAAAMMDDhhmmss/URL` |
| Variante usada (`id_` ou renderizada) | Muda o conteúdo e os hashes | Ficha de evidência |
| Ferramenta e versão | Comportamentos diferem | Ficha |
| Capturas de tela (opcional) | Mostram a renderização, não substituem o bruto | Guarde junto, rotulada como "ilustrativa" |

## Fluxo mínimo

```text
coletar índice  →  guardar CSV + .meta.json (imutáveis)
      ↓
baixar bruto (id_)  →  sha256  →  guardar sem editar
      ↓
analisar em CÓPIA  →  ficha de evidência por item relevante
      ↓
relatório  →  cita fichas, separa FATO observado de INFERÊNCIA
```

## Fato, inferência, hipótese

Escreva em camadas, e rotule cada frase:

- **Observação** — "A captura de 14/03/2019 12:00 UTC contém o texto X." *(verificável)*
- **Inferência** — "A página existia, com esse texto, até esse instante." *(consequência direta)*
- **Hipótese** — "Foi publicada pouco antes." *(precisa de corroboração; liste alternativas)*

## Modelos prontos

- [templates/ficha-de-evidencia.md](../templates/ficha-de-evidencia.md)
- [templates/relatorio-timeline.md](../templates/relatorio-timeline.md)

## Corroboração

Para marcos importantes procure **fonte independente** do mesmo arquivo: outro arquivador, cache de buscadores, registros públicos (WHOIS histórico, certificados), menções de terceiros datadas. Duas capturas da mesma Wayback não são duas fontes independentes.
