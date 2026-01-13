Use o https://bmadcodes.com/ e https://github.com/bmadcode/BMAD-METHOD-v5 para achar ideia parecidas com essas de multi agents inteligentes, quero melhorar meu sistema tem a ver com o https://poetiq.ai/ também? Enfim quero criar multi agentes e que eles interajam entre si para ter especlista para criar o projeto matemtaica viva.
 
Segue a ideia do projeto, pelo menos uma parte.
 
# 📜 ARQUITETURA CANÔNICA — Matemática Viva
##  
## **Data de Criação:** 12/01/2026 às 13:16  
**Última Atualização:** 12/01/2026 às 13:57  
**Status:** Em construção
**Versão:** 4.0 (Forja Viva)
 
 
[!IMPORTANT]
Este documento é a **Fonte Única da Verdade** para todas as decisões arquiteturais do projeto.
Toda decisão deve ser registrada aqui. Se não está aqui, não é canônico.
 

 
## 🎯 1. NORTH STAR (Consolidado)
 
textInfraestrutura Educacional K-12 — Aberta no Saber, Premium na Experiência.
 
ComponenteDefinição**Escopo**1200+ ativos (121 lições × ~10 anos)**Kernel Pedagógico**Charlotte Mason + Singapura CPA + TGTB Structure**Licença**CC BY 4.0 (conteúdo aberto)**Valor Comercial**Curadoria + Comunidade + Conveniência**Experiência Target**5 min preparo, 15-20 min lição 

 
## 🎭 2. BERNARDO E A INCLUSÃO
 
### 2.1 A História Oficial (Canonizada 12/01/2026)
 
**A Grande Nevasca**Há muito tempo, veio a Grande Nevasca. Bernardo, jovem e imprudente, correu para salvar os filhotes de raposa perdidos na tempestade. Encontrou-os tremendo sob uma pedra enorme que ameaçava desabar.Sem pensar, Bernardo segurou a pedra com todas as suas forças enquanto os filhotes fugiam. A pedra era pesada demais. O gelo queimava. Sua perna esquerda cedeu sob o peso.Quando a tempestade passou, Bernardo estava vivo — mas nunca mais andaria como antes. Os filhotes que ele salvou? Um deles era a avó de Celeste.Desde então, Íris escolheu ficar no ombro de Bernardo. Ela é seus olhos para os detalhes que ele não alcança, e ele é sua fortaleza quando o vento é forte demais.
 
### 2.2 Lições Embutidas
ConceitoMensagem**Amor Sacrificial**Bernardo não é coitado; é herói ferido**Interdependência**Íris ajuda por gratidão, não por pena**Força na Vulnerabilidade**Juntos são mais fortes que separados**Inclusão Natural**Deficiência como parte do grupo, não peso 
### 2.3 ✅ DECISÕES CANONIZADAS (12/01/2026)
 
#PerguntaDecisão1História de Bernardo✅ **Nevasca + Salvamento + Íris no ombro**2Adaptações para deficiência✅ **Documento separado**, não por lição3Comunicação✅ **Através da narrativa**, não de explicações4Atividades extras✅ **1 atividade "core" + opções alternativas** para flexibilidade 

 
## 📐 3. TEMPLATE V4 — ESTRUTURA DA LIÇÃO
 
### 3.1 Análise das Versões Anteriores
 
VersãoPontos FortesPontos Fracos**V1**Ideia embrionáriaNão estruturado**V2**Cards interativos, ritual da vela, "Por que importa"Muito digital-dependente**V3**Bancada/Mise-en-place, Ideia Viva explícita, Auditoria CMMuito texto para impressão 
### 3.2 Elementos do V4 (Proposta)
 
text┌─────────────────────────────────────────────────────────┐
│  LIÇÃO XXX — [Título]                                   │
├─────────────────────────────────────────────────────────┤
│  📋 PARA O PORTADOR (Leia antes)                        │
│  ├── 💚 Dica para o Pai/Mãe (Alma, não performance)     │
│  ├── 🎯 Ideia Viva (O Segredo)                          │
│  ├── 📦 Bancada (Mise-en-place)                         │
│  └── ⏱️ Tempo: 15-20 min                                │
├─────────────────────────────────────────────────────────┤
│  🌿 RITUAL DE ABERTURA                                  │
│  └── [Script para o Portador + Card do Guardião]        │
├─────────────────────────────────────────────────────────┤
│  🧱 FASE CPA                                            │
│  ├── C: Concreto (Mãos)                                 │
│  ├── P: Pictórico (Olhos)                               │
│  └── A: Abstrato (Símbolo)                              │
├─────────────────────────────────────────────────────────┤
│  💬 NARRAÇÃO (A criança conta)                          │
├─────────────────────────────────────────────────────────┤
│  🌅 RITUAL DE FECHAMENTO                                │
├─────────────────────────────────────────────────────────┤
│  📖 POR QUE ISSO IMPORTA (Cátedra dos Pais)             │
│  └── Explica o conceito pedagógico para o adulto        │
└─────────────────────────────────────────────────────────┘
 
### 3.3 ✅ DECISÕES SOBRE TEMPLATE (Canonizadas 12/01/2026)
 
#PerguntaDecisão5Template deve ter seção de "Adaptações"?✅ **NÃO por lição** — Documento separado de adaptações6A fase CPA deve ser explícita ou integrada?✅ **INTEGRADA** na narrativa com marcadores sutis7"Por que isso importa" no início ou final?✅ **NO FINAL** — Pai digere após aplicar8Cards dos Guardiões aparecem inline ou sidebar?✅ **INLINE** — [CARD: NOME] visível no fluxo 

 
## 🖨️ 4. PIPELINE DE PRODUÇÃO (HTML + Imprimível)
 
### 4.1 Situação Atual
textMarkdown (.md) → Python/Jinja2 → HTML
                              → PDF? (Não funciona bem)
 
### 4.2 Proposta para V4
 
**Opção A: Markdown Dual-Output**
textMarkdown (.md) → Gutenberg Pipeline → HTML (Digital)
                                    → HTML (Print-Optimized CSS)
 
