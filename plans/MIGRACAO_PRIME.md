# 🗺️ Plano de Migração: Padrão "Prime" (Visual & Engenharia)

Este documento detalha o plano para atualizar o pipeline de geração de lições (`build_lessons.py`) para produzir automaticamente o HTML "Prime" (`001_VER_C_PRIME.html`), aprovado como o novo padrão visual.

## 1. O Padrão "Prime" (Target)
O objetivo é alcançar a seguinte estrutura visual sem intervenção manual:
- **Scene Cards:** Cada seção lógica (Preparação, Jornada, Cena, Concreto) é encapsulada em um card branco com borda arredondada (12px), sombra suave e linha de acento dourada.
- **Iconografia Semântica:** Uso de ícones específicos para seções (ex: 🛡️ para Impecabilidade, 🧱 para Concreto) injetados automaticamente.
- **Foco no Portador:** Estilização específica (borda verde esquerda) para falas do Portador.
- **Centralização Visual:** Imagens de "Visualizar" centralizadas e destacadas.

## 2. Análise de Gap (YAML vs HTML)

| Componente | YAML Atual (`001_TRINDADE_PALMA.yaml`) | HTML "Prime" Desejado | Ação Necessária na Engenharia |
| :--- | :--- | :--- | :--- |
| **Scene Wrapper** | Chaves soltas (`cena_1`, `cena_2`) | `<div class="scene-card">` | **Agrupamento:** O Builder deve envolver cada item da `narrativa_principal` em um container Card. |
| **Ícones** | Texto puro ou emoji hardcoded | `<strong>🛡️ Título:</strong>` | **Injeção:** `ICON_MAP` em constante global no Builder. |
| **Portador** | `fala_portador` | `.portador-block` (Green Border) | **CSS Class:** Lógica `is_portador` na função `render_rich_content`. |
| **Visualizar** | `card_guardiao: "[CARD: X]"` | Bloco centralizado com imagem | **Regex:** `r'\[CARD:\s*(.*?)\]'` -> Renderiza template `centered_viz`. |
| **CSS** | `style.css` genérico | Variáveis CSS Prime (`--radius-md`) | **Refatoração:** Portar do HTML para `style.css`. Usar variáveis CSS. |

## 3. Plano de Ação por Expert

### 🎨 Design Expert (`design.yaml`)
Atualizar a definição de "Visual Language" para incluir o **Prime Design System**:
- **Border Radius:** 12px (padrão).
- **Shadows:** `0 4px 6px -1px rgba(0,0,0,0.05)`.
- **Accent:** Gold Gradient (`linear-gradient(90deg, #FCD34D 0%, #F59E0B 100%)`).
- **Icons:** Padronizar o set de ícones (Shield, Dove, Compass, Thread).

### ⚙️ Engenharia Expert (`build_lessons.py`)
Refatorar `render_recursive` e `format_content` para:
1.  **Card-ify:** Criar função `render_scene_card(title, content_dict)` que encapsula conteúdo no HTML `<div class="scene-card">`.
2.  **Icon Map Global:**
    ```python
    ICON_MAP = {
        'protocolo_impecabilidade': '🛡️',
        'nota_de_graca': '🕊️',
        'norte_absoluto': '🧭',
        'fio_de_ouro': '🧵',
        'transicao': '🌫️',
        'abertura_sensorial': '👁️',
        'local': '📍',
        'instrucao': '👉',
        'dica': '💡'
    }
    ```
3.  **Portador Logic:** Na função `render_rich_content`, se `key` contém "portador", adicionar classe `portador-block`.
4.  **Center Viz:** Implementar parser regex robusto para `[CARD: Nome]` que busca imagem em `assets/cards/guardioes/`.

### 🚓 QA & Orchestrator
1.  **Validar L001:** Gerar L001 via script e comparar *pixel-perfect* com `001_VER_C_PRIME.html`.
2.  **Regressão:** Garantir que L000 (O Portal) também seja gerada corretamente no novo padrão.

## 4. Próximos Passos (Execução)
1.  [ ] **CSS Migration:** Mover estilos de Prime para `style.css`.
2.  [ ] **Builder Upgrade:** Atualizar `build_lessons.py` com a lógica "Prime".
3.  [ ] **Test Run:** Gerar `site/sementes/001_TRINDADE_PALMA.html` automaticamente.
4.  [ ] **Validation:** Comparar com `site/TESTE/001_VER_C_PRIME.html`.

---
**Status:** Pronto para iniciar execução.
**Aprovação do Usuário:** Requerida para iniciar refatoração de código.
