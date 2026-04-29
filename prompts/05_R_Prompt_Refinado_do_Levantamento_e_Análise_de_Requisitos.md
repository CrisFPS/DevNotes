# Análise de Requisitos — DevNotes Local

Documento gerado com base no prompt refinado fornecido "05 - Prompt Refinado do Levantamento e Análise de Requisitos.md". 

---

## 1. Visão geral do produto

### 1.1 Objetivo

O **DevNotes Local** tem como objetivo ser uma aplicação web local, simples e didática, voltada para armazenar, organizar, pesquisar e reutilizar conteúdos técnicos utilizados em estudos ou no trabalho de desenvolvimento de software.

A aplicação deverá permitir o cadastro manual de anotações técnicas, upload simples de arquivos, classificação por metadados, busca textual e visualização preservando a formatação original do conteúdo.

---

### 1.2 Problema

Desenvolvedores costumam acumular conhecimento técnico em locais dispersos, como arquivos soltos, blocos de notas, mensagens, documentos, scripts antigos, consultas SQL, exemplos de procedures e anotações sobre regras de negócio.

Essa dispersão dificulta:

* encontrar conteúdos técnicos antigos;
* reutilizar trechos úteis;
* manter histórico de regras e decisões;
* organizar exemplos por sistema, linguagem ou domínio;
* estudar tecnologias e sistemas legados de forma estruturada.

---

### 1.3 Público-alvo

O público-alvo inicial é composto por:

* desenvolvedores de software;
* analistas de sistemas;
* estudantes de engenharia de software;
* profissionais que lidam com sistemas legados;
* usuários técnicos que desejam organizar snippets, scripts e anotações locais.

No MVP, o sistema será pensado para **uso individual e local**.

---

### 1.4 Premissas

| Código | Premissa                                                                                    |
| ------ | ------------------------------------------------------------------------------------------- |
| PR-001 | O sistema será usado localmente, por apenas um usuário.                                     |
| PR-002 | Não haverá autenticação no MVP.                                                             |
| PR-003 | O usuário terá conhecimento técnico suficiente para cadastrar e classificar seus conteúdos. |
| PR-004 | Os arquivos enviados serão de texto ou arquivos legados exportados em formato textual.      |
| PR-005 | O sistema usará SQLite como banco local.                                                    |
| PR-006 | A busca textual será implementada com SQLite FTS5.                                          |
| PR-007 | A aplicação terá interface simples, usando HTML, CSS e templates Jinja2.                    |
| PR-008 | O projeto será usado também como exercício didático de SDLC com apoio de IA generativa.     |

---

### 1.5 Restrições

| Código | Restrição                                                                                            |
| ------ | ---------------------------------------------------------------------------------------------------- |
| RE-001 | O backend deverá usar Python 3.11.                                                                   |
| RE-002 | A aplicação deverá usar FastAPI.                                                                     |
| RE-003 | O banco de dados deverá ser SQLite.                                                                  |
| RE-004 | A camada de acesso a dados deverá usar SQLAlchemy.                                                   |
| RE-005 | A busca textual deverá usar SQLite FTS5.                                                             |
| RE-006 | A renderização HTML deverá usar Jinja2.                                                              |
| RE-007 | O frontend deverá ser simples, sem framework sofisticado.                                            |
| RE-008 | O destaque de sintaxe deverá usar Highlight.js.                                                      |
| RE-009 | O ambiente local deverá usar venv.                                                                   |
| RE-010 | O limite máximo de upload será de 12 MB por arquivo.                                                 |
| RE-011 | O MVP não deverá incluir autenticação, múltiplos usuários, microsserviços ou publicação em produção. |

---

## 2. Requisitos funcionais

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
| RF-023 | Listar conteúdos cadastrados                         | O sistema deve exibir uma lista inicial dos conteúdos cadastrados.                                                                                  | Obrigatória | Pode conter título, categoria, linguagem, sistema e data. |
| RF-024 | Exibir detalhes de um conteúdo                       | O sistema deve permitir abrir um conteúdo específico para visualização completa.                                                                    | Obrigatória | Deve exibir texto formatado e metadados.                  |
| RF-025 | Registrar metadados do upload                        | O sistema deve registrar nome original, extensão, tipo de arquivo e caminho local do arquivo enviado.                                               | Obrigatória | Importante para rastreabilidade local.                    |
| RF-026 | Permitir tags pré-cadastradas                        | O sistema deve permitir selecionar tags definidas no `config.yaml`.                                                                                 | Desejável   | No MVP pode ser simples.                                  |
| RF-027 | Permitir múltiplas tags por conteúdo                 | O sistema deve permitir associar mais de uma tag a um conteúdo.                                                                                     | Desejável   | Pode usar relação lógica no modelo conceitual.            |
| RF-028 | Permitir busca sem termo textual                     | O sistema deve permitir filtrar conteúdos mesmo sem informar texto livre.                                                                           | Desejável   | Útil para listar por sistema, domínio ou linguagem.       |
| RF-029 | Exibir mensagens de erro amigáveis                   | O sistema deve informar erros de validação de forma compreensível.                                                                                  | Desejável   | Ex.: extensão inválida, arquivo grande, falha de leitura. |
| RF-030 | Registrar data de criação e atualização              | O sistema deve registrar data/hora de criação e última atualização do conteúdo.                                                                     | Desejável   | Ajuda na organização.                                     |

---

## 3. Requisitos não funcionais

