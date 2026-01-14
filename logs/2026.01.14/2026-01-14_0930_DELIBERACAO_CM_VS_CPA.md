# 🏛️ DELIBERAÇÃO — CM vs Singapura: Proporção Concreto em Sementes

**Data:** 14/01/2026 09:30  
**Modo:** REUNIÃO (Debate Multi-Expert)  
**Tema:** Inconsistência entre CM (100% Concreto) e CPA (60% Concreto) em Sementes  
**Requerente:** Maestro (Usuário)  
**Mediador:** Melquior (Orchestrator)

---

## 📋 O CONFLITO

| Fonte | Afirmação | Localização |
|-------|-----------|-------------|
| **Charlotte Mason** | 100% Concreto em Sementes (0-6 anos) | `charlotte_mason.yaml` VR-001: "Things before Signs" |
| **Jerome Bruner (CPA)** | 60% Concreto mínimo | `regras.yaml` linha 53-54 |
| **Triade.yaml** | CPA subordinado a CM | `triade.yaml` linha 6-8: "coordenador: Charlotte Mason" |

**Questão central:** Qual é a proporção correta de Concreto em Sementes?

---

## 🗣️ DEBATE DOS EXPERTS

### 🏛️ CHARLOTTE MASON (Coordenadora — PRI 1)

> **"Minha posição é clara: Things before Signs. Em Sementes (0-6 anos), a criança conhece COISAS reais antes de signos abstratos."**

**Argumentos:**
1. **Princípio 1:** "Children are born persons" — tratar com respeito significa não apressar desenvolvimento cognitivo.
2. **Citação fundante:** "Give them THINGS before signs" (baseado em Pestalozzi).
3. **Fisiologia:** O córtex pré-frontal (abstração) ainda está em desenvolvimento intenso até ~7 anos.

**Veto VR-001:**
```yaml
VR-001:
  trigger: pictorial_before_concrete
  ciclo: Sementes
  decisao: REJECT
  why: "CM - Things before Signs. Em Sementes só CONCRETO"
```

**Conclusão CM:** 
> "Aceito uma margem de 10-20% para reconhecimento visual do símbolo (Abstrato mínimo), mas o FOCO deve ser 80%+ Concreto. Pictórico é VETADO em Sementes, exceto L000."

---

### 📐 JEROME BRUNER (CPA — PRI 7, subordinado a CM)

> **"Minha teoria do Enativo apoia Charlotte Mason. Em 0-6 anos, o estágio ENATIVO (Concreto) é dominante."**

**Argumentos:**
1. **Teoria Enativa (1966):** "Aprender fazendo. Manipulativos físicos. Ação direta objetos."
2. **Idade 0-6:** Classificado como "primário" na teoria — 100% enativo.
3. **Spiral Curriculum:** O Pictórico retorna em Raízes (7-10 anos) com mais complexidade.

**Reconhecimento:**
> "O '60% Concreto' no arquivo de regras foi uma interpretação LIBERAL da minha teoria. Na verdade, para 0-6 anos, minha recomendação original é Concreto PREDOMINANTE (80-100%)."

**Proposta de Correção:**
```yaml
# ANTES (regras.yaml):
concreto:
  minimo: 60
  maximo: 80

# DEPOIS (alinhado CM):
concreto:
  minimo: 80
  maximo: 100
  nota: "CM lidera. Bruner concorda: Enativo predomina 0-6 anos."
```

---

### 🦁 MELQUIOR (Orchestrator — Mediador)

**Consulta a outros experts:**

#### CS Lewis (Narrativa):
> "Se a criança TOCA a semente, ela VIVE o número. Não a infantilize com desenhinhos. Ela pode manipular objetos reais."

#### Mães Personas (UX):
> **Priscila (Prática):** "Menos material impresso = menos tinta = menos dinheiro. Concreto puro funciona."
> **Júlia (Relacional):** "Meu filho ama brincar com objetos. Desenhar ele cansa."

