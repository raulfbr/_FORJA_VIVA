# 🛠️ PLANO DE IMPLEMENTAÇÃO: Limpeza + Templates por Ano

**Data:** 13/01/2026 às 10:27  
**Aprovações do Maestro:**
- ✅ 1 template por ano (13 total: K através 12)
- ✅ Propósitos narrativos elaborados por CM
- ✅ Revisão profunda para remover refs a GOVERNANÇA

---

## FASE 1: LIMPEZA DE ESTRUTURA

### Pastas a DELETAR:

| Pasta | Motivo | Ação |
|-------|--------|------|
| `memoria/` | Vazia | ❌ DELETAR |
| `docs/` | 4 arquivos antigos, sistema novo em .bmad | ❌ DELETAR |
| `_LEGADO/` | Já migrado para .bmad | 📦 MOVER para _ARQUIVADO ou DELETAR |

### Pastas a MANTER:

| Pasta | Motivo | Status |
|-------|--------|--------|
| `.bmad/` | Sistema principal | ✅ MANTER |
| `LORE/` | Dados SSOT globais | ✅ MANTER |
| `forja-core/` | Pipeline Gutenberg (código) | ✅ MANTER |
| `curriculo/` | Lições e currículos | ✅ MANTER |
| `logs/` | Logs de deliberação | ✅ MANTER |
| `site/` | Output HTML | ✅ MANTER |

### Arquivos na raiz a REVISAR:

| Arquivo | Tamanho | Decisão Proposta |
|---------|---------|------------------|
| `README.md` | 13KB | ✅ MANTER (atualizar) |
| `LICENSE` | 6KB | ✅ MANTER |
| `CONTRIBUTING.md` | 3KB | ✅ MANTER |
| `SECURITY.md` | 1KB | ✅ MANTER |
| `.gitignore` | 5KB | ✅ MANTER |
| `ARQUITETURA_CANONICA.md` | 12KB | ⚠️ MOVER para .bmad/docs |
| `CONTEXT_INDEX.md` | 2KB | ⚠️ MOVER para .bmad/docs |
| `CONTEXT_RESTORE.md` | 5KB | ⚠️ MOVER para .bmad/docs |
| `DEFINITION_OF_DONE.md` | 5KB | ⚠️ MOVER para .bmad/docs |
| `GUIA_REVISAO_MAESTRO.md` | 8KB | ⚠️ MOVER para .bmad/docs |
| `Texto.md` | 48KB | ⚠️ REVISAR (parece grande) |

---

## FASE 2: ATUALIZAÇÃO DE REFERÊNCIAS

### Currículos Mestres — Referências Antigas:

Os currículos atualmente referenciam:
- `GOVERNANCA/09_MATRIZ_DE_EVOLUCAO_K12.md`
- `GOVERNANCA/02_LIVRO_DO_REINO.md`
- `GOVERNANCA/10_DNA_DA_CRIACAO.md`
- `GOVERNANCA/04_MANUAL_DO_OFICIO.md`

**Nova estrutura:**
| Antigo | Novo |
|--------|------|
| `GOVERNANCA/02_LIVRO_DO_REINO.md` | `LORE/guardioes.yaml + locais.yaml` |
| `GOVERNANCA/09_MATRIZ_DE_EVOLUCAO_K12.md` | `.bmad/templates/[ciclo]/regras.yaml` |
| `GOVERNANCA/10_DNA_DA_CRIACAO.md` | `LORE/padroes_narrativos.yaml` |
| `GOVERNANCA/04_MANUAL_DO_OFICIO.md` | `.bmad/experts/narrativa/` |

---

## FASE 3: TEMPLATES POR ANO

### Estrutura Final:

```
.bmad/templates/
├── 000_global/
│   └── licao-base.yaml          # Seções obrigatórias em TODAS lições
├── 00_K_sementes/
│   └── regras.yaml              # ✅ JÁ EXISTE
├── 01_1ano_raizes/
│   └── regras.yaml              # A CRIAR
├── 02_2ano_raizes/
│   └── regras.yaml              # A CRIAR
├── 03_3ano_raizes/
│   └── regras.yaml              # A CRIAR
├── 04_4ano_raizes/
│   └── regras.yaml              # A CRIAR
├── 05_5ano_raizes/
│   └── regras.yaml              # A CRIAR
├── 06_6ano_logica/
│   └── regras.yaml              # A CRIAR
├── 07_7ano_logica/
│   └── regras.yaml              # A CRIAR
├── 08_8ano_logica/
│   └── regras.yaml              # A CRIAR
├── 09_9ano_legado/
│   └── regras.yaml              # A CRIAR
├── 10_10ano_legado/
│   └── regras.yaml              # A CRIAR
├── 11_11ano_legado/
│   └── regras.yaml              # A CRIAR
└── 12_12ano_legado/
    └── regras.yaml              # A CRIAR
```