| ID      | Requisito                            | Descrição                                                                                            | Prioridade  | Observações                                                            |
| ------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------- |
| RNF-001 | Simplicidade                         | A aplicação deve ser simples, objetiva e adequada ao escopo de estudo.                               | Obrigatória | Evitar complexidade desnecessária.                                     |
| RNF-002 | Uso local                            | O sistema deve funcionar localmente, sem necessidade de publicação em servidor externo.              | Obrigatória | Deve rodar na máquina do usuário.                                      |
| RNF-003 | Baixa complexidade arquitetural      | O MVP não deve usar microsserviços, mensageria, cloud ou arquitetura distribuída.                    | Obrigatória | Manter foco didático.                                                  |
| RNF-004 | Desempenho adequado                  | A busca e a navegação devem ter desempenho aceitável para uma base local pequena ou média.           | Obrigatória | Não há exigência de alta escala.                                       |
| RNF-005 | Preservação de formatação            | O conteúdo visualizado deve preservar quebras de linha, indentação e espaçamento.                    | Obrigatória | Essencial para código, SQL e scripts.                                  |
| RNF-006 | Compatibilidade com arquivos legados | O sistema deve lidar de forma simples com arquivos textuais legados, especialmente PowerBuilder.     | Obrigatória | Considerar encoding.                                                   |
| RNF-007 | Tratamento de encoding               | O sistema deve tentar ler arquivos em `utf-8`, depois `latin-1` e depois `cp1252`.                   | Obrigatória | Reduz falhas em arquivos antigos.                                      |
| RNF-008 | Organização do projeto               | A estrutura de pastas deve ser clara e coerente com o objetivo didático.                             | Obrigatória | `backend/`, `frontend/`, `uploads/`, `prompts/`, `tarefas/`, `tests/`. |
| RNF-009 | Testabilidade                        | O sistema deve permitir testes automatizados com pytest.                                             | Obrigatória | Testar regras principais do MVP.                                       |
| RNF-010 | Manutenibilidade                     | O código futuro deve ser organizado para facilitar evolução e leitura.                               | Obrigatória | Mesmo sendo MVP, evitar bagunça estrutural.                            |
| RNF-011 | Configurabilidade                    | Listas de linguagens, sistemas, domínios, extensões e tags devem ser centralizadas em `config.yaml`. | Obrigatória | Evita valores fixos espalhados.                                        |
| RNF-012 | Segurança local básica               | O sistema deve validar extensão e tamanho de arquivo antes de processar uploads.                     | Obrigatória | Mesmo local, precisa de validações mínimas.                            |
| RNF-013 | Interface simples                    | A interface deve ser funcional, leve e compreensível, sem sofisticação visual excessiva.             | Obrigatória | HTML e CSS simples.                                                    |
| RNF-014 | Clareza didática                     | O projeto deve manter artefatos de prompts e tarefas para apoiar aprendizado de SDLC com IA.         | Obrigatória | Pastas `prompts/` e `tarefas/`.                                        |
| RNF-015 | Rastreabilidade básica               | O sistema deve manter metadados suficientes para localizar origem e classificação do conteúdo.       | Desejável   | Especialmente em uploads.                                              |
| RNF-016 | Robustez em erros comuns             | O sistema deve tratar erros simples de upload, leitura e validação sem quebrar a aplicação.          | Desejável   | Pode exibir mensagens amigáveis.                                       |

---

## 4. Regras de negócio

| ID     | Regra                                    | Descrição                                                                                                                       |
| ------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| RN-001 | Upload único por operação                | O sistema deve permitir o envio de apenas um arquivo por vez no MVP.                                                            |
| RN-002 | Limite máximo de upload                  | O arquivo enviado não pode ultrapassar 12 MB.                                                                                   |
| RN-003 | Extensões permitidas                     | Somente arquivos com extensões configuradas como permitidas poderão ser enviados.                                               |
| RN-004 | Lista inicial de extensões               | O MVP deve aceitar `.py`, `.java`, `.sql`, `.md`, `.txt`, `.srw`, `.sru`, `.srd`, `.srm`, `.srf`, `.sra` e `.srs`.              |
| RN-005 | PowerBuilder como linguagem única        | Arquivos PowerBuilder devem ser classificados com linguagem `PowerBuilder`, independentemente da extensão específica.           |
| RN-006 | Tipo de objeto PowerBuilder por extensão | O tipo do objeto PowerBuilder deve ser identificado automaticamente pela extensão do arquivo.                                   |
| RN-007 | Mapeamento `.srw`                        | Arquivos `.srw` devem ser classificados como `PowerBuilder Window`.                                                             |
| RN-008 | Mapeamento `.sru`                        | Arquivos `.sru` devem ser classificados como `PowerBuilder User Object`.                                                        |
| RN-009 | Mapeamento `.srd`                        | Arquivos `.srd` devem ser classificados como `PowerBuilder DataWindow`.                                                         |
| RN-010 | Mapeamento `.srm`                        | Arquivos `.srm` devem ser classificados como `PowerBuilder Menu`.                                                               |
| RN-011 | Mapeamento `.srf`                        | Arquivos `.srf` devem ser classificados como `PowerBuilder Function`.                                                           |
| RN-012 | Mapeamento `.sra`                        | Arquivos `.sra` devem ser classificados como `PowerBuilder Application`.                                                        |
| RN-013 | Mapeamento `.srs`                        | Arquivos `.srs` devem ser classificados como `PowerBuilder Structure`.                                                          |
| RN-014 | Fallback de encoding                     | Ao ler arquivos enviados, o sistema deve tentar `utf-8`; se falhar, tentar `latin-1`; se falhar, tentar `cp1252`.               |
| RN-015 | Conteúdo pesquisável                     | Todo conteúdo cadastrado manualmente ou extraído de arquivo deve ser registrado no SQLite e indexado para busca textual.        |
| RN-016 | Marcação de regra de negócio             | Um conteúdo pode ser marcado como regra de negócio, permitindo filtro e identificação diferenciada.                             |
| RN-017 | Regras de negócio exigem classificação   | Conteúdos marcados como regra de negócio devem permitir associação a sistema e domínio.                                         |
| RN-018 | Configuração centralizada                | Sistemas, domínios, linguagens, extensões aceitas, tipos de objeto e tags pré-cadastradas devem ser definidos no `config.yaml`. |
| RN-019 | Busca textual com filtros                | A busca deve permitir texto livre e filtros complementares por metadados.                                                       |
| RN-020 | Visualização formatada                   | Conteúdos técnicos devem ser exibidos usando estrutura HTML que preserve formatação, especialmente `<pre><code>`.               |

---

## 5. Critérios de aceitação gerais do MVP

O MVP poderá ser considerado pronto quando os critérios abaixo forem atendidos:

| ID     | Critério de aceitação                                                                                                         |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| CA-001 | A aplicação inicia localmente usando Python 3.11, ambiente virtual `venv` e FastAPI.                                          |
| CA-002 | A estrutura mínima de pastas existe conforme definido: `backend/`, `frontend/`, `uploads/`, `prompts/`, `tarefas/`, `tests/`. |
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
| CA-027 | Existem artefatos simulados de Feature, User Story e tarefas técnicas na proposta documental.                                 |
| CA-028 | O sistema não inclui autenticação, múltiplos usuários ou recursos fora do escopo do MVP.                                      |

