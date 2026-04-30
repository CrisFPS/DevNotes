## 5. Prompt de Implementação/Codificação

Atue como desenvolvedor Python sênior, especialista em FastAPI, SQLite, SQLAlchemy, Jinja2, pytest e implementação incremental de MVPs locais.

Quero dar continuidade à implementação do projeto DevNotes Local.

A arquitetura da aplicação foi definida no prompt `06_Prompt_de_Arquitetura_Design_da_Solução.md` e está documentada formalmente em `docs/arquitetura/`. Toda a implementação deve estar alinhada com esses artefatos. O arquivo `prompts/06_R_Arquitetura_Design_da_Solução.md` é mantido como registro histórico da interação com a IA, mas **não é a fonte de verdade da arquitetura** — os documentos em `docs/arquitetura/` são.

---

## Documentação arquitetural de referência

Antes de implementar qualquer componente, leia os artefatos abaixo. Eles são a fonte de verdade da arquitetura e devem ser seguidos durante toda a implementação.

| Documento | O que contém |
|---|---|
| `docs/arquitetura/visao-geral.md` | Visão geral, estrutura de pastas, organização do backend e frontend, entidades SQLite, rotas, templates, decisões e riscos |
| `docs/arquitetura/diagramas.md` | 7 diagramas Mermaid: Contexto (C1), Containers (C2), Componentes (C3), Fluxo do usuário, Fluxo de upload, ER e Sequência de upload |
| `docs/arquitetura/adr/ADR-001-fastapi-jinja2.md` | Decisão: usar FastAPI + Jinja2 (sem SPA, sem frontend separado) |
| `docs/arquitetura/adr/ADR-002-sqlite-fts5.md` | Decisão: usar SQLite + FTS5 como banco de dados |
| `docs/arquitetura/adr/ADR-003-sqlalchemy-orm.md` | Decisão: usar SQLAlchemy como ORM com camada de repositórios |
| `docs/arquitetura/adr/ADR-004-separacao-backend-frontend.md` | Decisão: separação física backend/frontend sem dois projetos independentes |
| `docs/arquitetura/adr/ADR-005-config-yaml.md` | Decisão: centralizar listas e mapeamentos em config.yaml |

> Qualquer divergência detectada entre o código existente e esses documentos deve ser sinalizada e corrigida na **Etapa 0** antes de prosseguir com a implementação.

---

## Contexto do projeto

O DevNotes Local é uma aplicação web local, simples e didática para cadastrar, organizar, pesquisar e visualizar conteúdos técnicos como snippets, SQLs, anotações, scripts, arquivos legados PowerBuilder, Markdown e regras de negócio.

A aplicação será local, monolítica, sem autenticação, sem múltiplos usuários, sem nuvem, sem APIs externas e sem frontend sofisticado.

---

## Tecnologias obrigatórias

- Python 3.11;
- FastAPI;
- SQLite;
- SQLAlchemy;
- SQLite FTS5;
- Jinja2;
- HTML simples;
- CSS simples;
- JavaScript simples apenas se necessário;
- Highlight.js;
- pytest;
- Git;
- venv.

---

## Estrutura esperada do projeto

A estrutura de pastas e arquivos foi definida na arquitetura e deve ser respeitada:

```text
devnotes-local/
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
├── frontend/
│   ├── templates/
│   │   ├── base.html                  # layout base com navegação
│   │   ├── index.html                 # página inicial
│   │   ├── list.html                  # listagem de conteúdos
│   │   ├── detail.html                # detalhe com Highlight.js
│   │   ├── form.html                  # formulário de cadastro e edição
│   │   ├── search.html                # resultados da pesquisa
│   │   └── upload.html                # formulário de upload
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── app.js
├── tests/
│   ├── __init__.py
│   ├── test_content_service.py
│   ├── test_upload_service.py
│   ├── test_encoding_service.py
│   ├── test_extension_classifier.py
│   ├── test_search_fts.py
│   └── test_routes.py
├── uploads/
│   └── .gitkeep
├── docs/
│   ├── arquitetura/
│   │   ├── visao-geral.md         # visão geral, estrutura, entidades, rotas, decisões e riscos
│   │   ├── diagramas.md           # 7 diagramas Mermaid
│   │   └── adr/                   # Architecture Decision Records
│   │       ├── ADR-001-fastapi-jinja2.md
│   │       ├── ADR-002-sqlite-fts5.md
│   │       ├── ADR-003-sqlalchemy-orm.md
│   │       ├── ADR-004-separacao-backend-frontend.md
│   │       └── ADR-005-config-yaml.md
├── prompts/
├── config.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Decisão arquitetural

As decisões arquiteturais estão formalizadas nos ADRs em `docs/arquitetura/adr/`. Resumo das principais:

- Separar fisicamente `backend/` e `frontend/`, mas manter como único projeto → ver **ADR-004**
- Usar FastAPI + Jinja2 para renderização server-side (sem SPA) → ver **ADR-001**
- Usar SQLite + FTS5 como banco de dados → ver **ADR-002**
- Usar SQLAlchemy como ORM com camada de repositórios → ver **ADR-003**
- Centralizar sistemas, domínios, linguagens e mapeamentos em `config.yaml` → ver **ADR-005**
- O ponto de entrada é `backend/app/main.py`
- A configuração do SQLite e SQLAlchemy deve estar em `backend/app/database.py`
- A leitura do `config.yaml` deve estar em `backend/app/config.py`
- O acesso a dados (CRUD e FTS5) deve estar em `repositories/content_repository.py`
- O encoding de arquivos deve estar em um serviço separado: `services/encoding_service.py`

---

## Funcionalidades do MVP

- cadastrar conteúdo técnico manualmente;
- editar conteúdo;
- excluir conteúdo;
- pesquisar conteúdo;
- upload simples de um arquivo por vez;
- salvar arquivo em `uploads/`;
- validar extensões permitidas;
- validar tamanho máximo de 12 MB;
- ler conteúdo textual do arquivo;
- tentar encoding `utf-8`, depois `latin-1`, depois `cp1252`;
- classificar automaticamente linguagem e tipo de objeto pela extensão;
- registrar metadados e conteúdo textual no SQLite;
- indexar conteúdo usando SQLite FTS5;
- visualizar conteúdo com preservação da formatação usando `<pre><code>`;
- aplicar Highlight.js para destaque de sintaxe;
- classificar por categoria, linguagem, tags, tipo de arquivo, sistema e domínio;
- marcar conteúdo como regra de negócio.

---

## Extensões aceitas

- `.py`
- `.java`
- `.sql`
- `.md`
- `.txt`
- `.srw`
- `.sru`
- `.srd`
- `.srm`
- `.srf`
- `.sra`
- `.srs`

---

## Mapeamento PowerBuilder

- `.srw` → PowerBuilder Window
- `.sru` → PowerBuilder User Object
- `.srd` → PowerBuilder DataWindow
- `.srm` → PowerBuilder Menu
- `.srf` → PowerBuilder Function
- `.sra` → PowerBuilder Application
- `.srs` → PowerBuilder Structure

---

## Configuração via config.yaml

O arquivo `config.yaml` deve conter:

```yaml
sistemas:
  - Protheus
  - Sistema Atendimento
  - Sistema Financeiro
  - Sistema Telemarketing
  - Sistema Nova Reserva

dominios:
  - Contábil
  - Protheus
  - Título
  - Reserva
  - Financeiro
  - Técnico

linguagens:
  - Python
  - Java
  - SQL
  - Markdown
  - Texto comum
  - PowerBuilder

extensoes_aceitas:
  - .py
  - .java
  - .sql
  - .md
  - .txt
  - .srw
  - .sru
  - .srd
  - .srm
  - .srf
  - .sra
  - .srs

mapeamento_extensao_tipo:
  .py: Python
  .java: Java
  .sql: SQL
  .md: Markdown
  .txt: Texto comum
  .srw: PowerBuilder Window
  .sru: PowerBuilder User Object
  .srd: PowerBuilder DataWindow
  .srm: PowerBuilder Menu
  .srf: PowerBuilder Function
  .sra: PowerBuilder Application
  .srs: PowerBuilder Structure

tags_pre_cadastradas:
  - sql
  - procedure
  - powerbuilder
  - regra-negocio
  - contabilidade
  - financeiro
  - integracao
  - python
  - markdown
