# Diagramas Arquiteturais — DevNotes Local

**Versão:** 1.0
**Atualizado em:** 2026-04-29

Todos os diagramas seguem a abordagem *Diagrams as Code* usando Mermaid em Markdown.
Quando o código mudar e o diagrama não, o diagrama está errado — atualize-o junto com a implementação.

## Índice

- [11.1 Diagrama de Contexto](#111-diagrama-de-contexto)
- [11.2 Diagrama de Containers](#112-diagrama-de-containers)
- [11.3 Diagrama de Componentes](#113-diagrama-de-componentes)
- [11.4 Fluxo Principal do Usuário](#114-fluxo-principal-do-usuário)
- [11.5 Fluxo de Upload e Indexação](#115-fluxo-de-upload-e-indexação)
- [11.6 Diagrama Entidade-Relacionamento](#116-diagrama-entidade-relacionamento)
- [11.7 Diagrama de Sequência — Upload](#117-diagrama-de-sequência--upload)

---

## 11.1 Diagrama de Contexto

**O que mostra:** quem usa o sistema e quais elementos locais fazem parte do contexto.
**Pergunta respondida:** *o que existe no ambiente e como o usuário interage com o sistema?*

```mermaid
graph TD
    Usuario["Usuário / Desenvolvedor\n(máquina local)"]
    Navegador["Navegador Web\nlocalhost:8000"]
    App["DevNotes Local\n(FastAPI + Jinja2)"]
    Banco[("SQLite\ndevnotes.db")]
    Uploads["pasta uploads/\n(arquivos enviados)"]
    Config["config.yaml\n(listas e mapeamentos)"]

    Usuario -->|"Acessa via"| Navegador
    Navegador -->|"HTTP GET / POST"| App
    App -->|"Renderiza HTML"| Navegador
    App -->|"Lê e grava dados"| Banco
    App -->|"Salva arquivos físicos"| Uploads
    App -->|"Carrega configurações"| Config
```

---

## 11.2 Diagrama de Containers

**O que mostra:** a divisão macro da solução e como as partes principais se comunicam.
**Pergunta respondida:** *quais são os blocos principais e como eles se relacionam?*

```mermaid
graph TD
    subgraph DevNotesLocal["DevNotes Local — Aplicação única"]
        subgraph FE["Frontend (frontend/)"]
            Templates["Templates Jinja2\nHTML + CSS simples\nHighlight.js"]
        end

        subgraph BE["Backend (backend/)"]
            Rotas["Rotas FastAPI\n(content, upload, search)"]
            Servicos["Camada de Serviços\n(content, upload, encoding,\nclassifier, search)"]
            Repositorios["Camada de Persistência\n(SQLAlchemy + repositories)"]
        end
    end

    Banco[("SQLite\n(FTS5 incluso)")]
    Uploads["uploads/"]
    Config["config.yaml"]

    Rotas -->|"Renderiza"| Templates
    Rotas -->|"Chama"| Servicos
    Servicos -->|"Acessa dados via"| Repositorios
    Repositorios -->|"Lê e grava"| Banco
    Servicos -->|"Salva arquivos"| Uploads
    Servicos -->|"Carrega listas"| Config
```

---

## 11.3 Diagrama de Componentes

**O que mostra:** responsabilidades dos módulos internos.
**Pergunta respondida:** *quais são os componentes internos e o que cada um faz?*

```mermaid
graph TD
    subgraph Rotas["Rotas (FastAPI)"]
        CR["content_routes.py\nCadastro, edição,\nexclusão, detalhe"]
        UR["upload_routes.py\nUpload de arquivo"]
        SR["search_routes.py\nPesquisa e filtros"]
    end

    subgraph Servicos["Serviços"]
        CS["content_service.py\nRegras de conteúdo"]
        US["upload_service.py\nOrquestração de upload"]
        ES["encoding_service.py\nLeitura com fallback"]
        EX["extension_classifier.py\nClassificação por extensão"]
        SS["search_service.py\nBusca FTS5 e filtros"]
    end

    subgraph Persistencia["Persistência"]
        REP["content_repository.py\nCRUD + FTS"]
        MOD["models/content.py\nModelos SQLAlchemy"]
    end

    subgraph Frontend["Frontend (templates/)"]
        TMPL["Templates Jinja2\n(base, list, detail,\nform, search, upload)"]
        HL["Highlight.js\n(destaque de sintaxe)"]
    end

    CR --> CS
    UR --> US
    SR --> SS
    US --> ES
    US --> EX
    CS --> REP
    SS --> REP
    US --> REP
    REP --> MOD
    CR -->|"Renderiza"| TMPL
    UR -->|"Renderiza"| TMPL
    SR -->|"Renderiza"| TMPL
    TMPL --> HL
```

---

## 11.4 Fluxo Principal do Usuário

**O que mostra:** como o usuário navega pelas principais funcionalidades do MVP.
**Pergunta respondida:** *o que o usuário pode fazer e qual é o caminho percorrido?*

```mermaid
flowchart TD
    A([Usuário acessa\nlocalhost:8000]) --> B{O que fazer?}

    B --> C[Cadastrar conteúdo\nmanualmente]
    B --> D[Fazer upload\nde arquivo]
    B --> E[Pesquisar\nconteúdo]

    C --> C1[Preencher título\ne conteúdo]
    C1 --> C2[Classificar por linguagem,\nsistema, domínio, tags]
    C2 --> C3{Marcar como\nregra de negócio?}
    C3 -->|Sim| C4[Marcar flag\nis_business_rule]
    C3 -->|Não| C5[Salvar conteúdo\nno SQLite + FTS5]
    C4 --> C5
    C5 --> B

    D --> D1[Selecionar arquivo]
    D1 --> D2{Extensão\npermitida?}
    D2 -->|Não| D3[Exibir erro]
    D2 -->|Sim| D4{Tamanho\n<= 12 MB?}
    D4 -->|Não| D5[Exibir erro\nde limite]
    D4 -->|Sim| D6[Processar:\nclassificar, ler,\ngravar, indexar]
    D6 --> C5

    E --> E1[Informar texto livre\ne ou filtros]
    E1 --> E2[Buscar via FTS5\ncom filtros]
    E2 --> E3[Listar resultados]
    E3 --> E4[Selecionar item]
    E4 --> E5[Visualizar conteúdo\ncom formatação preservada]
    E5 --> E6[Highlight.js\naplicado]
    E6 --> E7{Próxima ação?}
    E7 -->|Copiar| E8[Copiar conteúdo]
    E7 -->|Editar| E9[Abrir formulário\nde edição]
    E7 -->|Excluir| E10[Confirmar\nexclusão]
    E7 -->|Voltar| B
    E8 --> B
    E9 --> C5
    E10 --> B
```

---

## 11.5 Fluxo de Upload e Indexação

**O que mostra:** o processo completo de upload com todas as regras técnicas aplicadas.
**Pergunta respondida:** *onde cada validação, leitura e gravação acontece?*

Este diagrama é crítico por envolver arquivos legados PowerBuilder e cuidados de encoding.

```mermaid
flowchart TD
    A([Usuário seleciona arquivo\ne submete formulário]) --> B{Extensão\npermitida?}

    B -->|Não| C[Retornar erro:\nExtensão não permitida]
    B -->|Sim| D{Tamanho\n<= 12 MB?}

    D -->|Não| E[Retornar erro:\nArquivo excede 12 MB]
    D -->|Sim| F[Identificar linguagem\ne tipo de objeto\npela extensão]

    F --> G[Salvar arquivo físico\nem uploads/]

    G --> H{Ler conteúdo\ncom UTF-8}
    H -->|Sucesso| K[Conteúdo\nlido com sucesso]
    H -->|Falha| I{Tentar\nlatin-1}
    I -->|Sucesso| K
    I -->|Falha| J{Tentar\ncp1252}
    J -->|Sucesso| K
    J -->|Falha| L[Registrar sem\nconteúdo textual]

    K --> M[Gravar metadados\nno SQLite:\nnome, extensão,\ntipo, encoding, tamanho]
    L --> M

    M --> N[Gravar conteúdo\ntextual no SQLite\ntabela content]

    N --> O[Indexar com\nSQLite FTS5\ntabela content_fts]

    O --> P[Upload concluído\nRedirecionar para\ndetalhe do conteúdo]
```

---

## 11.6 Diagrama Entidade-Relacionamento

**O que mostra:** entidades do banco e seus relacionamentos.
**Pergunta respondida:** *como o banco de dados está estruturado?*

```mermaid
erDiagram
    CONTENT {
        int id PK
        string title
        text content
        string category
        string language
        string system
        string domain
        string object_type
        bool is_business_rule
        datetime created_at
        datetime updated_at
    }

    TAG {
        int id PK
        string name
    }

    CONTENT_TAG {
        int content_id FK
        int tag_id FK
    }

    UPLOADED_FILE {
        int id PK
        int content_id FK
        string original_name
        string saved_name
        string local_path
        string extension
        string file_type
        string object_type
        int file_size
        string encoding_used
        datetime uploaded_at
    }

    CONTENT_FTS {
        int rowid
        string title
        text content
        string category
        string language
        string system
        string domain
        string tags
    }

    CONTENT ||--o{ CONTENT_TAG : "possui"
    TAG ||--o{ CONTENT_TAG : "associada a"
    CONTENT ||--o| UPLOADED_FILE : "pode ter"
    CONTENT ||--|| CONTENT_FTS : "indexado em"
```

> `CONTENT_FTS` é uma tabela virtual FTS5. O campo `rowid` referencia o `id` de `CONTENT`. O campo `tags` é uma representação textual das tags associadas, incluída para facilitar a busca full-text.

---

## 11.7 Diagrama de Sequência — Upload

**O que mostra:** a ordem das interações entre componentes durante um upload.
**Pergunta respondida:** *onde cada regra técnica é aplicada e em qual ordem?*

```mermaid
sequenceDiagram
    actor Usuario as Usuário
    participant Nav as Navegador
    participant Rota as upload_routes.py
    participant USvc as upload_service.py
    participant ESvc as encoding_service.py
    participant Cls as extension_classifier.py
    participant Dir as pasta uploads/
    participant DB as SQLite
    participant FTS as SQLite FTS5

    Usuario->>Nav: Seleciona arquivo e clica em enviar
    Nav->>Rota: POST /upload (multipart/form-data)

    Rota->>USvc: processar_upload(arquivo, metadados)

    USvc->>USvc: Validar extensão
    alt Extensão não permitida
        USvc-->>Rota: Erro de validação
        Rota-->>Nav: Renderizar upload.html com erro
        Nav-->>Usuario: Exibir mensagem de erro
    end

    USvc->>USvc: Validar tamanho (<= 12 MB)
    alt Arquivo muito grande
        USvc-->>Rota: Erro de tamanho
        Rota-->>Nav: Renderizar upload.html com erro
        Nav-->>Usuario: Exibir mensagem de erro
    end

    USvc->>Cls: classificar(extensão)
    Cls-->>USvc: linguagem="PowerBuilder", tipo_objeto="DataWindow"

    USvc->>Dir: Salvar arquivo com nome único
    Dir-->>USvc: caminho_local salvo

    USvc->>ESvc: ler_conteudo(caminho_local)
    ESvc->>ESvc: Tentar open(utf-8)
    alt utf-8 falhou
        ESvc->>ESvc: Tentar open(latin-1)
        alt latin-1 falhou
            ESvc->>ESvc: Tentar open(cp1252)
            alt cp1252 falhou
                ESvc-->>USvc: conteudo=None, encoding=None
            end
        end
    end
    ESvc-->>USvc: conteudo_texto, encoding_usado

    USvc->>DB: INSERT INTO content (title, content, language, object_type, ...)
    DB-->>USvc: content_id

    USvc->>DB: INSERT INTO uploaded_file (content_id, original_name, path, encoding_used, ...)
    DB-->>USvc: file_id

    USvc->>FTS: INSERT INTO content_fts (rowid, title, content, ...)
    FTS-->>USvc: indexado

    USvc-->>Rota: content_id do registro criado
    Rota-->>Nav: Redirect para GET /content/{content_id}
    Nav-->>Usuario: Exibir detalhe do conteúdo cadastrado
```
