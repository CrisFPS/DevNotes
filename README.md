# DevNotes Local

Aplicação web local para organizar, pesquisar e reutilizar conteúdos técnicos:
snippets, SQLs, scripts, anotações, arquivos de sistemas legados e regras de
negócio.

O projeto foi criado para fins didáticos em uma especialização de Engenharia de
Software com uso de Inteligência Artificial Generativa. A ideia central é simples:
trocar anotações técnicas dispersas por uma base local pesquisável, pequena o
suficiente para caber em um MVP, mas estruturada o bastante para exercitar SDLC,
arquitetura, testes, documentação e manutenção evolutiva.

---

## Objetivo

Centralizar conteúdos técnicos dispersos em um repositório local simples,
pesquisável e com preservação da formatação original.

O DevNotes Local atende especialmente cenários de estudo, manutenção de sistemas
legados, consulta rápida de snippets, organização de regras de negócio e
reaproveitamento de comandos ou scripts usados no dia a dia.

---

## Funcionalidades do MVP

- Cadastrar conteúdos técnicos manualmente.
- Editar e excluir conteúdos.
- Listar conteúdos com paginação de 20 itens por página.
- Fazer upload simples de um arquivo por vez, até 12 MB.
- Aceitar as extensões `.py`, `.java`, `.sql`, `.md`, `.txt`, `.srw`, `.sru`,
  `.srd`, `.srm`, `.srf`, `.sra`, `.srs`.
- Classificar automaticamente arquivos PowerBuilder pela extensão.
- Ler arquivos com fallback de encoding: `utf-8` → `latin-1` → `cp1252`.
- Pesquisar conteúdos com SQLite FTS5.
- Filtrar por categoria, linguagem, sistema, domínio, tags e regra de negócio.
- Visualizar conteúdo com formatação preservada usando `<pre><code>`.
- Destacar sintaxe com Highlight.js.

---

## Demonstração e exemplos de uso

Depois de iniciar a aplicação, acesse:

```text
http://localhost:8000
```

Fluxo básico pelo navegador:

1. Acesse `/content/new` para cadastrar uma anotação, snippet ou regra de negócio.
2. Acesse `/upload` para importar um arquivo textual aceito pelo MVP.
3. Acesse `/search` para pesquisar por texto livre e combinar filtros.
4. Acesse `/content` para navegar pela listagem paginada.
5. Abra um conteúdo para visualizar o texto preservado com destaque de sintaxe.

Exemplos via `curl`, úteis para validação rápida das rotas HTML:

```bash
# Listar conteúdos cadastrados
curl http://localhost:8000/content

# Cadastrar conteúdo manualmente
curl -i -X POST http://localhost:8000/content/new \
  -F "title=Exemplo SQL" \
  -F "content=SELECT * FROM clientes;" \
  -F "category=SQL" \
  -F "language=SQL" \
  -F "system=Sistema Financeiro" \
  -F "domain=Financeiro" \
  -F "tags=sql, snippet"

# Pesquisar conteúdos
curl -i -X POST http://localhost:8000/search \
  -F "query=clientes" \
  -F "language=SQL"

# Fazer upload de arquivo textual
curl -i -X POST http://localhost:8000/upload \
  -F "file=@exemplo.sql" \
  -F "title=Consulta de clientes" \
  -F "category=SQL" \
  -F "tags=sql, legado"
```

Observação: o projeto não expõe uma API REST JSON pública. As rotas foram
desenhadas para uma aplicação web server-side com FastAPI e Jinja2.

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

```text
devnotes-local/
├── backend/app/          FastAPI, rotas, serviços, modelos e persistência
├── docs/                 Documentação do projeto
│   ├── arquitetura/      Arquitetura da solução, diagramas e ADRs
│   ├── criterios/        Critérios de aceitação do MVP
│   ├── features/         Feature(s) do produto
│   ├── requisitos/       RF, RNF e regras de negócio
│   ├── riscos/           Registro de riscos identificados
│   ├── tasks/            Tarefas técnicas
│   ├── testes/           Estratégia, plano, casos, rastreabilidade e relatórios
│   └── us/               User Stories
├── frontend/             Templates Jinja2, CSS e JavaScript simples
├── prompts/              Prompts utilizados durante o desenvolvimento
├── scripts/              Scripts auxiliares, como geração de massa de dados
├── uploads/              Arquivos enviados pelo usuário
├── tests/                Testes automatizados com pytest
├── config.yaml           Configuração centralizada do MVP
├── config.example.yaml   Exemplo de configuração para referência
├── Makefile              Atalhos de instalação, execução, testes e limpeza
├── pyproject.toml        Metadados do projeto e configuração de ferramentas
└── requirements.txt      Dependências fixadas do projeto
```

