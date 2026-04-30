# 08 — Prompt de Testes (v2)

Atue como especialista em testes de software, qualidade, pytest, FastAPI, SQLite, SQLAlchemy e documentação de testes segundo padrões de Engenharia de Software e SDLC.

---

## Contexto do Projeto

O **DevNotes Local** é uma aplicação web local, didática, criada com Python 3.11, FastAPI, SQLite, SQLAlchemy, SQLite FTS5, Jinja2, HTML/CSS simples, Highlight.js e pytest.

O sistema permite cadastrar, editar, excluir, pesquisar e visualizar conteúdos técnicos, além de fazer upload simples de arquivos para armazenamento local e indexação textual.

---

## Estrutura de Pacotes Reais do Projeto

```
backend/
└── app/
    ├── main.py                          # FastAPI app (instância `app`)
    ├── config.py                        # Carrega config.yaml
    ├── database.py                      # Base, get_db, SessionLocal
    ├── models/
    │   └── content.py                   # Content, Tag, ContentTag, UploadedFile
    ├── repositories/
    │   └── content_repository.py        # ContentRepository
    ├── services/
    │   ├── content_service.py           # ContentService
    │   ├── upload_service.py            # validate_extension, save_upload (async)
    │   ├── encoding_service.py          # read_file_content
    │   ├── extension_classifier.py      # classify
    │   └── search_service.py            # SearchService
    ├── routes/
    │   ├── content_routes.py
    │   ├── upload_routes.py
    │   └── search_routes.py
    └── schemas/
        └── content_schema.py            # ContentForm (Pydantic)

frontend/
└── templates/
    ├── base.html, index.html, list.html
    ├── detail.html                      # Usa <pre><code> + Highlight.js
    ├── form.html, upload.html, search.html, 404.html

tests/
    ├── conftest.py                      # Fixtures db e client — JÁ IMPLEMENTADAS
    ├── test_content_service.py          # 5 testes existentes — EXPANDIR
    ├── test_encoding_service.py         # 3 testes existentes — EXPANDIR
    ├── test_extension_classifier.py     # 9 testes existentes — EXPANDIR
    ├── test_upload_service.py           # 5 testes existentes — EXPANDIR
    ├── test_search_fts.py               # 3 testes existentes — EXPANDIR
    └── test_routes.py                   # 7 testes existentes — EXPANDIR
```

---

## Assinaturas Reais das Funções Principais

```python
# upload_service.py
UPLOADS_DIR: Path  # variável de módulo — pode ser sobrescrita com monkeypatch
MAX_SIZE_BYTES: int  # config upload.tamanho_maximo_mb * 1024 * 1024 (padrão: 12 MB)

def validate_extension(filename: str) -> str:
    """Retorna a extensão (ex: '.py'). Lança HTTPException(400) se não permitida."""

async def save_upload(file: UploadFile) -> dict:
    """Valida extensão, lê bytes, verifica tamanho (12 MB), salva em UPLOADS_DIR,
    classifica, lê conteúdo com fallback de encoding. Lança HTTPException(400).
    Retorna: original_name, saved_name, local_path, extension, file_type,
             object_type, language, file_size, encoding_used, text_content."""

# encoding_service.py
def read_file_content(path: str | Path) -> tuple[str | None, str | None]:
    """Tenta ler em utf-8, latin-1, cp1252. Retorna (conteudo, encoding) ou (None, None)."""

# extension_classifier.py
def classify(extension: str) -> dict:
    """Retorna {"language": str, "object_type": str}."""

# content_service.py (ContentService)
def create(self, data: dict) -> Content:
    """data deve conter: title, content, category, language, system, domain,
    is_business_rule, tags (list[str])."""
def update(self, content: Content, data: dict) -> Content: ...
def delete(self, content: Content) -> None: ...
def list_all(self) -> list[Content]: ...
def get(self, content_id: int) -> Content | None: ...
def attach_file(self, content_id: int, file_meta: dict) -> None:
    """Grava registro em UploadedFile linkado ao content_id."""

# search_service.py (SearchService)
def search(self, query: str, filters: dict) -> list[Content]:
    """filters aceita: category, language, system, domain, is_business_rule."""
```

