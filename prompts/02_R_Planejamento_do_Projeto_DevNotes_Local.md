# Planejamento do Projeto — DevNotes Local

## 1. Visão geral do projeto

### Problema a ser resolvido

Durante atividades de desenvolvimento, manutenção de sistemas legados, estudos técnicos e análise de regras de negócio, é comum acumular diversos conteúdos úteis em locais dispersos: arquivos `.sql`, anotações em texto, trechos de código, scripts pequenos, regras de negócio, exemplos de procedures, comandos, prints transcritos, documentos exportados e observações técnicas.

O problema central é que esses conteúdos ficam difíceis de localizar, reutilizar e relacionar com contexto técnico, como sistema, domínio, linguagem, categoria ou regra de negócio.

O **DevNotes Local** busca resolver esse problema criando uma aplicação simples, local e organizada para armazenar, classificar, pesquisar e consultar conteúdos técnicos reutilizáveis.

---

### Objetivo do MVP

O objetivo do MVP é criar uma aplicação web local, pequena e funcional, capaz de:

* cadastrar conteúdos técnicos manualmente;
* editar e excluir conteúdos;
* pesquisar textos, códigos e anotações;
* fazer upload simples de arquivos;
* classificar conteúdos por metadados;
* visualizar textos e códigos preservando a formatação;
* destacar sintaxe de código com Highlight.js;
* praticar as fases principais do SDLC com apoio de IA generativa.

O foco não é construir uma aplicação comercial, mas sim um projeto didático, viável e tecnicamente coerente.

---

### Público-alvo

O público-alvo principal é o próprio desenvolvedor/estudante que deseja:

* organizar conhecimento técnico local;
* estudar Engenharia de Software aplicada;
* praticar desenvolvimento com FastAPI, SQLite e SQLAlchemy;
* experimentar o uso de IA generativa no ciclo de vida de software;
* criar um projeto pequeno, mas com estrutura próxima de um projeto real.

---

### Premissas

| Premissa          | Descrição                                                                   |
| ----------------- | --------------------------------------------------------------------------- |
| Uso local         | A aplicação será executada apenas na máquina do usuário.                    |
| Usuário único     | Não haverá controle de usuários, login ou permissões.                       |
| MVP pequeno       | O projeto deve caber em um ciclo curto de desenvolvimento assistido por IA. |
| Banco local       | O armazenamento será feito com SQLite.                                      |
| Interface simples | HTML, CSS e Jinja2 serão suficientes para a interface inicial.              |
| Busca textual     | A busca será feita com SQLite FTS5.                                         |
| Aprendizado       | O projeto deve permitir praticar SDLC, testes, organização e documentação.  |

---

### Restrições

| Restrição                | Impacto                                                       |
| ------------------------ | ------------------------------------------------------------- |
| Python 3.11 obrigatório  | O ambiente deve ser criado especificamente com essa versão.   |
| FastAPI obrigatório      | A aplicação deve seguir o modelo web/API com FastAPI.         |
| SQLite obrigatório       | Não usar PostgreSQL, SQL Server ou banco externo no MVP.      |
| Sem autenticação         | Simplifica o projeto e reduz riscos de escopo.                |
| Sem nuvem                | Não há deploy, infraestrutura ou configuração cloud.          |
| Sem frontend sofisticado | Evita complexidade com frameworks como React, Vue ou Angular. |
| Prazo curto              | O escopo precisa ser controlado com rigor.                    |

---

## 2. Escopo do MVP

### Funcionalidades incluídas

| Funcionalidade               | Descrição                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------- |
| Cadastro de conteúdo         | Permitir criar uma nova anotação técnica, snippet, SQL, regra ou texto.         |
| Edição de conteúdo           | Permitir alterar título, conteúdo, metadados e classificação.                   |
| Exclusão de conteúdo         | Permitir remover registros cadastrados.                                         |
| Pesquisa textual             | Buscar conteúdos por título, corpo do texto e metadados relevantes.             |
| Upload simples               | Permitir upload de um arquivo por vez para armazenamento local.                 |
| Visualização de conteúdo     | Exibir conteúdo preservando quebras de linha, espaços e estrutura.              |
| Destaque de sintaxe          | Usar Highlight.js para destacar código conforme linguagem informada.            |
| Classificação                | Categorizar por categoria, linguagem, tags, tipo de arquivo, sistema e domínio. |
| Marcação de regra de negócio | Permitir indicar se determinado conteúdo representa regra de negócio.           |
| Interface web local          | Telas simples usando Jinja2, HTML e CSS.                                        |
| Testes básicos               | Criar testes com pytest para principais regras e rotas.                         |

