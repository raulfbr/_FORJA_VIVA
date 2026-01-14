# DELIBERAÇÃO: revisar-licao-auto Restaurar 14 Experts?

**Data:** 2026-01-13 20:57  
**Questão:** Restaurar estrutura completa 14 experts (244L verbose) ou manter simplificado (34L lean)?  
**Participantes:** engenharia.yaml, charlotte_mason.yaml, orchestrator

---

## CONTEXTO

**Verbose revisar-licao-auto (244L):**
- 14 experts individuais com pergunta_north_star cada
- 4 níveis veto (ABSOLUTO, ALTA_PRIORIDADE, DOMINIO, CONSULTIVO)
- 4 fases workflow (CARREGAMENTO, INVOCAÇÃO PARALELO, CONSOLIDAÇÃO, DECISÃO)
- Output formato relatório detalhado
- 6 selos maes_personas

**Lean atual (34L):**
- 5 validações genéricas (V1-V5)
- Teste Café 3 cenários
- Economiza 86% linhas mas perde granularidade experts

---

## POSIÇÕES

### **Engenharia (SSOT/DRY/YAGNI)**

**Princípio aplicável:** YAGNI + DRY

**Análise:**
1. **DUPLICAÇÃO:** Verbose lista 14 experts com perguntas que JÁ existem em cada expert.yaml individual (SSOT violação)
2. **YAGNI:** Workflow não precisa RE-DECLARAR todos experts - orchestrator pode invocar dinamicamente lendo experts/*.yaml
3. **MAINTAINABILITY:** Se expert muda pergunta_north_star, teríamos que atualizar 2 lugares (expert + workflow)
4. **AI Eficiência YAML:** Lean força orquestrador ler experts via view_file (economiza 3-5s vs Python parse)

**Posição:** **MANTER LEAN SIMPLIFICADO**

**Justificativa:** Verbose viola SSOT (duplica perguntas experts). Lean força orchestrator invocar experts dinamicamente = melhor arquitetura. Informação NÃO está perdida, está nos experts individuais (SSOT correto).

---

### **Charlotte Mason (Pedagogia/Qualidade)**

**Princípio aplicável:** Qualidade Não Negociável

**Análise:**
1. **CLARITY:** Verbose explicita TODO fluxo validação - mais claro para humanos entenderem
2. **COMPLETENESS:** 4 níveis veto documentados (ABSOLUTO vs CONSULTIVO) - pedagogicamente importante
3. **USABILITY:** Mãe lendo workflow precisa VER quem valida o quê
4. **WORKFLOW CLARITY:** Fases 1-4 (CARREGAMENTO→INVOCAÇÃO→CONSOLIDAÇÃO→DECISÃO) são claras

**Posição:** **RESTAURAR ESTRUTURA INTERMEDIÁRIA**

**Justificativa:** Workflow precisa documentar FLUXO não RE-DECLARAR dados. Compromise: manter 4 fases + níveis veto + references a experts (não duplicar perguntas individuais).

---

## SÍNTESE (Orchestrator)

**Convergência:**
- Ambos concordam: não duplicar perguntas_north_star individuais (SSOT)
- Ambos concordam: workflow precisa ser CLARO

**Divergência:**
- Eng: Lean máximo (34L)
- CM: Estrutura intermediária com fases + veto levels

**Proposta:** **LEAN EXPANDIDO (~60L)**
- ✅ Manter 4 fases workflow verbose (CARREGAMENTO, INVOCAÇÃO, CONSOLIDAÇÃO, DECISÃO)
- ✅ Manter 4 níveis veto documentados (ABSOLUTO, ALTA, DOMINIO, CONSULTIVO)
- ✅ Manter output format relatório
- ❌ NÃO duplicar 14 experts individuais (reference dinâmico)
- ❌ NÃO duplicar perguntas_north_star (ler de experts/*.yaml)
- ✅ Adicionar nota: "Orchestrator invoca experts/*.yaml dinamicamente"

---

## DECISÃO FINAL (Charlotte Mason)

**Decisão:** **APROVAR LEAN EXPANDIDO**

**Justificativa:**
1. Engenharia correta: SSOT violação inaceitável
2. Mas workflow precisa DOCUMENTAR fluxo (não só validações)
3. Compromise preserva clareza SEM duplicação

**Ação:** Expandir revisar-licao-auto.yaml para ~60 linhas:
- 4 fases
- 4 níveis veto  
- Output format
- Reference dinâmico experts

**Alinhamento North Star:**
- ✅ Princípio #1 (Qualidade): Workflow claro executável
- ✅ SSOT/DRY: Sem duplicação experts

---

**Registrado:** 2026-01-13_2057_DELIBERACAO_REVISAR_LICAO_AUTO.md
