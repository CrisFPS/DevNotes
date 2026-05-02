# Levantamento Inicial de Requisitos — DevNotes Local

## 1. Objetivo do sistema

O **DevNotes Local** tem como objetivo permitir o armazenamento, organização, consulta e reutilização de conteúdos técnicos em uma aplicação web local, simples e voltada para estudo.

O sistema deverá servir como um repositório pessoal de anotações técnicas, snippets de código, SQLs, scripts, regras de negócio, exemplos de implementação e arquivos relacionados a sistemas legados.

A proposta do MVP é construir uma aplicação pequena, didática e funcional, adequada para praticar as principais etapas do ciclo de desenvolvimento de software utilizando tecnologias como Python, FastAPI, SQLite, SQLAlchemy, Jinja2 e pytest.

---

## 2. Problema que o sistema resolve

Durante o trabalho técnico, é comum acumular informações úteis em locais dispersos, como arquivos `.txt`, documentos, mensagens, prints, scripts soltos, consultas SQL, anotações no Notion, trechos de código e regras de negócio registradas informalmente.

Isso dificulta:

* encontrar rapidamente uma anotação antiga;
* reutilizar comandos SQL, scripts ou snippets;
* organizar conhecimento por sistema, linguagem ou domínio;
* preservar regras de negócio importantes;
* manter exemplos técnicos em um local pesquisável;
* consultar conteúdos técnicos mesmo sem depender de ferramentas externas.

O **DevNotes Local** resolve esse problema oferecendo uma aplicação simples, local e pesquisável para centralizar esse conhecimento técnico pessoal.

---

## 3. Requisitos funcionais

### RF01 — Cadastrar anotação técnica

O sistema deve permitir o cadastro de uma anotação técnica.

Cada anotação deve possuir, inicialmente:

* título;
* conteúdo;
* linguagem ou tipo de conteúdo;
* sistema relacionado;
* domínio;
* categoria;
* tags;
* indicação se é regra de negócio;
* data de criação;
* data da última alteração.

Exemplos de anotações:

* consulta SQL;
* trecho de código Python;
* regra de negócio de um sistema legado;
* explicação técnica;
* script de apoio;
* observação sobre uma procedure;
* comando útil;
* exemplo de erro e solução.

---

### RF02 — Editar anotação técnica

O sistema deve permitir a alteração de uma anotação já cadastrada.

O usuário deve conseguir modificar:

* título;
* conteúdo;
* linguagem;
* sistema;
* domínio;
* categoria;
* tags;
* marcação de regra de negócio.

Ao salvar a edição, o sistema deve atualizar a data da última alteração.

---

### RF03 — Excluir anotação técnica

O sistema deve permitir a exclusão de uma anotação cadastrada.

Como o MVP é local e simples, a exclusão pode ser definitiva.

Uma melhoria futura seria implementar exclusão lógica ou lixeira, mas isso não faz parte do MVP inicial.

---

### RF04 — Pesquisar anotações

O sistema deve permitir pesquisar anotações técnicas.

A pesquisa deve considerar, inicialmente:

* título;
* conteúdo;
* tags;
* linguagem;
* sistema;
* domínio;
* categoria.

A pesquisa deve permitir localizar rapidamente conteúdos cadastrados, mesmo quando o usuário não souber exatamente o título da anotação.

---

### RF05 — Utilizar pesquisa textual com SQLite FTS5

O sistema deve utilizar o recurso **SQLite FTS5** para melhorar a busca textual nas anotações.

A busca deve ser capaz de localizar palavras presentes no título e no conteúdo das anotações.

---

### RF06 — Fazer upload de arquivo

O sistema deve permitir o upload de arquivos relacionados a uma anotação técnica.

Exemplos de arquivos:

* `.sql`;
* `.txt`;
* `.md`;
* `.json`;
* `.xml`;
* `.csv`;
* arquivos exportados de sistemas legados;
* pequenos scripts;
* arquivos de apoio para análise.