---

## 6. Casos de uso ou fluxos principais

### 6.1 Cadastrar conteúdo manualmente

**Ator principal:** Usuário técnico.

**Objetivo:** Registrar manualmente uma anotação, snippet, SQL, script ou regra de negócio.

**Fluxo principal:**

1. O usuário acessa a tela de cadastro.
2. O sistema exibe formulário com campos de título, conteúdo e metadados.
3. O usuário informa o título.
4. O usuário cola ou digita o conteúdo técnico.
5. O usuário seleciona categoria, linguagem, sistema, domínio e tags, quando aplicável.
6. O usuário indica se o conteúdo é regra de negócio.
7. O usuário confirma o cadastro.
8. O sistema valida os dados obrigatórios.
9. O sistema grava o conteúdo no SQLite.
10. O sistema atualiza o índice textual.
11. O sistema exibe confirmação de cadastro.

**Fluxos alternativos:**

| Situação               | Tratamento                                |
| ---------------------- | ----------------------------------------- |
| Título não informado   | O sistema solicita preenchimento.         |
| Conteúdo não informado | O sistema solicita preenchimento.         |
| Falha ao gravar        | O sistema exibe mensagem de erro simples. |

---

### 6.2 Fazer upload de arquivo

**Ator principal:** Usuário técnico.

**Objetivo:** Enviar um arquivo textual para armazenamento, extração e indexação.

**Fluxo principal:**

1. O usuário acessa a tela de upload.
2. O sistema exibe opção para selecionar um arquivo.
3. O usuário seleciona um arquivo local.
4. O sistema valida a extensão.
5. O sistema valida o tamanho máximo de 12 MB.
6. O sistema salva o arquivo na pasta `uploads/`.
7. O sistema tenta ler o conteúdo com `utf-8`.
8. Se necessário, o sistema tenta `latin-1` e depois `cp1252`.
9. O sistema identifica linguagem e tipo de objeto conforme extensão.
10. O sistema grava metadados e conteúdo textual no SQLite.
11. O sistema indexa o conteúdo usando FTS5.
12. O sistema exibe confirmação de upload.

**Fluxos alternativos:**

| Situação                       | Tratamento                                              |
| ------------------------------ | ------------------------------------------------------- |
| Extensão inválida              | O sistema rejeita o arquivo e informa o motivo.         |
| Arquivo maior que 12 MB        | O sistema rejeita o arquivo e informa o limite.         |
| Falha de leitura               | O sistema informa que não foi possível extrair o texto. |
| Tipo PowerBuilder identificado | O sistema classifica automaticamente o tipo do objeto.  |

---

### 6.3 Pesquisar conteúdo

**Ator principal:** Usuário técnico.

**Objetivo:** Localizar conteúdos cadastrados usando busca textual e filtros.

**Fluxo principal:**

1. O usuário acessa a tela de pesquisa.
2. O sistema exibe campo de texto livre e filtros.
3. O usuário informa uma palavra, expressão ou trecho técnico.
4. O usuário seleciona filtros opcionais.
5. O sistema consulta o índice FTS5 e aplica filtros.
6. O sistema exibe a lista de resultados.
7. O usuário seleciona um resultado para visualizar.

**Fluxos alternativos:**

| Situação                        | Tratamento                                            |
| ------------------------------- | ----------------------------------------------------- |
| Nenhum resultado encontrado     | O sistema exibe mensagem informativa.                 |
| Busca sem texto, apenas filtros | O sistema lista conteúdos compatíveis com os filtros. |
| Nenhum filtro informado         | O sistema pesquisa apenas pelo texto livre.           |

---

### 6.4 Visualizar conteúdo

**Ator principal:** Usuário técnico.

**Objetivo:** Visualizar o conteúdo técnico preservando formatação.

**Fluxo principal:**

1. O usuário seleciona um conteúdo na lista ou resultado de busca.
2. O sistema abre a tela de detalhes.
3. O sistema exibe título e metadados.
4. O sistema exibe o conteúdo dentro de `<pre><code>`.
5. O sistema aplica Highlight.js conforme linguagem.
6. O usuário lê ou copia o conteúdo.

**Fluxos alternativos:**

| Situação                   | Tratamento                                          |
| -------------------------- | --------------------------------------------------- |
| Linguagem não identificada | O sistema exibe o conteúdo sem destaque específico. |
| Conteúdo muito longo       | O sistema exibe em bloco rolável, se necessário.    |

---

### 6.5 Editar conteúdo

**Ator principal:** Usuário técnico.

**Objetivo:** Alterar conteúdo ou metadados já cadastrados.

**Fluxo principal:**

1. O usuário acessa um conteúdo existente.
2. O usuário aciona a opção de edição.
3. O sistema exibe formulário preenchido.
4. O usuário altera conteúdo ou metadados.
5. O usuário confirma a alteração.
6. O sistema valida os dados.
7. O sistema atualiza o registro no SQLite.
8. O sistema atualiza o índice textual.
9. O sistema exibe confirmação.

---

### 6.6 Excluir conteúdo

**Ator principal:** Usuário técnico.

**Objetivo:** Remover um conteúdo cadastrado.

**Fluxo principal:**

1. O usuário acessa um conteúdo existente.
2. O usuário aciona a opção de exclusão.
3. O sistema solicita confirmação.
4. O usuário confirma.
5. O sistema remove o conteúdo do SQLite.
6. O sistema remove ou atualiza o índice textual correspondente.
7. O sistema exibe confirmação.

**Observação crítica:**
Mesmo no MVP, é recomendável solicitar confirmação antes da exclusão para evitar perda acidental.

---

## 7. Modelo conceitual inicial dos dados

> Este modelo é conceitual. Não representa ainda o modelo físico definitivo do banco.

### 7.1 Principais entidades e conceitos

