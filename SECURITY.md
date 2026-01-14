# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 6.x (BMAD v6 + YAML Lean v1.0) | :white_check_mark: |
| < 6.0   | :x:                |

## Reporting a Vulnerability

Se você descobrir uma vulnerabilidade de segurança, por favor:

1. **NÃO** abra uma Issue pública
2. Envie email confidencial para o mantenedor via GitHub
3. Descreva a vulnerabilidade em detalhes
4. Aguarde confirmação antes de divulgar publicamente

## Resposta Esperada

- Confirmação de recebimento: 48 horas
- Avaliação inicial: 7 dias  
- Correção (se aplicável): 30 dias

## Escopo

Este projeto é conteúdo educacional + BMAD Framework v6. Vulnerabilidades podem incluir:

### Conteúdo Educacional
- Exposição de dados sensíveis em lições
- Conteúdo inapropriado para crianças

### Infraestrutura Técnica (BMAD v6)
- Vulnerabilidades em `orchestrator.yaml`
- Scripts Python (`forja-core/pipeline/`)
- Workflows YAML (`  bmad/workflows/`)
- Dependencies no `requirements.txt`

### YAML Lean v1.0
- Violações SSOT causando inconsistências
- Parsing YAML malicioso
- Injeção via templates

## Dados Sensíveis

**Este projeto NÃO armazena:**
- Informações pessoais de famílias
- Dados de crianças
- Informações de pagamento

Todo conteúdo é público via CC BY 4.0.

---

Obrigado por ajudar a manter o projeto seguro para famílias! 🛡️
