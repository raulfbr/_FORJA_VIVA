# 🎯 ORCHESTRATOR: Análise Profunda — BMAD + Poetiq + Multi-Agentes

---
**Data:** 12/01/2026 às 19:25  
**Líder:** Orchestrator  
**Tema:** Evolução do Sistema Multi-Agentes da Forja Viva  
**Baseado em:** Texto.md + Pesquisa Web + Arquitetura Atual  

---

## 🔬 SUMÁRIO EXECUTIVO

O Maestro deseja evoluir o sistema de agentes da Forja Viva, inspirando-se no **BMAD Method** e potencialmente no **Poetiq.ai**, para criar um sistema multi-agentes que produza lições de alta fidelidade pedagógica.

Esta análise:
1. Compara o estado atual da Forja com frameworks de mercado
2. Identifica gaps e oportunidades
3. Propõe roadmap de evolução
4. Levanta perguntas estratégicas para decisão

---

## 📊 1. ESTADO ATUAL DA FORJA VIVA

### 1.1 O que Já Existe

| Componente | Status | Localização |
|------------|--------|-------------|
| 6 Agentes | ✅ Definidos | `forja-core/conselheiros/*.md` |
| Hierarquia | ✅ Clara | Maestro > Matriarca > Orchestrator > Agentes |
| LORE (dados) | ✅ YAML | `LORE/*.yaml` (6 arquivos, ~26KB) |
| Templates | ✅ V4 | `modelos/template-v4-sementes.md` |
| Workflows | ⚠️ Básicos | `workflows/cm-audit.md`, `pilot-sprint.md` |
| Pipeline | ⚠️ Manual | YAML → HTML via script Python |
| QA | ✅ Robusto | Verificação Quíntupla no `qa.md` |

### 1.2 O que Falta (Gaps Identificados)

| Gap | Impacto | Prioridade |
|-----|---------|------------|
| **Automação de fluxo** | Agentes não "conversam" sozinhos | 🔴 Alta |
| **Persistence/State** | Sem memória entre sessões | 🔴 Alta |
| **Loops de validação** | QA manual, não automático | 🟡 Média |
| **Sharding de contexto** | Perda de contexto em lições longas | 🟡 Média |
| **Expansion Pack** | Não há pacote empacotado | 🟢 Baixa |

---

## 🔍 2. ANÁLISE DO BMAD METHOD (v5/v6)

### 2.1 O que é o BMAD

O **BMAD Method** (Breakthrough Method for Agile AI-Driven Development) é um framework que:

| Conceito | Descrição | Aplicação para Forja |
|----------|-----------|----------------------|
| **Agent-as-Code** | Agentes definidos em Markdown + YAML | ✅ A Forja já faz isso! |
| **Agentic Planning** | Fase de planejamento colaborativo | ⚠️ Falta automatizar |
| **Context-Engineered Dev** | Stories com contexto completo embutido | ⚠️ Falta implementar |
| **Sharding** | Fragmentação de tarefas para evitar perda de contexto | ⚠️ Falta implementar |
| **Expansion Packs** | Módulos plugáveis por domínio | 🎯 Criar pack Matemática Viva |

### 2.2 Diferenças entre BMAD v5 e v6

| Aspecto | v5 | v6 |
|---------|-----|-----|
| **Foco** | Core workflow | Modularidade |
| **Agentes** | ~12 | ~19+ |
| **Workflows** | ~20 | ~50+ |
| **Web Bundles** | ❌ | ✅ (agentes como texto para ChatGPT) |
| **Scale-Adaptive** | ❌ | ✅ (Level 0-4 baseado em complexidade) |
| **CORE Engine** | Básico | Collaborative Optimization Reflection Engine |

### 2.3 O que Aprender do BMAD

1. **PRD antes de código** — Nenhum conteúdo sem especificação aprovada
2. **Story Files** — Cada tarefa tem TODO o contexto necessário
3. **Checkpoints humanos** — Human-in-the-loop em pontos críticos
4. **Determinismo** — Mesma entrada → mesma saída (via constraints)

---

## 🧠 3. ANÁLISE DO POETIQ.AI

