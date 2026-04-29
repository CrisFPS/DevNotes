---
id: CA
tipo: Critérios de Aceitação
projeto: DevNotes Local
versao: 1.0
status: aprovado
fonte: prompts/05_R_Prompt_Refinado_do_Levantamento_e_Análise_de_Requisitos.md
---

# Critérios de Aceitação Gerais do MVP — DevNotes Local

O MVP poderá ser considerado pronto quando os critérios abaixo forem atendidos:

## Rastreabilidade

| Work Item | Arquivo |
|---|---|
| Feature | [FEAT-001](../features/FEAT-001-devnotes-local-mvp.md) |
| User Story | [US-001](../us/US-001-gerenciar-conteudos-tecnicos-locais.md) |
| Req. Funcionais | [RF](../requisitos/RF-requisitos-funcionais.md) |

---

## Tabela de Critérios de Aceitação

| ID     | Critério de aceitação                                                                                                         |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| CA-001 | A aplicação inicia localmente usando Python 3.11, ambiente virtual `venv` e FastAPI.                                          |
| CA-002 | A estrutura mínima de pastas existe conforme definido: `backend/`, `frontend/`, `uploads/`, `prompts/`, `docs/`, `tests/`.   |
| CA-003 | O sistema possui banco SQLite configurado.                                                                                    |
| CA-004 | O sistema utiliza SQLAlchemy para persistência dos dados.                                                                     |
| CA-005 | O arquivo `config.yaml` centraliza listas e mapeamentos do MVP.                                                               |
| CA-006 | O usuário consegue cadastrar manualmente um conteúdo técnico.                                                                 |
| CA-007 | O usuário consegue editar um conteúdo cadastrado.                                                                             |
| CA-008 | O usuário consegue excluir um conteúdo cadastrado.                                                                            |
| CA-009 | O usuário consegue fazer upload de um arquivo permitido.                                                                      |
| CA-010 | O sistema rejeita arquivo com extensão não permitida.                                                                         |
| CA-011 | O sistema rejeita arquivo maior que 12 MB.                                                                                    |
| CA-012 | O sistema salva o arquivo enviado na pasta `uploads/`.                                                                        |
| CA-013 | O sistema extrai o conteúdo textual do arquivo enviado.                                                                       |
| CA-014 | O sistema aplica fallback de encoding ao ler arquivos.                                                                        |
| CA-015 | O sistema classifica automaticamente arquivos PowerBuilder conforme extensão.                                                 |
| CA-016 | O conteúdo manual e o conteúdo extraído de arquivo são gravados no SQLite.                                                    |
| CA-017 | O conteúdo gravado é indexado com SQLite FTS5.                                                                                |
| CA-018 | O usuário consegue pesquisar conteúdo por texto livre.                                                                        |
| CA-019 | O usuário consegue combinar busca textual com filtros.                                                                        |
| CA-020 | O usuário consegue visualizar conteúdo preservando indentação e quebras de linha.                                             |
| CA-021 | O conteúdo é exibido usando `<pre><code>`.                                                                                    |
| CA-022 | O Highlight.js é aplicado na visualização de conteúdo técnico.                                                                |
| CA-023 | O usuário consegue marcar conteúdo como regra de negócio.                                                                     |
| CA-024 | O usuário consegue classificar conteúdo por categoria, linguagem, tags, sistema e domínio.                                    |
| CA-025 | Existem testes automatizados com pytest cobrindo regras principais.                                                           |
| CA-026 | Existe documentação básica no `README.md`.                                                                                    |
| CA-027 | Existem artefatos de Feature, User Story e tarefas técnicas em `docs/features/`, `docs/us/` e `docs/tasks/`.                  |
| CA-028 | O sistema não inclui autenticação, múltiplos usuários ou recursos fora do escopo do MVP.                                      |
