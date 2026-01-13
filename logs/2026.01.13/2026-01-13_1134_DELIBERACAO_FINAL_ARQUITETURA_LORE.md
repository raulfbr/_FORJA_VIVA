# 🏛️ DELIBERAÇÃO MULTI-ROUND: Arquitetura Final do LORE

**Data:** 13/01/2026 às 11:34  
**Tema:** Equilibrar Complexidade, Qualidade e Prazo  
**Status:** DOCUMENTO FINAL PARA DECISÃO

---

## 🎯 O DILEMA DO MAESTRO

> "Muito complexo não fazemos a entrega e não honramos o prazo e o premium, mas se não deixamos imersivo também não fica belo e não fica amarrando toda a ideia. Ache o equilíbrio focando na qualidade."

### North Star — Princípio 1:
> **"Qualidade Não é Negociável"** — 3 lições impecáveis > 10 lições boas

### A Tensão:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   COMPLEXIDADE        ←─────────→        SIMPLICIDADE   │
│   (Imersão máxima)                    (Entrega rápida)  │
│                                                         │
│                    QUALIDADE                            │
│                  (O compromisso)                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# ROUND 1: ENGENHARIA (Eric Evans + BMAD + Clean Code)

## Eric Evans — Domain-Driven Design

> **POSIÇÃO:** "A complexidade não é o inimigo. A complexidade MAL GERENCIADA é o inimigo."

### Princípios DDD Aplicados:

| Princípio | Significado | Aplicação ao LORE |
|-----------|-------------|-------------------|
| **SSOT** | Um dado, um lugar | Cada conceito em UM arquivo |
| **Bounded Context** | Fronteiras claras | LORE = dados, Templates = regras |
| **Ubiquitous Language** | Termos consistentes | Glossário define termos |
| **Aggregate Root** | Ponto de entrada | **ARQUIVO MESTRE** como índice |

### Proposta Eric Evans: ARQUIVO MESTRE (index.yaml)

> "O problema não é ter muitos arquivos. O problema é não saber QUAL arquivo consultar QUANDO."

```yaml
# LORE/index.yaml — O Mestre
tipo: indice_lore
versao: "1.0"

navegacao:
  para_criar_licao:
    obrigatorios:
      - guardioes.yaml
      - locais.yaml
      - padroes_narrativos.yaml
    conforme_ciclo:
      sementes: [evolucao_guardioes.yaml#sementes]
      raizes: [evolucao_guardioes.yaml#raizes, artefatos.yaml#diario]
      logica: [artefatos.yaml, desafios.yaml]
      legado: [artefatos.yaml#tocha, viajante.yaml#portador]
      
  para_revisao:
    - north_star.yaml (propósitos)
    
  para_qa:
    - glossario.yaml (termos proibidos)
```

**Vantagem:** Com o `index.yaml`, mesmo com 12 arquivos, a navegação é SIMPLES.

---

## BMAD Framework

> **POSIÇÃO:** "Federated Knowledge — Agentes referenciam, não duplicam."

### Regra BMAD:
```yaml
principio: "Federated Knowledge"
aplicacao: "LORE/*.yaml como fonte única"
```

### Proposta BMAD: Sistema de Referências

Cada arquivo LORE referencia os outros com caminho explícito:

```yaml
# Em qualquer arquivo:
referencias_relacionadas:
  guardioes: "LORE/guardioes.yaml"
  locais: "LORE/locais.yaml"
  indice: "LORE/index.yaml"  # Ponto de entrada
```

---

## Clean Code

> **POSIÇÃO:** "Código (e dados) devem ser legíveis por humanos. Simplicidade > Esperteza."

### Regras Clean Code para LORE:

| Regra | Aplicação |
|-------|-----------|
| Nomes descritivos | `evolucao_guardioes.yaml` não `eg.yaml` |
| Uma responsabilidade | Cada arquivo faz UMA coisa |
| Comentários úteis | Headers explicam propósito |
| Evitar duplicação | Referenciar, não copiar |

### Pergunta Clean Code:
> "Um desenvolvedor novo conseguiria entender o LORE em 10 minutos?"

**Com `index.yaml`:** SIM — lê o índice, entende a estrutura.  
**Sem `index.yaml`:** TALVEZ — precisa abrir vários arquivos.

---

# ROUND 2: PEDAGOGIA (Charlotte Mason + North Star)

## Charlotte Mason

