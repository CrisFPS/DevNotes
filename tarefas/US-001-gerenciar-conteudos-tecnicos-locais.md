---
id: US-001
tipo: User Story
feature: FEAT-001
status: a_fazer
---

# US-001 — Gerenciar conteúdos técnicos locais para consulta e reutilização

## História

Como **desenvolvedor de software**,
quero **cadastrar, classificar, pesquisar e visualizar conteúdos técnicos em uma aplicação local**,
para **reutilizar snippets, SQLs, scripts, regras de negócio e arquivos legados de forma mais organizada**.

---

## Descrição

A aplicação deve permitir que o usuário registre conteúdos técnicos manualmente ou por upload de arquivos textuais. Esses conteúdos devem ser classificados por categoria, linguagem, tags, sistema e domínio, podendo também ser marcados como regra de negócio.

O sistema deve permitir busca textual usando SQLite FTS5, combinada com filtros. A visualização deve preservar a formatação original do conteúdo e aplicar destaque de sintaxe com Highlight.js.

---

## Critérios de aceitação

| ID        | Critério                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| CA-US-001 | Dado que estou na tela de cadastro, quando informo título, conteúdo e metadados válidos, então o sistema salva o conteúdo técnico.         |
| CA-US-002 | Dado que existe um conteúdo cadastrado, quando edito seus dados, então o sistema atualiza o conteúdo e o índice textual.                   |
| CA-US-003 | Dado que existe um conteúdo cadastrado, quando confirmo a exclusão, então o sistema remove o conteúdo.                                     |
| CA-US-004 | Dado que seleciono um arquivo permitido, quando faço upload, então o sistema salva o arquivo e registra seu conteúdo textual.              |
| CA-US-005 | Dado que seleciono um arquivo com extensão inválida, quando faço upload, então o sistema rejeita o arquivo.                                |
| CA-US-006 | Dado que seleciono um arquivo maior que 12 MB, quando faço upload, então o sistema rejeita o arquivo.                                      |
| CA-US-007 | Dado que envio um arquivo PowerBuilder, quando o sistema processa o upload, então ele identifica linguagem e tipo de objeto pela extensão. |
| CA-US-008 | Dado que há conteúdos cadastrados, quando pesquiso por texto livre, então o sistema retorna conteúdos compatíveis.                         |
| CA-US-009 | Dado que uso filtros, quando pesquiso, então o sistema restringe os resultados conforme os filtros selecionados.                           |
| CA-US-010 | Dado que abro um conteúdo, quando visualizo seus detalhes, então a formatação original é preservada.                                       |
| CA-US-011 | Dado que o conteúdo possui linguagem reconhecida, quando visualizo o conteúdo, então o Highlight.js aplica destaque de sintaxe.            |

---

## Regras envolvidas

| Regra  | Descrição                                                        |
| ------ | ---------------------------------------------------------------- |
| RN-001 | Upload único por operação.                                       |
| RN-002 | Limite máximo de 12 MB por arquivo.                              |
| RN-003 | Apenas extensões permitidas são aceitas.                         |
| RN-005 | PowerBuilder deve ser tratado como linguagem única.              |
| RN-006 | Tipo de objeto PowerBuilder deve ser identificado pela extensão. |
| RN-014 | Leitura de arquivos deve usar fallback de encoding.              |
| RN-015 | Conteúdo deve ser pesquisável.                                   |
| RN-016 | Conteúdo pode ser marcado como regra de negócio.                 |
| RN-018 | Listas e mapeamentos devem vir do `config.yaml`.                 |
| RN-020 | Visualização deve preservar formatação.                          |

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

- O cadastro manual e o upload devem alimentar a mesma base conceitual de conteúdos técnicos.
- O índice FTS5 deve ser atualizado após cadastro, edição e exclusão.
- A visualização deve priorizar legibilidade e preservação textual.
- O MVP não deve incluir autenticação nem múltiplos usuários.
