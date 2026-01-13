# 🎯 REUNIÃO DE DELIBERAÇÃO: Onde Incorporar Padrões de Narração por Ciclo

**Data:** 13/01/2026 às 09:45  
**Coordenadora:** Charlotte Mason  
**Tema:** Onde armazenar padrões de narração e como evoluir templates por ciclo  
**Modo:** `/reuniao-todos` — 14 experts convocados

---

## FASE 1: ABERTURA (Charlotte Mason)

> *"Senhores especialistas, temos uma questão arquitetural importante. O Maestro pergunta: onde devemos incorporar os padrões de narração imersiva para que permaneçam latentes em todas as futuras criações? E como devemos evoluir as lições de Sementes para Raízes, Lógica e Legado?"*

### Questões Centrais:
1. **ONDE** armazenar os padrões de narração? (Expert? Template? Expansion Pack?)
2. **COMO** evoluir o workflow `criar-licao-premium` por ciclo?
3. **O QUE** muda entre Sementes, Raízes-1, Raízes-2, Lógica, Legado?

### Participantes:
Todos os 14 experts convocados.

---

## FASE 2: POSIÇÕES INICIAIS

### 📚 Charlotte Mason (Pedagogia)

> **POSIÇÃO:** Os padrões de narração devem estar no **Template por Ciclo**, não em um único expert.

**Embasamento:**
> "A Education is a Life — e a vida muda conforme a criança cresce. O tom de Sementes é de MARAVILHAMENTO. O tom de Raízes é de EXPLORAÇÃO. O tom de Lógica é de DESCOBERTA. Não podemos ter um único template estático."

**Proposta:**
- Criar `templates/sementes/` com regras específicas de narração
- Criar `templates/raizes/` com evolução
- O expert `artesao.yaml` referencia o template do ciclo

---

### 📐 Jerome Bruner (Matemática/CPA)

> **POSIÇÃO:** Cada ciclo tem **proporções CPA diferentes**. Isso deve ser obrigatório no template.

**Embasamento:**
> "Em Sementes, 60%+ é Concreto, Pictórico é VETADO. Em Raízes, Pictórico abre. Em Lógica, Abstrato domina. Isso não é preferência — é DESENVOLVIMENTO COGNITIVO."

**Proposta de Proporções:**

| Ciclo | Idade | Concreto | Pictórico | Abstrato |
|-------|-------|----------|-----------|----------|
| Sementes | 4-6 | 60%+ | VETADO | Mínimo |
| Raízes-1 | 6-8 | 50% | 30% | 20% |
| Raízes-2 | 8-10 | 40% | 35% | 25% |
| Lógica | 10-12 | 30% | 30% | 40% |
| Legado | 12+ | 20% | 20% | 60% |

**Proposta:**
- Criar `templates/raizes/proporcoes_cpa.yaml`
- Workflow verifica proporções antes de aprovar

---

### 🐻 Lev Vygotsky (Scaffolding)

> **POSIÇÃO:** O **Scaffolding também evolui** — de mão-na-mão para dicas sutis.

**Embasamento:**
> "Em Sementes, o Portador FALA junto com a criança. Em Raízes, ele PERGUNTA. Em Lógica, ele ESPERA que a criança chegue sozinha."

**Proposta de Scaffolding por Ciclo:**

| Ciclo | Tipo de Scaffolding | Exemplo |
|-------|---------------------|---------|
| Sementes | Mão-na-mão | "Vamos contar JUNTOS: um, dois, três." |
| Raízes | Pergunta guiada | "O que vem depois do dois?" |
| Lógica | Produtive struggle | "Descubra. Eu sei que você consegue." |
| Legado | Autonomia | "Pesquise e me conte o que descobriu." |

---

### 📖 C.S. Lewis (Narrativa/Tom)

> **POSIÇÃO:** O **TOM** da narrativa evolui, mas a DIGNIDADE permanece constante.

**Embasamento:**
> "Never be within the child's mental range — em TODAS as idades. O que muda é a COMPLEXIDADE, não o RESPEITO."

**Proposta de Tom por Ciclo:**

| Ciclo | Tom | Exemplo |
|-------|-----|---------|
| Sementes | Encantamento mágico | "Sente o calor no seu rosto? É o mesmo sol..." |
| Raízes | Aventura exploratória | "Há um mistério escondido neste problema." |
| Lógica | Desafio intelectual | "Os antigos matemáticos chamavam isso de..." |
| Legado | Maestria vocacional | "O que você descobriu aqui é usado por engenheiros." |

**Proposta:**
- Criar seção `tom_por_ciclo` no expert `cs_lewis.yaml`

