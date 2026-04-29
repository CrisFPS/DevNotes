---
id: TASK-010
titulo: Implementar exclusão de conteúdo
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-008, TASK-018
---

# TASK-010 — Implementar exclusão de conteúdo

## Descrição

Permitir que o usuário exclua conteúdos cadastrados.

---

## Critérios de aceitação

- Usuário consegue solicitar exclusão de conteúdo.
- Sistema solicita confirmação.
- Sistema remove o conteúdo do SQLite.
- Sistema remove ou atualiza o índice textual correspondente.
- Sistema exibe confirmação após exclusão.

---

## Dependências

TASK-008, TASK-018.

---

## Observações técnicas

Para o MVP, exclusão física é aceitável, desde que confirmada pelo usuário.
