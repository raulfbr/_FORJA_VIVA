# PLANO DE IMPLEMENTAÇÃO: Upgrade Engenharia.yaml v2.0

**Base:** `.bmad/experts/engenharia/engenharia.yaml` (atual: 129 linhas)  
**Fonte:** `logs/2026-01-13_1800_UPGRADE_ENGENHARIA_DEEPSEEK.md`  
**Data:** 2026-01-13 18:08

---

## 📋 RESUMO EXECUTIVO

Este plano detalha **5 mudanças propostas** ao `engenharia.yaml`, cada uma com diff exato, justificativa técnica e opção de aprovação individual.

**Resultado Final Esperado:**
- Arquivo: 129 linhas → ~175 linhas (+35%)
- Especialistas: 4 → 5 (+ Poetiq Reasoner)
- Verificação: 5 passes → 7 passes (+ Reflexion + CoVe)
- Princípios North Star: 3 → 4 (+ Auto-Aperfeiçoamento)

---

## ✅ MUDANÇA #1: ADICIONAR ESPECIALISTA POETIQ REASONER

### 📍 Localização
Adicionar **APÓS** `especialistas[3]` (QA), **ANTES** de `mapa_projeto`

### 🎯 Objetivo
Criar um 5º especialista focado em meta-raciocínio, loops recursivos e auto-aperfeiçoamento do sistema.

### 📝 Diff Exato

```diff
  - id: qa
    nome: QA
    ...
    q: Todos checks passam?

+ - id: poetiq_reasoner
+   nome: Poetiq Meta-Reasoner
+   titulo: O Metapensador
+   tipo: Framework
+   desc: Meta-sistema reasoning loops recursivos. Não apenas testa — aprende e melhora estratégias.
+   foco: Recursive Self-Improvement, Reflexion, Chain-of-Verification (CoVe)
+   principios:
+     - {name: Reflexion Pattern, desc: Gerar → Criticar → Refinar → Persistir crítica útil, app: Agente critica próprio output antes finalizar}
+     - {name: Chain-of-Verification (CoVe), desc: Rascunho → Gerar 3 perguntas → Responder sem ver original → Verificar, app: Toda lição passa CoVe antes publicação}
+     - {name: Recursive Self-Improvement, desc: Sistema aprende estratégias funcionam armazena para reutilizar, app: Se analogia pizza confunde aprende evitar tenta barras chocolate}
+     - {name: Self-Auditing, desc: Sistema monitora próprio desempenho identifica padrões melhoria, app: Métricas sucesso/falha alimentam próximas decisões}
+   citacao: The meta-system acts as supervisor that decomposes problems researches strategies synthesizes knowledge - Poetiq.ai
+   fonte: poetiq.ai
+   veto:
+     pode: true
+     pri: 12
+     gatilhos:
+       - {id: logical_inconsistency, act: REJECT, just: Detectada contradição lógica via CoVe}
+       - {id: failed_reflexion, act: REJECT, just: Auto-crítica identificou falha crítica narrativa/matemática}
+       - {id: no_improvement_loop, act: WARN, just: Código/lição sem ciclo refinamento visível}
+     q: O sistema aprendeu algo novo com esta tarefa?

mapa_projeto:
  ...
```

### 💡 Justificativa
- **DeepSeek enfatiza:** "Logician (Validador Poetiq)" é crucial para garantir lições aprendem e melhoram
- **Impacto:** Adiciona camada de inteligência superior que evolui o sistema automaticamente
- **Precedente:** BMAD (pri 10), Evans (pri 9), QA (pri 8) — Poetiq pri 12 garante veto final lógico

### 📊 Impacto
- **Linhas adicionadas:** +20
- **Complexidade:** Alta (novo conceito meta-cognitivo)
- **Breaking change:** Não (backward compatible)

### ✅ Aprovação
- [ ] **APROVAR** — Adicionar Poetiq Reasoner conforme especificado
- [ ] **REJEITAR** — Manter apenas 4 especialistas atuais
- [ ] **MODIFICAR** — Aprovar mas com ajustes: ___________

---

## ✅ MUDANÇA #2: EXPANDIR BMAD COM SHARDING EXPLÍCITO

### 📍 Localização
Modificar `especialistas[0].bmad.principios` — adicionar 5º princípio

### 🎯 Objetivo
Tornar explícito que BMAD usa Sharding para escalar 400+ lições sem perder contexto.

### 📝 Diff Exato

```diff
  - id: bmad
    ...
    principios:
      - {name: Agent as Code (AaC), ...}
      - {name: YAML-Based Workflows, ...}
      - {name: Single Orchestrator, ...}
      - {name: Federated Knowledge, ...}
+     - {name: Sharding & Context Engineering, desc: Fragmentar docs grandes em micro-universos atômicos. Cada shard contém APENAS contexto necessário evita overflow, app: North Star geral → L001 shard (objetivos+CPA) → L002 shard. 400 lições = 400 shards focados}
```

