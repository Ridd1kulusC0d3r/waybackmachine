# 09 · Seis laboratórios de OSINT temporal

[Início](../README.md) · [Exercícios básicos](04-exercicios.md) · [Ficha de comparação](../templates/comparacao-temporal.md)

Estes são roteiros propostos, não resultados de experimentos executados. Use páginas públicas de demonstração ou domínios próprios. Escolha timestamps efetivamente retornados pelo índice; não invente datas de captura.

## 1. Primeiro registro observável

**Pergunta:** qual é a captura acessível mais antiga desta URL?

1. Consulte a URL exata com CDX, sem filtro de status e sem collapse.
2. Confira variantes HTTP/HTTPS, www e caminhos equivalentes, registrando cada consulta.
3. Abra a captura mais antiga disponível e identifique conteúdo, erro ou redirecionamento.
4. Busque evidências adicionais de data no próprio documento e em fontes independentes.

**Entrega:** tabela com URL, timestamp, status, conteúdo e limite da conclusão.
**Aceite:** escrever “observada nesta captura”, sem transformar a data em publicação comprovada. Um registro antigo pode pertencer a outro uso do mesmo domínio.

## 2. Mudança de afirmação pública

**Pergunta:** como mudou uma frase de uma página institucional?

1. Selecione duas capturas da mesma URL com a frase legível.
2. Guarde os conteúdos e timestamps efetivamente entregues, inclusive redirecionamentos.
3. Compare a frase com seu contexto; separe mudanças de texto de navegação, banners e scripts.
4. Procure capturas intermediárias. Registre lacunas e possíveis reversões.

**Entrega:** comparação antes/depois com URLs de evidência e hipótese alternativa.
**Aceite:** descrever diferença entre observações. A janela entre elas só delimita uma transição sob hipóteses explicitadas; não demonstra que houve uma única mudança.

## 3. Inventário histórico de documentos

**Pergunta:** quais PDFs um domínio teve indexados num período?

Consulta de exemplo, não executada:

```bash
curl -G 'https://web.archive.org/cdx/search/cdx' \
  --data-urlencode 'url=example.com' \
  --data 'matchType=domain' \
  --data 'from=2020' --data 'to=2025' \
  --data 'filter=mimetype:application/pdf' \
  --data 'output=json' \
  --data 'fl=timestamp,original,statuscode,mimetype,digest' \
  --data 'limit=1000'
```

1. Registre que a consulta está limitada a 1.000 linhas; use paginação para coleta completa.
2. Compare a busca por MIME com URLs contendo extensão PDF: nenhuma abordagem é cobertura garantida.
3. Recupere uma amostra e confirme se o arquivo corresponde ao tipo anunciado.
4. Preserve repetições no resultado bruto; deduplique somente uma cópia de trabalho.

**Entrega:** inventário com recuperado/não recuperado e motivo.
**Aceite:** não apresentar o inventário como todos os PDFs que já existiram no domínio.

## 4. Superfície histórica para defesa

**Pergunta:** quais caminhos e subdomínios apareceram nas fontes históricas?

1. Consulte CDX ou use gau com o provedor Wayback explícito.
2. Agrupe URLs por host, extensão e diretório em uma cópia derivada.
3. Separe endpoints históricos de ativos cuja existência atual foi verificada.
4. Em ambiente próprio, compare com o inventário atual e documente diferenças.

**Entrega:** tabela de pistas para revisão defensiva, com data e fonte.
**Aceite:** não classificar URL antiga como vulnerabilidade nem como ativo ainda pertencente à organização sem validação.

## 5. Preservação e teste de replay

**Pergunta:** consigo consultar a evidência após a página original mudar?

1. Capture uma página própria com ArchiveWeb.page ou Browsertrix Crawler.
2. Exporte o arquivo, registre versão/configuração e calcule seu SHA-256.
3. Abra em ReplayWeb.page ou pywb e revise conteúdo e recursos.
4. Depois de carregar o reprodutor, teste a navegação com acesso à origem indisponível e registre dependências externas.

**Entrega:** arquivo preservado, manifesto e tabela de falhas.
**Aceite:** distinguir conteúdo realmente contido no arquivo de recursos obtidos ao vivo. Não adicionar arquivos grandes ou dados de investigação ao Git sem necessidade.

## 6. Comparação entre acervos

**Pergunta:** Wayback e Arquivo.pt oferecem evidências diferentes para a mesma URL?

1. Defina URL e período iguais para as duas consultas.
2. Use as interfaces ou APIs documentadas por cada serviço.
3. Registre timestamp, URL de replay, origem e resultado de recuperação separadamente.
4. Compare cobertura e conteúdo sem presumir que datas próximas representam a mesma versão.

**Entrega:** matriz URL × provedor × captura × disponibilidade.
**Aceite:** resultado vazio significa “não encontrado nesta consulta”; não prova que a página nunca existiu.

## Critério comum de qualidade

Cada entrega deve permitir a outra pessoa reconstruir a consulta: pergunta, escopo, fonte, parâmetros, horários UTC, arquivos originais, hashes, transformações, observações e incertezas. Use [cadeia de evidência](05-cadeia-de-evidencia.md).

Fontes técnicas: [CDX](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server), [gau](https://github.com/lc/gau), [Webrecorder](08-ecossistema-e-preservacao.md), [Arquivo.pt](https://github.com/arquivo/pwa-technologies/wiki/APIs).