### Documentação arquitetural

| Documento | Descrição |
|---|---|
| [docs/arquitetura/visao-geral.md](docs/arquitetura/visao-geral.md) | Visão geral, estrutura, entidades, rotas, decisões e riscos |
| [docs/arquitetura/diagramas.md](docs/arquitetura/diagramas.md) | Diagramas Mermaid da solução |
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

Não é necessário instalar Docker, Node.js ou PostgreSQL, pois o projeto usa
FastAPI com templates Jinja2 e banco SQLite local.

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

O arquivo `requirements.txt` é a fonte principal de dependências do projeto. As
versões estão fixadas para facilitar a reprodução do ambiente.

O arquivo `config.example.yaml` documenta a estrutura esperada de configuração.
Em um clone novo, use-o como referência caso precise recriar ou adaptar o
`config.yaml`.

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

O `Makefile` centraliza as tarefas comuns do projeto. Ele usa o interpretador
definido em `PYTHON`; quando essa variável não é informada, usa `python`.

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

Os testes usam SQLite in-memory; nenhum dado é gravado no banco real do projeto.
A suíte validada possui **66 testes passando**.

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

**Suíte atual validada:** 66 testes | 7 arquivos | cobertura dos módulos de
serviço, rotas HTTP, busca FTS5, upload, encoding, classificação, exclusão e
paginação.

| Arquivo | Testes |
|---|---:|
| `test_content_service.py` | 6 |
| `test_delete.py` | 13 |
| `test_encoding_service.py` | 4 |
| `test_extension_classifier.py` | 12 |
| `test_routes.py` | 18 |
| `test_search_fts.py` | 6 |
| `test_upload_service.py` | 7 |

### Documentação de testes

| Documento | Descrição |
|-----------|-----------|
| [docs/testes/estrategia/TE-estrategia-de-testes.md](docs/testes/estrategia/TE-estrategia-de-testes.md) | Pirâmide de testes, objetivos e padrões |
| [docs/testes/plano/TP-plano-de-testes.md](docs/testes/plano/TP-plano-de-testes.md) | Plano formal com critérios de entrada e saída |
| [docs/testes/casos/](docs/testes/casos/) | Casos de teste canônicos por módulo |
| [docs/testes/rastreabilidade/RTM-matriz-rastreabilidade.md](docs/testes/rastreabilidade/RTM-matriz-rastreabilidade.md) | Rastreabilidade RF ↔ TC |
| [docs/testes/relatorios/TR-relatorio-execucao.md](docs/testes/relatorios/TR-relatorio-execucao.md) | Histórico de execuções |
| [docs/testes/COMO-EXECUTAR-TESTES.md](docs/testes/COMO-EXECUTAR-TESTES.md) | Guia completo de execução |

---

## Massa de dados opcional

Para avaliar a paginação e a visualização com maior volume de registros, existe
um script de geração de dados locais:

```powershell
.\venv\Scripts\python.exe scripts\seed_random_notes.py
```

Por padrão, o script cria 200 anotações técnicas variadas e reproduzíveis. Ele
também remove a massa anterior gerada pelo próprio script antes de inserir novos
registros, reduzindo duplicações em execuções repetidas.

---

## Arquivos locais e uploads

- A pasta `uploads/` existe no repositório por causa de `uploads/.gitkeep`.
- Arquivos enviados pelo usuário durante o uso local não devem ser versionados.
- Bancos SQLite locais, caches Python, caches pytest e ambientes virtuais são
  ignorados pelo `.gitignore`.

---

## Como a IA apoiou o desenvolvimento

O DevNotes Local foi desenvolvido com apoio de Inteligência Artificial Generativa
ao longo do ciclo de vida do projeto. A IA foi usada principalmente como parceira
de planejamento, refinamento de requisitos, desenho arquitetural, implementação
assistida, criação de testes e manutenção evolutiva.

O uso mais valioso ocorreu na organização do SDLC: os prompts registrados em
`prompts/` ajudaram a transformar uma ideia inicial em requisitos, ADRs, tarefas
técnicas, estratégia de testes e melhorias incrementais. Na arquitetura, a IA
apoiou decisões proporcionais ao porte do MVP, como manter FastAPI com Jinja2,
SQLite com FTS5, configuração centralizada em YAML e uma divisão simples entre
rotas, serviços, repositórios e templates.

Também houve ganhos na fase de qualidade. A suíte evoluiu até **66 testes
automatizados**, cobrindo serviços, rotas, upload, encoding, classificação,
busca FTS5, exclusão e paginação. A IA ajudou a identificar lacunas de teste,
documentar casos e orientar correções, enquanto a validação final permaneceu
baseada em revisão humana, execução real dos testes e conferência do histórico
do Git.