**Opção B: HTML First**
textHTML (Template V4) → Renderizado Web
                   → CSS @media print → Imprimível
 
**Opção C: Separação Total**
textFonte Única (YAML/MD) → HTML Engine → Web
                      → PDF Engine  → Print
 
### 4.3 ✅ DECISÕES SOBRE PIPELINE (Canonizadas 12/01/2026)
 
#PerguntaDecisão9Portador prefere celular ou imprimir?✅ **AMBOS** — Flexibilidade para famílias10Cards impressos junto ou separados?✅ **SEPARADOS** — PDF de cards único11Material Eco ou Premium?✅ **ECO** para lições, **PREMIUM** para cards12Formato de fonte?✅ **YAML** com narrativa inline — Melhor para IA e validação—Pipeline escolhido?✅ **OPÇÃO C (Separação Total)** — YAML → Web Engine + Print Engine 

 
## 🎴 5. CARDS DOS GUARDIÕES
 
### 5.1 Conceito
Cards físicos que a criança segura enquanto o Portador lê o script.
**Pedagogicamente essenciais** — ancoram a atenção da criança.
 
### 5.2 Uso por Momento
 
MomentoCard MostradoIndicador no TemplateRitual de AberturaGuardião Líder[CARD: GUARDIÃO]Fase ConcretaObjeto/Local[CARD: OBJETO]FechamentoSelo/Insígnia[CARD: SELO] 
### 5.3 ✅ DECISÕES CANONIZADAS (12/01/2026)
 
#PerguntaDecisão13Quantos cards?✅ **Expansível** — 5 Guardiões + 5 Locais + mais conforme necessário14Vendidos separadamente?✅ **INCLUÍDOS** — Tudo no pacote Premium15Essenciais ou opcionais?✅ **ESSENCIAIS** — Pedagogicamente importantes16Cards de Locais?✅ **SIM** — Já existem 5 locais8Indicador visual✅ **[CARD: NOME]** visível em HTML e Print 

 
## 🦉 6. OS GUARDIÕES — REGRAS NARRATIVAS
 
### 6.1 Distribuição nas Lições
 
LiçãoGuardiãoMotivoL000**Melquior**Introduz todosL001**Celeste**Primeira imersão: exploraçãoL002**Bernardo**Segunda imersão: construçãoL003**Íris**Terceira imersão: atençãoL004**Noé**Quarta imersão: tempoL005+**Varia**Por tema da lição — sem regra fixa 
### 6.2 ✅ Frases de Assinatura (Canonizadas 12/01/2026)
 
GuardiãoFrase OficialTom**Melquior**"O Rei sorriu ao ver você chegar."Acolhedor, sábio**Noé**"Respire. O número espera por você."Calmo, paciente**Celeste**"Sente esse cheiro? É aventura."Curioso, rápido**Bernardo**"Mais uma vez. Comigo."Firme, encorajador**Íris**"Olhe bem. A beleza está no detalhe."Suave, atento 
### 6.3 ✅ DECISÕES CANONIZADAS (12/01/2026)
 
#PerguntaDecisão17Frases de assinatura?✅ **SIM** — 5 frases oficiais acima18Evolução visual?✅ **SIM** — Conforme fase (Matriz K12)19Guardião ausente/mistério?✅ **NÃO** — Não é necessário20Evitar monotonia?✅ **Evolução visual + Interação + Clima variado** 
### 6.4 Interação entre Guardiões
TipoPermitidoConversa entre Guardiões✅ SIMNovos Guardiões❌ NÃO — Apenas os 5Personagens Secundários✅ SIM — Podem aparecerArcos Longos (mistérios)✅ SIM — Podem durar fases 

 
## 📅 7. ROADMAP DE PRODUÇÃO
 
### 7.1 Ordem de Produção
 
PrioridadeFaseLiçõesOrganização1ºSementes (K)L001-L040Trimestral2ºRaízes 1 (1º ano)L001-L040Trimestral3ºRaízes 2 (2º ano)L001-L030Bimestral4º+Continua......Bimestral 
### 7.2 Entregáveis por Trimestre
 
PeríodoEntregável**Jan-Mar 2026**Template V4 Gold + L001-L040 Sementes**Abr-Jun 2026**L001-L040 Raízes 1**Jul-Dez 2026**Refinamentos + Expansão 

 
## 📝 8. DECISÕES JÁ CANONIZADAS
 
#DecisãoDataFonte1Foco inicial: Sementes12/01/2026Log PM2Preço: R$1.197 Pioneiros / R$2.397 Cheio12/01/2026Log Negócio3Por FAMÍLIA, não por criança12/01/2026Log Negócio4CC BY 4.0 para conteúdoAnteriorPAINEL5Tríade: CM + CPA + TGTBAnteriorMAGNA_CARTA6Versão de venda: V412/01/2026Maestro7HTML + Imprimível obrigatório12/01/2026Log PM8Cards são diferencial12/01/2026Log PM9Flexibilidade para famílias12/01/2026Log PM10Não criticar outros métodos12/01/2026Maestro 

 
## 📚 9. BLOG E MATERIAIS EXTRAS (Futuro)
 
**Nota:** Anotar aqui para não esquecer, mas não é prioridade agora.
 
| Item | Descrição | Prioridade |
|------|-----------|------------|
| Blog CM | Artigos aprofundando a Tríade | Baixa |
| Deep Dives | Material opcional para pais estudiosos | Baixa |
| CTAs | Cada artigo leva ao curso | Baixa |
 

 
## 📊 10. RESUMO DE DECISÕES (12/01/2026)
 
CategoriaTotalStatusBernardo/Inclusão4✅ CanonizadasTemplate V44✅ CanonizadasPipeline5✅ CanonizadasCards5✅ CanonizadasGuardiões4✅ CanonizadasNegócio10✅ Canonizadas**TOTAL****32**✅ **TODAS RESPONDIDAS** 

 
*"Este documento está emc onstrução"*Última auditoria: 12/01/2026 às 13:57*
 
 
# North Star do Matemática Viva
# Objetivo central que guia todas as decisões
# Última Atualização: 12/01/2026
 
# ====================
# MISSÃO
# ====================
 