---

### Funcionalidades fora do escopo

| Fora do escopo                 | Motivo                                                   |
| ------------------------------ | -------------------------------------------------------- |
| Autenticação                   | Desnecessária para uso local e aumenta complexidade.     |
| Múltiplos usuários             | O projeto será individual.                               |
| Permissões                     | Não há perfis de acesso no MVP.                          |
| Backup automático              | Pode ser evolução futura.                                |
| APIs externas                  | Desvia o foco do aprendizado principal.                  |
| Frontend sofisticado           | O objetivo é praticar backend, organização e fluxo SDLC. |
| Microsserviços                 | Seria excesso arquitetural para um app local.            |
| Publicação em produção         | Não faz parte da proposta didática.                      |
| Versionamento interno avançado | Pode ser evolução futura, mas não cabe no MVP.           |

---

### Justificativa para manter o escopo pequeno

O maior risco desse projeto não é técnico; é **transformar um aplicativo didático em uma plataforma completa de gestão de conhecimento técnico**.

A ideia é boa o suficiente para crescer muito, mas o MVP precisa permanecer pequeno. Caso contrário, o projeto pode passar rapidamente a exigir autenticação, controle de versões, anexos múltiplos, importação em lote, OCR, integração com Git, busca semântica, RAG, IA embutida e outras funcionalidades interessantes, mas incompatíveis com o prazo de 3 a 12 horas.

Para fins de estudo, um MVP pequeno é melhor porque permite concluir um ciclo completo: planejar, levantar requisitos, desenhar, implementar, testar e evoluir.

---

## 3. Fases do SDLC aplicadas ao projeto

## 3.1 Planejamento

Nesta fase, o objetivo é delimitar o problema, definir o MVP e evitar crescimento descontrolado do escopo.

### Atividades principais

* definir visão do produto;
* delimitar funcionalidades do MVP;
* registrar o que está fora do escopo;
* definir tecnologias obrigatórias;
* definir critérios de sucesso;
* organizar backlog inicial;
* estimar uma estratégia incremental de entrega.

### Saídas esperadas

* documento de visão geral;
* escopo do MVP;
* backlog inicial;
* premissas e restrições;
* riscos iniciais;
* critérios de sucesso.

---

## 3.2 Levantamento e análise de requisitos

Nesta fase, o objetivo é transformar a ideia em requisitos compreensíveis.

### Requisitos funcionais iniciais

| Código | Requisito                                                                |
| ------ | ------------------------------------------------------------------------ |
| RF01   | O sistema deve permitir cadastrar conteúdos técnicos.                    |
| RF02   | O sistema deve permitir editar conteúdos existentes.                     |
| RF03   | O sistema deve permitir excluir conteúdos.                               |
| RF04   | O sistema deve permitir pesquisar conteúdos cadastrados.                 |
| RF05   | O sistema deve permitir upload de um arquivo por vez.                    |
| RF06   | O sistema deve permitir visualizar conteúdos preservando formatação.     |
| RF07   | O sistema deve permitir destacar código com base na linguagem informada. |
| RF08   | O sistema deve permitir classificar conteúdos por metadados.             |
| RF09   | O sistema deve permitir marcar conteúdos como regra de negócio.          |

### Requisitos não funcionais iniciais

