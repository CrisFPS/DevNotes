---
id: TASK-005
titulo: Configurar SQLite e SQLAlchemy
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-002, TASK-003
---

# TASK-005 — Configurar SQLite e SQLAlchemy

## Descrição

Configurar persistência local com SQLite e camada de acesso a dados com SQLAlchemy.

---

## Critérios de aceitação

- Banco SQLite local está configurado.
- SQLAlchemy está configurado para acesso ao banco.
- A aplicação consegue abrir conexão com o banco.
- A estrutura permite criação das entidades iniciais.

---

## Dependências

TASK-002, TASK-003.

---

## Observações técnicas

Evitar complexidade de banco externo no MVP.
