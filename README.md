# DevNotes Local

Aplicação web local para organizar, pesquisar e reutilizar conteúdos técnicos:
snippets, SQLs, scripts, anotações, arquivos de sistemas legados e regras de negócio.

Projeto criado para fins didáticos em especialização de Engenharia de Software com
uso de Inteligência Artificial Generativa.

---

## Objetivo

Centralizar conteúdos técnicos dispersos em um repositório local simples, pesquisável
e com preservação da formatação original.

---

## Tecnologias

- Python 3.11 ou superior
- FastAPI
- SQLite + SQLite FTS5
- SQLAlchemy
- Jinja2
- HTML e CSS simples
- Highlight.js
- pytest
- Git + venv

---

## Estrutura do projeto

```
devnotes-local/
├── backend/app/          FastAPI, rotas, serviços, modelos e persistência
├── docs/                 Documentação do projeto
│   ├── arquitetura/      Arquitetura da solução e diagramas
│   │   ├── visao-geral.md
│   │   ├── diagramas.md  Todos os diagramas Mermaid (C1, C2, C3, fluxos, ER, sequência)
│   │   └── adr/          Architecture Decision Records
│   ├── criterios/        Critérios de aceitação do MVP
│   ├── features/         Feature(s) do produto (estilo Azure DevOps)
│   ├── requisitos/       RF, RNF e Regras de Negócio
│   ├── riscos/           Registro de riscos identificados
│   ├── tasks/            Tarefas técnicas (estilo Azure DevOps)
│   ├── testes/           Documentação completa de testes (SDLC)
│   │   ├── estrategia/   Pirâmide, objetivos e padrões
│   │   ├── plano/        Plano de testes formal
│   │   ├── casos/        Casos de teste por módulo
│   │   ├── rastreabilidade/ Matriz RF ↔ TC
│   │   └── relatorios/   Histórico de execuções
│   └── us/               User Stories (estilo Azure DevOps)
├── frontend/             Templates Jinja2, CSS e JavaScript simples
├── prompts/              Prompts utilizados durante o desenvolvimento (didático)
├── uploads/              Arquivos enviados pelo usuário
├── tests/                Testes automatizados com pytest
├── config.yaml           Configuração centralizada do MVP
└── requirements.txt      Dependências do projeto
```

### Documentação arquitetural

| Documento | Descrição |
|---|---|
| [docs/arquitetura/visao-geral.md](docs/arquitetura/visao-geral.md) | Visão geral, estrutura, entidades, rotas, decisões e riscos |
| [docs/arquitetura/diagramas.md](docs/arquitetura/diagramas.md) | Todos os diagramas Mermaid da solução |
| [docs/arquitetura/adr/](docs/arquitetura/adr/) | Architecture Decision Records (ADRs) |

---

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.11 ou superior
- Git
- pip, normalmente incluído na instalação do Python
- venv, normalmente incluído na instalação do Python
- Navegador web para acessar a aplicação local
- GNU Make, opcional, apenas para usar os comandos `make`

Versão validada no ambiente virtual atual do projeto: **Python 3.12.7**.

Não é necessário instalar Docker, Node.js ou PostgreSQL, pois o projeto usa FastAPI com templates Jinja2 e banco SQLite local.

---

## Execução rápida no Windows

Fluxo recomendado para um clone novo do projeto:

```powershell
# 1. Criar ambiente virtual
python -m venv venv

# 2. Instalar dependências
.\venv\Scripts\python.exe -m pip install -r requirements.txt

# 3. Rodar a suíte de testes
.\venv\Scripts\python.exe -m pytest -v

# 4. Iniciar a aplicação
.\venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --port 8000
```

Acesse: http://localhost:8000

O arquivo `requirements.txt` é a fonte principal de dependências do projeto. As versões estão fixadas para facilitar a reprodução do ambiente.

---

## Execução com ambiente ativado

```bash
# Criar ambiente virtual com Python 3.11 ou superior
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Instalar dependências
python -m pip install -r requirements.txt

# Rodar os testes
python -m pytest -v

# Iniciar a aplicação
python -m uvicorn backend.app.main:app --reload --port 8000
```

Acesse: http://localhost:8000

---

## Comandos com Makefile

O `Makefile` centraliza as tarefas comuns do projeto. Ele usa o interpretador definido em `PYTHON`; quando essa variável não é informada, usa `python`.

```powershell
# Instalar dependências
make install

# Executar testes
make test

# Iniciar o servidor em localhost:8000
make run

# Formatar código Python com Black
make format

# Remover caches e arquivos temporários
make clean

# Exibir comandos disponíveis
make help
```