---

## Rotas Implementadas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Home — últimos 5 conteúdos |
| GET | `/content` | Lista todos os conteúdos |
| GET | `/content/new` | Formulário de criação |
| POST | `/content/new` | Cria conteúdo → redireciona para `/content/{id}` |
| GET | `/content/{id}` | Detalhe (404 se não existe) |
| GET | `/content/{id}/edit` | Formulário de edição |
| POST | `/content/{id}/edit` | Atualiza → redireciona para `/content/{id}` |
| POST | `/content/{id}/delete` | Exclui → redireciona para `/content` |
| GET | `/upload` | Formulário de upload |
| POST | `/upload` | Processa upload → redireciona para `/content/{id}` |
| GET | `/search` | Formulário de pesquisa |
| POST | `/search` | Executa pesquisa → retorna resultados na mesma página |

---

## Extensões Aceitas

`.py`, `.java`, `.sql`, `.md`, `.txt`, `.srw`, `.sru`, `.srd`, `.srm`, `.srf`, `.sra`, `.srs`

**Mapeamento PowerBuilder:**

| Extensão | Tipo de Objeto |
|----------|----------------|
| `.srw` | PowerBuilder Window |
| `.sru` | PowerBuilder User Object |
| `.srd` | PowerBuilder DataWindow |
| `.srm` | PowerBuilder Menu |
| `.srf` | PowerBuilder Function |
| `.sra` | PowerBuilder Application |
| `.srs` | PowerBuilder Structure |

---

## Escopo Fora dos Testes Neste Momento

- Autenticação, múltiplos usuários, permissões
- APIs externas
- Testes de carga
- Testes E2E completos com Selenium ou Playwright (podem ser citados como evolução futura)
- Testes em produção ou em infraestrutura em nuvem

---

## Sua Tarefa

Sua resposta deve cobrir **quatro blocos principais**:

1. Estratégia e documentação formal de testes (padrão SDLC)
2. Documentação retroativa dos 32 testes já implementados
3. Casos de teste para as lacunas identificadas (novos testes a implementar)
4. Implementação dos novos testes com exemplos pytest

---

## BLOCO 1 — Estratégia e Documentação Formal (padrão SDLC)

### 1.1 Objetivo dos Testes

Explique o que os testes devem garantir neste MVP. Inclua objetivos específicos para:

- Integridade do ciclo CRUD (criar, editar, excluir via serviço e via rota)
- Ciclo completo de upload (validar extensão → validar tamanho → salvar → classificar → ler encoding → criar Content → attach UploadedFile)
- FTS5 consultável após create, update e delete
- Cobertura das rotas POST (não apenas GET)
- Renderização correta de `<pre><code>` na tela de detalhe

### 1.2 Pirâmide de Testes Simplificada

Descreva os quatro níveis com exemplos dos módulos reais:

- **Unitários puros** (sem banco, sem fixture `db`): `validate_extension`, `classify`, `read_file_content`
- **Integração com banco** (fixture `db`): `ContentService`, `SearchService`, `attach_file`, FTS5 após operações
- **Rotas GET** (fixture `client`, verificação de status HTTP): formulários, listagens, 404
- **Rotas POST** (fixture `client`, verificação de comportamento e HTML): criação, edição, exclusão, upload, pesquisa
- **Renderização** (fixture `client`, verificação de conteúdo HTML específico): `<pre><code>`, título no detalhe, mensagens de erro

Inclua uma nota sobre `save_upload` ser `async` e como testá-la: via `asyncio.run()` com `AsyncMock`, ou preferencialmente via rota POST `/upload` com `TestClient`.

### 1.3 Modelo de Plano de Testes (Test Plan)

Gere um modelo de documento de Plano de Testes com as seguintes seções:

