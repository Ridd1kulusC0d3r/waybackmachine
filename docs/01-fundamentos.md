# 01 · Fundamentos: o que a Wayback prova

## O modelo mental

A Wayback Machine guarda **capturas** (*snapshots*, ou *mementos* no vocabulário do protocolo Memento). Cada captura é: *uma URL, vista por um rastreador (ou salva por alguém), num instante, com um conteúdo*.

| Ela prova | Ela **não** prova |
|---|---|
| Que **aquele conteúdo** foi observado **naquele instante** | Que a página foi publicada naquele instante |
| Que uma URL existia e respondia com certo status HTTP | Que a URL **não existia antes** da primeira captura |
| Que o conteúdo mudou entre duas capturas (digest diferente) | **Quando** mudou, nem **quem** mudou |
| — | Que a página renderizada é um estado que um visitante viu (recursos podem vir de capturas distintas) |

## Anatomia de uma URL da Wayback

```text
https://web.archive.org/web/20190314120000/http://example.com/pagina
                          └──── timestamp ───┘└──────── original ───────┘
```

`AAAAMMDDhhmmss`, em UTC. Timestamps parciais são aceitos e a Wayback redireciona para a captura mais próxima.

| Modificador | Exemplo | Efeito |
|---|---|---|
| *(nenhum)* | `/web/2019.../URL` | Página reescrita, com banner da Wayback |
| `id_` | `/web/2019...id_/URL` | **Conteúdo bruto**, como capturado. Use para hash e diff |
| `im_`, `js_`, `cs_` | `/web/2019...im_/URL` | Variante para imagem, script, CSS |
| `*` | `/web/*/example.com/*` | Interface de listagem de capturas por prefixo |

## Quatro portas de entrada

| Porta | Para quê | Detalhes |
|---|---|---|
| Interface web / extensão | Pesquisa manual | [Using the Wayback Machine](https://help.archive.org/help/using-the-wayback-machine/) |
| Availability API | "Existe captura perto desta data?" | [archive.org/help/wayback_api.php](https://archive.org/help/wayback_api.php) |
| **CDX Server API** | **Enumerar** todas as capturas, com filtros | [02-cdx-api.md](02-cdx-api.md) |
| Save Page Now | Criar uma captura agora | Publica a página: leia [07-etica-e-opsec.md](07-etica-e-opsec.md) |

## Limitações que mudam conclusões

- **Cobertura desigual.** Sites populares têm muitas capturas; páginas obscuras podem ter uma, ou nenhuma. Ausência de captura é ausência de **observação**.
- **Capturas incompletas.** HTML, imagens, CSS e JS são capturados em instantes diferentes; uma página "montada" pode ser uma colagem de épocas.
- **Conteúdo dinâmico e áreas autenticadas** raramente são preservados fielmente.
- **Exclusões e bloqueios.** Pedidos do dono do site e regras de exclusão podem tornar capturas inacessíveis. Isso pode apagar justamente o que você procura.
- **Redirecionamentos.** O status 301/302 também é um dado: registre-o em vez de seguir sem olhar.
- **Datas dentro do conteúdo** (rodapés, `Last-Modified`, metadados) são alegações do site, não do arquivo.

Regra prática: trate toda captura como **testemunho datado**, e corrobore com uma segunda fonte independente antes de afirmar.
