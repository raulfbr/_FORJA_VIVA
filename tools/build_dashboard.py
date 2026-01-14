"""
🔨 DASHBOARD BUILDER V2 (Premium)
=================================
Gera um index.html com estética MatViva Premium (Glassmorphism, Sidebar, Grid).
Integra visão do Currículo Sementes e prepara terreno para o Blog.
"""

import os
import yaml
from pathlib import Path
from datetime import datetime

# CONFIGURAÇÃO
INPUT_DIR_SEMENTES = Path("curriculo/01_SEMENTES")
OUTPUT_DIR = Path("site")
OUTPUT_HTML = OUTPUT_DIR / "index.html"

# CORES & ESTILO
STYLE_CSS = """
:root {
    --bg-color: #F8F9FA;
    --sidebar-bg: #FFFFFF;
    --text-primary: #1F2937;
    --text-secondary: #6B7280;
    --accent-color: #2F855A;  /* Verde MatViva */
    --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    
    /* Guardiões */
    --color-melquior: #D4A017;
    --color-celeste: #FF6B35;
    --color-bernardo: #8B4513;
    --color-noe: #483D8B;
    --color-iris: #9B59B6;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: var(--bg-color); color: var(--text-primary); display: flex; min-height: 100vh; }

/* SIDEBAR */
.sidebar { width: 260px; background: var(--sidebar-bg); border-right: 1px solid #E5E7EB; padding: 2rem; position: fixed; height: 100vh; overflow-y: auto; }
.brand { font-size: 1.5rem; font-weight: 800; color: var(--accent-color); margin-bottom: 2rem; display: flex; align-items: center; gap: 0.5rem; }
.nav-menu { list-style: none; }
.nav-item { margin-bottom: 0.5rem; }
.nav-link { display: block; padding: 0.75rem 1rem; border-radius: 0.5rem; color: var(--text-secondary); text-decoration: none; font-weight: 500; transition: all 0.2s; }
.nav-link:hover, .nav-link.active { background: #F3F4F6; color: var(--accent-color); }
.nav-section { margin-top: 2rem; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #9CA3AF; font-weight: 700; margin-bottom: 1rem; }

/* MAIN CONTENT */
.main-content { margin-left: 260px; padding: 2rem 4rem; width: 100%; }
.header { margin-bottom: 3rem; }
.page-title { font-size: 2rem; font-weight: 800; margin-bottom: 0.5rem; }
.page-subtitle { color: var(--text-secondary); font-size: 1.1rem; }

/* DASHBOARD STATS */
.stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-bottom: 3rem; }
.stat-card { background: white; padding: 1.5rem; border-radius: 1rem; box-shadow: var(--card-shadow); border: 1px solid #F3F4F6; }
.stat-value { font-size: 2rem; font-weight: 800; color: var(--accent-color); }
.stat-label { color: var(--text-secondary); font-size: 0.9rem; font-weight: 500; }

/* SECTIONS */
.section-title { font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem; }
.grid-lessons { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }

/* LESSON CARD */
.lesson-card { background: white; border-radius: 1rem; padding: 1.5rem; box-shadow: var(--card-shadow); transition: all 0.2s; border: 1px solid #F3F4F6; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; }
.lesson-card:hover { transform: translateY(-4px); box-shadow: var(--hover-shadow); }
.lesson-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; }
.lesson-id { font-size: 0.75rem; font-weight: 700; color: #9CA3AF; letter-spacing: 0.05em; }
.guardian-badge { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; background: #F3F4F6; }
.lesson-title { font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem; line-height: 1.4; }
.lesson-hook { font-size: 0.9rem; color: var(--text-secondary); font-style: italic; margin-bottom: 1.5rem; line-height: 1.5; flex-grow: 1; }
.lesson-footer { display: flex; justify-content: space-between; align-items: center; margin-top: auto; }
.btn-link { color: var(--accent-color); font-weight: 600; text-decoration: none; font-size: 0.9rem; }
.btn-link:hover { text-decoration: underline; }

/* GUARDIAN ACCENTS */
.lesson-card.celeste::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--color-celeste); }
.lesson-card.bernardo::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--color-bernardo); }
.lesson-card.melquior::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--color-melquior); }
.lesson-card.noe::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--color-noe); }
.lesson-card.iris::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--color-iris); }

/* BLOG PREVIEW */
.blog-placeholder { background: #E5E7EB; border-radius: 1rem; padding: 2rem; text-align: center; color: #6B7280; border: 2px dashed #D1D5DB; }

@media (max-width: 768px) {
    body { flex-direction: column; }
    .sidebar { width: 100%; height: auto; position: relative; padding: 1rem; }
    .main-content { margin-left: 0; padding: 1.5rem; }
    .stats-grid { grid-template-columns: 1fr; }
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forja Viva | Dashboard</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- SIDEBAR -->
    <aside class="sidebar">
        <div class="brand">🔥 Forja Viva</div>
        <ul class="nav-menu">
            <li class="nav-item"><a href="#" class="nav-link active">Dashboard</a></li>
            <li class="nav-item"><a href="#sementes" class="nav-link">🌱 Sementes</a></li>
            
            <li class="nav-section">Blog & Conteúdo</li>
            <li class="nav-item"><a href="#blog" class="nav-link">📝 Artigos</a></li>
            <li class="nav-item"><a href="#recursos" class="nav-link">🧰 Recursos</a></li>
            
            <li class="nav-section">Sistema</li>
            <li class="nav-item"><a href="#" class="nav-link">⚙️ Configurações</a></li>
        </ul>
    </aside>

    <!-- MAIN -->
    <main class="main-content">
        <header class="header">
            <h1 class="page-title">Bem-vindo, Maestro.</h1>
            <p class="page-subtitle">Visão geral do desenvolvimento do currículo Matemática Viva.</p>
        </header>

        <!-- STATS -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{{TOTAL_SEMENTES}}</div>
                <div class="stat-label">Lições Sementes Prontas</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">15/40</div>
                <div class="stat-label">Progresso Estação 1</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">Artigos Publicados</div>
            </div>
        </div>

        <!-- SEMENTES -->
        <section id="sementes" class="mb-12">
            <div class="section-title">
                <span>🌱</span> Ciclo Sementes <span style="font-size:0.8em; color:#9CA3AF; font-weight:400; margin-left:auto;">Última build: {{DATA}}</span>
            </div>
            <div class="grid-lessons">
                {{CARDS_SEMENTES}}
            </div>
        </section>

        <!-- BLOG -->
        <section id="blog" style="margin-top: 4rem;">
            <div class="section-title"><span>📝</span> Blog & Artigos</div>
            <div class="blog-placeholder">
                <h3>Em breve</h3>
                <p>O módulo de artigos está em construção. Aqui aparecerão as reflexões sobre CPA, CM e Narrativa.</p>
            </div>
        </section>

    </main>
</body>
</html>
"""

