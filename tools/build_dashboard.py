"""
🔨 DASHBOARD BUILDER — Índice Visual Sementes
=============================================
Gera um index.html elegante listando todas as lições do ciclo Sementes.

Uso:
    python tools/build_dashboard.py
"""

import os
import yaml
from pathlib import Path
from datetime import datetime

# CONFIGURAÇÃO
INPUT_DIR = Path("curriculo/01_SEMENTES")
OUTPUT_DIR = Path("site")
STYLE_SRC = Path("build/style.css")
STYLE_DEST = OUTPUT_DIR / "style.css"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forja Viva — Dashboard Sementes</title>
    <link rel="stylesheet" href="style.css">
    <style>
        body { background-color: #f4f4f9; color: #333; font-family: 'Georgia', serif; }
        .dashboard-container { max-width: 900px; margin: 40px auto; padding: 20px; }
        h1 { text-align: center; color: #2c3e50; margin-bottom: 40px; font-size: 2.5em; }
        .lesson-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
        .lesson-card { 
            background: white; 
            border-radius: 12px; 
            padding: 20px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
            transition: transform 0.2s, box-shadow 0.2s;
            border-left: 5px solid #ddd;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .lesson-card:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.1); }
        .lesson-card.melquior { border-color: #D4A017; }
        .lesson-card.celeste { border-color: #FF6B35; }
        .lesson-card.bernardo { border-color: #8B4513; }
        .lesson-card.noe { border-color: #483D8B; }
        .lesson-card.iris { border-color: #9B59B6; }
        
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .lesson-id { font-weight: bold; color: #7f8c8d; font-size: 0.85em; }
        .guardian-emoji { font-size: 1.5em; }
        
        .lesson-title { font-size: 1.2em; font-weight: bold; margin-bottom: 10px; color: #2c3e50; }
        .lesson-hook { font-size: 0.9em; color: #555; font-style: italic; margin-bottom: 20px; flex-grow: 1; }
        
        .btn-view { 
            display: block; 
            text-align: center; 
            background: #2c3e50; 
            color: white; 
            text-decoration: none; 
            padding: 10px; 
            border-radius: 6px; 
            font-weight: bold;
            transition: background 0.2s;
        }
        .btn-view:hover { background: #34495e; }
        
        /* Stats */
        .stats { text-align: center; margin-bottom: 30px; color: #7f8c8d; }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <h1>🌱 Ciclo Sementes</h1>
        
        <div class="stats">
            <p><strong>{{TOTAL}}</strong> Lições Prontas • Última atualização: {{DATA}}</p>
        </div>

        <div class="lesson-grid">
            {{CARDS}}
        </div>
    </div>
</body>
</html>"""

def get_guardian_class(name):
    name = name.lower()
    if 'celeste' in name: return 'celeste'
    if 'bernardo' in name: return 'bernardo'
    if 'noé' in name or 'noe' in name: return 'noe'
    if 'íris' in name or 'iris' in name: return 'iris'
    return 'melquior'

def get_guardian_emoji(name):
    name = name.lower()
    if 'celeste' in name: return '🦊'
    if 'bernardo' in name: return '🐻'
    if 'noé' in name or 'noe' in name: return '🦉'
    if 'íris' in name or 'iris' in name: return '🐦'
    return '🦁'

def build_card(lesson_file, metadata):
    lid = metadata.get('id', 'MV-S-XXX')
    titulo = metadata.get('titulo', 'Sem Título')
    guardiao = metadata.get('guardiao_lider', 'Melquior')
    ideia = metadata.get('ideia_viva', {}).get('frase', '...')
    
    html_link = f"sementes/{lesson_file.stem}.html"
    css_class = get_guardian_class(guardiao)
    emoji = get_guardian_emoji(guardiao)
    
    return f"""
    <div class="lesson-card {css_class}">
        <div class="card-header">
            <span class="lesson-id">{lid}</span>
            <span class="guardian-emoji" title="{guardiao}">{emoji}</span>
        </div>
        <div class="lesson-title">{titulo}</div>
        <div class="lesson-hook">"{ideia}"</div>
        <a href="{html_link}" class="btn-view">Ver Lição →</a>
    </div>
    """

def main():
    if not INPUT_DIR.exists():
        print(f"❌ Diretório não encontrado: {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Copiar CSS se existir
    if STYLE_SRC.exists():
        import shutil
        shutil.copy(STYLE_SRC, STYLE_DEST)
        print(f"🎨 CSS copiado para {STYLE_DEST}")

    cards_html = []
    files = sorted(list(INPUT_DIR.glob("*.yaml")) + list(INPUT_DIR.glob("*.yml")))
    
    for f in files:
        try:
            content = f.read_text(encoding='utf-8')
            # Parse YAML seguro
            # Se tiver frontmatter --- ... ---, pegar o meio. Se for puro, load direto.
            data = {}
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    data = yaml.safe_load(parts[1])
            else:
                data = yaml.safe_load(content)
            
            # Normalizar estrutura (alguns tem raiz 'licao', outros não)
            if 'licao' in data:
                meta = data['licao']['metadados']
                # Tentar pegar ideia_viva também
                if 'ideia_viva' in data['licao']:
                    meta['ideia_viva'] = data['licao']['ideia_viva']
            else:
                meta = data # Assumindo estrutura plana ou metadata na raiz
                
            cards_html.append(build_card(f, meta))
            print(f"✅ Processado: {f.name}")
            
        except Exception as e:
            print(f"⚠️ Erro ao ler {f.name}: {e}")

    final_html = HTML_TEMPLATE.replace("{{CARDS}}", "\n".join(cards_html))
    final_html = final_html.replace("{{TOTAL}}", str(len(cards_html)))
    final_html = final_html.replace("{{DATA}}", datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    (OUTPUT_DIR / "index.html").write_text(final_html, encoding='utf-8')
    print(f"\n🎉 Dashboard gerado com sucesso em: {OUTPUT_DIR / 'index.html'}")

if __name__ == "__main__":
    main()
