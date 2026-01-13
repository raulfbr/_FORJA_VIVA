# 📜 ARQUITETURA CANÔNICA — Matemática Viva

---
**Data de Criação:** 12/01/2026 às 13:16  
**Última Atualização:** 12/01/2026 às 13:57  
**Status:** Em construção
**Versão:** 4.0 (Forja Viva)

---

> [!IMPORTANT]
> Este documento é a **Fonte Única da Verdade** para todas as decisões arquiteturais do projeto.
> Toda decisão deve ser registrada aqui. Se não está aqui, não é canônico.

---

## 🎯 1. NORTH STAR (Consolidado)

```
Infraestrutura Educacional K-12 — Aberta no Saber, Premium na Experiência.
```

| Componente | Definição |
|------------|-----------|
| **Escopo** | 1200+ ativos (121 lições × ~10 anos) |
| **Kernel Pedagógico** | Charlotte Mason + Singapura CPA + TGTB Structure |
| **Licença** | CC BY 4.0 (conteúdo aberto) |
| **Valor Comercial** | Curadoria + Comunidade + Conveniência |
| **Experiência Target** | 5 min preparo, 15-20 min lição |

---

## 🎭 2. BERNARDO E A INCLUSÃO

### 2.1 A História Oficial (Canonizada 12/01/2026)

> **A Grande Nevasca**
>
> Há muito tempo, veio a Grande Nevasca. Bernardo, jovem e imprudente, correu para salvar os filhotes de raposa perdidos na tempestade. Encontrou-os tremendo sob uma pedra enorme que ameaçava desabar.
>
> Sem pensar, Bernardo segurou a pedra com todas as suas forças enquanto os filhotes fugiam. A pedra era pesada demais. O gelo queimava. Sua perna esquerda cedeu sob o peso.
>
> Quando a tempestade passou, Bernardo estava vivo — mas nunca mais andaria como antes. Os filhotes que ele salvou? Um deles era a avó de Celeste.
>
> Desde então, Íris escolheu ficar no ombro de Bernardo. Ela é seus olhos para os detalhes que ele não alcança, e ele é sua fortaleza quando o vento é forte demais.

### 2.2 Lições Embutidas
| Conceito | Mensagem |
|----------|----------|
| **Amor Sacrificial** | Bernardo não é coitado; é herói ferido |
| **Interdependência** | Íris ajuda por gratidão, não por pena |
| **Força na Vulnerabilidade** | Juntos são mais fortes que separados |
| **Inclusão Natural** | Deficiência como parte do grupo, não peso |

### 2.3 ✅ DECISÕES CANONIZADAS (12/01/2026)

| # | Pergunta | Decisão |
|---|----------|---------|
| 1 | História de Bernardo | ✅ **Nevasca + Salvamento + Íris no ombro** |
| 2 | Adaptações para deficiência | ✅ **Documento separado**, não por lição |
| 3 | Comunicação | ✅ **Através da narrativa**, não de explicações |
| 4 | Atividades extras | ✅ **1 atividade "core" + opções alternativas** para flexibilidade |

---

## 📐 3. TEMPLATE V4 — ESTRUTURA DA LIÇÃO

### 3.1 Análise das Versões Anteriores

| Versão | Pontos Fortes | Pontos Fracos |
|--------|---------------|---------------|
| **V1** | Ideia embrionária | Não estruturado |
| **V2** | Cards interativos, ritual da vela, "Por que importa" | Muito digital-dependente |
| **V3** | Bancada/Mise-en-place, Ideia Viva explícita, Auditoria CM | Muito texto para impressão |

### 3.2 Elementos do V4 (Proposta)

```
┌─────────────────────────────────────────────────────────┐
│  LIÇÃO XXX — [Título]                                   │
├─────────────────────────────────────────────────────────┤
│  📋 PARA O PORTADOR (Leia antes)                        │
│  ├── 💚 Dica para o Pai/Mãe (Alma, não performance)     │
│  ├── 🎯 Ideia Viva (O Segredo)                          │
│  ├── 📦 Bancada (Mise-en-place)                         │
│  └── ⏱️ Tempo: 15-20 min                                │
├─────────────────────────────────────────────────────────┤
│  🌿 RITUAL DE ABERTURA                                  │
│  └── [Script para o Portador + Card do Guardião]        │
├─────────────────────────────────────────────────────────┤
│  🧱 FASE CPA                                            │
│  ├── C: Concreto (Mãos)                                 │
│  ├── P: Pictórico (Olhos)                               │
│  └── A: Abstrato (Símbolo)                              │
├─────────────────────────────────────────────────────────┤
│  💬 NARRAÇÃO (A criança conta)                          │
├─────────────────────────────────────────────────────────┤
│  🌅 RITUAL DE FECHAMENTO                                │
├─────────────────────────────────────────────────────────┤
│  📖 POR QUE ISSO IMPORTA (Cátedra dos Pais)             │
│  └── Explica o conceito pedagógico para o adulto        │
└─────────────────────────────────────────────────────────┘
```

