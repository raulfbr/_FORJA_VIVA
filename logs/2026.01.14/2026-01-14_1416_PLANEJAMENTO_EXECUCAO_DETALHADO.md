# PLANEJAMENTO DE EXECUÇÃO: Matemática Viva MVP
# Data: 14/01/2026 | Versão: 1.0
# Tipo: EXECUÇÃO DETALHADA PARA IA
# Contexto: Este documento permite que uma IA continue o trabalho de forma autônoma

---

## INSTRUÇÕES PARA IA

> Se você é uma IA lendo este documento para continuar o trabalho:
> 1. Leia COMPLETAMENTE este arquivo
> 2. Leia o plano estratégico consolidado em `logs/2026-01-14_1329_PLANO_ESTRATEGICO_CONSOLIDADO.md`
> 3. Leia o LORE em `LORE/north_star.yaml` e `LORE/index.yaml`
> 4. Use o orchestrator em `.bmad/orchestrator.yaml` para workflows
> 5. Siga as tarefas na ordem indicada

---

## CONTEXTO RESUMIDO

### O Que É o Matemática Viva

Currículo de matemática K-12 baseado em:
- **Charlotte Mason** (filosofia) — lições curtas, ideias vivas
- **CPA/Bruner** (método) — Concreto → Pictórico → Abstrato
- **TGTB** (scope) — sequência de conteúdos

### Público-Alvo

- Famílias homeschoolers brasileiras
- Comunidade CMC (600+ famílias) — Sementes, 1º e 2º ano
- Solo fértil: querem CM, têm medo de matemática

### Diferencial

- **Play-and-Go:** Preparo ≤5 min para mãe
- **Narrativa Imersiva:** Guardiões conduzem histórias
- **Segurança + Flexibilidade:** Norte claro + adaptação

---

## DECISÕES JÁ TOMADAS (NÃO RENEGOCIAR)

| Decisão | Valor | Referência |
|---------|-------|------------|
| Tríade | CM + CPA + TGTB | Mantida |
| Comunicação | "Neurociência + CM" | Marketing |
| Ritmo Sementes/1º | TRIMESTRAL (40 lições) | Estrutura |
| Ritmo 2º+ | BIMESTRAL (~30 lições) | Estrutura |
| **Valor Percebido** | R$4.197/ano | Ancoragem |
| **Preço Cheio (2027+)** | R$2.397/ano | Após pioneiros |
| **Preço Pioneiros (2026)** | R$1.197/ano | Este ano |
| **Mentoria Gold** | R$4.197 (10 vagas) | 4 encontros + entrevista |
| Dashboard MVP | SIM | Para mãe |
| Gamificação criança | ZERO | CM Princípio |
| Blog | YAML → HTML, gratuito | Funil |
| Comunidade | WhatsApp | Praticidade |
| **Suporte** | Via comunidade WhatsApp | NÃO direto conosco (mas participamos) |
| **Suporte direto** | Só Mentoria Gold | Com entrevista prévia |
| Legado (9º-12º) | Khan Academy | ⚠️ PRECISA REVISÃO PROFUNDA |
| Berço (0-4) | Orientações | Sai no começo (fácil) |
| LIVRO DOURADO | Segundo momento | Incluído para Pioneiros |

---

## TIMELINE

| Período | Marco |
|---------|-------|
| **Janeiro W2** | ✅ Planejamento concluído |
| **Janeiro W3** | Criar L000-L010 Sementes + Blog |
| **Janeiro W4** | Mentoria CMC + Beta Pioneiras |
| **Fevereiro W1-3** | MVP Completo (110 lições) |
| **Fevereiro W4** | Fechar beta |
| **Março W1** | **LANÇAMENTO** |

---

## TAREFAS DETALHADAS

### FASE 1: Preparação para Mentoria CMC (Janeiro W3)

#### Tarefa 1.1: Criar L000-L010 Sementes

**Prioridade:** ALTA
**Estimativa:** 4-6 horas
**Responsável:** IA + Maestro
**Workflow:** `/criar-licao [num] [tema]`

| # | ID | Tema TGTB | Guardião |
|---|-----|-----------|----------|
| 0 | MV-S-000 | O Portal (Intro) | Melquior |
| 1 | MV-S-001 | Números 1 a 3 | Celeste |
| 2 | MV-S-002 | Quadros de Dez | Bernardo |
| 3 | MV-S-003 | Números 4 e 5 | Íris |
| 4 | MV-S-004 | Ordem dos Eventos | Noé |
| 5 | MV-S-005 | Palavras de Posição | Celeste |
| 6 | MV-S-006 | Prática de Números | Íris |
| 7 | MV-S-007 | Números 6 e 7 | Celeste |
| 8 | MV-S-008 | Correspondência Pt1 | Íris |
| 9 | MV-S-009 | Números 8 e 9 | Noé |
| 10 | MV-S-010 | Números Ordinais Pt1 | Celeste |

**Arquivos de entrada:**
- `.bmad/templates/00_K_sementes/licao-template.yaml`
- `LORE/guardioes.yaml`
- `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`