#### Vygotsky (ZPD):
> "O scaffolding 'mão-na-mão' é inerentemente concreto. Você não segura a mão da criança para desenhar — você conta objetos JUNTOS."

---

## 📊 CONSENSO DO CONSELHO

| Expert | Voto | Proporção Concreto |
|--------|------|-------------------|
| Charlotte Mason | ✅ | 80-100% |
| Jerome Bruner | ✅ | 80-100% (alinhado CM) |
| CS Lewis | ✅ | 100% (objetos reais > desenhos) |
| Mães Personas | ✅ | 80%+ (praticidade) |
| Vygotsky | ✅ | 80%+ (scaffolding concreto) |

**Votação: 5/5 a favor de 80-100% Concreto em Sementes**

---

## 🔧 SUGESTÕES DE AÇÃO

### Opção A: Correção Conservadora (Recomendada)
```yaml
# .bmad/templates/00_K_sementes/regras.yaml
cpa:
  concreto:
    minimo: 80
    maximo: 100
    descricao: "Manipulativos reais, toque, movimento"
    obrigatorio: true
    nota_cm: "CM lidera. 'Things before Signs'. Bruner concorda."
    
  pictorico:
    status: VETADO
    excecao: "L000 apenas, ou extensão opcional 'Se Quiser Voar'"
    
  abstrato:
    maximo: 20
    tipo: "Reconhecimento visual apenas"
    descricao: "Desenhar símbolo NO AR, reconhecer visualmente"
    proibido: ["Escrever no papel", "Contas escritas"]
```

### Opção B: Correção Radical (100% Concreto)
```yaml
cpa:
  concreto:
    minimo: 100
    descricao: "SOMENTE manipulativos. Zero representação."
    
  pictorico:
    status: VETADO_TOTAL
    
  abstrato:
    maximo: 0
    nota: "Nenhum símbolo. Só números falados, nunca escritos."
```

### Opção C: Meio-termo com "Bônus Pictórico"
```yaml
cpa:
  concreto:
    minimo: 80
    
  pictorico:
    status: OPCIONAL_BONUS
    quando: "Seção 'Se Quiser Voar' - apenas se criança pedir"
    
  abstrato:
    maximo: 20
    tipo: "Reconhecimento NO AR"
```

---

## 📝 DECISÃO PENDENTE DO MAESTRO

**Melquior (Orchestrator) recomenda: Opção A (Conservadora)**

**Razões:**
1. Mantém 80%+ Concreto (alinhado CM)
2. Permite 20% Abstrato mínimo (reconhecimento visual — já fazemos)
3. Pictórico vetado por padrão, mas disponível como bônus opcional
4. Não quebra lições já escritas

**Aguardando sua decisão para atualizar:**
- `regras.yaml`
- `triade.yaml`
- Template de lições

---

## 📚 REFERÊNCIAS CITADAS

1. Mason, Charlotte. *Home Education*, 1886 — "Things before Signs"
2. Bruner, Jerome. *Toward a Theory of Instruction*, 1966 — Estágio Enativo
3. Pestalozzi, Johann. *How Gertrude Teaches Her Children*, 1801 — Fundamento "Object Lessons"
4. Ministry of Education Singapore. *Primary Mathematics Syllabus* — CPA adaptado para 0-6

---

**Assinado:**
- 🦁 Melquior (Mediador)
- 📚 Charlotte Mason (Coordenadora)
- 📐 Jerome Bruner (CPA)
- ✍️ CS Lewis (Narrativa)
- 🐻 Vygotsky (ZPD)
- 👩‍👧 Tribunal das Mães

---

# 📌 CONTINUAÇÃO — 09:41

## ⚠️ PONTO LEVANTADO PELO MAESTRO

> "Tem que deixar claro que MELQUIOR é só do REINO CONTADO. Ele não aparece em discussões técnicas."

---

## 🏛️ DELIBERAÇÃO: DISTINÇÃO DE PAPÉIS

### O Problema Identificado
O uso de "Melquior" como mediador de deliberações técnicas mistura dois domínios:
1. **REINO CONTADO** — Narrativa imersiva (Guardiões, Herdeiros, etc.)
2. **SISTEMA IA** — Orquestração técnica (Orchestrator, Experts, Workflows)

