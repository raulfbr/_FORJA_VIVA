# 📊 REVISÃO PROFUNDA — Comparação L001 vs Template

**Data:** 12/01/2026  
**Objetivo:** Identificar gaps e sincronizar template com lição refinada  

---

## 📋 Comparação de Estruturas

### L001 (Atual) vs Template V4.1

| # | Seção L001 | Template V4.1 | Status |
|---|------------|---------------|--------|
| 1 | Para o Portador | ✅ Existe | 🟢 Alinhado |
| 2 | Bancada do Reino | ✅ Existe | 🟡 L001 tem "Para Enriquecer" |
| 3 | Dica para o Portador | ❌ Não existe | 🔴 Adicionar (era Áudio-Script) |
| 4 | Ritual de Abertura | ✅ Existe | 🟢 Alinhado |
| 5 | A Jornada | ✅ Existe | 🟢 Alinhado |
| 6 | Se Quiser Voar | ❌ Existe como opcional | 🟡 Marcar como opcional |
| 7 | Narração | ✅ Existe | 🟡 Template diz "Sondas de Sabedoria" |
| 8 | Ritual de Fechamento | ✅ Existe | 🟢 Alinhado |
| 9 | Por que Importa | ✅ Existe | 🟢 Alinhado |
| 10 | Sugestões | ✅ Existe | 🟡 L001 usa Guardiões, não Bruner |
| 11 | Auditoria CM | ✅ Existe | 🟢 Alinhado |

---

## 🔄 Mudanças Necessárias no Template

### 1. Frontmatter — Adicionar campos DEFINITION_OF_DONE

```yaml
# ATUAL
clima: "[...]"
local: "[...]"
virtude: "[...]"
artefato: "[...]"
link_anterior: "MV-S-XXX"
link_proximo: "MV-S-XXX"

# ADICIONAR (conforme DEFINITION_OF_DONE)
elo_anterior: "[Gancho narrativo da lição anterior]"
proximo_passo: "[Gancho para próxima lição]"
```

### 2. Bancada — Adicionar seção "Para Enriquecer"

```markdown
### Para Enriquecer (Opcional)

> [!TIP]
> **Quer deixar mais especial?** Estas ideias são opcionais.

- 🕯️ **Vela acesa** — Continuidade do ritual
- 🟢 **Tapete verde** — Marcar o espaço sagrado
- [...]
```

### 3. Áudio-Script → Dica para o Portador

```markdown
# ANTES (Template)
## 🎧 Áudio-Script (Somente para o Pai)

# DEPOIS (L001)
## 💡 Dica para o Portador
*Leia para si mesmo antes de chamar seu filho:*
```

### 4. Narração — Renomear "Sondas de Sabedoria"

```markdown
# ANTES (Template)
**Sondas de Sabedoria (use 1 ou 2):**

# DEPOIS (L001)
**Perguntas do Coração (use 1 ou 2):**
```

### 5. Sugestões — Usar Guardiões, não teóricos

```markdown
# ANTES (Template)
### 📐 Bruner (CPA)

# DEPOIS (L001)
### 🦁 Melquior (Sabedoria)
```

### 6. Clima — Integrar na narrativa com emoji

```markdown
☀️ *O sol da manhã atravessa as folhas...*
```

---

## ✅ Checklist de Ações

### Template V4.1 → V4.2

- [ ] Adicionar `elo_anterior` e `proximo_passo` ao frontmatter
- [ ] Renomear "Áudio-Script" → "Dica para o Portador"
- [ ] Adicionar seção "Para Enriquecer (Opcional)" na Bancada
- [ ] Renomear "Sondas de Sabedoria" → "Perguntas do Coração"
- [ ] Substituir "Bruner" por guardião nas Sugestões
- [ ] Adicionar instruções para integrar Clima na narrativa com emoji

### DEFINITION_OF_DONE

- [ ] Verificar se precisa atualização

---

*Próximo passo: Executar atualizações no template*
