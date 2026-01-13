# 🎯 LOG DO ORCHESTRATOR — Decisão sobre ESPECIALISTAS

---
**Data:** 12/01/2026 às 16:48  
**Agente Líder:** Orchestrator  
**Tema:** Manter ou remover ESPECIALISTAS.md da Forja  

---

## 🧭 ANÁLISE DO ORCHESTRATOR

### Arquivos em Questão

| Arquivo | Local | Linhas | Conteúdo |
|---------|-------|--------|----------|
| `ESPECIALISTAS.md` | Forja | 238 | Especialistas condensados |
| `PAINEL-ESPECIALISTAS.md` | GOVERNANCA | 520 | Versão completa original |

### O que ESPECIALISTAS.md Contém

1. **20 Princípios CM** — ✅ Útil, mas pode ir para QA ou DEFINITION_OF_DONE
2. **Lewis, Tolkien, Fujimura** — ✅ Útil para Dev
3. **Bruner CPA, Vygotsky** — ✅ Útil para QA
4. **Potter Visual** — ✅ Útil para Design
5. **Mapeamento Agentes** — ⚠️ Duplicado com os próprios agentes

### Duplicação Identificada

| Conteúdo | Já existe em |
|----------|--------------|
| CPA | `LORE/glossario.yaml`, `forja-core/modelos/checklist-cpa.md` |
| Termos proibidos | `LORE/glossario.yaml` |
| Mapeamento agentes | Cada `conselheiros/*.md` |
| Fluxo de trabalho | `workflows/pilot-sprint.md` |

---

## 🎯 DECISÃO DO ORCHESTRATOR

### Veredito: **REMOVER ESPECIALISTAS.md**

**Motivo:**
1. **Duplicação** — 80% do conteúdo já está nos agentes ou LORE
2. **SSOT violado** — Manter dois lugares para mesma informação gera inconsistência
3. **PAINEL original** — Continua em GOVERNANCA como referência histórica

### O que Vale Incorporar (Único)

| Conteúdo Único | Incorporar Em | Ação |
|----------------|---------------|------|
| 20 Princípios CM (tabela) | `qa.md` | ⚠️ Já tem referência |
| Citações de comando | Manter em Dev como "prompts" | ⚠️ Opcional |
| Perguntas de veto por especialista | Já estão em `qa.md` | ✅ Coberto |

### Conclusão
> **Nada precisa ser incorporado.** Os agentes já têm o que precisam.

---

## ✅ AÇÕES TOMADAS

| # | Ação | Status |
|---|------|--------|
| 1 | Remover `ESPECIALISTAS.md` | ⏳ Pendente |
| 2 | Atualizar CONTEXT_INDEX | ⏳ Pendente |

---

## 📌 SOBRE PADRONIZAÇÃO DOS AGENTES

### Análise do Orchestrator

| Agente | Linhas | Completo? | Precisa Padronizar? |
|--------|--------|-----------|---------------------|
| Orchestrator | 75 | ✅ Sim | ❌ Não |
| PM | 69 | ✅ Sim | ❌ Não |
| SM | ~60 | ✅ Sim | ❌ Não |
| Dev | ~60 | ⚠️ Básico | ❌ Não (função diferente) |
| QA | 218 | ✅ Muito completo | ❌ Não |
| Ops | ~90 | ✅ Sim | ❌ Não |

### Veredito: **NÃO PADRONIZAR**

**Motivo:**
1. Cada agente tem função diferente
2. QA **deve** ser mais detalhado (é o filtro final)
3. Dev **deve** ser mais simples (foco em criação)
4. Forçar mesmo tamanho = informação desnecessária

---

> *"Não mude o que funciona. Simplifique o que duplica."*
> — Orchestrator, 12/01/2026