```
Projeto:          DevNotes Local
Versão:           MVP 1.0
Autor:            [nome]
Data:             [data]
Responsável QA:   [nome]

Objetivo:         [descrever]
Escopo:           [o que está dentro e fora]
Estratégia:       [pirâmide, ferramentas, abordagem]
Critérios de entrada:  [pré-requisitos para iniciar os testes]
Critérios de saída:    [condições para considerar os testes concluídos]
Ambiente:         Python 3.11, pytest 8.3.3, SQLite in-memory, TestClient FastAPI
Riscos:           [listar riscos identificados]
Dependências:     [listar dependências]
```

### 1.4 Modelo Canônico de Caso de Teste

Defina o padrão de documentação de cada caso de teste. Cada TC deve conter:

| Campo | Descrição |
|-------|-----------|
| **ID** | Identificador único: `TC-<MÓDULO>-<NN>` (ex: TC-CNT-01) |
| **Título** | Nome curto e descritivo |
| **Módulo** | Arquivo/serviço testado |
| **Requisito** | RF rastreado (ex: RF-001) |
| **Pré-condição** | Estado necessário antes do teste |
| **Passos** | Sequência de ações |
| **Entrada** | Dados fornecidos |
| **Resultado Esperado** | O que deve ocorrer |
| **Resultado Obtido** | Preenchido após execução |
| **Status** | Passou / Falhou / Bloqueado |
| **Tipo** | Unitário / Integração / Rota |
| **Prioridade** | Alta / Média / Baixa |

### 1.5 Padrão de Docstring para Funções de Teste

Todo `def test_*` deve conter docstring no seguinte formato:

```python
def test_create_content(db):
    """TC-CNT-01 | Integração | Verificar criação de conteúdo com campos obrigatórios."""
```

### 1.6 Modelo de Relatório de Execução (Test Report)

Gere um modelo de tabela para ser preenchido após cada execução de `pytest`:

| Campo | Valor |
|-------|-------|
| Data de execução | |
| Versão do sistema | |
| Comando executado | `pytest -v --tb=short` |
| Total de testes | |
| Passou | |
| Falhou | |
| Bloqueado | |
| % Cobertura estimada | |
| Observações | |

### 1.7 Critérios de Aceite dos Testes

Alinhe os critérios de aceite dos testes com os critérios do MVP em `docs/criterios/CA-criterios-aceitacao-mvp.md`. Liste quais critérios de aceite são validados por testes automatizados e quais dependem de verificação manual.

---

## BLOCO 2 — Documentação Retroativa dos 32 Testes Já Implementados

Antes de gerar os casos de teste, leia o arquivo `docs/requisitos/RF-requisitos-funcionais.md` para obter os IDs e descrições corretos dos requisitos.

Os testes a seguir **já existem** no projeto. Sua tarefa é:

1. Gerar a **tabela de casos de teste completa** para cada um, com todos os campos canônicos preenchidos
2. Gerar as **docstrings** para adicionar em cada função de teste
3. Identificar o RF rastreado para cada teste

### Testes existentes a documentar:

**`tests/test_content_service.py`** (5 testes)
- `test_create_content`
- `test_list_content`
- `test_update_content`
- `test_delete_content`
- `test_business_rule_flag`

**`tests/test_encoding_service.py`** (3 testes)
- `test_read_utf8`
- `test_read_latin1`
- `test_read_nonexistent_returns_none`

**`tests/test_extension_classifier.py`** (9 testes)
- `test_python_classification`
- `test_sql_classification`
- `test_powerbuilder_window`
- `test_powerbuilder_datawindow`
- `test_powerbuilder_menu`
- `test_powerbuilder_function`
- `test_unknown_extension`
- `test_markdown`
- `test_java`

**`tests/test_upload_service.py`** (5 testes)
- `test_valid_extension_py`
- `test_valid_extension_sql`
- `test_valid_extension_srw`
- `test_invalid_extension_raises`
- `test_invalid_extension_docx`

**`tests/test_search_fts.py`** (3 testes)
- `test_search_by_text`
- `test_search_no_results`
- `test_search_with_filter`

**`tests/test_routes.py`** (7 testes)
- `test_home_returns_200`
- `test_list_returns_200`
- `test_new_form_returns_200`
- `test_search_form_returns_200`
- `test_upload_form_returns_200`
- `test_detail_nonexistent_returns_404`
- `test_create_and_view`

