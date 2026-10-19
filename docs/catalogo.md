# Catálogo de ferramentas

> Gerado por `scripts/build_catalog.py` a partir de `data/tools.json`. Não edite à mão.

_Curadoria documental ampliada em 2026-10-19. Status documentado significa leitura da documentação, não execução nem auditoria de manutenção ou segurança. Recursos complementares preservam ou reproduzem arquivos web; não são necessariamente clientes da Wayback. Cada projeto mantém sua própria licença._

## Por papel na investigação

### Descobrir URLs

- [xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore) — Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine.
- [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) — Recebe domínios e retorna URLs conhecidas pela Wayback, incluindo subdomínios.
- [lc/gau](https://github.com/lc/gau) — Coleta URLs de Wayback, Common Crawl, OTX e URLScan; oferece filtros e saída JSON.
- [akamhy/waybackpy](https://github.com/akamhy/waybackpy) — Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) — Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- [internetarchive/wayback — CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) — Código e documentação do serviço de consulta ao índice de capturas.
- [arquivo/pwa-technologies](https://github.com/arquivo/pwa-technologies) — Documenta tecnologias e APIs do Arquivo.pt, incluindo pesquisa de arquivos web.

### Recuperar conteúdo

- [xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore) — Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine.
- [akamhy/waybackpy](https://github.com/akamhy/waybackpy) — Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) — Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- [hartator/wayback-machine-downloader](https://github.com/hartator/wayback-machine-downloader) — Recupera arquivos arquivados, com filtros por período, URL e extensão.
- [internetarchive/wayback-machine-webextension](https://github.com/internetarchive/wayback-machine-webextension) — Extensão oficial para salvar páginas e acessar capturas antigas e recentes.
- [webrecorder/pywb](https://github.com/webrecorder/pywb) — Reproduz e grava arquivos web em uma infraestrutura própria.
- [webrecorder/replayweb.page](https://github.com/webrecorder/replayweb.page) — Reproduz arquivos web diretamente no navegador.
- [arquivo/pwa-technologies](https://github.com/arquivo/pwa-technologies) — Documenta tecnologias e APIs do Arquivo.pt, incluindo pesquisa de arquivos web.

### Analisar no tempo

- [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) — Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- [webrecorder/warcio](https://github.com/webrecorder/warcio) — Lê e escreve registros WARC e lê ARC em streaming.
- [webrecorder/replayweb.page](https://github.com/webrecorder/replayweb.page) — Reproduz arquivos web diretamente no navegador.

### Preservar páginas

- [akamhy/waybackpy](https://github.com/akamhy/waybackpy) — Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- [internetarchive/wayback-machine-webextension](https://github.com/internetarchive/wayback-machine-webextension) — Extensão oficial para salvar páginas e acessar capturas antigas e recentes.
- [webrecorder/pywb](https://github.com/webrecorder/pywb) — Reproduz e grava arquivos web em uma infraestrutura própria.
- [webrecorder/browsertrix-crawler](https://github.com/webrecorder/browsertrix-crawler) — Realiza captura com navegador em um contêiner Docker.
- [webrecorder/archiveweb.page](https://github.com/webrecorder/archiveweb.page) — Grava navegação no navegador para construir um arquivo web.
- [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) — Organiza um arquivo próprio de URLs e salva conteúdo em múltiplos formatos.

### Referência técnica

- [internetarchive/wayback — CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) — Código e documentação do serviço de consulta ao índice de capturas.
- [webrecorder/warcio](https://github.com/webrecorder/warcio) — Lê e escreve registros WARC e lê ARC em streaming.
- [arquivo/pwa-technologies](https://github.com/arquivo/pwa-technologies) — Documenta tecnologias e APIs do Arquivo.pt, incluindo pesquisa de arquivos web.

## Fichas

### xnl-h4ck3r/waymore

- **Tipo:** cli · **Linguagem:** Python · **Status:** documentado
- **Link:** <https://github.com/xnl-h4ck3r/waymore>
- **Serve para:** Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine.
- **Avaliação:** Primeira escolha para investigação exploratória: permite pesquisar o conteúdo recuperado, além de listar endereços.
- **Cuidado:** Combina várias fontes; registre a origem de cada resultado.

### tomnomnom/waybackurls

- **Tipo:** cli · **Linguagem:** Go · **Status:** documentado
- **Link:** <https://github.com/tomnomnom/waybackurls>
- **Serve para:** Recebe domínios e retorna URLs conhecidas pela Wayback, incluindo subdomínios.
- **Avaliação:** Melhor opção simples para pipelines: pequena e direta.
- **Cuidado:** A listagem, sozinha, não é análise de conteúdo.

### lc/gau

- **Tipo:** cli · **Linguagem:** Go · **Status:** documentado
- **Link:** <https://github.com/lc/gau>
- **Serve para:** Coleta URLs de Wayback, Common Crawl, OTX e URLScan; oferece filtros e saída JSON.
- **Avaliação:** Boa para ampliar cobertura.
- **Cuidado:** Registre a origem dos resultados para não atribuir tudo à Wayback (use --providers wayback para isolar).

### akamhy/waybackpy

- **Tipo:** lib+cli · **Linguagem:** Python · **Status:** documentado
- **Link:** <https://github.com/akamhy/waybackpy>
- **Serve para:** Biblioteca Python e CLI para Availability, CDX e Save Page Now.
- **Avaliação:** Boa porta de entrada para automação, com exemplos acessíveis.
- **Cuidado:** Save Page Now publica a página no arquivo: avalie o impacto operacional antes de usar.
- **Documentação:** <https://akamhy.github.io/waybackpy/>

### edgi-govdata-archiving/wayback

- **Tipo:** lib · **Linguagem:** Python · **Status:** documentado
- **Link:** <https://github.com/edgi-govdata-archiving/wayback>
- **Serve para:** Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos.
- **Avaliação:** Candidata para pipelines de pesquisa temporal; documentação dedicada à busca e recuperação.
- **Cuidado:** Cliente de pesquisa/recuperação; a análise temporal fica por sua conta.
- **Documentação:** <https://wayback.readthedocs.io/en/stable/>

### hartator/wayback-machine-downloader

- **Tipo:** cli · **Linguagem:** Ruby · **Status:** documentado
- **Link:** <https://github.com/hartator/wayback-machine-downloader>
- **Serve para:** Recupera arquivos arquivados, com filtros por período, URL e extensão.
- **Avaliação:** Útil para reconstrução local.
- **Cuidado:** Por padrão reúne a última versão de cada arquivo, podendo misturar datas: delimite o período.

### internetarchive/wayback-machine-webextension

- **Tipo:** extension · **Linguagem:** JavaScript · **Status:** documentado
- **Link:** <https://github.com/internetarchive/wayback-machine-webextension>
- **Serve para:** Extensão oficial para salvar páginas e acessar capturas antigas e recentes.
- **Avaliação:** Melhor começo sem programação, especialmente durante pesquisa manual.
- **Cuidado:** Salvar uma página a torna pública no arquivo.

### internetarchive/wayback — CDX Server

- **Tipo:** api · **Linguagem:** Java · **Status:** documentado
- **Link:** <https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server>
- **Serve para:** Código e documentação do serviço de consulta ao índice de capturas.
- **Avaliação:** Referência técnica essencial: ajuda a entender os dados que as outras ferramentas consultam.
- **Cuidado:** Fonte primária; confira a documentação antes de confiar em resumos.
- **Documentação:** <https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md>

### webrecorder/pywb

- **Tipo:** lib+server · **Linguagem:** Python · **Status:** documentado
- **Link:** <https://github.com/webrecorder/pywb>
- **Serve para:** Reproduz e grava arquivos web em uma infraestrutura própria.
- **Avaliação:** Escolha para servir coleções WARC e estudar replay.
- **Cuidado:** Complementar: não equivale a baixar todo o acervo da Wayback.
- **Documentação:** <https://pywb.readthedocs.io/en/latest/>

### webrecorder/warcio

- **Tipo:** lib+cli · **Linguagem:** Python · **Status:** documentado
- **Link:** <https://github.com/webrecorder/warcio>
- **Serve para:** Lê e escreve registros WARC e lê ARC em streaming.
- **Avaliação:** Útil para inspecionar metadados e extrair respostas de arquivos locais.
- **Cuidado:** Não descobre capturas na Wayback; exige um arquivo de entrada.
- **Documentação:** <https://github.com/webrecorder/warcio>

### webrecorder/browsertrix-crawler

- **Tipo:** crawler · **Linguagem:** TypeScript · **Status:** documentado
- **Link:** <https://github.com/webrecorder/browsertrix-crawler>
- **Serve para:** Realiza captura com navegador em um contêiner Docker.
- **Avaliação:** Opção para capturas reproduzíveis de páginas que dependem de navegador.
- **Cuidado:** Captura o presente; interações, autenticação e recursos ausentes exigem validação.
- **Documentação:** <https://github.com/webrecorder/browsertrix-crawler>

### webrecorder/archiveweb.page

- **Tipo:** extension · **Linguagem:** JavaScript · **Status:** documentado
- **Link:** <https://github.com/webrecorder/archiveweb.page>
- **Serve para:** Grava navegação no navegador para construir um arquivo web.
- **Avaliação:** Útil em preservação manual de páginas interativas.
- **Cuidado:** Capturar a navegação não garante que todos os estados da aplicação foram preservados.
- **Documentação:** <https://github.com/webrecorder/archiveweb.page>

### webrecorder/replayweb.page

- **Tipo:** viewer · **Linguagem:** JavaScript · **Status:** documentado
- **Link:** <https://github.com/webrecorder/replayweb.page>
- **Serve para:** Reproduz arquivos web diretamente no navegador.
- **Avaliação:** Bom para revisar e compartilhar coleções preservadas em formatos suportados.
- **Cuidado:** Reproduzir um arquivo não confirma a veracidade do conteúdo nem completa recursos ausentes.
- **Documentação:** <https://replayweb.page/docs/>

### ArchiveBox/ArchiveBox

- **Tipo:** platform · **Linguagem:** Python · **Status:** documentado
- **Link:** <https://github.com/ArchiveBox/ArchiveBox>
- **Serve para:** Organiza um arquivo próprio de URLs e salva conteúdo em múltiplos formatos.
- **Avaliação:** Útil para coleções de pesquisa e preservação recorrente.
- **Cuidado:** Revise os extratores e integrações habilitados; o comportamento depende da configuração.
- **Documentação:** <https://docs.archivebox.io/latest/>

### arquivo/pwa-technologies

- **Tipo:** api+reference · **Linguagem:** Várias · **Status:** documentado
- **Link:** <https://github.com/arquivo/pwa-technologies>
- **Serve para:** Documenta tecnologias e APIs do Arquivo.pt, incluindo pesquisa de arquivos web.
- **Avaliação:** Fonte complementar para comparar cobertura com a Wayback.
- **Cuidado:** Acervo independente: não misture timestamps ou proveniência entre provedores.
- **Documentação:** <https://github.com/arquivo/pwa-technologies/wiki/APIs>
