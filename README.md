<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="WaybackAtlas: mapa e guia de campo para OSINT temporal na Wayback Machine" width="100%">
  </picture>
</div>

<p align="center">
  <a href="https://github.com/Ridd1kulusC0d3r/waybackmachine/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Ridd1kulusC0d3r/waybackmachine/ci.yml?style=flat-square&label=CI&labelColor=17150f&color=b43c0e" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Ridd1kulusC0d3r/waybackmachine?style=flat-square&labelColor=17150f&color=4a463c" alt="MIT"></a>
  <img src="https://img.shields.io/badge/modo-evid%C3%AAncia%20primeiro-4a463c?style=flat-square&labelColor=17150f" alt="Evidência primeiro">
  <a href="https://github.com/Ridd1kulusC0d3r/LLmInjection"><img src="https://img.shields.io/badge/fam%C3%ADlia-LLmInjection-4a463c?style=flat-square&labelColor=17150f" alt="Família LLmInjection"></a>
</p>

<p align="center">
  <b>Mapa</b> das melhores ferramentas da Wayback Machine · <b>Guia</b> de uso passo a passo · <b>Método</b> para transformar capturas em evidência
</p>

---

## Por que existe

A Wayback Machine é um arquivo de **observações**: ela diz *quando um rastreador viu algo*, não *quando algo foi publicado*. Este repositório junta, num lugar só:

1. **Um mapa** das ferramentas que consultam ou recuperam esse arquivo (CLI, bibliotecas Python, extensão, API).
2. **Um guia** com trilha de estudo, exercícios e receitas prontas.
3. **Um método** de cadeia de evidência e higiene analítica, porque em investigação digital o maior risco não é a ferramenta, é a conclusão apressada.

> **Transparência:** as ferramentas foram selecionadas pelas funcionalidades **documentadas**. Nenhuma foi executada na curadoria inicial (status `documentado` no [catálogo](docs/catalogo.md)). Os scripts em `scripts/` têm testes automatizados contra um servidor simulado; contra a Wayback real, valide no seu ambiente.

## Comece por aqui

Para OSINT, a combinação de partida é **CDX API + waymore + uma biblioteca Python**: descobrir URLs antigas, recuperar conteúdo e montar análise temporal.

| Se você quer… | Vá para |
|---|---|
| Entender o que a Wayback prova (e o que não prova) | [docs/01-fundamentos.md](docs/01-fundamentos.md) |
| Consultar o índice de capturas | [docs/02-cdx-api.md](docs/02-cdx-api.md) |
| Uma ordem de estudo | [docs/03-trilha-de-estudo.md](docs/03-trilha-de-estudo.md) |
| Praticar | [docs/04-exercicios.md](docs/04-exercicios.md) |
| Documentar achados com rigor | [docs/05-cadeia-de-evidencia.md](docs/05-cadeia-de-evidencia.md) |
| Evitar vieses que sabotam a investigação | [docs/06-psicologia-investigativa.md](docs/06-psicologia-investigativa.md) |
| Limites éticos e de OPSEC | [docs/07-etica-e-opsec.md](docs/07-etica-e-opsec.md) |
| Playbooks de inteligência de ameaças (6 cenários) | [docs/11-playbooks-ti.md](docs/11-playbooks-ti.md) |
| Pivôs e IOCs: força, regras e esquema de compartilhamento | [docs/12-pivos-e-ioc.md](docs/12-pivos-e-ioc.md) |
| Adversário que engana o arquivo · desgaste do analista | [docs/13-psicologia-do-adversario-e-do-analista.md](docs/13-psicologia-do-adversario-e-do-analista.md) |
| Receitas de Shell (`awk`, `sort`, `comm`, `jq`) para a CDX | [docs/14-shell-cookbook.md](docs/14-shell-cookbook.md) |
| Glossário e perguntas frequentes | [docs/15-glossario-e-faq.md](docs/15-glossario-e-faq.md) |

## Curadoria ampliada

**15 ferramentas e referências no mapa principal (+ 4 complementares) · 13 guias externos · 6 laboratórios avançados · 6 playbooks de TI.**

| Próximo objetivo | Material |
|---|---|
| Escolher entre Wayback, captura local e outro acervo | [Ecossistema e preservação](docs/08-ecossistema-e-preservacao.md) |
| Praticar hipóteses, cronologia e comparação | [Laboratórios avançados](docs/09-laboratorios-avancados.md) |
| Resolver falhas de coleta e replay | [Diagnóstico e qualidade](docs/10-diagnostico-e-qualidade.md) |
| Registrar uma comparação reproduzível | [Ficha de comparação](templates/comparacao-temporal.md) |

