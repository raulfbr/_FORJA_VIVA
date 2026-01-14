"""
🔨 PDF FORGE — Pipeline YAML → PDF
====================================

Motor de conversão de lições YAML para PDF de qualidade profissional.
Versão: 2.0.0 (YAML Input Direto)
Autor: DevOps Agent (BMAD)

Uso:
    python pdf_forge.py --input curriculo/01_SEMENTES/000_INICIO_FORJA.yaml --output print/
    python pdf_forge.py --input curriculo/01_SEMENTES/ --output print/sementes/ --all

Dependências:
    pip install playwright pyyaml
    python -m playwright install chromium
"""

import argparse
import yaml
import re
from pathlib import Path
from datetime import datetime
from html import escape

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ Playwright não instalado. Execute:")
    print("   pip install playwright pyyaml")
    print("   python -m playwright install chromium")
    exit(1)


# ═══════════════════════════════════════════════════════════════
# CONFIGURAÇÃO
# ═══════════════════════════════════════════════════════════════

CONFIG = {
    "PAGE_FORMAT": "A4",
    "MARGIN_TOP": "1.5cm",
    "MARGIN_BOTTOM": "1.2cm",
    "MARGIN_LEFT": "2cm",        # BINDING - Espiral esquerda
    "MARGIN_RIGHT": "1cm",
    "PRINT_BACKGROUND": False,
    "HEADER_TEMPLATE": """
        <div style="font-size: 8px; font-family: Arial, sans-serif; 
                    color: #999; text-align: right; width: 100%; padding-right: 1cm;">
            <span class="pageNumber"></span> / <span class="totalPages"></span>
        </div>
    """,
    "FOOTER_TEMPLATE": "<span></span>",
}

# Mapeamento de Guardiões para emojis
GUARDIOES = {
    "melquior": "🦁",
    "noe": "🦉",
    "noé": "🦉",
    "celeste": "🦊",
    "bernardo": "🐻",
    "iris": "🐦",
    "íris": "🐦",
}

# ═══════════════════════════════════════════════════════════════
# TEMPLATE HTML INTERNO (2 COLUNAS)
# ═══════════════════════════════════════════════════════════════

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{{titulo}} — Matemática Viva</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700&family=Outfit:wght@400;600&display=swap');
        
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Merriweather', Georgia, serif;
            font-size: 9pt;
            line-height: 1.5;
            color: #000;
            background: white;
        }
        
        /* Header */
        .header {
            text-align: center;
            padding: 0.4cm 0;
            border-bottom: 0.25pt solid #999;
            margin-bottom: 0.4cm;
        }
        
        .lesson-id {
            font-family: 'Outfit', sans-serif;
            font-size: 8pt;
            color: white;
            background: #555;
            padding: 2px 8px;
            border-radius: 4px;
            display: inline-block;
            margin-bottom: 0.2cm;
        }
        
        .header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 14pt;
            color: #000;
            margin: 0.2cm 0;
        }
        
        .header-meta {
            font-family: 'Outfit', sans-serif;
            font-size: 9pt;
            color: #666;
        }
        
        /* Ideia Viva */
        .ideia-viva {
            background: #f5f5f5;
            border-left: 3px solid #666;
            padding: 0.3cm;
            margin: 0.4cm 0;
            font-style: italic;
        }
        
        /* Conteúdo em 2 colunas */
        .content {
            column-count: 2;
            column-gap: 0.7cm;
            column-rule: 0.25pt solid #ccc;
            text-align: justify;
        }
        
        /* Títulos atravessam colunas */
        h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 10pt;
            color: #000;
            border-bottom: 0.25pt solid #bbb;
            padding-bottom: 0.1cm;
            margin: 0.4cm 0 0.2cm 0;
            column-span: all;
            break-after: avoid;
        }
        
        h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 9pt;
            color: #000;
            margin: 0.2cm 0 0.15cm 0;
        }
        
        p {
            margin-bottom: 0.2cm;
            orphans: 3;
            widows: 3;
        }
        
        /* Blocos especiais */
        .bloco-portador {
            background: #fafafa;
            border: 1px solid #ddd;
            padding: 0.3cm;
            margin: 0.3cm 0;
            break-inside: avoid;
        }
        
        .bloco-portador-titulo {
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 9pt;
            color: #555;
            margin-bottom: 0.2cm;
        }
        
        .narrativa {
            margin: 0.2cm 0;
            padding-left: 0.3cm;
            border-left: 2px solid #ccc;
        }
        
        .fala-guardiao {
            font-style: italic;
            color: #333;
        }
        
        .instrucao {
            font-family: 'Outfit', sans-serif;
            font-size: 8pt;
            color: #666;
            background: #f9f9f9;
            padding: 0.2cm;
            margin: 0.2cm 0;
        }
        
        /* Listas */
        ul, ol {
            margin: 0.2cm 0 0.2cm 0.5cm;
            padding-left: 0.3cm;
        }
        
        li {
            margin-bottom: 0.1cm;
        }
        
        ul li::marker {
            color: #666;
        }
        
        /* Material */
        .material-item {
            display: flex;
            gap: 0.2cm;
            margin-bottom: 0.1cm;
        }
        
        .material-check {
            color: #666;
        }
        
        /* Footer interno (não o do Playwright) */
        .footer-interno {
            text-align: center;
            font-size: 8pt;
            color: #999;
            border-top: 0.5pt solid #ddd;
            padding-top: 0.2cm;
            margin-top: 0.5cm;
            column-span: all;
        }
        
        /* Controle de quebras */
        .no-break {
            break-inside: avoid;
        }
    </style>