### Mapa de Papéis (north_star.yaml)

| Domínio | Papel | Descrição |
|---------|-------|-----------|
| **Reino Contado** | Melquior | Guardião Leão, Mestre, Mentor narrativo. Aparece APENAS nas lições. |
| **Reino Contado** | Herdeiro | Viajante do ciclo Sementes (4-6 anos) |
| **Reino Contado** | Construtor | Viajante do ciclo Raízes (6-10 anos) |
| **Reino Contado** | Portador da Tocha | Viajante do ciclo Legado (14-18 anos). DIFERENTE de "Portador" (pai). |
| **Sistema IA** | Orchestrator | IA que coordena experts. NÃO é personagem narrativo. |
| **Família** | Portador | O pai/mãe que conduz a lição. Carrega a "tocha" da educação. |
| **Família** | Mentor/Maestro | Título opcional para pais avançados. |

### Regra Proposta

```yaml
# orchestrator.yaml — Adicionar seção de clarificação
distincao_papeis:
  regra: |
    NUNCA misturar domínio narrativo (Reino Contado) com domínio técnico (Sistema IA).
    
  narrativo:
    contexto: "Dentro das lições, materiais para crianças"
    personagens: [Melquior, Noé, Celeste, Bernardo, Íris]
    viajantes: [Broto, Herdeiro, Construtor, Explorador, Portador da Tocha]
    
  tecnico:
    contexto: "Deliberações IA, workflows, logs"
    atores: [Orchestrator (IA), Experts (CM, Bruner, Lewis...), QA, Engenharia]
    
  familia:
    contexto: "Pais e mães que aplicam o currículo"
    titulos: [Portador (pai/mãe), Maestro (avançado), Matriarca (mãe)]
    
  erros_evitar:
    - "Melquior aprova esta lição" → Deve ser: "CM aprova esta lição"
    - "O Herdeiro valida o HTML" → Deve ser: "QA valida o HTML"
```

---

## 🖐️ DELIBERAÇÃO: "ESCREVER NO AR" — É ÚTIL?

### A Questão do Maestro
> "Isso de escrever no AR ajuda? O que a CM fala?"

### Consulta aos Experts

#### Charlotte Mason (Coordenadora):
> "Eu não uso a expressão 'escrever no ar'. Meu foco é em COISAS reais antes de SIGNOS."
>
> **Referência:** Home Education, Vol. 1 — "The child should not be taught to write until he can read."
>
> No entanto, traçar formas com o DEDO (no ar, na areia, na mesa) é parte do **handicraft** e da **educação sensorial**. Não é "escrita" — é **exploração tátil do formato**.

#### Jerome Bruner (CPA):
> "Traçar no ar é ENATIVO, não SIMBÓLICO. A criança usa o CORPO para sentir a forma. Isso é CONCRETO, não abstrato."
>
> **Distinção importante:**
> - ❌ Escrever no papel = Abstrato (símbolo fixo)
> - ✅ Traçar no ar = Enativo (movimento corporal)

#### Vygotsky (Scaffolding):
> "Mão-na-mão: o pai guia a mão da criança no ar. Isso é scaffolding corporal. A criança SENTE o movimento antes de abstrair."

### Conclusão do Conselho

| Atividade | Classificação | Permitido em Sementes? |
|-----------|---------------|------------------------|
| Escrever no PAPEL | Abstrato | ❌ NÃO |
| Traçar no AR com dedo | Enativo/Concreto | ✅ SIM (movimento corporal) |
| Traçar na AREIA/MESA | Enativo/Concreto | ✅ SIM (tátil) |
| Reconhecer símbolo visualmente | Abstrato mínimo | ⚠️ Limitado (10-20%) |

**Veredicto:** "Escrever no ar" é mal-nomeado. Deve ser chamado de **"Traçar no ar"** e é classificado como CONCRETO (movimento corporal), não Abstrato.

---

