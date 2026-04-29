---
id: TASK-012
titulo: Validar extensão de arquivo
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-006, TASK-011
---

# TASK-012 — Validar extensão de arquivo

## Descrição

Implementar validação para aceitar somente arquivos com extensões permitidas.

---

## Critérios de aceitação

- Sistema consulta extensões permitidas no `config.yaml`.
- Sistema aceita arquivos com extensões configuradas.
- Sistema rejeita arquivos com extensões não permitidas.
- Sistema exibe mensagem clara quando rejeitar arquivo.

---

## Dependências

TASK-006, TASK-011.

---

## Observações técnicas

A validação deve considerar extensão de forma segura e padronizada.