---

### 📕 J.R.R. Tolkien (Consistência)

> **POSIÇÃO:** O **LORE permanece constante**, mas as histórias ficam mais complexas.

**Embasamento:**
> "Narnia não mudou — o que mudou foi quão profundo os personagens iam. Nosso Reino Contado deve ter LORE fixo: Guardiões, locais, artefatos. O que evolui são as CAMADAS de história."

**Proposta:**
- Manter `LORE/guardioes.yaml` como fonte única (SSOT)
- Cada ciclo revela MAIS sobre os Guardiões, não muda quem eles são
- Em Sementes: conhece Celeste. Em Raízes: descobre o passado dela.

---

### 🎨 Beatrix Potter (Estética)

> **POSIÇÃO:** A **DENSIDADE sensorial evolui** — de simples para complexa.

**Embasamento:**
> "Em Sementes, descrevemos UMA coisa por vez: o cheiro OU a cor. Em Lógica, podemos tecer várias sensações juntas."

**Proposta:**

| Ciclo | Densidade Sensorial |
|-------|---------------------|
| Sementes | 1 elemento por parágrafo |
| Raízes | 2-3 elementos |
| Lógica | Parágrafos densos |

---

### 🪔 Makoto Fujimura (Kintsugi)

> **POSIÇÃO:** As **Notas de Graça** permanecem em TODOS os ciclos.

**Embasamento:**
> "A beleza de reparar permanece. Mesmo em Lógica, o erro é honrado. O que muda é o TIPO de reparo: em Sementes é 'tudo bem, tente amanhã'. Em Lógica é 'o que você aprendeu com esse erro?'"

---

### 📣 Seth Godin (Tribos)

> **POSIÇÃO:** Cada ciclo é uma **TRIBO diferente**.

**Embasamento:**
> "Mães de Sementes têm dores diferentes de mães de Lógica. A mãe de Sementes quer SEGURANÇA. A mãe de Lógica quer RIGOR."

**Proposta:**
- Personas Mães também evoluem por ciclo
- Criar sub-personas: Débora-Sementes, Débora-Raízes

---

### 💰 Alex Hormozi (Value Equation)

> **POSIÇÃO:** O **PREPARO** também evolui.

**Embasamento:**
> "5 minutos de preparo funciona para Sementes. Mas Lógica pode ter 10-15 minutos de preparo porque a mãe já está acostumada. A TIME DELAY diminui com a fidelidade."

**Proposta:**

| Ciclo | Tempo Preparo | Materiais |
|-------|---------------|-----------|
| Sementes | ≤ 5 min | Caseiros |
| Raízes | ≤ 10 min | Ainda caseiros + alguns impressos |
| Lógica | ≤ 15 min | Permite comprados online |

---

### 🎯 Peter Thiel (Segredo)

> **POSIÇÃO:** O **SEGREDO permanece**, mas a PROFUNDIDADE aumenta.

**Embasamento:**
> "Nosso monopólio é: matemática é linguagem poética. Em Sementes, isso é 'números são promessas'. Em Lógica, isso é 'a geometria é a linguagem de Deus' (Galileu). MESMO segredo, mais profundo."

---

### 👩‍👧 Mães Personas (UX)

> **POSIÇÃO:** Os **SELOS** são constantes, mas os critérios ajustam.

**Embasamento:**
> "📱 Mobile-Friendly permanece. Mas '⏱️ 5 Minutos' vira '⏱️ 10 Minutos' em Raízes. O selo existe, o número muda."

**Proposta:**
- Criar `selos_por_ciclo.yaml` com critérios ajustados

---

### 💻 Eric Evans (Engenharia/DDD)

> **POSIÇÃO:** Precisamos de **TEMPLATES POR CICLO** na estrutura.

**Embasamento:**
> "DDD: Bounded Contexts. Cada ciclo é um CONTEXTO diferente. Não misture Sementes com Lógica no mesmo template."

**Proposta de Estrutura:**

```
.bmad/
├── templates/
│   ├── global/
│   │   └── base-licao.yaml     # Seções obrigatórias
│   ├── sementes/
│   │   ├── licao-sementes.yaml # Template específico
│   │   └── regras.yaml         # CPA vetado, etc.
│   ├── raizes-1/
│   │   └── licao-raizes-1.yaml
│   ├── raizes-2/
│   │   └── licao-raizes-2.yaml
│   ├── logica/
│   │   └── licao-logica.yaml
│   └── legado/
│       └── licao-legado.yaml
```

---

### 🔧 BMAD (Orquestração)

