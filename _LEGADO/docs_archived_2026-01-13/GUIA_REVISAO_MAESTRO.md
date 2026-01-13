# 📋 GUIA DE REVISÃO MANUAL — Maestro

---
**Criado:** 12/01/2026 às 18:08  
**Para:** Raul (Maestro)  
**Propósito:** Guia para revisão manual dos arquivos da Forja Viva  

---

## 🎯 OBJETIVO

Revisar manualmente os arquivos da Forja Viva para garantir que:
1. Estão corretos e completos
2. Não há duplicações
3. A estrutura faz sentido
4. Você entende e aprova o conteúdo

---

## 📁 ESTRUTURA FINAL DA FORJA

```
_FORJA_VIVA/
├── 📜 Core (4 arquivos) ────────────────────────────
│   ├── ARQUITETURA_CANONICA.md   (~12KB) ★ PRIORIDADE 1
│   ├── DEFINITION_OF_DONE.md     (~5KB)  ★ PRIORIDADE 2
│   ├── CONTEXT_INDEX.md          (~4KB)  → Mapa de contexto
│   └── README.md                 (~3KB)  → Introdução
│
├── 📖 LORE/ (6 YAMLs) ──────────────────────────────
│   ├── guardioes.yaml   (~4KB) ★ PRIORIDADE 3
│   ├── locais.yaml      (~5KB)
│   ├── climas.yaml      (~4KB)
│   ├── ontologia.yaml   (~4KB) ★ PRIORIDADE 4
│   ├── north_star.yaml  (~4KB) ★ PRIORIDADE 5
│   └── glossario.yaml   (~4KB)
│
├── 🛠️ forja-core/
│   ├── conselheiros/ (6 agentes)
│   │   ├── orchestrator.md  ★ VER SEÇÃO "COMO USAR"
│   │   ├── pm.md
│   │   ├── sm.md
│   │   ├── dev.md
│   │   ├── qa.md           → O mais completo
│   │   └── ops.md
│   ├── modelos/ (3 templates)
│   └── workflows/ (2 rituais)
│
├── 📋 logs/ (9 registros) → Histórico de decisões
├── 📜 pergaminhos/ → Narrativa
├── 📄 docs/ → Documentação técnica
├── 📚 curriculo/ → Lições (~102 arquivos)
├── 🌐 site/ → Landing page
└── 📤 saida/ → Output do pipeline
```

---

## 🔄 ORDEM DE REVISÃO SUGERIDA

### FASE 1: Core (Essencial) — ~30 min

| # | Arquivo | O que Verificar | Tempo |
|---|---------|-----------------|-------|
| 1 | `ARQUITETURA_CANONICA.md` | 32 decisões estão corretas? | 15 min |
| 2 | `DEFINITION_OF_DONE.md` | Checklist QA faz sentido? | 10 min |
| 3 | `CONTEXT_INDEX.md` | Mapa reflete a realidade? | 5 min |

### FASE 2: LORE (Dados) — ~20 min

| # | Arquivo | O que Verificar | Tempo |
|---|---------|-----------------|-------|
| 4 | `guardioes.yaml` | 5 Guardiões, frases, cores | 5 min |
| 5 | `ontologia.yaml` | Atores, hierarquia | 5 min |
| 6 | `north_star.yaml` | Missão, preços, tríade | 5 min |
| 7 | `locais.yaml`, `climas.yaml`, `glossario.yaml` | Dados corretos | 5 min |

### FASE 3: Agentes (Opcional) — ~15 min

| # | Arquivo | O que Verificar | Tempo |
|---|---------|-----------------|-------|
| 8 | `conselheiros/orchestrator.md` | Como invocar | 5 min |
| 9 | `conselheiros/qa.md` | Verificação Quíntupla | 10 min |

### FASE 4: Logs (Histórico) — ~10 min

| # | O que Fazer |
|---|-------------|
| 10 | Ler nomes dos 9 logs para entender histórico |
| 11 | Abrir `MESA_AGENTES_ARQUITETURA.md` (mais rico) |

---

## ✅ CHECKLIST DE REVISÃO

### Core
- [ ] `ARQUITETURA_CANONICA.md` — 32 decisões estão OK?
- [ ] `DEFINITION_OF_DONE.md` — Estrutura da lição faz sentido?
- [ ] `CONTEXT_INDEX.md` — Mapa está atualizado?

### LORE
- [ ] `guardioes.yaml` — 5 Guardiões corretos?
- [ ] `locais.yaml` — 5 Locais corretos?
- [ ] `climas.yaml` — 8 Climas corretos?
- [ ] `ontologia.yaml` — Atores corretos? Hierarquia OK?
- [ ] `north_star.yaml` — Missão, preços, tríade OK?
- [ ] `glossario.yaml` — Termos proibidos OK?