| Código | Requisito                                                         |
| ------ | ----------------------------------------------------------------- |
| RNF01  | A aplicação deve executar localmente.                             |
| RNF02  | A aplicação deve usar Python 3.11.                                |
| RNF03  | A aplicação deve usar FastAPI.                                    |
| RNF04  | A aplicação deve usar SQLite como banco local.                    |
| RNF05  | A busca textual deve usar SQLite FTS5.                            |
| RNF06  | A interface deve ser simples e funcional.                         |
| RNF07  | O projeto deve ter testes básicos com pytest.                     |
| RNF08  | O projeto deve ser versionado com Git.                            |
| RNF09  | O projeto deve ser organizado de forma compreensível para estudo. |

---

## 3.3 Arquitetura/design

A arquitetura deve ser simples, modular e coerente com um MVP local.

### Estilo arquitetural sugerido

Uma arquitetura em camadas simples é suficiente:

| Camada           | Responsabilidade                                         |
| ---------------- | -------------------------------------------------------- |
| Interface web    | Templates Jinja2, HTML, CSS e interações simples.        |
| Rotas FastAPI    | Receber requisições, validar entradas e chamar serviços. |
| Serviços         | Concentrar regras de aplicação e operações principais.   |
| Repositórios/DAO | Isolar acesso ao SQLite via SQLAlchemy.                  |
| Banco de dados   | Armazenar conteúdos, metadados e índice FTS5.            |
| Uploads          | Armazenar arquivos enviados localmente.                  |

### Opinião crítica

Não há justificativa para microsserviços, autenticação, filas, Docker obrigatório ou arquitetura distribuída neste MVP. Essas decisões tornariam o projeto mais “sofisticado”, mas menos didático e menos viável.

Para esse caso, a boa arquitetura é a que permite entender, testar e evoluir sem exagero.

---

## 3.4 Implementação

A implementação deve seguir entregas pequenas, validáveis e com commits frequentes.

### Diretrizes

* começar com o cadastro manual de conteúdos;
* só depois incluir upload;
* implementar a busca após ter dados persistidos;
* manter HTML simples;
* evitar JavaScript desnecessário;
* criar testes desde o início para partes essenciais;
* registrar prompts importantes usados com IA.

### Cuidados

* não tentar automatizar importações complexas no MVP;
* não misturar busca textual com busca semântica;
* não iniciar com uma interface sofisticada;
* evitar abstrações excessivas.

---

## 3.5 Testes

Os testes devem ser proporcionais ao tamanho do projeto.

### Tipos de teste recomendados

| Tipo                   | Aplicação no projeto                          |
| ---------------------- | --------------------------------------------- |
| Testes unitários       | Serviços, validações e regras simples.        |
| Testes de integração   | Rotas FastAPI com banco de teste.             |
| Testes de persistência | Cadastro, edição, exclusão e busca.           |
| Testes de upload       | Validação básica de arquivo enviado.          |
| Testes manuais         | Conferência visual da interface e formatação. |

### Pontos críticos para testar

* criação de conteúdo;
* edição de conteúdo;
* exclusão de conteúdo;
* busca por título;
* busca por conteúdo;
* busca por tags;
* upload de arquivo;
* visualização com quebras de linha preservadas;
* destaque de sintaxe funcionando no navegador.

---

## 3.6 Manutenção/evolução

Após o MVP, o projeto pode evoluir de forma controlada.

### Evoluções possíveis

| Evolução                       | Observação                                     |
| ------------------------------ | ---------------------------------------------- |
| Importação em lote             | Útil, mas deve ficar fora do MVP.              |
| Exportação dos conteúdos       | Pode ser útil para backup manual.              |
| Busca por filtros avançados    | Evolução natural após o FTS básico.            |
| Histórico de alterações        | Interessante, mas aumenta complexidade.        |
| Busca semântica com embeddings | Boa evolução futura, mas não necessária agora. |
| Integração com IA local ou API | Pode ser estudada em etapa posterior.          |
| Organização por projetos       | Útil se o volume de conteúdos crescer.         |

---

## 4. Estratégia de execução incremental

## Ordem sugerida de implementação

