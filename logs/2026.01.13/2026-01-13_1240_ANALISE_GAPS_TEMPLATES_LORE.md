# 🔍 ANÁLISE DE GAPS: Templates vs LORE

**Data:** 13/01/2026 às 12:40  
**Objetivo:** Verificar se templates referenciam corretamente o LORE

---

## VERIFICAÇÃO: `000_global/licao-base.yaml`

### Referências ATUAIS (linhas 81-91):
```yaml
referencias_globais:
  guardioes: "LORE/guardioes.yaml"         ✅
  locais: "LORE/locais.yaml"               ✅
  climas: "LORE/climas.yaml"               ✅
  north_star: "LORE/north_star.yaml"       ✅
  padroes_narrativos: "LORE/padroes_narrativos.yaml" ✅
```

### GAPS IDENTIFICADOS:

| Arquivo LORE | Referenciado? | Impacto |
|--------------|---------------|---------|
| `index.yaml` | ❌ NÃO | Falta ponto de entrada |
| `evolucao_guardioes.yaml` | ❌ NÃO | Como falam por ciclo |
| `artefatos.yaml` | ❌ NÃO | 6 objetos simbólicos |
| `viajante.yaml` | ❌ NÃO | Títulos da criança |
| `glossario.yaml` | ❌ NÃO | Termos proibidos |
| `ontologia.yaml` | ❌ NÃO | Atores do sistema |

### AÇÃO NECESSÁRIA:
Atualizar `referencias_globais` para incluir TODOS os arquivos LORE

---

## VERIFICAÇÃO: `00_K_sementes/regras.yaml`

### O que está BOM:
- ✅ Proporções CPA (Bruner)
- ✅ Tempo (CM)
- ✅ Scaffolding (Vygotsky)
- ✅ Tom (Lewis)
- ✅ Densidade Sensorial (Potter)
- ✅ Materiais (Mães Personas)
- ✅ Narração (CM)
- ✅ Adaptação Bernardo
- ✅ Guardiões por frequência
- ✅ Checklist QA

### GAPS IDENTIFICADOS:

| Elemento | No Template? | No LORE? | Gap |
|----------|--------------|----------|-----|
| Título Viajante "Herdeiro" | ⚠️ Citado | ✅ viajante.yaml | Falta referência explícita |
| Propósito "Promessas do Rei" | ❌ Não | ✅ north_star.yaml | Falta referência |
| Tom Guardiões por ciclo | ⚠️ Parcial | ✅ evolucao_guardioes.yaml | Falta referência |
| Artefatos | ❌ Não | ✅ artefatos.yaml | N/A (não há artefato em K) |
| Referência ao index.yaml | ❌ Não | — | Falta |

### AÇÃO NECESSÁRIA:
1. Adicionar seção `referencias_lore` no template
2. Adicionar `proposito_narrativo` referenciando north_star.yaml
3. Adicionar referência a `viajante.yaml#herdeiro`

---

## RESUMO DE GAPS

### Template Global (`licao-base.yaml`):
```yaml
# FALTA ADICIONAR:
referencias_globais:
  indice: "LORE/index.yaml"                        # ← NOVO
  evolucao_guardioes: "LORE/evolucao_guardioes.yaml"  # ← NOVO
  artefatos: "LORE/artefatos.yaml"                 # ← NOVO
  viajante: "LORE/viajante.yaml"                   # ← NOVO
  glossario: "LORE/glossario.yaml"                 # ← NOVO
  ontologia: "LORE/ontologia.yaml"                 # ← NOVO
```

### Template Sementes (`regras.yaml`):
```yaml
# FALTA ADICIONAR:
referencias_lore:
  indice: "LORE/index.yaml"
  proposito: "LORE/north_star.yaml#propositos_por_ano.K_sementes"
  titulo_viajante: "LORE/viajante.yaml#herdeiro"
  tom_guardioes: "LORE/evolucao_guardioes.yaml#sementes"
```

---

## PLANO DE CORREÇÃO

1. ✅ Atualizar `000_global/licao-base.yaml` — adicionar todas refs LORE
2. ✅ Atualizar `00_K_sementes/regras.yaml` — adicionar refs específicas
3. ⚠️ Verificar outros 12 templates de ano — mesma correção

*Análise concluída — Pronto para correção*
