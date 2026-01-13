# 📚 LORE — Fonte Única de Verdade do Reino Contado

> **LORE = Dados Canônicos Globais do Matemática Viva**
> 
> *"O segredo não é quantidade de elementos, mas simplicidade de estrutura."* — Eric Evans

---

## 🏛️ Arquitetura em 3 Camadas

```
┌─────────────────────────────────────────────────────────────────┐
│                      CAMADA 1: ÍNDICE                           │
│                      ─────────────────                          │
│                        index.yaml                               │
│                (Ponto de entrada ÚNICO)                         │
├─────────────────────────────────────────────────────────────────┤
│                      CAMADA 2: CORE                             │
│                      ─────────────                              │
│   north_star.yaml  │  guardioes.yaml  │  locais.yaml           │
│   (Princípios)     │  (5 personagens) │  (5 lugares)           │
│                                                                 │
│   climas.yaml      │  padroes_narrativos.yaml                  │
│   (8 climas +      │  (Regras de escrita)                      │
│    4 desafios)     │                                           │
├─────────────────────────────────────────────────────────────────┤
│                      CAMADA 3: EXTENSÕES                        │
│                      ─────────────────                          │
│   evolucao_guardioes.yaml  │  artefatos.yaml                   │
│   (Como falam por ciclo)   │  (6 objetos simbólicos)           │
│                                                                 │
│   viajante.yaml            │  glossario.yaml                   │
│   (Títulos por ciclo)      │  (Termos)                         │
│                                                                 │
│   ontologia.yaml                                                │
│   (Atores do sistema)                                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Arquivos (12 total)

| Arquivo | Propósito | Camada |
|---------|-----------|--------|
| `index.yaml` | Navegação e mapa do LORE | Índice |
| `north_star.yaml` | Propósito, princípios, propósitos por ano | Core |
| `guardioes.yaml` | 5 Guardiões (dados fixos) | Core |
| `locais.yaml` | 5 Locais sensoriais | Core |
| `climas.yaml` | 8 Climas + 4 Desafios atmosféricos | Core |
| `padroes_narrativos.yaml` | Regras de narração imersiva | Core |
| `evolucao_guardioes.yaml` | Como Guardiões comunicam por ciclo | Extensão |
| `artefatos.yaml` | 6 Objetos simbólicos | Extensão |
| `viajante.yaml` | Títulos e evolução da criança | Extensão |
| `glossario.yaml` | Termos Sistema vs Reino | Extensão |
| `ontologia.yaml` | Atores (Maestro, Portador, Viajante) | Extensão |
| `README.md` | Este arquivo | — |

---

## 🎯 Regras de Ouro

### 1. SSOT (Single Source of Truth)
> Cada dado existe em UM arquivo apenas.

### 2. Referência, não duplicação
> "Link, don't duplicate." — Eric Evans

### 3. Dados fixos vs Evolução
- **Dados fixos** (nome, cor, frase) → `guardioes.yaml`
- **Evolução** (tom por ciclo) → `evolucao_guardioes.yaml`

---

## 🚀 Por Onde Começar?

1. **Leia `index.yaml`** — Mapa de navegação
2. **Leia `north_star.yaml`** — Propósito do projeto
3. **Consulte conforme necessidade**

### Para criar lição:
- Sempre: `guardioes`, `locais`, `padroes_narrativos`
- Por ciclo: `evolucao_guardioes`, `artefatos`, `viajante`

---

## 📊 Estatísticas

- **12 arquivos** (era 7, cresceu para completude)
- **~120KB** de conhecimento estruturado
- **5 Guardiões** × 4 ciclos de evolução
- **6 Artefatos** simbólicos
- **4 Títulos** do Viajante
- **13 Propósitos** por ano (K-12)
- **4 Desafios** atmosféricos

---

*Última atualização: 13/01/2026*
*Arquitetura aprovada pelo Maestro*