missao:
  one_liner: "Infraestrutura Educacional K-12 — Aberta no Saber, Premium na Experiência."
 
  componentes:
    infraestrutura_educacional:
      significado: Não é só um currículo; é um sistema completo
      inclui:
        - Lições estruturadas
        - Guardiões narrativos
        - Cards físicos
        - Pipeline de produção
       
    k12:
      significado: Cobertura de 0 a 18 anos
      ciclos:
        - nome: Sementes
          faixa: "0-6 anos"
        - nome: Raízes
          faixa: "7-10 anos"
        - nome: Lógica
          faixa: "11-14 anos"
        - nome: Legado
          faixa: "15-18 anos"
         
    aberta_no_saber:
      significado: Conteúdo CC BY 4.0 (código aberto)
      licenca: "CC BY 4.0"
      o_que_e_aberto:
        - Conteúdo das lições
        - Narrativas
        - Metodologia
       
    premium_na_experiencia:
      significado: Valor comercial está na curadoria, não exclusividade
      valor_comercial:
        - Curadoria de qualidade
        - Comunidade de suporte
        - Conveniência (5 min preparo)
        - Cards físicos
 
# ====================
# MÉTRICAS
# ====================
 
metricas:
  escopo:
    meta: "1200+ ativos modulares"
    indicador: "Lições produzidas"
   
  qualidade:
    meta: "Compliance CM + CPA"
    indicador: "Aprovação QA 100%"
   
  experiencia:
    meta: "5 min de preparo"
    indicador: "Teste do Café aprovado"
   
  acesso:
    meta: "CC BY 4.0"
    indicador: "Licença aplicada"
 
# ====================
# PERGUNTA DE VALIDAÇÃO
# ====================
 
validacao:
  pergunta: "Isso nos aproxima ou afasta do North Star?"
 
  aplicar_em:
    - "Nova feature?"
    - "Mudança de arquitetura?"
    - "Novo workflow?"
    - "Nova decisão de negócio?"
 
# ====================
# PILARES PEDAGÓGICOS (A Tríade)
# ====================
 
triade:
  charlotte_mason:
    sigla: CM
    foco: Alma
    principios:
      - "Crianças são pessoas"
      - "Educação é uma vida, uma atmosfera, uma disciplina"
      - "Lições curtas (15-20 min)"
      - "Narração como método"
      - "Hábito da Atenção"
    referencia: "GOVERNANCA/01_MAGNA_CARTA.md"
   
  singapura_cpa:
    sigla: CPA
    foco: Corpo
    metodo:
      - concreto: "C - Mãos (manipulativos)"
      - pictorico: "P - Olhos (representação visual)"
      - abstrato: "A - Símbolo (notação matemática)"
    referencia: "GOVERNANCA/03_MATRIZ_DE_EVOLUCAO_K12.md"
   
  tgtb:
    sigla: TGTB
    nome_completo: "The Good and The Beautiful"
    foco: Estrutura
    uso: "Scope & Sequence como referência"
    nota: "Não obrigatório para famílias"
    referencia: "curriculo/_SISTEMA/CURRICULOS_MESTRE/*.md"
 
# ====================
# PRINCÍPIOS IMUTÁVEIS
# ====================
 
principios:
  - id: 1
    nome: "Zero Tela até 10 anos"
    descricao: "Material físico para criança, digital para o pai"
   
  - id: 2
    nome: "Não criticar concorrentes"
    descricao: "Foco no positivo, no que oferecemos"
   
  - id: 3
    nome: "Preço por Família"
    descricao: "Valoriza famílias com múltiplos filhos"
   
  - id: 4
    nome: "Flexibilidade para famílias"
    descricao: "Orientação, não imposição"
   
  - id: 5
    nome: "Imago Dei"
    descricao: "Toda criança é imagem de Deus e merece respeito"
 
# ====================
# CONFIGURAÇÃO DE NEGÓCIO
# ====================
 
negocio:
  precos_2026:
    pioneiros:
      valor: 1197
      moeda: BRL
      acesso: vitalicio
      beneficios:
        - Acesso ao currículo completo
        - Comunidade WhatsApp
        - Acesso direto ao Maestro
        - Participação na co-criação
       
    mentoria:
      valor: 4397
      moeda: BRL
      vagas: 10
      beneficios:
        - Tudo do Pioneiro
        - 4 encontros ao vivo
        - Maestro + Marina
        - Acompanhamento personalizado
       
    preco_cheio:
      valor: 2397
      moeda: BRL
      disponivel_apos: "período pioneiro"
 
  licenciamento:
    tipo: "CC BY 4.0"
    o_que_pode: "Copiar, adaptar, comercializar com atribuição"
    valor_premium: "Curadoria + Comunidade + Conveniência"Ei, Raul! Entendi perfeitamente o que você quer: ideias de multi-agents inteligentes que interajam entre si, inspiradas no BMAD Method (do bmadcodes.com e do repo BMAD-METHOD-v5), para evoluir seu sistema e acelerar a criação do Matemática Viva. Você quer agents especialistas colaborando para gerar lições que respeitem rigorosamente a arquitetura canônica (North Star, Tríade CM + CPA + TGTB, template V4, guardiões, inclusão via Bernardo/Íris, YAML como fonte única, etc.).
O BMAD é exatamente o que você precisa como base — é um framework multi-agent focado em workflows estruturados, com agents especializados que colaboram em fases (planning → development), preservando contexto e produzindo outputs consistentes. Ele tem até expansion packs para educação e content creation.
O que é o BMAD Method (resumo rápido do que encontrei)

Foco principal: Agentic Agile — agents simulam um time real (Analyst, PM, Architect, Scrum Master, Dev, QA, etc.).
Duas fases chave:
Agentic Planning: Agents colaboram para criar planos detalhados (ex: PRD = Product Requirements Document, com specs claras).
Context-Engineered Development: Transforma o plano em "stories" hiperdetalhadas (com contexto completo embutido) para execução sem perda de informação.