| Etapa | Entrega                      | Validação                                                                   |
| ----- | ---------------------------- | --------------------------------------------------------------------------- |
| 1     | Estrutura inicial do projeto | Aplicação sobe localmente com FastAPI.                                      |
| 2     | Modelo de dados básico       | Banco SQLite cria tabela de conteúdos.                                      |
| 3     | Cadastro manual              | É possível criar um conteúdo pela interface.                                |
| 4     | Listagem e visualização      | Conteúdos aparecem em lista e podem ser visualizados.                       |
| 5     | Edição e exclusão            | Conteúdos podem ser alterados e removidos.                                  |
| 6     | Classificação por metadados  | Categoria, linguagem, tags, sistema, domínio e regra de negócio são salvos. |
| 7     | Highlight.js                 | Código é exibido com destaque de sintaxe.                                   |
| 8     | Upload simples               | Um arquivo pode ser enviado e associado a um conteúdo.                      |
| 9     | Busca com FTS5               | Pesquisa textual retorna conteúdos relevantes.                              |
| 10    | Testes básicos               | pytest cobre fluxos principais.                                             |
| 11    | Revisão final do MVP         | Conferência contra critérios de sucesso.                                    |

---

## Entregas pequenas

### Entrega 1 — Aplicação mínima executável

Resultado esperado:

* ambiente virtual criado;
* dependências instaladas;
* FastAPI executando;
* página inicial simples renderizada com Jinja2.

---

### Entrega 2 — CRUD básico de conteúdos

Resultado esperado:

* cadastrar conteúdo;
* listar conteúdos;
* visualizar conteúdo;
* editar conteúdo;
* excluir conteúdo.

---

### Entrega 3 — Classificação e visualização técnica

Resultado esperado:

* metadados cadastrados;
* conteúdo exibido preservando formatação;
* destaque de sintaxe com Highlight.js.

---

### Entrega 4 — Upload e busca

Resultado esperado:

* upload simples funcionando;
* conteúdo do arquivo armazenado ou referenciado;
* busca textual com SQLite FTS5 funcionando.

---

### Entrega 5 — Testes e documentação mínima

Resultado esperado:

* testes principais criados;
* README básico;
* registro dos prompts usados;
* decisões técnicas principais documentadas.

---

## Marcos de validação

| Marco                 | Pergunta de validação                                   |
| --------------------- | ------------------------------------------------------- |
| MVP navegável         | Consigo acessar a aplicação pelo navegador local?       |
| Cadastro útil         | Consigo salvar uma anotação real que eu reutilizaria?   |
| Visualização adequada | O conteúdo aparece com formatação preservada?           |
| Busca funcional       | Consigo encontrar rapidamente uma anotação cadastrada?  |
| Upload simples        | Consigo enviar um arquivo técnico e consultá-lo depois? |
| Classificação útil    | Os metadados ajudam a organizar o conteúdo?             |
| Testes mínimos        | Os fluxos principais estão protegidos contra regressão? |

---

## 5. Organização inicial do projeto

## Estrutura sugerida de pastas

```text
devnotes-local/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── routes/
│   │   └── schemas/
│   │
│   └── devnotes.db
│
├── frontend/
│   ├── templates/
│   └── static/
│       ├── css/
│       ├── js/
│       └── vendor/
│
├── uploads/
│
├── prompts/
│
├── tarefas/
│
├── tests/
│
├── README.md
├── requirements.txt
├── .gitignore
└── pytest.ini
```

---

## Explicação das pastas principais

| Pasta       | Finalidade                                                                                            |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| `backend/`  | Concentrar a aplicação FastAPI, regras de aplicação, acesso ao banco e modelos.                       |
| `frontend/` | Guardar templates Jinja2, arquivos CSS, JavaScript simples e bibliotecas estáticas como Highlight.js. |
| `uploads/`  | Armazenar arquivos enviados pelo usuário de forma local.                                              |
| `prompts/`  | Registrar prompts usados no projeto, respostas relevantes da IA e refinamentos importantes.           |
| `tarefas/`  | Guardar planejamento, backlog, critérios de aceite, anotações de execução e decisões de projeto.      |
| `tests/`    | Concentrar testes automatizados com pytest.                                                           |

---

## Observação sobre `backend/` e `frontend/`

