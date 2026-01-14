#!/usr/bin/env python3
"""
Log YAML → HTML Converter
Converte deliberações YAML em páginas HTML legíveis e bonitas.
Uso: python log_to_html.py logs/arquivo.yaml
"""

import yaml
import sys
import os
from pathlib import Path
from datetime import datetime

# CSS embutido para não depender de arquivos externos
CSS = """
:root {
    --bg: #1a1a2e;
    --card: #16213e;
    --accent: #e94560;
    --text: #eaeaea;
    --muted: #a0a0a0;
    --success: #4ade80;
    --border: #0f3460;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
    max-width: 900px;
    margin: 0 auto;
}

h1 {
    color: var(--accent);
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
    border-bottom: 2px solid var(--accent);
    padding-bottom: 0.5rem;
}

h2 {
    color: var(--text);
    font-size: 1.3rem;
    margin: 1.5rem 0 0.8rem;
    padding-left: 0.5rem;
    border-left: 3px solid var(--accent);
}

h3 {
    color: var(--muted);
    font-size: 1rem;
    margin: 1rem 0 0.5rem;
}

.meta {
    color: var(--muted);
    font-size: 0.85rem;
    margin-bottom: 1.5rem;
}

.card {
    background: var(--card);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin: 0.8rem 0;
    border-left: 3px solid var(--border);
}

.card.expert {
    border-left-color: var(--accent);
}

.card.decision {
    border-left-color: var(--success);
    background: linear-gradient(135deg, #16213e, #1a3a2e);
}

.expert-name {
    font-weight: 600;
    color: var(--accent);
}

.quote {
    font-style: italic;
    color: var(--muted);
    padding: 0.5rem 1rem;
    border-left: 2px solid var(--border);
    margin: 0.5rem 0;
}

.tag {
    display: inline-block;
    background: var(--accent);
    color: white;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    margin-right: 0.3rem;
}

.tag.success { background: var(--success); color: #1a1a2e; }

ul, ol {
    margin: 0.5rem 0 0.5rem 1.5rem;
}

li { margin: 0.3rem 0; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}

th, td {
    padding: 0.5rem;
    text-align: left;
    border-bottom: 1px solid var(--border);
}

th { color: var(--accent); font-weight: 600; }

pre {
    background: #0d1b2a;
    padding: 1rem;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 0.85rem;
    margin: 0.5rem 0;
}

.footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.8rem;
    text-align: center;
}
"""


def render_value(value, depth=0):
    """Renderiza um valor YAML em HTML"""
    if value is None:
        return "<em>—</em>"
    
    if isinstance(value, str):
        # Multi-line strings
        if '\n' in value:
            return f"<pre>{value.strip()}</pre>"
        return value
    
    if isinstance(value, bool):
        return '<span class="tag success">✓</span>' if value else '<span class="tag">✗</span>'
    
    if isinstance(value, (int, float)):
        return str(value)
    
    if isinstance(value, list):
        if all(isinstance(x, dict) for x in value):
            # Lista de objetos → tabela
            if len(value) > 0:
                keys = list(value[0].keys())
                html = "<table><tr>"
                for k in keys:
                    html += f"<th>{k}</th>"
                html += "</tr>"
                for item in value:
                    html += "<tr>"
                    for k in keys:
                        html += f"<td>{render_value(item.get(k, ''))}</td>"
                    html += "</tr>"
                html += "</table>"
                return html
        else:
            # Lista simples → bullets
            html = "<ul>"
            for item in value:
                html += f"<li>{render_value(item)}</li>"
            html += "</ul>"
            return html
    
    if isinstance(value, dict):
        html = "<div class='card'>"
        for k, v in value.items():
            html += f"<strong>{k}:</strong> {render_value(v)}<br>"
        html += "</div>"
        return html
    
    return str(value)


def render_section(key, value):
    """Renderiza uma seção do YAML"""
    html = f"<h2>{key.replace('_', ' ').title()}</h2>"
    
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            # Detectar cards de especialistas
            if sub_key in ['posicao', 'fundamento', 'proposta', 'citacao']:
                html += f"<h3>{sub_key.replace('_', ' ').title()}</h3>"
                if sub_key == 'citacao':
                    html += f"<div class='quote'>{render_value(sub_value)}</div>"
                else:
                    html += render_value(sub_value)
            else:
                html += f"<h3>{sub_key.replace('_', ' ').title()}</h3>"
                html += render_value(sub_value)
    else:
        html += render_value(value)
    
    return html


def yaml_to_html(yaml_path):
    """Converte um arquivo YAML em HTML"""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Extrair metadados do cabeçalho
    title = yaml_path.stem.replace('_', ' ').title()
    
    # Começar HTML
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{CSS}</style>
</head>
<body>
    <h1>📋 {title}</h1>
    <div class="meta">
        Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} | Fonte: {yaml_path.name}
    </div>
"""
    
    # Processar seções principais
    skip_keys = ['#']  # Comentários YAML
    
    for key, value in data.items():
        if key.startswith('#') or key.startswith('_'):
            continue
        
        # Seções especiais
        if key == 'participantes':
            html += "<h2>👥 Participantes</h2>"
            html += render_value(value)
        
        elif key == 'posicoes_iniciais':
            html += "<h2>🎯 Posições dos Especialistas</h2>"
            for expert, pos in value.items():
                html += f"<div class='card expert'>"
                html += f"<span class='expert-name'>🎭 {expert.replace('_', ' ').title()}</span>"
                html += render_value(pos)
                html += "</div>"
        
        elif key == 'decisao':
            html += "<h2>✅ Decisão Final</h2>"
            html += "<div class='card decision'>"
            html += render_value(value)
            html += "</div>"
        
        elif key == 'assinaturas':
            html += "<h2>✍️ Assinaturas</h2>"
            html += render_value(value)
        
        else:
            html += render_section(key, value)
    
    # Footer
    html += f"""
    <div class="footer">
        Matemática Viva | Deliberação Formal | Gerado automaticamente de YAML
    </div>
</body>
</html>
"""
    
    return html


def main():
    if len(sys.argv) < 2:
        # Sem argumentos: processa todos os YAMLs em logs/
        logs_dir = Path('logs')
        if not logs_dir.exists():
            print("❌ Pasta logs/ não encontrada")
            sys.exit(1)
        
        yaml_files = list(logs_dir.glob('*.yaml'))
        if not yaml_files:
            print("❌ Nenhum arquivo YAML encontrado em logs/")
            sys.exit(1)
        
        for yaml_file in yaml_files:
            output_path = yaml_file.with_suffix('.html')
            html = yaml_to_html(yaml_file)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✅ {yaml_file.name} → {output_path.name}")
        
        print(f"\n📄 {len(yaml_files)} arquivo(s) convertido(s)")
    
    else:
        # Argumento específico
        yaml_path = Path(sys.argv[1])
        if not yaml_path.exists():
            print(f"❌ Arquivo não encontrado: {yaml_path}")
            sys.exit(1)
        
        output_path = yaml_path.with_suffix('.html')
        html = yaml_to_html(yaml_path)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ Convertido: {yaml_path} → {output_path}")


if __name__ == '__main__':
    main()