| Entidade / Conceito | Descrição                                                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Conteúdo Técnico    | Representa o item principal armazenado no sistema. Pode ser anotação, snippet, SQL, script, regra de negócio ou conteúdo extraído de arquivo. |
| Arquivo Enviado     | Representa um arquivo submetido via upload e salvo em `uploads/`.                                                                             |
| Categoria           | Classificação geral do conteúdo, como snippet, SQL, anotação, script, regra ou exemplo.                                                       |
| Linguagem           | Linguagem ou tecnologia associada ao conteúdo, como Python, Java, SQL, Markdown ou PowerBuilder.                                              |
| Tag                 | Marcador flexível usado para agrupar conteúdos por assunto.                                                                                   |
| Sistema             | Sistema relacionado ao conteúdo, especialmente útil para regras de negócio e arquivos legados.                                                |
| Domínio             | Área funcional ou domínio de negócio associado ao conteúdo.                                                                                   |
| Tipo de Arquivo     | Tipo identificado a partir da extensão do arquivo enviado.                                                                                    |
| Tipo de Objeto      | Tipo específico de objeto técnico, especialmente para PowerBuilder.                                                                           |
| Índice Textual      | Estrutura de busca baseada em SQLite FTS5 para pesquisar conteúdo textual.                                                                    |
| Configuração        | Representação lógica das listas e mapeamentos definidos em `config.yaml`.                                                                     |

---

### 7.2 Relações conceituais

| Relação                                         | Descrição                                                                                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Conteúdo Técnico pode ter Arquivo Enviado       | Um conteúdo pode ter origem manual ou origem em upload.                                                |
| Conteúdo Técnico possui Categoria               | Cada conteúdo deve poder ser classificado por uma categoria.                                           |
| Conteúdo Técnico possui Linguagem               | Cada conteúdo pode estar associado a uma linguagem.                                                    |
| Conteúdo Técnico pode possuir várias Tags       | Um conteúdo pode ser marcado com uma ou mais tags.                                                     |
| Conteúdo Técnico pode estar associado a Sistema | Útil para organizar conteúdos por sistema legado ou aplicação.                                         |
| Conteúdo Técnico pode estar associado a Domínio | Útil para regras de negócio e agrupamentos funcionais.                                                 |
| Arquivo Enviado possui Tipo de Arquivo          | O tipo pode ser inferido pela extensão.                                                                |
| Arquivo PowerBuilder possui Tipo de Objeto      | Arquivos `.srw`, `.sru`, `.srd`, `.srm`, `.srf`, `.sra` e `.srs` devem gerar classificação específica. |
| Conteúdo Técnico alimenta Índice Textual        | O texto cadastrado ou extraído deve ser indexado para busca.                                           |

---

### 7.3 Atributos conceituais sugeridos

#### Conteúdo Técnico

| Atributo            | Descrição                               |
| ------------------- | --------------------------------------- |
| Identificador       | Código interno do conteúdo.             |
| Título              | Nome descritivo informado pelo usuário. |
| Conteúdo textual    | Texto manual ou extraído de arquivo.    |
| Categoria           | Classificação geral.                    |
| Linguagem           | Linguagem associada.                    |
| Sistema             | Sistema relacionado.                    |
| Domínio             | Domínio funcional.                      |
| Tags                | Lista de marcadores.                    |
| É regra de negócio  | Indicador booleano.                     |
| Data de criação     | Data/hora de cadastro.                  |
| Data de atualização | Data/hora da última alteração.          |

#### Arquivo Enviado

| Atributo        | Descrição                             |
| --------------- | ------------------------------------- |
| Nome original   | Nome do arquivo enviado pelo usuário. |
| Nome salvo      | Nome usado no armazenamento local.    |
| Caminho local   | Caminho dentro de `uploads/`.         |
| Extensão        | Extensão do arquivo.                  |
| Tamanho         | Tamanho do arquivo.                   |
| Encoding usado  | Encoding utilizado na leitura.        |
| Tipo de arquivo | Tipo geral identificado.              |
| Tipo de objeto  | Tipo específico, quando aplicável.    |

#### Índice Textual

| Atributo               | Descrição                       |
| ---------------------- | ------------------------------- |
| Referência do conteúdo | Ligação com o conteúdo técnico. |
| Título indexado        | Título usado na busca.          |
| Conteúdo indexado      | Texto pesquisável.              |
| Metadados auxiliares   | Campos úteis para filtros.      |

---

## 8. Pontos de atenção e riscos

| ID    | Risco / Ponto de atenção             | Impacto                                                                        | Mitigação sugerida                                                                |
| ----- | ------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| R-001 | Encoding de arquivos legados         | Arquivos PowerBuilder podem não estar em UTF-8 e falhar na leitura.            | Implementar fallback `utf-8`, `latin-1`, `cp1252`.                                |
| R-002 | Busca com SQLite FTS5                | FTS5 exige cuidado na criação, atualização e remoção do índice.                | Testar cadastro, edição, exclusão e busca.                                        |
| R-003 | Preservação de formatação            | Conteúdos técnicos perdem valor se indentação e quebras forem alteradas.       | Exibir sempre com `<pre><code>`.                                                  |
| R-004 | Escopo excessivo                     | O projeto pode crescer demais e perder o caráter didático do MVP.              | Manter fora do MVP autenticação, produção, backup e frontend sofisticado.         |
| R-005 | Upload de arquivos inadequados       | Usuário pode enviar arquivos binários ou extensões indevidas.                  | Validar extensão e tamanho antes de processar.                                    |
| R-006 | Classificação automática incompleta  | Nem toda extensão permite inferir domínio, sistema ou categoria.               | Inferir apenas o que for seguro; permitir ajuste manual.                          |
| R-007 | Highlight.js com linguagem incorreta | Destaque pode ficar ruim se linguagem for mal definida.                        | Permitir linguagem padrão ou genérica.                                            |
| R-008 | Configuração inconsistente           | `config.yaml` pode conter listas incompletas ou mapeamentos inválidos.         | Validar configuração no início da aplicação.                                      |
| R-009 | Exclusão acidental                   | Usuário pode apagar conteúdo importante.                                       | Solicitar confirmação antes da exclusão.                                          |
| R-010 | Testes negligenciados                | MVP didático pode acabar sem testes úteis.                                     | Criar testes para regras principais: upload, extensão, tamanho, encoding e busca. |
| R-011 | Arquivos grandes dentro do limite    | Mesmo abaixo de 12 MB, arquivos podem gerar conteúdo grande para visualização. | Usar visualização simples e considerar rolagem no bloco de conteúdo.              |
| R-012 | Acoplamento entre regras e interface | Regras de validação podem ficar presas nos templates.                          | Concentrar validações no backend.                                                 |