</head>
<body>
    <header class="header">
        <span class="lesson-id">{{id}}</span>
        <h1>{{titulo}}</h1>
        <div class="header-meta">
            {{guardiao_emoji}} {{guardiao}} • ⏱️ {{tempo}} • {{fase}}
        </div>
    </header>
    
    <div class="ideia-viva">
        💡 <strong>Ideia Viva:</strong> {{ideia_viva}}
    </div>
    
    <main class="content">
        {{conteudo}}
    </main>
    
    <div class="footer-interno">
        Matemática Viva • {{data}}
    </div>
</body>
</html>
"""


# ═══════════════════════════════════════════════════════════════
# FUNÇÕES DE RENDERIZAÇÃO
# ═══════════════════════════════════════════════════════════════

def sanitize_text(text: str) -> str:
    """Limpa e escapa texto para HTML."""
    if not text:
        return ""
    # Escapar HTML
    text = escape(str(text))
    # Converter quebras de linha para <br>
    text = text.replace('\n', '<br>\n')
    return text


def render_multiline(text: str) -> str:
    """Renderiza texto multilinea em parágrafos HTML."""
    if not text:
        return ""
    paragraphs = str(text).strip().split('\n\n')
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p:
            # Detectar se é lista
            if p.startswith('- ') or p.startswith('* '):
                items = p.split('\n')
                html_parts.append('<ul>')
                for item in items:
                    item = item.lstrip('- *').strip()
                    if item:
                        html_parts.append(f'<li>{escape(item)}</li>')
                html_parts.append('</ul>')
            else:
                html_parts.append(f'<p>{escape(p).replace(chr(10), "<br>")}</p>')
    return '\n'.join(html_parts)


def render_materiais(materiais: list) -> str:
    """Renderiza lista de materiais."""
    if not materiais:
        return ""
    html = ['<div class="no-break">', '<h3>📦 Materiais</h3>', '<ul>']
    for m in materiais:
        item = m.get('item', '')
        qtd = m.get('quantidade', '')
        essencial = "✓" if m.get('essencial', False) else "○"
        html.append(f'<li><span class="material-check">{essencial}</span> {escape(item)} ({qtd})</li>')
    html.append('</ul></div>')
    return '\n'.join(html)


def render_narrativa(narrativa: dict) -> str:
    """Renderiza narrativa principal."""
    if not narrativa:
        return ""
    
    html = ['<h2>📖 Jornada</h2>']
    
    for key, cena in narrativa.items():
        if isinstance(cena, dict):
            local = cena.get('local', '')
            transicao = cena.get('transicao', '')
            descricao = cena.get('descricao', '')
            virtude = cena.get('virtude', '')
            
            html.append(f'<div class="no-break">')
            if local:
                html.append(f'<h3>📍 {escape(local)}</h3>')
            if transicao:
                html.append(f'<p class="narrativa">{escape(transicao).replace(chr(10), "<br>")}</p>')
            if descricao:
                html.append(f'<div class="fala-guardiao">{escape(descricao).replace(chr(10), "<br>")}</div>')
            if virtude:
                html.append(f'<p><strong>Virtude:</strong> {escape(virtude)}</p>')
            html.append('</div>')
    
    return '\n'.join(html)


def render_ritual(ritual: dict, titulo: str, emoji: str) -> str:
    """Renderiza ritual de abertura ou fechamento."""
    if not ritual:
        return ""
    
    html = [f'<h2>{emoji} {titulo}</h2>']
    
    if 'instrucao_ambiente' in ritual:
        html.append(f'<div class="instrucao">{escape(ritual["instrucao_ambiente"]).replace(chr(10), "<br>")}</div>')
    
    if 'fala_portador' in ritual:
        fala = ritual['fala_portador']
        if isinstance(fala, dict):
            script = fala.get('script', '')
        else:
            script = fala
        html.append(f'<div class="fala-guardiao">{escape(script).replace(chr(10), "<br>")}</div>')
    
    if 'fala_guardiao' in ritual:
        fala = ritual['fala_guardiao']
        if isinstance(fala, dict):
            script = fala.get('script', '')
        else:
            script = fala
        html.append(f'<div class="fala-guardiao">{escape(script).replace(chr(10), "<br>")}</div>')
    
    return '\n'.join(html)


def render_sugestoes(sugestoes: list) -> str:
    """Renderiza sugestões dos guardiões."""
    if not sugestoes:
        return ""
    
    html = ['<h2>💡 Dicas dos Guardiões</h2>']
    
    for s in sugestoes:
        guardiao = s.get('guardiao', '')
        emoji = s.get('emoji', '')
        dica = s.get('dica', '')
        sugestao = s.get('sugestao', '')
        
        html.append('<div class="no-break bloco-portador">')
        html.append(f'<div class="bloco-portador-titulo">{emoji} {escape(guardiao)}</div>')
        if dica:
            html.append(f'<p class="fala-guardiao">{escape(dica).replace(chr(10), "<br>")}</p>')
        if sugestao:
            html.append(f'<p>{escape(sugestao).replace(chr(10), "<br>")}</p>')
        html.append('</div>')
    
    return '\n'.join(html)


def render_conteudo_cpa(jornada: dict) -> str:
    """Renderiza seções Concreto, Pictórico, Abstrato."""
    if not jornada:
        return ""
    
    html = []
    
    # Concreto
    if 'concreto' in jornada:
        c = jornada['concreto']
        html.append('<h2>🎯 Atividade (Concreto)</h2>')
        if c.get('descricao'):
            html.append(f'<div class="fala-guardiao">{escape(c["descricao"]).replace(chr(10), "<br>")}</div>')
        if c.get('instrucoes_portador'):
            html.append('<ol>')
            for inst in c['instrucoes_portador']:
                acao = inst.get('acao', '')
                fala = inst.get('fala_sugerida', '')
                html.append(f'<li><strong>{escape(acao)}</strong><br><em>{escape(fala)}</em></li>')
            html.append('</ol>')
    
    # Pictórico
    if 'pictorico' in jornada and not jornada['pictorico'].get('vetado', True):
        p = jornada['pictorico']
        html.append('<h2>🎨 Atividade (Pictórico)</h2>')
        if p.get('atividade'):
            html.append(f'<p>{escape(p["atividade"]).replace(chr(10), "<br>")}</p>')
    
    # Abstrato
    if 'abstrato' in jornada:
        a = jornada['abstrato']
        html.append('<h2>🔢 Atividade (Abstrato)</h2>')
        if a.get('descricao'):
            html.append(f'<p>{escape(a["descricao"]).replace(chr(10), "<br>")}</p>')
    
    return '\n'.join(html)


# ═══════════════════════════════════════════════════════════════
# FUNÇÃO PRINCIPAL DE CONVERSÃO
# ═══════════════════════════════════════════════════════════════

def yaml_to_html(licao: dict) -> str:
    """Converte estrutura de lição YAML para HTML completo."""
    
    meta = licao.get('metadados', {})
    ideia = licao.get('ideia_viva', {})
    jornada = licao.get('jornada', {})
    
    # Dados básicos
    titulo = meta.get('titulo', 'Lição')
    lesson_id = meta.get('id', 'MV-X-000')
    guardiao = meta.get('guardiao_lider', 'Melquior')
    guardiao_lower = guardiao.lower()
    guardiao_emoji = GUARDIOES.get(guardiao_lower, '👤')
    tempo = licao.get('preparacao', {}).get('tempo_licao', '15-20 min')
    fase = meta.get('fase', 'Sementes')
    ideia_viva = ideia.get('frase', '')
    
    # Renderizar seções de conteúdo
    conteudo_parts = []
    
    # Para o Portador
    portador = licao.get('para_o_portador', {})
    if portador:
        conteudo_parts.append('<div class="bloco-portador no-break">')
        conteudo_parts.append('<div class="bloco-portador-titulo">📋 Para o Portador da Tocha</div>')
        if portador.get('dica_de_coracao'):
            conteudo_parts.append(f'<p>{escape(portador["dica_de_coracao"]).replace(chr(10), "<br>")}</p>')
        conteudo_parts.append('</div>')
    
    # Materiais
    materiais = licao.get('preparacao', {}).get('materiais', [])
    if materiais:
        conteudo_parts.append(render_materiais(materiais))
    
    # Ritual de Abertura
    conteudo_parts.append(render_ritual(licao.get('ritual_abertura', {}), 'Ritual de Abertura', '🕯️'))
    
    # Narrativa Principal
    narrativa = jornada.get('narrativa_principal', {})
    if narrativa:
        conteudo_parts.append(render_narrativa(narrativa))
    elif jornada.get('abertura_sensorial'):
        conteudo_parts.append('<h2>📖 Jornada</h2>')
        conteudo_parts.append(f'<p class="narrativa">{escape(jornada["abertura_sensorial"]).replace(chr(10), "<br>")}</p>')
    
    # Atividades CPA
    conteudo_parts.append(render_conteudo_cpa(jornada))
    
    # Narração
    narracao = licao.get('narracao', {})
    if narracao:
        conteudo_parts.append('<h2>🗣️ Momento de Narração</h2>')
        if narracao.get('pergunta_principal'):
            conteudo_parts.append(f'<div class="fala-guardiao">{escape(narracao["pergunta_principal"]).replace(chr(10), "<br>")}</div>')
    
    # Ritual de Fechamento
    conteudo_parts.append(render_ritual(licao.get('ritual_fechamento', {}), 'Ritual de Fechamento', '🕊️'))
    
    # Sugestões
    conteudo_parts.append(render_sugestoes(licao.get('sugestoes', [])))
    
    # Montar HTML final
    html = HTML_TEMPLATE
    html = html.replace('{{titulo}}', escape(titulo))
    html = html.replace('{{id}}', escape(lesson_id))
    html = html.replace('{{guardiao}}', escape(guardiao))
    html = html.replace('{{guardiao_emoji}}', guardiao_emoji)
    html = html.replace('{{tempo}}', escape(str(tempo)))
    html = html.replace('{{fase}}', escape(fase))
    html = html.replace('{{ideia_viva}}', escape(ideia_viva))
    html = html.replace('{{data}}', datetime.now().strftime('%d/%m/%Y'))
    html = html.replace('{{conteudo}}', '\n'.join(conteudo_parts))
    
    return html


def convert_yaml_to_pdf(yaml_path: Path, output_path: Path) -> bool:
    """Converte arquivo YAML para PDF."""
    try:
        # Ler YAML
        content = yaml_path.read_text(encoding='utf-8')
        data = yaml.safe_load(content)
        
        licao = data.get('licao', data)
        
        # Renderizar HTML
        html = yaml_to_html(licao)
        
        # Converter para PDF via Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.set_content(html, wait_until='networkidle')
            page.wait_for_timeout(500)  # Esperar fontes
            
            page.pdf(
                path=str(output_path),
                format=CONFIG['PAGE_FORMAT'],
                margin={
                    'top': CONFIG['MARGIN_TOP'],
                    'bottom': CONFIG['MARGIN_BOTTOM'],
                    'left': CONFIG['MARGIN_LEFT'],
                    'right': CONFIG['MARGIN_RIGHT'],
                },
                print_background=CONFIG['PRINT_BACKGROUND'],
                display_header_footer=True,
                header_template=CONFIG['HEADER_TEMPLATE'],
                footer_template=CONFIG['FOOTER_TEMPLATE'],
            )
            
            browser.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def process_single(input_path: Path, output_dir: Path) -> bool:
    """Processa um único arquivo YAML."""
    if not input_path.exists():
        print(f"❌ Arquivo não encontrado: {input_path}")
        return False
    
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_name = input_path.stem + ".pdf"
    output_path = output_dir / pdf_name
    
    print(f"📄 Convertendo: {input_path.name}")
    
    if convert_yaml_to_pdf(input_path, output_path):
        print(f"✅ Gerado: {output_path}")
        return True
    return False


def process_batch(input_dir: Path, output_dir: Path) -> tuple[int, int]:
    """Processa todos os arquivos YAML em um diretório."""
    if not input_dir.exists():
        print(f"❌ Diretório não encontrado: {input_dir}")
        return 0, 0
    
    yaml_files = list(input_dir.glob("*.yaml")) + list(input_dir.glob("*.yml"))
    
    if not yaml_files:
        print(f"⚠️ Nenhum arquivo YAML encontrado em: {input_dir}")
        return 0, 0
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🔨 PDF Forge v2.0 (YAML→PDF) — Convertendo {len(yaml_files)} lições\n")
    
    success = 0
    for yaml_file in sorted(yaml_files):
        pdf_name = yaml_file.stem + ".pdf"
        output_path = output_dir / pdf_name
        
        print(f"📄 [{success + 1}/{len(yaml_files)}] {yaml_file.name}")
        
        if convert_yaml_to_pdf(yaml_file, output_path):
            success += 1
            print(f"   ✅ → {pdf_name}")
        else:
            print(f"   ❌ Falhou")
    
    return success, len(yaml_files)


def main():
    parser = argparse.ArgumentParser(
        description="🔨 PDF Forge v2.0 — YAML → PDF (2 colunas)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python pdf_forge.py --input curriculo/01_SEMENTES/000_INICIO_FORJA.yaml --output print/
  python pdf_forge.py --input curriculo/01_SEMENTES/ --output print/sementes/ --all
        """
    )
    
    parser.add_argument("--input", "-i", required=True, help="Arquivo YAML ou diretório")
    parser.add_argument("--output", "-o", default="print", help="Diretório de saída")
    parser.add_argument("--all", "-a", action="store_true", help="Processar todos os YAMLs")
    parser.add_argument("--format", "-f", default="A4", choices=["A4", "Letter"], help="Formato")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output)
    CONFIG['PAGE_FORMAT'] = args.format
    
    start_time = datetime.now()
    
    if args.all or input_path.is_dir():
        input_dir = input_path if input_path.is_dir() else input_path.parent
        success, total = process_batch(input_dir, output_dir)
        duration = (datetime.now() - start_time).total_seconds()
        print(f"\n✅ Concluído: {success}/{total} PDFs em {output_dir}")
        print(f"⏱️ Tempo: {duration:.1f}s ({duration/max(total,1):.1f}s por PDF)")
    else:
        if process_single(input_path, output_dir):
            duration = (datetime.now() - start_time).total_seconds()
            print(f"⏱️ Tempo: {duration:.1f}s")
        else:
            exit(1)


if __name__ == "__main__":
    main()
