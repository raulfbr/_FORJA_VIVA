# 🗣️ REUNIÃO DE AUDITORIA — orchestrator.yaml

**Data:** 13/01/2026 às 13:39  
**Convocador:** Maestro  
**Propósito:** Verificar se orchestrator.yaml está atualizado com referências corretas

---

## 📋 ARQUIVO ANALISADO

`orchestrator.yaml` (172 linhas, 7KB)
- Versão: 1.0
- Última atualização: Não especificada

---

## 👥 PARTICIPANTES (TODOS OS 14 EXPERTS)

| Conselho | Experts |
|----------|---------|
| **Pedagogia** | Charlotte Mason, Susan Macaulay |
| **Matemática** | Jerome Bruner, Lev Vygotsky |
| **Narrativa** | C.S. Lewis, Tolkien, Beatrix Potter, Makoto Fujimura |
| **Negócios** | Seth Godin, Alex Hormozi, Peter Thiel |
| **Design** | Grupo Design |
| **Engenharia** | Eric Evans, BMAD |
| **UX** | Mães Personas |

---

## 🔍 ANÁLISE POR SEÇÃO

### 1. METADADOS (linhas 1-14)
| Item | Valor Atual | Status |
|------|-------------|--------|
| versão | "1.0" | ⚠️ Desatualizado (deveria ser 1.1 após mudanças) |
| coordenadora | charlotte_mason | ✅ OK |

**Eric Evans:** "Versão precisa ser atualizada para refletir mudanças."

---

### 2. MODOS DE OPERAÇÃO (linhas 17-103)

#### Modo REUNIAO ✅
- Fases bem definidas (1-6)
- CM coordena e decide
- **Status:** OK

#### Modo CRIAR_LICAO ⚠️
| Fase | Referência | Análise |
|------|------------|---------|
| Planning | `perd.yaml` | ⚠️ Deveria ser `LORE/index.yaml` + `templates/000_global/perd-template.yaml` |
| Development | `rascunho.yaml` | ⚠️ Não menciona LORE |
| Verification | `engenharia` | ✅ OK |

**Tolkien:** "Falta mencionar consulta ao LORE/guardioes.yaml para frases canônicas."

**Eric Evans:** "Modo CRIAR_LICAO deveria referenciar:
- `LORE/index.yaml` como ponto de entrada
- `templates/000_global/licao-base.yaml` como estrutura"

#### Modo REVISAO ⚠️
| Check | Referência | Análise |
|-------|------------|---------|
| CM Check | charlotte_mason | ✅ OK |
| Guardião Check | jrr_tolkien | ⚠️ Deveria referenciar `LORE/guardioes.yaml` |
| Template Check | engenharia | ⚠️ Deveria referenciar `definition-of-done.md` |

---

### 3. HIERARQUIA DE VETO (linhas 105-124) ✅
- Charlotte Mason prioridade 1
- Ordem correta (CM → Bruner → Lewis → Tolkien)
- **Status:** OK

---

### 4. COMANDOS (linhas 126-155)

| Comando | Workflow Referenciado | Status |
|---------|----------------------|--------|
| `/reuniao` | Nenhum | ⚠️ Deveria referenciar `reuniao-deliberacao.yaml` |
| `/criar-licao` | Nenhum | ⚠️ Deveria referenciar `criar-licao-premium.yaml` |
| `/revisar-licao-auto` | `revisar-licao-auto.yaml` | ✅ OK |
| `/revisar-pontos` | `revisar-pontos.yaml` | ✅ OK |

---

## 📊 RESUMO DE PROBLEMAS

| # | Problema | Severidade | Correção |
|---|----------|------------|----------|
| 1 | Versão desatualizada (1.0) | 🟡 Média | Atualizar para 1.1 |
| 2 | CRIAR_LICAO não referencia LORE | 🔴 Alta | Adicionar refs LORE |
| 3 | REVISAO não referencia LORE/guardioes | 🔴 Alta | Adicionar refs |
| 4 | /reuniao sem workflow | 🟡 Média | Adicionar ref |
| 5 | /criar-licao sem workflow | 🟡 Média | Adicionar ref |
| 6 | Falta seção `referencias_lore` | 🔴 Alta | Adicionar seção |

---

## 💬 POSIÇÕES DOS EXPERTS

### Charlotte Mason (Coordenadora)
> "O Orchestrator precisa guiar os agentes para o LORE. Sem isso, podem produzir lições desconectadas da North Star."

**VEREDITO:** 🔴 REQUER ATUALIZAÇÃO

### Eric Evans (SSOT)
> "Princípio SSOT violado. O Orchestrator deveria ser o HUB que aponta para todas as fontes canônicas:
> - LORE/index.yaml
> - templates/000_global/
> - workflows/"

**VEREDITO:** 🔴 REQUER ATUALIZAÇÃO

### J.R.R. Tolkien (Consistência)
> "O Guardião Check menciona verificar 'frases canônicas', mas não diz ONDE encontrá-las. Deveria apontar para LORE/guardioes.yaml."

**VEREDITO:** 🔴 REQUER ATUALIZAÇÃO

### BMAD Method (Engenharia)
> "Comandos precisam referenciar workflows explicitamente. Isso evita ambiguidade."

**VEREDITO:** 🟡 REQUER ATUALIZAÇÃO

---

## ✅ DECISÃO UNÂNIME

