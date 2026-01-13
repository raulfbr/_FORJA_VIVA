# 🎯 REUNIÃO DE DELIBERAÇÃO: LORE + Templates — Conexão Impecável

**Data:** 13/01/2026 às 10:52  
**Coordenadora:** Charlotte Mason  
**Tema:** Verificação e melhoria do LORE para conexão perfeita com Templates  
**Modo:** `/reuniao-todos` — 14 experts convocados

---

## FASE 0: INVENTÁRIO DO LORE

### Estado Atual (7 Arquivos):

| Arquivo | Bytes | Propósito | Status |
|---------|-------|-----------|--------|
| `north_star.yaml` | 20KB | Propósito, missão, princípios | ✅ GLOBAL |
| `guardioes.yaml` | 4.4KB | 5 Guardiões (dados canônicos) | ✅ GLOBAL |
| `locais.yaml` | 4.8KB | 5 Locais do Reino | ✅ GLOBAL |
| `climas.yaml` | 4.5KB | 8 Climas narrativos | ✅ GLOBAL |
| `glossario.yaml` | 4.5KB | Termos do projeto | ✅ GLOBAL |
| `ontologia.yaml` | 3.8KB | Atores do sistema | ⚠️ PRECISA ATUALIZAÇÃO |
| `padroes_narrativos.yaml` | 14KB | Regras de narração | ✅ GLOBAL + POR CICLO |

---

## FASE 1: ABERTURA (Charlotte Mason)

> *"Senhores especialistas, temos 7 arquivos LORE e 14 templates. A questão é: o LORE evolui por ano ou é sempre o mesmo? E como garantir que templates REFERENCIAM corretamente o LORE?"*

### Perguntas Centrais:
1. O LORE é GLOBAL ou evolui por ano/ciclo?
2. Cada arquivo está referenciado corretamente nos templates?
3. O que precisa ser corrigido ou melhorado?

---

## FASE 2: POSIÇÕES INICIAIS

### 📕 J.R.R. Tolkien (Consistência)

> **POSIÇÃO:** O LORE é GLOBAL — os dados não mudam. O que muda é a PROFUNDIDADE.

**Embasamento:**
> "Melquior é Melquior em Sementes e em Legado. O que muda é QUANTO dele revelamos. Em Sementes, ele apresenta. Em Legado, ele entrega a tocha. Mas os DADOS são os mesmos: cor, frase, local."

**Proposta:**
- Os arquivos LORE permanecem GLOBAIS
- Cada template pode FILTRAR o que usa
- Nova seção: `evolucao_por_ciclo` onde aplicável

---

### 📖 C.S. Lewis (Narrativa/Tom)

> **POSIÇÃO:** `padroes_narrativos.yaml` já tem evolução por ciclo. Correto.

**Embasamento:**
> "Vi o arquivo. Tem `scaffolding_por_ciclo`, `tom_por_ciclo`, `densidade_por_ciclo`. Isso está certo. O que muda é o TOM, não os Guardiões."

---

### 💻 Eric Evans (Engenharia/DDD)

> **POSIÇÃO:** Precisamos de referência BIDIRECIONAL.

**Embasamento:**
> "Os templates referenciam LORE (correto). Mas o LORE deveria listar ONDE é usado."

**Proposta:**
Adicionar em cada arquivo LORE:
```yaml
usado_por:
  - ".bmad/templates/*/regras.yaml"
  - "curriculo/*/lições"
```

---

### 🎨 Beatrix Potter (Estética)

> **POSIÇÃO:** `climas.yaml` está perfeito. 8 climas cobrem todos os tons.

**Embasamento:**
> "Olhei o arquivo. Tem Ensolarado, Nublado, Ventoso, Chuvoso, Outonal, Primaveril, Crepúsculo, Estrelado. Suficiente para qualquer lição."

---

### 📐 Jerome Bruner (Matemática/CPA)

> **POSIÇÃO:** CPA está nos templates, não no LORE. Correto.

**Embasamento:**
> "CPA é regra por ciclo, não dado global. Está certo estar em `templates/[ciclo]/regras.yaml`, não no LORE."

---

### 🐻 Lev Vygotsky (Scaffolding)

> **POSIÇÃO:** `padroes_narrativos.yaml` tem scaffolding por ciclo. Correto.

