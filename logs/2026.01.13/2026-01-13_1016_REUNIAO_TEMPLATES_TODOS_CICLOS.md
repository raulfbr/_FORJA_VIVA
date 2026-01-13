# 🎯 REUNIÃO DE DELIBERAÇÃO: Templates por Ciclo — Construção Inicial

**Data:** 13/01/2026 às 10:16  
**Coordenadora:** Charlotte Mason  
**Tema:** Criar estrutura inicial de templates para todos os ciclos  
**Modo:** `/reuniao-todos` — 14 experts convocados  
**Contexto:** Discussão referenciada da reunião anterior [0945_REUNIAO_TEMPLATES_POR_CICLO.md]

---

## CONTEXTO DESCOBERTO

### Estrutura de Templates (já criada):
```
.bmad/templates/
├── 000_global/        (vazia)
├── 00_sementes/       (regras.yaml ✅)
├── 01_raizes-1/       (vazia)
├── 02_raizes-2/       (vazia)
├── 03_logica/         (vazia)
├── 04_legado/         (vazia)
└── perd-template.yaml
```

### Currículos Mestres Existentes (14 arquivos):
| Arquivo | Série | Ciclo | Linhas |
|---------|-------|-------|--------|
| 000_K_SEMENTES | K | Sementes | 700+ |
| 001_1ANO_RAIZES-1 | 1º | Raízes-1 | 223 |
| 002_2ANO_RAIZES-2 | 2º | Raízes-2 | ~200 |
| 003_3ANO_RAIZES-3 | 3º | Raízes-3 | ~200 |
| 004_4ANO_RAIZES-4 | 4º | Raízes-4 | ~200 |
| 005_5ANO_RAIZES-5 | 5º | Raízes-5 | ~200 |
| 006_6ANO_LOGICA-1 | 6º | Lógica-1 | ~200 |
| 007_7ANO_LOGICA-2 | 7º | Lógica-2 | ~200 |
| 008_8ANO_LOGICA-3 | 8º | Lógica-3 | ~200 |
| 009_9ANO_LEGADO-1 | 9º | Legado-1 | ~200 |
| 010_10ANO_LEGADO-2 | 10º | Legado-2 | ~200 |
| 011_11ANO_LEGADO-3 | 11º | Legado-3 | ~200 |
| 012_12ANO_LEGADO-4 | 12º | Legado-4 | ~200 |

---

## FASE 1: ABERTURA (Charlotte Mason)

> *"Senhores especialistas, temos 14 currículos mestres prontos mas apenas 1 template de regras (Sementes). Precisamos decidir: devemos criar templates para todos os ciclos agora, ou aguardar?"*

### Perguntas para Deliberação:
1. Devemos criar templates para TODOS os ciclos agora ou por demanda?
2. Como referenciar os currículos mestres nas regras?
3. Que perguntas não foram feitas ainda?
4. Quais são os riscos de criar agora vs. esperar?

---

## FASE 2: POSIÇÕES INICIAIS

### 📚 Charlotte Mason (Pedagogia)

> **POSIÇÃO:** Criar templates BÁSICOS agora, mas marcar como "EM CONSTRUÇÃO".

**Embasamento:**
> "Education is a Life — e precisa crescer organicamente. Não posso definir regras pedagógicas para Lógica (10-12 anos) quando ainda não testei Sementes. Mas posso deixar a ESTRUTURA pronta."

**Proposta:**
- Criar `regras.yaml` para cada ciclo com: header "STATUS: EM_CONSTRUCAO"
- Referenciar o currículo mestre correspondente
- Deixar proporções CPA como "TBD" até validação

**Preocupação:**
- Se definirmos tudo agora, podemos engessar o que ainda não conhecemos.

---

### 📐 Jerome Bruner (Matemática/CPA)

> **POSIÇÃO:** As proporções CPA já estão teoricamente definidas. Podemos registrá-las.

**Embasamento:**
> "A teoria CPA é sólida. Eu JÁ SEI que crianças de 10-12 anos (Lógica) podem trabalhar 40% abstrato. Isso não muda."

**Proposta de Proporções (da reunião anterior):**

| Ciclo | Idade | Concreto | Pictórico | Abstrato |
|-------|-------|----------|-----------|----------|
| Sementes | 4-6 | 60%+ | VETADO | Mínimo |
| Raízes-1 | 6-8 | 50% | 30% | 20% |
| Raízes-2 | 8-10 | 40% | 35% | 25% |
| Lógica | 10-12 | 30% | 30% | 40% |
| Legado | 12+ | 20% | 20% | 60% |

**Pergunta que levanto:**
> "Temos Raízes-1 a Raízes-5 no currículo. São 5 anos. Temos templates para Raízes-1 e Raízes-2. E o 3, 4 e 5?"

---

### 🐻 Lev Vygotsky (Scaffolding)

> **POSIÇÃO:** Scaffolding por ciclo está definido, mas precisa de EXEMPLOS CONCRETOS.

**Embasamento:**
> "Dizer 'Produtive struggle' para Lógica é abstrato demais. Preciso de EXEMPLOS de frases do Portador."

