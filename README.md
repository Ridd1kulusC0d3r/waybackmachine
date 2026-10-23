<div align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img src="assets/banner-dark.svg" alt="wayback/atlas — mapa de ferramentas e guia de campo para OSINT temporal" width="100%">
  </picture>
</div>

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
| Playbooks de inteligência de ameaças (6 cenários) | [docs/08-playbooks-ti.md](docs/08-playbooks-ti.md) |
| Pivôs e IOCs: força, regras e esquema de compartilhamento | [docs/09-pivos-e-ioc.md](docs/09-pivos-e-ioc.md) |
| Adversário que engana o arquivo · desgaste do analista | [docs/10-psicologia-do-adversario-e-do-analista.md](docs/10-psicologia-do-adversario-e-do-analista.md) |
| Receitas de Shell (`awk`, `sort`, `comm`, `jq`) para a CDX | [docs/11-shell-cookbook.md](docs/11-shell-cookbook.md) |
| Glossário e perguntas frequentes | [docs/12-glossario-e-faq.md](docs/12-glossario-e-faq.md) |

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
<!-- tools:end -->

### Complementares (fontes independentes e alternativas)

Úteis para **corroborar** com outra fonte ou preservar sem publicar. Status `a-verificar`: sugeridas sem checagem da documentação atual.

<!-- extra:begin -->
| Repositório | Para que serve | Avaliação |
|---|---|---|
| [jsvine/waybackpack](https://github.com/jsvine/waybackpack) | Baixa o histórico de capturas de uma página da Wayback Machine. | **Alternativa leve para guardar todas as versões de uma única URL.** |
| [cocrawler/cdx_toolkit](https://github.com/cocrawler/cdx_toolkit) | Biblioteca/CLI para consultar índices CDX (Internet Archive e Common Crawl). | **Útil para cruzar a Wayback com o Common Crawl na mesma interface.** |
| [oduwsdl/MemGator](https://github.com/oduwsdl/MemGator) | Agregador Memento: consulta vários arquivos web ao mesmo tempo. | **Boa para obter uma segunda fonte de arquivamento independente da Wayback.** |
| [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | Arquivamento web auto-hospedado, sob seu controle. | **Alternativa ao Save Page Now quando a página não deve ser pública.** |
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
├── docs/                     ← 12 guias: fundamentos → CDX → trilha → exercícios → evidência →
│                               psicologia → ética → playbooks TI → pivôs/IOC → adversário → shell → FAQ
├── scripts/                  ← wb_cdx · timeline · inventory · fetch · extract · diff · build_catalog
│   └── sh/                   ← wb-pipeline · wb-cdx · wb-verify
├── templates/                ← ficha de evidência e relatório de cronologia
├── tests/                    ← testes (servidor Wayback simulado)
└── .github/                  ← CI, templates de issue e PR
```

Identidade visual e uso dos assets: [docs/identidade-visual.md](docs/identidade-visual.md). Contribuições: [CONTRIBUTING.md](CONTRIBUTING.md). Licença: [MIT](LICENSE).
