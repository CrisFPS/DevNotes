## 4. Prompt de Arquitetura/Design da Solução

Atue como arquiteto de software, especialista em aplicações web Python locais, FastAPI, SQLite, SQLAlchemy, Jinja2, documentação arquitetural e uso de Mermaid para diagramas em Markdown.

Quero que você elabore a arquitetura/design da solução para o projeto DevNotes Local.

Contexto:
O DevNotes Local será uma aplicação web local, simples e didática, usada para gerenciar snippets, SQLs, anotações técnicas, pequenos scripts, exemplos de código, arquivos exportados de sistemas legados e regras de negócio.

O objetivo não é criar uma arquitetura corporativa complexa.
O objetivo é ter um MVP local, monolítico, pequeno, organizado e adequado para aprendizado das fases do SDLC com apoio de IA.

Tecnologias obrigatórias:
- Python 3.11;
- FastAPI;
- SQLite;
- SQLAlchemy;
- SQLite FTS5;
- Jinja2;
- HTML simples;
- CSS simples;
- JavaScript simples apenas se necessário;
- Highlight.js;
- pytest;
- Git;
- ambiente virtual local com venv.

Decisão arquitetural já tomada:
A aplicação deve ter separação física entre backend e frontend, mas não deve ser tratada como dois projetos independentes.

A estrutura deve seguir a ideia:

devnotes-local/
  backend/
  frontend/
  uploads/
  prompts/
  docs/
  tests/
  config.yaml
  requirements.txt
  README.md
  .gitignore

O backend deve conter FastAPI, rotas, serviços, regras da aplicação, persistência e leitura de arquivos.
O frontend deve conter templates Jinja2, HTML, CSS e JavaScript simples.
A aplicação deve ser única, local e renderizada via Jinja2.

Funcionalidades do MVP:
- cadastrar conteúdos técnicos;
- editar conteúdos;
- excluir conteúdos;
- pesquisar conteúdos;
- colar manualmente trechos de código ou texto;
- fazer upload simples de um arquivo por vez;
- salvar arquivo localmente em uploads/;
- registrar conteúdo textual no SQLite;
- indexar conteúdo com SQLite FTS5;
- visualizar conteúdo com preservação da formatação original;
- visualizar código usando Highlight.js;
- classificar conteúdo por categoria, linguagem, tags, tipo de arquivo, sistema e domínio;
- marcar conteúdo como regra de negócio.

Upload:
- um arquivo por vez;
- limite máximo de 12 MB por arquivo;
- extensões aceitas:
  - .py
  - .java
  - .sql
  - .md
  - .txt
  - .srw
  - .sru
  - .srd
  - .srm
  - .srf
  - .sra
  - .srs

PowerBuilder:
Tratar PowerBuilder como linguagem única, mas identificar automaticamente o tipo de objeto pela extensão:
- .srw -> PowerBuilder Window
- .sru -> PowerBuilder User Object
- .srd -> PowerBuilder DataWindow
- .srm -> PowerBuilder Menu
- .srf -> PowerBuilder Function
- .sra -> PowerBuilder Application
- .srs -> PowerBuilder Structure

Encoding:
Ao ler arquivos enviados:
1. tentar utf-8;
2. se falhar, tentar latin-1;
3. se falhar, tentar cp1252.

Configuração:
Usar config.yaml para centralizar:
- sistemas;
- domínios;
- linguagens;
- extensões aceitas;
- mapeamento entre extensão e tipo de objeto;
- tags pré-cadastradas.

Escopo fora do MVP:
- autenticação;
- múltiplos usuários;
- controle de permissões;
- backup automático;
- APIs externas;
- microsserviços;
- infraestrutura em nuvem;
- frontend sofisticado;
- arquitetura distribuída;
- Docker obrigatório;
- versionamento interno avançado de snippets.

Sua tarefa:
Elabore uma proposta arquitetural simples, profissional e adequada ao MVP DevNotes Local.

A resposta deve conter:

1. Visão arquitetural geral
   - explique por que a solução será local;
   - explique por que FastAPI com Jinja2 é suficiente;
   - explique por que SQLite é adequado;
   - explique por que não é necessário microsserviço, SPA complexa, Docker obrigatório ou nuvem.

2. Estrutura inicial de pastas e arquivos
   - apresente a árvore de diretórios;
   - justifique a responsabilidade de cada diretório;
   - explique a separação backend/ e frontend/ sem tratá-los como projetos independentes;
   - explique o papel de uploads/, prompts/, docs/ e tests/.

3. Organização interna sugerida do backend
   - rotas;
   - serviços;
   - modelos;
   - repositórios ou camada de acesso a dados;
   - configuração;
   - leitura de arquivos;
   - busca textual;
   - tratamento de upload;
   - classificação por extensão.

4. Organização interna sugerida do frontend
   - templates Jinja2;
   - arquivos CSS;
   - JavaScript simples, se necessário;
   - uso de Highlight.js;
   - telas principais esperadas.

5. Proposta inicial das entidades/tabelas SQLite
   - conteúdo técnico;
   - tags;
   - relacionamento conteúdo-tags;
   - metadados de arquivo;
   - sistema;
   - domínio;
   - linguagem;
   - tipo de objeto;
   - indicação se é regra de negócio;
   - estrutura relacionada ao SQLite FTS5.

6. Proposta inicial das principais rotas FastAPI
   Inclua rotas para:
   - página inicial;
   - listagem;
   - cadastro;
   - edição;
   - exclusão;
   - detalhe;
   - pesquisa;
   - upload;
   - download ou acesso ao arquivo original, se fizer sentido no MVP.

