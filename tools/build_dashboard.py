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
STYLE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

:root {
    /* Foundation */
    --bg-page: #F3F4F6;
    --bg-sidebar: #FFFFFF;
    --bg-card: #FFFFFF;
    
    /* Typography */
    --font-heading: 'Lora', serif;
    --font-body: 'Inter', sans-serif;
    --text-primary: #111827;
    --text-secondary: #4B5563;
    --text-tertiary: #9CA3AF;
    
    /* Brand Accent */
    --primary: #047857; /* Verde Forja */
    --primary-light: #D1FAE5;
    
    /* Guardians (LORE) */
    --g-melquior: #D97706; /* Amber 600 */
    --g-celeste: #EA580C; /* Orange 600 */
    --g-bernardo: #78350F; /* Brown 900 */
    --g-noe: #4338CA; /* Indigo 700 */
    --g-iris: #DB2777; /* Pink 600 */
    
    /* UI Elevations */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
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

/* SIDEBAR - Distinção Técnico vs Narrativo */
.sidebar {
    width: 280px; 
    background: var(--bg-sidebar); 
    border-right: 1px solid #E5E7EB; 
    padding: 2rem; 
    position: fixed; 
    height: 100vh; 
    overflow-y: auto;
    z-index: 50;
}

.brand { 
    font-family: var(--font-heading);
    font-size: 1.5rem; 
    font-weight: 700; 
    color: var(--primary); 
    margin-bottom: 2.5rem; 
    display: flex; 
    align-items: center; 
    gap: 0.5rem; 
    letter-spacing: -0.02em;
}

.nav-section {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-tertiary);
    font-weight: 600;
    margin-top: 2rem;
    margin-bottom: 0.75rem;
}

.nav-item { margin-bottom: 0.25rem; }

.nav-link {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s ease;
}

.nav-link:hover { background: #F9FAFB; color: var(--text-primary); }
.nav-link.active { background: var(--primary-light); color: var(--primary); font-weight: 600; }

/* MAIN AREA */
.main-content { margin-left: 280px; padding: 3rem 4rem; width: 100%; max-width: 1600px; }

header { margin-bottom: 4rem; }
.role-badge { 
    display: inline-block; 
    padding: 0.25rem 0.75rem; 
    background: #E0E7FF; 
    color: #3730A3; 
    border-radius: 999px; 
    font-size: 0.75rem; 
    font-weight: 600; 
    margin-bottom: 1rem;
}

h1 { font-family: var(--font-heading); font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; color: #111827; }
.subtitle { color: var(--text-secondary); font-size: 1.125rem; line-height: 1.6; max-width: 600px; }

/* STATS CARDS */
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-bottom: 4rem; }
.stat-card { background: white; padding: 1.5rem; border-radius: 1rem; box-shadow: var(--shadow-sm); border: 1px solid #F3F4F6; }
.stat-val { font-size: 2rem; font-weight: 800; color: #111827; line-height: 1; margin-bottom: 0.5rem; }
.stat-label { font-size: 0.875rem; color: var(--text-secondary); }

/* SECTIONS */
.section-header { margin-bottom: 2rem; display: flex; align-items: baseline; justify-content: space-between; border-bottom: 1px solid #E5E7EB; padding-bottom: 1rem; }
.section-title { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 600; color: #111827; display: flex; align-items: center; gap: 0.75rem; }
.section-meta { font-size: 0.875rem; color: #9CA3AF; }

/* GRID SYSTEMS */
.grid-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2rem; }

/* CARD DESIGN */
.card { 
    background: var(--bg-card); 
    border-radius: 1rem; 
    border: 1px solid #E5E7EB;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    height: 100%;
}
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: #D1D5DB; }

/* Guardian Color Stripes */
.card.melquior { border-top: 4px solid var(--g-melquior); }
.card.celeste { border-top: 4px solid var(--g-celeste); }
.card.bernardo { border-top: 4px solid var(--g-bernardo); }
.card.noe { border-top: 4px solid var(--g-noe); }
.card.iris { border-top: 4px solid var(--g-iris); }

.card-body { padding: 1.5rem; flex-grow: 1; display: flex; flex-direction: column; }

.card-meta { display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem; }
.card-id { font-size: 0.75rem; font-weight: 700; color: #9CA3AF; letter-spacing: 0.05em; text-transform: uppercase; }
.guardian-icon { font-size: 1.5rem; line-height: 1; }
.guardian-icon-img { width: 48px; height: 48px; object-fit: contain; }

.card-title { font-family: var(--font-heading); font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem; line-height: 1.3; color: #111827; }
.card-desc { font-size: 0.95rem; color: #4B5563; line-height: 1.5; font-style: italic; margin-bottom: 1.5rem; flex-grow: 1; }

.card-footer { padding: 1rem 1.5rem; background: #F9FAFB; border-top: 1px solid #F3F4F6; display: flex; justify-content: flex-end; }
.btn-arr { color: var(--primary); font-weight: 600; font-size: 0.9rem; text-decoration: none; display: flex; align-items: center; gap: 0.25rem; transition: gap 0.2s; }
.btn-arr:hover { gap: 0.5rem; }

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
        if CARDS_DEST.exists(): shutil.rmtree(CARDS_DEST)
        shutil.copytree(CARDS_SRC, CARDS_DEST)
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