### 3.1 O que é o Poetiq

O **Poetiq.ai** é um meta-sistema de raciocínio que:

| Conceito | Descrição | Aplicação para Forja |
|----------|-----------|----------------------|
| **Reasoning Loops** | Gera → Critica → Refina iterativamente | ✅ Perfeito para auditoria CPA |
| **Self-Auditing** | O sistema monitora sua própria qualidade | ✅ Automatiza o QA |
| **LLM-Agnostic** | Funciona sobre qualquer LLM base | ✅ Flexibilidade |
| **ARC-AGI** | 75% accuracy (supera humanos em alguns testes) | 🤔 Talvez overengineering |

### 3.2 Resultados do Poetiq

| Benchmark | Score | Contexto |
|-----------|-------|----------|
| ARC-AGI-2 Semi-Private | 54% | Superou Gemini 3 Deep Think |
| ARC-AGI-2 Public | 75% | Supera média humana (60%) |

### 3.3 Relevância para Matemática Viva

| Caso de Uso | Relevância | Justificativa |
|-------------|------------|---------------|
| **Validação lógica de problemas** | 🟡 Média | Lições de Sementes são simples |
| **Detecção de alucinação matemática** | 🟡 Média | CM + CPA já tem checklist |
| **Currículo adaptativo** | 🟢 Baixa (agora) | Fase 2+ do projeto |

### 3.4 Veredito Orchestrator sobre Poetiq

> **Poetiq é interessante, mas talvez seja OVERENGINEERING para a fase atual.**
>
> O Matemática Viva, na fase Sementes, trata de contagem de 0-10 e conceitos básicos.
> Os "Reasoning Loops" da Poetiq brilham em problemas complexos de lógica abstrata.
> 
> **Recomendação:** Revisitar Poetiq quando chegar ao ciclo Lógica (11-14 anos).

---

## 🛠️ 4. ALTERNATIVAS AO BMAD

### 4.1 CrewAI

| Aspecto | CrewAI | BMAD |
|---------|--------|------|
| **Complexidade** | Simples | Complexo |
| **Setup** | Minutos | Horas |
| **Comunidade** | Grande | Menor |
| **Educação** | Vários exemplos | Expansion pack |
| **Flexibilidade** | Alta | Mais estruturado |

**Uso para Forja:** Crews de agentes (ex: `crew_pedagogia`, `crew_narrativa`) que trabalham sequencial ou hierarquicamente.

### 4.2 LangGraph

| Aspecto | LangGraph | BMAD |
|---------|-----------|------|
| **Paradigma** | Grafo de estados | Documentos |
| **State Management** | Nativo | Manual |
| **Checkpointing** | Nativo (Postgres/Redis) | Não |
| **Observability** | LangSmith | Não |

**Uso para Forja:** Workflows como grafos com estado persistente e debugging visual.

### 4.3 Comparativo para Matemática Viva

| Framework | Melhor Para | Complexidade | Recomendação |
|-----------|------------|--------------|--------------|
| **BMAD** | Projetos grandes e estruturados | Alta | 🟡 Fase 2+ |
| **CrewAI** | MVP rápido com multi-agents | Média | 🟢 Começar aqui |
| **LangGraph** | Workflows com estado | Alta | 🟡 Se precisar de persistence |
| **Poetiq** | Raciocínio lógico complexo | Muito Alta | 🔴 Ciclo Lógica+ |

---

## ❓ 5. PERGUNTAS ESTRATÉGICAS PARA O MAESTRO

### 5.1 Sobre Prioridade

| # | Pergunta | Opções |
|---|----------|--------|
| 1 | **O que é mais urgente?** | A) Produzir L001-L040 manualmente<br>B) Investir em automação multi-agent |
| 2 | **Aceita curva de aprendizado?** | A) Quer algo que funcione hoje<br>B) Pode investir semanas em setup |
| 3 | **Qual o critério de sucesso?** | A) 40 lições até março<br>B) Sistema escalável para 1200+ |

### 5.2 Sobre Arquitetura