7. Proposta inicial dos principais templates Jinja2
   Inclua templates para:
   - base/layout;
   - página inicial;
   - listagem;
   - formulário de cadastro/edição;
   - detalhe;
   - resultados da pesquisa;
   - upload.

8. Decisões arquiteturais
   Liste as principais decisões com justificativa, por exemplo:
   - uso de FastAPI;
   - uso de Jinja2;
   - uso de SQLite;
   - uso de SQLite FTS5;
   - uso de SQLAlchemy;
   - uso de config.yaml;
   - uso de uploads/ local;
   - uso de Highlight.js;
   - uso de venv;
   - separação física backend/frontend;
   - registro de prompts em prompts/;
   - registro de artefatos simulados em docs/features/, docs/us/ e docs/tasks/.

9. Riscos técnicos e mitigação
   Inclua:
   - encoding de arquivos legados;
   - limite de upload;
   - validação de extensões;
   - preservação de formatação;
   - busca textual com FTS5;
   - escopo excessivo;
   - duplicidade de responsabilidades entre camadas.

10. O que não implementar nesta fase
   Deixe claro que não devem ser tratados agora:
   - login;
   - usuários;
   - permissões;
   - APIs externas;
   - frontend sofisticado;
   - microsserviços;
   - Docker obrigatório;
   - nuvem;
   - backup automático;
   - versionamento interno avançado.

11. Diagramas arquiteturais em Markdown com Mermaid

Gere os seguintes diagramas, todos em Markdown, preferencialmente usando Mermaid.
Antes ou depois de cada diagrama, explique brevemente o objetivo do diagrama e como ele ajuda a entender a solução.

11.1. Diagrama de Contexto da Aplicação
Deve mostrar:
- usuário/desenvolvedor;
- navegador;
- DevNotes Local;
- backend FastAPI;
- banco SQLite;
- pasta uploads/;
- arquivo config.yaml.

Objetivo:
Mostrar em alto nível quem usa o sistema e quais elementos locais fazem parte do contexto da aplicação.

11.2. Diagrama de Containers ou Visão de Alto Nível
Deve mostrar:
- frontend com Jinja2, HTML, CSS e JavaScript simples;
- backend FastAPI;
- camada de serviços;
- camada de persistência com SQLAlchemy;
- banco SQLite;
- SQLite FTS5;
- uploads/;
- config.yaml.

Objetivo:
Explicar a divisão macro da solução e como as partes principais se comunicam.

11.3. Diagrama de Componentes
Deve representar:
- rotas de cadastro;
- rotas de edição;
- rotas de exclusão;
- rotas de pesquisa;
- rotas de visualização;
- rotas de upload;
- serviço de conteúdo;
- serviço de upload;
- serviço de leitura e encoding;
- serviço de classificação por extensão;
- repositório ou acesso a dados;
- modelos SQLAlchemy;
- templates Jinja2;
- Highlight.js.

Objetivo:
Mostrar as responsabilidades internas dos módulos e apoiar a futura implementação.

11.4. Diagrama de Fluxo Principal do Usuário
Deve contemplar:
- acessar a aplicação local;
- cadastrar conteúdo manualmente;
- fazer upload de arquivo;
- classificar por linguagem, sistema, domínio, tags e tipo;
- marcar como regra de negócio;
- pesquisar;
- visualizar resultado;
- copiar conteúdo preservando formatação;
- editar ou excluir conteúdo.

Objetivo:
Mostrar como o usuário navegará pelas principais funcionalidades do MVP.

11.5. Diagrama de Fluxo de Upload e Indexação
Deve representar:
- seleção do arquivo;
- validação da extensão;
- validação do tamanho máximo de 12 MB;
- tentativa de leitura com utf-8;
- fallback para latin-1;
- fallback para cp1252;
- identificação automática da linguagem e tipo de objeto pela extensão;
- salvamento do arquivo em uploads/;
- gravação dos metadados no SQLite;
- gravação do conteúdo textual;
- indexação com SQLite FTS5.

Objetivo:
Documentar uma parte crítica do MVP, principalmente por envolver PowerBuilder legado e encoding.

11.6. Diagrama Entidade-Relacionamento Simplificado
Deve considerar:
- conteúdo técnico;
- tags;
- relacionamento conteúdo-tags;
- informações do arquivo enviado;
- sistema;
- domínio;
- linguagem;
- tipo de objeto;
- indicação de regra de negócio;
- índice textual ou tabela FTS5.

Objetivo:
Apoiar a modelagem inicial do banco SQLite e orientar a implementação com SQLAlchemy.

11.7. Diagrama de Sequência Simplificado
Gere preferencialmente o diagrama de sequência do fluxo de upload.
Deve mostrar interações entre:
- usuário;
- navegador;
- rota FastAPI;
- serviço de upload;
- serviço de encoding;
- serviço de classificação;
- pasta uploads/;
- SQLite;
- SQLite FTS5.

Objetivo:
Mostrar a ordem das interações e deixar claro onde cada regra técnica é aplicada.

Formato da resposta:
- Gere tudo em Markdown.
- Use blocos Mermaid sempre que possível.
- Use títulos claros.
- Não gere código-fonte da aplicação.
- Não implemente arquivos reais.
- Não proponha tecnologias fora do escopo obrigatório.
- Justifique as decisões arquiteturais.
- Mantenha a solução simples, local, monolítica e viável para poucas horas de desenvolvimento.