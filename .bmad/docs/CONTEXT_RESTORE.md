# 📋 CONTEXT RESTORE — Sistema de Experts BMAD v6
**Data**: 12/01/2026 23:27
**Sessão**: Revisão e Expansão dos Experts

---

## ✅ O QUE FOI FEITO

### 1. Expansão Robusta de 6 Experts (Pesquisas Externas)

| Expert | Antes | Depois | Conteúdo Pesquisado |
|--------|-------|--------|---------------------|
| susan_macaulay | 50 | 204 | Citações "For the Children's Sake" |
| lev_vygotsky | 68 | 230 | ZPD, Scaffolding, Productive Struggle |
| seth_godin | 59 | 220 | Tribes, Permission Marketing |
| alex_hormozi | 64 | 260 | Value Equation ($100M Offers) |
| peter_thiel | 59 | 325 | Secrets, Monopoly, Definite Optimism |
| maes_personas | 105 | 418 | 6ª persona Mariana, selos_acessibilidade |

### 2. Padronização de TODOS os 14 Experts

Adicionado a cada expert:
- `alinhamento_north_star` (mapeia 2-3 princípios do North Star)
- `pergunta_north_star` (pergunta de validação específica)
- `referencias` (fontes primárias e secundárias)

### 3. Correção Crítica em Mães Personas

- `selos_inclusao` → `selos_acessibilidade`
- Nota clara: "ISTO NÃO É SOBRE GÊNERO GRAMATICAL"
- É sobre ACESSIBILIDADE FÍSICA para crianças como Bernardo

---

## 📁 ESTRUTURA ATUAL DOS EXPERTS

```
.bmad/experts/
├── pedagogia/
│   ├── charlotte_mason.yaml   # Coordenadora, veto final (380 linhas)
│   └── susan_macaulay.yaml    # Tradutora CM (204 linhas)
├── matematica/
│   ├── jerome_bruner.yaml     # Arquiteto CPA (237 linhas)
│   └── lev_vygotsky.yaml      # Scaffolding (230 linhas)
├── narrativa/
│   ├── cs_lewis.yaml          # Dignidade (213 linhas)
│   ├── jrr_tolkien.yaml       # Consistência (175 linhas)
│   ├── beatrix_potter.yaml    # Estética (198 linhas)
│   └── makoto_fujimura.yaml   # Beleza Generativa (197 linhas)
├── negocios/
│   ├── seth_godin.yaml        # Tribes (220 linhas)
│   ├── alex_hormozi.yaml      # Value Equation (260 linhas)
│   └── peter_thiel.yaml       # Monopoly (325 linhas)
├── design/
│   └── design.yaml            # Design System (348 linhas)
├── engenharia/
│   └── engenharia.yaml        # BMAD + QA (422 linhas)
└── ux_familias/
    └── maes_personas.yaml     # 6 Personas (418 linhas)
```

**Total: 14 experts, 3.000+ linhas**

---

## 🎯 PRÓXIMO PASSO: COMO UTILIZAR OS EXPERTS

### Questão Central
> "Como podemos INVOCAR e UTILIZAR esses experts no workflow de criação de lições?"

### Ideias Preliminares

#### 1. Workflow `/criar-licao-premium`
- Atualizar para invocar experts relevantes
- Cada fase da lição consulta experts específicos
- Validação final passa por todos os vetos

#### 2. Sistema de Deliberação BMAD
- Charlotte Mason sempre tem veto final
- Experts são invocados por domínio:
  - Pedagogia → CM, Susan Macaulay
  - Matemática → Bruner, Vygotsky
  - Narrativa → Lewis, Tolkien, Potter, Fujimura
  - UX → Mães Personas

#### 3. Integração com Orchestrator
- O arquivo `.bmad/orchestrator.yaml` pode coordenar
- Definir quais experts são invocados em cada tarefa

#### 4. Perguntas de Validação por Expert
Cada expert tem uma `pergunta_north_star` que pode ser usada como checklist:
- CM: "Esta lição trata a criança como PESSOA?"
- Bruner: "A progressão CPA foi respeitada?"
- Lewis: "O tom é digno, nunca condescendente?"
- Hormozi: "Esforço logístico baixo, relacional preservado?"
- Mães: "Funciona em 5 min com bebê no colo?"

---

## 📝 TAREFAS PENDENTES PARA PRÓXIMA SESSÃO

### Alta Prioridade
1. [ ] Definir como invocar experts no workflow
2. [ ] Atualizar `/criar-licao-premium` com deliberação
3. [ ] Testar workflow com lição piloto (L001)

### Média Prioridade
4. [ ] Criar sistema de veto em cascata
5. [ ] Documentar protocolo de deliberação
6. [ ] Integrar com orchestrator.yaml

### Exploração
7. [ ] Como usar `pergunta_north_star` de cada expert?
8. [ ] Como registrar decisões de veto?
9. [ ] Como fazer experts "conversarem" entre si?

---

## 🔑 NOSSO SEGREDO (Peter Thiel)

```
"Matemática é LINGUAGEM POÉTICA, não técnica.
Crianças aprendem melhor através de NARRATIVA IMERSIVA.
Ninguém está combinando CM + Singapore + Storytelling assim."
```

Este é nosso MONOPÓLIO CRIATIVO.

---

## 📌 ARQUIVOS RELEVANTES

- `.bmad/orchestrator.yaml` — Orquestrador central
- `.bmad/workflows/criar-licao-premium.md` — Workflow de criação
- `LORE/north_star.yaml` — 8 Princípios norteadores
- `.bmad/experts/**/*.yaml` — Todos os 14 experts
