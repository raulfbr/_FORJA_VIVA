"""
🔨 GUTENBERG FORJA — Pipeline YAML → HTML
==========================================

Pipeline oficial para converter lições YAML em HTML renderizado.
Versão: 2.0.0 (YAML-Only - Forja Viva)
Autor: DevOps Agent (BMAD)

Uso:
    python gutenberg_forja.py --input curriculo/01_SEMENTES/ --output site/sementes/

Nota: Todas as lições devem ser em formato .yaml (SSOT)
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from datetime import datetime


# ═══════════════════════════════════════════════════════════════
# CONFIGURAÇÃO
# ═══════════════════════════════════════════════════════════════

CONFIG = {
    "TEMPLATE_HTML": "base_template.html",
    "CSS_FILE": "style.css",
    "OUTPUT_DIR": "site/sementes",
    "CARD_IMG_PATH": "assets/img/cards",
}

# Mapeamento de Guardiões para imagens
GUARDIOES = {
    "MELQUIOR": {"emoji": "🦁", "img": "melquior.png", "cor": "#D4A017"},
    "NOE": {"emoji": "🦉", "img": "noe.png", "cor": "#8B4513"},
    "CELESTE": {"emoji": "🦊", "img": "celeste.png", "cor": "#FF6B35"},
    "BERNARDO": {"emoji": "🐻", "img": "bernardo.png", "cor": "#5D4E37"},
    "IRIS": {"emoji": "🐦", "img": "iris.png", "cor": "#9B59B6"},
}

# Mapeamento de Climas para emojis
CLIMAS = {
    "Ensolarado": "☀️",
    "Nublado": "☁️",
    "Ventoso": "🌬️",
    "Chuvoso": "🌧️",
    "Crepúsculo": "🌅",
    "Estrelado": "⭐",
    "Outonal": "🍂",
    "Primaveril": "🌸",
}


# ═══════════════════════════════════════════════════════════════
# FUNÇÕES PRINCIPAIS
# ═══════════════════════════════════════════════════════════════

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extrai frontmatter YAML do conteúdo Markdown."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return metadata, body
            except yaml.YAMLError as e:
                print(f"⚠️ Erro ao parsear YAML: {e}")
    return {}, content


def parse_yaml_lesson(content: str) -> tuple[dict, str]:
    """Processa arquivo YAML puro de lição (formato SSOT).
    
    Estrutura esperada:
    licao:
      metadados:
        id: MV-S-001
        titulo: "..."
        guardiao_lider: Celeste
        ...
      atmosfera:
        clima: ensolarado
        ...
      jornada:
        concreto: ...
        abstrato: ...
      ...
    """
    try:
        data = yaml.safe_load(content)
        
        # Estrutura da lição está em licao.metadados
        licao = data.get('licao', data)
        
        # Extrair metadata
        metadados = licao.get('metadados', {})
        if not metadados:
            metadados = licao.get('metadata', {})
        
        # Normalizar campos para o template
        metadata = {
            'id': metadados.get('id', 'MV-S-XXX'),
            'titulo': metadados.get('titulo', 'Lição'),
            'guardiao': metadados.get('guardiao_lider', ''),
            'tempo': licao.get('preparacao', {}).get('tempo_licao', '15-20'),
            'clima': licao.get('atmosfera', {}).get('clima', 'Ensolarado'),
            'elo_anterior': licao.get('linkage', {}).get('elo_anterior', {}).get('licao_id'),
            'proximo_passo': licao.get('linkage', {}).get('proximo_passo', {}).get('licao_id'),
        }
        
        # Converter conteúdo para markdown
        body = licao_to_markdown(licao)
        
        return metadata, body
        
    except yaml.YAMLError as e:
        print(f"⚠️ Erro ao parsear YAML: {e}")
        return {}, ""


def licao_to_markdown(licao: dict) -> str:
    """Converte estrutura de lição YAML para Markdown."""
    lines = []
    
    # Para o Portador (CRÍTICO para Débora)
    if 'para_o_portador' in licao:
        pp = licao['para_o_portador']
        lines.append("## 👨‍👩‍👧 Para o Portador\n")
        if pp.get('dica_de_coracao'):
            lines.append(f"> **Dica de Coração:** {pp['dica_de_coracao']}\n")
        if pp.get('o_que_seu_filho_vai_descobrir'):
            lines.append(f"\n**O que seu filho vai descobrir:** {pp['o_que_seu_filho_vai_descobrir']}\n")
        if pp.get('audio_script'):
            lines.append(f"\n🎧 **Áudio-Script:** {pp['audio_script']}\n")
        if pp.get('nota_de_graca'):
            lines.append(f"\n💚 {pp['nota_de_graca']}\n")
    
    # Ideia Viva
    if 'ideia_viva' in licao:
        iv = licao['ideia_viva']
        lines.append(f"\n## 💡 Ideia Viva\n")
        lines.append(f"> **{iv.get('frase', '')}**\n")
        lines.append(f"\n*{iv.get('conceito_matematico', '')}*\n")
    
    # Atmosfera
    if 'atmosfera' in licao:
        atm = licao['atmosfera']
        lines.append(f"\n## 🌤️ Atmosfera\n")
        if atm.get('clima_descricao'):
            lines.append(f"{atm['clima_descricao']}\n")
    
    # Ritual de Abertura
    if 'ritual_abertura' in licao:
        ra = licao['ritual_abertura']
        lines.append(f"\n## 🎬 Ritual de Abertura\n")
        if ra.get('instrucao_ambiente'):
            lines.append(f"\n📍 {ra['instrucao_ambiente']}\n")
        if ra.get('fala_portador', {}).get('script'):
            lines.append(f"\n**Fala do Portador:**\n{ra['fala_portador']['script']}\n")
        if ra.get('fala_guardiao', {}).get('script'):
            lines.append(f"\n**Guardião:**\n{ra['fala_guardiao']['script']}\n")
    
    # Jornada - Narrativa Principal
    if 'jornada' in licao:
        jornada = licao['jornada']
        
        # Abertura Sensorial
        if jornada.get('abertura_sensorial'):
            lines.append(f"\n## 🌳 A Jornada\n")
            lines.append(f"\n{jornada['abertura_sensorial']}\n")
        
        # Narrativa Principal (CRÍTICO - estava faltando)
        if 'narrativa_principal' in jornada:
            np = jornada['narrativa_principal']
            for cena_key, cena in np.items():
                if isinstance(cena, dict) and cena.get('descricao'):
                    lines.append(f"\n### {cena_key.replace('_', ' ').title()}\n")
                    lines.append(f"{cena['descricao']}\n")
                    if cena.get('instrucao_portador'):
                        lines.append(f"\n📝 *{cena['instrucao_portador']}*\n")
        
        # Concreto
        if 'concreto' in jornada:
            c = jornada['concreto']
            lines.append(f"\n## 🎯 Atividade Concreta (60%+)\n")
            lines.append(f"\n{c.get('descricao', '')}\n")
            if c.get('instrucoes_portador'):
                lines.append("\n### Passos:\n")
                for p in c['instrucoes_portador']:
                    passo = p.get('passo', p.get('acao', ''))
                    acao = p.get('acao', '')
                    fala = p.get('fala_sugerida', '')
                    lines.append(f"- **{acao}:** {fala}\n")
            if c.get('adaptacao_bernardo'):
                lines.append(f"\n{c['adaptacao_bernardo']}\n")
        
        # Abstrato
        if 'abstrato' in jornada:
            a = jornada['abstrato']
            lines.append(f"\n## 🔢 Abstrato (Mínimo)\n")
            lines.append(f"\n{a.get('descricao', '')}\n")
    
    # Narração
    if 'narracao' in licao:
        n = licao['narracao']
        lines.append(f"\n## 📖 Narração\n")
        lines.append(f"\n{n.get('pergunta_principal', '')}\n")
        if n.get('perguntas_do_coracao'):
            lines.append("\n**Perguntas do Coração:**\n")
            for q in n['perguntas_do_coracao']:
                lines.append(f"- {q}\n")
    
    # Fechamento
    if 'ritual_fechamento' in licao:
        rf = licao['ritual_fechamento']
        lines.append(f"\n## 🏁 Fechamento\n")
        if rf.get('fala_guardiao', {}).get('script'):
            lines.append(f"\n{rf['fala_guardiao']['script']}\n")
        if rf.get('fio_de_ouro'):
            lines.append(f"\n🧵 **Fio de Ouro:** {rf['fio_de_ouro']}\n")
    
    # Sugestões dos Guardiões
    if 'sugestoes' in licao:
        lines.append(f"\n## 🦊 Dicas dos Guardiões\n")
        for s in licao['sugestoes']:
            emoji = s.get('emoji', '💡')
            guardiao = s.get('guardiao', '')
            dica = s.get('dica', '')
            lines.append(f"\n{emoji} **{guardiao}:** {dica}\n")
    
    return "\n".join(lines)


def convert_admonitions(content: str) -> str:
    """Converte admonitions GitHub para HTML."""
    patterns = {
        r'> \[!IMPORTANT\]\n> (.+?)(?=\n\n|\n>|\Z)': 
            '<div class="admonition important"><span class="icon">⚠️</span><div class="content">\\1</div></div>',
        r'> \[!NOTE\]\n> (.+?)(?=\n\n|\n>|\Z)': 
            '<div class="admonition note"><span class="icon">📝</span><div class="content">\\1</div></div>',
        r'> \[!TIP\]\n> (.+?)(?=\n\n|\n>|\Z)': 
            '<div class="admonition tip"><span class="icon">💡</span><div class="content">\\1</div></div>',
        r'> \[!CAUTION\]\n> (.+?)(?=\n\n|\n>|\Z)': 
            '<div class="admonition caution"><span class="icon">🚫</span><div class="content">\\1</div></div>',
        r'> \[!RITUAL\]\n> (.+?)(?=\n\n|\n>|\Z)': 
            '<div class="admonition ritual"><span class="icon">🕯️</span><div class="content">\\1</div></div>',
    }
    
    for pattern, replacement in patterns.items():
        content = re.sub(pattern, replacement, content, flags=re.DOTALL | re.MULTILINE)
    
    return content


def convert_cards(content: str, card_path: str) -> str:
    """Converte [CARD: NOME] para HTML de card."""
    def replace_card(match):
        card_type = match.group(1).upper()
        
        if card_type in GUARDIOES:
            g = GUARDIOES[card_type]
            return f'''
<div class="guardian-card" style="border-color: {g['cor']}">
    <img src="{card_path}/{g['img']}" alt="{card_type}" />
    <span class="guardian-emoji">{g['emoji']}</span>
    <span class="guardian-name">{card_type.title()}</span>
</div>'''
        else:
            return f'<div class="object-card">[{card_type}]</div>'
    
    return re.sub(r'\[CARD:\s*(\w+)\]', replace_card, content)


def convert_clima_emoji(content: str, clima: str) -> str:
    """Substitui descrições de clima por emoji."""
    emoji = CLIMAS.get(clima, "☀️")
    # Adiciona emoji no início de parágrafos que descrevem cenário
    content = re.sub(
        r'(\*\[.+cenário.+\]\*)',
        f'{emoji} \\1',
        content,
        flags=re.IGNORECASE
    )
    return content


def markdown_to_html(content: str) -> str:
    """Converte Markdown básico para HTML."""
    # Headers
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    
    # Bold e Italic
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    
    # Code inline
    content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)
    
    # Listas
    content = re.sub(r'^- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'(<li>.+</li>\n)+', r'<ul>\g<0></ul>', content)
    
    # Checkboxes
    content = re.sub(r'\[ \]', '☐', content)
    content = re.sub(r'\[x\]', '☑', content)
    
    # Parágrafos
    content = re.sub(r'\n\n', '</p><p>', content)
    content = f'<p>{content}</p>'
    
    # Limpar tags vazias
    content = re.sub(r'<p>\s*</p>', '', content)
    
    return content


def generate_navigation(metadata: dict) -> str:
    """Gera HTML de navegação anterior/próximo."""
    nav = '<nav class="lesson-nav">'
    
    if metadata.get('elo_anterior'):
        prev_id = metadata.get('link_anterior', metadata.get('elo_anterior', ''))
        nav += f'<a href="{prev_id}.html" class="nav-prev">← Anterior</a>'
    
    nav += '<a href="index.html" class="nav-home">🏠 Início</a>'
    
    if metadata.get('proximo_passo'):
        next_id = metadata.get('link_proximo', metadata.get('proximo_passo', ''))
        nav += f'<a href="{next_id}.html" class="nav-next">Próximo →</a>'
    
    nav += '</nav>'
    return nav


def generate_html(metadata: dict, body: str, template: str) -> str:
    """Gera HTML final a partir do template."""
    # Processar corpo
    body = convert_admonitions(body)
    body = convert_cards(body, CONFIG["CARD_IMG_PATH"])
    
    if metadata.get('clima'):
        body = convert_clima_emoji(body, metadata['clima'])
    
    body = markdown_to_html(body)
    
    # Gerar navegação
    nav = generate_navigation(metadata)
    
    # Substituir placeholders no template
    html = template
    html = html.replace("{{TITULO}}", metadata.get('titulo', 'Lição'))
    html = html.replace("{{ID}}", metadata.get('id', 'MV-S-XXX'))
    html = html.replace("{{GUARDIAO}}", metadata.get('guardiao', ''))
    html = html.replace("{{TEMPO}}", str(metadata.get('tempo', '15-20')))
    html = html.replace("{{CLIMA}}", metadata.get('clima', 'Ensolarado'))
    html = html.replace("{{CONTEUDO}}", body)
    html = html.replace("{{NAVEGACAO}}", nav)
    html = html.replace("{{DATA}}", datetime.now().strftime("%Y-%m-%d"))
    
    return html


def process_lesson(input_path: Path, output_dir: Path, template: str) -> bool:
    """Processa uma lição individual (MD ou YAML)."""
    try:
        content = input_path.read_text(encoding='utf-8')
        
        # Detectar formato: YAML puro ou Markdown com frontmatter
        if input_path.suffix.lower() in ['.yaml', '.yml']:
            metadata, body = parse_yaml_lesson(content)
            print(f"📄 Processando YAML: {input_path.name}")
        else:
            metadata, body = parse_frontmatter(content)
        
        if not metadata:
            print(f"⚠️ Sem metadata: {input_path.name}")
            return False
        
        html = generate_html(metadata, body, template)
        
        # Nome do arquivo de saída
        output_name = input_path.stem + ".html"
        output_path = output_dir / output_name
        
        output_path.write_text(html, encoding='utf-8')
        print(f"✅ Gerado: {output_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ Erro em {input_path.name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="🔨 Gutenberg Forja — MD → HTML")
    parser.add_argument("--input", "-i", required=True, help="Diretório de entrada (MD)")
    parser.add_argument("--output", "-o", default=CONFIG["OUTPUT_DIR"], help="Diretório de saída (HTML)")
    parser.add_argument("--template", "-t", default=CONFIG["TEMPLATE_HTML"], help="Template HTML base")
    
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    output_dir = Path(args.output)
    
    if not input_dir.exists():
        print(f"❌ Diretório não encontrado: {input_dir}")
        return
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Carregar template
    template_path = Path(__file__).parent / args.template
    if template_path.exists():
        template = template_path.read_text(encoding='utf-8')
    else:
        template = DEFAULT_TEMPLATE
    
    # Processar lições YAML apenas (SSOT)
    yaml_files = list(input_dir.glob("*.yaml")) + list(input_dir.glob("*.yml"))
    print(f"\n🔨 Gutenberg Forja v2.0 (YAML-Only) — Processando {len(yaml_files)} lições\n")
    
    success = 0
    for yaml_file in sorted(yaml_files):
        if process_lesson(yaml_file, output_dir, template):
            success += 1
    
    print(f"\n✅ Concluído: {success}/{len(yaml_files)} lições YAML geradas em {output_dir}\n")


# ═══════════════════════════════════════════════════════════════
# TEMPLATE PADRÃO (usado se não houver arquivo externo)
# ═══════════════════════════════════════════════════════════════

DEFAULT_TEMPLATE = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITULO}} — Matemática Viva</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="lesson-page clima-{{CLIMA}}">
    <header class="lesson-header">
        <span class="lesson-id">{{ID}}</span>
        <h1>{{TITULO}}</h1>
        <div class="lesson-meta">
            <span class="guardian">👤 {{GUARDIAO}}</span>
            <span class="time">⏱️ {{TEMPO}} min</span>
            <span class="clima">{{CLIMA}}</span>
        </div>
    </header>
    
    {{NAVEGACAO}}
    
    <main class="lesson-content">
        {{CONTEUDO}}
    </main>
    
    {{NAVEGACAO}}
    
    <footer class="lesson-footer">
        <p>Matemática Viva • Template V4.1 • {{DATA}}</p>
    </footer>
</body>
</html>'''


if __name__ == "__main__":
    main()