No MVP, o upload deve ser simples e local.

---

### RF07 — Associar arquivo a uma anotação

O sistema deve permitir que um arquivo enviado seja associado a uma anotação técnica.

Uma anotação poderá ter nenhum ou mais arquivos vinculados, dependendo da simplicidade definida para o MVP.

Para manter o MVP mais enxuto, a primeira versão pode permitir apenas um arquivo por anotação.

---

### RF08 — Classificar anotação por linguagem

O sistema deve permitir informar a linguagem ou tipo técnico do conteúdo.

Exemplos:

* SQL;
* Python;
* PowerBuilder;
* C#;
* JavaScript;
* Markdown;
* Texto;
* JSON;
* XML;
* Outro.

---

### RF09 — Classificar anotação por sistema

O sistema deve permitir associar a anotação a um sistema específico.

Exemplos:

* Sistema legado;
* Sistema financeiro;
* Sistema contábil;
* Sistema de reservas;
* DevNotes;
* Outro.

Como o projeto é local e simples, essa classificação pode ser digitada livremente no início.

---

### RF10 — Classificar anotação por domínio

O sistema deve permitir classificar uma anotação por domínio de negócio ou domínio técnico.

Exemplos:

* contabilidade;
* financeiro;
* reservas;
* cobrança;
* integração;
* banco de dados;
* arquitetura;
* testes;
* regras de negócio.

---

### RF11 — Classificar anotação por categoria

O sistema deve permitir informar uma categoria para a anotação.

Exemplos:

* snippet;
* SQL;
* script;
* regra de negócio;
* erro conhecido;
* solução;
* documentação;
* estudo;
* procedimento;
* observação técnica.

---

### RF12 — Adicionar tags

O sistema deve permitir adicionar tags a uma anotação.

As tags devem facilitar a organização e a busca posterior.

Exemplos:

* `sql-server`;
* `procedure`;
* `powerbuilder`;
* `fastapi`;
* `contabilidade`;
* `legado`;
* `erro`;
* `performance`;
* `regra-negocio`.

---

### RF13 — Marcar anotação como regra de negócio

O sistema deve permitir marcar uma anotação como **regra de negócio**.

Essa marcação deve facilitar a identificação de conteúdos que representam comportamento esperado do sistema, decisões funcionais ou regras relevantes para análise futura.

---

### RF14 — Visualizar anotação preservando a formatação

O sistema deve permitir visualizar o conteúdo da anotação preservando quebras de linha, indentação e formatação básica.

Isso é importante principalmente para:

* código-fonte;
* SQLs;
* scripts;
* exemplos técnicos;
* regras estruturadas;
* blocos de texto com formatação.

---

### RF15 — Destacar código com Highlight.js

O sistema deve utilizar **Highlight.js** para destacar visualmente trechos de código na tela de visualização da anotação.

O destaque deve considerar a linguagem informada na anotação, quando possível.

---

### RF16 — Listar anotações cadastradas

O sistema deve exibir uma lista de anotações cadastradas.

A listagem deve apresentar informações resumidas, como:

* título;
* linguagem;
* sistema;
* categoria;
* indicação se é regra de negócio;
* data da última alteração.

---

### RF17 — Filtrar anotações

O sistema pode permitir filtros simples na listagem.

Filtros iniciais possíveis:

* linguagem;
* sistema;
* domínio;
* categoria;
* regra de negócio;
* tags.

Para manter o MVP pequeno, os filtros podem ser implementados de forma simples e progressiva.

---

### RF18 — Visualizar detalhes de uma anotação

O sistema deve permitir abrir uma anotação específica e visualizar seus detalhes completos.

A tela de detalhe deve exibir:

* título;
* conteúdo;
* linguagem;
* sistema;
* domínio;
* categoria;
* tags;
* indicação de regra de negócio;
* arquivo vinculado, se houver;
* data de criação;
* data da última alteração.