Mesmo usando FastAPI com Jinja2 em uma aplicação simples, separar `backend/` e `frontend/` ajuda didaticamente.

Essa separação não significa criar dois projetos independentes. Apenas organiza melhor:

* lógica da aplicação;
* templates;
* arquivos estáticos;
* testes;
* documentação;
* uploads.

Para um MVP local, essa separação é suficiente. Criar um frontend separado com React, build, Node.js e API isolada seria desnecessário.

---

## 6. Riscos iniciais

## 6.1 Riscos técnicos

| Risco                          | Impacto                                 | Mitigação                                       |
| ------------------------------ | --------------------------------------- | ----------------------------------------------- |
| Excesso de abstração           | Projeto fica maior que o necessário.    | Usar arquitetura simples em camadas.            |
| Configuração incorreta do FTS5 | Busca pode não funcionar como esperado. | Validar cedo com poucos dados.                  |
| Mistura de responsabilidades   | Código difícil de manter.               | Separar rotas, serviços e acesso a dados.       |
| Testes deixados para o fim     | Dificuldade para corrigir regressões.   | Criar testes básicos desde os primeiros fluxos. |

---

## 6.2 Riscos de escopo

| Risco                                          | Impacto                               | Mitigação                                      |
| ---------------------------------------------- | ------------------------------------- | ---------------------------------------------- |
| Querer criar uma base de conhecimento completa | MVP deixa de caber em 3 a 12 horas.   | Manter apenas CRUD, upload simples e busca.    |
| Adicionar IA dentro do aplicativo cedo demais  | Aumenta custo e complexidade.         | Usar IA como apoio externo ao desenvolvimento. |
| Criar filtros avançados demais                 | Atraso na entrega.                    | Começar com pesquisa textual simples.          |
| Melhorar demais a interface                    | Desvia o foco do aprendizado técnico. | HTML e CSS simples bastam.                     |

---

## 6.3 Riscos de encoding em arquivos legados

Esse é um risco importante, especialmente se forem enviados arquivos exportados de sistemas legados, scripts antigos ou textos gerados por ferramentas antigas.

| Risco                                        | Impacto                                        | Mitigação                                                     |
| -------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| Arquivos em ANSI, Windows-1252 ou ISO-8859-1 | Caracteres acentuados podem quebrar.           | Tentar detectar encoding ou permitir fallback controlado.     |
| Arquivos com caracteres inválidos            | Upload pode falhar ou conteúdo ficar ilegível. | Registrar erro amigável e manter arquivo original salvo.      |
| Mistura de encodings                         | Exibição inconsistente.                        | Definir estratégia simples de leitura e conversão para UTF-8. |

### Decisão recomendada para o MVP

Para o MVP, a melhor decisão é simples:

* salvar o arquivo original em `uploads/`;
* tentar ler como UTF-8;
* se falhar, tentar Windows-1252;
* se ainda falhar, permitir cadastro do arquivo, mas informar que o conteúdo não pôde ser convertido para visualização textual.

---

## 6.4 Riscos relacionados à busca textual

| Risco                               | Impacto                               | Mitigação                                                     |
| ----------------------------------- | ------------------------------------- | ------------------------------------------------------------- |
| FTS5 não refletir alterações        | Busca retorna dados desatualizados.   | Atualizar índice ao criar, editar e excluir.                  |
| Busca não encontrar termos parciais | Usuário pode achar que falhou.        | Documentar comportamento inicial da busca.                    |
| Tags e metadados fora do índice     | Pesquisa fica limitada.               | Indexar título, conteúdo, tags, sistema, domínio e categoria. |
| Busca textual não entende semântica | Resultados podem ser literais demais. | Aceitar como limitação do MVP.                                |

### Opinião crítica

Não vale a pena colocar busca semântica com embeddings no MVP. Apesar de interessante, isso mudaria a natureza do projeto. Primeiro é melhor fazer uma busca textual confiável, simples e explicável.

---

## 6.5 Riscos relacionados à preservação de formatação

