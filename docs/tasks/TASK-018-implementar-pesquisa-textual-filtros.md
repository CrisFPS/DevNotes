---
id: TASK-018
titulo: Implementar pesquisa textual com filtros
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-016, TASK-017
---

# TASK-018 — Implementar pesquisa textual com filtros

## Descrição

Permitir pesquisa por texto livre usando FTS5 e filtros por metadados.

---

## Critérios de aceitação

- Usuário consegue pesquisar por texto livre.
- Usuário consegue filtrar por categoria.
- Usuário consegue filtrar por linguagem.
- Usuário consegue filtrar por sistema.
- Usuário consegue filtrar por domínio.
- Usuário consegue filtrar por tags.
- Usuário consegue filtrar conteúdos marcados como regra de negócio.
- Sistema exibe lista de resultados.

---

## Dependências

TASK-016, TASK-017.

---

## Observações técnicas

A busca deve ser simples, mas útil. Não é necessário implementar ranking sofisticado no MVP.