---

## 9. Perguntas em aberto

| ID     | Pergunta                                                                                          | Motivo                                                        |
| ------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| PA-001 | Quais categorias iniciais devem existir no `config.yaml`?                                         | Ajuda a padronizar o cadastro.                                |
| PA-002 | Quais sistemas devem vir pré-cadastrados?                                                         | Necessário para classificação por sistema.                    |
| PA-003 | Quais domínios de negócio devem ser usados inicialmente?                                          | Importante para regras de negócio.                            |
| PA-004 | As tags serão apenas pré-cadastradas ou o usuário poderá criar novas tags pela tela?              | Afeta complexidade do cadastro.                               |
| PA-005 | A exclusão será física ou lógica no MVP?                                                          | Exclusão lógica preserva histórico, mas aumenta complexidade. |
| PA-006 | O conteúdo de arquivos enviados poderá ser editado depois do upload?                              | Afeta rastreabilidade entre arquivo original e texto editado. |
| PA-007 | O sistema deve permitir download do arquivo original enviado?                                     | Não foi exigido, mas pode ser útil.                           |
| PA-008 | O nome do arquivo salvo em `uploads/` deve preservar o nome original ou usar identificador único? | Evita conflito de nomes.                                      |
| PA-009 | Como tratar arquivos com conteúdo parcialmente ilegível?                                          | Pode ocorrer em arquivos legados.                             |
| PA-010 | A busca deve pesquisar apenas no conteúdo ou também em título e metadados?                        | Afeta configuração do índice FTS5.                            |
| PA-011 | Os filtros devem ser combinados com lógica `E` ou permitir lógica `OU`?                           | Afeta comportamento da pesquisa.                              |
| PA-012 | A tela inicial deve exibir últimos cadastrados ou abrir diretamente na pesquisa?                  | Decisão simples de experiência do usuário.                    |
| PA-013 | O MVP deve registrar data de criação e atualização?                                               | Recomendável para organização.                                |
| PA-014 | Será necessário importar vários arquivos futuramente?                                             | Fora do MVP, mas pode orientar evolução.                      |
| PA-015 | Haverá necessidade futura de versionar alterações de conteúdos?                                   | Fora do MVP, mas relevante para evolução.                     |

---

# 10. Artefatos simulando Azure DevOps

> Os artefatos abaixo são apenas propostas em Markdown para futura gravação na pasta `tarefas/`.
> Nenhum arquivo real está sendo criado.

---

## 10.1 Feature única do produto

### Nome sugerido do arquivo Markdown

`FEAT-001-devnotes-local-mvp.md`

---

### Título da Feature

**FEAT-001 — MVP do DevNotes Local para cadastro, organização, busca e visualização de conteúdos técnicos**

---

### Descrição

Implementar o MVP do DevNotes Local, uma aplicação web local para armazenamento, classificação, pesquisa e visualização de conteúdos técnicos, incluindo snippets, SQLs, scripts, anotações, regras de negócio e arquivos textuais de sistemas legados.

A Feature deve contemplar cadastro manual, upload simples de arquivos, validação de extensão e tamanho, leitura com fallback de encoding, gravação em SQLite, indexação com SQLite FTS5, busca textual com filtros, visualização preservando formatação e destaque de sintaxe com Highlight.js.

---

### Objetivo de negócio

Centralizar conteúdos técnicos usados em estudo e desenvolvimento de software, reduzindo dispersão de informações e facilitando a reutilização de snippets, SQLs, scripts, regras de negócio e arquivos legados em um ambiente local simples.

---

### Critérios de aceitação

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

### Observações técnicas

* O MVP deve evitar recursos fora do escopo, como autenticação, múltiplos usuários, publicação em produção e microsserviços.
* O projeto deve manter estrutura didática, adequada para estudo de SDLC.
* As listas e mapeamentos devem ser centralizados em `config.yaml`.
* A pasta `prompts/` deve armazenar prompts usados durante o desenvolvimento.
* A pasta `tarefas/` deve armazenar os artefatos simulados de gestão do projeto.

---

## 10.2 User Story principal

### Nome sugerido do arquivo Markdown

`US-001-gerenciar-conteudos-tecnicos-locais.md`

---

### Título da User Story

**US-001 — Gerenciar conteúdos técnicos locais para consulta e reutilização**

---

### História

Como **desenvolvedor de software**,
quero **cadastrar, classificar, pesquisar e visualizar conteúdos técnicos em uma aplicação local**,
para **reutilizar snippets, SQLs, scripts, regras de negócio e arquivos legados de forma mais organizada**.

---

### Descrição

A aplicação deve permitir que o usuário registre conteúdos técnicos manualmente ou por upload de arquivos textuais. Esses conteúdos devem ser classificados por categoria, linguagem, tags, sistema e domínio, podendo também ser marcados como regra de negócio.

O sistema deve permitir busca textual usando SQLite FTS5, combinada com filtros. A visualização deve preservar a formatação original do conteúdo e aplicar destaque de sintaxe com Highlight.js.

---

### Critérios de aceitação

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

### Regras envolvidas

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

### Observações técnicas

* O cadastro manual e o upload devem alimentar a mesma base conceitual de conteúdos técnicos.
* O índice FTS5 deve ser atualizado após cadastro, edição e exclusão.
* A visualização deve priorizar legibilidade e preservação textual.
* O MVP não deve incluir autenticação nem múltiplos usuários.

---

## 10.3 Tarefas técnicas necessárias

---

### Tarefa 1

**Nome sugerido do arquivo Markdown:**
`TASK-001-criar-estrutura-inicial-projeto.md`

**Título da tarefa:**
Criar estrutura inicial do projeto

**Descrição:**
Criar a estrutura mínima de diretórios e arquivos do projeto DevNotes Local, respeitando a organização definida para o MVP.

**Critérios de aceitação:**

* Estrutura contém `backend/`.
* Estrutura contém `frontend/`.
* Estrutura contém `uploads/`.
* Estrutura contém `prompts/`.
* Estrutura contém `tarefas/`.
* Estrutura contém `tests/`.
* Arquivos base `README.md`, `requirements.txt`, `.gitignore` e `config.yaml` estão previstos.

