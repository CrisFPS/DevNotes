---
id: TC-RTE
tipo: Casos de Teste
modulo: routes
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — Rotas HTTP

Arquivos de implementação: `backend/app/routes/content_routes.py`, `upload_routes.py`, `search_routes.py`
Arquivo de testes: `tests/test_routes.py`

---

## TC-RTE-01 — GET / retorna status 200

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-01 |
| **Título** | GET / retorna status 200 |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-023 |
| **Pré-condição** | Fixture `client` ativa |
| **Passos** | 1. GET `/` |
| **Entrada** | — |
| **Resultado Esperado** | `status_code == 200` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-01 | Rota | GET / deve retornar status 200."""`

---

## TC-RTE-02 — GET /content retorna status 200

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-02 |
| **Título** | GET /content retorna status 200 |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-023 |
| **Pré-condição** | Fixture `client` ativa |
| **Passos** | 1. GET `/content` |
| **Entrada** | — |
| **Resultado Esperado** | `status_code == 200` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-02 | Rota | GET /content deve retornar status 200."""`

---

## TC-RTE-03 — GET /content/new retorna formulário 200

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-03 |
| **Título** | GET /content/new retorna formulário com status 200 |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-001 |
| **Passos** | 1. GET `/content/new` |
| **Entrada** | — |
| **Resultado Esperado** | `status_code == 200` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-03 | Rota | GET /content/new deve retornar formulário com status 200."""`

---

## TC-RTE-04 — GET /search retorna formulário 200

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-04 |
| **Título** | GET /search retorna formulário de pesquisa com status 200 |
| **Módulo** | `backend/app/routes/search_routes.py` |
| **Requisito** | RF-004 |
| **Passos** | 1. GET `/search` |
| **Entrada** | — |
| **Resultado Esperado** | `status_code == 200` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-04 | Rota | GET /search deve retornar formulário de pesquisa com status 200."""`

---

## TC-RTE-05 — GET /upload retorna formulário 200

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-05 |
| **Título** | GET /upload retorna formulário de upload com status 200 |
| **Módulo** | `backend/app/routes/upload_routes.py` |
| **Requisito** | RF-007 |
| **Passos** | 1. GET `/upload` |
| **Entrada** | — |
| **Resultado Esperado** | `status_code == 200` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-05 | Rota | GET /upload deve retornar formulário de upload com status 200."""`

---

## TC-RTE-06 — GET /content/{id} com ID inexistente retorna 404

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-06 |
| **Título** | GET /content/{id} com ID inexistente retorna 404 com mensagem amigável |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-029 |
| **Passos** | 1. GET `/content/99999` |
| **Entrada** | ID `99999` (inexistente) |
| **Resultado Esperado** | `status_code == 404`, "não encontrado" presente no HTML |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-06 | Rota | GET /content/{id} com ID inexistente deve retornar 404 amigável."""`

---

## TC-RTE-07 — POST /content/new cria conteúdo e redireciona para detalhe

| Campo | Valor |
|-------|-------|
| **ID** | TC-RTE-07 |
| **Título** | POST /content/new cria conteúdo e redireciona para detalhe |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-001, RF-024 |
| **Pré-condição** | Fixture `client` ativa |
| **Passos** | 1. POST `/content/new` com dados válidos. 2. Seguir redirecionamento |
| **Entrada** | `title="Teste via rota"`, `content="SELECT 1"`, `category="SQL"`, `language="SQL"` |
| **Resultado Esperado** | `status_code == 200`, "Teste via rota" no HTML |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-RTE-07 | Rota | POST /content/new deve criar conteúdo e redirecionar para detalhe."""`

---

## TC-RND-01 — Template detail.html renderiza bloco `<pre><code>` *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-RND-01 |
| **Título** | Template detail.html renderiza bloco `<pre><code>` |
| **Módulo** | `frontend/templates/detail.html` + rota `GET /content/{id}` |
| **Requisito** | RF-014 |
| **Pré-condição** | Conteúdo criado com campo `content` preenchido |
| **Passos** | 1. Criar conteúdo com `content="SELECT * FROM clientes"`. 2. GET `/content/{id}` |
| **Entrada** | `content="SELECT * FROM clientes"`, `language="SQL"` |
| **Resultado Esperado** | `<pre><code` presente no HTML, "SELECT * FROM clientes" visível |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Média |

**Docstring:** `"""TC-RND-01 | Rota | Template detail.html deve conter bloco <pre><code>."""`

---

## TC-RND-02 — Template detail.html exibe título do conteúdo *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-RND-02 |
| **Título** | Template detail.html exibe título do conteúdo |
| **Módulo** | `frontend/templates/detail.html` + rota `GET /content/{id}` |
| **Requisito** | RF-024 |
| **Pré-condição** | Conteúdo criado com título específico |
| **Passos** | 1. Criar conteúdo com `title="Título Único 12345"`. 2. GET `/content/{id}` |
| **Entrada** | `title="Título Único 12345"` |
| **Resultado Esperado** | `status_code == 200`, "Título Único 12345" presente no HTML |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Média |

**Docstring:** `"""TC-RND-02 | Rota | Template detail.html deve exibir o título do conteúdo."""`
