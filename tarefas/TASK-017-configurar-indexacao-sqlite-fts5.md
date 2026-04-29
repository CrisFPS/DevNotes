---
id: TASK-017
titulo: Configurar indexação com SQLite FTS5
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-005, TASK-007, TASK-008, TASK-011
---

# TASK-017 — Configurar indexação com SQLite FTS5

## Descrição

Criar estrutura de indexação textual usando SQLite FTS5 para permitir pesquisa eficiente no conteúdo técnico.

---

## Critérios de aceitação

- Existe estrutura FTS5 para indexar conteúdo textual.
- Conteúdos cadastrados manualmente são indexados.
- Conteúdos extraídos de upload são indexados.
- O índice é atualizado após edição.
- O índice é atualizado após exclusão.

---

## Dependências

TASK-005, TASK-007, TASK-008, TASK-011.

---

## Observações técnicas

É uma das partes tecnicamente mais importantes do MVP.
