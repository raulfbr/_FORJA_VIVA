"""
🔨 DASHBOARD BUILDER V3 (Orchestrator Aligned)
==============================================
Gera um index.html com estética MatViva Premium.
Alinhamento: North Star (Qualidade Impecável) + Orchestrator (Distinção Papéis).
"""

import os
import yaml
from pathlib import Path
from datetime import datetime

# CONFIGURAÇÃO
INPUT_DIR_SEMENTES = Path("curriculo/01_SEMENTES")
OUTPUT_DIR = Path("site")
OUTPUT_HTML = OUTPUT_DIR / "index.html"

# CORES & ESTILO (Palette North Star)
# CORES & ESTILO (Palette North Star - Potter/Morris/TocaBoca)
STYLE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Lora:ital,wght@0,400;0,600;1,400&family=Gloria+Hallelujah&display=swap');

:root {
    /* Palette Beatrix Potter (Organic & Earthy) */
    --bg-page: #FDF5E6; /* Warm Cream - Creme Quente */
    --bg-card: #FFFFFF;
    
    /* Brand Colors */
    --primary: #2A5A3F; /* Forest Green - Mata Viva */
    --primary-light: #D1FAE5;
    --accent-gold: #BFA265; /* Old Gold - Nobreza */
    --text-primary: #1C1917; /* Stone 900 */
    --text-secondary: #44403C; /* Stone 700 */
    --text-tertiary: #A8A29E; /* Stone 400 */
    
    /* Guardians (Vibrant yet Natural) */
    --g-melquior: #D97706;
    --g-celeste: #EA580C;
    --g-bernardo: #78350F;
    --g-noe: #4338CA;
    --g-iris: #DB2777;
    
    /* Typography */
    --font-heading: 'Lora', serif;
    --font-body: 'Outfit', sans-serif; /* Toca Boca Style: Clean & Round */
    --font-hand: 'Gloria Hallelujah', cursive; /* Toque Humano */
    
    /* UI Toca Boca (Round & Friendly) */
    --radius-sm: 12px;
    --radius-md: 24px;
    --radius-lg: 32px;
    --shadow-soft: 0 10px 40px -10px rgba(0,0,0,0.08);
    --shadow-hover: 0 20px 50px -12px rgba(0,0,0,0.15);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body { 
    font-family: var(--font-body); 
    background: var(--bg-page); 
    color: var(--text-primary); 
    display: flex; 
    min-height: 100vh;
    overflow-x: hidden;
}

/* SIDEBAR REFINADA */
.sidebar {
    width: 280px; 
    background: #FFFCF5; /* Lighter Cream */
    border-right: 1px solid rgba(0,0,0,0.05); 
    padding: 2.5rem 2rem; 
    position: fixed; 
    height: 100vh; 
    overflow-y: auto;
    z-index: 50;
    box-shadow: 2px 0 20px rgba(0,0,0,0.02);
}

.brand { 
    font-family: var(--font-heading);
    font-size: 1.4rem; 
    font-weight: 700; 
    color: var(--primary); 
    margin-bottom: 3rem; 
    display: flex; 
    align-items: center; 
    gap: 0.75rem; 
}

.nav-section {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent-gold);
    margin-top: 2.5rem;
    margin-bottom: 1rem;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 1.25rem;
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s ease;
    margin-bottom: 0.5rem;
}
.nav-link:hover { background: #FFFFFF; color: var(--primary); transform: translateX(4px); box-shadow: var(--shadow-soft); }
.nav-link.active { background: var(--primary-light); color: var(--primary); font-weight: 700; }

/* MAIN CONTENT */
.main-content { margin-left: 280px; padding: 4rem 5rem; width: 100%; max-width: 1600px; }

header { margin-bottom: 5rem; }
.role-badge { 
    display: inline-flex; align-items: center; justify-content: center;
    padding: 0.5rem 1rem; 
    background: #E0E7FF; color: #3730A3; 
    border-radius: 99px; 
    font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
    margin-bottom: 1.5rem;
}

h1 { font-family: var(--font-heading); font-size: 3rem; font-weight: 600; margin-bottom: 1rem; color: #292524; letter-spacing: -0.02em; }
.subtitle { font-family: var(--font-body); font-size: 1.2rem; color: var(--text-secondary); max-width: 650px; line-height: 1.6; }

/* STATS (Pill Style) */
.stats { display: flex; gap: 2rem; margin-bottom: 4rem; }
.stat-card { 
    background: #FFFFFF; padding: 1.5rem 2rem; 
    border-radius: var(--radius-md); 
    box-shadow: var(--shadow-soft); 
    display: flex; flex-direction: column; 
    min-width: 200px;
}
.stat-val { font-size: 2.5rem; font-weight: 700; color: var(--primary); font-family: var(--font-heading); line-height: 1; margin-bottom: 0.25rem; }
.stat-label { font-size: 0.9rem; color: var(--text-tertiary); font-weight: 500; }

/* CARDS - TOCA BOCA STYLE (Rounder, Friendlier) */
.section-header { margin-bottom: 2.5rem; display: flex; align-items: baseline; justify-content: space-between; padding-bottom: 1rem; border-bottom: 2px dashed rgba(0,0,0,0.05); }
.section-title { font-family: var(--font-heading); font-size: 2rem; color: var(--text-primary); }

.grid-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2.5rem; }

.card { 
    background: var(--bg-card); 
    border-radius: var(--radius-lg); /* 32px - Bem Redondo */
    border: 1px solid rgba(0,0,0,0.03);
    box-shadow: var(--shadow-soft);
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); /* Bouncy Spring */
    display: flex; flex-direction: column;
    overflow: hidden;
    position: relative;
    height: 100%;
}
.card:hover { transform: translateY(-8px) scale(1.02); box-shadow: var(--shadow-hover); }

