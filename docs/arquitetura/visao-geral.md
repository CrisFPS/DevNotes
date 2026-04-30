# Arquitetura e Design da Solução — DevNotes Local

**Versão:** 1.0
**Atualizado em:** 2026-04-29

## Índice

- [1. Visão arquitetural geral](#1-visão-arquitetural-geral)
- [2. Estrutura de pastas e arquivos](#2-estrutura-de-pastas-e-arquivos)
- [3. Organização interna do backend](#3-organização-interna-do-backend)
- [4. Organização interna do frontend](#4-organização-interna-do-frontend)
- [5. Entidades e tabelas SQLite](#5-entidades-e-tabelas-sqlite)
- [6. Principais rotas FastAPI](#6-principais-rotas-fastapi)
- [7. Principais templates Jinja2](#7-principais-templates-jinja2)
- [8. Decisões arquiteturais](#8-decisões-arquiteturais)
- [9. Riscos técnicos e mitigação](#9-riscos-técnicos-e-mitigação)
- [10. O que não implementar nesta fase](#10-o-que-não-implementar-nesta-fase)
- [Diagramas](./diagramas.md)
- [Architecture Decision Records](./adr/)

---

## 1. Visão arquitetural geral

### Por que a solução será local

O DevNotes Local é um projeto didático e de uso pessoal. Não existe requisito de acesso remoto, colaboração entre múltiplos usuários ou disponibilidade contínua. Executar a aplicação localmente elimina a necessidade de infraestrutura em nuvem, configuração de servidores, domínios, certificados TLS, CI/CD e toda a complexidade que acompanha uma solução publicada. O usuário inicia a aplicação na própria máquina e a acessa pelo navegador em `http://localhost:8000`.

### Por que FastAPI com Jinja2 é suficiente

Para um MVP local com renderização server-side, FastAPI com Jinja2 é a escolha mais direta. FastAPI oferece rotas claras, validação de entrada, suporte a upload de arquivos e um servidor embutido via Uvicorn. Jinja2 renderiza páginas HTML no servidor, evitando a necessidade de um frontend separado com build, bundler ou framework JavaScript. O resultado é uma aplicação web funcional com pouquíssima infraestrutura.

Não há justificativa para usar React, Vue, Angular ou qualquer SPA neste contexto. Essas tecnologias aumentariam a complexidade, exigiriam Node.js, build pipeline e comunicação via API JSON separada.

### Por que SQLite é adequado

SQLite é um banco de dados embutido, sem necessidade de servidor, que armazena os dados em um único arquivo local. Para um sistema com uso individual, sem concorrência de escrita e com volume moderado de dados, SQLite é mais que suficiente. Ele também oferece suporte nativo ao SQLite FTS5, que é a base da busca textual do projeto.

Usar PostgreSQL ou SQL Server seria excesso técnico para um MVP local didático.

### Por que não são necessários microsserviços, SPA, Docker ou nuvem

| Tecnologia proposta | Por que não é necessária |
|---|---|
| Microsserviços | Excesso arquitetural para uma aplicação local com uso individual |
| SPA (React/Vue) | Requer infraestrutura de build, separação de API, maior esforço |
| Docker | Útil em produção, desnecessário para executar localmente com venv |
| Nuvem | Não há requisito de acesso remoto, escala ou disponibilidade |
| Mensageria / filas | Não há operações assíncronas ou distribuídas |

A boa arquitetura para este projeto é a mais simples que atende aos requisitos. Qualquer adição além disso torna o projeto menos didático e mais difícil de entregar.

---

## 2. Estrutura de pastas e arquivos

```text
devnotes-local/
│
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py                    # ponto de entrada do FastAPI
│       ├── config.py                  # leitura e exposição do config.yaml
│       ├── database.py                # configuração do SQLite e SQLAlchemy
│       ├── models/
│       │   ├── __init__.py
│       │   └── content.py             # modelos SQLAlchemy (tabelas)
│       ├── repositories/
│       │   ├── __init__.py
│       │   └── content_repository.py  # acesso a dados (CRUD + FTS)
│       ├── services/
│       │   ├── __init__.py
│       │   ├── content_service.py     # regras de conteúdo técnico
│       │   ├── upload_service.py      # orquestração do upload
│       │   ├── encoding_service.py    # leitura com fallback de encoding
│       │   ├── extension_classifier.py# classificação por extensão
│       │   └── search_service.py      # busca textual e filtros
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── content_routes.py      # cadastro, edição, exclusão, detalhe
│       │   ├── upload_routes.py       # upload de arquivo
│       │   └── search_routes.py       # pesquisa e filtros
│       └── schemas/
│           ├── __init__.py
│           └── content_schema.py      # schemas Pydantic para validação
│
├── frontend/
│   ├── templates/
│   │   ├── base.html                  # layout base com navegação
│   │   ├── index.html                 # página inicial
│   │   ├── list.html                  # listagem de conteúdos
│   │   ├── detail.html                # detalhe do conteúdo
│   │   ├── form.html                  # formulário de cadastro e edição
│   │   ├── search.html                # tela de pesquisa e resultados
│   │   └── upload.html                # tela de upload
│   └── static/
│       ├── css/
│       │   └── style.css              # estilos simples
│       └── js/
│           └── app.js                 # JS simples, apenas se necessário
│
├── uploads/                           # arquivos enviados pelos usuários
├── prompts/                           # prompts utilizados no projeto (didático)
├── docs/                              # documentação do projeto
├── tests/                             # testes automatizados com pytest
├── config.yaml                        # configuração centralizada do MVP
├── requirements.txt
├── README.md
└── .gitignore
```

### Justificativa das pastas principais

| Pasta | Responsabilidade |
|---|---|
| `backend/app/` | Concentra toda a lógica da aplicação FastAPI |
| `backend/app/models/` | Define as entidades mapeadas pelo SQLAlchemy |
| `backend/app/repositories/` | Isola o acesso ao banco; rotas e serviços não acessam SQLAlchemy diretamente |
| `backend/app/services/` | Concentra regras de aplicação: upload, encoding, classificação, busca |
| `backend/app/routes/` | Define as rotas FastAPI, sem lógica de negócio |
| `backend/app/schemas/` | Schemas Pydantic para validação de entrada |
| `frontend/templates/` | Templates Jinja2 renderizados pelo backend |
| `frontend/static/` | Arquivos estáticos servidos diretamente: CSS, JS |
| `uploads/` | Armazenamento físico dos arquivos enviados |
| `prompts/` | Registro dos prompts usados, com finalidade didática |
| `docs/` | Documentação: requisitos, critérios, riscos e artefatos de gestão |
| `tests/` | Testes automatizados com pytest |

### Separação backend/ e frontend/ sem projetos independentes

A separação física entre `backend/` e `frontend/` organiza responsabilidades sem criar dois projetos independentes. O FastAPI em `backend/` serve tanto as rotas da aplicação quanto os arquivos estáticos de `frontend/static/`. Os templates em `frontend/templates/` são renderizados pelo Jinja2 configurado no FastAPI.

Não há dois servidores, dois processos, dois `package.json` ou dois repositórios. É uma única aplicação Python com organização de pastas clara.

---

## 3. Organização interna do backend

### Rotas (`routes/`)

| Arquivo | Rotas principais |
|---|---|
| `content_routes.py` | Listagem, cadastro, edição, exclusão, detalhe de conteúdos |
| `upload_routes.py` | Upload de arquivo e associação com conteúdo |
| `search_routes.py` | Pesquisa textual com filtros |

As rotas devem ser finas: recebem requisição, validam entrada com schemas Pydantic e chamam serviços. Não devem conter regras de negócio ou acesso direto ao banco.

### Serviços (`services/`)

| Arquivo | Responsabilidade |
|---|---|
| `content_service.py` | Criar, editar, excluir conteúdo; atualizar índice FTS5 |
| `upload_service.py` | Orquestrar upload: validar, salvar, classificar, extrair texto |
| `encoding_service.py` | Ler arquivo com fallback: utf-8 → latin-1 → cp1252 |
| `extension_classifier.py` | Identificar linguagem e tipo de objeto pela extensão |
| `search_service.py` | Executar busca FTS5 e aplicar filtros adicionais |

### Modelos (`models/`)

Define as classes mapeadas pelo SQLAlchemy, representando tabelas do SQLite.

### Repositórios (`repositories/`)

Encapsula as operações de persistência. Serviços chamam repositórios; repositórios chamam modelos SQLAlchemy. Essa separação facilita testes e manutenção.

### Configuração (`config.py`)

Lê o arquivo `config.yaml` na inicialização e expõe os dados como objetos acessíveis pelos serviços (sistemas, domínios, linguagens, extensões aceitas, mapeamentos e tags pré-cadastradas).

---

## 4. Organização interna do frontend

### Templates Jinja2

| Template | Conteúdo |
|---|---|
| `base.html` | Layout base: cabeçalho, navegação e rodapé comuns |
| `index.html` | Página inicial com atalhos para principais funções |
| `list.html` | Listagem de conteúdos com metadados resumidos |
| `detail.html` | Detalhe do conteúdo com bloco `<pre><code>` e Highlight.js |
| `form.html` | Formulário único usado para cadastro e edição |
| `search.html` | Formulário de pesquisa e listagem de resultados |
| `upload.html` | Formulário de upload com indicação de extensões aceitas |

### Arquivos CSS

`style.css` concentra os estilos da aplicação. O objetivo é clareza e funcionalidade, não sofisticação visual. Foco em leitura confortável de conteúdo técnico, bloco de código com fonte monoespaçada e layout simples com navegação clara.

### JavaScript

`app.js` será usado apenas se necessário — botão de copiar conteúdo para a área de transferência e confirmação de exclusão via `confirm()`. Nenhum framework JavaScript deve ser adicionado.

### Highlight.js

Carregado via CDN ou localmente em `frontend/static/`. Iniciado com `hljs.highlightAll()` no final do template `detail.html`.

---

## 5. Entidades e tabelas SQLite

### Tabela `content` — Conteúdo técnico

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PK | Identificador único |
| `title` | TEXT NOT NULL | Título do conteúdo |
| `content` | TEXT | Texto do conteúdo (manual ou extraído) |
| `category` | TEXT | Categoria: snippet, sql, script, anotação, regra |
| `language` | TEXT | Linguagem: Python, SQL, PowerBuilder, etc. |
| `system` | TEXT | Sistema relacionado |
| `domain` | TEXT | Domínio funcional |
| `object_type` | TEXT | Tipo de objeto (especialmente para PowerBuilder) |
| `is_business_rule` | BOOLEAN | Indica se é regra de negócio |
| `created_at` | DATETIME | Data de criação |
| `updated_at` | DATETIME | Data de última atualização |

### Tabela `tag`

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PK | Identificador único |
| `name` | TEXT UNIQUE | Nome da tag |

### Tabela `content_tag` — Relacionamento conteúdo-tags

| Coluna | Tipo | Descrição |
|---|---|---|
| `content_id` | INTEGER FK | Referência ao conteúdo |
| `tag_id` | INTEGER FK | Referência à tag |

### Tabela `uploaded_file` — Metadados do arquivo enviado

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PK | Identificador único |
| `content_id` | INTEGER FK | Referência ao conteúdo técnico associado |
| `original_name` | TEXT | Nome original do arquivo |
| `saved_name` | TEXT | Nome usado ao salvar em `uploads/` |
| `local_path` | TEXT | Caminho relativo em `uploads/` |
| `extension` | TEXT | Extensão do arquivo |
| `file_type` | TEXT | Tipo geral (Python, SQL, PowerBuilder, etc.) |
| `object_type` | TEXT | Tipo específico de objeto PowerBuilder |
| `file_size` | INTEGER | Tamanho em bytes |
| `encoding_used` | TEXT | Encoding utilizado na leitura |
| `uploaded_at` | DATETIME | Data do upload |

### Tabela virtual `content_fts` — Índice FTS5

```sql
CREATE VIRTUAL TABLE content_fts USING fts5(
    title,
    content,
    category,
    language,
    system,
    domain,
    tags,
    content='content',
    content_rowid='id'
);
```

O índice FTS5 deve ser atualizado sempre que um conteúdo for criado, editado ou excluído, via triggers no SQLite ou manualmente no repositório.

---

## 6. Principais rotas FastAPI

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Página inicial com atalhos |
| GET | `/content` | Listagem de conteúdos |
| GET | `/content/new` | Formulário de novo conteúdo |
| POST | `/content/new` | Salvar novo conteúdo |
| GET | `/content/{id}` | Detalhe do conteúdo |
| GET | `/content/{id}/edit` | Formulário de edição |
| POST | `/content/{id}/edit` | Salvar edição |
| POST | `/content/{id}/delete` | Excluir conteúdo |
| GET | `/search` | Tela de pesquisa com formulário |
| POST | `/search` | Executar pesquisa e exibir resultados |
| GET | `/upload` | Tela de upload |
| POST | `/upload` | Processar upload de arquivo |

> Para o MVP local, o uso de `POST` para exclusão (sem AJAX) é aceitável e evita JavaScript adicional. O botão de excluir no frontend pode usar um mini-formulário com método POST.

---

## 7. Principais templates Jinja2

| Template | Herda de | Funcionalidade |
|---|---|---|
| `base.html` | — | Layout base: `<head>`, navegação, bloco `content`, rodapé, Highlight.js |
| `index.html` | `base.html` | Mensagem de boas-vindas e atalhos para as principais ações |
| `list.html` | `base.html` | Tabela com conteúdos, metadados resumidos e links para ações |
| `form.html` | `base.html` | Formulário reutilizável para cadastro e edição |
| `detail.html` | `base.html` | Título, metadados, bloco `<pre><code>` com Highlight.js, botões editar/excluir |
| `search.html` | `base.html` | Formulário de pesquisa com campo de texto e filtros; seção de resultados |
| `upload.html` | `base.html` | Formulário de upload com indicação das extensões aceitas e limite de 12 MB |

---

## 8. Decisões arquiteturais

> Para rastreabilidade completa, veja os [Architecture Decision Records](./adr/).

| Decisão | Justificativa |
|---|---|
| **FastAPI** | Framework Python moderno, com suporte a upload, validação com Pydantic, servidor Uvicorn embutido e integração direta com Jinja2 |
| **Jinja2** | Renderização server-side simples; evita a necessidade de frontend separado ou SPA |
| **SQLite** | Banco embutido, sem servidor, arquivo único; adequado para uso local e individual |
| **SQLite FTS5** | Módulo nativo do SQLite para busca textual; não exige bibliotecas externas |
| **SQLAlchemy** | ORM consolidado; organiza acesso ao banco e facilita testes com banco em memória |
| **config.yaml** | Centraliza listas e mapeamentos mutáveis sem espalhá-los pelo código |
| **pasta uploads/** | Armazenamento físico simples e local para os arquivos enviados |
| **Highlight.js** | Destaque de sintaxe via CDN ou local; sem dependência de build |
| **venv** | Isolamento do ambiente Python; evita conflito de dependências |
| **Separação backend/frontend** | Organiza responsabilidades sem criar dois projetos independentes |
| **pasta prompts/** | Registro dos prompts utilizados; finalidade didática e versionamento do raciocínio com IA |
| **pasta docs/** | Documenta requisitos, critérios, riscos e artefatos de gestão em subpastas |
| **pytest** | Framework de testes padrão no ecossistema Python; suporte a fixtures e banco em memória |

---

## 9. Riscos técnicos e mitigação

| Risco | Impacto | Mitigação |
|---|---|---|
| **Encoding de arquivos legados** | Arquivos PowerBuilder podem não estar em UTF-8 | Fallback: tentar `utf-8`, depois `latin-1`, depois `cp1252`; registrar qual encoding foi usado |
| **Limite de upload** | Arquivo maior que 12 MB pode causar lentidão ou falha silenciosa | Validar tamanho antes de processar; configurar limite no FastAPI |
| **Validação de extensões** | Usuário pode enviar arquivo com extensão não permitida | Validar extensão no backend antes de qualquer processamento |
| **Preservação de formatação** | Conteúdo técnico perde valor se indentação for perdida | Exibir sempre com `<pre><code>`; armazenar conteúdo original sem transformações |
| **Busca textual com FTS5** | Índice pode ficar desatualizado após edição ou exclusão | Atualizar entrada FTS5 sempre que o conteúdo for criado, editado ou excluído |
| **Escopo excessivo** | O projeto pode crescer além do viável | Manter a lista do que está fora do MVP e recusar incrementos fora do escopo |
| **Duplicidade de responsabilidades** | Regras de negócio podem migrar para rotas ou templates | Manter regras nos serviços; rotas apenas orquestram; templates apenas exibem |
| **Nome de arquivo duplicado** | Dois arquivos com o mesmo nome sobrescrevem um ao outro | Gerar nome único ao salvar (ex.: `{uuid}_{nome_original}`) |
| **Highlight.js com linguagem incorreta** | Destaque de sintaxe incorreto se linguagem for desconhecida | Usar detecção automática do Highlight.js como fallback |

---

## 10. O que não implementar nesta fase

| Item | Motivo |
|---|---|
| **Login e autenticação** | Aplicação local e de uso individual; adiciona complexidade sem benefício |
| **Controle de usuários** | Desnecessário no contexto local |
| **Permissões e perfis de acesso** | Não há requisito de segurança multi-usuário |
| **APIs externas** | Desvia o foco do aprendizado das fases do SDLC |
| **Frontend sofisticado** | Jinja2 com HTML/CSS simples atende ao objetivo |
| **Microsserviços** | Excesso arquitetural; a aplicação é monolítica por design |
| **Docker obrigatório** | venv é suficiente para ambiente local |
| **Infraestrutura em nuvem** | Não há requisito de publicação ou acesso remoto |
| **Backup automático** | Pode ser evolução futura; no MVP o backup é manual |
| **Versionamento interno de snippets** | Aumenta complexidade do modelo sem necessidade imediata |
| **Editor Markdown avançado** | `<pre><code>` é suficiente para o MVP |
| **Importação em lote** | Upload é de um arquivo por vez |
| **Busca semântica com embeddings** | FTS5 textual é suficiente para o MVP |
