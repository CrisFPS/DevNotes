---
id: ADR-002
title: Uso de SQLite com extensão FTS5 como banco de dados
status: Aceito
data: 2026-04-29
---

## Contexto

A aplicação precisa de persistência de dados e busca textual sobre o conteúdo técnico armazenado. É necessário decidir qual banco de dados usar e como implementar a busca.

## Decisão

Usar SQLite como banco de dados principal com a extensão FTS5 para busca textual full-text. O banco será armazenado em um único arquivo local (`devnotes.db`).

## Justificativa

- SQLite é embutido: não exige instalação, configuração ou processo separado de servidor.
- Para uso individual sem concorrência de escrita, SQLite é mais que suficiente.
- A extensão FTS5 é nativa do SQLite e oferece busca textual eficiente sem bibliotecas externas.
- O arquivo único do banco facilita backup manual e portabilidade.

## Consequências

**Fica mais fácil:**
- Configurar e executar o ambiente sem dependências de infraestrutura.
- Fazer backup manual (copiar o arquivo `.db`).
- Usar busca textual sem instalar Elasticsearch, Solr ou similares.

**Fica mais difícil:**
- Escalar para múltiplos usuários simultâneos com alta carga de escrita.
- Migrar para outro banco de dados no futuro (embora SQLAlchemy mitigue parte disso).

## O que não se aplica

SQLite não é adequado para aplicações com múltiplos escritores simultâneos, alta carga ou requisitos de replicação. Esses cenários estão fora do escopo do MVP.

## Alternativas descartadas

| Alternativa | Motivo do descarte |
|---|---|
| PostgreSQL | Exige servidor separado; excesso para uso individual local |
| SQL Server | Licença, instalação e configuração desnecessárias para MVP local |
| Elasticsearch | Infraestrutura pesada para busca textual; FTS5 é suficiente |
| Banco em memória | Não persiste dados entre reinicializações |