| # | Pergunta | Impacto |
|---|----------|---------|
| 4 | **Manter agentes em Markdown ou migrar?** | Markdown é portátil; Python/YAML é mais funcional |
| 5 | **Onde rodar os agentes?** | Local (Cursor/VSCode), Cloud (ChatGPT), Híbrido |
| 6 | **Precisa de memória entre sessões?** | Se sim, precisa de LangGraph ou similar |

### 5.3 Sobre Validação

| # | Pergunta | Trade-off |
|---|----------|-----------|
| 7 | **QA automático ou manual?** | Automático = setup; Manual = tempo por lição |
| 8 | **Quem valida a narrativa?** | Marina (Matriarca) ou agente simulado? |
| 9 | **Quanto erro é tolerável?** | Zero (precisa Veritas/Poetiq) ou Baixo (checklist)? |

---

## 🎯 6. GAPS IDENTIFICADOS NA FORJA ATUAL

### 6.1 Gap Crítico: Agentes Não Interagem

**Estado atual:** Agentes são documentos estáticos. Você (Maestro) atua como orquestrador manual.

**Problema:** Cada lição exige:
1. Invocar PM para planejar
2. Invocar Dev para escrever
3. Invocar QA para validar
4. Aprovar manualmente

**Solução proposta:** Workflow automatizado onde agentes passam artefatos entre si.

### 6.2 Gap Médio: Sem Sharding

**Estado atual:** Agentes recebem toda a lição de uma vez.

**Problema:** Para lições complexas (20+ min), o contexto pode se perder.

**Solução proposta:** Fragmentar lição em "Story Files" (BMAD) ou "Tasks" (CrewAI).

### 6.3 Gap Menor: Sem Expansion Pack Empacotado

**Estado atual:** Configurações espalhadas em vários arquivos.

**Problema:** Difícil replicar ou compartilhar o setup.

**Solução proposta:** Criar `bmad-matematica-viva/` ou `crewai-matviva/` empacotado.

---

## 📐 7. PROPOSTA DE ARQUITETURA EVOLUÍDA

### 7.1 Opção A: CrewAI Simples (MVP)

```
┌─────────────────────────────────────────────────────────┐
│  MAESTRO (Humano) — Aprova/Dirige                       │
├─────────────────────────────────────────────────────────┤
│  CREW: Produção de Lição                                │
│  ├── 📊 Agente PM → Gera PRD da lição (YAML)            │
│  ├── 🦁 Agente Narrador → Escreve narrativa             │
│  ├── 📐 Agente CPA → Valida fases C-P-A                 │
│  ├── 🛡️ Agente QA → Verificação Quíntupla              │
│  └── 📤 Agente Output → Gera YAML final                 │
└─────────────────────────────────────────────────────────┘
```

**Prós:** Rápido de implementar, comunidade ativa
**Contras:** Menos estruturado que BMAD

### 7.2 Opção B: BMAD Lite Adaptado

```
┌─────────────────────────────────────────────────────────┐
│  MAESTRO (Humano) — Aprova/Dirige                       │
├─────────────────────────────────────────────────────────┤
│  FASE 1: PLANNING                                       │
│  ├── Sofia (PM Pedagógico) → PeRD (Pedagogical RD)      │
│  ├── Euclides (Lógico) → Valida estrutura CPA           │
│  └── Checkpoint Humano → Maestro aprova                 │
├─────────────────────────────────────────────────────────┤
│  FASE 2: DEVELOPMENT                                    │
│  ├── Nexus (SM) → Cria Story Files                      │
│  ├── Artesão (Dev) → Escreve conteúdo                   │
│  ├── Ludus (UX) → Valida experiência                    │
│  └── Checkpoint Humano → Matriarca valida tom           │
├─────────────────────────────────────────────────────────┤
│  FASE 3: VERIFICATION                                   │
│  ├── Veritas (QA) → Simulação adversarial               │
│  └── Output → YAML + HTML                               │
└─────────────────────────────────────────────────────────┘
```

**Prós:** Estrutura clara, checkpoints humanos, escalável
**Contras:** Setup mais longo, curva de aprendizado

### 7.3 Opção C: LangGraph para Persistência