## 🔀 NOVA OPÇÃO: HÍBRIDA A+C

### O Pedido do Maestro
> "Eu gosto da opção C no sentido de se a criança quiser ela tem a opção de fazer... mas sempre com orientação de ser concreto."

### Opção D: Híbrida (Concreto Norte + Bônus Opcional)

```yaml
cpa_sementes:
  filosofia: |
    CM LIDERA. Concreto é o NORTE absoluto.
    "Se Quiser Voar" é convite, não obrigação.
    
  concreto:
    minimo: 80
    maximo: 100
    obrigatorio: true
    nota: "NORTE ABSOLUTO. Manipulativos reais, toque, movimento."
    tracar_no_ar:
      permitido: true
      classificacao: "ENATIVO (movimento corporal, não símbolo)"
      nota: "Traçar no ar = concreto. Escrever no papel = vetado."
    
  pictorico:
    status: VETADO_PADRAO
    excecao: "Seção 'Se Quiser Voar' — apenas se criança demonstrar interesse espontâneo"
    nota: |
      O pai NÃO oferece pictórico. Se a criança PEDIR para desenhar,
      pode permitir como extensão opcional. NUNCA como parte core.
    
  abstrato:
    maximo: 20
    tipo: "Reconhecimento visual + traçar no ar"
    permitido:
      - "Traçar número no ar com o dedo (enativo)"
      - "Reconhecer símbolo visualmente"
      - "Ouvir o nome do número"
    proibido:
      - "Escrever no papel"
      - "Fazer contas escritas"
      - "Memorização forçada de símbolos"
      
  extensao_se_quiser_voar:
    titulo: "Se Quiser Voar"
    regra: |
      APENAS se os olhos da criança pedirem "MAIS!".
      O pai NÃO sugere — a criança demonstra interesse.
    permitido_bonus:
      - "Desenhar o que aprendeu (se ela quiser)"
      - "Traçar número na areia/mesa"
      - "Contar objetos extras"
    nota_cm: |
      "Não force. Se ela quiser, permita.
      O interesse espontâneo é sinal de prontidão."
```

---

## 📊 COMPARAÇÃO FINAL DAS OPÇÕES

| Aspecto | A (Conservadora) | B (Radical) | C (Meio-termo) | **D (Híbrida)** |
|---------|------------------|-------------|----------------|-----------------|
| Concreto mínimo | 80% | 100% | 80% | **80%** |
| Pictórico | Vetado | Vetado total | Bônus | **Vetado + Bônus SE pedir** |
| Abstrato | 20% | 0% | 20% | **20% (traçar no ar = enativo)** |
| "Se Quiser Voar" | Sem menção | Sem menção | Inclui | **Inclui com regra clara** |
| Traçar no ar | Abstrato | Vetado | Abstrato | **Reclassificado como ENATIVO** |

---

## ✅ RECOMENDAÇÃO FINAL DO CONSELHO

**Opção D (Híbrida)** é a mais alinhada com:
1. **CM:** Norte de Concreto preservado, sem forçar abstrato
2. **Bruner:** Traçar no ar = Enativo, não Simbólico
3. **Mães:** Pictórico só se criança pedir (menos pressão)
4. **Vygotsky:** Scaffolding corporal (mão-na-mão) valorizado

---

## 📝 AÇÕES PENDENTES (Aguardando Maestro)

1. [x] Aprovar Opção D (Híbrida)? ✅ APROVADO 09:48
2. [x] Atualizar `regras.yaml` com nova proporção? ✅ FEITO (80-100% Concreto)
3. [x] Adicionar `distincao_papeis` ao `orchestrator.yaml`? ✅ FEITO (Maestro=Raul, Matriarca=Marina)
4. [x] Renomear "escrever no ar" para "traçar no ar" nos templates? ✅ FEITO (L001 atualizada)

---

**Assinado (Continuação):**
- 🤖 Orchestrator (IA — não Melquior)
- 📚 Charlotte Mason
- 📐 Jerome Bruner
- 🐻 Vygotsky
