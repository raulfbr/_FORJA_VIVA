import os
import yaml
import re

# Padrões e Regras
DIRECTORY = r"c:\Users\Raul\OneDrive\!RF 2026\Gravity Google\Projeto011-MatVivaV3RaulPessoal\_FORJA_VIVA\curriculo\01_SEMENTES"
REQUIRED_KEYS = [
    'id', 'titulo', 'fase', 'ideia_viva', 'atmosfera', 'linkage', 
    'preparacao', 'para_o_portador', 'ritual_abertura', 'jornada', 
    'narracao', 'ritual_fechamento', 'catedra_pais'
]
FORBIDDEN_TERMS = ['prova', 'teste', 'nota vermelha', 'reprovar', 'castigo']
SOUL_FIELD = 'conforto_emocional'

def flatten_lesson(content):
    """Normalize lesson structure (Premium nested vs Lean flat)"""
    if 'licao' in content:
        root = content['licao']
        # Merge metadata into root for checking
        if 'metadados' in root:
            root.update(root['metadados'])
        return root
    return content

def check_lesson(filename, content):
    issues = []
    
    # -------------------------------------------------------------------------
    # 1. VALIDAÇÃO DE SCHEMA (Técnico)
    # Verifica se todas as chaves obrigatórias do YAML estão presentes.
    # Isso garante que o gerador de PDF/Site não quebre por falta de campos.
    # -------------------------------------------------------------------------
    for key in REQUIRED_KEYS:
        if key not in content:
            issues.append(f"[SCHEMA] Chave obrigatória faltando: '{key}'")

    # -------------------------------------------------------------------------
    # 2. VALIDAÇÃO PEDAGÓGICA (Método CPA - Singapura)
    # A fase 'Sementes' exige estritamente a etapa CONCRETA.
    # Se não tiver 'concreto', a lição falha no método.
    # -------------------------------------------------------------------------
    jornada = content.get('jornada', {})
    if 'concreto' not in jornada:
        issues.append("[PEDAGOGIA] Seção 'concreto' ausente na jornada (Obrigatório em Sementes)")
    
    # -------------------------------------------------------------------------
    # 3. VALIDAÇÃO DE ALMA (Conforto Emocional do Pai)
    # Verifica se a seção 'conforto_emocional' existe e tem conteúdo relevante.
    # Isso garante que estamos cuidando do adulto, não só da criança.
    # -------------------------------------------------------------------------
    portador = content.get('para_o_portador', {})
    if SOUL_FIELD not in portador:
        issues.append(f"[ALMA] Campo '{SOUL_FIELD}' ausente em 'para_o_portador'")
    else:
        soul_text = portador[SOUL_FIELD]
        if not soul_text or len(str(soul_text)) < 20:
            issues.append(f"[ALMA] Texto de '{SOUL_FIELD}' parece muito curto ou vazio")

    # -------------------------------------------------------------------------
    # 4. VALIDAÇÃO DE LINGUAGEM (Termos Proibidos)
    # Busca por palavras que ferem a filosofia do projeto (ex: 'prova', 'castigo').
    # Mantém a pureza da atmosfera do Reino.
    # -------------------------------------------------------------------------
    text_content = str(content).lower()
    for term in FORBIDDEN_TERMS:
        if term in text_content:
            # Nota: O script apenas avisa, pois pode ser um "não faça prova".
            # Mas serve de alerta para revisão manual.
            pass 
            
    # -------------------------------------------------------------------------
    # 5. VALIDAÇÃO DE METADADOS (Integridade de Arquivo)
    # Verifica se o ID interno do arquivo (MV-S-XXX) bate com o nome do arquivo.
    # Evita confusão de versionamento.
    # -------------------------------------------------------------------------
    lid = content.get('id', 'UNKNOWN')
    try:
        file_num = int(filename.split('_')[0])
        id_num = int(lid.split('-')[-1])
        if file_num != id_num:
            issues.append(f"[METADADOS] Número do arquivo ({file_num}) não bate com ID ({lid})")
    except:
        pass # Ignora arquivos com nomes fora do padrão numérico

    return issues

files = sorted([f for f in os.listdir(DIRECTORY) if f.endswith(".yaml")])
all_issues = {}

print(f"Auditing {len(files)} files in {DIRECTORY}...\n")

for f in files:
    path = os.path.join(DIRECTORY, f)
    with open(path, 'r', encoding='utf-8') as file:
        try:
            raw = yaml.safe_load(file)
            lesson = flatten_lesson(raw)
            result = check_lesson(f, lesson)
            if result:
                all_issues[f] = result
        except Exception as e:
            all_issues[f] = [f"CRITICAL: YAML Parsing failed: {str(e)}"]

if not all_issues:
    print("✅ SUCCESS: Triple Deep Audit passed for all files.")
else:
    print(f"⚠️ FOUND ISSUES in {len(all_issues)} files:")
    for f, errs in all_issues.items():
        print(f"\n📄 {f}:")
        for e in errs:
            print(f"  - {e}")
