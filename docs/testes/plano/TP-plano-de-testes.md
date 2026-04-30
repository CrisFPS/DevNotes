---
id: TP
tipo: Plano de Testes
projeto: DevNotes Local
versao: 1.0
status: aprovado
---

# Plano de Testes — DevNotes Local

| Campo | Valor |
|-------|-------|
| **Projeto** | DevNotes Local |
| **Versão** | MVP 1.0 |
| **Autor** | [nome do responsável] |
| **Data** | [data de elaboração] |
| **Responsável QA** | [nome do QA] |

---

## Objetivo

Validar que as funcionalidades centrais do MVP (CRUD de conteúdo, upload de arquivos, busca FTS5, classificação e renderização) estão implementadas corretamente, são estáveis e atendem aos requisitos funcionais definidos em `docs/requisitos/RF-requisitos-funcionais.md`.

---

## Escopo

### Dentro do escopo

- CRUD de conteúdo via serviço (`ContentService`) e rotas HTTP
- Upload com validação de extensão, tamanho e encoding
- Busca FTS5 com e sem filtros
- Classificação de extensões (incluindo PowerBuilder)
- Renderização de templates HTML (detail, list, home)
- Metadados de upload (tabela `UploadedFile`)

### Fora do escopo

- Autenticação e controle de acesso
- APIs externas
- Testes de carga e performance
- Testes E2E com Selenium/Playwright
- Infraestrutura em nuvem ou produção

---

## Estratégia

Pirâmide com 4 níveis: unitários puros → integração com banco → rotas GET → rotas POST + renderização.

**Ferramentas:** pytest 8.3.3, TestClient FastAPI, AsyncMock, monkeypatch.

**Banco:** SQLite in-memory com `StaticPool`.

Ver detalhes em `docs/testes/estrategia/TE-estrategia-de-testes.md`.

---

## Critérios de Entrada

- Código-fonte disponível e instalável (`pip install -e .` ou venv ativo)
- pytest instalado e executável
- `conftest.py` com fixtures `db` e `client` funcionais
- `config.yaml` presente e válido

---

## Critérios de Saída

- 100% dos testes obrigatórios (listados abaixo) passando
- Nenhum teste com status `E` (erro inesperado)
- Cobertura estimada ≥ 80% dos módulos de serviço

---

## Ambiente

| Item | Versão |
|------|--------|
| Python | 3.12 |
| pytest | 8.3.3 |
| Banco de testes | SQLite in-memory |
| HTTP client | TestClient (FastAPI/httpx) |
| SO | Windows 10 |

---

## Riscos

| Risco | Mitigação |
|-------|-----------|
| `UPLOADS_DIR` aponta para diretório real | Usar fixture `upload_dir` com monkeypatch |
| `save_upload` é async | Testar via rota POST ou `asyncio.run` |
| FTS5 pode não ser criado se fixture não executar DDL completo | `conftest.py` cria `content_fts` explicitamente |
| Testes de encoding dependem de bytes específicos por plataforma | Usar `write_bytes` com sequências exatas |

---

## Dependências

- `fastapi`, `sqlalchemy`, `pytest`, `httpx` (TestClient)
- `config.yaml` com extensões e limites configurados
- Modelos `Content`, `Tag`, `ContentTag`, `UploadedFile` registrados

---

## Testes Mínimos Obrigatórios para o MVP

Os testes abaixo precisam passar para que o MVP seja considerado válido:

| Teste | Arquivo | RF Coberto | Motivo |
|-------|---------|------------|--------|
| `test_create_content` | test_content_service.py | RF-001 | Função central do sistema |
| `test_update_content` | test_content_service.py | RF-002 | Edição é requisito obrigatório |
| `test_delete_content` | test_content_service.py | RF-003 | Exclusão é requisito obrigatório |
| `test_search_by_text` | test_search_fts.py | RF-004 | Busca FTS5 é diferencial do MVP |
| `test_search_with_filter` | test_search_fts.py | RF-005 | Filtros são requisito obrigatório |
| `test_valid_extension_py` | test_upload_service.py | RF-009 | Validação de extensão obrigatória |
| `test_invalid_extension_raises` | test_upload_service.py | RF-009 | Rejeição de extensão obrigatória |
| `test_upload_rejects_oversized_file` | test_upload_service.py | RF-010 | Limite 12 MB é requisito obrigatório |
| `test_upload_via_route` | test_routes.py | RF-007, RF-008 | Ciclo completo de upload |
| `test_attach_file_saves_uploaded_file_record` | test_content_service.py | RF-025 | Metadados de upload obrigatórios |
| `test_read_utf8` | test_encoding_service.py | RF-011 | Leitura de arquivo obrigatória |
| `test_read_latin1` | test_encoding_service.py | RF-011 | Fallback de encoding obrigatório |
| `test_powerbuilder_window` | test_extension_classifier.py | RF-021 | Identificação de tipo PowerBuilder |
| `test_edit_content_via_route` | test_routes.py | RF-002 | Edição via interface obrigatória |
| `test_delete_content_via_route` | test_routes.py | RF-003 | Exclusão via interface obrigatória |
| `test_detail_renders_pre_code_block` | test_routes.py | RF-014 | Formatação `<pre><code>` obrigatória |
| `test_fts_updated_after_content_update` | test_search_fts.py | RF-013 | FTS deve estar sincronizado com dados |
| `test_fts_cleared_after_delete` | test_search_fts.py | RF-013 | FTS deve remover dados excluídos |
| `test_search_combined_filters` | test_search_fts.py | RF-005 | Filtros combinados obrigatórios |
| `test_detail_nonexistent_returns_404` | test_routes.py | RF-029 | Erro amigável obrigatório |

---

## Como Executar

```bash
# Execução básica
./venv/Scripts/pytest.exe

# Com detalhes de falhas
./venv/Scripts/pytest.exe -v --tb=short

# Apenas um arquivo
./venv/Scripts/pytest.exe tests/test_routes.py -v

# Apenas um teste específico
./venv/Scripts/pytest.exe tests/test_routes.py::test_edit_content_via_route -v

# Com cobertura
./venv/Scripts/pytest.exe --cov=backend/app --cov-report=term-missing
```

| Símbolo | Significado |
|---------|-------------|
| `.` | Passou |
| `F` | Falhou |
| `E` | Erro (exceção inesperada) |
| `s` | Skipped |
| `x` | xfail (falha esperada) |
