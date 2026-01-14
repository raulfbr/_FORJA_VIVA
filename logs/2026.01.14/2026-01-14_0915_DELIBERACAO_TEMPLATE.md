# 🏛️ Deliberação do Orchestrator — Template de Lições

**Data:** 14/01/2026  
**Modo:** REUNIAO (deliberação multi-expert)  
**Tema:** Como criar lições padronizadas mas únicas?

---

## 🎯 Decisão do Maestro

### O Problema
- **Padronização** garante qualidade e previsibilidade
- **Unicidade** garante que cada lição seja uma experiência viva

### Solução: Template Esqueleto + Expressões Únicas

```
TEMPLATE (fixo)     +    EXPRESSÕES (variáveis)
─────────────────        ─────────────────────
• Estrutura 13 seções    • Clima (Ensolarado/Chuvoso...)
• Ordem CPA              • Local (Jardim/Caverna...)
• Rituais abertura/      • Guardião líder
  fechamento             • Ideia Viva única
• Narração obrigatória   • Atmosfera sensorial
• Tempo ≤20min           • Virtude trabalhada
```

---

## 📋 Ação: Mover Template para .bmad/templates

O template do legado (`template-v4.1-sementes.yaml`) será movido e renomeado:

```
_LEGADO/forja-core_modelos_ARCHIVED_2026-01-13/template-v4.1-sementes.yaml
                     ↓
.bmad/templates/00_K_sementes/licao-template.yaml
```

---

## 🌱 Criar L001 de Teste

Usando o workflow `criar-licao-premium`:
- **Tema:** A Trindade na Palma (contar 1, 2, 3)
- **Guardião:** Celeste (Curiosidade)
- **Clima:** Ensolarado
- **Virtude:** Curiosidade

---

## ✅ Próximos Passos

1. [x] Mover template para estrutura ativa
2. [ ] Criar L001 baseada no template
3. [ ] Gerar PDF de L001
4. [ ] Validar pipeline completo