**Verificação:**
```yaml
scaffolding_por_ciclo:
  - ciclo: sementes → "Mão-na-mão"
  - ciclo: raizes_1 → "Pergunta guiada"
  - ciclo: logica → "Produtive struggle"
  - ciclo: legado → "Autonomia total"
```
✅ Presente

---

### 🔧 BMAD (Orquestração)

> **POSIÇÃO:** `ontologia.yaml` precisa atualizar referências.

**Problema encontrado:**
```yaml
referencias:
  agentes: "forja-core/conselheiros/*.md"  # ❌ ANTIGO
```

**Correção:**
```yaml
referencias:
  agentes: ".bmad/experts/"  # ✅ NOVO
```

---

### 👩‍👧 Mães Personas (UX)

> **POSIÇÃO:** O LORE não precisa de nada específico para nós.

**Embasamento:**
> "Os selos estão nos templates. O LORE é para narrativa, não UX. Está correto."

---

## FASE 3: SÍNTESE (Charlotte Mason)

### O que está CERTO:
1. ✅ LORE é GLOBAL — dados não mudam por ano
2. ✅ `padroes_narrativos.yaml` tem evolução por ciclo
3. ✅ Templates referenciam LORE corretamente
4. ✅ `climas.yaml` cobre todos os tons necessários
5. ✅ `guardioes.yaml` está completo

### O que PRECISA MELHORAR:
1. ⚠️ `ontologia.yaml` → Atualizar referências antigas
2. ⚠️ Cada arquivo LORE → Adicionar seção `usado_por`
3. ⚠️ Cada arquivo LORE → Adicionar seção `proposito`

---

## FASE 4: DECISÃO FINAL (Charlotte Mason)

### ✅ DECISÃO APROVADA

**1. LORE permanece GLOBAL:**
- Guardiões, Locais, Climas: mesmos em todos os anos
- O que muda é a PROFUNDIDADE de uso, não os dados

**2. Atualizar cada arquivo LORE com header padronizado:**
```yaml
# ════════════════════════════════════════════
# [NOME DO ARQUIVO]
# ════════════════════════════════════════════
# 
# PROPÓSITO: [descrição clara]
# 
# USADO POR:
#   - .bmad/templates/*/regras.yaml
#   - curriculo/*/lições
#   - workflows/criar-licao-premium.yaml
# 
# EVOLUI POR CICLO: Não (dados estáticos)
# ════════════════════════════════════════════
```

**3. Corrigir `ontologia.yaml`:**
- Linha 152: `forja-core/conselheiros/*.md` → `.bmad/experts/`

**4. Verificar conexões:**

| Template Referencia | LORE Arquivo | Status |
|--------------------|--------------|--------|
| `lore_guardioes` | `LORE/guardioes.yaml` | ✅ |
| `lore_locais` | `LORE/locais.yaml` | ✅ |
| `lore_narrativo` | `LORE/padroes_narrativos.yaml` | ✅ |
| `north_star` | `LORE/north_star.yaml` | ✅ |
| `climas` | `LORE/climas.yaml` | ⚠️ Não referenciado |

---

## 📋 AÇÕES APROVADAS

| # | Ação | Impacto |
|---|------|---------|
| 1 | Atualizar `ontologia.yaml` linha 152 | Baixo |
| 2 | Adicionar header com propósito em cada arquivo LORE | Médio |
| 3 | Adicionar referência a `climas.yaml` nos templates | Baixo |
| 4 | Criar README.md para LORE explicando estrutura | Médio |

---

## RESPOSTA À PERGUNTA DO MAESTRO

### "O LORE precisa evoluir ao longo dos anos?"

> **NÃO.** O LORE são DADOS CANÔNICOS que não mudam.
> 
> O que evolui são as REGRAS DE USO, que estão nos templates.
> 
> Exemplo:
> - `guardioes.yaml` → Melquior sempre tem a mesma frase canônica
> - `templates/00_K_sementes/regras.yaml` → Em Sementes, usa frase X
> - `templates/12_12ano_legado/regras.yaml` → Em Legado, usa frase Y
> 
> O DADO é o mesmo. O USO é diferente.

---

*Reunião encerrada às 10:52 em 13/01/2026*  
*Coordenadora: Charlotte Mason*