Ao final deste bloco, gere a **Matriz de Rastreabilidade parcial** dos TCs já existentes:

| Requisito | Descrição (resumida) | Casos de Teste cobertos |
|-----------|----------------------|------------------------|
| RF-001 | ... | TC-CNT-01, TC-CNT-02, ... |
| ... | ... | ... |

Identifique também quais RFs **ainda não têm nenhum TC** cobrindo-os.

---

## BLOCO 3 — Novos Casos de Teste (Lacunas Identificadas)

Gere os casos de teste completos (tabela canônica) para as seguintes lacunas identificadas. Estes testes **ainda não foram implementados**:

### Grupo UPL — Upload

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-UPL-04 | Rejeitar arquivo acima de 12 MB | RF-010 | Unitário | Alta |
| TC-UPL-05 | Upload completo via rota POST /upload | RF-007, RF-008, RF-025 | Rota | Alta |

### Grupo CNT — Conteúdo via Rota

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-CNT-06 | Editar conteúdo via rota POST /content/{id}/edit | RF-002 | Rota | Alta |
| TC-CNT-07 | Excluir conteúdo via rota POST /content/{id}/delete | RF-003 | Rota | Alta |

### Grupo UPF — Metadados de Upload

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-UPF-01 | Gravar metadados na tabela uploaded_file via attach_file | RF-025 | Integração | Alta |

### Grupo FTS — Indexação FTS5

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-FTS-04 | FTS5 atualizado após update de conteúdo | RF-013 | Integração | Média |
| TC-FTS-05 | FTS5 limpo após delete de conteúdo | RF-013 | Integração | Média |

### Grupo RND — Renderização

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-RND-01 | Template detail.html renderiza bloco `<pre><code>` | RF-014 | Rota | Média |
| TC-RND-02 | Template detail.html exibe título do conteúdo | RF-024 | Rota | Média |

### Grupo SCH — Pesquisa

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-SCH-04 | Pesquisa via rota POST /search retorna resultado no HTML | RF-004 | Rota | Média |
| TC-SCH-05 | Filtros combinados (language + is_business_rule) | RF-005 | Integração | Média |

### Grupo EXT — Extensão

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-EXT-06 | Rejeitar arquivo sem extensão | RF-009 | Unitário | Baixa |

### Grupo CLS — Classificação PowerBuilder (extensões ausentes)

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-CLS-10 | Classificar .sru como PowerBuilder User Object | RF-021 | Unitário | Baixa |
| TC-CLS-11 | Classificar .sra como PowerBuilder Application | RF-021 | Unitário | Baixa |
| TC-CLS-12 | Classificar .srs como PowerBuilder Structure | RF-021 | Unitário | Baixa |

### Grupo ENC — Encoding (extensão)

| ID | Título | RF | Tipo | Prioridade |
|----|--------|----|------|------------|
| TC-ENC-04 | Fallback de encoding para cp1252 como terceira opção | RF-011 | Unitário | Baixa |

Para cada novo TC, preencha a tabela canônica completa (todos os campos da seção 1.4).

Ao final, gere a **Matriz de Rastreabilidade completa** — existentes + novos:

| Requisito | Descrição (resumida) | TCs existentes | TCs novos | Cobertura |
|-----------|----------------------|----------------|-----------|-----------|
| RF-001 | Cadastrar conteúdo | TC-CNT-01, TC-CNT-02 | — | Parcial |
| ... | ... | ... | ... | ... |

---

## BLOCO 4 — Implementação dos Novos Testes

### 4.1 Fixtures a Adicionar no conftest.py

O `conftest.py` já contém as fixtures `db` e `client`. **Não as recrie.** Adicione apenas as seguintes:

