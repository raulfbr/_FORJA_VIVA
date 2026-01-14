# 🦁 CONSELHO DOS SÁBIOS: REVISÃO DE PLANEJAMENTO (ESTAÇÃO 2)
Data: 14/01/2026 | Foco: Impecabilidade & Alinhamento

## 1. A Voz da Matriarca (Charlotte Mason) - Pedagogia & Atmosfera
> *"A educação é uma atmosfera, uma disciplina, uma vida."*

*   **Crítica:** O plano de produção "em lotes" (L016-L020) corre o risco de se tornar mecânico.
*   **Veto/Ajuste:** Exijo que cada lote tenha uma **"Ideia Viva"** central definida antes da produção. Não podemos apenas preencher YAMLs.
*   **Check de Atmosfera:** A Estação 2 é sobre "Ritmo". As lições devem refletir o ciclo (dia/noite, estações). O plano precisa explicitar como essa *narrativa* será tecida (não apenas "títulos").

## 2. A Voz do Mestre (Jerome Bruner) - Método CPA
> *"Qualquer assunto pode ser ensinado a qualquer criança... se for honesto."*

*   **Crítica:** Vamos introduzir **Adição**. Isso é perigoso se for abstrato.
*   **Exigência:** O script de validação (`deep_audit`) DEVE verificar não apenas a presença de `concreto`, mas a presença de palavras-chave como "juntar", "agrupar", "feixe" na seção concreta.
*   **Alerta:** As imagens (Pictórico) são cruciais agora. O plano técnico menciona "copiar imagens", mas não *como* elas validam o conceito.

## 3. A Voz da Engenharia (Code & Architecture) - A Estrutura
> *"Clean Code, Clean Soul."*

*   **Falha Identificada:** O `implementation_plan.md` diz "Integrar assets", mas o código atual do Dashboard usa **Emojis** (`🦁`).
*   **Gap Técnico:** A estrutura de pastas em `docs/cards/web` possui subpastas (`guardioes/`, `numeros/`). O script `shutil.copytree` preservará isso.
*   **Correção Necessária:** Precisamos atualizar o `tools/build_dashboard.py` (e talvez `tools/build_lessons.py`) para substituir a lógica de Emojis por tags `<img>` apontando para `assets/cards/guardioes/{nome_normalizado}.webp`.
*   **Risco:** Se o nome do guardião no YAML ("Melquior") não bater com o arquivo ("melquior.webp"), a imagem quebrará. Precisamos de uma **função de normalização** robusta.

## 4. O Veredito do Orchestrator
**Estado Atual:** ⚠️ APROVADO COM RESSALVAS.
**Ação Imediata:**
1.  Refinar `implementation_plan.md` para incluir a refatoração do HTML (Emoji -> Imagem).
2.  Adicionar passo de "Normalização de Nomes" no script.
3.  Atualizar `task.md` para explicitar a tarefa de "Refatoração Visual (Img vs Emoji)".

---
*Assinado: Orchestrator v1.2*
