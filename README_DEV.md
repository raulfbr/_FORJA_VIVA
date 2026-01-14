# 📐 MATEMÁTICA VIVA — Arquitetura Multi-Agent & Evolução do Projeto

[![BMAD Framework](https://img.shields.io/badge/BMAD-v6.0-blue)](https://bmadcodes.com)
[![YAML Lean](https://img.shields.io/badge/YAML%20Lean-v1.0-green)](.bmad/docs/)
[![Multi-Agent](https://img.shields.io/badge/experts-14%2B-purple)](.bmad/experts/)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)](LICENSE)

> **📚 Para famílias e educadores:** Leia o [README principal](README.md)  
> **💻 Para desenvolvedores e pesquisadores:** Este documento explica a **arquitetura multi-agent** e a evolução da pesquisa

---

## 🎯 Propósito deste README

**Este projeto demonstra** uma arquitetura de **orquestração multi-agent** aplicada a conteúdo educacional de qualidade impecável — um caso de uso real de BMAD Framework v6 em produção.

**Se você está interessado em:**
- Entender como **14+ especialistas AI** colaboram via YAML
- Ver evolução de **PAINEL-ESPECIALISTAS.md** → **BMAD v6** → **YAML Lean v1.0**
- Aprender **SSOT/DRY/YAGNI** em contexto educacional real
- Contribuir para **arquitetura e metodologia** multi-agent

**Você está no lugar certo.** Continue lendo.

---

## 🧬 A Evolução: De Painel a Orquestração Multi-Agent

### Fase 1: PAINEL-ESPECIALISTAS.md (Arquivado)

**Início:** Gemini 3.0 Experimental + Antigravity  
**Formato:** Markdown com lista de 22+ especialistas (520 linhas)  
**Limitações:** Estático, sem orquestração, consulta manual  
**Propósito:** Documentação inicial de personas para simulação de consultoria

**Ver arquivo histórico completo:** `_ARQUIVADO/PAINEL-ESPECIALISTAS.md`

### Fase 2: BMAD Framework Adotado

**Transição:** Descoberta do BMAD (_Breakthrough Method for Agile AI-Driven Development_)  
**Ganho:** Agent as Code (AaC) — Especialistas viram **arquivos YAML declarativos**

### Fase 3: YAML Lean v1.0 (Atual)

**AI Colaboradores:** Gemini 3.0 Antigravity → **Claude Opus 4.5 (Extended Thinking)**  
**Conquista:** 87% projeto convertido (21 arquivos, 68% redução, zero perda)  
**Status:** Produção, orquestração funcional, deliberações formais documentadas

---

## 🏗️ Arquitetura Multi-Agent (BMAD v6)

### Conceito Central: Agent as Code (AaC)

**Cada especialista é um arquivo YAML** com:
- Biografia e contexto
- Princípios fundamentais
- Poder de veto (hierarquia definida)
- Citações autênticas
- Aplicações práticas

**Exemplo:** `.bmad/experts/pedagogia/charlotte_mason.yaml`

```yaml
id: charlotte_mason
tipo: expert
conselho: pedagogia
role: coordenadora
nome: Charlotte Maria Shaw Mason
nasc: 1842
falec: 1923

principios_20:
  - {n: 1, p: Children are born persons, ...}
  - {n: 2, p: Not born good or bad..., ...}
  ...

veto:
  pode: true
  pri: 1
  authority: VETO_FINAL
```

### 14+ Especialistas com Pesquisa Intensiva

Cada expert foi baseado em **pesquisa profunda** de obras originais:

| Expert | Obras Consultadas | Linhas YAML |
|--------|-------------------|-------------|
| **Charlotte Mason** | 6 volumes (Home Education, Philosophy of Education, etc.) | 128 |
| **Jerome Bruner** | Process of Education, Toward a Theory of Instruction | 68 |
| **CS Lewis** | Abolition of Man, Chronicles of Narnia, On Stories | 70 |
| **JRR Tolkien** | On Fairy-Stories, Letters, Silmarillion | 59 |
| **Seth Godin** | Tribes, Purple Cow, This is Marketing | 82 |
| **Peter Thiel** | Zero to One, entrevistas, Stanford lectures | 87 |
| ... | ... | ... |

**Total:** 1185 linhas de especialização curada (após YAML Lean v1.0)

### Orquestração: orchestrator.yaml

Coordena colaboração entre experts:
- Invoca especialistas relevantes por domínio
- Gerencia contexto entre workflows
- Previne conflitos (SSOT enforcement)
- Registra deliberações formais

---

## 🔄 Workflows Declarativos

### 1. criar-licao-premium.yaml

**3 Fases, 11 Passos, 2 Checkpoints**

```
PLANEJAMENTO → DESENVOLVIMENTO → VALIDAÇÃO
(CM+Bruner+Vygotsky) (Lewis+Tolkien+Potter) (Fujimura+Eng+Mães)
```

### 2. reuniao-deliberacao.yaml

**6 Fases Debate Estruturado**

Quando questão complexa exige conselho formal:

1. **ABERTURA** — CM apresenta tema
2. **POSIÇÕES INICIAIS** — Experts manifestam fundamentados
3. **RÉPLICA** — Questionam uns aos outros
4. **TRÉPLICA** — Ajustam ou defendem posição
5. **SÍNTESE** — CM organiza convergências
6. **DECISÃO** — CM decide (voz final)

**Exemplo real:** `logs/Upgrade_YAML_Lean/2026-01-13_2057_DELIBERACAO_REVISAR_LICAO_AUTO.md`

### 3. revisar-licao-auto.yaml

**4 Fases, 4 Níveis Veto, 14 Experts Invocados**

Validação automática multi-expert antes humano.

### 4. revisar-pontos.yaml

**13 Pontos Críticos Auditados**

Pedagogia (P1-P3), Narrativa (N1-N3), Estética (E1-E3), Usabilidade (U1-U3)

---

## 💡 YAML Lean v1.0 — Conquista Técnica

### O Desafio

YAMLs verbose (média 220L/expert) → Manutenção difícil, leitura lenta

### A Solução

Conversão para **YAML Lean v1.0** preservando TODA semântica:

**Antes (verbose):**
```yaml
biografia:
  nascimento: 1960
  nacionalidade: Americano
  profissao: Autor e Empresário
  ...
```

**Depois (lean):**
```yaml
nasc: 1960
nac: Americano
prof: Autor Empresário
...
```

### Resultados

- **21 conversões** (14 experts + 2 groups + 4 workflows + 3 templates)
- **4857 → 1562 linhas** (68% redução média)
- **6 correções** vigilantes aplicadas (zero perda final)
- **100% YAML válido** (Python yaml.safe_load())

**Princípios:**
1. **SSOT** — Cada dado UM lugar (Eric Evans DDD)
2. **DRY** — Don't Repeat Yourself
3. **AI Eficiência** — `view_file` direto economiza 3-5s/expert

---

## 🗂️ Estrutura Arquitetural

```
_FORJA_VIVA/
├── .bmad/                     # ⭐ BMAD Framework v6
│   ├── orchestrator.yaml      # Orquestrador central
│   ├── experts/               # 14 especialistas (1185L lean)
│   │   ├── pedagogia/         # CM, Susan Macaulay
│   │   ├── matematica/        # Bruner, Vygotsky
│   │   ├── narrativa/         # Lewis, Tolkien, Potter, Fujimura
│   │   ├── negocios/          # Godin, Hormozi, Thiel
│   │   ├── ux_familias/       # 6 Personas Mães
│   │   ├── design/            # 4 Design Experts
│   │   └── engenharia/        # BMAD, Evans, CleanCode, QA
│   ├── workflows/             # 4 workflows declarativos
│   └── templates/             # Templates + DoD
│
├── LORE/                      # ⭐ SSOT Narrativa
│   ├── north_star.yaml        # 8 Princípios Fundamentais
│   ├── guardioes.yaml         # 5 Guardiões canônicos
│   ├── index.yaml             # Mapa navegação
│   └── ...
│
├── _ARQUIVADO/                # ⭐ Histórico Evolução
│   └── PAINEL-ESPECIALISTAS.md # Fase 1 (Gemini 3.0)
│
├── _LEGADO/
│   └── yaml_verbose/          # Pre-Lean v1.0
│
└── logs/
    └── Upgrade_YAML_Lean/     # Deliberações + Sessões
```

---

## 🤝 Como Contribuir (Ênfase: Arquitetura, não Conteúdo)

### O Que Buscamos

✅ **Melhorias na Orquestração Multi-Agent**  
✅ **Otimizações YAML Lean v1.0**  
✅ **Novos Workflows Declarativos**  
✅ **Pesquisa de Novos Especialistas** (com fontes primárias)  
✅ **Aprimoramentos SSOT/DRY**  

❌ **NÃO buscamos:** Criação de lições individuais  
❌ **Foco:** Metodologia e arquitetura, não volume de conteúdo

### Como Começar

1. **Estude a arquitetura:**
   - Leia `.bmad/orchestrator.yaml`
   - Explore experts em `.bmad/experts/*/`
   - Veja workflows em ação nos logs

2. **Entre em contato:**
   - **Issues GitHub** — Proponha melhorias arquiteturais
   - **Discussões** — Questões sobre multi-agent design
   - **Email via GitHub** — Pesquisa colaborativa

3. **Contribua:**
   - **Documentação** — Explique padrões descobertos
   - **Refatoração** — Melhore orquestração
   - **Pesquisa** — Adicione expert com fontes primárias

**Ver:** [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📚 Pesquisa & Metodologia

### Fontes Primárias por Expert

Cada especialista baseado em obras originais, não resumos:

**Charlotte Mason:**
- Home Education (1886)
- Parents and Children (1896)
- School Education (1904)
- Philosophy of Education (1923) — Vols 1-6 completos

**Jerome Bruner:**
- Process of Education (1960)
- Toward a Theory of Instruction (1966)
- Acts of Meaning (1990)

**CS Lewis:**
- Abolition of Man (1943)
- On Stories and other Essays (1966)
- Chronicles of Narnia (1950-1956)

**Seth Godin:**
- Tribes (2008)
- Purple Cow (2003)
- This is Marketing (2018)

*... e assim por diante para todos 14+ experts.*

### Metodologia de Extração

1. **Leitura Primária** — Obras originais, não secundárias
2. **Citações Autênticas** — Aspas reais, contexto preservado
3. **Aplicação Prática** — Como princípio se aplica ao projeto
4. **Veto Hierarchy** — Prioridade baseada em domínio de expertise

---

## 🔬 Casos de Uso Técnicos

### Deliberação Formal Registrada

**Exemplo:** Converter expert para YAML Lean sem perder informação

```
Questão: Revisar-licao-auto deve listar 14 experts ou referenciar dinamicamente?

Participantes: Engenharia.yaml + Charlotte Mason

Posições:
- Engenharia: Reference dinâmico (SSOT violação se listar)
- Charlotte Mason: Clareza exige ver lista completa

Síntese: LEAN EXPANDIDO
- 4 fases documentadas
- 4 níveis veto preservados
- Reference dinâmico para experts (não duplicar)

Resultado: 244L → 44L, zero perda, SSOT preservado
```

**Log completo:** `logs/.../2026-01-13_2057_DELIBERACAO_REVISAR_LICAO_AUTO.md`

### AI Colaboração Evolutiva

**Gemini 3.0 Antigravity:** Criação inicial PAINEL-ESPECIALISTAS.md  
**Claude Sonnet 4.5 Extended Thinking:** Conversão YAML Lean v1.0, deliberações formais

**Ganho:** Extended Thinking permite deliberações profundas multi-expert em contexto

---

## 🔐 Security & Ethics

**Este projeto é pesquisa aberta:**
- ✅ Metodologia transparente (CC BY 4.0)
- ✅ Fontes citadas
- ✅ Processo documentado
- ❌ Sem dados sensíveis de crianças/famílias

**Ver:** [SECURITY.md](SECURITY.md)

---

## 🙏 Reconhecimentos

### Frameworks
- **BMAD Framework** — Agent as Code methodology
- **Eric Evans** — Domain-Driven Design (SSOT)
- **Robert C. Martin** — Clean Code principles

### AI Colaboradores
- **Google Gemini 3.0 Experimental + Antigravity** — Fase inicial (PAINEL)
- **Claude Sonnet 4.5 Extended Thinking** — YAML Lean v1.0 conversion

### Inspiração Metodológica
- Charlotte Mason, Jerome Bruner, Lev Vygotsky (Pedagogia)
- CS Lewis, JRR Tolkien (Narrativa)
- Seth Godin, Alex Hormozi, Peter Thiel (Estratégia)

---

## 📬 Contato

**Interessado em arquitetura multi-agent para educação?**

- 📧 **Email:** Através de GitHub
- 💬 **Discussões:** GitHub Discussions
- 🐛 **Issues:** Melhorias arquiteturais
- 🔒 **Security:** Ver [SECURITY.md](SECURITY.md)

**NÃO para:** Pedidos de criação de lições  
**SIM para:** Discussões sobre orquestração multi-agent, SSOT, pesquisa metodológica

---

## 📜 License

**CC BY 4.0** (Creative Commons Attribution 4.0)

- ✅ Estudar, adaptar, construir sobre esta arquitetura
- ℹ️ Dar crédito ao projeto original

Código e metodologia abertos porque **pesquisa deve ser acessível**.

---

<div align="center">

**Feito com ❤️ usando orquestração multi-agent**

*"Código robusto, manutenível, elegante. SSOT/DRY 100%."* — Engenharia.yaml

**Evolução:** PAINEL → BMAD v6 → YAML Lean v1.0  
**AI:** Gemini 3.0 Antigravity → Claude Sonnet 4.5 Extended Thinking

---

📚 [README Famílias](README.md) • 💻 README Desenvolvedores (você está aqui) • 🤝 [Contributing](CONTRIBUTING.md)

</div>