/* Decorative Top Bar */
.card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 8px; background: #E5E7EB; }
.card.melquior::before { background: var(--g-melquior); }
.card.celeste::before { background: var(--g-celeste); }
.card.bernardo::before { background: var(--g-bernardo); }
.card.noe::before { background: var(--g-noe); }
.card.iris::before { background: var(--g-iris); }

.card-body { padding: 2rem; flex-grow: 1; display: flex; flex-direction: column; }

.card-meta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
.card-id { 
    font-size: 0.7rem; font-weight: 800; color: var(--accent-gold); 
    background: #FEF9C3; padding: 0.4rem 0.8rem; border-radius: 99px;
    letter-spacing: 0.05em; text-transform: uppercase; 
}
.guardian-icon-img { width: 56px; height: 56px; object-fit: contain; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1)); transition: transform 0.3s; }
.card:hover .guardian-icon-img { transform: scale(1.1) rotate(5deg); }

.card-title { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; line-height: 1.25; color: var(--text-primary); }
.card-desc { font-size: 1rem; color: var(--text-secondary); line-height: 1.6; font-style: normal; margin-bottom: 2rem; flex-grow: 1; opacity: 0.9; }

.card-footer { padding: 1.5rem 2rem; background: #FAFAF9; border-top: 1px solid rgba(0,0,0,0.02); text-align: right; }
.btn-arr { 
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: var(--primary); color: white; 
    padding: 0.75rem 1.5rem; border-radius: 99px;
    font-weight: 600; text-decoration: none; font-size: 0.95rem;
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(4, 120, 87, 0.2);
}
.btn-arr:hover { background: #065F46; padding-right: 2rem; }


/* BLOG PLACEHOLDER */
.blog-empty { 
    background: #F9FAFB; 
    border: 2px dashed #E5E7EB; 
    border-radius: 1rem; 
    padding: 3rem; 
    text-align: center;
}
.blog-empty h3 { color: #374151; margin-bottom: 0.5rem; font-weight: 600; }
.blog-empty p { color: #6B7280; font-size: 0.9rem; max-width: 400px; margin: 0 auto; }

@media (max-width: 1024px) {
    .sidebar { display: none; }
    .main-content { margin-left: 0; padding: 2rem; }
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matemática Viva | Orchestrator Dashboard</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <nav class="sidebar">
        <div class="brand">
            <img src="assets/cards/guardioes/melquior-leao.png" alt="Logo" style="width: 32px; height: 32px;"> Matemática Viva
        </div>
        
        <div class="nav-section">Reino Contado</div>
        <a href="#sementes" class="nav-link active"><span>🌱</span> Ciclo Sementes</a>
        <a href="#" class="nav-link"><span>🌳</span> Ciclo Raízes <small>(Em breve)</small></a>
        
        <div class="nav-section">Acervo Público</div>
        <a href="#blog" class="nav-link"><span>📝</span> Artigos & Ensaios</a>
        <a href="#" class="nav-link"><span>📚</span> Biblioteca Pedagogia</a>
        
        <div class="nav-section">Sistema (Orchestrator)</div>
        <a href="#" class="nav-link"><span>⚙️</span> Configurações</a>
        <a href="#" class="nav-link"><span>📊</span> Analytics</a>
    </nav>

    <main class="main-content">
        <header>
            <div class="role-badge">Admin: Maestro Raul</div>
            <h1>Visão Geral do Reino</h1>
            <p class="subtitle">O progresso da Matemática Viva, monitorado pelo Orchestrator. Aqui a "Qualidade Não é Negociável" se torna visível.</p>
        </header>

        <section class="stats">
            <div class="stat-card">
                <div class="stat-val">{{TOTAL_SEMENTES}}</div>
                <div class="stat-label">Lições Sementes Produzidas</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">100%</div>
                <div class="stat-label">Conformidade North Star</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">Production</div>
                <div class="stat-label">Ambiente Atual</div>
            </div>
        </section>

        <section id="sementes" class="mb-16">
            <div class="section-header">
                <div class="section-title"><span>🌱</span> Ciclo Sementes</div>
                <div class="section-meta">Estação 1: A Fundação • Build: {{DATA}}</div>
            </div>
            
            <div class="grid-cards">
                {{CARDS_SEMENTES}}
            </div>
        </section>

        <section id="blog" style="margin-top: 6rem;">
            <div class="section-header">
                <div class="section-title"><span>📝</span> Blog & Ensaios</div>
                <div class="section-meta">Base de Conhecimento</div>
            </div>
            
            <div class="blog-empty">
                <h3>O sistema de blog está sendo forjado.</h3>
                <p>Em breve, artigos sobre Método CPA, Charlotte Mason e a visão da Matemática Viva estarão disponíveis aqui para o público.</p>
            </div>
        </section>
        
        <footer style="margin-top: 6rem; border-top: 1px solid #E5E7EB; padding-top: 2rem; color: #9CA3AF; font-size: 0.875rem; display: flex; justify-content: space-between;">
            <div>&copy; 2026 Matemática Viva. Built by Orchestrator.</div>
            <div>Versão 1.5.0 (Vercel)</div>
        </footer>
    </main>
</body>
</html>
"""

def get_guardian_data(name):
    name = name.lower()
    if 'celeste' in name: return 'celeste', 'assets/cards/guardioes/celeste-raposa.png'
    if 'bernardo' in name: return 'bernardo', 'assets/cards/guardioes/bernardo-urso.png'
    if 'noé' in name or 'noe' in name: return 'noe', 'assets/cards/guardioes/noe-coruja.png'
    if 'íris' in name or 'iris' in name: return 'iris', 'assets/cards/guardioes/iris-passarinho.png'
    return 'melquior', 'assets/cards/guardioes/melquior-leao.png'

def build_lesson_card(file_path):
    try:
        content = file_path.read_text(encoding='utf-8')
        data = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2: data = yaml.safe_load(parts[1])
        else:
            data = yaml.safe_load(content)
        
        # Extração
        meta = data.get('licao', {}).get('metadados', {}) if 'licao' in data else data
        ideia = data.get('licao', {}).get('ideia_viva', {}).get('frase', '') if 'licao' in data else data.get('ideia_viva', {}).get('frase', '')
        
        lid = meta.get('id', 'MV-S-XXX')
        titulo = meta.get('titulo', 'Sem Título')
        guardiao = meta.get('guardiao_lider', 'Melquior')
        tipo = meta.get('tipo', 'Lição').upper()
        
        if not ideia: ideia = "O mistério dos números aguarda..."
        
        link = f"sementes/{file_path.stem}.html"
        css_class, img_path = get_guardian_data(guardiao)
        
        return f"""
        <article class="card {css_class}">
            <div class="card-body">
                <div class="card-meta">
                    <span class="card-id">{tipo}</span>
                    <img src="{img_path}" class="guardian-icon-img" alt="{guardiao}" title="{guardiao}">
                </div>
                <h3 class="card-title">{titulo}</h3>
                <p class="card-desc">“{ideia}”</p>
            </div>
            <div class="card-footer">
                <a href="{link}" class="btn-arr">Abrir Lição <span>→</span></a>
            </div>
        </article>
        """
    except Exception as e:
        print(f"❌ Erro em {file_path.name}: {e}")
        return ""

def main():
    print("🥁 Orchestrator: Refinando Dashboard V3...")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 0. ASSETS SYNC (Orchestrator Infra)
    import shutil
    CARDS_SRC = Path("docs/cards/web")
    CARDS_DEST = OUTPUT_DIR / "assets/cards"
    
    if CARDS_SRC.exists():
        print(f"   ↳ Sincronizando Assets ({len(list(CARDS_SRC.glob('*')))} files)...")
        # Overwrite assets safely (Windows Friendly)
        try:
            shutil.copytree(CARDS_SRC, CARDS_DEST, dirs_exist_ok=True)
        except Exception as e:
            print(f"   ⚠️ Aviso ao copiar assets: {e}")
    else:
        print("   ⚠️ AVISO: docs/cards/web não encontrado.")

    # 1. BUILD DAS LIÇÕES (Integração Vercel)
    # Garante que as páginas HTML existam antes de criar os links
    print("   ↳ Disparando Build de Lições...")
    import build_lessons
    build_lessons.main()
    
    # Gerar CSS
    (OUTPUT_DIR / "style.css").write_text(STYLE_CSS, encoding='utf-8')
    
    # Processar Cards
    cards = []
    if INPUT_DIR_SEMENTES.exists():
        files = sorted(list(INPUT_DIR_SEMENTES.glob("*.yaml")))
        for f in files:
            c = build_lesson_card(f)
            if c: cards.append(c)
    
    # Montar HTML
    html = HTML_TEMPLATE.replace("{{CARDS_SEMENTES}}", "\n".join(cards))
    html = html.replace("{{TOTAL_SEMENTES}}", str(len(cards)))
    html = html.replace("{{DATA}}", datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    OUTPUT_HTML.write_text(html, encoding='utf-8')
    print(f"✨ Dashboard Impecável gerado em: {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
