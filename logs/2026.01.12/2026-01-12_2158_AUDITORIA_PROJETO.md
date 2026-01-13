# 📋 AUDITORIA COMPLETA — _FORJA_VIVA

**Data:** 12/01/2026  
**Objetivo:** Mapear TODO o projeto para refinamento impecável  

---

## 📊 MAPA COMPLETO DO PROJETO

### 📁 RAIZ (7 arquivos)
| Arquivo | Bytes | Propósito |
|---------|-------|-----------|
| `ARQUITETURA_CANONICA.md` | 12KB | Arquitetura geral |
| `CONTEXT_INDEX.md` | 2KB | Índice de navegação |
| `CONTEXT_RESTORE.md` | 1KB | Resumo para IA |
| `DEFINITION_OF_DONE.md` | 4KB | Critérios de qualidade |
| `GUIA_REVISAO_MAESTRO.md` | 8KB | Guia de revisão |
| `README.md` | 1KB | Introdução |
| `Texto.md` | 48KB | Texto longo (?) |

---

### 📁 .bmad/ (19 YAML) ✅ JÁ REVISADO
| Pasta | Arquivos |
|-------|----------|
| orchestrator.yaml | Super Agente |
| experts/ | 14 especialistas |
| workflows/ | 2 workflows |
| templates/ | 2 templates |

---

### 📁 LORE/ (6 YAML)
| Arquivo | Propósito |
|---------|-----------|
| `north_star.yaml` | ✅ Atualizado com sistema_agentes |
| `climas.yaml` | Atmosferas narrativas |
| `locais.yaml` | Cenários do Reino |
| `guardioes.yaml` | Os 5 Guardiões |
| `glossario.yaml` | Termos canônicos |
| `ontologia.yaml` | Estrutura conceitual |

---

### 📁 forja-core/ (9 arquivos)
| Subpasta | Arquivos | Status |
|----------|----------|--------|
| **modelos/** | | |
| | `template-v4.1-sementes.yaml` | ✅ Novo |
| | `template-v4-sementes.md` | ⚠️ Legado? |
| | `checklist-cpa.md` | Revisar |
| | `story-template.md` | Revisar |
| **pipeline/** | | |
| | `gutenberg_forja.py` | ⚠️ Precisa YAML |
| | `style.css` | Verificar |
| | `README.md` | Verificar |
| **workflows/** | | |
| | `cm-audit.md` | ⚠️ Duplicado? |
| | `pilot-sprint.md` | Revisar |
| **conselheiros/** | (vazio) | Limpar |

---

### 📁 _LEGADO/ (11 arquivos)
| Subpasta | Arquivos |
|----------|----------|
| `bmad_agents/` | sofia, euclides, artesao, veritas |
| `bmad_roles/` | dev, ops, orchestrator, pm, qa, sm |
| `PAINEL-ESPECIALISTAS.md` | Fonte original |

---

### 📁 curriculo/ (~79 arquivos)
| Subpasta | Conteúdo |
|----------|----------|
| `01_SEMENTES/` | Lições K (0-6) |
| `02_RAIZES/` | Lições 1-4 ano |
| `03_LOGICA/` | Lições 5-8 ano |
| `04_LEGADO/` | Lições 9-12 ano |
| `_SISTEMA/CURRICULOS_MESTRE/` | TGTB ref |
| `PAGES/` | Páginas do site |

---

### 📁 docs/ (4 arquivos)
| Arquivo | Propósito |
|---------|-----------|
| `architecture.md` | Arquitetura técnica |
| `prd.md` | Product Reqs |
| `AUDITORIA_FORJA_vs_PAINEL.md` | Comparação |
| `DELIBERACAO_RENASCIMENTO.md` | Decisões |

---

### 📁 logs/ (~20 arquivos)
| Tipo | Conteúdo |
|------|----------|
| Deliberações | Sessões de multi-agentes |
| Análises | Orchestrator |

---

## 🔧 ANÁLISE POR EXPERT DE ENGENHARIA

### 🔵 DEVOPS — "O build roda sem intervenção manual?"

| Arquivo | Problema | Decisão |
|---------|----------|---------|
| `gutenberg_forja.py` | Lê MD, não YAML | ⚠️ ATUALIZAR |
| `forja-core/pipeline/` | Local antigo | MANTER (pipeline vive aqui) |
| `.bmad/workflows/` | Workflows novos | OK |

**Veredito DevOps:** Pipeline precisa ler YAML. Um comando = HTML + PDF.

---

### 🟢 QA — "Links funcionam? YAML válido?"

| Arquivo | Status |
|---------|--------|
| `.bmad/*.yaml` | ✅ Válidos |
| `LORE/*.yaml` | ✅ Válidos |
| `forja-core/*.md` | ⚠️ Revisar links |

**Veredito QA:** Rodar validação em todos os YAML e MD.

---

### 🟡 ERIC EVANS (DDD) — "Há duplicação? SSOT respeitado?"

| Duplicação | Arquivo A | Arquivo B | Decisão |
|------------|-----------|-----------|---------|
| Workflows | `.bmad/workflows/` | `forja-core/workflows/` | **SSOT = .bmad** |
| Templates | `template-v4.md` | `template-v4.1.yaml` | **SSOT = YAML** |
| Especialistas | `_LEGADO/bmad_*` | `.bmad/experts/` | ✅ LEGADO correto |

**Veredito Evans:** 
- `.bmad/` é o SSOT para especialistas e workflows
- `forja-core/` é o SSOT para pipeline e templates de produção
- Não duplicar entre os dois

---

## 📋 PLANO DE REFINAMENTO (Baseado em Engenharia)

### FASE 1: SSOT Workflows ✅ APROVADO
**Decisão:** Manter workflows em 2 locais com propósitos diferentes:
- `.bmad/workflows/` = Workflows de **deliberação** (multi-agente)
- `forja-core/workflows/` = Workflows de **produção** (pipeline)

**Ação:** Renomear para clareza, não fundir.

### FASE 2: SSOT Templates
- **MANTER:** `forja-core/modelos/template-v4.1-sementes.yaml`
- **MOVER para _LEGADO:** `forja-core/modelos/template-v4-sementes.md`

### FASE 3: Pipeline YAML
- **ATUALIZAR:** `gutenberg_forja.py` para ler YAML
- **Teste:** `python gutenberg_forja.py L001.yaml` → HTML

### FASE 4: Limpeza
- **EXCLUIR:** `forja-core/conselheiros/` (vazio)
- **VERIFICAR:** `_LEGADO/` está completo

### FASE 5: Documentação
- **ATUALIZAR:** `CONTEXT_INDEX.md` com nova estrutura
- **CRIAR:** `README.md` no `.bmad/`

---

## ✅ PRÓXIMO PASSO

Executar Fase 2 (mover template legado) e Fase 4 (limpar vazios)?