def get_guardian_data(name):
    name = name.lower()
    if 'celeste' in name: return 'celeste', '🦊'
    if 'bernardo' in name: return 'bernardo', '🐻'
    if 'noé' in name or 'noe' in name: return 'noe', '🦉'
    if 'íris' in name or 'iris' in name: return 'iris', '🐦'
    return 'melquior', '🦁'

def build_lesson_card(file_path):
    try:
        content = file_path.read_text(encoding='utf-8')
        data = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2: data = yaml.safe_load(parts[1])
        else:
            data = yaml.safe_load(content)
        
        # Extração segura
        meta = data.get('licao', {}).get('metadados', {}) if 'licao' in data else data
        ideia = data.get('licao', {}).get('ideia_viva', {}).get('frase', '') if 'licao' in data else data.get('ideia_viva', {}).get('frase', '')
        
        lid = meta.get('id', 'MV-S-XXX')
        titulo = meta.get('titulo', 'Sem Título')
        guardiao = meta.get('guardiao_lider', 'Melquior')
        
        if not ideia: ideia = "..."
        
        link = f"sementes/{file_path.stem}.html"
        css_class, emoji = get_guardian_data(guardiao)
        
        print(f"  • Processando: {lid}")
        
        return f"""
        <div class="lesson-card {css_class}">
            <div class="lesson-top">
                <span class="lesson-id">{lid}</span>
                <div class="guardian-badge" title="{guardiao}">{emoji}</div>
            </div>
            <div class="lesson-title">{titulo}</div>
            <div class="lesson-hook">"{ideia}"</div>
            <div class="lesson-footer">
                <a href="{link}" class="btn-link">Acessar Lição →</a>
            </div>
        </div>
        """
    except Exception as e:
        print(f"❌ Erro em {file_path.name}: {e}")
        return ""

def main():
    print("🚀 Iniciando Build do Dashboard V2...")
    
    # Garantir diretórios
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Gerar CSS
    (OUTPUT_DIR / "style.css").write_text(STYLE_CSS, encoding='utf-8')
    print("🎨 Style.css gerado.")
    
    # 2. Processar Sementes
    cards_sementes = []
    if INPUT_DIR_SEMENTES.exists():
        files = sorted(list(INPUT_DIR_SEMENTES.glob("*.yaml")))
        for f in files:
            card = build_lesson_card(f)
            if card: cards_sementes.append(card)
    
    # 3. Montar HTML
    html = HTML_TEMPLATE.replace("{{CARDS_SEMENTES}}", "\n".join(cards_sementes))
    html = html.replace("{{TOTAL_SEMENTES}}", str(len(cards_sementes)))
    html = html.replace("{{DATA}}", datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    OUTPUT_HTML.write_text(html, encoding='utf-8')
    print(f"✅ Dashboard gerado com sucesso: {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
