---
id: TC-FTS
tipo: Casos de Teste
modulo: search_service / FTS5
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — SearchService / FTS5

Arquivo de implementação: `backend/app/services/search_service.py`
Arquivo de testes: `tests/test_search_fts.py`

---

## TC-FTS-01 — Busca por texto retorna conteúdo indexado

| Campo | Valor |
|-------|-------|
| **ID** | TC-FTS-01 |
| **Título** | Busca por texto retorna conteúdo indexado |
| **Módulo** | `backend/app/services/search_service.py` |
| **Requisito** | RF-004, RF-013 |
| **Pré-condição** | Conteúdo com "fechamento" criado via `ContentService` |
| **Passos** | 1. Criar conteúdo com título "Procedure de fechamento". 2. Chamar `search.search("fechamento", {})` |
| **Entrada** | `query="fechamento"`, `filters={}` |
| **Resultado Esperado** | `len(results) >= 1`, resultado contém "fechamento" no título ou conteúdo |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-FTS-01 | Integração | Busca por texto deve retornar conteúdo indexado no FTS5."""`

---

## TC-FTS-02 — Busca por termo inexistente retorna lista vazia

| Campo | Valor |
|-------|-------|
| **ID** | TC-FTS-02 |
| **Título** | Busca por termo inexistente retorna lista vazia |
| **Módulo** | `backend/app/services/search_service.py` |
| **Requisito** | RF-004 |
| **Pré-condição** | Banco com ao menos um conteúdo que não contém o termo |
| **Passos** | 1. Criar conteúdo genérico. 2. Chamar `search.search("termoqueNaoExiste12345", {})` |
| **Entrada** | `query="termoqueNaoExiste12345"`, `filters={}` |
| **Resultado Esperado** | `results == []` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Média |

**Docstring:** `"""TC-FTS-02 | Integração | Busca por termo inexistente deve retornar lista vazia."""`

---

## TC-FTS-03 — Filtro por linguagem retorna apenas itens correspondentes

| Campo | Valor |
|-------|-------|
| **ID** | TC-FTS-03 |
| **Título** | Filtro por linguagem retorna apenas itens correspondentes |
| **Módulo** | `backend/app/services/search_service.py` |
| **Requisito** | RF-005, RF-017 |
| **Pré-condição** | Conteúdo Python e SQL criados no banco |
| **Passos** | 1. Criar conteúdo Python. 2. Criar conteúdo SQL. 3. Chamar `search.search("", {"language": "Python"})` |
| **Entrada** | `query=""`, `filters={"language": "Python"}` |
| **Resultado Esperado** | Todos os resultados têm `language == "Python"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-FTS-03 | Integração | Filtro por linguagem deve retornar apenas itens correspondentes."""`

---

## TC-FTS-04 — FTS5 atualizado após update de conteúdo *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-FTS-04 |
| **Título** | FTS5 atualizado após update de conteúdo |
| **Módulo** | `backend/app/services/search_service.py` + `content_service.py` |
| **Requisito** | RF-013 |
| **Pré-condição** | Conteúdo com título "Título original" criado |
| **Passos** | 1. Criar conteúdo. 2. Chamar `svc.update(item, {"title": "Título modificado", ...})`. 3. Chamar `search.search("modificado", {})` |
| **Entrada** | `query="modificado"` |
| **Resultado Esperado** | Resultado contém item com "modificado" no título |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Média |

**Docstring:** `"""TC-FTS-04 | Integração | FTS5 deve refletir título atualizado após update."""`

---

## TC-FTS-05 — FTS5 limpo após delete de conteúdo *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-FTS-05 |
| **Título** | FTS5 limpo após delete de conteúdo |
| **Módulo** | `backend/app/services/search_service.py` + `content_service.py` |
| **Requisito** | RF-013 |
| **Pré-condição** | Conteúdo com título único criado |
| **Passos** | 1. Criar conteúdo com título "ItemParaDeletar99". 2. Chamar `svc.delete(item)`. 3. Chamar `search.search("ItemParaDeletar99", {})` |
| **Entrada** | `query="ItemParaDeletar99"` |
| **Resultado Esperado** | `results == []` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Média |

**Docstring:** `"""TC-FTS-05 | Integração | FTS5 não deve retornar item após delete."""`

---

## TC-SCH-04 — POST /search retorna resultado com título no HTML *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-SCH-04 |
| **Título** | POST /search retorna resultado com título do conteúdo no HTML |
| **Módulo** | `backend/app/routes/search_routes.py` |
| **Requisito** | RF-004 |
| **Pré-condição** | Conteúdo com título "Procedure contábil" criado; fixture `client` ativa |
| **Passos** | 1. Criar conteúdo. 2. POST `/search` com `query="contábil"` |
| **Entrada** | `data={"query": "contábil", "category": "", "language": "", "system": "", "domain": ""}` |
| **Resultado Esperado** | `status_code == 200`, "Procedure contábil" presente no HTML |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Média |

**Docstring:** `"""TC-SCH-04 | Rota | POST /search deve retornar HTML com título do resultado."""`

---

## TC-SCH-05 — Filtros combinados language + is_business_rule *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-SCH-05 |
| **Título** | Filtros combinados language + is_business_rule retornam apenas item correspondente |
| **Módulo** | `backend/app/services/search_service.py` |
| **Requisito** | RF-005 |
| **Pré-condição** | 3 conteúdos criados: SQL+regra, SQL+não-regra, Python+regra |
| **Passos** | 1. Criar 3 conteúdos. 2. Chamar `search.search("", {"language": "SQL", "is_business_rule": True})` |
| **Entrada** | `filters={"language": "SQL", "is_business_rule": True}` |
| **Resultado Esperado** | `len(results) == 1`, `results[0].title == "Regra SQL"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Média |

**Docstring:** `"""TC-SCH-05 | Integração | Filtros combinados devem retornar apenas itens que satisfazem todos."""`
