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

## Execução 3 — 2026-05-02 (implementação da paginação)

| Campo | Valor |
|-------|-------|
| **Data de execução** | 2026-05-02 |
| **Versão do sistema** | MVP 1.0 - TASK-023 concluída |
| **Branch / commit** | main |
| **Comando executado** | `./venv/Scripts/python.exe -m pytest -q -p no:cacheprovider` |
| **Total de testes** | 66 |
| **Passou** | 66 |
| **Falhou** | 0 |
| **Bloqueado / Skipped** | 0 |
| **% Cobertura estimada** | — |
| **Duração** | 0,72s |
| **Observações** | Execução completa feita fora do sandbox para permitir acesso ao diretório temporário do Windows usado por fixtures de upload. Inclui os novos testes TC-RTE-08 a TC-RTE-12 da paginação. |

---

## Execução 2 — 2026-05-02 (documentação da paginação)

| Campo | Valor |
|-------|-------|
| **Data de execução** | 2026-05-02 |
| **Versão do sistema** | MVP 1.0 - manutenção evolutiva planejada |
| **Branch / commit** | main |
| **Comando executado** | Validação documental por inspeção e `rg "TASK-023|TC-RTE-08|TC-RTE-09|TC-RTE-10|TC-RTE-11|TC-RTE-12|RF-023" docs` |
| **Total de testes** | Não executado nesta etapa |
| **Passou** | Não aplicável |
| **Falhou** | Não aplicável |
| **Bloqueado / Skipped** | Não aplicável |
| **% Cobertura estimada** | — |
| **Duração** | — |
| **Observações** | Rodada documental da TASK-023. A execução automatizada de pytest fica para a etapa de implementação da paginação e dos testes planejados. |

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