**Saída esperada:**
- `curriculo/01_SEMENTES/L000.yaml` a `L010.yaml`
- HTML gerado via pipeline Gutenberg

---

#### Tarefa 1.2: Criar Blog Básico (3-5 Artigos)

**Prioridade:** ALTA
**Estimativa:** 2-3 horas
**Responsável:** IA escreve, Maestro revisa

**Artigos:**

| # | Arquivo | Título | Objetivo |
|---|---------|--------|----------|
| 1 | `001_o_que_e_cpa.yaml` | "O que é CPA e por que funciona" | Educar sobre Bruner |
| 2 | `002_cm_matematica.yaml` | "Charlotte Mason e Matemática" | Conectar filosofia |
| 3 | `003_criancas_nao_gostam.yaml` | "Por que crianças não gostam de matemática" | Dor |
| 4 | `004_narrativa_imersiva.yaml` | "Narrativa imersiva no ensino" | Diferencial |
| 5 | `005_como_nasceu.yaml` | "Como o Matemática Viva nasceu" | Story |

**Antes de escrever:**
1. Criar pasta `blog/artigos/`
2. Criar template `blog/_templates/artigo-template.yaml`
3. Criar script `tools/blog_to_html.py`

**Call-to-Action em cada artigo:**
> "Se você gostou dessas ideias, conheça o Matemática Viva —
> um currículo completo que aplica tudo isso para sua família."

---

#### Tarefa 1.3: Criar Documento de Visão (1 Página)

**Prioridade:** MÉDIA
**Estimativa:** 30 min
**Responsável:** IA

**Conteúdo:**
- Problema que resolvemos
- Nossa solução (tríade)
- Diferenciais (Play-and-Go, Narrativa, Segurança)
- Público-alvo
- Preços e modelo

**Saída:** `docs/VISAO_MATEMATICA_VIVA.md`

---

#### Tarefa 1.4: Criar FAQ Antecipado

**Prioridade:** MÉDIA
**Estimativa:** 30 min
**Responsável:** IA

**Perguntas esperadas:**
1. O que é o Matemática Viva?
2. Para que idades?
3. Preciso saber matemática para ensinar?
4. Quanto custa?
5. É alinhado com Charlotte Mason?
6. Como funciona a comunidade?
7. E se meu filho não gostar?
8. Posso testar antes?

**Saída:** `docs/FAQ_MATEMATICA_VIVA.md`

---

### FASE 2: MVP Completo (Janeiro W4 - Fevereiro W3)

#### Tarefa 2.1: Completar 1º Trimestre Sementes (L011-L040)

**Prioridade:** ALTA
**Estimativa:** 10-15 horas
**Responsável:** IA + revisão Maestro

| Bloco | Lições | Tema Geral |
|-------|--------|------------|
| S011-S015 | 5 | Continuação Fundação |
| S016-S030 | 15 | Operações e Ritmo |
| S031-S038 | 8 | Geometria e Banquetes |
| S039-S040 | 2 | Banquete da Memória (Revisão) |

---

#### Tarefa 2.2: Criar 1º Trimestre 1º Ano (L000-L040)

**Prioridade:** ALTA
**Estimativa:** 10-15 horas
**Responsável:** IA + revisão Maestro

**Arquivos de entrada:**
- `curriculo/_SISTEMA/CURRICULOS_MESTRE/001_1ANO_RAIZES-1_CURRICULO_MESTRE.md`
- `.bmad/templates/01_raizes/licao-template.yaml` (criar se não existir)

---

#### Tarefa 2.3: Criar 1º Bimestre 2º Ano (L000-L030)

**Prioridade:** ALTA
**Estimativa:** 8-12 horas
**Responsável:** IA + revisão Maestro

**Arquivos de entrada:**
- `curriculo/_SISTEMA/CURRICULOS_MESTRE/002_2ANO_RAIZES-2_CURRICULO_MESTRE.md`

---

#### Tarefa 2.4: Criar Orientações Berço

**Prioridade:** MÉDIA
**Estimativa:** 2-3 horas
**Responsável:** IA

**Conteúdo:**
- CM: Antes de 6 anos = natureza, hábitos, ideias vivas
- NÃO matemática formal
- Sugestões de atividades naturais (contagem no parque, etc.)
- Guardiões como personagens de história de dormir (opcional)

**Saída:** `curriculo/00_BERCO/ORIENTACOES.md`

---

### FASE 3: Infraestrutura Blog (Paralelo)

#### Tarefa 3.1: Criar Script blog_to_html.py

**Prioridade:** ALTA
**Estimativa:** 1 hora
**Responsável:** IA

**Base:** `tools/log_to_html.py`

**Funcionalidades:**
- Converter `blog/artigos/*.yaml` → `dist/blog/*.html`
- CSS consistente com site
- CTA no final de cada artigo

---

#### Tarefa 3.2: Criar Template Artigo YAML

**Prioridade:** ALTA
**Estimativa:** 30 min
**Responsável:** IA

**Estrutura sugerida:**

