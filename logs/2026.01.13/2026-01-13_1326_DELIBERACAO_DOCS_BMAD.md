# 🗣️ REUNIÃO DE DELIBERAÇÃO — Arquivos .bmad/docs/

**Data:** 13/01/2026 às 13:26  
**Convocador:** Maestro  
**Propósito:** Decidir destino de 4 documentos em .bmad/docs/

---

## 📋 PAUTA

1. Analisar cada documento
2. Recomendar: ARQUIVAR, MANTER ou CONSOLIDAR
3. Verificar consistência com north_star.yaml
4. Aguardar decisão do Maestro

---

## 👥 PARTICIPANTES

| Expert | Área | Papel na Reunião |
|--------|------|------------------|
| **Eric Evans** | DDD/SSOT | Avalia duplicações |
| **Charlotte Mason** | Pedagogia | Avalia se conteúdo é essencial |
| **Susan Macaulay** | Praticidade | Avalia utilidade para famílias |
| **BMAD Method** | Engenharia | Avalia estrutura do sistema |

---

## 📄 ANÁLISE DOS DOCUMENTOS

### 1. `ARQUITETURA_CANONICA.md` (291 linhas, 12KB)

**Conteúdo:**
- 32 decisões canônicas (12/01/2026)
- História de Bernardo (canonizada)
- Template V4 estrutura
- Pipeline de produção
- Frases dos Guardiões
- Roadmap de produção

**Análise dos Experts:**

| Expert | Opinião |
|--------|---------|
| **Eric Evans** | ⚠️ "Muita informação está DUPLICADA. Guardiões já estão em `LORE/guardioes.yaml`. Decisões canônicas deveriam estar em `LORE/north_star.yaml`." |
| **Charlotte Mason** | ⚠️ "A história de Bernardo é bonita, mas deveria estar em `LORE/guardioes.yaml` ou arquivo próprio." |
| **BMAD** | ⚠️ "Documento de sessão específica (12/01). Muitas referências desatualizadas (forja-core/modelos, estrutura antiga)." |

**🔴 VEREDICTO: ARQUIVAR**  
*Motivo: Maioria do conteúdo já migrou para LORE. Manter em _LEGADO para histórico.*

---

### 2. `CONTEXT_INDEX.md` (83 linhas, 2.4KB)

**Conteúdo:**
- Mapa de diretórios (desatualizado)
- Links para arquivos (muitos não existem mais)

**Análise dos Experts:**

| Expert | Opinião |
|--------|---------|
| **Eric Evans** | ❌ "Referencia `forja-core/modelos` que não existe. Referencia `.agent/` que é outra coisa. Totalmente desatualizado." |
| **BMAD** | ❌ "Este era um índice de sessão. A estrutura mudou completamente." |

**🔴 VEREDICTO: ARQUIVAR**  
*Motivo: 100% desatualizado. Não há nada para extrair.*

---

### 3. `GUIA_REVISAO_MAESTRO.md` (248 linhas, 7.8KB)

**Conteúdo:**
- Guia de revisão manual para Maestro
- Como usar o Orchestrator
- Checklist de revisão
- Resumo de sessão (12/01)

**Análise dos Experts:**

| Expert | Opinião |
|--------|---------|
| **Eric Evans** | ⚠️ "Seção 'Como usar Orchestrator' é útil. Resto é contexto de sessão." |
| **Susan Macaulay** | ✅ "A seção sobre orquestrador pode ajudar na próxima sessão." |
| **BMAD** | ⚠️ "Checklists já estão em DEFINITION_OF_DONE. Mas seção Orchestrator é única." |

**⚠️ CONTEÚDO A EXTRAIR antes de arquivar:**

```markdown
## 🎯 COMO USAR O ORCHESTRATOR

O **Orchestrator** é o coordenador da Forja. Ele:
- Coordena todos os outros agentes
- Toma decisões usando análise estruturada
- Registra decisões em logs
- Sempre pede aprovação antes de executar

### Comandos Úteis
| Comando | O que Faz |
|---------|-----------|
| "Use o ORCHESTRATOR para decidir..." | Decisão complexa |
| "Use os agentes para deliberar..." | Mesa de reunião |
| "Faça verificação tripla" | 3 passes de verificação |
```

**🟡 VEREDICTO: EXTRAIR + ARQUIVAR**  
*Ação: Salvar seção Orchestrator em `.bmad/docs/como-usar-orchestrator.md` e arquivar o resto.*

---

### 4. `DEFINITION_OF_DONE.md` (159 linhas, 5KB)

**Conteúdo:**
- Checklist de QA para lições
- Metadados YAML obrigatórios
- Estrutura das 13 seções da lição
- 8 climas narrativos
- Métricas de qualidade
- Indicadores de CARD

**Análise dos Experts:**

| Expert | Opinião |
|--------|---------|
| **Charlotte Mason** | ✅ "Essencial! Define o que é uma boa lição." |
| **Eric Evans** | ⚠️ "Climas já estão em `LORE/climas.yaml`. Estrutura de lição já está em `licao-base.yaml`. Mas checklist QA é único." |
| **BMAD** | ✅ "Este é o DoD! Quase todo sistema de produção precisa disso." |
| **Susan Macaulay** | ✅ "Ajuda a garantir qualidade para famílias." |

**⚠️ CONTEÚDO VALIOSO:**
- Checklist de QA (seção 4) — ÚNICO
- Métricas de qualidade — ÚNICO
- Processo de validação — ÚNICO

**🟢 VEREDICTO: MANTER (com atualização)**  
*Ação: Mover para `.bmad/templates/000_global/definition-of-done.md` e atualizar referências.*

---

## 📊 RESUMO DAS DECISÕES (Aguardando Maestro)

| Documento | Decisão | Ação |
|-----------|---------|------|
| `ARQUITETURA_CANONICA.md` | 🔴 ARQUIVAR | Mover para `_LEGADO/` |
| `CONTEXT_INDEX.md` | 🔴 ARQUIVAR | Mover para `_LEGADO/` |
| `GUIA_REVISAO_MAESTRO.md` | 🟡 EXTRAIR+ARQUIVAR | Salvar Orchestrator, arquivar resto |
| `DEFINITION_OF_DONE.md` | 🟢 MANTER | Mover para templates/000_global/ |

---

## 🔍 VERIFICAÇÃO NORTH_STAR.YAML

| Item | Status |
|------|--------|
| Melquior é "líder dos Guardiões" (não Rei) | ⚠️ Verificar se north_star.yaml menciona incorretamente |
| Famílias Pioneiras (não só Rodrigues) | ⚠️ Verificar menções |
| Fase Berço (0-4 anos) | ✅ Já adicionado |
| Onboarding | ✅ Já adicionado |

---

## ❓ PERGUNTAS PARA O MAESTRO

1. **Aprovar arquivamento** de ARQUITETURA_CANONICA.md e CONTEXT_INDEX.md?

2. **Extrair seção Orchestrator** de GUIA_REVISAO para novo arquivo antes de arquivar?

3. **Manter DEFINITION_OF_DONE** e mover para templates/000_global/?

4. **Verificar north_star.yaml** para corrigir menções a Melquior ou Família Rodrigues?

---

*Aguardando decisão do Maestro para prosseguir.*

---

> *"Cada documento serve a um propósito. Se não serve mais, deve ir para o arquivo."*  
> — Eric Evans (SSOT)

> *"Mantenha apenas o que ajuda as famílias."*  
> — Susan Macaulay