### 3.3 ✅ DECISÕES SOBRE TEMPLATE (Canonizadas 12/01/2026)

| # | Pergunta | Decisão |
|---|----------|--------|
| 5 | Template deve ter seção de "Adaptações"? | ✅ **NÃO por lição** — Documento separado de adaptações |
| 6 | A fase CPA deve ser explícita ou integrada? | ✅ **INTEGRADA** na narrativa com marcadores sutis |
| 7 | "Por que isso importa" no início ou final? | ✅ **NO FINAL** — Pai digere após aplicar |
| 8 | Cards dos Guardiões aparecem inline ou sidebar? | ✅ **INLINE** — `[CARD: NOME]` visível no fluxo |

---

## 🖨️ 4. PIPELINE DE PRODUÇÃO (HTML + Imprimível)

### 4.1 Situação Atual
```
Markdown (.md) → Python/Jinja2 → HTML
                              → PDF? (Não funciona bem)
```

### 4.2 Proposta para V4

**Opção A: Markdown Dual-Output**
```
Markdown (.md) → Gutenberg Pipeline → HTML (Digital)
                                    → HTML (Print-Optimized CSS)
```

**Opção B: HTML First**
```
HTML (Template V4) → Renderizado Web
                   → CSS @media print → Imprimível
```

**Opção C: Separação Total**
```
Fonte Única (YAML/MD) → HTML Engine → Web
                      → PDF Engine  → Print
```

### 4.3 ✅ DECISÕES SOBRE PIPELINE (Canonizadas 12/01/2026)

| # | Pergunta | Decisão |
|---|----------|---------|
| 9 | Portador prefere celular ou imprimir? | ✅ **AMBOS** — Flexibilidade para famílias |
| 10 | Cards impressos junto ou separados? | ✅ **SEPARADOS** — PDF de cards único |
| 11 | Material Eco ou Premium? | ✅ **ECO** para lições, **PREMIUM** para cards |
| 12 | Formato de fonte? | ✅ **YAML** com narrativa inline — Melhor para IA e validação |
| — | Pipeline escolhido? | ✅ **OPÇÃO C (Separação Total)** — YAML → Web Engine + Print Engine |

---

## 🎴 5. CARDS DOS GUARDIÕES

### 5.1 Conceito
> Cards físicos que a criança segura enquanto o Portador lê o script.
> **Pedagogicamente essenciais** — ancoram a atenção da criança.

### 5.2 Uso por Momento

| Momento | Card Mostrado | Indicador no Template |
|---------|---------------|----------------------|
| Ritual de Abertura | Guardião Líder | `[CARD: GUARDIÃO]` |
| Fase Concreta | Objeto/Local | `[CARD: OBJETO]` |
| Fechamento | Selo/Insígnia | `[CARD: SELO]` |

### 5.3 ✅ DECISÕES CANONIZADAS (12/01/2026)

| # | Pergunta | Decisão |
|---|----------|---------|
| 13 | Quantos cards? | ✅ **Expansível** — 5 Guardiões + 5 Locais + mais conforme necessário |
| 14 | Vendidos separadamente? | ✅ **INCLUÍDOS** — Tudo no pacote Premium |
| 15 | Essenciais ou opcionais? | ✅ **ESSENCIAIS** — Pedagogicamente importantes |
| 16 | Cards de Locais? | ✅ **SIM** — Já existem 5 locais |
| 8 | Indicador visual | ✅ **`[CARD: NOME]`** visível em HTML e Print |

---

## 🦉 6. OS GUARDIÕES — REGRAS NARRATIVAS

### 6.1 Distribuição nas Lições

| Lição | Guardião | Motivo |
|-------|----------|--------|
| L000 | **Melquior** | Introduz todos |
| L001 | **Celeste** | Primeira imersão: exploração |
| L002 | **Bernardo** | Segunda imersão: construção |
| L003 | **Íris** | Terceira imersão: atenção |
| L004 | **Noé** | Quarta imersão: tempo |
| L005+ | **Varia** | Por tema da lição — sem regra fixa |

