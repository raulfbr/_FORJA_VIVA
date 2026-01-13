# 💬 DISCUSSÃO — Reorganização BMAD v6

**Data:** 12/01/2026 às 21:23  
**Status:** AGUARDANDO DECISÕES  

---

## 📊 RESUMO DO QUE ENTENDI

### O que você quer:

1. **Usar "Charlotte Mason" diretamente**, não "Sofia" (persona inventada)
2. **Todos arquivos em YAML**, não MD
3. **Conectar pastas desconectadas** (LORE, memoria, pergaminhos, saida)
4. **Ter vários agentes de áreas diferentes** (TI, Design, Negócios, etc.)
5. **BMAD v6** como framework

### O que descobri:

| Arquivo | Conteúdo |
|---------|----------|
| `_LEGADO/PAINEL-ESPECIALISTAS.md` | **22 especialistas em 11 Conselhos** — MUITO rico! |
| `logs/..._ORCHESTRATOR_ANALISE_BMAD_POETIQ.md` | Decisão: CM coordena Tríade com VETO |

---

## ❓ PERGUNTAS PARA DECISÃO

### 1. Agentes Pedagógicos — Nomes

| Atual | Proposta A (Real) | Proposta B (Persona) |
|-------|-------------------|----------------------|
| Sofia | **Charlotte Mason** | Manter Sofia |
| Euclides | **Jerome Bruner** | Manter Euclides |
| Artesão | **C.S. Lewis** + Tolkien + Potter | Manter Artesão |
| Veritas | **Makoto Fujimura** | Manter Veritas |

**Pergunta:** Usar os nomes REAIS ou manter as personas?

---

### 2. Estrutura de Pastas — Proposta

**Atual (desconectado):**
```
_FORJA_VIVA/
├── LORE/          # Dados narrativos
├── memoria/       # Vazio
├── pergaminhos/   # ?
├── saida/         # ?
├── forja-core/    # Conselheiros + Modelos
├── .bmad/         # Agentes
└── _LEGADO/       # Painel antigo
```

**Proposta de reorganização:**
```
_FORJA_VIVA/
├── .bmad/
│   ├── experts/           ← 22 especialistas do PAINEL (YAML)
│   │   ├── pedagogia/     ← CM, Macaulay
│   │   ├── matematica/    ← Bruner, Vygotsky
│   │   ├── narrativa/     ← Lewis, Tolkien, Fujimura, Potter
│   │   ├── negocios/      ← Godin, Hormozi, Thiel
│   │   ├── ux/            ← 5 Mães Personas
│   │   ├── engenharia/    ← DevOps, QA, DDD
│   │   └── agentes/       ← Antigravity, Estrategista, Mordomo
│   ├── workflows/
│   └── templates/
│
├── LORE/                  ← Manter (dados narrativos)
├── memoria/               ← Resumos de lições
├── pergaminhos/           ← ??? O que vai aqui?
├── saida/                 ← Output HTML/PDF

```

**Pergunta:** Qual é o propósito de `pergaminhos/` e `saida/`?

---

### 3. Formato YAML para Especialistas

Quer que eu converta os 22 especialistas para YAML assim?

```yaml
# .bmad/experts/pedagogia/charlotte_mason.yaml
id: charlotte_mason
tipo: expert
conselho: pedagogia
nome: Charlotte Mason
titulo: "A Governanta"
funcao: "Auditora de Dignidade e Princípios"
diretriz: |
  "Eu julgo o método pelos 20 Princípios. 
   Se fere um deles, fere a criança."
conceito: "Code of Law (20 Principles)"
citacao: |
  "Não me venha com 'métodos' que insultam 
   a inteligência divina da criança."
pergunta_veto: |
  "Esta lição viola o Princípio nº 1 (Dignidade)?"
protocolo_ativacao: |
  "Ative o Modo Charlotte Mason. Verifique se esta 
   lição trata o aluno como Pessoa ou Produto."
```

**Pergunta:** Este formato está bom?

---

### 4. Consultor de TI

Você mencionou querer um "especialista de TI para consultar".

**Já existe no PAINEL:**
- DevOps (O Maquinista) — Build automático
- QA (O Verificador) — Validação
- Eric Evans (DDD) — Consistência de dados
- **Antigravity** — Auditor de agentes IA

**Pergunta:** Falta algo? Qual tipo de TI você precisa que não está lá?

---

### 5. Workflow de Criação de Lição

O relatório do Orchestrator já definiu 13 passos:

```
FASE 1: PLANEJAMENTO
  1. PM recebe tema
  2. CM define Ideia Viva
  3. Bruner propõe CPA
  4. CM veta ou aprova
  → Output: PeRD

FASE 2: DESENVOLVIMENTO
  6. Artesão escreve
  7. Tolkien valida consistência
  8. Lewis valida tom
  9. CM revisa
  → Output: Rascunho YAML

FASE 3: VERIFICAÇÃO
  11. Veritas audita (5 checks)
  12. Matriarca valida confiança
  → Output: YAML Final + HTML
```

**Pergunta:** Este fluxo está OK ou quer ajustar?

---

## 📋 PRÓXIMOS PASSOS (AGUARDANDO APROVAÇÃO)

| # | Ação | Espera |
|---|------|--------|
| 1 | Decidir nomes (Real vs Persona) | ❓ Resposta |
| 2 | Clarificar `pergaminhos/` e `saida/` | ❓ Resposta |
| 3 | Converter 22 especialistas para YAML | ✅ Após aprovação |
| 4 | Reorganizar estrutura de pastas | ✅ Após aprovação |
| 5 | Criar workflow `criar-licao-premium.yaml` | ✅ Após aprovação |

---

*Aguardando suas decisões antes de prosseguir.*
