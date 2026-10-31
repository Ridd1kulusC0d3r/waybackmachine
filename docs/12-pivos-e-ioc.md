# 12 · Pivôs e IOCs extraídos de capturas

Um **pivô** é um dado que liga o objeto atual a outros. Um **IOC** é um indicador que se pode compartilhar. Um dado pode ser os dois, mas **nem todo pivô é um bom IOC**: um ID de analytics liga sites; não é "malicioso".

## Força do pivô

| Tipo | Extraído por `wb_extract.py` | Força | Por quê | Risco de falsa ligação |
|---|---|---|---|---|
| ID de analytics (`UA-`, `G-`, `GTM-`) | sim | **forte** | Pertence a uma conta | Template copiado com ID do autor; agências com conta única |
| AdSense (`pub-`) | sim | **forte** | Conta de monetização | Conta de agência |
| `.onion` v3 | sim | média | Identidade de serviço | Listas e diretórios que apenas citam |
| E-mail | sim | média | Contato/coleta | Contatos legítimos citados; e-mails descartáveis |
| Handle do Telegram | sim | média | Canal/conta | Citação por terceiros |
| Domínio | sim | média | Infraestrutura | CDNs, serviços compartilhados |
| IPv4 | sim (privados descartados) | fraca | Hospedagem | Hospedagem compartilhada; IPs reutilizados no tempo |
| URL | sim | fraca | Caminho específico | Muita volatilidade |
| Carteira BTC/ETH | candidata | fraca sem validação | Pode ser pivô financeiro | Regex acerta strings que não são endereços; valide checksum |

## Regras de uso

1. **Dois pivôs independentes** antes de ligar dois objetos; um só é pista, não ligação.
2. **Consistência temporal**: o identificador estava no site *no mesmo período* nos dois lados? `first_capture`/`last_capture` no CSV ajudam.
3. **Distinga autoria de compartilhamento.** Mesmo ID em dois sites pode significar mesma conta, mesma agência, ou template copiado.
4. **Contra-hipótese obrigatória**: escreva ao menos uma explicação inocente.
5. **Defang** em tudo que for compartilhado: `hxxps://evil[.]example`, `ana[@]alvo[.]test`.

## Esquema sugerido para compartilhar

Um registro por indicador, sempre com proveniência:

```json
{
  "type": "ga_universal",
  "value": "UA-1234567-1",
  "role": "pivot",
  "confidence": "moderada",
  "first_capture": "20190101000000",
  "last_capture": "20200101000000",
  "source": "https://web.archive.org/web/20190101000000/http://alvo.test/",
  "sha256_of_capture": "…",
  "collected_at_utc": "2026-10-23T12:00:00Z",
  "tlp": "TLP:CLEAR",
  "notes": "Observado em 2 capturas; sem corroboração independente."
}
```

`wb_extract.py --format json` já entrega `summary` (valor → arquivos) e `files` (com SHA-256); preencher `confidence`, `role` e `notes` é trabalho **analítico**, do humano.

## Fluxo

```text
raw/*.bin  ──wb_extract.py──▶  iocs.json (candidatos)
                                   │  triagem humana: descartar ruído, ligar com 2+ pivôs
                                   ▼
                      registros com confiança + proveniência  ──▶  relatório / compartilhamento
```