---

## 4. Requisitos não funcionais

### RNF01 — Execução local

O sistema deve ser executado localmente na máquina do usuário.

Não haverá publicação em servidor, nuvem ou ambiente produtivo no MVP.

---

### RNF02 — Simplicidade

O sistema deve ser simples, didático e adequado para estudo.

A prioridade não é criar uma solução empresarial completa, mas sim um MVP funcional para praticar levantamento de requisitos, desenvolvimento, testes e organização de um pequeno projeto web.

---

### RNF03 — Uso de Python 3.11

O sistema deve ser desenvolvido utilizando **Python 3.11**.

---

### RNF04 — Uso de FastAPI

O backend da aplicação deve utilizar **FastAPI**.

Mesmo sendo uma aplicação web simples, o uso do FastAPI permitirá praticar rotas, organização de endpoints e integração com templates.

---

### RNF05 — Uso de SQLite

O sistema deve utilizar **SQLite** como banco de dados local.

A escolha do SQLite é adequada ao objetivo do MVP, pois evita dependência de instalação de servidores de banco de dados.

---

### RNF06 — Uso de SQLAlchemy

O acesso ao banco de dados deve ser feito utilizando **SQLAlchemy**.

Isso permite praticar mapeamento de entidades, sessões, persistência e consultas de forma organizada.

---

### RNF07 — Uso de SQLite FTS5

O sistema deve utilizar **SQLite FTS5** para pesquisa textual.

Esse requisito é importante porque a busca é uma das funcionalidades centrais da aplicação.

---

### RNF08 — Uso de Jinja2

O sistema deve utilizar **Jinja2** para renderização das páginas HTML.

---

### RNF09 — Interface simples

A interface deve ser construída com **HTML e CSS simples**.

Não devem ser utilizados frameworks frontend sofisticados no MVP.

---

### RNF10 — Uso de pytest

O projeto deve utilizar **pytest** para criação de testes automatizados.

Os testes podem começar cobrindo funcionalidades essenciais, como cadastro, edição, exclusão e pesquisa.

---

### RNF11 — Baixa complexidade de instalação

O sistema deve ser simples de instalar e executar em ambiente local.

O ideal é que a aplicação possa ser iniciada com poucos comandos.

---

### RNF12 — Persistência local dos dados

As anotações e arquivos enviados devem permanecer armazenados localmente.

---

### RNF13 — Preservação da legibilidade do conteúdo técnico

O sistema deve preservar a legibilidade de conteúdos técnicos, especialmente código-fonte, SQLs e scripts.

Indentação, quebras de linha e caracteres especiais não devem ser perdidos na visualização.

---

### RNF14 — Organização mínima do código

Mesmo sendo um MVP simples, o projeto deve ter uma organização mínima que facilite manutenção e estudo.

A estrutura não precisa ser complexa, mas deve evitar concentrar toda a lógica em um único arquivo.

---

### RNF15 — Desempenho adequado para uso local

O sistema deve ter desempenho adequado para um volume pequeno ou moderado de anotações pessoais.

Não é necessário otimizar para grande escala.

---

## 5. Regras de negócio iniciais

### RN01 — Toda anotação deve possuir título

Uma anotação técnica não deve ser cadastrada sem título.

O título é necessário para facilitar identificação, listagem e pesquisa.

---

### RN02 — Toda anotação deve possuir conteúdo

Uma anotação técnica não deve ser cadastrada sem conteúdo principal.

O conteúdo representa a informação técnica que o usuário deseja armazenar.

---

### RN03 — A marcação de regra de negócio deve ser opcional

Nem toda anotação será uma regra de negócio.

O sistema deve permitir que o usuário marque apenas os conteúdos que representam regras relevantes do sistema ou do domínio analisado.

---

### RN04 — Tags devem auxiliar a pesquisa e classificação