> **POSIÇÃO:** "Não sacrifique a alma pelo prazo."

### Princípio CM:
> "Education is a life — não uma máquina de produção."

### Análise CM:

| Abordagem | Prós | Contras | Veredito CM |
|-----------|------|---------|-------------|
| **Mínimo (7 arquivos)** | Entrega rápida | Lições menos imersivas | ❌ Insuficiente |
| **Médio (10 arquivos)** | Equilíbrio | Precisa organização | ✅ Recomendado |
| **Máximo (15+ arquivos)** | Muito rico | Complexo demais | ❌ Arriscado |

### Proposta CM:

> "Comecemos com 10 arquivos MUITO BEM ORGANIZADOS. Se precisar de mais, expandimos. Se for demais, simplificamos. Mas NUNCA entregamos algo sem alma para cumprir prazo."

---

## North Star — Princípio 1 vs Princípio de Entrega

### Tensão Real:

| North Star Diz | Prazo Diz |
|----------------|-----------|
| "3 impecáveis > 10 boas" | "Entrega é honra" |
| "Qualidade não é negociável" | "Premium exige cumprimento" |

### Resolução:

> **"Qualidade INCLUI entrega."** Uma lição perfeita que nunca sai não serve a ninguém. Uma lição boa que sai no prazo serve à família.

**Mas:** Uma lição medíocre que sai rápido DESONRA o projeto.

### Aplicação:

| Cenário | Decisão |
|---------|---------|
| Posso entregar COM qualidade no prazo | ✅ Entregar |
| Posso entregar MAS sem qualidade | ❌ Atrasar e fazer direito |
| Não sei se vou conseguir | ⚠️ Simplificar escopo |

---

# ROUND 3: PROPOSTA FINAL DE ARQUITETURA

## O Problema:

> "Como ter imersão SEM complexidade paralisante?"

## A Solução:

### Arquitetura em 3 Camadas:

```
┌─────────────────────────────────────────────────────────┐
│                    CAMADA 1: ÍNDICE                     │
│                    ───────────────                      │
│                     index.yaml                          │
│              (Mapa de navegação ÚNICO)                  │
├─────────────────────────────────────────────────────────┤
│                    CAMADA 2: CORE                       │
│                    ──────────────                       │
│   north_star.yaml  │  guardioes.yaml  │  locais.yaml   │
│   (Princípios)     │  (5 personagens) │  (5 lugares)   │
│                                                         │
│   climas.yaml      │  padroes_narrativos.yaml          │
│   (8+4 atmosferas) │  (Regras de escrita)              │
├─────────────────────────────────────────────────────────┤
│                    CAMADA 3: EXTENSÕES                  │
│                    ─────────────────                    │
│   evolucao_guardioes.yaml  │  artefatos.yaml           │
│   (Como falam por ciclo)   │  (6 objetoss)             │
│                                                         │
│   viajante.yaml            │  glossario.yaml           │
│   (Títulos por ciclo)      │  (Termos)                 │
│                                                         │
│   ontologia.yaml                                        │
│   (Atores do sistema)                                   │
└─────────────────────────────────────────────────────────┘
```

### Total: 11 arquivos (atual: 7 + 4 novos)

| Camada | Arquivos | Propósito |
|--------|----------|-----------|
| **Índice** | 1 | Navegação |
| **Core** | 5 | Essenciais para toda lição |
| **Extensões** | 5 | Usados conforme necessidade |

---

## Detalhamento dos 4 Novos Arquivos:

### 1. `index.yaml` — O Mestre (CRÍTICO)

```yaml
# ════════════════════════════════════════════════════════════════════════
# ÍNDICE DO LORE — Arquivo Mestre de Navegação
# ════════════════════════════════════════════════════════════════════════
tipo: indice
versao: "1.0"

estrutura:
  camada_core:
    - north_star.yaml: "Propósito, princípios, propósitos por ano"
    - guardioes.yaml: "5 Guardiões (dados fixos)"
    - locais.yaml: "5 Locais"
    - climas.yaml: "8 climas + 4 desafios atmosféricos"
    - padroes_narrativos.yaml: "Regras de narração"
    
  camada_extensoes:
    - evolucao_guardioes.yaml: "Como Guardiões comunicam por ciclo"
    - artefatos.yaml: "6 objetos simbólicos"
    - viajante.yaml: "Títulos do Viajante por ciclo"
    - glossario.yaml: "Termos Sistema vs Reino"
    - ontologia.yaml: "Atores (Maestro, Portador, Viajante)"

navegacao_por_tarefa:
  criar_licao:
    sempre: [guardioes, locais, padroes_narrativos]
    por_ciclo:
      sementes: [evolucao_guardioes#sementes]
      raizes: [evolucao_guardioes#raizes, artefatos#diario]
      logica: [evolucao_guardioes#logica, artefatos]
      legado: [evolucao_guardioes#legado, artefatos#tocha, viajante#portador]
      
  revisar_licao:
    sempre: [north_star#propositos, glossario#proibidos]
    
  entender_sistema:
    ler: [ontologia, index]
```

