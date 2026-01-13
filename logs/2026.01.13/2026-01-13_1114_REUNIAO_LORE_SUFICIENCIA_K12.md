# 🎯 REUNIÃO DE DELIBERAÇÃO: LORE é Suficiente para K-12?

**Data:** 13/01/2026 às 11:14  
**Coordenadora:** Charlotte Mason  
**Tema:** Verificar se o LORE atual cobre TODAS as necessidades de K-12  
**Modo:** `/reuniao-todos` — 14 experts convocados

---

## CONTEXTO

O LORE atual contém 7 arquivos:
1. `north_star.yaml` — Propósito, missão, princípios
2. `guardioes.yaml` — 5 Guardiões
3. `locais.yaml` — 5 Locais
4. `climas.yaml` — 8 Climas
5. `padroes_narrativos.yaml` — Regras de narração
6. `ontologia.yaml` — Atores do sistema
7. `glossario.yaml` — Termos

**Pergunta Central:** Isso é SUFICIENTE para criar lições de K até 12º ano?

---

## FASE 1: ABERTURA (Charlotte Mason)

> *"Senhores especialistas, estamos construindo um sistema K-12 — 13 anos de jornada. O LORE atual cobre o que precisamos? O que falta? O que está sobrando?"*

### Perguntas para Deliberação:
1. Cada arquivo será útil em TODOS os anos?
2. Há lacunas que só perceberemos ao criar lições avançadas?
3. Que perguntas o Maestro não está fazendo?

---

## FASE 2: POSIÇÕES INICIAIS

### 📕 J.R.R. Tolkien (Consistência/Lore)

> **POSIÇÃO:** Faltam ARTEFATOS e HISTÓRIA DO REINO.

**Embasamento:**
> "Tenho 5 Guardiões e 5 Locais. Mas onde está a HISTÓRIA do Reino? Em Legado (12º ano), a criança estuda 'história da matemática'. Preciso saber: Quando o Reino foi fundado? Quem foi o primeiro Rei? Qual é a lenda de cada Guardião completa?"

**Lacunas Identificadas:**
1. ❌ `artefatos.yaml` — Objetos mágicos/simbólicos (ex: Diário do Reino, Tocha)
2. ❌ `historia_reino.yaml` — Linha do tempo e lendas
3. ❌ Backstory completa de cada Guardião (só Bernardo tem história da Nevasca)

**Pergunta:**
> "Em Raízes-3, quando a criança explora a Vastidão, quais ARTEFATOS ela encontra? Não está definido."

---

### 📖 C.S. Lewis (Narrativa/Tom)

> **POSIÇÃO:** `padroes_narrativos.yaml` está ótimo, mas precisa de EXEMPLOS por ano.

**Embasamento:**
> "Tenho scaffolding_por_ciclo e tom_por_ciclo. Mas ciclo = grupo de anos. E os 13 ANOS individuais? O tom do 6º ano (11-12) é igual ao 8º ano (13-14)? Não deveria ser."

**Lacuna Identificada:**
1. ⚠️ Tom por ANO, não só por ciclo
2. ⚠️ Exemplos de falas de Guardião por ano

**Sugestão:**
> "Adicionar seção `exemplos_por_ano` em padroes_narrativos.yaml"

---

### 📐 Jerome Bruner (Matemática/CPA)

> **POSIÇÃO:** LORE não precisa de CPA — isso está nos templates. Correto.

**Embasamento:**
> "CPA é regra pedagógica, não dado narrativo. Está no lugar certo: templates/[ano]/regras.yaml. O LORE não precisa disso."

**Status:** ✅ Nenhuma lacuna

---

### 🐻 Lev Vygotsky (Scaffolding)

> **POSIÇÃO:** Scaffolding por ciclo está bom, mas falta PROGRESSÃO DENTRO do ciclo.

**Embasamento:**
> "Raízes vai do 1º ao 5º ano. São 5 ANOS. O scaffolding é o mesmo nesses 5 anos? Não deveria ser. Uma criança de 6 anos precisa de mais apoio que uma de 10."

**Lacuna Identificada:**
1. ⚠️ Scaffolding por ANO dentro do ciclo, não só por ciclo

**Pergunta:**
> "Quando exatamente a criança faz a transição de 'pergunta guiada' para 'pista sutil'? No 3º ano? 4º?"

