---
id: TR
tipo: Relatório de Execução de Testes
projeto: DevNotes Local
versao: 1.0
---

# Relatório de Execução de Testes — DevNotes Local

Preencher após cada execução de `pytest`. Adicionar nova seção ao topo a cada rodada.

---

## Modelo de Preenchimento

| Campo | Valor |
|-------|-------|
| **Data de execução** | |
| **Versão do sistema** | |
| **Branch / commit** | |
| **Comando executado** | `./venv/Scripts/pytest.exe -v --tb=short` |
| **Total de testes** | |
| **Passou** | |
| **Falhou** | |
| **Bloqueado / Skipped** | |
| **% Cobertura estimada** | |
| **Duração** | |
| **Observações** | |

---

## Execução 1 — 2026-04-30 (implementação inicial)

| Campo | Valor |
|-------|-------|
| **Data de execução** | 2026-04-30 |
| **Versão do sistema** | MVP 1.0 |
| **Branch / commit** | main |
| **Comando executado** | `./venv/Scripts/pytest.exe -v --tb=short` |
| **Total de testes** | 48 |
| **Passou** | 48 |
| **Falhou** | 0 |
| **Bloqueado / Skipped** | 0 |
| **% Cobertura estimada** | — |
| **Duração** | 0,45s |
| **Observações** | Suite expandida de 32 para 48 testes. Todos os novos testes (TC-CNT-06, TC-CNT-07, TC-UPF-01, TC-UPL-04, TC-UPL-05, TC-FTS-04, TC-FTS-05, TC-SCH-04, TC-SCH-05, TC-RND-01, TC-RND-02, TC-EXT-06, TC-CLS-10, TC-CLS-11, TC-CLS-12, TC-ENC-04) passaram na primeira execução. |

---

## Tabela de Símbolos pytest

| Símbolo | Significado |
|---------|-------------|
| `.` | Passou |
| `F` | Falhou |
| `E` | Erro (exceção inesperada) |
| `s` | Skipped |
| `x` | xfail (falha esperada) |
| `X` | xpass (passou mas era esperado falhar) |

---

## Como executar

```bash
# Básico
./venv/Scripts/pytest.exe

# Com detalhes de falhas
./venv/Scripts/pytest.exe -v --tb=short

# Apenas um módulo
./venv/Scripts/pytest.exe tests/test_routes.py -v

# Apenas um teste
./venv/Scripts/pytest.exe tests/test_routes.py::test_edit_content_via_route -v

# Com cobertura (requer pytest-cov)
./venv/Scripts/pytest.exe --cov=backend/app --cov-report=term-missing
```
