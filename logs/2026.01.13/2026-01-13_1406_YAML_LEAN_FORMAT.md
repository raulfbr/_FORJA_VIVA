# 🔧 DELIBERAÇÃO TÉCNICA — Otimização do Formato YAML

**Data:** 13/01/2026 às 14:06  
**Tipo:** Análise Técnica  
**Participantes:** BMAD Method, Eric Evans (DDD)

---

## 📋 PROBLEMA IDENTIFICADO

O Maestro observou corretamente que nossos arquivos YAML têm:

| Desperdício | Exemplo | Bytes gastos |
|-------------|---------|--------------|
| **Emojis** | `📚`, `🎯`, `✅` | 3-4 bytes cada |
| **Separadores decorativos** | `════════════════════` | 80+ bytes por linha |
| **Comentários longos** | `# ─────────────────` | 40+ bytes |
| **Descrições verbose** | Parágrafos explicativos | Centenas de bytes |

### Exemplo do problema atual:

```yaml
# ════════════════════════════════════════════════════════════════════════════════
# CHARLOTTE MASON — Coordenadora da Tríade Pedagógica
# ════════════════════════════════════════════════════════════════════════════════
# Fonte: Home Education Series (6 volumes), 20 Principles
# Última Atualização: 12/01/2026

id: charlotte_mason
tipo: expert
conselho: pedagogia
role: coordenadora  # Tem veto final em conflitos

# ════════════════════════════════════════════════════════════════════════════════
# DADOS BIOGRÁFICOS
# ════════════════════════════════════════════════════════════════════════════════

nome: Charlotte Maria Shaw Mason
titulo: "A Governanta — Coordenadora da Tríade"
```

**Problema:** ~500 bytes gastos apenas com decoração visual que a IA não precisa!

---

## 🎯 OBJETIVO

Criar formato YAML **LEAN** (enxuto) para:
1. Minimizar tokens/contexto consumido pela IA
2. Manter TODA informação semântica necessária
3. Gerar versão "bonita" sob demanda (não padrão)

---

## ✅ PROPOSTA: YAML LEAN FORMAT

### Regras do Formato Lean:

| Regra | Antes | Depois |
|-------|-------|--------|
| **Sem emojis** | `📚 Pedagogia` | `pedagogia` |
| **Sem separadores** | `════════════` | (remover) |
| **Sem comentários decorativos** | `# ─────────` | (remover) |
| **Keys curtas** | `descricao_completa` | `desc` |
| **Valores inline** | Multi-linha | Single-line quando possível |
| **Sem redundância** | `tipo: expert\n conselho: pedagogia` | `type: expert.pedagogia` |

### Exemplo LEAN (charlotte_mason.yaml):

```yaml
# LEAN FORMAT v1.0
id: charlotte_mason
type: expert.pedagogia
role: coordinator
veto: ABSOLUTE

bio:
  name: Charlotte Maria Shaw Mason
  years: 1842-1923
  nation: UK
  works: [Home Education, Parents and Children, School Education, Ourselves, Formation of Character, A Philosophy of Education]

philosophy:
  core: Children are born persons
  instruments: [atmosphere, discipline, life]
  motto: Education is an atmosphere, a discipline, a life

principles:
  - {n: 1, en: Children are born persons, pt: Crianças nascem pessoas, apply: respeitar}
  - {n: 2, en: Not born good or bad, pt: Não nascem boas nem más, apply: educar para o bem}
  - {n: 3, en: Authority and obedience are fundamental, pt: Autoridade e obediência, apply: liderar com amor}
  # ... (20 total, formato compacto)

veto_rules:
  - {id: VR001, trigger: pictorial_before_concrete, action: REJECT, reason: Sementes só Concreto}
  - {id: VR002, trigger: lesson_gt_20min, action: REJECT, reason: Princípio 13}
  - {id: VR003, trigger: over_explanation, action: REJECT, reason: Apresentar não explicar}
  - {id: VR004, trigger: no_narration, action: REJECT, reason: Princípio 14}
  - {id: VR005, trigger: child_as_object, action: REJECT, reason: Princípio 1}
  - {id: VR006, trigger: exclusionary_lang, action: WARN, reason: Inclusão} 

audit:
  - {id: AQ001, q: Criança respeitada como pessoa?, ref: P1}
  - {id: AQ002, q: Lição curta (≤20min)?, ref: P13}
  - {id: AQ003, q: CPA usado (Concreto primeiro)?, ref: things_before_signs}
  - {id: AQ004, q: Narração incluída?, ref: P14}
  - {id: AQ005, q: Ideia Viva apresentada (não explicada)?, ref: P8}

refs:
  primary: [Home Education Series]
  sites: [amblesideonline.org, simplycharlottemason.com]
```