No Windows, se quiser garantir o uso do ambiente virtual sem ativá-lo antes:

```powershell
make test PYTHON=.\venv\Scripts\python.exe
make run PYTHON=.\venv\Scripts\python.exe
```

---

## Como rodar os testes

Os testes usam SQLite in-memory — nenhum dado é gravado no banco real do projeto. A suíte validada possui **61 testes passando**.

```powershell
# Todos os testes
.\venv\Scripts\python.exe -m pytest -v

# Com detalhes de falha
.\venv\Scripts\python.exe -m pytest -v --tb=short

# Apenas um arquivo
.\venv\Scripts\python.exe -m pytest tests/test_routes.py -v

# Apenas um teste específico
.\venv\Scripts\python.exe -m pytest tests/test_routes.py::test_edit_content_via_route -v
```

Também é possível usar:

```powershell
make test
```

---

## Comandos de manutenção

Os comandos abaixo exigem GNU Make instalado no ambiente:

```powershell
# Formatar código Python com Black
make format

# Remover caches e arquivos temporários
make clean
```

**Suíte atual validada:** 61 testes | 7 arquivos | cobertura dos módulos de serviço, rotas HTTP e operações de exclusão.

### Arquivos locais e uploads

- A pasta `uploads/` existe no repositório por causa de `uploads/.gitkeep`.
- Arquivos enviados pelo usuário durante o uso local não devem ser versionados.
- Bancos SQLite locais, caches Python, caches pytest e ambientes virtuais são ignorados pelo `.gitignore`.

| Arquivo | Testes |
|---|---|
| `test_routes.py` | 13 |
| `test_delete.py` | 13 |
| `test_extension_classifier.py` | 12 |
| `test_upload_service.py` | 7 |
| `test_content_service.py` | 6 |
| `test_search_fts.py` | 6 |
| `test_encoding_service.py` | 4 |

### Documentação de testes

| Documento | Descrição |
|-----------|-----------|
| [docs/testes/estrategia/TE-estrategia-de-testes.md](docs/testes/estrategia/TE-estrategia-de-testes.md) | Pirâmide de testes (diagrama Mermaid), objetivos e padrões |
| [docs/testes/plano/TP-plano-de-testes.md](docs/testes/plano/TP-plano-de-testes.md) | Plano formal com critérios de entrada e saída |
| [docs/testes/casos/](docs/testes/casos/) | Casos de teste canônicos por módulo |
| [docs/testes/rastreabilidade/RTM-matriz-rastreabilidade.md](docs/testes/rastreabilidade/RTM-matriz-rastreabilidade.md) | Rastreabilidade RF ↔ TC |
| [docs/testes/relatorios/TR-relatorio-execucao.md](docs/testes/relatorios/TR-relatorio-execucao.md) | Histórico de execuções |
| [docs/testes/COMO-EXECUTAR-TESTES.md](docs/testes/COMO-EXECUTAR-TESTES.md) | Guia completo de execução |

---

## Funcionalidades do MVP

- Cadastrar conteúdos técnicos manualmente
- Editar e excluir conteúdos
- Upload simples de um arquivo por vez (até 12 MB)
- Extensões aceitas: `.py`, `.java`, `.sql`, `.md`, `.txt`, `.srw`, `.sru`, `.srd`, `.srm`, `.srf`, `.sra`, `.srs`
- Classificação automática de arquivos PowerBuilder pela extensão
- Leitura com fallback de encoding: utf-8 → latin-1 → cp1252
- Pesquisa textual com SQLite FTS5
- Filtros por categoria, linguagem, sistema, domínio, tags e regra de negócio
- Visualização com formatação preservada (`<pre><code>`)
- Destaque de sintaxe com Highlight.js

---

## Fora do escopo do MVP

- Autenticação e controle de usuários
- Publicação em produção
- Backup automático
- APIs externas
- Microsserviços ou arquitetura distribuída
- Frontend sofisticado

---

## Uso das pastas didáticas

- `prompts/` — armazena os prompts utilizados em cada fase do SDLC, permitindo
  acompanhar o raciocínio, as decisões e o refinamento das solicitações à IA.
- `docs/` — armazena toda a documentação do projeto: requisitos funcionais e não
  funcionais (`requisitos/`), regras de negócio, critérios de aceitação (`criterios/`),
  registro de riscos (`riscos/`) e artefatos de gestão simulando Azure DevOps:
  features (`features/`), user stories (`us/`) e tarefas técnicas (`tasks/`).
