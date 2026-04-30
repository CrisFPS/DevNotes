# Diagnóstico e Análise da Primeira Implementação — DevNotes Local

**Data:** 2026-04-29
**Sessão:** Execução do prompt `prompts/07_Prompt_de_Implementação_Codificação.md`
**Escopo:** Verificação do estado atual da aplicação, análise de gaps em relação à arquitetura definida em `docs/arquitetura/`, correção de divergências e eliminação de débitos técnicos não-funcionais.

---

## 1. Etapa 0 — Verificação e análise de gaps

### 1.1. Componentes implementados e alinhados com a arquitetura

| Camada | Itens verificados | Status |
|---|---|---|
| Raiz do projeto | `config.yaml`, `requirements.txt`, `.gitignore`, `pytest.ini`, `README.md`, `uploads/.gitkeep`, ambiente virtual `venv/`, repositório `.git` | ✅ Implementado |
| `backend/app/` | `main.py` (entrada FastAPI), `config.py` (leitura do YAML), `database.py` (engine SQLAlchemy + `Base` + criação de tabelas + virtual table FTS5) | ✅ Implementado |
| `backend/app/models/` | `content.py` com as entidades `Content`, `Tag`, `ContentTag`, `UploadedFile` — alinhado à seção 5 da `visao-geral.md` | ✅ Implementado |
| `backend/app/schemas/` | `content_schema.py` (Pydantic `ContentForm`) | ✅ Implementado |
| `backend/app/repositories/` | `content_repository.py` cobrindo CRUD e operações FTS5 (`_index_fts`, `_update_fts`, `_delete_fts`, `search_fts`); única camada que toca o banco diretamente | ✅ Implementado |
| `backend/app/services/` | `encoding_service.py` (fallback `utf-8` → `latin-1` → `cp1252`), `extension_classifier.py`, `upload_service.py`, `content_service.py`, `search_service.py` — todos separados conforme arquitetura | ✅ Implementado |
| `backend/app/routes/` | `content_routes.py` (CRUD + detalhe), `upload_routes.py`, `search_routes.py` — cobrem todas as rotas da seção 6 da `visao-geral.md` | ✅ Implementado |
| `frontend/templates/` | `base.html`, `index.html`, `list.html`, `detail.html`, `form.html`, `search.html`, `upload.html` — todos os 7 templates listados na seção 7 | ✅ Implementado |
| `frontend/static/` | `css/style.css`, `js/app.js` | ✅ Implementado |
| `tests/` | `conftest.py` (fixtures de banco em memória + cliente HTTP) e seis arquivos de teste | ✅ Implementado |
| `docs/arquitetura/` | `visao-geral.md`, `diagramas.md` e cinco ADRs (001 a 005) | ✅ Implementado |

### 1.2. Aderência aos ADRs

| ADR | Decisão | Estado |
|---|---|---|
| ADR-001 | FastAPI + Jinja2, sem SPA | ✅ Respeitado |
| ADR-002 | SQLite + FTS5 | ✅ Respeitado (virtual table `content_fts` criada em `database.py`) |
| ADR-003 | SQLAlchemy + camada de repositórios | ✅ Respeitado (`content_repository.py` é a única camada de acesso a dados) |
| ADR-004 | Backend e frontend separados fisicamente, projeto único | ✅ Respeitado |
| ADR-005 | Configuração centralizada em `config.yaml` | ✅ Respeitado (sistemas, domínios, linguagens, extensões, mapeamentos e tags carregados via `config.py`) |

### 1.3. Divergências detectadas

#### 1.3.1. Bug funcional (corrigido nesta sessão)

A rota de detalhe (`GET /content/{content_id}`) chamava o template `404.html` quando o conteúdo não existia, mas esse template não estava presente em `frontend/templates/`. Acessar uma URL inexistente como `/content/9999` causaria erro `TemplateNotFound`. A suíte de testes existente cobria todas as rotas felizes, mas não o caminho 404, o que ocultou o problema.

#### 1.3.2. Débitos técnicos não-funcionais (corrigidos nesta sessão)

Apesar de não violarem os ADRs nem a `visao-geral.md`, três usos de APIs deprecadas geravam ruído em runtime:

- `@app.on_event("startup")` no entrypoint FastAPI.
- `datetime.utcnow()` nos modelos e no `content_service`.
- Assinatura antiga de `TemplateResponse(name, {"request": request, ...})` em todas as rotas.

---

## 2. Etapa 1 — Correções aplicadas

### 2.1. Correção do bug funcional do 404

- Criado o template `frontend/templates/404.html` estendendo `base.html`, com mensagem amigável e atalhos de retorno para a listagem e a página inicial.
- Adicionado novo teste `test_detail_nonexistent_returns_404` em `tests/test_routes.py`, garantindo que a rota responde com status 404 e renderiza a mensagem esperada quando o `content_id` não existe.

### 2.2. Eliminação dos deprecation warnings

| Mudança | Arquivos afetados |
|---|---|
| `@app.on_event("startup")` substituído por um `lifespan` (async context manager) registrado na criação do `FastAPI` | `backend/app/main.py` |
| `datetime.utcnow()` substituído por `datetime.now(UTC)`, encapsulado em um helper `_now()` para reutilização nos `default`/`onupdate` do SQLAlchemy | `backend/app/models/content.py`, `backend/app/services/content_service.py` |
| Assinatura de `TemplateResponse` migrada para `TemplateResponse(request, name, {...})` em todas as rotas | `backend/app/routes/content_routes.py`, `backend/app/routes/upload_routes.py`, `backend/app/routes/search_routes.py` |

---

## 3. Verificação final

| Verificação | Resultado |
|---|---|
| `pytest tests/` | **32 testes passando** (31 originais + 1 novo de 404) |
| `pytest -W error::DeprecationWarning` (deprecations promovidas a erro) | **32 testes passando, zero warnings** |
| Importação de `backend.app.main:app` em modo estrito (`python -W error::DeprecationWarning`) | **OK — 17 rotas registradas** |
| Comando para subir o servidor | `uvicorn backend.app.main:app --reload --port 8000` |

---

## 4. Limitações conhecidas (após esta sessão)

As limitações abaixo são intencionais para manter o escopo do MVP. Estão documentadas para orientar evoluções futuras.

1. **Sem tratamento explícito de upload concorrente.** A coleção UUID evita colisão de nome do arquivo salvo em disco, mas não há controle de lock no SQLite. Aceitável para uso pessoal/local.
2. **Sem paginação na listagem.** A rota `/content` retorna todos os registros; aceitável para o volume previsto no escopo.
3. **Sem migração de schema.** `create_tables()` apenas cria o que ainda não existe; alterações no modelo exigem dropar manualmente `backend/devnotes.db`.
4. **Highlight.js carregado via CDN.** Exige internet no primeiro acesso à página de detalhe. Decisão coerente com a simplicidade do MVP, alinhada ao ADR-001.
5. **Cobertura de testes parcial no upload.** O pipeline end-to-end (validação + classificação + persistência) não é testado de ponta a ponta; apenas `validate_extension` é testado isoladamente.
6. **Sem autenticação, sem múltiplos usuários, sem APIs externas, sem backup automático, sem Docker obrigatório.** Excluídos do MVP por decisão arquitetural — ver seção 10 da `visao-geral.md`.

---

## 5. Conclusão

A aplicação encontrava-se praticamente completa antes desta sessão: estrutura de pastas, camadas (modelos, repositórios, serviços, rotas, schemas), templates, configuração, testes e documentação arquitetural estavam todos alinhados ao prompt e aos ADRs.

A sessão atuou em dois pontos:

- Eliminou um único **bug funcional real** (template `404.html` ausente, referenciado pela rota de detalhe).
- Eliminou três classes de **deprecation warnings** (lifespan FastAPI, `datetime.utcnow`, assinatura de `TemplateResponse`), deixando o projeto compatível com as versões atuais do FastAPI/Starlette/SQLAlchemy sem qualquer ruído em runtime.

Após as correções, o projeto está em um estado verde: 32 testes passando, sem deprecation warnings, com inicialização limpa do servidor e plenamente alinhado à arquitetura formalizada em `docs/arquitetura/`.
