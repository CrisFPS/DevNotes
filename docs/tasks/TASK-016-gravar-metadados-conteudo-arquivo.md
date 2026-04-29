---
id: TASK-016
titulo: Gravar metadados do conteúdo e do arquivo
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-007, TASK-008, TASK-011, TASK-015
---

# TASK-016 — Gravar metadados do conteúdo e do arquivo

## Descrição

Gravar no SQLite os metadados associados a conteúdos cadastrados manualmente e arquivos enviados.

---

## Critérios de aceitação

- Sistema grava título.
- Sistema grava categoria.
- Sistema grava linguagem.
- Sistema grava sistema e domínio, quando informados.
- Sistema grava tags, quando informadas.
- Sistema grava indicador de regra de negócio.
- Para upload, sistema grava nome original, extensão, caminho local, tamanho e tipo de objeto.

---

## Dependências

TASK-007, TASK-008, TASK-011, TASK-015.

---

## Observações técnicas

Os metadados serão essenciais para filtros e organização.