### 💡 Justificativa
- **DeepSeek cita:** "Sharding é vital... não podemos alimentar agente com todo currículo K-12 de uma vez"
- **Impact:** Documenta como Matemática Viva escala 0-18 anos tecnicamente
- **Alinhamento:** Princípio #5 North Star "Conexão 0-18 Anos" depende de Sharding

### 📊 Impacto
- **Linhas adicionadas:** +1 (inline)
- **Complexidade:** Baixa (apenas documentação)
- **Breaking change:** Não

### ✅ Aprovação
- [ ] **APROVAR** — Adicionar 5º princípio BMAD conforme especificado
- [ ] **REJEITAR** — Manter apenas 4 princípios atuais
- [ ] **MODIFICAR** — Aprovar mas com ajustes: ___________

---

## ✅ MUDANÇA #3: UPGRADE QA 5→7 PASSES (ADICIONAR REFLEXION + COVE)

### 📍 Localização
Adicionar **APÓS** `especialistas[3].qa.verificacao_quintupla` (5 passes existentes)

### 🎯 Objetivo
Expandir QA Quíntupla → QA Séptupla com mecanismos avançados de auto-crítica e verificação de cadeia.

### 📝 Diff Exato

```diff
  - id: qa
    ...
    verificacao_quintupla:
      - {pass: 1, name: SUPERFÍCIE, ...}
      - {pass: 2, name: CONSISTÊNCIA, ...}
      - {pass: 3, name: PEDAGÓGICO, ...}
      - {pass: 4, name: CPA, ...}
      - {pass: 5, name: UX FAMÍLIA, ...}
+   
+   verificacao_septupla_avancada:
+     nota: Passes 6-7 executados APÓS aprovar passes 1-5. Focam em loops meta-cognitivos.
+     
+     - pass: 6
+       name: REFLEXION
+       resp: Poetiq Reasoner
+       desc: Loop auto-crítica antes finalizar
+       steps:
+         - {n: 1, act: Gerar lição/código completo}
+         - {n: 2, act: Agente assume persona crítica analisa (tom/CPA/narrativa/lógica)}
+         - {n: 3, act: Corrigir baseado na crítica gerada}
+         - {n: 4, act: Persistir críticas úteis em memória longo prazo para evitar erros futuros}
+       checks: [Auto-crítica gerada?, Correções aplicadas?, Crítica persistida?]
+     
+     - pass: 7
+       name: CHAIN-OF-VERIFICATION (CoVe)
+       resp: Poetiq Reasoner
+       desc: Anti-alucinação matemática via verificação independente
+       steps:
+         - {n: 1, act: Rascunho matemático/narrativo pronto}
+         - {n: 2, act: Gerar 3-5 perguntas booleanas independentes para testar fatos (ex - Analogia preserva propriedade comutativa?)}
+         - {n: 3, act: Responder perguntas SEM ver rascunho original (evita viés confirmação)}
+         - {n: 4, act: Se discrepâncias detectadas corrigir rascunho}
+       checks: [Perguntas geradas?, Respondidas independentemente?, Inconsistências corrigidas?]
+     
+     criterio_aprovacao: Lição só publicada se passar TODOS 7 passes (score ≥90/100 em cada)
```

### 💡 Justificativa
- **DeepSeek método:** "Reflexion + CoVe são centrais para Poetiq... crítica verbal explícita"
- **Impacto:** Eleva rigor técnico de Matemática Viva ao nível de sistemas AGI research
- **ROI:** Maior proteção contra alucinações matemáticas (crítico para educação)

### 📊 Impacto
- **Linhas adicionadas:** +15
- **Complexidade:** Média-Alta (requer Poetiq specialist)
- **Breaking change:** Não (expande QA existente)

### ✅ Aprovação
- [ ] **APROVAR** — Adicionar passes 6-7 conforme especificado
- [ ] **REJEITAR** — Manter apenas 5 passes atuais
- [ ] **MODIFICAR** — Aprovar mas com ajustes: ___________

---

## ✅ MUDANÇA #4: ADICIONAR SEÇÃO RECURSIVE PEDAGOGICAL LOOP (RPL)

### 📍 Localização
Adicionar **NOVA SEÇÃO** após `protocolo_ativacao`, antes de `veto_coletivo`

### 🎯 Objetivo
Documentar formalmente o fluxo iterativo não-linear que Matemática Viva usa para criar lições.

### 📝 Diff Exato