```python
import pytest
from unittest.mock import AsyncMock, MagicMock

# Fixture: arquivo .txt temporário
@pytest.fixture
def txt_file(tmp_path):
    """TC-ENC-01 | Arquivo .txt UTF-8 para testes de encoding."""
    f = tmp_path / "nota.txt"
    f.write_text("Conteúdo simples em texto", encoding="utf-8")
    return f

# Fixture: arquivo .sql temporário
@pytest.fixture
def sql_file(tmp_path):
    """Arquivo .sql UTF-8 para testes de upload e extensão."""
    f = tmp_path / "consulta.sql"
    f.write_text("SELECT id, nome FROM cliente WHERE ativo = 1", encoding="utf-8")
    return f

# Fixture: arquivo .srw temporário
@pytest.fixture
def srw_file(tmp_path):
    """Arquivo .srw para testes de classificação PowerBuilder."""
    f = tmp_path / "w_principal.srw"
    f.write_text("$PBExportHeader$w_principal.srw", encoding="utf-8")
    return f

# Fixture: arquivo com encoding latin-1
@pytest.fixture
def latin1_file(tmp_path):
    """Arquivo com encoding latin-1 para testes de fallback."""
    f = tmp_path / "legado.txt"
    f.write_bytes("Conteúdo com acentuação em latin-1".encode("latin-1"))
    return f

# Fixture: arquivo com extensão inválida
@pytest.fixture
def invalid_ext_file(tmp_path):
    """Arquivo .xlsx para testar rejeição de extensão inválida."""
    f = tmp_path / "planilha.xlsx"
    f.write_bytes(b"conteudo qualquer")
    return f

# Fixture: conteúdo acima do limite de 12 MB
@pytest.fixture
def oversized_content():
    """Bytes que excedem 12 MB para testar validação de tamanho."""
    return b"x" * (13 * 1024 * 1024)

# Helper: cria um UploadFile mock compatível com save_upload (async)
def make_upload_file(filename: str, content: bytes) -> MagicMock:
    """Cria um UploadFile mock com .filename e .read() async."""
    mock = MagicMock()
    mock.filename = filename
    mock.read = AsyncMock(return_value=content)
    return mock

# Fixture: monkeypatch de UPLOADS_DIR para evitar arquivos reais
@pytest.fixture
def upload_dir(tmp_path, monkeypatch):
    """Redireciona UPLOADS_DIR para diretório temporário durante o teste."""
    import backend.app.services.upload_service as us
    monkeypatch.setattr(us, "UPLOADS_DIR", tmp_path)
    return tmp_path
```

### 4.2 Exemplos de Implementação dos Novos Testes

Implemente os testes abaixo nos arquivos indicados. Cada função deve conter a docstring no padrão `"""TC-xxx | Tipo | Objetivo."""`.

---

**`tests/test_upload_service.py`** — adicionar:

```python
import asyncio
from unittest.mock import AsyncMock, MagicMock
import pytest
from fastapi import HTTPException
from backend.app.services.upload_service import save_upload

def test_upload_rejects_oversized_file(oversized_content, upload_dir):
    """TC-UPL-04 | Unitário | Rejeitar arquivo acima de 12 MB com HTTPException 400."""
    mock_file = make_upload_file("grande.sql", oversized_content)
    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(save_upload(mock_file))
    assert exc_info.value.status_code == 400
    assert "12" in exc_info.value.detail or "limite" in exc_info.value.detail.lower()

def test_validate_extension_no_ext():
    """TC-EXT-06 | Unitário | Rejeitar filename sem extensão com HTTPException 400."""
    from backend.app.services.upload_service import validate_extension
    with pytest.raises(HTTPException) as exc_info:
        validate_extension("arquivo_sem_extensao")
    assert exc_info.value.status_code == 400
```

---

**`tests/test_routes.py`** — adicionar:

