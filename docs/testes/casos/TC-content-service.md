---
id: TC-CNT
tipo: Casos de Teste
modulo: content_service
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — ContentService

Arquivo de implementação: `backend/app/services/content_service.py`
Arquivo de testes: `tests/test_content_service.py`

---

## TC-CNT-01 — Criar conteúdo com campos obrigatórios e tags

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-01 |
| **Título** | Criar conteúdo com campos obrigatórios e tags |
| **Módulo** | `backend/app/services/content_service.py` |
| **Requisito** | RF-001, RF-018 |
| **Pré-condição** | Banco in-memory inicializado com fixture `db` |
| **Passos** | 1. Instanciar `ContentService(db)`. 2. Chamar `svc.create({...})` com title, content, category, language, system, domain, is_business_rule, tags |
| **Entrada** | `title="Teste de cadastro"`, `content="SELECT 1"`, `category="SQL"`, `language="SQL"`, `tags=["sql","teste"]` |
| **Resultado Esperado** | Retorna objeto `Content` com `id` não nulo e `title == "Teste de cadastro"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CNT-01 | Integração | Verificar criação de conteúdo com campos obrigatórios e tags."""`

---

## TC-CNT-02 — Listar todos os conteúdos cadastrados

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-02 |
| **Título** | Listar todos os conteúdos cadastrados |
| **Módulo** | `backend/app/services/content_service.py` |
| **Requisito** | RF-023 |
| **Pré-condição** | Banco in-memory com 2 conteúdos já criados |
| **Passos** | 1. Criar 2 conteúdos. 2. Chamar `svc.list_all()` |
| **Entrada** | Dois conteúdos com títulos distintos |
| **Resultado Esperado** | Retorna lista com exatamente 2 itens |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CNT-02 | Integração | Verificar listagem de todos os conteúdos cadastrados."""`

---

## TC-CNT-03 — Atualizar título e conteúdo de item existente

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-03 |
| **Título** | Atualizar título e conteúdo de item existente |
| **Módulo** | `backend/app/services/content_service.py` |
| **Requisito** | RF-002 |
| **Pré-condição** | Conteúdo criado com título "Original" |
| **Passos** | 1. Criar conteúdo. 2. Chamar `svc.update(item, {...})` com novo título |
| **Entrada** | `title="Atualizado"`, `content="novo texto"`, `tags=[]` |
| **Resultado Esperado** | Objeto retornado tem `title == "Atualizado"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CNT-03 | Integração | Verificar atualização de título e conteúdo via ContentService."""`

---

## TC-CNT-04 — Excluir conteúdo e confirmar ausência na listagem

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-04 |
| **Título** | Excluir conteúdo e confirmar ausência na listagem |
| **Módulo** | `backend/app/services/content_service.py` |
| **Requisito** | RF-003 |
| **Pré-condição** | Conteúdo criado no banco |
| **Passos** | 1. Criar conteúdo. 2. Chamar `svc.delete(item)`. 3. Chamar `svc.list_all()` |
| **Entrada** | Conteúdo com título "Para excluir" |
| **Resultado Esperado** | `list_all()` retorna lista vazia |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CNT-04 | Integração | Verificar exclusão de conteúdo e ausência na listagem."""`

---

## TC-CNT-05 — Marcar conteúdo como regra de negócio

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-05 |
| **Título** | Marcar conteúdo como regra de negócio |
| **Módulo** | `backend/app/services/content_service.py` |
| **Requisito** | RF-020 |
| **Pré-condição** | Banco in-memory inicializado |
| **Passos** | 1. Criar conteúdo com `is_business_rule=True` |
| **Entrada** | `title="Regra contábil"`, `is_business_rule=True`, `tags=[]` |
| **Resultado Esperado** | `item.is_business_rule is True` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Média |

**Docstring:** `"""TC-CNT-05 | Integração | Verificar flag is_business_rule=True persiste no banco."""`

---

## TC-CNT-06 — Editar conteúdo via rota POST /content/{id}/edit *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-06 |
| **Título** | Editar conteúdo via rota POST /content/{id}/edit |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-002 |
| **Pré-condição** | Conteúdo criado via `ContentService`; fixture `client` ativa |
| **Passos** | 1. Criar conteúdo com título "Original". 2. POST `/content/{id}/edit` com `title="Editado"`. 3. Seguir redirecionamento |
| **Entrada** | `title="Editado"`, `content="novo texto"`, demais campos vazios |
| **Resultado Esperado** | `status_code == 200`, "Editado" presente no HTML |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CNT-06 | Rota | Editar conteúdo via POST /content/{id}/edit."""`

---

## TC-CNT-07 — Excluir conteúdo via rota POST /content/{id}/delete *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-CNT-07 |
| **Título** | Excluir conteúdo via rota POST /content/{id}/delete |
| **Módulo** | `backend/app/routes/content_routes.py` |
| **Requisito** | RF-003 |
| **Pré-condição** | Conteúdo criado via `ContentService`; fixture `client` ativa |
| **Passos** | 1. Criar conteúdo com título "Para excluir". 2. POST `/content/{id}/delete`. 3. GET `/content` |
| **Entrada** | ID do conteúdo criado |
| **Resultado Esperado** | Redirecionamento bem-sucedido (200); "Para excluir" ausente no GET /content |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CNT-07 | Rota | Excluir conteúdo via POST /content/{id}/delete."""`

---

## TC-UPF-01 — Gravar metadados na tabela uploaded_file via attach_file *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPF-01 |
| **Título** | Gravar metadados na tabela uploaded_file via attach_file |
| **Módulo** | `backend/app/services/content_service.py` |
| **Requisito** | RF-025 |
| **Pré-condição** | Conteúdo criado via `ContentService` |
| **Passos** | 1. Criar conteúdo. 2. Chamar `svc.attach_file(item.id, file_meta)`. 3. Query em `UploadedFile` |
| **Entrada** | `file_meta` com `original_name`, `saved_name`, `local_path`, `extension`, `file_type`, `language`, `file_size=1024`, `encoding_used="utf-8"` |
| **Resultado Esperado** | Registro encontrado no banco com `original_name == "consulta.sql"`, `file_size == 1024`, `encoding_used == "utf-8"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Integração |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPF-01 | Integração | attach_file deve gravar registro na tabela uploaded_file."""`