---

## 📊 COMPARAÇÃO DE ECONOMIA

| Métrica | Formato Atual | Formato Lean | Economia |
|---------|---------------|--------------|----------|
| **Linhas** | 380 | ~80 | **-79%** |
| **Bytes** | 16,511 | ~3,500 | **-79%** |
| **Tokens (aprox)** | ~4,000 | ~900 | **-77%** |
| **Informação perdida** | — | **ZERO** | — |

### A IA precisa de:
- ✅ IDs para referenciar
- ✅ Regras para aplicar
- ✅ Princípios para validar
- ✅ Perguntas de auditoria

### A IA NÃO precisa de:
- ❌ Emojis decorativos
- ❌ Separadores visuais
- ❌ Descrições narrativas longas
- ❌ Citações literárias extensas

---

## 🔧 ENGENHARIA: PARECER TÉCNICO

### Eric Evans (DDD)
> "YAML para máquina deve ser data-oriented, não human-readable. Humanos podem pedir versão formatada quando necessário. Single Source of Truth deve ser LEAN."

### BMAD Method
> "Agent-as-Code funciona melhor com arquivos compactos. Menos contexto = mais espaço para raciocínio. Formato atual consome tokens desnecessariamente."

### Consenso:
> "Implementar YAML Lean como padrão. Manter arquivos atuais em `_LEGADO/` para referência humana. Gerar versão 'bonita' sob demanda."

---

## 📝 CONVENÇÕES DO FORMATO LEAN

### 1. Nomenclatura de Keys:

| Atual | Lean |
|-------|------|
| `descricao` | `desc` |
| `principios` | `rules` ou omitir (implícito) |
| `aplicacao` | `apply` |
| `referencia` | `ref` |
| `pergunta` | `q` |
| `resposta` | `a` |
| `numero` | `n` |
| `condicao` | `if` |
| `acao` | `do` |

### 2. Estrutura Inline (para listas curtas):

```yaml
# ANTES (4 linhas)
materiais:
  - item: pedras
    quantidade: 5
    alternativa: botões

# DEPOIS (1 linha)
materials: [{item: pedras, qty: 5, alt: botões}]
```

### 3. Enums Implícitos:

```yaml
# ANTES
tipo: expert
conselho: pedagogia
role: coordenadora

# DEPOIS
type: expert.pedagogia.coordinator
```

### 4. Sem Headers Decorativos:

```yaml
# ANTES
# ════════════════════════════════════════════════════════════════════════════════
# SEÇÃO IMPORTANTE
# ════════════════════════════════════════════════════════════════════════════════

# DEPOIS
# (nada, vai direto ao conteúdo)
```

---

## ✅ DECISÃO

### Implementar em 2 passos:

**Passo 1 (Agora):** 
- Definir especificação YAML Lean v1.0
- Criar conversor de referência

**Passo 2 (Gradual):**
- Converter arquivos mais usados primeiro (orchestrator, CM, north_star)
- Manter originais em `_LEGADO/yaml_verbose/`

### O que NÃO fazer:
- ❌ Converter tudo de uma vez (risco de quebrar)
- ❌ Perder informação semântica
- ❌ Remover comentários explicativos ESSENCIAIS

---

## ❓ PERGUNTAS PARA O MAESTRO

1. **Aprovar YAML Lean como padrão?**

2. **Converter quais arquivos primeiro?**
   - [ ] orchestrator.yaml
   - [ ] charlotte_mason.yaml
   - [ ] north_star.yaml
   - [ ] Outros?

3. **Manter versão "bonita" em paralelo?** (para humanos lerem)

4. **Quais keys abreviar?** (proposta acima está boa?)

---

## 📋 ESPECIFICAÇÃO YAML LEAN v1.0

```yaml
# YAML LEAN FORMAT SPECIFICATION v1.0
# For AI consumption - minimal tokens, maximum data

spec:
  version: "1.0"
  purpose: "Minimize context, preserve semantics"
  
rules:
  - no_emojis: true
  - no_decorative_separators: true
  - no_verbose_comments: true
  - inline_short_lists: true
  - abbreviated_keys: true
  - max_line_length: 120
  
key_abbrev:
  description: desc
  application: apply
  reference: ref
  question: q
  answer: a
  number: n
  condition: if
  action: do
  quantity: qty
  alternative: alt
  
type_notation:
  pattern: "category.subcategory.role"
  example: "expert.pedagogia.coordinator"
```

---

> *"Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."*  
> — Antoine de Saint-Exupéry

> *"Menos tokens = mais espaço para pensar."*  
> — BMAD Method

---

**Deliberação técnica aprovada por Engenharia.**  
**Aguardando decisão do Maestro para implementação.**
