# 🎯 DELIBERAÇÃO CRÍTICA — Tríade vs BMAD v6

**Data:** 13/01/2026 às 14:04  
**Tipo:** Análise Crítica Interna  
**Propósito:** Determinar o que REALMENTE precisamos do BMAD v6

---

> [!IMPORTANT]
> Esta deliberação questiona: "A Tríade já não é forte o suficiente? Precisamos mesmo de tudo isso do BMAD v6?"

---

## 📋 CONTEXTO DA DISCUSSÃO

### O que já temos (north_star.yaml + experts):

| Componente | Status | Análise |
|------------|--------|---------|
| **Tríade** (CM + CPA + TGTB) | ✅ COMPLETO | 3 pilares bem definidos |
| **Charlotte Mason** | ✅ COMPLETO | 20 Princípios + 6 Veto Rules + 6 Audit Questions |
| **Jerome Bruner** | ✅ COMPLETO | CPA estruturado |
| **North Star** | ✅ COMPLETO | 8 Princípios Fundamentais + métricas |
| **14 Experts** | ✅ COMPLETO | 7 conselhos organizados |
| **LORE** | ✅ COMPLETO | 12 arquivos interconectados |
| **Templates** | ✅ COMPLETO | 13 anos + globais |
| **Workflows** | ✅ COMPLETO | 4 workflows |

### O que o BMAD v6 propõe adicionar:

| Componente | Propósito | Já temos equivalente? |
|------------|-----------|----------------------|
| PeRD (Pedagogical Requirements Doc) | Definir lição antes de escrever | ⚠️ PARCIAL (perd-template.yaml existe) |
| Reasoning Loops | Ciclos de refinamento | ❌ NÃO |
| QA Adversarial | Simulação de cenários | ⚠️ PARCIAL (mães_personas) |
| Agent-as-Code | Formato padrão experts | ⚠️ PARCIAL (já são YAML) |
| PADR | Decisões versionadas | ❌ NÃO |

---

## 🗣️ DISCUSSÃO INTERNA — A TRÍADE

### Charlotte Mason (Coordenadora)
> "Meus 20 Princípios são completos. Meu arquivo já tem 6 Veto Rules e 6 Audit Questions. O que mais precisamos?"

**Análise do arquivo `charlotte_mason.yaml`:**
- ✅ VR-001: Veta Pictórico antes de Concreto
- ✅ VR-002: Veta lição > 20 min
- ✅ VR-003: Veta over-explanation
- ✅ VR-004: Veta ausência de narração
- ✅ VR-005: Veta tratar criança como objeto
- ✅ VR-006: Alerta linguagem excludente

> "Isso já É um sistema de validação. Não preciso de 'Reasoning Loops' — preciso que as regras sejam APLICADAS."

---

### C.S. Lewis (Narrativa)
> "Concordo com Charlotte. O problema não é falta de regras — é garantir que sejam usadas. BMAD v6 parece adicionar burocracia."

**Contra-argumento:**
> "Porém... a ideia de REVISAR antes de publicar tem mérito. Hoje criamos e só depois verificamos. Loops permitem pegar problemas ANTES."

---

### TGTB (Scope & Sequence)
> "Sou apenas referência de sequência. Não tenho opinião sobre processos. O que importa é que os conceitos matemáticos estejam na ordem certa."

---

## 🔍 ANÁLISE CRÍTICA: O QUE REALMENTE PRECISAMOS?

### O CORE do BMAD v6 (essência):

1. **Documentação-como-Fonte-da-Verdade** → ✅ JÁ TEMOS (LORE)
2. **Experts especializados** → ✅ JÁ TEMOS (14 experts)
3. **Validação antes de produção** → ⚠️ PARCIAL
4. **Ciclos de refinamento** → ❌ NÃO TEMOS
5. **Decisões versionadas** → ❌ NÃO TEMOS

### O que NÃO precisamos:

- ❌ **Agent-as-Code formal** → Nossos experts já são YAML estruturado
- ❌ **Codinomes** (Sofia, Veritas) → Usamos nomes reais
- ❌ **Reasoning Loops complexos** → Simples "revisar antes de publicar" basta
- ❌ **Story Files atomizados** → Nosso template já é completo

---

## 💡 SÍNTESE: O MELHOR DOS DOIS MUNDOS

### O que MANTER do nosso sistema:

| Item | Motivo |
|------|--------|
| **Tríade** (CM + CPA + TGTB) | É a essência do projeto |
| **20 Princípios CM** | Já são regras de validação |
| **6 Veto Rules** | Já implementadas no CM |
| **14 Experts reais** | Nomes reais, conhecimento real |
| **LORE como SSOT** | 12 arquivos canônicos |
| **north_star.yaml** | 748 linhas de orientação |

### O que ADOTAR do BMAD v6 (versão simplificada):

| Conceito BMAD | Nossa Adaptação Simplificada |
|---------------|------------------------------|
| **PeRD** | Expandir `perd-template.yaml` com campos obrigatórios |
| **Reasoning Loops** | Adicionar 1 checkpoint de revisão no workflow |
| **QA Adversarial** | Formalizar "Teste do Café" como cenários |

### O que NÃO adotar:

| Conceito BMAD | Por que não |
|---------------|-------------|
| Agent-as-Code | Já temos YAML — funciona |
| PADR | Nice-to-have, não bloqueador |
| Codinomes | Confunde mais que ajuda |
| Story Files | Template já é completo |

---

## ✅ DECISÃO FINAL DOS EXPERTS

### Charlotte Mason (Voto Decisivo)
> "A Tríade é forte. O BMAD v6 tem ideias boas, mas não precisamos de tudo. Adotar apenas:
> 1. PeRD expandido (5 campos obrigatórios)
> 2. UM checkpoint de revisão (não loops complexos)
> 3. Teste do Café formalizado"

**VOTO:** ✅ SIMPLIFICAR

### C.S. Lewis
> "Concordo. Menos é mais. Tom Noble sobre burocracia."

**VOTO:** ✅ SIMPLIFICAR

### Jerome Bruner
> "CPA já está funcionando. Não precisa de mais camadas."

**VOTO:** ✅ SIMPLIFICAR

### Eric Evans
> "LORE já é SSOT. Adicionar mais documentação pode criar duplicação."

**VOTO:** ✅ SIMPLIFICAR

### Susan Macaulay
> "Famílias não se importam com 'Reasoning Loops'. Querem lições que funcionem."

**VOTO:** ✅ SIMPLIFICAR

---

## 📝 PLANO REVISADO (VERSÃO FINAL SIMPLIFICADA)

### O que fazer AGORA:

| Ação | Descrição | Tempo |
|------|-----------|-------|
| **1** | Expandir `perd-template.yaml` com 5 campos obrigatórios | 10 min |
| **2** | Adicionar 1 checkpoint de revisão no workflow | 10 min |
| **3** | Formalizar "Teste do Café" (3 cenários) | 10 min |

### Total: ~30 minutos (não 5 fases de horas)

### O que NÃO fazer:

- ❌ Agent-as-Code (desnecessário)
- ❌ PADR formal (nice-to-have futuro)
- ❌ Loops complexos (simplificar para 1 checkpoint)
- ❌ 5 cenários QA (reduzir para 3 essenciais)

---

## 🔧 IMPLEMENTAÇÃO SIMPLIFICADA

### 1. PeRD Expandido (5 campos obrigatórios)

```yaml
# perd-template.yaml atualizado

campos_obrigatorios:
  1_ideia_viva: str        # O Segredo em uma frase
  2_principio_cm: int      # Qual dos 20 Princípios aplica (1-20)
  3_estrutura_cpa: 
    concreto: str          # O que a criança FAZ
    abstrato: str          # O símbolo introduzido
  4_guardiao: enum         # Qual guardião lidera
  5_tempo: int             # ≤ 20 min

# Se qualquer campo vazio ou inválido → BLOQUEAR criação
```

### 2. Checkpoint de Revisão (1 único)

```yaml
# Adicionar em criar-licao-premium.yaml

checkpoint_revisao:
  quando: "Após fase 2 (Desenvolvimento)"
  quem: "Charlotte Mason + C.S. Lewis"
  perguntas:
    - "Ideia Viva está clara?"
    - "Tom é nobre (não condescendente)?"
    - "Tempo ≤ 20 min?"
  se_falhar: "Feedback específico → uma revisão"
  max_revisoes: 1  # Não 3, apenas 1
```

### 3. Teste do Café (3 cenários)

```yaml
# Adicionar em revisar-licao-auto.yaml

teste_do_cafe:
  descricao: "Mãe exausta com café na mão consegue aplicar?"
  
  cenarios:
    - id: "5-minutos"
      pergunta: "Preparo ≤ 5 min?"
      responsavel: maes_personas
      
    - id: "material-caseiro"
      pergunta: "Usa materiais comuns de casa?"
      responsavel: susan_macaulay
      
    - id: "interrompivel"
      pergunta: "Pode pausar e retomar?"
      responsavel: charlotte_mason
```

---

## 📊 COMPARAÇÃO: ANTES vs DEPOIS

| Aspecto | Plano Anterior | Plano Simplificado |
|---------|----------------|-------------------|
| **Fases** | 5 fases | 3 ações simples |
| **Tempo** | 2+ horas | ~30 minutos |
| **Complexidade** | Alta | Baixa |
| **Valor agregado** | Marginal | Alto (foco no essencial) |
| **Risco de quebra** | Médio | Mínimo |

---

## ✅ CONCLUSÃO

### A Tríade já é forte. Não precisa de muito mais.

**O que importa:**
1. Ideia Viva definida ANTES de escrever
2. Um checkpoint para pegar problemas de tom
3. Teste do Café para garantir praticidade

**O que NÃO importa:**
- Formato padrão de experts (já funciona)
- Loops complexos (um checkpoint basta)
- Decisões versionadas (nice-to-have)

---

## ❓ PERGUNTAS FINAIS PARA O MAESTRO

1. **Aprovar versão simplificada?** (3 ações em 30 min)

2. **Quer que eu execute agora?** (expandir PeRD, adicionar checkpoint, formalizar Teste do Café)

3. **Alguma modificação?**

---

> *"Simplicidade é a sofisticação suprema."*  
> — Leonardo da Vinci

> *"A Tríade é a força. O resto é refinamento."*  
> — Consenso dos Experts

---

**Deliberação aprovada por 5/5 experts.**  
**Versão simplificada recomendada unanimemente.**
