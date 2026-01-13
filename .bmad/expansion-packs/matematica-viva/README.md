# 📦 Expansion Pack: Matemática Viva

> *"Um sistema BMAD customizado para criar lições de matemática premium baseadas em Charlotte Mason."*

---

## 🎯 O que é este Pack?

Este é um **Expansion Pack BMAD v6** customizado para o projeto **Matemática Viva**.

Ele contém:
- Agentes especializados em pedagogia CM + CPA + TGTB
- Workflow para criar lições premium
- Templates para documentos pedagógicos
- Especificação da Tríade Pedagógica

---

## 📁 Estrutura

```
.bmad/
├── agents/                 # Agentes especializados
│   ├── sofia.md           # CM Coordinator (VETO power)
│   ├── euclides.md        # CPA Expert
│   ├── artesao.md         # Narrative Writer
│   └── veritas.md         # QA Quíntupla
├── workflows/              # Processos
│   └── criar-licao-premium.md
├── templates/              # Templates
│   ├── perd-template.yaml # Pedagogical Requirements
│   └── resumo-memoria.yaml # Memória entre lições
└── expansion-packs/
    └── matematica-viva/    # Este pack
        ├── README.md       # Este arquivo
        └── triade.yaml     # Especificação da Tríade
```

---

## 🧠 Agentes

| Agente | Função | Autoridade |
|--------|--------|------------|
| **Sofia** | CM Coordinator | ✅ VETO |
| **Euclides** | CPA Expert | Propositivo |
| **Artesão** | Narrative Writer | Executivo |
| **Veritas** | QA Auditor | Validação |

### Hierarquia

```
SOFIA (CM Coordinator)
    ↓
    ├── EUCLIDES (CPA) — Sugere, Sofia decide
    └── ARTESÃO (Writer) — Executa, Sofia valida
                ↓
            VERITAS (QA) — Valida tudo
```

---

## 🎯 Tríade Pedagógica

| Nível | Metodologia | Autoridade |
|-------|-------------|------------|
| 1 | Charlotte Mason | VETO_FINAL |
| 2 | Singapura (CPA) | Propositivo |
| 3 | TGTB | Referência |

### Regra de Ouro

> **CM > Singapura > TGTB**
>
> Em caso de conflito, a metodologia de nível superior decide.

---

## 🔄 Workflow: Criar Lição Premium

### Fases

1. **PLANEJAMENTO** — Sofia + Euclides definem estrutura
2. **DESENVOLVIMENTO** — Artesão escreve narrativa
3. **VERIFICAÇÃO** — Veritas executa QA Quíntupla
4. **OUTPUT** — YAML + HTML finais

### Comando de Uso

```
Execute o workflow criar-licao-premium:
- Tema: [seu tema]
- Ciclo: Sementes
- Lição: L001
- Guardião: [nome]
```

---

## 📐 Templates

### PeRD (Pedagogical Requirements Document)

Usado na Fase 1 para documentar:
- Ideia Viva (Sofia)
- Estrutura CPA (Euclides)
- Guardião Líder (Artesão)
- Checklist CM

### Resumo de Memória

Criado a cada 5 lições para:
- Conceitos introduzidos
- Decisões pedagógicas
- Arcos narrativos
- Referências futuras

---

## 🛡️ Verificação Quíntupla

| V# | Foco | Fail → |
|----|------|--------|
| V1 | CM (20 Princípios) | Sofia |
| V2 | CPA (ordem correta) | Euclides |
| V3 | Tempo (≤20 min) | Artesão |
| V4 | Guardiões (tom) | Artesão |
| V5 | Template V4 | Artesão |

---

## 🚀 Como Usar

1. **Definir tema** — O que a lição vai ensinar
2. **Invocar Sofia** — Ela define Ideia Viva e estrutura
3. **Invocar Euclides** — Ele propõe CPA (Sofia aprova)
4. **Invocar Artesão** — Ele escreve narrativa
5. **Invocar Veritas** — Ele valida com QA Quíntupla
6. **Gerar outputs** — YAML + HTML

---

## 📚 Recursos

- `LORE/*.yaml` — Dados do Reino Contado
- `forja-core/modelos/` — Templates de lições
- `GOVERNANCA/` — Documentos canônicos
- `memoria/` — Resumos de lições

---

## 🔗 Dependências

- BMAD Method v6
- Charlotte Mason (20 Princípios)
- Singapore Math (CPA)
- The Good and The Beautiful

---

> *"Cada lição é uma jornada no Reino Contado."*
> — Matemática Viva
