# 13 · Psicologia: o adversário que sabe que é arquivado, e o analista que lê

Complementa [06](06-psicologia-investigativa.md). Lá: vieses de quem analisa. Aqui: **engano deliberado** e **desgaste** do próprio analista.

## Parte A · O arquivo também é um campo de engano

Qualquer pessoa pode pedir ao arquivo que capture uma página, e um operador atento sabe que rastreadores existem. Consequências:

| Tática | O que parece | Contramedida |
|---|---|---|
| **Cloaking** | O servidor entrega conteúdo inocente ao rastreador e o golpe à vítima | Procure sinais de divergência: digest idêntico por anos num site "ativo", páginas vazias, `User-Agent` condicional no código |
| **Plantio de capturas** | Alguém salva uma página (própria ou forjada) para criar uma "prova" datada | Procure capturas isoladas surgidas sem tráfego anterior; exija corroboração independente |
| **Limpeza** | Remoção ou bloqueio de capturas comprometedoras | Ausência de captura não é ausência de existência; busque outros arquivos (Memento, Common Crawl) |
| **Isca de atribuição (false flag)** | Idioma, fuso, metadados e nomes plantados para sugerir outro autor | Trate artefatos "culturais" como fracos; privilegie pivôs técnicos consistentes |
| **Reaproveitamento de domínio** | Domínio com bom histórico reutilizado para golpe | Procure descontinuidade (playbook 4 em [11](11-playbooks-ti.md)) |

Regra: **o adversário controla o que o rastreador viu.** A captura é testemunho de um servidor possivelmente hostil.

## Parte B · Hábitos do adversário (e o perigo de atribuir por eles)

Operadores deixam padrões: reuso de template, convenções de nome, horário de atividade, erros de OPSEC repetidos. Isso gera boas hipóteses de **agrupamento**; mas:

- **Padrão ≠ pessoa.** Muita gente copia as mesmas ferramentas e tutoriais.
- **Cuidado com o viés de agrupamento:** a mente adora unir casos parecidos. Liste explicitamente o que diferencia os casos que você uniu.
- **Atribuição é um gradiente**, não um veredicto: descreva o nível (atividade → cluster → ator) e o que falta para o próximo.

## Parte C · O analista como instrumento

Você também é um sistema com limites. Em trabalho prolongado com dados temporais e, às vezes, conteúdo perturbador:

| Risco | Sinal | Prática |
|---|---|---|
| **Fadiga decisória** | Aceitar "bom o bastante", pular o hash, confiar na primeira leitura | Blocos de 50–90 min, pausas reais; *checklist* ao fim de cada bloco |
| **Túnel** | Horas na mesma hipótese | "O que me faria desistir?"; troca de problema por 20 min; revisão por par |
| **Exposição a conteúdo nocivo** | Intrusão de imagens, irritabilidade, entorpecimento | Minimize exposição (miniaturas desligadas, sem som, texto antes de imagem); limite de tempo; conversar com colega ou profissional; **peça ajuda cedo** |
| **Paranoia ou hipervigilância** | Ver conexões em tudo | Sono, rotina, e a regra dos **dois pivôs independentes** como freio |
| **Comprometimento do ego** | Dificuldade de aceitar que errou | Normalize a correção: registre o erro e o aprendizado na ficha |

> Isso é higiene de trabalho, não tratamento. Se o trabalho com conteúdo perturbador estiver afetando seu sono, humor ou relações, procure um profissional de saúde mental.

## Prática semanal sugerida (15 minutos)

1. Releia uma conclusão sua com a pergunta: *qual evidência eu estaria ignorando se estivesse errado?*
2. Atualize a tabela de hipóteses alternativas.
3. Registre um erro ou quase-erro da semana, sem culpa.