```python
from backend.app.services.content_service import ContentService

def test_edit_content_via_route(client, db):
    """TC-CNT-06 | Rota | Editar conteúdo via POST /content/{id}/edit."""
    svc = ContentService(db)
    item = svc.create({"title": "Original", "content": "texto", "tags": []})
    response = client.post(f"/content/{item.id}/edit", data={
        "title": "Editado",
        "content": "novo texto",
        "category": "",
        "language": "",
        "system": "",
        "domain": "",
        "tags": "",
        "is_business_rule": "",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Editado" in response.text

def test_delete_content_via_route(client, db):
    """TC-CNT-07 | Rota | Excluir conteúdo via POST /content/{id}/delete."""
    svc = ContentService(db)
    item = svc.create({"title": "Para excluir", "content": "...", "tags": []})
    item_id = item.id
    response = client.post(f"/content/{item_id}/delete", follow_redirects=True)
    assert response.status_code == 200
    list_response = client.get("/content")
    assert "Para excluir" not in list_response.text

def test_detail_renders_pre_code_block(client, db):
    """TC-RND-01 | Rota | Template detail.html deve conter bloco <pre><code>."""
    svc = ContentService(db)
    item = svc.create({
        "title": "Código SQL",
        "content": "SELECT * FROM clientes",
        "language": "SQL",
        "tags": [],
    })
    response = client.get(f"/content/{item.id}")
    assert response.status_code == 200
    assert "<pre><code" in response.text
    assert "SELECT * FROM clientes" in response.text

def test_detail_renders_title(client, db):
    """TC-RND-02 | Rota | Template detail.html deve exibir o título do conteúdo."""
    svc = ContentService(db)
    item = svc.create({"title": "Título Único 12345", "content": "...", "tags": []})
    response = client.get(f"/content/{item.id}")
    assert response.status_code == 200
    assert "Título Único 12345" in response.text

def test_search_route_returns_results(client, db):
    """TC-SCH-04 | Rota | POST /search deve retornar HTML com título do resultado."""
    svc = ContentService(db)
    svc.create({"title": "Procedure contábil", "content": "EXEC sp_contabil", "tags": []})
    response = client.post("/search", data={
        "query": "contábil",
        "category": "",
        "language": "",
        "system": "",
        "domain": "",
    })
    assert response.status_code == 200
    assert "Procedure contábil" in response.text

def test_upload_via_route(client, upload_dir):
    """TC-UPL-05 | Rota | Upload completo via POST /upload deve criar Content e redirecionar."""
    sql_content = b"SELECT 1 FROM dual"
    response = client.post(
        "/upload",
        data={"title": "Consulta via Upload"},
        files={"file": ("teste.sql", sql_content, "text/plain")},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Consulta via Upload" in response.text
```

---

**`tests/test_content_service.py`** — adicionar:

```python
from backend.app.models.content import UploadedFile

def test_attach_file_saves_uploaded_file_record(db):
    """TC-UPF-01 | Integração | attach_file deve gravar registro na tabela uploaded_file."""
    svc = ContentService(db)
    item = svc.create({"title": "Com arquivo", "content": "SELECT 1", "tags": []})
    file_meta = {
        "original_name": "consulta.sql",
        "saved_name": "abc123.sql",
        "local_path": "/uploads/abc123.sql",
        "extension": ".sql",
        "file_type": "SQL",
        "object_type": "SQL",
        "language": "SQL",
        "file_size": 1024,
        "encoding_used": "utf-8",
    }
    svc.attach_file(item.id, file_meta)
    record = db.query(UploadedFile).filter(UploadedFile.content_id == item.id).first()
    assert record is not None
    assert record.original_name == "consulta.sql"
    assert record.file_size == 1024
    assert record.encoding_used == "utf-8"
```

---

**`tests/test_search_fts.py`** — adicionar:

