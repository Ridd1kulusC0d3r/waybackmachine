# Contribuindo

## Adicionar ou corrigir uma ferramenta

1. Edite **somente** `data/tools.json` (siga o formato das entradas existentes; `roles` devem existir em `roles`).
2. Rode `make catalog` para regenerar `README.md` (tabelas) e `docs/catalogo.md`.
3. Rode `make test`.
4. Abra o PR usando o template.

Critérios de entrada:

- Faz algo específico com a Wayback Machine / CDX / Internet Archive.
- Está mantida ou, se não, o `caveat` diz isso.
- `status` honesto: `documentado` (documentação lida), `a-verificar` (sugerida, sem checagem) ou `testado` (você executou; descreva como no PR).
- `tier`: `core` entra no mapa principal; `complementar` na seção de fontes alternativas.
- O `verdict` é uma avaliação fundamentada, não propaganda.

## Scripts

- Somente biblioteca padrão do Python. Compatível com 3.9+.
- Shell: `set -euo pipefail`, aprovado no `shellcheck` (`make lint`).
- Todo comportamento novo tem teste em `tests/` usando o servidor simulado (sem rede real).
- Não adicione coleta que ignore limites de taxa ou o `User-Agent` identificável.

## Documentos

Português do Brasil, tom técnico e calibrado. Toda afirmação sobre o que a Wayback "prova" deve respeitar [docs/01-fundamentos.md](docs/01-fundamentos.md).