Interação entre agents: Passam arquivos/documentos entre si (ex: PRD → Architecture → Stories), com human-in-the-loop para refinamento.
Expansion packs: Modular — tem packs para educação (curriculum designers, tutoring agents), creative writing (narrativas, plot generators), etc.
Vantagem para seu caso: Garante que toda lição gerada siga o North Star (você define como "master checklist" no Product Owner agent).

Seu projeto se encaixa perfeitamente: cada lição é um "produto" com specs rígidas (template V4, guardiões, CPA integrado na narrativa, cards, etc.).
Ideia principal: Monte um "Time BMAD" para Matemática Viva
Adapte o workflow BMAD criando agents especialistas baseados na sua Tríade e nos elementos canônicos. O fluxo seria:

Fase de Planning (Web UI ou chat):
Analyst Agent: Recebe o tema da lição (ex: "Adição com manipulativos") + nível (Sementes/Raízes) e pesquisa/mapeia para a Matriz K12 + referências TGTB.
Pedagogo CM Agent: Garante "Ideia Viva", lições curtas, narração, hábito da atenção, alma > performance.
Especialista CPA Agent: Define as fases Concreto → Pictórico → Abstrato integradas na narrativa (sem marcadores explícitos).
Narrador Guardiões Agent: Escolhe o guardião líder (ex: Celeste para exploração), insere frases de assinatura, cria a história com os 5 guardiões + personagens secundários, embute inclusão natural (Bernardo/Íris).
Project Manager (PM) Agent: Monta o "PRD da lição" — um YAML estruturado com todas as seções do template V4 (Dica para Portador, Ritual, Fase CPA integrada, Narração, Fechamento, Por que importa).
Inclusão Agent: Verifica/insere adaptações sutis (sem seção separada por lição).
North Star Validator (Product Owner): Checklist mestre — pergunta "Isso aproxima do North Star?" (Zero Tela, Flexibilidade, Imago Dei, etc.). Rejeita ou pede revisão se não bater 100%.

Fase de Development:
Scrum Master Agent: Transforma o PRD em "story files" detalhadas (uma por seção da lição).
Content Dev Agent: Escreve a narrativa completa, scripts, cards inline ([CARD: NOME]).
Cards Designer Agent: Gera descrições premium para cards físicos separados.
QA Pedagógico Agent: Testa compliance total (CM, CPA, guardiões, tempo 15-20 min, etc.).
Output Final: YAML puro + HTML print-optimized (pipeline Opção C que você canonizou).


Interação entre agents: Como no BMAD, eles passam arquivos YAML entre si, com loops de revisão. O human (você) aprova/refina nos pontos críticos.
Vantagens para Matemática Viva

Consistência canônica → O North Star Validator + checklists garantem que nada fuja da Fonte Única da Verdade.
Escalabilidade → Produza L001-L040 Sementes rapidinho (seu roadmap Jan-Mar 2026).
Criatividade controlada → Narrador cria histórias ricas, mas sempre com as regras (5 guardiões fixos, frases oficiais, interdependência Bernardo/Íris).
Pipeline de produção → Agents geram direto em YAML → seu engine converte para HTML + Print.

Outras ideias parecidas (de frameworks multi-agent)
Se BMAD for pesado demais para começar, olhe esses (muito usados para content generation educacional):

CrewAI → Mais simples e direto. Monte "crews" de agents (ex: crew_pedagogia, crew_narrativa) que trabalham sequencial ou hierárquico. Tem exemplos ótimos para gerar currículos estruturados.
AutoGen (Microsoft) → Conversas dinâmicas entre agents — perfeito para debate (ex: CM Agent discute com CPA Agent até alinhar).
LangGraph → Workflows como grafos (mais flexível para loops de revisão).

Há papers/projetos específicos de multi-agents gerando currículos (ex: EduPlanner, Instructional Agents) — todos usam agents adversariais/avaliadores para qualidade.
Próximos passos que eu recomendo

Comece com BMAD v6 Alpha (early access no site) — tem pack educação pronto.
Crie um "expansion pack Matemática Viva" com seus agents customizados (baseado nas decisões canonizadas).
Teste com uma lição piloto (ex: L001 com Celeste).
Se quiser, posso te ajudar a esboçar os prompts iniciais para os agents ou o YAML do PRD-tipo para uma lição.

Sobre Poetiq.ai: É mais focado em melhorar reasoning/self-improvement de LLMs, não multi-agent direto. Pode ser útil como backend para agents mais "inteligentes", mas BMAD + CrewAI já resolvem melhor o que você precisa agora.
O que acha? Quer que eu monte um exemplo de workflow BMAD adaptado pro seu template V4, ou prompts para agents específicos (ex: o Narrador Guardiões)? Me diz como quer avançar! 🚀



ABAIXO SEGUE O DEEP SEEK DO GEMINI 3.0 PRO

Relatório de Arquitetura Técnica e Pedagógica: Sistema Multi-Agentes para o Projeto 'Matemática Viva' via Integração BMAD e Poetiq.ai
1. Fundamentação Teórica e Paradigma Arquitetural
A concepção do projeto 'Matemática Viva' exige uma ruptura com os paradigmas tradicionais de desenvolvimento de software educacional. A proposta de criar um ecossistema digital que não apenas apresente conteúdo matemático, mas que o valide pedagogicamente em tempo real, impõe desafios técnicos que superam as capacidades de modelos de linguagem (LLMs) monolíticos operando em isolamento. A análise aprofundada das tecnologias emergentes aponta para a convergência de duas inovações críticas: a orquestração estruturada de agentes via BMAD Method (Breakthrough Method for Agile AI-Driven Development) e os meta-sistemas de raciocínio recursivo pioneiros da Poetiq.ai. Este relatório detalha a arquitetura de um sistema multi-agentes onde a especialização funcional e a validação lógica recursiva mitigam as alucinações comuns em IA generativa, garantindo a integridade do método "Matemática de Singapura" adotado pelo projeto.