```

---

## Sua tarefa

### Etapa 0 — Verificação e análise de gaps (obrigatória antes de implementar)

Antes de gerar qualquer código:

1. Leia e descreva brevemente o código-fonte já existente no projeto, se houver.
2. Compare o estado atual com a estrutura esperada definida neste prompt e nos artefatos em `docs/arquitetura/` (especialmente `visao-geral.md` seções 2–3 e `diagramas.md` diagrama 11.3 de Componentes).
3. Liste o que já está implementado, o que está faltando e o que diverge da arquitetura.
4. Apresente um plano resumido do que será implementado ou corrigido nesta sessão.

Só então inicie a implementação.

---

### Etapa 1 — Implementação incremental

Conduza a implementação de forma incremental, segura e didática, seguindo esta ordem:

1. Criar fisicamente a estrutura de pastas do projeto.
2. Criar ambiente virtual com `venv`.
3. Orientar ativação do ambiente virtual no Windows.
4. Criar `requirements.txt` com todas as dependências.
5. Instalar as dependências com `pip install -r requirements.txt`.
6. Iniciar o Git com `git init`, se ainda não estiver iniciado.
7. Criar `.gitignore` adequado para Python, venv e SQLite.
8. Criar `config.yaml` com o conteúdo definido acima.
9. Criar `backend/app/config.py` — leitura do `config.yaml`.
10. Criar `backend/app/database.py` — configuração do SQLite e SQLAlchemy (engine, session, Base).
11. Criar `backend/app/main.py` — ponto de entrada do FastAPI, configuração do Jinja2 e arquivos estáticos.
12. Criar `backend/app/models/content.py` — modelos SQLAlchemy (tabela principal e FTS5 virtual table).
13. Criar `backend/app/schemas/content_schema.py` — schemas Pydantic para validação de entrada e saída.
14. Criar `backend/app/repositories/content_repository.py` — acesso a dados (CRUD e busca FTS5).
15. Criar `backend/app/services/encoding_service.py` — leitura de arquivos com fallback `utf-8` → `latin-1` → `cp1252`.
16. Criar `backend/app/services/extension_classifier.py` — classificação de linguagem e tipo de objeto pela extensão.
17. Criar `backend/app/services/upload_service.py` — orquestração do upload: validação, leitura, classificação e persistência.
18. Criar `backend/app/services/content_service.py` — regras de negócio para cadastro, edição e exclusão de conteúdo.
19. Criar `backend/app/services/search_service.py` — busca textual com FTS5 e filtros combinados.
20. Criar `backend/app/routes/content_routes.py` — rotas de cadastro, edição, exclusão e detalhe.
21. Criar `backend/app/routes/upload_routes.py` — rota de upload de arquivo.
22. Criar `backend/app/routes/search_routes.py` — rota de pesquisa e filtros.
23. Criar templates Jinja2 básicos em `frontend/templates/`: `base.html`, `index.html`, `list.html`, `detail.html`, `form.html`, `search.html`, `upload.html`.
24. Criar `frontend/static/css/style.css` e `frontend/static/js/app.js` simples.
25. Integrar Highlight.js no template `detail.html` via CDN.
26. Criar testes iniciais com pytest em `tests/`.
27. Atualizar `README.md` com instruções de execução local e execução dos testes.

---

## Regras de implementação

- Priorize simplicidade e clareza didática.
- Não implemente autenticação.
- Não implemente múltiplos usuários.
- Não implemente APIs externas.
- Não implemente backup automático.
- Não implemente frontend sofisticado.
- Não use arquitetura distribuída.
- Não transforme `backend/` e `frontend/` em projetos independentes.
- Não adicione Docker como obrigatório.
- Não crie dependências desnecessárias.
- Não use frameworks frontend pesados.
- Evite abstrações excessivas — o código deve ser claro, organizado e didático.
- O `encoding_service.py` deve ser um serviço independente, não misturado ao `upload_service.py`.
- O `content_repository.py` deve ser a única camada que acessa o banco diretamente.
- O `database.py` deve centralizar a criação do engine, da sessão e do Base do SQLAlchemy.
- O `config.py` deve ser responsável exclusivamente pela leitura e exposição do `config.yaml`.

---

## Formato da resposta

- Use Markdown.
- Inicie com a **Etapa 0** (verificação e análise de gaps).
- Mostre a árvore de pastas resultante.
- Para cada arquivo criado ou modificado, informe o caminho completo e o conteúdo completo e funcional.
- Separe bem cada etapa com títulos claros.
- Explique brevemente as decisões mais importantes.
- Ao final, informe como executar a aplicação localmente.
- Ao final, informe como rodar os testes.
- Ao final, liste limitações conhecidas da versão gerada.

---

## Importante

- Implemente de forma incremental.
- Se a resposta ficar grande, priorize uma primeira versão mínima funcional, deixando melhorias para etapas seguintes.
- Em caso de divergência entre o código existente e a arquitetura estabelecida, sinalize e corrija, justificando brevemente a decisão.
- Não altere o escopo funcional do MVP.
- Não proponha tecnologias fora do conjunto obrigatório.
