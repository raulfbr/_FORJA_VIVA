# 📋 LOG DE DISCUSSÃO — PM + Orchestrator

---
**Data:** 12/01/2026  
**Horário:** 12:48  
**Tema:** Entendimento profundo do projeto e refinamento do currículo  
**Agentes:** Orchestrator → PM  
**Solicitante:** Maestro  

---

## 🎯 CONTEXTO CARREGADO

| Item | Status |
|------|--------|
| NORTH_STAR.md | ✅ Carregado |
| CONTEXT_INDEX.md | ✅ Carregado |
| GLOSSARIO.md | ✅ Carregado |
| Currículo em _FORJA_VIVA | ✅ 13 pastas, cópia para refinamento |

---

## 📊 ESTRUTURA DO CURRÍCULO (Cópia na Forja)

```
_FORJA_VIVA/curriculo/
├── 00_VIVENCIA (7 arquivos) — Ciclo 0 (0-4 anos)
├── 01_SEMENTES (22 arquivos) — Ciclo K (5-6 anos)
├── 01_SEMENTES-UTILIZAR (32)
├── 01_SEMENTES_ATAS (26)
├── 01_SEMENTES_TESTE (32)
├── 02_RAIZES (66 arquivos) — Ciclo 1-5 (7-10 anos)
├── 03_LOGICA (1 arquivo) — Ciclo 6-8 (11-14 anos)
├── 04_LEGADO (2 arquivos) — Ciclo 9-12 (15-18 anos)
├── 90_LIVRO_DOURADO (1)
├── LIVRO_GUARDIOES_FONETICA (22)
├── MINI_LIVRO_FONETICA (22)
├── PAGES (7)
├── _SISTEMA (85 arquivos) — Infraestrutura
└── README_CURRICULO.md
```

---

## ❓ PERGUNTAS DO PM PARA O MAESTRO

### Sobre o Escopo do Produto

| # | Pergunta | Por quê é importante |
|---|----------|---------------------|
| 1 | **Qual fase será o foco inicial?** Sementes apenas, ou Sementes + Raízes 1? | Define volume de produção |
| 2 | **Quantas lições você quer entregar no lançamento?** (L001-L030? L001-L060?) | Define sprint planning |
| 3 | **O currículo na Forja é para refinar ou recriar do zero?** | Define se preservo ou substituo |
| 4 | **As 3 pastas SEMENTES (UTILIZAR, ATAS, TESTE) são versões diferentes?** | Preciso entender qual é a canônica |

### Sobre a Produção

| # | Pergunta | Por quê é importante |
|---|----------|---------------------|
| 5 | **Já existe um template de lição "Gold" aprovado?** | Preciso saber o padrão |
| 6 | **A Lição 000 (O Portal) está finalizada?** | É a entrada de toda família |
| 7 | **Qual é o tempo médio para produzir UMA lição hoje?** | Define capacidade de sprint |
| 8 | **Quem valida as lições?** Você sozinho, você + Marina, ou Raulzito testa? | Define processo de QA |

### Sobre a Narrativa

| # | Pergunta | Por quê é importante |
|---|----------|---------------------|
| 9 | **Cada lição tem um Guardião específico ou varia?** | Define padrão narrativo |
| 10 | **Os Guardiões falam diretamente ao Viajante ou ao Portador?** | Define tom de voz |
| 11 | **A "Ideia Viva" é obrigatória em cada lição?** | Define checklist de QA |
| 12 | **Existe um arco narrativo que conecta as lições?** (história contínua?) | Define complexidade |

### Sobre a Entrega

| # | Pergunta | Por quê é importante |
|---|----------|---------------------|
| 13 | **O material será entregue em Markdown, PDF ou HTML?** | Define pipeline Gutenberg |
| 14 | **A família imprime ou usa tela?** | Define formato de saída |
| 15 | **Haverá materiais físicos (cards, manipulativos)?** | Define escopo de produção |
| 16 | **O currículo sincroniza com o calendário brasileiro?** (Início fevereiro) | Define timeline |

### Sobre o Negócio

| # | Pergunta | Por quê é importante |
|---|----------|---------------------|
| 17 | **Qual é a prioridade entre Sementes e 1º Ano?** | Define roadmap |
| 18 | **Há dependência externa (ex: licença TGTB)?** | Define riscos legais |
| 19 | **O CMC pode indicar famílias ou há acordo formal?** | Define canal de vendas |
| 20 | **Você pretende fazer lives para a comunidade Pioneira?** | Define operação |

---

## 💡 SUGESTÕES DO PM

### 1. Consolidar as 3 Pastas de Sementes

| Pasta | Minha Sugestão |
|-------|----------------|
| `01_SEMENTES` | Provavelmente a original |
| `01_SEMENTES-UTILIZAR` | Parece ser a versão "em uso" |
| `01_SEMENTES_TESTE` | Parece ser a versão Gold/teste |
| **Ação:** | Unificar em UMA pasta canônica |

### 2. Definir "Definition of Done" para Lição

```
Uma lição está PRONTA quando:
- [ ] Tem Ideia Viva
- [ ] CPA completo (Concreto → Pictórico → Abstrato)
- [ ] Tempo ≤ 20 min (Sementes)
- [ ] Guardião(s) apresentado(s)
- [ ] Roteiro do Portador claro
- [ ] Aprovada pela Família Rodrigues
```

### 3. Criar "Lição Modelo" (Gold Standard)

Antes de produzir L001-L030, finalizar UMA lição impecável que serve de referência para todas as outras.

**Sugestão:** L001 (Numbers 1 to 3) como Gold Standard.

---

## 📌 PLANO DE TAREFAS SUGERIDO

| # | Tarefa | Prioridade | Responsável |
|---|--------|------------|-------------|
| 1 | Unificar pastas SEMENTES | Alta | Orchestrator |
| 2 | Revisar L000 (Portal) | Alta | QA |
| 3 | Criar L001 Gold Standard | Alta | Dev |
| 4 | Testar L001 com Raulzito | Alta | Maestro |
| 5 | Produzir L002-L010 | Média | Dev |
| 6 | Lançar para Pioneiros | Média | Ops |

---

## 📝 AGUARDANDO RESPOSTAS

O PM aguarda as respostas das perguntas 1-20 para:
- Definir o PRD final do Pilot Sprint
- Criar o roadmap de lançamento
- Estruturar o processo de QA

---

> *Log gerado pelo PM em 12/01/2026 às 12:48*