### 6.2 ✅ Frases de Assinatura (Canonizadas 12/01/2026)

| Guardião | Frase Oficial | Tom |
|----------|---------------|-----|
| **Melquior** | "O Rei sorriu ao ver você chegar." | Acolhedor, sábio |
| **Noé** | "Respire. O número espera por você." | Calmo, paciente |
| **Celeste** | "Sente esse cheiro? É aventura." | Curioso, rápido |
| **Bernardo** | "Mais uma vez. Comigo." | Firme, encorajador |
| **Íris** | "Olhe bem. A beleza está no detalhe." | Suave, atento |

### 6.3 ✅ DECISÕES CANONIZADAS (12/01/2026)

| # | Pergunta | Decisão |
|---|----------|---------|
| 17 | Frases de assinatura? | ✅ **SIM** — 5 frases oficiais acima |
| 18 | Evolução visual? | ✅ **SIM** — Conforme fase (Matriz K12) |
| 19 | Guardião ausente/mistério? | ✅ **NÃO** — Não é necessário |
| 20 | Evitar monotonia? | ✅ **Evolução visual + Interação + Clima variado** |

### 6.4 Interação entre Guardiões
| Tipo | Permitido |
|------|-----------|
| Conversa entre Guardiões | ✅ SIM |
| Novos Guardiões | ❌ NÃO — Apenas os 5 |
| Personagens Secundários | ✅ SIM — Podem aparecer |
| Arcos Longos (mistérios) | ✅ SIM — Podem durar fases |

---

## 📅 7. ROADMAP DE PRODUÇÃO

### 7.1 Ordem de Produção

| Prioridade | Fase | Lições | Organização |
|------------|------|--------|-------------|
| 1º | Sementes (K) | L001-L040 | Trimestral |
| 2º | Raízes 1 (1º ano) | L001-L040 | Trimestral |
| 3º | Raízes 2 (2º ano) | L001-L030 | Bimestral |
| 4º+ | Continua... | ... | Bimestral |

### 7.2 Entregáveis por Trimestre

| Período | Entregável |
|---------|------------|
| **Jan-Mar 2026** | Template V4 Gold + L001-L040 Sementes |
| **Abr-Jun 2026** | L001-L040 Raízes 1 |
| **Jul-Dez 2026** | Refinamentos + Expansão |

---

## 📝 8. DECISÕES JÁ CANONIZADAS

| # | Decisão | Data | Fonte |
|---|---------|------|-------|
| 1 | Foco inicial: Sementes | 12/01/2026 | Log PM |
| 2 | Preço: R$1.197 Pioneiros / R$2.397 Cheio | 12/01/2026 | Log Negócio |
| 3 | Por FAMÍLIA, não por criança | 12/01/2026 | Log Negócio |
| 4 | CC BY 4.0 para conteúdo | Anterior | PAINEL |
| 5 | Tríade: CM + CPA + TGTB | Anterior | MAGNA_CARTA |
| 6 | Versão de venda: V4 | 12/01/2026 | Maestro |
| 7 | HTML + Imprimível obrigatório | 12/01/2026 | Log PM |
| 8 | Cards são diferencial | 12/01/2026 | Log PM |
| 9 | Flexibilidade para famílias | 12/01/2026 | Log PM |
| 10 | Não criticar outros métodos | 12/01/2026 | Maestro |

---

## 📚 9. BLOG E MATERIAIS EXTRAS (Futuro)

> **Nota:** Anotar aqui para não esquecer, mas não é prioridade agora.

| Item | Descrição | Prioridade |
|------|-----------|------------|
| Blog CM | Artigos aprofundando a Tríade | Baixa |
| Deep Dives | Material opcional para pais estudiosos | Baixa |
| CTAs | Cada artigo leva ao curso | Baixa |

---

## 📊 10. RESUMO DE DECISÕES (12/01/2026)

| Categoria | Total | Status |
|-----------|-------|--------|
| Bernardo/Inclusão | 4 | ✅ Canonizadas |
| Template V4 | 4 | ✅ Canonizadas |
| Pipeline | 5 | ✅ Canonizadas |
| Cards | 5 | ✅ Canonizadas |
| Guardiões | 4 | ✅ Canonizadas |
| Negócio | 10 | ✅ Canonizadas |
| **TOTAL** | **32** | ✅ **TODAS RESPONDIDAS** |

---

> *"Este documento está emc onstrução"
> 
> *Última auditoria: 12/01/2026 às 13:57*