> **POSIÇÃO:** O workflow detecta o ciclo e aplica o template correto.

**Embasamento:**
> "Agent as Code. O workflow `/criar-licao-premium` deve receber o CICLO como parâmetro e carregar as regras corretas."

**Proposta:**
```
/criar-licao-premium L050 "Frações" ciclo=raizes-1
```
O workflow carrega `.bmad/templates/raizes-1/regras.yaml` automaticamente.

---

## FASE 3: RÉPLICA

### CM questiona Bruner:
> "As proporções CPA são fixas ou apenas GUIAS?"

**Bruner responde:**
> "São GUIAS com margem de 10%. Não é 60% exato, mas 55-65%. O importante é a TENDÊNCIA, não o número exato."

### Lewis questiona Tolkien:
> "Se o LORE é fixo, como evitamos que as histórias fiquem repetitivas?"

**Tolkien responde:**
> "Revelação progressiva. Em Sementes, Celeste 'fareja aventura'. Em Raízes, descobrimos POR QUE ela fareja — talvez tenha perdido algo uma vez. O personagem cresce, não muda."

### Eric Evans questiona CM:
> "Vamos ter templates SEPARADOS ou um template ÚNICO com flags de ciclo?"

**CM responde:**
> "Templates separados. Muito mais claro para manutenção. O custo de duplicação é menor que o custo de complexidade."

---

## FASE 4: TRÉPLICA

### Consensus Building:

1. ✅ **Templates por ciclo** — todos concordam
2. ✅ **Proporções CPA por ciclo** — Bruner define, CM aprova
3. ✅ **Tom evolui, dignidade constante** — Lewis + CM alinhados
4. ✅ **LORE fixo, revelação progressiva** — Tolkien + narrativa alinhados
5. ✅ **Selos ajustados por ciclo** — Mães + Hormozi alinhados
6. ✅ **Workflow detecta ciclo** — Eric Evans + BMAD alinhados

---

## FASE 5: SÍNTESE (Charlotte Mason)

> **Convergência Total.**
>
> A solução é clara: **Templates por Ciclo** armazenados em `.bmad/templates/[ciclo]/`.
>
> Cada template contém:
> - Proporções CPA obrigatórias
> - Tom de narração esperado
> - Tipo de scaffolding
> - Selos com critérios ajustados
> - Regras de densidade sensorial
>
> O workflow `/criar-licao-premium` recebe o ciclo e carrega automaticamente.
> O LORE permanece em `LORE/*.yaml` como SSOT.
> Os padrões de narração imersiva vão para um arquivo de referência.

---

## FASE 6: DECISÃO FINAL (Charlotte Mason)

### ✅ DECISÃO APROVADA POR UNANIMIDADE

**Implementar:**

1. **Criar estrutura de templates por ciclo:**
   ```
   .bmad/templates/
   ├── global/          # Base comum
   ├── sementes/        # K (4-6)
   ├── raizes-1/        # 1º-2º ano
   ├── raizes-2/        # 3º-4º ano
   ├── logica/          # 5º-6º ano
   └── legado/          # 7º+ ano
   ```

2. **Criar arquivo de padrões narrativos:**
   - `LORE/padroes_narrativos.yaml` — referência para narração imersiva
   - Contém: transições sensoriais, [tons], pausas, frases canônicas

3. **Atualizar workflow:**
   - `/criar-licao-premium [ID] [TEMA] ciclo=[CICLO]`
   - Carrega automaticamente template do ciclo

4. **Criar `regras.yaml` por ciclo:**
   - CPA proportions
   - Tempo de preparo
   - Scaffolding type
   - Tom esperado

**Justificativa CM:**
> "A educação é uma vida — e a vida cresce. Nosso sistema deve crescer com a criança, mantendo a dignidade em todas as fases."

---

## 📋 AÇÕES APROVADAS

| # | Ação | Responsável | Prioridade |
|---|------|-------------|------------|
| 1 | Criar estrutura `.bmad/templates/[ciclo]/` | Eric Evans | Alta |
| 2 | Criar `LORE/padroes_narrativos.yaml` | Tolkien + Lewis | Alta |
| 3 | Criar `regras.yaml` para Sementes | CM + Bruner | Alta |
| 4 | Atualizar workflow com parâmetro ciclo | BMAD | Alta |
| 5 | Criar `regras.yaml` para Raízes-1 | Fase 2 | Média |

---

*Reunião encerrada às 09:45 em 13/01/2026*  
*Coordenadora: Charlotte Mason*  
*Secretário: Forja (IA)*  
*Status: DECISÃO APROVADA POR UNANIMIDADE*
