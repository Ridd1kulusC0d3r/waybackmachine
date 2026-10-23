# Catálogo de ferramentas

> Gerado por `scripts/build_catalog.py` a partir de `data/tools.json`. Não edite à mão.

_Descrições baseadas na documentação dos projetos. Nenhuma ferramenta foi executada na curadoria. Status: 'documentado' = documentação lida na curadoria inicial; 'a-verificar' = entrada complementar sugerida a partir de conhecimento geral, ainda sem checagem da documentação atual._

## Por papel na investigação

### Descobrir URLs

- [xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore) — Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine.
- [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) — Recebe domínios e retorna URLs conhecidas pela Wayback, incluindo subdomínios.
- [lc/gau](https://github.com/lc/gau) — Coleta URLs de Wayback, Common Crawl, OTX e URLScan; oferece filtros e saída JSON.
- [akamhy/waybackpy](https://github.com/akamhy/waybackpy) — Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) — Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- [internetarchive/wayback — CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) — Código e documentação do serviço de consulta ao índice de capturas.
- [cocrawler/cdx_toolkit](https://github.com/cocrawler/cdx_toolkit) — Biblioteca/CLI para consultar índices CDX (Internet Archive e Common Crawl).
- [oduwsdl/MemGator](https://github.com/oduwsdl/MemGator) — Agregador Memento: consulta vários arquivos web ao mesmo tempo.
- [Common Crawl — índice de URLs](https://index.commoncrawl.org/) — Índice de URLs rastreadas pelo Common Crawl, fonte independente da Wayback.

### Recuperar conteúdo

- [xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore) — Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine.
- [akamhy/waybackpy](https://github.com/akamhy/waybackpy) — Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) — Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- [hartator/wayback-machine-downloader](https://github.com/hartator/wayback-machine-downloader) — Recupera arquivos arquivados, com filtros por período, URL e extensão.
- [internetarchive/wayback-machine-webextension](https://github.com/internetarchive/wayback-machine-webextension) — Extensão oficial para salvar páginas e acessar capturas antigas e recentes.
- [jsvine/waybackpack](https://github.com/jsvine/waybackpack) — Baixa o histórico de capturas de uma página da Wayback Machine.

### Analisar no tempo

- [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) — Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- [cocrawler/cdx_toolkit](https://github.com/cocrawler/cdx_toolkit) — Biblioteca/CLI para consultar índices CDX (Internet Archive e Common Crawl).

### Preservar páginas

- [akamhy/waybackpy](https://github.com/akamhy/waybackpy) — Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- [internetarchive/wayback-machine-webextension](https://github.com/internetarchive/wayback-machine-webextension) — Extensão oficial para salvar páginas e acessar capturas antigas e recentes.
- [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) — Arquivamento web auto-hospedado, sob seu controle.

### Referência técnica

- [internetarchive/wayback — CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) — Código e documentação do serviço de consulta ao índice de capturas.
- [Common Crawl — índice de URLs](https://index.commoncrawl.org/) — Índice de URLs rastreadas pelo Common Crawl, fonte independente da Wayback.

## Fichas

### xnl-h4ck3r/waymore

- **Tipo:** cli · **Linguagem:** Python · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/xnl-h4ck3r/waymore>
- **Serve para:** Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine.
- **Avaliação:** Primeira escolha para investigação exploratória: permite pesquisar o conteúdo recuperado, além de listar endereços.
- **Cuidado:** Combina várias fontes; registre a origem de cada resultado.

### tomnomnom/waybackurls

- **Tipo:** cli · **Linguagem:** Go · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/tomnomnom/waybackurls>
- **Serve para:** Recebe domínios e retorna URLs conhecidas pela Wayback, incluindo subdomínios.
- **Avaliação:** Melhor opção simples para pipelines: pequena e direta.
- **Cuidado:** A listagem, sozinha, não é análise de conteúdo.

### lc/gau

- **Tipo:** cli · **Linguagem:** Go · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/lc/gau>
- **Serve para:** Coleta URLs de Wayback, Common Crawl, OTX e URLScan; oferece filtros e saída JSON.
- **Avaliação:** Boa para ampliar cobertura.
- **Cuidado:** Registre a origem dos resultados para não atribuir tudo à Wayback (use --providers wayback para isolar).

### akamhy/waybackpy

- **Tipo:** lib+cli · **Linguagem:** Python · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/akamhy/waybackpy>
- **Serve para:** Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- **Avaliação:** Boa porta de entrada para automação, com exemplos acessíveis.
- **Cuidado:** Save Page Now publica a página no arquivo: avalie o impacto operacional antes de usar.
- **Documentação:** <https://akamhy.github.io/waybackpy/>

### edgi-govdata-archiving/wayback

- **Tipo:** lib · **Linguagem:** Python · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/edgi-govdata-archiving/wayback>
- **Serve para:** Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- **Avaliação:** Candidata para pipelines de pesquisa temporal; documentação dedicada à busca e recuperação.
- **Cuidado:** Cliente de pesquisa/recuperação; a análise temporal fica por sua conta.
- **Documentação:** <https://wayback.readthedocs.io/en/stable/>

### hartator/wayback-machine-downloader

- **Tipo:** cli · **Linguagem:** Ruby · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/hartator/wayback-machine-downloader>
- **Serve para:** Recupera arquivos arquivados, com filtros por período, URL e extensão.
- **Avaliação:** Útil para reconstrução local.
- **Cuidado:** Por padrão reúne a última versão de cada arquivo, podendo misturar datas: delimite o período.

### internetarchive/wayback-machine-webextension

- **Tipo:** extension · **Linguagem:** JavaScript · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/internetarchive/wayback-machine-webextension>
- **Serve para:** Extensão oficial para salvar páginas e acessar capturas antigas e recentes.
- **Avaliação:** Melhor começo sem programação, especialmente durante pesquisa manual.
- **Cuidado:** Salvar uma página a torna pública no arquivo.

### internetarchive/wayback — CDX Server

- **Tipo:** api · **Linguagem:** Java · **Nível:** core · **Status:** documentado
- **Link:** <https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server>
- **Serve para:** Código e documentação do serviço de consulta ao índice de capturas.
- **Avaliação:** Referência técnica essencial: ajuda a entender os dados que as outras ferramentas consultam.
- **Cuidado:** Fonte primária; confira a documentação antes de confiar em resumos.
- **Documentação:** <https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md>

### jsvine/waybackpack

- **Tipo:** cli · **Linguagem:** Python · **Nível:** complementar · **Status:** a-verificar
- **Link:** <https://github.com/jsvine/waybackpack>
- **Serve para:** Baixa o histórico de capturas de uma página da Wayback Machine.
- **Avaliação:** Alternativa leve para guardar todas as versões de uma única URL.
- **Cuidado:** Confirme parâmetros e limites na documentação atual antes de usar.

### cocrawler/cdx_toolkit

- **Tipo:** lib+cli · **Linguagem:** Python · **Nível:** complementar · **Status:** a-verificar
- **Link:** <https://github.com/cocrawler/cdx_toolkit>
- **Serve para:** Biblioteca/CLI para consultar índices CDX (Internet Archive e Common Crawl).
- **Avaliação:** Útil para cruzar a Wayback com o Common Crawl na mesma interface.
- **Cuidado:** Confirme o escopo atual do projeto na documentação.

### oduwsdl/MemGator

- **Tipo:** cli+server · **Linguagem:** Go · **Nível:** complementar · **Status:** a-verificar
- **Link:** <https://github.com/oduwsdl/MemGator>
- **Serve para:** Agregador Memento: consulta vários arquivos web ao mesmo tempo.
- **Avaliação:** Boa para obter uma segunda fonte de arquivamento independente da Wayback.
- **Cuidado:** Confirme a lista de arquivos suportados na documentação.

### ArchiveBox/ArchiveBox

- **Tipo:** self-hosted · **Linguagem:** Python · **Nível:** complementar · **Status:** a-verificar
- **Link:** <https://github.com/ArchiveBox/ArchiveBox>
- **Serve para:** Arquivamento web auto-hospedado, sob seu controle.
- **Avaliação:** Alternativa ao Save Page Now quando a página não deve ser pública.
- **Cuidado:** Exige operar e proteger sua própria instância.

### Common Crawl — índice de URLs

- **Tipo:** api · **Linguagem:** — · **Nível:** complementar · **Status:** a-verificar
- **Link:** <https://index.commoncrawl.org/>
- **Serve para:** Índice de URLs rastreadas pelo Common Crawl, fonte independente da Wayback.
- **Avaliação:** Corrobora existência de URLs sem depender do Internet Archive.
- **Cuidado:** Cobertura e granularidade diferem da Wayback; não são equivalentes.