```
┌─────────────────────────────────────────────────────────┐
│  GRAFO DE ESTADOS                                       │
├─────────────────────────────────────────────────────────┤
│  Estado: lesson_draft                                    │
│  ├── Node: generate_prd                                 │
│  ├── Node: write_narrative                              │
│  ├── Node: validate_cpa                                 │
│  ├── Node: qa_audit                                     │
│  └── Node: finalize_yaml                                │
├─────────────────────────────────────────────────────────┤
│  Checkpointing: PostgreSQL                              │
│  Observability: LangSmith                               │
└─────────────────────────────────────────────────────────┘
```

**Prós:** Estado persistente, debugging visual, resume de falhas
**Contras:** Mais complexo, requer infra

---

## 📋 8. ROADMAP SUGERIDO

### 8.1 Fase 1: Fundação (Jan 2026)

| Semana | Tarefa | Entregável |
|--------|--------|------------|
| 1-2 | Decidir framework (CrewAI vs BMAD) | Decisão canonizada |
| 3-4 | Setup básico + 1 agente funcional | Prova de conceito |

### 8.2 Fase 2: MVP (Fev 2026)

| Semana | Tarefa | Entregável |
|--------|--------|------------|
| 5-6 | Implementar fluxo PM → Dev → QA | Pipeline funcional |
| 7-8 | Gerar L001-L005 via multi-agent | 5 lições piloto |

### 8.3 Fase 3: Escala (Mar 2026)

| Semana | Tarefa | Entregável |
|--------|--------|------------|
| 9-12 | Gerar L006-L040 Sementes | 40 lições |
| Contínuo | Refinar prompts e qualidade | Melhoria contínua |

---

## 🔑 9. INSIGHTS NÃO MENCIONADOS NO TEXTO ORIGINAL

### 9.1 PADR — Pedagogical Architecture Decision Records

**Ideia do relatório Gemini:** Criar registros de decisão pedagógica, como ADRs de software.

**Aplicação:** Cada decisão sobre CPA, narrativa ou adaptação é documentada com:
- Contexto
- Alternativas consideradas
- Decisão final
- Justificativa pedagógica

**Onde implementar:** `docs/adrs/PADR-001-cpa-integrado.md`

### 9.2 Simulate-Student-Misconception

**Ideia:** O agente Veritas simula erros comuns de alunos para testar se a lição lida bem com eles.

**Exemplo:** Se a lição ensina 3-7, Veritas simula um aluno que sempre subtrai menor do maior e verifica se há feedback explicativo.

### 9.3 Currículo Infinito (Fase Futura)

**Ideia:** Com validação matemática automatizada, o sistema pode gerar problemas intermediários sob demanda.

**Aplicação futura:** Se um aluno trava na transição barras → números, gerar 10 problemas extras automaticamente.

### 9.4 Web Bundles (BMAD v6)

**Ideia:** Compilar agentes em arquivos de texto que funcionam em ChatGPT Custom GPTs.

**Aplicação:** Criar um "GPT Matemática Viva" que famílias podem usar para tirar dúvidas.

---

## ✅ 10. CONCLUSÕES DO ORCHESTRATOR

### 10.1 O que Fazer AGORA

| Ação | Motivo |
|------|--------|
| Decidir: CrewAI ou BMAD ou Manual | Framework define tudo |
| Responder as 9 Perguntas da Seção 5 | Clarificam escopo |
| Criar 1 lição piloto com multi-agent | Validar approach |

### 10.2 O que NÃO Fazer Agora

| Evitar | Motivo |
|--------|--------|
| Integrar Poetiq.ai | Overengineering para Sementes |
| Setup LangGraph completo | Complexo demais para MVP |
| Criar expansion pack antes de validar | Prematuro |

### 10.3 Recomendação Final

> **Opção A (CrewAI Simples)** para o MVP.
> 
> É mais rápido de implementar, tem comunidade ativa, e permite validar a ideia antes de investir em arquitetura pesada.
> 
> **Migrar para BMAD v6** se o projeto escalar para 100+ lições com múltiplos colaboradores.

---

## 📌 11. PRÓXIMOS PASSOS (AÇÕES CONCRETAS)

