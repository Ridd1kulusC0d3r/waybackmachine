# 12 · Glossário e FAQ

## Glossário

| Termo | Significado |
|---|---|
| **Captura (snapshot / memento)** | Uma cópia de uma URL num instante, guardada no arquivo |
| **CDX** | Índice de capturas consultável por API; linhas com timestamp, URL, status, MIME, digest… |
| **Digest** | Hash do conteúdo capturado; digests iguais indicam conteúdo bruto igual |
| **`id_`** | Modificador de URL que devolve o conteúdo bruto, sem banner nem links reescritos |
| **Save Page Now (SPN)** | Serviço que cria uma captura agora; **publica** a página |
| **Memento** | Padrão (RFC 7089) para acessar versões passadas de recursos web |
| **Pivô** | Dado que liga o objeto atual a outros |
| **IOC** | Indicador compartilhável associado a atividade maliciosa |
| **Defang** | Neutralizar um indicador para não ser clicável (`hxxp`, `[.]`) |
| **Cloaking** | Servir conteúdo diferente a rastreadores e a vítimas |
| **TLP** | Protocolo de sinalização de compartilhamento (CLEAR, GREEN, AMBER, RED) |
| **ACH** | Análise de hipóteses concorrentes |
| **Proveniência** | Registro de como, quando e por quem um dado foi obtido |

## FAQ

**A primeira captura é a data de publicação?**
Não. É a primeira *observação arquivada*. A página pode ter existido antes.

**Não achei captura. Então não existia?**
Não. Ausência de captura é ausência de observação. Tente outras variações da URL (com/sem `www`, `http`/`https`, barra final) e outras fontes.

**Digest diferente significa que o conteúdo mudou?**
Que o conteúdo *bruto* mudou. Pode ser um contador, um token, um anúncio. Confirme com diff.

**Posso usar `collapse=digest` para limpar o resultado?**
Numa segunda etapa, sim. No primeiro passe da cronologia, não: as repetições são evidência.

**Salvar a página para "garantir a prova" é boa ideia?**
Cuidado: o Save Page Now é público e pode alertar o dono. Para material sensível, preserve localmente com hash.

**Por que ficam diferentes a página renderizada e o `id_`?**
A renderizada reescreve links e injeta banner; recursos (CSS, JS, imagens) podem vir de capturas de outras datas. Use `id_` para análise, renderizada para ilustração.

**`wb_cdx.py` retorna menos linhas que o site da Wayback.**
Verifique `--limit`, `--collapse` e filtros; compare a URL exata gravada em `.meta.json`.

**Posso compartilhar o `iocs.json`?**
Revise antes: são *candidatos*. Defang, confiança e proveniência precisam estar preenchidos, e dados pessoais, minimizados ([07](07-etica-e-opsec.md)).

**As ferramentas foram testadas?**
As do catálogo foram curadas pela documentação (`documentado`/`a-verificar`). Os scripts deste repositório têm testes contra um servidor simulado; valide-os contra a Wayback real no seu ambiente.