### Estrutura
- [ ] Sem arquivos duplicados?
- [ ] Sem pastas vazias?
- [ ] Nomes fazem sentido?

---

## 💡 DICAS PARA REVISÃO

### O que Procurar

| Tipo | Exemplo |
|------|---------|
| **Erro de dado** | Preço errado, nome errado |
| **Duplicação** | Mesmo conteúdo em dois lugares |
| **Desatualizado** | Referência a arquivo que não existe |
| **Inconsistência** | Decisão A diz X, decisão B diz Y |

### O que NÃO Precisa Fazer

- ❌ Revisar cada linha de código
- ❌ Verificar ortografia (já verificado)
- ❌ Reformatar arquivos
- ❌ Revisar os 102 arquivos de currículo agora

---

## 🎯 COMO USAR O ORCHESTRATOR

### O que é o Orchestrator?

O **Orchestrator** é o coordenador da Forja. Ele:
- Coordena todos os outros agentes (PM, SM, Dev, QA, Ops)
- Toma decisões usando análise estruturada
- Registra decisões em logs
- Sempre pede aprovação antes de executar

### Quando Usar

| Situação | Comando Sugerido |
|----------|------------------|
| Precisa tomar decisão complexa | "Use o ORCHESTRATOR para decidir..." |
| Quer reunir os agentes | "Use o ORCHESTRATOR para reunir os agentes..." |
| Quer verificação completa | "Use o ORCHESTRATOR para verificar..." |
| Quer plano de ação | "Use o ORCHESTRATOR para planejar..." |

### Como Invocar

```
"Use o ORCHESTRATOR para [TAREFA]."

Exemplos:
- "Use o ORCHESTRATOR para verificar a estrutura."
- "Use o ORCHESTRATOR para decidir se devemos manter X."
- "Use o ORCHESTRATOR para criar um plano de produção."
- "Use o ORCHESTRATOR para reunir os agentes e discutir Y."
```

### O que Esperar

Quando você invoca o Orchestrator, ele:

1. **Analisa** o problema
2. **Consulta** os agentes relevantes
3. **Cria um log** com a discussão
4. **Propõe** opções e decisões
5. **Pergunta** sua aprovação antes de executar
6. **Executa** após aprovação

### Princípios do Orchestrator

| Princípio | Significado |
|-----------|-------------|
| **Orquestração Humana** | Você (Maestro) decide, ele prepara |
| **Transparência** | Sempre mostra o que está fazendo |
| **Sem Decisões Finais** | Nunca executa sem sua aprovação |
| **Condição de Parada** | Todo workflow tem critério de conclusão |

### Outros Comandos Úteis

| Comando | O que Faz |
|---------|-----------|
| "Faça verificação tripla" | 3 passes de verificação |
| "Crie um log da discussão" | Registra em logs/ |
| "Use os agentes para deliberar" | Mesa com todos os agentes |
| "Converta para YAML" | Transforma MD em YAML |

---

## 📊 RESUMO DA SESSÃO DE HOJE

### O que Foi Feito

| Hora | Tema |
|------|------|
| 11:16 | Avaliação North Star |
| 11:19 | Discussão de negócio |
| 11:36 | Consolidação |
| 11:49 | Plano de negócio final |
| 12:48 | Perguntas do PM |
| 13:39 | Mesa dos Agentes (14 decisões) |
| 14:09 | Migração GOVERNANCA → LORE |
| 16:34 | Auto-verificação agentes |
| 16:48 | Decisão sobre ESPECIALISTAS |
| 18:08 | Verificação final + Este guia |

### Arquivos Criados

| Tipo | Quantidade |
|------|------------|
| YAMLs (LORE) | 6 |
| Logs | 9 |
| Documentos Core | 4 |
| Agentes atualizados | 2 |

### Arquivos Removidos

| Arquivo | Motivo |
|---------|--------|
| ONTOLOGIA.md | Duplicado com YAML |
| NORTH_STAR.md | Duplicado com YAML |
| CONTEXTO_RETOMADA.md | Obsoleto |
| GLOSSARIO.md | Duplicado com YAML |
| ESPECIALISTAS.md | Duplicado com agentes |
| pasta rituais/ | Vazia |

---

## 🚀 PRÓXIMOS PASSOS (Após Revisão)

1. [ ] **Criar template de lição em YAML** — Formato fonte único
2. [ ] **Criar Engine YAML → HTML** — Pipeline de conversão
3. [ ] **Criar L001** — Primeira lição no novo formato
4. [ ] **Testar com Raulzito** — Validação real

---

> *"Revise com olhos de dono. Se algo não faz sentido, pergunte."*
> — Orchestrator, 12/01/2026