**Dependências:**
Nenhuma.

**Observações técnicas:**
A estrutura deve ser simples e didática, evitando separações excessivamente sofisticadas.

---

### Tarefa 2

**Nome sugerido do arquivo Markdown:**
`TASK-002-configurar-ambiente-python-venv.md`

**Título da tarefa:**
Configurar ambiente Python com venv

**Descrição:**
Configurar o ambiente virtual local do projeto usando Python 3.11 e preparar o arquivo de dependências.

**Critérios de aceitação:**

* Ambiente virtual pode ser criado com `venv`.
* Dependências do MVP estão previstas no `requirements.txt`.
* O projeto pode ser executado localmente a partir do ambiente virtual.

**Dependências:**
TASK-001.

**Observações técnicas:**
O README deve futuramente explicar como criar e ativar o ambiente virtual.

---

### Tarefa 3

**Nome sugerido do arquivo Markdown:**
`TASK-003-configurar-fastapi.md`

**Título da tarefa:**
Configurar FastAPI

**Descrição:**
Preparar a aplicação FastAPI como backend principal do DevNotes Local.

**Critérios de aceitação:**

* Aplicação FastAPI inicial está definida.
* Existe rota básica de verificação da aplicação.
* O backend pode ser iniciado localmente.
* A estrutura permite adicionar rotas de cadastro, upload, busca e visualização.

**Dependências:**
TASK-001, TASK-002.

**Observações técnicas:**
Não incluir autenticação no MVP.

---

### Tarefa 4

**Nome sugerido do arquivo Markdown:**
`TASK-004-configurar-jinja2.md`

**Título da tarefa:**
Configurar Jinja2

**Descrição:**
Configurar o uso de templates Jinja2 para renderização das páginas HTML da aplicação.

**Critérios de aceitação:**

* O backend consegue renderizar templates HTML.
* Existe estrutura prevista para templates.
* Existe estrutura prevista para arquivos estáticos.
* Uma página inicial simples pode ser renderizada.

**Dependências:**
TASK-003.

**Observações técnicas:**
O frontend deve permanecer simples, usando HTML e CSS básico.

---

### Tarefa 5

**Nome sugerido do arquivo Markdown:**
`TASK-005-configurar-sqlite-sqlalchemy.md`

**Título da tarefa:**
Configurar SQLite e SQLAlchemy

**Descrição:**
Configurar persistência local com SQLite e camada de acesso a dados com SQLAlchemy.

**Critérios de aceitação:**

* Banco SQLite local está configurado.
* SQLAlchemy está configurado para acesso ao banco.
* A aplicação consegue abrir conexão com o banco.
* A estrutura permite criação das entidades iniciais.

**Dependências:**
TASK-002, TASK-003.

**Observações técnicas:**
Evitar complexidade de banco externo no MVP.

---

### Tarefa 6

**Nome sugerido do arquivo Markdown:**
`TASK-006-criar-config-yaml.md`

**Título da tarefa:**
Criar arquivo `config.yaml`

**Descrição:**
Criar o arquivo de configuração centralizada do MVP contendo listas e mapeamentos utilizados pela aplicação.

**Critérios de aceitação:**

* `config.yaml` contém sistemas.
* `config.yaml` contém domínios.
* `config.yaml` contém linguagens.
* `config.yaml` contém extensões aceitas.
* `config.yaml` contém mapeamento de extensão para tipo de objeto.
* `config.yaml` contém tags pré-cadastradas.

**Dependências:**
TASK-001.

**Observações técnicas:**
O arquivo deve evitar valores fixos espalhados no código da aplicação.

---

### Tarefa 7

**Nome sugerido do arquivo Markdown:**
`TASK-007-modelar-entidades-iniciais.md`

**Título da tarefa:**
Modelar entidades iniciais

**Descrição:**
Definir a modelagem inicial das entidades necessárias ao MVP, considerando conteúdo técnico, arquivo enviado, tags, sistema, domínio, linguagem, tipo de objeto e índice textual.

**Critérios de aceitação:**

* Existe entidade conceitual para conteúdo técnico.
* Existe representação para metadados de arquivo enviado.
* Existe forma de representar categoria, linguagem, sistema e domínio.
* Existe forma de associar tags ao conteúdo.
* Existe previsão de integração com índice textual FTS5.

**Dependências:**
TASK-005, TASK-006.

**Observações técnicas:**
Não é necessário sofisticar o modelo para múltiplos usuários ou versionamento.

---

### Tarefa 8

**Nome sugerido do arquivo Markdown:**
`TASK-008-implementar-cadastro-manual-conteudo.md`

**Título da tarefa:**
Implementar cadastro manual de conteúdo

**Descrição:**
Permitir que o usuário cadastre manualmente conteúdos técnicos com título, texto e metadados.

**Critérios de aceitação:**

* Usuário consegue informar título.
* Usuário consegue informar conteúdo textual.
* Usuário consegue selecionar ou informar metadados.
* Sistema grava o conteúdo no SQLite.
* Sistema prepara o conteúdo para indexação textual.

**Dependências:**
TASK-004, TASK-005, TASK-007.

**Observações técnicas:**
O formulário deve ser simples e funcional.

---

### Tarefa 9

**Nome sugerido do arquivo Markdown:**
`TASK-009-implementar-edicao-conteudo.md`

**Título da tarefa:**
Implementar edição de conteúdo

**Descrição:**
Permitir que o usuário edite conteúdos técnicos previamente cadastrados.

**Critérios de aceitação:**

* Usuário consegue abrir conteúdo existente para edição.
* Sistema exibe dados atuais preenchidos.
* Usuário consegue alterar texto e metadados.
* Sistema salva alterações no SQLite.
* Sistema atualiza o índice textual após edição.

**Dependências:**
TASK-008, TASK-018.

**Observações técnicas:**
A edição deve manter consistência entre conteúdo salvo e conteúdo indexado.

---

### Tarefa 10

**Nome sugerido do arquivo Markdown:**
`TASK-010-implementar-exclusao-conteudo.md`

**Título da tarefa:**
Implementar exclusão de conteúdo

**Descrição:**
Permitir que o usuário exclua conteúdos cadastrados.

**Critérios de aceitação:**

