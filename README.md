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

- Python 3.11
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

## Como configurar o ambiente

```bash
# Criar ambiente virtual com Python 3.11
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

---

## Como executar

```bash
# Com o ambiente virtual ativado
uvicorn backend.app.main:app --reload --port 8000
```

Acesse: http://localhost:8000

---

## Como rodar os testes

```bash
pytest
```

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