1. [ ] **Maestro responde as 9 perguntas** da Seção 5
2. [ ] **Escolher framework** (CrewAI recomendado para MVP)
3. [ ] **Criar 1 agente funcional** (ex: Narrador Guardiões)
4. [ ] **Gerar L001 via multi-agent** como piloto
5. [ ] **Documentar decisões** em PADR

---

> *"Não busque a perfeição do sistema antes de produzir a primeira lição. Um sistema perfeito que não produz nada é pior que um sistema imperfeito que entrega valor."*
> — Orchestrator, 12/01/2026

---

## 📝 12. RESPOSTAS DO MAESTRO (19:43)

### 12.1 Perguntas Respondidas

| # | Pergunta | Resposta do Maestro |
|---|----------|---------------------|
| 1 | O que é mais urgente? | **B) Automação multi-agent** |
| 2 | Aceita curva de aprendizado? | **B) Pode investir tempo** — visando qualidade |
| 3 | Critério de sucesso? | **B) Sistema escalável para 1200+** com alta qualidade |
| 4 | Markdown ou funcional? | **Funcional/Qualidade** |
| 5 | Onde rodar? | **Local VSCode** — tem PRO com Claude Opus 4.5 e Gemini 3 PRO |
| 6 | Memória entre sessões? | **Não per se** — usar arquivos base + resumos a cada 5-10 lições |
| 7 | QA automático ou manual? | **Por lição feita** — workflow de discussão entre agentes |

### 12.2 Decisões Estratégicas do Maestro

| Decisão | Detalhe |
|---------|---------|
| **Framework** | ✅ BMAD v6 (maior qualidade multi-agent) |
| **Poetiq** | 🟡 Reservar para ciclo Lógica (11-14 anos) |
| **CM como Coordenadora** | ✅ CM direciona a Tríade; em conflito CM > Singapura |
| **Memória** | ✅ Resumos detalhados a cada 5-10 lições |
| **Documentar pensamentos** | ✅ PADR — registrar raciocínio para consulta |
| **Simulate-Student-Misconception** | 🟡 Interessante mas não prioridade inicial |
| **Currículo Infinito** | 🟡 Fase futura — aprendizado narrado (consultar CM) |
| **Web Bundles** | 🟡 2ª ou 3ª fase — auxiliar famílias |

### 12.3 Princípio Central: CM Coordena Tudo

> **Exemplo dado pelo Maestro:**
> 
> "Singapura acha que 5/6 anos já tem que ir pro Pictórico, enquanto CM quer só CONCRETO.
> Logo é **só Concreto**. A base tem que ser o que a CM ordenar, com embasamento."

**Hierarquia Pedagógica Canonizada:**
```
CHARLOTTE MASON (Coordenadora)
    ↓
    ├── Direciona CPA (Singapura)
    ├── Direciona TGTB (Scope & Sequence)
    └── Tem VETO final em conflitos
```

---

## 🎯 13. MESA DOS AGENTES — DELIBERAÇÃO BMAD v6

**Data:** 12/01/2026 às 19:50  
**Convocados:** PM, SM, Dev, QA, Ops  
**Líder:** Orchestrator  
**Tema:** Implementação BMAD v6 para Forja Viva  

---

### 🎯 ORCHESTRATOR: Abertura

> "O Maestro decidiu: BMAD v6, automação multi-agent, escalável para 1200+ lições, 
> CM como coordenadora da Tríade. Local VSCode com Claude Opus 4.5 / Gemini 3 PRO.
> Memória via resumos a cada 5-10 lições. Vamos deliberar sobre a implementação."

---

### 📊 PM: Análise de Viabilidade

**Sobre BMAD v6 no VSCode:**
> "O BMAD v6 é framework de documentos (Markdown + YAML). Não precisa de infra externa.
> Roda 100% local via prompts estruturados. Perfeito para VSCode."

**Sobre LangGraph:**
> "LangGraph core é open-source. O que é pago é LangSmith (observability).
> Para memória simples, podemos usar arquivos JSON/YAML como checkpoints."