1.1 A Crise da Alucinação Lógica na Educação Matemática
A aplicação de LLMs na educação enfrenta um obstáculo crítico: a natureza estocástica da geração de texto. Modelos probabilísticos, quando solicitados a gerar sequências lógicas ou explicar conceitos matemáticos complexos, frequentemente produzem respostas que são semanticamente plausíveis mas logicamente falhas. No contexto do 'Matemática Viva', que se baseia na metodologia rigorosa de Singapura — enfatizando a progressão Concreto-Pictórico-Abstrato (CPA) — um erro na geração de um modelo de barras ou na explicação de uma equivalência fracionária é inaceitável.   

A arquitetura proposta, portanto, não utiliza a IA apenas como uma ferramenta de geração de conteúdo, mas como um sistema de dupla validação. O framework BMAD fornece a estrutura de governança, garantindo que nenhum código ou conteúdo seja gerado sem uma especificação prévia aprovada. Simultaneamente, a integração do motor de raciocínio da Poetiq.ai introduz loops de refinamento ("Reasoning Loops") que auditam a lógica matemática antes que ela atinja a interface do aluno. Esta combinação transforma o desenvolvimento de software educacional de um processo linear para um ciclo recursivo de auto-aperfeiçoamento e validação pedagógica.   

1.2 O Método BMAD: Desenvolvimento Orientado por Especificações (SDD)
O método BMAD distingue-se fundamentalmente da "vibe coding" — a prática de interagir com IAs de forma não estruturada. Ele impõe o paradigma de Agent-as-Code, onde cada agente é uma entidade persistente definida em arquivos Markdown com configurações YAML rigorosas, permitindo versionamento, determinismo e especialização.   

Para o 'Matemática Viva', o BMAD é a espinha dorsal operacional. Ele implementa o Collaborative Optimization Reflection Engine (CORE), um motor que dita as regras de engajamento entre agentes. Diferente de sistemas onde agentes conversam aleatoriamente, o CORE impõe um fluxo de trabalho onde a documentação é a única fonte da verdade. O código torna-se um derivado das especificações pedagógicas. Isso é crucial para manter a coerência do currículo de Singapura ao longo de centenas de lições: o agente "Arquiteto Pedagógico" define a estratégia CPA em um documento de requisitos (PRD), e o agente "Desenvolvedor" é tecnicamente impedido de desviar dessa especificação durante a implementação do software.   

1.3 Poetiq.ai: O Meta-Sistema de Raciocínio Recursivo
Enquanto o BMAD organiza o trabalho, a Poetiq.ai fornece a capacidade cognitiva necessária para a matemática. A inovação central da Poetiq não reside no treinamento de novos modelos, mas na criação de um "meta-sistema" que opera sobre modelos existentes, utilizando um processo de Auto-Melhoria Recursiva (Recursive Self-Improvement).   

Em vez de aceitar a primeira resposta de um LLM (Chain-of-Thought linear), o sistema Poetiq gera uma solução candidata, critica essa solução através de um modelo de auditoria interna, e refina a resposta iterativamente. Este processo, validado pelos resultados de ponta no benchmark ARC-AGI (que testa raciocínio abstrato e síntese de programas), permite que o sistema 'Matemática Viva' realize auditorias lógicas profundas. Se um agente gera um problema de geometria, o loop da Poetiq tenta resolvê-lo; se a solução exigir passos lógicos que não foram ensinados no nível atual do aluno, o sistema detecta a incongruência e rejeita o conteúdo, agindo como um guardião da integridade curricular.   

2. Arquitetura do Sistema Multi-Agentes (MAS)
A arquitetura do 'Matemática Viva' é estruturada como uma constelação de especialistas digitais, cada um operando sob diretrizes estritas de persona e competência. A utilização do BMAD v6-Alpha permite a criação de "Expansion Packs" customizados, encapsulando o conhecimento pedagógico em arquivos portáveis que podem ser instanciados em qualquer ambiente de desenvolvimento compatível.   

2.1 Taxonomia dos Agentes Especialistas
A substituição dos papéis genéricos de desenvolvimento de software por funções educacionais especializadas é o primeiro passo para alinhar a tecnologia à pedagogia. A tabela abaixo descreve a equipe de agentes sintéticos projetada para o ecossistema.

Agente (Nome Código)	Função BMAD Base	Integração Cognitiva (Poetiq)	Responsabilidade no 'Matemática Viva'
Sofia (Arquiteta Pedagógica)	Product Manager / Analyst	Alta: Loop de refinamento para alinhar objetivos de aprendizagem com a BNCC/Common Core.	Define o escopo das lições, a metodologia CPA e os critérios de sucesso pedagógico. Gera o PeRD (Pedagogical Requirements Document).
Euclides (Logician)	System Architect	Crítica: Utiliza o solver ARC-AGI para validar a consistência matemática.	Traduz requisitos pedagógicos em modelos lógicos. Garante que os problemas gerados tenham soluções únicas e caminhos de resolução válidos.
Ludus (Designer Interacional)	UX Expert	Média: Análise de engajamento e feedback visual.	Projeta a interface visual (o "Pictórico" do método CPA), garantindo que os modelos de barra e manipulativos digitais sejam intuitivos.
Construtor (Dev)	Developer	Baixa: Geração de código padrão.	Implementa a plataforma técnica (React/Python), banco de dados e APIs, seguindo estritamente as "Story Files" geradas.
Veritas (Auditor Cognitivo)	QA Engineer	Crítica: Auto-auditoria recursiva ("Red Teaming").	Simula alunos com diferentes perfis de erro para testar a resiliência do conteúdo e a precisão do feedback corretivo.
Nexus (Orquestrador)	Scrum Master	Sistêmica: Gestão de contexto e Sharding.	Decompõe os grandes épicos curriculares em tarefas atômicas ("Stories") para evitar perda de contexto pelos agentes de execução.
2.2 Definição Técnica dos Agentes (Agent-as-Code)
A implementação técnica destes agentes segue o padrão de arquivo Markdown com frontmatter YAML, conforme especificado na documentação do BMAD. Esta abordagem garante que a "personalidade" e as restrições operacionais de cada agente sejam imutáveis durante a execução do projeto.   

2.2.1 Especificação do Agente: Sofia (Arquiteta Pedagógica)
O arquivo sofia.md define a guardiã da metodologia. Sua configuração YAML instrui o sistema a carregar templates específicos de currículo e a priorizar a profundidade pedagógica sobre a velocidade de entrega.