* Usuário consegue solicitar exclusão de conteúdo.
* Sistema solicita confirmação.
* Sistema remove o conteúdo do SQLite.
* Sistema remove ou atualiza o índice textual correspondente.
* Sistema exibe confirmação após exclusão.

**Dependências:**
TASK-008, TASK-018.

**Observações técnicas:**
Para o MVP, exclusão física é aceitável, desde que confirmada pelo usuário.

---

### Tarefa 11

**Nome sugerido do arquivo Markdown:**
`TASK-011-implementar-upload-simples-arquivo.md`

**Título da tarefa:**
Implementar upload simples de arquivo

**Descrição:**
Permitir que o usuário envie um arquivo por vez para armazenamento local e extração de conteúdo textual.

**Critérios de aceitação:**

* Tela permite selecionar um arquivo.
* Sistema recebe apenas um arquivo por operação.
* Sistema salva arquivo válido na pasta `uploads/`.
* Sistema registra metadados básicos do arquivo.

**Dependências:**
TASK-003, TASK-004, TASK-005.

**Observações técnicas:**
O upload deve ser simples, sem múltiplos arquivos no MVP.

---

### Tarefa 12

**Nome sugerido do arquivo Markdown:**
`TASK-012-validar-extensao-arquivo.md`

**Título da tarefa:**
Validar extensão de arquivo

**Descrição:**
Implementar validação para aceitar somente arquivos com extensões permitidas.

**Critérios de aceitação:**

* Sistema consulta extensões permitidas no `config.yaml`.
* Sistema aceita arquivos com extensões configuradas.
* Sistema rejeita arquivos com extensões não permitidas.
* Sistema exibe mensagem clara quando rejeitar arquivo.

**Dependências:**
TASK-006, TASK-011.

**Observações técnicas:**
A validação deve considerar extensão de forma segura e padronizada.

---

### Tarefa 13

**Nome sugerido do arquivo Markdown:**
`TASK-013-validar-tamanho-maximo-upload.md`

**Título da tarefa:**
Validar tamanho máximo de 12 MB

**Descrição:**
Implementar validação para rejeitar arquivos maiores que 12 MB.

**Critérios de aceitação:**

* Sistema identifica o tamanho do arquivo enviado.
* Sistema aceita arquivos com até 12 MB.
* Sistema rejeita arquivos acima de 12 MB.
* Sistema informa o limite ao usuário.

**Dependências:**
TASK-011.

**Observações técnicas:**
O limite deve ser centralizado ou facilmente configurável.

---

### Tarefa 14

**Nome sugerido do arquivo Markdown:**
`TASK-014-implementar-leitura-fallback-encoding.md`

**Título da tarefa:**
Implementar leitura de arquivos com fallback de encoding

**Descrição:**
Implementar leitura textual de arquivos enviados tentando `utf-8`, depois `latin-1` e depois `cp1252`.

**Critérios de aceitação:**

* Sistema tenta ler inicialmente com `utf-8`.
* Se falhar, tenta `latin-1`.
* Se falhar, tenta `cp1252`.
* Sistema registra ou identifica qual encoding foi utilizado.
* Sistema trata falha final de leitura com mensagem clara.

**Dependências:**
TASK-011, TASK-012, TASK-013.

**Observações técnicas:**
Essa tarefa é importante para arquivos legados PowerBuilder.

---

### Tarefa 15

**Nome sugerido do arquivo Markdown:**
`TASK-015-classificar-automaticamente-por-extensao.md`

**Título da tarefa:**
Classificar automaticamente por extensão

**Descrição:**
Implementar classificação automática de linguagem e tipo de objeto com base na extensão do arquivo.

**Critérios de aceitação:**

* Arquivos `.py` são classificados como Python.
* Arquivos `.java` são classificados como Java.
* Arquivos `.sql` são classificados como SQL.
* Arquivos `.md` são classificados como Markdown.
* Arquivos `.txt` são classificados como Texto.
* Arquivos PowerBuilder são classificados como linguagem PowerBuilder.
* Arquivos PowerBuilder recebem tipo de objeto conforme extensão.

**Dependências:**
TASK-006, TASK-014.

**Observações técnicas:**
O mapeamento deve vir do `config.yaml`.

---

### Tarefa 16

**Nome sugerido do arquivo Markdown:**
`TASK-016-gravar-metadados-conteudo-arquivo.md`

**Título da tarefa:**
Gravar metadados do conteúdo e do arquivo

**Descrição:**
Gravar no SQLite os metadados associados a conteúdos cadastrados manualmente e arquivos enviados.

**Critérios de aceitação:**

* Sistema grava título.
* Sistema grava categoria.
* Sistema grava linguagem.
* Sistema grava sistema e domínio, quando informados.
* Sistema grava tags, quando informadas.
* Sistema grava indicador de regra de negócio.
* Para upload, sistema grava nome original, extensão, caminho local, tamanho e tipo de objeto.

**Dependências:**
TASK-007, TASK-008, TASK-011, TASK-015.

**Observações técnicas:**
Os metadados serão essenciais para filtros e organização.

---

### Tarefa 17

**Nome sugerido do arquivo Markdown:**
`TASK-017-configurar-indexacao-sqlite-fts5.md`

**Título da tarefa:**
Configurar indexação com SQLite FTS5

**Descrição:**
Criar estrutura de indexação textual usando SQLite FTS5 para permitir pesquisa eficiente no conteúdo técnico.

**Critérios de aceitação:**

* Existe estrutura FTS5 para indexar conteúdo textual.
* Conteúdos cadastrados manualmente são indexados.
* Conteúdos extraídos de upload são indexados.
* O índice é atualizado após edição.
* O índice é atualizado após exclusão.

**Dependências:**
TASK-005, TASK-007, TASK-008, TASK-011.

**Observações técnicas:**
É uma das partes tecnicamente mais importantes do MVP.

---

### Tarefa 18

**Nome sugerido do arquivo Markdown:**
`TASK-018-implementar-pesquisa-textual-filtros.md`

**Título da tarefa:**
Implementar pesquisa textual com filtros

**Descrição:**
Permitir pesquisa por texto livre usando FTS5 e filtros por metadados.

**Critérios de aceitação:**