**Proposta PM:**
| Componente | Implementação |
|------------|---------------|
| Agentes | Markdown + YAML frontmatter (BMAD style) |
| Workflows | Prompts estruturados em cadeia |
| Memória | Resumos YAML a cada 5-10 lições |
| Observability | Logs Markdown (já fazemos!) |

---

### 🔨 SM: Estrutura de Workflows

**Workflow Proposto: "Lição Premium"**
```
┌─────────────────────────────────────────────────────────────┐
│  WORKFLOW: CRIAR LIÇÃO PREMIUM                              │
├─────────────────────────────────────────────────────────────┤
│  FASE 1: PLANEJAMENTO (CM Valida)                            │
│  ├── 1. PM → Recebe tema + ciclo                            │
│  ├── 2. Sofia (Pedagogo CM) → Define Ideia Viva + estrutura │
│  ├── 3. Euclides (CPA) → Propõe fases C-P-A                 │
│  ├── 4. CM (Coordenadora) → VETA ou APROVA                  │
│  └── 5. Output → PeRD (Pedagogical Requirements Doc)        │
├─────────────────────────────────────────────────────────────┤
│  FASE 2: DESENVOLVIMENTO                                    │
│  ├── 6. Artesão (Dev) → Escreve narrativa com Guardiões     │
│  ├── 7. Tolkien → Valida consistência do Reino              │
│  ├── 8. Lewis → Valida tom (dignidade da criança)           │
│  ├── 9. CM → Revisa fluxo e lições embutidas                │
│  └── 10. Output → Rascunho YAML                             │
├─────────────────────────────────────────────────────────────┤
│  FASE 3: VERIFICAÇÃO (QA Quíntupla)                         │
│  ├── 11. Veritas (QA) → 5 verificações                      │
│  │       ├── CM: 20 Princípios                              │
│  │       ├── CPA: Ordem correta                             │
│  │       ├── Tempo: 15-20 min                               │
│  │       ├── Guardiões: Frases corretas                     │
│  │       └── Template: V4 completo                          │
│  ├── 12. Matriarca → Valida tom e confiança para pais       │
│  └── 13. Output → YAML Final + HTML                         │
└─────────────────────────────────────────────────────────────┘
```

---

### ⚒️ DEV: Estrutura de Agentes BMAD

**Proposta de Agentes (Expansion Pack Matemática Viva):**

| # | Agente | Função | Especialistas Invocados |
|---|--------|--------|-------------------------|
| 1 | **Sofia** | Arquiteta Pedagógica | CM (20 Princípios) |
| 2 | **Euclides** | Especialista CPA | Bruner, Vygotsky |
| 3 | **Artesão** | Escritor de Narrativas | Tolkien, Lewis, Potter |
| 4 | **Veritas** | Auditor QA | CM, Bruner, Fujimura |
| 5 | **Nexus** | Orquestrador/SM | Gerencia fluxo |
| 6 | **Mordomo** | Ops/Documentação | Arquiva e versiona |

**Estrutura de Diretórios Proposta:**
```
_FORJA_VIVA/
├── .bmad/                          # NOVO: Núcleo BMAD
│   ├── agents/                     # Definições dos agentes
│   │   ├── sofia.md               # Arquiteta Pedagógica (CM)
│   │   ├── euclides.md            # Especialista CPA
│   │   ├── artesao.md             # Escritor Narrativo
│   │   ├── veritas.md             # Auditor QA
│   │   ├── nexus.md               # Orquestrador
│   │   └── mordomo.md             # Ops
│   ├── workflows/                  # Definições de processos
│   │   ├── criar-licao-premium.md
│   │   └── criar-resumo-memoria.md
│   ├── templates/                  # Templates de output
│   │   ├── perd-template.yaml     # Pedagogical RD
│   │   ├── licao-template.yaml    # Output de lição
│   │   └── resumo-memoria.yaml    # Template de resumo
│   └── expansion-packs/
│       └── matematica-viva/       # Pack customizado
│           ├── README.md
│           ├── triade.yaml        # CM + CPA + TGTB
│           └── guardioes.yaml     # Referência aos 5
├── LORE/                           # Dados (já existe)
├── forja-core/                     # Agentes antigos (migrar)
└── memoria/                        # NOVO: Resumos de lições
    ├── sementes/
    │   ├── resumo-L001-L005.yaml
    │   ├── resumo-L006-L010.yaml
    │   └── ...
    └── raizes/
```