Exemplos concretos de uso da IA no projeto:

- Planejamento do MVP em escopo de 3 a 12 horas, evitando funcionalidades grandes
  demais para o objetivo didático.
- Refinamento de requisitos funcionais, não funcionais, regras de negócio,
  critérios de aceitação e riscos.
- Geração e revisão de ADRs para decisões como FastAPI + Jinja2, SQLite + FTS5,
  SQLAlchemy e `config.yaml`.
- Expansão da estratégia de testes, incluindo documentação SDLC, matriz de
  rastreabilidade e novos casos automatizados.
- Manutenção evolutiva com geração de massa de 200 registros e implementação da
  paginação na listagem.

Uma lição importante foi que a IA acelera bastante a produção de artefatos,
alternativas e código inicial, mas não substitui validação humana. O projeto
exigiu revisão de escopo, execução real dos testes, leitura dos diffs e atualização
da documentação para evitar divergências, como números de testes desatualizados.

---

## Uso das pastas didáticas

- [`prompts/`](prompts/) armazena os prompts utilizados em cada fase do SDLC, permitindo
  acompanhar o raciocínio, as decisões e o refinamento das solicitações à IA.
- [`docs/`](docs/) armazena toda a documentação do projeto: requisitos funcionais e não
  funcionais ([`requisitos/`](docs/requisitos/)), regras de negócio, critérios de aceitação
  ([`criterios/`](docs/criterios/)), registro de riscos ([`riscos/`](docs/riscos/)) e artefatos de gestão simulando
  Azure DevOps: features ([`features/`](docs/features/)), user stories ([`us/`](docs/us/)) e tarefas técnicas
  ([`tasks/`](docs/tasks/)).

---

## Limitações conhecidas

- O sistema é local e individual; não há autenticação, autorização ou múltiplos
  usuários.
- O banco é SQLite; adequado ao MVP, mas sem estratégia de migração de schema.
  Alterações estruturais podem exigir recriação manual do banco local.
- A busca FTS5 é textual e lexical; ela não faz busca semântica nem entende
  intenção do usuário.
- O upload processa um arquivo por vez e limita arquivos a 12 MB.
- A listagem paginada usa 20 itens por página, mas o espaçamento visual atual
  entre os itens pode exigir rolagem excessiva em telas menores.
- O Highlight.js é carregado via CDN, então o destaque de sintaxe pode depender
  de internet no primeiro acesso.
- Não há backup automático, exportação formal ou sincronização em nuvem.
- As rotas são voltadas para HTML server-side; o projeto não oferece uma API JSON
  estável para integração externa.

---

## Fora do escopo do MVP

- Autenticação e controle de usuários.
- Publicação em produção.
- Backup automático.
- APIs externas.
- Microsserviços ou arquitetura distribuída.
- Frontend sofisticado ou SPA.
- Busca semântica, RAG ou IA embutida no produto.

---

## Próximos passos

Evoluções coerentes com o porte do projeto:

- Adicionar capturas de tela ou um GIF curto demonstrando cadastro, upload,
  pesquisa e visualização.
- Criar exportação simples dos dados locais.
- Adicionar rotina de backup manual do banco SQLite e da pasta `uploads/`.
- Avaliar migrações com Alembic se o modelo de dados continuar evoluindo.
- Servir Highlight.js localmente para reduzir dependência de CDN.
- Melhorar a densidade visual da listagem paginada, compactando o espaçamento
  entre itens antes de alterar o tamanho padrão da página.
- Avaliar, após o ajuste visual, um seletor de quantidade de itens por página
  com opções como 10, 20 e 50.
- Melhorar busca com paginação combinada a filtros.
- Estudar busca semântica ou integração com IA em uma etapa posterior, fora do
  MVP atual.

---

## Estado para submissão

- Branch principal: `main`.
- Repositório remoto público verificado: `https://github.com/CrisFPS/DevNotes`.
- Dependências fixadas em `requirements.txt`.
- Projeto versionado como `1.0.0` em `pyproject.toml`.
- Suíte automatizada validada com `pytest`: **66 passed**.
- Documentação técnica organizada em `docs/`.
- Prompts do processo de desenvolvimento registrados em `prompts/`.

Antes da submissão final, recomenda-se criar uma tag ou release `v1.0.0` no
GitHub apontando para o commit final entregue.

---

## Licença e uso

Este projeto está publicado para fins de avaliação acadêmica e demonstração do
miniprojeto.

Nenhuma licença open source foi definida neste momento. Todos os direitos sobre
o código permanecem reservados ao autor.
