# Prompt Refinado do Levantamento e Análise de Requisitos

Atue como especialista em Engenharia de Requisitos, Análise de Negócio, Engenharia de Software e documentação de itens no estilo Azure DevOps.

Quero realizar o levantamento e a análise profissional dos requisitos do projeto DevNotes Local.

Contexto do projeto:
O DevNotes Local será uma aplicação web local, simples e didática, destinada a organizar, armazenar, pesquisar e reutilizar conteúdos técnicos usados em estudos ou no trabalho de desenvolvimento de software.

O sistema será usado localmente, sem publicação em produção, com foco em aprendizado das fases do SDLC com apoio de Inteligência Artificial Generativa.

Problema a resolver:
Desenvolvedores acumulam comandos SQL, trechos de código, exemplos de procedures, anotações sobre regras de negócio, scripts, comandos de terminal, arquivos exportados de sistemas legados e observações técnicas em locais dispersos. Isso dificulta encontrar, reutilizar e manter esse conhecimento técnico.

Objetivo do MVP:
Criar uma aplicação web local para centralizar esses conteúdos, permitir cadastro manual, upload simples de arquivos, classificação, busca textual e visualização preservando a formatação original.

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

Funcionalidades mínimas esperadas:
- cadastrar conteúdos técnicos manualmente;
- editar conteúdos cadastrados;
- excluir conteúdos;
- pesquisar conteúdos por texto livre;
- combinar pesquisa com filtros;
- colar manualmente trechos de código, SQL ou texto;
- fazer upload simples de um arquivo por vez;
- salvar arquivo enviado em pasta local uploads/;
- extrair conteúdo textual do arquivo enviado;
- registrar o conteúdo textual no SQLite;
- indexar conteúdo usando SQLite FTS5;
- visualizar conteúdos com preservação da formatação original;
- usar estrutura HTML com <pre><code>conteúdo</code></pre>;
- usar Highlight.js para destaque de sintaxe;
- classificar conteúdos por categoria, linguagem, tags, tipo de arquivo, sistema e domínio;
- marcar conteúdos como regra de negócio;
- permitir classificação de regras de negócio por sistema e domínio.

Upload:
O MVP deve permitir upload de um arquivo por vez.
O limite máximo deve ser de 12 MB por arquivo.
As extensões aceitas são:
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
O PowerBuilder deve ser tratado como uma linguagem única, mas o sistema deve identificar automaticamente o tipo de objeto pela extensão:
- .srw -> PowerBuilder Window
- .sru -> PowerBuilder User Object
- .srd -> PowerBuilder DataWindow
- .srm -> PowerBuilder Menu
- .srf -> PowerBuilder Function
- .sra -> PowerBuilder Application
- .srs -> PowerBuilder Structure

Encoding:
Ao ler arquivos enviados, o sistema deve tentar inicialmente utf-8.
Caso falhe, deve tentar latin-1 e cp1252.
Esse cuidado é importante porque arquivos legados PowerBuilder podem não estar em UTF-8.

Configuração:
O sistema deve usar um arquivo config.yaml para centralizar listas e configurações do MVP, incluindo:
- sistemas;
- domínios;
- linguagens;
- extensões aceitas;
- mapeamento entre extensão e tipo de objeto;
- tags pré-cadastradas.

Estrutura mínima esperada do projeto:
- backend/
- frontend/
- uploads/
- prompts/
- tarefas/
- tests/
- config.yaml
- requirements.txt
- README.md
- .gitignore

A pasta prompts/ deve armazenar os prompts usados durante o desenvolvimento, com finalidade didática, versionamento e refinamento.
A pasta tarefas/ deve armazenar artefatos simulando itens do Azure DevOps, como Feature, User Story e tarefas.

Escopo fora do MVP:
- autenticação;
- múltiplos usuários;
- controle de permissões;
- versionamento interno de snippets;
- backup automático;
- publicação em produção;
- arquitetura distribuída;
- microsserviços;
- APIs externas;
- tela administrativa complexa;
- frontend sofisticado.

