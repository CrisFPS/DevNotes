---
id: TC-UPL
tipo: Casos de Teste
modulo: upload_service
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — UploadService

Arquivo de implementação: `backend/app/services/upload_service.py`
Arquivo de testes: `tests/test_upload_service.py`

---

## TC-UPL-01 — Aceitar extensão .py como válida

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-01 |
| **Título** | Aceitar extensão .py como válida |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-009 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `validate_extension("script.py")` |
| **Entrada** | `"script.py"` |
| **Resultado Esperado** | Retorna `".py"` sem exceção |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-01 | Unitário | Aceitar extensão .py como válida."""`

---

## TC-UPL-02 — Aceitar extensão .sql como válida

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-02 |
| **Título** | Aceitar extensão .sql como válida |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-009 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `validate_extension("consulta.sql")` |
| **Entrada** | `"consulta.sql"` |
| **Resultado Esperado** | Retorna `".sql"` sem exceção |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-02 | Unitário | Aceitar extensão .sql como válida."""`

---

## TC-UPL-03 — Aceitar extensão .srw como válida

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-03 |
| **Título** | Aceitar extensão .srw (PowerBuilder) como válida |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-009, RF-021 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `validate_extension("janela.srw")` |
| **Entrada** | `"janela.srw"` |
| **Resultado Esperado** | Retorna `".srw"` sem exceção |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-03 | Unitário | Aceitar extensão .srw (PowerBuilder) como válida."""`

---

## TC-UPL-04 — Rejeitar arquivo acima de 12 MB *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-04 |
| **Título** | Rejeitar arquivo acima de 12 MB |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-010 |
| **Pré-condição** | Fixture `upload_dir` redirecionando `UPLOADS_DIR` para `tmp_path` |
| **Passos** | 1. Criar mock com `.read` retornando 13 MB de bytes. 2. Chamar `asyncio.run(save_upload(mock_file))` |
| **Entrada** | `filename="grande.sql"`, `content=b"x" * (13 * 1024 * 1024)` |
| **Resultado Esperado** | Levanta `HTTPException` com `status_code=400`, mensagem contém "12" ou "limite" |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-04 | Unitário | Rejeitar arquivo acima de 12 MB com HTTPException 400."""`

---

## TC-UPL-05 — Upload completo via rota POST /upload *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-05 |
| **Título** | Upload completo via rota POST /upload |
| **Módulo** | `backend/app/routes/upload_routes.py` |
| **Requisito** | RF-007, RF-008, RF-025 |
| **Pré-condição** | Fixtures `client`, `db` e `upload_dir` (monkeypatch de `UPLOADS_DIR`) |
| **Passos** | 1. POST `/upload` com arquivo .sql e título. 2. Seguir redirecionamento |
| **Entrada** | `file=("teste.sql", b"SELECT 1 FROM dual", "text/plain")`, `data={"title": "Consulta via Upload"}` |
| **Resultado Esperado** | `status_code == 200`, título "Consulta via Upload" presente no HTML do detalhe |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Rota |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-05 | Rota | Upload completo via POST /upload deve criar Content e redirecionar."""`

---

## TC-UPL-ERR-01 — Rejeitar extensão .exe com HTTPException 400

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-ERR-01 |
| **Título** | Rejeitar extensão .exe com HTTPException 400 |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-009, RF-029 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `validate_extension("arquivo.exe")` |
| **Entrada** | `"arquivo.exe"` |
| **Resultado Esperado** | `HTTPException` com `status_code=400` e mensagem "não permitida" |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-ERR-01 | Unitário | Rejeitar extensão .exe com HTTPException 400."""`

---

## TC-UPL-ERR-02 — Rejeitar extensão .docx com HTTPException

| Campo | Valor |
|-------|-------|
| **ID** | TC-UPL-ERR-02 |
| **Título** | Rejeitar extensão .docx com HTTPException |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-009 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `validate_extension("documento.docx")` |
| **Entrada** | `"documento.docx"` |
| **Resultado Esperado** | Levanta `HTTPException` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-UPL-ERR-02 | Unitário | Rejeitar extensão .docx com HTTPException."""`

---

## TC-EXT-06 — Rejeitar arquivo sem extensão *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-EXT-06 |
| **Título** | Rejeitar arquivo sem extensão |
| **Módulo** | `backend/app/services/upload_service.py` |
| **Requisito** | RF-009 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `validate_extension("arquivo_sem_extensao")` |
| **Entrada** | `"arquivo_sem_extensao"` |
| **Resultado Esperado** | `HTTPException` com `status_code=400` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-EXT-06 | Unitário | Rejeitar filename sem extensão com HTTPException 400."""`