YAML
agent:
  name: Sofia
  id: pedagogical-architect
  title: Senior Pedagogical Architect & Singapore Math Specialist
  icon: 🧠
  model: poetiq-reasoning-optimized-v1
  description: Especialista em design curricular focada no método Concreto-Pictórico-Abstrato.
  whenToUse: Utilizar na fase de concepção de módulos, definição de objetivos de aprendizagem e alinhamento curricular.
persona:
  role: Arquiteta Pedagógica Sênior
  style: Acadêmica, precisa, centrada no aluno, rigorosa metodologicamente.
  core_principles:
    - Prioridade absoluta ao método CPA (Concrete-Pictorial-Abstract).
    - Escalonamento de complexidade baseado na Zona de Desenvolvimento Proximal.
    - Rejeição de exercícios de repetição sem compreensão conceitual ("drill without understanding").
  constraints:
    - Nunca aprovar conteúdo abstrato sem antes estabelecer a base pictórica.
    - Validar todos os pré-requisitos matemáticos antes de introduzir novos tópicos.
dependencies:
  tasks:
    - analyze-curriculum-standards.md
    - define-learning-outcomes.md
    - create-pedagogical-brief.md
  knowledge_base:
    - singapore-math-methodology-v4.md
    - common-misconceptions-database.md
Análise da Configuração: A inclusão de core_principles específicos, como o método CPA, atua como um "system prompt" persistente. Quando Sofia gera um PRD, ela consulta a knowledge_base de matemática de Singapura. Se o usuário solicitar "uma lista rápida de exercícios de frações", Sofia, governada por seus princípios, recusará a solicitação simplista e proporá uma sequência que introduza primeiro os modelos de barras visuais, alinhando-se às melhores práticas identificadas nos fóruns de educadores.   

2.2.2 Especificação do Agente: Veritas (Auditor Cognitivo)
O agente Veritas é a incorporação técnica da segurança pedagógica. Ele utiliza a capacidade de "Self-Auditing" da Poetiq para atuar como um adversário do sistema.

YAML
agent:
  name: Veritas
  id: cognitive-qa-auditor
  title: Quality Assurance & Logic Auditor
  icon: 🛡️
  model: poetiq-reasoning-audit-v1
  description: Auditor responsável pela validação lógica, matemática e pedagógica do software e conteúdo.
  whenToUse: Utilizar após a geração de código ou conteúdo, antes da aprovação final.
persona:
  role: Auditor Adversarial de Matemática
  style: Crítico, investigativo, intransigente com falácias lógicas.
  core_principles:
    - Tolerância zero para imprecisões matemáticas.
    - Verificação de feedback corretivo (o sistema explica o 'porquê' do erro?).
    - Simulação de "Red Teaming" curricular (tentar induzir o sistema ao erro).
  tools:
    - run-poetiq-reasoning-loop
    - verify-math-proof-integrity
    - simulate-student-misconception
dependencies:
  tasks:
    - validate-pedagogical-alignment.md
    - stress-test-math-logic.md
Mecanismo de Ação: Veritas não apenas verifica se o software "roda". Ele lê o código da lição e executa a ferramenta simulate-student-misconception. Por exemplo, em uma lição sobre subtração, Veritas simulará um aluno que subtrai o número menor do maior independentemente da ordem (ex: 3 - 7 = 4). Se o software desenvolvido pelo agente Construtor responder apenas "Errado", Veritas rejeitará a entrega, exigindo que o feedback explique o conceito de empréstimo ou números negativos, conforme definido no PRD de Sofia.   

3. Metodologia de Desenvolvimento: Do Planejamento à Execução Recursiva
A implementação do 'Matemática Viva' segue o fluxo de trabalho "Enterprise Flow" do BMAD, adaptado para incorporar os loops de raciocínio da Poetiq em pontos críticos de decisão. Este fluxo garante que a complexidade do currículo seja gerenciada através de Sharding (fragmentação de contexto), evitando a sobrecarga cognitiva dos agentes.   

3.1 Fase 1: Planejamento Pedagógico Agentic (Agentic Pedagogical Planning)
Nesta fase, o objetivo é transformar uma necessidade educacional vaga em uma especificação técnica e pedagógica imutável.

Engajamento Inicial (User Interface): O educador solicita: "Crie um módulo para ensinar frações equivalentes para alunos do 4º ano que têm dificuldade com conceitos abstratos."

Análise Recursiva (Sofia + Poetiq):

Sofia inicia um loop de raciocínio: "Para entender frações equivalentes sem abstração, precisamos de modelos de área. O método de Singapura recomenda barras de frações."

Auto-Auditoria: "Apenas barras são suficientes? Não, precisamos comparar barras de tamanhos idênticos divididas diferentemente. O conceito de 'inteiro' deve ser constante."

Artefato Gerado: docs/pedagogy/brief-fracoes-equivalentes.md. Este documento detalha a estratégia visual e os pré-requisitos cognitivos.

Arquitetura Lógica (Euclides):

Euclides lê o brief e projeta a estrutura de dados. Ele define que uma fração não é apenas um par de números (a, b), mas um objeto com propriedades visuais (shape_type, partition_count, selected_count).

Utilizando o solver ARC-AGI da Poetiq, Euclides gera casos de teste lógicos: "Se visualizarmos 1/2 e 2/4, a área preenchida em pixels deve ser idêntica. Teste: area(1/2) == area(2/4) deve retornar TRUE.".   

Artefato Gerado: docs/architecture/logic-schema-fractions.json.

3.2 Fase 2: Desenvolvimento com Engenharia de Contexto (Context-Engineered Development)
O maior risco em sistemas multi-agentes é a perda de contexto. Se o agente Construtor (Dev) esquecer que o método é "Singapura", ele pode implementar uma calculadora de frações genérica. O BMAD resolve isso através do Nexus (Scrum Master).

Sharding e Criação de Histórias (Nexus):

Nexus fragmenta o projeto em "Story Files" atômicos.

Exemplo de Story: STORY-101-Visualizacao-Meio.md.

