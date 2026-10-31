# 11 · Playbooks de inteligência de ameaças com a Wayback

Seis cenários recorrentes. Cada um traz pergunta, passos, o que a evidência **prova e não prova**, e a armadilha típica. Todos assumem os cuidados de [05](05-cadeia-de-evidencia.md) e [07](07-etica-e-opsec.md) e usam os scripts do repositório. Variável usada nos exemplos: `ALVO=dominio.exemplo`.

> Capturas de infraestrutura maliciosa são **amostras**. Baixe com `id_`, nunca abra renderizado no navegador principal, trate tudo em ambiente isolado.

---

## 1. Linha do tempo de um domínio suspeito

**Pergunta:** desde quando este domínio é observado e o que ele serviu ao longo do tempo?

```bash
scripts/sh/wb-pipeline.sh "$ALVO" --match domain --fetch 30
# lê: out/$ALVO/timeline.md  inventory.md  iocs.json
```

1. Em `timeline.md`, ache **pontos de mudança** (digest/status). Mudança de 200 → 404 → 200 com conteúdo novo sugere reaproveitamento.
2. Em `inventory.md`, veja hosts e tipos; compare o primeiro host com os subdomínios surgidos depois.
3. Abra o diff dos pontos de mudança relevantes: `wb_diff.py URL TS_A TS_B`.

**Prova:** o que foi observado e quando. **Não prova:** data de registro, de ativação ou de uso malicioso. **Armadilha:** tratar a 1ª captura como "nascimento" do domínio ([06](06-psicologia-investigativa.md): ancoragem).

---

## 2. Recuperar kit de phishing ou página clonada

**Pergunta:** o que a página servia quando foi denunciada, e há artefatos reaproveitáveis?

1. Colete o índice **só da URL denunciada** e do diretório pai (`--match prefix`).
2. Priorize capturas próximas à data da denúncia, com status 200.
3. Baixe com `wb_fetch.py`; extraia pivôs com `wb_extract.py --defang`.
4. Olhe: destinos de formulário (`action=`), endpoints de exfiltração, e-mails de coleta, IDs de analytics, comentários HTML, nomes de arquivos de recursos.

**Prova:** o que o rastreador recebeu. **Não prova:** que a vítima viu o mesmo; **cloaking** é comum (o servidor mostra conteúdo inocente a rastreadores e o golpe a vítimas). Ausência de formulário na captura não inocenta.

---

## 3. Pivô por identificadores compartilhados

**Pergunta:** que outros domínios compartilham o mesmo operador ou template?

`wb_extract.py` devolve IDs de analytics (`UA-`, `G-`, `GTM-`), AdSense (`pub-`), e-mails, handles do Telegram e `.onion`. Cada um é um **pivô** para outras fontes (buscadores de código-fonte, serviços de varredura de URL, registros passivos de DNS). Tabela de pivôs e força em [12](12-pivos-e-ioc.md).

**Prova:** que dois sites exibiram o mesmo identificador. **Não prova:** mesmo operador. Templates vendidos, temas clonados e IDs copiados criam **falsas ligações**. Exija ≥ 2 pivôs independentes e consistência temporal.

---

## 4. Mudança de dono ou de propósito de um domínio

**Pergunta:** o domínio mudou de mãos (aquisição, expiração e recompra, parqueamento)?

1. Cronologia sem `collapse`; procure **lacunas** longas e depois mudança brusca de conteúdo, idioma ou tecnologia.
2. Compare rodapés, páginas de contato, política de privacidade e identificadores antes e depois.
3. Corrobore com registros externos (WHOIS histórico, certificados, DNS passivo).

**Prova:** descontinuidade de conteúdo. **Não prova:** troca de titular. Reformas e migrações também geram descontinuidade.

---

## 5. Triagem de exposição acidental (credenciais, backups, repositórios)

**Pergunta:** o domínio expôs arquivos sensíveis no passado?

1. Rode o pipeline e leia as **URLs sinalizadas** (`/.git/`, `.env`, `.sql`, `.bak`, `/admin`…).
2. Só consulte o **status e o tamanho** no índice; não baixe sem necessidade legítima.
3. Se encontrar segredo real: **não teste nem reutilize**. Notifique o responsável (canal de segurança, `security.txt`, CSIRT) e registre a ciência.

**Prova:** que uma URL com esse nome foi observada. **Não prova:** que o conteúdo era sensível (muitas dessas URLs respondem 404/403). Segredo antigo provavelmente já foi rotacionado, mas isso não é seu para presumir.

---

## 6. Impersonação de marca ao longo do tempo

**Pergunta:** quando um domínio parecido (typosquat) passou a imitar a marca, e como evoluiu?

1. Liste candidatos (variações do nome) e rode o índice de cada um.
2. Para os que têm capturas, compare logotipo, textos e formulários com o site legítimo no mesmo período.
3. Monte a cronologia comparativa: legítimo × impostor, **no mesmo eixo de tempo**.

**Prova:** semelhança observada em capturas datadas. **Não prova:** intenção; defesa de marca e paródia existem. Qualificação jurídica não é papel da evidência técnica.

---

## Como fechar qualquer playbook

- [ ] Ficha de evidência por item relevante, com hash.
- [ ] Observação / inferência / hipótese rotuladas.
- [ ] Ao menos uma **fonte independente** para os marcos principais.
- [ ] Hipóteses alternativas e lacunas de cobertura declaradas.
- [ ] Indicadores compartilhados em **defang**, com nível de confiança.
