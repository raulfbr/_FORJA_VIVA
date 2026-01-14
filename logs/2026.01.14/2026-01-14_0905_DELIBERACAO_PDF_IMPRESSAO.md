# 📐 Deliberação do Conselho de Design — PDF para Impressão Caseira

**Data:** 14/01/2026  
**Tema:** Otimização do PDF para pais imprimirem em A4 com encadernação espiral

---

## 🎯 Requisitos do Usuário

1. **Impressão A4** — Formato padrão
2. **Mínimo de tinta** — Economia para famílias
3. **Espiral no lado esquerdo** — Margem de encadernação

---

## 📊 Pesquisa Externa — Margens para Espiral

| Borda | Recomendação | Fonte |
|-------|--------------|-------|
| **Esquerda (binding)** | 18-22mm | Book Printing UK, Vervante |
| **Topo** | 15mm | Padrão |
| **Direita** | 10-15mm | Aproveitamento |
| **Inferior** | 15mm | Padrão |

> **Nota:** Os furos da espiral ocupam ~10mm. Deixar 18-22mm garante que texto não seja perfurado.

---

## 👥 Posições dos Especialistas

### 🎨 Beatrix Potter (Estética)
> "Brancos e pretos. Sem gradientes. Ilustrações com linhas finas economizam tinta. Os ícones devem ser outline, não preenchidos."

**Veredito:** ✅ Aprovado (fundo branco já está OK)

---

### 📐 William Morris (Tipografia)
> "Margem esquerda generosa é funcional E elegante. 2cm (20mm) no binding edge. Tipografia preta 100% — nada de cinza claro que força a impressora."

**Recomendação:**
- Margem esquerda: **2cm** (binding)
- Cor do texto: **#000** (preto puro) em vez de #222

---

### 🧸 Toca Boca (UX Família)
> "Pais vão furar em casa, provavelmente com furador de 2 furos comum. Os furos ficam a ~1.5cm da borda. Deixar 2cm é seguro."

**Recomendação:**
- Header pode ter numeração no canto superior direito (não esquerdo)
- Evitar informações importantes na área de furo

---

### 📊 Edward Tufte (Clareza)
> "Data-ink ratio: cada gota de tinta deve comunicar. Remover:
> - Linhas decorativas desnecessárias
> - Ícones preenchidos → usar outline
> - Bordas de caixas → usar apenas borda esquerda"

**Recomendação:**
- Reduzir espessura de linhas para 0.25pt
- Ícones como emoji são OK (não consomem tinta)

---

## ✅ Síntese — Configurações Recomendadas

```python
CONFIG = {
    "PAGE_FORMAT": "A4",
    "MARGIN_TOP": "1.5cm",      # Padrão
    "MARGIN_BOTTOM": "1.5cm",   # Padrão  
    "MARGIN_LEFT": "2cm",       # BINDING - Espiral
    "MARGIN_RIGHT": "1cm",      # Aproveitamento
}
```

### CSS Ajustes

```css
body { color: #000; }  /* Preto puro */
.header { border-bottom: 0.25pt solid #999; }  /* Linha fina */
h2 { border-bottom: 0.25pt solid #bbb; }
```

### Posição da Numeração

| Local | Antes | Depois |
|-------|-------|--------|
| Numeração página | Centro inferior | **Superior direito** |

---

## 🗳️ Decisão CM (Charlotte Mason)

> "O design serve à família. Se os pais vão furar à esquerda, nossa margem deve acomodar isso. A simplicidade é virtude — menos tinta, mais clareza."

**Decisão Final:**
- ✅ Margem esquerda: 2cm
- ✅ Texto preto puro #000
- ✅ Linhas 0.25pt
- ✅ Numeração no canto superior direito