---

## FASE 4: PROPÓSITOS NARRATIVOS (Elaborados por CM)

### Charlotte Mason Elabora:

> *"Cada ciclo é uma estação da alma. A criança não apenas aprende — ela AMADURECE. O propósito narrativo deve refletir essa transformação interior."*

| Série | Ciclo | Idade | Propósito Narrativo (CM Elaborado) |
|-------|-------|-------|-----------------------------------|
| K | Sementes | 4-6 | **"Os números são promessas do Rei."** A criança descobre que cada quantidade guarda um segredo sagrado. O mundo é encantado e cheio de tesouros escondidos. Ela é HERDEIRA de algo maior. |
| 1º | Raízes-1 | 6-7 | **"Sou o Construtor da Vila."** A criança usa as promessas para CONSTRUIR. Cada número agora serve a um propósito: medir, contar, organizar. Ela sai do jardim e entra na oficina. |
| 2º | Raízes-2 | 7-8 | **"O Mercado me ensina justiça."** A criança troca, compara, equilibra. A matemática se torna moeda de relação com os outros. O zelo e a honestidade entram em cena. |
| 3º | Raízes-3 | 8-9 | **"Exploro a Vastidão do Reino."** A criança expande horizontes. Números maiores, operações combinadas, geometria do espaço. O mundo cresce e ela cresce com ele. |
| 4º | Raízes-4 | 9-10 | **"Ordeno o que descobri."** A criança sistematiza. Frações, decimais, proporções. O que era intuição vira estrutura. Ela começa a ver PADRÕES. |
| 5º | Raízes-5 | 10-11 | **"A linguagem dos padrões se revela."** A criança vê que tudo se conecta. Multiplicação e divisão são danças inversas. Ela está pronta para a abstração. |
| 6º | Lógica-1 | 11-12 | **"A matemática é a linguagem do universo."** (Galileu) A criança descobre que os números não são inventados — são DESCOBERTOS. A álgebra é poesia codificada. |
| 7º | Lógica-2 | 12-13 | **"O raciocínio é uma forja."** A criança aprende a PROVAR. Não basta sentir que algo é verdade — ela precisa demonstrar. A lógica formal entra em cena. |
| 8º | Lógica-3 | 13-14 | **"O abstrato ilumina o concreto."** A criança usa álgebra para resolver problemas reais. O abstrato não é fuga — é ferramenta de poder sobre o mundo. |
| 9º | Legado-1 | 14-15 | **"O que descobri é usado pelo mundo."** A criança vê matemática em engenharia, economia, ciência. Ela não apenas estuda — ela APLICA. |
| 10º | Legado-2 | 15-16 | **"Sou aprendiz dos mestres antigos."** A criança estuda a história da matemática. Pitágoras, Euclides, Arquimedes não são nomes — são mentores. |
| 11º | Legado-3 | 16-17 | **"A matemática me prepara para servir."** A criança vê que cálculo, estatística e geometria resolvem problemas reais. O conhecimento é para o BEM do próximo. |
| 12º | Legado-4 | 17-18 | **"Sou mordomo do saber."** A criança está pronta para a universidade ou a vida. O que aprendeu não é SEU — é herança para passar adiante. O ciclo se completa. |

---

## FASE 5: ORDEM DE EXECUÇÃO

### Prioridade 1 — Limpeza (Agora):
1. [x] Determinar pastas a deletar
2. [ ] Deletar `memoria/`
3. [ ] Mover ou deletar `docs/`
4. [ ] Arquivar `_LEGADO/`
5. [ ] Mover arquivos contexto da raiz para `.bmad/docs/`

### Prioridade 2 — Templates (Agora):
1. [ ] Renomear pastas existentes para nova nomenclatura (`00_K_sementes`)
2. [ ] Criar `regras.yaml` para cada ano (K-12)
3. [ ] Cada arquivo marca `STATUS: EM_CONSTRUCAO`
4. [ ] Cada arquivo referencia currículo mestre correspondente

### Prioridade 3 — Atualização de Referências (Próxima Sessão):
1. [ ] Revisar cada currículo mestre
2. [ ] Substituir refs GOVERNANÇA por LORE/.bmad
3. [ ] Verificar links funcionam

---

## 📋 RESUMO PARA APROVAÇÃO

| Item | Ação | Impacto |
|------|------|---------|
| `memoria/` | DELETAR | Nenhum (vazio) |
| `docs/` | DELETAR ou _LEGADO | Baixo (4 arquivos antigos) |
| `_LEGADO/` | ARQUIVAR ou DELETAR | Baixo (já migrado) |
| Templates | Criar 13 | Alto (base para lições) |
| Propósitos | CM elaborou | Alto (direção narrativa) |
| Referências | Atualizar | Médio (currículos mestres) |

---

*Aguardando aprovação para executar Fase 1 e 2*