* Usuário consegue pesquisar por texto livre.
* Usuário consegue filtrar por categoria.
* Usuário consegue filtrar por linguagem.
* Usuário consegue filtrar por sistema.
* Usuário consegue filtrar por domínio.
* Usuário consegue filtrar por tags.
* Usuário consegue filtrar conteúdos marcados como regra de negócio.
* Sistema exibe lista de resultados.

**Dependências:**
TASK-016, TASK-017.

**Observações técnicas:**
A busca deve ser simples, mas útil. Não é necessário implementar ranking sofisticado no MVP.

---

### Tarefa 19

**Nome sugerido do arquivo Markdown:**
`TASK-019-implementar-visualizacao-pre-code.md`

**Título da tarefa:**
Implementar visualização com `<pre><code>`

**Descrição:**
Exibir conteúdos técnicos preservando quebras de linha, espaços e indentação.

**Critérios de aceitação:**

* Tela de detalhe exibe título e metadados.
* Conteúdo é exibido dentro de `<pre><code>`.
* Quebras de linha são preservadas.
* Indentação é preservada.
* Conteúdos longos continuam legíveis.

**Dependências:**
TASK-004, TASK-008, TASK-011.

**Observações técnicas:**
Esse requisito é essencial para snippets, SQLs, scripts e arquivos PowerBuilder.

---

### Tarefa 20

**Nome sugerido do arquivo Markdown:**
`TASK-020-integrar-highlightjs.md`

**Título da tarefa:**
Integrar Highlight.js

**Descrição:**
Integrar Highlight.js à tela de visualização para destaque de sintaxe.

**Critérios de aceitação:**

* Highlight.js é carregado na página de visualização.
* O destaque de sintaxe é aplicado ao bloco de conteúdo.
* A linguagem do conteúdo é usada quando disponível.
* Conteúdos sem linguagem identificada continuam visíveis sem erro.

**Dependências:**
TASK-019, TASK-015.

**Observações técnicas:**
O destaque deve ser apoio visual, não requisito para interpretação semântica do conteúdo.

---

### Tarefa 21

**Nome sugerido do arquivo Markdown:**
`TASK-021-criar-testes-pytest.md`

**Título da tarefa:**
Criar testes com pytest

**Descrição:**
Criar testes automatizados para validar as principais regras e fluxos do MVP.

**Critérios de aceitação:**

* Existem testes para validação de extensão.
* Existem testes para validação de tamanho máximo.
* Existem testes para fallback de encoding.
* Existem testes para classificação por extensão.
* Existem testes para cadastro de conteúdo.
* Existem testes para busca textual.
* Existem testes para filtros principais.
* Os testes podem ser executados com pytest.

**Dependências:**
TASK-012, TASK-013, TASK-014, TASK-015, TASK-017, TASK-018.

**Observações técnicas:**
Os testes devem priorizar regras do domínio do MVP, não apenas inicialização da aplicação.

---

### Tarefa 22

**Nome sugerido do arquivo Markdown:**
`TASK-022-documentar-readme.md`

**Título da tarefa:**
Criar documentação básica no README.md

**Descrição:**
Documentar o objetivo do projeto, escopo do MVP, tecnologias usadas, como executar localmente e principais funcionalidades.

**Critérios de aceitação:**

* README descreve o objetivo do DevNotes Local.
* README informa tecnologias utilizadas.
* README explica como configurar ambiente virtual.
* README explica como instalar dependências.
* README explica como executar a aplicação.
* README lista funcionalidades do MVP.
* README informa o que está fora do escopo.
* README cita o uso didático das pastas `prompts/` e `tarefas/`.

**Dependências:**
TASK-001, TASK-002, TASK-003.

**Observações técnicas:**
O README deve ser simples, direto e útil para retomada futura do projeto.

---

## 10.4 Visão resumida das tarefas

| Tarefa   | Título                                   | Dependências principais                |
| -------- | ---------------------------------------- | -------------------------------------- |
| TASK-001 | Criar estrutura inicial do projeto       | Nenhuma                                |
| TASK-002 | Configurar ambiente Python com venv      | TASK-001                               |
| TASK-003 | Configurar FastAPI                       | TASK-001, TASK-002                     |
| TASK-004 | Configurar Jinja2                        | TASK-003                               |
| TASK-005 | Configurar SQLite e SQLAlchemy           | TASK-002, TASK-003                     |
| TASK-006 | Criar `config.yaml`                      | TASK-001                               |
| TASK-007 | Modelar entidades iniciais               | TASK-005, TASK-006                     |
| TASK-008 | Implementar cadastro manual              | TASK-004, TASK-005, TASK-007           |
| TASK-009 | Implementar edição                       | TASK-008, TASK-018                     |
| TASK-010 | Implementar exclusão                     | TASK-008, TASK-018                     |
| TASK-011 | Implementar upload simples               | TASK-003, TASK-004, TASK-005           |
| TASK-012 | Validar extensão                         | TASK-006, TASK-011                     |
| TASK-013 | Validar tamanho máximo                   | TASK-011                               |
| TASK-014 | Ler arquivos com fallback de encoding    | TASK-011, TASK-012, TASK-013           |
| TASK-015 | Classificar automaticamente por extensão | TASK-006, TASK-014                     |
| TASK-016 | Gravar metadados                         | TASK-007, TASK-008, TASK-011, TASK-015 |
| TASK-017 | Configurar FTS5                          | TASK-005, TASK-007, TASK-008, TASK-011 |
| TASK-018 | Implementar pesquisa com filtros         | TASK-016, TASK-017                     |
| TASK-019 | Visualizar com `<pre><code>`             | TASK-004, TASK-008, TASK-011           |
| TASK-020 | Integrar Highlight.js                    | TASK-019, TASK-015                     |
| TASK-021 | Criar testes com pytest                  | TASK-012 a TASK-018                    |
| TASK-022 | Documentar README                        | TASK-001, TASK-002, TASK-003           |

---

## Observação final crítica

Para um MVP didático, o escopo está bem delimitado. O principal cuidado é não transformar o DevNotes Local em um sistema de gestão documental completo logo no início.

A decisão mais importante é manter o foco em quatro capacidades centrais:

1. **guardar conteúdo técnico;**
2. **classificar minimamente;**
3. **pesquisar com qualidade aceitável;**
4. **visualizar preservando formatação.**

Todo o restante deve ser tratado como evolução futura.
