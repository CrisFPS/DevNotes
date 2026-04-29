---
id: FEAT-001
tipo: Feature
status: a_fazer
---

# FEAT-001 — MVP do DevNotes Local para cadastro, organização, busca e visualização de conteúdos técnicos

## Descrição

Implementar o MVP do DevNotes Local, uma aplicação web local para armazenamento, classificação, pesquisa e visualização de conteúdos técnicos, incluindo snippets, SQLs, scripts, anotações, regras de negócio e arquivos textuais de sistemas legados.

A Feature deve contemplar cadastro manual, upload simples de arquivos, validação de extensão e tamanho, leitura com fallback de encoding, gravação em SQLite, indexação com SQLite FTS5, busca textual com filtros, visualização preservando formatação e destaque de sintaxe com Highlight.js.

---

## Objetivo de negócio

Centralizar conteúdos técnicos usados em estudo e desenvolvimento de software, reduzindo dispersão de informações e facilitando a reutilização de snippets, SQLs, scripts, regras de negócio e arquivos legados em um ambiente local simples.

---

## Critérios de aceitação

| ID          | Critério                                                         |
| ----------- | ---------------------------------------------------------------- |
| CA-FEAT-001 | O usuário consegue cadastrar conteúdos técnicos manualmente.     |
| CA-FEAT-002 | O usuário consegue editar e excluir conteúdos.                   |
| CA-FEAT-003 | O usuário consegue fazer upload de um arquivo permitido por vez. |
| CA-FEAT-004 | O sistema rejeita arquivos com extensão não permitida.           |
| CA-FEAT-005 | O sistema rejeita arquivos maiores que 12 MB.                    |
| CA-FEAT-006 | O sistema extrai conteúdo textual do arquivo enviado.            |
| CA-FEAT-007 | O sistema aplica fallback de encoding.                           |
| CA-FEAT-008 | O sistema identifica tipo de objeto PowerBuilder por extensão.   |
| CA-FEAT-009 | O conteúdo é salvo no SQLite.                                    |
| CA-FEAT-010 | O conteúdo é indexado com SQLite FTS5.                           |
| CA-FEAT-011 | O usuário consegue pesquisar por texto livre.                    |
| CA-FEAT-012 | O usuário consegue combinar busca com filtros.                   |
| CA-FEAT-013 | O conteúdo é exibido preservando formatação.                     |
| CA-FEAT-014 | O Highlight.js é usado na visualização.                          |
| CA-FEAT-015 | O projeto contém documentação básica no README.                  |
| CA-FEAT-016 | Existem testes automatizados cobrindo regras principais.         |

---

## User Stories vinculadas

- [US-001 — Gerenciar conteúdos técnicos locais para consulta e reutilização](US-001-gerenciar-conteudos-tecnicos-locais.md)

---

## Tarefas técnicas vinculadas

| Tarefa   | Título                                   |
| -------- | ---------------------------------------- |
| TASK-001 | Criar estrutura inicial do projeto       |
| TASK-002 | Configurar ambiente Python com venv      |
| TASK-003 | Configurar FastAPI                       |
| TASK-004 | Configurar Jinja2                        |
| TASK-005 | Configurar SQLite e SQLAlchemy           |
| TASK-006 | Criar arquivo config.yaml                |
| TASK-007 | Modelar entidades iniciais               |
| TASK-008 | Implementar cadastro manual de conteúdo  |
| TASK-009 | Implementar edição de conteúdo           |
| TASK-010 | Implementar exclusão de conteúdo         |
| TASK-011 | Implementar upload simples de arquivo    |
| TASK-012 | Validar extensão de arquivo              |
| TASK-013 | Validar tamanho máximo de 12 MB          |
| TASK-014 | Implementar leitura com fallback encoding|
| TASK-015 | Classificar automaticamente por extensão |
| TASK-016 | Gravar metadados do conteúdo e do arquivo|
| TASK-017 | Configurar indexação com SQLite FTS5     |
| TASK-018 | Implementar pesquisa textual com filtros |
| TASK-019 | Implementar visualização com pre/code    |
| TASK-020 | Integrar Highlight.js                    |
| TASK-021 | Criar testes com pytest                  |
| TASK-022 | Criar documentação básica no README.md   |

---

## Observações técnicas

- O MVP deve evitar recursos fora do escopo, como autenticação, múltiplos usuários, publicação em produção e microsserviços.
- O projeto deve manter estrutura didática, adequada para estudo de SDLC.
- As listas e mapeamentos devem ser centralizados em `config.yaml`.
- A pasta `prompts/` deve armazenar prompts usados durante o desenvolvimento.
- A pasta `tarefas/` deve armazenar os artefatos simulados de gestão do projeto.
