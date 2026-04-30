---
id: ADR-003
title: Uso de SQLAlchemy como ORM
status: Aceito
data: 2026-04-29
---

## Contexto

A aplicação precisa de uma camada de acesso a dados que organize as operações de persistência, evite SQL disperso pelo código e facilite os testes automatizados.

## Decisão

Usar SQLAlchemy como ORM para mapear as entidades do banco SQLite e encapsular as operações de persistência na camada de repositórios.

## Justificativa

- SQLAlchemy é o ORM padrão do ecossistema Python, com integração nativa ao FastAPI.
- Permite trocar o banco de dados no futuro sem alterar a lógica da aplicação.
- Facilita testes unitários com banco SQLite em memória.
- A camada de repositórios, combinada com o SQLAlchemy, mantém SQL fora de serviços e rotas.

## Consequências

**Fica mais fácil:**
- Testar serviços com banco em memória usando `sqlite:///:memory:`.
- Trocar o banco de dados alterando apenas a string de conexão.
- Manter operações de banco centralizadas nos repositórios.

**Fica mais difícil:**
- Usar queries FTS5 avançadas, que exigem `text()` com SQL nativo pois o SQLAlchemy não abstrai FTS5.

## Alternativas descartadas

| Alternativa | Motivo do descarte |
|---|---|
| SQL puro com sqlite3 | Dispersa SQL pelo código; dificulta testes e manutenção |
| Tortoise ORM | Menor adoção e documentação que SQLAlchemy |
| Peewee | Menor integração com o ecossistema FastAPI |
