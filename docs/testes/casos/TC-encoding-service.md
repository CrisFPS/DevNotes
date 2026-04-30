---
id: TC-ENC
tipo: Casos de Teste
modulo: encoding_service
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — EncodingService

Arquivo de implementação: `backend/app/services/encoding_service.py`
Arquivo de testes: `tests/test_encoding_service.py`

---

## TC-ENC-01 — Ler arquivo UTF-8 e retornar conteúdo com encoding correto

| Campo | Valor |
|-------|-------|
| **ID** | TC-ENC-01 |
| **Título** | Ler arquivo UTF-8 e retornar conteúdo com encoding correto |
| **Módulo** | `backend/app/services/encoding_service.py` |
| **Requisito** | RF-011 |
| **Pré-condição** | Arquivo temporário criado com encoding UTF-8 |
| **Passos** | 1. Criar arquivo .txt com conteúdo UTF-8. 2. Chamar `read_file_content(path)` |
| **Entrada** | `"SELECT * FROM tabela WHERE campo = 'valor'"` em UTF-8 |
| **Resultado Esperado** | `content` não nulo, `"SELECT"` presente, `enc == "utf-8"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-ENC-01 | Unitário | Verificar leitura de arquivo UTF-8 com encoding correto."""`

---

## TC-ENC-02 — Fallback de encoding para latin-1

| Campo | Valor |
|-------|-------|
| **ID** | TC-ENC-02 |
| **Título** | Fallback de encoding para latin-1 |
| **Módulo** | `backend/app/services/encoding_service.py` |
| **Requisito** | RF-011 |
| **Pré-condição** | Arquivo temporário criado com encoding latin-1 |
| **Passos** | 1. Criar arquivo .txt com bytes latin-1. 2. Chamar `read_file_content(path)` |
| **Entrada** | `"Conteúdo com acentuação"` codificado em latin-1 |
| **Resultado Esperado** | `content` não nulo, `enc in ("latin-1", "utf-8")` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-ENC-02 | Unitário | Verificar fallback de encoding para latin-1."""`

---

## TC-ENC-03 — Retornar (None, None) para arquivo inexistente

| Campo | Valor |
|-------|-------|
| **ID** | TC-ENC-03 |
| **Título** | Retornar (None, None) para arquivo inexistente |
| **Módulo** | `backend/app/services/encoding_service.py` |
| **Requisito** | RF-011, RF-029 |
| **Pré-condição** | Caminho não existe no sistema de arquivos |
| **Passos** | 1. Chamar `read_file_content("/caminho/que/nao/existe.txt")` |
| **Entrada** | Caminho inválido |
| **Resultado Esperado** | Retorna `(None, None)` sem lançar exceção |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Média |

**Docstring:** `"""TC-ENC-03 | Unitário | Verificar retorno (None, None) para arquivo inexistente."""`

---

## TC-ENC-04 — Fallback de encoding para cp1252 como terceira opção *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-ENC-04 |
| **Título** | Fallback de encoding para cp1252 como terceira opção |
| **Módulo** | `backend/app/services/encoding_service.py` |
| **Requisito** | RF-011 |
| **Pré-condição** | Arquivo com byte `0x80` (válido em cp1252, inválido em utf-8 puro) |
| **Passos** | 1. Criar arquivo com `b"\x80\x99texto cp1252"`. 2. Chamar `read_file_content(f)` |
| **Entrada** | Bytes `b"\x80\x99texto cp1252"` |
| **Resultado Esperado** | `content is not None`, `enc in ("cp1252", "latin-1")` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-ENC-04 | Unitário | Fallback de encoding deve tentar cp1252 como terceira opção."""`
