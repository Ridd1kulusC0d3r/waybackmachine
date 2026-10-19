# 06 · Psicologia para investigação digital

Dados temporais convidam a histórias: a linha do tempo "faz sentido" cedo demais. Esta página lista os vieses que mais distorcem o trabalho com arquivos web, com uma **contramedida operacional** para cada um.

| Viés | Como aparece com a Wayback | Contramedida |
|---|---|---|
| **Ancoragem** | A primeira captura vira "a data de criação" e todo o resto se ajusta a ela | Escreva "observada pela 1ª vez em…" e liste o que impede datas anteriores |
| **Viés de confirmação** | Você só abre as capturas que sustentam a hipótese | Defina, **antes**, o que contradiria a hipótese; procure isso primeiro |
| **Viés de sobrevivência** | O que foi arquivado parece "o que existiu" | Estime a cobertura (quantas capturas? lacunas longas?) e declare-a |
| **Ilusão de padrão (apofenia)** | Dois picos de capturas "coincidem" com um evento | Teste contra o acaso: compare com a frequência geral do domínio |
| **Falácia narrativa** | Encadeia mudanças numa história causal elegante | Separe sequência (A antes de B) de causa (A causou B) |
| **Excesso de confiança** | "Digest diferente, logo houve edição relevante" | Confirme com diff; digest muda por banners, contadores, tokens |
| **Efeito halo / autoridade** | Confiar mais porque a fonte é "o Internet Archive" | O arquivo é confiável quanto à *observação*, não quanto ao *conteúdo* |
| **Viés retrospectivo** | "Era óbvio" depois de saber o desfecho | Anote as hipóteses **antes** de abrir a captura seguinte |
| **Custo afundado** | Defender uma tese após horas investidas | Marcos de revisão: a cada fase, "o que me faria desistir desta linha?" |

## Hábitos de higiene analítica

1. **Hipóteses concorrentes (ACH simplificada).** Liste ≥ 3 explicações; para cada evidência marque se é consistente, inconsistente ou neutra com cada uma. Valem mais as evidências que **discriminam** hipóteses.
2. **Registre a incerteza em palavras e em números.** Use uma escala fixa e curta (ex.: baixa / moderada / alta) com critérios escritos, o mesmo vocabulário no relatório inteiro.
3. **Pré-registro leve.** Antes de coletar, escreva em 3 linhas: pergunta, o que contaria a favor, o que contaria contra.
4. **Revisão por par (red team de 15 min).** Peça a alguém que tente derrubar a conclusão, ou faça você mesmo como "advogado do diabo" em outro dia.
5. **Fadiga e ritmo.** Coletas longas pioram o julgamento. Pause antes de concluir; escreva a conclusão no dia seguinte.
6. **Separe coleta de interpretação.** Primeiro gere os artefatos brutos; só depois interprete. Facilita auditoria.

## Pessoas por trás dos dados

Se a investigação envolve indivíduos, lembre que o arquivo preserva o que alguém quis esconder ou já deixou de ser verdade. Veja [07-etica-e-opsec.md](07-etica-e-opsec.md) antes de expor qualquer pessoa.
