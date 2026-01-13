# 🔬 AUDITORIA ERIC EVANS: Organização do LORE

**Data:** 13/01/2026 às 10:07  
**Auditor:** Eric Evans (DDD/SSOT)  
**Questão:** LORE deve ir para `templates/global/`? O que é global vs ciclo-específico?

---

## ANÁLISE DOS ARQUIVOS LORE

| Arquivo | Linhas | Escopo Atual | Análise |
|---------|--------|--------------|---------|
| `north_star.yaml` | 404 | **GLOBAL** | ✅ Define os 4 ciclos, propósito, princípios. Claramente GLOBAL. |
| `guardioes.yaml` | 128 | **GLOBAL** | ✅ Guardiões são os MESMOS em todos os ciclos. GLOBAL. |
| `locais.yaml` | 132 | **GLOBAL** | ✅ Locais do Reino são os MESMOS. GLOBAL. |
| `climas.yaml` | ~100 | **GLOBAL** | ✅ Climas do Reino. GLOBAL. |
| `glossario.yaml` | ~100 | **GLOBAL** | ✅ Termos do projeto. GLOBAL. |
| `ontologia.yaml` | ~80 | **GLOBAL** | ✅ Estrutura conceitual. GLOBAL. |
| `padroes_narrativos.yaml` | ~280 | **MISTO** | ⚠️ Contém regras por ciclo. Precisa reavaliação. |

---

## DIAGNÓSTICO ERIC EVANS

### Pergunta 1: LORE deve ir para `templates/global/`?

> **NÃO.** LORE é uma pasta de DADOS (knowledge base). Templates são ESTRUTURAS.
>
> Princípio DDD: "Separe dados de estruturas."
>
> - `LORE/` = **DADOS** (Guardiões, locais, glossário)
> - `.bmad/templates/` = **ESTRUTURAS** (regras de como criar)

**Veredito:** Manter `LORE/` separado. Não misturar com templates.

---

### Pergunta 2: O que é GLOBAL vs Ciclo-Específico?

**GLOBAL (não muda por ciclo):**
- Guardiões (Melquior, Noé, Celeste, Bernardo, Íris)
- Locais (Jardim, Árvore, Clareira, Caverna, Ninho)
- North Star (propósito, missão, princípios)
- Glossário (termos do projeto)
- Ontologia (estrutura conceitual)
- Climas (ensolarado, chuvoso, etc.)

**CICLO-ESPECÍFICO (muda):**
- Proporções CPA (Sementes: 60% C, Lógica: 40% A)
- Tom de narração (Encantamento → Desafio)
- Scaffolding (Mão-na-mão → Autonomia)
- Tempo de preparo (5 min → 15 min)
- Densidade sensorial (1 elem → 4 elem)

---

### Pergunta 3: Como organizar `padroes_narrativos.yaml`?

**O problema:** Este arquivo contém TANTO dados globais QUANTO regras por ciclo.

**Solução proposta:**

1. **Regras de COMO narrar** (formato, pausas, tons) → GLOBAL (fica em LORE)
2. **O QUE muda por ciclo** (scaffolding, densidade) → Já está em `.bmad/templates/[ciclo]/regras.yaml`

O arquivo `padroes_narrativos.yaml` deve conter apenas as **regras de formato** (como usar tons, pausas, transições). Os dados específicos por ciclo estão em `templates/[ciclo]/regras.yaml`.

---

## ESTRUTURA RECOMENDADA (Eric Evans)

```
_FORJA_VIVA/
├── LORE/                           # DADOS GLOBAIS (SSOT)
│   ├── north_star.yaml             # Propósito, missão, princípios
│   ├── guardioes.yaml              # 5 Guardiões (não muda por ciclo)
│   ├── locais.yaml                 # 5 Locais do Reino
│   ├── climas.yaml                 # Climas disponíveis
│   ├── glossario.yaml              # Termos do projeto
│   ├── ontologia.yaml              # Estrutura conceitual
│   └── padroes_narrativos.yaml     # Regras de COMO narrar (formato)
│
├── .bmad/
│   ├── templates/
│   │   ├── global/                 # Estrutura base
│   │   │   └── licao-base.yaml     # Seções obrigatórias em TODAS lições
│   │   ├── sementes/               # 00_sementes
│   │   │   └── regras.yaml         # CPA, tempo, scaffolding
│   │   ├── raizes-1/               # 01_raizes-1
│   │   │   └── regras.yaml
│   │   ├── raizes-2/               # 02_raizes-2
│   │   │   └── regras.yaml
│   │   ├── logica/                 # 03_logica
│   │   │   └── regras.yaml
│   │   └── legado/                 # 04_legado
│   │       └── regras.yaml
```

---

## SOBRE A NUMERAÇÃO (00_, 01_, 02_, 03_)

O usuário quer renomear para ordem visual. Análise:

| Atual | Proposto | Ordem Visual |
|-------|----------|--------------|
| sementes | 00_sementes | ✅ 1º |
| raizes-1 | 01_raizes-1 | ✅ 2º |
| raizes-2 | 02_raizes-2 | ✅ 3º |
| logica | 03_logica | ✅ 4º |
| legado | 04_legado | ✅ 5º |

**Veredito Eric Evans:**
> "Numeração com prefixo `00_`, `01_` é boa prática para ordenação em filesystem."
> 
> Mas **CUIDADO**: Se os workflows referenciam `templates/sementes/`, precisa atualizar todos.

**Recomendação:**
1. ✅ Usar `00_sementes`, `01_raizes-1`, etc. para CURRICULO (pastas de lições)
2. ⚠️ Manter nomes sem número em `.bmad/templates/` para simplicidade nos workflows

---

## VEREDITO FINAL

| Questão | Decisão |
|---------|---------|
| LORE em `templates/global/`? | ❌ **NÃO** — LORE é dados, templates é estrutura |
| Guardiões/Locais são globais? | ✅ **SIM** — não mudam por ciclo |
| `padroes_narrativos.yaml` onde? | ✅ Permanece em `LORE/` (regras de formato) |
| Renomear templates com `00_`? | ⚠️ **Opcional** — pode complicar workflows |

---

## AÇÃO RECOMENDADA

Nenhuma reorganização drástica necessária. A estrutura atual está CORRETA:

- `LORE/` = Dados globais ✅
- `.bmad/templates/[ciclo]/` = Regras por ciclo ✅
- Engenharia já referencia corretamente: "LORE/*.yaml como fonte única" ✅

**O único ajuste seria:** Se quiser numerar, aplicar apenas em `curriculo/`.

---

*Auditoria executada em 13/01/2026 às 10:07*  
*Auditor: Eric Evans + Clean Code*
