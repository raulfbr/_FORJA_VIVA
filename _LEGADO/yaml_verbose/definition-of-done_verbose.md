# ✅ DEFINITION OF DONE — Lição Sementes V4

---
**Última Atualização:** 13/01/2026  
**Status:** Canônico  
**Referência LORE:** `LORE/north_star.yaml`  
**Template:** V4 (Forja Viva)  

---

> [!IMPORTANT]
> Uma lição só está PRONTA quando todos os itens obrigatórios estão ✅.

---

## 📖 0. OS 20 PRINCÍPIOS DE CHARLOTTE MASON (Auditoria Base)

| # | Princípio | Aplicação na Lição |
|:--|:----------|:-------------------|
| 1 | *"Children are born persons."* | Tratar criança como pessoa completa |
| 2 | *"Not born good or bad..."* | Educação forma, não só informa |
| 3 | *"Authority and obedience..."* | Pais têm autoridade legítima |
| 4 | *"Authority is not license."* | Autoridade respeita a pessoa |
| 5 | *"Atmosphere, discipline, life."* | Os 3 instrumentos em cada lição |
| 6 | *"Atmosphere is natural..."* | Não criar atmosfera artificial |
| 7 | *"Discipline of habits..."* | Formar hábitos mentais/morais |
| 8 | *"Life = living ideas..."* | **IDEIA VIVA obrigatória** |
| 9 | *"Mind feeds on ideas..."* | Mente digere ideias |
| 10 | *"Generous curriculum."* | Currículo amplo e rico |
| 11 | *"Knowledge through curriculum."* | Currículo é veículo |
| 12 | *"Science of relations."* | Conectar matemática com vida |
| 13 | *"Short lessons."* | **≤20 min (Sementes: 15-20)** |
| 14 | *"Narration..."* | **Criança reconta** |
| 15 | *"Single careful reading..."* | Uma leitura atenta > repetições |
| 16 | *"No rewards, no prizes..."* | Valorizar conhecimento, não prêmios |
| 17 | *"No rivalry."* | Cooperação > Competição |
| 18 | *"Narration, not testing."* | Avaliar através de narração |
| 19 | *"Give time..."* | Respeitar ritmo individual |
| 20 | *"Child does the work."* | **Criança trabalha, pai facilita** |

### As 5 Perguntas de Auditoria CM

| # | Pergunta | Fonte |
|---|----------|-------|
| 1 | A criança é respeitada como pessoa capaz? | Princípio 1 |
| 2 | O Hábito da Atenção é preservado (lição curta)? | Princípio 13 |
| 3 | Things before Signs: CPA usado (Concreto primeiro)? | Singapore/Bruner |
| 4 | Há espaço para Narração ao final? | Princípio 14 |
| 5 | A Ideia Viva é "apresentada" (não "explicada")? | Princípio 8 |

---

## 📋 1. METADADOS YAML (Obrigatórios)

```yaml
# Exemplo de cabeçalho obrigatório
id: MV-S-XXX
titulo: "[Título Poético]"
fase: Sementes
guardiao: "[Nome do Guardião Líder]"
ideia_viva: "[Frase curta - O Segredo]"
clima: "[Ensolarado | Nublado | Ventoso | ...]"
tempo: 15-20
materiais:
  - item: "[Material 1]"
    quantidade: X
    alternativa: "[Se não tiver...]"
tgtb_ref: "000-LXX"
elo_anterior: "[Gancho da lição anterior]"
proximo_passo: "[Gancho para próxima]"
status: rascunho | em_revisao | canonico
```

---

## 📜 2. ESTRUTURA DAS SEÇÕES (V4)

| # | Seção | Obrigatório | Descrição |
|---|-------|-------------|-----------|
| 1 | **📋 Para o Portador** | ✅ | Dica para pai/mãe + Ideia Viva |
| 2 | **📦 Bancada** | ✅ | Mise-en-place com materiais |
| 3 | **🎧 Áudio-Script** | ⭐ | Texto para ler antes |
| 4 | **🌿 Ritual de Abertura** | ✅ | Acender vela + [CARD: GUARDIÃO] |
| 5 | **🗺️ A Jornada** | ✅ | Narrativa imersiva sensorial |
| 6 | **💡 A Ideia Viva** | ✅ | Conceito revelado |
| 7 | **🧱 CPA Integrado** | ✅ | Concreto → Pictórico → Abstrato |
| 8 | **🦋 Se Quiser Voar** | ⭐ | Extensão opcional (marcada) |
| 9 | **💬 Narração** | ✅ | Criança conta o que aprendeu |
| 10 | **🌅 Ritual de Fechamento** | ✅ | Despedida + apagar vela |
| 11 | **📖 Por que Importa** | ✅ | Cátedra dos Pais (CM + CPA) |
| 12 | **🛡️ Auditoria CM** | ✅ | Checklist de conformidade |
| 13 | **🎓 Sugestões** | ⭐ | Dicas dos especialistas |