As tags devem ser usadas como elementos de classificação e busca.

Uma anotação pode ter várias tags.

---

### RN05 — Uma anotação pode existir sem arquivo anexado

O upload de arquivo deve ser opcional.

O usuário deve conseguir cadastrar uma anotação apenas com título, conteúdo e classificações.

---

### RN06 — Arquivos enviados devem ficar armazenados localmente

Todo arquivo enviado deve ser salvo em uma pasta local da aplicação.

---

### RN07 — A exclusão de anotação remove o vínculo com o arquivo

Ao excluir uma anotação, o sistema deve remover o vínculo com o arquivo associado.

Para o MVP, pode ser decidido se o arquivo físico também será apagado ou se apenas deixará de aparecer no sistema.

---

### RN08 — A data de criação não deve ser alterada

Depois que uma anotação for cadastrada, a data de criação deve permanecer fixa.

---

### RN09 — A data de atualização deve mudar a cada edição

Sempre que uma anotação for alterada, a data de última atualização deve ser modificada.

---

### RN10 — A busca deve priorizar título e conteúdo

A pesquisa textual deve considerar principalmente o título e o conteúdo da anotação.

Tags e classificações podem complementar a pesquisa.

---

### RN11 — O sistema não terá controle de acesso

Como o uso será local e individual, o MVP não terá login, senha, perfis ou permissões.

---

## 6. Restrições do MVP

O MVP do **DevNotes Local** não deve incluir:

* autenticação;
* login;
* controle de usuários;
* múltiplos perfis;
* permissões;
* publicação em produção;
* deploy em nuvem;
* microsserviços;
* frontend sofisticado;
* SPA com React, Angular ou Vue;
* backup automático;
* sincronização com serviços externos;
* integração com Git;
* integração com Azure DevOps;
* integração com IA;
* versionamento avançado das anotações;
* controle de histórico de alterações;
* editor Markdown avançado;
* permissões por categoria;
* criptografia dos dados;
* API pública;
* importação automática de grandes volumes de arquivos;
* processamento avançado de anexos.

Essas funcionalidades podem ser avaliadas futuramente, mas não fazem parte do primeiro MVP.

---

## 7. Dúvidas ou pontos que precisam ser esclarecidos

### D01 — O conteúdo será digitado diretamente ou importado de arquivos?

É necessário definir se o foco principal será cadastrar o conteúdo manualmente pela tela ou importar o conteúdo de arquivos enviados.

Minha sugestão para o MVP: permitir digitação manual e upload simples de arquivo, sem processar automaticamente o conteúdo do arquivo.

---

### D02 — Uma anotação poderá ter mais de um arquivo?

É preciso decidir se uma anotação poderá ter vários arquivos anexados ou apenas um.

Minha sugestão para o MVP: começar com apenas um arquivo por anotação para reduzir complexidade.

---

### D03 — As tags serão digitadas livremente?

É preciso definir se as tags serão livres ou cadastradas previamente.

Minha sugestão para o MVP: tags digitadas livremente, separadas por vírgula.

---

### D04 — Linguagem, sistema, domínio e categoria serão listas fixas ou campos livres?

É necessário decidir se esses campos terão valores pré-cadastrados ou se o usuário poderá digitar livremente.

Minha sugestão para o MVP: começar como campos livres ou listas simples, sem cadastro separado.

---

### D05 — O sistema deve permitir visualização em Markdown?

O requisito atual menciona preservação de formatação e Highlight.js, mas não define se o conteúdo será interpretado como Markdown.

Minha sugestão para o MVP: não implementar renderização Markdown inicialmente; apenas preservar quebras de linha e destacar código.

---

### D06 — Arquivos enviados deverão ser pesquisáveis?

É preciso decidir se o conteúdo dos arquivos enviados também será indexado na pesquisa.

Minha sugestão para o MVP: não pesquisar dentro dos arquivos anexados na primeira versão. Pesquisar apenas título, conteúdo e metadados da anotação.

