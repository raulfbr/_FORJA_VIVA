# 🎯 Como Usar o Orchestrator

**Fonte:** Extraído de GUIA_REVISAO_MAESTRO.md  
**Data:** 13/01/2026  

---

## O que é o Orchestrator?

O **Orchestrator** é o coordenador da Forja. Ele:
- Coordena todos os outros agentes (PM, SM, Dev, QA, Ops)
- Toma decisões usando análise estruturada
- Registra decisões em logs
- Sempre pede aprovação antes de executar

---

## Quando Usar

| Situação | Comando Sugerido |
|----------|------------------|
| Precisa tomar decisão complexa | "Use o ORCHESTRATOR para decidir..." |
| Quer reunir os agentes | "Use o ORCHESTRATOR para reunir os agentes..." |
| Quer verificação completa | "Use o ORCHESTRATOR para verificar..." |
| Quer plano de ação | "Use o ORCHESTRATOR para planejar..." |

---

## Como Invocar

```
"Use o ORCHESTRATOR para [TAREFA]."

Exemplos:
- "Use o ORCHESTRATOR para verificar a estrutura."
- "Use o ORCHESTRATOR para decidir se devemos manter X."
- "Use o ORCHESTRATOR para criar um plano de produção."
- "Use o ORCHESTRATOR para reunir os agentes e discutir Y."
```

---

## O que Esperar

Quando você invoca o Orchestrator, ele:

1. **Analisa** o problema
2. **Consulta** os agentes relevantes
3. **Cria um log** com a discussão
4. **Propõe** opções e decisões
5. **Pergunta** sua aprovação antes de executar
6. **Executa** após aprovação

---

## Princípios do Orchestrator

| Princípio | Significado |
|-----------|-------------|
| **Orquestração Humana** | Você (Maestro) decide, ele prepara |
| **Transparência** | Sempre mostra o que está fazendo |
| **Sem Decisões Finais** | Nunca executa sem sua aprovação |
| **Condição de Parada** | Todo workflow tem critério de conclusão |

---

## Outros Comandos Úteis

| Comando | O que Faz |
|---------|-----------|
| "Faça verificação tripla" | 3 passes de verificação |
| "Crie um log da discussão" | Registra em logs/ |
| "Use os agentes para deliberar" | Mesa com todos os agentes |
| "Converta para YAML" | Transforma MD em YAML |

---

> *"O Orchestrator prepara; o Maestro decide."*
