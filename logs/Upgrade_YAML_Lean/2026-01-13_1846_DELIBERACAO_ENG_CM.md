# 🏗️ DELIBERAÇÃO ENGENHARIA: Expansões Charlotte Mason

**Data:** 2026-01-13 18:46  
**Deliberadores:** BMAD, Eric Evans (DDD), Clean Code, QA  
**Questão:** Aplicar 4 expansões CM? Qual? Evitar duplicação (SSOT).

---

## 🎯 ANÁLISE POR ESPECIALISTA

### **BMAD Framework (Federated Knowledge)**
**Princípio:** "Conhecimento distribuído SSOT consultáveis. Não duplicar."

**Análise Expansões:**
- ✅ **#1 Tribal:** North Star TEM princípio #6, mas CM NÃO referencia → **GAP legítimo, adicionar**
- ❌ **#2 Orquestração:** `hierarchy_experts` duplicaria `engenharia.yaml.veto_coletivo` → **REJEITAR, já existe**
- ❌ **#3 Métricas CM:** North Star JÁ tem metricas globais → **REJEITAR, duplicação**
- ⚠️ **#4 Hierarchy:** Parcialmente em `engenharia.veto_coletivo` mas sem CM explícita → **REFERENCIAR, não duplicar**

**Voto BMAD:** Apenas #1 (Tribal). Demais violam Federated Knowledge.

---

### **Eric Evans (DDD - SSOT)**
**Princípio:** "Single Source of Truth — cada dado UM lugar apenas"

**Análise SSOT:**
```
North Star (LORE/) = SSOT para:
  ✓ Princípios fundamentais (8)
  ✓ Métricas projeto
  ✓ Tríade definição
  ✓ Hierarquia geral

Engenharia.yaml = SSOT para:
  ✓ Veto hierarchy
  ✓ Pipeline técnico
  ✓ QA métodos

Charlotte Mason = SSOT para:
  ✓ 20 Princípios CM
  ✓ Filosofia pedagógica
  ? Alinhamento North Star (referência local OK)
```

**Duplicações detectadas:**
- **#2 Orquestração:** `protocolo_orquestracao.hierarquia` duplicaria `engenharia.veto_coletivo.hierarquia` → **SSOT violado**
- **#3 Métricas:** `metricas_cm` duplicaria `north_star.metricas` + específicos QA → **SSOT violado**
- **#4 Hierarchy:** `hierarchy_experts` duplicaria tríade/veto → **SSOT violado**

**Soluções DDD:**
- #2, #3, #4 → **Referenciar SSOT existente, não criar novo**
- #1 → **Adicionar pois é gap legítimo** (NS tem #6, CM não referencia)

**Voto Evans:** #1 sim. #2-4 transformar em REFERÊNCIAS não duplicações.

---

### **Clean Code (DRY - Don't Repeat Yourself)**
**Princípio:** "Cada lógica um lugar. Funções reutilizáveis."

**Análise DRY:**
- **#1 Tribal:** Novo, não repete nada → ✅ **OK**
- **#2 Orquestração:** Repetiria lógica hierarchy → ❌ **DRY violado**
- **#3 Métricas:** Repetiria estrutura métricas → ❌ **DRY violado**
- **#4 Hierarchy:** Repetiria dados tríade → ❌ **DRY violado**

**Solução Clean:**
```yaml
# ERRADO (duplicação):
hierarchy_experts:
  pedagogia: [CM, Susan, Bruner]
  
# CERTO (referência):
hierarchy_ref: Ver north_star.yaml.triade + engenharia.yaml.veto_coletivo
```

**Voto Clean Code:** Apenas #1. Demais violam DRY.

---

### **QA (Qualidade Não Negociável)**
**Pergunta:** "Todos checks passam?"

**Quality Checks:**
1. **Completude:** CM alinha 7/8 North Star → 88% → ⚠️ **INCOMPLETO**
2. **SSOT:** #2-4 criam duplicação → ❌ **FALHA SSOT**
3. **Manutenibilidade:** +25 linhas vs +1 linha → ⚠️ **Mais código = mais manutenção**
4. **Valor:** #1 fecha gap crítico → ✅ **VALOR ALTO**