---

### 🛡️ QA: Validação CM como Coordenadora

**Regras de Veto (CM > Outros):**

| Conflito | Decisão | Justificativa CM |
|----------|---------|------------------|
| Singapura quer Pictórico aos 5 anos | ❌ Só Concreto | "Things before Signs" |
| TGTB sugere velocidade maior | ❌ Manter ritmo CM | "Lições curtas, hábito da atenção" |
| Dev quer explicar demais | ❌ Narrar, não explicar | "A criança digere ideias" |

**Implementação no Agente Sofia:**
```yaml
veto_rules:
  - trigger: "pictorial_before_concrete"
    action: REJECT
    reason: "CM Princípio: Things before Signs"
    
  - trigger: "lesson_too_long"
    action: REJECT
    reason: "CM Princípio 13: Lições curtas"
    
  - trigger: "over_explanation"
    action: REJECT
    reason: "CM: Apresentar, não explicar"
```

---

### 🗂️ OPS: Sistema de Memória

**Proposta: Resumos a cada 5 lições**

| Lições | Arquivo | Conteúdo |
|--------|---------|----------|
| L001-L005 | `resumo-L001-L005.yaml` | Conceitos, guardiões usados, decisões |
| L006-L010 | `resumo-L006-L010.yaml` | Referências a lições anteriores |

**Estrutura do Resumo:**
```yaml
# memoria/sementes/resumo-L001-L005.yaml
meta:
  ciclo: Sementes
  range: L001-L005
  data_criacao: 2026-01-15
  
conceitos_introduzidos:
  - {licao: L001, conceito: "Contagem 1-3", guardiao: Celeste}
  - {licao: L002, conceito: "Contagem 4-5", guardiao: Bernardo}
  
decisoes_pedagogicas:
  - {licao: L003, decisao: "Só manipulativos, sem desenho", justificativa: "CM veto"}
  
arcos_narrativos:
  - {inicio: L001, fim: L005, arco: "Primeiros passos no Ninho"}
  
referencias_futuras:
  - {para_licao: L006, referencia: "Celeste menciona o que aprenderam"}
```

---

### 🎯 ORCHESTRATOR: Síntese e Decisões

**Decisões Tomadas pela Mesa:**

| # | Decisão | Responsável |
|---|---------|-------------|
| 1 | Criar pasta `.bmad/` com estrutura BMAD v6 | Dev |
| 2 | Criar 6 agentes especializados | Dev |
| 3 | CM é coordenadora com poder de VETO | QA (implementar) |
| 4 | Memória via resumos YAML a cada 5 lições | Ops |
| 5 | Workflow "Lição Premium" como padrão | SM |
| 6 | Documentar decisões em PADR | PM |

**Próximos Passos Concretos:**

1. [ ] **Criar estrutura `.bmad/`** na Forja
2. [ ] **Criar agente Sofia** (CM Coordinator) — mais importante
3. [ ] **Criar agente Euclides** (CPA Expert)
4. [ ] **Criar agente Artesão** (Narrative Writer)
5. [ ] **Criar agente Veritas** (QA Quíntupla)
6. [ ] **Criar workflow `criar-licao-premium.md`**
7. [ ] **Testar com L001** como piloto

---

### 📌 VEREDITO FINAL DA MESA

> **BMAD v6 é viável e será implementado.**
>
> - Roda 100% local no VSCode
> - Usa Claude Opus 4.5 / Gemini 3 PRO como backend
> - Agentes em Markdown + YAML (portáveis)
> - CM coordena a Tríade com poder de VETO
> - Memória via resumos estruturados a cada 5 lições
>
> **Poetiq reservado para ciclo Lógica (fase futura).**

---

> *"A estrutura está definida. Agora é criar os agentes e testar."*
> — Mesa dos Agentes, 12/01/2026