**Pergunta que levanto:**
> "Para cada template, devemos incluir 3-5 exemplos de falas por tipo de scaffolding?"

---

### 📖 C.S. Lewis (Narrativa/Tom)

> **POSIÇÃO:** O tom JÁ ESTÁ nos currículos mestres. Os templates devem REFERENCIAR.

**Embasamento:**
> "Olhei o Raízes-1. Cada lição tem um 'Hook de Excelência' com tom específico. O template não precisa redefinir — precisa APONTAR."

**Proposta:**
- Template contém `referencia_curriculo: curriculo/_SISTEMA/CURRICULOS_MESTRE/001_*.md`
- Template diz: "Consulte o currículo mestre para hooks narrativos"

**Pergunta que levanto:**
> "Os currículos mestres precisam ser REVISADOS à luz do que aprendemos com Sementes?"

---

### 📕 J.R.R. Tolkien (Consistência)

> **POSIÇÃO:** Os currículos mestres usam os MESMOS Guardiões.

**Embasamento:**
> "Vi que Raízes-1 usa Celeste, Bernardo, Noé, Íris exatamente como Sementes. O LORE está consistente. Isso facilita."

**Observação:**
> "Os currículos mestres já definem qual Guardião aparece em cada lição. Isso é OURO. Devemos preservar."

---

### 🎨 Beatrix Potter (Estética)

> **POSIÇÃO:** Densidade sensorial deve CRESCER com os ciclos.

**Embasamento:**
> "Vi os hooks de Raízes-1: 'Ouvir o som do cinzel na pedra'. Já são mais densos que Sementes. Correto."

**Proposta:**
- Cada template define `densidade_sensorial.elementos_por_paragrafo`
- Sementes: 1 | Raízes-1: 2 | Raízes-2: 3 | Lógica: 4 | Legado: 4+

---

### 💰 Alex Hormozi (Value Equation)

> **POSIÇÃO:** Tempo de preparo deve ESCALAR com confiança da família.

**Embasamento:**
> "No Sementes, mãe é nova e insegura. Precisa de 5 min preparo. Em Raízes-2, ela já usa o sistema há 2 anos. Pode ser 10 min. Em Legado, 15 min."

**Proposta:**

| Ciclo | Tempo Preparo | Justificativa |
|-------|---------------|---------------|
| Sementes | ≤ 5 min | Família nova |
| Raízes-1 | ≤ 7 min | 1 ano de uso |
| Raízes-2 | ≤ 10 min | 2+ anos |
| Lógica | ≤ 12 min | Família experiente |
| Legado | ≤ 15 min | Família madura |

---

### 🎯 Peter Thiel (Segredo)

> **POSIÇÃO:** Cada ciclo deve ter uma "Ideia Central" diferente.

**Embasamento:**
> "Em Sementes, o segredo é 'Números são promessas do Rei'. Qual é o segredo de Raízes? De Lógica? De Legado?"

**Pergunta que levanto:**
> "Precisamos definir o PROPÓSITO NARRATIVO de cada ciclo antes de fazer templates."

---

### 👩‍👧 Mães Personas (UX)

> **POSIÇÃO:** Os selos devem AJUSTAR por ciclo, não mudar.

**Embasamento:**
> "Tempo de preparo muda. Materiais mudam. Mas os SELOS são os mesmos."

**Proposta de Selos por Ciclo:**

| Selo | Sementes | Raízes | Lógica | Legado |
|------|----------|--------|--------|--------|
| ⏱️ Tempo | ≤ 5 min | ≤ 10 min | ≤ 12 min | ≤ 15 min |
| 🫘 Materiais | Cozinha | Casa + Alguns comprados | Comprados OK | Ferramentas específicas OK |
| 📱 Mobile | Sim | Sim | Sim | Sim |
| 💡 Adaptação | Sim | Sim | Sim | Sim |

---

### 💻 Eric Evans (Engenharia/DDD)

> **POSIÇÃO:** Criar templates ESQUELETO agora é ARQUITETURALMENTE CORRETO.

**Embasamento:**
> "DDD: Defina Bounded Contexts cedo. Ter um arquivo `regras.yaml` em cada pasta, mesmo com 'TBD', é melhor que pasta vazia."

**Proposta de Estrutura:**
```yaml
# .bmad/templates/01_raizes-1/regras.yaml
# ════════════════════════════════════════════
# STATUS: EM_CONSTRUCAO
# Última revisão: [data]
# ════════════════════════════════════════════

status: EM_CONSTRUCAO
ciclo: raizes-1
serie: "1º Ano"
idade_alvo: "6-8 anos"

referencias:
  curriculo_mestre: "curriculo/_SISTEMA/CURRICULOS_MESTRE/001_1ANO_RAIZES-1_CURRICULO_MESTRE.md"
  lore_guardioes: "LORE/guardioes.yaml"
  lore_locais: "LORE/locais.yaml"

cpa:
  concreto: 50  # TBD — validar com lições piloto
  pictorico: 30
  abstrato: 20

# ... (resto a definir)
```

