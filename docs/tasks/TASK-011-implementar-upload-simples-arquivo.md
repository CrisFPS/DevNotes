---
id: TASK-011
titulo: Implementar upload simples de arquivo
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-003, TASK-004, TASK-005
---

# TASK-011 — Implementar upload simples de arquivo

## Descrição

Permitir que o usuário envie um arquivo por vez para armazenamento local e extração de conteúdo textual.

---

## Critérios de aceitação

- Tela permite selecionar um arquivo.
- Sistema recebe apenas um arquivo por operação.
- Sistema salva arquivo válido na pasta `uploads/`.
- Sistema registra metadados básicos do arquivo.

---

## Dependências

TASK-003, TASK-004, TASK-005.

---

## Observações técnicas

O upload deve ser simples, sem múltiplos arquivos no MVP.
