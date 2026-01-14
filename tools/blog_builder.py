"""
🔨 BLOG BUILDER
==============
Gera a estrutura HTML para os artigos do Blog.
"""

import os
import yaml
from pathlib import Path
from datetime import datetime

# CONFIGURAÇÃO
INPUT_DIR = Path("blog")
OUTPUT_DIR = Path("site/blog")

def build_blog_index(articles):
    # TODO: Implementar geração do índice do blog
    pass

def build_article_page(article_file):
    # TODO: Implementar conversão de Markdown para HTML do artigo
    pass

def main():
    if not INPUT_DIR.exists():
        print(f"⚠️ Diretório de blog não encontrado: {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("🚀 Iniciando build do Blog...")
    # Lógica de build aqui
    print("✅ Build do Blog concluído.")

if __name__ == "__main__":
    main()