**Voto QA:** #1 passa em todos checks. #2-4 falham SSOT.

---

## 📊 VOTO COLETIVO ENGENHARIA

| Expansão | BMAD | Evans | Clean | QA | Voto |
|----------|------|-------|-------|-----|------|
| **#1 Tribal** | ✅ SIM | ✅ SIM | ✅ SIM | ✅ SIM | **APROVADO** |
| **#2 Orquestração** | ❌ NÃO | ❌ NÃO | ❌ NÃO | ❌ NÃO | **REJEITADO** |
| **#3 Métricas CM** | ❌ NÃO | ❌ NÃO | ❌ NÃO | ❌ NÃO | **REJEITADO** |
| **#4 Hierarchy** | ⚠️ REF | ⚠️ REF | ❌ NÃO | ⚠️ REF | **REFERÊNCIA** |

---

## ✅ DECISÃO FINAL ENGENHARIA

### **APROVAR:**
✅ **Expansão #1 (Tribal)** — Adicionar alinhamento North Star #6

**Implementação:**
```yaml
alinhamento_north_star:
  principios:
    # ... 7 existentes ...
    - {id: 6, name: Identidade Tribal, como: 'CM fundou PNEU (Parents National Educational Union) 1887 — primeira tribo homeschool história. Mães se apoiam, trocam narrativas, crescem juntas. Isolamento dificulta, comunidade fortalece. Princípio: This is for people like us (Godin)'}
```

**Linhas:** +1  
**Resultado:** CM 88% → 100% North Star alignment ✅

---

### **REJEITAR (SSOT violado):**
❌ **#2 Orquestração** — Duplica `engenharia.yaml.veto_coletivo`  
❌ **#3 Métricas** — Duplica `north_star.yaml.metricas` + QA checks  

**Alternativa:** Adicionar REFERÊNCIAS não duplicações:
```yaml
# Em cm.yaml (se necessário futuro):
protocolo_ref: Ver engenharia.yaml.veto_coletivo (hierarchy decisões)
metricas_ref: Ver north_star.yaml.metricas + QA.verificacao_quintupla
```

---

### **TRANSFORMAR (DRY):**
⚠️ **#4 Hierarchy** — Não criar nova, REFERENCIAR existente

**Implementação minimalista:**
```yaml
# Expandir triade_relacao atual:
triade_relacao:
  papel_cm: Coordenadora pedagógica veto final (pri: 1)
  especialistas:
    - {nome: Jerome Bruner, dominio: CPA Singapura, relacao: CM direciona quando aplicar C→P→A}
    - {nome: TGTB Reference, dominio: Scope & Sequence, relacao: CM valida ritmo princípios}
    - {nome: Susan Macaulay, dominio: Aplicação prática CM, relacao: CM fundamento Macaulay implementação}
  hierarchy_ref: Ver engenharia.yaml.veto_coletivo para hierarchy completa experts
```

**Linhas:** +2 (expande existente, não cria novo)

---

## 📋 IMPLEMENTAÇÃO FINAL APROVADA

### **MUDANÇAS:**
1. ✅ Adicionar Tribal (#6) → +1 linha
2. ✅ Expandir `triade_relacao` (add Susan + ref) → +2 linhas

**Total:** +3 linhas (125 → 128)

### **RESULTADO:**
- **North Star alignment:** 88% → 100% ✅
- **SSOT:** Mantido ✅
- **DRY:** Respeitado ✅
- **Qualidade:** Máxima ✅

---

## 🏆 VEREDITO ENGENHARIA

**Charlotte Mason v1.2:**
- ✅ Tribal adicionado (100% North Star)
- ✅ Susan Macaulay reconhecida
- ✅ Hierarchy por referência (não duplicação)
- ✅ SSOT preservado
- ✅ +3 linhas (eficiente)

**Status:** ✅ **APROVADO IMPLEMENTAR**

---

**Próximo passo:** Aplicar mudanças aprovadas ao charlotte_mason.yaml