| Risco                                   | Impacto                                 | Mitigação                                   |
| --------------------------------------- | --------------------------------------- | ------------------------------------------- |
| Perda de quebras de linha               | Código e SQL ficam difíceis de ler.     | Usar exibição em blocos pré-formatados.     |
| Espaços e tabs alterados                | Código pode perder legibilidade.        | Preservar texto original no banco.          |
| HTML interpretado indevidamente         | Risco de exibição incorreta.            | Escapar conteúdo e exibir como texto.       |
| Highlight.js alterar visualmente demais | Pode confundir leitura em alguns casos. | Permitir visualização simples e previsível. |

---

## 7. Critérios de sucesso do MVP

## 7.1 Critérios funcionais

| Critério           | Resultado esperado                                                                  |
| ------------------ | ----------------------------------------------------------------------------------- |
| Cadastro           | O usuário consegue cadastrar uma anotação técnica.                                  |
| Edição             | O usuário consegue alterar conteúdo e metadados.                                    |
| Exclusão           | O usuário consegue excluir conteúdo.                                                |
| Pesquisa           | O usuário consegue encontrar conteúdo por texto.                                    |
| Upload             | O usuário consegue enviar um arquivo por vez.                                       |
| Visualização       | O usuário consegue visualizar conteúdo preservando formatação.                      |
| Destaque de código | O código é exibido com destaque de sintaxe.                                         |
| Classificação      | O conteúdo pode ser classificado por categoria, linguagem, tags, sistema e domínio. |
| Regra de negócio   | O usuário consegue marcar um conteúdo como regra de negócio.                        |

---

## 7.2 Critérios técnicos

| Critério       | Resultado esperado                             |
| -------------- | ---------------------------------------------- |
| Execução local | Aplicação roda localmente com FastAPI.         |
| Banco SQLite   | Dados são persistidos em SQLite.               |
| SQLAlchemy     | Acesso ao banco usa SQLAlchemy.                |
| FTS5           | Busca textual usa SQLite FTS5.                 |
| Templates      | Interface usa Jinja2.                          |
| Testes         | pytest cobre fluxos essenciais.                |
| Git            | Projeto possui commits organizados.            |
| Organização    | Pastas são compreensíveis e coerentes.         |
| Simplicidade   | Não há dependências desnecessárias para o MVP. |

---

## 7.3 Critérios didáticos

| Critério             | Resultado esperado                                                                      |
| -------------------- | --------------------------------------------------------------------------------------- |
| SDLC praticado       | O projeto passa por planejamento, requisitos, design, implementação, testes e evolução. |
| IA usada com método  | Prompts e decisões são registrados.                                                     |
| Escopo controlado    | O MVP permanece pequeno e entregável.                                                   |
| Código compreensível | A estrutura permite explicar o funcionamento do sistema.                                |
| Projeto reutilizável | O resultado pode servir como base para estudos futuros.                                 |

---

## 8. Backlog inicial em alto nível

## Épico 1 — Estruturação do projeto

| Item                        | Descrição                                                             |
| --------------------------- | --------------------------------------------------------------------- |
| Criar estrutura inicial     | Organizar pastas principais do projeto.                               |
| Configurar ambiente virtual | Usar venv com Python 3.11.                                            |
| Configurar dependências     | FastAPI, SQLAlchemy, Jinja2, pytest e demais bibliotecas necessárias. |
| Configurar Git              | Criar repositório local e `.gitignore`.                               |
| Criar README inicial        | Documentar objetivo, execução e tecnologias.                          |

---

## Épico 2 — Cadastro e gestão de conteúdos

| Item                     | Descrição                                      |
| ------------------------ | ---------------------------------------------- |
| Criar modelo de conteúdo | Definir campos principais da anotação técnica. |
| Cadastrar conteúdo       | Criar formulário para novo registro.           |
| Listar conteúdos         | Exibir registros cadastrados.                  |
| Visualizar conteúdo      | Exibir detalhes de um conteúdo.                |
| Editar conteúdo          | Permitir alteração dos dados.                  |
| Excluir conteúdo         | Permitir remoção controlada.                   |

---

## Épico 3 — Classificação técnica

