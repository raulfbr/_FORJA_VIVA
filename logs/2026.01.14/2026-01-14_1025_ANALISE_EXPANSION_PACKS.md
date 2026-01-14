# 🏗️ ANÁLISE ARQUITETURAL — Expansion Packs vs Orchestrator

**Data:** 14/01/2026 10:25  
**Modo:** ENGENHARIA (Eric Evans + BMAD)

---

## 📂 O QUE É `expansion-packs/`?

### Conceito BMAD
No BMAD Framework, **Expansion Packs** são módulos de conhecimento **específicos de domínio** que estendem o Orchestrator base. São como "plugins" que adicionam regras específicas para um projeto.

### Estrutura Atual
```
.bmad/
├── orchestrator.yaml          ← Orquestração GENÉRICA (modos, comandos)
├── expansion-packs/
│   └── matematica-viva/
│       └── triade.yaml        ← Regras ESPECÍFICAS do MatViva
```

---

## 🔍 ANÁLISE DE DUPLICAÇÃO

| Conceito | orchestrator.yaml | triade.yaml | regras.yaml | DUPLICADO? |
|----------|-------------------|-------------|-------------|------------|
| Hierarquia CM > CPA > TGTB | ✅ hierarquia_veto | ✅ hierarquia.niveis | ✅ triade | ⚠️ **SIM** |
| Vetos canonizados | ❌ | ✅ vetos.VR-001 a VR-004 | ✅ cpa.pictorico | ⚠️ **SIM** |
| Ciclos (Sementes, Raízes) | ❌ | ✅ ciclos | ✅ ciclo: Sementes | ⚠️ **SIM** |
| Princípios CM | ❌ | ✅ principios_cm | ✅ nota_cm | ⚠️ **PARCIAL** |
| Regras conflito | ❌ | ✅ conflitos | ❌ | ✅ OK (único) |
| Mapeamento CPA por ciclo | ❌ | ✅ | ✅ | ⚠️ **SIM** |

**Problema Eric Evans:** Mesma informação em 3 lugares = SSOT violado.

---

## 🎯 OPÇÕES DE SOLUÇÃO

### Opção A: Eliminar Expansion Packs (Incorporar ao Orchestrator)
```yaml
# orchestrator.yaml expande para incluir a tríade
orchestrator.yaml:
  triade:
    hierarquia: [CM (veto), CPA (propositivo), TGTB (ref)]
    vetos: [VR-001, VR-002, VR-003, VR-004]
    ciclos: {...}
```
**Prós:** Um só arquivo de referência  
**Contras:** Orchestrator fica grande demais, perde modularidade

### Opção B: Manter Expansion Packs como SSOT da Tríade
```yaml
# orchestrator.yaml referencia expansion-pack
orchestrator.yaml:
  triade: {extends: .bmad/expansion-packs/matematica-viva/triade.yaml}

# regras.yaml referencia expansion-pack
regras.yaml:
  triade: {extends: .bmad/expansion-packs/matematica-viva/triade.yaml}
```
**Prós:** SSOT preservado, modular  
**Contras:** Mais arquivos para navegar

### Opção C: HÍBRIDA (Recomendada)
1. **triade.yaml** → SSOT único para regras da tríade
2. **orchestrator.yaml** → Só referencia triade.yaml
3. **regras.yaml** → Só referencia triade.yaml
4. **licao-template.yaml** → Não precisa repetir (herda das regras)

```yaml
# orchestrator.yaml (LEAN)
triade:
  extends: .bmad/expansion-packs/matematica-viva/triade.yaml
  nota: "Fonte única para hierarquia CM/CPA/TGTB"

# regras.yaml (LEAN)
triade:
  ref: .bmad/expansion-packs/matematica-viva/triade.yaml
```

---

## 📋 WORKFLOW criar-licao-premium — ANÁLISE

### Issues Identificadas

| Linha | Issue | Severidade |
|-------|-------|------------|
| 10-11 | `Concreto ≥ 60%` → Deveria ser **80%+** (Opção D) | ⚠️ DESATUALIZADO |
| 12-13 | Fase experts OK | ✅ |
| 14-15 | QA checks OK | ✅ |
| - | Falta referência a `triade.yaml` | ⚠️ SSOT |

### Correções Necessárias
1. Atualizar `Concreto ≥ 60%` → `Concreto ≥ 80%` (Opção D)
2. Adicionar `triade_ref: .bmad/expansion-packs/matematica-viva/triade.yaml`

---

## ✅ RECOMENDAÇÃO DO CONSELHO ENGENHARIA

**Opção C (Híbrida):**

1. ✅ **Manter `expansion-packs/`** — É padrão BMAD para modularidade
2. ✅ **triade.yaml como SSOT** — Única fonte para hierarquia/vetos/ciclos
3. ✅ **Atualizar referências** — orchestrator e regras apontam para triade.yaml
4. ✅ **Atualizar workflow** — 60% → 80%+ (Opção D)
5. ✅ **Refatorar triade.yaml para YAML Lean** — Mesmo padrão dos outros

---

## 📝 AÇÕES PROPOSTAS

1. [ ] Refatorar `triade.yaml` para YAML Lean
2. [ ] Atualizar `orchestrator.yaml` para referenciar triade.yaml
3. [ ] Atualizar `regras.yaml` para referenciar triade.yaml  
4. [ ] Atualizar `criar-licao-premium.yaml` para 80%+ Concreto
5. [ ] Remover duplicações

**Aguardando aprovação do Maestro.**
