# 🔨 Pipeline Gutenberg Forja

Conversão de lições Markdown para HTML renderizado.

## Estrutura

```
forja-core/pipeline/
├── gutenberg_forja.py   # Script principal
├── style.css            # Estilos das lições
├── base_template.html   # Template HTML (opcional)
└── README.md            # Este arquivo
```

## Uso

```bash
# Converter todas as lições de Sementes
python gutenberg_forja.py --input curriculo/01_SEMENTES/ --output site/sementes/

# Com template customizado
python gutenberg_forja.py -i curriculo/01_SEMENTES/ -o site/sementes/ -t meu_template.html
```

## Features

- ✅ Parse de frontmatter YAML
- ✅ Conversão de admonitions GitHub
- ✅ Cards de Guardiões com imagens
- ✅ Climas com backgrounds dinâmicos
- ✅ Navegação anterior/próximo
- ✅ CSS Glassmorphism
- ✅ Responsivo e imprimível

## Guardiões Suportados

| Card | Emoji | Cor |
|------|-------|-----|
| `[CARD: MELQUIOR]` | 🦁 | Gold |
| `[CARD: NOE]` | 🦉 | Terra |
| `[CARD: CELESTE]` | 🦊 | Laranja |
| `[CARD: BERNARDO]` | 🐻 | Marrom |
| `[CARD: IRIS]` | 🐦 | Roxo |

## Climas

| Clima | Emoji | Background |
|-------|-------|------------|
| Ensolarado | ☀️ | Dourado |
| Nublado | ☁️ | Cinza |
| Chuvoso | 🌧️ | Azul |
| Crepúsculo | 🌅 | Rosa |

---

*Pipeline v1.0.0 — Forja Viva*
