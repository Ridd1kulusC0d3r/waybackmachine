# 10 · Diagnóstico e qualidade da coleta

[Início](../README.md) · [CDX](02-cdx-api.md) · [Laboratórios](09-laboratorios-avancados.md)

| Sintoma | Hipóteses a verificar | Próximo passo |
|---|---|---|
| Consulta sem resultados | URL/escopo inadequado, filtros, lacuna no índice | Guardar a consulta; verificar variantes e remover filtros um a um |
| HTTP 429 | Limitação de requisições | Respeitar Retry-After quando presente, reduzir concorrência e usar backoff limitado |
| HTTP 5xx ou timeout | Falha transitória do serviço | Registrar tentativa; repetir com limite e pausa, sem concluir ausência |
| Registro CDX existe, replay falha | Registro inacessível, falha de recuperação, restrição | Guardar metadados e erro; tentar outro snapshot ou acervo |
| Data entregue difere da pedida | Redirecionamento ou captura próxima | Registrar URL final e timestamp efetivo; não rotular pelo timestamp solicitado |
| Página sem imagens/CSS | Recursos não capturados ou de outra data | Conferir as URLs dos recursos e anotar incompletude |
| HTTP 200 com mensagem de erro | Soft-404, bloqueio ou tela intermediária | Inspecionar corpo; status 200 não garante conteúdo útil |
| Diff enorme com pouco texto mudado | HTML dinâmico, atributos, menus, scripts | Preservar bruto e criar uma comparação textual derivada |
| Ferramentas discordam | Provedores, filtros, períodos ou deduplicação diferentes | Comparar configurações antes de interpretar divergência |

## Três decisões antes de automatizar

1. **Disponibilidade ou inventário?** Availability busca uma captura disponível próxima à data; CDX permite consultar registros. Não use uma resposta de disponibilidade como lista completa.
2. **Coleta completa ou amostra?** `limit` corta resultados. Documente paginação, interrupções e limite de orçamento; nunca chame uma amostra de levantamento exaustivo.
3. **Consulta histórica ou captura nova?** Save Page Now solicita preservação atual. Não recupera uma versão passada que não foi arquivada.

## Registro mínimo de execução

Anote ferramenta e versão/commit, fonte, parâmetros, início e fim UTC, códigos HTTP, retries, URL solicitada, URL efetiva, arquivos salvos e SHA-256. Não registre tokens, cookies ou credenciais nos relatórios.

Não há um limite universal de requisições que se possa prometer para todas as APIs e condições. Adapte a taxa às respostas do serviço. Em reexecuções, compare os resultados porque os índices podem mudar.

## Controle de interpretação

- Digest diferente é uma pista de diferença de payload, não uma explicação da mudança.
- Digest igual não assegura igualdade visual de todos os recursos da página.
- Uma captura não demonstra continuidade de publicação entre observações.
- Ausência no arquivo não demonstra ausência na web.
- A página pode conter uma afirmação falsa: arquivamento preserva uma fonte, não valida seu conteúdo.

Fontes: [Wayback APIs](https://archive.org/help/wayback_api.php), [CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server), [ajuda oficial](https://help.archive.org/help/using-the-wayback-machine/), [EDGI wayback](https://wayback.readthedocs.io/en/stable/). A tabela é uma síntese operacional; confirme o comportamento na versão usada.