```yaml
id: artigo_001
titulo: "Título do Artigo"
autor: Raul Rodrigues
data: 2026-01-14
categoria: metodo|pratica|filosofia|depoimento
resumo: "Descrição curta para SEO"
tags: [cpa, bruner, matemática]
conteudo:
  introducao: "..."
  secoes:
    - titulo: "Seção 1"
      texto: "..."
    - titulo: "Seção 2"
      texto: "..."
  conclusao: "..."
cta:
  texto: "Se você gostou..."
  link: https://matematicaviva.com.br
```

---

### FASE 4: Dashboard Simples (Fevereiro W4)

#### Tarefa 4.1: Criar Página Dashboard

**Prioridade:** MÉDIA
**Estimativa:** 2-3 horas
**Responsável:** IA

**Elementos:**
- Lição atual
- Próxima lição
- Barra de progresso por ciclo
- % completado

**Sem gamificação.** Só informação.

---

## ARQUIVOS IMPORTANTES

### Leitura Obrigatória

| Arquivo | Conteúdo |
|---------|----------|
| `LORE/north_star.yaml` | Missão, preços, princípios |
| `LORE/index.yaml` | Índice de todos os LORE |
| `.bmad/orchestrator.yaml` | Modos e comandos |
| `logs/2026-01-14_1329_PLANO_ESTRATEGICO_CONSOLIDADO.md` | Todas as decisões |

### Templates

| Arquivo | Uso |
|---------|-----|
| `.bmad/templates/00_K_sementes/licao-template.yaml` | Template lição Sementes |
| `.bmad/templates/000_global/definition-of-done.md` | Critérios de qualidade |
| `.bmad/templates/000_global/perd-template.yaml` | PRD de lição |

### Currículos Mestre

| Arquivo | Ciclo |
|---------|-------|
| `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md` | Sementes |
| `curriculo/_SISTEMA/CURRICULOS_MESTRE/001_1ANO_RAIZES-1_CURRICULO_MESTRE.md` | 1º Ano |
| `curriculo/_SISTEMA/CURRICULOS_MESTRE/002_2ANO_RAIZES-2_CURRICULO_MESTRE.md` | 2º Ano |

---

## COMANDOS DO ORCHESTRATOR

Use estes comandos para executar tarefas:

```
/criar-licao L001 "Números 1 a 3"    → Criar lição seguindo workflow
/revisar L001                         → QA Quíntupla na lição
/reuniao "Tema para discutir"         → Deliberação com experts selecionados
/reuniao-todos "Tema importante"      → Deliberação com 14 experts
```

---

## EXPERTS DISPONÍVEIS

### Pedagogia
- **Charlotte Mason** — Coordenadora, veto final
- **Susan Macaulay** — Consultora CM moderna

### Matemática
- **Jerome Bruner** — CPA, espiral (subordinado a CM)
- **Lev Vygotsky** — ZPD, scaffolding

### Narrativa
- **CS Lewis** — Tom, dignidade
- **JRR Tolkien** — Consistência mundo
- **Beatrix Potter** — Estética, cores
- **Makoto Fujimura** — Kintsugi (honrar imperfeição)

### Negócios
- **Seth Godin** — Marketing tribal
- **Alex Hormozi** — Grand Slam Offers
- **Peter Thiel** — Monopólio, diferenciação

### UX
- **6 Mães Personas** — Débora, Priscila, Elisa, Júlia, Raquel, Renata

### Engenharia
- **BMAD** — Framework agentes
- **Eric Evans** — DDD, SSOT
- **Clean Code** — Código limpo
- **QA** — Verificação Quíntupla

---

## HIERARQUIA DE VETO

| Prioridade | Expert | Poder |
|------------|--------|-------|
| 1 | Charlotte Mason | Veto absoluto |
| 2 | Jerome Bruner | Veto CPA (sujeito a CM) |
| 3 | CS Lewis | Veto tom |
| 4 | JRR Tolkien | Veto consistência |

**Regra:** CM tem palavra final SEMPRE.

---

## CHECKLIST DE QUALIDADE (Definition of Done)

✅ CM: Criança é pessoa? Ideia Viva? Lição ≤20min?
✅ CPA: Concreto ≥80%? Pictórico vetado (Sementes)? Ordem C→P→A?
✅ Narrativa: Frase canônica guardião? Tom Lewis? Consistência Tolkien?
✅ UX: Preparo ≤5min? Uma mão celular? Sem pedagogês?
✅ Template: Seções obrigatórias? Linkage? Atmosfera única?

---

## PRÓXIMA AÇÃO IMEDIATA

**Para IA que continua:**

1. Execute `Tarefa 1.1`: Criar L000-L010 Sementes
2. Use o comando `/criar-licao L001 "Números 1 a 3"`
3. Siga o workflow de 3 fases (Planning → Development → Verification)
4. Salve em `curriculo/01_SEMENTES/L001.yaml`
5. Repita para L002-L010

---

## CONTATO

- **Maestro:** Raul (decisor final)
- **Matriarca:** Marina (revisão sensibilidade)

**Se tiver dúvida, pergunte ao Maestro antes de decidir.**

---

*Documento criado: 14/01/2026 14:16*
*Última atualização: 14/01/2026 14:16*
