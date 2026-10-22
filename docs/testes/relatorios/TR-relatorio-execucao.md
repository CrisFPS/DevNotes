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

## Execução 6 — 2026-10-22 (testes de integração das rotas)

| Campo | Valor |
|-------|-------|
| **Data de execução** | 2026-10-22 |
| **Versão do sistema** | v1.0.0 |
| **Branch / commit** | `main`, com os testes de integração ainda sem commit |
| **Comando executado** | `./venv/Scripts/python.exe -m pytest -q -p no:cacheprovider` |
| **Total de testes** | 134 |
| **Passou** | 134 |
| **Falhou** | 0 |
| **Bloqueado / Skipped** | 0 |
| **% Cobertura estimada** | — |
| **Duração** | 1,43s |
| **Observações** | 27 casos novos de integração das rotas HTTP: 13 em `tests/test_integracao_funcional.py` (TC-IFN-01 a TC-IFN-13) e 14 em `tests/test_integracao_estrutural.py` (TC-IES-01 a TC-IES-14). Os prompts estão em `prompts/10.01` a `prompts/10.04`. A primeira geração, com oráculos de API JSON, ficou em `docs/testes/casos/gerados/` e não entra na coleta do pytest. Antes desta rodada a suíte tinha 107 testes. |

---

## Execução 5 — 2026-10-14 (revisão de Clean Code de normalize_tags)

| Campo | Valor |
|-------|-------|
| **Data de execução** | 2026-10-14 |
| **Versão do sistema** | v1.0.0 + `normalize_tags` (módulo ainda não chamado pelas rotas) |
| **Branch / commit** | `main` em `339c1f6`, com os ajustes da revisão ainda sem commit; eles entram no commit que registra esta execução |
| **Comando executado** | `./venv/Scripts/python.exe -m pytest -q -p no:cacheprovider` |
| **Total de testes** | 107 |
| **Passou** | 107 |
| **Falhou** | 0 |
| **Bloqueado / Skipped** | 0 |
| **% Cobertura estimada** | — |
| **Duração** | 0,92s |
| **Observações** | Atividade de Clean Code do fórum 12 (C12, Unidade II). Registro completo em `prompts/09.01_R_Revisao_Clean_Code.md`, e critérios e pedidos em `prompts/09.01_Prompt_de_Clean_Code.md`. Ajustes só de legibilidade, sem mudança de comportamento: docstring de módulo apontando o cartão e as lacunas; comentários citando os itens do cartão e a ordem `strip()`→`sub()`; comentário do `\s` corrigido (29 caracteres, o mesmo conjunto de `str.strip()`/`str.isspace()`); `test_typed_form_matches_preregistered_tag` renomeado para `test_spaced_and_hyphenated_forms_become_one_tag`; ids `none`/`list`/`int` no TC-TAG-11; LAC-03 com a saída atual; **LAC-04 nova e aberta** (a lista de espaços em branco do item 4 do cartão é fechada?). Nenhum teste mudou de entrada ou de valor esperado.<br>Linha de base antes dos ajustes: 107 passed. Depois: `pytest tests/test_tag_normalizer.py` 41 passed; suíte 107 passed; `black --check` sem alteração nos 3 arquivos tocados; `ast.parse(..., feature_version=(3, 11))` ok no módulo e nos testes.<br>**Injeção de defeitos** (`scripts/injetar_defeitos_tag_normalizer.py`, com o nome do teste renomeado atualizado em `EXAMPLE_TESTS`; nenhum trecho de mutante mudou): sem defeito, 41 passed; D1 a D11 mortos (de 1 a 16 testes falhando cada); G1 a G4 sobrevivem, como na Execução 4; módulo restaurado byte a byte. |

---

## Execução 4 — 2026-10-13 (experimento normalize_tags)

| Campo | Valor |
|-------|-------|
| **Data de execução** | 2026-10-13 |
| **Versão do sistema** | v1.0.0 + `normalize_tags` (módulo novo, ainda não chamado pelas rotas) |
| **Branch / commit** | `main` em `ba7b3c3` (`v1.0.0-3-gba7b3c3`), com os arquivos do experimento ainda sem commit; eles entram no commit que registra esta execução |
| **Comando executado** | `./venv/Scripts/python.exe -m pytest -q -p no:cacheprovider` |
| **Total de testes** | 107 |
| **Passou** | 107 |
| **Falhou** | 0 |
| **Bloqueado / Skipped** | 0 |
| **% Cobertura estimada** | — |
| **Duração** | 0,69s |
| **Observações** | Experimento do fórum 12 (C12, Unidade II) com o agente Desenvolvedor: `normalize_tags` em `backend/app/services/tag_normalizer.py` e 41 testes novos em `tests/test_tag_normalizer.py`. Sem o arquivo novo (`--ignore=tests/test_tag_normalizer.py`), a linha de base é 66 passed; só o arquivo novo, 41 passed; `black --check` deixa os 4 arquivos Python novos sem alteração.<br>**Etapa 1 reproduzida (testes antes da implementação):** com o módulo renomeado para `tag_normalizer.py.etapa1`, `pytest tests/test_tag_normalizer.py` para na coleta com `ModuleNotFoundError`, sem `SyntaxError`; o nome foi restaurado em seguida.<br>**Injeção de defeitos** (`scripts/injetar_defeitos_tag_normalizer.py`): sem defeito, 41 passed. D1 a D11, que violam o cartão da tarefa, foram mortos (de 1 a 16 testes falhando cada). G1 a G4 sobreviveram, como esperado: G1 a G3 resolvem em silêncio as lacunas LAC-01 a LAC-03 e G4 remove acentos (fora do escopo), casos que o cartão não define. O módulo voltou byte a byte, com o mesmo SHA-256 antes e depois.<br>**Bug do HTTP 500** (`scripts/reproduz_bug_tags_repetidas.py`, SQLite em memória): `"SQL, sql"` responde 303 e grava duas tags (`SQL` e `sql`); `"sql, sql"` responde 500 e o segundo conteúdo fica gravado sem tags (2 ligações conteúdo-tag no total, ambas do primeiro). O bug continua porque `normalize_tags` ainda não é chamada pela rota. `backend/devnotes.db` e `uploads/` conferidos antes e depois da rodada: sem alteração. |

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