| Item             | Descrição                                                        |
| ---------------- | ---------------------------------------------------------------- |
| Categoria        | Classificar conteúdo por tipo geral.                             |
| Linguagem        | Informar linguagem como SQL, Python, PowerBuilder, Markdown etc. |
| Tags             | Permitir palavras-chave livres.                                  |
| Tipo de arquivo  | Identificar origem ou extensão.                                  |
| Sistema          | Informar sistema relacionado.                                    |
| Domínio          | Informar domínio de negócio ou técnico.                          |
| Regra de negócio | Marcar se o conteúdo representa regra de negócio.                |

---

## Épico 4 — Upload de arquivos

| Item                    | Descrição                                   |
| ----------------------- | ------------------------------------------- |
| Upload simples          | Permitir envio de um arquivo por vez.       |
| Armazenamento local     | Salvar arquivo em `uploads/`.               |
| Associação com conteúdo | Relacionar arquivo ao registro cadastrado.  |
| Leitura textual básica  | Tentar extrair texto quando possível.       |
| Tratamento de encoding  | Lidar minimamente com UTF-8 e Windows-1252. |

---

## Épico 5 — Busca textual

| Item                          | Descrição                                     |
| ----------------------------- | --------------------------------------------- |
| Configurar FTS5               | Criar estrutura de busca textual.             |
| Indexar conteúdo              | Incluir título, corpo e metadados relevantes. |
| Pesquisar conteúdo            | Criar campo de busca na interface.            |
| Exibir resultados             | Mostrar lista de conteúdos encontrados.       |
| Validar atualização do índice | Garantir consistência após edição e exclusão. |

---

## Épico 6 — Visualização e usabilidade básica

| Item                 | Descrição                                                    |
| -------------------- | ------------------------------------------------------------ |
| Preservar formatação | Exibir conteúdo com quebras e espaços preservados.           |
| Highlight.js         | Aplicar destaque de sintaxe.                                 |
| CSS simples          | Melhorar legibilidade sem sofisticação.                      |
| Navegação básica     | Criar links entre listagem, cadastro, edição e visualização. |
| Mensagens simples    | Exibir feedback básico de sucesso ou erro.                   |

---

## Épico 7 — Testes e validação

| Item            | Descrição                        |
| --------------- | -------------------------------- |
| Testar cadastro | Validar criação de conteúdo.     |
| Testar edição   | Validar alteração de dados.      |
| Testar exclusão | Validar remoção.                 |
| Testar busca    | Validar retorno de resultados.   |
| Testar upload   | Validar envio básico de arquivo. |
| Testar serviços | Cobrir regras principais.        |

---

## Épico 8 — Documentação e registro de IA

| Item                    | Descrição                                    |
| ----------------------- | -------------------------------------------- |
| Registrar prompts       | Guardar prompts usados durante o projeto.    |
| Registrar decisões      | Documentar decisões técnicas relevantes.     |
| Criar notas de evolução | Registrar ideias fora do MVP.                |
| Revisar README          | Atualizar instruções de execução e objetivo. |

---

## 9. Recomendações para uso de IA durante o projeto

## 9.1 Uso de IA na fase de requisitos

A IA pode ajudar a transformar a ideia inicial em requisitos mais claros.

### Usos recomendados

* revisar requisitos funcionais;
* identificar requisitos não funcionais;
* sugerir critérios de aceite;
* apontar ambiguidades;
* separar MVP de evolução futura;
* transformar ideias em backlog.

### Cuidados

A IA tende a aumentar o escopo. Por isso, toda sugestão deve ser filtrada pela pergunta:

> Isso é necessário para o MVP local de 3 a 12 horas?

Se a resposta for não, deve ir para uma lista de evolução futura.

---

## 9.2 Uso de IA na arquitetura/design

A IA pode apoiar na criação de uma arquitetura simples e coerente.

### Usos recomendados

* sugerir estrutura de pastas;
* comparar alternativas de organização;
* propor fluxo entre telas, rotas, serviços e banco;
* revisar responsabilidades das camadas;
* sugerir modelo de dados inicial;
* apontar riscos de acoplamento.

