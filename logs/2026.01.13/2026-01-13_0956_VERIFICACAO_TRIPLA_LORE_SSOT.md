# 🔍 VERIFICAÇÃO TRIPLA: Arquitetura BMAD + Conexão com LORE

**Data:** 13/01/2026 às 09:56  
**Coordenadora:** Eric Evans (DDD/SSOT)  
**Tema:** Verificar arquitetura criada e conexão com LORE existente

---

## PASS 1: INVENTÁRIO DO LORE EXISTENTE

Descoberta de arquivos em `LORE/`:

| Arquivo | Linhas | Conteúdo | Status |
|---------|--------|----------|--------|
| `north_star.yaml` | 404 | Propósito, missão, princípios, tríade | ✅ SSOT |
| `guardioes.yaml` | 128 | 5 Guardiões com frases, cores, locais | ✅ SSOT |
| `locais.yaml` | 132 | 5 Locais com atmosfera sensorial | ✅ SSOT |
| `climas.yaml` | ~100 | Climas do Reino | ✅ SSOT |
| `glossario.yaml` | ~100 | Termos do projeto | ✅ SSOT |
| `ontologia.yaml` | ~80 | Estrutura conceitual | ✅ SSOT |
| `padroes_narrativos.yaml` | 300 | Padrões de narração (NOVO) | ⚠️ DUPLICAÇÃO PARCIAL |

---

## ⚠️ ALERTA ERIC EVANS: DUPLICAÇÃO DETECTADA

### O que eu criei em `padroes_narrativos.yaml`:
- Frases canônicas dos Guardiões
- Locais canônicos
- Virtudes dos Guardiões
- Tom por Guardião

### O que JÁ EXISTE em `guardioes.yaml`:
- ✅ Frases canônicas (`frase_assinatura`)
- ✅ Virtudes (`semente`)
- ✅ Tom de voz (`tom_de_voz`)
- ✅ Local associado (`local_associado`)

### O que JÁ EXISTE em `locais.yaml`:
- ✅ Descrição sensorial completa (`atmosfera`)
- ✅ Luz, cheiro, som, textura
- ✅ Uso narrativo

### DIAGNÓSTICO:
> **Violação de SSOT.** Eu dupliquei dados que já existiam.
> Isso vai causar inconsistência quando alguém atualizar um arquivo e não o outro.

---

## PASS 2: O QUE ESTÁ CORRETO (Manter)

### ✅ Em `.bmad/templates/sementes/regras.yaml`:
- Proporções CPA por ciclo (ORIGINAL — não existe em outro lugar)
- Scaffolding por ciclo (ORIGINAL)
- Tempo de preparo por ciclo (ORIGINAL)
- Checklist QA (ORIGINAL)

### ✅ Em `padroes_narrativos.yaml` (Partes Originais):
- Transições sensoriais (REGRAS, não dados)
- Falas com [tom] (REGRAS, não dados)
- Pausas explícitas (REGRAS, não dados)
- Scaffolding por ciclo (REGRAS)
- Tom por ciclo (REGRAS)
- Densidade sensorial por ciclo (REGRAS)

### ❌ Em `padroes_narrativos.yaml` (DUPLICADO — Remover):
- Seção `frases_canonicas` — já em `guardioes.yaml`
- Seção `virtude_encarnada` — já em `guardioes.yaml`
- Dados de locais — já em `locais.yaml`

---

## PASS 3: REORGANIZAÇÃO PROPOSTA

### Princípio Eric Evans: "Link, Don't Duplicate"

**Antes (problema):**
```
padroes_narrativos.yaml
├── frases_canonicas (DUPLICADO)
├── virtude_encarnada (DUPLICADO)
└── regras de narração (ORIGINAL)
```

**Depois (corrigido):**
```
padroes_narrativos.yaml
├── referencia: "LORE/guardioes.yaml" ← LINK
├── referencia: "LORE/locais.yaml" ← LINK
├── regras_transicao_sensorial (ORIGINAL)
├── regras_falas_tom (ORIGINAL)
├── regras_pausas (ORIGINAL)
├── scaffolding_por_ciclo (ORIGINAL)
├── tom_por_ciclo (ORIGINAL)
└── densidade_por_ciclo (ORIGINAL)
```

---

## MAPA DE SSOT ATUALIZADO

| Dado | Fonte Única (SSOT) | Referenciado Por |
|------|-------------------|------------------|
| Guardiões (nomes, frases, cores) | `LORE/guardioes.yaml` | templates, lessons |
| Locais (atmosfera sensorial) | `LORE/locais.yaml` | templates, lessons |
| Climas | `LORE/climas.yaml` | lessons |
| North Star (princípios) | `LORE/north_star.yaml` | experts, workflows |
| **Regras de narração** | `LORE/padroes_narrativos.yaml` | templates, lessons |
| **Regras por ciclo** | `.bmad/templates/[ciclo]/regras.yaml` | workflows |
| Experts | `.bmad/experts/[grupo]/` | orchestrator |
| Workflows | `.bmad/workflows/` | orchestrator |

---

## RECOMENDAÇÃO: Onde colocar o quê

### Em `.bmad/templates/[ciclo]/regras.yaml`:
- Proporções CPA obrigatórias
- Tempo de preparo máximo
- Scaffolding esperado
- Checklist QA do ciclo

### Em `LORE/padroes_narrativos.yaml`:
- Transições sensoriais (como fazer, não dados)
- Regras de [tom] (como indicar, não quais são)
- Pausas (tipos e quando usar)
- Scaffolding por ciclo (o que muda)
- Tom por ciclo (o que muda)
- Densidade sensorial (o que muda)

### Em `LORE/guardioes.yaml` (JÁ EXISTE):
- Frases canônicas
- Virtudes
- Tom de voz
- Local associado

### Em `LORE/locais.yaml` (JÁ EXISTE):
- Descrição sensorial completa
- Atmosfera (luz, cheiro, som, textura)
- Uso narrativo

---

## AÇÃO REQUERIDA

1. **REMOVER** de `padroes_narrativos.yaml`:
   - Seção `frases_canonicas` (linhas 130-175)
   - Seção `virtude_encarnada` (linhas 177-200)
   
2. **ADICIONAR** referências em vez de dados:
   ```yaml
   referencias_ssot:
     guardioes: "LORE/guardioes.yaml"
     locais: "LORE/locais.yaml"
     climas: "LORE/climas.yaml"
   ```

3. **ATUALIZAR** `.bmad/experts/engenharia/engenharia.yaml`:
   - Adicionar regra de verificação de SSOT
   - Adicionar lista de arquivos SSOT

---

## 🎖️ VEREDITO DA VERIFICAÇÃO TRIPLA

| Pass | Aspecto | Status |
|------|---------|--------|
| 1 | Inventário LORE | ✅ Completo (7 arquivos) |
| 2 | Arquitetura nova | ⚠️ Duplicação parcial detectada |
| 3 | SSOT respeitado | ❌ Violado — correção necessária |

### Status: ⚠️ APROVADO COM CORREÇÃO OBRIGATÓRIA

A arquitetura está correta em estrutura, mas há duplicação de dados.
Correção: remover dados duplicados e usar referências.

---

*Verificação executada em 13/01/2026 às 09:56*  
*Auditor: Eric Evans (DDD/SSOT)*
