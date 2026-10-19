# 04 · Quatro exercícios

Cada exercício termina com um **artefato** e uma **frase de conclusão calibrada** (o que dá para afirmar, e com que grau de confiança).

---

## Exercício 1 · Recuperar uma página removida

**Objetivo:** localizar e salvar o conteúdo de uma página que não existe mais no ar.

1. Confirme que está fora do ar (registre o status atual e o instante da checagem).
2. Liste capturas: `python scripts/wb_cdx.py URL --out out/e1.csv`.
3. Escolha capturas com `statuscode` 200; evite as de 3xx/404 como fonte de conteúdo.
4. Abra com `id_` (conteúdo bruto) e calcule o SHA-256 do que salvar.
5. Preencha a [ficha de evidência](../templates/ficha-de-evidencia.md).

**Artefato:** HTML bruto + ficha. **Armadilha:** a captura "mais recente" pode já ser uma página de erro ou de domínio estacionado.

---

## Exercício 2 · Inventariar as URLs de um domínio

**Objetivo:** mapear superfície histórica (seções, subdomínios, arquivos, parâmetros).

1. `python scripts/wb_cdx.py dominio.com --match domain --fields timestamp,original,statuscode,mimetype --out out/e2.csv`
2. Compare com `waybackurls` e `gau --providers wayback`: as listas batem? Por quê?
3. Agrupe por extensão, por subdomínio e por primeiro segmento do caminho.
4. Marque o que **sumiu** (só aparece em capturas antigas).

**Artefato:** tabela de inventário com a **fonte** de cada URL. **Armadilha:** misturar provedores (`gau` padrão inclui Common Crawl, OTX, URLScan) e atribuir tudo à Wayback.

---

## Exercício 3 · Comparar versões

**Objetivo:** descobrir *o que* mudou entre duas capturas.

1. Gere o CSV e rode `python scripts/wb_timeline.py out/e1.csv` para achar **pontos de mudança**.
2. Para cada ponto, `python scripts/wb_diff.py URL TS_ANTERIOR TS_NOVO`.
3. Separe mudança **de conteúdo** de mudança **de template** (menu, rodapé, scripts de analytics).
4. Anote o **intervalo** em que a mudança ocorreu: entre `TS_ANTERIOR` e `TS_NOVO`, nunca "em TS_NOVO".

**Artefato:** diff anotado. **Armadilha:** digest diferente ≠ mudança relevante; um contador de visitas muda o hash.

---

## Exercício 4 · Linha do tempo com evidências

**Objetivo:** consolidar tudo em relatório que outra pessoa consiga refazer.

1. Parta do [modelo de relatório](../templates/relatorio-timeline.md).
2. Cada evento da linha do tempo cita: captura (URL completa com timestamp), hash, o que a captura mostra e **o que não mostra**.
3. Busque **uma fonte independente** para os marcos mais importantes (outro arquivo, registro público, cache de buscador).
4. Redija as conclusões com graus de confiança (ver [06](06-psicologia-investigativa.md)) e liste hipóteses alternativas que você **não** conseguiu descartar.

**Artefato:** relatório com anexos (CSV + `.meta.json` + brutos + fichas).
