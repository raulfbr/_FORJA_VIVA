# PROMPT MESTRE PARA LOVABLE.DEV (MATEMÁTICA VIVA)

> **Instrução para o Usuário:** Copie TODO o conteúdo abaixo e cole na caixa de diálogo do [Lovable.dev](https://lovable.dev/).

---

**ROLE:**
Atue como um **Senior Frontend Engineer** e **Editorial Designer** especialista em interfaces que misturam "Old School Academia" com "Modern Web Performance".

**PROJECT GOAL:**
Criar o dashboard educacional "Matemática Viva". Não é um LMS genérico; é uma "Biblioteca Digital Clássica". A estética deve ser **Editorial, Premium, Minimalista e Calma**. Pense em: Tinta verde sobre papel creme, tipografia serifada elegante, respiro e silêncio visual.

---

### 1. DESIGN SYSTEM & TAILWIND CONFIG
Por favor, configure o `tailwind.config.js` estritamente com estes valores. Não invente cores fora desta paleta.

**Colors (Extend Theme):**
*   `paper`: '#F8F5E9' (Fundo Principal - Creme Quente)
*   `paper-dark`: '#EDE8D5' (Camada Secundária/Cards)
*   `ink`: '#304837' (Texto Principal/Verde Floresta)
*   `ink-light`: '#4A6B50' (Texto Secundário/Hover)
*   `gold`: '#B89B5E' (Destaques/Botões)
*   `gold-light`: '#D4B87A' (Gold Hover)

**Typography (Google Fonts):**
Importe estas fontes no `index.html`:
`<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">`

*   `font-serif`: ['Libre Baskerville', 'serif'] (Para Títulos e Citações)
*   `font-sans`: ['Outfit', 'sans-serif'] (Para UI, Menus e Texto Corrido)

**Border Radius:**
*   Use `rounded-sm` ou `rounded-md`. Evite `rounded-xl` ou `full` (exceto botões pill). Queremos um visual mais "papelaria" e menos "app tech".

---

### 2. LAYOUT & ATMOSPHERE

**Background Strategy (The "Paper" Feel):**
*   **Base:** `bg-paper`.
*   **Texture:** Create a pseudo-element `fixed inset-0 pointer-events-none opacity-[0.03] mix-blend-multiply` with a `background-image` using a simple SVG noise pattern. *Goal: Eliminate the "digital flatness".*

**Navigation (Responsive):**
*   **Desktop:** Sidebar lateral elegante (`w-64`, `border-r border-ink/10`).
*   **Mobile (Critical):** Use uma **Bottom Navigation Bar** (`fixed bottom-0 w-full bg-paper border-t border-ink/10`).
    *   Reasons: Mothers use the app with one hand while holding a baby. Menu must be reachable by thumb.
*   **Items:** Home, Currículo, Diário, Perfil.
*   **Active State:** Ícone preenchido ou com `text-gold`.

---

### 3. MAIN VIEWS TO GENERATE

#### A. The Dashboard (Home)
*   **Hero Section:** Um cumprimento calmo. "Bem-vindo à Ordem, [Nome]".
*   **Quote do Dia:** Um card com `font-serif italic`, borda esquerda `border-l-4 border-gold`, fundo `bg-paper-dark`.
*   **Progresso Visual:** Não use barras de progresso verdes "neon". Use uma linha fina `bg-ink/10` com o preenchimento em `bg-gold`.
*   **Trilha Atual:** Card mostrando o módulo atual ("Sementes" ou "Raízes").

#### B. The Curriculum Grid (Modules)
Mostre os ciclos como "Livros" ou "Cards Elegantes".
*   **Sementes (4-6 anos):** Ícone de uma semente ou broto.
*   **Raízes (7-10 anos):** Ícone de uma árvore robusta.

**Card Style (Base):**
*   Borda fina: `border border-ink/10`.
*   Hover: `border-gold` e leve `shadow-sm`.
*   Tipografia: Título em Serif, descrição em Sans leve.

**Guardian Themes (Character Injection):**
Implemente utility classes para os personagens (apenas para bordas sutis ou tags):
*   `guardian-noe`: `#7B68B8` (Purple)
*   `guardian-celeste`: `#E8A87C` (Orange)
*   *Use dynamic borders:* `hover:border-[#7B68B8]` para items do Noé.

#### C. The Lesson View (O Leitor)
Esta é a tela mais importante. Onde a criança/pai lê a lição.
*   **Container:** Largura de leitura otimizada (max-w-prose ou max-w-3xl) centralizada.
*   **Typography:** Tamanho de fonte confortável (`text-lg` ou `text-[18px]`). Leading relaxado (`leading-relaxed`).
*   **Elementos Pedagógicos:**
    *   **Caixa de Material:** Um box com fundo `bg-paper-dark` listando o que precisa (Feijões, Lápis).
    *   **Ação:** Botões de "Próximo" devem ser `bg-ink` text `text-paper` hover `bg-ink-light`.

---

### 4. BEHAVIOR RULES
*   **Mobile First:** Tudo deve funcionar perfeitamente no celular (stack vertical).
*   **No "Flashy" Animations:** Use transições suaves (`duration-300 ease-in-out`), nada de pulos ou zooms exagerados.
*   **Tone:** O site deve parecer que você está entrando em uma biblioteca de madeira nobre, não em uma startup do Vale do Silício.

**Executar.**
