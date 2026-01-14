"""
🔨 BLOG BUILDER V1 (Orchestrator Aligned)
========================================
Gera páginas estáticas do Blog a partir de arquivos Markdown/YAML.
Integra-se ao visual Premium (Glassmorphism, Sidebar, Typography).
"""

import os
import yaml
import markdown
from pathlib import Path
from datetime import datetime

# CONFIGURAÇÃO
INPUT_DIR = Path("blog")
OUTPUT_DIR = Path("site/blog")
TEMPLATE_DIR = Path("_templates")

# CORES & ESTILO (Reutiliza style.css principal)
HTML_TEMPLATE_ARTICLE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITULO}} | Blog Forja Viva</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    <style>
        .blog-container { max-width: 800px; margin: 0 auto; padding: 4rem 2rem; }
        .article-header { text-align: center; margin-bottom: 3rem; }
        .article-meta { color: #6B7280; font-size: 0.9rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
        h1 { font-family: 'Lora', serif; font-size: 3rem; color: #111827; line-height: 1.2; margin-bottom: 1.5rem; }
        .article-summary { font-size: 1.25rem; color: #4B5563; line-height: 1.6; font-style: italic; max-width: 600px; margin: 0 auto 2rem; }
        
        .article-body { background: #FFF; padding: 3rem; border-radius: 1rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); line-height: 1.8; font-size: 1.125rem; color: #374151; font-family: 'Lora', serif; }
        .article-body h2 { font-family: 'Inter', sans-serif; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.5rem; color: #111827; }
        .article-body p { margin-bottom: 1.5rem; }
        .article-body ul { margin-bottom: 1.5rem; padding-left: 1.5rem; }
        .article-body li { margin-bottom: 0.5rem; }
        .article-body blockquote { border-left: 4px solid #047857; padding-left: 1rem; margin: 1.5rem 0; color: #4B5563; font-style: italic; }
        
        .home-btn { position: fixed; top: 2rem; left: 2rem; width: 3rem; height: 3rem; background: #FFF; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #E5E7EB; color: #374151; text-decoration: none; transition: all 0.2s; z-index: 100; }
        .home-btn:hover { transform: translateY(-2px); color: #047857; }
        
        @media (max-width: 768px) {
            .blog-container { padding: 2rem 1rem; }
            h1 { font-size: 2rem; }
            .article-body { padding: 1.5rem; }
        }
    </style>
</head>
<body>
    <a href="../index.html" class="home-btn" title="Voltar ao Dashboard">🏠</a>

    <article class="blog-container">
        <header class="article-header">
            <div class="article-meta">{{DATA}} • Por {{AUTOR}}</div>
            <h1>{{TITULO}}</h1>
            <div class="article-summary">{{RESUMO}}</div>
        </header>
        
        <div class="article-body">
            {{CONTEUDO}}
        </div>
    </article>
</body>
</html>
"""

def parse_article(file_path):
    try:
        content = file_path.read_text(encoding='utf-8')
        if content.startswith('---'):
            parts = content.split('---', 2) # Frontmatter handling # Frontmatter handling: Should be empty string before first ---
            # Wait, proper split for '--- ... --- content' usually results in ['', yaml, content]
            # My previous scripts handled this loosely. Let's be strict.
            # Assuming file starts with key: value (no initial ---) or standard frontmatter.
            # Standard Frontmatter:
            # ---
            # key: value
            # ---
            # content
            
            # Re-implementing logic:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # parts[0] is empty, parts[1] is yaml, parts[2] is content
                metadata = yaml.safe_load(parts[1])
                body_md = parts[2]
                return metadata, body_md
        
        # Fallback: Try to parse as simple YAML if no separator (error prone for content)
        # Or maybe it's "meta\n\n---\n\ncontent"?
        # Let's stick to standard frontmatter or fail gracefully.
        print(f"⚠️ {file_path.name} sem Frontmatter padrão (---). Tentando ler tudo como texto.")
        return {'titulo': file_path.stem}, content
        
    except Exception as e:
        print(f"❌ Erro ao ler {file_path.name}: {e}")
        return None, None

def main():
    print("🚀 Iniciando Blog Builder...")
    
    if not INPUT_DIR.exists():
        print(f"⚠️ Diretório de blog não encontrado: {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    articles = sorted(list(INPUT_DIR.glob("*.md")), reverse=True) # Newest first
    
    for article_file in articles:
        meta, body_md = parse_article(article_file)
        if not meta: continue
        
        # Convert MD to HTML
        html_content = markdown.markdown(body_md, extensions=['extra', 'codehilite'])
        
        # Build Page
        html = HTML_TEMPLATE_ARTICLE
        html = html.replace('{{TITULO}}', meta.get('titulo', 'Sem Título'))
        html = html.replace('{{DATA}}', str(meta.get('data', 'Data Desconhecida')))
        html = html.replace('{{AUTOR}}', meta.get('autor', 'Forja Viva'))
        html = html.replace('{{RESUMO}}', meta.get('resumo', ''))
        html = html.replace('{{CONTEUDO}}', html_content)
        
        # Save
        out_file = OUTPUT_DIR / f"{article_file.stem}.html"
        out_file.write_text(html, encoding='utf-8')
        print(f"  ✅ Artigo Gerado: {out_file.name}")

    print("✨ Blog atualizado com sucesso!")

if __name__ == "__main__":
    main()