**TODOS OS EXPERTS CONCORDAM:** O orchestrator.yaml precisa de atualização para incluir:

1. **Seção `referencias_lore`** no início
2. **Atualizar versão** para 1.1
3. **Modo CRIAR_LICAO** com refs LORE e templates
4. **Modo REVISAO** com refs LORE/guardioes e definition-of-done
5. **Comandos** com refs explícitas para workflows

---

## 🔧 CORREÇÕES PROPOSTAS

### Adicionar após linha 14:
```yaml
# ═══════════════════════════════
# REFERÊNCIAS LORE (SSOT)
# ═══════════════════════════════

referencias_lore:
  indice: "LORE/index.yaml"
  north_star: "LORE/north_star.yaml"
  guardioes: "LORE/guardioes.yaml"
  locais: "LORE/locais.yaml"
  climas: "LORE/climas.yaml"
  padroes: "LORE/padroes_narrativos.yaml"

referencias_templates:
  global: ".bmad/templates/000_global/"
  licao_base: ".bmad/templates/000_global/licao-base.yaml"
  definition_done: ".bmad/templates/000_global/definition-of-done.md"
  perd: ".bmad/templates/000_global/perd-template.yaml"

referencias_workflows:
  reuniao: ".bmad/workflows/reuniao-deliberacao.yaml"
  criar_licao: ".bmad/workflows/criar-licao-premium.yaml"
  revisar_auto: ".bmad/workflows/revisar-licao-auto.yaml"
  revisar_pontos: ".bmad/workflows/revisar-pontos.yaml"
  cm_audit: ".bmad/workflows/cm-audit.md"
```

---

## ❓ PERGUNTA PARA O MAESTRO

**Aprovar estas correções no orchestrator.yaml?**

---

## 📂 ANÁLISE DOS WORKFLOWS (7 arquivos)

### Inventário Atual:

| # | Arquivo | Tamanho | Análise |
|---|---------|---------|---------|
| 1 | `criar-licao-premium.yaml` | 5.6KB | ✅ ESSENCIAL — Workflow principal de criação |
| 2 | `criar-licao-premium.md` | 7.6KB | 🔴 **DUPLICATA** do .yaml (formato diferente) |
| 3 | `reuniao-deliberacao.yaml` | 7.4KB | ✅ ESSENCIAL — Reuniões de experts |
| 4 | `revisar-licao-auto.yaml` | 10KB | ✅ ESSENCIAL — QA automática por 14 experts |
| 5 | `revisar-pontos.yaml` | 11KB | ⚠️ ÚTIL — Revisão por pontos específicos |
| 6 | `cm-audit.md` | 3.1KB | ⚠️ **REFERÊNCIA OBSOLETA** (menciona MAGNA_CARTA inexistente) |
| 7 | `pilot-sprint.md` | 2.5KB | 🔴 **OBSOLETO** — Usa termos antigos (STORY, PM/SM roles) |

---

### 💬 POSIÇÕES DOS EXPERTS SOBRE WORKFLOWS

**Eric Evans (SSOT):**
> "Duplicação clara: `criar-licao-premium.yaml` e `.md` fazem a mesma coisa. Manter apenas um."
> **VEREDITO:** Arquivar o `.md`, manter o `.yaml`

**Charlotte Mason:**
> "`cm-audit.md` tem os 20 Princípios corretos, mas referencia 'MAGNA_CARTA lines 107-133' que não existe. O conteúdo está em `LORE/north_star.yaml`."
> **VEREDITO:** Atualizar referência ou integrar ao `definition-of-done.md`

**BMAD Method:**
> "`pilot-sprint.md` usa linguagem BMAD v5 (STORY, PM, SM). Isso não condiz com nossa estrutura atual (experts por conselho)."
> **VEREDITO:** Arquivar

**Susan Macaulay:**
> "`revisar-pontos.yaml` é muito complexo (280 linhas). Famílias não vão usar. É mais para o sistema."
> **VEREDITO:** Manter (é interno)

---

### ✅ DECISÃO SOBRE WORKFLOWS

| Arquivo | Decisão | Ação |
|---------|---------|------|
| `criar-licao-premium.yaml` | 🟢 **MANTER** | Principal |
| `criar-licao-premium.md` | 🔴 **ARQUIVAR** | Duplicata |
| `reuniao-deliberacao.yaml` | 🟢 **MANTER** | Essencial |
| `revisar-licao-auto.yaml` | 🟢 **MANTER** | QA 14 experts |
| `revisar-pontos.yaml` | 🟢 **MANTER** | Útil interno |
| `cm-audit.md` | 🟡 **CONSOLIDAR** | Integrar ao definition-of-done |
| `pilot-sprint.md` | 🔴 **ARQUIVAR** | Obsoleto |

---

### 📊 RESULTADO FINAL

**Antes:** 7 workflows  
**Depois:** 4 workflows essenciais + 2 integrados/arquivados

**Workflows Finais:**
1. `criar-licao-premium.yaml` — Criar lição
2. `reuniao-deliberacao.yaml` — Reuniões
3. `revisar-licao-auto.yaml` — QA automática
4. `revisar-pontos.yaml` — Revisão por pontos

---

> *"O Orchestrator é o mapa. Sem referências corretas, os agentes se perdem."*  
> — Eric Evans

> *"Consistência exige que todos consultem a mesma fonte."*  
> — J.R.R. Tolkien
