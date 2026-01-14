"""
🔨 LESSON BUILDER V1 (Orchestrator Aligned)
===========================================
Gera páginas HTML individuais para cada lição YAML.
Injeta navegação (Anterior/Próxima) e aplica identidade visual Premium.
"""

import os
import yaml
from pathlib import Path
import re

# CONFIGURAÇÃO
INPUT_DIR = Path("curriculo/01_SEMENTES")
OUTPUT_DIR = Path("site/sementes")

# TEMPLATE IMPÉCAVEL (Baseado no Dashboard V3)
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITULO}} | Matemática Viva</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    <style>
        /* Lesson Specific Styles */
        .lesson-container { max-width: 800px; margin: 0 auto; padding: 4rem 2rem; }
        
        .lesson-header { text-align: center; margin-bottom: 4rem; position: relative; }
        .lesson-id { font-size: 0.875rem; font-weight: 700; color: #9CA3AF; letter-spacing: 0.1em; text-transform: uppercase; display: block; margin-bottom: 1rem; }
        h1 { font-family: 'Lora', serif; font-size: 3rem; color: #111827; margin-bottom: 1rem; line-height: 1.2; }
        .lesson-idea { font-family: 'Lora', serif; font-size: 1.5rem; color: #4B5563; font-style: italic; margin-bottom: 2rem; display: block; }
        
        .metadata-grid { display: flex; justify-content: center; gap: 2rem; margin-top: 2rem; font-size: 0.9rem; color: #6B7280; flex-wrap: wrap; }
        .meta-item { display: flex; align-items: center; gap: 0.5rem; background: #FFF; padding: 0.5rem 1rem; border-radius: 2rem; border: 1px solid #E5E7EB; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        
        .lesson-body { background: #FFF; padding: 3rem; border-radius: 1.5rem; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); border: 1px solid #E5E7EB; line-height: 1.8; color: #374151; font-size: 1.1rem; }
        
        h2 { font-family: 'Lora', serif; margin-top: 2.5rem; margin-bottom: 1.5rem; font-size: 1.8rem; color: #111827; border-bottom: 2px solid #F3F4F6; padding-bottom: 0.5rem; }
        h3 { margin-top: 2rem; font-size: 1.3rem; color: #1F2937; }
        
        ul { margin-bottom: 1.5rem; padding-left: 1.5rem; }
        li { margin-bottom: 0.5rem; }
        p { margin-bottom: 1.5rem; }
        
        .quote-box { background: #F9FAFB; border-left: 4px solid #047857; padding: 1.5rem; margin: 2rem 0; font-style: italic; color: #4B5563; }
        
        /* Navigation Controls */
        .lesson-nav { display: flex; justify-content: space-between; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #E5E7EB; }
        .nav-btn { display: flex; flex-direction: column; text-decoration: none; color: #6B7280; transition: all 0.2s; max-width: 45%; }
        .nav-btn:hover { color: #047857; }
        .nav-label { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 0.25rem; }
        .nav-title { font-family: 'Lora', serif; font-size: 1.1rem; font-weight: 600; }
        .nav-btn.prev { text-align: left; }
        .nav-btn.next { text-align: right; }
        .disabled { opacity: 0; pointer-events: none; }
        
        /* Home Button */
        .home-btn { position: fixed; top: 2rem; left: 2rem; width: 3rem; height: 3rem; background: #FFF; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #E5E7EB; color: #374151; text-decoration: none; transition: all 0.2s; z-index: 100; }
        .home-btn:hover { transform: translateY(-2px); color: #047857; }

        @media (max-width: 768px) {
            .home-btn { top: 1rem; left: 1rem; }
            .lesson-container { padding: 2rem 1rem; }
            .lesson-body { padding: 1.5rem; }
            h1 { font-size: 2rem; }
        }
    </style>
</head>
<body class="{{CLIMA_CLASS}}">
    <a href="../index.html" class="home-btn" title="Voltar ao Dashboard">🏠</a>

    <div class="lesson-container">
        <header class="lesson-header">
            <span class="lesson-id">{{ID}}</span>
            <h1>{{TITULO}}</h1>
            <span class="lesson-idea">"{{IDEIA_VIVA}}"</span>
            
            <div class="metadata-grid">
                <div class="meta-item">
                    <img src="{{GUARDIAO_IMG}}" alt="{{GUARDIAO}}" style="width: 24px; height: 24px; object-fit: contain;">
                    {{GUARDIAO}}
                </div>
                <div class="meta-item"><span>⏱️</span> {{TEMPO}}</div>
                <div class="meta-item"><span>🌤️</span> {{CLIMA}}</div>
            </div>
        </header>

        <article class="lesson-body">
            {{CONTEUDO_HTML}}
        </article>

        <nav class="lesson-nav">
            {{LINK_PREV}}
            {{LINK_NEXT}}
        </nav>
    </div>
</body>
</html>
"""

def simple_markdown_to_html(md_text):
    """Conversor ultra-simples de MD para HTML para manter integridade."""
    if not md_text: return ""
    
    html = md_text
    
    # Headers
    html = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Bold/Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Lists (Simples)
    lines = html.split('\n')
    new_lines = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
            new_lines.append(f'<li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            if line.strip():
                if not line.startswith('<h') and not line.startswith('<ul') and not line.startswith('<li'):
                     new_lines.append(f'<p>{line}</p>')
                else:
                    new_lines.append(line)
    
    if in_list: new_lines.append('</ul>')
    
    return "\n".join(new_lines)

def load_lessons():
    """
    CARREGAMENTO DE DADOS (O 'Crawler')
    -----------------------------------
    1. Varre a pasta 'curriculo/01_SEMENTES'.
    2. Lê cada arquivo .yaml.
    3. Normaliza os dados (lida com diferenças de indentação entre versões).
    4. Retorna uma lista limpa pronta para virar HTML.
    """
    lessons = []
    if not INPUT_DIR.exists(): return []
    
    files = sorted(list(INPUT_DIR.glob("*.yaml")))
    for f in files:
        try:
            content = f.read_text(encoding='utf-8')
            data = {}
            # Tratamento para Frontmatter (se houver --- no início)
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 2: data = yaml.safe_load(parts[1])
            else:
                data = yaml.safe_load(content)
            
            # NORMALIZAÇÃO DE ESTRUTURA (Premium Nested vs Lean Flat)
            # Alguns arquivos têm 'licao: { metadados: ... }', outros são diretos.
            meta = data.get('licao', {}).get('metadados', {}) if 'licao' in data else data
            ideia = data.get('licao', {}).get('ideia_viva', {}).get('frase', '') if 'licao' in data else data.get('ideia_viva', {}).get('frase', '')
            corpo = data.get('licao', {}) if 'licao' in data else data
            
            # Remove chaves de metadados do dicionário de conteúdo para não imprimir duplicado
            content_dict = {k:v for k,v in corpo.items() if k not in ['metadados', 'ideia_viva']}
            
            lessons.append({
                'file_stem': f.stem,
                'id': meta.get('id', 'MV-S-XXX'),
                'sort_id': int(re.sub(r'\D', '', meta.get('id', '0'))) if re.sub(r'\D', '', meta.get('id', '0')) else 999,
                'titulo': meta.get('titulo', 'Sem Título'),
                'ideia': ideia,
                'guardiao': meta.get('guardiao_lider', 'Melquior'),
                'tempo': meta.get('tempo_estimado', '20 min'),
                'clima': meta.get('clima', 'Ensolarado'),
                'raw_content': content_dict
            })
        except Exception as e:
            print(f"⚠️ Erro ao carregar {f.name}: {e}")
            
    # Ordena pelo ID numérico (ex: 1, 2, 10...) para garantir sequência correta
    return sorted(lessons, key=lambda x: x['sort_id'])

def format_content(content_dict):
    """
    TRANSFORMAÇÃO DE CONTEÚDO (O Coração do Builder)
    ------------------------------------------------
    Esta função pega o dicionário cru do YAML e o transforma em HTML bonito.
    Ela segue uma ordem lógica pedagógica (Abertura -> Concreto -> Abstrato -> Fechamento).
    """
    html_parts = []
    
    # ORDEM LÓGICA DE EXIBIÇÃO NA PÁGINA
    # Aqui definimos a sequência exata em que as seções aparecem no site.
    order = ['preparacao_do_portador', 'ritual_abertura', 'atividade_concreta', 'atividade_pictorica', 'atividade_abstrata', 'narramos_juntos', 'ritual_fechamento']
    
    # RÓTULOS AMIGÁVEIS (Para o Título da Seção)
    labels = {
        'preparacao_do_portador': '👨‍👩‍👧 Preparação do Portador',
        'ritual_abertura': '🎬 Ritual de Abertura',
        'atividade_concreta': '🧱 Atividade Concreta',
        'atividade_pictorica': '🎨 Atividade Pictórica',
        'atividade_abstrata': '🔢 Atividade Abstrata',
        'narramos_juntos': '🗣️ Narramos Juntos',
        'ritual_fechamento': '🏁 Ritual de Fechamento'
    }

    for key in order:
        if key in content_dict and content_dict[key]:
            section = content_dict[key]
            html_parts.append(f"<h2>{labels.get(key, key.title())}</h2>")
            
            if isinstance(section, dict):
                for k, v in section.items():
                    key_clean = k.replace('_', ' ').title()
                    
                    if isinstance(v, list):
                        html_parts.append(f"<p><strong>{key_clean}:</strong></p><ul>")
                        for item in v: html_parts.append(f"<li>{item}</li>")
                        html_parts.append("</ul>")
                    
                    elif isinstance(v, dict):
                        # Tratamento especial para objetos de Script (Fala, Instrução)
                        tom = v.get('tom', '')
                        script = v.get('script', '') or v.get('fala', '') or v.get('instrucao', '')
                        
                        if 'fala' in k or 'guardiao' in k or 'portador' in k:
                            # Dialogues
                            tom_html = f'<span class="script-tone">({tom})</span>' if tom else ''
                            html_parts.append(f'<div class="script-block"><strong class="script-role">{key_clean} {tom_html}:</strong> <span class="script-text">"{script}"</span></div>')
                        else:
                            # Generic Dict (Instruction/Transition)
                            parts = [f"<strong>{sub_k.title()}:</strong> {sub_v}" for sub_k, sub_v in v.items()]
                            html_parts.append(f"<p class='generic-dict'>{'; '.join(parts)}</p>")
                            
                    else:
                         # Simple Key-Value
                         html_parts.append(f"<p><strong>{key_clean}:</strong> {v}</p>")
            elif isinstance(section, str):
                html_parts.append(simple_markdown_to_html(section))
    
    return "\n".join(html_parts)


def get_guardian_data(name):
    name = name.lower()
    if 'celeste' in name: return '../assets/cards/guardioes/celeste-raposa.png'
    if 'bernardo' in name: return '../assets/cards/guardioes/bernardo-urso.png'
    if 'noé' in name or 'noe' in name: return '../assets/cards/guardioes/noe-coruja.png'
    if 'íris' in name or 'iris' in name: return '../assets/cards/guardioes/iris-passarinho.png'
    return '../assets/cards/guardioes/melquior-leao.png'

def main():
    print("🚀 Iniciando Lesson Builder...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    lessons = load_lessons()
    print(f"📦 {len(lessons)} lições carregadas.")
    
    for i, lesson in enumerate(lessons):
        # Navigation Logic
        prev_lesson = lessons[i-1] if i > 0 else None
        next_lesson = lessons[i+1] if i < len(lessons)-1 else None
        
        # Guardian Image
        guardiao_img = get_guardian_data(lesson['guardiao'])
        
        # Build HTML
        html = HTML_TEMPLATE
        html = html.replace('{{TITULO}}', lesson['titulo'])
        html = html.replace('{{ID}}', lesson['id'])
        html = html.replace('{{IDEIA_VIVA}}', lesson['ideia'])
        html = html.replace('{{GUARDIAO}}', lesson['guardiao'])
        html = html.replace('{{GUARDIAO_IMG}}', guardiao_img)
        html = html.replace('{{TEMPO}}', lesson['tempo'])
        html = html.replace('{{CLIMA}}', lesson['clima'])
        html = html.replace('{{CLIMA_CLASS}}', f"clima-{lesson['clima'].lower()}")
        
        # Content Generation
        content_html = format_content(lesson['raw_content'])
        html = html.replace('{{CONTEUDO_HTML}}', content_html)
        
        # Links Injection
        if prev_lesson:
            link_prev = f'<a href="{prev_lesson["file_stem"]}.html" class="nav-btn prev"><span class="nav-label">← Anterior</span><span class="nav-title">{prev_lesson["titulo"]}</span></a>'
        else:
            link_prev = '<div class="nav-btn prev disabled"></div>'
            
        if next_lesson:
            link_next = f'<a href="{next_lesson["file_stem"]}.html" class="nav-btn next"><span class="nav-label">Próxima →</span><span class="nav-title">{next_lesson["titulo"]}</span></a>'
        else:
            link_next = '<div class="nav-btn next disabled"></div>'
            
        html = html.replace('{{LINK_PREV}}', link_prev)
        html = html.replace('{{LINK_NEXT}}', link_next)
        
        # Write File
        out_file = OUTPUT_DIR / f"{lesson['file_stem']}.html"
        out_file.write_text(html, encoding='utf-8')
        print(f"  ✅ Gerada: {out_file.name}")
        
    print("✨ Todas as lições foram geradas com sucesso!")

if __name__ == "__main__":
    main()