```diff
protocolo_ativacao: |
  Ative Modo Engenharia: ...

+recursive_pedagogical_loop:
+  desc: Fluxo não-linear auto-corretivo criação lições. Itera até qualidade aprovada.
+  fases:
+    - {n: 1, name: Inicialização, agent: North Star, output: objetivo.md, ex: Ensinar Divisão Longa, dur: 5min}
+    - {n: 2, name: Planejamento, agent: Structuralist (Singapore), output: structure.md, note: Progressão C→P→A rigorosa, dur: 15min}
+    - {n: 3, name: Rascunho, agent: Storyteller (CM/Lewis), input: structure.md, output: lesson_draft_v1.md, dur: 30min}
+    - {n: 4, name: Reasoning Loop, agent: Poetiq Logician, act: Analisa V1 → Executa CoVe → Detecta erros → Gera feedback, dur: 10min}
+    - {n: 5, name: Refinamento, agent: Storyteller, input: feedback, output: lesson_draft_v2.md, trigger: Se score <90 volta aqui, dur: 20min}
+    - {n: 6, name: Aprovação Final, agent: Logician + QA, cond: Score ≥90/100 em TODOS 7 passes, output: lesson_final.md + publicação}
+  
+  metricas:
+    iteracoes_media: 2-3 ciclos fases 4-5 por lição
+    tempo_total: 1h-2h por lição (inclui iterações)
+    taxa_aprovacao_primeira: 30% (70% precisam refinamento)
+  
+  nota: Loop é RECURSIVO não linear. Fase 5 pode voltar para 4 múltiplas vezes. Fase 4 pode voltar para 2 se estrutura CPA estiver fundamentalmente falha.

veto_coletivo:
  ...
```

### 💡 Justificativa
- **DeepSeek propõe:** "Recursive Pedagogical Loop (RPL) — fluxo cíclico auto-corretivo"
- **Impacto:** Formaliza processo que já existe implicitamente, tornando-o replicável
- **Transparência:** Documenta SLA (tempo) e métricas (taxa aprovação)

### 📊 Impacto
- **Linhas adicionadas:** +12
- **Complexidade:** Média (requer compreender fluxo iterativo)
- **Breaking change:** Não (documentação adicional)

### ✅ Aprovação
- [ ] **APROVAR** — Adicionar RPL conforme especificado
- [ ] **REJEITAR** — Não adicionar (manter implícito)
- [ ] **MODIFICAR** — Aprovar mas com ajustes: ___________

---

## ✅ MUDANÇA #5: ADICIONAR 9º PRINCÍPIO NORTH STAR

### 📍 Localização
Modificar `alinhamento_north_star.principios` — adicionar 4º princípio

### 🎯 Objetivo
Expandir alinhamento com North Star incluindo filosofia de evolução contínua via Poetiq loops.

### 📝 Diff Exato

```diff
alinhamento_north_star:
  principios:
    - {id: 1, name: Qualidade Não Negociável, ...}
    - {id: 8, name: Norte Mínimo + Flexibilidade, ...}
    - {id: 5, name: Conexão 0-18 Anos, ...}
+   - {id: 9, name: Auto-Aperfeiçoamento Contínuo, como: Poetiq loops garantem sistema aprende cada lição. Estratégias eficazes persistem memória longo prazo reutilização. Sistema evolui 400+ lições sem repetir erros.}
  
- q_north_star: Este código funciona impecável para 400+ lições?
+ q_north_star: Este código funciona impecável E aprende/melhora sistema para próximas 400 lições?
```

### 💡 Justificativa
- **Filosofia CM:** "Habit is ten natures" — sistemas que aprendem criam hábitos melhores
- **Impacto:** Alinha Poetiq (técnico) com North Star (pedagógico)
- **Consistência:** Fecha loop conceitual BMAD→Poetiq→North Star

### 📊 Impacto
- **Linhas adicionadas:** +2
- **Complexidade:** Baixa
- **Breaking change:** Não

### ✅ Aprovação
- [ ] **APROVAR**
- [ ] **REJEITAR** 
- [ ] **MODIFICAR**: ___________

---

## 📊 TABELA RESUMO

| # | Mudança | Linhas | Complexidade | Prioridade |
|---|---------|--------|--------------|------------|
| 1 | Poetiq Reasoner | +20 | Alta | 🔴 Crítica |
| 2 | BMAD Sharding | +1 | Baixa | 🟡 Média |
| 3 | QA 7 Passes | +15 | Alta | 🔴 Crítica |
| 4 | RPL Loop | +12 | Média | 🟢 Baixa |
| 5 | 9º Princípio | +2 | Baixa | 🟡 Média |

**Total:** +50 linhas (129→179)

---

## 🎯 OPÇÕES GLOBAIS

**A) APROVAR TUDO** — 5 mudanças completas  
**B) CRÍTICAS (#1,#3)** — Apenas Poetiq + QA 7  
**C) COM MODIFICAÇÕES** — Ajustar conforme feedback  
**D) REJEITAR TUDO** — Manter v1.0 atual

Aguardando sua decisão! ✋