```python
def test_fts_updated_after_content_update(db):
    """TC-FTS-04 | Integração | FTS5 deve refletir título atualizado após update."""
    svc = ContentService(db)
    item = svc.create({"title": "Título original", "content": "base", "tags": []})
    svc.update(item, {"title": "Título modificado", "content": "atualizado", "tags": []})
    search = SearchService(db)
    results = search.search("modificado", {})
    assert any("modificado" in r.title.lower() for r in results)

def test_fts_cleared_after_delete(db):
    """TC-FTS-05 | Integração | FTS5 não deve retornar item após delete."""
    svc = ContentService(db)
    item = svc.create({"title": "ItemParaDeletar99", "content": "...", "tags": []})
    svc.delete(item)
    search = SearchService(db)
    results = search.search("ItemParaDeletar99", {})
    assert results == []

def test_search_combined_filters(db):
    """TC-SCH-05 | Integração | Filtros combinados devem retornar apenas itens que satisfazem todos."""
    svc = ContentService(db)
    svc.create({"title": "Regra SQL", "content": "...", "language": "SQL", "is_business_rule": True, "tags": []})
    svc.create({"title": "Script SQL", "content": "...", "language": "SQL", "is_business_rule": False, "tags": []})
    svc.create({"title": "Regra Python", "content": "...", "language": "Python", "is_business_rule": True, "tags": []})
    search = SearchService(db)
    results = search.search("", {"language": "SQL", "is_business_rule": True})
    assert len(results) == 1
    assert results[0].title == "Regra SQL"
```

---

**`tests/test_extension_classifier.py`** — adicionar:

```python
def test_powerbuilder_user_object():
    """TC-CLS-10 | Unitário | .sru deve classificar como PowerBuilder User Object."""
    result = classify(".sru")
    assert result["language"] == "PowerBuilder"
    assert result["object_type"] == "PowerBuilder User Object"

def test_powerbuilder_application():
    """TC-CLS-11 | Unitário | .sra deve classificar como PowerBuilder Application."""
    result = classify(".sra")
    assert result["object_type"] == "PowerBuilder Application"

def test_powerbuilder_structure():
    """TC-CLS-12 | Unitário | .srs deve classificar como PowerBuilder Structure."""
    result = classify(".srs")
    assert result["object_type"] == "PowerBuilder Structure"
```

---

**`tests/test_encoding_service.py`** — adicionar:

```python
def test_read_cp1252(tmp_path):
    """TC-ENC-04 | Unitário | Fallback de encoding deve tentar cp1252 como terceira opção."""
    f = tmp_path / "cp1252.txt"
    # Caractere 0x80 é válido em cp1252 (€) mas inválido em utf-8 e latin-1 puro
    f.write_bytes(b"\x80\x99texto cp1252")
    content, enc = read_file_content(f)
    assert content is not None
    assert enc in ("cp1252", "latin-1")
```

---

### 4.3 Testes Mínimos Obrigatórios para Considerar o MVP Aceitável

Os testes abaixo **precisam passar** para que o MVP seja considerado válido. Apresente como tabela:

| Teste | Arquivo | RF Coberto | Motivo de ser obrigatório |
|-------|---------|-----------|--------------------------|
| `test_create_content` | test_content_service.py | RF-001 | Função central do sistema |
| `test_update_content` | test_content_service.py | RF-002 | Edição é requisito obrigatório |
| `test_delete_content` | test_content_service.py | RF-003 | Exclusão é requisito obrigatório |
| `test_search_by_text` | test_search_fts.py | RF-004 | Busca FTS5 é diferencial do MVP |
| `test_search_with_filter` | test_search_fts.py | RF-005 | Filtros são requisito obrigatório |
| `test_valid_extension_py` | test_upload_service.py | RF-009 | Validação de extensão obrigatória |
| `test_invalid_extension_raises` | test_upload_service.py | RF-009 | Rejeição de extensão obrigatória |
| **`test_upload_rejects_oversized_file`** | test_upload_service.py | RF-010 | Limite 12 MB é requisito obrigatório |
| **`test_upload_via_route`** | test_routes.py | RF-007, RF-008 | Ciclo completo de upload |
| **`test_attach_file_saves_uploaded_file_record`** | test_content_service.py | RF-025 | Metadados de upload obrigatórios |
| `test_read_utf8` | test_encoding_service.py | RF-011 | Leitura de arquivo obrigatória |
| `test_read_latin1` | test_encoding_service.py | RF-011 | Fallback de encoding obrigatório |
| `test_powerbuilder_window` | test_extension_classifier.py | RF-021 | Identificação de tipo PowerBuilder |
| **`test_edit_content_via_route`** | test_routes.py | RF-002 | Edição via interface obrigatória |
| **`test_delete_content_via_route`** | test_routes.py | RF-003 | Exclusão via interface obrigatória |
| **`test_detail_renders_pre_code_block`** | test_routes.py | RF-014 | Formatação `<pre><code>` obrigatória |
| **`test_fts_updated_after_content_update`** | test_search_fts.py | RF-013 | FTS deve estar sincronizado com dados |
| **`test_fts_cleared_after_delete`** | test_search_fts.py | RF-013 | FTS deve remover dados excluídos |
| **`test_search_combined_filters`** | test_search_fts.py | RF-005 | Filtros combinados obrigatórios |
| `test_detail_nonexistent_returns_404` | test_routes.py | RF-029 | Erro amigável obrigatório |

