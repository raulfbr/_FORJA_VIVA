# PROJETO FORJA VIVA 2.0 — Integração BMAD v6 Simplificada

**Documento:** Plano Mestre de Evolução  
**Data de Criação:** 13/01/2026  
**Última Atualização:** 13/01/2026 às 14:35  
**Status:** APROVADO — Pronto para Execução  
**Versão:** 2.1 (Revisado)

---

> [!IMPORTANT]
> Este é o documento DEFINITIVO que consolida:
> - Análise BMAD v6 vs Sistema Atual
> - Decisões do Maestro
> - Especificação YAML Lean v1.0
> - Planejamento detalhado de execução
> - Progresso de cada tarefa
>
> **Use este documento como referência única para todo o projeto de otimização.**

---

> [!NOTE]
> **Notas de Implementação:**
> - Sempre fazer backup antes de alterar qualquer arquivo
> - Alterar SEÇÃO POR SEÇÃO, nunca arquivo inteiro
> - Validar YAML após cada alteração (parse sem erro)
> - Submeter cada seção para aprovação do Maestro
> - Atualizar a tabela de progresso (PARTE 5) após cada tarefa concluída
> - Se parar no meio, anotar exatamente onde parou no histórico (5.3)

---

# SUMÁRIO

1. [Contexto e Objetivo](#parte-1-contexto-e-objetivo)
2. [Decisões Aprovadas](#parte-2-decisões-aprovadas)
3. [Especificação YAML Lean v1.0](#parte-3-especificação-yaml-lean-v10)
4. [Planejamento Detalhado](#parte-4-planejamento-detalhado)
5. [Progresso e Status](#parte-5-progresso-e-status)
6. [Validação e Testes](#parte-6-validação-e-testes)
7. [Referências](#parte-7-referências)

---

# PARTE 1: CONTEXTO E OBJETIVO

## 1.1 Por Que Este Projeto Existe

O projeto Forja Viva possui uma base sólida (90% alinhada com BMAD v6), mas os arquivos YAML consomem tokens desnecessários com:
- Emojis decorativos (📚, 🎯, ✅)
- Separadores visuais (════════════)
- Descrições verbose
- Comentários longos

## 1.2 Objetivo Final

| Meta | Descrição |
|------|-----------|
| **Economia de tokens** | Reduzir ~70% do consumo de contexto |
| **Preservar semântica** | Toda informação importante mantida |
| **Facilitar IA** | Formato otimizado para processamento |
| **Manter legibilidade** | Dicionário explícito para clareza |

## 1.3 O Que JÁ Temos (Inventário)

| Componente | Arquivo Principal | Linhas | Status |
|------------|-------------------|--------|--------|
| North Star | `LORE/north_star.yaml` | 748 | 🔄 A converter |
| Charlotte Mason | `experts/pedagogia/charlotte_mason.yaml` | 380 | 🔄 A converter |
| Orchestrator | `.bmad/orchestrator.yaml` | 200 | 🔄 A converter |
| Engenharia | `.bmad/experts/engenharia/engenharia.yaml` | 422 | 🔄 A converter |
| Demais experts | `.bmad/experts/**/*.yaml` | ~2000 | 🔄 A converter |
| Workflows | `.bmad/workflows/*.yaml` | 4 arquivos | ⏳ Fase 6 |
| Templates | `.bmad/templates/**` | 14 pastas | ⏳ Fase 7 |

---

# PARTE 2: DECISÕES APROVADAS

## 2.1 Decisões do Maestro (13/01/2026)

| # | Pergunta | Decisão |
|---|----------|---------|
| 1 | YAML Lean com dicionário? | ✅ SIM — Criar dicionário no header de north_star |
| 2 | Manter verbose em LEGADO? | ✅ SIM — Mas NUNCA referenciar (são arquivos mortos) |
| 3 | Keys estruturais vs descritivas? | ✅ Estruturais completas, descritivas abreviadas |
| 4 | Começar por north_star? | ✅ SIM — É a base de tudo |
| 5 | Execução em partes? | ✅ SIM — Seção por seção com aprovação |
| 6 | Checkpoint de revisão? | ✅ SIM — Adicionar no workflow |
| 7 | Teste do Café? | ✅ SIM — Incluir no planejamento |
| 8 | Expandir PeRD? | ✅ SIM — Mas só APÓS converter todos YAML |
| 9 | Quem decide formato interno? | ✅ Engenharia decide (otimizado para IA) |

## 2.2 Princípios de Implementação

| # | Princípio | Regra |
|---|-----------|-------|
| 1 | Não quebrar | Alterações seção por seção |
| 2 | North Star primeiro | Base de todas as mudanças |
| 3 | Sem refs a LEGADO | Arquivos mortos, sem links |
| 4 | Engenharia decide formato | Otimizado para IA |
| 5 | Dicionário explícito | No header do north_star |
| 6 | Validar sempre | Testar após cada seção |

## 2.3 O Que Implementar do BMAD v6

| Conceito | Nossa Versão | Quando |
|----------|--------------|--------|
| YAML Lean | Formato compacto com dicionário | AGORA |
| 1 Checkpoint de revisão | Após fase de desenvolvimento | Após YAMLs |
| Teste do Café (3 cenários) | No QA automático | Após YAMLs |
| PeRD (5 campos obrigatórios) | No perd-template.yaml | Após YAMLs |

## 2.4 O Que NÃO Implementar

| Conceito | Motivo |
|----------|--------|
| Agent-as-Code formal | Já temos YAML funcional |
| Codinomes (Sofia, Veritas) | Usamos nomes reais |
| PADR complexo | Nice-to-have futuro |
| Reasoning Loops (3 ciclos) | 1 checkpoint basta |
| Story Files atomizados | Template já é completo |

---

# PARTE 3: ESPECIFICAÇÃO YAML LEAN v1.0

## 3.1 Regras Gerais

| Regra | Aplicação |
|-------|-----------|
| Sem emojis | Remover todos (📚, 🎯, ✅, etc) |
| Sem separadores decorativos | Remover linhas de = ou - |
| Sem comentários longos | Máximo 1 linha se necessário |
| Keys estruturais completas | `id`, `type`, `name`, `ref` |
| Keys descritivas abreviadas | Ver dicionário abaixo |
| Inline quando possível | Listas curtas em uma linha |
| Sem redundância | Type composto: `expert.pedagogia` |

## 3.2 Dicionário de Abreviações (OFICIAL)

Este dicionário será incluído no header de `north_star.yaml` para referência:

```yaml
# DICIONÁRIO YAML LEAN v1.0
# Keys estruturais: completas | Keys descritivas: abreviadas
_dict:
  # Estruturais (NÃO abreviar)
  id: identificador único
  type: tipo do elemento
  name: nome completo
  ref: referência a outro arquivo
  
  # Descritivas (abreviar)
  desc: descricao
  apply: aplicacao
  q: pergunta
  a: resposta
  n: numero
  qty: quantidade
  alt: alternativa
  cond: condicao
  do: acao
  ex: exemplo
  src: fonte/source
  ctx: contexto
  req: requerido/requisito
  opt: opcional
  val: valor/validacao
  max: maximo
  min: minimo
  msg: mensagem
  err: erro
  ok: aprovado
  fail: reprovado
  warn: alerta
```

## 3.3 Exemplo de Conversão

### ANTES (verbose — 15 linhas):
```yaml
# ════════════════════════════════════════════════════════════════════════════════
# PROPÓSITO CENTRAL
# ════════════════════════════════════════════════════════════════════════════════

proposito:
  frase: |
    "Matemática Viva existe para ajudar famílias a amarem matemática juntas,
    através de ideias vivas e histórias que transformam."
  
  essencia: |
    Não somos um currículo. Somos um MOVIMENTO de famílias que descobriram
    que matemática pode ser viva, bela e conectada à realidade.
```

### DEPOIS (lean — 4 linhas):
```yaml
purpose:
  motto: Matemática Viva existe para ajudar famílias a amarem matemática juntas
  essence: MOVIMENTO de famílias que descobriram que matemática pode ser viva
```

**Economia:** ~400 bytes → ~150 bytes (62%)

## 3.4 Regras para Veto Rules e Princípios

Para elementos críticos como Veto Rules e 20 Princípios CM:

```yaml
# ANTES (verbose)
veto_rules:
  - id: VR-001
    trigger: pictorial_before_concrete
    condition: "Fase Pictórica proposta antes do Concreto para ciclo Sementes (0-6)"
    acao: REJECT
    motivo: "CM Princípio: Things before Signs. Em Sementes, só CONCRETO."
    recomendacao: "Remover fase Pictórica; expandir Concreto com mais manipulativos."

# DEPOIS (lean)
veto:
  - {id: VR001, if: pictorial_before_concrete, do: REJECT, msg: Sementes só Concreto}
```

---

# PARTE 4: PLANEJAMENTO DETALHADO

## 4.0 Legenda de Status

| Símbolo | Significado |
|---------|-------------|
| ⬜ | Não iniciado |
| 🔄 | Em progresso |
| ✅ | Concluído |
| ⏸️ | Pausado |
| ❌ | Bloqueado |

## 4.1 FASE 0: Preparação

| # | Tarefa | Status | Observações |
|---|--------|--------|-------------|
| 0.1 | Aprovar especificação YAML Lean v1.0 | ✅ | Aprovado 13/01 |
| 0.2 | Definir dicionário de abreviações | ✅ | Ver seção 3.2 |
| 0.3 | Criar backup de north_star.yaml | ⬜ | `_LEGADO/yaml_verbose/` |
| 0.4 | Ler estrutura atual de north_star | ⬜ | Identificar seções |

## 4.2 FASE 1: north_star.yaml (BASE)

### Estrutura do Arquivo (748 linhas):

| # | Seção | Linhas | Prioridade | Status |
|---|-------|--------|------------|--------|
| 1.1 | Header + Dicionário | 1-10 | 🔴 Alta | ⬜ |
| 1.2 | proposito | 11-19 | 🔴 Alta | ⬜ |
| 1.3 | missao (componentes) | 20-67 | 🔴 Alta | ⬜ |
| 1.4 | principios_fundamentais (8) | 68-211 | 🔴 Alta | ⬜ |
| 1.5 | metricas | 212-232 | 🟡 Média | ⬜ |
| 1.6 | validacao | 233-245 | 🟡 Média | ⬜ |
| 1.7 | triade | 246-278 | 🔴 Alta | ⬜ |
| 1.8 | diretrizes_operacionais | 279-310 | 🟡 Média | ⬜ |
| 1.9 | ciclos_por_ano (13 anos) | 311-748 | 🟡 Média | ⬜ |

### Detalhamento de Cada Subseção:

#### 1.1 Header + Dicionário
- Adicionar `_dict` no topo
- Remover separadores decorativos
- Atualizar versão e data
- **Validação:** YAML parseia corretamente

#### 1.2 proposito
- Converter para formato lean
- `frase` → `motto`
- `essencia` → `essence`
- **Validação:** Significado preservado

#### 1.3 missao
- Manter structure `one_liner`, `componentes`
- Abreviar descrições
- Inline listas curtas
- **Validação:** Refs funcionam

#### 1.4 principios_fundamentais (8 princípios)
- Converter cada princípio:
  ```yaml
  # ANTES
  - id: 1
    nome: "Qualidade Não é Negociável"
    descricao: |
      O difícil não é fazer...
    aplicacao: [...]
    pergunta: "..."
  
  # DEPOIS
  - id: 1
    name: Qualidade Não é Negociável
    desc: O difícil não é fazer. O difícil é distinguir o BOM do ÓTIMO.
    apply: [3 lições impecáveis > 10 boas, Experts deliberam, Qualidade percebida]
    q: Isso é BOM ou ÓTIMO?
  ```
- **Validação:** Todos 8 princípios preservados

#### 1.5-1.8 metricas, validacao, triade, diretrizes
- Formato inline
- Sem separadores
- **Validação:** Links para outros arquivos funcionam

#### 1.9 ciclos_por_ano
- Esta seção é grande (13 anos × ~30 linhas cada)
- Avaliar se pode ser compactado significativamente
- Manter estrutura por ano
- **Validação:** Propósitos por ano claros

## 4.3 FASE 2: orchestrator.yaml

| # | Seção | Status |
|---|-------|--------|
| 2.1 | Header + metadados | ⬜ |
| 2.2 | referencias_lore | ⬜ |
| 2.3 | referencias_templates | ⬜ |
| 2.4 | referencias_workflows | ⬜ |
| 2.5 | modos_operacao | ⬜ |
| 2.6 | hierarquia_veto | ⬜ |
| 2.7 | comandos | ⬜ |

## 4.4 FASE 3: charlotte_mason.yaml (CRÍTICO)

| # | Seção | Criticidade | Status |
|---|-------|-------------|--------|
| 3.1 | Header + bio | 🟢 Baixa | ⬜ |
| 3.2 | filosofia | 🟡 Média | ⬜ |
| 3.3 | vinte_principios (20) | 🔴 **CRÍTICO** | ⬜ |
| 3.4 | citacoes | 🟢 Baixa | ⬜ |
| 3.5 | veto_rules (6) | 🔴 **CRÍTICO** | ⬜ |
| 3.6 | audit_questions (6) | 🔴 **CRÍTICO** | ⬜ |
| 3.7 | hierarchy | 🟡 Média | ⬜ |
| 3.8 | output_format | 🟡 Média | ⬜ |
| 3.9 | alinhamento_north_star | 🟡 Média | ⬜ |
| 3.10 | referencias | 🟢 Baixa | ⬜ |

> [!WARNING]
> Seções 3.3, 3.5 e 3.6 são CRÍTICAS.
> Qualquer erro quebra o sistema de validação.
> Testar cada veto rule após conversão.

## 4.5 FASE 4: engenharia.yaml

| # | Seção | Status |
|---|-------|--------|
| 4.1 | Header + especialistas | ⬜ |
| 4.2 | BMAD framework | ⬜ |
| 4.3 | Eric Evans (DDD) | ⬜ |
| 4.4 | DevOps | ⬜ |
| 4.5 | QA | ⬜ |
| 4.6 | principios_engenharia | ⬜ |
| 4.7 | ferramentas | ⬜ |

## 4.6 FASE 5: Demais Experts (12 restantes)

| # | Expert | Conselho | Status |
|---|--------|----------|--------|
| 5.1 | susan_macaulay.yaml | pedagogia | ⬜ |
| 5.2 | jerome_bruner.yaml | matematica | ⬜ |
| 5.3 | lev_vygotsky.yaml | matematica | ⬜ |
| 5.4 | cs_lewis.yaml | narrativa | ⬜ |
| 5.5 | jrr_tolkien.yaml | narrativa | ⬜ |
| 5.6 | beatrix_potter.yaml | narrativa | ⬜ |
| 5.7 | makoto_fujimura.yaml | narrativa | ⬜ |
| 5.8 | seth_godin.yaml | negocios | ⬜ |
| 5.9 | alex_hormozi.yaml | negocios | ⬜ |
| 5.10 | peter_thiel.yaml | negocios | ⬜ |
| 5.11 | maes_personas.yaml | ux_familias | ⬜ |
| 5.12 | design.yaml | design | ⬜ |

## 4.7 FASE 6: Workflows (Após todos YAMLs)

| # | Tarefa | Status |
|---|--------|--------|
| 6.1 | Converter criar-licao-premium.yaml para lean | ⬜ |
| 6.2 | Adicionar checkpoint de revisão | ⬜ |
| 6.3 | Converter reuniao-deliberacao.yaml | ⬜ |
| 6.4 | Converter revisar-licao-auto.yaml | ⬜ |
| 6.5 | Adicionar Teste do Café (3 cenários) | ⬜ |
| 6.6 | Converter revisar-pontos.yaml | ⬜ |

## 4.8 FASE 7: Templates e PeRD (Por último)

| # | Tarefa | Status |
|---|--------|--------|
| 7.1 | Converter licao-base.yaml | ⬜ |
| 7.2 | Expandir perd-template.yaml (5 campos) | ⬜ |
| 7.3 | Converter definition-of-done.md | ⬜ |
| 7.4 | Atualizar templates por ano | ⬜ |

## 4.9 FASE 8: LORE (Opcional/Gradual)

| # | Arquivo | Linhas | Status |
|---|---------|--------|--------|
| 8.1 | index.yaml | ~50 | ⬜ |
| 8.2 | guardioes.yaml | ~200 | ⬜ |
| 8.3 | evolucao_guardioes.yaml | ~300 | ⬜ |
| 8.4 | locais.yaml | ~100 | ⬜ |
| 8.5 | climas.yaml | ~50 | ⬜ |
| 8.6 | artefatos.yaml | ~100 | ⬜ |
| 8.7 | viajante.yaml | ~50 | ⬜ |
| 8.8 | padroes_narrativos.yaml | ~200 | ⬜ |
| 8.9 | glossario.yaml | ~200 | ⬜ |

---

# PARTE 5: PROGRESSO E STATUS

## 5.1 Visão Geral

| Fase | Descrição | Tarefas | Concluídas | % |
|------|-----------|---------|------------|---|
| 0 | Preparação | 4 | 2 | 50% |
| 1 | north_star.yaml | 9 | 0 | 0% |
| 2 | orchestrator.yaml | 7 | 0 | 0% |
| 3 | charlotte_mason.yaml | 10 | 0 | 0% |
| 4 | engenharia.yaml | 7 | 0 | 0% |
| 5 | Demais experts | 12 | 0 | 0% |
| 6 | Workflows | 6 | 0 | 0% |
| 7 | Templates | 4 | 0 | 0% |
| 8 | LORE (opcional) | 9 | 0 | 0% |

**Total:** 68 tarefas | 2 concluídas | 3% completo

## 5.2 Próxima Tarefa

| Campo | Valor |
|-------|-------|
| **Fase** | 0 |
| **Tarefa** | 0.3 |
| **Descrição** | Criar backup de north_star.yaml |
| **Destino** | `_LEGADO/yaml_verbose/north_star_verbose.yaml` |
| **Status** | ⬜ Não iniciado |

## 5.3 Histórico de Alterações

| Data/Hora | Fase.Tarefa | Descrição | Status |
|-----------|-------------|-----------|--------|
| 13/01 14:27 | 0.1 | Aprovar YAML Lean spec | ✅ |
| 13/01 14:27 | 0.2 | Definir dicionário | ✅ |
| 13/01 14:35 | — | Revisão do documento | ✅ |

---

# PARTE 6: VALIDAÇÃO E TESTES

## 6.1 Checklist Após Cada Seção

- [ ] YAML válido (parse sem erro)
- [ ] Referências funcionam
- [ ] Semântica preservada
- [ ] Tokens reduzidos (verificar tamanho)
- [ ] Maestro aprovou seção

## 6.2 Testes de Regressão (Após cada arquivo)

- [ ] orchestrator.yaml consegue ler north_star?
- [ ] Workflows referenciam experts corretamente?
- [ ] Veto rules funcionam como esperado?
- [ ] LORE/index.yaml está atualizado?

## 6.3 Testes Críticos (Após charlotte_mason.yaml)

- [ ] VR001 (pictorial before concrete) funciona?
- [ ] VR002 (lesson > 20 min) funciona?
- [ ] VR003 (over explanation) funciona?
- [ ] VR004 (no narration) funciona?
- [ ] VR005 (child as object) funciona?
- [ ] VR006 (exclusionary language) funciona?

---

# PARTE 7: REFERÊNCIAS

## 7.1 Documentos Consolidados Neste Projeto

| Documento | Propósito | Status |
|-----------|-----------|--------|
| `2026-01-13_1339_AUDITORIA_ORCHESTRATOR.md` | Auditoria orchestrator | Consolidado |
| `2026-01-13_1348_ANALISE_BMAD_V6_PROFUNDA.md` | Análise BMAD v6 | Consolidado |
| `2026-01-13_1353_PLANO_INCREMENTAL_BMAD.md` | Deliberação Tríade vs BMAD | Consolidado |
| `2026-01-13_1406_YAML_LEAN_FORMAT.md` | Especificação YAML Lean | Consolidado |

## 7.2 Arquivos Alvo (Ordem de Execução)

| # | Arquivo | Prioridade |
|---|---------|------------|
| 1 | `LORE/north_star.yaml` | 🔴 Primeira |
| 2 | `.bmad/orchestrator.yaml` | 🔴 Alta |
| 3 | `.bmad/experts/pedagogia/charlotte_mason.yaml` | 🔴 Alta |
| 4 | `.bmad/experts/engenharia/engenharia.yaml` | 🟡 Média |
| 5-16 | Demais experts | 🟡 Média |
| 17-20 | Workflows | 🟢 Após YAMLs |
| 21+ | Templates | 🟢 Por último |

## 7.3 Arquivos em LEGADO (Não Referenciar)

> [!WARNING]
> Estes arquivos são "mortos". Existem apenas para histórico.
> NUNCA criar links ou referências para eles.

- `_LEGADO/yaml_verbose/` — Versões originais antes de lean
- `_LEGADO/docs_archived_*` — Documentos arquivados
- `_LEGADO/workflows_archived_*` — Workflows obsoletos

---

# PARTE 8: O QUE VEM APÓS YAMLS (ROADMAP)

## 8.1 Após Converter Todos YAMLs

| # | Tarefa | Descrição |
|---|--------|-----------|
| 1 | Checkpoint de Revisão | Adicionar em criar-licao-premium.yaml |
| 2 | Teste do Café | 3 cenários em revisar-licao-auto.yaml |
| 3 | PeRD Expandido | 5 campos obrigatórios |

## 8.2 Checkpoint de Revisão (Especificação)

```yaml
checkpoint_revisao:
  when: Após fase DESENVOLVIMENTO
  who: [charlotte_mason, cs_lewis]
  questions:
    - {id: C1, q: Ideia Viva está clara?}
    - {id: C2, q: Tom é nobre (não condescendente)?}
    - {id: C3, q: Tempo ≤ 20 min?}
  if_fail: Feedback específico + 1 revisão
  max_revisions: 1
```

## 8.3 Teste do Café (Especificação)

```yaml
teste_cafe:
  desc: Mãe exausta com café consegue aplicar?
  scenarios:
    - {id: TC1, q: Preparo ≤ 5 min?, who: maes_personas}
    - {id: TC2, q: Usa materiais de casa?, who: susan_macaulay}
    - {id: TC3, q: Pode pausar e retomar?, who: charlotte_mason}
```

## 8.4 PeRD Expandido (Especificação)

```yaml
perd_required:
  1_ideia_viva: str       # O Segredo em uma frase
  2_principio_cm: int     # Qual dos 20 Princípios (1-20)
  3_cpa:
    concreto: str         # O que a criança FAZ
    abstrato: str         # O símbolo introduzido
  4_guardiao: enum        # Melquior|Bernardo|Celeste|Noé|Íris
  5_tempo: int            # ≤ 20 min (obrigatório)

validation: Se qualquer campo vazio → BLOQUEAR criação
```

---

# PARTE 9: PERGUNTAS RESOLVIDAS

| # | Pergunta | Resposta |
|---|----------|----------|
| 1 | Dicionário de abreviações? | ✅ Criar no header de north_star |
| 2 | Verbose em LEGADO? | ✅ Sim, mas sem referências |
| 3 | Keys estruturais? | ✅ Completas (id, type, name, ref) |
| 4 | Começar por north_star? | ✅ Confirmado |
| 5 | Sessões ou contínuo? | ✅ Seção por seção com aprovação |
| 6 | Aprovar cada seção? | ✅ Sim, Maestro aprova |
| 7 | Checkpoint de revisão? | ✅ Implementar após YAMLs |
| 8 | Teste do Café? | ✅ Implementar após YAMLs |
| 9 | Expandir PeRD? | ✅ Implementar após YAMLs |

---

# PARTE 10: PRÓXIMOS PASSOS IMEDIATOS

1. **Criar backup** de `north_star.yaml` em `_LEGADO/yaml_verbose/`
2. **Ler estrutura** completa de north_star.yaml
3. **Converter seção 1.1** (Header + Dicionário)
4. **Submeter para aprovação** do Maestro
5. **Repetir** para seções 1.2-1.9
6. **Avançar** para orchestrator.yaml

---

> *"Um projeto bem planejado é um projeto meio executado."*  
> — Engenharia

> *"Cada seção convertida é um passo rumo à eficiência."*  
> — BMAD Method

> *"A Tríade permanece forte. O formato muda, a essência não."*  
> — Charlotte Mason

---

**Documento aprovado por:**
- ✅ Maestro (13/01/2026 14:27)
- ✅ Charlotte Mason (Pedagogia)
- ✅ Engenharia (BMAD + Eric Evans)
- ✅ C.S. Lewis (Narrativa)

**Pronto para iniciar execução.**