**Por que é CRÍTICO:**
- Responde: "Onde está o quê?"
- Evita confusão com muitos arquivos
- Único ponto de entrada

---

### 2. `evolucao_guardioes.yaml` — Como Comunicam

```yaml
# Cada guardião tem dados FIXOS em guardioes.yaml
# Aqui está COMO evoluem na comunicação

evolucao:
  melquior:
    sementes:
      tom: "Encantamento paternal"
      exemplo: "Sente o calor no seu rosto?"
    raizes:
      tom: "Mentoria encorajadora"
      exemplo: "Você já construiu a fundação."
    logica:
      tom: "Desafio respeitoso"
      exemplo: "Os antigos matemáticos..."
    legado:
      tom: "Comissionamento solene"
      exemplo: "Você sai Portador da Tocha."
      
  # ... (mesma estrutura para cada guardião)
```

**Por que separado de `guardioes.yaml`:**
- Guardiões = dados FIXOS (nome, cor, frase)
- Evolução = dados POR CICLO (como falam)
- SSOT: cada tipo de dado em seu lugar

---

### 3. `artefatos.yaml` — 6 Objetos (Mínimo Viável)

```yaml
artefatos:
  diario_do_reino:
    nome: "Diário do Reino"
    emoji: "📔"
    guardiao: Melquior
    significado: "Registro da jornada"
    quando_aparece: "Entregue em Raízes-1"
    uso_narrativo: "Criança anota descobertas"
    
  bussola_celeste:
    nome: "Bússola de Celeste"
    emoji: "🧭"
    guardiao: Celeste
    significado: "Direção e curiosidade"
    quando_aparece: "Lógica (exploração)"
    uso_narrativo: "Orienta em problemas complexos"
    
  # ... (4 outros: Martelo, Pena, Ampulheta, Tocha)

regras:
  uso: "Artefatos aparecem quando fazem sentido, não obrigatoriamente."
  referencia: "Lição menciona: 'ver artefatos.yaml#diario_do_reino'"
```

---

### 4. `viajante.yaml` — Títulos e Evolução

```yaml
titulos:
  sementes:
    titulo: "Herdeiro"
    significado: "Recebe a herança do saber"
    ritual_entrada: "Melquior apresenta o Reino"
    
  raizes:
    titulo: "Construtor"
    significado: "Usa o saber para construir"
    ritual_entrada: "Bernardo entrega ferramentas"
    
  logica:
    titulo: "Explorador"
    significado: "Busca verdade além do visível"
    ritual_entrada: "Celeste revela a Bússola"
    
  legado:
    titulo: "Portador da Tocha"
    significado: "Passa adiante o que recebeu"
    ritual_entrada: "Melquior entrega a Tocha"
    ritual_saida: "O ciclo se completa"
```

---

## Modificações em Arquivos EXISTENTES:

### 1. `north_star.yaml` — Adicionar propósitos por ano

```yaml
# Adicionar seção:
propositos_por_ano:
  K_sementes:
    frase: "Os números são promessas do Rei."
    elaboracao: "..."
  1_raizes:
    frase: "Sou o Construtor da Vila."
    elaboracao: "..."
  # ... (13 anos)
```

### 2. `climas.yaml` — Adicionar 4 desafios atmosféricos

```yaml
# Adicionar seção:
desafios_atmosfericos:
  vento_gelado:
    nome: "O Vento Gelado"
    emoji: "❄️"
    representa: "Frustração quando nada funciona"
    quando_usar: "Lições difíceis"
    tom: "Desconforto temporário"
    superacao: "Persistência de Bernardo"
    
  nevoa_do_vale:
    nome: "A Névoa do Vale"
    emoji: "🌫️"
    representa: "Confusão conceitual"
    quando_usar: "Conceitos abstratos"
    tom: "Mistério"
    superacao: "Clareza vem com paciência"
    
  # ... (Relógio Apressado, Sombra Cinza)
```

