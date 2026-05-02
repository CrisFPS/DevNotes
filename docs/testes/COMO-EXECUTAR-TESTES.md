---
id: HOW-TO-TESTS
tipo: Guia de Execução
projeto: DevNotes Local
versao: 1.0
---

# Como Executar os Testes — DevNotes Local

## Pré-requisitos

Antes de executar os testes, verifique que:

- O projeto está clonado e a pasta raiz é `DevNotes/`
- O ambiente virtual (`venv`) foi criado e as dependências instaladas
- O arquivo `config.yaml` está presente na raiz do projeto

Se ainda não criou o ambiente virtual:

```bash
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## Estrutura dos Testes

```
tests/
├── conftest.py                  # Fixtures compartilhadas (db, client, upload_dir, etc.)
├── test_content_service.py      # CRUD via ContentService + attach_file
├── test_encoding_service.py     # Leitura de arquivos com fallback de encoding
├── test_extension_classifier.py # Classificação de extensões (Python, SQL, PowerBuilder)
├── test_routes.py               # Rotas GET e POST via TestClient
├── test_search_fts.py           # Busca FTS5 e filtros via SearchService
└── test_upload_service.py       # Validação de extensão e tamanho de upload
```

---

## Executando os Testes

### Todos os testes de uma vez

```bash
.\venv\Scripts\python.exe -m pytest
```

### Com saída detalhada (recomendado)

```bash
.\venv\Scripts\python.exe -m pytest -v
```

### Com detalhes de falhas

```bash
.\venv\Scripts\python.exe -m pytest -v --tb=short
```

---

## Executando por Arquivo

```bash
# Testes do ContentService (CRUD + attach_file)
.\venv\Scripts\python.exe -m pytest tests/test_content_service.py -v

# Testes de encoding (utf-8, latin-1, cp1252)
.\venv\Scripts\python.exe -m pytest tests/test_encoding_service.py -v

# Testes de classificação de extensões
.\venv\Scripts\python.exe -m pytest tests/test_extension_classifier.py -v

# Testes de rotas HTTP (GET e POST)
.\venv\Scripts\python.exe -m pytest tests/test_routes.py -v

# Testes de busca FTS5 e filtros
.\venv\Scripts\python.exe -m pytest tests/test_search_fts.py -v

# Testes de upload (extensão e tamanho)
.\venv\Scripts\python.exe -m pytest tests/test_upload_service.py -v
```

---

## Executando um Teste Específico

```bash
.\venv\Scripts\python.exe -m pytest tests/test_routes.py::test_edit_content_via_route -v
.\venv\Scripts\python.exe -m pytest tests/test_content_service.py::test_attach_file_saves_uploaded_file_record -v
.\venv\Scripts\python.exe -m pytest tests/test_search_fts.py::test_fts_updated_after_content_update -v
```

---

## Executando por Grupo (usando `-k`)

A flag `-k` filtra testes pelo nome. Exemplos:

```bash
# Todos os testes de PowerBuilder
.\venv\Scripts\python.exe -m pytest -k "powerbuilder" -v

# Todos os testes de rota POST
.\venv\Scripts\python.exe -m pytest -k "route" -v

# Todos os testes de encoding
.\venv\Scripts\python.exe -m pytest -k "encoding or enc" -v

# Testes obrigatórios de upload
.\venv\Scripts\python.exe -m pytest -k "upload" -v
```

---

## Medindo a Cobertura de Código

Requer o pacote `pytest-cov`. Para instalar:

```bash
.\venv\Scripts\python.exe -m pip install pytest-cov
```

Executar com relatório no terminal:

```bash
.\venv\Scripts\python.exe -m pytest --cov=backend/app --cov-report=term-missing
```

Gerar relatório HTML (abre em `htmlcov/index.html`):

```bash
.\venv\Scripts\python.exe -m pytest --cov=backend/app --cov-report=html
start htmlcov/index.html
```

---

## Interpretando o Resultado

### Símbolos na saída do pytest

| Símbolo | Significado |
|---------|-------------|
| `.` | Passou |
| `F` | Falhou — asserção não satisfeita |
| `E` | Erro — exceção inesperada durante o teste |
| `s` | Skipped — ignorado (marcado com `@pytest.mark.skip`) |
| `x` | xfail — falhou como esperado |
| `X` | xpass — passou mas era esperado falhar |

### Exemplo de saída bem-sucedida

```
============================= test session starts =============================
collected 61 items

tests/test_content_service.py::test_create_content PASSED
tests/test_content_service.py::test_list_content PASSED
...
============================== 61 passed in 0.59s =============================
```

### Exemplo de falha

```
FAILED tests/test_routes.py::test_edit_content_via_route - AssertionError: ...
```

Quando ocorrer falha, execute com `--tb=long` para ver o traceback completo:

```bash
.\venv\Scripts\python.exe -m pytest -v --tb=long
```

---

## Testes Obrigatórios para o MVP

Os testes abaixo precisam passar para o MVP ser considerado válido. Execute-os isoladamente para verificação rápida:

```bash
.\venv\Scripts\python.exe -m pytest -v -k "test_create_content or test_update_content or test_delete_content or test_search_by_text or test_search_with_filter or test_valid_extension_py or test_invalid_extension_raises or test_upload_rejects_oversized_file or test_upload_via_route or test_attach_file_saves_uploaded_file_record or test_read_utf8 or test_read_latin1 or test_powerbuilder_window or test_edit_content_via_route or test_delete_content_via_route or test_detail_renders_pre_code_block or test_fts_updated_after_content_update or test_fts_cleared_after_delete or test_search_combined_filters or test_detail_nonexistent_returns_404"
```

---

## Observações Importantes

**Banco de dados:**
Os testes usam SQLite in-memory com `StaticPool`. Nenhum dado é gravado no banco real do projeto. Cada teste parte de um estado limpo.

**UPLOADS_DIR:**
Testes que envolvem upload (`test_upload_via_route`, `test_upload_rejects_oversized_file`) usam a fixture `upload_dir`, que redireciona o diretório de uploads para uma pasta temporária. Nenhum arquivo é gravado na pasta `uploads/` real.

**Funções async:**
`save_upload` é `async`. Os testes que a chamam diretamente usam `asyncio.run()`. Os testes via rota usam `TestClient`, que lida com o contexto async automaticamente.

---

## Documentação Relacionada

| Documento | Caminho |
|-----------|---------|
| Estratégia de testes | `docs/testes/estrategia/TE-estrategia-de-testes.md` |
| Plano de testes | `docs/testes/plano/TP-plano-de-testes.md` |
| Casos de teste | `docs/testes/casos/` |
| Matriz de rastreabilidade | `docs/testes/rastreabilidade/RTM-matriz-rastreabilidade.md` |
| Relatório de execução | `docs/testes/relatorios/TR-relatorio-execucao.md` |
