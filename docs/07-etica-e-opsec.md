# 07 · Ética e OPSEC

Este material é para **pesquisa, jornalismo, defesa e inteligência de ameaças autorizada**. Use apenas em dados de que você pode legitimamente tratar.

## OPSEC: o que você revela ao consultar

| Ação | O que pode vazar | Mitigação |
|---|---|---|
| **Save Page Now** | Cria uma captura **pública** da URL, que pode alertar o dono do site e fixa o conteúdo para todos | Só salve o que pode ser público; para páginas sensíveis, preserve localmente (captura de tela + HTML + hash) |
| Consultar a Wayback | Seu IP e `User-Agent` chegam ao Internet Archive | Use a rede/identidade apropriada à sensibilidade da investigação |
| Abrir capturas renderizadas | Scripts arquivados executam no seu navegador | Prefira `id_` (bruto) ou um ambiente isolado; não abra capturas de alvos hostis no seu navegador principal |
| Baixar arquivos (`.exe`, `.zip`, `.js`) | Malware histórico fica preservado | Trate como amostra: VM isolada, nunca execute |
| Reconstrução local de sites | Credenciais e segredos antigos podem aparecer | Não use credenciais encontradas; reporte vazamento conforme o caso |

## Limites

- **Dados pessoais.** Mesmo públicos e arquivados, aplicam-se leis de proteção de dados (LGPD, GDPR) e o princípio da necessidade. Colete o mínimo; proteja o que coletar.
- **Remoção e esquecimento.** Pessoas podem ter pedido remoção do conteúdo. Se o arquivo o oculta, não tente contornar por outro caminho sem justificativa legítima.
- **Credenciais e segredos** achados em capturas antigas: não teste, não reutilize. Notifique o responsável quando cabível.
- **Termos de uso e limites de taxa.** Respeite os termos do Internet Archive e as respostas 429.
- **Proporcionalidade.** O benefício da investigação deve justificar a exposição de quem está nos dados.

## Antes de publicar

- [ ] Cada afirmação aponta para uma ficha de evidência.
- [ ] Observação, inferência e hipótese estão rotuladas ([05](05-cadeia-de-evidencia.md)).
- [ ] Hipóteses alternativas e lacunas de cobertura estão declaradas ([06](06-psicologia-investigativa.md)).
- [ ] Dados pessoais foram minimizados ou removidos.
- [ ] Há base legal ou autorização para o trabalho.