**Legenda:** ✅ = Obrigatório | ⭐ = Altamente Recomendado

---

## 🌤️ 3. CLIMAS NARRATIVOS

| Clima | Emoji | Quando Usar | Exemplo de Descrição |
|-------|-------|-------------|----------------------|
| **Ensolarado** | ☀️ | Lições de introdução | "A luz dourada banha o jardim..." |
| **Nublado** | ☁️ | Consolidação, revisão | "Uma névoa suave envolve a clareira..." |
| **Ventoso** | 🌬️ | Muita atividade física | "As folhas dançam ao redor de vocês..." |
| **Chuvoso** | 🌧️ | Contemplativas | "O som da chuva embala o Reino..." |
| **Outonal** | 🍂 | Fechamento de unidades | "As folhas caem suavemente..." |
| **Primaveril** | 🌸 | Novas fases | "Flores desabrocham por toda parte..." |
| **Crepúsculo** | 🌅 | Celebração/revisão | "O sol se despede pintando o céu..." |
| **Estrelado** | ⭐ | Números grandes, infinitude | "As estrelas brilham como promessas..." |

---

## 🔍 4. CHECKLIST DE QA (Verificação)

### ✅ OBRIGATÓRIOS (Se faltar 1 = Reprovado)
- [ ] ID e Título presentes
- [ ] Guardião nomeado
- [ ] Ideia Viva declarada
- [ ] Clima definido e coerente
- [ ] Elo anterior e próximo passo
- [ ] CPA completo (Concreto → Pictórico → Abstrato)
- [ ] Narração incluída
- [ ] [CARD: NOME] indicado pelo menos 1x
- [ ] "Por que Importa" no final
- [ ] Auditoria CM preenchida

### ⭐ RECOMENDADOS (Se faltar 2+ = Revisar)
- [ ] Descrição sensorial rica (5 sentidos)
- [ ] Pausas de maravilha indicadas
- [ ] Falas com indicação de tom
- [ ] Atividade de extensão opcional

### 🚀 PREMIUM (Diferencia bom de excepcional)
- [ ] Lido em voz alta sem tropeços
- [ ] Tempo ≤ 20 min
- [ ] Validado com criança real

---

## 📊 5. MÉTRICAS DE QUALIDADE

| Critério | Peso | Mínimo |
|----------|------|--------|
| Metadados Completos | 10% | 100% |
| Seções Obrigatórias | 25% | 100% |
| Imersão Sensorial | 20% | 85% |
| Ortografia | 10% | 100% |
| Fluxo Narrativo | 15% | 85% |
| Validação Humana | 20% | 100% |

**Score mínimo para Selo:** 90%

---

## 🔄 6. PROCESSO DE VALIDAÇÃO

```
1. GERAÇÃO
   └─> Criar lição em YAML/MD

2. SELF-REVIEW
   └─> Checklist de QA (seção 4)

3. RENDER
   └─> Pipeline gera HTML + Print

4. LEITURA EM VOZ ALTA
   └─> Maestro ou Matriarca lê

5. TESTE COM CRIANÇA (Opcional)
   └─> Aplicar com Raulzito

6. SELO
   └─> Status = "canonico"
   └─> Tracker atualizado
```

---

## 🏷️ 7. INDICADORES DE CARD

Usar dentro da narrativa para indicar ao Portador quando mostrar card:

```markdown
[CARD: MELQUIOR]   → Hora de mostrar card do Leão
[CARD: CELESTE]    → Hora de mostrar card da Raposa
[CARD: OBJETO]     → Hora de mostrar card de objeto/número
[CARD: LOCAL]      → Hora de mostrar card do local
```

> Estes indicadores são renderizados visualmente no HTML e Print.

---

> *"Uma lição não está pronta até que uma família possa usá-la com confiança."*