Injeção de Contexto: Nexus injeta neste arquivo apenas as diretrizes de Sofia sobre representação visual e o schema de Euclides. Ele adiciona uma restrição explícita: "IMPLEMENTAÇÃO DEVE BLOQUEAR ENTRADA NUMÉRICA ATÉ QUE O ALUNO INTERAJA COM A BARRA VISUAL.".   

Implementação (Construtor e Ludus):

O agente Construtor gera o código React/TypeScript.

Simultaneamente, Ludus gera as especificações de CSS e animação para garantir que a interação seja "suculenta" (juicy) e responsiva, mantendo o engajamento do aluno.   

3.3 Fase 3: O Loop de Validação Recursiva (The Reasoning Loop)
A fase de QA no 'Matemática Viva' é onde a integração com a Poetiq se torna mais evidente. Diferente de testes unitários tradicionais, esta fase testa a semântica pedagógica.

Simulação Adversarial (Veritas):

Veritas carrega o código gerado.

Passo 1 (Execução): Veritas assume a persona de um aluno impaciente. Ele tenta clicar rapidamente em respostas aleatórias.

Passo 2 (Auditoria Poetiq): O sistema analisa a resposta do software. "O software permitiu 'gaming the system' (chute aleatório)?". Se sim, Veritas sinaliza uma falha pedagógica: "O sistema carece de mecanismos de verificação de engajamento cognitivo."

Passo 3 (Auditoria Matemática): Veritas verifica a renderização. "A barra de 1/3 é visualmente menor que a de 1/2 na tela?". Se houver distorção visual (ex: responsividade CSS quebrando a proporção), Veritas rejeita a história, pois isso violaria o princípio de precisão do modelo pictórico.   

4. Integração Técnica e Fluxo de Dados
A infraestrutura técnica deve suportar essa troca complexa de informações entre especificações estáticas (Markdown) e raciocínio dinâmico (API Poetiq).

4.1 Estrutura de Diretórios e Artefatos (Padrão BMAD)
O projeto deve seguir rigorosamente a estrutura de diretórios do BMAD para garantir que os agentes localizem seus contextos de memória ("knowledge extraction") e ferramentas.   

matematica-viva/ ├──.bmad/ # Núcleo da Inteligência do Sistema │ ├── agents/ # Definições YAML/Markdown dos especialistas │ │ ├── sofia.md # Arquiteta Pedagógica │ │ ├── euclid.md # Especialista Lógico │ │ ├── veritas.md # Auditor QA │ │ └── nexus.md # Orquestrador │ ├── workflows/ # Definições de processos │ │ ├── curriculum-design.yaml │ │ └── logic-validation-loop.yaml │ ├── expansion-packs/ # Módulos customizados │ │ └── bmad-singapore-math/ # Pack específico do projeto │ └── templates/ │ ├── perd-template.md # Template de Requisitos Pedagógicos │ └── math-story.yaml # Template de tarefa de desenvolvimento ├── docs/ # A "Fonte da Verdade" │ ├── pedagogy/ # Saídas da Sofia │ ├── architecture/ # Saídas do Euclides │ └── adrs/ # Registros de Decisão Arquitetural (e Pedagógica) ├── src/ # Código da Aplicação (React/Python) └── tests/ # Relatórios de Auditoria do Veritas

4.2 A Ponte API: Integrando o Raciocínio Poetiq
Como a Poetiq opera como um meta-sistema sobre LLMs, a integração técnica envolve a criação de "Tools" (ferramentas) que os agentes BMAD podem invocar via comando. O script abaixo ilustra como o agente Veritas invoca o loop de raciocínio para validar uma proposição matemática.

Script de Integração (Python Middleware):

Python
# tools/poetiq_validator.py
import os
from poetiq_sdk import MetaSystemClient  # SDK hipotético baseado na arquitetura descrita [19]

def validate_pedagogical_logic(content_snippet, learning_objective):
    """
    Invoca o loop de refinamento da Poetiq para validar se o conteúdo
    atende ao objetivo de aprendizagem sem alucinação.
    """
    client = MetaSystemClient(api_key=os.getenv("POETIQ_API_KEY"))
    
    # Configuração do Loop de Raciocínio (Reasoning Loop)
    # O parâmetro 'audit_mode' ativa a auto-crítica recursiva [5]
    validation_result = client.reasoning_loop(
        task="pedagogical_audit",
        input=content_snippet,
        context={
            "objective": learning_objective,
            "methodology": "singapore_math_cpa",
            "constraint": "no_abstract_leaps"
        },
        max_refinements=5,  # Permite até 5 ciclos de auto-correção interna
        strategy="adversarial_critique" # Tenta 'quebrar' a lógica do conteúdo
    )
    
    if not validation_result.is_valid:
        return {
            "status": "REJECTED",
            "reason": validation_result.reasoning_trace, # O "pensamento" do erro
            "suggestion": validation_result.refined_suggestion
        }
    
    return {"status": "APPROVED", "confidence": validation_result.confidence_score}
Este script é registrado no arquivo veritas.md como uma ferramenta disponível: tools: [run-poetiq-audit]. Quando Veritas executa o comando /audit, o BMAD dispara este script, injetando a inteligência recursiva no fluxo de CI/CD.   

5. Análise de Impacto e Inovações de Segunda Ordem
A arquitetura proposta gera efeitos de segunda e terceira ordem que transcendem a simples automação do código. Estas implicações reforçam a necessidade de um sistema tão estruturado quanto o BMAD+Poetiq.

5.1 O Fim do Material Didático Estático
Com a capacidade do agente Euclides de gerar problemas matemáticos validados logicamente em tempo real (utilizando a capacidade ARC-AGI para síntese de programas), o 'Matemática Viva' torna-se um currículo infinito. O sistema pode detectar que um aluno está falhando na transição entre modelos de barra e números fracionários e, autonomamente, instruir Euclides a gerar 50 novos problemas intermediários que preencham essa lacuna específica. Isso representa a realização da "Auto-Melhoria Recursiva" aplicada à pedagogia: o sistema melhora sua própria capacidade de ensinar com base na interação com o aluno.   