Sua tarefa:
Faça uma análise profissional de requisitos para o projeto DevNotes Local.

A resposta deve conter:

1. Visão geral do produto
   - objetivo;
   - problema;
   - público-alvo;
   - premissas;
   - restrições.

2. Requisitos funcionais
   - liste os requisitos com identificadores, por exemplo RF-001, RF-002 etc.;
   - cada requisito deve ter descrição clara;
   - indique prioridade: obrigatória, desejável ou futura;
   - indique observações quando necessário.

3. Requisitos não funcionais
   - liste com identificadores, por exemplo RNF-001, RNF-002 etc.;
   - inclua simplicidade, uso local, desempenho adequado, preservação de formatação, encoding, organização, testabilidade e manutenibilidade.

4. Regras de negócio
   - liste com identificadores, por exemplo RN-001, RN-002 etc.;
   - inclua regras de extensão permitida, limite de upload, classificação por extensão, regra de negócio como marcação especial, uso de config.yaml e busca textual.

5. Critérios de aceitação gerais do MVP
   - descreva critérios objetivos para considerar o MVP pronto.

6. Casos de uso ou fluxos principais
   - cadastrar conteúdo manualmente;
   - fazer upload de arquivo;
   - pesquisar conteúdo;
   - visualizar conteúdo;
   - editar conteúdo;
   - excluir conteúdo.

7. Modelo conceitual inicial dos dados
   - descreva as principais entidades ou conceitos;
   - não precisa criar modelo físico detalhado ainda;
   - considere conteúdo técnico, arquivo enviado, tags, sistema, domínio, linguagem, tipo de objeto e índice textual.

8. Pontos de atenção e riscos
   - encoding;
   - busca com SQLite FTS5;
   - preservação de formatação;
   - escopo excessivo;
   - tratamento simples de arquivos legados.

9. Perguntas em aberto
   - liste perguntas úteis para refinamento futuro.

10. Artefatos simulando Azure DevOps

Crie, em Markdown, uma proposta de artefatos que futuramente seriam salvos dentro da pasta tarefas/.

Importante:
Não crie arquivos reais.
Não implemente código.
Apenas gere o conteúdo em Markdown representando os artefatos.

A estrutura deve conter:

10.1. Feature única do produto
- Nome sugerido do arquivo Markdown;
- Título da Feature;
- Descrição;
- Objetivo de negócio;
- Critérios de aceitação;
- Observações técnicas.

10.2. User Story principal
- Nome sugerido do arquivo Markdown;
- Título da User Story;
- Como [persona], quero [necessidade], para [benefício];
- Descrição;
- Critérios de aceitação;
- Regras envolvidas;
- Observações técnicas.

10.3. Tarefas técnicas necessárias
Para cada tarefa:
- Nome sugerido do arquivo Markdown;
- Título da tarefa;
- Descrição;
- Critérios de aceitação;
- Dependências;
- Observações técnicas.

As tarefas devem cobrir, no mínimo:
- criação da estrutura inicial do projeto;
- configuração do ambiente Python com venv;
- configuração do FastAPI;
- configuração do Jinja2;
- configuração do SQLite e SQLAlchemy;
- criação do config.yaml;
- modelagem inicial das entidades;
- cadastro manual de conteúdo;
- edição de conteúdo;
- exclusão de conteúdo;
- upload simples de arquivo;
- validação de extensão;
- validação de tamanho máximo de 12 MB;
- leitura de arquivos com fallback de encoding;
- classificação automática por extensão;
- gravação dos metadados;
- indexação com SQLite FTS5;
- pesquisa textual com filtros;
- visualização com <pre><code>;
- integração com Highlight.js;
- testes com pytest;
- documentação básica no README.md.

Formato da resposta:
- Gere tudo em Markdown.
- Use tabelas quando ajudarem.
- Seja claro e profissional.
- Não implemente o sistema.
- Não gere código-fonte da aplicação.
- Não avance para arquitetura detalhada.
- O foco é análise de requisitos e organização dos artefatos iniciais.