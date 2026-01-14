# Contributing to Forja Viva

Obrigado por considerar contribuir com o projeto **Forja Viva**! 🎉

Este documento fornece diretrizes para contribuições.

---

## 📋 Código de Conduta

### Nossos Princípios

1. **Qualidade Não é Negociável** — Buscamos o impecável
2. **Família é o Centro** — Tudo deve funcionar em casa real
3. **Positividade Sempre** — Tom encorajador, nunca julgador
4. **Inclusão como Honra** — Bernardo consegue participar?

### Comportamento Esperado

- Seja respeitoso e inclusivo
- Aceite feedback construtivo
- Foque no que é melhor para as famílias
- Mantenha a qualidade alta

---

## 🚀 Como Contribuir

### 1. Reportar Bugs

- Use o template de Issue
- Descreva o problema claramente
- Inclua passos para reproduzir
- Anexe screenshots se relevante

### 2. Sugerir Melhorias

- Abra uma Issue com tag `enhancement`
- Explique o benefício para as famílias
- Descreva como se alinha aos 8 Princípios

### 3. Contribuir com Código/Conteúdo

```bash
# 1. Fork o repositório
# 2. Clone seu fork
git clone https://github.com/seu-usuario/_FORJA_VIVA.git

# 3. Crie uma branch
git checkout -b feat/minha-contribuicao

# 4. Faça suas alterações
# 5. Commit com mensagem clara
git commit -m "feat: adiciona lição sobre frações"

# 6. Push para seu fork
git push origin feat/minha-contribuicao

# 7. Abra um Pull Request
```

---

## 📝 Padrões de Commit

Usamos Conventional Commits:

| Tipo | Descrição |
|------|-----------|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Documentação |
| `style:` | Formatação (não afeta código) |
| `refactor:` | Refatoração |
| `test:` | Testes |
| `chore:` | Manutenção |

**Exemplos:**
```
feat(licao): adiciona L025 sobre adição
fix(template): corrige formatação de cards
docs(readme): atualiza seção de instalação
```

---

## ✅ Checklist de Pull Request

Antes de submeter, verifique:

- [ ] Código segue os padrões do projeto
- [ ] Testa bem em ambiente local
- [ ] Documentação atualizada se necessário
- [ ] Commit messages seguem Conventional Commits
- [ ] PR tem descrição clara

### Para Lições

- [ ] Segue template padrão
- [ ] Charlotte Mason aprovaria? (criança como pessoa)
- [ ] CPA respeitado? (Concreto primeiro)
- [ ] Funciona em 5 minutos com bebê no colo?
- [ ] Bernardo consegue participar? (acessibilidade)

---

## 📁 Estrutura de Arquivos

### Lições
```
curriculo/01_SEMENTES/
└── LXX_NOME_DA_LICAO.md   # Markdown da lição
└── LXX_NOME_DA_LICAO.yaml # Metadados
```

### Experts
```
.bmad/experts/[conselho]/
└── nome_expert.yaml       # Definição do expert
```

---

## 🤝 Processo de Review

1. **Triagem** — Mantedor verifica se segue padrões
2. **Review** — Feedback técnico e pedagógico
3. **Deliberação** — Experts virtuais consultados se necessário
4. **Merge** — Após aprovação

---

## 📐 Padrões YAML Lean v1.0

### Princípios de Qualidade

Este projeto segue **YAML Lean v1.0** com padrões rigorosos:

**1. SSOT (Single Source of Truth)**
- Cada informação existe EM UM lugar apenas
- Nunca duplicar dados - sempre referenciar
- Exemplo: Guardiões definidos em `LORE/guardioes.yaml`, lições referenciam

**2. DRY (Don't Repeat Yourself)**  
- Refatorar duplicações para funções/templates
- Workflows reutilizáveis

**3. AI Eficiência YAML**
- Experts leem YAML diretamente via `view_file`
- Não parsear Python desnecessariamente
- Economiza 3-5s por deliberação

### Quando em Dúvida — Delibere

Questões complexas seguem `reuniao-deliberacao.yaml`:

1. **ABERTURA** — Formular questão claramente
2. **POSIÇÕES** — Experts manifestam fundamentados
3. **RÉPLICA** — Questionar posições
4. **TRÉPLICA** — Ajustar ou defender
5. **SÍNTESE** — Charlotte Mason organiza
6. **DECISÃO** — Charlotte decide (voz final)

Deliberações documentadas em `logs/`

---

## 📬 Dúvidas?

- Abra uma Issue com tag `question`
- Seja específico sobre sua dúvida
- Inclua contexto relevante

---

**Obrigado por ajudar a construir algo impecável para as famílias!** 💛