---

# ROUND 4: ANÁLISE DE VIABILIDADE

## Esforço de Implementação:

| Item | Esforço | Tempo Estimado |
|------|---------|----------------|
| `index.yaml` | Baixo | 15 min |
| `evolucao_guardioes.yaml` | Médio | 45 min |
| `artefatos.yaml` | Baixo | 20 min |
| `viajante.yaml` | Baixo | 15 min |
| Adicionar em `north_star.yaml` | Médio | 30 min |
| Adicionar em `climas.yaml` | Baixo | 15 min |
| **TOTAL** | — | **~2h30** |

## Matriz de Risco:

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Arquivos ficam desatualizados | Média | Alto | `index.yaml` como checkpoint |
| Complexidade paralisa | Baixa | Alto | Começar com mínimo |
| Falta imersão | Alta (se não fazer) | Alto | Fazer os 4 arquivos |
| Prazo não cumprido | Baixa | Médio | 2h30 é aceitável |

---

# ROUND 5: DECISÃO FINAL (Engenharia + CM + North Star)

## Consenso:

> **"11 arquivos COM `index.yaml` são MENOS complexos que 7 arquivos SEM organização clara."**

### Eric Evans diz:
> "A complexidade está na DESORGANIZAÇÃO, não na quantidade."

### Charlotte Mason diz:
> "Uma lição sem alma não serve. Os artefatos e evolução dão ALMA."

### North Star diz:
> "Qualidade não é negociável. Mas qualidade inclui entrega."

---

## ✅ PROPOSTA FINAL PARA APROVAÇÃO

| # | Item | Ação | Prioridade |
|---|------|------|------------|
| 1 | `index.yaml` | **CRIAR** — Arquivo Mestre de navegação | CRÍTICA |
| 2 | `evolucao_guardioes.yaml` | **CRIAR** — Como comunicam por ciclo | ALTA |
| 3 | `artefatos.yaml` | **CRIAR** — 6 objetos simbólicos | ALTA |
| 4 | `viajante.yaml` | **CRIAR** — Títulos por ciclo | ALTA |
| 5 | `north_star.yaml` | **MODIFICAR** — Adicionar propósitos/ano | ALTA |
| 6 | `climas.yaml` | **MODIFICAR** — Adicionar 4 desafios | MÉDIA |
| 7 | Atualizar referências | Todos arquivos apontam para `index.yaml` | MÉDIA |

### Estrutura Final:

```
LORE/ (11 arquivos)
├── index.yaml                 ← MESTRE (NOVO)
├── north_star.yaml            ← +propósitos_por_ano
├── guardioes.yaml             ← (inalterado)
├── evolucao_guardioes.yaml    ← NOVO
├── locais.yaml                ← (inalterado)
├── climas.yaml                ← +desafios_atmosfericos
├── artefatos.yaml             ← NOVO
├── viajante.yaml              ← NOVO
├── padroes_narrativos.yaml    ← (inalterado)
├── ontologia.yaml             ← (inalterado)
├── glossario.yaml             ← (inalterado)
└── README.md
```

---

## 📋 CHECKLIST DE APROVAÇÃO

Marque suas decisões:

- [ ] **1. Aprovar criação de `index.yaml`?** (Arquivo Mestre)
- [ ] **2. Aprovar criação de `evolucao_guardioes.yaml`?**
- [ ] **3. Aprovar criação de `artefatos.yaml`?** (6 itens)
- [ ] **4. Aprovar criação de `viajante.yaml`?** (4 títulos)
- [ ] **5. Aprovar adicionar propósitos/ano em `north_star.yaml`?**
- [ ] **6. Aprovar adicionar 4 desafios em `climas.yaml`?**
- [ ] **7. Aprovar atualizar referências para `index.yaml`?**

### Alternativas:

- [ ] **A.** Aprovar TUDO (implementar agora)
- [ ] **B.** Aprovar parcialmente: _____________
- [ ] **C.** Rejeitar e simplificar mais
- [ ] **D.** Adiar decisão e deliberar mais

---

*Documento final de deliberação — Aguardando decisão do Maestro*  
*Coordenadores: Eric Evans + Charlotte Mason + BMAD*  
*Data: 13/01/2026*