---

### 🎨 Beatrix Potter (Estética)

> **POSIÇÃO:** `climas.yaml` está completo. 8 climas cobrem tudo.

**Embasamento:**
> "Ensolarado, Nublado, Ventoso, Chuvoso, Outonal, Primaveril, Crepúsculo, Estrelado. Esses 8 climas cobrem qualquer tom emocional de lição."

**Status:** ✅ Nenhuma lacuna

---

### 💰 Alex Hormozi (Value Equation)

> **POSIÇÃO:** Falta mapeamento de DOR por ano.

**Embasamento:**
> "Seth Godin define 'tribo'. Em Sementes, a dor é 'não sei se estou fazendo certo'. Em Legado, a dor é 'meu filho está pronto para a universidade?'. Essas dores são DIFERENTES."

**Lacuna Identificada:**
1. ❌ `personas_por_ano.yaml` — Dor do Portador por ano

**Pergunta:**
> "As mães personas atuais cobrem todos os anos? Ou precisamos de personas para cada fase?"

---

### 🎯 Peter Thiel (Diferenciação/Segredo)

> **POSIÇÃO:** Falta o SEGREDO de cada ano.

**Embasamento:**
> "Aprovamos propósitos narrativos por ano (Sementes = 'Números são promessas'). Mas isso está nos TEMPLATES, não no LORE. Deveria estar no LORE para ser fonte única."

**Lacuna Identificada:**
1. ⚠️ `propositos_por_ano.yaml` ou seção em north_star.yaml

**Sugestão:**
> "Mover os propósitos narrativos para LORE/north_star.yaml e referenciar nos templates"

---

### 👩‍👧 Mães Personas (UX)

> **POSIÇÃO:** `ontologia.yaml` define Portador, mas falta evolução do Portador.

**Embasamento:**
> "Em Sementes, mãe é NOVA e insegura. Em Legado, mãe é EXPERIENTE e pode liderar discussões complexas. Isso não está documentado."

**Lacuna Identificada:**
1. ⚠️ Evolução do Portador ao longo dos anos

**Pergunta:**
> "O Portador de um jovem de 17 anos faz o mesmo papel do Portador de uma criança de 5? O script pode ser igual?"

---

### 💻 Eric Evans (Engenharia/DDD)

> **POSIÇÃO:** O LORE está bem estruturado, mas falta ÍNDICE.

**Embasamento:**
> "Tenho 7 arquivos, mas quando crio uma lição do 8º ano, quais arquivos DEVO consultar? Não há um índice que diz: 'Para ano X, consulte Y, Z'."

**Lacuna Identificada:**
1. ⚠️ `index.yaml` — Mapa de navegação do LORE

**Sugestão:**
> "Criar arquivo índice que mapeia: ano → arquivos necessários"

---

### 🔧 BMAD (Orquestração)

> **POSIÇÃO:** O LORE precisa de VERSIONAMENTO por ano.

**Embasamento:**
> "Quando atualizarmos algo no Sementes, como saber se afeta Legado? Preciso de rastreabilidade."

**Sugestão:**
> "Adicionar seção `changelog` em cada arquivo LORE"

---

### 🪔 Makoto Fujimura (Kintsugi/Graça)

> **POSIÇÃO:** Falta documentar NOTAS DE GRAÇA por ano.

**Embasamento:**
> "Em Sementes, erro é 'tudo bem, tente amanhã'. Em Lógica, erro é 'o que você aprendeu com isso?'. Essa EVOLUÇÃO do tratamento do erro deve estar no LORE."

**Lacuna Identificada:**
1. ⚠️ Seção `tratamento_erro_por_ciclo` em padroes_narrativos.yaml

---

## FASE 3: SÍNTESE (Charlotte Mason)

### O que está BOM (Manter):

| Arquivo | Status | Justificativa |
|---------|--------|---------------|
| `north_star.yaml` | ✅ | Propósito e princípios completos |
| `guardioes.yaml` | ✅ | 5 Guardiões com dados essenciais |
| `locais.yaml` | ✅ | 5 Locais com atmosfera sensorial |
| `climas.yaml` | ✅ | 8 climas cobrem todas as emoções |
| `glossario.yaml` | ✅ | Termos Sistema vs Reino |
| `ontologia.yaml` | ⚠️ | Falta evolução do Portador |
| `padroes_narrativos.yaml` | ⚠️ | Falta exemplos por ano, tratamento de erro |

