# Identidade visual · wayback/atlas

## Conceito

**Atlas** = mapa; **wayback** = voltar no tempo. A marca combina um *anel de relógio aberto* (o tempo, com a interrupção onde fica o ponto de evidência) e **duas setas de retroceder** (⏪). O anel interno pontilhado em ciano remete aos *ticks* de uma linha do tempo; o ponto âmbar é a captura que importa.

Tom de voz: **técnico, sóbrio, preciso**. Frases curtas; afirmações calibradas; nunca sensacionalista.

## Logos

| Arquivo | Uso |
|---|---|
| [`assets/logo-dark.svg`](../assets/logo-dark.svg) | Fundos escuros, avatar da organização |
| [`assets/logo-light.svg`](../assets/logo-light.svg) | Fundos claros |
| [`assets/banner-dark.svg`](../assets/banner-dark.svg) / [`banner-light.svg`](../assets/banner-light.svg) | Topo do README (alternam por tema via `<picture>`) |
| `assets/social-preview.png` | Imagem de compartilhamento 1280×640 (ver abaixo) |

Área de respiro mínima: metade do diâmetro do anel. Tamanho mínimo: 24 px.

## Paleta

| Token | Hex | Papel |
|---|---|---|
| `--wa-ink` | `#0B1020` | Fundo escuro / texto em fundo claro |
| `--wa-deep` | `#121A33` | Superfícies elevadas |
| `--wa-paper` | `#F4EFE6` | Fundo claro / texto em fundo escuro |
| `--wa-amber` | `#F5A524` | Acento primário: **o ponto de evidência** (`#C77D00` em fundo claro) |
| `--wa-cyan` | `#3DDBD9` | Acento secundário: linha do tempo, dados (`#0E8F8D` em fundo claro) |
| `--wa-mute` | `#8A93B2` | Texto secundário (`#4A5273` em fundo claro) |
| `--wa-flag` | `#FF5C5C` | Alertas: viés, risco, dado não verificado |

Valores em [`assets/tokens.css`](../assets/tokens.css) (fonte única). As variantes "-d" existem para manter contraste legível em fundo claro.

**Regra do âmbar:** use-o uma vez por composição, no elemento que o leitor deve notar. Âmbar em tudo é ruído.

## Tipografia

Monoespaçada, para casar com terminal e hashes: `ui-monospace, "JetBrains Mono", Menlo, Consolas, monospace`. Título em peso 700, corpo em 400.

## Linguagem visual

- **Grade** de 32 px em linhas finas, como papel milimetrado de mapa.
- **Régua de capturas**: traços verticais de alturas variadas sobre uma linha; um deles destacado em âmbar.
- Ícones de linha, cantos arredondados, traço 3–7 px conforme o tamanho.

## Social preview

Gerada a partir do banner. Para regenerar (requer Chromium via Playwright ou similar):

```bash
make social
```

Depois, em *Settings → General → Social preview* do GitHub, envie `assets/social-preview.png`.

## Tópicos sugeridos para o repositório

`osint` · `wayback-machine` · `internet-archive` · `threat-intelligence` · `cdx-api` · `digital-forensics` · `python`