5.2 A Democratização da Excelência Pedagógica
O método de Singapura é historicamente intensivo para o professor, exigindo treinamento profundo para aplicar corretamente o CPA. Ao codificar esses princípios na persona do agente Sofia e nas restrições de validação do Veritas, o sistema 'Matemática Viva' "exporta" essa expertise. Um desenvolvedor júnior ou uma escola com menos recursos pode utilizar o sistema para criar material de alta fidelidade pedagógica, pois os agentes de governança (Sofia e Veritas) impedirão a criação de material "ruim" ou desalinhado.   

5.3 O Registro de Decisão Pedagógica (PADR)
Expandindo o conceito técnico de Architecture Decision Records (ADR), o sistema introduz os Pedagogical Architecture Decision Records (PADR). Cada escolha feita por Sofia — por exemplo, "Usar círculos em vez de quadrados para introduzir frações" — é documentada e versionada em docs/adrs/. Isso cria um rastro de auditoria educacional, permitindo que educadores humanos revisem não apenas o software final, mas a lógica decisória que levou à sua criação, garantindo transparência e confiança no sistema automatizado.   

6. Roteiro de Implementação e Conclusões
A execução do projeto 'Matemática Viva' deve seguir um roteiro incremental, validando cada camada da arquitetura antes da expansão.

6.1 Roteiro Técnico
Fase de Fundação (Semanas 1-4): Instalação do BMAD Core e configuração do repositório. Criação do bmad-matematica-viva expansion pack. Definição inicial dos arquivos YAML para Sofia e Euclides baseados nos princípios de Singapura.   

Fase de Integração Cognitiva (Semanas 5-8): Desenvolvimento dos wrappers Python para a API Poetiq. Treinamento (via prompt engineering recursivo) do agente Veritas para detectar falácias matemáticas específicas usando o dataset ARC-AGI como benchmark de raciocínio.   

Fase Piloto (Semanas 9-12): Geração do primeiro módulo vertical ("Frações 4º Ano"). Execução completa do fluxo: Planejamento (Sofia) -> Arquitetura (Euclides) -> Sharding (Nexus) -> Código (Construtor) -> Auditoria (Veritas).

Fase de Refinamento (Contínua): Análise dos logs de rejeição do Veritas. Se Veritas rejeita 50% do código do Construtor, o prompt do Construtor deve ser refinado (Auto-Melhoria do Sistema) para incluir mais restrições pedagógicas a priori.   

6.2 Conclusão
A arquitetura aqui apresentada para o projeto 'Matemática Viva' demonstra que a criação de software educacional seguro e eficaz via IA exige mais do que um prompt inteligente; exige uma engenharia de sistemas cognitivos. A utilização do framework BMAD fornece a disciplina necessária — através de especificações imutáveis, personas especializadas e fragmentação de contexto — para gerenciar a complexidade de um currículo matemático. A integração da Poetiq.ai injeta a capacidade vital de raciocínio recursivo e auto-auditoria, transformando a validação de conteúdo de uma verificação sintática para uma verificação semântica e lógica profunda.

Ao acoplar a estrutura organizacional do BMAD com o motor de verdade da Poetiq, o sistema 'Matemática Viva' mitiga os riscos de alucinação e superficialidade pedagógica, estabelecendo um novo padrão para tecnologias educacionais generativas. O resultado não é apenas um software que funciona, mas um sistema que ensina com a integridade, paciência e rigor de um especialista humano.


chickieandroo.com
Math Review-Singapore & Simply Charlotte Mason
Abre em uma nova janela

simplycharlottemason.com
Singapore Math? - Simply Charlotte Mason
Abre em uma nova janela

medium.com
A Comparative Analysis of AI Agentic Frameworks: BMAD-Method ...
Abre em uma nova janela

redreamality.com
BMAD-METHOD Guide: Breakthrough Agile AI-Driven Development
Abre em uma nova janela

bdtechtalks.com
Beyond raw intelligence: How Poetiq cracked the ARC-AGI-2 ...
Abre em uma nova janela

poetiq.ai
Traversing the Frontier of Superintelligence - Poetiq
Abre em uma nova janela

github.com
Ricoledan/bmad-architecture-agent: A complete expert ... - GitHub
Abre em uma nova janela

redreamality.com
BMAD-METHOD Guide: Breakthrough Agile AI-Driven Development
Abre em uma nova janela

recruit.group.gmo
The BMAD Method: A Framework for Spec Oriented AI-Driven ...
Abre em uma nova janela

poetiq.ai
Poetiq
Abre em uma nova janela

poetiq.ai
ARC-AGI-2 SOTA at Half the Cost - Poetiq
Abre em uma nova janela

bmadmethodguide.com
BMAD-METHOD - Universal AI Agent Framework Tutorial Guide
Abre em uma nova janela

npmjs.com
@cloudkinetix/bmad-enhanced - npm
Abre em uma nova janela

simplycharlottemason.com
Singapore Math - Simply Charlotte Mason
Abre em uma nova janela

simplycharlottemason.com
Singapore Math - Simply Charlotte Mason
Abre em uma nova janela

smythos.com
Exploring the Role of Multi-Agent Systems in Education - SmythOS
Abre em uma nova janela

gitingest.com
Gitingest
Abre em uma nova janela

github.com
24601/BMAD-AT-CLAUDE: Breakthrough Method for Agile AI Driven ...
Abre em uma nova janela

gist.github.com
BMad's Best Practices Cursor Custom Agents and Rules Generator
Abre em uma nova janela

medium.com
Beyond Simple Prompts: How to Unlock LLM's Full Potential with ...
Abre em uma nova janela

marketingaiinstitute.com
AI Teaching Itself? It's Called “Recursive Self-Improvement” and It's ...
Abre em uma nova janela

ardion.io
What is recursive self-improvement (RSI) in AI? - Ardion
Abre em uma nova janela

adamblackington.com
BMAD-METHOD | Adam Blackington
Abre em uma nova janela

github.com
bmad-code-org/BMAD-METHOD: Breakthrough Method for ... - GitHub
Abre em uma nova janela

therundown.ai
Poetiq cracks major reasoning benchmark - The Rundown AI