> Testes em **negrito** são novos — precisam ser implementados antes da primeira execução completa do suite.

---

### 4.4 Como Executar os Testes

```bash
# Execução básica
pytest

# Com detalhes de falhas
pytest -v --tb=short

# Apenas um arquivo
pytest tests/test_routes.py -v

# Apenas um teste específico
pytest tests/test_routes.py::test_edit_content_via_route -v
```

**Interpretação dos resultados:**

| Símbolo | Significado |
|---------|-------------|
| `.` | Passou |
| `F` | Falhou |
| `E` | Erro (exceção inesperada) |
| `s` | Skipped |
| `x` | xfail (falha esperada) |

**Atenção — UPLOADS_DIR:**
O `upload_service.py` usa `UPLOADS_DIR` como variável de módulo apontando para `uploads/` real do projeto. Testes que chamam `save_upload` diretamente (fora de rota) devem usar a fixture `upload_dir` para redirecionar via monkeypatch e evitar arquivos reais no diretório do projeto.

**Atenção — funções async:**
`save_upload` é uma corrotina (`async def`). Para testá-la fora de contexto async, use `asyncio.run(save_upload(mock))`. Alternativamente, teste via rota `POST /upload` com `TestClient` — abordagem mais simples e recomendada para o MVP.

---

### 4.5 Recomendações de Manutenção

1. **Monkeypatch de UPLOADS_DIR** — sempre use a fixture `upload_dir` em testes que invocam `save_upload` diretamente para isolar o sistema de arquivos real.

2. **Separação de fixtures** — testes de serviço usam apenas `db`; testes de rota usam `client` (que depende de `db`). Isso facilita diagnóstico: se um teste de serviço falha, o problema está no serviço, não na camada HTTP.

3. **StaticPool** — o conftest usa `StaticPool` para que todas as conexões SQLAlchemy compartilhem o mesmo banco em memória. Isso é necessário para o override de `get_db` funcionar corretamente no `TestClient`. Não altere sem entender esse comportamento.

4. **Novos requisitos** — ao adicionar uma funcionalidade, siga o fluxo:
   - Registre o RF em `docs/requisitos/RF-requisitos-funcionais.md`
   - Crie o TC na tabela de casos de teste com todos os campos
   - Implemente o teste com docstring padronizada
   - Atualize a Matriz de Rastreabilidade
   - Atualize o Relatório de Execução

5. **Testes E2E (evolução futura)** — quando o MVP evoluir para ambiente compartilhado, considere adicionar testes E2E com Playwright ou Selenium para fluxos críticos (upload + visualização, busca + filtro).

6. **Cobertura** — para medir cobertura, instale `pytest-cov` e execute:
   ```bash
   pytest --cov=backend/app --cov-report=term-missing
   ```

---

## Regras para o LLM

- Use Markdown. Use tabelas onde ajudar à compreensão.
- Documente cada caso de teste com todos os campos canônicos.
- Gere docstrings para todos os testes (existentes e novos).
- Leia `docs/requisitos/RF-requisitos-funcionais.md` antes de montar a Matriz de Rastreabilidade.
- Os exemplos de código devem usar os imports e assinaturas reais descritos neste prompt — não invente módulos.
- O `conftest.py` já contém `db` e `client` — não as recrie.
- Priorize testes úteis para o MVP; não proponha ferramentas complexas demais.
- Não altere o escopo funcional do MVP.
- Mantenha os testes compatíveis com projeto local e pequeno.