### LACUNAS IDENTIFICADAS:

| # | Lacuna | Prioridade | Impacto |
|---|--------|------------|---------|
| 1 | Artefatos do Reino | Alta | Lógica/Legado precisam |
| 2 | História/Lendas do Reino | Média | Enriquece profundidade |
| 3 | Propositos por ano no LORE | Alta | Templates referenciam |
| 4 | Scaffolding granular (por ano) | Média | 5 anos em Raízes |
| 5 | Evolução do Portador | Média | Script muda |
| 6 | Tratamento de erro por ciclo | Baixa | Já implícito |
| 7 | Índice do LORE | Baixa | Conveniência |

### PERGUNTAS QUE O MAESTRO NÃO ESTÁ FAZENDO:

1. **"Quais artefatos a criança coleta ao longo da jornada?"**
   - Diário do Reino (Raízes-1)?
   - Bússola de Celeste (exploração)?
   - Martelo de Bernardo (persistência)?

2. **"Há rituais de TRANSIÇÃO entre ciclos?"**
   - Sementes → Raízes: Ritual de passagem?
   - Raízes → Lógica: Cerimônia?
   - Lógica → Legado: Entrega da tocha?

3. **"Os Guardiões envelhecem ou mudam?"**
   - Tolkien pergunta: "Melquior é o mesmo leão em Sementes e Legado?"
   - Sugestão: Guardiões são eternos, mas REVELAM mais de si ao longo do tempo

4. **"Há antagonistas ou desafios?"**
   - O Reino é só paz? Ou há dificuldades narrativas?
   - Ex: "O Vento Gelado" como metáfora para frustração matemática?

5. **"O Viajante muda de título?"**
   - Sementes: Herdeiro
   - Raízes: Construtor
   - Lógica: Explorador
   - Legado: Portador da Tocha (passa adiante)

---

## FASE 4: DECISÃO FINAL (Charlotte Mason)

### ✅ PRIORIDADE ALTA — Fazer AGORA:

1. **Mover propósitos por ano para LORE:**
   - Criar seção em `north_star.yaml` ou arquivo `propositos_por_ano.yaml`
   - Templates referenciam, não duplicam

2. **Criar `artefatos.yaml`:**
   - Objetos simbólicos da jornada
   - Cada artefato tem história e significado

### ⚠️ PRIORIDADE MÉDIA — Fazer ao criar Raízes:

3. **Granular scaffolding por ano dentro de Raízes**
4. **Documentar evolução do Portador**
5. **Adicionar rituais de transição entre ciclos**

### 📌 PRIORIDADE BAIXA — Fazer quando necessário:

6. **História completa do Reino (lendas)**
7. **Índice do LORE**
8. **Changelog por arquivo**

---

## 📋 PERGUNTAS PARA O MAESTRO

Antes de implementar, preciso de suas decisões:

### 1. Artefatos do Reino
Sugestões dos experts:
- 📔 Diário do Reino (onde registra aprendizado)
- 🧭 Bússola de Celeste (direção, exploração)
- 🔨 Martelo de Bernardo (persistência)
- 🪶 Pena de Íris (atenção aos detalhes)
- ⏳ Ampulheta de Noé (paciência)
- 🔥 Tocha de Melquior (sabedoria passada adiante)

**Devo criar `artefatos.yaml` com esses itens?**

### 2. Títulos do Viajante por Ciclo
Sugestão:
- Sementes → Herdeiro
- Raízes → Construtor
- Lógica → Explorador
- Legado → Portador da Tocha

**Aprova esses títulos?**

### 3. Rituais de Transição
Deveria haver ritual narrativo quando a criança passa de ciclo?
- Sementes → Raízes: "Melquior entrega o Diário"
- Raízes → Lógica: "Celeste revela a Bússola"
- Lógica → Legado: "Melquior entrega a Tocha"

**Devo documentar esses rituais no LORE?**

---

*Reunião encerrada às 11:14 em 13/01/2026*  
*Coordenadora: Charlotte Mason*  
*Aguardando decisões do Maestro*
