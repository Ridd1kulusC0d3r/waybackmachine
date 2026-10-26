# Identidade visual · WaybackAtlas

Mesma família visual do [LLmInjection](https://github.com/Ridd1kulusC0d3r/LLmInjection): a **mesa de analista**. Papel, tinta e **uma só cor de sinal**. Os dois projetos devem parecer da mesma bancada: o LLmInjection mostra *o que foi injetado*; o WaybackAtlas mostra *o que foi arquivado*.

## Conceito

O motivo do LLmInjection é uma **página de documento com tarjas de redação**, uma delas em cor de sinal ("conteúdo injetado, trate como dado"). Aqui o motivo vira uma **pilha de capturas**: várias versões da mesma página, uma sobre a outra. Na página da frente, a tarja de sinal marca a **observação arquivada**, com a legenda que resume o método do projeto:

> **OBSERVAÇÃO ARQUIVADA. NÃO É DATA DE PUBLICAÇÃO.**

Tom de voz: **técnico, sóbrio, calibrado**. "Evidência acima de hype." Frases curtas, afirmações com grau de confiança, nunca sensacionalista.

## Arquivos

| Arquivo | Uso |
|---|---|
| [`assets/banner-light.svg`](../assets/banner-light.svg) / [`banner-dark.svg`](../assets/banner-dark.svg) | Topo do README (alterna por tema via `<picture>`) |
| [`assets/logo-light.svg`](../assets/logo-light.svg) / [`logo-dark.svg`](../assets/logo-dark.svg) | Avatar, favicon, ícone |
| [`assets/social-preview.png`](../assets/social-preview.png) | Imagem de compartilhamento 1280×640 |
| [`assets/tokens.css`](../assets/tokens.css) | **Fonte única** da paleta e tipografia |

Os SVGs usam as cores de `tokens.css` embutidas (SVG em `<img>` não lê variáveis CSS). Ao mudar um token, atualize os SVGs com o mesmo valor.

## Paleta

| Token | Claro | Escuro | Papel |
|---|---|---|---|
| `--paper` | `#f3f0e8` | `#131210` | Fundo |
| `--paper-2` | `#ebe7dc` | `#1b1915` | Superfícies, capturas de trás |
| `--page` | `#fbf9f3` | `#1b1915` | A página em destaque |
| `--ink` | `#17150f` | `#ece8dd` | Texto, linhas e tarjas pretas |
| `--ink-2` | `#4a463c` | `#b9b4a6` | Texto secundário |
| `--rule` | `#cfc9ba` | `#37332b` | Linhas finas, barras de "texto" |
| `--signal` | `#b43c0e` | `#f0885a` | **Única cor de acento** |

**Regra do sinal:** uma vez por composição, no elemento que o leitor deve notar (a observação arquivada, um alerta, o link ao passar o mouse). Sinal em tudo vira ruído.

## Tipografia

- **Título e marca:** Georgia bold, tracking −0,02 em (`-2` no banner); subtítulo em Georgia *itálico*.
- **Rótulos:** monoespaçada em **CAIXA-ALTA**, negrito, espaçamento largo (`letter-spacing` 2 px), 11–12 px. Ex.: `WAYBACKATLAS / OSINT TEMPORAL EM ARQUIVOS WEB`, `TLP:CLEAR`.
- **Corpo:** fonte do sistema (sans). **Código e hashes:** mono.

## Linguagem visual

- **Cantos retos.** Nenhum raio, nenhuma sombra, nenhum degradê.
- **Linhas finas de tinta** (1 px) separam seções; o sinal aparece em traços curtos de 4 px sob o título.
- **Cabeçalho de documento:** linha de rótulo mono com a classificação (`TLP:CLEAR`) à direita, filete de tinta embaixo.
- **Tarjas:** barras cinza (`--rule`) como texto, barra de tinta como redação, barra de sinal como achado.
- Selos de status (shields) com `labelColor=17150f` e `color=b43c0e`.

## Regenerar os assets

Logos, banners e social preview saem do mesmo gabarito, para manter as variantes consistentes. O social preview, a partir do HTML:

```bash
make social CHROME=/caminho/do/chromium   # requer Chromium e ImageMagick
```

Depois, em *Settings → General → Social preview* do GitHub, envie `assets/social-preview.png`.

## Tópicos sugeridos

`osint` · `wayback-machine` · `internet-archive` · `threat-intelligence` · `cdx-api` · `digital-forensics` · `python`