Os oito recursos iniciais focam Wayback e descoberta de URLs; os sete adicionais cobrem preservação, replay, WARC e um acervo complementar. São referências documentais, sem incorporação de código externo.

## Mapa de repositórios

<!-- tools:begin -->
| Repositório | Para que serve | Avaliação |
|---|---|---|
| [xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore) | Descobre URLs em diferentes fontes e baixa respostas arquivadas da Wayback Machine. | **Primeira escolha para investigação exploratória: permite pesquisar o conteúdo recuperado, além de listar endereços.** |
| [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) | Recebe domínios e retorna URLs conhecidas pela Wayback, incluindo subdomínios. | **Melhor opção simples para pipelines: pequena e direta.** |
| [lc/gau](https://github.com/lc/gau) | Coleta URLs de Wayback, Common Crawl, OTX e URLScan; oferece filtros e saída JSON. | **Boa para ampliar cobertura.** |
| [akamhy/waybackpy](https://github.com/akamhy/waybackpy) | Biblioteca Python e CLI para Availability, CDX e Save Page Now. | **Boa porta de entrada para automação, com exemplos acessíveis.** |
| [edgi-govdata-archiving/wayback](https://github.com/edgi-govdata-archiving/wayback) | Cliente Python para pesquisar e recuperar capturas históricas, chamadas mementos. | **Candidata para pipelines de pesquisa temporal; documentação dedicada à busca e recuperação.** |
| [hartator/wayback-machine-downloader](https://github.com/hartator/wayback-machine-downloader) | Recupera arquivos arquivados, com filtros por período, URL e extensão. | **Útil para reconstrução local.** |
| [internetarchive/wayback-machine-webextension](https://github.com/internetarchive/wayback-machine-webextension) | Extensão oficial para salvar páginas e acessar capturas antigas e recentes. | **Melhor começo sem programação, especialmente durante pesquisa manual.** |
| [internetarchive/wayback — CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) | Código e documentação do serviço de consulta ao índice de capturas. | **Referência técnica essencial: ajuda a entender os dados que as outras ferramentas consultam.** |
| [webrecorder/pywb](https://github.com/webrecorder/pywb) | Reproduz e grava arquivos web em uma infraestrutura própria. | **Escolha para servir coleções WARC e estudar replay.** |
| [webrecorder/warcio](https://github.com/webrecorder/warcio) | Lê e escreve registros WARC e lê ARC em streaming. | **Útil para inspecionar metadados e extrair respostas de arquivos locais.** |
| [webrecorder/browsertrix-crawler](https://github.com/webrecorder/browsertrix-crawler) | Realiza captura com navegador em um contêiner Docker. | **Opção para capturas reproduzíveis de páginas que dependem de navegador.** |
| [webrecorder/archiveweb.page](https://github.com/webrecorder/archiveweb.page) | Grava navegação no navegador para construir um arquivo web. | **Útil em preservação manual de páginas interativas.** |
| [webrecorder/replayweb.page](https://github.com/webrecorder/replayweb.page) | Reproduz arquivos web diretamente no navegador. | **Bom para revisar e compartilhar coleções preservadas em formatos suportados.** |
| [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | Organiza um arquivo próprio de URLs e salva conteúdo em múltiplos formatos. | **Útil para coleções de pesquisa e preservação recorrente.** |
| [arquivo/pwa-technologies](https://github.com/arquivo/pwa-technologies) | Documenta tecnologias e APIs do Arquivo.pt, incluindo pesquisa de arquivos web. | **Fonte complementar para comparar cobertura com a Wayback.** |
<!-- tools:end -->

### Complementares (fontes independentes e alternativas)

Úteis para **corroborar** com outra fonte ou preservar sem publicar. Três tiveram o README lido em 2026-10-26; o Common Crawl segue `a-verificar` (site inacessível na checagem). Manutenção ativa não foi auditada.

<!-- extra:begin -->
| Repositório | Para que serve | Avaliação |
|---|---|---|
| [jsvine/waybackpack](https://github.com/jsvine/waybackpack) | Baixa todas as capturas de uma URL (ou só lista os timestamps com --list). | **Alternativa leve para guardar todas as versões de uma única URL.** |
| [cocrawler/cdx_toolkit](https://github.com/cocrawler/cdx_toolkit) | Biblioteca e CLI (cdxt) para consultar índices CDX do Common Crawl e da Wayback Machine e extrair páginas para WARC, jsonl ou csv. | **Útil para cruzar a Wayback com o Common Crawl na mesma interface.** |
| [oduwsdl/MemGator](https://github.com/oduwsdl/MemGator) | Agregador Memento em Go (CLI e servidor): consulta vários arquivos web e devolve TimeMap/TimeGate em link, JSON ou CDXJ. | **Boa para obter uma segunda fonte de arquivamento independente da Wayback.** |
| [Common Crawl — índice de URLs](https://index.commoncrawl.org/) | Índice de URLs rastreadas pelo Common Crawl, fonte independente da Wayback. | **Corrobora existência de URLs sem depender do Internet Archive.** |
<!-- extra:end -->

Fichas completas e filtro por papel (descobrir, recuperar, analisar, preservar): [docs/catalogo.md](docs/catalogo.md). Dados-fonte: [`data/tools.json`](data/tools.json) — para adicionar uma ferramenta, edite o JSON e rode `make catalog`.

### Qual escolher?

```text
Sem programar, pesquisa manual ........ extensão oficial
Lista de URLs para um pipeline ........ waybackurls (simples) · gau (mais fontes)
Explorar e ler o conteúdo recuperado .. waymore
Automatizar em Python ................. waybackpy · wayback (EDGI)
Reconstruir um site localmente ........ wayback-machine-downloader (delimite o período!)
Entender o que está por baixo ......... CDX Server (referência)
```

## Trilha de estudo

<!-- guides:begin -->
| Ordem | Guia | O que aprender |
|---|---|---|
| 1 | [Using the Wayback Machine — Internet Archive](https://help.archive.org/help/using-the-wayback-machine/) | Navegação, capturas e limitações do arquivamento. |
| 2 | [Save Pages in the Wayback Machine](https://archivesupport.zendesk.com/hc/en-us/articles/360001513491-Save-Pages-in-the-Wayback-Machine) | Preservação de páginas com Save Page Now e extensões. |
| 3 | [Wayback Machine APIs — documentação oficial](https://archive.org/help/wayback_api.php) | Consulta programática de disponibilidade de capturas. |
| 4 | [CDX Server API — documentação oficial](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) | Enumeração, datas, filtros, campos, deduplicação e paginação. |
| 5 | [Waybackpy — documentação](https://akamhy.github.io/waybackpy/) | Uso das APIs por Python e terminal. |
| 6 | [Wayback (EDGI) — documentação](https://wayback.readthedocs.io/en/stable/) | Pesquisa e recuperação de capturas em scripts. |
| 7 | [pywb — documentação](https://pywb.readthedocs.io/en/latest/) | Coleções locais, reprodução e gravação de arquivos web. |
| 8 | [warcio — guia do mantenedor](https://github.com/webrecorder/warcio) | Registros WARC/ARC, cabeçalhos e leitura em streaming. |
| 9 | [Browsertrix Crawler — guia do projeto](https://github.com/webrecorder/browsertrix-crawler) | Captura automatizada com navegador e Docker. |
| 10 | [ArchiveWeb.page — guia do projeto](https://github.com/webrecorder/archiveweb.page) | Preservação manual de navegação. |
| 11 | [ReplayWeb.page — documentação](https://replayweb.page/docs/) | Abrir e revisar arquivos web no navegador. |
| 12 | [Arquivo.pt — APIs](https://github.com/arquivo/pwa-technologies/wiki/APIs) | Pesquisa complementar em outro acervo. |
| 13 | [ArchiveBox — documentação](https://docs.archivebox.io/latest/) | Organização e configuração de um arquivo próprio. |
<!-- guides:end -->

Material do Internet Archive ou dos próprios mantenedores. Versão comentada em [docs/03-trilha-de-estudo.md](docs/03-trilha-de-estudo.md).

## Três exemplos para começar

**1. Consultar o índice de uma página, preservando datas e metadados**

```bash
curl -G 'https://web.archive.org/cdx/search/cdx' \
  --data-urlencode 'url=example.com/pagina' \
  --data 'output=json' \
  --data 'fl=timestamp,original,statuscode,mimetype,digest'
```

Mantenha todas as capturas no primeiro passe: deduplicar cedo pode esconder repetições relevantes.

**2. Listar URLs históricas de um domínio**

```bash
go install github.com/tomnomnom/waybackurls@latest
printf '%s\n' 'example.com' | waybackurls > urls.txt
```

**3. Usar o `gau` só com a Wayback (procedência clara)**

```bash
go install github.com/lc/gau/v2/cmd/gau@latest
gau --providers wayback --subs --o urls-wayback.txt example.com
```

## Scripts incluídos

Python 3.9+ só com biblioteca padrão; Shell em Bash. Sem dependências.

### Pipeline em um comando

```bash
scripts/sh/wb-pipeline.sh example.com --match domain --fetch 20
```

Gera `out/example.com/` com `cdx.csv` (+ `.meta.json`), `timeline.md`, `inventory.md`, e, com `--fetch N`, `raw/`, `manifest.jsonl`, `SHA256SUMS` e `iocs.json` (defanged). Tudo registrado em `RUN.log`. Depois, `scripts/sh/wb-verify.sh out/example.com` confere a integridade.

### Peças avulsas

| Script | Faz | Cuidado embutido |
|---|---|---|
| [`wb_cdx.py`](scripts/wb_cdx.py) | Consulta a CDX com paginação por `resumeKey` e retry | Grava a URL exata e o SHA-256 do resultado |
| [`wb_timeline.py`](scripts/wb_timeline.py) | Cronologia em Markdown com pontos de mudança | Lembra: 1ª captura ≠ data de publicação |
| [`wb_inventory.py`](scripts/wb_inventory.py) | Triagem de URLs por host, tipo e caminhos sensíveis | "Sinalizado ≠ exposto" |
| [`wb_fetch.py`](scripts/wb_fetch.py) | Baixa brutos (`id_`), retomável, com manifesto e `SHA256SUMS` | Registra a URL **final** (a Wayback pode servir a captura mais próxima) |
| [`wb_extract.py`](scripts/wb_extract.py) | Pivôs candidatos: analytics IDs, e-mails, domínios, IPs, `.onion`, Telegram, carteiras | Candidatos, não achados; `--defang`; cada item com hash do arquivo |
| [`wb_diff.py`](scripts/wb_diff.py) | Diff entre duas capturas brutas | Registra hashes dos dois lados |
| [`sh/wb-cdx.sh`](scripts/sh/wb-cdx.sh) | CDX em TSV só com `curl` | User-Agent identificável e retry |
| [`sh/wb-verify.sh`](scripts/sh/wb-verify.sh) | Verifica `SHA256SUMS` | Falha com código 1 se algo mudou |
| [`build_catalog.py`](scripts/build_catalog.py) | Gera tabelas do README e `docs/catalogo.md` | `--check` no CI |

## O cuidado analítico mais importante

**A primeira captura encontrada não determina a data de publicação.** Ela documenta uma observação arquivada; a página pode ter existido antes. Páginas e recursos podem estar incompletos ou vir de capturas diferentes. Inspecione conteúdo e timestamps antes de afirmar quando algo surgiu ou mudou.

## Quatro exercícios

**recuperar uma página removida → inventariar URLs de um domínio → comparar versões → produzir uma linha do tempo com evidências.** Esse caminho ensina mais do que instalar várias ferramentas que fazem a mesma coleta. Roteiros completos em [docs/04-exercicios.md](docs/04-exercicios.md).

## Estrutura do repositório

```text
.
├── README.md                 ← você está aqui
├── assets/                   ← identidade visual (logos, banners, tokens)
├── data/tools.json           ← fonte única do mapeamento de ferramentas
├── docs/                     ← 15 guias: fundamentos → CDX → trilha → exercícios → evidência → psicologia →
│                               ética → ecossistema → laboratórios → diagnóstico → playbooks TI →
│                               pivôs/IOC → adversário → shell → FAQ
├── scripts/                  ← wb_cdx · timeline · inventory · fetch · extract · diff · build_catalog
│   └── sh/                   ← wb-pipeline · wb-cdx · wb-verify
├── templates/                ← ficha de evidência e relatório de cronologia
├── tests/                    ← testes (servidor Wayback simulado)
└── .github/                  ← CI, templates de issue e PR
```

Identidade visual e uso dos assets: [docs/identidade-visual.md](docs/identidade-visual.md). Contribuições: [CONTRIBUTING.md](CONTRIBUTING.md). Licença: [MIT](LICENSE).
