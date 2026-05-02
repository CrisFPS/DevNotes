---
id: RF
tipo: Requisitos Funcionais
projeto: DevNotes Local
versao: 1.0
status: aprovado
fonte: prompts/05_R_Prompt_Refinado_do_Levantamento_e_Análise_de_Requisitos.md
---

# Requisitos Funcionais — DevNotes Local

## Rastreabilidade

| Work Item | Arquivo |
|---|---|
| Feature | [FEAT-001](../features/FEAT-001-devnotes-local-mvp.md) |
| User Story | [US-001](../us/US-001-gerenciar-conteudos-tecnicos-locais.md) |
| Regras de Negócio | [RN](./RN-regras-de-negocio.md) |
| Req. Não Funcionais | [RNF](./RNF-requisitos-nao-funcionais.md) |

---

## Tabela de Requisitos Funcionais

| ID     | Requisito                                            | Descrição                                                                                                                                           | Prioridade  | Observações                                               |
| ------ | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------- |
| RF-001 | Cadastrar conteúdo técnico manualmente               | O sistema deve permitir que o usuário cadastre manualmente uma anotação técnica, snippet, SQL, script, regra de negócio ou texto livre.             | Obrigatória | Deve permitir informar título, conteúdo e metadados.      |
| RF-002 | Editar conteúdo cadastrado                           | O sistema deve permitir alterar conteúdos já cadastrados.                                                                                           | Obrigatória | A edição deve atualizar conteúdo e metadados.             |
| RF-003 | Excluir conteúdo cadastrado                          | O sistema deve permitir excluir conteúdos cadastrados.                                                                                              | Obrigatória | Pode ser exclusão física no MVP.                          |
| RF-004 | Pesquisar por texto livre                            | O sistema deve permitir pesquisar conteúdos usando texto livre.                                                                                     | Obrigatória | A busca deve consultar o índice FTS5.                     |
| RF-005 | Combinar busca com filtros                           | O sistema deve permitir combinar pesquisa textual com filtros por categoria, linguagem, sistema, domínio, tags, tipo de arquivo e regra de negócio. | Obrigatória | Pode ser implementado de forma simples no MVP.            |
| RF-006 | Colar trechos técnicos manualmente                   | O sistema deve permitir colar manualmente trechos de código, SQL, Markdown, texto ou scripts.                                                       | Obrigatória | O conteúdo deve ser preservado como texto.                |
| RF-007 | Fazer upload de arquivo                              | O sistema deve permitir upload simples de um arquivo por vez.                                                                                       | Obrigatória | Apenas extensões permitidas.                              |
| RF-008 | Salvar arquivo enviado localmente                    | O sistema deve salvar o arquivo enviado na pasta local `uploads/`.                                                                                  | Obrigatória | O nome pode ser normalizado para evitar conflitos.        |
| RF-009 | Validar extensão de arquivo                          | O sistema deve aceitar apenas extensões configuradas como permitidas.                                                                               | Obrigatória | Lista definida em `config.yaml`.                          |
| RF-010 | Validar tamanho máximo do arquivo                    | O sistema deve rejeitar arquivos maiores que 12 MB.                                                                                                 | Obrigatória | Mensagem clara ao usuário.                                |
| RF-011 | Extrair texto do arquivo enviado                     | O sistema deve ler o conteúdo textual do arquivo enviado.                                                                                           | Obrigatória | Deve considerar fallback de encoding.                     |
| RF-012 | Registrar conteúdo textual no SQLite                 | O sistema deve gravar o texto extraído no banco SQLite.                                                                                             | Obrigatória | O conteúdo deve ser pesquisável.                          |
| RF-013 | Indexar conteúdo com SQLite FTS5                     | O sistema deve indexar o conteúdo textual para permitir busca eficiente.                                                                            | Obrigatória | Pode usar tabela virtual FTS5.                            |
| RF-014 | Visualizar conteúdo preservando formatação           | O sistema deve exibir o conteúdo mantendo quebras de linha, indentação e espaçamento.                                                               | Obrigatória | Usar estrutura `<pre><code>`.                             |
| RF-015 | Destacar sintaxe com Highlight.js                    | O sistema deve usar Highlight.js para destacar sintaxe quando aplicável.                                                                            | Obrigatória | Linguagem pode ser inferida ou informada.                 |
| RF-016 | Classificar por categoria                            | O sistema deve permitir classificar conteúdos por categoria.                                                                                        | Obrigatória | Exemplos: snippet, SQL, regra, script, anotação.          |
| RF-017 | Classificar por linguagem                            | O sistema deve permitir classificar conteúdos por linguagem.                                                                                        | Obrigatória | Ex.: Python, SQL, Java, Markdown, PowerBuilder.           |
| RF-018 | Classificar por tags                                 | O sistema deve permitir associar tags ao conteúdo.                                                                                                  | Obrigatória | Tags podem vir de lista pré-cadastrada.                   |
| RF-019 | Classificar por sistema e domínio                    | O sistema deve permitir associar conteúdo a sistema e domínio.                                                                                      | Obrigatória | Especialmente útil para regras de negócio.                |
| RF-020 | Marcar como regra de negócio                         | O sistema deve permitir marcar um conteúdo como regra de negócio.                                                                                   | Obrigatória | Deve facilitar filtros e identificação.                   |
| RF-021 | Identificar tipo de objeto PowerBuilder por extensão | O sistema deve identificar automaticamente o tipo de objeto PowerBuilder com base na extensão do arquivo.                                           | Obrigatória | Ex.: `.srd` = DataWindow.                                 |
| RF-022 | Usar configurações do `config.yaml`                  | O sistema deve carregar listas e mapeamentos a partir do arquivo `config.yaml`.                                                                     | Obrigatória | Sistemas, domínios, linguagens, extensões, tags e tipos.  |
| RF-023 | Listar conteúdos cadastrados                         | O sistema deve exibir uma lista inicial dos conteúdos cadastrados, com paginação quando houver maior volume de registros.                           | Obrigatória | Pode conter título, categoria, linguagem, sistema, data e controles de navegação. |
| RF-024 | Exibir detalhes de um conteúdo                       | O sistema deve permitir abrir um conteúdo específico para visualização completa.                                                                    | Obrigatória | Deve exibir texto formatado e metadados.                  |
| RF-025 | Registrar metadados do upload                        | O sistema deve registrar nome original, extensão, tipo de arquivo e caminho local do arquivo enviado.                                               | Obrigatória | Importante para rastreabilidade local.                    |
| RF-026 | Permitir tags pré-cadastradas                        | O sistema deve permitir selecionar tags definidas no `config.yaml`.                                                                                 | Desejável   | No MVP pode ser simples.                                  |
| RF-027 | Permitir múltiplas tags por conteúdo                 | O sistema deve permitir associar mais de uma tag a um conteúdo.                                                                                     | Desejável   | Pode usar relação lógica no modelo conceitual.            |
| RF-028 | Permitir busca sem termo textual                     | O sistema deve permitir filtrar conteúdos mesmo sem informar texto livre.                                                                           | Desejável   | Útil para listar por sistema, domínio ou linguagem.       |
| RF-029 | Exibir mensagens de erro amigáveis                   | O sistema deve informar erros de validação de forma compreensível.                                                                                  | Desejável   | Ex.: extensão inválida, arquivo grande, falha de leitura. |
| RF-030 | Registrar data de criação e atualização              | O sistema deve registrar data/hora de criação e última atualização do conteúdo.                                                                     | Desejável   | Ajuda na organização.                                     |