### Cuidados

A IA pode sugerir padrões exagerados, como DDD completo, microsserviços, Docker obrigatório, autenticação ou frontend moderno. Para esse projeto, isso seria excesso.

A arquitetura ideal deve ser pequena, legível e suficiente.

---

## 9.3 Uso de IA na implementação

A IA pode ser usada como copiloto, não como substituta da revisão técnica.

### Usos recomendados

* gerar esqueleto inicial de arquivos;
* sugerir rotas FastAPI;
* ajudar com SQLAlchemy;
* explicar erros;
* sugerir testes;
* revisar código;
* melhorar mensagens de erro;
* propor refatorações simples.

### Cuidados

Todo código gerado por IA deve ser revisado. Atenção especial para:

* imports inexistentes;
* uso incorreto do SQLAlchemy;
* exemplos incompatíveis com Python 3.11;
* falhas na configuração do FTS5;
* tratamento inseguro de upload;
* mistura indevida de regras em rotas;
* excesso de complexidade.

---

## 9.4 Uso de IA nos testes

A IA pode ajudar bastante na criação dos testes iniciais.

### Usos recomendados

* sugerir casos de teste;
* criar matriz de testes;
* gerar testes com pytest;
* identificar cenários negativos;
* revisar cobertura mínima;
* sugerir testes de regressão.

### Exemplos de cenários importantes

| Cenário                     | Validação                               |
| --------------------------- | --------------------------------------- |
| Cadastro válido             | Conteúdo é salvo corretamente.          |
| Cadastro sem título         | Sistema trata erro de validação.        |
| Edição                      | Dados são atualizados.                  |
| Exclusão                    | Registro deixa de aparecer.             |
| Busca por termo existente   | Resultado é retornado.                  |
| Busca por termo inexistente | Lista vazia ou mensagem adequada.       |
| Upload de arquivo texto     | Arquivo é salvo e associado.            |
| Encoding incompatível       | Sistema não quebra de forma inesperada. |

---

## 9.5 Registro de prompts e decisões

Uma das partes mais importantes para fins didáticos é registrar como a IA foi usada.

### Pasta recomendada

```text
prompts/
```

### O que registrar

| Item               | Exemplo                         |
| ------------------ | ------------------------------- |
| Prompt usado       | Pedido feito à IA.              |
| Objetivo           | Por que o prompt foi usado.     |
| Resumo da resposta | O que foi aproveitado.          |
| Ajustes humanos    | O que foi alterado manualmente. |
| Decisão final      | O que entrou ou não no projeto. |

---

## Registro de decisões técnicas

Além dos prompts, vale manter decisões técnicas na pasta:

```text
tarefas/
```

Ou em uma subpasta específica:

```text
tarefas/decisoes/
```

### Exemplos de decisões a registrar

| Decisão                  | Justificativa                                     |
| ------------------------ | ------------------------------------------------- |
| Usar SQLite              | Simples, local e suficiente para o MVP.           |
| Usar FTS5                | Permite busca textual sem instalar outro serviço. |
| Não usar autenticação    | Aplicação local e usuário único.                  |
| Não usar React           | Jinja2 atende ao objetivo didático.               |
| Não usar busca semântica | Complexidade desnecessária no MVP.                |
| Salvar arquivo original  | Evita perda de dados em problemas de encoding.    |

---

## Conclusão

O **DevNotes Local** é um excelente projeto didático porque é pequeno, útil e permite praticar várias disciplinas de Engenharia de Software sem cair em uma complexidade artificial.

O ponto mais importante é manter o projeto fiel ao seu propósito: uma aplicação local para organizar conteúdos técnicos e praticar SDLC com apoio de IA.

A melhor estratégia é construir o MVP em incrementos curtos:

1. aplicação local funcionando;
2. CRUD de conteúdos;
3. classificação;
4. visualização com formatação;
5. upload simples;
6. busca textual;
7. testes;
8. documentação e registro dos prompts.

Esse caminho permite concluir um projeto realista, demonstrável e alinhado ao objetivo da especialização.