---

### D07 — A exclusão deve apagar o arquivo físico?

É necessário decidir se, ao excluir uma anotação, o arquivo anexado também será removido da pasta local.

Minha sugestão para o MVP: apagar o arquivo físico junto com a anotação, desde que ele esteja vinculado apenas àquela anotação.

---

### D08 — A pesquisa precisa ter filtros avançados?

É preciso definir se a pesquisa será apenas textual ou se também terá filtros combinados.

Minha sugestão para o MVP: começar com busca textual e filtros simples, sem criar uma tela de busca avançada.

---

### D09 — Será necessário exportar anotações?

O MVP não menciona exportação, mas pode ser útil no futuro.

Minha sugestão: deixar exportação fora do MVP.

---

### D10 — O sistema precisa aceitar imagens ou prints?

Como o objetivo envolve conteúdos técnicos e sistemas legados, pode ser útil anexar prints.

Minha sugestão: para o MVP, permitir upload de arquivos comuns, mas sem tratamento especial para imagens.

---

## 8. Sugestão de próximos passos

### Passo 1 — Validar o escopo do MVP

Revisar os requisitos acima e decidir o que realmente entra na primeira versão.

Uma sugestão de escopo mínimo seria:

* cadastrar anotação;
* editar anotação;
* excluir anotação;
* listar anotações;
* pesquisar por título e conteúdo;
* classificar por linguagem, sistema, domínio, categoria e tags;
* marcar como regra de negócio;
* visualizar conteúdo com formatação preservada;
* destacar código com Highlight.js;
* fazer upload simples de um arquivo.

---

### Passo 2 — Definir o modelo conceitual simples

Depois de validar os requisitos, o próximo passo será definir quais informações compõem uma anotação.

Exemplo inicial:

* Anotação;
* Arquivo anexado;
* Tags.

Ainda não é necessário criar uma arquitetura detalhada, mas é importante identificar as entidades principais.

---

### Passo 3 — Criar uma visão inicial das telas

Antes de implementar, pode ser útil definir telas simples:

* tela inicial/listagem;
* tela de cadastro;
* tela de edição;
* tela de detalhe;
* tela de pesquisa.

Essa etapa ajuda a transformar requisitos em fluxo de uso.

---

### Passo 4 — Priorizar os requisitos

Nem todos os requisitos precisam ser implementados ao mesmo tempo.

Uma priorização inicial poderia ser:

| Prioridade | Requisito                                                     |
| ---------- | ------------------------------------------------------------- |
| Alta       | Cadastrar anotação                                            |
| Alta       | Editar anotação                                               |
| Alta       | Excluir anotação                                              |
| Alta       | Listar anotações                                              |
| Alta       | Pesquisar anotações                                           |
| Alta       | Visualizar conteúdo preservando formatação                    |
| Média      | Classificar por linguagem, sistema, domínio, categoria e tags |
| Média      | Marcar como regra de negócio                                  |
| Média      | Highlight.js                                                  |
| Baixa      | Upload de arquivo                                             |
| Baixa      | Filtros combinados                                            |

---

### Passo 5 — Definir critérios de aceitação

Após validar os requisitos iniciais, o próximo refinamento deve transformar os principais requisitos em critérios de aceitação.

Exemplo:

> Dado que estou na tela de cadastro, quando informo título e conteúdo válidos e salvo, então o sistema deve registrar a anotação e exibi-la na listagem.

---

### Passo 6 — Seguir para arquitetura/design somente depois da validação

A arquitetura deve ser definida em uma próxima etapa, depois que o escopo funcional estiver mais claro.

Nesse momento, ainda não é necessário detalhar:

* estrutura de pastas;
* rotas;
* models;
* migrations;
* serviços;
* templates;
* testes;
* scripts de execução.

Esses itens devem ficar para a próxima fase do SDLC.