---

## FASE 3: RÉPLICA

### CM questiona Bruner:
> "As proporções CPA são TEORIA. E se Raízes-1 brasileiro for diferente do Singapore original?"

**Bruner responde:**
> "Então ajustamos APÓS o piloto. Mas ter 50-30-20 como ponto de partida é melhor que vazio."

### Evans questiona Thiel:
> "Precisamos do 'propósito narrativo' ANTES de criar os templates?"

**Thiel responde:**
> "Talvez não. Podemos deixar um campo `proposito_narrativo: TBD` e revisitar."

### Lewis questiona CM:
> "Os currículos mestres precisam de revisão?"

**CM responde:**
> "Sim, mas NÃO AGORA. Marcamos como 'CURRICULO_MESTRE_REVISAO_PENDENTE' e seguimos."

---

## FASE 4: TRÉPLICA

### Convergência:

1. ✅ Criar templates ESQUELETO para todos os ciclos
2. ✅ Marcar como `STATUS: EM_CONSTRUCAO`
3. ✅ Referenciar currículo mestre correspondente
4. ✅ Incluir proporções CPA como ponto de partida (ajustável)
5. ✅ Incluir tempos de preparo escalados
6. ⚠️ Propósito narrativo de cada ciclo: TBD
7. ⚠️ Revisão de currículos mestres: PENDENTE

---

## FASE 5: SÍNTESE (Charlotte Mason)

### Perguntas Levantadas:

| # | Pergunta | Responsável | Status |
|---|----------|-------------|--------|
| 1 | Temos Raízes 1-5. Devemos agrupar ou separar templates? | Bruner + Evans | ⚠️ DISCUTIR |
| 2 | Qual o propósito narrativo de cada ciclo? | Thiel + Lewis | ⚠️ TBD |
| 3 | Os currículos mestres precisam de revisão? | CM | ⚠️ PENDENTE |
| 4 | Devemos incluir exemplos de falas por tipo de scaffolding? | Vygotsky | ⚠️ SUGESTÃO |
| 5 | Como tratar a transição entre ciclos (Sementes→Raízes)? | Tolkien | ⚠️ LORE |

### Sugestões Adicionais:

| # | Sugestão | Impacto |
|---|----------|---------|
| 1 | Criar uma lição de TRANSIÇÃO entre ciclos | Alto — UX |
| 2 | Definir "Distintivos" ou marcos por ciclo | Alto — Motivação |
| 3 | Incluir "Ideias Vivas Centrais" por ciclo | Médio — Consistência |
| 4 | Mapear quais Guardiões são mais frequentes por ciclo | Baixo — Já existe no currículo |

---

## FASE 6: DECISÃO FINAL (Charlotte Mason)

### ✅ DECISÃO APROVADA

**Implementar agora (Fase 1):**

1. ✅ Criar `regras.yaml` ESQUELETO para:
   - `01_raizes-1/`
   - `02_raizes-2/`
   - `03_logica/`
   - `04_legado/`
   - `000_global/` (base comum)

2. ✅ Cada arquivo contém:
   - Header: `STATUS: EM_CONSTRUCAO`
   - Referência ao currículo mestre
   - Proporções CPA (ponto de partida)
   - Tempo de preparo escalado
   - Scaffolding esperado
   - Densidade sensorial

3. ✅ NÃO resolver agora:
   - Propósito narrativo detalhado
   - Revisão dos currículos mestres
   - Agrupamento Raízes 3-4-5 (usar Raízes-2 como proxy por enquanto)

**Justificativa:**
> "Ter estrutura com 'TBD' é melhor que pasta vazia. Podemos iterar após o piloto de Sementes."

---

## 📋 PERGUNTAS PARA O MAESTRO

Antes de implementar, precisamos de sua decisão:

### 1. Agrupamento de Raízes
Os currículos têm Raízes 1-5 (5 séries). Os templates têm Raízes-1 e Raízes-2.

**Opções:**
- A) Criar 5 templates (raizes-1 a raizes-5)
- B) Manter 2 (raizes-1 agrupa 1º-2º, raizes-2 agrupa 3º-5º)
- C) Outra sugestão

### 2. Propósito Narrativo
Cada ciclo deveria ter um "segredo" central. Sugestões:

| Ciclo | Sugestão de Propósito |
|-------|----------------------|
| Sementes | "Números são promessas do Rei" |
| Raízes | "Construímos a Vila com o que contamos" |
| Lógica | "A matemática revela a linguagem do universo" |
| Legado | "O que você descobriu é usado pelo mundo" |

**Você aprova estas sugestões ou prefere definir depois?**

### 3. Currículos Mestres
Os currículos mestres são ricos mas podem precisar de pequenos ajustes (ex: referências a GOVERNANCA, que agora podem ir para LORE).

**Opções:**
- A) Marcar para revisão futura (não bloqueia)
- B) Revisar um currículo como piloto antes de prosseguir

---

*Reunião encerrada às 10:16 em 13/01/2026*  
*Aguardando decisões do Maestro antes de implementar*
