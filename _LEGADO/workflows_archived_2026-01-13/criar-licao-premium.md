---
workflow:
  name: criar-licao-premium
  id: WF-001
  title: Criar Lição Premium — Workflow Multi-Agent
  description: Workflow completo para criar uma lição de alta qualidade com todos os agentes deliberando.
  version: 1.0
  
phases:
  - id: P1
    name: PLANEJAMENTO
    description: Definir estrutura pedagógica com validação CM
    steps:
      - step: 1
        agent: PM/User
        action: "Fornecer tema + ciclo + número da lição"
        input: "Ex: Contagem 1-3, Sementes, L001"
        output: "Solicitação inicial"
        
      - step: 2
        agent: Sofia
        action: "Definir Ideia Viva + estrutura pedagógica"
        invoke: "Ative a Sofia (CM Coordinator) para definir a Ideia Viva"
        output: "Ideia Viva + estrutura aprovada"
        
      - step: 3
        agent: Euclides
        action: "Propor fases CPA"
        invoke: "Ative Euclides para propor as fases CPA"
        note: "Sementes = só Concreto (CM override)"
        output: "Proposta CPA"
        
      - step: 4
        agent: Sofia
        action: "VETO CHECK"
        decide: "Aprovar ou vetar proposta CPA"
        output: "PeRD (Pedagogical Requirements Doc)"
        checkpoint: HUMANO_OPCIONAL
        
  - id: P2
    name: DESENVOLVIMENTO
    description: Escrever narrativa com Guardiões
    steps:
      - step: 5
        agent: Artesão
        action: "Escrever narrativa com Guardião líder"
        invoke: "Ative o Artesão para escrever a narrativa"
        input: "PeRD + Guardião definido"
        output: "Rascunho narrativo"
        
      - step: 6
        agent: Lewis/Tolkien/Potter
        action: "Validar tom e consistência"
        questions:
          - "Infantilizamos o Mistério? (Lewis)"
          - "Há contradição lógica? (Tolkien)"
          - "Visual honra a natureza? (Potter)"
        output: "Narrativa validada"
        
      - step: 7
        agent: Sofia
        action: "Revisar lições embutidas"
        focus: "CM embedded in story"
        output: "Narrativa aprovada por CM"
        checkpoint: HUMANO_OPCIONAL
        
  - id: P3
    name: VERIFICAÇÃO
    description: QA Quíntupla + aprovação final
    steps:
      - step: 8
        agent: Veritas
        action: "Executar Verificação Quíntupla"
        invoke: "Ative Veritas para executar QA Quíntupla"
        checks:
          - "V1: CM (20 Princípios)"
          - "V2: CPA (ordem correta)"
          - "V3: Tempo (≤20 min Sementes)"
          - "V4: Guardiões (frases e tom)"
          - "V5: Template V4 (seções completas)"
        output: "Relatório QA"
        
      - step: 9
        condition: "Se Veritas reprovou"
        action: "Retornar para agente responsável"
        loop_to: "Step correspondente ao problema"
        
      - step: 10
        condition: "Se Veritas aprovou"
        agent: Matriarca
        action: "Validação final de tom e confiança para pais"
        checkpoint: HUMANO_RECOMENDADO
        
  - id: P4
    name: OUTPUT
    description: Gerar outputs finais
    steps:
      - step: 11
        agent: Mordomo
        action: "Gerar YAML final"
        output: "licao-XXX.yaml"
        
      - step: 12
        agent: Mordomo
        action: "Converter para HTML"
        output: "licao-XXX.html"
        
      - step: 13
        agent: Mordomo
        action: "Arquivar e versionar"
        output: "Commit no repositório"

checkpoints:
  - type: HUMANO_OPCIONAL
    description: "Maestro pode revisar, mas não obrigatório"
    
  - type: HUMANO_RECOMENDADO
    description: "Marina (Matriarca) deve revisar tom"
    
  - type: HUMANO_OBRIGATORIO
    description: "Não avançar sem aprovação humana"

invocation:
  full_workflow: |
    ## 🎯 WORKFLOW: CRIAR LIÇÃO PREMIUM
    
    **Tema:** [descrever]
    **Ciclo:** [Sementes/Raízes/Lógica/Legado]
    **Número:** [L001, L002, etc]
    **Guardião Líder:** [sugerido ou definido]
    
    ### Iniciar Workflow
    
    Por favor, execute o workflow `criar-licao-premium` com os agentes:
    1. Sofia → Definir Ideia Viva e estrutura
    2. Euclides → Propor CPA (respeitando veto CM)
    3. Artesão → Escrever narrativa
    4. Veritas → Verificação Quíntupla
    
    Ao final, gere o YAML da lição.

templates:
  perd: |
    # PeRD — Pedagogical Requirements Document
    
    **Lição:** [ID]
    **Ciclo:** [nome]
    **Tema:** [descrição]
    
    ## Ideia Viva (Sofia)
    [Uma frase que captura a essência]
    
    ## Estrutura CPA (Euclides)
    - **Concreto:** [manipulativos]
    - **Pictórico:** [VETADO POR CM se Sementes]
    - **Abstrato:** [mínimo]
    
    ## Guardião Líder (Artesão)
    - **Nome:** [guardião]
    - **Frase:** [assinatura oficial]
    - **Tom:** [descrição]
    
    ## Validação CM (Sofia)
    - [ ] Criança como pessoa
    - [ ] Lição curta
    - [ ] Narração presente
    - [ ] Ideia Viva apresentada
    
    **Status:** [APROVADO / EM REVISÃO]
---

# 🎯 WORKFLOW: CRIAR LIÇÃO PREMIUM

> *"Uma lição premium não é acidente. É o produto de vários especialistas deliberando."*

## Visão Geral

Este workflow orquestra todos os agentes BMAD para criar uma lição de alta qualidade.

## Fluxo Visual

```
┌─────────────────────────────────────────────────────────┐
│  FASE 1: PLANEJAMENTO                                   │
│  PM → Sofia → Euclides → Sofia (VETO) → PeRD           │
├─────────────────────────────────────────────────────────┤
│  FASE 2: DESENVOLVIMENTO                                │
│  Artesão → Lewis/Tolkien/Potter → Sofia → Rascunho     │
├─────────────────────────────────────────────────────────┤
│  FASE 3: VERIFICAÇÃO                                    │
│  Veritas (Quíntupla) → [Loop se falhar] → Matriarca    │
├─────────────────────────────────────────────────────────┤
│  FASE 4: OUTPUT                                         │
│  Mordomo → YAML → HTML → Arquivar                      │
└─────────────────────────────────────────────────────────┘
```

## Como Usar

### Comando Rápido

```
Execute o workflow criar-licao-premium:
- Tema: [seu tema]
- Ciclo: Sementes
- Lição: L001
```

### Comando Completo

```
## INICIAR WORKFLOW: CRIAR LIÇÃO PREMIUM

**Input:**
- Tema: Contagem de 1 a 3
- Ciclo: Sementes
- Número: L001
- Guardião: Celeste

**Agentes a invocar em sequência:**
1. Sofia (Ideia Viva + estrutura)
2. Euclides (CPA, respeitando CM)
3. Artesão (narrativa com Celeste)
4. Veritas (QA Quíntupla)

Ao final, gere o YAML completo da lição.
```

## Outputs Esperados

| Fase | Output |
|------|--------|
| P1 | PeRD (Pedagogical Requirements Doc) |
| P2 | Rascunho narrativo |
| P3 | Relatório QA (aprovado/reprovado) |
| P4 | YAML + HTML finais |
